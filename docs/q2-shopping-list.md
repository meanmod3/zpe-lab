# Q2 calibration rig — shopping list (operational elaboration of promoted 515, Q2 protocol)

Status: PRICE-VERIFIED 2026-07-11 (live DigiKey/Mouser/eBay pass). Zero purchases made —
this is the operator's buy list. **Honest correction to the Q2 protocol's <$200 circuit
target: not achievable at current catalog pricing — the verified circuit-side range is
$245–385** (real high-meg resistor and enclosure prices). Instruments are listed separately
because they ARE main-rig BOM items (bought once, exercised first on Q2).

Q2 recap (protocols/q2-thibado-calibration.md): a known-answer exercise — thermal-noise
source + opposed low-leakage diodes + storage caps; expected result is transient charging
that SATURATES (zero net current at matched-temperature equilibrium). Q2.3 deliberately
injects a thermal gradient our instrumentation must catch. No graphene required.

## A. Q2 circuit components (the <$200 core)

| # | Item | Spec / candidate parts | Qty | Est. | Source | Q2 role |
|---|---|---|---|---|---|---|
| A1 | Ultra-low-leakage diodes | Linear Integrated Systems **PAD1** (<1 pA; DigiKey PAD1-TO-72-3L-ROHS, $7.04@1, in stock) or **PAD5** (same family, active); JFET-as-diode fallback: **Linear Integrated Systems 2N4117A-TO-72-4L** ($7.46@1 — the Vishay 2N4117A is OBSOLETE/0-stock, do NOT hunt it); SMD backup: Nexperia **BAS416** (3 pA typ). Avoid 1N4148 (~25 nA typ — verified unsuitable) | 6 (2 opposed + spares/matching) | $40–45 | DigiKey / Mouser | The rectifier pair — the heart of Q2.1/Q2.2 |
| A2 | High-meg noise-source resistors | 100 MΩ + 1 GΩ: Ohmite MOX (e.g. MOX-750231007FE 1 GΩ ±1% = $13.67 ea, in stock); **10 GΩ: NO in-stock catalog part confirmed — verify a real Vishay 'Above 1 GΩ' part number + lead time BEFORE relying on that value**, or cap the sweep at 1 GΩ | 2 each value | $70–150 | DigiKey/Mouser | Johnson-noise source at known T; value sweep varies noise magnitude |
| A3 | Storage capacitors, low-leakage | C0G/NP0 ceramic 1–100 nF (TDK/Murata) + polypropylene film 1 µF (WIMA MKP) + polystyrene if findable | 4–6 assorted | $10–20 | DigiKey/Mouser | The charge-accumulation element (Q2.1 transient, Q2.2 saturation) |
| A4 | PTFE insulation hardware | PTFE standoffs/terminals (deadbug construction), PTFE-insulated wire | 10+ standoffs | $15–25 | DigiKey / eBay | Leakage discipline — board leakage must sit below the diode leakage |
| A5 | Shielded enclosure | Hammond **1590D** ($28–34) + 4 BNC bulkhead feedthroughs (insulated variants cost more than plain — buy both kinds) | 1 box, 4 BNC | $55–95 | DigiKey/Mouser | Faraday enclosure for the fA-scale node |
| A6 | Matched thermistor pair | 10 kΩ NTC, e.g. TDK/EPCOS **B57891M** class ±1% — buy 10, select the best-matched pair (also feeds main-rig row 1) | 10 | $10–15 | DigiKey | Q2.3 thermal channels; mK-resolution via bridge/DMM ratio |
| A7 | Gradient injector | 25–50 Ω power resistor heater + adhesive pad (or a small TEC module, 12 V) + bench supply reuse | 1 | $10–20 | DigiKey / Amazon | Q2.3's deliberate false-positive injection |
| A8 | Hygiene consumables | Desiccant packs, IPA (flux/residue cleaning), nitrile gloves | — | $15 | Amazon / hardware | GΩ-node humidity + contamination control (leakage killers) |

