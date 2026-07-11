# Device Parameter Sheet — Casimir/Optical-Cavity MIM Photoinjector

Sources (both fetched and read as full text, including supplement):
- **[PRR]** Moddel, Weerakkody, Doroski, Bartusiak, "Casimir-cavity-induced conductance changes," Phys. Rev. Research 3, L022007 (2021). doi:10.1103/PhysRevResearch.3.L022007. Full article text fetched from journals.aps.org (open access). **[PRR-SM]** = its Supplemental Material PDF (link.aps.org/supplemental/10.1103/PhysRevResearch.3.L022007), also fetched in full.
- **[SYM]** Moddel, Weerakkody, Doroski, Bartusiak, "Optical-Cavity-Induced Current," Symmetry 13(3), 517 (2021). doi:10.3390/sym13030517. Full text obtained from the arXiv mirror (arXiv:2101.03085), which is explicitly labeled on its own title page "Revised version: Published in Symmetry 22 March 2021" with the final Symmetry citation — i.e., this is represented as the published version's text, not the earlier preprint. I was not able to load the MDPI HTML page directly (403), so treat SYM table/figure OCR as authoritative for prose but double-check any number that looks like an OCR artifact against the prose sentences (flagged below).

Confidence note: all numbers below were read directly out of extracted PDF text (pdftotext -layout) of the actual papers, not from memory or secondary summaries. Table layouts (esp. SYM Table 1) suffered column-alignment loss in extraction — where a number's row/column mapping is ambiguous I say so explicitly rather than guess.

---

## A. Device geometry

