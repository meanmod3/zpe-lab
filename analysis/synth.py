"""Synthetic run generators for pipeline tests (intent 515).

Deterministic (seeded) — these are the pipeline's answer-key scenarios:
  null            : artifact channels in bounds, no cavity-correlated signal
  injected signal : genuine in-phase differential present only in CLOSED runs
  thermal artifact: a run with a deliberate dT excursion (must be QC-excluded)
  emf drift       : a slow common-mode drift hitting OPEN and CLOSED alike
                    (must NOT produce a differential verdict)
"""

import random

NOISE_A = 5e-12   # per-segment lock-in noise scale (Johnson-class at kohm)


def make_session():
    """Session metadata as the operator would record it (kohm-class device,
    per the promoted-513 device-selection rule)."""
    return {
        "r_j_ohm": 1.0e3,
        "f_mod_Hz": 1.0,
        "dT_K_worst": 0.5e-3,          # within Q1.5 bound
        "delta_C_F_measured": 1e-15,   # post-mitigation, Q1.3-consistent
        "v_rf_V_measured": 10e-6,      # enclosure-verified
        "gnd_emf_V_measured": 0.3e-6,  # Q1.1-passing rig
        "power_audit_accounted": True,
    }


def _artifacts_ok(rng):
    return {
        "dT_K": 0.3e-3 + rng.uniform(0, 0.2e-3),
        "decoupled_null_A": 2e-12,
        "accel_rms_g": 2e-4,
        "gnd_shift_V": 0.2e-6,
        "cal_pre_ok": True, "cal_post_ok": True,
        "charge_C": 1.5e-3,   # per-run integrated |I|dt
    }


def _run(run_id, rng, mean_I=0.0, mean_Q=0.0, n_seg=60):
    return {
        "run_id": run_id,
        "segments": [{"lockin_I_A": mean_I + rng.gauss(0, NOISE_A),
                      "lockin_Q_A": mean_Q + rng.gauss(0, NOISE_A)}
                     for _ in range(n_seg)],
        "artifacts": _artifacts_ok(rng),
        "_true_state": None,  # set by callers; stripped before stage A in tests
    }


def _pair_order(k):
    """ABBA sequencing per the blinded-measurement protocol: alternate the
    within-pair order so slow common-mode drift cancels across pairs."""
    return ("closed", "open") if k % 2 == 0 else ("open", "closed")


def make_runs_null(session, n_pairs=4, seed=1):
    rng = random.Random(seed)
    runs = []
    for k in range(n_pairs):
        for state in _pair_order(k):
            r = _run(f"run-{k:02d}-{state[0]}", rng)
            r["_true_state"] = state
            runs.append(r)
    return runs


def make_runs_signal(session, i_signal_A=2e-9, n_pairs=4, seed=2):
    """Genuine effect: in-phase differential present only when cavity CLOSED
    (a real effect follows the mirror, not the run schedule)."""
    rng = random.Random(seed)
    runs = []
    for k in range(n_pairs):
        for state in _pair_order(k):
            amp = i_signal_A if state == "closed" else 0.0
            r = _run(f"run-{k:02d}-{state[0]}", rng, mean_I=amp)
            r["_true_state"] = state
            runs.append(r)
    return runs


def make_runs_thermal_artifact(session, n_pairs=4, seed=3):
    """One CLOSED run carries a deliberate thermal excursion (Q2.3-style):
    big apparent in-phase current AND a dT channel violation. The pipeline
    must EXCLUDE that run at QC, before any label is seen."""
    runs = make_runs_null(session, n_pairs=n_pairs, seed=seed)
    rng = random.Random(seed + 100)
    victim = next(r for r in runs if r["_true_state"] == "closed")
    for s in victim["segments"]:
        s["lockin_I_A"] += 40e-9
    victim["artifacts"]["dT_K"] = 5e-3   # exceeds the 1 mK bound
    return runs


def make_runs_emf_drift(session, drift_A=10e-9, n_pairs=4, seed=4):
    """Slow common-mode EMF drift: shifts OPEN and CLOSED runs EQUALLY
    (it does not know about the mirror). Paired differential must stay null."""
    runs = make_runs_null(session, n_pairs=n_pairs, seed=seed)
    for idx, r in enumerate(runs):
        offset = drift_A * (idx / len(runs))   # slow ramp across the session
        for s in r["segments"]:
            s["lockin_I_A"] += offset
    return runs


def make_labels(runs):
    return {r["run_id"]: r["_true_state"] for r in runs}


def strip_labels(runs):
    """What stage A actually receives: no state anywhere."""
    out = []
    for r in runs:
        c = {k: v for k, v in r.items() if k != "_true_state"}
        out.append(c)
    return out