**Circuit-side subtotal (price-verified): ~$245–385.** The Q2 protocol's <$200 aspiration is
superseded by this verified range — the honest number wins; the delta is real resistor and
enclosure prices, not scope growth.

## B. Readout — TWO paths (choose one; path 1 is a main-rig purchase brought forward)

| Path | Contents | Est. | Notes |
|---|---|---|---|
| **B1. Used electrometer (main-rig BOM item 3 bought early)** | Keithley **617** (verified eBay cluster $480–800 — the budget-realistic target) or **6514** (budget $800–2,000; commands a premium) | $480–2,000 | fA-class input; THE main-rig signal instrument — buying now means Q2 exercises the real chain (spend belongs to the main-rig budget line) |
| **B2. DIY femtoamp front-end (bridge option if B1 waits)** | TI **LMP7721** (verified: datasheet-titled '3-Femtoampere Input Bias', active, $7.34@1, 2,363 in stock) + 1–10 GΩ glass-sealed feedback R + guard-ring deadbug + 9 V lithium supply, read by any DMM/ADC. Optional upgrade: ADI **ADA4530-1** (±20 fA MAX, production-tested; $38.41@1, ~5× price; not required for Q2 pass) | $40–90 | Classic sub-pA TIA; teaches the µV/fA discipline cheaply; NOT a substitute for the electrometer at DUT time |

## C. Logging + thermometry readout (shared with main rig)

| # | Item | Spec | Est. | Notes |
|---|---|---|---|---|
| C1 | 6.5-digit DMM, used | Keithley **2000** ($150–350, still realistic) or Keysight **34401A** (verified now ~$350–450 used) | $200–450 | Thermistor bridge readout + general bench; main-rig reuse |
| C2a | Logger/DAQ — budget path | Raspberry Pi + 24-bit ADC HAT | $60–150 | One timebase for all channels — the pipeline's run format (analysis/README.md) starts HERE |
| C2b | Logger/DAQ — turnkey path | LabJack **U3-LV** (verified $210.94, Active, in stock) or **T4** ($305 new) | $210–305 | Same role; verified pricing — the old '$60–200 LabJack' band no longer exists |
| C3 | Battery supply | 9 V lithium packs / sealed lead-acid 12 V + holders | $20–40 | Floating front-end supply (row-4 grounding discipline from day one) |

## D. What Q2 deliberately does NOT need
- No lock-in amplifier (that's the DUT-phase discriminator, BOM item 2 — buy at Q1 time).
- No piezo stage, no SDR, no fabricated devices.
- No graphene (per the protocol: any high-R thermal-noise source reproduces the measurement
  problem class).

## Totals
- **Q2-only path (circuit + B2 DIY front-end + C2a logger):** **~$350–750 all-new**
  (price-verified; the earlier ~$240–525 estimate is superseded).
- **Program-smart path (circuit + B1 617-class electrometer + C1 DMM + C2):**
  **~$950–2,000 typical** ($950–3,000+ tail if the 6514 is targeted instead of the 617) —
  most of which is main-rig BOM items 3/8/14 purchased early, which Q2 then validates.
  Recommended: program-smart path with the **Keithley 617** as the realistic target, since
  Q2's whole purpose is proving out the REAL chain.

## Q2 pass-criteria coverage map
- Q2.1 transient (≥10:1 SNR): A1–A5 + readout path.
- Q2.2 saturation (zero net current at equilibrium, 2σ): logging duration via C2; low-leakage
  discipline A3/A4/A8 is what makes "zero" measurable.
- Q2.3 gradient injection flagged by artifact channels: A6 thermistors + A7 heater + C1.
- Q2.4 end-to-end through the frozen pipeline: C2's timestamped channels in the run format.

## Purchase rules (standing)
All purchases are the operator's. eBay/used-market items: prefer sellers with test
photos/return policy; calibration certs for B1/C1 if available. Nothing here commits the
32%-over-envelope decision — that trigger only fires with the full main-rig purchase.
