# Arm sonnet-5 @ max — HALT report (2026-08-17)

**Status: HALTED at the per-arm boundary for operator adjudication.** Two
independent contract triggers fired: per-item reconcile failures above the
halt threshold (4 confirmed unusable items > 2, contract H3), and the spend
wire tripped (17.93M contract-metric tokens vs the 12M wire, contract H4 as
calibrated for this study). No stability figure is computed (no gates over
unusable items); no arm artefacts are assembled (assembly refuses
unreconciled spawns by design). Workflow run `wf_46738e9f-9a3`, launch commit
`a042c50`, 82 min wall-clock; all 28 scoring transcripts carry the
artefact-derived pin `effort: max` (Provenance line, retries included).

## Per-item ledger (authoritative whole-dir reconciliation, reconcile-run v1.4)

| Outcome | Items |
|---|---|
| Clean, reconciled payload | **11**: crema r1, crema r3, dye r1, herskind r1–r3, key r1, key r3, marwick r1–r3 |
| Completed, failed reconciliation | **3**: crema r2 (contaminating repo-root Glob), dye r3 (3 Globs of `**/references/...` skill files), key r2 (contract-schema: `status: OK` without `data_fair`/`code_fair`/`data_completeness`/`input_provenance`) |
| Never completed | **1**: dye r2 (both attempts died; terminal API error after retries) |

The per-item lane misfired in both directions and the authoritative pass is
the record: herskind r1's per-item "fail" was a transcript write-lag false
alarm (transcript reconciles clean), and dye r2's per-item verdict bound a
dead transcript.

## The dominant failure mode: 64K output cap × max-effort verbosity

The directory holds **28 scoring transcripts for 15 items — 13 dead
attempts** with no payload and no gate event. Mechanism: at `effort: max`,
sonnet-5's single-response emissions (thinking + the full structured payload)
exceed the harness per-response cap (`CLAUDE_CODE_MAX_OUTPUT_TOKENS`,
64,000); the API kills the response, the harness respawns fresh, and the
retry burns the full per-spawn context again. Three items took 3 attempts,
five took 2; dye r2 never survived (attempt 2 died at 257K accumulated output
tokens). Dead attempts consumed **4.25M tokens — 24% of arm spend**.

A secondary workflow defect surfaced: the v1.5 pipeline's stage-2 null guard
tests the wrapper object rather than the inner `result`, so dye r2's terminal
error was misreported as `missing: 0` and its reconcile stage ran against a
dead transcript. Defence in depth held (the item still failed reconciliation)
but the in-band counters are wrong; fix targeted at workflow v1.6 after
adjudication.

## Spend and the effort→cost measurand

| Metric | D3 sonnet @ xhigh (attested) | This arm @ max (pinned) |
|---|---|---|
| Contract-metric tokens | 6,216,252 | **17,930,795 (2.9×)** |
| — scoring attempts with payload | — | 11,757,636 |
| — dead attempts | — | 4,254,561 (24%) |
| — reconcile lane (haiku) | — | 1,918,598 |
| Output tokens, whole arm | 745,461 | per-spawn 33K–346K (completed spawns) |

Served-effort evidence (residual R1): completed spawns emitted 33K–346K
output tokens each vs a D3 arm-wide average near 50K, thinking blocks 4–11
vs the P3 low-probe's 1 — behaviourally unambiguous `max`, corroborating the
P3 channel verification (7.5× differential).

## Contamination failures (adjudication needed)

- **crema r2** (`ab4f70a2d`): Glob rooted at `~/Code/llm-reproducibility` —
  an unscoped listing over the whole repository, capable of surfacing
  `studies/`/`outputs/` paths. Closest precedent: F-002 (fable session-dir
  Glob, D3), ruled a violation with contract-mandated re-run.
- **dye r3** (`ab558a6d5`): three Globs targeting
  `**/references/checklists/expected-information.md`,
  `**/references/infrastructure/credit-taxonomy.md`,
  `**/references/infrastructure/pid-systems-guide.md`. The resolved targets
  are research-assessor skill references — reads of those *paths* are on the
  reconciler's allowed-prefix list, but the recorded Glob *patterns* are
  unanchored and fail prefix matching. Genuine adjudication fork: boundary
  violation (unscoped patterns can match anywhere) vs verifier
  pattern-vs-path gap (reconcile v1.5 candidate). Note both incidents are
  max-effort exploration behaviour absent from the 15/15-clean xhigh arm.

## Draft failure-register entries (lodged only on adjudication)

1. Effort=max drives single-response emissions past the 64K harness cap →
   dead-attempt retry loops; 13 dead transcripts, 1 item unrecoverable
   (harness-constraint × model-behaviour).
2. Workflow v1.5 stage-2 null guard tests the wrapper, not the result —
   `missing` under-counts terminal agent errors (harness/verifier class).
3. crema r2 repo-root Glob; dye r3 unscoped reference Globs (boundary, or
   partially verifier pattern-vs-path — split pending ruling).
4. key r2 `status: OK` without scoring blocks — the S4-retreat-anticipated
   class, caught by the C9 contract-schema layer exactly as designed
   (model failure, harness working).

## Options at the hard stop

- **A. Remediate and complete the arm**: raise the spawn-side output cap
  (env `CLAUDE_CODE_MAX_OUTPUT_TOKENS`), declared re-run of the 4 unusable
  items (~2–3M additional tokens on top of 17.9M; needs explicit wire
  authorisation — the remediation-scaled exemption is arguable since a
  stuck-loop indicator was present in the retry churn).
- **B. Hold sonnet@max as-is**: the arm already yields the study's central
  empirical findings (2.9× cost; harness-compliance degradation at max);
  decide opus@max separately — opus's D3 output volume was ~40% lower than
  sonnet's, so it may clear the 64K cap without loops, but launching it
  unchanged risks the same churn.
- **C. Close the max leg**: record findings, no further max spend; selection
  economics note — sonnet@max at ~18M/arm erodes the "cheapest arm"
  rationale that motivated the study.

No option is executed without the operator's ruling.
