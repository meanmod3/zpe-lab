> **WITHDRAWN 2026-07-13 — fundraising closed; project archived, not an active pursuit. No funds were raised. This document is retained only as an honest record. Do not fund.**

# Emergent Ventures application — SUBMITTED 2026-07-11

> **STATUS: SUBMITTED** by the operator (form filled collaboratively in-browser; operator
> completed consents + CAPTCHA + Submit). EV states responses typically arrive within a
> week — check by ~2026-07-18; if silence stretches past ~3 weeks, a polite status inquiry
> to the EV team is acceptable. As-submitted deltas from this draft: restructured to EV's
> mandated 3-part format (personal story / consensus-view answer = the second law /
> the idea), 974 words; budget + itemized breakdown entered in the form's dedicated fields;
> tweet-length pitch (248 chars) led with the $12M-startup-zero-tests hook.

> DRAFT — submission is the operator's act (the EV form also asks short bio/contact
> questions only you can complete). Proposal below is ~1,050 words, inside the ~1,500 cap.
> Route: mercatus.org/emergent-ventures → application form. Ask: **$18,500**
> (minimum viable $8,000 — say so if the form invites flexibility).

---

## Proposal: The first independent test of a five-year-old "vacuum energy" claim — pre-registered, blinded, and publishable in any outcome

**This is a falsification-first replication, not a free-energy venture.** In 2021 an
NSF-funded group at CU Boulder published, in *Physical Review Research*, the claim that
metal-insulator-metal (MIM) tunnel junctions faced with sub-micron "Casimir cavities" produce
tens of nanoamps at zero bias, drawn from vacuum fluctuations — with a companion paper citing
70 W/m² practical power density and a granted patent family. Standard thermodynamics says
this should be impossible; my pre-registered expectation is that the effect will resolve to a
named measurement artifact. Either way, the field needs the answer, and after five years
nobody has produced it.

**The hole in the record is verified, not assumed.** I ran an adversarially-reviewed
prior-art sweep across the complete citation universe of both papers, thirteen data
repositories, thesis databases, and the patent record: **zero independent replications**
(positive, null, or artifact-attributed), zero public raw datasets, zero experimental
critiques. The only formal theoretical engagement — invited by the original author — concedes
the zero-bias current "does not seem to have a plausible explanation" in the proposed
framework. The authors' own supplemental material reports a persistent ~6 µV anomalous offset
they were "unable to eliminate," with the promised follow-up publication never appearing.
Meanwhile, the stakes stopped being academic: in May 2026 a startup commercializing this
device class closed a $12M oversubscribed seed round. Private capital is now deployed on a
claim no third party has ever tested.

**What I will do.** Fabricate the published device stack at an independent facility (quotes
in progress at RIT and Texas A&M — pointedly not at the original institution's cleanroom),
with three controls the original work never ran:

1. **Matched Pd/Pt/Ni top electrodes in a single fabrication run.** The published devices use
   palladium on alumina — literally the standard hydrogen-sensor configuration — and the
   original eight-artifact checklist never tested the Pd-hydride pathway. If the "vacuum"
   signal tracks the electrode's hydrogen chemistry instead of the cavity, that one split
   ends the story.
2. **A same-junction cavity-open/closed protocol** via a retractable mirror, eliminating the
   device-to-device variability that dominates the published between-device comparisons.
3. **Interleaved decoy runs** — the piezo actuator driven at identical duty cycle with the
   mirror mechanically decoupled — so any artifact that follows the *drive* rather than the
   *cavity* is caught in-campaign, automatically.

**Why believe my rigor rather than my intentions.** The entire analysis is already frozen —
before any device exists. Blinded run labels held apart from the analyst; instrument
constants cryptographically sealed before the blind draw; a quantified seven-class artifact
budget (thermoelectric, vibration, EMI, grounding, stored charge, calibration, hidden inputs)
with a pre-registered 3σ criterion; and golden-vector regression tests that make any
post-hoc change to the arithmetic visible. This pipeline survived three rounds of adversarial
review that I commissioned against my own work — the first round *blocked* it after
demonstrating, with running code, that it could be fooled by an actuation-correlated artifact
and unblinded through a naming convention; the published revision history shows every attack
and every fix. I also digitized every figure of the original papers into uncertainty-tagged
numerical benchmarks, so my results compare against the claim quantitatively, not
impressionistically. All of it is auditable today, before a dollar of fabrication money is
spent.

**Budget: $18,500** — fabrication run with the control splits ($1.5–3k, quotes pending),
used-market instrumentation (Keithley-class electrometer, lock-in, DMM: $1.2–2.7k), a
known-answer calibration rig I build and validate first ($250–400, price-verified),
shielding/piezo/thermometry/DAQ ($0.9–1.8k), consumables and calibration certificates, a
second-site replication stage for whatever survives, and ~20% contingency on used-market
volatility. A floor of $8,000 funds everything except the second-site stage.

**Timeline: six months** from fabrication order to manuscript. Months 0–1: fab order +
calibration-rig validation (my methodology must first reproduce a *known* answer — a
thermal-rectification exercise whose correct result is established physics — before touching
the contested device). Months 2–3: rig qualification against a pre-registered sub-microvolt
EMF floor; no device is measured until that gate passes. Months 3–5: the blinded campaign.
Months 5–6: unblinding against the frozen criterion and the manuscript.

**Outcomes.** Three, all pre-registered, all publishable: (a) the effect survives blinded,
decoy-controlled, hydride-controlled replication — extraordinary, and this protocol is the
credibility such a result would demand; (b) the signal resolves to a named mundane source —
the most likely outcome, the most useful to the field, and a template for how contested
claims should be closed; (c) a clean bounded null. A funded startup, a patent family, and a
five-year-old *Physical Review* claim will finally have their first independent test — and
the methodology (pre-registration, sealed instruments, decoy controls, adversarial review
with published failure history) is reusable for the growing class of contested single-group
claims in condensed-matter physics.

**Who I am.** An independent researcher working outside any institution — which for this
specific project is the qualification, not the gap: every existing positive result comes from
one group, and the first test must come from hands with nothing at stake in the answer. My
governance process, protocols, benchmarks, and the complete adversarial-review history are
available for inspection on request, as are the fabrication quotes as they arrive.

---

> **Operator notes (not part of the application):**
> - The EV form asks name/contact/short-bio questions — yours to fill; attach or link the
>   supporting-material list from `formal-request-core.md` if the form allows links.
> - The first sentence is deliberate fringe-risk inoculation per the landscape dossier —
>   keep it first.
> - If asked "what would you do with more money": the L2 second-site replication stage and
>   an ADA4530-1-class front-end upgrade are the honest next increments.
> - Parallel tracks per the landscape: Experiment.com staged campaign (fab run first) and a
>   Manifund public page — the Manifund page doubles as a citable public artifact here.
