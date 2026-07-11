# C1 Casimir-cavity MIM falsification rig — draft BOM (intent 513)

Status: DRAFT — zero spend authorized; every line is a target price (used-market where noted)
for operator review. Totals are compared against the 511 cost envelope ($3.3–7.5k).

| # | Item | Purpose (budget row) | Target price | Notes |
|---|---|---|---|---|
| 1 | Thin-film fabrication run (MIM stack + Casimir cavity layers, incl. Ni-electrode control variant + dummy-junction dies) | DUT | $1,500–3,000 | See fab-quote-package.md; single biggest cost + schedule risk |
| 2 | Lock-in amplifier, used (SR510/SR830 class) | primary discriminator | $500–1,500 | ENBW down to mHz; f_mod reference out |
| 3 | Source-meter / electrometer, used (Keithley 617/6517/2400 class) | signal chain, rows 1–6 | $800–2,000 | fA–nA class input; calibration cert preferred |
| 4 | Battery-powered low-noise transimpedance preamp (kit/build) | signal chain, row 4 | $150–300 | battery supply removes mains-borne ground paths |
| 5 | Piezo flexure stage + driver (small travel, ~µm) | cavity modulation | $300–600 used | drive line isolated; mirror-decoupled crosstalk test required |
| 6 | Faraday enclosure (mesh + gasketed box, self-built) + reference antenna | row 3 | $150–300 | verify ≥60 dB 10 kHz–6 GHz with SDR sweep |
| 7 | SDR receiver (RTL-SDR/HackRF class) | row 3 ambient log | $30–300 | inside + outside spectra, timestamped |
| 8 | Matched thermistor pair + readout (mK-resolution bridge) | row 1 | $100–250 | calibrated pair across junction |
| 9 | 3-axis accelerometer + logger | row 2a | $50–150 | synchronous channel to main logger |
| 10 | Temperature-controlled dark enclosure (Peltier + PID, self-built) | rows 1, 7 | $150–300 | photodiode dark monitor included |
| 11 | Precision current/voltage reference (traceable) | row 6 | $150–400 | pre/post-run calibration checks |
| 12 | Power-audit metering on every enclosure penetration | row 7 | $100–200 | µW-class resolution on DC lines |
| 13 | Cabling: triax/guarded + rigid mounting hardware | rows 2b, 4 | $150–300 | microphonics mitigation is mechanical |
| 14 | Data logger / DAQ (all channels, one timebase) | protocol | $150–300 | |

**Total (target): $4,280–9,900. Used-market + favorable fab quote: ~$3.4–5k.**
Consistent with the 511 envelope; items 2–3 dominate variance. Nothing is purchased under
intent 513 — this BOM is the operator-approval package for a future build intent.
