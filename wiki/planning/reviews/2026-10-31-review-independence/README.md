# Lane v1.9, the re-review's independence: PR and review drafts (2026-10-31)

Drafts for branch `fix/review-only-independence` (head `003a8e0`; code
`08d013b` and `6d417e2`, docs `a540e3c`, `3f62eee`, `3da75d3`, and
`003a8e0`), written in session 4c1fd032 on zbook and amended in session
e765dd2a on amd-tower for the gate-ordering seam and the pre-launch scan.
The change is described in `wiki/planning/reproduction-gate-1-3-design.md`,
"Independence of a re-review".

**Status (2026-11-01, session e765dd2a): neither draft is sent; both are
amended and await Shawn's approval of the PR text.**

- `pr-draft.md`: the pull request's title and body. **Not yet approved by
  Shawn, and the PR is not opened.** After his approval of the exact text,
  open it with `gh pr create` from the branch, read it back against this
  file, and record its number and URL here.
- `astra-review-request.md`: the review request for Astra (GPT in Codex).
  Not sent. Add the PR number, then send it through agent mail from
  amd-tower (`~/agent-mail/claude/outbox/codex/`, timestamped name), with
  her reply expected in `~/agent-mail/codex/outbox/claude/`.

Merge only after Astra approves and Shawn says to merge.

**Closed 2026-11-01 (`6d417e2`, `3da75d3`; Shawn chose reorder and
guard), and mentioned in both drafts.** As found at handoff: on the branch,
`check_attempt`'s comment and the test
`test_the_gate_report_agrees_with_admission_after_a_review_only_audit` say
that the gate's admitted coverage agrees with admission after a review-only
run. That holds only if the gate runs after `audit-run`, and
the review-only runbook runs the authoritative gate (step 4) before the
audit (step 5), while the old run audit still stands; `adjudicate` then
copies that figure into its history. Credit is unaffected. Close it on the
branch (re-run `check-attempt` after `audit-run` in review-only mode, or
reorder the steps), and mention the fix in both drafts.
