# Phase 2 shakedown — pre-committed regression criterion

**Version:** 1.0
**Committed:** 2026-10-03, before any planner, executor, or reviewer spawn for
this run. Any later change is a deviation, recorded in the run record with
its reason. It is not an edit to this file.
**Run:** `phase2-shakedown-2026-10` (`run-config.yaml`, this directory)

## Status of this run

This is a **pre-gate shakedown**, not the registered §8 regression gate
(Shawn, 2026-10-03). The preregistration (§8,
`protocol/phase-2-preregistration-draft.md`) defines that gate. It requires
"identical verdicts and identical value-level comparison results (prose
differences and build-iteration counts may drift; verdict or value changes
are failures)", and it includes a stochastic-path leg that regenerates the
Crema et al. tables from archived posteriors. Amendment 1 §3 orders the gate
after model selection, on the selected configuration with both lanes pinned.
This run applies the same criterion to herskind-riede-2024 and
dye-et-al-2023 as a rehearsal. A PASS here is evidence that the agentic
lane works. It does not discharge the registered gate.

## Baseline

The pilot's `attempt-01` artefacts for each paper (both verdicts
SUCCESSFUL):

- **herskind-riede-2024:** 291 n-gram rows (165 bigrams, 106 trigrams, 20
  quadrigrams) compared against the deposit's S3.xlsx, plus the
  frequency-distribution table, the per-period PMI (Pointwise Mutual
  Information) summary, and three structural figure checks. Value files are
  `attempt-01/outputs/{bigrams,trigrams,quadrigrams}.csv`.
- **dye-et-al-2023:** 54 Allen-algebra probability values compared against
  supplement Tables 2–10 and the stable-solid-branching section, plus the
  occurrence plot (72 interments) and the tempo plots (23 bead types). The
  value file is `attempt-01/outputs/summary-stats.txt`.

Neither paper's `attempt-01` directory holds an adversarial-review artefact
(file listings checked 2026-10-03). Review outcomes are therefore reported,
not compared.

## Criterion

For each paper, the operator applies these checks after the run, by script,
outside the blinded agents:

1. **Verdict identity.** The attempt-02 verdict in `comparison.json` equals
   the attempt-01 verdict.
2. **Value identity.** Every published value that attempt-01 compared is
   located in attempt-02's value-level evidence. Its reproduced value must
   equal attempt-01's reproduced value at the published precision, with the
   same match or mismatch outcome against the published value.
3. **No new unexplained discrepancies.** A target that attempt-02
   enumerates beyond attempt-01's scope does not fail the run. If such a
   target has a non-match outcome (MINOR_DISCREPANCY, MAJOR_DISCREPANCY,
   CANNOT_COMPARE, or PAPER_ERROR), it is a new finding and needs an
   explanation before the run is labelled.

## Input-version drift (herskind-riede-2024)

Attempt-01 used Zenodo version 1. Attempt-02 uses version 2, under rule
AP-12. The deposit files differ between versions: S1.xlsx is 442,501 bytes
in v1 and 442,983 in v2, and S3.xlsx is 31,384 in v1 and 31,598 in v2, by
Zenodo API checksums retrieved 2026-10-03. Before applying check 2, the
operator diffs v1 and v2 S1.xlsx and S3.xlsx cell by cell. An attempt-01 to
attempt-02 value difference that traces to a changed input cell is
**explained input drift**, not a harness failure. The verdict is governed by
the comparison against the published values in the paper and v2's S3.xlsx.

Dye has no input drift. The MCMC file at `tsdye.online/AP/beads-1.csv` was
byte-identical to the attempt-01 copy on 2026-10-03 (sha256
`02cf52d4ace408b6329e69e7a0e4bd457084ae9605f2fa5eccc2abad20ab9051`).

## Permitted drift

Prose, build-iteration counts, base-image and package versions (unless a
value changes), wrapper code style, file layout, and the number of targets
enumerated.

## Harness-integrity conditions (shakedown-specific)

- Every governed spawn's receipts re-validate post-run (`reproduction-lane.py
  audit-run`).
- Zero contaminating accesses to blinded paths (same audit).
- The deterministic artefact gate passes (`reproduction-lane.py
  check-attempt`), including a one-to-one match between the approved plan's
  locked target ids and `comparison.json`.

## Labels

| Label | Meaning |
|---|---|
| PASS | Checks 1–3 hold, with no drift beyond the permitted list |
| PASS-WITH-EXPLAINED-DRIFT | Checks 1 and 3 hold; every check-2 difference is explained input drift |
| FAIL | A verdict change, or an unexplained value change |
| INCONCLUSIVE | A harness-integrity condition failed, or the run did not complete, so the comparison cannot be made |

## Cost instrumentation (an early read for the Phase 3 cost gate)

Per paper and per agent: tokens (deduplicated per API request), API-equivalent
USD at the run-config prices, and wall-clock from transcript timestamps. Human
minutes (plan review, approval, escalations) are recorded by hand in the run
record.
