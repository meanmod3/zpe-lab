# Fab-quote request package — C1 device wafers (intent 513)

Purpose: a spec a thin-film deposition service (or shared university facility) can quote
against. Stack replicates the photolithography-device family of PRR 3, L022007 (2021) +
Symmetry 13(3), 517 (2021); all layer values below are [extracted] from those papers'
fabrication sections (see casimir-device-parameters.md for figure-level provenance).
Zero spend authorized under intent 513 — this document is for quotes only.

## Substrate
- Si wafer, thermally oxidized, 300 nm SiO2.

## Die types requested (per wafer, mask set TBD with vendor)
1. **DUT, Pd top / SiO2 cavity:** Ni 50 nm (base, normal incidence) → native NiOx (uncontrolled,
   ~2.3 nm on photolitho process) + RF-sputtered AlOx 1.3 nm (75 W, 30 sccm O2 / 20 sccm Ar)
   → Pd top electrode 8.7–15 nm (split across wafer) → SiO2 spacer 12 nm and 50 nm splits
   (RF sputter 50 W, same gas mix) → Al mirror 150 nm (thermal evap, 6 Å/s).
   Areas: 25 / 625 / 10,000 µm² squares (area-scaling control on-die).
2. **No-mirror control:** identical through the SiO2 spacer, NO Al mirror (papers' §3.2.4
   staged-processing control).
3. **No-cavity control:** bare MIM (Ni/NiOx+AlOx/Pd), no spacer, no mirror.
4. **Ni-top-electrode variant:** as (1) with Ni replacing Pd top electrode — the hydride-free
   chemistry control from the promoted 511 budget row 5 (our addition; not in the papers).
4b. **Pt-top-electrode variant (added by intent 518):** as (1) with Pt replacing Pd, matched in
   the SAME fab run — the 518 data-existence review confirmed the Pd–H pathway is absent from
   Moddel's own artifact checklist (Al₂O₃/Pd = the standard H₂ sensor configuration); Pd-vs-Pt
   matched pairs are the most accessible hydride falsification test. Handling note for the
   measurement phase: H₂-free (glovebox/inert) storage and measurement environment recommended.
5. **Dummy-junction dies:** same pad geometry, insulator thick enough to be non-tunneling
   (≥10 nm AlOx) — the modulated-dummy control for budget rows 2b/3.

## Retractable-cavity note (our rig's key departure)
Die type (2) (no mirror) is ALSO the substrate for the rig's mechanically retractable external
mirror (piezo/flexure, ~µm travel): a discrete Al-mirrored flat positioned over the open cavity
face. The fixed-mirror die type (1) replicates the papers as-published; the retractable variant
enables the same-junction cavity-open/closed protocol. Vendor only supplies dies; the mirror
stage is rig-side (BOM item 5).

## Acceptance / QC
- VASE or profilometry thickness report per layer per wafer.
- Room-temp 4-point resistance sampling: expected junction band 120 Ω–6.1 kΩ at the
  625–10,000 µm² areas (per PRR-SM reference-device band); dies far outside band flagged.
- Target quote: full mask set + 1–2 wafers, $1.5–3k (511 envelope line 1).

## Supplementary fabrication references (added by intent 518)
Patents US11133758B2 / US11563388B2 / US12166434B2 (Moddel, Univ. of Colorado) carry MORE
fabrication detail than the journal papers (VASE tables, Fowler-Nordheim 0.06–0.08 eV effective
barriers, process variations across >1,000 devices / 21 batches) — hand these to the vendor
alongside this spec. Also flagged by 518 for the build intent's PT: sputter-deposition
stress / piezoelectric offsets in NiOx as a candidate thickness-dependent artifact (discuss
stress control / anneal options with the vendor).

## Known risks to discuss with vendor
- Native NiOx thickness is process-history-dependent (papers: 0.6–1 nm GSM vs 2.3 nm
  photolitho) — dominant source of device-to-device resistance spread; request minimal
  queue time between Ni deposition and AlOx sputter.
- Papers leave a 0.4 nm NR9 photoresist monolayer under Pd (not removed, to avoid further
  insulator oxidation) — vendor must either replicate or document the deviation.
