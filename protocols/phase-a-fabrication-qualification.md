# Phase A — Fabrication qualification (governed by intent 570, rev 2 post-PT-570-BLOCK)

**The honest answer to "develop until you see power production, then register."** The original
author correctly notes that these thin-film / interface devices are materials-sensitive: a
device that isn't competently fabricated tests nothing. He proposes developing the recipe until
the anomalous zero-bias current appears, and only then registering a replication. The program
cannot adopt that sequencing — **tune-then-register manufactures false positives**: an artifact
that emerges under unblinded tuning is reliably reproduced by "iterate until you see it," and
registering afterward launders it into a "confirmation." This protocol is the synthesis:
develop the fabrication freely, but qualify only against the published MUNDANE device baselines,
and never select or tune on the contested signal.

## What "independent" does and does NOT mean here (read this first)

The integrity of this split rests on a claim that must be stated with precision, because a
sloppy version of it is false and the original author is exactly the reader who would catch it.

- **The Phase-A criteria ARE independent of the contested signal *itself*.** The contested
  observable is the **within-device cavity-open vs cavity-closed differential** (retractable
  mirror, same junction). Phase A never measures that differential and never selects a device
  on it. Phase A cannot tune a within-device open/closed contrast: it picks *which* devices are
  tested, holding each device's resistance, barrier, and thickness fixed across the very
  open/closed comparison that constitutes the test.
- **The Phase-A criteria are NOT independent of the *expected magnitude* of the effect if it
  is real.** This is our own finding and we state it openly: the papers' data
  (`docs/casimir-device-parameters.md` Table C; `benchmarks/benchmarks.json`
  `sym-fig5b-insulator`, `prr-fig4b-insulator`) show Isc / G scaling **exponentially with
  insulator thickness** — Isc ~170 nA at 3.49 nm falling to ~5 nA at 4.22 nm; G/area ~55 → 2.3
  µS/µm² over 3.49–4.00 nm. Insulator thickness is the same parameter that sets junction
  resistance (A1) and barrier height (A3). So qualifying on the 120 Ω–6.1 kΩ resistance band
  **preferentially admits thin-insulator / high-conductance devices, which per the authors'
  own scaling curves are the high-signal end.** A1/A3/A4 ride the same tunnel-barrier physics
  as any anomalous current, real or artifactual.

**Why the split still defeats tune-then-register despite that coupling.** The failure mode being
guarded against is a *feedback loop*: measure the anomalous output → adjust fabrication to
increase it → repeat → register. Two things break that loop, and neither is disturbed by the
resistance↔signal coupling:
1. **Fixed targets.** The Phase-A target values are locked to the published baselines BEFORE
   fabrication begins and are never adjusted toward "more signal." You develop toward a device
   matching the paper's ordinary characteristics, not toward maximizing an output you are
   measuring. A well-made device may also be a larger-signal device — but *both* the
   real-effect and the artifact hypotheses predict that, so it does not bias *between* them.
   What biases between them is selecting on the effect's presence, which the gate forbids.
2. **Within-device contrast.** Because the test is cavity-open vs cavity-closed on the *same*
   junction, population-level selection of high-conductance devices changes *which* devices are
   tested, not whether toggling the cavity changes their current. A conductance-scaled artifact
   still has to survive the per-device decoy control and the per-device artifact budget, which
   operate identically regardless of how the device was selected.

The residual population-level coupling is therefore made **auditable, not eliminated** (§Audit
surface below). The narrow, exact promise remains: **no device is ever admitted to the blinded
test on the basis of having shown the effect, and the tuning feedback loop is never closed.**

## The rule

1. **Phase A: develop freely** against the mundane baselines below (all cavity-OPEN / no-mirror
   or pre-mirror measurements — see A4 note).
2. **Admission gate (enforced, not advisory).** A device enters Phase B only if a
   **sealed Phase-A record** exists for it — a hashed record of its measured A1–A4 values,
   committed to the repo BEFORE any cavity/mirror measurement exists for that device (the
   `seal_session` pattern already used for run constants). The pipeline refuses a device whose
   Phase-A record is missing, unsealed, or post-dated relative to its first cavity measurement.
