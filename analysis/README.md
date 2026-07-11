# Run-data format (documents the FROZEN pipeline's expectations — rev 3, `bd81f70`)

This README documents what `pipeline.py` already enforces (pinned by tests + golden vectors).
It changes nothing; changing the format itself requires a new governed intent + PT.

## One RUN = one JSONL/JSON file: `data/runs/<run_id>.json`

```json
{
  "run_id": "run-000",
  "segments": [ {"lockin_I_A": 1.2e-12, "lockin_Q_A": -0.4e-12}, ... ],
  "artifacts": {
    "dT_K":            0.0004,   "// junction thermistor-pair differential, worst sustained",
    "decoupled_null_A": 2e-12,   "// per-run re-check: drive energized, mirror decoupled",
    "accel_rms_g":     0.0002,   "// 3-axis RMS over the run",
    "gnd_shift_V":     2e-7,     "// ground-permutation check result",
    "rf_v_V":          8e-6,     "// SDR in-band worst level at the junction",
    "r_j_check_ohm":   1010.0,   "// the run's own junction I-V check (cross-checked vs sealed session)",
    "cal_pre_ok": true, "cal_post_ok": true,
    "charge_C":        0.0015    "// integrated |I| dt for the run"
  }
}
```

Rules the pipeline enforces:
- **run_id MUST be an opaque serial `run-<digits>`**, assigned before the operator's blind
  draw. State-encoding ids are rejected outright.
- **NO cavity-state field anywhere in the data file.** Mirror position readback and piezo
  duty logs route to the operator-held label side.
- Segments are lock-in samples at f_mod (in-phase/quadrature, amps at the junction).
- Every artifact channel above is REQUIRED (QC bounds: dT<1 mK, decoupled null<10 pA,
  accel<1e-3 g RMS, gnd<0.5 µV, cal checks true).

## Operator-held files (provided only at unblinding, kept OUTSIDE the repo until then)
- `labels-<session>.json`: `{ "run-000": "closed" | "open" | "decoy", ... }`
- attestations: `{ "power_audit_accounted": true }` (an operator ATTESTATION, not a measurement)

## Sealed session record (committed BEFORE the blind draw)
Produced by `pipeline.seal_session({...})` over: `r_j_ohm` (device I-V), `f_mod_Hz`,
`q1_dummy_null_A` (Q1.3 record), `mech_phase_deg` (Q1 phase reference). The pipeline refuses
seal mismatches, refuses q1 values at/over bound, and cross-checks r_j against every run's
`r_j_check_ohm` (±20%).

## Q2 calibration runs
Q2 (known-answer exercise) uses the SAME file format so Q2.4 can process end-to-end:
lock-in fields carry the DC/averaged charge-accumulation readings per logging segment;
`decoupled_null_A` and `rf_v_V` may be recorded from the bench baseline; states in the label
file for Q2 are `heated` / `baseline` instead of cavity states (Q2 is not blinded — it is a
methodology rehearsal; stage A runs identically, stage B is not applied to Q2 data).
