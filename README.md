# zpe-lab — the first independent test of the Casimir-cavity MIM "vacuum energy" claim

**A pre-registered, blinded, adversarially-reviewed replication study.** In 2021, an
NSF-funded group published in *Physical Review Research* that metal-insulator-metal tunnel
junctions faced with sub-micron "Casimir cavities" produce zero-bias currents drawn from
vacuum fluctuations (PRR **3**, L022007; *Symmetry* **13**, 517). Five years later there are
**zero independent replications, zero public raw datasets, and zero experimental critiques**
— a gap this project verified adversarially before deciding to close it.

**Pre-registered prior, stated up front:** the vacuum is a passive state; the expected
outcome is that the claimed effect resolves to a named measurement artifact (the untested
palladium-hydride pathway and microvolt-scale parasitic EMFs are the lead candidates) or a
bounded null. A clean falsification is this program's definition of success. If the effect
instead survives every control below, that would be extraordinary — and this protocol is the
credibility such a result would require.

## Honesty invariants (standing, from the program's founding telos)

- Never claim success unless net energy survives full input/loss/uncertainty accounting,
  blinded controls, and independent replication.
- Heat, vibration, EMI, grounding, stored charge, calibration error, and hidden external
  sources are ALWAYS competing explanations to be excluded first.
- Negative results are first-class deliverables. Never redefine failure as success.

## Why you can audit this before believing it

Everything analytical is **frozen before any device exists**, and the git history preserves
the full adversarial record — including the reviews that FAILED this project's own work and
forced redesigns:

- **Frozen analysis pipeline** ([analysis/](analysis/)) — blinded run labels, sha256-sealed
  instrument constants, interleaved decoy-run controls, a seven-class quantitative artifact
  budget with a pre-registered 3σ criterion, golden-vector regression tests. Round one of
  its adversarial review **blocked it** by demonstrating, with running code, an
  actuation-correlated false positive and an 8/8 unblinding attack; the fixes and the
  re-attacks are all in the history.
- **Protocols** ([protocols/](protocols/)) — rig build, sub-µV EMF-floor qualification (Q1),
  a known-answer calibration exercise that must pass before the contested device is touched
  (Q2), and the blinded measurement procedure.
- **Simulation + artifact budget** ([sim/](sim/)) — Simmons transport model and per-row
  artifact calculators, parameterized from a full-text extraction of the original papers.
- **Benchmarks** ([benchmarks/](benchmarks/)) — every figure of the original papers
  digitized into uncertainty-tagged numerical data, with the source images preserved for
  re-verification ([attribution](benchmarks/figs/ATTRIBUTION.md)).
- **Prior-art verification** ([outputs/](outputs/)) — the "zero independent replications"
  claim, itself adversarially counter-searched before being relied on.
- **Funding + procurement record** ([docs/funding/](docs/funding/), [docs/](docs/)) —
  applications, quotes, price-verified parts lists, and the data request to the original
  authors, kept in the open.

Run the test suite: `python -m pytest sim/ analysis/ benchmarks/ -q` (58 tests).

## Status (2026-07-11)

Design, simulation, protocols, pipeline, and benchmarks are complete and frozen.
Fabrication quotes are in progress (RIT SMFL, Texas A&M AggieFab — deliberately not the
original institution's cleanroom). Funding applications are live. Hardware has not been
purchased; no physical measurement has occurred; **no result exists yet in either
direction** — anyone claiming otherwise is ahead of the data.

## The three pre-registered outcomes

1. The effect survives blinded, decoy-controlled, hydride-controlled replication —
   extraordinary, publish with full data.
2. The signal reproduces but resolves to a named mundane source — the most likely outcome,
   publish the attribution.
3. Bounded null — publish the bound.

No level-skipping, no post-hoc criteria changes (any change to the frozen analysis requires
a new governed revision, visible in this history), no redefining failure as success.

## Governance

This repository holds the engineering artifacts. The program's full governance record
(intents, adversarial pressure-test reviews, promotion lineage) lives in a separate
governance vault; the pressure-test verdicts that shaped each artifact here are reflected in
the commit messages and revision notes.

## License

Code: MIT. Research documents, protocols, and benchmark data: CC BY 4.0 ("Ben Davis,
zpe-lab"). Third-party CC BY 4.0 material retains original attribution — see
[LICENSE](LICENSE) and [benchmarks/figs/ATTRIBUTION.md](benchmarks/figs/ATTRIBUTION.md).

## Contact

Ben Davis — interplore.media@gmail.com