3. **Phase B: the existing FROZEN blinded test** (`blinded-measurement.md`, pipeline `bd81f70`),
   unchanged.

## Phase-A qualification criteria (PRE-REGISTERED, targets LOCKED before fabrication)

| # | Criterion | Target (locked to published baselines) | Measured with | Relation to the effect |
|---|---|---|---|---|
| A1 | Junction differential resistance (per area) | within extracted **120 Ω – 6.1 kΩ** band | 4-point I-V, no mirror | correlated with signal magnitude (stated above), NOT with the open/closed differential |
| A2 | Low-bias I(V) linearity | linear near zero bias (papers' stated design property) | 4-point I-V sweep, no mirror | mundane transport property |
| A3 | Fowler-Nordheim barrier heights | consistent with **0.2 eV (NiOx) / 0.3 eV (Al2O3)** | FN analysis, no mirror | shares barrier physics with signal magnitude |
| A4 | Layer thicknesses | within tolerance of the target stack | VASE/AFM on the deposited stack | design-target check; see note |

**A4 note (PT-570 fix):** thicknesses are verified against the *deposition target* by VASE/AFM
on the fabricated stack. The Al MIRROR is part of the target stack spec but its presence does
NOT make A1–A3 cavity-dependent: **all A1–A3 electrical checks are performed cavity-OPEN
(mirror retracted / not yet engaged).** A1–A3 are never measured with the mirror in the design
gap.

**Explicitly NOT a Phase-A criterion:** the zero-bias current, the cavity-open/closed
differential, or any cavity-state-correlated quantity. If any Phase-A criterion were the
contested signal, the split would be defeated — this table plus the §Audit surface is where
that is checked.

## Audit surface (PT-570 mitigations — makes the residual coupling checkable)

- **Full-distribution commit.** Every fabricated device's Phase-A record — **pass AND fail**,
  with measured R / barrier / thickness values and the qualification rate (N attempted, M
  passed) — is committed to the public repo. An outside reviewer can audit directly for
  thin-insulator / low-resistance selection bias.
- **Pre-registered admission order.** Among a passing cohort, Phase-B entry order is
  **fabrication-date-sequential (or seeded-random), never resistance/thickness-optimized.** No
  discretionary "test the best-looking ones first."
- **Sealed pre-cavity record.** Per-device hashed Phase-A record (above) prevents backdating or
  post-hoc editing of the qualification.

## Deposition-parameter provision

The Phase-A recipe is sourced (1) verbatim from the author's specific deposition conditions if
provided (pre-registered so a null cannot be blamed on deviation), else (2) the
non-specifiability is recorded as a pre-registered reproducibility finding — **with a stopping
rule so this is a falsifiable declaration, not a discretionary escape (PT-570 fix):** a recipe
is declared non-specifiable only after **≥ 20 qualified fabrication attempts across ≥ 3
distinct deposition-parameter sets fail to yield the effect at ≥ 3σ**, OR after a **90-day
non-response** to a specific written request to the author for parameters, whichever first. The
threshold and its outcome are committed before the count starts.

## Honesty boundary (stated, not hidden)

The split closes tune-then-register and the tuning feedback loop; it does not eliminate the
population-level resistance↔magnitude coupling (which is physically unavoidable in a MIM system
and is instead made auditable above). If a real effect required a fabrication condition
specifiable *only* via the contested signal, Phase-A-qualified devices might not show it — but
that is precisely the not-independently-reproducible case, a **finding**, not a protocol
failure.

## What this does NOT change

The frozen analysis pipeline (`analysis/`, `bd81f70`), the blinded criterion, the seven-class
artifact budget, and Q1/Q2 are unchanged. Phase A is a new upstream gate; any change to the
frozen pipeline arithmetic remains a separate governed revision.