### A1. Junction area
- GSM (germanium shadow-mask) devices: elliptical overlap, **0.02 x 0.006 mm2** (i.e. ~1.2x10-4 cm2 quoted as "0.02 x 0.006 μm2" in the PRR figure caption — this is very likely a typo for **μm2 units meant as the device's overlap in μm2**, but cross-checking against [PRR-SM] which independently states the Casimir-cavity area for GSM devices is **7 μm2**, and against [SYM] Table 1 listing area "0.02" (μm2) for GSM devices in Figs 4(a)/4(b)/6(a)/8/9/10/11 — the areas are in **μm2**, not mm2. [PRR] Fig. 2 caption / [SYM] Fig. 2 caption, Table 1.
- Photolithography (large-area) devices: square overlap area, range from **6.25 μm2 to 10,000 μm2** [PRR] Fig. 4 caption text ("areas of 6.25 to 10 000 μm2"); edge lengths "between 5 and 100 μm" [SYM] Fig. 3 caption. SYM Table 1 lists specific areas used per figure: **10,000 μm2** (Fig 5a), **625 μm2** (Fig 5b), **25–10,000 μm2** (Fig 6b), **0.02 x 16 μm2 [likely an array, i.e. 16 GSM-area devices]** (Fig 7b).
- Casimir-cavity lithographic pattern area for GSM devices: **7 μm2**, sized to overshadow/overlap the MIM junction [PRR-SM].

### A2. Electrode materials + thicknesses
- Upper electrode: **Pd (palladium)**.
  - GSM devices: nominal deposition thickness, but *effective* (angle-corrected) thickness **8.3 nm** [PRR] Fig. 3 caption, [PRR-SM] fabrication section ("11 nm of thermally evaporated Pd (1.3 Å/sec), angled at 39.3°... the thickness of Pd upper electrode is 8.3 nm" — i.e. 11 nm normal-incidence deposition becomes 8.3 nm effective due to the 39.3° angled evaporation).
  - Photolithography devices: Pd deposited **8.7 nm to 24 nm** (varied to test thickness dependence) [PRR-SM], [SYM] Table 1 ("8.7-24" nm, Fig 5a); also **15 nm** and **15.6 nm** used in specific figures (SYM Table 1, Figs 5b/6b/7b — column alignment uncertain, treat 15/15.6 nm as approximate for those specific sub-figures).
  - Deposition rate: 1.3 Å/sec (GSM) or 1.5 Å/sec (photolitho) [PRR-SM].
  - A monolayer (0.4 nm) of NR9 photoresist remains on photolitho devices under the Pd (not removed, to avoid further oxidizing the insulator) [PRR-SM], [SYM] §2.1.
- Base/lower electrode: **Ni (nickel)**.
  - GSM devices: **38 nm** effective thickness (50 nm nominal deposition at 39.3° angle, 1.5 Å/sec) [PRR] Fig. 3 caption, [PRR-SM].
  - Photolithography devices: **50 nm** (normal incidence, 2.7 Å/sec) [PRR-SM], [SYM] §2.1 ("50 nm for the photolithographic devices").
- No Al layer is used as an electrode — Al (150 nm) is used only as the **Casimir/optical-cavity mirror** (see A4).
- Substrate: thermally oxidized Si wafer with **300 nm SiO2** coating [PRR-SM] (both GSM base process uses 300 nm SiO2-coated wafer under a PMMA/Ge shadow-mask stack, and the large-area photolitho process starts on the same 300 nm SiO2/Si wafer).

### A3. Insulator material + thickness
- Composition: **native NiOx (grown on the Ni base electrode) + sputtered non-stoichiometric Al2O3**, treated as a single combined tunnel barrier ("effective insulator thickness" = NiOx + Al2O3).
- Al2O3: RF sputtered at 75 W, 30 sccm O2 + 20 sccm Ar, target thickness typically **1.3 nm** as deposited, but varied 0.7–2.3 nm across different figure datasets [PRR-SM]; [SYM] Table 1 lists Al2O3 values of 1.3, 0.9, 2.3, 0.7 nm depending on the specific figure/dataset.
- NiOx (native oxide, uncontrolled growth):
  - GSM devices: extracted **0.6–1 nm** via electrical simulation/Fowler-Nordheim fit (effective barrier height 0.06–0.08 eV) [PRR-SM].
  - Photolitho devices: measured directly by VASE: **2.3 nm** [PRR-SM], [SYM] §2.1 (thicker than GSM because of higher processing temperature and less protection from the Ge bridge).
- **Total effective insulator thickness** (combined NiOx+Al2O3), the quantity plotted on the x-axis of the "insulator thickness" scaling figures:
  - GSM PMMA-cavity reference devices: **2.3 nm** [PRR] Fig. 3 caption.
  - GSM SiO2-cavity reference devices: **1.9 nm** (thinner insulator) [PRR] Fig. 3 caption; also stated as **1.7 nm** for a PMMA-cavity comparison device in [PRR-SM] Fig. S6 caption ("PMMA transparent dielectric (36 nm) had an effective transport insulator of 1.7 nm... SiO2 transparent dielectric (50 nm) had an effective transport insulator of 1.9 nm").
  - Scaling-study range (x-axis of [PRR] Fig. 4(b) / [SYM] Fig. 5(b)): approximately **3.4–4.2 nm** effective insulator thickness.
  - General statement: total insulator is "<10 lattice constants thick" and thickness varies device-to-device even under nominally identical fabrication [PRR], [SYM] — this is called out explicitly as the dominant source of device-to-device resistance variation.
- Barrier heights (Fowler-Nordheim-derived): electrons **0.2 eV (NiOx)** and **0.3 eV (Al2O3)**; holes **3.2 eV (NiOx)** and **5.9 eV (Al2O3)** [PRR] main text (electrons dominate transport as a result) — consistent with [PRR-SM]'s more detailed Table 1 VASE-derived numbers (Al2O3 band gap 6.20 eV [PRR-SM Table 1 — note the paper's Table 1 columns appear misaligned in OCR; the Al2O3 "6.20 eV" band-gap figure may actually belong to a different row — treat with caution] and a directly stated 0.3 eV conduction-band offset / 5.9 eV valence-band offset for Pd/Al2O3 from Fowler-Nordheim analysis).

