# Blinded measurement protocol — DUT phase (intent 515)

Implements the promoted 511 falsification criterion with the 513 §2 scope
reconciliation. The analysis pipeline (`analysis/pipeline.py`) is FROZEN before any
data exists; this protocol defines how data reaches it without the analyst being able
to tune on labels.

## Run structure
- One RUN = one contiguous logging session at one cavity state (CLOSED = mirror engaged
  at design gap; OPEN = mirror retracted), fixed f_mod, fixed device.
- A PAIR = consecutive CLOSED/OPEN runs on the SAME junction, same session, order
  alternated between pairs (ABBA sequencing).
- Minimum evidence unit (pre-registered, 511): **≥3 valid blinded pairs**.
- Every run also logs: thermistor pair (mK), 3-axis accelerometer, SDR event log,
  integrated charge counter, enclosure power meters, calibration pre/post checks,
  mirror-decoupled crosstalk check (once per session).

## Blinding mechanics (metric #5: unblinding must be structurally awkward)
1. The OPERATOR sets the cavity state per a private random sequence and records
   run_id → state in `labels-<session>.json`, kept OUTSIDE the repo (password manager,
   sealed note — anywhere the analyst does not see).
2. Data files (`data/runs/<run_id>.jsonl`) contain NO cavity-state field. The mirror
   position readback channel is routed to the label file, not the data file.
3. `analysis/pipeline.py` stage A consumes data ONLY and emits per-run statistics
   (`per-run-stats.json`) — it cannot compute a verdict without labels.
4. Only after per-run stats are committed does the operator provide the label file;
   stage B joins labels and evaluates the pre-registered criterion. Committing stats
   BEFORE the join is the audit trail that analysis wasn't label-tuned.

## Verdict criterion (frozen; matches promoted 513 §2 exactly)
For the paired differential (CLOSED − OPEN) across ≥3 valid pairs:
- **Signal test:** |mean differential| > 3 × RSS(rows 1,2,3,4,6 as current-equivalents,
  computed from the SAME session's measured artifact channels via the sim calculators).
- **Phase test:** differential appears in the lock-in in-phase component consistent with
  mechanical modulation (mirror-decoupled control null).
- **Row-5 gate:** cumulative ∫|I|dt across the campaign > 10 mC with signal undiminished.
- **Row-7 gate:** all metered inputs accounted; report carries the L3 caveat verbatim.
- **QC validity:** a run is INVALID (excluded before unblinding, logged with reason) if
  any artifact channel exceeds its Q1-baseline bound; exclusions after unblinding are
  forbidden.

## Outcome ladder (no level-skipping; from promoted 511)
- Criterion met → L1 established (anomaly exists) → proceed to L2 artifact-exclusion
  campaign (H-loading, Ni-variant, second site). NOT a success claim.
- Criterion not met → the design-point is falsified for the tested space → document and
  either widen the tested space (new intent) or close per telos outcome 3.
- Any anomaly attributed to a mundane source → telos outcome 2 → name it, document it.
