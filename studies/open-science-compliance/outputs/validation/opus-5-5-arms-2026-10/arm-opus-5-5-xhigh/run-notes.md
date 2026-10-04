# Run notes — arm opus-5-5 at effort xhigh (2026-10-04)

Arm 3 of 3 in the Opus 5.5 validation block (`../design-note.md`). Operator:
Claude (Opus 5.5), session `c5ee7a27`. The procedure and contract are as
for arm 1 (`../arm-opus-5-5-high/run-notes.md`); only the differences and
the checks are recorded here. The governed-edit freeze (Q6) ends with this
arm's commit.

## Launch

- **Workflow run:** `wf_3863b134-e26` (workflow v1.7, args builder v1.5).
- **Launch commit:** `656036f3e3ee1f3ee97749b6317bb6437e4b821f` (arm 2's
  commit); args checksum `07c2d772a8cc318a`. The checksum guard passed.
  Apart from `effort`, `launch_commit`, and `args_checksum`, the args are
  identical to arm 1's.
- **Result:** 15/15 scoring spawns returned, 0 missing, 0 ESCALATE, 0
  per-item reconciliation failures; about 10.5 minutes wall-clock.

## Residual R2 (relayed user message): not observed

No spawn received a `[Workflow harness — user request]` message (0 of 30).
The arm was launched from a task-notification turn, as arm 2 was.

## Contract checks

- **Authoritative reconciliation:** `--expect-spawns 15 --require-pack
  --contract-schema assessment-system/schema/benchmark-fair-output-schema.json
  --out <run_dir>/reconciliation-authoritative`: 15/15 clean.
- **Gate divergence:** two spawns (`aa1ee7a17cd1419c0`,
  `aa1f898ffa100802c`) logged a SubagentStop `block` ("no structured output
  found"), with output present (`blocked_but_output_present`). This is the
  same advisory pattern as arm 1 and the registered arms.
- **H3:** 0 reconciliation failures, 0 ESCALATEs.
- **H4:** 2,274,311 per-request contract-metric tokens against the 4.5M
  wire. Harness-side `subagent_tokens` was 2,125,004.
- **Provenance:** effort `xhigh` and the launch commit asserted
  artefact-derived (assembler v1.6). Model receipted: `claude-opus-5-5`.

## Unpersisted final usage (see arm 1's notes)

93 of 187 requests lack a final transcript entry. 4 are in scoring spawns,
one each, and 1 of those (`a9d7cf9e`) is the final `StructuredOutput`
request. The rest are in the Haiku reconciliation spawns. The cost bounds
are computed in the block's selection-cost step.
