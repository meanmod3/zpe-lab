# Blinded measurement protocol — DUT phase (intent 515)

Implements the promoted 511 falsification criterion with the 513 §2 scope
reconciliation. The analysis pipeline (`analysis/pipeline.py`) is FROZEN before any
data exists; this protocol defines how data reaches it without the analyst being able
to tune on labels.

## Run structure
- One RUN = one contiguous logging session at one state, fixed f_mod, fixed device.
  THREE states (rev 2, PT-515): **CLOSED** (mirror engaged at design gap), **OPEN**
  (mirror retracted), **DECOY** (piezo drive energized with a duty cycle identical to
  CLOSED, mirror MECHANICALLY DECOUPLED — the actuation-artifact control).
- A PAIR = consecutive CLOSED/OPEN runs on the SAME junction, same session, order
  alternated between pairs (ABBA sequencing).
- Minimum evidence unit (pre-registered): **≥3 valid blinded pairs AND ≥2 decoy runs
  interleaved through the campaign** (not clustered at the ends).
- Every run logs: thermistor pair (mK), 3-axis accelerometer, SDR in-band level,
  integrated charge counter, enclosure power meters, calibration pre/post checks,
  per-run decoupled-drive null re-check.

## Blinding mechanics (metric #5: unblinding must be structurally awkward)
1. **Run ids are opaque sequential serials (`run-000`, `run-001`, …) assigned BEFORE
   the operator's blind state draw. Encoding state in run ids, filenames, or any data
   field is FORBIDDEN** — the pipeline rejects non-serial ids outright (PT-515
   demonstrated an 8/8 unblinding attack through a state-suffixed naming convention).
2. The OPERATOR draws the state sequence privately and records run_id → state
   (closed/open/decoy) in `labels-<session>.json`, kept OUTSIDE the repo.
3. Data files (`data/runs/<run_id>.jsonl`) contain NO state field. Mirror position
   readback and piezo duty-cycle logs route to the label file side, not the data file.
4. `analysis/pipeline.py` stage A consumes data ONLY and emits per-run statistics —
   it cannot compute a verdict without labels.
5. Only after per-run stats are committed does the operator provide the label file;
   stage B joins labels and evaluates the pre-registered criterion. Committing stats
   BEFORE the join is the audit trail that analysis wasn't label-tuned.

## Verdict criterion (frozen, rev 2; implements promoted 513 §2 + PT-515 corrections)
For the paired differential (CLOSED − OPEN) across ≥3 valid pairs:
- **Signal test:** |mean differential| > 3 × RSS(rows 1,2,3,4,6 as current-equivalents).
  Floor provenance is structural: rows 1/3/4 use the MAXIMA of the campaign's own
  per-run measured channels (dT, RF level, ground shift); row 2 uses the larger of the
  per-run decoupled nulls and the Q1.3 dummy record (cross-checked against its bound —
  an unqualified rig makes the pipeline refuse to compute a floor); row 6 = 1% of the
  quantity under test. No hand-supplied floor inputs exist.
- **Phase test:** every amplitude-qualified CLOSED run (amp > 3×SEM and > floor) within
  ±30° of the Q1 measured mechanical phase reference.
- **DECOY test:** |mean(DECOY) − mean(OPEN)| < 1 × RSS floor. A differential that
  follows the piezo DRIVE (appears in decoys, mirror decoupled) is an
  actuation-correlated mundane artifact → verdict ACTUATION-ARTIFACT (telos outcome-2
  candidate), NEVER a cavity attribution. A real cavity effect follows the MIRROR and
  cannot appear in decoys.
- **Row-5 gate:** cumulative ∫|I|dt > 10 mC AND signal undiminished (last CLOSED run
  ≥ 50% of the first — a decaying signal is a depleting-source signature, not L1).
- **Row-7 gate:** all metered inputs accounted; report carries the L3 caveat verbatim.
- **QC validity:** a run is INVALID (excluded before unblinding, logged with reason) if
  any artifact channel exceeds its Q1-baseline bound; exclusions after unblinding are
  forbidden.

**Known residual limitation (stated, not hidden):** an artifact correlated with the
MIRROR's mechanical engagement itself (not the drive) — e.g. contact between mirror
assembly and DUT mount — is not separable by the decoy test; it is excluded
mechanically (no-contact verification at Q1) and by the L2 campaign (H-loading,
Ni-variant, second site), not by this pipeline.

## Outcome ladder (no level-skipping; from promoted 511)
- Criterion met → L1 established (anomaly exists) → proceed to L2 artifact-exclusion
  campaign (H-loading, Ni-variant, second site). NOT a success claim.
- Criterion not met → the design-point is falsified for the tested space → document and
  either widen the tested space (new intent) or close per telos outcome 3.
- Any anomaly attributed to a mundane source → telos outcome 2 → name it, document it.