### A4. Casimir/optical cavity construction
- Structure: transparent dielectric spacer layer + **aluminum mirror**, deposited directly on top of the completed MIM stack (cavity is *external*, adjoining only the upper/Pd side of the MIM junction — asymmetric, one-sided).
- Spacer/transparent dielectric materials tested: **PMMA (polymethyl methacrylate)** and **SiO2** (both tested explicitly to rule out PMMA-specific artifacts; results were qualitatively similar for both — see C/D below).
  - PMMA: spin-coated, cured; refractive index at λ=300 nm ≈ **1.49 [SYM]** (also independently reported for a related PMMA layer as **1.52** in [SYM] §2.1's VASE sentence — note apparent inconsistency between the two PMMA refractive-index values quoted in the same section of [SYM]: "measured refractive indices for the spun-on PMMA and deposited SiO2 are 1.52 and 1.49" vs. [PRR-SM] Table 1 which lists PMMA n=1.49 at λ=300 nm and SiO2 n=1.72 at λ=300nm — the two papers' VASE tables do not agree with each other on exact PMMA/SiO2 index values; report both explicitly rather than pick one).
  - SiO2: RF sputtered, 50 W, 30 sccm O2 + 20 sccm Ar target [PRR-SM].
  - Thickness ranges tested: **30 nm to 1100 nm** for PMMA (GSM devices) [PRR-SM]; specific thicknesses called out in figures: **33 nm, 79 nm, 230 nm, 1100 nm** [PRR] Fig. 3(a)/[SYM] Fig. 4(a); scaling-curve x-axis spans roughly **30–1100 nm** [PRR] Fig. 3(b) / [SYM] Fig. 4(b).
  - SiO2 cavity thickness for large-area/photolitho devices: typically **12 nm** [PRR] Fig. 4 caption ("Casimir-cavity SiO2 thickness is 12 nm for all three sets" — i.e. for the electrode-thickness, insulator-thickness, and area scaling studies); also **50 nm** and **11 nm** and **35 nm** cited for other specific figure datasets [SYM] Table 1.
  - Mirror comparison: SiO2 cavity thicknesses of **33 nm to 79 nm** used for the leakage-resistance check [PRR] main text.
- Mirror material: **aluminum, 150 nm thick**, thermally evaporated at 6 Å/sec, used for essentially all devices [PRR-SM], [SYM] §2.1 ("The aluminum mirror is 150 nm thick for all devices").
  - Ag comparison: one explicit head-to-head test used **150 nm Ag + 3 nm Ti (adhesion layer)** mirror vs. 150 nm Al mirror, both on otherwise-identical devices (38 nm Ni / 1.9 nm NiO+Al2O3 / 8.3 nm Pd / 50 nm SiO2 cavity) [PRR-SM].
  - Devices with **no mirror** ("cavity dielectric but without mirror") were fabricated as a control and showed much lower G than devices with the mirror present [PRR-SM].
- Cutoff wavelength: for a 33 nm PMMA cavity with n≈1.5, the nominal Airy-function cavity cutoff is **~100 nm**, but because PMMA absorbance rises sharply below 250 nm, the *actual* effective cutoff is **>100 nm** [PRR] main text.

---

## B. Electrical measurements

