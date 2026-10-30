# Agentic reproduction lane — workflows and runbook

**Version:** 1.4 (2026-10-31, the review-only re-run, independent of the review it replaces; 1.3 2026-10-18, gate 1.3.2: target-scoped rulings and the adjudicated result; 1.2 2026-10-12, gate 1.3; 1.1 2026-10-04; 1.0 2026-10-03)
**Status:** built for the Phase 2 shakedown (`wiki/planning/agentic-modernisation-plan.md`
§5, Phase 2 option (a), approved 2026-10-02). It sits alongside the
session-per-phase human lane (`reproduction-system/prompts/`), which remains
available.

## What this is

The reproduction workflow from the modernisation plan (§4.2), built as two
Claude Code workflow scripts plus one deterministic tool:

| Piece | Role |
|---|---|
| `reproduction-plan.workflow.js` | Stage 1. One governed `reproduction-planner` spawn per paper. Plans come back for persistence and **batched human approval** (invariant 1). |
| `reproduction-execute.workflow.js` | Stage 2, approved papers only, pipelined per paper. `reproduction-executor` (Docker build, wrapper, run, comparison) → a mechanical **artefact gate** → a fresh-context `adversarial-reviewer` (invariant 4). |
| `scripts/reproduction-lane.py` | Everything the workflows cannot do, because workflow scripts have no filesystem access: commit-pinned args, plan persistence and triage, hash-bound approval, the artefact gate, result persistence, and the post-run audit. |

Two workflows rather than one: a human approval must sit between planning and
execution, and a workflow cannot pause for a person. Splitting at the approval
point turns invariant 1 into a structural property.

The three agent definitions (`.claude/agents/`; the versions are in
`manifest.yaml`; all pinned to `claude-opus-5-5`) receive their instruments by
the SubagentStart push hook, and their receipts are checked by the
SubagentStop gate, which serve this lane as they serve the FAIR lane. In the
workflow lane the stop gate's blocks are advisory (a block is logged but the
output is still collected), so `audit-run`'s re-validation is authoritative.

Gate 1.3 (`wiki/planning/reproduction-gate-1-3-design.md`) is what this
version describes: every run goes through `reproduction-lane.py
run-container`, which seals a run record, and admission to study data is
decided from those records, the transcript audit, the run audit, and human
rulings. Version 1.2 of this runbook was rewritten after the gate's final
review (2026-10-12), which found it still described gate 1.2 and ran
persistence before the audit that persistence needs.

## Runbook

Every step is a command an operator can re-run. `CFG` is the run
configuration (for the shakedown:
`studies/open-science-compliance/outputs/validation/phase2-shakedown/run-config.yaml`).
`SCRATCH` is a scratch directory outside the repository.

1. **Commit** everything the run depends on. The args builders refuse a tree
   with modified tracked files, because the launch commit must describe the
   bytes used.
2. **Plan args:**
   `venv/bin/python scripts/reproduction-lane.py build-plan-args --config $CFG --scratch-root $SCRATCH --out $SCRATCH/plan-args.json`
3. **API gate** (global rule): state the model, the number of spawns, and the
   estimated cost, and get explicit approval. State the estimate's time and
   cost with its basis (the plan's compute estimate, earlier attempts of the
   paper), because both vary from paper to paper. The run's tripwires derive
   from it: at the top of the estimate the operator checks progress, and at
   1.5 times the top the workflow is halted (Shawn, 2026-10-17).
   **Before a blinded run, scan the prompts** (Shawn, 2026-10-21). Render
   each agent's full prompt from the built args (the workflow script run
   with `agent()` stubbed to capture each prompt) and scan it against the
   run's blinding list. A blinded substring anywhere but the blinding
   instruction is a leak to remove, or a pointer an obedient agent would
   follow into a contaminating access; the gate 1.3.2 planner pilot had two
   such pointers before its launch.
