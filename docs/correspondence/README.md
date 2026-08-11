# Correspondence status — outbound drafts + technical learnings

This directory holds OUR outbound reply drafts. Inbound private emails are not reproduced
here out of courtesy to correspondents; only the technical facts and program decisions that
follow from them are recorded, since those are material to the (public) methodology.

## Status (2026-07-13)

**AggieFab (Texas A&M) — replied, engaged.** Technical facts learned that shape the plan:
- RF-sputtered Al2O3 deposits at ~1 nm/min on their Lesker tools; a ~1.3 nm barrier is near
  the edge of controllable at that rate; AFM is the thickness-verification path.
- They stock **Ni sputter targets only**; **no Pd or Pt sputter targets**. Pt is available as
  e-beam pellets for limited staff runs. **Pd availability is the open blocker** — the primary
  electrode and the hydride control both need Pd. Reply asks whether we can supply Pd source
  material for a staff run.
- Staff-run is available, but an unaffiliated researcher is an **external corporate customer**
  (higher rate tier). Reply requests the actual corporate quote — this likely lifts the
  fab-run cost above the academic-rate estimate and may reshape the budget / the Experiment.com
  $2,400 goal.
- Practical asks answered in the draft: we provide Si+300nm-SiO2 wafers; ~100 mm; GDSII/DXF to
  be produced for the Heidelberg MLA (simple geometry). RRID acknowledgement agreed.
- Draft reply: `reply-aggiefab-DRAFT.md` (operator sends).

**Prof. Moddel (original author) — replied, willing to help.** Raised a genuine
methodological point (thin-film / interface materials-sensitivity) with a proposed sequencing
that the program CANNOT adopt as stated: developing the fabrication until the anomalous signal
appears and only then registering. That is tune-then-register, which manufactures false
positives and would forfeit the program's entire falsification value. **Program decision
(recommend governing as a zpe-lab intent + pressure-test):** adopt a two-phase split —
  - Phase A: fabrication development qualified against the PUBLISHED MUNDANE device baselines
    (resistance band, linear low-bias I-V, Fowler-Nordheim barrier heights, layer thicknesses)
    — no reference to the anomalous current, so it cannot bias the test;
  - Phase B: the existing FROZEN blinded cavity-open/closed test, on Phase-A-qualified devices.
  The reply asks Moddel for the SPECIFIC deposition parameters he considers necessary (if
  specifiable, we pre-register exactly those; if the only recipe is "iterate until you see the
  effect," that is itself a reproducibility finding). Draft reply: `reply-moddel-DRAFT.md`
  (operator sends; recommend the governed intent lands first so the reasoning is on record).

**RIT SMFL — no reply yet** (sent 2026-07-11).

## The affiliation/cost issue (cross-cutting)
"External corporate" pricing at university facilities (flagged in `../vendor-shortlist.md`,
now concrete at AggieFab) threatens the fab-run budget across the whole shortlist. Open
decision for the operator: accept corporate rates and size the funding asks accordingly, OR
pursue a legitimate academic-affiliation / fiscal-sponsorship route. Interacts with the
funding effort (EV / Manifund / Experiment.com $2,400 fab-run goal may need revising upward).


## WIND-DOWN (2026-07-13)
Project not proceeding to a physical experiment (AI-assisted design exercise; not carried into real fabrication). Honest wind-down notes to Malhotra, Moddel, and Emergent Ventures are in `winddown-emails.md` (operator sends). The earlier continue-path reply drafts are marked SUPERSEDED. Manifund page being hidden; Experiment.com never launched; no funds raised anywhere.