### B1. Zero-bias / short-circuit currents (cavity vs. no-cavity)
- [SYM] is the paper reporting **absolute zero-bias (short-circuit) currents**, since PRR frames the same phenomenon primarily in terms of *differential conductance* change rather than absolute current at V=0.
- [SYM] Fig. 4(a): I(V) curves for a 0.02 μm2 GSM device at four cavity thicknesses (33, 79, 230, 1100 nm PMMA); short-circuit currents visually range roughly **20–100 nA** depending on cavity thickness (curve peaks ~100 nA at 33 nm cavity down toward lower values for the 1100 nm cavity) — read from Fig. 4(a) axis (current axis spans -25 to 125 nA); the paper does not give a single-number table, so treat these as approximate figure-read values, not exact tabulated numbers.
- [SYM] states explicitly: for the 33-nm-thick-cavity device, the **maximum output power is 1.4 pW** in the 0.02 μm2 active area, computed as |ISCVOC|/4 for the linear I-V region [SYM] §3.1. This is the paper's own reported power figure (see E below).
- [SYM] Fig. 8: as-built MIM (no cavity dielectric, no mirror) → "only a negligible current is produced"; after 180°C/15 min anneal (thermal-cycle control) → "again, no significant current was evident"; after depositing cavity dielectric alone (PMMA or SiO2, no mirror yet) → "no change in the current"; only after the **Al mirror is added** does current "jump" to the full-device values (~tens of nA, matching Fig. 4/6/7 scale) [SYM] §3.2.4. This is the key "cavity requires the mirror, not just the dielectric or processing" control.
- [SYM] Fig. 6(b): current vs. device area for photolitho devices spanning **0–10,000 μm2**, short-circuit current scaling roughly linearly up to **~50–60 nA** at the largest areas tested.
- [SYM] states devices are stable: after ~6 months, PMMA-cavity device output degraded **<10%**; SiO2-cavity device output degraded **<20%** [SYM] §3.2.4.

### B2. Differential conductance (G) values and cavity-induced conductance change
- [PRR] Fig. 3(a): explicit numeric example — for the SAME basic device geometry, a **33 nm PMMA cavity** device shows differential conductance G ≈ **1 mS**, vs. a **1100 nm PMMA cavity** device (i.e., effectively negligible-suppression/thick cavity, serving as the "no-cavity-like" reference) showing G ≈ **20 μS**. That is a **~50x (5000%) increase in G** going from thick (1100 nm) to thin (33 nm) cavity — this is the paper's headline cavity-induced conductance change, quoted directly in the Fig. 3 caption: "differential conductance values at 0 V and G of 1 mS and 20 μS."
- [PRR-SM] Fig. S6 / accompanying text: differential conductance is "significantly higher" for the completed device with mirror vs. (a) devices with no cavity at all and (b) devices with cavity dielectric but no mirror — qualitative comparison only, no separate numeric table extracted (values are in the figure, not the prose).
- [PRR-SM] direct numeric conductance comparison for a mirror-material control: **Al mirror → G = 3.1 ± 0.3 mS**; **Ag+Ti mirror → G = 3.2 ± 1.5 mS** (both on otherwise-identical 38 nm Ni / 1.9 nm NiO+Al2O3 / 8.3 nm Pd / 50 nm SiO2-cavity devices) — i.e. statistically indistinguishable conductance between Al and Ag mirrors despite Ag's UV reflectivity dropping below 450 nm, supporting the interpretation that short-wavelength (UV) modes are not the dominant contributor.
- [PRR] Fig. 3(b) plots G (mS) vs. cavity thickness on log-log axes from ~30 nm to ~1000 nm, for both PMMA and SiO2 cavity fillers — SiO2-filled cavities show systematically larger G than PMMA at the same thickness, attributed by the authors mainly to a slightly thinner insulator in those particular devices and to SiO2's greater near-UV transparency, not necessarily an intrinsic dielectric-type effect.
- [PRR] Fig. 4: differential-conductance-per-unit-area (G/area, units **μS/μm2**) plotted vs. (a) upper (Pd) electrode thickness (range ~8–24 nm, peak response near **~12 nm**), (b) effective insulator thickness (range ~3.4–4.2 nm, exponential falloff with increasing thickness), and (c) device area (range ~6.25–10,000 μm2, confirmed linear).

