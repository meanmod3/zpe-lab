"""Pre-registered blinded analysis pipeline (intent 515) — FROZEN before any
hardware data exists. Changing the arithmetic below requires a new governed
intent with its own pressure-test.

Stage A (label-free): QC each run against Q1-baseline bounds, emit per-run
statistics. Cannot produce a verdict — data files carry no cavity-state field.
Stage B (after per-run stats are committed): join the operator-held label file,
form ABBA pairs, evaluate the promoted-513 criterion:
    |mean paired differential| > 3 x RSS(rows 1,2,3,4,6 as current-equivalents)
    AND lock-in phase consistency AND row-5 charge gate AND row-7 audit gate.

Run `python pipeline.py --demo` for a synthetic end-to-end demonstration.
"""

import json
import math
import os
import statistics
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "sim"))
import config as cfg                      # noqa: E402  (sim/config.py — promoted 513 parameters)
from artifacts import (                   # noqa: E402
    thermo_emf_current, microphonic_current, emi_rectified_current,
    ground_loop_current, calibration_drift_current, rss,
)
from transport import responsivity_bound_V_inv  # noqa: E402

# --- pre-registered QC bounds (Q1 protocol, numeric) --------------------------

QC_BOUNDS = {
    "dT_K_max": 1e-3,              # Q1.5 / 511 row 1
    "decoupled_null_A_max": 10e-12,  # Q1.2/Q1.3 crosstalk+microphonics bound
    "accel_rms_g_max": 1e-3,       # rig-baseline vibration bound
    "gnd_shift_V_max": 0.5e-6,     # Q1.1/Q1.4
}

MIN_VALID_PAIRS = 3                 # promoted 511 criterion
CHARGE_GATE_C = cfg.STORED_CHARGE_EXCLUSION_C   # 10 mC, row 5
PHASE_TOLERANCE_DEG = 30.0          # lock-in in-phase consistency window


# --- Stage A: label-free ------------------------------------------------------

def qc_run(run: dict) -> list:
    """Return list of QC violations (empty = valid). Pre-registered bounds only;
    post-hoc exclusion reasons are forbidden by protocol."""
    a = run["artifacts"]
    v = []
    if a["dT_K"] > QC_BOUNDS["dT_K_max"]:
        v.append(f"dT {a['dT_K']:.2e} K > {QC_BOUNDS['dT_K_max']:.0e}")
    if a["decoupled_null_A"] > QC_BOUNDS["decoupled_null_A_max"]:
        v.append("decoupled-drive lock-in null exceeded")
    if a["accel_rms_g"] > QC_BOUNDS["accel_rms_g_max"]:
        v.append("vibration bound exceeded")
    if a["gnd_shift_V"] > QC_BOUNDS["gnd_shift_V_max"]:
        v.append("ground-permutation shift exceeded")
    if not (a["cal_pre_ok"] and a["cal_post_ok"]):
        v.append("calibration check failed")
    return v

def run_stats(run: dict) -> dict:
    """Per-run lock-in statistics. NO label access."""
    I = [s["lockin_I_A"] for s in run["segments"]]
    Q = [s["lockin_Q_A"] for s in run["segments"]]
    mi, mq = statistics.fmean(I), statistics.fmean(Q)
    amp = math.hypot(mi, mq)
    phase = math.degrees(math.atan2(mq, mi))
    return {
        "run_id": run["run_id"],
        "mean_I_A": mi, "mean_Q_A": mq,
        "amp_A": amp, "phase_deg": phase,
        "sigma_I_A": statistics.stdev(I) if len(I) > 1 else 0.0,
        "n_segments": len(I),
        "charge_C": run["artifacts"]["charge_C"],
        "qc_violations": qc_run(run),
    }

def stage_a(runs: list) -> list:
    return [run_stats(r) for r in runs]


# --- Stage B: label join + criterion ------------------------------------------

