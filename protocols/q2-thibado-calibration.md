# Q2 — Thibado-style known-answer calibration exercise (intent 515; 511 "Phase-1b")

**THIS IS NOT A VACUUM-ENERGY TEST.** Thibado's graphene-ripple work (PRE 108, 024130
(2023)) is explicitly THERMAL physics and second-law-compliant — its own authors say
same-temperature steady-state harvesting is forbidden. We run a version of it because
the correct result is KNOWN, which makes it a calibration standard for exactly the
disciplines our contested-claim rig needs: fA–nA electrometry, thermal-gradient control,
grounding, and honest transient-vs-steady-state bookkeeping.

## Expected result (stated up front — this is the answer key)
1. With the rectifier circuit at a common temperature with the fluctuation source:
   capacitor charge accumulates TRANSIENTLY, the accumulation rate decays, and net
   charging **saturates**; long-run net current at equilibrium → **zero** within
   measurement uncertainty.
2. Any apparent sustained net current is a METHODOLOGY BUG in our lab (thermal gradient,
   ground loop, instrument offset, diode self-heating) — find it and fix it. That is the
   exercise working as intended.

## Build (off-the-shelf, <$200; no graphene needed)
The calibration does not require actual graphene: any high-impedance thermal-noise
source (large-R resistor at known T) + two opposed low-leakage diodes + storage caps
reproduces the same measurement problem class (fA-scale rectification bookkeeping at
matched temperature). Optional stretch: commercial few-layer-graphene-on-grid sample.

## Pass criteria
| # | Test | Pass threshold |
|---|---|---|
| Q2.1 | Transient phase: charge accumulation observed and logged from cold start | accumulation curve recorded with ≥10:1 SNR |
| Q2.2 | Saturation: d(charge)/dt at t ≥ 10× initial decay constant | consistent with **zero** within 2σ of the measured noise floor |
| Q2.3 | Thermal-gradient injection (deliberate, e.g. +2 °C on diodes): apparent "signal" appears | our artifact channels (thermistor pair) FLAG it and the analysis attributes it to row 1, not to the source |
| Q2.4 | Full run processed end-to-end through `analysis/pipeline.py` | pipeline QC + attribution behave as designed on real hardware data |

Q2.3 is the most valuable test: it deliberately creates the classic free-energy false
positive and verifies our instrumentation + pipeline catch it. **Do not skip it.**

## Honest-reporting rule
Q2 results are reported as calibration outcomes. Under no circumstances may Q2 transient
charging be described as "energy harvesting" in any program document without the
saturation curve attached (this is the exact press-conflation failure mode the 511
dossier documented).
