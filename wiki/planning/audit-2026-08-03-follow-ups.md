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

1. **Gate fallback substitution (re-audit C-2).** When the final message
   carries a payload with missing/malformed receipt fields, the gate
   silently discards it and validates an earlier transcript tool-call
   payload — receipts are not bound to the item (`paper_slug` never read).
   Fix: fall back to the transcript ONLY when no final-message payload
   exists; when both exist, require `paper_slug` agreement.
2. **Gate still blocked 9/15 fable spawns and cannot say why (re-audit
   C-1).** One block message covers two branches; the log carries no
   `agent_id` and no fallback-branch marker; `agent_transcript_path` is a
   design-doc field name never confirmed against a live event. Fix: log
   event keys (names only) + `agent_id` + branch on every decision; confirm
   the real SubagentStop field names from a captured event before the
   census.
3. **Preflight fail-closed blast radius (re-audit M-1) + non-UTF-8 hole
   (M-2) + docstring contradictions (M-3/M-4).** Catch `Exception` not just
   `JSONDecodeError`; decide deny-vs-allow for unattributable events ONCE,
   apply consistently across both hooks, and make docstrings state the
   actual behaviour. Current state: preflight denies unparseable (all spawn
   types — project-wide stop if the env breaks); receipt gate ALLOWS
   unparseable; `tool_input` non-dict allows. `test_list_tool_input_denies_
   not_crashes` asserts nothing about denial (L-7) — rename or fix.
4. **Enumeration exclusions still leak (re-audit M-5).** `corpus`/`project`
   /`version_history`/`licences` subtrees and list-of-dicts entries escape.
   Fix: walk lists too; shrink the exclusion set to sections that produce
   their own entity kinds (shared_content, agent_definitions,
   reference_datasets, entity_checks, workflow_passes).
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
