TITLE: fix(lane): keep a review-only re-review independent (v1.9)

BODY:

## Summary

- **Principle** (Shawn, 2026-10-31): information moves one way, from execution to review to rulings. A review-only re-review is handed what a first review is handed, and nothing downstream of a review outlives its replacement.
- **Input:** `stage-review` writes the reviewer's gate report with `coverage_admitted` computed with no rulings (`unruled_coverage`). `audit-run` fails a staged report that counts any issue as ruled.
- **Output:** once a review-only audit replaces the review of record, every issue the attempt holds (gate, transcript audit, executor run-audit) is bound to the new review's identity (`review_bound`). Earlier rulings stay in the file as history, and each issue is ruled again. This reverses PR #15's carry-over of executor and unchanged gate rulings.
- Execute-mode attempts are unchanged; attempt 04 still adjudicates to 13/18.

## Why

Found while preparing the gate 1.3.2 reviewer-only pilot. F4 makes every re-review run on a fully ruled attempt, so two things would happen:

- **The re-gated report leaks the rulings.** It told a fresh reviewer 14/18 admitted with nothing unruled; the first reviewer saw 0/18 with 7 unruled. Four of those rulings discharge review obligations on the earlier reviewer's findings.
- **Carried rulings rest on the replaced review.** Besides the four discharges, three executor-side rulings cite its findings (line 27's tolerated statement, T13, T05's PAPER_ERROR). A ruling's free-text note cannot show which did, so all lapse.

## Tests

- `tests/test_review_only_mode.py`: 7 new tests and 3 updated. Every change is pinned by a test that fails under a mutation of it (8 mutations).
- Full suite: 781 passed, 7 skipped.
- Rehearsal on the pilot's labelled copy: the staged report shows 0 admitted, 6 of 6 unruled; attempt 04 and the copy both still adjudicate to 13/18.

## Review

Astra (relayed by Shawn while agent mail is unreachable).

🤖 Generated with [Claude Code](https://claude.com/claude-code)
