TITLE: fix(lane): keep a review-only re-review independent (v1.9)

BODY:

## Summary

- **Principle** (Shawn, 2026-10-31): information moves one way, from execution to review to rulings. A review-only re-review is handed what a first review is handed, and nothing downstream of a review outlives its replacement.
- **Input:** `stage-review` writes the reviewer's gate report with `coverage_admitted` computed with no rulings (`unruled_coverage`). `audit-run` fails a staged report that counts any issue as ruled.
- **Output:** once a review-only audit replaces the review of record, every issue the attempt holds (gate, transcript audit, executor run-audit) is bound to the new review's identity (`review_bound`). Earlier rulings stay in the file as history, and each issue is ruled again. This reverses PR #15's carry-over of executor and unchanged gate rulings.
- **Order:** the gate's admitted coverage reads the same binding, which exists only after `audit-run`. The review-only runbook now audits before the authoritative gate. `check-attempt` records the binding it read (`review_binding`), and `adjudicate` refuses a gate report checked under another review of record. `stage-review` clears the binding in the reviewer's copy.
- **Pre-launch scan** (Shawn, 2026-11-01): runbook step 3 also greps each agent's definition and pushed instruments for the blinding list and the blinded attempt's markers. The rendered-prompt scan cannot see those files.
- Execute-mode attempts are unchanged; attempt 04 still adjudicates to 13/18.

## Why

Found while preparing the gate 1.3.2 reviewer-only pilot. F4 makes every re-review run on a fully ruled attempt, so two things would happen:

- **The re-gated report leaks the rulings.** It told a fresh reviewer 14/18 admitted with nothing unruled; the first reviewer saw 0/18 with 7 unruled. Four of those rulings discharge review obligations on the earlier reviewer's findings.
- **Carried rulings rest on the replaced review.** Besides the four discharges, three executor-side rulings cite its findings (line 27's tolerated statement, T13, T05's PAPER_ERROR). A ruling's free-text note cannot show which did, so all lapse.

A third came up afterwards. The runbook ran the authoritative gate before the audit, so the gate read the replaced review's rulings (14 admitted, none unruled, while admission saw all six gate issues unruled). `adjudicate` would have kept that figure as the gate's history in the study-data record. Credit was not affected.

## Tests

- `tests/test_review_only_mode.py`: 7 new tests and 3 updated; 33 pass. The end-to-end test follows the runbook's order, and a gate run before the audit is refused at adjudication.
- Mutations: eight in the first round; for the reorder, four more (guard off, binding not recorded, binding kept in the staged copy, the gate's binding call site), each failing a named test.
- Full suite on amd-tower: 820 passed.
- Rehearsal on the pilot's labelled copy: re-gated and staged, the reviewer's report shows 0 admitted, 6 of 6 unruled; attempt 04 and the copy both still adjudicate to 13/18.

## Review

Astra, by agent mail.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
