"""Analysis-pipeline tests (intent 515 metric #3): QC, blinding structure,
and the three mandatory synthetic scenarios (null / injected-signal /
injected-artifact), plus criterion-freeze guards."""

import math
import pytest

from pipeline import (
    qc_run, run_stats, stage_a, stage_b, artifact_floor_A,
    QC_BOUNDS, MIN_VALID_PAIRS, CHARGE_GATE_C,
)
from synth import (
    make_session, make_runs_null, make_runs_signal,
    make_runs_thermal_artifact, make_runs_emf_drift,
    make_labels, strip_labels,
)


@pytest.fixture
def session():
    return make_session()


# --- QC + stage A -------------------------------------------------------------

def test_qc_clean_run_passes(session):
    runs = make_runs_null(session, n_pairs=1, seed=7)
    assert qc_run(runs[0]) == []

def test_qc_flags_thermal_violation(session):
    runs = make_runs_thermal_artifact(session, seed=7)
    flagged = [r for r in runs if qc_run(r)]
    assert len(flagged) == 1
    assert any("dT" in v for v in qc_run(flagged[0]))

def test_run_stats_shape(session):
    r = make_runs_null(session, n_pairs=1, seed=7)[0]
    s = run_stats(r)
    assert s["n_segments"] == 60
    assert abs(s["mean_I_A"]) < 5e-12  # null run: mean within noise scale

def test_stage_a_needs_no_labels(session):
    """Blinding structure: stage A runs on label-stripped data identically."""
    runs = make_runs_null(session, n_pairs=2, seed=8)
    stats_stripped = stage_a(strip_labels(runs))
    assert all("_true_state" not in s for s in stats_stripped)
    assert len(stats_stripped) == 4

# --- mandatory scenario 1: null -------------------------------------------------

def test_null_scenario_falsified(session):
    runs = make_runs_null(session, n_pairs=4, seed=11)
    verdict = stage_b(stage_a(strip_labels(runs)), make_labels(runs), session)
    assert verdict["verdict"] == "FALSIFIED-AT-DESIGN-POINT"

# --- mandatory scenario 2: injected genuine signal ------------------------------

def test_signal_scenario_detected(session):
    runs = make_runs_signal(session, i_signal_A=2e-9, n_pairs=4, seed=12)
    verdict = stage_b(stage_a(strip_labels(runs)), make_labels(runs), session)
    assert verdict["verdict"] == "L1-CANDIDATE"
    assert verdict["signal_test"] and verdict["phase_test"]

def test_signal_verdict_is_not_a_success_claim(session):
    runs = make_runs_signal(session, i_signal_A=2e-9, n_pairs=4, seed=12)
    verdict = stage_b(stage_a(strip_labels(runs)), make_labels(runs), session)
    assert "NOT a success claim" in verdict["why"]
    assert "L1/L2" in verdict["l3_caveat"]

# --- mandatory scenario 3: injected artifacts -----------------------------------

def test_thermal_artifact_excluded_before_labels(session):
    runs = make_runs_thermal_artifact(session, n_pairs=4, seed=13)
    stats = stage_a(strip_labels(runs))          # QC happens label-free
    verdict = stage_b(stats, make_labels(runs), session)
    assert verdict["n_excluded"] == 1
    assert verdict["verdict"] != "L1-CANDIDATE"  # 40 nA fake never reaches the verdict

def test_emf_drift_not_attributed(session):
    """Slow common-mode drift (10 nA across the session — 100x the floor) must
    cancel under ABBA pairing, never producing a cavity attribution."""
    runs = make_runs_emf_drift(session, drift_A=10e-9, n_pairs=4, seed=14)
    verdict = stage_b(stage_a(strip_labels(runs)), make_labels(runs), session)
    assert verdict["verdict"] == "FALSIFIED-AT-DESIGN-POINT"

# --- gates + insufficiency ------------------------------------------------------

def test_insufficient_pairs(session):
    runs = make_runs_signal(session, n_pairs=2, seed=15)
    verdict = stage_b(stage_a(strip_labels(runs)), make_labels(runs), session)
    assert verdict["verdict"] == "INSUFFICIENT-DATA"

def test_charge_gate_blocks_l1(session):
    runs = make_runs_signal(session, i_signal_A=2e-9, n_pairs=4, seed=16)
    for r in runs:
        r["artifacts"]["charge_C"] = 1e-4        # campaign total 0.8 mC < 10 mC
    verdict = stage_b(stage_a(strip_labels(runs)), make_labels(runs), session)
    assert verdict["verdict"] == "GATES-PENDING"

# --- criterion freeze guards ----------------------------------------------------

def test_frozen_constants_match_promoted_513():
    assert MIN_VALID_PAIRS == 3
    assert CHARGE_GATE_C == pytest.approx(10e-3)
    assert QC_BOUNDS["dT_K_max"] == pytest.approx(1e-3)
    assert QC_BOUNDS["decoupled_null_A_max"] == pytest.approx(10e-12)

def test_floor_matches_hand_rss(session):
    f = artifact_floor_A(session, i_signal_A=2e-9)
    hand = math.sqrt(f["i1"]**2 + f["i2"]**2 + f["i3"]**2 + f["i4"]**2 + f["i6"]**2)
    assert f["rss"] == pytest.approx(hand)
    # kohm-class session, Q1-passing rig: floor must sit well below nA scale
    assert f["rss"] < 1e-9
