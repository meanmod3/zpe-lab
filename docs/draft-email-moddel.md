# DRAFT — raw-data request to Prof. Garret Moddel (intent 520)

> **STATUS: DRAFT ONLY. NOT SENT.** Sending is the operator's decision and action
> (outward-facing contact is never performed autonomously). Review, edit the sender
> identity/affiliation lines, and send from your own account if you choose to.
> To: moddel@colorado.edu
> Suggested subject: `Independent replication of your Casimir-cavity MIM results — raw data request`

---

Dear Prof. Moddel,

I am preparing an independent experimental replication of the Casimir-cavity MIM device
results your group reported in "Casimir-cavity-induced conductance changes" (Phys. Rev.
Research 3, L022007, 2021) and "Optical-Cavity-Induced Current" (Symmetry 13, 517, 2021).
These are extraordinary claims facing the well-known thermodynamic objection, and after five
years there is still no published independent replication — I would like to change that with
a fabrication-independent, blinded test, designed and pre-registered before any device is
measured. A null result or an artifact attribution would be published with the same care as
a confirmation.

The published figures are the only public form of your data (the Symmetry data-availability
statement notes all analyzed data is included in the article), and figure-reads limit how
precisely I can set quantitative expectations. Would you be willing to share the underlying
numerical data for the following, in any tabular format (CSV/XLSX/origin/matlab exports all
fine)?

**Specific datasets requested:**
1. **Symmetry Fig. 4(a)** — I(V) sweeps for the 0.02 µm² GSM device at the four PMMA cavity
   thicknesses (33/79/230/1100 nm), as voltage-current pairs.
2. **Symmetry Fig. 4(b)** — short-circuit current vs. cavity thickness, PMMA and SiO₂ series.
3. **Symmetry Figs. 5(a)/5(b)/6(b)** — I_sc vs. Pd thickness, vs. effective insulator
   thickness, and vs. device area (with per-device resistance if recorded).
4. **Symmetry Fig. 6(a)** — the 4-hour I_sc time series (raw sampling, not decimated, if
   available).
5. **Symmetry Figs. 10/11** — the three-shielding-environment I(V) comparison and the
   stage-temperature sweep (I_sc and V_oc vs. temperature).
6. **PRR Figs. 3(a)/3(b)/4(a–c)** — G(V) for the 33 nm and 1100 nm cavity devices and the
   G-vs-thickness/area scaling series, plus the Supplemental Material's reference-device
   offset data if it exists in numerical form.

**Per-device metadata that would make comparison meaningful (where recorded):**
- junction differential resistance at zero bias, device area, and batch/wafer identifier;
- effective insulator thickness for each plotted device (VASE or fit-derived, as used for the
  Fig. 4(b)/5(b) axes);
- measurement-instrument settings — in particular **integration time / NPLC and averaging
  counts** for the Keithley 2612 / HP 3478A chain, which the papers do not state;
- the current-reversal raw pairs (both polarities) rather than only the corrected values, if
  retained.

**Three specific questions, if you can spare the time:**
1. My reading of the PRR Supplemental Material is that cavity-equipped devices showed
   persistent anomalous voltage/current offsets (of order several µV in voltage) that your
   correction methods did not fully eliminate — please correct me if I have misread the SM.
   If that is right, is the underlying dataset (offset vs. time / device / configuration)
   available? For a low-impedance junction, microvolt-scale parasitic EMFs are exactly where
   my artifact budget concentrates, so this is the single most valuable dataset you could
   share.
2. Your JSE 2022 article mentions measurements near 80 K showing the effect does not
   diminish with temperature. Is that dataset shareable, even informally? It bears directly
   on thermoelectric exclusion.
3. The JSE article also mentions that other labs have tested your devices and reproduced the
   measurements. Were those independently *fabricated* devices or your devices measured
   elsewhere, and is any of that work headed for publication?

For transparency about my design, in return I am happy to share: my pre-registered analysis
protocol (blinded cavity-open/closed pairs on the same junction with a retractable mirror,
interleaved drive-on/mirror-decoupled control runs, and a quantitative artifact budget), and
one design note you may find useful or may wish to comment on: my review found the Pd–H
pathway absent from the artifact tests in the published papers, so my fabrication run includes
matched Pd/Pt/Ni top-electrode devices and H₂-controlled handling. If there is an unpublished
control on this point, I would much rather know now than rediscover it.

I will of course credit any shared data appropriately, keep it distinct from my own
measurements (shared data informs expectations; it cannot substitute for the independent
test), and send you the manuscript before submission regardless of the result's direction.

Thank you for considering this — and for publishing enough fabrication detail (papers +
patents) that an independent attempt is even possible.

Best regards,

[OPERATOR NAME]
[Affiliation / independent-researcher line — operator fills in]
[Contact details]

---

> **Operator notes (not part of the email):**
> - The email deliberately states the falsification-first framing plainly — Moddel knows the
>   skepticism landscape; pretending otherwise would read as bad faith.
> - **The "manuscript before submission" line is a REAL promise you make by sending** (PT-520
>   correction #4): standard collegial practice, but strike it if you don't want to carry it.
> - Q1's ~µV offset framing is deliberately hedged "my reading of the SM… correct me if I
>   have misread": our source is the full-text PRR-SM extraction
>   (docs/casimir-device-parameters.md §B4, ~6 µV) plus a search-verified quote ("unable to
>   eliminate the anomalous voltage and current offsets"), but the 513 PT's residual — eyeball
>   the PRR-SM PDF yourself before sending — still stands.
> - The three questions are ranked by value to us: (1) the 6 µV offset dataset >
>   (2) the 80 K data > (3) the unpublished-replications clarification.
> - If no reply in ~2 weeks, a polite single follow-up is normal academic practice; beyond
>   that, the figure-read benchmarks (benchmarks/benchmarks.json) are our fallback and the
>   program proceeds unchanged.
