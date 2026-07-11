"""Synthetic run generators for pipeline tests (intent 515, rev 2 after PT-515).

Deterministic (seeded). Scenarios:
  null              : artifact channels in bounds, no cavity-correlated signal
  injected signal   : genuine in-phase differential following the MIRROR
                      (closed runs only — decoys, drive-on/mirror-decoupled,
                      show nothing, because the cavity is what matters)
  thermal artifact  : one run with a deliberate dT excursion (QC-excluded)
  emf drift         : slow time-ramp hitting all states alike (ABBA cancels)
  piezo heat        : PT-515 blocker-3 scenario — an actuation-correlated
                      artifact that follows the DRIVE duty cycle, so it
                      appears in closed AND decoy runs (mirror irrelevant).
                      The decoy test must catch it: verdict ACTUATION-ARTIFACT.

Run ids are opaque sequential serials assigned BEFORE the state draw
(PT-515 blocker 2) — they cannot encode cavity state.
"""

import random

NOISE_A = 5e-12


def make_session():
    """SEALED measured device/rig constants (seal committed pre-draw):
    r_j from the device's own I-V check; q1_dummy_null_A from the Q1.3
    qualification record; mech_phase_deg from the Q1 phase reference."""
    from pipeline import seal_session
    return seal_session({
        "r_j_ohm": 1.0e3,
        "f_mod_Hz": 1.0,
        "q1_dummy_null_A": 3e-12,
        "mech_phase_deg": 0.0,
    })


def make_attestations():
    """Operator attestations delivered WITH the label file at unblinding."""
    return {"power_audit_accounted": True}


def _artifacts_ok(rng):
    return {
        "dT_K": 0.3e-3 + rng.uniform(0, 0.2e-3),
        "decoupled_null_A": 2e-12,
        "accel_rms_g": 2e-4,
        "gnd_shift_V": 0.2e-6,
        "rf_v_V": 8e-6,
        "r_j_check_ohm": 1.0e3 * (1 + rng.uniform(-0.05, 0.05)),  # per-run I-V check
        "cal_pre_ok": True, "cal_post_ok": True,
        "charge_C": 1.5e-3,
    }


def _run(serial, rng, mean_I=0.0, mean_Q=0.0, n_seg=60):
    return {
        "run_id": f"run-{serial:03d}",     # opaque serial, no state encoding
        "segments": [{"lockin_I_A": mean_I + rng.gauss(0, NOISE_A),
                      "lockin_Q_A": mean_Q + rng.gauss(0, NOISE_A)}
                     for _ in range(n_seg)],
        "artifacts": _artifacts_ok(rng),
        "_true_state": None,
    }


def draw_schedule(n_pairs, rng):
    """The operator's RANDOM blind draw (re-PT-515 blocker 2: a deterministic
    schedule was 100% predictable from campaign size alone). BALANCED-random:
    equal counts of closed-first and open-first pairs in a random permutation —
    unpredictable to the analyst, yet linear common-mode drift still cancels to
    first order (the property the old fixed-ABBA order existed for; odd
    n_pairs leaves a one-pair residual, noted in the protocol). The two decoys
    land at random INTERIOR positions (never first, never last — the
    anti-clustering rule the fixed schedule violated)."""
    if n_pairs < 2:
        raise ValueError("campaign below protocol minimum: need >=2 pairs to "
                         "place 2 interior decoys (and >=3 valid pairs to analyze)")
    orders = ["cf"] * ((n_pairs + 1) // 2) + ["of"] * (n_pairs // 2)
    rng.shuffle(orders)
    seq = []
    for o in orders:
        seq.extend(("closed", "open") if o == "cf" else ("open", "closed"))
    positions = sorted(rng.sample(range(1, len(seq)), 2))
    for i, p in enumerate(positions):
        seq.insert(p + i, "decoy")
    return seq


def _build(session, n_pairs, seed, amp_for):
    """amp_for(state) -> (mean_I, mean_Q) injected into that run."""
    rng = random.Random(seed)
    runs = []
    for serial, state in enumerate(draw_schedule(n_pairs, rng)):
        mi, mq = amp_for(state)
        r = _run(serial, rng, mean_I=mi, mean_Q=mq)
        r["_true_state"] = state
        runs.append(r)
    return runs


def make_runs_null(session, n_pairs=4, seed=1):
    return _build(session, n_pairs, seed, lambda s: (0.0, 0.0))


def make_runs_signal(session, i_signal_A=2e-9, n_pairs=4, seed=2):
    """Genuine effect: follows the MIRROR — closed only, never decoys."""
    return _build(session, n_pairs, seed,
                  lambda s: (i_signal_A, 0.0) if s == "closed" else (0.0, 0.0))


def make_runs_piezo_heat(session, i_artifact_A=2e-9, n_pairs=4, seed=5,
                         coupling=1.0):
    """PT-515 blocker-3: actuation-correlated artifact — follows the DRIVE,
    appearing in closed runs at full strength and in decoy runs at
    `coupling` x strength (re-PT-515 quantified the old decoy test's blind
    spot below ~12% coupling; the statistical decoy test must catch far less)."""
    def amp(s):
        if s == "closed":
            return (i_artifact_A, 0.0)
        if s == "decoy":
            return (coupling * i_artifact_A, 0.0)
        return (0.0, 0.0)
    return _build(session, n_pairs, seed, amp)


def make_runs_thermal_artifact(session, n_pairs=4, seed=3):
    runs = make_runs_null(session, n_pairs=n_pairs, seed=seed)
    victim = next(r for r in runs if r["_true_state"] == "closed")
    for s in victim["segments"]:
        s["lockin_I_A"] += 40e-9
    victim["artifacts"]["dT_K"] = 5e-3
    return runs


def make_runs_emf_drift(session, drift_A=10e-9, n_pairs=4, seed=4):
    runs = make_runs_null(session, n_pairs=n_pairs, seed=seed)
    for idx, r in enumerate(runs):
        offset = drift_A * (idx / len(runs))
        for s in r["segments"]:
            s["lockin_I_A"] += offset
    return runs


def make_labels(runs):
    return {r["run_id"]: r["_true_state"] for r in runs}


def strip_labels(runs):
    return [{k: v for k, v in r.items() if k != "_true_state"} for r in runs]