4. **Run** `reproduction-plan.workflow.js` from the repository with the
   `Workflow` tool: `scriptPath` set to the committed file, `args` set to the
   builder's JSON, passed unedited. The builder stamps `args_checksum`. The
   workflow recomputes it over what it received and refuses to start on any
   difference, so a transcription slip cannot reach the agents.
   **Launch with a fixed, neutral message.** The harness relays the message
   that starts a workflow to every agent, ahead of the workflow's own
   instructions. Start each stage with exactly `Run the approved stage.`,
   and put no results, expectations, or opinions in that message: whatever
   it says reaches blinded agents. Launch only in direct reply to a typed
   approval, never after an answer given through a question tool, where
   what the harness relays is untested.
   **Launch from a fresh session** if agent definitions, hooks, or workflow
   scripts changed since the current session started
   (`docs/agent-guidance.md`, "Paid agentic runs").
   **During the run, leave the main checkout alone** until the authoritative
   gate (step 10) has run: no commit, pull, merge, or checkout. The agents
   load their definitions, hooks, and the lane script from it.
5. **Persist:**
   `venv/bin/python scripts/reproduction-lane.py persist-plans --config $CFG --run-dir <workflow run dir>`
   This writes `reproduction-plan.json` and `.md` into each attempt directory,
   plus `triage-<run>.md` beside the config. It validates every payload
   against the full plan schema and the plan-level checks.
   To re-plan an unapproved paper, run `supersede-plans --config $CFG --slug <slug>` (or
   `--all`) and commit before step 2. The old plan moves beside the run config, a blinded
   location, so the new planner cannot anchor on it.
6. **Batched approval** (human). Read the triage report and each
   `reproduction-plan.md`, then for each paper run:
   `venv/bin/python scripts/reproduction-lane.py approve --config $CFG --slug <slug> --decision approve|hold|reject --approver "<name>"`
   The approval binds to the plan file's sha256. An approved plan is locked:
   persist-plans and approve both refuse to replace it, because the target
   list is now the coverage denominator.
   Since gate 1.3.2 the plan quotes each lodged rule it relies on whole
   (`reproduction-system/lodged-rules.yaml`), and persist-plans and approve
   refuse a paraphrase, a missing condition, a target citing a rule it does
   not apply, and a condition that denies credit on a target planned
   creditable, and `unknown` on a condition the plan settles itself (such
   as whether a target's inputs come from executing the authors' code;
   Shawn, 2026-10-19). What they cannot check is whether each stated condition is
   true of the target's inputs: that is the approval's job. Read the plan's
   "Lodged rules applied" table against each target's method (for example,
   are T17's inputs really the authors' code's outputs?). A target planned
   not creditable is never credited by the gate. Approval never amends a
   rule; a rule that is wrong is changed where it was lodged.
7. **Commit** the plans and approvals.
8. **Execute args** (the executor builds its image with `reproduction-lane.py
   build-image`, which keeps the build log under `lane-records/build-NN/`):
   `venv/bin/python scripts/reproduction-lane.py build-exec-args --config $CFG --scratch-root $SCRATCH --out $SCRATCH/exec-args.json`
   Only papers with a committed approval whose hash still matches go in.
   Others are listed in `skipped`, never dropped silently.
   An attempt whose execution stopped partway is used up: the builder
   refuses only an attempt that already has `comparisons/comparison.json`,
   so do not re-run into one that holds a partial run's files. The next
   try is a new attempt.
9. **API gate** again (each stage is approved separately), then run
   `reproduction-execute.workflow.js` the same way, with the same launch
   message.
10. **Authoritative gate.** For each paper, re-run
    `venv/bin/python scripts/reproduction-lane.py check-attempt <attempt dir> --image <tag> --launch-commit <launch commit> --out <attempt dir>/gate-report.json`.
    This is the authoritative gate; the in-workflow gate is a relay.
    `--launch-commit` binds the anchors and run records to the commit the
    workflow ran from.
11. **Audit:**
    `venv/bin/python scripts/reproduction-lane.py audit-run --config $CFG --run-dir <workflow run dir>`
    It writes the workflow audit beside the config (receipts, blinding,
    writes outside scope, cost), and into each attempt the transcript audit
    (`transcript-audit.json`) and the run audit (`run-audit.json`): each
    governed role's verdict, the launch commit and plan it ran under, and
    flags for every escalation, review concern, and blinding warning. The
    run audit is bound to this workflow run, to each role's agent and
    accepted payload (by digest), and to the attempt state the in-workflow
    gate check recorded just before the review. It selects results as
    `persist-results` does and refuses two results for one paper.
