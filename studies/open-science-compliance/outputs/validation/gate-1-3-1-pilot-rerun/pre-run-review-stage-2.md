# Pre-run review: stage 2 of the gate 1.3.1 pilot re-run

Run `gate-1-3-1-pilot-rerun-2026-10`, herskind-riede-2024 attempt 4, stage 2
(execute: executor, Haiku gate step, adversarial reviewer). Workflow
`reproduction-system/workflows/reproduction-execute.workflow.js`; run
configuration `run-config.yaml` in this folder. Reviewed with Shawn using the
`pre-run-review` skill, 2026-10-13 (sections) and 2026-10-17 (his
explain-back and decisions); recorded by Claude (Opus 5.5).

This record sits beside the run configuration on purpose: `outputs/validation/`
is a blinded path, so no agent in the run can read it. The stage-2 arguments
are rebuilt at the commit that adds this file. `wiki/continuity.md` records
that launch commit after the run, since H1 forbids commits during it.

## Pre-launch checks

Run 2026-10-13 at `a19cb62`, and repeated just before launch; the repeat's
results go into continuity after the run. No API cost.

| Check | Result (2026-10-13) |
|---|---|
| Test suite on main | 699 passed, none failed |
| Docker on amd-tower | 29.2.1 running; only the Syncthing container active |
| Disk | 35 GB free (93% used) |
| attempt-04 | Only the plan, its Markdown, and the approval, all committed |
| Image `llmr-herskind-riede-2024-attempt-04` | Not yet built |
| Zenodo record 10801706 | Reachable (HTTP 200) |
| Anchor registry | herskind entry pinned to `10.5281/zenodo.10801706` (`corpus/evidence-packs/declared-links.yaml`) |

## The operator's explain-back (Shawn, 2026-10-17, verbatim)

> stage 2 inventories Herskind's components, builds an execution environment,
> test the setup, run the reproduction, documents the setup, and confirms
> successful completion.
>
> stops when verified complete, or there is an error or surprise, order
> error, or we stop it. I would like to extend the stop list to cover cost
> and time overruns.
>
> At end Theres a confirmation check and a report.

Gaps filled in by Claude, for Shawn to confirm:

- **The core step is the comparison.** The executor compares reproduced
  values with the 18 locked targets of the approved plan and reaches a
  verdict (SUCCESSFUL, PARTIAL, FAILED, or BLOCKED). The run reports a
  verdict; it does not confirm success.
- **Two checks follow the executor:** the Haiku gate step (a mechanical check
  of the artefacts) and the adversarial reviewer (fresh context, artefacts
  only), which tries to refute the verdict.
- **Two stop classes not named:** substitutes (an input other than the one
  specified, such as Zenodo version 1 or another host) and environment (the
  machine, permissions, and this session staying open).
- **After the run:** the authoritative gate check, the PR #12 merge, the
  audit, the human queue, Shawn's rulings, and persistence (H2).

## Hardenings

**H1. No-touch window.** From launch until the authoritative `check-attempt`
has run, nothing touches the main checkout: no commit, pull, merge, or
checkout, continuity notes included. The agents load their definitions,
hooks, and the lane script from it, and the executor writes into it.

**H2. Post-run order, with PR #12 placed.**

1. `check-attempt` with `--launch-commit` (the authoritative gate)
2. Merge PR #12 (per-request pricing, lane v1.5), with Shawn's approval.
   Astra approved head `154b637` on 2026-10-13
   (`2026-10-13-codex-pr12-closure-review.md`: both findings closed, no
   remaining blocker). The merge is safe here: PR #12 changes only
   `manifest.yaml`, the lane script, this configuration's pricing rows, and
   tests. It does not touch the anchor registry, which the gate binds at the
   launch commit, and `audit-run` checks receipts against the manifest at the
   launch commit.
3. `audit-run`
4. `human-queue`, written beside this configuration, never into the attempt
5. Rulings (at least one: the launch message, H6)
6. `persist-results`

**H3. Cost and time overruns stop the run (Shawn, 2026-10-17).** Cost and
time vary from paper to paper, so no fixed figure is general. The general
rule: each stage's API gate states its own time and cost estimate with its
basis, and the tripwires derive from that statement. At the top of the
estimate, Claude checks progress and tells Shawn; at 1.5 times the top, Claude
halts the workflow and reports.

This run's estimate and basis:

- **Time 45 to 90 min.** Attempt-03's execute stage took 42 min
  (`wf_7c18dfdc-298`), but this plan budgets 0.5 to 1 h for the image build
  alone (`reproduction-plan.md`, compute strategy). Check at 90 min; halt at
  135 min.
- **Cost $13 to $18 API-equivalent.** Attempt-03's execute stage priced at
  $12.74 across its three agents ($10.4571, $2.273, $0.0074, re-priced under
  PR #12). Check at $18; halt at $27.

Mechanism: a read-only watcher, run in the background from launch, prices the
run's agent transcripts with the lane's own `transcript_usage` and
`price_usage` every minute and exits when a threshold is crossed, which
re-invokes the session. Checked against stage 1 (`wf_db7d121a-5d5`): $1.30,
against the audited $1.2969. Before PR #12 the watcher cannot price the Haiku
step (about $0.01), which runs after the executor. A lane subcommand for this
is a follow-up.

**H4. A run that stops halfway uses up the attempt.** The args builder refuses
a re-run only when `comparisons/comparison.json` exists
(`scripts/reproduction-lane.py`, `cmd_build_exec_args`). If stage 2 stops
before that file exists, attempt-04 is used up: no re-run goes into it, and
the next try is a new attempt, decided with Shawn. Follow-up PR: the builder
refuses an attempt that holds any execution artefact.

**H5. A material difference from attempt-03 is a finding.** Attempt-03's
execute stage reached SUCCESSFUL. If attempt-04's verdict or coverage differs
materially, Claude compares the two target by target before any ruling and
brings the comparison to Shawn.

**H6. Launch message: a plain go-ahead.** The harness relays the message that
starts the workflow to every agent, as the only user voice, above the
workflow's own instructions. Shawn launches with a plain go-ahead in his own
words, made only of approval words (go, yes, ok, approved, launch, run, and
the like). Claude checks the message against that rule before launching and
launches only in direct reply to such a typed message, never after an answer
given through the question tool: what the harness relays in that case is
untested, and could be an earlier message. Today's run audit flags any
wording other than the runbook's fixed phrase, and Shawn rules it once in
step 5 of H2. The word rule itself goes into a PR after the pilot.

**H7. Environment: amd-tower, as the approved plan says.** The locked plan
states "Run on this machine only, through run-container. No run is sent to
sapphire" (`reproduction-plan.md`, compute strategy). On 2026-10-17 Shawn
reported sapphire fixed and asked to move runs there. `run-container`
bind-mounts local paths into the container, so a remote Docker host cannot
see the attempt; runs on sapphire need a session running on sapphire, or lane
support for a remote host. Attempt 4 therefore runs on amd-tower unless Shawn
decides otherwise (which would mean a re-plan). Keep this session open and
the machine awake. If the executor goes quiet early, around its first
`build-image`, suspect a permission prompt.

## Not done, and why

The skill's clean-context agent pass was not run. Its purpose is to audit new
contract code; PR #11's code had several review rounds with Fable and Astra,
and this pilot run is itself its test.

## Changelog

- 2026-10-17: created after the review dialogue (2026-10-13) and Shawn's
  explain-back and decisions (2026-10-17).
