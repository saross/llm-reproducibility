---
title: "Audit 2026-08-03 — outstanding follow-ups"
tags: [infrastructure, governance]
created: 2026-08-03
updated: 2026-08-14
status: open
---

# Audit 2026-08-03 — outstanding follow-ups

Two-lens audit (implementation correctness + test adequacy) of the gate,
hooks, schema, and unwrap script, plus a second-pass re-audit of the fix
commit `3b01676`. First-round Critical/Medium fixes landed in `3b01676`;
this file records everything still open so nothing lives only in a chat
log. Deferred-by-design items carry their reason.

**Pre-run review 2026-08-14:** the Phase C execution contract governing
these fixes is hardened and recorded in
`wiki/planning/instrument-clarification-plan.md` (Phase C pre-run review
section). It binds every item below: one-commit rule (fix + regression
test + register tick per commit), the C1↔C2 ordering interlock, and a
fresh-context round-3 re-audit of the fix commits with a reported
denominator.

## Round 2 — regressions found in the fix commit (fix next)

1. **[x] 2026-08-14 — Gate fallback substitution (re-audit C-2).** Fixed per
   the re-specified rule below; four regression tests (receipt-less final
   JSON falls through, cross-slug substitution blocks, same-slug fallback
   passes, well-formed final payload is never overridden). Tests 87 → 91.
   Original defect: when the final message
   carries a payload with missing/malformed receipt fields, the gate
   silently discards it and validates an earlier transcript tool-call
   payload — receipts are not bound to the item (`paper_slug` never read).
   ~~Fix: fall back to the transcript ONLY when no final-message payload
   exists; when both exist, require `paper_slug` agreement.~~
   **Fix re-specified 2026-08-14 (pre-run audit B2: the struck wording
   was self-contradictory and, read literally, reinstated the C4-era
   final-message-only regression):** the gate searches for a
   *well-formed receipt payload* — final message first; only if the
   final message carries no well-formed receipt payload does it search
   the transcript's tool calls (a receipt-less JSON object in the final
   message must NOT suppress that search). If well-formed payloads exist
   in both places, they must agree on `paper_slug`; disagreement blocks.
   `paper_slug` agreement is internal consistency, not item binding
   (audit S6) — binding design follows the C2 capture.
