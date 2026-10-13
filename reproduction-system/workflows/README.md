# Agentic reproduction lane — workflows and runbook

**Version:** 1.2 (2026-10-12, gate 1.3; 1.1 2026-10-04; 1.0 2026-10-03)
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
   estimated cost, and get explicit approval.
4. **Run** `reproduction-plan.workflow.js` from the repository with the
   `Workflow` tool: `scriptPath` set to the committed file, `args` set to the
   builder's JSON, passed unedited. The builder stamps `args_checksum`. The
   workflow recomputes it over what it received and refuses to start on any
   difference, so a transcription slip cannot reach the agents.
   **Launch with a fixed, neutral message.** The harness relays the message
   that starts a workflow to every agent, ahead of the workflow's own
   instructions. Start each stage with exactly `Run the approved stage.`,
   and put no results, expectations, or opinions in that message: whatever
   it says reaches blinded agents.
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
7. **Commit** the plans and approvals.
8. **Execute args** (the executor builds its image with `reproduction-lane.py
   build-image`, which keeps the build log under `lane-records/build-NN/`):
   `venv/bin/python scripts/reproduction-lane.py build-exec-args --config $CFG --scratch-root $SCRATCH --out $SCRATCH/exec-args.json`
   Only papers with a committed approval whose hash still matches go in.
   Others are listed in `skipped`, never dropped silently.
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
    evidence changes.
14. **Persist results:**
    `venv/bin/python scripts/reproduction-lane.py persist-results --config $CFG --run-dir <workflow run dir>`,
    last. It persists an attempt's payloads only when the attempt is
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
  transcript (Read, Grep, and Glob paths, and the path-like tokens of Bash
  commands; URLs are excluded) and reports contaminating accesses.
  Mentions of blinded paths in command output are warnings for human review.
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
