# C2 probe annex — live SubagentStop capture and operative-gate demonstration

**Date:** 2026-08-14 | **Machine:** amd-tower | **Operator approval:** Shawn,
same day (standing Application Programming Interface (API) review gate:
sonnet-pinned governed spawns, real-time, ≤4; three were used).
**Contract:** `wiki/planning/instrument-clarification-plan.md`, Phase C
pre-run review, hardening 7; probes are pack-free, score only the synthetic
fixture `tests/fixtures/c2-synthetic-paper.md`, and nothing here is a
persisted assessment.

## Probe design and outcomes

| Probe | Lane | Design | Push (UTC) | Gate event | Outcome |
|---|---|---|---|---|---|
| A | Agent tool | Compliant spawn, JSON in final message | 07:40:11 | `pass`, `payload_source: final_message`, 1 verified pull | Full-chain pass |
| B | Workflow, schema-forced | Compliant spawn, output rides a StructuredOutput tool call | 07:45:46 | `pass`, `payload_source: transcript_tool_call` | Transcript-borne pass proven |
| C | Workflow, relaxed schema | Receipts deliberately omitted in first emission | 07:48:39 | `block` ("no structured output found") | Catch fired; **consequence absent** |

Raw records: `gate-log-slice.jsonl` and `push-log-slice.jsonl` in this
directory (verbatim slices of the live hook logs for 2026-08-14).
Spawn agent ids: A `a0b3fc4d3abb2326b`, B `a8df23f30c440eba9`,
C `ad4e71866853621b8` (match across push, gate, and workflow journal).

## Findings

1. **Field names confirmed (closes register item 2b).** The live
   SubagentStop event carries `agent_type`, `agent_id`,
   `agent_transcript_path` (the design-doc name was correct), a separate
   `transcript_path` (parent session), `last_assistant_message`, plus
   `background_tasks`, `cwd`, `effort`, `hook_event_name`,
   `permission_mode`, `prompt_id`, `session_crons`, `session_id`,
   `stop_hook_active`. **Lane differential:** workflow-lane events carry
   NO `last_assistant_message` (13 keys vs the Agent lane's 14) — in that
   lane the transcript path is the gate's only payload source.
2. **Pass paths proven in both lanes.** Probe A validated end-to-end in
   the Agent lane (preflight allow → push receipted with sha256 → gate
   pass including a transcript-verified full pull). Probe B validated the
   transcript-borne path in the workflow lane.
3. **The catch fires but has no consequence in the workflow lane
   (pre-run audit B1's mechanism, confirmed).** Probe C's gate block was
   logged, but the block message appears nowhere in C's transcript (0
   occurrences) — it was never delivered to the agent, no retry occurred,
   and the workflow's `agent()` returned the receipt-less output as a
   normal result. SubagentStop block decisions are advisory in the
   workflow lane: the harness collects StructuredOutput results
   independently of them.
4. **The 2026-08-03 benchmark's 39/45 blocks are diagnosed as transcript
   write lag, and its provenance is retroactively machine-verified.**
   Today's search function, run over all 45 retained benchmark
   transcripts, finds a well-formed receipt payload in **45/45**; full
   validation (instrument versions, receipt tokens, model pins, agent
   versions, and every declared pulled read checked against transcript
   Read calls) passes **45/45**. The payloads were always there; the
   runtime searches failed because the transcript was not yet readable
   within the old 4 × 0.75 s retry budget, and the block message
   conflated "transcript unavailable" with "searched and found nothing".
   The benchmark's hand-tallied "receipts 15/15 pass" per arm is thereby
   upgraded to machine-verified fact — the blocks were false alarms; no
   unverified output entered the record.
5. **Probe A's assessor flagged the spawn framing** — its definition
   *body* (the injected instruction text) carries no "never invoked ad
   hoc" clause; that phrase lives only in the frontmatter `description`,
   which the harness does not inject. Correct scepticism, and a candidate
   wording alignment for the D1 governed definitions edit.

## Remedies (landed today / queued)

- **Landed with this annex's commit:** retry budget 8 × 1.0 s;
  `transcript_state` (`not-needed` / `read` / `none-declared` /
  `unavailable-after-retries`) logged on every decision; distinct block
  reason for the unavailable case. Tests 106 → 107.
- **Queued as plan item C9 (pre-census requirement):** orchestrator-side
  gate reconciliation — after each workflow `agent()` returns, the run
  consults the gate log for that agent id and treats anything but a
  `pass` as unverified (re-validate post-hoc from the completed
  transcript, exactly as done for the 45 above; re-run or fail the item
  otherwise). This implements the adopted divergence tripwire (gate
  events vs outputs-collected) and is the authoritative backstop that
  makes hook-time lag harmless.

## Verdict against the register's operative criterion

Capture ✓ (both lanes, field names anchored above). Pass ✓ (both lanes).
Catch ✓ (fires, correctly, on a receipt-less payload). **Consequence ✗ in
the workflow lane** — therefore the gate is operative in the Agent lane
and *detection-operative but consequence-blind* in the workflow lane
until C9 lands. C9 is the condition for calling the workflow-lane gate
operative; the D3 re-benchmark must not run without it.