12. **Human queue:** rebuild it from the authoritative records with
    `reproduction-lane.py human-queue --config $CFG --workflow-result <the
    workflow's result JSON> --out <file>`. It lists every failed gate and
    every issue from the gate report, the transcript audit, and the run
    audit, ruled or unruled, and exits 1 if a gate report is missing or the
    relay lost a flag. Never clear the queue from the relay alone.
13. **Rulings** (human): for each issue, record a decision with
    `reproduction-lane.py rule-flags --config $CFG --slug <slug> --approver "<name>" --rulings <file>`.
    A ruling binds to the issue's evidence fingerprint, so it lapses if the
    evidence changes. A blinding warning that says "possibly a blinded read"
    may be a real read the scan could not confirm (a `cd` in a branch Bash
    may skip, a fallback expansion such as `"${F:-x}"`): check in the
    transcript what the command opened before ruling it admissible. Each issue states its scope: `targets` (the ones it
    names) or `paper` (all of them). Since gate 1.3.2 a ruling can also
    dispose of single targets within its issue, `"targets": {"T17":
    "excluded"}`; record a ruled classification, `"classification":
    {"T03": "PAPER_ERROR"}`; and, on the review's verdict flag
    (`review:...`), set the ruled verdict, `"verdict": "SUCCESSFUL"`. The
    note must name each target singled out, and a ruling never creates
    credit: an outcome the comparison did not reproduce cannot be ruled into
    a reproduced one. Rule outcomes this way, never in the note alone, since
    the adjudicated result (step 15) reads only these fields. Whoever drafts
    the rulings drafts these parts with them, at ruling time, rather than
    restating a note afterwards (Shawn, 2026-10-21).
14. **Persist results:**
    `venv/bin/python scripts/reproduction-lane.py persist-results --config $CFG --run-dir <workflow run dir>`.
    It persists an attempt's payloads only when the attempt is
    eligible: a passing gate, a clean transcript audit, a run audit with
    both roles clean, and every issue ruled. The run audit must be the one
    for this workflow run and must have cleared these very results, and the
    attempt must be unchanged since the gate check that preceded its review:
    after a changed artefact, re-run the review, since re-auditing cannot
    supply a review of the new state. Rulings, the authoritative gate
    report, the audits, and the persisted results are not part of that
    state. To keep payloads before then, `--record-unruled` records them as
    ineligible, and a fresh `persist-results --force` is needed after the
    rulings.
15. **Adjudicate**, last:
    `venv/bin/python scripts/reproduction-lane.py adjudicate <attempt dir>`
    writes `adjudicated-result.json`, the attempt's result as study data
    reads it (gate 1.3.2). It records, per locked target, the credit, the
    ruled classification, and the rulings that set them, with the ruled
    coverage over every locked target and the verdict disposition; it keeps
    the gate's raw and pre-ruling coverage as history, and binds every record
    it was derived from by digest. It is written only when final: admission
    passes for the persisted results, every issue is ruled, and no rulings
    conflict. Writing it does not change the reviewed state. **Study
    reporting and export read this record, through `verify_adjudicated` (or
    `adjudicate --check`), and nothing earlier**: neither the comparison's
    outcomes nor the gate's coverage reflect the rulings. After any later
    ruling, adjudicate again, since the check refuses a stale record.

## Review-only re-run

`reproduction-review.workflow.js` (gate 1.3.2, criterion 4) re-reviews an
executed attempt with a fresh reviewer and no executor. The design, and
Shawn's rulings on it, are in `wiki/planning/reproduction-gate-1-3-design.md`
("The review-only mode as designed"). A review-only run takes its own run
configuration, with `mode: review-only`; the plan and execute builders
refuse that configuration, and `build-review-args` refuses any other.

It re-reviews only an attempt still exactly as its executor's run left it:
the attempt's run audit must have cleared its persisted executor result,
clean, for the attempt as it stands. A changed comparison is refused,
because corrections go into new attempts (Shawn, 2026-10-13). The steps
follow the main runbook, with these differences:

