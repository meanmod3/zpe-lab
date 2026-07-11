# Fabrication-Route Shortlist — C1 Device Wafers (intent 522)

**Research only — nothing was contacted, no forms submitted, no accounts created.** All info
from public websites/rate pages as of 2026-07-11. Facilities without public rate cards are
marked quote-only. This is a shortlist for the **operator** to contact directly.

Source spec: `docs/fab-quote-package.md` — Ni 50nm / native NiOx / RF-sputtered AlOx ~1.3nm /
{Pd, Pt, Ni} top electrode 8.7–15nm / SiO2 spacer 12+50nm split / Al mirror 150nm; 5 die
types; 5–100µm photolitho; VASE/profilometry QC; target $1.5–3k for mask set + 1–2 wafers.

## Tier 1 — best fit (published rates or clear staff-run path, full stack capable)

1. **RIT SMFL (Rochester)** — full in-house flow (photolitho, sputter, e-beam/flash evap,
   RIE, dicing). Published tiers: $75–190/hr by tool class; **Dedicated Staff Support
   $95/hr (staff runs the job)**; masks $350–650. Route: Lab Ops Manager via
   rit.edu/nanofab/external-customers. Independence: clean. Best match to "vendor quotes
   and runs it"; $1.5–3k plausible staff-run.
2. **AggieFab, Texas A&M** — Lesker sputter (RF Al2O3/SiO2 explicitly listed — covers our
   AlOx + spacer), EVG610 aligner, **Heidelberg MLA150 maskless litho** (avoids hard-mask
   cost for a 5-die set). Published external rates: outside-academic 1.5×TAMU (sputter/evap
   $52.50–75/hr; MLA150 $97.50/hr). Route: aggiefab.tamu.edu/become-a-user. Clean. Most
   transparent rate card found — good ROM basis.
3. **Cornell CNF (NNCI flagship)** — three AJA multi-gun DC+RF load-locked sputter systems
   (ideal for the multi-material stack + thin AlOx control), deepest process maturity.
   Rates behind NEMO login (industry "set to match commercial"). Route:
   userprogram@cnf.cornell.edu. Clean. Budget fit unverified — worth a quote regardless.

## Tier 2 — strong fit, rates partial or contact-required

4. **COSINC, CU Boulder** ⚠️ **INDEPENDENCE FLAG: Moddel's own institution's shared
   cleanroom.** Full capability + real staff-run path (Assistance $47–118/hr; External
   Industry 2.5× CU rate). Listed for cost comparison ONLY — using it would undercut the
   replication's independence; avoid or disclose prominently.
5. **Harvard CNS (NNCI)** — 50+ materials PVD + full photolitho; Non-Harvard Academic =
   +45%; "Incubator" tier for non-affiliated users; pull the current rate PDF directly
   (cns1.rc.fas.harvard.edu). Clean.
6. **ASU NanoFab (NNCI)** — Lesker sputters + MLA-150 maskless + in-house
   Filmetrics/Zygo QC; internal $52.50/hr published, external rates by contact
   (nanofab@asu.edu). Clean.
7. **Georgia Tech IEN (NNCI)** — full shared cleanroom; live rate page unreachable during
   this survey; external users via billyde.brown@gatech.edu. Clean.
8. **Michigan LNF (NNCI)** — sputter + evap + photolitho; 2026 fee schedule exists but
   403'd to our tools (retry as a human); PO/credit-card invoicing. Clean.
9. **Minnesota Nano Center (NNCI)** — sputter explicitly lists Al, Pt, Ti; full photolitho;
   rates by contact (mnc@umn.edu). Clean.
10. **Brown NCF** — deposition + litho + explicit staff-run option; rates by contact. Clean.

## Tier 3 — commercial deposition-only (partial-stack; pair with a litho house)

11. **Platypus Technologies (WI)** — rare commercial shop with BOTH metal deposition AND
    photolitho in-house (Class-1000); oxide/AlOx sputter capability unconfirmed — ask.
    Quote-only. Clean.
12. **University Wafer service network** — sputter + e-beam evap of metals/oxides on
    customer wafers; no photolitho advertised; fallback for blanket-deposition control/dummy
    dies. Quote via order.universitywafer.com. Clean.
13. **PVD Products (MA)** — custom DC/RF sputter incl. combinatorial multi-pad (useful for
    split-thickness dies); takes small R&D jobs; no litho. contact@pvdproducts.com. Clean.
14. **Substrata (Ontario, Canada — non-US, flagged)** — reactive sputter + patterned
    coatings; 24-h response claim; sub-2nm oxide capability unconfirmed.
15. **DRLI (optical coatings)** — weak fit; no litho/MIM evidence; deprioritize.
16. **Thin Film Devices Inc.** — display/TCO production orientation; unlikely fit.

## Category C — MPW/broker programs: none fit
MEMSCAP MUMPs / Science Wafer Services = fixed polysilicon surface-micromachining flows
(wrong material system; 2µm min features irrelevant to our need); CMOS shuttle brokers
inapplicable. University shared facilities ARE the closest MPW-analog for this job.

## Cross-cutting notes for the operator
- **Hardest technical ask = the ~1.3nm AlOx tunnel barrier + Pd/Pt/Ni triple-electrode split
  in ONE run.** No public materials confirm sub-2nm RF-oxide control explicitly — raise it as
  a direct question in every quote request; QCM-controlled sputter at this facility class
  should manage it, but confirm, never assume.
- **Budget:** RIT + AggieFab published rates suggest $1.5–3k is achievable ONLY staff-run
  (not self-use-trained), and **maskless litho (AggieFab/ASU MLA-150) can erase the
  $350–650/mask hard-mask line entirely** for our small 5-die set.
- **Independence default:** any Tier 1/2 candidate EXCEPT COSINC.
- Ask each candidate whether the per-layer VASE/profilometry QC report can be delivered in
  the same engagement (ASU has in-house metrology; most NNCI sites run ellipsometry as
  standard).
