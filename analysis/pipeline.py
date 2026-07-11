"""Pre-registered blinded analysis pipeline (intent 515, rev 2 after PT-515 BLOCK).

What "frozen" means here, precisely: the constants below are pinned by tests,
the end-to-end behavior is pinned by golden-vector regression tests, and the
committed hash is recorded in the vault note. Formula changes are detectable
by the golden vectors and forbidden by governance (new intent + PT required).

Stage A (label-free): QC each run against Q1-baseline bounds, emit per-run
statistics. Data files carry NO cavity-state field and run ids MUST be opaque
sequential serials assigned before the operator's blind draw (PT-515 blocker 2).
Stage B (after per-run stats are committed): join the operator-held label file
(states: closed / open / decoy) and evaluate the criterion:

  - artifact floor: RSS of rows 1,2,3,4,6 as current-equivalents, computed
    from the MEASURED per-run artifact channels of THIS campaign's valid runs
    (maxima across runs — PT-515 blocker 1: no hand-supplied floor inputs),
    plus the Q1.3 measured dummy null (cross-checked against its bound).
  - signal test: |mean paired closed-open differential| > 3 x RSS floor.
  - phase test: every amplitude-qualified closed run within tolerance of the
    session's measured mechanical phase reference (PT-515 correction 5).
  - DECOY test (PT-515 blocker 3): interleaved decoy runs (piezo drive with
    identical duty cycle, mirror mechanically decoupled) must show NO
    differential vs open — an actuation-correlated artifact follows the drive
    and appears in decoys; a real cavity effect follows the MIRROR and cannot.
  - row-5 charge gate: >= 10 mC cumulative AND signal undiminished
    (last closed run >= 50% of first closed run — PT-515 correction 4).
  - row-7 audit gate + L3 caveat.

Run `python pipeline.py --demo` for a synthetic end-to-end demonstration.
"""

import json
import math
import os
import statistics
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "sim"))
import config as cfg                      # noqa: E402
from artifacts import (                   # noqa: E402
    thermo_emf_current, emi_rectified_current,
    ground_loop_current, calibration_drift_current, rss,
)
from transport import responsivity_bound_V_inv  # noqa: E402

# --- pre-registered QC bounds (Q1 protocol, numeric) --------------------------

QC_BOUNDS = {
    "dT_K_max": 1e-3,                # Q1.5 / 511 row 1
    "decoupled_null_A_max": 10e-12,  # Q1.2/Q1.3 crosstalk+microphonics bound
    "accel_rms_g_max": 1e-3,         # Q1.3 accelerometer RMS baseline bound
    "gnd_shift_V_max": 0.5e-6,       # Q1.1/Q1.4
}

MIN_VALID_PAIRS = 3                  # promoted 511 criterion
MIN_DECOY_RUNS = 2                   # PT-515: interleaved actuation controls
CHARGE_GATE_C = cfg.STORED_CHARGE_EXCLUSION_C   # 10 mC, row 5
PHASE_TOLERANCE_DEG = 30.0           # vs measured mechanical phase reference
UNDIMINISHED_FRACTION = 0.5          # row-5 "signal undiminished" (511)

RUN_ID_ALLOWED = "run-"              # opaque serial prefix; digits only after


# --- Stage A: label-free ------------------------------------------------------

def validate_run_id(run_id: str):
    """PT-515 blocker 2: run ids must be opaque sequential serials that cannot
    encode cavity state. Anything but run-<digits> is rejected outright."""
    tail = run_id[len(RUN_ID_ALLOWED):]
    if not (run_id.startswith(RUN_ID_ALLOWED) and tail.isdigit()):
        raise ValueError(
            f"run_id '{run_id}' is not an opaque serial (run-<digits>); "
            "state-encoding identifiers are forbidden by protocol")


