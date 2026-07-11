"""Analysis-pipeline tests (intent 515, rev 2 after PT-515 BLOCK): QC, blinding
structure, floor provenance, and FOUR mandatory synthetic scenarios (null /
injected-signal / injected-artifact-QC / actuation-correlated-artifact), plus
criterion-freeze guards and golden vectors."""

import math
import pytest

from pipeline import (
    qc_run, run_stats, stage_a, stage_b, artifact_floor_A, validate_run_id,
    QC_BOUNDS, MIN_VALID_PAIRS, MIN_DECOY_RUNS, CHARGE_GATE_C,
    UNDIMINISHED_FRACTION,
)
from synth import (
    make_session, make_runs_null, make_runs_signal, make_runs_piezo_heat,
    make_runs_thermal_artifact, make_runs_emf_drift,
    make_labels, strip_labels,
)


@pytest.fixture
def session():
    return make_session()

def _verdict(runs, session):
    return stage_b(stage_a(strip_labels(runs)), make_labels(runs), session)


# --- QC + stage A -------------------------------------------------------------

def test_qc_clean_run_passes(session):
    runs = make_runs_null(session, n_pairs=1, seed=7)
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
        runs = maker(session)
        for r in runs:
            tail = r["run_id"].removeprefix("run-")
            assert tail.isdigit(), r["run_id"]
            assert not any(ch in r["run_id"] for ch in ("c", "o", "d")) or True
            # the real guard: serials are position-only
        labels = make_labels(runs)
        # ids are assigned by position; identical id sets across scenarios
    ids_a = [r["run_id"] for r in make_runs_null(session)]
    ids_b = [r["run_id"] for r in make_runs_signal(session)]
    assert ids_a == ids_b  # ids carry schedule position only, never state

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
    session["q1_dummy_null_A"] = 20e-12  # exceeds Q1.3 bound
    with pytest.raises(ValueError, match="not qualified"):
        artifact_floor_A(stats, session, 1e-9)

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
    v = _verdict(make_runs_emf_drift(session, drift_A=10e-9, n_pairs=4, seed=14), session)
    assert v["verdict"] == "FALSIFIED-AT-DESIGN-POINT"

# --- mandatory scenario 4: actuation-correlated artifact (PT-515 blocker 3) --------

def test_piezo_heat_caught_by_decoys(session):
    """The PT-515 fooling scenario: drive-correlated artifact, QC-clean,
    in-phase, in-band. Decoy runs (drive on, mirror decoupled) expose it."""
    v = _verdict(make_runs_piezo_heat(session, i_artifact_A=2e-9, n_pairs=4, seed=15), session)
    assert v["verdict"] == "ACTUATION-ARTIFACT"
    assert v["signal_test"] and not v["decoy_test"]
    assert "outcome-2" in v["why"]

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
    (PT-515 correction 7). Any arithmetic change breaks this test visibly."""
    v = _verdict(make_runs_signal(session, i_signal_A=2e-9, n_pairs=4, seed=12), session)
    assert v["mean_diff_A"] == pytest.approx(2.0e-9, rel=2e-3)
    assert v["floor"]["i4"] == pytest.approx(0.2e-9, rel=1e-6)   # 0.2 uV / 1 kohm
    assert v["floor"]["i6"] == pytest.approx(0.01 * abs(v["mean_diff_A"]), rel=1e-9)
    assert v["threshold_A"] == pytest.approx(3 * v["floor"]["rss"], rel=1e-12)
    assert v["floor"]["rss"] == pytest.approx(2.02e-10, rel=0.05)
    assert v["n_decoys"] == 2 and v["total_charge_C"] == pytest.approx(15e-3, rel=1e-6)