### B3. Resistance / resistance-area product
- [PRR] main text: leakage-check devices had cavity-dielectric thicknesses of **33–79 nm**; resistance THROUGH the transparent cavity dielectric was, in every case, **at least 106x (a factor of a million) greater** than resistance through the MIM junction itself — ruling out cavity-leakage as an explanation for the conductance change.
- [SYM] Fig. 9: quantitatively plots this same comparison — "Optical cavity transparent dielectric" resistance is shown on a log axis from **~10^7 Ω up to ~10^11 Ω** across cavity-dielectric thicknesses of 30–80 nm, versus "MIM structure" resistance which sits far lower (near the bottom of the same log-decade axis, ~10^1–10^3 Ω-ish based on the axis floor of 10^1 Ω) — exact MIM-structure resistance values were not separately tabulated in the extracted text; treat the MIM resistance band only as "several orders of magnitude below the dielectric leakage path," consistent with the ≥10^6x statement above.
- [PRR-SM] fabrication-verification section: reference (no-cavity) MIM control devices spanned **differential resistances of ~200 Ω** (used for the offset-current-precision check) up to a broader test set of **120 Ω to 6100 Ω** (item 4 of the four reference-device types used to validate the current-sourcing measurement technique).
- [PRR-SM]: a "low resistance (~100 Ω) device with nonlinear I-V characteristics" was used specifically for the Fowler-Nordheim barrier-height extraction.

### B4. I-V curve characteristics / barrier heights
- I-V characteristics are described as close to **linear** near zero bias (deliberately engineered via low barrier heights) — [SYM] §3.2.6 explicitly states the devices were "designed... to have low barrier heights and consequently linear I(V) characteristics."
- Barrier heights (both papers, consistent): electrons **0.2 eV (Pd/NiOx)**, **0.3 eV (Pd/Al2O3)**; holes **3.2 eV (Pd/NiOx)**, **5.9 eV (Pd/Al2O3)** — derived via Fowler-Nordheim analysis on a ~100 Ω low-resistance nonlinear reference device, cross-checked against VASE-measured band gaps.
- Anomalous DC offsets (zero-cavity-related electronic offset, NOT the cavity-induced current itself, but relevant as a measurement-precision benchmark): reference (no-cavity) MIM devices, after current-reversal correction, show **current offset <1 nA and voltage offset <1 μV** [PRR-SM] Fig. S4(a) text. By contrast, cavity-equipped devices show a persistent anomalous offset of order **~6 μV** in voltage [PRR-SM], and the current-offset trace in [PRR] Fig. 5 spans roughly **-20 nA to +120 nA** over a **-100 mV to +100 mV** voltage window for the 33 nm vs. 1100 nm cavity comparison devices (same devices as Fig. 3(a)).
- Uncorrected/pre-reversal-method offsets on reference (no-cavity) devices with ~200 Ω differential resistance: offset current **~60 nA**, offset voltage **~10 μV** [PRR-SM] — this establishes the noise floor / systematic-offset baseline that the current-reversal method removes.

---

## C. Scaling relations claimed (direction + rough magnitude)

| Parameter varied | Trend in signal (G or I) | Rough magnitude / range | Source |
|---|---|---|---|
| Casimir/optical cavity thickness ↓ | G (or short-circuit current) **increases** | G: ~20 μS (1100 nm) → ~1 mS (33 nm), i.e. ~50x over ~33x thickness change, roughly following a power-law-ish trend on log-log axes but explicitly **not** the naive cubic (1/d^3) dependence the authors initially expected from vacuum-energy-density scaling — attributed to multiple competing energy-dependent mechanisms | [PRR] Fig. 3(b); [SYM] Fig. 4(b), §4 |
| Upper (Pd) electrode thickness ↑ | G/area (or Isc) **peaks near ~10–12 nm** then falls off on both sides (rises from thin, peaks, then falls with further thickening) | Range tested 8–24 nm; peak at Pd absorption depth ≈10 nm for 0.4 μm light; falls off above that due to increased carrier scattering, falls off below ~10 nm due to reduced photon absorption | [PRR] Fig. 4(a); [SYM] Fig. 5(a), §3.1 |
| Effective insulator thickness ↑ | G/area (or Isc) **decreases exponentially** | Range tested ~3.4–4.2 nm; consistent with tunneling-dominated transport (Simmons formula), i.e. exponential falloff with insulator thickness | [PRR] Fig. 4(b), main text ("G would follow an exponential trend"); [SYM] Fig. 5(b), §3.1/§4 |
| Device area ↑ | G (or Isc) **increases linearly** | Range 6.25–10,000 μm2; explicitly confirmed linear, supporting a bulk/area-scaling photoinjection origin rather than an edge or circuit artifact | [PRR] Fig. 4(c); [SYM] Fig. 6(b) |
| Number of devices in series/parallel arrays | Voltage/current offsets scale **by the array factor (4x for a 4x4 array, i.e. 4 in series or 4 in parallel)** | Confirmed factor-of-4 scaling for both a "staggered" 4x4 array and a "series-parallel" 4x4 array | [PRR-SM] Fig. S4(b); [SYM] Fig. 7(b), §3.2.3 |