2. **Gate still blocked 9/15 fable spawns and cannot say why (re-audit
   C-1).** One block message covers two branches; the log carries no
   `agent_id` and no fallback-branch marker; `agent_transcript_path` is a
   design-doc field name never confirmed against a live event.
   **Scale correction (2026-08-14, pre-run audit B1, re-derived from the
   gate log):** the benchmark-wide picture was 39/45 spawns blocked
   (opus 15/15, sonnet 15/15, fable 9/15) with every output still
   collected — the block decision had no downstream consequence
   anywhere, on any arm.
   **Fix, split per the one-commit rule (audit N1):**
   - **[x] 2026-08-14 2a.** Log event keys (names only) + `agent_id` + branch on
     every decision — done, plus `paper_slug` on every decision (closes M-9
     early) and env-overridable log paths (`LLMR_RECEIPT_GATE_LOG`,
     `LLMR_PUSH_RECEIPT_LOG`) as the test seam / C8 archival hook. Tests
     84 → 87.
   - **[x] 2026-08-14 2b.** Confirm the real SubagentStop field names from
     a captured live event — done via the C2 probes (annex:
     `studies/open-science-compliance/outputs/validation/c2-probes-2026-08-14/`).
     `agent_transcript_path` is real; workflow-lane events carry NO
     `last_assistant_message`; on S6's question, the event carries
     `agent_id` and `prompt_id` but no paper-level identifier, so item
     binding stays payload-side (`paper_slug`, per item 1's re-spec).
3. **[x] 2026-08-14 — Preflight fail-closed blast radius (re-audit M-1) +
   non-UTF-8 hole (M-2) + docstring contradictions (M-3/M-4).** Policy
   decided ONCE and applied to both hooks: unattributable events (parse
   failures incl. non-UTF-8, non-object events, non-object tool_input,
   import failures) fail closed — preflight denies, gate blocks — with
   messages naming the fault class as environment/parse fault, not a
   verdict (audit N2). Gate gains the same fail-closed import guard as
   preflight; L-7 test now asserts denial; N5 folded (preflight passes
   `--preflight` to D5, duplicate env check removed). Tests 91 → 95.
   Original defect: Catch `Exception` not just
   `JSONDecodeError`; decide deny-vs-allow for unattributable events ONCE,
   apply consistently across both hooks, and make docstrings state the
   actual behaviour. Current state: preflight denies unparseable (all spawn
   types — project-wide stop if the env breaks); receipt gate ALLOWS
   unparseable; `tool_input` non-dict allows. `test_list_tool_input_denies_
   not_crashes` asserts nothing about denial (L-7) — rename or fix.
   Also fold in (audit N5): `preflight-agent.py` invokes the D5 checker
   without `--preflight`, leaving the script's env-override branch
   test-only — unify so both hooks share one fail-closed path.
4. **[x] 2026-08-14 — Enumeration exclusions still leak (re-audit M-5).**
   Fixed as specified: the walk recurses into lists (`section[i]` paths)
   and the exclusion set shrank to the five sections producing their own
   entity kinds (shared_content, agent_definitions, reference_datasets,
   entity_checks, workflow_passes). Live manifest unchanged at 57/57
   (zero entity churn, as the pre-run audit's simulation predicted).
   Tests 95 → 97.
5. **[x] 2026-08-14 — `rglob("*")` stray-file tripwire (re-audit M-6).**
   Fixed: the reverse sweep skips dotfiles, dot-directories, and
   `__pycache__` in scan directories (dotfile route chosen over
   `git check-ignore` — deterministic, no subprocess). Tests cover
   `.DS_Store`, an editor swap file, and `__pycache__` contents.
6. **[x] 2026-08-14 — `normalise_rules_of` crashes on scalar rules
   (re-audit M-7).** Fixed with the `<invalid>` sentinel as specified;
   a scalar `normalise: 3` now raises the unknown-rule error instead of
   crashing the gate. Items 5+6 tests: 97 → 100.
7. **[x] 2026-08-14 — Lows batch, all eight closed:** M-9 (item identifier
   in every gate log — landed early with item 2a); L-1 (an incomplete
   nested `receipts` dict no longer masks complete flat fields); L-3
   (empty declared pull blocks instead of matching everything); L-4 (E6
   honours `path:` entities and names its real target); L-5 (list-rooted
   manifest reports instead of tracebacking); L-6 (`main()`'s last-resort
   handler now under test); L-8 (positive allowed-governed-spawn test);
   L-10 (E8 empty-key test asserts a clean report, not one absent
   string). Tests 100 → 106.

## Pre-run audit additions (2026-08-14, adjudicated; registrant approved)

Clean-context audit findings folded into this register (adjudication
record and contract amendments in
`wiki/planning/instrument-clarification-plan.md`, Phase C):

8. **[x] 2026-08-14 — S1 — commit gate runs tests.** Done, block-tested
   live (an injected red test refused a commit). Prefers the venv's
   pytest, falls back to stdlib unittest discovery so venv-less machines
   still enforce it; zbook picks this up when it re-runs
   `./scripts/install-git-hooks.sh` (standing carry-forward). Accepted
   residual, documented: like D5, the gate reads the working tree, not
   the index, so a partially staged manifest/instrument pair can commit
   green — mitigated by the standing explicit-pathspec discipline for
   concurrent sessions; index-accurate checking is a future enhancement,
   not a Phase C item. **Residual observed live the same day:** the
   block-test probe's unstaging failed silently and the staged copy
   leaked into `5618e30` while the worktree-reading gate saw green;
   removed in `d2cb58a`. Observed, not theoretical. (2026-08-14
   addendum: the fallback unittest runner now needs jsonschema for the
   C3 schema battery — a venv-less machine gets a loud import failure
   at commit; create the per-machine venv per step-0.)
9. **S2 — operative demo covers three cases:** final-message pass,
   transcript-borne pass (the shape that actually failed 39/45), and a
   consequence-verified catch — the blocked spawn's output demonstrably
   excluded or retried, never merely a `block` line in the log (audit
   B1). **Outcome 2026-08-14:** case 1 ✓ (probe A), case 2 ✓ (probe B),
   case 3 half: the catch fires correctly but the consequence is ABSENT
   in the workflow lane (probe C — block undelivered, output collected);
   operative status in that lane pends plan item C9's reconciliation.
   Diagnostic bonus: all 45 benchmark transcripts re-validated clean
   post-hoc — the 39 benchmark blocks were transcript-lag false alarms.
   Full record in the C2 annex.
10. **[x] 2026-08-14 — S3 — schema identity receipted.** Landed as a
    validator-enforced `schema_version` const in v1.1 (the model cannot
    hash a schema, so self-identification + the E4/C7 registry hashes
    close the chain instead of a model-echoed sha256); the receipt gate
    blocks payloads whose declared schema_version mismatches the
    registry (absent = v1.0-era, passes). Workflow-side stop-stripping
    of `version` and run-record hash wiring ride C9/D3 prep.
11. **S4 — v1.1 validator compatibility.** Standard JSON Schema
    keywords only; a validator probe confirms acceptance before D3.
    New stop condition: v1.1 rejected at spawn time halts the block.
12. **N4 — C5's self-check gets a committed home:**
    `tests/test_unwrap_paste.py`, regression-anchored to the
    amendment 1 paste artefact.

## Deferred by design (with reasons)

- **Schema v1.1** (audit C6 ESCALATE-forces-fabrication; M12 bounds,
  evidence minLength, A1 cross-reference conditional; M13 dot→underscore
  mapping note): deferred so all three benchmark arms ran identical
  config. Build v1.1 BEFORE the census; it also needs a supply mechanism —
  the schema is registered but nothing pushes it ("schema supplied at
  spawn" is currently orchestrator-side only, cross-file finding 2).
- **C7 — no content-integrity check on push-only frozen instruments**
  (5 of 7 have no body check; mirrored ones cover 81%/59% of lines).
  GOVERNED: add `sha256:` to `shared_content` entries + checker support;
  aligns with monitoring-plan Phase 2b. Registrant decision required on
  the edit workflow (every gated instrument edit then updates its hash).
- **Agent-definition output contract wording** (flat receipt fields vs the
  schema's nested `receipts`): GOVERNED (hash-registered definitions). The
  gate now accepts both; align wording at the next gated definitions edit.
- **M10 — receipt tokens prove delivery-and-echo, not consumption, for
  pushed instruments**: documented in the gate docstring; a stronger
  consumption proof is a design question, not a patch.
- **unwrap-paste-file.py M14/M15/M16** (indented list absorption,
  year-line mis-protection, global double-space collapse): latent until
  the next lodgement; fix with a self-check before OSF amendment 2 or any
  future paste artefact.
- **Wiki correction**: continuity/session-log claims of "17 synthetic
  pipe-tests" for the hooks — the tests were ephemeral and never
  committed (audit C4). Committed suite now exists (`tests/test_hooks.py`);
  add a dated correction note at the next continuity update.
- **Coverage self-report cannot detect enumerator+declaration co-removal**
  (lens B M1): accepted residual risk — the gate cannot defend against
  coordinated edits to itself; recorded in the monitoring plan's terms.
- **L-9**: `test_hooks.py` pins fair-instrument v2.0 — deliberate tripwire;
  update alongside any gated instrument version bump.
