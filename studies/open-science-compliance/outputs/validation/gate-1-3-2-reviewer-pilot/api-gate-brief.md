# Gate 1.3.2 reviewer-only pilot: API-gate brief and launch checklist

**Prepared:** 2026-10-30 (Claude, Opus 5.5), on zbook, on main after PRs
#14 and #15 merged (`37a3fe7`); the labelled copy is `2a3d577` and the
configuration `5084dd0`. **Status:** not approved and not launched. Shawn
approves at the API gate, from a fresh Claude Code session on amd-tower.
Two decisions are open before launch (see "Open before launch").

**Why this run.** Gate 1.3.2 changed what the reviewer writes
(`adversarial-reviewer` v1.4: target-scoped concerns and a method row per
locked target), and the design's §2.2 asks one real run of such a change.
Criterion 4 (Fable's proposal, Astra's scope) makes that run the review-only
mode on attempt 04: one reviewer spawn, binding the original executor
result, a fresh reviewed state, a fresh reviewer identity and audit, and
the retry and changed-comparison tests. It also pilots the mode itself
(lane v1.8, run audit 1.2, `reproduction-review.workflow.js` v1.0).
Configuration: `run-config.yaml` beside this file. The reviewed attempt is
the labelled copy at
`studies/open-science-compliance/pilot-copies/gate-1-3-2-reviewer-pilot/`
(Shawn's choice, 2026-10-30), so the original attempt 04 keeps its 13/18,
its review, and its rulings.

## What runs

| Item | Value |
|---|---|
| Workflow | `reproduction-system/workflows/reproduction-review.workflow.js` v1.0 |
| Paper | herskind-riede-2024, the labelled copy of attempt 04 |
| Bound executor | `wf_4fd7a886-ada`, agent `a23bd74af4155b907`, payload `42455c5d…`, launch commit `6b18505` |
| Agents and models | 1 mechanical gate step (`general-purpose`, `claude-haiku-5-5`, effort low); 1 governed `adversarial-reviewer` v1.4, `claude-opus-5-5`, effort high |
| Mode | real-time workflow on the Max plan, priced API-equivalent; not batch |
| Spawns | 2 (no planner, no executor; Docker only for the gate's image check) |
| API requests | about 4 for the gate step and 30 to 45 for the reviewer |
| Estimate | $3.50 to $5.50 API-equivalent; 8 to 15 minutes |
| Tripwires | check progress at $5.50 or 15 minutes; halt at $8.25 or 22.5 minutes |

**Basis.** Attempt 04's own review, in the gate 1.3.1 pilot re-run
(`wf_4fd7a886-ada`, audit `../gate-1-3-1-pilot-rerun/audit-wf_4fd7a886-ada.json`):
the v1.3 reviewer cost $3.3045 over 31 requests and 464.7 seconds (32,396
output tokens, 5.97 million input-side tokens), and its gate step $0.0092
over 4 requests. The v1.4 reviewer reads the same artefacts and writes more:
a method row for each of 18 targets and a scoped concern list. The range
allows 5 to 65 per cent more than the basis. The tripwires follow the
runbook's rule: check at the top of the estimate, halt at 1.5 times it.

## What the preparation checked (2026-10-30, no API cost)

- **The copy.** 339 files, `diff -r` clean against the original, artefact
  state `f549d2f5…` equal to the original's, and `carried_executor` binds
  the cleared executor with no problems.
- **The gate on the copy.** `check-attempt` with the executor's launch
  commit, run on a throwaway copy without the image, passes at gate 1.3.2
  with six issues, every one matched by attempt 04's existing rulings (none
  unruled).
- **The args.** `build-review-args` on the committed tree binds the
  executor above, 18 locked targets, image `llmr-herskind-riede-2024-attempt-04`,
  and receipt keys `pipeline-invariants` and `adversarial-review-framework`;
  it wrote nothing outside its `--out`.
- **The prompts.** Both prompts rendered from those args (workflow run
  under node with stubbed agents): no blinded substring outside the
  blinding instruction. The gate's two commands pass the lane's own scan
  clean.
- **The staging.** `stage-review` of the copy into a scratch folder: 333
  files copied, 6 withheld, state equal. The staged copy holds only
  pre-review records (the approval note dates from plan time, the gate
  report from the original run).

## Open before launch

1. **The reviewer's own definition points at the earlier review's
   evidence.** `.claude/agents/adversarial-reviewer.md` line 99 gives, as
   its example of an evidence path, `comparisons/t17-cluster-objects-vs-table3.csv`
   (added in `2ccda2e`, gate 1.3.2 criterion 1). That is a real file in
   attempt 04 and the evidence the earlier review cited for its central
   concern (T17's credit under ruling Q5). It is pushed to the reviewer in
   its definition, outside any blinding, and names no conclusion, but it
   draws a fresh reviewer's attention to exactly the target this pilot
   would compare. The prompt scan cannot see it (it is not a path under a
   blinded substring). Recommendation: a v1.4.1 that replaces the example
   with outcome-neutral paths (`comparisons/comparison.json`,
   `reproduction-plan.json`), with the manifest's version and sha256, before
   launch. Without it, a T17 finding by the fresh reviewer cannot be read
   as independent.
2. **The re-gated report tells the reviewer every gate issue was ruled.**
   The gate step re-runs `check-attempt` in the copy, whose rulings file
   holds Shawn's rulings, and the report's `coverage_admitted` then reads
   14 of 18 admitted with no unruled issues (the original reviewer saw 0 of
   18, with 7 unruled). It names no target ruling and nothing of the
   earlier review, but a fresh reviewer learns that a human admitted every
   gate issue. This is a property of the mode (any review that replaces a
   review of record meets ruled gate issues), not of this pilot; a later
   change could stage a gate report computed without rulings. For this
   run: proceed and record it as a known difference, or hold for that
   change.

## Launch checklist (in a fresh session on amd-tower)

A fresh session loads the reviewer definition from main, and amd-tower holds
attempt 04's image.

1. `git fetch`, then confirm main is level with origin and contains
   `5084dd0` (and the v1.4.1 commit, if item 1 above lands); the tracked
   tree is clean.
2. Confirm the definition on disk and the manifest:
   `grep -c "agent definition v1.4" .claude/agents/adversarial-reviewer.md`
   and `venv/bin/python scripts/check-manifest-consistency.py`.
3. Confirm the image: `docker image inspect llmr-herskind-riede-2024-attempt-04`
   succeeds. Without it the gate step fails and nothing is reviewed.
4. Build the args (no API cost):
   `venv/bin/python scripts/reproduction-lane.py build-review-args --config studies/open-science-compliance/outputs/validation/gate-1-3-2-reviewer-pilot/run-config.yaml --scratch-root ~/scratch/llmr-runs --out ~/scratch/llmr-runs/gate-1-3-2-reviewer-pilot-2026-11-args.json`.
   Keep the args file outside the run's scratch folder, so the staging
   folder starts empty. Check the executor binding above, 18 targets, and
   37 blinding entries (29 configured, 8 withheld records added by the
   lane). If a commit moves `HEAD` after this, rebuild.
5. Re-render and scan the prompts (runbook step 3), as on 2026-10-30.
6. API gate: present the table above with the args checksum; Shawn
   approves.
7. Launch: the Workflow tool with `scriptPath` set to the committed workflow
   file and `args` set to the built JSON, unedited, in direct reply to a
   typed approval. The relayed launch message reaches the reviewer:
   Shawn's go-ahead should be exactly `Run the approved stage.`, since the
   launch word rule (an operational follow-up) is not yet built, and the
   audit flags any other message for a ruling.
8. During the run, leave the main checkout alone: the agents run the lane
   script from it.

## After the run (runbook, "Review-only re-run")

In this order, with `CFG` the configuration above and `COPY` the copy's
attempt directory:

1. **Authoritative gate:** `check-attempt $COPY --plan $COPY/reproduction-plan.json --image llmr-herskind-riede-2024-attempt-04 --launch-commit 6b1850554def6a563d82a5409dd821f56b4cb1d4`.
2. **Audit, before clearing the scratch folder:** `audit-run --config $CFG
   --run-dir <workflow run dir>`. It verifies the staged copy by re-hashing
   it.
3. **Human queue** (`human-queue`), then **rulings** (`rule-flags`), drafted
   with their target and verdict parts at ruling time. Check the transcript
   before ruling any "possibly a blinded read" warning admissible.
4. **Persist** (`persist-results`), then **adjudicate** `$COPY`.
5. **Results** in `results-<date>.md` beside this brief, against the
   acceptance checks below.

## Acceptance

1. **The binding.** The run audit in the copy carries the executor from
   `wf_4fd7a886-ada` unchanged (its cleared state `f549d2f5…`), moves the
   earlier run audit to `superseded/wf_4fd7a886-ada/`, and binds the
   reviewer to this run.
2. **A fresh reviewed state.** The reviewed state comes from the gate
   step's `stage-review` record; `audit-run` re-hashes the staged copy and
   its gate report, and the reviewer's prompt named that copy.
3. **A clean audit.** Receipts valid (`adversarial-reviewer v1.4`, or
   v1.4.1), no contaminating access by either agent, no writes outside
   scope.
4. **The v1.4 review, live.** One method row per locked target (18), none
   missing, duplicated, or unknown; concerns with scope and targets; a
   verdict challenge. It persists without a schema or row failure.
5. **No inherited clearance.** The new review's concerns, method rows, and
   verdict flag reach the human queue unruled; the six gate issues, whose
   fingerprints are unchanged, keep their rulings.
6. **Persistence and adjudication in the copy.** Only the review is
   persisted; the earlier review and adjudicated result move to
   `superseded/wf_4fd7a886-ada/`; the new adjudicated result names this run
   as `review_run` and passes `adjudicate --check`.
7. **The original untouched.** `git status` shows nothing under the
   original attempt 04, and its `adjudicate --check` still reads 13/18.
8. **The retry and changed-comparison tests** (mechanical, no spend, on
   throwaway copies of the post-run copy and run directory): a changed
   `comparisons/comparison.json` is refused by `build-review-args` and at
   admission; a second reviewer result appended to the run's journal is
   refused by `audit-run` and `persist-results`; a review payload changed
   after its audit is refused at admission.

**Findings, not criteria** (compared afterwards, by the orchestrator, with
the earlier review, which stays withheld from the reviewer): does the v1.4
reviewer raise T17's credit under Q5, and target-scope it; does it find the
method departures the v1.3 reviewer found (T01, T03, T04, T12) and the
declared T13; does its verdict challenge support SUCCESSFUL. Read item 1 of
"Open before launch" with any T17 finding.

## Stop states

- **Receipts invalid** (for example a stale definition): the session loaded
  the wrong reviewer. The pilot is void; rerun from a fresh session, with a
  new API approval.
- **Contaminating access** by either agent: the run is unusable as a
  blinded test; record it, and rule on a rerun.
- **The gate step fails or does not stage** (no image, a changed copy): the
  reviewer does not run and little is spent. Fix the cause, change the
  `run_id` (the staging folder must start empty), rebuild, and take a new
  API approval.
- **Tripwire at 1.5 times the estimate:** halt the workflow; a run stopped
  halfway is used up.

## Known limits of the blinding

- **Recorded paths.** Two reviewable records in the copy name the
  original attempt's location (`plan-approval.json`'s `plan_file`;
  `lane-records/build-01/build.json`'s build context). Following one is a
  contaminating access (checked with the lane's scan); the run notes tell
  the reviewer to resolve such paths against its review copy. Printing
  either with Bash gives a "named in command output" warning, ruled on the
  transcript.
- **The copy's reviewable files are readable.** They are byte-identical to
  the staged copy, so reading them conveys nothing; its withheld records,
  and the whole original attempt, are blinded.
- **The blinding instruction names the withheld records**, by design, so
  the reviewer knows what not to open.
- **The lane script is readable**: the gate step runs it. It names no
  outcome (checked 2026-10-30: only generic `attempt-04` examples in two
  docstrings).
- **Git history and PRs #13 to #15** describe the conclusions; neither is
  path-blinded, as for earlier runs. The audit flags blinded path names in
  command output, and the reviewer is told never to seek earlier reviews.

## Pre-run review

Two spawns in one stage, about ten to fifteen minutes. The handoff of
2026-10-30 asks for a pre-run review before the API gate; this brief covers
its artefacts, finished states, stop states, and verification stack, for
Shawn's explain-back.
