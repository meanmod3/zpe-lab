"""MIM tunnel-junction transport model (Simmons, low-voltage limit).

Simmons, J. Appl. Phys. 34, 1793 (1963), low-voltage approximation for a
rectangular barrier. Engineering form (phi in eV, s in Angstrom):

    G/A = 3.16e10 * sqrt(phi) / s * exp(-1.025 * s * sqrt(phi))   [ohm^-1 cm^-2]

Every caller must treat outputs as ORDER-OF-MAGNITUDE physics, valid for
2-50 A barriers and low bias; that is sufficient for artifact budgeting,
which needs decades, not percent.
"""

import math

def simmons_conductance_per_cm2(phi_eV: float, s_angstrom: float) -> float:
    """Zero-bias tunneling conductance per cm^2 (ohm^-1 cm^-2)."""
    if phi_eV <= 0 or s_angstrom <= 0:
        raise ValueError("barrier height and thickness must be positive")
    root_phi = math.sqrt(phi_eV)
    return 3.16e10 * root_phi / s_angstrom * math.exp(-1.025 * s_angstrom * root_phi)

def junction_resistance_ohm(phi_eV: float, s_angstrom: float, area_cm2: float) -> float:
    """Junction resistance for a given device area."""
    g = simmons_conductance_per_cm2(phi_eV, s_angstrom) * area_cm2
    if g == 0:
        return float("inf")
    return 1.0 / g

def responsivity_bound_V_inv() -> float:
    """Even-order nonlinearity parameter beta ~ I''/(2 I') in V^-1 — a FLAT
    engineering upper bound, deliberately NOT operating-point-derived
    (PT-513 correction #4: former signature took decorative phi/s params).

    MIM small-signal square-law responsivity is typically 1-10 V^-1
    (barrier-asymmetry dependent); overestimating EMI rectification is the
    safe direction for artifact budgeting. [assumption: beta_max = 10 V^-1,
    engineering upper bound for asymmetric MIM diodes; rectenna literature]
    """
    return 10.0
