"""Analysis-pipeline tests (intent 515, rev 2 after PT-515 BLOCK): QC, blinding
structure, floor provenance, and FOUR mandatory synthetic scenarios (null /
injected-signal / injected-artifact-QC / actuation-correlated-artifact), plus
criterion-freeze guards and golden vectors."""

import math
import pytest

import random

from pipeline import (
    qc_run, run_stats, stage_a, stage_b, artifact_floor_A, validate_run_id,
    seal_session, verify_session,
    QC_BOUNDS, MIN_VALID_PAIRS, MIN_DECOY_RUNS, CHARGE_GATE_C,
    UNDIMINISHED_FRACTION, DECOY_ABS_FLOOR_A,
)
from synth import (
    make_session, make_attestations, draw_schedule,
    make_runs_null, make_runs_signal, make_runs_piezo_heat,
    make_runs_thermal_artifact, make_runs_emf_drift,
    make_labels, strip_labels,
)


@pytest.fixture
def session():
    return make_session()

def _verdict(runs, session):
    return stage_b(stage_a(strip_labels(runs)), make_labels(runs), session,
                   make_attestations())


# --- QC + stage A -------------------------------------------------------------

def test_qc_clean_run_passes(session):
    runs = make_runs_null(session, n_pairs=2, seed=7)
    assert qc_run(runs[0]) == []

def test_qc_flags_thermal_violation(session):
    runs = make_runs_thermal_artifact(session, seed=7)
    flagged = [r for r in runs if qc_run(r)]
    assert len(flagged) == 1 and any("dT" in v for v in qc_run(flagged[0]))

def test_stage_a_needs_no_labels(session):
    runs = make_runs_null(session, n_pairs=2, seed=8)
    stats = stage_a(strip_labels(runs))
    assert all("_true_state" not in s for s in stats)

# --- blinding regression (PT-515 blocker 2) -------------------------------------

def test_run_ids_are_opaque_serials(session):
    """No state character may survive in run ids; stats must carry no
    recoverable state signal in their identifiers."""
    for maker in (make_runs_null, make_runs_signal, make_runs_piezo_heat):
        for r in maker(session):
            assert r["run_id"].removeprefix("run-").isdigit(), r["run_id"]
    ids_a = [r["run_id"] for r in make_runs_null(session)]
    ids_b = [r["run_id"] for r in make_runs_signal(session)]
    assert ids_a == ids_b  # ids carry schedule position only, never state

def test_schedule_is_random_and_decoys_interior():
    """re-PT-515 blocker 2: the draw must be unpredictable (schedules differ
    across seeds), balanced (equal closed-first/open-first pairs for drift
    cancellation), and decoys must be INTERIOR (never first or last run)."""
    schedules = [draw_schedule(4, random.Random(seed)) for seed in range(12)]
    assert len({tuple(s) for s in schedules}) > 1   # not deterministic
    for s in schedules:
        assert s[0] != "decoy" and s[-1] != "decoy"
        assert s.count("decoy") == 2
        pair_states = [x for x in s if x != "decoy"]
        firsts = [pair_states[i] for i in range(0, len(pair_states), 2)]
        assert firsts.count("closed") == firsts.count("open")  # balanced

def test_position_parity_predictor_defeated():
    """The re-PT attack recovered 100% of states from position parity alone.
    Against the random draw, the same predictor must NOT be perfect across seeds."""
    def parity_predict(n_runs):  # the re-PT attack's model of the old schedule
        seq = []
        for k in range(4):
            seq.extend(("closed", "open") if k % 2 == 0 else ("open", "closed"))
            if k in (0, 3):
                seq.append("decoy")
        return seq
    hits = total = 0
    for seed in range(12):
        runs = make_runs_null(make_session(), n_pairs=4, seed=seed)
        truth = [r["_true_state"] for r in runs]
        pred = parity_predict(len(truth))
        hits += sum(p == t for p, t in zip(pred, truth)); total += len(truth)
    assert hits / total < 0.9   # far from the 100% recovery of the fixed schedule

