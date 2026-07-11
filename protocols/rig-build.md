# Rig build protocol — C1 measurement chain (intent 515)

Operator-executable assembly of the measurement chain per the promoted 511 design and
513 BOM. Order below is deliberate: everything is qualifiable BEFORE any DUT exists.

## 1. Enclosure + thermal
- Faraday enclosure (BOM 6): gasketed box, all penetrations through filtered feedthroughs.
  Verify ≥60 dB attenuation 10 kHz–6 GHz: reference antenna inside, swept source outside,
  SDR (BOM 7) records both sides; keep the sweep file as the enclosure's birth certificate.
- Inner temperature-controlled dark stage (BOM 10): Peltier + PID, photodiode dark
  monitor. Target: junction-scale ΔT < 1 mK sustained (verified by the matched thermistor
  pair, BOM 8, mounted across the future DUT position).

## 2. Grounding + signal chain (the load-bearing part)
- SINGLE star ground point; document it with a photo + wiring map in `data/rig-map/`.
- Battery-powered transimpedance front-end (BOM 4) inside the enclosure; triax/guarded
  cable (BOM 13) only; every cable mechanically clamped (microphonics discipline).
- Lock-in (BOM 2) referenced to the piezo drive; source-meter/electrometer (BOM 3) for
  DC + I-V; ALL instruments on one DAQ timebase (BOM 14).
- Piezo flexure stage (BOM 5): drive line isolated + separately shielded; the
  mirror-decoupling mechanism (drive energized, mirror not moving) must be operable
  without opening the enclosure — it is a per-session control, not a one-time test.
- Current-reversal capability wired in from day one (polarity-swap relay or manual
  fixture) — the papers' own offsets drop 10 µV → <1 µV under reversal; ours must too.

## 3. Metering (row 7)
- Every enclosure penetration gets a power audit point (BOM 12), µW-class on DC lines.
- Pre-registered honesty note (513 finding 4): this bounds µW-scale hidden inputs only;
  it CANNOT certify pW-scale claims — L3 is out of scope at single-device scale.

## 4. Calibration discipline (row 6)
- Traceable current/voltage reference (BOM 11): pre- AND post-run checks, logged into
  the run file; interleaved shorted/open baseline segments in every run.
- Instrument calibration certificates filed in `data/rig-map/`.

## 5. Qualification order (hard gates)
1. Enclosure sweep passes → 2. Q2 calibration exercise (protocols/q2) passes →
3. Q1 EMF-floor qualification (protocols/q1) passes → 4. ONLY THEN order/mount DUT dies.
- Purchases and the 32%-over-envelope decision are the operator's (513 BOM flag).
- Device selection rule (promoted 513): prioritize kΩ-class+ junctions; any low-R_j
  (~120 Ω) result is inconclusive unless Q1 passed in the same session.