---

## D. Measurement setup

### D1. Instruments
- Source/measure unit: **Keithley 2612 source meter**, calibrated to NIST standards — used to source either voltage or current across two of the four probe pads.
- Voltage read-back: **HP 3478A digital multimeter (DMM)** — measured the voltage drop directly across the MIM junction (the other two of the four probe pads).
- Configuration: **four-point probe** to eliminate lead-resistance error.
- Precision quoted: voltage-sourcing mode has "applied bias ± 0.02% + 250 μV" offset (too imprecise for low-current work); current-sourcing mode is "applied current ± 0.06% + 100 pA" (used preferentially for low-resistance/low-current devices). Measurement precision stated elsewhere in [PRR-SM] as **1 μV and <1 nA** in voltage and current respectively.
- A **mercury switch** was used to short all four contact pads together during probe manipulation, to prevent electrostatic-discharge damage to the MIM junction.
- **Current-reversal method** (per Keithley/industry white papers cited) used throughout to null thermoelectric/systematic offsets: two opposite-polarity measurements (base grounded vs. upper electrode grounded) subtracted from each other.
- Thickness/optical-constant metrology: **Woollam M2000UI VASE** (variable-angle spectroscopic ellipsometry) tool at UC Santa Barbara, spectral range 0.7–6.4 eV (λ = 194–1700 nm), incidence angles 55°–75° in 10° steps; analysis via **CompleteEASE** software with a Cauchy-layer fit in the transparent region.
- Fabrication tools named: DUV stepper (UCSB NanoFabrication Facility) for GSM patterning; ICP-RIE etch system (CHF3/CF4/O2 at 0.5 Pa, 75 W ICP power, 75 W RF substrate bias, 135 s) for germanium etch; separate O2 RIE (100 W, 350 mTorr, 6 min) for PMMA strip; RF sputtering system for Al2O3/SiO2 deposition (75 W or 50 W respectively, 30 sccm O2 + 20 sccm Ar).

### D2. Shielding
- Ambient-radiation/EM-pickup test: measurements repeated in three environments — (i) open ambient lab conditions, (ii) inside a **mu-metal box** (blocks low-frequency EM fields), (iii) inside an **aluminum box** (blocks higher-frequency EM/RF) — all three gave statistically identical I-V characteristics [SYM] §3.2.6, Fig. 10 (axis range approximately ±5 μV, ±200 nA).
- Optical/light-leakage test: devices covered with a **blackout cloth (Thor Labs)** over the entire probe station; hundreds of I-V sweeps with and without ambient lighting showed no difference [PRR-SM].
- Magnetic-field check: the probe station's motorized translational stage produces a "significant" local magnetic field; measurements repeated on a different, non-motorized probe station showed identical offsets, ruling out that stage's magnetic field as the source [PRR-SM].