def test_state_encoding_run_id_rejected():
    bad = {"run_id": "run-00-c", "segments": [{"lockin_I_A": 0, "lockin_Q_A": 0}],
           "artifacts": {}}
    with pytest.raises(ValueError, match="opaque serial"):
        run_stats(bad)

def test_validate_run_id_accepts_serials():
    validate_run_id("run-007")  # no raise

# --- floor provenance (PT-515 blocker 1) -----------------------------------------

def test_floor_inputs_come_from_measured_run_channels(session):
    runs = make_runs_null(session, n_pairs=4, seed=9)
    stats = [s for s in stage_a(strip_labels(runs)) if not s["qc_violations"]]
    f = artifact_floor_A(stats, session, 1e-9)
    assert f["inputs"]["dT_K"] == max(s["measured"]["dT_K"] for s in stats)
    assert f["inputs"]["gnd_V"] == max(s["measured"]["gnd_shift_V"] for s in stats)
    # tampering with a run's measured channel MUST move the floor inputs
    runs[0]["artifacts"]["dT_K"] = 0.9e-3
    stats2 = [s for s in stage_a(strip_labels(runs)) if not s["qc_violations"]]
    f2 = artifact_floor_A(stats2, session, 1e-9)
    assert f2["inputs"]["dT_K"] == pytest.approx(0.9e-3)
    assert f2["i1"] > f["i1"]

def test_unqualified_rig_refuses_floor(session):
    runs = make_runs_null(session, n_pairs=4, seed=9)
    stats = stage_a(strip_labels(runs))
    bad = seal_session({**{k: session[k] for k in
                           ("r_j_ohm", "f_mod_Hz", "mech_phase_deg")},
                        "q1_dummy_null_A": 20e-12})
    with pytest.raises(ValueError, match="not qualified"):
        artifact_floor_A(stats, bad, 1e-9)

def test_exactly_at_bound_refused(session):
    """re-PT-515 minor: Q1.3's pass criterion is strict <; a rig AT the bound
    failed qualification and must be refused (was accepted by strict >)."""
    bad = seal_session({**{k: session[k] for k in
                           ("r_j_ohm", "f_mod_Hz", "mech_phase_deg")},
                        "q1_dummy_null_A": QC_BOUNDS["decoupled_null_A_max"]})
    with pytest.raises(ValueError, match="not qualified"):
        verify_session(bad)

def test_session_seal_tampering_refused(session):
    """re-PT-515 blocker 1: post-seal edits to any sealed constant (the r_j
    inflation attack, the mech-phase attack) must be refused outright."""
    runs = make_runs_null(session, n_pairs=4, seed=9)
    stats = [s for s in stage_a(strip_labels(runs)) if not s["qc_violations"]]
    tampered = {**session, "r_j_ohm": 1e7}          # the verdict-flip attack
    with pytest.raises(ValueError, match="seal mismatch"):
        artifact_floor_A(stats, tampered, 1e-9)
    tampered2 = {**session, "mech_phase_deg": 45.0}  # the phase attack
    with pytest.raises(ValueError, match="seal mismatch"):
        verify_session(tampered2)

def test_sealed_rj_crosschecked_against_runs(session):
    """Even a PRE-seal inflated r_j is caught: every run's own I-V check
    channel must agree with the sealed value within 20%."""
    runs = make_runs_null(session, n_pairs=4, seed=9)
    stats = [s for s in stage_a(strip_labels(runs)) if not s["qc_violations"]]
    inflated = seal_session({**{k: session[k] for k in
                                ("f_mod_Hz", "q1_dummy_null_A", "mech_phase_deg")},
                             "r_j_ohm": 1e7})
    with pytest.raises(ValueError, match="inconsistent with run"):
        artifact_floor_A(stats, inflated, 1e-9)