def artifact_floor_A(session: dict, i_signal_A: float) -> dict:
    """RSS floor from the SAME session's measured artifact channels, via the
    promoted-513 calculators. Rows 1,2,3,4,6 as current-equivalents."""
    r_j = session["r_j_ohm"]
    i1 = thermo_emf_current(cfg.SEEBECK_V_PER_K, session["dT_K_worst"], r_j)
    i2 = microphonic_current(cfg.V_OFFSET_MICROPHONIC_V,
                             session["delta_C_F_measured"], session["f_mod_Hz"])
    i3 = emi_rectified_current(responsivity_bound_V_inv(), 1.0 / r_j,
                               session["v_rf_V_measured"])
    i4 = ground_loop_current(session["gnd_emf_V_measured"], r_j)
    i6 = calibration_drift_current(abs(i_signal_A))
    return {"i1": i1, "i2": i2, "i3": i3, "i4": i4, "i6": i6,
            "rss": rss(i1, i2, i3, i4, i6)}

def stage_b(per_run_stats: list, labels: dict, session: dict) -> dict:
    valid = [s for s in per_run_stats if not s["qc_violations"]]
    excluded = [s for s in per_run_stats if s["qc_violations"]]
    closed = [s for s in valid if labels[s["run_id"]] == "closed"]
    open_ = [s for s in valid if labels[s["run_id"]] == "open"]
    n_pairs = min(len(closed), len(open_))

    result = {
        "n_runs": len(per_run_stats), "n_valid": len(valid),
        "n_excluded": len(excluded),
        "excluded": [{"run_id": s["run_id"], "why": s["qc_violations"]} for s in excluded],
        "n_pairs": n_pairs,
    }
    if n_pairs < MIN_VALID_PAIRS:
        result["verdict"] = "INSUFFICIENT-DATA"
        result["why"] = f"{n_pairs} valid pairs < pre-registered minimum {MIN_VALID_PAIRS}"
        return result

    diffs = [c["mean_I_A"] - o["mean_I_A"] for c, o in zip(closed, open_)]
    mean_diff = statistics.fmean(diffs)
    floor = artifact_floor_A(session, mean_diff)
    threshold = 3.0 * floor["rss"]

    signal_test = abs(mean_diff) > threshold
    phases = [c["phase_deg"] for c in closed if c["amp_A"] > 0]
    phase_test = (len(phases) > 0 and
                  max(phases) - min(phases) <= 2 * PHASE_TOLERANCE_DEG)
    total_charge = sum(s["charge_C"] for s in valid)
    charge_gate = total_charge >= CHARGE_GATE_C
    audit_gate = session["power_audit_accounted"]

    result.update({
        "mean_diff_A": mean_diff, "floor": floor, "threshold_A": threshold,
        "signal_test": signal_test, "phase_test": phase_test,
        "total_charge_C": total_charge, "charge_gate": charge_gate,
        "audit_gate": audit_gate,
        "l3_caveat": ("Power-audit floor (~1 uW) cannot bound pW-scale inputs; "
                      "this analysis supports L1/L2 claims ONLY (promoted 513 finding 4)."),
    })
    if signal_test and phase_test and charge_gate and audit_gate:
        result["verdict"] = "L1-CANDIDATE"
        result["why"] = ("Pre-registered criterion met. This is NOT a success claim: "
                         "proceed to the L2 artifact-exclusion campaign "
                         "(H-loading, Ni-variant, second site).")
    elif signal_test and phase_test:
        result["verdict"] = "GATES-PENDING"
        result["why"] = "Signal+phase pass but row-5/row-7 gates not yet satisfied."
    else:
        result["verdict"] = "FALSIFIED-AT-DESIGN-POINT"
        result["why"] = ("Differential does not exceed 3x the session artifact floor "
                         "with phase consistency — telos outcome 3 for this design point.")
    return result


# --- demo ----------------------------------------------------------------------

def _demo():
    from synth import make_session, make_runs_null, make_labels
    session = make_session()
    runs = make_runs_null(session, n_pairs=4, seed=11)
    stats = stage_a(runs)
    labels = make_labels(runs)
    verdict = stage_b(stats, labels, session)
    print(json.dumps(verdict, indent=2, default=str)[:1500])
    print("--- demo verdict:", verdict["verdict"])


if __name__ == "__main__":
    if "--demo" in sys.argv:
        _demo()
    else:
        print(__doc__)
