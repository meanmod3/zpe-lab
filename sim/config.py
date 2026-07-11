"""Phase-1 simulation configuration (intent 513).

EVERY value carries a provenance tag:
  [extracted: ...]  — read from the primary sources by the 2026-07-11 full-text
                      extraction (docs/casimir-device-parameters.md): PRR =
                      Phys. Rev. Research 3, L022007 (2021) (+SM); SYM =
                      Symmetry 13(3), 517 (2021) via its arXiv-published text.
  [assumption: ...] — modeled/engineering value NOT stated in the papers.
Intent 513 metric #2: zero unlabeled numbers.
"""

# --- claimed-signal scale (the thing the rig must discriminate) --------------

# [extracted: SYM Fig. 4(a) — short-circuit currents ~20-100 nA for the
#  0.02 um^2 GSM device across 33-1100 nm cavities; figure-read, not tabulated]
I_CLAIMED_GSM_A = 50e-9

# [extracted: SYM Fig. 6(b) — Isc up to ~50-60 nA at 10,000 um^2 photolitho
#  devices; figure-read] — benchtop replication would use photolitho-scale dies.
I_CLAIMED_PHOTOLITHO_A = 50e-9

# [extracted: SYM 3.1 — only absolute power figure in either paper: 1.4 pW max
#  at 0 V for the 33 nm-cavity 0.02 um^2 device, P = |Isc*Voc|/4]
P_CLAIMED_MAX_W = 1.4e-12

# [extracted: PRR-SM — cavity devices show persistent anomalous voltage offset
#  ~6 uV; no-cavity references <1 uV / <1 nA after current-reversal correction]
V_ANOMALOUS_OFFSET_V = 6e-6

# --- junction impedance points (intent metric #4 requires >= 2) --------------

# [extracted: PRR Fig. 3(a) — G = 1 mS (33 nm cavity) => R_j = 1 kohm]
# [extracted: PRR-SM — reference MIM devices spanned 120-6100 ohm]
R_J_POINTS_OHM = {
    "GSM-33nm-cavity (G=1 mS)": 1.0e3,
    "photolitho-low-R (ref set floor)": 120.0,
    "photolitho-high-R (ref set ceiling)": 6.1e3,
}

# [extracted: PRR — Fowler-Nordheim barrier heights: electrons 0.2 eV (NiOx),
#  0.3 eV (Al2O3); effective insulator 1.7-4.2 nm across device sets]
BARRIER_EV_RANGE = (0.2, 0.3)
INSULATOR_NM_RANGE = (1.7, 4.2)

# --- rig / artifact parameters ------------------------------------------------

# [assumption: 20 uV/K effective stack Seebeck bound — PRR-SM cites bulk
#  Ni -18, Pd -9, insulator >100 uV/K and notes thin-film values deviate;
#  20 uV/K is a deliberate over-bound of the metal pair for budgeting]
SEEBECK_V_PER_K = 20e-6
# [assumption: rig spec from promoted 511 budget row 1]
DELTA_T_K = 1e-3

# [assumption: 1 mV standing offset across modulated capacitance — generous
#  bound on contact-potential differences in the front-end wiring]
V_OFFSET_MICROPHONIC_V = 1e-3
# [assumption: 1 fF residual piezo-synchronous capacitance modulation after
#  rigid triax mounting; 100 fF unmitigated worst case]
DELTA_C_MITIGATED_F = 1e-15
DELTA_C_WORST_F = 1e-13
# [assumption: 511 design — mechanical cavity modulation 1 Hz]
F_MOD_HZ = 1.0

# [assumption: 1 V/m ambient field, 60 dB enclosure, ~1 cm effective pickup
#  => ~10 uV RF at the junction; conservative]
V_RF_AT_JUNCTION_V = 10e-6

# [assumption: 0.1 uV residual differential ground EMF after star ground +
#  battery front-end + current-reversal protocol; 1 uV without reversal —
#  chosen because PRR-SM shows uncorrected offsets ~10 uV collapsing to
#  <1 uV under the current-reversal method]
V_GND_RESIDUAL_V = 0.1e-6
V_GND_NO_REVERSAL_V = 1e-6

# [assumption: room-temperature rig, matches papers' 21.6-23.4 C]
TEMP_K = 296.0

# [extracted: SYM 3.2.1 — papers demonstrate only a 4-hour stability window;
#  our stored-charge exclusion (511 row 5) needs integrated charge > 10 mC]
PAPER_STABILITY_WINDOW_S = 4 * 3600.0
STORED_CHARGE_EXCLUSION_C = 10e-3
