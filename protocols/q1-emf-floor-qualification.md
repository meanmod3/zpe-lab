# Q1 — Sub-µV EMF-floor qualification protocol (intent 515)

**Purpose:** the promoted 513 verdict is a CONDITIONED GO — no DUT (device-under-test)
measurement is valid until the rig demonstrates the EMF floor this protocol defines.
At the papers' own unexplained ~6 µV offset level, a 120 Ω junction's verdict is NO-GO;
this qualification is what makes results interpretable.

**Hardware under qualification:** the full signal chain WITHOUT any tunneling device:
dummy-junction die (non-tunneling, ≥10 nm AlOx; fab die type 5) mounted identically to a
DUT, driven through the IDENTICAL piezo modulation waveform, read through the identical
battery transimpedance front-end → lock-in → logger.

## Pass criteria (all numeric, all mandatory)

| # | Test | Pass threshold | Traceability |
|---|---|---|---|
| Q1.1 | DC offset, dummy in place, piezo OFF, 1 h log | equivalent EMF < **0.5 µV** (I_offset × R_dummy_readout) after current-reversal | 513 sensitivity: 1 µV floor halves the 120 Ω margin; 0.5 µV keeps kΩ-class margins >10× |
| Q1.2 | Lock-in amplitude at f_mod, piezo ON, mirror MECHANICALLY DECOUPLED (drive energized, nothing moves), 1 h | < instrument noise floor (no f_mod-synchronous electrical crosstalk) | 511 row 2b/3 shared control |
| Q1.3 | Lock-in amplitude at f_mod, piezo ON, mirror MOVING over dummy, ≥3 h | < **10 pA** equivalent (f_mod-synchronous microphonics bound); simultaneously establish the accelerometer RMS baseline — campaign QC bound = **1×10⁻³ g RMS** (any DUT run above it is invalid) and record the **mechanical phase reference** (lock-in phase of the drive) used by the pipeline's phase test | 513 budget row 2; 10 pA = 5000× below claimed 50 nA; accel + phase-ref feed pipeline QC_BOUNDS / session record |
| Q1.6 | Mirror no-contact verification: engage/retract cycle under microscope + electrical continuity check between mirror assembly and DUT mount | zero mechanical contact, open circuit at all travel points | residual-limitation control (blinded-measurement protocol): a mirror-contact artifact is NOT separable by decoy runs |
| Q1.7 | Decoy-path fidelity: inject a deliberate drive-line disturbance (e.g. 10× drive amplitude step) in CLOSED config, then in DECOY config (mirror decoupled, identical duty cycle) | disturbance amplitude in DECOY config ≥ **80%** of CLOSED config | re-PT-515: the decoy control only catches drive-path artifacts to the extent the decoy config actually couples to the drive like the closed config does — this test BOUNDS that coupling instead of assuming it |
| Q1.4 | Ground-topology permutation (≥3 configurations: star point moved, ground lifted where safe, battery vs isolated supply) | per-config DC shift < **0.5 µV** equivalent | 511 row 4 |
| Q1.5 | Thermal soak: enclosure setpoint stepped ±2 °C, junction ΔT logged | junction ΔT < **1 mK** sustained; output shift < Q1.1 bound | 511 row 1 (papers' own stage sweeps were 22–25 °C ambient scale) |

## Procedure notes
- Every test logs ALL artifact channels (thermistor pair, accelerometer, SDR events,
  integrated charge, enclosure power meters) in the standard run format
  (`analysis/README` schema) — Q1 runs double as the artifact-channel baseline dataset.
- Q1 failing is a RIG finding, not a program failure: fix mechanics/grounding and repeat.
  The rig is qualified when all five pass in a SINGLE contiguous session, recorded and
  committed as `data/q1-qualification-<date>/`.
- **Requalification triggers:** any cabling change, front-end battery swap, enclosure
  penetration change, or >30 days elapsed.