### D3. Temperature control
- All measurements at **room temperature**; stated stage temperature **21.6°C**, ambient **23.4°C** (baseline) in the thermal-artifact check [PRR-SM].
- Active thermal-gradient tests: heat gun raised stage temperature to **24.8°C** (ambient held constant) — no change in offset voltage over 20 min; ambient temperature raised independently — no change; ambient cooled to **21°C** via portable air conditioner — no change [PRR-SM].
- [SYM] Fig. 11 thermoelectric-effect test: measurement-stage temperature swept from roughly **22°C to 25°C** against a constant ambient of **23.4°C**; short-circuit current (~axis range 0–50 nA) and open-circuit voltage (~axis range 0–16 μV) both show **no significant variation** with the imposed stage/ambient temperature differential.
- Bulk Seebeck coefficients cited for context (not directly used to model the device, since layers are too thin for bulk values to apply reliably): Ni = **-18 μV/°C**, Pd = **-9 μV/°C**, insulator **>100 μV/°C** [PRR-SM]. A temperature differential of **<1°C** would in principle be sufficient to produce the observed ~6 μV offset if bulk coefficients applied — but the authors note thin-film coefficients can deviate substantially from bulk values, and the follow-up temperature-sweep experiments found no dependence, arguing against a simple thermoelectric origin.

### D4. Integration times / stability windows
- Long-duration current-vs-time stability check: continuous short-circuit current measurement over **4 hours**, no observed decay/change [SYM] Fig. 6(a); [PRR-SM] Fig. S5 shows the same style of test (current offset vs. time) "over a period of hours" with an explicit example device (38 nm Ni/1.7 nm Al2O3+NiOx/8.3 nm Pd/33 nm PMMA/150 nm Al) — no decay observed.
- Long-term (aging) stability: device output re-measured after **~6 months**; PMMA-cavity device degraded **<10%**, SiO2-cavity device degraded **<20%** [SYM] §3.2.4.
- No explicit per-point integration/dwell time (e.g., NPLC or averaging count) is given numerically in either paper's extracted text — this is a gap; if the simulation needs a concrete integration time, it is **not reported** in either paper and should not be assumed.

### D5. Artifact controls described (papers' own list)
[SYM] explicitly frames **eight types of artifact tests** (§3.2.1–3.2.8), each with a "negative" (i.e., artifact-ruled-out) result:
1. **Stability over time** (§3.2.1) — 4-hour continuous measurement, no decay (rules out transient/charging/hysteresis).
2. **Area dependence** (§3.2.2) — current scales linearly with active device area.
3. **Array dependence** (§3.2.3) — current/voltage scale with number of devices in parallel/series (factor of 4 for 4x4 arrays); rules out contact-level artifacts such as simple thermoelectric junction effects that wouldn't scale.
4. **Processing dependence** (§3.2.4) — staged fabrication check: as-built MIM (no current) → annealed MIM (no current) → + cavity dielectric only, no mirror (no current) → + Al mirror (current appears). Isolates the effect to "cavity + mirror," not general processing/thermal cycling.
5. **Current leakage through the cavity** (§3.2.5) — cavity-dielectric resistance measured and shown to be ≥10^6x higher than MIM-junction resistance (SYM Fig. 9; PRR main text, "33-79 nm" thickness range devices).
6. **Electromagnetic pickup** (§3.2.6) — three shielding environments (ambient / mu-metal box / aluminum box) give identical I-V; devices deliberately designed with low barrier heights → linear I-V to minimize rectification of any picked-up AC signal.
7. **Thermoelectric effects on electrodes (external/contact)** (§3.2.7) — current-reversal method + array-voltage-scaling argument (a contact-level thermoelectric offset would not scale with series device count, but the measured voltage does scale).
8. **Thermoelectric effects on devices (internal, stage-vs-ambient gradient)** (§3.2.8) — controlled stage-temperature sweep (22-25°C) against fixed ambient (23.4°C); no change in Isc or Voc (SYM Fig. 11).