def test_floor_matches_hand_rss(session):
    runs = make_runs_null(session, n_pairs=4, seed=9)
    stats = [s for s in stage_a(strip_labels(runs)) if not s["qc_violations"]]
    f = artifact_floor_A(stats, session, 2e-9)
    hand = math.sqrt(f["i1"]**2 + f["i2"]**2 + f["i3"]**2 + f["i4"]**2 + f["i6"]**2)
    assert f["rss"] == pytest.approx(hand) and f["rss"] < 1e-9

# --- mandatory scenario 1: null --------------------------------------------------

def test_null_scenario_falsified(session):
    assert _verdict(make_runs_null(session, n_pairs=4, seed=11),
                    session)["verdict"] == "FALSIFIED-AT-DESIGN-POINT"

# --- mandatory scenario 2: injected genuine signal --------------------------------

def test_signal_scenario_detected(session):
    v = _verdict(make_runs_signal(session, i_signal_A=2e-9, n_pairs=4, seed=12), session)
    assert v["verdict"] == "L1-CANDIDATE"
    assert v["signal_test"] and v["phase_test"] and v["decoy_test"]
    assert "NOT a success claim" in v["why"] and "L1/L2" in v["l3_caveat"]

# --- mandatory scenario 3: injected artifact (QC class) ----------------------------

def test_thermal_artifact_excluded_before_labels(session):
    v = _verdict(make_runs_thermal_artifact(session, n_pairs=4, seed=13), session)
    assert v["n_excluded"] == 1 and v["verdict"] != "L1-CANDIDATE"

def test_emf_drift_not_attributed(session):
    """Drift must NEVER be cavity-attributed: balanced pairing cancels it
    (FALSIFIED) or, if residuals leak into decoys, the decoy test names it
    (ACTUATION-ARTIFACT). Either way, no L1/GATES-PENDING — across seeds."""
    for seed in (14, 21, 22, 23):
        v = _verdict(make_runs_emf_drift(session, drift_A=10e-9, n_pairs=4,
                                         seed=seed), session)
        assert v["verdict"] in ("FALSIFIED-AT-DESIGN-POINT", "ACTUATION-ARTIFACT"), \
            (seed, v["verdict"])

# --- mandatory scenario 4: actuation-correlated artifact (PT-515 blocker 3) --------

def test_piezo_heat_caught_by_decoys(session):
    """The PT-515 fooling scenario: drive-correlated artifact, QC-clean,
    in-phase, in-band. Decoy runs (drive on, mirror decoupled) expose it."""
    v = _verdict(make_runs_piezo_heat(session, i_artifact_A=2e-9, n_pairs=4, seed=15), session)
    assert v["verdict"] == "ACTUATION-ARTIFACT"
    assert v["signal_test"] and not v["decoy_test"]
    assert "outcome-2" in v["why"]

def test_partial_coupling_caught(session):
    """re-PT-515 blocker 3: the old 1x-RSS decoy threshold was blind below
    ~12% drive-to-decoy coupling. The statistical decoy test must catch a
    10% (and even 2%) coupled artifact."""
    for coupling in (0.10, 0.02):
        v = _verdict(make_runs_piezo_heat(session, i_artifact_A=2e-9, n_pairs=4,
                                          seed=15, coupling=coupling), session)
        assert v["verdict"] == "ACTUATION-ARTIFACT", (coupling, v["verdict"])

def test_genuine_signal_survives_decoys(session):
    """Symmetry check: the decoy test must NOT kill a mirror-following effect."""
    v = _verdict(make_runs_signal(session, i_signal_A=2e-9, n_pairs=4, seed=16), session)
    assert v["decoy_test"] and v["verdict"] == "L1-CANDIDATE"

# --- gates ------------------------------------------------------------------------

def test_insufficient_pairs(session):
    v = _verdict(make_runs_signal(session, n_pairs=2, seed=17), session)
    assert v["verdict"] == "INSUFFICIENT-DATA"

