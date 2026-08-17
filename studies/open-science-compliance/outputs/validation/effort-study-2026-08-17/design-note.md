# Effort study — design note (2026-08-17)

**Status:** rulings captured, awaiting the standing API gate GO.
**Operator rulings:** Shawn, 2026-08-17 (delta pre-run review Q1–Q7).
**Plan of record:** `wiki/planning/instrument-clarification-plan.md` (decision log,
2026-08-17 effort-study entry).

## Purpose

Exploratory instrument-development study, not a registered gate re-run. Two
questions:

1. **Stability under pinned effort.** Does reasoning effort pinned at `max`
   lift arm stability — especially sonnet-5, the cheapest arm, which sits at
   0.853 against the registered ≥ 0.90 stability gate (amendment 2 §4) under
   the D3 cycle's session-inherited, attestation-only `xhigh`?
2. **Effort→cost, measured.** Higher thinking effort is presumed more
   expensive (more thinking tokens), but that must be demonstrated empirically
   (operator rider, 2026-08-17). Per-arm token telemetry against the D3
   baselines is a first-class study output, not a side effect.

## Design

Same benchmark harness and design as D3: `fair-benchmark-arm.workflow.js`
(v1.5, effort pinning), 5 pilot papers × 3 runs = 15 scoring spawns + 15
per-item reconcile spawns per arm. Arms sequential with per-arm hard stop:

1. `sonnet-5` @ `max` (prioritised — selection economics). **Halted
   2026-08-17** (4/15 items unusable, wire tripped — see
   `arm-sonnet-5-max/halt-report-2026-08-17.md`); operator ruled
   completion: output cap raised to 128K, 4 items re-run (workflow v1.6).
2. `sonnet-5` @ `high` — **added by operator ruling 2026-08-17**, runs
   after the max arm completes, pinning the other end of the effort
   spectrum.
3. `opus-5` @ `max` — **OFF unless the opus xhigh run shows deficiencies**
   (operator ruling 2026-08-17, superseding the original arm-2 plan).

## Arm identity and provenance (Q1, Q2)

- Output home: `studies/open-science-compliance/outputs/validation/effort-study-2026-08-17/`
- **Effort is part of arm identity from this study onward**: arm directories
  are `arm-sonnet-5-max/`, `arm-opus-5-max/`. If a pinned-effort arm is
  selected at D4, the effort pin enters the registered arm-choice record.
- Args are built **fresh per arm at launch** by
  `scripts/build-benchmark-args.py <arm> --effort max` (v1.2): the embedded
  `launch_commit` is HEAD at build time, and the launcher refuses a tree with
  modified tracked files. The governed-edit freeze window (contract H2)
  guarantees instrument bytes are identical across the block even where the
  two arms' launch commits differ by output-artefact commits.

## Contract (delta over the D3 run contract)

The D3 run contract hardenings H1–H15 (plan of record, D3 entry) carry over
**verbatim** except:

- **H4/H6 (wire and home).** Sonnet@max wire = **12M contract-metric tokens**
  (provisional ≈ 2× a projected 5.5–6.5M, from the D3 sonnet actual of 6.22M
  plus max-inflation headroom). The opus@max wire is then **derived
  empirically**: 2 × (5.07M × the measured sonnet max/xhigh inflation ratio).
  The remediation-scaled rule (wire grows by the re-run percentage absent a
  stuck-loop indicator) carries unchanged. Calibration lesson recorded: the
  D3 7M wire was set at 2× a 3.33M recount baseline, but realised D3 spend was
  5.07–7.10M — the wire nearly fired on ordinary spend.
- **H12/H13 (verification).** Assembler invocations gain
  `--expect-effort max --expect-launch-commit <hash>` (v1.4 artefact-derived
  provenance). The summary verification pass gains a **telemetry-contrast
  step**: per-spawn thinking-block counts and token spend vs the D3 arms'
  v1.3 telemetry, as the empirical served-effort signal (residual R1 below).
- Reconcile stage stays haiku @ `low` (pinned in workflow opts since v1.1).

