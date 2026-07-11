"""Artifact-magnitude calculators for the C1 Casimir-cavity MIM rig.

One function per row of the promoted 511 artifact budget, each returning a
predicted artifact CURRENT (amps, current-equivalent at the junction) so all
rows are directly comparable with the claimed signal. Row 5 (stored charge)
is a charge budget, returned separately. Every default parameter carries a
provenance tag in config.py; nothing here invents sourced-looking numbers.
"""

import math

K_B = 1.380649e-23  # J/K

def thermo_emf_current(seebeck_V_per_K: float, delta_T_K: float, r_j_ohm: float) -> float:
    """Row 1: thermoelectric artifact. Series voltage S*dT driven through R_j."""
    return seebeck_V_per_K * delta_T_K / r_j_ohm

def microphonic_current(v_offset_V: float, delta_C_F: float, f_mod_Hz: float) -> float:
    """Rows 2a/2b: vibration/microphonics. Capacitance modulation dC at f_mod
    against a standing offset voltage produces i = V_off * 2*pi*f * dC."""
    return v_offset_V * 2.0 * math.pi * f_mod_Hz * delta_C_F

def emi_rectified_current(beta_V_inv: float, g_j_S: float, v_rf_V: float) -> float:
    """Row 3: EMI. Square-law rectification in the junction nonlinearity:
    i_rect ~ 0.5 * beta * G_j * V_rf^2 (V_rf = RF voltage reaching the junction
    after shielding)."""
    return 0.5 * beta_V_inv * g_j_S * v_rf_V ** 2

def ground_loop_current(v_gnd_V: float, r_j_ohm: float) -> float:
    """Row 4: grounding. Residual differential ground potential across the
    measurement loop, driven through R_j (worst case: appears at the input)."""
    return v_gnd_V / r_j_ohm

def calibration_drift_fraction() -> float:
    """Row 6: calibration. Traceable-reference drift bound between pre/post
    checks. [assumption: 1e-2 fractional per run, spec-sheet class]"""
    return 1e-2

def calibration_drift_current(i_signal_A: float) -> float:
    """Row 6 as a CURRENT-EQUIVALENT (PT-513 correction #7): drift is
    multiplicative on the measured signal, so its current-equivalent is the
    drift fraction times the claimed signal magnitude."""
    return calibration_drift_fraction() * i_signal_A

def hidden_input_resolution_W() -> float:
    """Row 7: hidden external energy. Power-audit metering floor.
    [assumption: 1 uW resolution on every enclosure penetration]"""
    return 1e-6

def johnson_noise_current(r_j_ohm: float, temp_K: float, bandwidth_Hz: float) -> float:
    """Johnson-Nyquist current noise of the junction resistance (A rms)."""
    return math.sqrt(4.0 * K_B * temp_K * bandwidth_Hz / r_j_ohm)

def integration_time_for_3sigma(i_signal_A: float, i_noise_1Hz_A: float) -> float:
    """Lock-in integration time (s) for the WHITE-NOISE component alone to
    reach 3 sigma: ENBW ~ 1/(4*tau) => tau = (3*i_n(1Hz) / i_sig)^2 / 4."""
    if i_signal_A <= 0:
        return float("inf")
    return (3.0 * i_noise_1Hz_A / i_signal_A) ** 2 / 4.0

def rss(*currents_A: float) -> float:
    """Root-sum-square combination of artifact terms."""
    return math.sqrt(sum(c * c for c in currents_A))
