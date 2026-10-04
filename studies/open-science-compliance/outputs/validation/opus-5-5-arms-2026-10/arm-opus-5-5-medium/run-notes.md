# Run notes — arm opus-5-5 at effort medium (2026-10-04)

Arm 2 of 3 in the Opus 5.5 validation block (`../design-note.md`). Operator:
Claude (Opus 5.5), session `c5ee7a27`. The procedure and contract are as
for arm 1 (`../arm-opus-5-5-high/run-notes.md`); only the differences and
the checks are recorded here.

## Launch

- **Workflow run:** `wf_0f3600c3-5ef` (workflow v1.7, args builder v1.5).
- **Launch commit:** `2c93a5dfae4fd452f8bc2c3b7103fe3cb51edb24` (arm 1's
  commit); args checksum `520c07efd4a76a7d`. The checksum guard passed.
  Apart from `effort`, `launch_commit`, and `args_checksum`, the args are
  identical to arm 1's.
- **Result:** 15/15 scoring spawns returned, 0 missing, 0 ESCALATE, 0
  per-item reconciliation failures; about 3.4 minutes wall-clock.

## Residual R2 (relayed user message): not observed

No spawn received a `[Workflow harness — user request]` message (0 of 30).
This arm was launched from a task-notification turn, not from a typed
user message. P4 behaved the same way. The relay therefore appears to fire
only when a workflow launches in the same turn as a typed user message.
The last user message in the session was the neutral go-ahead `Go`.

## Contract checks

- **Authoritative reconciliation:** `--expect-spawns 15 --require-pack
  --contract-schema assessment-system/schema/benchmark-fair-output-schema.json
  --out <run_dir>/reconciliation-authoritative`: 15/15 clean. Every
  SubagentStop gate event was `pass`.
- **H3:** 0 reconciliation failures, 0 ESCALATEs.
- **H4:** 1,910,794 per-request contract-metric tokens against the 4.5M
  wire. Harness-side `subagent_tokens` was 2,121,612.
- **Provenance:** effort `medium` and the launch commit asserted
  artefact-derived (assembler v1.6). Model receipted: `claude-opus-5-5`.

## Unpersisted final usage (see arm 1's notes)

94 of 162 requests lack a final transcript entry. 7 are in scoring spawns,
one each. In 3 of those the final `StructuredOutput` request is left with a
placeholder `output_tokens` (recorded scoring outputs of 831, 850, and 876).
The rest are in the Haiku reconciliation spawns. The cost bounds are
computed in the block's selection-cost step.
