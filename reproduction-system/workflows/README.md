# Agentic reproduction lane — workflows and runbook

**Version:** 1.0 (2026-10-03)
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

The three agent definitions (`.claude/agents/`, v1.1, pinned to
`claude-opus-5-5`) receive their instruments by the SubagentStart push hook,
and their receipts are checked by the SubagentStop gate. Both hooks are
unchanged and serve this lane exactly as they serve the FAIR lane.

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
8. **Execute args:**
   `venv/bin/python scripts/reproduction-lane.py build-exec-args --config $CFG --scratch-root $SCRATCH --out $SCRATCH/exec-args.json`
   Only papers with a committed approval whose hash still matches go in.
   Others are listed in `skipped`, never dropped silently.
9. **API gate** again (each stage is approved separately), then run
   `reproduction-execute.workflow.js` the same way.
10. **Verify and persist:** for each paper, re-run
    `reproduction-lane.py check-attempt <attempt dir>`. This is the
    authoritative gate; the in-workflow gate is a relay. Then run
    `persist-results` and `audit-run`.
11. **Human queue:** the workflow's `human_queue` must be cleared before any
    result enters study data (plan §4.4). It lists ESCALATE outputs, failed
    gates, QUALIFIED or CHALLENGED reviews, and PAPER_ERROR or CANNOT_COMPARE
    calls.

## Where each invariant is enforced

| Invariant | Mechanism |
|---|---|
| 1 Plan approval before compute | Separate workflows; `approve` binds the plan sha256; `build-exec-args` refuses unapproved, changed, or uncommitted plans; the executor re-verifies the hash first |
| 2 Wrapper cardinal rule | Executor instrument and brief; every modification is self-reported with `changes_what_is_computed`; the reviewer audits scripts |
| 3 Every target accounted for | `check-attempt`: one record per locked target id in `comparisons/comparison.json`, no extras; coverage recomputed from outcomes |
| 4 Fresh-context review for every paper | The reviewer runs for every paper whose executor returned, gate pass or fail; artefacts-only tools; blinded from earlier attempts |
| 5 Docker only | Executor brief; `check-attempt --image` confirms the image exists; the reviewer's methodological-soundness dimension |
| 6 Persistence verified, not asserted | `check-attempt` reads the disk; the executor's `artefacts_written` is never trusted |

## Known limits (v1.0)

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
  is advisory; step 10's operator re-run is authoritative.
- **Executor permissions.** The executor writes files and runs Docker and
  network commands from inside a workflow. Check that the session's
  permission settings allow this before stage 2, or spawns will stall on
  prompts.