def qc_run(run: dict) -> list:
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
    """Per-run lock-in statistics + measured artifact channels passthrough
    (the floor is built from these, not from any hand-supplied value)."""
    validate_run_id(run["run_id"])
    I = [s["lockin_I_A"] for s in run["segments"]]
    Q = [s["lockin_Q_A"] for s in run["segments"]]
    mi, mq = statistics.fmean(I), statistics.fmean(Q)
    sigma = statistics.stdev(I) if len(I) > 1 else 0.0
    return {
        "run_id": run["run_id"],
        "mean_I_A": mi, "mean_Q_A": mq,
        "amp_A": math.hypot(mi, mq),
        "phase_deg": math.degrees(math.atan2(mq, mi)),
        "sigma_I_A": sigma, "sem_I_A": sigma / math.sqrt(len(I)),
        "n_segments": len(I),
        "charge_C": run["artifacts"]["charge_C"],
        "measured": {k: run["artifacts"][k] for k in
                     ("dT_K", "decoupled_null_A", "gnd_shift_V", "rf_v_V")},
        "qc_violations": qc_run(run),
    }


def stage_a(runs: list) -> list:
    return [run_stats(r) for r in runs]


# --- Stage B: label join + criterion ------------------------------------------

def artifact_floor_A(valid_stats: list, session: dict, i_signal_A: float) -> dict:
    """RSS floor from THIS campaign's measured channels (PT-515 blocker 1):
    rows 1/3/4 use the MAXIMA of the valid runs' measured artifact channels;
    row 2 uses the larger of the per-run decoupled nulls and the Q1.3 dummy
    null (a measured current, cross-checked against its qualification bound);
    row 6 is the calibration drift fraction of the quantity under test.
    `session` supplies only measured device/rig constants: r_j (device I-V),
    q1_dummy_null_A (Q1.3 record), mech_phase_deg (Q1 reference)."""
    if session["q1_dummy_null_A"] > QC_BOUNDS["decoupled_null_A_max"]:
        raise ValueError("session Q1.3 dummy null exceeds its qualification "
                         "bound — rig is not qualified; refuse to compute a floor")
    r_j = session["r_j_ohm"]
    dT = max(s["measured"]["dT_K"] for s in valid_stats)
    v_rf = max(s["measured"]["rf_v_V"] for s in valid_stats)
    v_gnd = max(s["measured"]["gnd_shift_V"] for s in valid_stats)
    null = max([session["q1_dummy_null_A"]] +
               [s["measured"]["decoupled_null_A"] for s in valid_stats])
    i1 = thermo_emf_current(cfg.SEEBECK_V_PER_K, dT, r_j)
    i2 = null                                   # measured f_mod-synchronous bound
    i3 = emi_rectified_current(responsivity_bound_V_inv(), 1.0 / r_j, v_rf)
    i4 = ground_loop_current(v_gnd, r_j)
    i6 = calibration_drift_current(abs(i_signal_A))
    return {"i1": i1, "i2": i2, "i3": i3, "i4": i4, "i6": i6,
            "inputs": {"dT_K": dT, "v_rf_V": v_rf, "gnd_V": v_gnd,
                       "null_A": null, "r_j_ohm": r_j},
            "rss": rss(i1, i2, i3, i4, i6)}


def _phase_test(closed: list, session: dict, floor_rss: float) -> dict:
    """Amplitude-qualified closed runs (amp > 3x SEM AND above the floor) must
    all sit within tolerance of the measured mechanical phase reference."""
    ref = session["mech_phase_deg"]
    qualified = [s for s in closed
                 if s["amp_A"] > 3 * s["sem_I_A"] and s["amp_A"] > floor_rss]
    if not qualified:
        return {"ok": False, "why": "no amplitude-qualified closed runs"}
    off = [abs((s["phase_deg"] - ref + 180) % 360 - 180) for s in qualified]
    ok = max(off) <= PHASE_TOLERANCE_DEG
    return {"ok": ok, "n_qualified": len(qualified), "max_offset_deg": max(off)}