def test_missing_decoys_is_insufficient(session):
    runs = [r for r in make_runs_signal(session, n_pairs=4, seed=18)
            if r["_true_state"] != "decoy"]
    v = _verdict(runs, session)
    assert v["verdict"] == "INSUFFICIENT-DATA" and "decoys" in v["why"]

def test_charge_gate_blocks_l1(session):
    runs = make_runs_signal(session, i_signal_A=2e-9, n_pairs=4, seed=19)
    for r in runs:
        r["artifacts"]["charge_C"] = 1e-4
    assert _verdict(runs, session)["verdict"] == "GATES-PENDING"

def test_diminishing_signal_blocks_charge_gate(session):
    """PT-515 correction 4: row-5 requires the signal UNDIMINISHED."""
    runs = make_runs_signal(session, i_signal_A=2e-9, n_pairs=4, seed=20)
    last_closed = [r for r in runs if r["_true_state"] == "closed"][-1]
    for s in last_closed["segments"]:
        s["lockin_I_A"] -= 1.6e-9        # signal decays 80% by campaign end
    v = _verdict(runs, session)
    assert not v["signal_undiminished"] and v["verdict"] != "L1-CANDIDATE"

# --- freeze guards ------------------------------------------------------------------

def test_frozen_constants():
    assert MIN_VALID_PAIRS == 3 and MIN_DECOY_RUNS == 2
    assert CHARGE_GATE_C == pytest.approx(10e-3)
    assert UNDIMINISHED_FRACTION == pytest.approx(0.5)
    assert QC_BOUNDS == {"dT_K_max": 1e-3, "decoupled_null_A_max": 10e-12,
                         "accel_rms_g_max": 1e-3, "gnd_shift_V_max": 0.5e-6}

def test_golden_vector_signal_scenario(session):
    """End-to-end golden regression: pins formula BEHAVIOR, not just constants
    (PT-515 correction 7; re-PT-515 minor: SIGNED decoy_diff_A now pinned so a
    sign flip in the decoy differential is visible)."""
    v = _verdict(make_runs_signal(session, i_signal_A=2e-9, n_pairs=4, seed=12), session)
    assert v["mean_diff_A"] == pytest.approx(2.0e-9, rel=2e-3)
    assert v["floor"]["i4"] == pytest.approx(0.2e-9, rel=1e-6)   # 0.2 uV / 1 kohm
    assert v["floor"]["i6"] == pytest.approx(0.01 * abs(v["mean_diff_A"]), rel=1e-9)
    assert v["threshold_A"] == pytest.approx(3 * v["floor"]["rss"], rel=1e-12)
    assert v["floor"]["rss"] == pytest.approx(2.02e-10, rel=0.05)
    assert v["n_decoys"] == 2 and v["total_charge_C"] == pytest.approx(15e-3, rel=1e-6)
    assert v["decoy_threshold_A"] == pytest.approx(DECOY_ABS_FLOOR_A, rel=1e-9)

def test_golden_decoy_diff_signed(session):
    """Pin the SIGNED decoy differential on the full-coupling artifact scenario:
    decoys carry +i_artifact vs open near 0, so decoy_diff_A must be POSITIVE
    ~2 nA — a sign flip (mean_open - mean_decoy) breaks this assertion."""
    v = _verdict(make_runs_piezo_heat(session, i_artifact_A=2e-9, n_pairs=4,
                                      seed=15, coupling=1.0), session)
    assert v["decoy_diff_A"] == pytest.approx(2.0e-9, rel=5e-3)
    assert v["decoy_diff_A"] > 0

def test_audit_gate_is_attestation(session):
    """power_audit_accounted moved out of the sealed session: it is an
    operator attestation delivered with labels, defaults FALSE if absent."""
    runs = make_runs_signal(session, i_signal_A=2e-9, n_pairs=4, seed=12)
    v = stage_b(stage_a(strip_labels(runs)), make_labels(runs), session, {})
    assert not v["audit_gate"] and v["verdict"] == "GATES-PENDING"
    assert v["audit_is_attestation"] is True
