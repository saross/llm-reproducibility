# Run notes — arm opus-5-5 at effort high (2026-10-04)

Arm 1 of 3 in the Opus 5.5 validation block (`../design-note.md`). Operator:
Claude (Opus 5.5), session `c5ee7a27`, under Shawn's API gate stage 2
approval (2026-10-04).

## Launch

- **Workflow run:** `wf_965c388c-bfb` (workflow v1.7, args builder v1.5).
- **Launch commit:** `108a88d36dc45763c599bdc3cab43b7cb6b9ec7f`; args checksum
  `fc4d5c5ce69f5cac`. The checksum guard passed.
- **Harness:** Claude Code 2.1.289 (the P4 probe's version).
- **Pre-flight:** tree clean; `fair-assessor-opus-5-5` in the
  available-agents list (register F-018); no governed file changed since
  P4 (`9553f46`), so no re-probe.
- **Result:** 15/15 scoring spawns returned, 0 missing, 0 ESCALATE, 0
  per-item reconciliation failures; about 4.6 minutes wall-clock.

## Residual R2 (relayed user message): observed, neutral

The relay was **active** in this arm, unlike P4. Every one of the 30 spawns
(15 scoring, 15 reconciliation) received `[Workflow harness — user request]`
carrying exactly `Go`. Per the Q7 ruling, Shawn sent that neutral go-ahead
as the last user message before launch. It is recorded as
`run_environment.launch_user_message`.

## Authoritative reconciliation

- **Accepted pass:** `reconcile-run.py <run_dir> --expect-spawns 15
  --require-pack --contract-schema
  assessment-system/schema/benchmark-fair-output-schema.json --out
  <run_dir>/reconciliation-authoritative`: 15/15 clean. This matches the
  registered arms' authoritative pass
  (`../../benchmark-2026-08-17/benchmark-summary.md`, line 9).
- **Procedural slip, no effect on the record:** the first pass followed the
  2026-10-04 handoff, which omitted `--contract-schema` and `--out`. It came
  back 15/15 clean but wrote to the default `<run_dir>/reconciliation/`,
  overwriting the per-item stage's last report there. That file sits
  outside the repository and the assembler does not use it. The per-item
  verdicts survive in the workflow journal and result (all `pass`).
- **Gate divergence:** two spawns (`a4ae6a0c3df878505` herskind r1,
  `aaf0570ecf3124fd2` herskind r2) logged a SubagentStop `block` ("no
  structured output found"), with output present
  (`blocked_but_output_present`). The registered arms show the same
  pattern (opus-5 xhigh 5, fable-5 9, sonnet-5 max 5). The gate is advisory
  in this lane, and reconciliation is authoritative.

## Contract checks

- **H3:** 0 reconciliation failures, 0 ESCALATEs.
- **H4:** 1,939,730 per-request contract-metric tokens against the 4.5M
  wire. The workflow's harness-side `subagent_tokens` was 2,112,878, also
  under the wire.
- **Provenance:** effort `high` and the launch commit are artefact-derived
  from every scoring prompt (assembler v1.6 `--expect-effort` and
  `--expect-launch-commit` both asserted). Model receipted:
  `claude-opus-5-5`.

## Finding: output tokens under-counted where a request's final entry is missing

The harness writes one transcript entry per content block. Usually the
request's last entry carries the final `usage` and a `stop_reason`. In some
requests **no** entry carries a `stop_reason`. Each entry then holds only
the streaming-start usage snapshot, so `output_tokens` reads as a
placeholder (for example 8) instead of the request's true output. Input
and cache fields are set at stream start, so they are unaffected; only
output is under-counted.

- **This arm:** 95 of 172 requests lack a final entry. 6 are in scoring
  spawns (4 spawns: crema r1, crema r2, dye r1, key r3, each missing its
  final `StructuredOutput` request of about 14,000 characters). The other
  89 are in the Haiku reconciliation spawns.
- **Pre-existing:** the registered transcripts show it too. opus-5 high
  (`wf_d691e836-2f2`, 2.1.233) has 26 of 209 requests; opus-5 xhigh
  (`wf_67cd3484-a08`) has 11 of 209. The registered selection-cost figures
  therefore also under-count output.
- **Not recoverable from the run files:** the journal and meta sidecars
  carry no per-agent usage.
- **Bearing:** cost only (the selection rule's price leg). Scores, gates,
  and the H4 wire are unaffected. To be lodged as a register candidate and
  quantified across all arms in the selection-cost step.
