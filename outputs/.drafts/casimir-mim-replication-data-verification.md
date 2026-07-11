# Verification Review: Casimir-MIM Replication Data Landscape Brief

**Reviewer:** Automated verification pass
**Date:** 2026-07-11
**Draft reviewed:** outputs/.drafts/casimir-mim-replication-data-draft.md
**Plan:** outputs/.plans/casimir-mim-replication-data.md

---

## Summary Verdict

The brief is **substantially sound** -- its core conclusion (no independent experimental replication exists) is well-supported by a multi-database search methodology and a complete citation-universe classification. However, several claims exceed what the cited evidence can strictly support, and the verified absence framing needs qualification. **No FATAL issues found. Three MAJOR, five MINOR.**

---

## Issues Found

### ISSUE 1 -- MAJOR: Verified absence overstates epistemic certainty

**Location:** Executive Summary, S1 header, S6 Recommendation
**Claim:** The verified absence of independent data is itself the actionable finding.
**Problem:** The search covers English-language databases (INSPIRE-HEP, Semantic Scholar, arXiv, IEEE, Google Scholar, APS). It does not cover:
- Chinese-language journals (CNKI/Wanfang) -- relevant given Jiang et al. (SJTU) work on cavity band-structure theory
- Russian-language Casimir physics literature (Klimchitskaya/Mostepanenko publish in both English and Russian)
- Japanese/Korean condensed-matter journals
- Industry-internal reports (e.g., from Casimir Inc. or Limitless Space Institute beyond patents)
- Unpublished negative results (selection bias)
- Conference proceedings databases (APS March Meeting abstracts, MRS, AVS) which could contain poster/talk abstracts

**Severity:** MAJOR -- the conclusion is probably correct but verified absence implies exhaustive coverage that was not achieved.

**Fix:** Reword to extensive search found no evidence and add a Limitations subsection listing unsearched domains. Change fully justifies to strongly supports.

---

### ISSUE 2 -- MAJOR: Moddel unpublished replication claim (JSE 2022) -- single-source, unverifiable

**Location:** S1 (Moddel own claim of external validation), S5, Open Questions #1
**Claim:** Moddel wrote multiple labs have tested our devices and reproduced what we measure.
**Problem:** This is cited from JSE 2022, a non-mainstream journal. The brief correctly flags the claim as unpublished but uses it as evidence in three separate sections without noting that:
1. The JSE quote itself has not been independently verified against the source text
2. Tested our devices vs. independently fabricated devices is a critical distinction raised only in Open Questions -- should be flagged at first mention
3. JSE editorial standards differ substantially from APS/Nature; claims published there carry less evidentiary weight

**Severity:** MAJOR -- a key claim about external validation is single-source from a low-impact-factor venue.

**Fix:** At first mention (S1), add caveat about JSE standards and the unspecified scope of tested.

---

### ISSUE 3 -- MAJOR: Ford 3-order-of-magnitude amplitude gap -- arithmetic not shown

**Location:** S4, Open Questions #4
**Claim:** The amplitude mismatch is ~3 orders of magnitude between prediction and observation.
**Problem:**
1. Where does the ~1e-3 eV effects figure come from? Not attributed to any source.
2. Ford paper may state the gap differently -- brief should quote Ford own language.
3. 6e-6 vs. 1e-3 is actually 2.2 orders of magnitude (~167x), not ~3 orders. Imprecision matters for a quantitative claim.

**Severity:** MAJOR -- key quantitative claim has no source attribution for one number and may contain arithmetic error.

**Fix:** Cite the source of the ~1e-3 eV figure or quote Ford verbatim. Correct the order-of-magnitude calculation.

---

### ISSUE 4 -- MINOR: Citation count ~14-20 is imprecise and unattributed

**Location:** Executive Summary
**Problem:** The citation table lists ~10 works but the summary claims ~14-20. Source database for this count is not stated.

**Fix:** State which database gives which count with retrieval date.

---

### ISSUE 5 -- MINOR: Bouche et al. affiliation uncertain

**Location:** S1, Consolidated Assessment table
**Problem:** Listed as Boston U? with question mark. Should be confirmed from the arXiv abstract.

**Fix:** Confirm affiliation and remove the question mark.

---

### ISSUE 6 -- MINOR: Dee identification speculative

**Location:** S3
**Problem:** The Doroski -> D. theory is unsupported speculation. Source of the name Dee is not identified.

**Fix:** State No person by this name found in Moddel group records. Origin of name unclear.

---

### ISSUE 7 -- MINOR: Missing caveat on Casimir community silence interpretation

**Location:** S4, Open Questions #2
**Problem:** Missing interpretation (d): the theoretical impossibility of net ZPE extraction is considered settled (cf. Jaffe 2005), making formal experimental engagement unnecessary from the community perspective.

**Fix:** Add this fourth interpretation.

---

### ISSUE 8 -- MINOR: Recommendation S6 confidence mismatch

**Location:** S6 Recommendation
**Problem:** Fully justifies is an overstatement. Absence of replication is necessary but not sufficient. Full justification also requires credible theoretical mechanism, feasibility, and cost-benefit analysis.

**Fix:** Reword to strongly supports the case for building hardware, provided the replication design addresses identified artifact pathways.

---

## Plan Acceptance Criteria Check

| Criterion | Status | Notes |
|---|---|---|
| All 6 questions answered | PASS | All six questions from the plan addressed |
| Each claimed replication cross-verified | PASS (vacuously) | No independent replications found |
| Dataset URLs directly checked | PARTIAL | Repositories searched but URL-level verification not confirmed for all |
| No single-source claims on critical findings | FAIL | Ford amplitude gap (Issue 3) and JSE claim (Issue 2) are single-source |
| Contradictions identified and addressed | PASS | Ford prediction-vs-observation and JSE tensions correctly noted |

---

## What is Correct

- **Citation universe classification (S1 table):** Comprehensive. Each citing work correctly classified.
- **Data repository search (S2):** Thorough with explicit negative results. Symmetry data availability statement directly quoted.
- **Thesis analysis (S3):** Careful group member tracking with thesis topics distinguished from Casimir-cavity work.
- **Artifact hypothesis table (S4):** Excellent. Pd-hydride as most credible untested artifact is well-reasoned and actionable.
- **Patent analysis (S6):** Thorough enumeration with correct identification that patent data = paper data.
- **Consolidated Assessment matrix:** Clear and honest.
- **Overall structure:** Answers the plan six questions systematically with evidence.

---

## Disposition

| Severity | Count | Action Required |
|---|---|---|
| FATAL | 0 | -- |
| MAJOR | 3 | Must fix before promoting to final |
| MINOR | 5 | Note in Open Questions or accept |

**Recommendation:** Fix the three MAJOR issues (reword verified absence, qualify JSE claim at first mention, source the Ford amplitude gap arithmetic), then promote to final. MINOR issues can be addressed in-brief or noted as limitations.