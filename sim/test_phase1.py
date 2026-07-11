"""Phase-1 model tests — physics sanity + verdict logic (intent 513 metric #1)."""

import math
import pytest

from transport import simmons_conductance_per_cm2, junction_resistance_ohm, responsivity_V_inv
from artifacts import (
    thermo_emf_current, microphonic_current, emi_rectified_current,
    ground_loop_current, stored_charge_budget_C, calibration_drift_fraction,
    hidden_input_resolution_W, johnson_noise_current,
    integration_time_for_3sigma, rss,
)
from verdict import VerdictInput, decide, MAX_PRACTICAL_INTEGRATION_S


# --- transport -------------------------------------------------------------

def test_simmons_thicker_barrier_less_conductive():
    g_thin = simmons_conductance_per_cm2(1.0, 20.0)
    g_thick = simmons_conductance_per_cm2(1.0, 30.0)
    assert g_thick < g_thin

def test_simmons_higher_barrier_less_conductive():
    assert simmons_conductance_per_cm2(2.0, 25.0) < simmons_conductance_per_cm2(0.5, 25.0)

def test_simmons_known_magnitude():
    # phi=1 eV, s=20 A: exp(-1.025*20) ~ 1.2e-9; prefactor 1.58e9 -> G/A ~ O(1) S/cm^2.
    g = simmons_conductance_per_cm2(1.0, 20.0)
    assert 0.1 < g < 10.0

def test_junction_resistance_scales_inverse_area():
    r1 = junction_resistance_ohm(1.0, 25.0, 1e-4)
    r2 = junction_resistance_ohm(1.0, 25.0, 2e-4)
    assert r1 / r2 == pytest.approx(2.0)

def test_simmons_rejects_nonphysical():
    with pytest.raises(ValueError):
        simmons_conductance_per_cm2(-1.0, 20.0)

# --- artifact calculators ---------------------------------------------------

def test_thermo_emf_example():
    # 10 uV/K * 1 mK / 1 kohm = 10 pA
    assert thermo_emf_current(10e-6, 1e-3, 1e3) == pytest.approx(10e-12)

def test_microphonic_scales_with_fmod_and_dC():
    base = microphonic_current(1e-3, 1e-15, 1.0)
    assert microphonic_current(1e-3, 1e-15, 10.0) == pytest.approx(10 * base)
    assert microphonic_current(1e-3, 1e-14, 1.0) == pytest.approx(10 * base)

def test_emi_rectified_square_law():
    i1 = emi_rectified_current(10.0, 1e-3, 1e-5)
    i2 = emi_rectified_current(10.0, 1e-3, 2e-5)
    assert i2 == pytest.approx(4 * i1)

def test_ground_loop_ohms_law():
    assert ground_loop_current(1e-6, 1e6) == pytest.approx(1e-12)

def test_static_budget_rows_present():
    assert stored_charge_budget_C() > 0
    assert 0 < calibration_drift_fraction() < 1
    assert hidden_input_resolution_W() > 0

def test_johnson_noise_magnitude():
    # 1 Mohm at 300 K, 1 Hz: sqrt(4kT/R) ~ 129 fA/rtHz
    i_n = johnson_noise_current(1e6, 300.0, 1.0)
    assert i_n == pytest.approx(1.29e-13, rel=0.02)

def test_integration_time_shrinks_with_signal():
    assert integration_time_for_3sigma(1e-12, 1e-13) < integration_time_for_3sigma(1e-13, 1e-13)

def test_rss():
    assert rss(3.0, 4.0) == pytest.approx(5.0)

# --- verdict ----------------------------------------------------------------

def test_verdict_go_when_margin_and_time_ok():
    v = decide(VerdictInput("x", 1e-9, 1e-11, 1e-13, 10.0))
    assert v.go and v.margin > 1.0

def test_verdict_no_go_on_artifact_floor():
    v = decide(VerdictInput("x", 1e-12, 1e-11, 1e-13, 10.0))
    assert not v.go and "artifact" in v.limiting_factor

def test_verdict_no_go_on_integration_time():
    v = decide(VerdictInput("x", 1e-9, 1e-11, 1e-13, MAX_PRACTICAL_INTEGRATION_S * 2))
    assert not v.go and "integration" in v.limiting_factor
