> **WITHDRAWN 2026-07-13 — fundraising closed; project archived, not an active pursuit. No funds were raised. This document is retained only as an honest record. Do not fund.**

# Manifund project page — POSTED 2026-07-11

> **LIVE: https://manifund.org/projects/first-independent-test-of-the-casimir-cavity-vacuum-energy-claim**
> Posted from the operator's logged-in session (operator created the account/login; content
> filled and published per operator instruction). Settings as posted: min $2,000 / goal
> $18,500 / decision deadline 2026-08-21 / cause: Science & technology. Grant agreement SIGNED by the operator
> 2026-07-11. Remaining funding requirements are external: (2) reach the $2,000 minimum by
> 2026-08-21, (3) Manifund approval.

> Structure follows Manifund's project-creation prompts. Suggested settings:
> **Minimum funding: $2,000** (fab-run partial) · **Funding goal: $18,500** ·
> in-between milestones spend in the priority order under "How will this funding be used."
> Tone calibrated for the Manifund/ACX donor pool: explicit priors, pre-registration,
> published failure history.

---

## Title
**The first independent test of the "Casimir-cavity vacuum energy" claim — pre-registered, blinded, publishable in any outcome**

## Subtitle
A Physical Review Research paper has claimed for five years that tunnel junctions draw power
from the quantum vacuum. Zero independent tests exist. A startup just raised $12M on the
claim class. I've pre-registered the falsification study; I need the hardware.

## Project summary

In 2021, an NSF-funded group published in *Physical Review Research* (a respectable venue)
that metal-insulator-metal tunnel junctions faced with sub-micron "Casimir cavities" produce
tens of nanoamps at zero bias — energy from vacuum fluctuations, per the authors, with a
patent family and a companion paper citing 70 W/m². I ran an adversarially-reviewed prior-art
sweep: in five years there have been **zero independent replications** (positive, null, or
artifact-attributed), zero public raw datasets, and zero experimental critiques. The
specialist Casimir community's 75-year anniversary review doesn't mention it. Meanwhile a
company commercializing this device class closed a $12M oversubscribed seed round in May 2026.

Someone should just... test it. That's this project.