## Comparability caveat and residual R1 (Q5)

The D3 `xhigh` baselines were **session-inherited and operator-attested**; the
study's `max` arms are **pinned via workflow opts** — the request channel
itself changed between cycles. Residual R1: the pin is a *requested* value;
nothing artefact-derived proves the *served* effort matched (spawn metadata
carries no effort field — proven 2026-08-17). Mitigations, both adopted
(mitigation 1 AMENDED 2026-08-17, operator-accepted: the CLI could not switch
the main session to `max` without invalidating the session cache, so the
passive fallback-equals-pin arrangement is replaced by an active probe):

1. **P3 differential effort probe, strictly before arm 1** — two sonnet-5
   spawns, identical reasoning prompt (bar an attribution label), one pinned
   `effort: low` and one `effort: max` via workflow opts. Transcript recount
   (thinking blocks + output tokens, same machinery as the assembler) must
   show a large differential; near-identical telemetry means the opts channel
   is ignored and the study halts before any arm spend. Session effort
   remains `xhigh` and is attested honestly
   (`--environment session_effort=xhigh`); a silent pin failure despite P3
   would produce an xhigh replicate of the D3 condition — conservative, and
   caught by mitigation 2 before arm 2 launches.
2. The telemetry-contrast step above — thinking-block and token deltas against
   the xhigh baselines are the empirical served-effort evidence.

## Governance (Q4)

No OSF amendment: selection was registered as "cheapest eligible arm" and
nothing in the registered instrument or gates changes. The study is recorded
here and in the plan's decision log. Stability is computed per arm immediately
(the ≥ 0.90 figure is a reference point; the registrant's gates ruling waits
on concordance). **Concordance stays deliberately uncomputed pending E8 v2**
(contract H5 carried). Effort→cost measurement rides the same run records.

## Probes (Q7)

No new probe spawns. S4's condition (schema conditionals) is unchanged since
it passed and the retreat applied; P2's (Bash in the reconcile lane) is a
stable harness property. The v1.5 changes fail fast and pre-spend: malformed
args throw in the script before any spawn, an opts rejection throws before
spend, and the prompt format is pinned by `tests/test_effort_pinning.py`
cross-file contract tests. Accepted residual: a semantic prompt defect could
burn up to the concurrency cap (~10 scoring spawns) before the first reconcile
verdict — the same exposure D3 accepted.

## Cost estimate (standing API gate input)

Token projection: cache-creation dominates the contract metric and effort does
not inflate it; thinking rides output tokens. From D3 actuals (contract-metric
sonnet 6.22M, opus 5.07M; output 745K / 437K; cache-read 14.9M / 17.3M), with
output inflated 1.5–2× at `max`:

- **Tokens (contract metric):** sonnet ≈ 6.6–7.0M, opus ≈ 5.3–5.5M,
  total ≈ **12–12.5M** — consistent with the carried ~11–13M estimate.
- **API-equivalent dollars** (list rates 2026-08-17: sonnet-5 intro $2/$10
  per MTok through 2026-08-31, opus-5 $5/$25; cache-write premium 1.25×
  (5-min TTL) to 2× (1-h TTL); reads 0.1×):
  - sonnet@max ≈ **$28–40** (write $14–22 + output $11–15 + reads $3)
  - opus@max ≈ **$54–77** (write $29–46 + output $16–22 + reads $9)
  - **two-arm total ≈ $80–120**
- **Correction:** the previously carried ≈$15–25 two-arm figure understated
  cost 4–5× — the token projection was sound, but the dollar conversion
  omitted the cache-write premium and the cache-read volume. Recorded here so
  the discrepancy is visible at the gate; billing in practice rides the Max
  plan (API-equivalent is an accounting figure), and the wire is
  token-denominated.

## Artefact set (per arm, contract H6 carried)

`arm-<model>-<effort>/run-record.json` (v1.4: `provenance_pinned`
artefact-derived block), `run-<N>/<slug>.json` score payloads,
`reconciliation/` report + log slices, one commit per arm.
