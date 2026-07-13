# Phase A — Fabrication qualification (governed by intent 570)

**The honest answer to "develop until you see power production, then register."** The original
author correctly notes that these thin-film / interface devices are materials-sensitive: a
device that isn't competently fabricated tests nothing. He proposes developing the recipe until
the anomalous zero-bias current appears, and only then registering a replication. The program
cannot adopt that sequencing — **tune-then-register manufactures false positives**: an artifact
that emerges under unblinded tuning is reliably reproduced by "iterate until you see it," and
registering afterward launders it into a "confirmation." That is the exact failure the whole
program exists to avoid.

This protocol is the synthesis: **develop the fabrication freely, but qualify only against the
published MUNDANE device baselines — never against the contested signal.**

## The rule

1. **Phase A (this document): develop freely.** Iterate the fabrication recipe until junctions
   match the published *ordinary* device characteristics below. Every criterion is measurable
   **with no cavity present** and makes **no reference to the anomalous zero-bias current**, so
   developing against them cannot bias the Phase-B test.
2. **Admission gate.** Only devices that pass ALL Phase-A criteria — with their measured values
   recorded — are admitted to Phase B. A device that never qualifies is a *fabrication* outcome,
   not a physics result, and is logged as such.
3. **Phase B (unchanged): the frozen blinded test** (`blinded-measurement.md`, analysis pipeline
   `bd81f70`). Phase A does not touch it.

## Phase-A qualification criteria (PRE-REGISTERED)

Each is tied to a value extracted from the published papers (see `docs/casimir-device-parameters.md`
and `benchmarks/benchmarks.json`) and is a mundane, cavity-independent device property.

| # | Criterion | Target (from published baselines) | Measured with | Cavity-independent? |
|---|---|---|---|---|
| A1 | Junction differential resistance (per device area) | within the extracted **120 Ω – 6.1 kΩ** reference-device band | 4-point I-V, no cavity | Yes — bare MIM |
| A2 | Low-bias I(V) linearity | linear near zero bias (the papers' own stated design property; low barrier heights) | 4-point I-V sweep, no cavity | Yes |
| A3 | Fowler-Nordheim barrier heights | consistent with extracted **0.2 eV (NiOx) / 0.3 eV (Al2O3)** | FN analysis of I-V, no cavity | Yes |
| A4 | Layer thicknesses | within tolerance of the target stack (Ni 50 nm / NiOx+AlOx ~1.3–4 nm / Pd·Pt·Ni top / SiO2 spacer / Al mirror) | VASE / AFM | Yes — pre-cavity metrology |

**Explicitly NOT a Phase-A criterion:** the zero-bias current, the cavity-open/closed
differential, or any cavity-correlated quantity. Those live only in Phase B, blinded. If any
Phase-A criterion were the contested signal, the split would be defeated — this table is the
audit surface for that.

## Deposition-parameter provision (pre-registered position)

The Phase-A *recipe* is sourced as follows, in priority order:
1. **If the original author (or the papers/patents) specifies the deposition conditions** —
   rates, pressures, substrate temperatures, timings, anneal steps — those are pre-registered
   **verbatim** as the Phase-A recipe and followed faithfully, so a null result cannot be
   attributed to recipe deviation.
2. **If the working window is genuinely NOT specifiable** except as "iterate until you see the
   effect," that non-specifiability is itself recorded as a **pre-registered reproducibility
   finding**: an effect whose fabrication window can only be identified by the contested signal
   is, by construction, not independently reproducible.

## Honesty boundary (stated, not hidden)

This split closes the tune-then-register pathway **for the anomalous signal**. It does not, and
cannot, claim to eliminate every conceivable tuning correlation: if the effect requires a
fabrication condition specifiable *only* via the contested signal, then Phase-A-qualified
devices might not show it even if it is "real" — but that scenario is precisely the
not-independently-reproducible case above, and it is a **finding**, not a failure of the
protocol. The protocol's promise is narrow and exact: **no device is ever admitted to the
blinded test on the basis of having shown the effect.**

## What this does NOT change

The frozen analysis pipeline (`analysis/`, `bd81f70`), the blinded-measurement criterion, the
seven-class artifact budget, and the Q1/Q2 qualification are all unchanged. Phase A is a new
*upstream* gate; any change to the frozen pipeline arithmetic remains a separate governed
revision.
