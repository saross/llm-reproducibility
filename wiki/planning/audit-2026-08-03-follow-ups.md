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
   - **2b.** Confirm the real SubagentStop field names from a captured
     live event (closed by C2's capture, which also records whether the
     event carries assignment identifiers — audit S6).
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
5. **`rglob("*")` stray-file tripwire (re-audit M-6).** A `.DS_Store`/swap
   file in a scan directory blocks all commits and all governed spawns.
   Fix: skip dot-directories/dotfiles and `__pycache__`, or filter via
   `git check-ignore`.
6. **`normalise_rules_of` crashes on scalar rules (re-audit M-7).** Return
   an `<invalid>` sentinel so the unknown-rule error fires instead.
7. Lows worth batching: gate log without item identifier (M-9), flat+
   `receipts`-dict carrier misselection (L-1), empty-string pulled path
   free pass (L-3), E6 path-only error message (L-4), list-rooted manifest
   traceback (L-5), untested `main()` fail-closed handler (L-6), no
   allowed-governed-spawn test (L-8), weak E8 empty-key assertion (L-10).

## Pre-run audit additions (2026-08-14, adjudicated; registrant approved)

Clean-context audit findings folded into this register (adjudication
record and contract amendments in
`wiki/planning/instrument-clarification-plan.md`, Phase C):

8. **S1 — commit gate runs tests.** Add the pytest suite to the
   pre-commit hook (the suite runs in under a second). Accepted
   residual, documented: the D5 pre-commit check reads the working
   tree, not the index, so a partially staged manifest/instrument pair
   can commit green — mitigated by the standing explicit-pathspec
   discipline for concurrent sessions; index-accurate checking is a
   future enhancement, not a Phase C item.
9. **S2 — operative demo covers three cases:** final-message pass,
   transcript-borne pass (the shape that actually failed 39/45), and a
   consequence-verified catch — the blocked spawn's output demonstrably
   excluded or retried, never merely a `block` line in the log (audit
   B1).
10. **S3 — schema identity receipted.** C3 adds schema version + sha256
    to the receipt fields; the benchmark workflow stops stripping
    `version` before spawn.
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