[PRR-SM] additionally documents (largely the same tests, framed for the conductance-change / anomalous-offset phenomenon specifically): reference-device offset-current/voltage baselining (<1 nA, <1 μV after current-reversal correction on no-cavity MIM references with resistances 120-6100 Ω); the PMMA-vs-SiO2 cavity-dielectric comparison to rule out a PMMA-specific artifact; the "with vs. without mirror" comparison (Fig. S6); the Al-vs-Ag mirror comparison (rules out UV-specific reflectivity artifacts); VASE-based thickness/optical-constant characterization (Table 1) to validate the nominal vs. actual layer thicknesses used in all the scaling plots.

---

## E. Power/energy figures stated in these two papers themselves

- **[SYM] §3.1, explicit and the only quantitative absolute-power number in either paper**: "For the device with a 33 nm thick cavity, the maximum power is **1.4 pW** in a 0.02 μm2 area" — computed from the linear-I-V maximum-power formula P_max = |I_SC * V_OC| / 4.
  - Implied power density: 1.4 pW / 0.02 μm2 = **~7 x 10^7 pW/mm2 = ~70 W/m2** — this is a derived (not stated) figure; treat as a computed cross-check, not a value directly printed in the paper. (Calculation: 1.4e-12 W / 0.02e-12 m2 = 70 W/m2.)
- **[PRR]**, being framed around differential conductance rather than absolute output, does not state any absolute power or energy-output figure. Its only "energy" content is the qualitative/theoretical **ΔE·Δt uncertainty-principle-like relation**: for ΔE·Δt ≈ ℏ/2, hot electrons from a **1 eV** excitation would be available for **0.3 fs** [PRR] main text — this is an order-of-magnitude theoretical constraint the authors invoke to explain why only femtosecond-fast MIM transport times allow the effect to manifest, not a measured energy/power output of the device.
- **[SYM] §4** repeats the identical ΔE·Δt / 1 eV / 0.3 fs relation in its Discussion section, again as a theoretical framing device rather than a measured energy quantity.
- **Transport/transit-time figures** (relevant for time-constants in a simulation, not power but often paired with it): hot-carrier velocity in metal ≥ Fermi velocity **10^6 m/s**; metal transit time **<10 fs** for ~10 nm thickness; insulator ballistic transit time **~1 fs**; base-electrode inelastic scattering lifetime **≤10 fs** (i.e., **at most 10 fs**); combined hot-carrier transport+capture process **~10 fs** overall [PRR] and [SYM], both papers, near-identical wording.

---

## Open items / things NOT found in either paper's own text (do not assume/backfill)

- No explicit numeric NPLC / integration-time / averaging-count setting for the Keithley 2612 or HP 3478A.
- No single consolidated table of "current at V=0 for cavity vs. no-cavity, same device" — the closest is [SYM] Fig. 8 (qualitative bar/point comparison: negligible → negligible → negligible → jump) and [PRR] Fig. 3(a) (G = 1 mS at 33 nm cavity vs. 20 μS at 1100 nm cavity, which is a thin-vs-thick cavity comparison, not literally a cavity-vs-no-cavity comparison).
- Exact numeric resistance of the bare MIM structure in [SYM] Fig. 9 was not separately printed in text (only visible on the log-scale plot, whose exact intercept value did not survive PDF text extraction).
- SYM Table 1's Pd-thickness/area/material columns for Figs. 5(b), 6(b), 7(b), 8, 9, 10, 11 suffered pdftotext column misalignment; the values reported above for those rows should be treated as best-effort reconstructions from a garbled table and cross-checked against the source PDF's rendered table if exact per-figure values matter for the simulation.
- PMMA/SiO2 refractive index values are inconsistently reported between [SYM] §2.1 prose (PMMA 1.52, SiO2 1.49 at 300 nm) and [PRR-SM] Table 1 (PMMA 1.49, SiO2 1.72 at 300 nm) — likely a swap/typo somewhere in one of the two papers; do not silently pick one without flagging the discrepancy.