def stage_b(per_run_stats: list, labels: dict, session: dict) -> dict:
    valid = [s for s in per_run_stats if not s["qc_violations"]]
    excluded = [s for s in per_run_stats if s["qc_violations"]]
    closed = [s for s in valid if labels[s["run_id"]] == "closed"]
    open_ = [s for s in valid if labels[s["run_id"]] == "open"]
    decoy = [s for s in valid if labels[s["run_id"]] == "decoy"]
    n_pairs = min(len(closed), len(open_))

    result = {
        "n_runs": len(per_run_stats), "n_valid": len(valid),
        "n_excluded": len(excluded),
        "excluded": [{"run_id": s["run_id"], "why": s["qc_violations"]} for s in excluded],
        "n_pairs": n_pairs, "n_decoys": len(decoy),
    }
    if n_pairs < MIN_VALID_PAIRS or len(decoy) < MIN_DECOY_RUNS:
        result["verdict"] = "INSUFFICIENT-DATA"
        result["why"] = (f"{n_pairs} valid pairs (need {MIN_VALID_PAIRS}) / "
                         f"{len(decoy)} decoys (need {MIN_DECOY_RUNS})")
        return result

    diffs = [c["mean_I_A"] - o["mean_I_A"] for c, o in zip(closed, open_)]
    mean_diff = statistics.fmean(diffs)
    floor = artifact_floor_A(valid, session, mean_diff)
    threshold = 3.0 * floor["rss"]
    signal_test = abs(mean_diff) > threshold

    mean_open = statistics.fmean([o["mean_I_A"] for o in open_])
    decoy_diff = statistics.fmean([d["mean_I_A"] for d in decoy]) - mean_open
    decoy_test = abs(decoy_diff) < floor["rss"]          # 1x floor, pre-registered

    ph = _phase_test(closed, session, floor["rss"])

    first, last = abs(closed[0]["mean_I_A"]), abs(closed[-1]["mean_I_A"])
    undiminished = (last >= UNDIMINISHED_FRACTION * first) if first > floor["rss"] else True
    total_charge = sum(s["charge_C"] for s in valid)
    charge_gate = total_charge >= CHARGE_GATE_C and undiminished
    audit_gate = session["power_audit_accounted"]

    result.update({
        "mean_diff_A": mean_diff, "floor": floor, "threshold_A": threshold,
        "signal_test": signal_test, "phase": ph, "phase_test": ph["ok"],
        "decoy_diff_A": decoy_diff, "decoy_test": decoy_test,
        "total_charge_C": total_charge, "signal_undiminished": undiminished,
        "charge_gate": charge_gate, "audit_gate": audit_gate,
        "l3_caveat": ("Power-audit floor (~1 uW) cannot bound pW-scale inputs; "
                      "this analysis supports L1/L2 claims ONLY (promoted 513 finding 4)."),
    })

    if signal_test and not decoy_test:
        result["verdict"] = "ACTUATION-ARTIFACT"
        result["why"] = ("Differential follows the piezo DRIVE (present in decoy "
                         "runs with the mirror decoupled), not the mirror — a "
                         "mundane actuation-correlated source. Telos outcome-2 "
                         "candidate: characterize and name it.")
    elif signal_test and ph["ok"] and decoy_test and charge_gate and audit_gate:
        result["verdict"] = "L1-CANDIDATE"
        result["why"] = ("Pre-registered criterion met incl. decoy null. This is "
                         "NOT a success claim: proceed to the L2 artifact-exclusion "
                         "campaign (H-loading, Ni-variant, second site).")
    elif signal_test and ph["ok"] and decoy_test:
        result["verdict"] = "GATES-PENDING"
        result["why"] = "Signal+phase+decoy pass but row-5/row-7 gates not yet satisfied."
    else:
        result["verdict"] = "FALSIFIED-AT-DESIGN-POINT"
        result["why"] = ("Differential does not exceed 3x the measured artifact floor "
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
