# Gate 1.3.2 planner pilot: API-gate brief and launch checklist

**Prepared:** 2026-10-21 (Claude, Opus 5.5), on main after PR #13 merged
(`df394c1`). **Status:** not approved and not launched. Shawn approves at the
API gate, from a fresh Claude Code session.

**Why this run.** Gate 1.3.2's criterion 3 changed what the planner writes:
plan schema 1.1, reproduction-planner v1.4, plan workflow v1.1, and the
lodged-rule registry in the planner's prompt. The design's §2.2 asks one
real run of such a change, and attempt 04's locked plan cannot provide it.
Astra's scope for criterion 4 (her review of 2026-10-19, recorded in the
design's gate 1.3.2 note) asks for this pilot. Configuration:
`run-config.yaml` beside this file.

## What runs

| Item | Value |
|---|---|
| Workflow | `reproduction-system/workflows/reproduction-plan.workflow.js` v1.1 (stage 1 only) |
| Paper | herskind-riede-2024, new attempt 05 |
| Agent and model | `reproduction-planner` v1.4, `claude-opus-5-5`, effort high |
| Mode | real-time workflow on the Max plan, priced API-equivalent; not batch |
| Spawns | 1 governed planner (no executor, no reviewer, no Docker) |
| API requests | one per agent turn, estimated 15 to 25 |
| Estimate | $1.20 to $1.80 API-equivalent; 6 to 12 minutes |
| Tripwires | check progress at $1.80 or 12 minutes; halt at $2.70 or 18 minutes |

**Basis.** Gate 1.3.1's stage 1 on this paper (`wf_db7d121a-5d5`, audit
`../gate-1-3-1-pilot-rerun/audit-wf_db7d121a-5d5.json`): $1.2969, 17
requests, 436.5 seconds, 20,303 output tokens, 1.51 million input-side
tokens. This run adds the lodged-rule block to the prompt (10 rules, about
2,000 tokens, cached across turns) and the `rules_applied` output (a few
thousand output tokens). The tripwires follow the runbook's rule: check at
the top of the estimate, halt at 1.5 times it.

## Launch checklist (in a fresh session)

A fresh session loads reproduction-planner v1.4 from main. This session's
agent definitions may predate the merge; a planner on v1.3 would receipt the
wrong agent version and the audit would reject the run.

1. `git fetch`, then confirm main is level with origin and contains
   `df394c1` and this configuration's commit; the tracked tree is clean.
2. Confirm the definition on disk:
   `grep -c "agent definition v1.4" .claude/agents/reproduction-planner.md`
   (expect 1) and `venv/bin/python scripts/check-manifest-consistency.py`.
3. Build the args (no API cost):
   `venv/bin/python scripts/reproduction-lane.py build-plan-args --config studies/open-science-compliance/outputs/validation/gate-1-3-2-planner-pilot/run-config.yaml --scratch-root ~/scratch/llmr-runs --out ~/scratch/llmr-runs/gate-1-3-2-planner-pilot-2026-10/plan-args.json`.
   Check the args carry `lodged_rules` (10 rules) and `lodged_rules_sha256`.
   If a commit moves `HEAD` after this, rebuild.
4. API gate: present this table with the args checksum; Shawn approves.
5. Launch: the Workflow tool with `scriptPath` set to the committed workflow
   file and `args` set to the built JSON, unedited. The launch message is
   Shawn's plain go-ahead (decided 2026-10-17); the audit raises one flag on
   any message other than the runbook's fixed phrase, for Shawn to rule.
6. Watch the tripwires. Then, in order:
   - `persist-plans --config <cfg> --run-dir <workflow run dir>`;
   - `audit-run --config <cfg> --run-dir <workflow run dir>`: receipts valid
     (`agent_version` "reproduction-planner v1.4"), no contaminating access,
     no writes outside scope;
   - read the triage report and `attempt-05/reproduction-plan.md`.

## Acceptance (Astra's scope)

1. **Persisted normally.** `persist-plans` writes the plan, its view, and
   the triage report, with no blocking rule problem. A block is itself a
   finding about the planner contract: record what the planner got wrong.
2. **Rules quoted and applied.** Every rule a target relies on or names is
   in `rules_applied`, quoted whole; every listed condition is stated with
   evidence; no plan-settled condition is `unknown`.
3. **The approver's explicit check.** Find the target corresponding to
   attempt 04's T17, the named value that the Ertebølle-cluster ornament
   strings occur on only ten objects (p. 7, Section 5); it may carry another
   id. Check its input provenance against Q5's condition "it is credited
   only where its inputs come from executing the authors' code". Attempt
   04's plan tested it with an S1 lookup of objects bearing at least two of
   the five cluster motifs, a selection rule inferred from Table 3, so its
   inputs were deposited data, not outputs of the authors' code. If this
   plan's method is the same, the condition is `no` and the target must be
   `not-creditable`. A `yes` needs evidence that is true of the method.
   Record the decision with `approve` (approve or hold): it re-runs the
   rule checks on a real plan and binds the registry's sha256, which is
   criterion 3's approval step exercised live. No execution follows.
4. **No silent correction.** An unsupported creditable or unknown answer is
   a pilot finding, recorded as found, never corrected by the orchestrator.
5. **Then the mechanical fixture.** Take the plan's actual not-creditable
   application into an isolated, labelled fixture, and show the gate and
   adjudication exclude that target against a reproduced outcome. Never
   attach the new plan to attempt 04's execution and call it a live
   execution under the new plan.

## Stop states

- **Receipts invalid** (for example `reproduction-planner v1.3`): the
  session loaded the old definition. The pilot is void; rerun from a fresh
  session, with a new API approval.
- **Contaminating access** in the audit: the plan is unusable as a blinded
  test; record it, and rule on a rerun.
- **Tripwire at 1.5 times the estimate:** halt the workflow; a run stopped
  halfway is used up (the stage 2 pre-run review's rule).

## Known limits of the blinding

- The planner's own definition (v1.4) states the general lesson: "in the
  gate 1.3.1 pilot a plan stated Q5's consequence without its input
  condition". It names no paper or target. That is the contract under
  test, not a leak of the answer, but a planner is primed by it.
- The registry gives R1 to R4's source as the shakedown run configuration,
  under `outputs/validation/`, which is blinded. The full rule text is in
  the prompt, so the planner never needs the file; opening it would be a
  contaminating access.
- Git history and PR #13 describe the conclusions. Neither is path-blinded;
  the audit flags blinded path names in command output, and the planner is
  told never to seek earlier attempts.
- `manifest.yaml`'s pilot statistics (herskind: successful, from attempt
  01's human lane) were visible to earlier planners too.

## Pre-run review

This is one spawn in one stage, about ten minutes. The standing rule asks
for the full pre-run review with Shawn's explain-back before a paid
multi-agent stage, which this is not; this brief covers its artefacts,
finished states, and stop states. Shawn may still ask for the full review.