**My prior, stated for the record:** P(effect survives blinded, hydride-controlled,
decoy-controlled replication) ≈ **3%**. P(signal reproduces but resolves to a named mundane
artifact — most likely palladium-hydride chemistry or µV-scale parasitic EMFs) ≈ **55%**.
P(clean bounded null — effect doesn't reproduce at all in independently fabricated devices)
≈ **42%**. All three outcomes are pre-registered as publishable; the second and third are the
expected wins. If you think funding a study whose author expects the exciting hypothesis to
LOSE is strange, consider the alternative equilibrium: extraordinary claims that nobody tests
don't get falsified — they accumulate patents and venture rounds.

## What are this project's goals, and how will you achieve them?

**Goal: give a five-year-old extraordinary claim its first independent test, under conditions
that discriminate rather than merely repeat.** Three design choices do the discriminating:

1. **Matched Pd/Pt/Ni top electrodes in one fabrication run.** The published devices are
   palladium-on-alumina — the standard hydrogen-sensor configuration — and the original
   artifact checklist never tested the Pd–H pathway. If the "vacuum" signal tracks electrode
   hydrogen chemistry instead of cavity geometry, one split ends the story.
2. **Same-junction cavity-open/closed protocol** via a retractable mirror — the published
   comparisons are between *different* devices, where fabrication variability dominates.
3. **Interleaved decoy runs** (actuator driven at identical duty cycle, mirror mechanically
   decoupled) so an artifact that follows the *drive* rather than the *cavity* is caught
   automatically, in-campaign.

The analysis is already **frozen, before any device exists**: blinded run labels held apart
from the analyst, instrument constants cryptographically sealed before the blind draw, a
quantified seven-class artifact budget with a pre-registered 3σ criterion, and golden-vector
regression tests that make post-hoc changes to the arithmetic visible. Everything is public at **github.com/meanmod3/zpe-lab** — protocols, pipeline, benchmarks,
price-verified parts lists, and the full revision history. The pipeline survived
three rounds of adversarial review I commissioned against my own work — **round one BLOCKED
it** after demonstrating, with running code, that it could be fooled by an actuation-correlated
artifact and unblinded through a run-naming leak. The revision history preserves every attack
and every fix; I'll link the full record from this page. Before the contested device is ever
measured, the methodology must first reproduce a *known* answer (a thermal-rectification
calibration whose correct outcome is textbook physics), and the rig must pass a pre-registered
sub-microvolt EMF-floor qualification.

## How will this funding be used?

Priority order (partial funding buys the front of the list):
1. **$2,000 — device fabrication run** (mask set + wafers, 5 die types including the
   Pd/Pt/Ni splits; quotes in progress at RIT and Texas A&M — deliberately NOT the original
   institution's cleanroom).
2. **$2,500 — used electrometer + lock-in** (Keithley 617-class, SR510/830-class — the
   fA-scale measurement chain).
3. **$1,500 — calibration rig, shielding, piezo stage, thermometry, DAQ** (parts list is
   already price-verified line-by-line against live catalog data).
4. **$1,000 — consumables, wafers, calibration certificates.**
5. **$3,500 — second-site replication stage** for whatever survives (different building,
   different mains, same frozen pipeline).
6. Remainder: ~20% contingency on used-market volatility and fab requotes.

Minimum ($2,000) starts fabrication while other funding routes resolve. Full goal ($18,500)
funds the entire campaign through manuscript.

## Who is on your team? What's your track record?

Solo: an independent builder working outside any institution — which for this specific
project is the qualification, not the gap, since every existing positive result traces to one
group and the first test should come from hands with no stake in the answer. Track record of
the relevant kind: the project's own artifacts — the pre-registered protocols, the frozen
pipeline with its adversarial-review history (including the failures), the digitized
uncertainty-tagged benchmarks of the original papers' figures, and the prior-art verification
dossier — are all inspectable **before you fund**, which is the only track record that should
matter here. I am not a credentialed physicist; every measurement protocol is designed so
that its integrity is checkable by construction rather than by trust.

## What are the most likely causes and outcomes if this project fails?

Honest failure modes, ranked: (1) **fabrication risk** — the ~1.3 nm tunnel barrier is the
hardest ask; mitigated by facility staff-run processes and per-layer metrology, but a bad run
costs months and ~$2k; (2) **used-instrument risk** — a dud electrometer; mitigated by
tested-seller purchases and the known-answer calibration gate, which exists precisely to
catch a bad chain before it touches the contested device; (3) **inconclusive-data risk** —
the rig fails its own pre-registered sub-µV qualification and DUT results would be
uninterpretable; the pre-registration makes this VISIBLE (the run is invalid, not spun);
(4) **the boring failure** — I underestimate timeline as everyone does; the six-month plan
has explicit gates so slippage is public in the artifact record. "The effect turns out real"
is not a failure mode — it's the 3% branch and would be the most important result of the lot.

## What other funding are you or your project getting?

An Emergent Ventures application was submitted 2026-07-11 (decision typically ~1 week; this
page and that application are mutually disclosed). A staged Experiment.com campaign is
prepared as a parallel route. A raw-data request to the original authors is outstanding.
No other funding; no revenue; the deliverable is a publication and a reusable open
methodology for testing contested single-group claims.

---

> **Operator notes (not part of the page):**
> - Manifund requires an account to post — yours to create; paste sections into their form.
> - The probability triple (3/55/42) is my calibrated read of the program's promoted
>   artifacts; adjust if your own priors differ — they're YOUR public numbers once posted.
> - RESOLVED: public mirror live at https://github.com/meanmod3/zpe-lab (published
>   2026-07-11, history audited) — the page now links it directly.
> - Cross-link this page in the Experiment.com campaign and mention it if EV asks for
>   supporting material.