1. **Review args:**
   `venv/bin/python scripts/reproduction-lane.py build-review-args --config $CFG --scratch-root $SCRATCH --out $SCRATCH/review-args.json`
   binds each attempt's executor result (its run, workflow run, agent,
   payload digest, and launch commit) and names a fresh review folder
   under the scratch root. It refuses an executor record persisted
   ineligible: finish that run's rulings and its `persist-results --force`
   first.
2. **API gate**, then run the workflow as in step 4. Launch from a fresh
   session after any change to agent definitions, hooks, or workflow
   scripts.
3. In the workflow, the gate step runs `check-attempt` with the
   **executor's** launch commit, since the sealed run records are checked
   against it, and then `stage-review <attempt> --to <review folder>`.
   That copies the reviewable state and the gate report, checks the copy's
   digest against the attempt's, and prints the staging record, so the
   harness records the copy the reviewer was handed. The reviewer reads
   only the copy, named in its prompt as `Review copy:`. The executor's
   report, the earlier review, the rulings, the audits, and the
   adjudicated result are withheld. So is anything derived from the
   rulings: the copied gate report's admitted coverage is recomputed with
   no rulings (lane v1.9), so the reviewer meets every issue unruled, as a
   first reviewer does, and never learns what a human admitted with the
   replaced review in hand. The attempt's own gate report keeps the ruled
   figure for the operator.
4. **Authoritative gate** as in step 10, with the executor's launch commit.
5. **Audit** as in step 11, **before clearing the scratch folder**. The run
   audit (1.2) carries the executor's clearance from the attempt's earlier
   run audit, which moves to `superseded/<its workflow run>/`. The reviewed
   state is the successful staging record's, never a `check-attempt`
   digest, and the audit re-hashes the staged copy and its gate report and
   checks the reviewer was handed that copy; admission needs it verified.
   It also fails a staged gate report that counts any issue as ruled.
   A later re-audit of the same run that finds the copy gone keeps that
   first verification, so the scratch folder may be cleared once this audit
   has passed; a copy still there but changed fails.
6. **Human queue** and **rulings** as in steps 12 and 13. **Every issue
   needs a new ruling** (Shawn, 2026-10-31). Rulings follow the review:
   obligations are discharged on its findings, and rulings on the
   executor's own issues have cited them too, while a ruling's note cannot
   show which did. So once the audit makes this review the review of
   record, every issue the attempt holds (the gate's flags and
   obligations, the transcript audit's, and the executor's) is bound to
   this review's identity, as its own concerns, method rows, and verdict
   flag are (lane v1.9). Rule each against the new review; where an
   earlier decision still holds, restate it, with a note saying it was
   checked against the new review. The earlier rulings stay in the
   rulings file as history. A re-audit of the same run keeps the new
   rulings.
7. **Persist results** as in step 14. Only the review is persisted. The
   review it replaces, and the adjudicated result derived from that
   review, move to `superseded/<their workflow run>/`. Admission binds the
   executor from its persisted record and the reviewer from this run.
8. **Adjudicate** as in step 15. The result names the review's run as
   `review_run`.

## Where each invariant is enforced

| Invariant | Mechanism |
|---|---|
| 1 Plan approval before compute | Separate workflows; `approve` binds the plan sha256; `build-exec-args` refuses unapproved, changed, or uncommitted plans; the executor re-verifies the hash first |
| 2 Wrapper cardinal rule | Executor instrument and brief; every modification is self-reported with `changes_what_is_computed`; the reviewer audits scripts. `check-attempt` (gate 1.3) reads `authors-code-manifest.json`: every executed authors' file must be byte-identical to its hash at retrieval, anchored to a committed record the executor did not write, and every other code file in the attempt must be a declared wrapper. Each run's sealed record (`run-container`) holds the hook's account of every file R loaded and every text it evaluated, which the gate matches to the originals and wrappers. A declared edit, and anything the gate cannot settle, becomes an issue for a human ruling; what it cannot see (wrapper semantics, dynamic evaluation, content fetched into the image) becomes a review obligation. `pass` means only that every code file is accounted for. |
| 3 Every target accounted for | `check-attempt`: one record per locked target id in `comparisons/comparison.json`, no extras; coverage recomputed from outcomes |
| 4 Fresh-context review for every paper | The reviewer runs for every paper whose executor returned, gate pass or fail; artefacts-only tools; blinded from earlier attempts |
| 5 Docker only | Every run goes through `run-container`, which records it; the transcript audit (`transcript-audit.json`, spec §12) treats a direct `docker run`/`exec`/`cp`/`compose`, a write into the lane's records or outputs, and a host run of authors' code after the final run as hard failures, and an earlier host run as a flag |
| 6 Persistence verified, not asserted | `check-attempt` reads the disk; the executor's `artefacts_written` is never trusted; `persist-results` admits only eligible attempts |

## Known limits

- **Blinding is instruction plus detection, not prevention.** The harness
  cannot path-scope reads at spawn (amendment 2 §4). `audit-run` scans every
  transcript (Read, Grep, and Glob paths, and every token of Bash commands,
  bare names included, also placed under a `cd` earlier in the same command;
  URLs are excluded) and reports contaminating accesses. Since blinding scan
  1.1 (lane v1.7), a match in a command is contaminating when scan 1.0 would
  have found it (a word holding a `/`, or ending in `.json`, `.md`, or
  `.csv`), or when its word is a path argument (of `ls`, `cat`, `cd`, and
  the like, or a file argument of `grep`, `sed`, or `awk`) at a location the
  walk is sure of. Any other match, such as a pattern, an option's value,
  literal text, a path under an uncertain directory, or an argument whose
  expansion the walk cannot resolve (`"${F:-x}"`, `"$(...)"`, a variable set
  in a branch that may not run), is a warning for human review (Shawn,
  2026-10-30, refined by role after Astra's review and re-checks). The walk
  follows every state the shell can be in (its directory, its variables,
  and the last command's status): a command after `&&` or `||` runs only
  in the states where it would, `cd` and assignments are assumed to
  succeed, `true`, `:`, and `false` have known statuses, and any other
  command may do either. A match is an access when the command reads a
  blinded path in every state it runs in, and a warning ("possibly a
  blinded read") when in only some. A subshell or command substitution
  keeps its directory and variables to itself. Blinded paths named in command output are
  warnings for human review; blinded names listed bare in output (an `ls`
  of a parent directory) are recorded in the audit, with no ruling (Shawn,
  2026-10-30). Not detected: a recursive read of a blinded directory's
  parent (`grep -r x outputs/`) whose output names no blinded path; a path
  built by command substitution; and a `cd` or a read inside a heredoc fed
  to a shell (`bash <<EOF`), whose words are judged as text but whose
  directory changes are not followed.
- **The receipt gate's `schema_version` check is FAIR-specific**
  (`subagent-receipt-gate.py` compares any declared `schema_version` with the
  benchmark contract). The reproduction schemas therefore carry no
  `schema_version` field. Their contract versions are recorded in the
  manifest, and `audit-run` validates payloads against the full registered
  schemas instead. A per-agent schema map in the gate is the clean follow-up.
- **Mechanical gate relay.** The in-workflow gate is a cheap agent running
  `check-attempt`, because workflow scripts cannot run commands. Its relay
  is advisory: its flags and warnings are required fields, and the queue
  fails closed when they are missing, but a relay could still return an
  empty list wrongly. Step 10's operator re-run is authoritative, and step
  12's `human-queue` reconciles the two.
- **What gate 1.3 cannot prove.** The limits are listed in the design's
  §14. In short: a re-implementation spelled differently from the authors'
  code, content fetched into the image at build time, and wrapper semantics
  stay the reviewer's obligations, and blinding remains instruction plus
  detection. A wrapper that runs an original statement by statement does it
  through the hook's `run_file` evaluator, which records every statement it
  parsed and ran; the old pattern, a wrapper's own `parse(file =)` loop, is
  flagged `parsed-not-run` (the final review's A-new-1; see
  `wiki/planning/reproduction-gate-1-3-final-review-brief.md`).
- **Executor permissions.** The executor writes files and runs Docker and
  network commands from inside a workflow. Check that the session's
  permission settings allow this before stage 2, or spawns will stall on
  prompts.
