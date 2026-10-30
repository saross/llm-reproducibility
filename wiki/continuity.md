---
title: "llm-reproducibility — Continuity (Living Doc)"
tags: [infrastructure, coding-practices]
created: 2026-06-07
updated: 2026-10-23
status: active
---

# llm-reproducibility — Continuity (Living Doc)

**Purpose:** cross-session state, pending work, and a session-by-session log
for this repo. Updated in place at session end (no new file per session).

**Status: ACTIVE** (promoted from seed 2026-07-06). The four-artefact wiki
layout is fully in place (migration completed 2026-07-03, task B below):
continuity, working-notes, reflections/, user-observations, claude-observations,
and planning/ all live under `wiki/`; `docs/` stays at repo root as product
documentation (decided 2026-07-03). This file was created 2026-06-07 as the
migration seed, from a session working primarily in the
`2026-mq-llm-dh-judgement-paper-b` repo (the matching-grade PDF extractor
merged here as PR #1).

**How to update at session end** (per the canonical convention —
`~/personal-assistant/global-claude-md/handoff-protocol.md`):

1. Mark done items in place: `[ ]` → `[x] YYYY-MM-DD`; never delete.
2. Add new items as `[ ]` with a brief note.
3. Append a new "Session log" entry at the bottom (most recent first).
4. Carry forward open questions.

---

## Repo state (2026-10-09, session be70c3be, Shawn's rulings) — START HERE

- **⏩ NEXT SESSION (from the 2026-10-23 handoff, session a9c4834d). Shawn
  works from zbook for the week of eResearch Australasia.** The gate 1.3.2
  planner pilot is run, ruled, held, fixtured, and mailed to Astra; the
  record is
  `studies/open-science-compliance/outputs/validation/gate-1-3-2-planner-pilot/results-2026-10-21.md`.
  Criterion 4 now waits on Astra's reply. Work that does not wait on her
  is listed below. Fable is still rationed; reviews go to Astra.
  - [ ] **On zbook, first (Shawn, once): `sudo apt install docker-buildx`.**
    zbook's Docker (Ubuntu `docker.io` 29.1.3) has no buildx plugin, so the
    lane's `docker build --progress=plain` (`build_image` in
    `scripts/reproduction-lane.py`) exits 125 and
    `tests/test_run_container.py::BuildImageDockerTests` fails. The
    pre-commit hook runs the whole suite, so **every commit on zbook is
    blocked until it is installed**; never use `--no-verify`. Afterwards
    `venv/bin/python -m pytest -q` should pass, with the seven
    launcher-matrix tests skipping (no `llmr-launcher-matrix:4.3.2` image
    on zbook).
  - **zbook was synced on 2026-10-23** (session a9c4834d, from amd-tower
    over SSH): clone fast-forwarded from `e3fd5b2` and level with origin;
    pre-commit hook re-installed with `scripts/install-git-hooks.sh` (it
    was the 24 July version); venv matched to amd-tower's package set
    (`pytest` and `openpyxl` were missing); corpus store copied to
    `~/corpora/llm-reproducibility` (`fetch-corpus.py verify`: 18/18 and
    16/16 files OK) with the `corpus/store` link. Every branch, worktree,
    and stash on amd-tower was checked: nothing unpushed.
  - **Agent mail lives on amd-tower only.** `~/agent-mail` is not a git
    repository and not in Syncthing, zbook has no copy (checked
    2026-10-23), and Astra runs on amd-tower, where Shawn wakes her. On the
    home network, zbook reads it over SSH
    (`ssh amd-tower 'ls -t ~/agent-mail/codex/outbox/claude/ | head'`;
    worked 2026-10-23). **Away from home it is unreachable from zbook**:
    amd-tower is `192.168.1.70`, and neither machine runs a VPN. During
    the conference, Astra's reply is readable only through a
    remote-control session on amd-tower, or once Shawn is home; zbook
    sessions take the work that does not wait on her.
  - [ ] **Astra's reply** to
    `~/agent-mail/claude/outbox/codex/20261021T125238.665157Z-claude-gate132-planner-pilot-results.md`
    (on amd-tower): (1) does route A close check 5's mechanical half;
    (2) is the long-term fix sound, and is it a gate 1.3.2 addendum or
    gate 1.3.3; (3) does the delta since `67569cb` reopen anything.
  - [ ] **The long-term fix**, after her scoping (branch + PR): the
    registrant's reading of `inputs-from-authors-code`, **text approved by
    Shawn on 2026-10-21** and quoted in the results doc, into the registry
    beside the condition; per-input lineage declared by the plan, the
    condition derived by the lane, and "computed by" citations of load-only
    lines refused; no credit on a reading put to the approver; optionally
    a fresh-context verifier; the T15 application as a negative fixture.
    Then a re-plan under its own API gate, estimated from this run's basis
    ($2.59, 73,985 output tokens).
  - [ ] **Not waiting on Astra (suggested order):** (1) the operational
    follow-up PRs below, each on a branch + PR, starting with the blinding
    audit gap (a bare-name Bash read of a blinded file is missed outright),
    since it guards the re-plan; (2) the review-only mode (branch + PR,
    Astra's review), then the reviewer-only pilot on attempt 04 at the API
    gate.
    - [x] 2026-10-30 `docker-buildx` installed on zbook (Shawn); 771 pass,
      7 skip.
    - [x] 2026-10-30 **The blinding audit gap: PR #14 merged** (`1b91eb5`,
      with Shawn's approval, after Astra approved `d7ecf0d`) (session 789afcf9,
      branch `fix/blinding-bare-names`, `0d2b0cf` and `7876470`; lane v1.7,
      blinding scan 1.1). Shawn's tiering (2026-10-30): a Bash match is
      contaminating only when its word is evidently a path, otherwise a
      warning; bare names in output are `noted`, with no ruling. **Awaiting
      Astra's review**, which Shawn relays by hand while on zbook (request
      text in that session's scratchpad, `astra-review-request-pr14.md`;
      file a copy in `~/agent-mail/claude/outbox/codex/` once on
      amd-tower). Merge after her review.
      - [x] 2026-10-30 Astra's review at `7876470` (pasted by Shawn):
        changes requested, four findings (the harness-file exemption's
        directory form; subshell scopes, both directions; clustered value
        options; file-name suffixes over roles), all closed at `b23ef4f`
        (`1b93991`, `31892ad`). Shawn ruled roles replace the
        "file name with an extension" leg. Her probes, run from a copy at
        `1b93991`, give the intended results; parity holds (1,152 cases).
        PR comment posted with Shawn's approval (issuecomment-6514208269).
      - [x] 2026-10-30 **Astra's re-check at `b23ef4f`** (pasted by
        Shawn): the exemption and option findings closed; three residual
        false blocks (R1, a `cd` or assignment in a branch Bash may skip;
        R2, awk `name=value` operands; R3, unresolved expansions such as
        `"${F:-x}"`), all closed in `774bddf`, regression test `b2c9586`.
        Her unmodified harness passes at `774bddf` (nine tests, 1,152
        parity cases, original and residual Bash fixtures); 778 pass.
      - [x] 2026-10-30 **Possible reads labelled** (`fac4805`, after a
        side agent's note): a warning on a path argument the scan could
        not resolve says "possibly a blinded read" and to check the
        transcript before ruling; the runbook's rulings step says so.
      - [x] 2026-10-30 Astra's re-check at `b2c9586` (pasted by Shawn): R2
        and R3 closed; R1 open in two modes (a condition lost across an
        assignment, a regression; a skipped branch overwriting the state
        Bash kept, a miss). Closed in `f5dcb7b` by replacing the
        certainty flags with a walk over every possible shell state
        (directory, variables, last status): an access only when the
        command reads a blinded path in every state it runs in; `true`,
        `:`, and `false` known. Her full final-check harness passes (twelve
        tests, 1,152 parity cases, all three Bash fixture sets); 779 pass.
      - [x] 2026-10-30 Astra's re-check at `f5dcb7b` (pasted by Shawn): a
        pipeline skipped by the && before it revived the skipped states
        (six of her 160 Bash state cases). Closed in `d7ecf0d`: a pipeline
        runs whole where its first command runs, and only its last
        command's status reaches those states. Her harness, unmodified:
        thirteen tests, 1,152 parity cases, all fixture sets, and 160 state
        cases with 0 failures; 780 pass.
      - [x] 2026-10-30 Astra's re-check at `d7ecf0d`: **approved** (14
        focused tests, 1,152 parity cases, 25 earlier Bash fixtures, all
        160 state cases).
      - [ ] **File in agent mail once on amd-tower:** her five PR #14
        reviews (pasted into session 789afcf9) and Claude's replies
        (`astra-review-request-pr14.md`, `astra-reply-pr14-closure.md`,
        `astra-reply-pr14-recheck.md`, `astra-reply-pr14-states.md`,
        `astra-reply-pr14-pipelines.md` in that session's scratchpad).
    - [x] 2026-10-30 **The review-only mode: PR #15 merged** (`37a3fe7`,
      with Shawn's approval, after Astra approved `4e490b3`) (session 789afcf9, branch
      `feat/review-only-mode`, `c601fe3` and `d02e75b`; lane v1.8, run
      audit 1.2, `reproduction-review.workflow.js` v1.0). Shawn's choices
      (2026-10-30): the pilot reviews a labelled copy of attempt 04 (its
      13/18 untouched), and the reviewer reads a clean staged copy. Design
      in `wiki/planning/reproduction-gate-1-3-design.md`, "The review-only
      mode as designed". Also fixes a gate 1.3.2 defect: re-gating any
      adjudicated attempt failed (`DOCUMENT_NAMES` lacked
      `adjudicated-result.json`). **Awaiting Astra's review**, relayed by
      hand (`astra-review-request-review-only-mode.md` in that session's
      scratchpad; file a copy in agent mail once on amd-tower). Whichever
      of #14 and #15 merges second needs a rebase (lane header, manifest).
      - [x] 2026-10-30 Astra's review at `d02e75b` (pasted by Shawn):
        changes requested, four findings (the executor's cleared state
        relabelled by a later review; a fresh reviewer inheriting earlier
        rulings; the staged copy never re-checked; an ineligible executor
        record making an unrecoverable run), all closed in `a3ac8dc` and
        `ac0d99c`; 789 pass. Recorded in the design note.
      - [x] 2026-10-30 A re-audit of the same run keeps its staging
        verification once the scratch copy is gone (`097233c`, after a side
        agent's note); 790 pass.
      - [x] 2026-10-30 Astra's re-check at `ac0d99c` (pasted by Shawn):
        F1, F3, F4 closed; F2's identity binding overwrote the verdict
        flag's `review` content digest, so a changed verdict challenge
        kept its ruling on a same-run re-audit. Closed in `4e490b3` (the
        identity under `review_identity`); 791 pass.
      - [x] 2026-10-30 Astra's re-check at `4e490b3`: **approved** (18
        focused tests, all closure probes).
      - [x] 2026-10-30 **Combined and merged.** PR #14's branch merged into
        #15's (`ec0bb3d`): the lane header (v1.8 notes v1.8 then v1.7) and
        the manifest entry reconciled, a combined test added (a bare-name
        read of a withheld record after a cd is an access; the exemption
        and the staged copy clean). Her approved harnesses for both PRs
        pass on the combined code. `main` merged in (`6cf63bd`) for
        GitHub; main at `37a3fe7`: 806 pass, 7 skip; attempt 04 still
        adjudicates to 13/18.
      - [ ] **File in agent mail once on amd-tower:** her three PR #15
        reviews and Claude's replies (`astra-review-request-review-only-mode.md`,
        `astra-reply-pr15-closure.md` in session 789afcf9's scratchpad).
    - [ ] **Next: the reviewer-only pilot** (#15 is merged): its own run
      configuration (`mode: review-only`), the labelled copy of attempt 04
      outside any path study reporting reads, a blinding list that blinds
      the original attempt 04, a pre-run review, the API gate, a launch
      from a fresh session (a workflow script was added), on a machine
      holding attempt 04's image (amd-tower).
  - [ ] Working-notes candidates WN-ax, WN-ay (session log, 2026-10-18 →
    10-21) and WN-az, WN-ba (session log, 2026-10-21 → 10-23) await
    Shawn's verdict.
  - **Only on amd-tower:** the pilot's workflow transcript
    (`~/.claude/projects/-home-shawn-Code-llm-reproducibility/e854d6a4-f815-47a6-911a-1b8de0c8d07a/subagents/workflows/wf_88429e16-a85/`,
    needed only to re-run `audit-run`) and its scratch
    (`~/scratch/llmr-runs/gate-1-3-2-planner-pilot-2026-10/`, including
    the planner's two stray scripts under
    `evidence-planner-stray-scripts/`). The archive-drift gate (35
    sessions not archived; `~/personal-assistant/scripts/bulk-archive.py`)
    was still open at handoff.

- **⏩ Earlier (from the 2026-10-21 handoff, session a1bac2e9):
  monitor and analyse the gate 1.3.2 planner pilot, then the rest of
  criterion 4.** Gate 1.3.2's criteria 1 to 3 are on main: PR #13 merged as
  `df394c1`, after Astra approved `67569cb` in her third round. Attempt 04
  adjudicates to 13/18. Shawn launched the planner pilot on 2026-10-21 from
  a fresh session (run `gate-1-3-2-planner-pilot-2026-10`, herskind attempt
  05, stage 1 only); its configuration and brief are in
  `studies/open-science-compliance/outputs/validation/gate-1-3-2-planner-pilot/`.
  This session did not see the launch. Find the workflow run as the newest
  `wf_*` under
  `~/.claude/projects/-home-shawn-Code-llm-reproducibility/*/subagents/workflows/`
  (or ask Shawn for its id), and check whether the launching session has
  already run the post-run steps before repeating any.
  **Correction (session a9c4834d):** at handoff the launch session
  (`e854d6a4`) was still paused at the API gate; Shawn's go came at 09:58
  AEDT and the run started at 09:59. A second session (a9c4834d, started
  from this handoff) ran pre-flight in parallel; its args rebuild was
  byte-identical, so no harm, but two sessions then worked one run in one
  checkout. Shawn moved the run to a9c4834d after the hold.
  - [x] 2026-10-21 **Post-run, by the brief.** Run `wf_88429e16-a85`
    (launch commit `904d70d`); `persist-plans` and `audit-run` (`741345b`):
    receipts `reproduction-planner v1.4`, audit clean, $2.59 API-equivalent
    (estimate $1.20 to $1.80; halt $2.70), 15.8 min. Checks 1, 2, and 4
    met; **check 3 failed**: T15 (the old T17) planned creditable with Q5
    `inputs-from-authors-code: yes`, on `data`, which is
    `Herskind&Riede_S2.R` line 30 (`read_excel` of S1, never modified).
    Shawn ruled the condition `no` and **held** the plan (`aea100f`), and
    ruled the run admissible on blinding (the planner's `ls` printed the
    blinded name `lodged-rules.yaml`; never opened). Results:
    `validation/gate-1-3-2-planner-pilot/results-2026-10-21.md`
    (`5cc0f33`, `02376eb`, `2476c64`).
  - [x] 2026-10-21 **Mechanical fixture, route A** (`f34a756`): the plan
    wrote no not-creditable application (138 of 138 creditable), so a
    labelled, approver-amended copy
    (`tests/fixtures/planner-pilot-t15-approver-amendment.json`) shows
    approval, gate, and adjudication excluding T15 (16 of 17) against a
    synthetic reproduced outcome. 773 tests pass. The planner half stays
    open until the long-term fix's re-plan.
  - [x] 2026-10-21 **Mailed Astra** (Shawn approved the text): pilot
    results, the v1.2 and docstring changes since her approval, route A,
    the long-term fix, and the audit gaps; three questions
    (`~/agent-mail/claude/outbox/codex/20261021T125238.665157Z-claude-gate132-planner-pilot-results.md`).
  - [ ] **Await Astra's reply:** (1) does route A close check 5's
    mechanical half; (2) is the fix sound, and is it a gate 1.3.2
    addendum or gate 1.3.3; (3) does the delta since `67569cb` reopen
    anything.
  - [ ] **The long-term fix** (results doc, "The long-term fix"; branch +
    PR after Astra's scoping): the registrant's reading of
    `inputs-from-authors-code` (**text approved by Shawn 2026-10-21**) into
    the registry beside the condition; per-input lineage declared by the
    plan, the condition derived by the lane, "computed by" citations of
    load-only lines refused; no credit on a reading put to the approver;
    optionally a fresh-context verifier; T15 as a negative fixture. Then a
    re-plan under its own API gate, estimated from this run's $2.59 basis.
  - [ ] Then the review-only mode (branch + PR, Astra's review) and the
    reviewer-only pilot on attempt 04 at the API gate.
  - [ ] Working-notes candidates WN-ax and WN-ay (session log, 2026-10-18
    → 10-21) await Shawn's verdict.
  - The open items above are carried forward in the 2026-10-23 block.

- **⏩ Earlier (from the 2026-10-18 handoff, session 8e28871d): build
  gate 1.3.2 on a branch, to the acceptance criteria at the top of
  `wiki/planning/reproduction-gate-1-3-design.md`.** Gate 1.3.1 is closed
  (version-scoped); the hardening stays open until 1.3.2 lands and is
  reviewed, before the §8 gate. Fable is rationed (credit limited); route
  reviews to Astra, who has plenty. The operational fixes are separate
  PRs. Background, the pilot re-run: stage 2 ran
  (`wf_4fd7a886-ada`, launch commit `6b18505`, 42 min, $14.02
  API-equivalent), and every post-run step is done: authoritative
  `check-attempt` pass, PR #12 merged (`a29f16a`, Shawn), `audit-run`
  clean, human queue of 17 issues, all ruled by Shawn, and
  `persist-results` eligible (`2f9beff`, `67dd4af`). Verdict SUCCESSFUL;
  study coverage **13/18** (T17 not creditable under amendment 3 §7(d)),
  while the lane admits 14/18. Both blind runs (attempts 03 and 04) found
  the same Table 1 cells and Fig. 4 boxes.
  - [x] 2026-10-17 **Decided (Shawn): gate 1.3.1 closes for the findings
    it addressed, and gate 1.3.2 opens for the three gaps below** (recorded
    at the top of `wiki/planning/reproduction-gate-1-3-design.md`). Outcome
    mailed with Shawn's approval, 2026-10-17, each asking two questions
    (does a gap reopen a finding; is the 1.3.2 scope complete):
    `~/agent-mail/claude/outbox/claude/20261017T073937.869344Z-claude-gate131-closed-fable.md`
    (bounded ask) and
    `~/agent-mail/claude/outbox/codex/20261017T073937.869344Z-claude-gate131-closed-astra.md`
    (no token limit; Astra has plenty of credit). [x] 2026-10-18 Both replies in, same verdict (closure sound; scope right, with criteria to make explicit): Astra's `~/agent-mail/codex/outbox/claude/2026-10-17-codex-gate131-pilot-and-gate132-scope-review.md` (four acceptance criteria: target-scoped concerns plus a derived adjudicated result; a per-target reviewer method assessment; rules quoted whole and their conditions mapped to each target's inputs; the operational follow-ups keep the earlier protections) and Fable's `~/agent-mail/claude/outbox/claude/20261018T044003.960111Z-claude-gate131-closed-fable-reply.md` (adds: obligations need target scope too, since `method-adherence:targets` is as targetless as `review:qualified`; the review-only mode on attempt 04 can serve as 1.3.2's pilot). [x] 2026-10-18 Folded both sets into the 1.3.2 scope at the top of the design doc (Shawn: "proceed as suggested"): gaps classed (gap 2 a D, gap 3 an A, gap 1 a strengthening of F4); four acceptance criteria; the operational fixes as separate PRs outside the gate's review, as Fable placed them. **Credit
    is limited (Shawn, 2026-10-17): this follow-up with Fable is the last
    Fable use for now; ration aggressively after it.** The question was:
    does a run with these findings close the hardening? Fable's earlier view: a clean re-run closes it. The gate's
    mechanics all worked (receipts, blinding, sealed runs, strict binding,
    audit, admission), but the pilot found three gaps. (1) The executor's
    `method_as_planned` declarations caught one departure of five (T13);
    the reviewer found T01, T03, T04, and T12 (side agent, 2026-10-17).
    (2) A review concern cannot be ruled against one target: the review
    issue names no targets, so it is all or nothing, and T17 stays in the
    lane's 14/18. (3) The approved plan paraphrased ruling Q5 without its
    input condition, and plan approval (Shawn's, and Claude's walk-through)
    did not catch it. Consider mailing Fable and Astra the outcome.
  - [ ] **Gate 1.3.2, before the §8 gate: build to the acceptance criteria
    at the top of `wiki/planning/reproduction-gate-1-3-design.md`**
    (2026-10-18, from both reviews): (1) target-scoped concerns and
    obligations, plus a derived adjudicated result that study reporting
    reads (fixture: 13/18 from attempt 04, T17 only excluded, T03 as
    PAPER_ERROR); (2) a reviewer row per locked target, raising
    `method-deviation:<target>` and flagging disagreement with the
    executor; (3) lodged rules quoted whole, with each target's condition
    and evidence stated and checked at approval (T17 the negative fixture);
    (4) a live check through the review-only mode on attempt 04 (one
    reviewer spawn, its own API gate). Close with regression evidence and
    a review of the final changes. Branch + PR (schema and admission
    changes). [x] 2026-10-18 **Criterion 1 built** on `feat/gate-1-3-2`
    (worktree `.claude/worktrees/gate-1-3-2`; lane v1.6, `GATE_VERSION`
    1.3.2; review schema 1.1; adversarial-reviewer v1.4): `2ccda2e`,
    `081040c`, `89f70ef`. 735 tests pass. Shawn's rulings (2026-10-18): a
    ruling never creates credit; the verdict is ruled only on the review
    flag; the adjudicated result is written only when final; a reviewer's
    target slip makes the item paper-wide to rule, not a hard failure (a
    side agent's note). Shawn approved restating two attempt-04 rulings
    (T17 excluded on `review:qualified`, verdict SUCCESSFUL; T03 PAPER_ERROR
    on `escalation:executor:OTHER:T03`); recorded and adjudicated
    (`f9328ed`): **13/18, only T17 excluded**. **Draft PR #13**
    (https://github.com/saross/llm-reproducibility/pull/13), title and body
    as Shawn approved them, read back identical. [x] 2026-10-18 Criteria 2
    and 3 on the same branch (`4038937`, `6eafb1f`; docs `33df238`,
    `e2b0a6e`; fix `383e208`). Shawn's rulings: method disagreements folded
    into the reviewer's flag; the paper-wide `method-adherence` obligation
    retired; lodged rules from a registry
    (`reproduction-system/lodged-rules.yaml`); the gate enforces a plan's
    "not creditable"; Q5 and R2 condition lists approved 2026-10-19
    (`bc85895`). 755 tests pass. [x] 2026-10-19 **Astra's review requested**
    for criteria 1 to 3 at `bc85895`
    (`~/agent-mail/claude/outbox/codex/20261018T220501.705369Z-claude-gate132-review-request.md`);
    Shawn wakes Astra. [x] 2026-10-19 **Astra's review in**
    (`~/agent-mail/codex/outbox/claude/2026-10-19-codex-gate132-criteria-review.md`):
    changes requested, three class D (verdict ruling unbound to the verdict
    challenge; contradictory or incomplete method rows passing; scalar
    collections crashing). All closed on the branch (`07ac8b3`, docs
    `700a8f2`), with Shawn's ruling that a condition the plan settles
    (`decided_at: plan`, e.g. Q5's input condition) cannot be `unknown`
    (a side agent's note). 765 tests pass. Closures mailed for re-check
    (`~/agent-mail/claude/outbox/codex/20261019T050404.082545Z-claude-gate132-findings-closed.md`).
    [x] 2026-10-19 Planner pilot decided: yes (Shawn, and Astra's scope:
    fresh blinded planning attempt, approver checks the T17-equivalent's
    input provenance, plus an isolated labelled mechanical fixture; the
    design note records it). [x] 2026-10-20 **Astra's re-check**
    (`~/agent-mail/codex/outbox/claude/2026-10-20-codex-gate132-closure-recheck.md`,
    at `700a8f2`): D-Astra-132-1 closed; residuals of 132-2 (explicit nulls
    passing as assessed) and 132-3 (malformed dimensions crashing, also in
    persist-results). Both closed (`02e35df`, docs `67569cb`): concerns and
    method rows validated against their review-schema definitions; a
    malformed dimensions block is a paper-wide defect, and persist-results
    notes an uncomputable count. 768 tests pass. Mailed for a further check
    (`~/agent-mail/claude/outbox/codex/20261020T033740.363391Z-claude-gate132-residuals-closed.md`).
    [x] 2026-10-20 **Astra approved the corrective delta** at `67569cb`
    (`~/agent-mail/codex/outbox/claude/2026-10-20-codex-gate132-residual-closure-review.md`):
    all three findings closed, "no remaining code-review blocker for
    criteria 1 to 3"; the live checks remain. Receipted 2026-10-21 (with
    the two earlier gate 1.3.2 mails). [x] 2026-10-21 **PR #13 merged** on
    Shawn's instruction ("yes, merge PR #13"): marked ready, merged as a
    merge commit pinned to the approved head (`df394c1`, head `67569cb`).
    Main's code is identical to `67569cb`; 768 tests pass on main; manifest
    83/83; attempt 04's adjudicated result verifies (13/18). Worktree
    `.claude/worktrees/gate-1-3-2` removed; the branch is kept. Gate 1.3.2
    stays open for criterion 4. [x] 2026-10-21 **Planner pilot prepared**
    (`99b9c04`): `validation/gate-1-3-2-planner-pilot/run-config.yaml` (run
    `gate-1-3-2-planner-pilot-2026-10`, herskind attempt 05, stage 1 only;
    the gate 1.3.1 run's rulings, deposits, and prices unchanged; six new
    blinding entries) and `api-gate-brief.md` beside it (estimate $1.20 to
    $1.80, 6 to 12 min, from the last planner run's $1.2969 and 436.5 s;
    tripwires $1.80/12 min check, $2.70/18 min halt; launch checklist,
    Astra's acceptance, stop states, blinding limits). Dry-run args build
    clean (10 lodged rules, 4 rulings, 27 blinding entries). [x] 2026-10-21
    Two side-agent notes fixed before launch, both routes by which a blinded
    path would have voided the run: (a) the lane script was blinded while
    the run notes name run-container in it; its seven docstring lines naming
    attempt 04's outcome are reworded (`a37a1f6`, Shawn chose this over
    keeping it blinded) and the config unblinds it (26 entries, `71fdd72`);
    (b) the planner's rules block named R1 to R4's blinded source; plan
    workflow v1.2 drops source paths from the prompt (`3307000`). A full
    render of the pilot's prompt names no blinded path outside the blinding
    instruction; brief updated (`c649259`). Tell Astra about v1.2 with the
    criterion 4 material (it changed after her approval). [ ] **Next,
    criterion 4 (Astra's scope, in the design note):** (1) the planner
    pilot, launched by Shawn from a **fresh session** (so
    reproduction-planner v1.4 loads from main) by the brief's checklist:
    rebuild the args at the launch commit, API gate, launch, persist-plans,
    audit-run, then the approver's check of the old T17's input provenance
    and an `approve` decision; (2) an isolated, labelled
    mechanical fixture showing that plan's not-creditable target excluded;
    (3) build the review-only mode (its own review), then the reviewer-only
    pilot on attempt 04 at the API gate.
  - [ ] **Operational follow-up PRs, outside the gate's review:** the
    launch word rule (screen the whole relayed message); the args-builder
    guard (allow the planned initial state, reject prior execution
    evidence or an active run); the cost and time watcher (independent
    start time; session 8e28871d's watcher, a session-scratch script not
    kept, priced with `transcript_usage` and `price_usage` but measured
    file change times, so **its time check could not fire**; test a run
    whose files stop changing, restart, and missing telemetry). Added from
    the gate 1.3.2 planner pilot (2026-10-21, results doc F3 and F4): the
    live cost check lags by one turn (the last and largest turn is
    invisible until the run ends); the run audit's
    `writes_outside_scope` cannot fire for a planner (it counts only
    Write, Edit, and NotebookEdit; use `segment_writes()` for Bash); the
    blinding scan's `path_tokens()` drops bare names, so a blinded name in
    output raises no warning and `cd <dir> && cat <blinded-name>` gives no
    hit at all (`file_accesses()` covers only Read, Grep, and Glob); and
    the harness scratchpad competes with the run's scratch directory (F5).
    Also screen for a second live session on the same run before launch.
  - [x] 2026-10-17 Repeated pre-launch checks at `6b18505`: 699 tests pass,
    Docker 29.2.1, 30 GB free, Zenodo 200, attempt-04 holds only the plan
    and approval, no attempt-04 image. Launched on Shawn's "go", which
    passed the word rule and was relayed verbatim (checked in the
    executor's transcript).

- **⏩ Earlier (from the 2026-10-13 handoff, session b5f7b974).**
  Gate 1.3.1 is on main (PR #11 merged, `10500ea`, after Astra's approval).
  The pilot re-run is half done: stage 1 ran clean
  (`wf_db7d121a-5d5`, $1.2969 API-equivalent, audit clean) and Shawn
  approved the attempt-04 plan (18 locked targets). **Stage 2 (execute)
  is next, at the API review gate.** Its args were built at `e2b42c6`;
  the handoff commits moved `HEAD`, so **rebuild them** first
  (`build-exec-args`, no API cost), then present the gate (≈$13–18
  API-equivalent, 45–60 min). Settle the launch first: Shawn wants a
  serious pre-run review or an easy trigger, not a fixed phrase (the
  launch-mechanism item below). Keep main fixed at the launch commit until
  the run ends.
  PR #12 (per-request pricing) awaits Astra's check of `154b637`; do not
  merge it while stage 2 is pending or running (it moves `HEAD`); merge it
  before the post-run `audit-run`, so the Haiku gate step is priced.
  - [x] 2026-10-17 **Stage 2, then the post-run order**: authoritative
    `check-attempt` (with `--launch-commit`), `audit-run`, `human-queue`
    (written beside the run config, never into the attempt), rulings,
    `persist-results`. Fable's view: with a clean re-run the hardening
    closes. Done; see the 2026-10-17 block above.
  - [x] 2026-10-17 **Mail:** Astra's check of PR #12 at `154b637` arrived
    2026-10-13 17:31 (`2026-10-13-codex-pr12-closure-review.md`, receipted
    2026-10-17): source approval, both findings closed, no remaining
    blocker. Merge at step 2 of the post-run order (H2 of the pre-run
    review), with Shawn's approval.
  - [x] 2026-10-17 **Pre-run review of stage 2** (the `pre-run-review`
    skill; sections 2026-10-13, Shawn's explain-back and decisions
    2026-10-17). Hardenings H1–H7 in
    `studies/open-science-compliance/outputs/validation/gate-1-3-1-pilot-rerun/pre-run-review-stage-2.md`
    (a blinded path, so no agent reads it): no-touch window, post-run
    order with PR #12 at step 2, cost and time tripwires derived per run
    from the gate estimate (check at the top, halt at 1.5 times; Shawn:
    they vary from paper to paper), an attempt stopped halfway is used up,
    a material difference from attempt-03 is a finding, the launch message,
    and amd-tower as the approved plan says. General rules added to
    `reproduction-system/workflows/README.md`. The launch commit and the
    repeated pre-launch checks are recorded here after the run (H1).
  - [ ] **Sapphire for runs (Shawn, 2026-10-17):** sapphire's problems are
    solved and he wants runs moved there. Attempt 4's locked plan says
    amd-tower only, and `run-container` bind-mounts local paths
    (`scripts/reproduction-lane.py`, `container_argv`), so a remote
    Docker host cannot see the attempt. Needs a session running on
    sapphire, or lane support for a remote host; update the run notes in
    later configurations.
  - [ ] **Follow-up PRs after the pilot:** the launch word rule (below);
    `build-exec-args` refuses an attempt holding any execution artefact
    (H4); a lane subcommand for the cost and time watcher (H3; the
    session's scratch `watch-run.py` did the job for stage 2).
  - [x] 2026-10-17 **Launch mechanism decided** (Shawn): the word rule,
    built as a PR after the pilot; stage 2 launches on his plain go-ahead
    and he rules the audit's flag once. Original item: He finds
    "repeat this exact phrase" annoying, not useful: "I'd like a more
    serious review before a launch … or trigger easily". So, for stage 2:
    offer the pre-run review (the `pre-run-review` skill, in which he
    explains the run back in his own words: what it does, when it stops),
    and propose a launch that keeps the relayed message neutral without a
    fixed phrase. Options to weigh, none built: widen `NEUTRAL_LAUNCH_RE`
    to short approvals ("go", "approved, go"); or treat Shawn's approval
    message as the launch message and record it, since an approval says
    nothing about results. The relay itself (F3) is the harness's.
  - [x] 2026-10-13 **Astra's delta review of `1d875d2`** received
    (`2026-10-12-codex-gate131-delta-review.md`, receipted): changes
    required, three class D incomplete closures. D-Astra-1 (F2: shell reads
    credited without delivery; Read matched by substring), D-Astra-2 (F1:
    a comment and `grep cp` became hard write failures), D-Astra-3 (F8:
    persistence could use another workflow's cleared run audit). All
    closed on PR #11 (head `3a411f8`: `1b5b2d1`, `9bec885`, `dae59da`,
    docs `3a411f8`); 665 tests pass with Docker; Astra's probes rerun give
    the intended verdicts. Closures mailed
    (`20261012T222048.473640Z-claude-gate131-astra-delta-closed.md`, with
    the rerun probe beside it).
  - [x] 2026-10-13 **Astra's check of those closures** at `3a411f8`
    (`2026-10-13-codex-gate131-closure-review.md`, receipted): D-Astra-3
    and the strict binding accepted; two command-mode residuals (class D):
    `cat --help x` earned read credit, and `cp --help … outputs/x` was a
    hard write. Both closed on PR #11 (head `579104b`: `7b4510b`,
    `ab5a4ac`, docs `579104b`); 667 tests pass with Docker; her closure
    probes rerun as intended. Mailed
    (`20261013T030316.777082Z-claude-gate131-astra-residuals-closed.md`).
  - [x] 2026-10-13 **Astra's check of the two residual closures** at
    `579104b` (`20261013-codex-gate131-option-closure-approval.md`,
    receipted): source approval, no remaining blocker (not pilot, Docker,
    or live-workflow acceptance).
  - [x] 2026-10-13 **PR #11 merged** on Shawn's instruction ("complete all
    merges that are ready"), as a merge commit pinned to the approved head
    (`10500ea`); its branch is kept, as for earlier PRs. Main's code is
    identical to `579104b`; 667 tests pass on main. No other PR was open,
    and every other remote branch is fully merged, so nothing was mailed
    for review. The worktree `.claude/worktrees/gate-1-3-1` is now on a
    merged branch and can be removed.
  - [x] 2026-10-13 Removed the clean worktrees on merged branches
    (`correction-ledger-draft`, `agent-a8a2378c2a5dbdc98`,
    `amendment-3-instruments`); their branches remain.
  - [x] 2026-10-13 **Shawn's ruling: the reviewed-state binding stays
    strict.** A result is admitted only if the attempt matches the state
    the in-workflow gate check recorded just before its review (the
    lane's post-review records aside). Any other edit needs a new review,
    and no ruling overrides it; corrections go into new attempts, and the
    human queue stays beside the run configuration. Options declined:
    excluding prose notes from the state, and a rulable state-change flag.
  - [ ] **Follow-up PR after the pilot: a review-only re-run mode** in the
    execute workflow (gate check and reviewer on an existing attempt), so
    a post-review fix costs one reviewer spawn rather than all of stage 2
    (Shawn, 2026-10-13).
  - [x] 2026-10-13 (PR #11 merged before the pilot, as ordered)
    **Merge order (side note, 2026-10-12):** the re-run must test PR
    #11's code. The session's agent definitions, hooks, and workflow
    scripts load from the main checkout, so launching before PR #11 merges
    would test the old gate. Order: Astra's delta review comes back clean,
    then Shawn merges PR #11, then the pilot runs from main. Any defect the
    pilot finds goes into a follow-up PR.
  - [x] 2026-10-13 **Pilot configuration committed** (`0513572`):
    `validation/gate-1-3-1-pilot-rerun/run-config.yaml`, run
    `gate-1-3-1-pilot-rerun-2026-10`, herskind attempt 4, effort high,
    rulings R1 to R4; blinding adds attempt-03 and its scratch, args, and
    workflow-result files under `~/scratch/llmr-runs`. Plan args first built
    at `0513572`, then rebuilt at `5fdaf87` after a continuity commit moved
    `HEAD` (`~/scratch/llmr-runs/gate-1-3-1-pilot-rerun-2026-10/plan-args.json`,
    checksum `3ad040ae63363ca2`).
  - [x] 2026-10-13 **Stage 1 (plan) run** on Shawn's approval at the API
    gate, launched with the neutral phrase: workflow `wf_db7d121a-5d5`
    (one Opus 5.5 planner, 7.4 min), status OK, 18 targets (8 display
    items, 10 named values), 4 exclusions, no relayed launch message.
    Persisted with triage (`triage-wf_db7d121a-5d5.md`). The approval note
    is stored only in `plan-approval.json`; agents see the locked plan, the
    config's rulings, and the run notes, so a ruling that differs from the
    plan needs the config or a re-plan.
  - [x] 2026-10-13 **Plan approved** by Shawn after a walk-through,
    accepting the plan's treatment of all six approver questions (record
    10801706 per AP-12; R 4.3.2; log-base and t = 482 as a methods note;
    T14 against the stated nine; T15 scoped to the culture-specific Fig. 3b
    bigrams; "nearly half" excluded). Plan sha256 `6837cf60785a…`, 18 locked
    targets. Attempt-03's planner listed 20 targets, so coverage compares
    only roughly; the gate test is unaffected.
  - [x] 2026-10-13 **Stage 1 audited** (`audit-wf_db7d121a-5d5.json`):
    planner clean, receipts valid, no blinded access, no writes outside
    scope; $1.2969 API-equivalent, 17 requests, 436.5 s.
  - [ ] **Stage 2 (execute)** at Shawn's API review gate: executor, Haiku
    gate step, and reviewer, ≈$13–18 API-equivalent, 45–60 min. Args built
    at `e2b42c6` (checksum `5423adb95a43673f`); rebuild at the current
    `HEAD` before presenting the gate. Shawn asked for `/reflect` and
    `/handoff` first, so the next session starts here.
  - [ ] **Effort comparison before scaling** (Shawn, 2026-10-13): measure the
    reproduction lane at `medium` against `high`. The FAIR scorer's result
    (effort steps ≈$1.80 per arm, results insensitive; scorer confirmed at
    `medium` 2026-10-04) does not transfer to long executor runs. The gate
    1.3.1 pilot stays at `high` (Shawn's 2026-10-03 lane ruling) so it
    compares cleanly with attempt-03.
  - [x] 2026-10-13 **Standing approval (Shawn): Claude and Astra may run
    each other's code**, as an efficiency step; the formal rule change
    (`common.md` and the mail-watch skill say a peer's code needs Shawn's
    approval) is to follow later, by PR reviewed by the other agent.
    Before this, Claude had twice run Astra's probe scripts (read in full,
    disposable copies, no network or API) without asking; disclosed.
  - [ ] **PR #12, per-request pricing (lane v1.5)** for Haiku 5.5's two
    cards, verified against the live pricing page on 2026-10-13. Astra's
    two reviews of `43d4b72` (changes required: rate cards unvalidated;
    missing usage priced at 0.0) are closed at `154b637` and mailed
    (`20261013T051105.142768Z-claude-pr12-findings-closed.md`); her check
    approved `154b637` (2026-10-13, see Mail above). Follow-up noted, not in the PR: keep per-model, per-tier
    usage subtotals in audit records, so a tiered model can be re-priced
    after transcripts rotate. Worktree
    `~/worktrees/llm-reproducibility/claude-opus-pricing`.
  - [ ] **Pilot re-run under gate 1.3.1 (from main, after PR #11 merges):**
    a new run configuration (herskind attempt 4, a new run id) beside
    `validation/gate-1-3-pilot-rerun/run-config.yaml`. Then the API review
    gate (≈$14 API-equivalent on the Max plan, as before), and plan
    approval. Launch each stage with exactly `Run the approved stage.`
    Then the post-run order: check-attempt, audit-run, human-queue,
    rulings, persist-results. Fable's view: with a clean re-run the
    hardening closes. [x] 2026-10-13 config, stage 1, and plan approval
    done (above); stage 2 and the post-run order remain.
  - [x] 2026-10-13 **Haiku 5.5 pricing** (Sonnet subagent, 2026-10-12,
    verified against platform.claude.com/docs/en/about-claude/pricing). It has two
    tiers by prompt length, in USD per million tokens (input, output,
    5-minute and 1-hour cache writes, cache read). Up to 100,000 tokens:
    0.10, 0.50, 0.125, 0.20, 0.01. Over: 0.50, 2.50, 0.625, 1.00, 0.05. The
    tier is set per request, so `price_usage` must price request by
    request. Add both rows to the run configurations. Deferred until
    Astra's delta review lands. Rates and the prompt-length rule
    re-verified on the live page 2026-10-13; built as PR #12 (see above).
  - [ ] Fable's delta notes, accepted as notes and not built: published
    values kept under `comparisons/` are invisible to the F6 check; build
    records are not sealed into `index.jsonl`; `run_file` prints warnings
    together at the end (documented in the wrapper reference).
  - [x] 2026-10-13 Worktrees on merged branches, all clean at handoff, can be removed:
    `.claude/worktrees/correction-ledger-draft` (PR #10),
    `agent-a8a2378c2a5dbdc98` (PR #7), and `amendment-3-instruments`
    (PR #9). Removed, with `.claude/worktrees/gate-1-3-1` (PR #11).
  - [ ] Held for Shawn: three user-observation candidates (pending section
    in `wiki/user-observations.md`) and two working-notes candidates (the
    session log entry below). Still held 2026-10-13. [x] 2026-10-14 the
    user-obs part closed with the backlog redesign (`2ccd4f7`); the two
    working-notes candidates are still held. Session b5f7b974's
    own batch was adjudicated the same day: user-obs A and C accepted, B
    replaced by Shawn's observation on launches, D discarded; WN-at and
    WN-au accepted as Observations 56 and 57.

- **⏩ Earlier (2026-10-12): ledger frozen (PR #10 ready to merge); gate
  1.3.1 fixes on PR #11; delta review requested.**
  - [x] 2026-10-12 **Both final reviews in** (Fable mail
    `20261012T032928.805148Z`, Astra `2026-10-12-codex-gate13-final-review.md`):
    the round does not close the hardening. Consolidated in the brief
    (`c73eea6`).
  - [x] 2026-10-12 **Step 1: ledger frozen** (PR #10): pre-freeze checks
    (`3c97be2`; corpus store `280165d` on main), main merged in (`9ff97c9`),
    frozen as `correction-ledger-v1.0.json` (`a299416`, sha256
    `189e8a33…`). Astra accepted L18–L20 (no blocker). [x] 2026-10-12
    **Merged** on Shawn's instruction (`d0e6dfc`); hash re-verified on main.
  - [x] 2026-10-12 **Step 2: gate 1.3.1** (PR #11, head `c34cc73`): every D
    and A finding fixed with tests (648 pass with Docker); hook `1.6-inst`
    `run_file` evaluator; `build-image`; run audit in admission; pilot
    re-audit in `validation/gate-1-3-pilot-rerun/reaudit-gate-1.3.1/`.
  - [x] 2026-10-12 **Fable's delta review** (mail
    `20261012T113743.407608Z`): every finding landed; three second-pass
    items (D-1 reviewer never bound by audit-run; D-2 piped and same-named
    reads; B-1 evaluator resolved through globalenv) plus D-3 and notes.
    All closed on PR #11 (head `1d875d2`), with two side-note fixes:
    receipts checked at the run's launch commit (`9e1f123`) and "read
    declared pulls in full" in all three definitions (`4559bbd`). 654 tests
    pass. Closures mailed (`20261012T120008.812403Z`). Fable: with these
    closed and a clean pilot re-run, the hardening closes.
  - [ ] **Astra's delta review** of `1d875d2` (delayed by an upgrade; Shawn,
    2026-10-12). Then one pilot re-run (API gate), then Shawn merges PR #11.
  - [x] 2026-10-12 Shawn's coverage question: the three proposals are
    queued as amendment 4 items 5–7 in `prereg/erratum-log.md` (`e6997a0`).
  - [ ] For the §8 gate run: its comparison script maps the ledger's
    `REPRODUCED_VISUAL` to any within-tolerance outcome.
  - [x] 2026-10-12 Haiku 5.5's API-equivalent price checked (two tiers;
    see NEXT SESSION above).
  - [x] 2026-10-12 Shawn's user observation recorded (`460b736`): keep
    Fable in the review rotation.

- **⏩ Earlier (2026-10-11, evening): herskind pilot re-run done; gate 1.3
  final review out to Astra and Fable.**
  - [x] 2026-10-11 **Herskind attempt-03 through the agentic lane** (Shawn
    approved at the API gate; Max plan). Plan `wf_14d5db9b-bed` ($1.21,
    audit clean); execute `wf_7c18dfdc-298` ($12.73, 42 min). SUCCESSFUL,
    17/20, authoritative gate pass (no flags), review QUALIFIED. Both
    PAPER_ERROR calls match the shakedown and HER-T04, found blind.
    Artefacts `78137fe`.
  - [ ] **Final review**: brief `wiki/planning/reproduction-gate-1-3-final-review-brief.md`
    (`d03f658`); Astra mailed (`20261011T120856.313092Z`); Shawn wakes
    Fable (top-tier credit). Provisional defects F1 (transcript audit's
    false hard failures: `>` in quoted awk/heredoc, `--help`) and F2
    (receipt check misses `cat` reads); F3–F4 possible ordinary routes.
  - [ ] Human queue for attempt-03: six unruled items plus two PAPER_ERROR
    calls and the T06 method change; not study data, so it can wait for
    the review.

- **⏩ Earlier (2026-10-11, later): all rulings in (L1–L20); PR #7 merged;
  PR #10 needs only the pre-freeze checks.**
  - [x] 2026-10-11 **Shawn ruled L18 (a) again, L19 (a), and L20 (a)**
    (PR #10 `2d40bde`, ledger 0.3.5-draft, nothing open). L18: CREMA-T04
    MINOR_DISCREPANCY vs the VoR, matching v3's regenerated figure2.pdf
    (`cf61c685…`) in all three panels; crema SUCCESSFUL. L19: MAR-T10's R²
    labels within the deposited supplement's Table 3 95 % intervals. L20:
    keep the Dockerfile's R 4.4.1; report the conflict with the lockfile's
    4.5.0 beside the verdict as a minor discrepancy (README finding 9).
    Shawn: "exactly the kind of minor error we should point out, without
    failing the entire run"; "these discrepancy reports are extremely
    valuable".
  - [x] 2026-10-11 **Astra's re-review received** (mail 07:08Z, at
    `d6beec4`): B3 accepted; L18 (a) supported with PAPER_ERROR wording
    softened and (a) widened to the full figure; asked for L19 and L20.
    All applied in `2d40bde`; reply sent (mail `20261011T104239.952791Z`).
  - [x] 2026-10-11 **PR #7 merged** on Shawn's instruction (`3be8313`),
    including `306181f`: executor v1.6 sets package repository dates
    (rocker images default to their own snapshot date; `r-ver:4.3.1` →
    2023-10-30). Merged before the planned final cross-model review;
    Astra asked for a post-merge review by mail.
  - [x] 2026-10-10 **PR #9 merged** by Shawn (`2dcd3d5` on main). PR #7
    merged main in at `66792b1` (reproduction-executor v1.5).
  - [x] 2026-10-11 **L18 reopened** (PR #10 `a722e14`) after Astra's review (mail
    07:24Z): four options, now including (d) PAPER_ERROR; recommendation
    (a) MINOR_DISCREPANCY with the expected selected-archive figure and
    tolerance stated. Shawn's earlier "(a)" was on the incomplete framing;
    he must re-rule. Re-ruled (a) on 2026-10-11 (above).
  - [x] 2026-10-11 **B3 fixed** (PR #10 `3f4dcb0`): crema rebuilt honouring
    all 68 session-info pins (v3; 67 honoured, nimbleCarbon 0.2.4 → 0.2.1);
    every figure and Fig. 2 check identical to the first probe. v2 (unused)
    had two install-script defects, recorded in the probe README.
  - [x] 2026-10-11 **Marwick probe passed** (PR #10 `d6beec4`, ledger
    0.3.4-draft, `evidence/marwick-fig2-probe/`): fit 19.19 h on zbook,
    render 3 min, peak memory 19.6 GiB (render). Trend lines within 1 px,
    points identical; two R² labels differ in the fourth digit (unseeded
    `bayes_R2` subsample). Marwick's expected verdict no longer
    provisional. The 1.7 GB fit stays in the stopped container on zbook.
    **Corrected 2026-10-11 (`2d40bde`):** "points identical" overclaimed;
    the check finds no strong point discrepancies outside excluded marks.
    The fit differs from the authors' despite seed 123 (divergences 3/4
    vs 6/0), so the R² differences are consistent with stochastic
    variation from the fit or the subsample, not the subsample alone.
  - [x] 2026-10-11 **Astra re-review requested** (mail
    `20261011T022409.862798Z`): B3, probe READMEs, L18 framing, and the R
    4.4.1 (Dockerfile) vs 4.5.0 (lockfile) point for marwick. Received
    07:08Z (above).
  - [ ] Pre-freeze checks still open: hash marwick's in-zip files; L13
    review counts; Q10 corpus-store deposits; hold L18's reference render
    (crema v3 `figure2.pdf`) in the corpus store. Then merge main into PR
    #10 (expect the erratum-log Entry 6/7 conflict), freeze as v1.0 with
    its sha256, and Shawn merges.

- **⏩ Earlier (2026-10-10): L5 and L17 ruled, probes running, L18 open.**
  - [x] 2026-10-10 **PR #9 at `4252e43`, ready for Shawn's merge.** A side
    agent caught that `062c20a`'s N1 rewordings reworded frozen text that
    amendment 3 does not lodge (routing design §6 rule 3: an OSF amendment
    is required before an affected run). Reverted; B1 kept (it applies
    lodged clarification 3). Astra re-reviewed (mail 06:33Z): no blocker,
    and she withdrew her own N1 acceptance. D5 PASS; 378 tests + 16
    subtests (the venv at `venv/bin/python -m pytest tests`).
  - [x] 2026-10-10 **Shawn ruled L5 (c) and L17 (c), probes first**
    (PR #10 `ddd4dcf`). Crema's leg covers Table 1 + five figures; CREMA-T04
    to T06 corrected (pilot's v2.0.0 figures differ from v1.0.0's). MAR-T10
    in the gate; its `eval: false` chunk runs verbatim from a wrapper. Shawn:
    the gate tests the lane, not the papers, so it should be as realistic as
    possible without slavishly mirroring production. Amendment 4 queue
    (Entry 7) gained the N1 rewordings, a rule for author-disabled code,
    and a figure-centrality heuristic (Shawn's request; not in the gate).
  - [x] 2026-10-10 **Crema probe done** (amd-tower; PR #10 `353e151`,
    `evidence/crema-figures-probe/`): Figs 1, 3, 4, 5 pixel-identical to
    the deposit's PDFs; Fig. 2 panel a is not, because v1.0.0's
    `post_sim1a.RData` is not the posterior behind its own published panel
    (v2.0.0's is). **L18 open** (CREMA-T04's expected outcome); recommended
    (a) MINOR_DISCREPANCY. Astra asked to review (mail 07:07Z).
  - [x] 2026-10-11 **Marwick L17 probe running on zbook** since 17:56 AEDT (container
    `llmr-probe-marwick-fig2`; files and `out/` under
    `~/scratch/llmr-probes/marwick-fig2/` on zbook; amd-tower holds the
    build files). The authors' Dockerfile fails as supplied (rstan binary vs
    lockfile RcppParallel); `probe.Dockerfile` builds StanHeaders and rstan
    from source at their pins. Five models run one after another, 4 cores
    each, as the authors wrote them. When done: compare
    `fig-smooth-plots-paper-probe.png` with the version of record, commit
    evidence to PR #10, and report to Shawn.
  - **zbook is available as secondary compute** (Shawn, 2026-10-10); sapphire
    stays held until its memory soak test is done.
  - Marwick's 1.3 zip is downloaded (`~/scratch/llmr-probes/marwick-fig2/dl/`,
    md5 matches Zenodo), so the in-zip hashing pre-freeze task can be done.

- **⏩ Earlier (2026-10-09, later): merges before any run (Shawn).** Astra
  reviewed PR #9 and PR #10 (mail 08:46Z and 08:53Z); both had blocking
  items, all fixed and re-review requested by mail.
  - [x] 2026-10-09 **PR #9** at `062c20a`: B1 (the v2.1 aggregation rule
    still counted "non-principal upstream sources"; now qualified by v2.2
    clarification 3) and N1 (paper-error procedure made an optional
    diagnostic; tolerance rule admits PAPER_ERROR). Mirrors re-spliced,
    digests and Entry 6 updated; D5 PASS; 410 tests pass. N2 deferred:
    the FAIR guide's v2.1 pointer needs guide v1.2 plus four assessor
    definitions (before §10 step 5); schema strings and
    `reproduction-lane.py:104` after PR #7 merges.
  - [x] 2026-10-09 **PR #10** at `916eb7b` (ledger 0.2.1-draft): B1
    confirmed visually (MAR-T09 and MAR-T11 corrected; marwick unchanged
    8 to 6; MAR-T13 checked and unchanged; Astra's panel F example was
    wrong and the mail says so), and B2 (HER-T02 back to the pilot's 3 dp).
  - **L17 recommendation withdrawn from (a), now (c) after a local probe,
    (b) as the fallback.** Astra was right: registration §8's exception is
    crema's leg only; eligibility criterion 4's cap is 168 h per paper;
    §7.6 locks the denominator. Dropping MAR-T10 would need a prospective
    amendment. The JSON still carries the old text; revise with the ruling.
  - [ ] **Hold sapphire for reproduction runs until its memory fix is
    confirmed** (personal-assistant session, 2026-10-10: a load-dependent
    single-bit fault, non-ECC, that can silently alter values in runs that
    appear to succeed; worst under sustained multi-worker load). Checked
    2026-10-10: no llm-reproducibility compute ran there since 2026-10-05
    (amd-tower transcripts and the `~/cc-archives/llm-reproducibility`
    mirror; the only matches are greps of the execution prompt), so nothing
    needs re-running. But `02-execution-and-verification.md` §1.2 and the
    plan guide send runs over an hour to sapphire. Pin the herskind re-run
    and any L17 local fit to amd-tower, and say so in the plan approval.
  - **Merge order proposed:** PR #9 (after Astra's re-review), then rebase
    PR #7 on main (manifest and executor-definition conflict), then the
    herskind re-run and the final review, then PR #7. PR #10 merges once
    ruled and frozen (before the §8 gate, not before the re-run). Fable is
    not needed until the re-run is done.
- **Earlier: Shawn ruled the overnight questions (2026-10-09, by remote
  session from a tablet).**
  - **Q1 (a):** build the dry-run record's design on PR #7 before the final
    review: verbatim short texts with their verified caller, templates for
    package internals, and one obligation per place and caller.
    [x] 2026-10-09 Built on PR #7 (head `8eeefd3`): hook `1.5-inst`
    carries each text up to 512 bytes and its caller (`65d9eb2`); the gate
    checks it against the md5, matches 3 package templates, and groups the
    rest per place and caller as `run-time-texts` (`a018a0a`); records in
    the spec and dry-run note (`8eeefd3`). The re-run: 119 obligations
    become 1 (all 107 conditions listed), 12 texts match templates, 142 of
    142 verbatim texts hash to their md5s, and the 34 outputs stay
    identical to attempt-02's. One defect found and fixed: R reports a
    promise forced in a data mask as its own parent, so the conditions'
    caller read as `base::parse`; it is now `promise`. 595 tests pass.
  - **Q2:** start the final review after Q1 (a). That means the full
    herskind re-run through the agentic workflow (Shawn approves the plan
    and launches it; it passes the API review gate), then one round with
    Astra and Fable.
  - **Q3, the correction ledger:** ruled except L5 and L17. L1 (a), L2
    (a), L3 (a), L4 (a), **L6 (c): the gate runs dye, herskind, and
    marwick**, plus crema's leg, L7 (a), L8 (a), L9 (b), L10 (a), L11 (a),
    L12 (a), L13 (a), L14 (a), L15 (a), and L16 (a). Applied on PR #10 at
    `e4f5b94` (ledger 0.2.0-draft).
    - **Open, L5:** Shawn asked whether crema's figures repeat Table 1.
      They mostly do not: Table 1 covers case studies 1a and 1b only, and
      Figs 2 (simulation tests) and 5 (all of case study 2) appear nowhere
      else. The recommendation is revised to (c), all five figures in the
      leg.
    - **Open, L17 (new):** under L11 (a), marwick's Fig. 2 can be
      regenerated only from `supplement-GAMS-details.qmd`'s `eval: false`
      brms chunk ("this takes a few hours"), and its saved fit is not in
      the tag 1.3 tree. The recommendation is (a): outside the gate, as a
      stated scope limit like crema's full-MCMC path.
  - **Q4 (a):** erratum-log Entry 7 on PR #10 (`9b66683`), with the OSF
    note queued as item 1 of a new "Queued amendment 4 scope" list.
  - **Working notes:** Shawn accepted every pending candidate.
    [x] 2026-10-09 WN-am to WN-aq written as Obs 51 to 55 (`35a0f84`),
    re-verified at source. On the way, the writer corrected two anchors:
    the abductive entry of 2026-10-05 is in
    `wiki/reflections/abductive-reasoning.md`, and WN-ap's 98,004
    characters come from `session-reflection.md` Entry 24, not the
    lodgement script's header. Obs 53 places D-7's ruling in session
    fabeab56's walk-through, not b1a1e102's. **User observations:**
    deferred.
  - **Next, Q2:** the full herskind re-run through the agentic workflow,
    which Shawn launches (API gate, plan approval), then one review round
    with Astra and Fable. Open decision: run it on PR #7's branch with the
    shakedown's settings (attempt-03, effort high, rulings R1 to R4), or
    after PR #9's instruments merge.
  - Astra was mailed PR #10's new head (outbox,
    `20261009T021635.717643Z-claude-correction-ledger-ruled-new-head.md`).

- **⏩ START HERE: an AUTONOMOUS OVERNIGHT session (Shawn, 2026-10-08).**
  Get as far as possible by morning. When blocked on one track, switch to
  another. Stop and wait only for a decision that is genuinely Shawn's, and
  record it under "Questions for Shawn" below. Amendment 3 is LODGED, so
  amendment 3 §10's steps 2 onwards are unblocked.
- **Overnight progress (Opus 5.5, session be70c3be, 2026-10-08):**
  - [x] 2026-10-08 Track 1 step 1, the gate's account of load events,
    pushed to PR #7 (`4bf14e8`, `1c0bfe0`, `63eb010`, `9944be7`; 520 tests
    pass). Three defects found and fixed on the way (spec §2.4): `-e` text
    was hashed escaped, a fork's nesting used the parent's numbering, and
    the hook and shim were not bound to the launch commit. A
    launcher-matrix test image is built locally
    (`llmr-launcher-matrix:4.3.2`, from
    `tests/fixtures/launcher-matrix/Dockerfile`).
  - [x] 2026-10-08 Track 1 step 2, `PKGBUILD`, the littler shim, and the
    census rules, pushed to PR #7 (`eba8d98`, `40e2c54`, `d7caf2c`; 538
    tests pass). The probes overturned the spec's premise (`R CMD
    INSTALL`'s inner start does load the hook; its code arrives on stdin),
    so the shim now captures stdin scripts and the gate binds them by
    content. They also found callr children evading the hook (an A, fixed
    by a re-pin in the shim) and `R -f` scripts unlogged (a D, fixed).
  - [x] 2026-10-08 Track 1 steps 3 to 5 pushed to PR #7: the launcher
    matrix (every §13 launcher runs the authors' code with no finding of
    the account's own; `a3f2b47`, `8bae60d`), the semantics-neutrality
    test (`77b577e`), fresh computation and static checks (`ed9dd23`), and
    the lane's own conversion comparison (`a45d3c6`), with spec records
    after each. 575 tests pass. **`openpyxl` is now a requirement**: run
    `venv/bin/pip install -r requirements.txt` on zbook and amd-tower.
    The matrix image needs a one-off local build on each machine (its
    Docker tests skip without it).
  - [x] 2026-10-09 Track 1 step 6 pushed to PR #7: the transcript audit
    (`2cef8c7`) and the workflow switch (`40fdd58`: executor brief v1.3,
    definition v1.4, preparation prompt v1.4, `GATE_VERSION` 1.3,
    `snapshot-code` retired, `coverage_creditable` dropped). **The gate 1.3
    build is complete** (all six §15 steps); 590 tests pass at `230134f`.
  - [x] 2026-10-09 A dry run of the herskind pilot's execution layer
    (no agents, no model calls): `wiki/planning/reproduction-gate-1-3-pilot-dry-run.md`
    on PR #7. The run sealed complete and all 34 CSV and text outputs are
    byte-identical to attempt-02's. It found a defect, fixed (`f5b77d7`:
    an original run part by part read as never run), and raised Q1 below.
  - [x] 2026-10-09 Track 2 on PR #9 (branch
    `feat/amendment-3-instruments`, head `276b7e5`, open, not merged):
    five frozen instruments edited to the lodged text, namely
    fair-instrument 2.2 (§4), and verdicts-and-precision,
    data-availability-taxonomy, coverage-rules, and invariants 1.1 (§7(a)
    to (d)). Mirrors re-spliced, seven agent definitions moved to the new
    versions, manifest digests re-registered, and erratum Entry 6 added.
    Astra's review is requested by mail (outbox, 2026-10-08T13:34Z).
  - [x] 2026-10-09 Track 3: **the draft correction ledger is on PR #10**
    (draft, branch `feat/correction-ledger-draft`, head `0ad4b50`, not
    merged; worktree `.claude/worktrees/correction-ledger-draft`). Marked
    DRAFT: not ruled, frozen, or hashed. All five pilots, 46 targets, and 16
    rulings (L1–L16), in
    `studies/open-science-compliance/outputs/validation/correction-ledger/`.
    `check-printed-values.py` finds 239/239 printed values on their cited
    PDF pages. An operator run of dye's section 5 and 7 code,
    byte-identical, confirms the corrected 0.999667 (ruling L9). Astra's
    review is requested by mail (2026-10-08T14:10Z). Q3 and Q4 below.
- **Track 1 (primary): gate 1.3 instrumentation on PR #7.** Branch
  `feat/lane-gate-1-1-code-audit`, head `7d577b8`, open and not merged.
  Worktree: `.claude/worktrees/agent-a8a2378c2a5dbdc98`. Work in the order
  of the specification's §15 checklist
  (`wiki/planning/reproduction-gate-1-3-design.md` in the worktree):
  1. the gate's account of `LOAD`, `TEXT`, `CONN`, `PKG`, and `HOOKERR`
     (§8), with per-load binding of nested loads (D-3) and the md5 of every
     original;
  2. `PKGBUILD` for `R CMD INSTALL`, the littler shim, and the remaining
     census rules;
  3. the launcher matrix (§13);
  4. the semantics-neutrality test (§13);
  5. fresh computation (§9), conversions (§11, with revision 2's datetime,
     collision, and sheet rules), and the static additions (§10);
  6. the transcript audit (§12), the remaining acceptance tests, and the
     workflow switch.

  Probe R behaviour in Docker before relying on it (Docker 29.2.1 and
  `rocker/r-ver:4.3.2` are local; no pulls are needed). Tick §15 items
  with dates as they land. Commit and push to the PR branch after each
  step. The worktree's local branch (`worktree-agent-a8a2378c2a5dbdc98`)
  has no upstream, so push with
  `git push origin HEAD:feat/lane-gate-1-1-code-audit`. 525 tests passed
  at `7d577b8` (re-run 2026-10-08). The final review (§2.2, with the
  herskind pilot re-run) needs Astra and Fable, so prepare it but do not
  wait on it.
- **Track 2: §10 step 2, the instrument edits, on a new branch and PR.**
  Do not merge. Edit the frozen instruments to amendment 3's lodged text
  (tag `osf-amendment-3-2026-10-08`):
  - the FAIR instrument goes from v2.1 to v2.2 with §4's items (AP-3 and
    AP-7 to AP-17). Keep the Pass 6 mirror's normative blocks
    byte-identical
    (`extraction-system/prompts/06-infrastructure_pass6_prompt.md`), and
    handle the receipt token for the push consumers;
  - the four reproduction instruments take §7(a) to (d) verbatim:
    `verdicts-and-precision.md`, `data-availability-taxonomy.md`, and
    `coverage-rules.md` in
    `studies/open-science-compliance/protocol/instruments/`, and
    `.claude/shared/invariants.md`. §7(d) carries the B1 ruling, under
    which a failed pin is followed by its own neighbours. No lane code or
    prompt states the version search yet;
  - new versions and sha256 values go in `manifest.yaml`, following the
    v2.0 to v2.1 precedent (2026-08-15, erratum Entry 3; the manifest's
    `fair-instrument` comment);
  - run the D5 gate and the tests, and check consistency against the
    lodged text (maintenance rule 4).

  PR #7 also touches `manifest.yaml` and
  `reproduction-system/prompts/01-preparation.md`, so expect to rebase
  `manifest.yaml`. Where an instrument cannot take the lodged text
  cleanly, record a question and do not reinterpret the text.
- **Track 3 (if time): draft the correction ledger (§9) for Shawn to
  rule.** Use amendment 3 §9's per-target and per-paper fields, and the
  executed-code audit at `c4553f9` (tag `executed-code-audit-2026-10-04`,
  `findings.json`, with Q1 to Q10 ruled). Mark it DRAFT, and do not freeze
  or hash it. Freezing comes after his ruling (§10 step 3).
- **Stop rules.**
  - Never merge a PR. Make no OSF or other public post, and no paid model
    API call (none is needed).
  - Do not edit Codex-owned paths. Do not change what lodged text means.
  - Fable (peer session `llm-reproducibility-ea`, idle) can review by
    SendMessage. That spends top-tier credit, so use it for
    registered-text or design questions only, and say so.
  - Astra answers by mail only when Shawn runs Codex, so mail requests
    tonight for the morning.
  - Update this section at natural stopping points, so the morning read is
    current even if the session ends early.
- **Questions for Shawn (morning). All four RULED 2026-10-09; see NOW
  above:**
  - **Q1. 119 run-time texts on herskind, one obligation each.** The dry
    run's analysis builds 107 subset conditions that dplyr parses, and
    rlang, cli, and ggplot2 parse 12 more texts internally. The gate makes
    each a separate `unmatched-text` obligation on an md5, which a human
    cannot judge, and admission would need 119 rulings. Options:
    (a) build the dry-run record's design before the final review, so that
    the reviewers see one coherent build: verbatim short texts with their
    verified caller, templates for package internals, and one obligation
    per place and caller; (b) ask the reviewers to classify it first
    (spec §16, question 6), then build; (c) accept it as an operability
    limit. **Recommendation: (a).** It changes evidence, not rules, and
    admission is impractical without it on any dplyr or ggplot2 analysis.
    About an evening's work.
  - **Q2. When to start the final review.** It needs the full herskind
    re-run through the agentic workflow, which you start (plan approval,
    multi-agent launch), and Fable's review spends top-tier credit.
    **Recommendation:** after Q1 and the full re-run, one round for both
    reviewers, as §2.2's stopping rule intends. Nothing is sent to Fable
    tonight; Astra's review requests are in agent mail (see below).
  - **Q3. Rule the correction ledger (PR #10).** The sixteen rulings are in
    `correction-ledger.md`, each with options and a recommendation. Two
    carry the rest: **L1**, the target list (no pilot has a locked list, so
    the draft uses each attempt-01 report's compared items), and **L4**,
    "unchanged" meaning that the expected result equals the pilot's,
    whatever the pilot's credit eligibility. **L6 recommends dye and
    marwick** as the gate papers, plus crema's registered leg: dye has 11
    testable unchanged targets, marwick 8, herskind 2, key and crema none.
    The draft also found pilot errors the audit missed:
    - marwick's printed Kendall's W is 0.64, where the pilot recorded
      "~0.70" and credited an exact match;
    - dye's pilot "published" branching values were its own output.
  - **Q4. A lodged example rests on a pilot transcription slip (ledger
    L16).** Audit Q5(ii) sends key's "two inconsistent cells (3.1%,
    19.6%)" to the paper-error protocol, and lodged amendment 3 §7(d)
    repeats it as an example. The paper prints Midland Thickness 19.6 and
    Clovis Mass 3.1; the pilot's wrapper swapped them (attempt-01
    `run-analysis.R` lines 260–261). The rule itself is unaffected; only
    its example fails. Options: (a) an erratum-log entry only; (b) also an
    OSF note, now or with the next amendment. **Recommendation: (a) now,
    with (b) folded into the next amendment.** It changes no rule, so a
    standalone OSF update would be noise. The gate is unaffected, because
    every key target is expected-untestable.
- **Done this session (2026-10-06 to 10-08):**
  - [x] 2026-10-06 Astra's amendment 3 review folded in (`23c72fc`);
    D-7 to D-9 and the revision's new rules ruled (`9536962`, `2f3529d`).
  - [x] 2026-10-06 Gate 1.3 specification revision 2 (`340f77d`), the F1
    completeness corrections (`e6fe231`), and the hook's loader traces
    (`7d577b8`).
  - [x] 2026-10-08 Shawn approved amendment 3. Opening paragraph and
    scope sentence ruled; Astra's follow-up (B1, S1, S2) folded in
    (`4258db8`); re-check "No blocking issues found".
  - [x] 2026-10-08 **Amendment 3 LODGED**: OSF revision
    `6ac775afb5ed5b4afee88a4a`, tag `osf-amendment-3-2026-10-08` at
    `abde9b1`, via `lodge-osf-amendment.py`. Round trip byte-identical;
    public page checked by Shawn. The draft's status block and the
    erratum log record it.
  - [x] 2026-10-08 personal-assistant PR #169 merged (2026-10-07). Its
    worktree was already removed, and the composed `CLAUDE.md` carries
    its review-delivery rule.
- **Still with Shawn (not blocking tonight):**
  - user-observation candidates: the 2026-10-06 batch (A to C) and the
    2026-10-08 batch (A to D), both pending in `wiki/user-observations.md`.
    Deferred by Shawn, 2026-10-09;
  - [x] 2026-10-09 working-notes candidates WN-am and WN-an (b1a1e102),
    and WN-ao and WN-ap (session log below): accepted, with WN-aq;
  - PR #7's merge, after the final review.

  To start Astra here, run `~/gpt-hub/config/launch-codex.sh
  --no-alt-screen` from `~/worktrees/llm-reproducibility/sol-repro-entry`.
- **Carry-forward:** any git subprocess scrubs `GIT_*`. Reviews are
  documents, never posts. Mail to Astra uses `Project: llm-reproducibility`,
  `Lane: astra`.

## Repo state (2026-10-06, session b1a1e102 close) — superseded by the section above

- **⏩ START HERE: amendment 3 lodgement, then Astra's review, then gate 1.3
  instrumentation.**
  1. **Lodgement** (Shawn reading the draft at handoff). Once he has read
     and edited `studies/open-science-compliance/prereg/amendment-3-draft.md`,
     run the pre-lodgement checklist's steps 2–6 on the final text:
     - consistency against the logs, rulings, planning note, F2 report, and
       manifest;
     - token checks (numbers, identifiers, dates, and quoted strings);
     - register exit checks;
     - the manifest gate and tests green at the commit, and the tag
       `osf-amendment-3-<date>`;
     - the paste artefact.

     Then **ask before lodging** through the OSF API. Lodgement is step 1
     of §10; the correction ledger (§9) is ruled after it. **Astra was asked
     for a review of the draft** (2026-10-06, at Shawn's request:
     `~/agent-mail/claude/outbox/codex/20261006T071537.739395Z-claude-repro-amendment3-review.md`,
     against `38b59b0`, Workstream `amendment-3-review`). Fold its blocking
     and should-fix findings in with Shawn's edits before running the
     checklist.
  2. **Astra's review** of the gate 1.3 specification. It was requested by
     `~/agent-mail/claude/outbox/codex/20261005T062134.544396Z-claude-repro-gate13-consolidated.md`
     against `53413bc`, and had not arrived by 2026-10-06. Replies land in
     `~/agent-mail/codex/outbox/claude/`. Fold it in against revision 1
     (`b409ef5`) as revision 2, classifying findings by §2.1, and fix
     anything D or A it finds in F1–F3.
  3. **Gate 1.3 instrumentation** (§15 step 4) on PR #7
     (`feat/lane-gate-1-1-code-audit`, head `42da7fc`, **open, not
     merged**; worktree `.claude/worktrees/agent-a8a2378c2a5dbdc98`):
     - the full hook (§8), with traces installed *before* the profile
       (Fable's D-1);
     - `PKGBUILD` for `R CMD INSTALL`'s inner start;
     - the littler shim;
     - the launcher matrix in Docker, on a test image with `callr`,
       `targets`, `future`, `knitr`, and `rmarkdown` from CRAN.

     Then the remaining §15 steps, including the workflow switch to
     `run-container`.
- **Why it matters.** The registered §8 regression gate cannot run until
  gate 1.3 is merged and the correction ledger (amendment 3 §9) is ruled.
  §2 of the specification now has a stopping rule for hardening, which
  session reflection 22 asked for. After the final review, only a defect
  or an ordinary route reopens the build.
- **Done this session (2026-10-05):**
  - [x] 2026-10-05 The digest cache is confined to one snapshot
    (`664bb72`). Two of its six tests failed on the old cache.
  - [x] 2026-10-05 **Consolidated specification** (`53413bc`). The draft
    is archived at
    `archive/planning/reproduction-gate-1-3-design-draft-2026-10-05.md`.
    The three conflicts are resolved, and the §2 stopping rule classes
    findings as defect, ordinary, deliberate, or outside the model. It was
    sent to Astra by mail and to Fable by SendMessage.
  - [x] 2026-10-05 **A Docker probe** on `rocker/r-ver:4.3.2` settled
    start-up facts; they are listed at the top of the specification. For
    example, a project `.Renviron` overrides `R_PROFILE_USER` set by
    `docker run -e`.
  - [x] 2026-10-05 **Fable reviewed the consolidated text**
    (`~/agent-mail/claude/outbox/claude/20261005T062807.778832Z-claude-pr7-fable-gate-1-3-spec-review.md`,
    plus two SendMessage follow-ups on `R CMD`). Folded in as revision 1
    (`b409ef5`).
  - [x] 2026-10-05 **The foundations are built:**
    - F1, `run-container` and sealed run records (`0ce7f25`);
    - F2, consumption, credited runs, and output citations, with
      comparison schema 1.1 (`f07763a`);
    - F3, issues, rulings, and admission (`59f4e58`).

    488 tests pass, including 9 Docker tests that skip without the local
    `rocker/r-ver:4.3.2` image.
- **Awaiting Shawn — cleared on 2026-10-06** in a decision walk-through:
  - [x] 2026-10-06 **Amendment 3 D-1 to D-5 ruled** (`c99c2a0`):
    - D-1: lodge the clarifications as instrument v2.2;
    - D-2: planned platform-row rules, deciding 0s only;
    - D-3: the re-validation gates on all 150 items;
    - D-4: the census curation procedure is deferred to a later amendment,
      with constraints fixed now;
    - D-5: the corrected BI wording, with the `input` tag clarified.
  - [x] 2026-10-06 **Audit Q2–Q10 ruled**: `question_rulings` in
    `findings.json` (`c4553f9`, PR #7). The general rules from Q5 and Q6
    are in amendment §7(d) (`38b59b0`).
  - [x] 2026-10-06 **Astra's two PR #7 reviews** now open with an
    attribution line. The review protocol for both agents is documents,
    not posts, with a bot account later; the shared-guidance proposal is
    personal-assistant PR #169.
  - [x] 2026-10-06 **PR #8 merged** (`7f84e73`).
  - [x] 2026-10-06 **WN-ag to WN-al accepted**, as Obs 45–50 (`a8da2e1`).
    They were re-verified on writing, and WN-al's "non-overlapping" claim
    was dropped.
  - [x] 2026-10-06 **User-obs adjudicated** (`10a75c0`):
    - 2026-10-04 s2: A, B, and E kept, E generalised;
    - 2026-10-05: A (generalised), B, and C kept.
  - [x] 2026-10-06 **Lane script split:** after gate 1.3 merges (§15 of
    the specification).
  - [x] 2026-10-06 **Record-weighted coverage:** not collected.
- **Still with Shawn:**
  1. **Read amendment 3 in full** (`studies/open-science-compliance/prereg/amendment-3-draft.md`),
     then Claude runs the pre-lodgement checklist (steps 2–6) and asks
     before lodging through the OSF API. Text written 2026-10-05/06: §5(b)'s
     planned-rules bullet, §6(d)'s curation constraints, the two new
     §7(d) bullets, and the ruling notes.
  2. **Merge personal-assistant PR #169** (review delivery). Then re-run
     `scripts/compose-global-claude-md.sh`.
- **Work the rulings created** (after lodgement, in §10's order unless
  noted):
  - **Draft the correction ledger** (§9 fields) from the Q1–Q10 rulings,
    for Shawn's ruling; it is frozen before the regression run.
  - **Regression re-runs**, through gate 1.3's `run-container` once it is
    merged:
    - dye: wrapper-only, with the authors' files restored;
    - key: wrapper-only, executing the authors' script; rows on
      reconstructed inputs are expected-untestable;
    - crema at v1.0.0, with `rnaturalearthhires` pinned at build;
    - marwick at 1.3;
    - herskind: attempt-02 is the baseline.
  - **Q10:** store the crema v1.0.0 and herskind v1 deposits in the corpus
    store, with manifest entries (URLs and sha256 are in `findings.json`).
  - **D-2:** build and validate the 0-only platform-row rules before census
    scoring.
  - **D-4:** draft the census curation-procedure amendment before census
    scoring.
- **Owed by Claude:**
  - review the halt-condition mnemonics with Shawn during the next run
    (user-obs 2026-08-15 A);
  - build a usage source that records final usage before census cost
    tracking (F-019, item 3).
- **Carry-forward:**
  - **After personal-assistant PR #169 merges:** re-run
    `scripts/compose-global-claude-md.sh`, then remove the worktree
    `~/worktrees/personal-assistant/claude-review-protocol`.
  - [x] 2026-10-06 **Git hook re-installed on AMD-tower-ubuntu** after PR #8. The
    diff was exactly the `AGENTS` filename exception. Other machines pick
    it up when they next run `scripts/install-git-hooks.sh`, which zbook
    still needs anyway.
  - **Nothing is admission-eligible yet, by design.** Admission needs a
    transcript audit that writes `transcript-audit.json` (§12), which is
    not built.
  - **Transition.** The executor and workflow still use `snapshot-code`.
    Run records become mandatory, and `coverage_creditable` is dropped, at
    the workflow switch (§15 step 7). Until then, `check-code` verifies run
    records wherever `lane-records/` exists.
  - **Worktrees.** The PR #7 worktree is
    `.claude/worktrees/agent-a8a2378c2a5dbdc98`, branch
    `worktree-agent-a8a2378c2a5dbdc98`, pushed as
    `feat/lane-gate-1-1-code-audit`. Fable's worktrees
    `~/worktrees/llm-reproducibility/claude-fable-pr7` and `…-pr7-fix` can
    be removed.
  - **Fable** is the open session `llm-reproducibility-ea`. Reviews by
    SendMessage work both ways.
  - **Git safety.** Any code that runs git as a subprocess scrubs `GIT_*`.
  - **Review briefs** ask for replies by mail or file, never GitHub posts.
  - **Infrastructure.** At session start, Syncthing reported the
    zbook-ubuntu peer absent for 65 hours.
  - **From earlier sessions:**
    - unrecorded originals (Key's supplement archives; the crema v1.0.0
      and herskind v1 deposits, audit Q10);
    - relay R2 is provisional;
    - the hook fault is with personal-assistant-0e;
    - zbook still needs `install-git-hooks.sh` and a venv;
    - the `llmr-*-attempt-02` Docker images are kept.

## Repo state (2026-10-05, session ef0412bd close) — superseded by the section above

- **⏩ START HERE: consolidate the gate 1.3 specification, then build its
  foundations.** The reproduction lane's integrity gate is on PR #7
  (`feat/lane-gate-1-1-code-audit`, head `2bd35aa`, **open, not merged**).
  Its plan is `wiki/planning/reproduction-gate-1-3-design.md` on that
  branch: status "NOT ready to build", and its last section, "Consolidated
  build plan", gives the order. In that order:
  1. **Fix the part 1 digest cache** (`cached_digest` in
     `scripts/reproduction-lane.py`). Confine it to one immutable snapshot,
     since an edit that keeps the size, with its mtime restored, could
     return a stale digest (Astra's design review, point 5). Add a test.
  2. **Write the consolidated specification:** one text replacing §§1–7 and
     both revision sections. Resolve the three conflicts it lists, and state
     a **stopping rule for hardening**, since the threat model assumes a
     good-faith executor (session reflection 22). Send it to Astra (mail,
     Lane astra) and Fable (a Claude session; by SendMessage if it is still
     open, otherwise Shawn starts one) before building.
  3. **Build the foundations, in Astra's order:**
     - the record boundary: a host-captured stream and sealed receipt, with
       records outside the input tree;
     - run and output binding: per-run empty outputs, the image id, a lock,
       and failure states;
     - ruling binding: issue id plus evidence fingerprint, raw against
       admitted coverage, and the blocking rules.

     Then the R loader hook and child-process matrix in Docker
     (`rocker/r-ver:4.3.2` is local), fresh-computation policy,
     conversions, transcript audit, and acceptance tests. Then a final
     review by both peers.
- **Why it matters.** The registered §8 regression gate cannot run until
  gate 1.3 is merged and the correction ledger (amendment 3 §9) is ruled.
  The executed-code audit found the pilot baseline weaker than the gate
  assumes:
  - three pilot attempt-01s ran re-implementations;
  - crema and marwick ran versions other than the AP-12 one;
  - crema's Table 1 was credited against v2.0.0's own re-run (0.1003,
    against the paper's 0.1023).
- **Done this session (2026-10-04 third session → 10-05):**
  - [x] 2026-10-04 The F2 rule (AP-15), harvester v1.2, the v1.2 packs, and
    the hybrid validation:
    - commits `8864ceb`, `4c77b67`, `6c8ed51`, `cf0d92e`, `06c1ca9`,
      `ff278ff`, and `07b6fba`;
    - the rule matches the reference on 10/10 pilot F2 items (the model on
      4/10);
    - the hybrid at `medium` scores 137/141 (BI excluded) and 139/150
      (all items).
  - [x] 2026-10-04 The F2 miss is an input gap: the v1.1 packs had no
    keywords, and 20 of 90 Opus F2 evidence strings say so.
  - [x] 2026-10-05 **Amendment 3 full draft**,
    `studies/open-science-compliance/prereg/amendment-3-draft.md` (`4c5bdf7`,
    `1763b2a`, `f3fb3a7`, `208bf5e`). Shawn's rulings:
    - D-6 RULED: adopt Astra's correction ledger, now §9;
    - Fable's ledger conditions drafted into §9;
    - **class (ii) consequence RULED** in §7(d): a result resting on an
      authors' file edited for mechanics counts only after a wrapper-only
      re-run. So **dye's 22 attempt-02 targets need re-running.**
  - [x] 2026-10-05 Reproduction-lane code hashing and the one-off
    executed-code audit, built on PR #7. Not yet merged, so the two checklist
    items in `wiki/planning/deterministic-output-checks.md` stay open until
    the merge.
  - [x] 2026-10-05 PR #7 went through three cross-model review rounds:
    - Astra, two code reviews and one design review;
    - Fable, one code review and one design review.

    Gate 1.2 (`458878b`, `43a3453`, `0d87a8f`) and gate 1.3 part 1
    (`5766fb4`, `4244a51`) are built, and 421 tests pass. Design review
    commits: `5e741a3`, `71fb731`, `2bd35aa`.
  - [x] 2026-10-05 Claude-to-Claude agent mail queued as infrastructure
    (PA data `64b36a3`).
- **Awaiting Shawn:**
  1. **Amendment 3 decisions D-1 to D-5** (D-6 is ruled) and lodgement on
     OSF. The order of operations is §10 of the draft.
  2. **The audit's questions Q2–Q10**, in
     `studies/open-science-compliance/outputs/validation/executed-code-audit-2026-10-04/findings.json`
     on PR #7. Q1 is answered by the class (ii) rule. These feed the
     correction ledger.
  3. **Astra posted two PR #7 reviews to GitHub under your account,**
     because my first two briefs invited it (claude-obs 70). Decide whether
     that is acceptable. Fable's review is unposted, at
     `~/agent-mail/claude/outbox/claude/20261005T044136.617510Z-claude-pr7-fable-review-reply.md`.
  4. **PR #8**, Codex's `AGENTS.md` entry point (`sol/repo-agent-guidance`):
     your review. It is a Codex-owned file.
  5. **Held over:** working-notes candidates WN-ag to WN-ai (previous
     session) and **WN-aj to WN-al** (session log below); user-obs
     2026-10-04 s2 A–E and **2026-10-05 A–D**
     (`wiki/user-observations.md`).
  6. **Low priority, before the census:** an optional record-weighted
     coverage field in the output schema.
- **Owed by Claude:**
  - review the halt-condition mnemonics with Shawn during the next run
    (user-obs 2026-08-15 A);
  - build a usage source that records final usage before census cost
    tracking (F-019, item 3).
- **Carry-forward:**
  - **Worktrees.** The PR #7 worktree is
    `.claude/worktrees/agent-a8a2378c2a5dbdc98`, branch
    `worktree-agent-a8a2378c2a5dbdc98`, pushed as
    `feat/lane-gate-1-1-code-audit`. Fable's worktrees
    `~/worktrees/llm-reproducibility/claude-fable-pr7` and `…-pr7-fix` are
    clean and can be removed.
  - **Git safety.** Any code that runs git as a subprocess scrubs `GIT_*`.
    Hook-run fixtures without the scrub set `core.bare = true` on
    2026-10-05; it was repaired, and the scratchpad has the principle.
  - **Review briefs** ask for replies by mail or file, never GitHub posts.
  - **Claude-to-Claude.** Use SendMessage to live sessions; agent mail drops
    self-addressed messages until the backlog item lands.
  - **Unrecorded originals.** Key's supplement archives are not in the corpus
    store or manifest. The crema v1.0.0 and herskind v1 deposits are not
    kept either (audit Q10); URLs and sha256 are in `findings.json`.
  - **From earlier sessions:**
    - relay R2 is still provisional;
    - the hook fault is with personal-assistant-0e;
    - zbook still needs `install-git-hooks.sh` and a venv;
    - the `llmr-*-attempt-02` Docker images are kept.

## Repo state (2026-10-04, second-session close) — superseded by the section above

- **⏩ START HERE: pre-gate build, then amendment 3, then the registered
  regression gate.** The census scorer is CONFIRMED as `claude-opus-5-5`
  at effort `medium` (results:
  `studies/open-science-compliance/outputs/validation/opus-5-5-arms-2026-10/results-2026-10-04.md`).
  Next, in order:
  1. **No-spend pre-gate build** (ruled 2026-10-04; checklist in
     `wiki/planning/deterministic-output-checks.md`, "Next step"):
     - (B) the F2 rule (AP-15) from pack registry fields. Score it
       against the E8-v2 reference on the five pilots, then recompute both
       gates for the hybrid scorer (amendment 3 item 6(b) criteria);
     - reproduction lane: hash the authors' code files at retrieval and
       check that the executed copies are byte-identical;
     - a one-off audit of each pilot's executed code against the authors'
       originals, looking for undeclared repairs like dye's T02;
     - (C) Layer 3 flag-only evidence checks, which can follow the gate.
  2. **Amendment 3 full text** for Shawn to lodge on OSF. The running list
     is in `studies/open-science-compliance/prereg/erratum-log.md`, items
     1–8; items 5–8 were added today with draft wording. **Sequence:**
     Shawn lodges; then the frozen instruments are edited and
     version-bumped to the clarified text; then the regression gate runs
     under that text.
  3. **The registered regression gate** (with the Crema leg) on Opus 5.5
     `medium`, then the pre-census supplement check. **API gate:** present
     the model, mode, call count, and cost, and get Shawn's approval
     first.
- **Done 2026-10-04 (session `c5ee7a27`):**
  - [x] The three Opus 5.5 arms ran clean (`2c93a5d`, `656036f`, `7365e14`).
  - [x] Selection CONFIRMED: `claude-opus-5-5` at `medium`, amendment 3
    item 5. The commit carrying it is `6b79980`, mislabelled "Obs 37" by a
    git race; see `dbcb2db`.
  - [x] F-019 RULED, with a note added to the D4 record (`43cc274`).
  - [x] Dye T06 PAPER_ERROR (`bc54450`); dye's regression label is PASS
    (`22ee93b`).
  - [x] Bias described (`fa67244`).
  - [x] Mechanical-check policy RULED (`22ee93b`); Layer 1 built as
    `check-payload-quality.py` v1.1 (`132f95a`, report `d10fbb3`).
  - [x] Reproduction clarifications (a)–(d) RULED (`07666c8`), with the
    follow-ons (`4e0033e`). They are amendment 3 items 7 and 8.
  - [x] Observations 34–44. The obs-writer runs Sonnet, although its
    trailers say Opus 5.5 (the brief's error).
  - [x] All held user-obs batches adjudicated (`49243da`).
  - [x] Messages sent: the hook fault to personal-assistant-0e, with a
    correction; T06 and the scorer to cv-and-applications-d9.
  - [x] /reflect (`f22c72e`) and /handoff.
- **Awaiting Shawn:**
  1. **New working-notes candidates WN-ag, WN-ah, and WN-ai** (session log
     below).
  2. **New user-obs batch** for 2026-10-04 (second session), A–D
     (`wiki/user-observations.md`, pending section).
  3. **Low priority, before the census:** an optional record-weighted
     coverage field in the output schema. This is a governed schema
     change; see `deterministic-output-checks.md`, the Layer 1 coverage
     note.
  4. **Optional:** log the invented premise in my message to
     personal-assistant-0e with `/confab`. It is already recorded in
     `wiki/reflections/llm-observations.md` and claude-obs 66.
- **Owed by Claude:**
  - review the halt-condition mnemonics with Shawn during the next run
    (user-obs 2026-08-15 A);
  - build a usage source that records final usage before census cost
    tracking (F-019, item 3).
- **Carry-forward:**
  - **Relay (R2), provisional.** It fires only when a workflow launches in
    the same turn as a typed user message; launches from notification
    turns receive nothing. This is abductive-reasoning 2026-10-04 (second
    session), not yet a rule.
  - **Hook fault** (sync and index steps not refreshing their gates after
    the archive step): reported to personal-assistant-0e for a dedicated
    infra session.
  - **Git hygiene:** run any committing subagent in its own worktree, and
    commit by pathspec (claude-obs 65).
  - The pitch deadline is Fri 9 Oct.
  - zbook still needs `install-git-hooks.sh` and a venv.
  - Docker images `llmr-*-attempt-02` are still kept.

## Repo state (2026-10-04, arms run) — superseded by the section above

- **⏩ START HERE: the census scorer is CONFIRMED as `claude-opus-5-5` at
  effort `medium`** (Shawn, 2026-10-04). The three Opus 5.5 arms ran
  clean (`2c93a5d`, `656036f`, `7365e14`); all three clear both gates,
  and the analysis tool and H13 agree on every figure. Results:
  `studies/open-science-compliance/outputs/validation/opus-5-5-arms-2026-10/results-2026-10-04.md`.
  It is amendment 3 running-list item 5 (erratum log). **Next on this
  configuration:** the registered regression gate (with the Crema leg)
  and the pre-census supplement check.
- **Done 2026-10-04 (session `c5ee7a27`), after the arms:**
  - [x] Selection confirmed; recorded in the decision log and the erratum
    log (the commit carrying it is `6b79980`, mislabelled "Obs 37" by a
    git race; see `dbcb2db`).
  - [x] F-019 RULED ("Agree, add a note"); a note was added to the D4
    ruling record (`43cc274`).
  - [x] Dye T06 PAPER_ERROR on the version of record (`bc54450`).
  - [x] Bias described: no detectable general bias, plus one systematic F2
    over-credit shared across model generations (`fa67244`).
  - [x] Working-notes candidates cleared: Observations 34–44 (WN-l, m,
    p+r, q, y+z, aa, ab, ac+F-019, ad, af; WN-ae folded into Obs 34). The
    commits were written by the obs-writer agent, which runs Sonnet,
    although its trailers say Opus 5.5 (the brief's error).
  - [x] User-obs batches cleared: 2026-08-03, 08-15, 08-19, 10-03, and
    10-04 (`49243da`).
  - [x] Session-hook fault reported to personal-assistant-0e for a
    dedicated infra session (with a correction to one invented
    hypothesis in the first message).
  - [x] Pitch session (cv-and-applications-d9) told that T06 is confirmed.
- **Awaiting Shawn:**
  1. confirm dye's regression label as **PASS on the substance** (the
     shakedown results, ruling 7);
  2. rule on the disagreement policy for mechanical checks
     (`wiki/planning/deterministic-output-checks.md`, "Proposed position":
     compute derived fields; validate and then amend for rule-determined
     items such as F2; flag-only for judgement items);
  3. before the registered gate: instrument-clarification candidates
     (a)–(d) (shakedown results, "Rulings (2026-10-04)").
- **Owed by Claude:** review the halt-condition mnemonics with Shawn
  during the next run (user-obs 2026-08-15 A; missed during the arms);
  run `/handoff` for session `c5ee7a27`.

## Repo state (2026-10-04) — superseded by the section above

- [x] 2026-10-04 **Run the three Opus 5.5 arms** (session `c5ee7a27`).
- **⏩ START HERE: run the three Opus 5.5 arms. They are APPROVED.**
  Shawn approved API gate stage 2 at session close on 2026-10-04: run all
  three arms, `high` → `medium` → `xhigh`, sequentially with per-arm hard
  stops, and continue unless something goes wrong. The estimate is about
  $42 API-equivalent, plan-billed. Everything is built, and the P4 probe
  passed (`wf_85e5e3d2-e19`, commit `9553f46`). Design and rulings:
  `studies/open-science-compliance/outputs/validation/opus-5-5-arms-2026-10/design-note.md`.
- **Per-arm procedure** (from the scripts' CLIs, checked 2026-10-04):
  1. **Check the session.**
     - The tree is clean.
     - `fair-assessor-opus-5-5` appears in the available-agents list
       (register F-018; it is registered in `manifest.yaml`).
     - If any governed file has changed since `9553f46`, re-run P4 first.
       Governed files: the agent definition, instrument, guide, schema,
       workflow, and args builder.
  2. **Build the args:**
     `venv/bin/python scripts/build-benchmark-args.py opus-5-5 --effort <level> --out <scratch>/args-<level>.json`.
     Builder v1.5 stamps `args_checksum`.
  3. **Launch** `Workflow({scriptPath: "<repo>/studies/open-science-compliance/protocol/validation/fair-benchmark-arm.workflow.js", args: <the JSON, verbatim>})`.
     Workflow v1.7 refuses altered args.
  4. **Reconcile** (authoritative pass, H15):
     `venv/bin/python scripts/reconcile-run.py <transcript-dir> --expect-spawns 15 --require-pack`.
     It must come back clean.
     **Corrected 2026-10-04:** that command is incomplete. The registered
     arms' pass also used
     `--contract-schema assessment-system/schema/benchmark-fair-output-schema.json`
     and `--out <transcript-dir>/reconciliation-authoritative`, and the
     assembler refuses to run without the latter.
  5. **Assemble:**
     `venv/bin/python scripts/assemble-arm-record.py <transcript-dir> opus-5-5 studies/open-science-compliance/outputs/validation/opus-5-5-arms-2026-10/arm-opus-5-5-<level> --expect-effort <level> --expect-launch-commit <hash>`.
     Pass `--environment key=value` pairs as in earlier records
     (`billing_route=max-plan`, `operator_ruling=...`). Assembler v1.6
     counts tokens per request.
  6. **Commit the arm, then launch the next.**
- **Halt conditions:** stop and report, do not continue, on any of:
  - H3: more than 2 reconciliation failures or ESCALATEs in an arm;
  - H4: more than 4.5M per-request contract-metric tokens for an arm;
  - a checksum refusal, or any anomaly.

  The governed-edit freeze runs from arm 1's launch until arm 3 is
  committed.
- **After the three arms:**
  1. Run `analyse-benchmark-disagreements.py` v1.2 over all nine arm
     directories, with `--reference-key pilot_fair_assessments_v2`, both
     with and without `--exclude-bi`.
  2. Run the H13 script as the second derivation.
     **Gotcha:** `h13-rederivation-2026-10-04/h13-rederive.py` hard-codes
     the six arms (`ARMS`, line 75), so add the three new ones.
  3. Run `gates-ruling-2026-10-04/selection-cost.py` with Opus 5.5 pricing.
     **Gotcha:** it has no `claude-opus-5-5` row ($4 / $20), and it uses a
     single 0.1× cache-read multiplier. Opus 5.5's cache reads are 0.05×
     ($0.20), so make the multiplier per-model.
  4. Apply the **pre-declared** rule (design note Q4): eligible only if
     both gates clear under the 2026-10-04 ruling; cheapest-eligible
     across all eligible configurations. Then get Shawn's confirmation,
     and if Opus 5.5 is selected, add it to amendment 3.
- **Done this session (2026-10-04):**
  - shakedown queue ruled (`b446415`);
  - PRs #6 and #5 merged (`783f7e2`, `d92fd30`) and the `claude-e8v2`
    worktree removed;
  - H13 (`976c573`);
  - gates ruled (`6c00a0b`): majority-vote concordance, BI-excluded
    admissible, both reported;
  - erratum-log Entry 5 drafted for amendment 3 (`6fb1f37`);
  - D4 by rule = `claude-opus-5` @ `high`, held for Opus 5.5 (`ad765b4`);
  - F-013 and F-015 fixed (`59d643b`);
  - args guard (`c8eca55`);
  - Opus 5.5 arm built and probed (`c3cb02d`, `9553f46`).

  Details are in the session log below and in the plan's decision log
  (`wiki/planning/instrument-clarification-plan.md`, rows dated
  2026-10-04).
- **Owed:**
  - **Shawn:** dye T06 version-of-record check
    (doi:10.1016/j.jas.2023.105765; record PAPER_ERROR if it still reads
    0.87).
  - **F-013:** re-derive the study cost estimate.
  - **F-017:** implement the prompt and audit changes before the next
    reproduction-lane run.
  - **Instrument-clarification candidates (a)–(d)** (shakedown results,
    "Rulings (2026-10-04)").
  - **Amendment 3** (erratum-log running list, items 1–5), lodged before
    census.
  - **Pre-census items**: supplement inputs, instrument clarifications,
    and the pre-census supplement check.
  - **Optional:** marwick-2025 as a third shakedown paper.
- **Carry-forward:**
  - The pitch deadline is Fri 9 Oct.
  - cv-and-applications-d9 was sent the rulings anchor and the herskind
    12/15 → 11/15 correction. The message was delivered but unread when
    sent.
  - Docker images `llmr-*-attempt-02` are still kept.
  - The archive-drift gate (`scripts/bulk-archive.py` in
    personal-assistant): status not re-checked this session.
  - zbook still needs `install-git-hooks.sh` and a venv.
  - The 128K output cap stands.
- **PENDING VERDICTS (no silent discard):**
  - NEW: user-obs 2026-10-04 batch A–D (pending section of
    `wiki/user-observations.md`);
  - NEW: working-notes candidates WN-ad, WN-ae, and WN-af (session log
    below);
  - still held: WN-aa, WN-ab, and WN-ac (2026-10-03 s2); the 2026-10-03
    first-session user-obs A–D; WN-y/z and user-obs A–C (2026-08-19);
    WN-l/m and user-obs A–C (2026-08-03); WN-p/q/r and user-obs A–D
    (2026-08-15).
  - The 2026-10-03 s2 user-obs batch was adjudicated today (A–C accepted,
    D discarded).

## Repo state (2026-10-03, second session — overnight close)

- **TWO PRs OPEN, both unmerged; `main` is untouched by them.**
  [#5](https://github.com/saross/llm-reproducibility/pull/5)
  (`feat/reproduction-workflow`, head `77e2d50`) holds the agentic
  reproduction lane and the Phase 2 shakedown.
  [#6](https://github.com/saross/llm-reproducibility/pull/6)
  (`feat/e8v2-registration`, head `6e0d17a`) holds E8-v2 registration,
  analysis tool v1.2, the six-arm concordance, and a launcher fix. Merge #6
  first or alongside #5: #5's `reproduction-lane.py` reuses the launcher
  function #6 fixes. #6 was built in a worktree,
  `~/worktrees/llm-reproducibility/claude-e8v2`; remove it after merge
  (`git worktree remove`; it holds an untracked `venv` symlink).
- **(1) Phase 2 — DONE as a pre-gate shakedown** (Shawn: not the registered
  §8 gate; that gate runs after model selection and adds the Crema leg).
  Results are in
  `studies/open-science-compliance/outputs/validation/phase2-shakedown/results-2026-10-03.md`
  (on #5).
  - **Verdicts:** herskind SUCCESSFUL, matching the pilot, coverage 12/15.
    Dye PARTIAL against the pilot's SUCCESSFUL, coverage 25/34.
  - **Values:** identical to the pilot wherever both attempts computed
    them (`regression-value-check.json`).
  - **Reviews:** both QUALIFIED, each supporting its executor's verdict.
  - **Cost:** herskind $7.50, dye $10.89 (API-equivalent, counted per
    request); human time about 7.5 min per paper from the `/track` log.
  - **Reported** to cv-and-applications-d9 by SendMessage (2026-10-03).
    It recorded the result in its
    `planning/cosmos-pitch-suggested-text-2026-09-25.md` §15 (commit
    `0c80fde`), with the PAPER_ERROR calls marked PENDING. **Owed:** a
    one-line message with the file anchor to cv-and-applications if Shawn
    confirms the PAPER_ERROR calls or approves marwick-2025.
- **(2) E8-v2 registration and concordance — DONE** (on #6;
  `e8-v2-concordance-2026-10-03/summary.md`). Over all 150 items only
  fable-5 clears both 0.90 gates. With the 9 BI items excluded, opus-5
  also clears at both efforts (0.922 xhigh, 0.901 high), and its errors
  are all over-credit.
- **NEXT, in order:**
  1. **Shawn clears the shakedown human queue** (results §"Human queue";
     items 1–9). These include dye T02 (the pilot's index shift: mechanical
     or not?) and T06 (the p.16 0.87 PAPER_ERROR), the herskind PAPER_ERROR
     calls, T11 versus T14 consistency, the dye L-level, and F-017.
  2. Decide on the **held-out artefacts**: dye
     `attempt-02/data/beads-1.csv` (unlicensed; identical to attempt-01's
     tracked copy) and `vendor/ArchaeoPhases_1.8.tar.gz`. Both are
     untracked in the main checkout.
  3. Merge PRs #6 and #5.
  4. **H13** fresh-context re-derivation, then **Shawn's gates ruling**,
     informed by the concordance readings. The central question is
     whether the BI-excluded figure is admissible.
  5. Optional: marwick-2025 as a third shakedown paper. It needs a plan
     approval and an API gate, at roughly $8–12.
- **Register entries awaiting ruling:**
  - **F-013:** the contract-metric token over-count, 1.9–2.9× and
    model-dependent, bears on cost claims and the cheapest-eligible rule.
  - **F-015:** Claude Code 2.1.288 indents spawn prompts. By inspection,
    FAIR-lane `assemble-arm-record.py` `PROMPT_RE` breaks on the next run;
    fix before the next FAIR run.
  - **F-017:** the Read-only pull check versus executors and reviewers
    that read with Bash.

  F-014 and F-016 are closed.
- **Paper-level findings (pending confirmation):**
  - herskind: Table 1 has 8 of 130 cells off by one against the authors'
    own S3, with v1/v2 data drift excluded by `input-drift-herskind.md`.
    The "nine" list names eight; C5–C12 is omitted.
  - dye: p.16's 0.87 is the Amethyst→Disc cell. The pilot's table had
    silently re-mapped it.
  - dye: the section-4 code fails under ArchaeoPhases 1.8, which the
    reviewer attributes to the package version.
  - dye: the corpus `vor.pdf` is the **White Rose accepted manuscript**,
    not the version of record (corpus mislabel).
- **Live state:**
  - Docker images `llmr-{herskind-riede-2024,dye-et-al-2023}-attempt-02`
    are kept locally for any approved T02 re-execution.
  - The main checkout is back on `main`.
- **Carry-forward:**
  - The archive-drift infra gate (2 raw sessions unarchived) was relayed
    at session start; run `scripts/bulk-archive.py` in personal-assistant.
  - The pitch deadline is Fri 9 Oct; cv-and-applications cited "Shawn
    sends on Tue 6 Oct".
  - zbook still needs `install-git-hooks.sh` and a venv.
  - The 128K output cap is standing.
- **PENDING VERDICTS (no silent discard):**
  - NEW: user-obs 2026-10-03 (second session) batch A–D, in the pending
    section of `wiki/user-observations.md`;
  - NEW: working-notes candidates WN-aa, WN-ab, and WN-ac (session log
    below);
  - still held: the 2026-10-03 (first session) batch A–D; WN-y/z and
    user-obs A–C (2026-08-19); WN-l/m and user-obs A–C (2026-08-03);
    WN-p/q/r and user-obs A–D (2026-08-15).

## Repo state (2026-10-03)

- **E8-v2 WORKSHEET COMPLETE** (`7da90bf`): all 150 reference items
  adjudicated in ten sittings (2026-09-03, 2026-10-01 → 10-03). Reference
  **110 → 95 of 150**; 39 items changed (27 down, 12 up); 9 tagged
  beyond-instrument (`worksheet.json` field `beyond_instrument`) so
  concordance can be reported with and without them. Reasoning and forward
  principles AP-1 to AP-17:
  `studies/open-science-compliance/outputs/validation/e8-v2-rederivation/adjudication-log.md`.
- **NEXT, in order (Shawn's sequencing):** (1) **Phase 2 regression test**
  (approved 2026-10-02, option (a); `wiki/planning/agentic-modernisation-plan.md`
  Phase 2 note): build a minimal reproduction workflow (planner → batched
  plan approval → executor → fresh-context adversarial reviewer, with
  artefact gates), then run herskind-riede (Zenodo v2 per AP-12) and dye,
  instrumenting per-paper cost (tokens, wall-clock, human minutes). Needs
  Shawn: plan approvals (~10–20 min) and the API gate. **Deadline: the
  Cosmos Ventures pitch must be submitted by Fri 9 Oct 2026.** Report
  results with file anchors to the cv-and-applications session by agent
  mail. (2) **E8-v2 registration and concordance:** assemble the reference
  from `worksheet.json`, register it in `manifest.yaml`
  `reference_datasets`, add a BI-exclusion option to
  `analyse-benchmark-disagreements.py`, then run the six-arm concordance
  with and without BI items (invocation in the 2026-08-19 block). (3) H13
  fresh-context re-derivation, then Shawn's gates ruling.
- **Open in Shawn's court:** confirm attempt numbering — regression test =
  dye attempt-02, the approved OxCal re-derivation → attempt-03 (recorded
  only as a working assumption).
- **F-010 CLOSED** — path rule; reconcile-run v1.5 (PR #4, merged
  `5ebb6a0`); replay of 13 reconciliations, one flip (crema r2 → clean);
  register F-012. Tests 267 → 277; gate 66/66.
- **Rulings with protocol consequences:** repair rule
  (`studies/open-science-compliance/protocol/data-repair-rule-2026-09-03.md`,
  routes a/b/c, effort bound ~3× the dye estimate); census spawns receive
  supplements (`studies/open-science-compliance/protocol/supplements-as-inputs-2026-10-02.md`;
  benchmark not re-run); "all rights reserved" → 0; F2 requires creators,
  title, content description, and ≥1 keyword; AP-12 refined (score and
  reproduce the cited version; always run supplement / published-values /
  date checks; unspecified versions flagged).
- **Amendment 2 precedent error:** the paper never cites
  10.5281/zenodo.14561925 — erratum-log Entry 4 (`dfc74ef`); registry entry
  withdrawn; public correction queued on the amendment 3 running list.
- **Pre-census queue** (plan pre-census items, `wiki/planning/instrument-clarification-plan.md`):
  instrument clarifications AP-8 to AP-17; harvester fields (file formats,
  descriptions, keywords, related identifiers, versions); a deterministic
  identifier check (presence in the paper's text, record-number matching,
  extraction records scanned too); supplement collection (Elsevier CDN
  route verified); census coding variables (licence-conflict type; "data
  shared, rights-incompatible"); amendment 3.
- **Findings logged:** Observations 30–33 in `wiki/working-notes.md`
  (licence conflicts; the noisy surface; the old reference's errors;
  resolution is not verification); Clarivate terms vs marwick's deposited
  Web of Science records (rights-incompatible); GPL-2-derived code under CC
  BY (key); herskind's pilot extraction cites two unrelated DOIs that
  resolve.
- **Carry-forward:** publisher supplement files fetched this session
  (herskind 3, key 5, crema 1) sit only in a scratchpad, not the corpus
  store — URLs and checksums are in the adjudication log; marwick's version
  of record is unresolved for reproduction (immaterial for scores); dye
  attempt-03 (OxCal re-derivation) accepted, after the worksheet; zbook
  still needs install-git-hooks.sh + venv; 128K output cap standing.
- **PENDING VERDICTS (no silent discard):** NEW user-obs 2026-10-03 batch
  A–D (pending section in `wiki/user-observations.md`); still held: WN-y/z
  + user-obs A–C (2026-08-19); WN-l/m + user-obs A–C (2026-08-03); WN-p/q/r
  + user-obs A–D (2026-08-15).

## Repo state (2026-08-19)

- **BALL IS IN SHAWN'S COURT — his two tasks, in order:** (1) **E8-v2
  worksheet sitting** (`outputs/validation/e8-v2-rederivation/worksheet.md`
  — adjudication columns still empty; 150 items, 68 disputed, 3 entailed
  flips, 10 spot-checks); (2) **F-010 pattern-vs-path ruling** (register
  entry is self-contained). Everything downstream of the sitting
  (all-arms concordance + error-direction → gates ruling → census
  selection) is now tooled and waiting. H13 fresh-context re-derivation
  is Claude's, sequenced at the gates stage.
- **ANALYSIS TOOL v1.1 SHIPPED** (`48568fb`, 2026-08-17 evening): the
  `--arms` carry-forward is CLEARED. `--arms` takes explicit arm dirs
  spanning cycles (labels from `arm-*` basenames, duplicate labels
  rejected; `--out-dir` required so no cycle's committed
  disputed-items.json is overwritten); per-arm error-direction split
  (over-/under-credit + per-item `error_direction`); `--reference-key`
  (E8-v2 reference joins by manifest registration, not code edit);
  guideless-minority reporting generalised to every arm. Verified:
  legacy mode byte-identical to committed 2026-08 disputed-items;
  six-arm `--stability-only` pass matched every known figure. Tests
  251 → 267; gate 66/66.
- **Found en route: the guideless predicate was VACUOUS post-A3** — all
  90 spawns in the 2026-08-17 cycles reported guideless because A3's
  pull→push promotion (2026-08-15) moved the guide from
  `pulled_files_read` into `instrument_receipts` and the detector was
  pull-era. Fixed (two-era detection, same commit). Corollary: the
  guideless-minority correlation is era-bound — structurally
  unmeasurable on post-A3 data (treatment group cannot exist). Logged in
  reflections (abductive + llm-observations); working-notes candidates
  WN-y/WN-z pending Shawn's verdict below.
- **Gates-stage invocation (ready to run once E8 v2 lands in the
  manifest):** from repo root, `venv/bin/python
  studies/open-science-compliance/protocol/validation/analyse-benchmark-disagreements.py
  --arms <V>/benchmark-2026-08-17/arm-{sonnet-5,opus-5,fable-5}
  <V>/effort-study-2026-08-17/arm-{sonnet-5-high,sonnet-5-max,opus-5-high}
  --reference-key <e8-v2 manifest key> --out-dir <new analysis dir>`
  where `<V>=studies/open-science-compliance/outputs/validation` (drop
  `--stability-only` for the concordance pass; brace expansion needs a
  shell, else list the six dirs).
- **PENDING VERDICTS (no silent discard):** NEW this session —
  working-notes candidates **WN-y** (apparatus evolution silently
  vacates derived statistics; two-era semantics required) and **WN-z**
  (the A3 promotion consumed its own evidence base — guideless
  correlation frozen at old-cycle n; re-test = deliberate ablation), plus
  **user-obs 2026-08-19 batch A–C** (pending-review section written in
  user-observations.md). Still held from before: WN-l/m + user-obs A–C
  (2026-08-03); WN-p/q/r + user-obs A–D (2026-08-15).
- **Carry-forward (unchanged):** sonnet intro API pricing ends
  2026-08-31; 128K output cap in project settings deliberate and
  standing; zbook still needs install-git-hooks.sh + venv; Shawn's list
  (Cosmos window, Fable billing split, Zotero proxy, ELSEVIER key,
  Marwick duplicates). Shawn away for a few days after 2026-08-19.

## Repo state (2026-08-17, second session)

- **EFFORT STUDY COMPLETE — OPUS PASSES AT HIGH; EFFORT DOES NOT RESCUE
  SONNET.** Six datapoints (sonnet high/xhigh/max 0.813/0.853/0.867 all
  below the ≥0.90 gate; opus high/xhigh both 0.953 PASS; fable xhigh
  0.947 context): model, not effort, is the operative axis. Opus is
  effort-insensitive on stability, cost, AND pack-utilisation (~80% vs
  sonnet's 47–57%); **opus@high and opus@xhigh are cost-indistinguishable**
  (the "cheapest passing configuration" headline was CORRECTED on
  Shawn's catch, `5c193e3` — the contract metric is ~92% effort-independent
  cache-writes; within-model effort comparisons must read output tokens,
  which fell 33% at high). Study spend ≈32.2M contract-metric tokens
  under explicit authorisations. Full record:
  `studies/open-science-compliance/outputs/validation/effort-study-2026-08-17/`
  (design note, study summary, per-arm run records + reconciliation).
- **EFFORT PINNING SHIPPED** (`3f4cde6`): launcher v1.3 (required
  `--effort`, `launch_commit` embedding, dirty-tree refusal, `--items`
  re-runs), workflow v1.6 (opts pin + Provenance prompt line + items
  filter + null-guard fix), assembler v1.5 (artefact-derived
  `provenance_pinned`, mixed-vintage error, `--allow-launch-commits`
  declared splits, `--expect-effort`). The harness persists NO effort
  field in spawn metadata (proven) — the transcript prompt is the only
  durable carrier. P3 differential probe verified the opts channel
  (7.5× output differential) before spend; P5 verified settings-env
  inheritance to spawns.
- **SONNET@MAX HALT AND COMPLETION** — the study's richest specimen:
  max-effort emissions blew the 64K per-response harness cap → 14 dead
  retry transcripts (24% of arm spend), 4 unusable items, wire tripped
  at 17.9M/12M; Shawn adjudicated completion (cap → 128,000 in
  `.claude/settings.json`, STANDING; zero dead attempts after — F-008
  confirmed causally); key r2 took three attempts (schema violation →
  repo-root Glob → clean). **Register F-008–F-011 lodged**; F-010's
  pattern-vs-path verifier question (unanchored Globs resolving to
  allowed paths) is deliberately OPEN for ruling.
- **Mechanical quality layer LIVE** (`scripts/check-payload-quality.py`,
  operator-accepted approach): pack_refs validity, A1-rule consistency,
  pack-utilisation. Study-wide: zero unresolvable pack_refs (2,700
  scores), zero A1 violations. Tests 222 → 251; gate 66/66 throughout.
- **NEXT (agreed order):** (1) **Shawn's E8-v2 worksheet sitting**
  (`outputs/validation/e8-v2-rederivation/worksheet.md`) → concordance
  across ALL arms in one pass (effort arms included; add the
  error-direction split) → gates ruling → census selection — candidate
  set now includes opus at either effort; (2) H13 fresh-context
  stability re-derivation at the gates stage (my figures are recounts
  replicating the registered derivation, flagged in every run record);
  (3) F-010 pattern-vs-path ruling (reconcile v1.5 candidate);
  (4) pre-census harvester rendering + challenge-page detection;
  (5) D4. **Opus@max stays OFF** (no deficiency in either opus record);
  optional small-sample evidence-groundedness audit (quality layer c)
  awaits explicit go.
- **Carry-forward gotchas:** the registered analysis tool
  (`analyse-benchmark-disagreements.py`) hardcodes the three-arm
  benchmark layout and cannot read effort-study arm dirs — needs an
  `--arms` extension (v-bump) before study arms join a tool-run at the
  summary/gates stage. Sonnet-5 intro API pricing ends 2026-08-31
  (cost projections in the design note used it). The 128K output cap in
  project settings is deliberate and standing.
- **PENDING VERDICTS (no silent discard):** WN-l/m + user-obs A–C
  (2026-08-03); WN-p/q/r + user-obs A–D (2026-08-15). **CLEARED at
  close (Shawn, 2026-08-17 s2):** WN-v/w/x ACCEPTED → working-notes
  Observations 27–29; user-obs s2 batch adjudicated — A and D accepted
  (D carries a standing ruling: **build-while-waiting on
  proposed-but-unratified no-spend read-only tooling is the right
  default**), B and C dropped as routine contract-following.

## Repo state (2026-08-17)

- **AMENDMENT 2 LODGED AND THE D3 RE-BENCHMARK RUN — TWO ARMS PASS
  STABILITY.** OSF SchemaResponse `6a824828f323f5c6ead66c4b` (approved,
  DOI unchanged, tag `osf-amendment-2-2026-08-17` at `9f7343e`;
  round-trip + public render verified; §6 comparator fix DISSOLVED —
  OSF escapes comparators on write and decodes on render, no defect
  ever visible). D3 then ran same day under a pre-run-review contract
  (15 hardenings) + clean-context Opus audit (19 findings, 5 pre-spend
  blockers, all fixed; the audit pass is now CODIFIED in the
  pre-run-review skill, personal-assistant `0b3a6bd`). **Stability:
  sonnet 128/150 = 0.853 (below), opus 143/150 = 0.953 PASS, fable
  142/150 = 0.947 PASS** (vs 0.807/0.873/0.813); disputed 68 → 56;
  A1.2 10 → 3; dye F-block flip gone. Concordance deliberately
  uncomputed pending E8 v2. Full package:
  `studies/open-science-compliance/outputs/validation/benchmark-2026-08-17/`.
- **FAILURE-MODE REGISTER LIVE** (Shawn's directive; he rates it "a
  goldmine for alignment-related assessment"):
  `outputs/validation/failure-modes/register.md` — append-only,
  categorised (model-fabrication/boundary/honest-failure,
  verifier-error, harness-constraint/change), every entry anchored.
  Seeded F-001–F-007; headline: **fable fabricated a pull declaration**
  (F-001, caught by three layers, item re-run clean) and globbed the
  session dir (F-002); telemetry shows validator retries 3/1/0
  (sonnet/opus/fable) against incidents 0/0/2 — form-compliance and
  attestation-integrity look like separate axes. Standing rule: every
  reconciliation failure/gate block gains an entry at adjudication.
- **Phase B shape + platform-table corrections RULED (2026-08-15)**;
  D1 window executed (instrument v2.1, guide v1.1 pushed, definitions
  v1.2, C7 hashes); identifier-recovery rule LIVE — first run recovered
  marwick's lost deposit (dead zenodo.14561925 → curated
  zenodo.15603267, flagged `recovered` in the pack) [correction 2026-10-03: no deposit
  was lost — 15603267 is v1.3 of the concept DOI the paper cites;
  14561925 came from the pilot extraction; erratum-log Entry 4]. CoreTrustSeal/
  re3data enrichment committed (ADS to 2027, DANS to 2028, tDAR lapsed,
  Zenodo never applied). E8-v2 adjudication worksheet GENERATED
  (`outputs/validation/e8-v2-rederivation/worksheet.md`, 150 items /
  68 disputed / 3 flips / seeded 10 spot-checks) — **Shawn's sitting is
  the critical path to concordance and the gates ruling.**
- **Wire rule AMENDED (Shawn): remediation-scaled** — the spend wire
  grows by the re-run percentage unless a stuck-loop indicator is
  present; fable accepted at 7.10M vs adjusted 7.93M
  (`arm-fable-5/tripwire-event.md`). $50 wind-down standing.
- **Effort is ATTESTATION-ONLY this cycle** (session-inherited xhigh;
  Claude's "high" claim was a confabulation Shawn caught via /effort —
  logged to the confab tracker). Run records carry run_environment
  attestations + v1.3 telemetry (retries, thinking blocks, wall-clock,
  served variants — opus ran `claude-opus-5[1m]`). **Pinning (effort in
  workflow opts + stated in prompts + launcher --effort +
  launch-commit embedding) is the next session's opening build.**
- **NEXT (agreed order):** (1) effort-pinning build + abbreviated
  delta pre-run review; (2) **effort study under the standing API
  gate**: sonnet@max + opus@max first (30+30 spawns, ~11–13M tokens,
  ≈$15–25 API-equivalent), conditional high arms after — sonnet
  prioritised (selection economics: cheapest arm currently fails at
  0.853); (3) Shawn's E8-v2 worksheet sitting → concordance across ALL
  arms in one pass → gates ruling → census selection; (4) D4.
- **PENDING VERDICTS (no silent discard):** WN-l/m + user-obs A–C
  (2026-08-03); WN-p/q/r + user-obs A–D (2026-08-15). **CLEARED
  2026-08-17 at close:** WN-s/t/u ACCEPTED → working-notes Observations
  23–25, plus Shawn-directed Observation 26 (errors-are-specimens /
  the failure-register decision); user-obs batch adjudicated — B and C
  accepted, A and D dropped with reasons recorded (`5b60221`).

## Repo state (2026-08-15)

- **PHASE C COMPLETE (2026-08-14–15) — all nine items; tests 84 → 172;
  D5 gate 57 → 65 entities; 25 commits `f3368ff`→`7ba9a45` + handoff.**
  Erratum-log **Entry 3 + amendment 2 scope RATIFIED** (2026-08-14,
  incorporating the 2026-08-11 ratification-read consolidations);
  **C7 RULED YES**; **consolidated D1 governed-edit window ADOPTED**
  (one batch, on a branch: definitions wording + v1.1 pointer + guide
  pull→push promotion + C7 sha256 hashes + §4 rewording + platform-table
  corrections + pack-staleness sentence).
- **Pre-run review + clean-context audit PoC (2026-08-14):**
  ten-hardening execution contract in the plan; the Opus audit confirmed
  4 blockers — headline: the receipt gate "blocked" 39/45 benchmark
  spawns with zero downstream consequence. C2 probes diagnosed it:
  transcript write-lag false alarms (the block message conflated two
  fault classes), and SubagentStop blocks are **advisory in the workflow
  lane** (probe C's engineered violation was logged-blocked yet
  collected; the block never reached the agent).
- **THE BENCHMARK IS RETROACTIVELY VINDICATED:** all 45 retained
  transcripts machine-validate — receipts 45/45 (versions, tokens,
  model pins, agent versions, pulls) AND **zero contaminating file
  accesses** (§4 isolation empirically held). Committed evidence:
  `studies/open-science-compliance/outputs/validation/benchmark-2026-08/reconciliation-2026-08-15/`.
  One warning case: the dye/sonnet spawn's guide reads failed at a
  nonexistent user-level path and it honestly declared no pulls,
  scoring guideless — **footnote for the §2-card "sonnet pulled 9/15"
  evidence: pull counts were attempt-based and may mislead in both
  directions.**
- **Built and pushed:** schema **v1.1** (ESCALATE no longer forces
  fabrication; bounds; soft A1 cross-reference honouring the ethical
  exception; `schema_version` const enforced by validator AND gate;
  ratified `input_provenance`; `pack_refs`); unwrap script M14–M16 +
  committed self-check; **artefact-metadata harvester + five committed
  evidence packs** (`corpus/evidence-packs/`; conflict flags live —
  marwick's three asserted licences vs Zenodo's single cc-by-4.0 fired,
  key's CC BY cleared after CC-URL canonicalisation; marwick's cited
  DOI 10.5281/zenodo.14561925 **404s at DataCite and Zenodo** — Phase B
  finding [correction 2026-10-03: never cited by the paper; a
  pilot-extraction error, erratum-log Entry 4]; CRAN an honest endpoint-flagged gap); **`reconcile-run.py`**
  (C8+C9 in one tool: post-hoc receipt re-validation incl. the new
  **attempts-are-not-reads** rule, per-spawn file-access lists with
  contamination flagging, divergence tripwire, log-slice archival,
  exit-1 hard stop). GitHub fine-grained public-read token in the PA
  `.env` (`GITHUB_API_TOKEN_LLMR`), read at run time only.
- **PLATFORM-ROW VERIFICATION NOTE AWAITS SHAWN'S D1 RULINGS**
  (`outputs/validation/platform-rows-2026-08-15/verification-note.md`,
  34 assertions, every row HOLDS WITH CAVEAT): DataCite's own
  retraction workflow withdraws metadata from the Public API
  (tombstone limb contradicted); Zenodo's licence floor is a
  **pre-filled form default** (82.6% of sampled records) and scoped to
  open records only; ADS ≫ DANS > tDAR on ingest enforcement; GitLab
  licence data is opt-in with no SPDX id; Crossref article persistence
  is a member obligation + Crossref right, not a warranty; component
  DOIs number 9.3M but are metadata-poor; tDAR/DANS bot-gate scripted
  fetches (rendering + challenge-page detection needed for future
  endpoints).
- **Incidents (both the S1 index-vs-worktree residual, now observed
  live twice):** a deliberately failing probe test leaked into
  `5618e30` (removed `d2cb58a`); `5fdc172`'s message claimed the
  live-gate rule its staging missed (completed `2d8b074`). Standing
  remedy adopted (claude-obs 39): post-commit stat + status check
  before claiming anything landed.
- **NEXT (in order):** (1) **Phase B shape discussion (Shawn)** —
  re-derivation design (human-adjudication anchor? n=12 subsample
  seed? E8 update retaining the old set); (2) **A3 + D1 consolidation**
  — the governed window above, incl. Shawn's rulings on the
  platform-table corrections; (3) **D2 lodge** (API route; C5-fixed
  unwrap for the paste artefact); (4) **D3 re-benchmark prep**: wire
  reconcile-run into `fair-benchmark-arm.workflow.js` as a per-item
  hard stop + schema push with sha256 receipts + the S4 validator
  probe; standing API gate (45 spawns) — **gate template addition:
  state the billing route (plan allowance vs API), per user-obs
  candidate D**; (5) D4 gates → selection → census.
- **PENDING VERDICTS (no silent discard):** WN-l, WN-m and user-obs
  A–C (2026-08-03 batch) still held; **NEW this session:** working-notes
  candidates **WN-p/q/r** (see 2026-08-15 session-log entry) and
  user-obs **2026-08-15 batch A–D** (pending in
  `wiki/user-observations.md`).

## Repo state (2026-08-10)

- **§2 ROUTING-FIX CARD DECLINED (Shawn, 2026-08-03/10) — INSTRUMENT
  CLARIFICATION ROUTE ADOPTED.** Receipts evidence killed the candidate's
  premise (sonnet pulled the guide 9/15; opus and fable 15/15 and failed
  both gates anyway; the guide is silent on the disputed cases). Route:
  erratum → OSF amendment 2 → re-benchmark. **Plan of record:
  `wiki/planning/instrument-clarification-plan.md`** (phases A–D, decision
  log, all rulings). Phase A COMPLETE except A3 (guide alignment, rides
  D1): A1 mining pass verified and reduced 68/150 disputed items to three
  root causes; A2 drafted as **erratum-log Entry 3 + "Queued amendment 2
  scope"** (ten items of operative text, PROPOSED — Shawn's ratification
  read pending).
- **ALL EIGHT DECISION POINTS RULED (Shawn, 2026-08-10):** research-surface
  rule (unit = artefacts required to reproduce, status scored, fault never;
  provenance as non-scoring per-input flag); two-rung evidence ladder with
  closed platform table; A1.2 open-case satisfied; R1.3 deposit-level
  standards only; R1.1 licence semantics (supplements default same-as-paper;
  repository licences checked at the service; conflicts → most restrictive);
  F-block gradient (F1 explicit-association; 4/4 vs 1/4 vs 0/4);
  unscoreable→0 only after the ladder. **Deterministic artefact-metadata
  harvester approved** (plan C6; extensible platform list — Dataverse/ADA/
  Figshare flagged); amendment 2 re-specifies §4 read-scope as paper +
  receipt-covered evidence pack. **Reference re-derivation (Phase B1) is
  now ENTAILED** — rulings flip identified reference scores (dye data
  R1.3, key A2, F-block items).
- **SCOUT/VERIFIER PIPELINE:** prior-art survey verified with material
  corrections — four fabricated quotations, ACM v1.1 claim INVERTED
  (origin-gated "Author-created artifacts…" → named deliberate departure);
  JIE badges survive as closest precedent. Cite only
  `wiki/planning/scout-reports/2026-08-10-fair-third-party-artefacts-prior-art-verified.md`.
  Countermeasure shipped: prior-art-scout must emit a claim per direct
  quotation (personal-assistant `a3f5793`). Eleven verified refs in Zotero
  staging `2026-08-10-fair-third-party-artefacts-prior-art`; Marwick 2017 +
  Tedersoo 2021 read directly (both support the ruling).
- **PENDING VERDICTS (no silent discard):** WN-l, WN-m (2026-08-03) and
  user-obs candidates A–C (2026-08-03) remain held. **Cleared 2026-08-10:**
  WN-n and WN-o ACCEPTED → working-notes **Observations 21** (audit surface
  must equal the reader's trust surface) **and 22** (test a one-shot
  resource's premise against primary artefacts before spending it);
  user-obs 2026-08-10 batch adjudicated — A dropped, B and C accepted
  ("both are good approaches going forward").
- **PRE-CENSUS REQUIREMENTS UNCHANGED:** audit fix round 2 + schema v1.1
  (now also carries the provenance flag) + receipt-gate operative demo
  (`wiki/planning/audit-2026-08-03-follow-ups.md`); C7 GOVERNED decision
  still open; monitoring Phase 4 unstarted.
- **2026-08-14 (mid-session addenda):** erratum-log Entry 3 + amendment 2
  scope RATIFIED; C7 RULED YES (hashes land in the D1 governed-edit
  window); Phase C pre-run review complete — hardened contract in
  `wiki/planning/instrument-clarification-plan.md`; amd-tower venv
  recreated, baseline 84/84 green. **Shawn will provide a GitHub API
  token for the C6 harvester when asked** (rate-limit headroom for the
  GitHub endpoint; unauthenticated is 60 req/h) — request it at C6
  build time. Clean-context pre-run audit (Opus PoC) adjudicated: all
  four blockers confirmed — headline: the receipt gate blocked 39/45
  benchmark spawns with no downstream consequence (B1, scale-corrected
  from the register's 9/15); new plan item **C8** implements amendment
  1 §4's asserted isolation controls (registrant: implement, erratum
  where infeasible). PoC verdict: the clean-context pass belongs in
  `/pre-run-review` — extension queued (personal-assistant repo).

## Repo state (2026-08-03)

- **AMENDMENT 1 LODGED — TASK E COMPLETE.** Filed via the OSF API as
  registration Version 2 (revision `6a7017da97adb06288afef80`, DOI
  unchanged, tag `osf-amendment-1-2026-08-03`); lodgement text is the
  promoted academic-prose re-expression + a §5 cross-vendor
  pre-declaration (OpenAI arms considered, deferred to the FAIR4RS
  extension pattern). Details in the task-E block and the draft's status
  header.
- **MONITORING PHASES 0–3 SHIPPED** (plan §8/§10): 57-entity enumeration,
  `entity_checks` registry + E8 reference-dataset registration, per-class
  checker with undeclared-entity failure, coverage self-report line.
  §9 all resolved. Phase 4 (E7 hashes) remains.
- **BENCHMARK COMPLETE — ALL THREE ARMS BELOW BOTH 0.90 GATES.**
  Stability 0.807 (sonnet) / 0.873 (opus) / 0.813 (fable); concordance
  0.773 / 0.807 / 0.820. Item-structured disagreement shared across arms
  (A1.2, R1.1, A2, R1.3, F-block upstream crediting) = instrument
  evidence. Full package:
  `studies/open-science-compliance/outputs/validation/benchmark-2026-08/`
  (benchmark-summary.md + per-arm run-records with per-spawn tokens).
  **NEXT SESSION'S FIRST DECISION (Shawn, amendment §2): the single
  permitted routing-fix attempt** — candidate: push
  `fair-principles-guide.md` uniformly (receipts show inconsistent
  pulling) — then one re-run; else the registered majority-vote census
  (arm choice to be recorded explicitly). The workflow harness is rescued
  at `studies/open-science-compliance/protocol/validation/fair-benchmark-arm.workflow.js`.
- **AUDIT ROUND 2 OPEN.** Two-lens audit + fix pass `3b01676` (tests
  48→84, committed hook suite) + re-audit that found regressions in the
  fixes. Register: `wiki/planning/audit-2026-08-03-follow-ups.md` —
  fix round 2 and schema v1.1 are PRE-CENSUS requirements; C7 (instrument
  sha256) is a GOVERNED decision for Shawn. **Correction owed:** the
  2026-07-24 records claim "17 synthetic pipe-tests" for the hooks — those
  were ephemeral and never committed (audit C4); `tests/test_hooks.py`
  now exists. This note is the dated correction's anchor.
- **PENDING VERDICTS (no silent discard):** working-notes candidates WN-l,
  WN-m; user-obs candidates A–C (2026-08-03 batch); user-obs A–C from
  2026-07-27 — A and B ACCEPTED 2026-08-02/03, C discarded (systematised
  as handoff step 0).

## Repo state (2026-07-27, second session)

- **FOUR HELD-OVER VERDICTS CLEARED (2026-07-27, amd-tower, second session).**
  The block flagged below under "HELD OVER" is resolved:
  1. **WN-h/WN-i ACCEPTED** → `wiki/working-notes.md` Observations 16
     (structural instrument checks have a prose-shaped blind spot) and 17
     (independent reimplementation is a review technique). Both existed only as
     one-line summaries in this file; drafted against their sources (erratum-log
     Entry 2, and the `03f10ad`→`ceb1d79` commit range) before the verdict.
  2. **User-obs candidates A–C: HELD AGAIN.** Reviewed, not accepted, not
     discarded — annotated as such in `wiki/user-observations.md` so they read
     as triaged rather than untouched. Re-present at the next handoff.
  3. **Opus-5 benchmark arm CONFIRMED, plus a third arm authorised.** Shawn
     approved the deferred Fable 5 variant, discharging the 2026-07-22
     "ask-before-Fable" condition. Benchmark arms are now **Sonnet 5 + Opus 5 +
     Fable 5**.
  4. **Amendment §3 provenance paragraph: read at lodgement**, per the
     2026-07-24 one-read decision. Text unchanged
     (`amendment-1-draft.md:113–125`); the pre-lodgement checklist governs.
- **FABLE 5 ARM BUILT.** `.claude/agents/fair-assessor-fable-5.md` generated
  *from* the Opus 5 file rather than hand-transcribed, then diffed: the three
  variants differ only in name, description, model pin, role heading, sibling
  sentence, and `agent_version` — the "only the model pin differs" claim is now
  verified, not asserted. (Hand-transcription had silently introduced a
  `sub-principle`→`sub principle` defect; the diff caught it.) Registered in
  `manifest.yaml` with sha256; the sibling-sentence edit changed the Sonnet 5
  and Opus 5 hashes too, all three updated in the same commit. **32 tests green,
  live gate PASS (0 errors, 0 warnings)** — and because the D5 gate enforces the
  agent registry in both directions, that PASS is positive evidence the new file
  is registered and correctly hashed.
- **Fable 5 caveats recorded in the manifest comment, neither blocking
  authorship:** $10/$50 per MTok (2× Opus 5, 3.3× Sonnet 5 standard), and it
  requires 30-day data retention — unavailable under zero data retention, which
  surfaces as a 400 on *every* call rather than as a capability difference.
  **The benchmark run itself is still ungated:** authoring a definition is not
  an API call, so the run needs explicit approval with a billing route decided.
  Three arms × 5 pilot papers × 3 runs = 45 scoring spawns.
- **CORPUS ITEMS 5 AND 6 DONE — the corpus plan's build list is now closed.**
  Both were already *specified* in `corpus/README.md`; only the implementations
  were missing.
  - **Item 5 (`bd5bc40`, on main):** reproduction preparation prompt v1.0→v1.1.
    New §1.0 (hash at fetch time — reconstructing at session end makes the
    retrieval dates guesses) and §1.0.1 (three destinations: corpus store for
    publisher content and never git; attempt directory for author-released
    materials; scratch for what nothing references). `log-template.md` gains a
    **Materials Acquired** table. Verification and handoff gained matching
    checks.
  - **Item 6 (PR #2, branch `feat/schema-v2.7-source-provenance`):** schema
    v2.7 adding optional `source_file` + `source_sha256`. Branched not pushed,
    per the standing schema-change rule. Additivity verified mechanically (no
    v2.6 property or top-level key dropped; `required` unchanged), not asserted.
    **v2.6 retained and the pilots deliberately not back-filled** — the field
    records what a run actually read, so retro-fitting a digest would make it
    lie in its first use. Out of scope and flagged in the PR:
    `docs/user-guide/schema-reference.md` and `docs/README.md` still say v2.6
    (prose rewrite; belongs with task D).
- **FINDING — the D5 gate's version check covers 7 of 25 registered entries.**
  Found by probing this session's own change: setting the reproduction
  preparation prompt's manifest version to a deliberately wrong `9.9` still
  produced `PASS`. Cause is scope, not a bug — `check_canonical_entry`
  (`scripts/check-manifest-consistency.py:180`) runs **only** over
  `shared_content`, so `components.*`, `assessment.prompts.*`,
  `reproduction.prompts.*` and the rest are unchecked. Same shape as
  Observation 16: a gate reporting PASS over a narrower scope than a reader
  assumes — and this file described D5 as "verifies version lines" without the
  qualifier. A sweep of all 25 registered `file`+`version` entries found:
  8 matching, 6 cosmetic `v1.0`-vs-`1.0` prefix differences, 8 with no
  `**Version:**` line (the six agent definitions use frontmatter and are
  hash-checked instead — stronger, not weaker), and 1 apparent mismatch that
  **turned out not to be one** (see below).
  **Shawn's decision 2026-08-02: WIDEN — every registered entity is to be
  checked hard.** A reorganisation to support that is acceptable. Plan drafted
  at `wiki/planning/artefact-integrity-monitoring-plan.md`; not implemented.

- **CORRECTED 2026-08-02 — the `assessment_json` "mismatch" was mine, not the
  repo's.** On 2026-07-27 this was logged as a genuine conflict needing a
  verdict on which number was right. It is not: `1.1` and `2.1` measure
  different things, and both are correct. `**Version:** 2.1` is the *document*
  version of `assessment-schema.md` (2.0→2.1 at `05e9706`, 2025-11-29; never
  1.x). `schema_version: "1.1"` is the *payload* version stamped into each
  `assessment.json` (1.0→1.1 at `faef450`, 2026-02-12). The manifest entry
  tracks the payload axis while its `file:` points at the guide documenting it.
  The naive sweep compared the two axes and reported a conflict that does not
  exist; a note in `manifest.yaml` now says so, so the next reader does not
  "reconcile" them into one number.
- **STALE COMMIT HASHES — a history rewrite orphaned pre-rewrite references.**
  The real defect behind the above. `c3654f6` does not resolve; nor do the two
  hashes logged beside it. All three were re-identified by exact
  commit-message match (`e1e4cba`→`aa75817`, `c3654f6`→`faef450`,
  `c026756`→`be7271a`, all 2026-02-12, contents unchanged). Fixed in
  `manifest.yaml` and `wiki/reflections/session-log.md` (with an inline note
  recording the remap rather than silently swapping).
  **Scale, measured 2026-08-02:** of backticked commit-shaped references across
  `wiki/`, `manifest.yaml`, `studies/`, and `corpus/`, **115 resolve and 21 do
  not**; all 21 sit in `wiki/` (continuity, session-log, reflections,
  working-notes). Three are now fixed; **18 remain** and each needs
  message-match re-identification. Deliberately not batch-fixed here — the
  remap must be verified per commit, not guessed. A resolve-check is a
  candidate control in the monitoring plan.

## Repo state (2026-07-27)

- **D5 GATE HARDENED (2026-07-27, amd-tower; `03f10ad`→`ceb1d79`).** A third
  session, resuming from the 2026-07-24 handoff, independently reimplemented D5
  before discovering the zbook build had already landed (7 commits pulled
  mid-session). Rather than discard either, the two were compared; the second
  implementation caught two gaps in the first, both now ported in and tested:
  - **Byte-exact mirror regions.** The structural check (fenced blocks + table
    rows) cannot see prose. **The Pass 6 prompt's "verbatim mirror" banner was
    untrue** — four normative statements from prereg §7.1 were missing
    (unscoreable→0; never aggregated; the A1 majority rule; FAIR4RS out of
    scope) while every block and row matched, so the gate reported PASS.
    Marker pairs now delimit the region and it is compared byte for byte.
    **Erratum-log Entry 2**; impact checked against persisted pilot outputs —
    no pilot score revised (all /15, none unscored, none aggregated,
    key-et-al-2024 shows the A1 rule operating).
  - **Reverse sweep.** An unregistered `.md` dropped into the instruments
    directory passed the old gate. Every file in
    `shared_content_policy.scan_directories` must now be registered.
  - Mirrors that cannot be one contiguous region declare
    `mirror_mode: structural` and warn every run that prose divergence is
    undetected — the weaker guarantee is announced, not assumed.
  - Tests 17→28. Amendment 1 draft updated (§1 gains Entry 2; §3 gains the
    model-identifier provenance limit — pinned IDs are the provider's exact
    complete strings with no dated snapshot available, so an ID names a model
    as served at call time, not a frozen weight set).
- **SECOND MIRROR CONVERGED (2026-07-27, Shawn's call).**
  `verdicts-and-precision` → reproduction-assessor `SKILL.md` is now byte-exact
  in six **named segments** (`#verdicts`, `#precision`, `#tolerances`,
  `#discrepancy`, `#scope`, `#environment`) — the check gained segment support
  so a mirror can land in several places in a document without giving up
  byte-exactness. Convergence replaced reworded restatements with canon's
  wording and added two things the skill never carried: the PAPER_ERROR
  human-escalation sentence and environment-spec levels 0–5 (new SKILL.md
  section H). **No erratum, no amendment** — SKILL.md is not in the frozen
  artefact set, the discrepancy vocabulary is not registered text, and
  converging a mirror changes delivery not instrument semantics; ordinary §8
  implementation change riding the Phase 1 regression gate. Reasoning recorded
  in erratum-log Entry 2 under "related finding". `mirror_mode: structural`
  survives as the declared-weaker fallback; nothing uses it.
- **FORWARD MODEL PINS → OPUS 5 (2026-07-27, Shawn's call).** Every pin that
  was `claude-opus-4-8` is now `claude-opus-5`: `fair-assessor-opus-4-8.md`
  renamed to `fair-assessor-opus-5.md`, plus reproduction-planner,
  reproduction-executor, adversarial-reviewer. Same price ($5/$25 per MTok),
  higher capability, no reason to prefer 4.8 for new work. **History is not
  rewritten** — no scored artefact ever ran on 4.8 (existing extractions record
  `claude-opus-4-5`/`claude-sonnet-4-5` and keep those), and the dated decision
  records in the session log and reflections stand as written; the manifest
  comment records 2026-07-22 → 2026-07-24 → superseded-2026-07-27 as a chain.
  The validation benchmark's Opus arm is now Opus 5. Selection still happens at
  the validation phase under the amendment's gates-plus-cost rule.
- **Session close (2026-07-27):** `/reflect` written — session-reflection Entry
  10, llm-observations (independent reimplementation as a review technique),
  abductive entry (the sync check that could not fail, reflog-anchored),
  session log, claude-obs 25–28. Secret-safety fix outside this repo:
  `~/personal-assistant/.env.bak-2026-07-27` held live API keys and was not
  gitignored (`.env` was covered, `.env.*` was not) — broadened, committed,
  pushed.
- **HELD OVER — needs Shawn's verdict (no silent discard):** [x] 2026-07-27
  ALL FOUR CLEARED — see the second-session block above. Two working-notes
  candidates drafted at this handoff, **WN-h** (structural instrument checks
  have a systematic blind spot: fenced blocks and table rows pass while
  normative prose diverges — measured on the live Pass 6 mirror) and **WN-i**
  (independent reimplementation as a review technique: two readings of one
  specification map where the spec was silent; the delta was two real gaps).
  Plus **user-obs candidates A–C for 2026-07-27** in `wiki/user-observations.md`
  (pending review). Also still open from earlier: the Opus-5 benchmark-arm
  change and the amendment's provenance paragraph, both flagged in-session but
  not explicitly signed off.
- **Process fix for concurrent sessions — IMPLEMENTED.** The collision cost a
  full duplicate build. Root cause: `git status` and
  `git rev-list origin/main...HEAD` read the *local* `origin/main` ref and never
  contact the remote, so without a `git fetch` they report "in sync" from a
  stale pointer — indistinguishable from real sync. The harness's session-start
  snapshot does not fetch either. Reflog confirms this repo's `origin/main`
  pointer had not moved since 2026-07-24 14:16 until a fetch at 2026-07-27
  11:25, while the zbook commits landed 14:29–20:01 on 24 July. Fix: fetch-first
  is now the opening instruction in this repo's `CLAUDE.md`, and the `/handoff`
  resume-prompt template opens with `git fetch && git status -sb`
  (`~/personal-assistant/global-claude-md/handoff-protocol.md` step 6).

## Repo state (2026-07-24)

- **PHASE 1 BUILD QUEUE EXECUTED (2026-07-24, second session; commits
  `b1aab17`→`115d202`):** the four-item queue from the bullet below is DONE.
  (1) **D5 gate live:** `scripts/check-manifest-consistency.py` wired into
  pre-commit (block-tested) — verifies version lines, end-of-file receipt
  tokens, mirror normative blocks (fenced code + table rows byte-identical),
  push/pull consumer routing evidence, agent-definition hashes (§3.4),
  model pins (§3.3, no `inherit`), and the `memory:` prohibition (§3.9);
  17 unit tests in `tests/test_manifest_consistency.py`. (2) **Instrument
  canon complete — 7 `shared_content` entries:** FAIR instrument + five new
  canonical files (data-availability-taxonomy, verdicts-and-precision incl.
  env levels 0–5, coverage-rules, eligibility-criteria,
  `.claude/shared/invariants.md`) + adversarial-review-framework promoted
  pull→push and registered (v1.1, governed header + token); reproduction
  SKILL.md registered as a second machine-checked mirror (verdict/tolerance/
  scope tables). (3) **Five agent definitions** with pinned models:
  fair-assessor ×2 per-model variants (`claude-sonnet-5`, `claude-opus-4-8`
  — NB Sonnet 5/Opus 4.8 expose NO dated snapshot IDs; the aliases ARE the
  exact IDs, never append dates); reproduction-planner/executor/
  adversarial-reviewer provisionally `claude-opus-4-8` pending the
  validation-phase benchmark (pin changes are governed manifest edits).
  `agent_definitions` hash registry added to the manifest. (4) **Production
  hooks live** (probe archived to `archive/phase1-spike/`): manifest-driven
  SubagentStart push + sha256/version receipt log; SubagentStop receipt gate
  (version echo, token quote, model_id hard gate, transcript-verified full
  pulled reads, D-12 retry-then-fail-closed, ESCALATE passthrough,
  decision:block self-healing); PreToolUse[Agent|Task] pre-flight denying
  governed spawns on D5 failure / missing instruments /
  `CLAUDE_CODE_SUBAGENT_MODEL`; 17 synthetic pipe-tests green. **Consolidated
  OSF amendment DRAFTED** from the ratified scope:
  `studies/open-science-compliance/prereg/amendment-1-draft.md` (lodge just
  before the validation phase; pre-lodgement checklist inside; erratum log
  cross-references it). **NEXT (Phase 1 remainder):** census screener
  (deterministic script + instrument-like triage prompt, design §5); output
  schemas for the structured-output layer + census/validation workflow
  scripts (§9); corpus items 5–6; then amendment lodgement → validation
  phase.
- **PHASE 1 OPENED (2026-07-24):** D-2 hook spike **PASSED** on all four
  datapoints (two haiku probes: hooks fire for workflow spawns; injected
  context arrives; transcript path delivered; named `agentType` reaches
  matchers) — **engine = workflows CONFIRMED**; build rule: workflow
  `agent()` calls always pass `agentType`; headless `--agent` fan-out stays
  as documented fallback. FAIR instrument v2.0 extracted to its canonical
  file (`studies/open-science-compliance/protocol/instruments/fair-instrument.md`,
  receipt token `3ddcbfd82575a2f8`; Pass 6 prompt keeps a banner-marked
  verbatim mirror); `manifest.yaml` `shared_content` registry started
  (`25d1c0d`). Probe hook neutered to log-only scaffolding. **Elsevier TDM
  trail:** three diagnostic 403s (entitlement → key-provisioning →
  TDM-checkbox-insufficient; full chain in corpus plan decision 5); support
  email drafted but deprioritised on Brian's field intelligence — **Zotero +
  institutional proxy is the probable acquisition route** (Shawn
  investigating); key still to add on amd-tower. **BUILD QUEUE NEXT:** D5
  manifest-consistency script (pre-commit + pre-flight) → remaining
  instrument files (taxonomy L1–L6, verdicts+precision, coverage rules,
  eligibility, `.claude/shared/invariants.md`) → five agent definitions with
  pinned full model IDs → production push/receipt hooks +
  `PreToolUse[Agent]` pre-flight → corpus items 5–6.
- **ROUTING DESIGN SIGNED OFF (Shawn, 2026-07-24, at v0.2.2)** — Phase 1
  design gate CLEARED. Amendment scope RATIFIED same day; lodgement timing:
  defer to the hard stop (just before the validation phase), accumulating any
  further errata into one amendment.
- **CORPUS MANAGEMENT EXECUTED (2026-07-24) — census blockers DONE:** store
  live at `~/corpora/llm-reproducibility/` (16 papers, 28 files, 71.7 MB, all
  sha256-verified; originals retained, copy-then-verify); manifests written
  (`corpus/development-manifest.yaml` 11 papers;
  `studies/open-science-compliance/corpus/manifest.yaml` 5 pilots);
  `scripts/fetch-corpus.py` operational (verify 28/28 OK; gen-meta done);
  LFS narrowed to own-artefact scopes; pre-commit corpus gate installed +
  block-tested (override: `CORPUS_GATE_OVERRIDE=1`); first QNAP sync complete
  via `scripts/sync-corpus.sh` (44 files both sides; NO automated schedule —
  run after each acquisition session). Remaining corpus items 5–6 ride
  Phase 1. **Elsevier TDM:** Shawn requested an API key 2026-07-24; storage
  convention `ELSEVIER_API_KEY_TDM` in `~/personal-assistant/.env`;
  entitlement test (closed JAS article from campus) pending — see corpus plan
  decision 5 for the nuances. ~~NEXT: Phase 1 build, opening with the D-2
  hook spike~~ [x] 2026-07-24 spike RUN and PASSED — see the Phase 1 bullet
  at the top of this list.
- **Pre-build juncture /review-implementation COMPLETE (2026-07-24, Shawn's
  request):** fresh-context review of design v0.2.1 + corpus scope v0.2 +
  validation-phase plan. Verdict: proceed, four cheap fixes first. 12 defects
  (1 critical compliance: the §2.2 remediation ladder was a deviation from
  prereg §8's registered majority-vote consequence — must be pre-specified by
  amendment BEFORE the validation phase) + 8 enhancements. Fidelity audit of
  v0.2 vs the 2026-07-22 findings: clean. Report externalised to
  `wiki/planning/reviews/2026-07-24-pre-build-juncture-review.md`. ALL cheap
  fixes APPLIED same day: design → v0.2.2 (§2.2 compliant ladder; §9
  conditional-on-spike with headless `--agent` fallback named; pre-flight →
  `PreToolUse[Agent]`; model-alias layer hard-gated; D-12 transcript-lag
  retry; cost gate re-specified for Max-plan window consumption); corpus plan
  → v0.2.1 (item 7 backup PROMOTED to census-blocking; copy-then-verify;
  `meta.json` machine-generated; fetch politeness; Elsevier TDM enquiry =
  ACTION Shawn); erratum-log gains a **Queued amendment scope** section
  (ladder, unanimity statistic, all-five-pilots, gates-plus-cost model
  selection with E-4 concordance floor, read-scope isolation, robustness
  annex) — PROPOSED, pending Shawn's ratification; consolidated amendment must
  lodge before the validation phase. D-2 hook spike = Phase 1 opening hour.
- **Routing design v0.2 WRITTEN (2026-07-23, `3914f81`) — superseded by
  v0.2.2 above; still awaiting Shawn's
  review/sign-off** (he is reading it; the four judgement calls to check: hook
  injection as primary push; §2.2 remediation ladder; instrument extraction
  deferred to build; memory prohibition + hot-reload governance). Phase 1 build
  blocked on this sign-off.
- **Corpus-management implementation SCOPED (2026-07-23):** repo audit, build
  order (8 items, ≈1 day, items 1–4 census-blocking), target structure, and
  decision log now in `wiki/planning/corpus-management-plan.md` v0.2. Decision
  status: path mechanism AGREED; out-of-tree store and study-scoped manifests
  recommended (registration-integrity argument: purges rewrite history and
  would invalidate the hashes the OSF registration pins) — awaiting Shawn's
  confirmation; execution ON HOLD until the routing-design review lands.
- **Routing-design review passes COMPLETE + externalised (2026-07-22):**
  implementation review at
  `wiki/planning/reviews/2026-07-22-routing-design-implementation-review.md`
  (10 defects D1–D10, 8 enhancements E1–E8; headline: build push/receipt/
  pre-flight on native harness primitives — SubagentStart/SubagentStop hooks,
  `skills:` preload, `--json-schema` — not hand-rolled plumbing; pin model IDs);
  prior-art scout, adversarially verified 110/110 claims clean, at
  `wiki/planning/scout-reports/2026-07-22-routing-design-prior-art-verified.md`
  (headline: subagent cold-cache caveat + open issue anthropics/claude-code#29966
  — census cost gate must NOT assume prompt-cache discount without an empirical
  `cache_read_input_tokens` check). Design v0.2 fold-in is the next design task.
- **Pass 6 instrument defects FIXED (2026-07-22, `abdc526`):** stale /16
  example, legacy 5-level access taxonomy (renamed Tier 0–4 + demarcation
  note vs prereg L1–L6), dead schema pointer — all three were in the
  OSF-frozen copy at `ee3fda3`. **Erratum log started** (Shawn approved
  erratum-then-amendment path):
  `studies/open-science-compliance/prereg/erratum-log.md` — amendment must
  lodge before census scoring; instrument-file extraction (review D1) queued
  for Phase 1 build.
- **Sequence BLESSED (Shawn, 2026-07-22):** Pass 6 fix → routing design v0.2
  + sign-off → corpus-management implementation → Phase 1 agentic build →
  ONE combined validation phase (regression gate ≥2 pilots incl. Crema
  posterior-table leg + FAIR reliability spot-check 3 papers × 3 runs) →
  census. The previously planned standalone "weekend run" is superseded —
  both checks now ride the post-build validation phase, run once on the
  pipeline + model(s) that will score the census.
- **Model-testing decisions (Shawn, 2026-07-22):** step-5 spot-check
  benchmarks ALL THREE Claude models. Sonnet 5 + Opus 4.8 first, on the
  Claude Max subscription; **ASK before running Fable 5** (may go via API
  instead — Max coverage unclear). Shawn also wants an OpenAI **Sol** arm
  (GPT-5.6 Sol, released ~Jul 2026:
  <https://openai.com/index/previewing-gpt-5-6-sol/>; "capable but not
  Fable-level") — possibly a Fable-driving-Sol combination; design discussion
  deferred; cross-provider arm needs its own harness and an OSF amendment if
  adopted for the census (registration documents Claude as the instrument).
  API-call approval gate applies to every run as usual.
- `main` current through 2026-07-15 @ `885e664` (history rewritten 2026-07-13 —
  pre-purge hashes are stale). Earlier landmarks: plan v0.3 review,
  Cosmos form capture + proposal draft v0.2, article-text untracking, and the
  scout-report series). Project v3.0.1.
- **Scout sweep COMPLETE (2026-07-08), all follow-ups executed:** whole-stack
  positioning (12 verified reports + synthesis), arXiv blind-spot sweeps (S1/S2),
  approved deeper chaining (C1–C3), and the OSF/grey-literature guard pass (G1)
  all live in `wiki/planning/scout-reports/` (start at the synthesis; README
  indexes everything). Headlines: no direct competitor to any lane, but the
  middle is converging (Chakravorti 2026; Zhu 2026 pair) — speed-to-publish now
  matters; the zero-archaeology null is DOCUMENTED (G1, 26-query log) so
  first-mover claims must be scoped + "to our knowledge" with Spennemann 2023
  demarcated; Zotero staging holds all verified finds (P1–P6, S1–S2, chains).
  lit-scout + verifier agents patched (author-count rule; arXiv handling).
- **Cosmos application: SUBMITTED 2026-07-21** 🎉 (deadline 26 Jul; rolling
  review, decision ~1 month — watch for Cosmos correspondence mid-August).
  Submitted content = `cosmos-application-form-paste.txt` at `de30d7c`: title
  "Making Verification of Published Research Routine"; merged one-liner;
  498-word we-voice body; parity-length Brian entry; US$8,000; evidence pack
  live at `docs/cosmos-evidence-pack.md`; both CVs attached (Ross letterhead
  phone corrected + re-uploaded); field 20 = Lukianoff Substack. Draft
  history below. Proposal draft v0.4 (2026-07-21, academic-prose pass)
  in `wiki/planning/cosmos-application-draft.md` — body 499/500 aligned with the
  lodged registration (already-preregistered + osf.io/dqnhg, control series,
  pilot error-detection, window 2022–2026); field 19 extended (human-validation
  link, agent-relay audit line, delivery-and-follow-on paragraph: Claude/Codex
  skills + self-hostable runner with Brian Ballsun-Stanton, FAIR4RS, CC0 data
  outputs, follow-on API-cost driver); field 18 Brian entry (v0.5: CV-verified
  — Lecturer, Faculty of Arts, MQ; research-integrity award; both CVs read
  from ~/Downloads/, kept out of repo); applicant affiliation resolved
  (Honorary Professor MQ primary + EFN director secondary); team-pedigree
  line (preregistration chapter + JCAA FAIRer-data paper); candidates
  drafted for title/one-liner/self-pitch/amount (worked US$8,000) with
  CV-verified credential fragments. **v0.6 (2026-07-21): clean-context
  adversarial verification run + reconciled with the PA-hub session's ledger**
  — all submission-facing claims confirmed (499/500 recounted; 2,118 scout
  ledger records so "over 1,800" conservative); three ledger pointer errors
  fixed (Obs 4 not 6; pilot §1/§7; Florida chapter in Brian's CV only);
  field 19 wording corrected (registrant hand-scoring, ReplicatorBench/I4R
  scoping, DataCite + Spennemann demarcation, web-search-layer, CC0
  demarcated from registration); self-pitch recomposed to Shawn's
  done-things steer; **final paste set drafted for every form field (1–21)**.
  Body revised by Shawn 2026-07-21 (long-tail reframing, combined-approaches
  problem, JAS: Reports named, survey clause) and jointly tightened to v0.7 at
  499/500 — voice now "we" (Brian named collaborator; supersedes the
  first-person-singular verdict; field 6 self-pitch stays "I"), truth-seeking
  token restored, computational-subset wording protected. Remaining: field
  selections, profile links, field 20, phone check, submit. ~~Pre-submission
  gates~~ [x] 2026-07-21 BOTH CLEARED: embargo lifted by Shawn (journal
  check had cleared JAS / JAS:R / JCAA — none requires double-blind);
  registration verified public via anonymous API, DOI 10.17605/OSF.IO/DQNHG
  (recorded in draft, paste blocks, prereg README). Deadline 26 Jul 2026.
  (v0.3 was `7435865`, body 482/500.)
- **OSF preregistration DRAFTED + STRESS-TESTED (2026-07-14/15):**
  `studies/open-science-compliance/protocol/phase-2-preregistration-draft.md`
  v0.2 (`885e664`; v0.1 `9405182`). Open-ended registration format; honours all
  three drafting-care constraints (instrument fixed, regression-gated pipeline
  changes, no-new-corpus-contact). /review-implementation revisions: H2
  de-circularised (verification-target coverage endpoint, exact
  Jonckheere–Terpstra primary, fractional-logit secondary), H1 restricted to
  quantitative papers (post-treatment conditioning argument) with
  trend-adjusted secondary, **JAS: Reports DiD control arm (Shawn approved
  2026-07-14** — FAIR lane; reproduction = exploratory stretch; AER absence
  grounded in Marwick 2025, re-verify guidelines pre-launch), H4 reworded to
  match its test, assessment-before-reproduction blinding, 0.90 stability
  threshold, human-validation subsample (n=12), power table. **v0.7
  LODGEMENT-READY at `ee3fda3` (2026-07-18)** — all resolutions applied plus
  four review-batch revisions (see the 2026-07-18 session log entry);
  lodgement materials in `studies/open-science-compliance/prereg/` (plain
  summary, two glyph-verified PDFs, README with recipe + checklist).
  **LODGED 2026-07-20: <https://osf.io/dqnhg/>** — by hand from the project
  flow (standalone Registries flow caps form attachments at five files; the
  project flow froze all six artefacts from OSF Storage); embargoed at
  lodgement (Shawn 2026-07-21: deliberate deviation from the no-embargo
  plan — double-blind peer-review contingency; the lodgement tag's
  annotation still says "no embargo", predating the correction).
  **Embargo LIFTED 2026-07-21** (journal check cleared JAS / JAS:R / JCAA:
  none requires double-blind; JAS:R dropped its double-blind mandate
  between mid-2024 and 2026-07-21). **Registration PUBLIC, verified by
  anonymous API 2026-07-21; DOI 10.17605/OSF.IO/DQNHG.**
  Tag `osf-prereg-phase2-2026-07-20`;
  paste files unwrapped to flowing lines (OSF text boxes render line-breaks
  literally). Known cosmetic defect: §10 power table pasted as run-together
  pipe text — accepted, fix rides with any future amendment (tables rule
  now in prereg README + convention memory). Option A ordering satisfied:
  new-corpus FAIR scoring is unblocked. Live URL linked from the Cosmos draft (body now reads "already
  preregistered", census window corrected 2023→2022, 484/500 words).
- **Current gates:** the §9 verdicts are DELIVERED (2026-07-15/16), so the
  Phase 1 hold on the agentic modernisation plan
  (`wiki/planning/agentic-modernisation-plan.md`, v0.3) is now gated only on
  (a) review of the content-routing design (below) and (b) the
  corpus-management-plan implementation (pre-Phase-1 prerequisite). ~~OSF
  preregistration must precede FAIR scoring of any new JAS papers (Option A
  ordering constraint, plan §6).~~ [x] 2026-07-20 SATISFIED — registration
  lodged (<https://osf.io/dqnhg/>).
- **Agent content-routing design v0.1 WRITTEN (2026-07-15, `10947aa`):**
  `wiki/planning/agent-content-routing-design.md` — resolves plan §9 item 3
  with a three-way routing rule (embed role behaviour / push instruments
  verbatim with read receipts / pull pattern libraries; silent-vs-loud
  failure as the routing criterion). Read receipts decided by Shawn
  (reliability-first, duplication acceptable if cleanly split;
  no-agent-to-agent-duplication rule; shared_content registry folds into
  manifest.yaml). Queued: `/review-implementation` + prior-art-scout passes
  against it (Shawn wants both) → v0.2 before Phase 1 build.
- **Framework paper QUEUED (2026-07-13):** plan externalised to
  `wiki/planning/long-tail-credibility-framework-paper.md` (v0.1) — a
  state-of-play/agenda paper staking out long-tail research credibility
  assessment with AI, built on the verified scout sweeps. Prioritisation
  deferred until Shawn finishes his current paper (week of 2026-07-13); open
  question is authorship model (solo lit-review-and-state-of-play — his
  current lean — vs consortium via COS/CWTS Leiden/RDA contacts).
- **Deferred watch list (from chain reports C1/C3):** re-check forward citers
  of Chakravorti et al. 2026 (10.48550/arXiv.2605.27394) and the
  ReplicatorBench cluster around Sep–Oct 2026; Cheng & Khoo 2025
  (10.31083/ko44513) and Bolanos-Burgos et al. 2026 (10.7717/peerj-cs.3921)
  around Oct 2026–Jan 2027. Sources: c1/c3 reports' deeper-chaining sections.
- **Working notes WRITTEN (2026-07-13):** Obs 5 (prompt-injection sightings)
  and Obs 6 (verifier catch taxonomy) in `wiki/working-notes.md` (`f51737b`).
  The gap Obs 5 flagged — no standing anti-injection rule in the scout agent
  definitions — was closed the same day (personal-assistant `b31342b`,
  injection-defence rule added to all four scout agents' Constraints).
- ~~**§9 verdicts: Shawn has committed (2026-07-13)** to delivering the six
  judgement-call verdicts~~ [x] 2026-07-15/16 ALL DELIVERED: items 1–2 =
  prereg Decision 7 (reliability checks + 0.90 threshold, confirmed); item 3
  = content-routing design (sign-off pending the review passes); items 4–5
  accepted (R-A+R-B merge; drift clause as encoded in prereg §8); item 6
  realised by the prereg draft itself.
- **HISTORY PURGE COMPLETE (2026-07-13, pushed by Shawn; remote verified
  clean):** git filter-repo removed the dye-et-al-2023 supplement.pdf (both
  historical paths) and marwick-2025.txt from all 242 commits; local
  untracked copies intact; full pre-purge backup (mirror, LFS objects, plain
  files, commit-map) at
  `~/Code/repo-backups/llm-reproducibility-pre-purge-20260713/`.
  Residual notes: (1) commit hashes cited in wiki/docs before 2026-07-13 are
  stale — translate via the backed-up commit-map or search by commit
  subject; (2) GitHub's server-side LFS storage may retain the unreferenced
  supplement object — full scrub needs a GitHub Support ticket or repo
  delete/recreate (low urgency: nothing references it); (3) other local
  clones must be re-cloned or hard-reset. The CC BY SocArXiv preprint of
  Marwick 2025 is at
  `studies/open-science-compliance/corpus/pdfs/marwick-2025-socarxiv-preprint.pdf`
  (gitignored dir) for future licence-clean extraction.
- **Corpus management redesign AGREED (2026-07-13), implementation queued:**
  `wiki/planning/corpus-management-plan.md` — out-of-tree corpus store, DOI
  manifest + fetch-with-checksum script (Shawn endorsed fetch-with-checksum
  as the reproduction-run default), LFS/pre-commit guardrails, rpi-server
  sync. Sequenced as a PRE-PHASE-1 prerequisite in the agentic modernisation
  plan; must land before the JAS census acquires papers at scale.
- **OA check RESOLVED (2026-07-13):** six of eight
  papers are CC BY 4.0 — no purge needed (ballsun-stanton-et-al-2018,
  penske-et-al-2023, sobotkova-et-al-2016 [OA book], sobotkova-et-al-2024
  [Emerald page confirms CC BY despite Unpaywall "bronze"], crema-et-al-2024,
  key-et-al-2024). ~~PENDING~~ [x] 2026-07-13 both actions COMPLETED (see
  HISTORY PURGE COMPLETE above); original scoping notes retained: (1) `git filter-repo` purge of
  dye-et-al-2023's `reproduction/attempt-01/supplement.pdf` — publisher
  (Elsevier) supplement to a green-only article, no open licence; NOTE it
  was tracked via Git LFS, so the purge must remove the LFS object as well
  as the pointer; history rewrite of the public repo awaits Shawn's go.
  (2) `marwick-2025.txt` near-certainly from the closed VoR: the on-disk
  source PDF (studies/open-science-compliance/corpus/pdfs/marwick-2025.pdf)
  IS the Elsevier JAS version of record (first-page check 2026-07-13) and no
  preprint PDF is present — joins the purge list pending Shawn's one-word
  confirmation. LOCAL COPIES CONFIRMED before any purge (Shawn's
  requirement, 2026-07-13): dye supplement intact on disk (820,582 bytes,
  real PDF, not an LFS pointer) and marwick text + VoR PDF both on disk.
  Purge scoping: the dye supplement exists at TWO historical paths
  (pre-reorg `outputs/dye-et-al-2023/...` and the current `studies/...`
  path) — filter by basename/blob, not one path — and the LFS object must
  be removed too. History audit of all ever-tracked PDFs found one other
  publisher PDF (Sobotkova et al. 2023, old `sources/PDF/` path) — checked:
  Applied Geography, 10.1016/j.apgeog.2023.102967, hybrid OA, CC BY →
  CLEAR, no purge. The corpus PDFs and `input/sources/original-pdf/` were
  never tracked; all currently tracked PDFs are the project's own artefacts
  (reproduction figures; a draft proposal). Side-fix applied:
  key-et-al-2024's DOI in the corpus queue corrected to the resolving
  2023-prefix form (recorded 2024-prefix form 404s; verified at CrossRef).
- **Identity confabulation CORRECTED (2026-07-14, `38adf36`):** CITATION.cff,
  codemeta.json, CONTRIBUTING.md, and the pilot findings report had carried
  "Shawn Graham" / Carleton University / github.com/shawngraham since their
  2025-11-13 creation. Now Shawn Ross / Macquarie University /
  github.com/saross, ORCID 0000-0002-6492-9025 (verified against author lines
  in Shawn's published papers). archive/ and verbatim extracted texts left
  untouched (the sobotkova-et-al-2016 mention is the real Shawn Graham).
- **Machine sync COMPLETE (2026-07-15):** amd-tower ready for resume. Old
  pre-purge clone quarantined (NOT deleted) at
  `~/Code/repo-backups/llm-reproducibility-pre-purge-clone-20260715` on
  amd-tower — never pull/push from it (pre-purge history; also holds on-disk
  copies of the purged files, consistent with keep-local-copies). Fresh clone
  at `~/Code/llm-reproducibility`: purged paths absent from history (verified
  0 hits), pre-commit hooks installed, 30 gitignored corpus/text assets
  rsynced from zbook with all checksums verified (incl. dye supplement
  820,582 bytes; marwick CC BY preprint). Gotchas: amd-tower remote is now
  **HTTPS + gh credentials** (its GitHub SSH key needs an interactive agent;
  `git remote set-url origin git@github.com:saross/llm-reproducibility.git`
  to switch back); venv not recreated (`python -m venv venv &&
  venv/bin/pip install -r requirements.txt` when scripts are needed);
  `.claude/settings.local.json` deliberately not copied (machine-local).
- **Immediate priority (displaces the above):** draft the Cosmos Institute
  grant application (deadline 26 Jul 2026); framing in
  `wiki/planning/cosmos-grant-application-framing.md`.
- Stale-carry-forward note for future resumes: the 2026-07-06 handoff
  verdicts were already applied in `a1e52de` — do not re-solicit them.

### Earlier state (2026-06-07)

- `main` @ `1c4650e` (merge of PR #1). Working tree clean.
- **PR #1** added a matching-grade extraction layer to
  `extraction-system/scripts/pdf_processing/`: `normalise_for_matching`,
  `normalise_text_readable`, `PDFExtractor.extract_pages` (per-page text with
  page-index + section locators), and promoted cleaners (`strip_running_headers`,
  `drop_fragment_headings`, `split_body_references`, `strip_affiliation_tail`,
  `looks_like_heading`). First tests in the repo at
  `extraction-system/scripts/pdf_processing/tests/test_matching_layer.py`
  (24/24 pass). Additive/opt-in: existing `extract()` behaviour unchanged.
  Built for an annotated-bibliography (AB+) pipeline in the paper-b project;
  design context in that repo's
  `planning/pdf-extractor-consolidation-plan-2026-06-07.md`.

## Pending tasks

### E. AMENDMENT LODGEMENT — three tasks, then the validation phase unblocks  [x] 2026-08-03

**This is the critical path.** The consolidated OSF amendment must lodge
*before* the validation phase runs (hard stop, registrant's 2026-07-24 timing
call). Three items stand between here and the OSF form; the checklist itself
lives at the foot of
`studies/open-science-compliance/prereg/amendment-1-draft.md`.

- [x] **E1. Fold the third benchmark arm into §3.** 2026-08-02 — **Shawn:
      add the Fable arm** (option (a), name all three identifiers). Done: §3's
      provenance paragraph now pins `claude-sonnet-5`, `claude-opus-5`,
      `claude-fable-5`. Two further edits followed from it, both pre-declaring
      rather than reconstructing:
      - §3's selection rule now states that the three arms are strictly
        ordered by published price, so **the Fable arm cannot be selected for
        the census under any spot-check outcome** — it is run to test whether a
        more capable model clears the same reliability gates (evidence about
        the instrument, not the model) and to supply §5 robustness data. A
        pricing-change clause applies the rule to prices in force at selection.
      - §5 now says the annex explicitly covers an arm excluded from selection
        by construction.
      **Billing route settled the same day:** Max-plan Fable allocation first
      (if that route is feasible for subagent spawns), with a configured
      Anthropic API billing account for direct calls or excess-of-plan usage.
      No per-arm approval outstanding — the run is governed by the ordinary
      standing API review gate, presented once before it runs.
- [x] **E2. §1 word-for-word consistency check — done 2026-08-02.**
      Checked against canonical `fair-instrument.md`, the Pass 6 prompt mirror
      (byte-identical to canon, 5,123 bytes, re-diffed), prereg §7.1, the
      frozen copy at `ee3fda3`, and the persisted pilot outputs. Record in
      `amendment-1-draft.md` (final section): 7 deliberate differences
      recorded; 3 flags raised and **adjudicated same day** — (1) quotation
      placement FIXED (parenthetical moved outside the quotes, Shawn's
      verdict); (2) en dash inside quotes ACCEPTED as typography; (3) the
      "four of five persisted FAIR assessments" scope flag DISSOLVED: a fifth
      persisted assessment exists (crema run-02, key `infrastructure` not
      `reproducibility_infrastructure`, one level below the `outputs/*/`
      glob — the two reasons erratum Entry 2's sweep and this check's first
      pass both missed it). Verified: 12/15 + 12/15 matching Table 5, none
      unscored, no aggregate, A1 present. §1's sentence stands as written for
      all five pilots. Run-01 was archived not lost (`c41242b`). **Candidate
      follow-ups, Shawn's call:** dated correction note on erratum Entry 2's
      "the four papers carrying FAIR assessments" scoping; working-notes obs
      candidate (Observation-16 shape again — a sweep scoped narrower than
      its readers assume, this time by glob depth + key name).
- [x] **E3. Build the paste artefact — done 2026-08-03.**
      `prereg/osf-amendment-1.txt`, generated mechanically from the promoted
      amendment text and unwrapped via `unwrap-paste-file.py`. Docstring
      verification passed: word count unchanged by unwrap (1,263 → 1,263),
      numbered lines 5 → 5 (the section headings), 0 bullets, 0 table rows,
      no markdown residue; token comparison against the canonical section
      identical (68 numeric, 4 quoted, 10 § refs).
      **Context for E4 (2026-08-03 decisions):** the lodgement text is the
      promoted academic-prose re-expression (registrant read both versions;
      skill-test record archived at `archive/prereg/`); rule-4 check re-run
      against it, PASS (13 frozen phrases verbatim, addendum in the draft's
      record section). §5 gained a two-sentence cross-vendor pre-declaration:
      **OpenAI arms (Sol/Terra/Luna) considered and deferred** to a possible
      post-census extension via dated amendment plus the §8 reliability
      protocol — not folded into this registration's validation phase
      (confound: cross-vendor arms cannot hold the delivery apparatus
      constant, so they compare model+harness bundles, not models).
- [x] **E4. LODGED 2026-08-03 — route changed to API filing on Shawn's
      decision.** Not by-hand paste: filed as an OSF versioned registration
      update (SchemaResponse revision `6a7017da97adb06288afef80`) after an
      Opus-agent sweep of the developer docs, a staged in-progress draft
      verified byte-identical on round-trip (39,725 chars; original 30,907
      untouched), and Shawn's placement decision (append at end — the
      summary field is the landing content). Submit + approve in one
      sitting. **DOI unchanged by design**; amendment version URL
      <https://osf.io/dqnhg?revisionId=6a7017da97adb06288afef80>; tag
      `osf-amendment-1-2026-08-03`. Reading done at promotion.
      **TASK E COMPLETE — the validation phase is unblocked.** Same-day
      follow-through (2026-08-03): **PR #2 MERGED** (`58c3fe7`) as the one
      change — schema v2.7 + eight-prompt cascade + project.version 3.0.1 →
      3.1; Pass 6 edits outside the mirror region, classified an ordinary
      §8 implementation change (no erratum, no amendment; classification
      presented, standing land decision applied). **Monitoring §9 all
      RESOLVED** (Shawn: wiki not registered; E7 warn-first; one verified
      remap pass early Phase 4; crema register-without-rewrite) and
      **Phase 0 COMPLETE** — 55 entities enumerated and classified, plan
      §10; per-entry re-check found no true drift, four
      missing-version-carrier flags for Phase 1. Phase 0 gate passed and
      **Phase 1 COMPLETE same day** (Shawn's go, 2026-08-03): central
      `entity_checks:` map (56 declarations) + `reference_datasets:` E8
      registration (five pilot FAIR assessments, crema's key declared
      as-is) + two version carriers added (workflow.md, credibility JSON
      schema). Two Phase 0 flags dissolved — the skills and the
      credibility template already carried versions under labels the
      Phase 0 regex missed; carriers declared instead of added. Gate
      PASS, 32/32. **Phase 2 COMPLETE same day** (`e2b6568`): the gate now reads
      `entity_checks` — per-class verification E3-E8, undeclared-entity
      and unresolvable-declaration failures, declared normalisation.
      Tests 32 → 46 (one injected defect per class). Closure probe: the
      2026-08-02 probe (9.9 on the preparation prompt) that then
      produced PASS now FAILS with a named error. **Next gate:
      Phase 3** (coverage self-report line + pre-flight wiring). Remaining
      after that: the three-arm benchmark run (still gated on the
      standing API review presentation: model, batch vs real-time, 45
      spawns, estimated cost). Flag from the docs sweep, low priority: the
      original registration text's two escaped comparators ("post &gt; pre
      on all measures", "pinned &lt; unpinned") may render as literal
      entity strings on the public page; eyeball, and if wrong it is
      erratum-log material for a future revision, not a ride-along edit.

### A. Git hygiene — untrack the committed virtualenv  [x] 2026-07-03

> Done 2026-07-03 exactly as prescribed below: 2,114 index deletions, files kept
> on disk; post-check `git ls-files | grep -c '^venv/'` = 0; stray-bytecode sweep
> outside venv = 0 tracked files.

The repo tracks the **entire `venv/`** — **2,114 files** (verified 2026-06-07:
`git ls-files | grep -c '^venv/'`), including thousands of `.pyc`. `.gitignore`
**already** lists `venv/`, `__pycache__/`, and `*.py[cod]` (lines ~5–10), so
these were force-added or pre-date the ignore (tracked files are not
auto-ignored).

Fix (own commit/PR — large, mechanical):

```bash
git rm -r --cached venv
git commit -m "chore: untrack committed virtualenv (already in .gitignore)"
```

Caveats:

- ~2,114 deletions from the index (files stay on disk). Do it standalone.
- Anyone relying on the committed venv must recreate it:
  `python -m venv venv && venv/bin/pip install -r requirements.txt` — note this
  in the commit body and/or README.
- After: `git ls-files | grep -c '^venv/'` should be `0`.
- Also sweep any other tracked bytecode outside venv:
  `git ls-files | grep -E '__pycache__|\.pyc$' | grep -v '^venv/'` (should be
  empty — PR #1 already removed the one stray
  `extraction-system/scripts/pdf_processing/__pycache__/pdf_cleaner.cpython-312.pyc`).

### B. Migrate docs to the wiki-style layout  [x] 2026-07-03

> Done 2026-07-03. `docs/notes/working-notes.md` → `wiki/working-notes.md`;
> `docs/notes/reflections/` → `wiki/reflections/`; repo-root `planning/` →
> `wiki/planning/` (all via `git mv`); created `wiki/index.md`,
> `wiki/user-observations.md`, `wiki/claude-observations.md`; wiki frontmatter
> merged into migrated pages (additive — `/reflect`'s priority/scope/audience
> keys preserved); reference sweep across all living docs (archive/ and frozen
> reproduction artefacts deliberately untouched); CLAUDE.md continuity pointer
> added; README gained a docs-vs-wiki disambiguation map. **docs/ disposition
> decided (Shawn, 2026-07-03): stays at repo root** — product documentation
> follows the GitHub/JOSS convention (Pages builds from /docs); only the
> process layer moved to wiki/.

This repo uses the **legacy `docs/notes/` layout** and lacks `continuity.md`
(this seed) and `user-observations.md`. Target = the canonical per-project
wiki layout (authoritative reference: `~/personal-assistant/wiki/index.md`,
"PA project layer" table; migration precedent:
`~/personal-assistant/wiki/planning/wiki-index-draft.md`).

| Artefact | Target | Source now |
|---|---|---|
| `continuity.md` | `wiki/continuity.md` | **this file (seed, in place)** |
| `index.md` | `wiki/index.md` | new (small index; model on PA's) |
| `working-notes.md` | `wiki/working-notes.md` | `docs/notes/working-notes.md` |
| `reflections/` | `wiki/reflections/` | `docs/notes/reflections/*` (session-log, session-reflection, abductive-reasoning, llm-observations) |
| `user-observations.md` | `wiki/user-observations.md` | new (model on paper-b's `docs/notes/user-observations.md`) |
| `planning/` | `wiki/planning/` | repo-root `planning/` |
| Documentation | decide: keep `docs/` vs `wiki/docs/` | repo-root `docs/` |

Steps:

1. `git mv` legacy files into `wiki/` (preserve history).
2. Create `wiki/index.md` + `wiki/user-observations.md` from the convention.
3. Add wiki frontmatter (`title`/`tags`/`created`/`updated`/`status`) to
   migrated pages; tags from the 24-term vocabulary in PA's `wiki/index.md`.
4. Add a "Session continuity → `wiki/continuity.md`" pointer to this repo's
   `CLAUDE.md` (belt-and-braces; the global session-start protocol already
   reads `wiki/continuity.md`).
5. Resolve the `docs/` disposition (see open decision).

Caveats:

- `docs/` here is large and public-facing (assessment guides, background
  research, FAIR docs) — unlike PA's, it may warrant staying at repo root
  rather than moving under `wiki/docs/`. Decide deliberately.
- `/reflect`, `/observe`, `/handoff` are layout-aware and fall back to legacy
  paths; after migration they target `wiki/`.

### C. Fix lossy de-hyphenation of genuine compounds  [x] 2026-07-06

> Done 2026-07-06, following the fix direction below with one refinement: the
> dictionary check takes precedence over the affix list (if the joined form is
> a known closed-form word, join — so `multi-\nple` → `multiple` even though
> `multi-` is a compound prefix; otherwise a compound prefix keeps its hyphen —
> `self-\ncorrection` → `self-correction`). Dictionary = frozen subset of
> wamerican 2020.12.07-2 shipped at
> `extraction-system/scripts/pdf_processing/affix-joined-words.txt` (9,810
> affix-prefixed words) so canonical matching keys stay machine-independent.
> Chained breaks handled (dict check sees the flattened fragment:
> `multi-\nfa-\nceted` → `multifaceted`). Idempotence preserved; golden tests
> green; 8 regression tests added incl. the Huang self-correction case
> (32/32 pass). Residual ambiguity documented in the `_dehyphenate` docstring:
> a deliberate hyphen broken at exactly that hyphen resolves to the closed
> form when that form is a dictionary word; non-prefix compounds
> (`decision-\nmaking`) keep the historical joining behaviour.

`_dehyphenate` (`extraction-system/scripts/pdf_processing/pdf_cleaner.py:348-361`,
regex `re.sub(r"(?:-\s*\n\s*)+([a-z])", r"\1", text)`) joins any end-of-line
hyphen followed by a **lowercase** letter and **drops the hyphen
unconditionally**. This is correct for line-break artefacts
(`archaeo-\nlogy` → `archaeology`) but **lossy for genuinely-hyphenated
compounds broken before a lowercase letter** — e.g. `self-\ncorrection` →
`selfcorrection` (hyphen lost). The existing guard only protects compounds
broken before a **capital** (`well-\nKnown` stays). Feeds **both**
`normalise_for_matching` and `normalise_text_readable`.

Concrete case (re-verifiable): Huang et al. 2023 (Zotero attachment
`K294C8KD`), `page_index 3`, "...after self-\ncorrection, the accuracies..." →
the matching key contains `selfcorrection`, so a naturally-written quote
("after self-correction, ...") **fails** the deterministic quote-checker even
though the content is present. Discovered 2026-06-10 during the paper-b AB+
co-design (`planning/section2-grounding/ab-plus/huang2023large.md`, "Extraction /
fidelity notes").

Impact: a quote spanning a line-broken hyphenated compound silently fails the
checker; paper-b currently works around it (quote from text-as-extracted +
display-cleanup) but the canonical key itself is wrong here.

Fix direction (heuristic — full de-hyphenation is ambiguous): keep the hyphen
when the prefix is a known hyphenating affix (`self-`, `multi-`, `non-`, `pre-`,
`co-`, `anti-`, `inter-`, `intra-`, `well-`, `re-`, `e-`, …) or when **both**
fragments are independently valid words (wordlist check); drop it otherwise.
Must preserve `_dehyphenate`'s **idempotence** (the readable + matching
normalisers depend on it) and keep golden tests green; add a regression test
for the `self-correction` case. Additive/worktree discipline.

### D. Consolidate version-history sources  [ ]

Version history is now maintained by hand in four places (`manifest.yaml`
`version_history` — nominally canonical; `CHANGELOG.md`; README "Development
History"; `docs/research-assessor-guide/version.md`). The 2026-07-06 session
updated three of them in parallel to say the same thing. Candidate fix: derive
the CHANGELOG and README sections from the manifest (script or documented
cascade checklist, mirroring the assessment-schema compliance pattern from
February). Low priority; logged from llm-observations 2026-07-06.

## Open decisions

- [x] 2026-07-03 `docs/` disposition: **stays at repo root** (decided with the
  conventions rationale recorded in task B note above and README's docs-vs-wiki map).
- [x] 2026-07-03 Sequencing: done as separate commits (A on 2026-07-03 standalone;
  B as its own migration commit).

## Session log

### 2026-10-21 → 10-23 (session a9c4834d) — gate 1.3.2 planner pilot analysed, held, fixtured, and mailed; zbook synced

One session on Opus 5.5, worked partly over remote control, no
compaction. It opened from the a1bac2e9 handoff to monitor the pilot,
which had not yet launched: the launch session (`e854d6a4`) was paused at
the API gate, and Shawn's go there at 09:58 AEDT on 2026-10-21 started it
while this session ran pre-flight in parallel (byte-identical args, so
harmless). `e854d6a4` ran `persist-plans`, `audit-run`, and the hold;
Shawn then moved the run here. The state is in the NEXT SESSION block.

- **Run:** `wf_88429e16-a85`, $2.59, 15.8 min, audit clean. Acceptance
  checks 1, 2, and 4 met; 3 failed on T15 (the old T17), credited on
  `data`, which is `Herskind&Riede_S2.R` line 30 (`read_excel` of S1).
- **Ruled by Shawn:** T15's Q5 input condition `no`; the plan held
  (`aea100f`); the run admissible on blinding; route A for check 5; the
  registrant's reading of `inputs-from-authors-code` (text in the results
  doc); the mail to Astra.
- **Built:** the labelled route A fixture (`f34a756`; five tests; 773
  pass on amd-tower).
- **Docs:** the results doc (`5cc0f33` from `e854d6a4`; `02376eb`
  corrected its claim that the hold re-ran the rule checks; `2476c64`);
  continuity (`1c88d69`, and this handoff).
- **Found:** the blinding audit misses a bare-name Bash read outright;
  `writes_outside_scope` cannot fire for a planner; the cost estimate was
  low by about half.
- **zbook synced** for the week away (NEXT SESSION block): clone, hook,
  venv, and corpus store; `docker-buildx` left for Shawn (needs sudo).
- **Working-notes candidates (held for Shawn's verdict):**
  - **WN-az:** a plan contract's mechanical checks pass a condition
    answered consistently but falsely. In the gate 1.3.2 planner pilot the
    planner quoted all 10 lodged rules whole across 138 applications,
    stated every condition, and planned T15 creditable on true but
    irrelevant evidence ("Presence columns are read from `data` created by
    executing the authors' PART 1"; `data` is S1 loaded by `read_excel`).
    `rule_problems` found nothing, and only the approver's check of the
    authors' code caught it. The planner had flagged its own reading for
    the approver and claimed the credit anyway. Anchors: results doc F1;
    `PlannerPilotFixtureTests.test_the_held_plan_passes_every_mechanical_check`
    (`f34a756`).
  - **WN-ba:** per-target rule applications multiplied a planner's output
    and hid it from the live cost check. The pilot's planner wrote 73,985
    output tokens, against 20,303 for the same paper's previous planner
    (`wf_db7d121a-5d5`), at $2.59 against $1.2969, both over 17 requests;
    the estimate's "a few thousand tokens" for `rules_applied` missed that
    10 rules over 17 targets gave 138 applications with evidence. Its last
    turn alone was 46,825 output tokens, and the watcher, pricing completed
    turns, read $1.655 at 12.6 minutes and still at 15.6, so a cost
    tripwire can be overshot by one turn. Anchors:
    `audit-wf_88429e16-a85.json`,
    `../gate-1-3-1-pilot-rerun/audit-wf_db7d121a-5d5.json`; results doc
    F2 and F3.

### 2026-10-18 → 10-21 (session a1bac2e9) — gate 1.3.2 criteria 1 to 3 built, reviewed, merged; planner pilot launched

One session on Opus 5.5 across four days, no compaction. The state is in
the NEXT SESSION block above; the factual record is in
`wiki/reflections/session-log.md`.

- **Built:** criteria 1 to 3 on `feat/gate-1-3-2` (target-scoped concerns
  and rulings, `adjudicate`; reviewer method rows; the lodged-rule registry
  and `rules_applied`), merged as PR #13 (`df394c1`).
- **Ruled by Shawn:** about a dozen design choices (in the design's gate
  1.3.2 note); the restated attempt-04 rulings (`f9328ed`); the PR text;
  the Q5 and R2 condition lists; `unknown` refused where the plan settles a
  condition; the lane script neutralised and unblinded for the pilot.
- **Reviews:** Astra, three rounds (three class D, then two residuals,
  then approval). Fable not used (rationed).
- **Side agents:** five notes, all adopted: slips as rulable flags, the
  planner pilot, `unknown`, the blinded lane script, the blinded rule
  source in the prompt.
- **Working-notes candidates (held for Shawn's verdict):**
  - **WN-ax:** hand-enumerated malformed-shape checks took three review
    rounds; validating against the agent's own output schema closed the
    class. Astra's first review (2026-10-19) found scalar collections
    crashing the review validators; the guards closed the named sites, and
    her re-check (2026-10-20) found a present `null` passing as assessed
    and a list-valued `dimension` still crashing, including in
    `persist-results`. Validating each concern and method row against its
    definition in `adversarial-review-output.json` (`shape_defects`,
    `02e35df`) closed both, and her third round approved. Anchors: her mails
    `2026-10-19-codex-gate132-criteria-review.md`,
    `2026-10-20-codex-gate132-closure-recheck.md`,
    `2026-10-20-codex-gate132-residual-closure-review.md`; commits
    `07ac8b3`, `02e35df`.
  - **WN-ay:** a blinding list can contaminate an obedient agent when the
    prompt points at what it forbids. Two such routes in the planner pilot:
    the run notes named `run-container`, in the blinded lane script, and
    the prompt named R1 to R4's source, in the blinded `outputs/validation/`.
    `audit_agent` counts any Bash command naming a blinded path as
    contaminating unless it errored. Base rate: the previous herskind
    planner (`wf_db7d121a-5d5`) made 19 tool calls and touched neither.
    After the fixes (`a37a1f6`, `71fdd72`, `3307000`), a full render of the
    pilot's prompt from dry-run args named no blinded path outside the
    blinding instruction.

### 2026-10-13 → 10-18 (session 8e28871d) — pilot stage 2 run, ruled, and persisted; gate 1.3.1 closed, 1.3.2 scoped

One session on Opus 5.5 across five days, no compaction; from 10-17 Shawn
worked over remote control. The results are in the NEXT SESSION block
above; the factual record is in `wiki/reflections/session-log.md`.

- **Run:** pilot stage 2 (`wf_4fd7a886-ada`, launch `6b18505`, 42 min,
  $14.02), after a pre-run review with Shawn's explain-back
  (`pre-run-review-stage-2.md`, H1–H7) and launched on his bare "go".
- **Merged:** PR #12 (`a29f16a`), between the authoritative gate and the
  audit.
- **Ruled by Shawn:** all 17 issues (T17 not creditable, study coverage
  13/18); gate 1.3.1 closed and 1.3.2 opened; the launch word rule as a PR
  after the pilot; cost and time overruns as stop conditions set per run;
  attempt 4 kept on amd-tower.
- **Reviews:** Astra (2026-10-17) and Fable (2026-10-18) on the closure and
  scope, both concurring; criteria folded into the design document.
- **Disclosed:** the watcher's time check could not have fired.
- **How we work (Shawn, 2026-10-18; standing rules in the global
  scratchpad):** the full pre-run review with his explain-back before every
  paid multi-agent stage, a short walk-through for single-agent runs; hold
  edits to files a reviewer is reading until the reply lands; Fable spend
  needs his OK every time, mail asks and spawns alike.
- **Working-notes candidates (accepted by Shawn 2026-10-18 as
  Observations 58 and 59):**
  - **WN-av:** the executor's per-target `method_as_planned` declarations
    caught one method departure of five on herskind attempt 04 (T13
    declared; T01, T03, T04, and T12 recorded as following the plan),
    while the adversarial reviewer, under a named method-adherence
    obligation, found all four undeclared ones. None changed an outcome.
    Self-declared deviations are weak evidence; the reviewer duty is the
    working mechanism. Anchors: attempt-04 `comparisons/comparison.json`
    (`method_as_planned`), `adversarial-review.json`
    (`methodological_soundness`), `flag-rulings.json`
    (`method-adherence:targets`).
  - **WN-aw:** two blind executor runs on herskind, under independently
    planned denominators (attempt 03, 20 targets; attempt 04, 18),
    reproduced the same discrepancy findings: the same eight Table 1 cells
    and the same two Fig. 4 boxes. They labelled them differently (Fig. 4
    PAPER_ERROR against MINOR_DISCREPANCY; Fig. 5 EXACT_MATCH against
    CANNOT_COMPARE), as each plan scoped the target. Findings replicated;
    outcome labels varied with plan wording. Extends Observation 56.
    Anchors: both attempts' `comparisons/comparison.json` and
    `reproduction-plan.json`.

### 2026-10-12 → 10-13 (session b5f7b974) — gate 1.3.1 merged, pilot stage 1 run and approved, PR #12 pricing

One session on Opus 5.5, no compaction, with a mail watch on Astra's
reviews. The results are in the NEXT SESSION block above; the factual
record is in `wiki/reflections/session-log.md`.

- **Merged:** PR #11 (`10500ea`), after Astra's delta review (three class
  D findings), her closure review (two residuals), and her approval.
- **Ruled by Shawn:** the reviewed-state binding stays strict
  (review-only mode later); the attempt-04 plan, accepting all six
  approver questions; the pilot stays at effort `high`, with a
  medium-against-high comparison before scaling; standing approval for
  Claude and Astra to run each other's code.
- **Run:** pilot stage 1 (`wf_db7d121a-5d5`), clean; stage 2 waits at its
  API gate.
- **Open:** PR #12 (lane v1.5), Astra's check pending.
- **Disclosed:** Claude ran Astra's probe scripts twice before the
  standing approval existed.
- **Working-notes candidates (accepted by Shawn 2026-10-13 as
  Observations 56 and 57):**
  - **WN-at:** two blinded planner runs on herskind with the same model,
    effort, rulings, and instruments gave different denominators: 20
    targets and 7 exclusions (attempt-03, launch `ad03008`) against 18 and
    4 (attempt-04, launch `5fdaf87`). The 8 display-item targets match;
    the named values differ (12 against 10), which the planner flags as a
    hand enumeration. Coverage denominators therefore vary between
    planning runs, a quantity worth measuring before production scale.
    Anchors: both attempts' `reproduction-plan.json`.
  - **WN-au:** the fixed launch phrase stopped relayed-message
    contamination in a live run. Attempt-03's planner, launched with a
    free-text message, listed Shawn's billing question among its approver
    questions (F3); attempt-04's planner, launched with "Run the approved
    stage", relayed nothing. Anchors: both plans' `questions_for_approver`.

### 2026-10-10 → 10-12 (session be70c3be) — ledger frozen, PR #7 merged, herskind pilot re-run, gate 1.3.1

One long session on Opus 5.5, compacted once (after the probes). The
results are in the NOW blocks above. The factual record is in
`wiki/reflections/session-log.md`, and the reflections are at `7592099`.

- **Merged:** PR #7 (`3be8313`, before its final review, which then ran
  post-merge) and PR #10 (`d0e6dfc`, the ledger frozen as v1.0).
- **Run:** herskind attempt-03 through the agentic lane (`78137fe`). It
  came out SUCCESSFUL at 17/20, but it is inadmissible under gate 1.3.1,
  correctly so, for its agents' partial reads.
- **Open:** PR #11 (gate 1.3.1), with Fable's delta findings closed and
  Astra's review pending.
- **Side notes Shawn relayed** turned into fixes:
  - the rocker snapshot date;
  - PR #7's skipped review;
  - coverage and minor discrepancies (amendment 4 items 5–7);
  - partial reads being unrulable;
  - audits checking against today's manifest.
- **Working-notes candidates (held for Shawn):**
  - **WN-ar:** both final reviews found their most serious defects by
    running the lane's code on the pilot's real artefacts: Fable's
    in-memory alteration, and the reviewer prompt lacking "Attempt
    directory:". Neither came from reading the code. A gate review should
    budget for one adversarial run, not only a read. Anchors: Fable's
    mails `20261012T032928.805148Z` and `20261012T113743.407608Z`.
  - **WN-as:** the transcript audit's false hard failures came from
    regex splitting of shell commands, and every one was a common idiom
    (`awk 'NR>1'`, a heredoc with `>=`, `--help`). An unwaivable check
    built on pattern matching must be tested on real agent transcripts
    before it is trusted. Anchor: PR #11 `4dc74d7`.

### 2026-10-08 → 10-09 (session be70c3be) — overnight: gate 1.3 built, instruments edited, ledger drafted

An autonomous overnight session on Opus 5.5, compacted once. It worked in
the PR #7 worktree (Track 1), the PR #9 worktree (Track 2), and a new
ledger worktree (Track 3). Results are in "Overnight progress" above.

- **Track 3 method.** Four read-only Opus subagents transcribed the
  printed values, one per pilot. Each load-bearing claim was then
  re-checked at source: the text layer, a page render for raster labels,
  and scripts against the pilot reports and outputs. The re-checks caught
  three of my own slips before commit: wrong initials for three of key's
  authors, a differing-cell count (21 written, 18 true), and a missing
  ruling id.
- **Network:** public downloads only. Crema's v1.0.0 zip came from Zenodo
  and marwick's `paper.docx` at tag 1.3 from GitHub; a Zenodo re-download
  of marwick's zip returned HTTP 504. **Slip, reported:** the first
  Zenodo request's User-Agent header carried Shawn's email address, which
  breaks the rule against sending it to unrelated services. Later requests
  omitted it.
- **Working-notes candidate (held for Shawn):**
  - **WN-aq:** in four of the five pilots, the comparison report's
    "published" column was wrong. Crema's held v2.0.0's own re-run,
    dye's held branching values taken from its own output, marwick's held
    a W never read from the paper, and key's swapped two cells. The
    executed-code audit checked what code ran, not what it was compared
    against, so it found only crema's. An audit of a reproduction needs
    both legs. Anchors: PR #10, `correction-ledger/README.md`, "Findings
    beyond the executed-code audit".

### 2026-10-06 → 10-08 (session fabeab56) — amendment 3 lodged

One session: Fable 5.1, then Opus 5.5 from the decision walk-through,
compacted once. It worked in the main checkout and the PR #7 worktree.

- **2026-10-08: lodgement.** Shawn approved the revision as is, then ruled
  that the opening paragraph would be renamed and a scope sentence added.
  Astra's follow-up (at `857702d`) said revise. B1 was blocking: the
  failed-pin sequence had never been specified, and Shawn ruled the pin's
  own neighbours. S1 corrected the audit's location, now cited at
  `c4553f9` with a tag. S2 narrowed the lodgement script's failure
  guarantee. The re-check (at `4258db8`) found no blocking issues, and the
  lodgement ran at `abde9b1` as OSF revision `6ac775afb5ed5b4afee88a4a`.
- **Working-notes candidates (held for Shawn):**
  - **WN-ao:** a rule joined from two separately reviewed rulings (the
    4 October cap and D-7's precedence) left the failed-pin sequence
    unspecified. It passed the drafting session, Fable's advice, and two
    reads by the registrant. It was caught when a reviewer ran a concrete
    case (pin P fails; what is attempt two?) against the hypothesis it
    feeds (H3). Anchors: amendment 3's revision record, "Follow-up
    review"; Astra's mail `20261008T075615Z-codex-amendment3-followup-review.md`.
  - **WN-ap:** facts about OSF's schema-response API, from the lodgement
    and OSF's source.
    - A Summary of 98,004 characters was accepted.
    - Text with no `<` or `>` is stored byte-identical.
    - Anonymous listings show approved revisions only.
    - A second unfinished revision cannot be created.

    Anchors: the header of `lodge-osf-amendment.py`, and
    `get_default_queryset` and `create_from_previous_response` on OSF's
    develop branch, 2026-10-08.

- **Astra's amendment 3 review** (six blocking, five should-fix) was
  verified premise by premise at source before any edit, and every premise
  held. Three findings needed registrant decisions rather than drafting,
  so they became D-7 to D-9 with proposed text. Fable gave a second
  opinion
  by SendMessage; its refinements went in where verified, and two
  unverified counts were dropped, then restored once Fable supplied anchors
  that checked out.
- **A register pass** brought the revised prose back inside the targets
  (announcement colons 2.09 to 1.56 per thousand words) without touching
  the quoted rulings.
- **Gate 1.3.** Astra's specification review folded in as revision 2; then
  the F1 completeness corrections and the hook's traces, each probed in
  Docker before being written. Revision 2's parent-side `JOIN` lasted an
  hour: the probe showed the child's own `mcexit` is the reliable terminal
  event, and the text was corrected before any code was built.
- **Pattern worth keeping.** Every multi-line edit in both repositories
  went through an exact-once replacement script that aborts before
  writing, so a partial edit was impossible.

### 2026-10-05 → 10-06 (session b1a1e102) — gate 1.3 consolidated, reviewed, and its foundations built; every pending ruling cleared

One session on Opus 5.5. It worked in the PR #7 worktree, with Fable
reviewing live by SendMessage.

- **Cache fix first.** The part 1 digest cache was process-wide. Two new
  tests (a same-size edit with the modification time restored) failed on
  it, which showed the gap was real.
- **Consolidation.** One effective specification replaced the draft and
  its two revision sections, and it carries a stopping rule. A Docker probe
  turned several memory-based review points into tested facts; the most
  consequential is that a project `.Renviron` overrides `R_PROFILE_USER`.
- **Fable's review** came back within the hour. Its findings included two
  defects in the new text (trace order, and pairing processes by PID) and
  four ordinary routes. Most went straight into F1's code.
- **Exchange on `R CMD`.** Fable proposed a subcommand list. The image's
  own `BATCH` and `INSTALL` scripts showed that subcommands re-enter the
  front end, so their inner starts are censused separately. Fable
  withdrew the list, and `INSTALL`'s inner start is now the one real gap.
- **F1–F3** are built, each with tests, all pushed. Astra's review of the
  specification is outstanding.
- **Decision walk-through (2026-10-06, Shawn present).** About 34 pending
  decisions, scattered across three sessions, were cleared in one sitting
  from structured questions, with each item's context re-assembled from
  its source:
  - amendment 3 D-1 to D-5 (`c99c2a0`);
  - audit Q2–Q10 (`c4553f9`, and `38b59b0` for the general rules);
  - Astra's posted reviews (attributed; reviews are documents from now
    on, personal-assistant PR #169);
  - PR #8, merged (`7f84e73`);
  - WN-ag to WN-al, as Obs 45–50 (`a8da2e1`);
  - the user-obs batches (`10a75c0`);
  - the lane-script split, after merge (`42da7fc`);
  - record-weighted coverage, not collected.

  Two items needed a pros-and-cons round. In one (D-2), assembling the
  trade-offs exposed an incomplete framing and changed the recommendation.
- **Reflections:** `/reflect` (`75cc6d8`), with Entry 23, an abductive
  entry, and claude-obs 71–74.
- **Working-notes candidates (held for Shawn's verdict; silence holds
  them over):**
  - **WN-am:** instrumenting R reproductions, a project `.Renviron`
    outranks a container's `-e R_PROFILE_USER`. In `rocker/r-ver:4.3.2`
    the project's profile loaded in place of the lane hook under every
    launcher tried, until the lane took over the environment-file phase
    (`R_ENVIRON_USER`). A naive logging hook would therefore run unhooked
    on any project that sets its own profile. This bears on the paper's
    account of how the reproduction lane establishes what code ran.
    Sources: gate 1.3 specification, probe facts 1–2 (PR #7), and the
    abductive entry of 2026-10-05.
  - **WN-an:** the cost of human oversight in the governance loop. About
    34 decisions had accumulated over three sessions of autonomous work.
    One sitting cleared them, once each item's context was re-assembled
    from its source, grouped by what it blocked, and offered with a
    recommendation; two needed a trade-offs round first. This bears on
    the paper's account of what supervising an agentic pipeline costs the
    researcher, and how the cost is batched.

### 2026-10-04 (third session) → 10-05 — F2 rule and v1.2 packs; amendment 3 drafted; PR #7 through three review rounds; gate 1.3 part 1

One session (ef0412bd) on Opus 5.5, no compaction. The plan was the
no-spend pre-gate build, then amendment 3.

- **F2 rule.** Building it exposed that the evidence packs lacked the F2
  fields, which changed the plan to a census-input re-validation (amendment
  3 §6). The rule and hybrid validated without API spend.
- **Amendment 3** is drafted in full, with six decisions. Two are ruled: the
  correction ledger and the class (ii) consequence.
- **Reproduction-lane audit.** A subagent built the code-integrity gate and
  ran the executed-code audit, which weakened the pilot baseline (see START
  HERE).
- **Review rounds.** Shawn put PR #7 through cross-model review, adding Fable
  for a second opinion: three rounds by Astra and two by Fable. They found,
  in turn, provenance resting on the executor's manifest, execution never
  bound, and about a dozen executed bypass routes.
- **Gate status.** Gates 1.2 and 1.3 part 1 are built. The run command
  (Shawn: build it now, writable-copy design) and lane-computed conversions
  (option C) are designed and reviewed, but not built.
- **Incident.** Hook-run test fixtures inherited `GIT_DIR` and set
  `core.bare` in the shared config. It was repaired before any push and
  reported with `/feedback`.

Full record: `wiki/reflections/session-log.md`; reflections at `7da4177`.

- **Commits (main):**
  - `8864ceb`, `4c77b67`, `6c8ed51`, `cf0d92e`, `06c1ca9`, `07b6fba`, and
    `ff278ff` (F2 work);
  - `4c5bdf7`, `1763b2a`, `f3fb3a7`, and `208bf5e` (amendment 3);
  - `7da4177` (reflections);
  - PA data `64b36a3` (backlog).
- **Commits (PR #7, `feat/lane-gate-1-1-code-audit`):**
  - `916a097`, `ff5f911`, `2907806`, and `dc67b81` (subagent);
  - `71e1f21` (audit report);
  - `458878b`, `43a3453`, `0d87a8f`, `5766fb4`, and `4244a51` (gates 1.2
    and 1.3 part 1);
  - `5e741a3`, `71fb731`, and `2bd35aa` (gate 1.3 design and reviews).
- **Working-notes candidates (held for Shawn's verdict):**
  - **WN-aj:** the scorer's systematic F2 over-credit was an input gap, not
    a judgement error. The v1.1 packs carried no keywords or descriptions,
    and 20 of the 90 Opus F2 evidence strings for the Zenodo pilots name
    that gap and credit F2 anyway ("caveat, then credit"). The gate figures
    therefore count missing input against the model.
  - **WN-ak:** the pilot regression baseline is weaker than §8 assumes.
    - Three attempt-01s executed no authors' file.
    - Two executed a non-AP-12 version.
    - Crema's Table 1 credit compared v2.0.0's re-run with itself (0.1003
      against the paper's 0.1023).
    - In key, the authors' script computes the means (`summary()`), but the
      reproducer recomputed them.

    This is evidence for reporting reproduction results as artefact-bound,
    not as claims about the paper.
  - **WN-al:** cross-model review of a mechanical gate. Reading for trust
    boundaries (Astra) and running attack scripts (Fable) found different,
    non-overlapping classes of defect. Each round found new routes,
    including in the fixes for the previous round's findings. A method
    finding for the paper's account of LLM-assisted pipeline building.

### 2026-10-04 (second session) — Opus 5.5 arms run; `medium` selected; checks policy, clarifications, and Layer 1 built

One session (c5ee7a27) on Opus 5.5, no compaction. Shawn sent a neutral "Go"
at launch, then returned for rulings. The three approved Opus 5.5 arms ran
clean in about 18 minutes. All three efforts clear both gates, and two
derivations agree on every figure across nine arms. By the pre-declared
rule the cheapest eligible configuration is `claude-opus-5-5` at `medium`
($8.70 recorded scoring cost, against opus-5 high's $17.27), and Shawn
confirmed it.

Along the way:

- **F-019 found.** Output tokens are under-counted where a request's final
  transcript entry is missing. It is pre-existing and weakens the
  2026-10-04 D4 record's high-versus-xhigh cost ordering; ruled, and a
  note added.
- **Dye.** T06 is PAPER_ERROR, and dye's regression label is PASS.
- **Mechanical checks.** The disagreement policy was ruled and Layer 1
  built: `check-payload-quality.py` v1.1.
- **Clarifications.** The four reproduction-lane clarifications and six
  follow-ons were ruled as amendment 3 items 6–8.
- **Registers.** Observations 34–44 were written, and every held user-obs
  batch adjudicated.

Full factual record: `wiki/reflections/session-log.md` (2026-10-04, second
session).

- **Commits:**
  - arms `2c93a5d`, `656036f`, `7365e14`; F-019 `40d9008`; gates and cost
    `31cdc85`;
  - rulings `43cc274`, `fa67244`, `bc54450`, `22ee93b`, `07666c8`,
    `4e0033e`;
  - Observations `0393092` to `abbac69`; user-obs `49243da`;
  - checker `132f95a` and `d10fbb3`; race note `dbcb2db`; reflections
    `f22c72e`.
- **Working-notes candidates (held for Shawn's verdict):**
  - **WN-ag:** model-produced structured records carry arithmetic slips at
    a low but non-zero rate. Under v1.1, 2 of 135 benchmark payloads had
    one: a total that disagrees with its items, and a scored item in a
    section marked unavailable. The builder also reported two miscounted
    totals and a record-weighted coverage figure in the primary field in
    the August fable arm; I have not re-verified those. Computing derived
    fields removes the whole class, so the right verb is "compute", not
    "check".
  - **WN-ah:** delegates told to re-derive from sources caught the
    coordinator's errors. The obs-writer corrected the herskind R1.3 claim
    in my brief, and the checker's builder found contradictions in my
    planning note and a nuance in the coverage rule. A brief carries the
    coordinator's confabulations, and a "deviations" section turns the
    delegate into a check on its author.
  - **WN-ai:** the harness relays the user's message only into workflows
    launched in the same turn as a typed message. Arm 1 received "Go";
    arms 2 and 3 (notification turns) received nothing. This bears on what
    the methods section can say about how purely scripted the scoring
    prompts were; it is provisional (abductive-reasoning, same date).

### 2026-10-04 — Shakedown queue ruled; PRs merged; H13 and gates ruled; Opus 5.5 arm built, probed, approved

One session (c51bef29) on Opus 5.5, with Shawn present throughout, and
about fifteen rulings taken through structured questions. Spend, each
stage API-gated: one blinded H13 agent (about $1–3 API-equivalent) and the
P4 probe (about $0.71 per request; the first attempt cost nothing).

The shakedown queue was cleared. Dye T02 moved from "mechanical" to
**fail-and-uplift** after a CRAN check showed that no public ArchaeoPhases
release runs the published code. Herskind T04, T08, and T11 were confirmed
as PAPER_ERROR; T11 was completed by operator deviation, giving coverage
11/15.

PRs #6 and #5 were merged. H13 matched the tool in every cell but read
"(same statistic)" more strictly. The gates were ruled (majority vote;
BI-excluded admissible, both reported). D4 by rule is `claude-opus-5` @
`high`, held so Opus 5.5 can be validated first.

F-013 and F-015 were fixed, and an args checksum guard added. The Opus 5.5
arm was built, its pre-run review ruled, and P4 passed. The arms were
deferred, then approved at close for the next session.

- Shakedown rulings `b446415`; T11 completion `4bc3200`; fetch script
  `8949da5`; user-obs adjudication `3bddb55`.
- Merges `783f7e2` (#6) and `d92fd30` (#5).
- H13 `976c573`; gates ruling and D4 `6c00a0b`; erratum Entry 5 `6fb1f37`;
  D4 hold and F-013 ruling `ad765b4`.
- Assembler v1.6 and record replay `59d643b`; Opus 5.5 arm `c3cb02d`;
  args guard `c8eca55`.
- Design note `339e09d`, rulings `ca01789`, F-018 `4815a39` (corrected
  `0c5fdb3`), P4 `9553f46`, deferral `171fbb9` and `3b20c71`.
- Reflections `ad538c5`.
- **Working-notes candidates (held for Shawn's verdict):**
  - **WN-ad:** amendment 1's "concordance (same statistic)"
    underdetermines the gate. A blinded reader took four-way unanimity,
    under which no arm is eligible on any BI choice. The tool's majority
    vote (since 2026-08-03) admits opus-5 on the BI-excluded statistic. An
    operationalisation choice can decide a gate outright, so fix it in
    registered text, not in code.
  - **WN-ae:** effort → cost, measured per request. Over 15 scorings,
    opus-5 at `high` cost $17.27 against $19.46 at `xhigh` (−11%), with 36%
    fewer output tokens, even though per-entry totals made `high` look
    larger (F-013). Cache writes are a fixed floor of about $6–7 per arm,
    so effort steps cost only about $1.80 per arm at Opus 5.5 prices.
  - **WN-af:** dye's published section-4 code ran on no public
    ArchaeoPhases release (1.5, 1.6, 1.8 all drop the iteration column).
    The pilot's index repair recovered the intended 72 dates. This is the
    first case of the fail-and-uplift bright line: version pins are
    routine, code edits are not.

### 2026-10-03 (second session) — Agentic lane built and shaken down on herskind + dye; E8-v2 registered; concordance run

One session (4d22016c) on Opus 5.5, with Shawn present until about 22:45
AEST and autonomous overnight close. API spend, each stage gated: $21.14
API-equivalent across three workflow runs. Built the minimal reproduction
workflow (Phase 2 option (a)): plan and execute workflows, a deterministic
lane tool, four schemas, and agent definitions v1.1 pinned to Opus 5.5 at
`high` effort.

Shawn's rulings:

- the run is a pre-gate shakedown, because preregistration §8 and
  amendment 1 place the registered gate after model selection, with a
  Crema leg;
- attempt numbering is confirmed (shakedown = attempt-02; OxCal = dye
  attempt-03);
- the agents are blinded from the pilot;
- R1–R4 planning rulings;
- criterion clarification D1;
- two adjudications.

Plan round 1 was superseded by an orchestrator defect (F-014: the blinding
list collided with the push channel). Round 2 was approved. Execution
reproduced every pilot value and surfaced paper-level errors the pilot had
missed or absorbed. While waiting, registered E8-v2 and ran the six-arm
concordance on a worktree branch. Found and fixed a launcher bug that
blocked every worktree commit. Found the token over-count, F-013.

- PR #5 (`feat/reproduction-workflow`): `98f3eb9` agents; `87c5365` lane;
  `a411e3c` inputs; `7b5e898` plan rulings; `191744b` → `344049d` launcher
  replaced by checksum; `aef79a8`, `26b9a5b`, `b06b1fd` harness fixes;
  `846f8b5`, `4112b2d` register F-013, F-014, F-015; `26344a5`, `56e58aa`,
  `e5f3554` plan rounds and approvals (F-016); `6de3f27` input drift;
  `cfbd79b`, `4e77cec` attempt-02 artefacts; `77e2d50` results and F-017.
- PR #6 (`feat/e8v2-registration`): `c692fb1` launcher `GIT_*` scrub;
  `fd24cf4` E8-v2 reference; `f9de633` analysis v1.2; `6e0d17a`
  concordance.
- Feedback was sent: the Workflow dialog offered only "no" for a scratchpad
  launcher script.
- **Working-notes candidates (held for Shawn's verdict):**
  - **WN-aa:** the coverage denominator moved from 23 to 34 targets for dye
    between plan rounds, with rulings partly responsible (R3 wording). H2's
    denominator is sensitive to wording and run-to-run variation; a
    two-planner reconciliation safeguard is proposed.
  - **WN-ab:** regression against a human-directed baseline also audits the
    baseline. All values were identical, but the agentic run flagged errors
    the pilot had absorbed (dye p.16 re-mapped; herskind Table 1 never
    checked against the paper).
  - **WN-ac:** harness transcripts repeat a response's usage on every
    content block, so per-entry token sums over-count by 1.9–2.9×
    depending on the model (F-013). Measurement apparatus is part of the
    instrument.

### 2026-08-29 → 2026-10-03 — F-010 path rule shipped; E8-v2 worksheet adjudicated end to end

One session (003fda8b) across three sittings separated by Shawn's absences;
model changed from Fable 5 to Opus 5.5 at the 2026-10-01 resume; no API
spend. Shipped the F-010 path rule (reconcile-run v1.5, PR #4, `5ebb6a0`),
then adjudicated the whole E8-v2 worksheet with the registrant, adopting
forward principles AP-1 to AP-17 that were applied to every later section.
Primary-source checks overturned several inherited claims: amendment 2's
precedent DOI was never in the paper (erratum-log Entry 4); crema's version
of record is v1.0.0 by published-values match, not the date rule's v2.0.0;
marwick's open deposit of Web of Science records conflicts with Clarivate's
public terms. Approved mid-session (via agent mail from cv-and-applications):
the Phase 2 regression test, sequenced after the worksheet, for a pitch due
Fri 9 Oct.

- Validation: `6fc45df`, `383e3c6`, `af81640`, `be11750` (F-010); sittings
  `b764b5e`, `c9fee3e`, `e07a2a6`, `0bb03ad`, `7298681`, `8fee957`,
  `45aaa2a`, `6c0c2ec`, `8905c6c`, `7da90bf`; ARR survey `399b86b`; F2
  keywords `6b6d14a`; Clarivate `34fe6a3`.
- Protocol and prereg: `01cd737`, `e3fd5b2`, `cba1d77`, `64f0454`; erratum
  Entry 4 `dfc74ef`.
- Planning: `795caab`, `834b020`, `c53e2ce`, `a10c747` (future-work items
  10 and 11).
- Observations: `8c91342`, `e70fadb`, `87873e3`, pointer `7eb4f96`;
  reflections `2bf6671` (claude-obs 50–53).

### 2026-08-17 (third session) → 2026-08-19 — Analysis tool v1.1 shipped while waiting; ball handed to Shawn

One build sitting (evening of the 17th, session 92427cb5), wind-down on
the 19th. No spend, no rulings — the first pure build-while-waiting
session, run under the standing default ruled at the s2 close. Resumed
at `1a0ae7d` (clean, 0/0, fetch-first); verified 251 tests + 66/66 gate;
built and shipped `analyse-benchmark-disagreements.py` v1.1
(`48568fb`): `--arms` spanning cycles, error-direction split,
`--reference-key`, per-arm guideless reporting, and — found via
ground-truth verification — the two-era guide-detection fix (the
pull-era predicate was vacuous for all 90 post-A3 spawns). Legacy mode
verified byte-identical; six-arm stability pass matched every known
figure. Tests 251 → 267. /reflect + /handoff run at wind-down
(reflections Entry 17, abductive entry, llm-observations entry,
claude-obs 48–49, user-obs A–C pending, WN-y/z pending). E8-v2
worksheet untouched (Shawn's sitting); F-010 open; concordance
deliberately uncomputed pending E8 v2.

### 2026-08-17 (second session) — Effort study end to end: pinning built, six datapoints, opus passes at high

One session (f605c78a), one sitting; 12 commits `3f4cde6`→`5c193e3` +
handoff/reflect commits. Built and shipped effort pinning (launcher
v1.2→v1.3, workflow v1.5→v1.6, assembler v1.4→v1.5, 29 new tests) after
proving the harness drops opts.effort from spawn metadata. Delta
pre-run review ruled Q1–Q7; the session-/effort mitigation died on the
CLI cache constraint and was replaced (operator-accepted) by the P3
differential probe (7.5× output differential = channel verified).
Sonnet@max halted at the boundary (4 unusable items, wire 17.9M/12M;
64K-cap retry churn = 24% of spend) → Shawn ruled completion at cap
128K; key r2 took three attempts; register F-008–F-011 lodged.
Sonnet@high and opus@high both clean first pass. Result: sonnet
0.813/0.853/0.867 (below gate at every effort), opus 0.953 at BOTH
efforts, cost-indistinguishable — Shawn's "is it really cheaper?" catch
corrected the cheapest-configuration headline (`5c193e3`); the contract
metric is a spend wire, not an effort-response measure. Mechanical
quality checker shipped: zero invalid pack_refs / zero A1 violations
study-wide; pack-utilisation separates models (opus ~80%, sonnet
47–57%), not efforts. Corrected the carried study cost estimate 4–5×
upward pre-gate ($80–120 API-equivalent vs $15–25; cache-write premium
+ read volume had been omitted).

**Candidates ADJUDICATED at close (Shawn, same session):** WN-v/w/x all
ACCEPTED → working-notes Observations 27 (artefact-derived effort pins +
channel probes), 28 (composite spend metrics cannot measure effort
response), 29 (harness caps are part of the measurement apparatus).
User-obs s2 batch: A + D accepted (D with the standing
build-while-waiting ruling), B + C dropped.

**Carry-forward:** analysis tool needs `--arms` extension before study
arms join a tool-run; H13 fresh-context re-derivation at gates stage;
F-010 open; 128K cap standing; sonnet intro pricing ends 2026-08-31;
zbook hooks+venv still pending; Shawn's list (Cosmos window, Fable
billing split, Zotero proxy, ELSEVIER key, Marwick duplicates)
unchanged. Prior pending verdicts (2026-08-03 and 2026-08-15 batches)
still held.

### 2026-08-15 → 2026-08-17 — Phase B ruled, amendment 2 lodged, D3 passed by two arms, register born

One session (6e8352ed), three sittings; ~25 commits `f9976fc`→`6b0025c`
+ PR #3 + tag `osf-amendment-2-2026-08-17`; personal-assistant
`0b3a6bd`, pa-data `c96f43e`/`1325b49`. Sitting 1: Phase B + platform
rulings, CTS/re3data enrichment, D1 governed window (instrument v2.1;
guide pushed; C7 hashes), identifier-recovery rule. Sitting 2: PR
merged, prereg register layer, D2 lodged (§6 dissolved on
verification), D3 prep (reconcile/workflow/harvester v1.1s, marwick
deposit recovered live, E8-v2 worksheet). Sitting 3: pre-run review +
codified clean-context audit (5 pre-spend blockers), S4 retreat, three
arms run/adjudicated/accepted (fable at 7.10M with the tripwire event;
wire now remediation-scaled), stability 0.853/0.953/0.947, failure
register seeded, run-environment + telemetry capture, effort
confabulation caught and logged. Full factual log:
`wiki/reflections/session-log.md` 2026-08-15→17 entry.

**Held-over candidates (no silent discard), for Shawn's verdicts:**

- **WN-s:** verifiers encode delivery-mechanism assumptions — a silent
  harness change (additionalContext spilling to files past ~77KB)
  turned 14/15 correct behaviours into flagged violations; a checker
  must model the channel it rides on.
- **WN-t:** schema compliance and attestation integrity are separate
  axes — validator retries 3/1/0 vs receipt incidents 0/0/2 across
  identical contracts; the better the model, the less the validator
  measures.
- **WN-u:** budget tripwires need a legitimate-excess clause and a
  stuck-loop indicator from birth — remediation spend tripped a wire
  that "runaway spend" framing never anticipated.

**Carry-forward:** next session must check `/effort` before launching
any arm (spawns inherit it until pinning lands). zbook still needs
`./scripts/install-git-hooks.sh` + venv. pa-data submodule pointer in
personal-assistant deliberately not bumped (three data commits this
session; PA routines own the pointer). Shawn: Cosmos window OPEN;
Fable billing split; Zotero proxy; ELSEVIER key; Marwick Zotero
duplicates.


### 2026-08-10 / 2026-08-14–15 — Ratification, pre-run review, Phase C end to end

One session (04169f15), three sittings; 25 commits `f3368ff`→`7ba9a45`;
tests 84 → 172; gate 57 → 65 entities. Sitting 1 landed the four
ratification-read consolidations (clause restored; two-rung ladder with
the pack inside rung (i); per-artefact licence-conflict scope;
endpoint/table independence + supplement-row qualification). Sitting 2:
Entry 3 RATIFIED, C7 ruled, `/pre-run-review` on Phase C (ten-hardening
contract), the clean-context Opus audit PoC (4 blockers confirmed — B1
extended to 39/45 inert blocks), C1's eight fix commits, and the three
C2 probes (field names anchored; workflow lane lacks
`last_assistant_message`; consequence absent). Sitting 3: schema v1.1,
unwrap self-check, harvester + five evidence packs, reconcile-run
(C8+C9), the platform-row verification note, and Phase C closure — with
the 45/45 + zero-contamination retro-vindication of the benchmark as
the day's headline. Full factual log:
`wiki/reflections/session-log.md` 2026-08-10/14–15 entry; plan of
record unchanged: `wiki/planning/instrument-clarification-plan.md`.

**Held-over candidates (no silent discard), for Shawn's verdicts:**

- **WN-p:** hook-time gate decisions are advisory in the workflow lane;
  authoritative verification must run post-hoc on completed artefacts
  (measured: probe C collected despite block; 39/45 lag false alarms;
  45/45 retro-validation).
- **WN-q:** platform by-construction entitlements are presence floors,
  not choice floors — and the floors are empirical claims (Zenodo
  82.6% pre-filled default; DataCite tombstone contradiction; dated
  note committed).
- **WN-r:** receipt checks must verify success, not attempts — a
  declared pull whose every Read errored never entered context (dye/
  sonnet guideless spawn; rule now in gate + reconciler).

**Carry-forward:** zbook needs `./scripts/install-git-hooks.sh` after
pull **and a venv** (`python3 -m venv venv && venv/bin/pip install -r
requirements.txt pytest`) — the new commit test gate's fallback needs
jsonschema. Shawn: **Cosmos decision window OPEN**; Fable billing split;
Zotero proxy; `ELSEVIER_API_KEY_TDM`; Marwick Zotero duplicates
(573 + 4151); PA data-submodule inbox flag.

### 2026-08-03 (second) / 2026-08-10 — §2 declined, research-surface rulings, A2 drafted

One session, two sittings a week apart (52a81f4b; renamed
"LLM-Repro-2026-08-06"); twelve commits `b686b6f`→`8521d50` + handoff, plus
personal-assistant `a3f5793`. The §2 card was declined on receipts evidence
gathered before presenting; Shawn chose the instrument-clarification route
(robust instrument over speed-to-census) and, across two sittings, ruled
all eight benchmark-derived decision points — anchored by his
research-surface reframing of the assessment target. Prior-art scout +
adversarial verifier ran the evidence leg (four fabricated quotations
caught; ACM inverted claim converted to a named departure; agent-definition
countermeasure shipped); Marwick and Tedersoo read directly; eleven
verified references staged in Zotero. Phase A closed bar A3: mining pass
verified all published benchmark figures from primary artefacts, and A2's
ten items of drafted operative text sit in erratum-log Entry 3 awaiting
ratification. Full factual log: `wiki/reflections/session-log.md`
2026-08-03/10 entry; plan of record:
`wiki/planning/instrument-clarification-plan.md`.

**NEXT (in order):** (1) Shawn's ratification read of erratum Entry 3's
drafted text; (2) Phase C build — audit fix round 2, schema v1.1 (+
provenance flag), C6 harvester, C7 GOVERNED decision; (3) A3 + D1
consolidation → lodge amendment 2 → re-benchmark; (4) Phase B reference
re-derivation design (entailed, needs Shawn's shape decision).

**Carry-forward:** zbook still needs `./scripts/install-git-hooks.sh` after
pull. Shawn: Fable Max-vs-API billing split check still open; Zotero-proxy;
`ELSEVIER_API_KEY_TDM` still absent; **Cosmos decision window now open**
(~1 month from 2026-07-21 submission). New this session: lit-scout may want
the same quotation-claim rule (deferred pending evidence); COPE case URL
unverifiable by automation (browser-check before ever citing); Marwick 2017
now has duplicate Zotero items (573 + 4151, merge when convenient);
`published/agents/prior-art-scout.md` drift picked up at next `/retro`.
Pending verdicts: see the 2026-08-10 repo-state block.

### 2026-08-03 — Lodgement, monitoring 0–3, benchmark, two audit rounds

One very long session (0360402e); ~28 commits `a208f9d`→`9f67480` + tag
`osf-amendment-1-2026-08-03` + reflections/handoff. Task E closed:
E2 re-check, crema "missing assessment" dissolved (pre-v2.6 key), prose
re-expression promoted, §5 cross-vendor pre-declaration added, lodged via
the OSF API as registration Version 2 (DOI unchanged). PR #2 + cascade
merged; monitoring §9 resolved and Phases 0–3 shipped same day. Benchmark
ran per amendment §3 (45 spawns, 4.25M tokens, ≈$27): all arms below both
gates, item-structured — the §2 remediation decision is deliberately
parked for next session. Two audit rounds: fix pass 3b01676 (tests
48→84), re-audit found regressions in the fixes; everything registered in
audit-2026-08-03-follow-ups.md. Full factual log:
`wiki/reflections/session-log.md` 2026-08-03.

**NEXT (in order):** (1) Shawn's §2 decision (routing-fix candidate:
uniform push of fair-principles-guide) → possible single re-run via the
rescued workflow script; (2) audit fix round 2 + schema v1.1 — both
PRE-CENSUS; before the census the gate needs one captured SubagentStop
event and one live pass-plus-catch demonstration; (3) C7 GOVERNED
decision; (4) monitoring Phase 4; (5) census frame.

**Carry-forward:** zbook must run `./scripts/install-git-hooks.sh` after
pulling. Shawn: check Fable Max-allocation vs API billing split after this
session's ~1.4M Fable tokens; Zotero-proxy investigation;
`ELSEVIER_API_TDM` key still absent; Cosmos watch ~mid-August. Pending
verdicts listed in the 2026-08-03 repo-state block.

### 2026-07-27 (second session) / 2026-08-02 — Verdicts cleared, corpus list closed, monitoring planned

Two sittings on amd-tower off the 2026-07-27 resume prompt; seven commits
(`640ffbb`→`8a4e946`) plus PR #2 opened and deliberately held. **Sitting one:**
all four held-over verdicts cleared — WN-h/WN-i accepted as working-notes
Observations 16–17 (drafted against sources first, since only one-line summaries
existed), user-obs A–C held again, Opus-5 arm confirmed and a Fable 5 arm
authorised, provenance paragraph deferred to the lodgement read. Fable 5 agent
definition *generated from* the Opus 5 file and diffed rather than transcribed —
which caught a `sub-principle`→`sub principle` defect the hand-written attempt
had introduced. Corpus items 5 (fetch-with-checksum, destinations, Materials
Acquired table) and 6 (schema v2.7, PR #2) closed the corpus build list.
**Sitting two:** walked a returning collaborator through two findings and
corrected one of them; fixed the orphaned commit hashes; drafted the monitoring
plan; named the Fable arm in amendment §3, closing task E1.

**Findings.** The D5 gate's version check covers **7 of 25** registered entries
(`check_canonical_entry` iterates `shared_content` only) — found by probing this
session's own change with a deliberately wrong version. Backticked commit
references: **115 resolve, 21 do not**, all 21 in `wiki/`; 3 remapped by exact
message match, 18 outstanding.

**Correction.** The `assessment_json` "genuine mismatch" escalated on 2026-07-27
was a measurement error, not repo drift — `1.1` (payload `schema_version`) and
`2.1` (document version) are different axes, both correct. Withdrawn 2026-08-02
with evidence; a manifest note now prevents the next reader "reconciling" them.

**Decisions (Shawn, 2026-08-02):** widen the gate so every registered entity is
checked hard, reorganisation acceptable; add the Fable arm to the lodged
amendment text; billing route settled (Max-plan first, API account for excess,
ordinary API review gate before the run); PR #2 held until after lodgement.

**NEXT:** task E — E2 (§1 consistency check) and E3 (paste artefact) are
Claude's; E3 follows Shawn's read, not precedes it. Then PR #2 plus the prompt
cascade as one change; then monitoring Phase 0.

**Carry-forward:** user-obs candidates A–C (2026-07-27) **still held and
un-adjudicated** — carried a second time. Of the 2026-08-02 batch, F accepted,
D and E discarded (Shawn, 2026-08-02). Working-notes candidates WN-j/WN-k
**accepted** as Observations 18 and 19. zbook must run
`./scripts/install-git-hooks.sh` after pulling. Shawn: Zotero-proxy investigation; `ELSEVIER_API_KEY_TDM` still absent
from `~/personal-assistant/.env`; Cosmos watch ~mid-August.

### 2026-07-24 (second session) — Phase 1 build queue executed; amendment drafted

Single autonomous session off the resume prompt. Four build-queue items + the
amendment draft, five commits (`b1aab17` D5 gate → `18cb659` instrument canon
→ `de175d3` agent definitions → `115d202` production hooks → amendment/
continuity commit): D5 consistency gate (pre-commit-wired, block-tested,
17 unit tests incl. §3.3 model-pin and §3.9 memory-prohibition checks);
instrument canon to 7 registered entries (five new canonical files + the
adversarial framework promoted pull→push; reproduction SKILL.md became a
second machine-checked mirror); five agent definitions with pinned models
(claude-api reference confirmed Sonnet 5/Opus 4.8 have no dated snapshot IDs
— the aliases are the exact IDs; reproduction-lane pins provisional
`claude-opus-4-8` pending the validation benchmark); production hooks
(manifest-driven push + receipt log, receipt gate with model_id hard gate and
transcript-verified pulled reads, PreToolUse pre-flight; 17 synthetic
pipe-tests). OSF amendment 1 drafted at
`prereg/amendment-1-draft.md` from the ratified scope — lodgement deferred to
just before the validation phase per Shawn's timing call. One mid-session
rebase over a parallel session's handoff commits (the 2026-07-22/24 entry
below landed while this session ran).

**NEXT:** Phase 1 remainder per the repo-state bullet — census screener,
output schemas + workflow scripts, corpus items 5–6; amendment lodgement then
validation phase.

**Decision pass (Shawn, 2026-07-24, same session, all seven queued decisions
resolved):** (1) reproduction-lane model pins stay provisional (Opus 5
expected imminently; real selection at the validation phase — rationale
recorded in the manifest comment); (2) fair-assessor Fable 5 variant deferred
— authored only when Shawn approves the Fable benchmark run (billing route
decided then); (3) amendment-1 draft gets one read, at lodgement; (4) all
three build judgement calls RATIFIED (env-levels co-location, invariants to
all three reproduction agents, SKILL.md mirror); (5) WN-a–g ALL ACCEPTED →
working-notes Observations 9–15; (6) user-obs candidates A–C ALL ACCEPTED —
C makes confidence labels on external-system predictions a bilateral
standing rule; (7) MQ TDM enquiry DROPPED (rely on Zotero-proxy route +
Elsevier support-email fallback). Parallel session confirmed finished, no
conflict.

**Carry-forward (pruned):** Shawn: Zotero-proxy investigation, amd-tower
`.env` key; Cosmos watch ~mid-August; PA data-submodule unpushed inbox
commit (PA session to sweep); zbook: re-run `./scripts/install-git-hooks.sh`
after pulling (hook now includes the D5 manifest gate).

### 2026-07-22/24 — Review cascade; corpus infrastructure; Phase 1 opens

Three-day amd-tower session (remote-controlled from campus days 2–3; four
zbook paper-b commits rebased over mid-session). **Day 1:** routing-design
review passes run + adversarially verified (110/110 clean); Pass 6 instrument
defects found in the OSF-frozen copy and fixed (`abdc526`); erratum log
started (`f4dfa0e`, Shawn-approved accumulate-then-amend path); reports
externalised (`c9a6ecd`); model-testing decisions recorded (three-model
spot-check; Sonnet 5 + Opus 4.8 on Max first; ask-before-Fable;
Sol arm later). **Day 2:** design v0.2 (`3914f81`); corpus implementation
scoped (`edf7f56`); zbook synced. **Day 3:** §9 workflows added (v0.2.1,
`74e7ed9`, from Shawn's review question); pre-build juncture
/review-implementation (his request) found 12 defects incl. one critical
compliance catch (§2.2 ladder = prereg deviation) — all cheap fixes applied
(v0.2.2 + corpus v0.2.1 + ratified amendment scope queued in erratum log,
`3080022`); **Shawn SIGNED OFF v0.2.2 and confirmed corpus decisions**
(`01fd8d4`); corpus census blockers EXECUTED (`fbf477c`: store 16 papers /
71.7 MB verified, manifests, fetch-corpus.py, LFS narrowed, corpus gate
tested, first QNAP sync); **Phase 1 opened** — D-2 spike PASSED, engine =
workflows, FAIR instrument extracted to canon (`25d1c0d`); Elsevier trail
diagnosed to unresolved key-provisioning failure, Zotero-proxy now the
probable route (`c903b89`…`5b77b78`); migration script archived (`cb7a24c`).
Reflections + claude-obs 19–21 written at close.

**NEXT:** (1) build queue per the Phase 1 bullet (D5 consistency script
first); (2) draft the consolidated OSF amendment from the ratified scope
(lodge just before the validation phase — Shawn's timing call); (3) Shawn:
Zotero-proxy investigation, amd-tower `.env` key, MQ TDM enquiry optional;
(4) Cosmos correspondence watch ~mid-August.

~~**Held over pending Shawn's verdicts (no silent discard):**~~ [x] 2026-07-24
ALL RESOLVED in the second session's decision pass: WN-a–g all ACCEPTED
(now working-notes Observations 9–15); user-obs candidates A–C all ACCEPTED
(C → bilateral confidence-label rule). Original hold-over text: working-notes
candidates WN-a/b (2026-07-18) + WN-c/d/e (2026-07-21) — still owed — plus
NEW this session: WN-f (docs-vs-harness canary-probe method: settings-hook
canary + control/test spawns settled in 20 s what three doc citations
mispredicted) and WN-g (reliability-gate statistics: n=90 gives ~12%
false-pass at true 0.85, halved by all-five pilots; agreement definition
shifts the 0.90 gate across 10–30% item-flip rates; model ranking
structurally unavailable pre-census). User-obs candidates for 2026-07-24
written to `wiki/user-observations.md` (pending review).

### 2026-07-20/21 — Prereg LODGED on OSF; Cosmos application SUBMITTED

amd-tower session, two days. Preregistration lodged by hand (browser extension
unavailable; Claude supplied verified paste artefacts): project-flow lodgement
dodged the standalone form's five-file cap; paste files unwrapped to flowing
lines (`f2f467a`) after OSF text boxes rendered breaks literally; §10 power
table pasted as pipe soup — accepted, tables now banned from paste-field
content (`6577119`, README + convention memory). Lodged WITH embargo
(double-blind contingency); journal-policy agent found no candidate venue
requires it (JAS:R dropped its mid-2024 mandate); embargo lifted, registration
public, **DOI 10.17605/OSF.IO/DQNHG** (`13261c1`). Cosmos application then
driven v0.4→v0.7: registration alignment, CV-verified credentials, two-pass
claim verification (PA-hub ledger `ef8a6cb` reconciled against a clean-context
adversarial agent — three ledger pointer errors and six wording drifts fixed),
Shawn's body revision tightened 566→498 in we-voice, all fields selected
(statement-of-mission title; merged one-liner; two-sentence self-pitch and
parity-length Brian entry, preregistration claims deflated to "argued the case
for"). Live form differed from the 2026-07-07 capture (links-only
additional-info field; multi-file CV upload) → evidence pack published at
`docs/cosmos-evidence-pack.md`; paste file + committed generator
(`build-cosmos-form-paste.py`) keep form text and verified draft in lockstep.
**SUBMITTED 2026-07-21** (`f9c14b0`), US$8,000, five days ahead of deadline.
Reflections + claude-obs 15–18 written (`f7450dc`).

**NEXT:** (1) weekend run: FAIR reliability spot-check + pilot regression gate
(pilot papers only; prereg-safe); (2) routing-design review passes
(/review-implementation + prior-art-scout) → v0.2; (3) corpus-management
implementation before census; (4) watch for Cosmos correspondence ~mid-August;
(5) census sweep once gates pass.

**Held over pending Shawn's verdicts (no silent discard):** working-notes
candidates WN-a/WN-b (2026-07-18: xelatex glyph-drop hazard; emphasis-stripping
fixpoint) plus NEW WN-c/d/e (2026-07-21: paste-surface conventions;
external-fact half-life — the JAS:R policy drift; verification ledgers drift
from sources) — WN verdicts still owed. ~~user-obs candidates 1–8~~ [x]
2026-07-22 ALL RESOLVED: 1–5 and 7 accepted (7 elevated to a standing
default: interface-shaped paste artefacts for any web-form output; riders on
1 and 2: critical-friend pushback on domain judgements stays welcome; hold
ground when pushback is off-base), 6 and 8 discarded.

### 2026-07-18 — Prereg v0.3→v0.7 lodgement-ready; OSF materials; authorship posture

Shawn returned (Paper B finished on the train) and final-reviewed the prereg
through four revision batches; everything committed and pushed; lodgement is
the morning of 2026-07-19. Version chain (all 2026-07-18):

- **v0.3** — nine decision-point resolutions applied (D3 → 168 h on named
  hardware + archived-intermediates partial path; others as drafted).
- **v0.4** — census window start → 2022-01-01 (two full pre-policy years;
  H1b parallel trends partially checkable; power table recomputed, δ ≈ 0.28
  at 80/80); H5 + credibility lane reclassified pre-specified exploratory;
  *Reports* control census option via cost gate.
- **v0.5** — credibility outputs constrained to descriptive structural
  metrics; availability taxonomy → six friction-ordered levels (machine
  boundary L2/L3, discretion boundary L3/L4; "on request" split from
  archive registration; standardised L4 request protocol); sampling-cap gate
  clause; pre-specified descriptive reporting block; R-only limitation
  sharpened (Marwick-adjacent oversampling caveat).
- **v0.6** — H5 gains two schema-verified RDMAP metrics (implicit-status
  proportion; expected-information gaps); L4 window → 3 weeks + late-response
  clause; credibility signals computable internally with aggregate-only
  reporting (per-paper scores never published); FAIR4RS named as
  amendment-path extension; FAIR×coverage estimation added; human-validation
  wording fixed (one instrument, data + code applications).
- **v0.7 + pilot report v1.2** — LLM removed from authorship per
  journal/university policy: report has sole human author + §10 LLM-use
  statement (v1.0–v1.1 correction recorded in-document); CITATION.cff and
  codemeta author fields cleaned (tooling disclosure retained in
  runtimePlatform/softwareRequirements); git Co-Authored-By trailers stay
  (Shawn confirmed — VCS provenance, not scholarly authorship).

Lodgement materials (`studies/open-science-compliance/prereg/`, convention
transferred from `~/Code/inscriptions/wiki/prereg/`): plain-prose summary
(4,347 words, emphasis stripped to fixpoint), glyph-verified PDFs of prereg +
pilot report (DejaVu fonts — Latin Modern silently dropped α/δ/≤; verified by
pdftotext), README with regeneration recipe + lodgement checklist. Study
protocol and Pass 6 prompt upload as markdown only (✅/❌ glyphs drop silently
under xelatex). Upload set: 4 canonical .md + 2 PDFs at `ee3fda3`; commit
hash goes in the OSF project description; tag `osf-prereg-phase2-<date>`
after submission. OSF approach memorised (memory `2026-07-18-10b38c994a0a`);
Quarto-workflow discussion captured to PA inbox for a future session.

**NEXT:** (1) lodge on OSF (morning 2026-07-19; checklist in prereg README);
(2) Cosmos application remaining fields + link the live registration
(deadline 26 Jul); (3) weekend run: FAIR reliability spot-check + pilot
regression gate (pilot papers only — prereg-safe before and after lodgement);
(4) routing-design review passes (/review-implementation + prior-art-scout);
(5) corpus-management implementation before census.

**Held over pending Shawn's verdicts (no silent discard):** working-notes
candidates WN-a (xelatex silently drops out-of-font glyphs — meaning-inversion
hazard for instruments; verify builds by text extraction) and WN-b
(markdown-emphasis stripping needs fixpoint iteration — nested/line-wrapped
spans survive one pass); ~~user-obs candidates 1–4 in
`wiki/user-observations.md` (pending review)~~ [x] 2026-07-22 all four
accepted (with riders; see user-observations.md).

### 2026-07-15/16 — All prereg decision points resolved; content-routing design v0.1

amd-tower resume session, closed for machine swap to the laptop (train). All nine
preregistration decision points resolved with Shawn:

- **D1** sole registrant + LLM disclosure in Summary §8. **D2** cutoff 2026-06-30,
  **D4** 15–25 band, **D5** per-hypothesis families (Holm only within H1a's pair),
  **D6** availability taxonomy, **D8** *Reports* 120/60, **D9** n = 12 — all confirmed
  as drafted.
- **D3 REVISED:** compute cap raised 48 h → **168 h wall-clock on named reference
  hardware**, with the archived-intermediates/table-regeneration partial path written
  into §5 criterion 4 (over-cap papers scoped down via archived posteriors, not
  excluded). Rationale: ad-hoc drops would systematically exclude Bayesian/MCMC papers
  — exactly H4's stochastic side.
- **D7** reliability checks + 0.90 threshold confirmed (= §9 items 1–2).
- Verdict-capture caveat: D3, D7, and §9 items 4–5 arrived via rejected
  AskUserQuestion dialogs (provisional but consistent; D7 twice) — reconfirm wording
  when applying the draft edits.

§9 verdicts thereby all delivered (see repo-state bullet). Item 3 resolved by the new
`wiki/planning/agent-content-routing-design.md` v0.1 (`10947aa`): embed role behaviour
/ push instruments with read receipts / pull pattern libraries. Shawn's design brief:
reliability first, duplication acceptable if split cleanly; read receipts definitely
in. Discussion en route covered pull-miss risk calibration (low per-call, silent,
non-trivial at census scale; stability checks don't catch a consistently-wrong scorer
— the n = 12 human subsample does).

**NEXT ACTIONS (laptop):** (1) apply D1–D9 resolutions to the prereg draft and close
its decision table; (2) run `/review-implementation` + prior-art-scout against the
routing design → v0.2; (3) lodge prereg on OSF; (4) Cosmos remaining fields (deadline
26 Jul); (5) corpus-management implementation before census. PA data synced for the
swap (data `38b78d3`, pointer `183d5e0`). Interaction lesson recorded in the PA
scratchpad: don't pair substantive prose with an AskUserQuestion dialog in one turn —
the prose may not render.

### 2026-07-14/15 — Prereg drafted + stress-tested to v0.2; identity fix; amd-tower sync

One-day session on zbook, closed for machine switch to amd-tower. Phase 2 OSF
preregistration drafted (v0.1 `9405182`) then stress-tested via
`/review-implementation` and revised to v0.2 (`885e664`) — see the repo-state
bullet for the full change list; nine decision points open. Author-identity
confabulation corrected across public metadata and living docs (`38adf36`).
amd-tower brought into sync (quarantine + fresh clone + verified asset rsync;
repo-state bullet has gotchas). Also: prereg v0.1 commit `9405182` includes the
seven-decision table later superseded by v0.2's nine.
~~**Held over pending Shawn's verdicts (no silent discard):**~~ [x] 2026-07-15
all verdicts returned same session: WN-a and WN-b both ACCEPTED (now
Observations 7–8 in `wiki/working-notes.md`); user-obs candidates 1–3 all
ACCEPTED (pending marker cleared). Follow-on question from Shawn: is
`/review-implementation` fit for purpose for study-design reviews, or does it
need a checklist update? Assessment delivered 2026-07-15: protocol phases
generalise; a "Study Designs and Preregistrations" domain checklist is the
gap (circularity, criterion contamination, post-treatment conditioning,
wording-vs-test match, counterfactual presence, pre-specification
completeness, blinding, instrument validation, power-as-estimation) —
APPLIED 2026-07-15 to the canonical skill (personal-assistant `5b76a87`,
`skills/review-implementation/SKILL.md`; live everywhere via the
sync-symlinks convention — canonical skills in personal-assistant
`skills/`, symlinked into `~/.claude/skills/` by
`scripts/sync-symlinks.sh`; amd-tower gets it on next pull/cron sync).

### 2026-07-07/14 — Verified stack sweep, Cosmos evidence, licence purge, corpus plan

Eight-day conversation (compaction 2026-07-08; two usage-limit interruptions).
Full detail in `wiki/reflections/session-log.md` (2026-07-07/14 entry); highlights:
19 verified scout reports + synthesis (P1–P6, S1–S2, C1–C3, G1) with the
speed-to-publish competitor finding; eleven Zotero staging collections; three
scout-agent patches (author gating, arXiv handling, injection defence); Cosmos
draft v0.3 + field-19 evidence pack; framework-paper and corpus-management plans
externalised; working notes Obs 5–6; OA audit → `git filter-repo` purge of two
copyrighted files (Shawn pushed; remote verified clean; backup + commit-map at
`~/Code/repo-backups/llm-reproducibility-pre-purge-20260713/`); Marwick CC BY
preprint downloaded. Held-over gates: none new — queue is Paper B → OSF prereg →
§9 verdicts → corpus implementation → Phase 1. No unreviewed working-note
candidates (Obs 5–6 written and pushed).

### 2026-07-03/06 — Revival: modernisation plan, wiki migration, tasks A-C closed

Project revived after the February pause (one conversation spanning four days,
Shawn intermittently AFK). Three parallel explorers mapped repo state: the JAS
pilot is COMPLETE (5/5 papers, 4 SUCCESSFUL / 1 PARTIAL reproductions; headline
finding: data availability, not code availability, predicts reproduction
outcome). Wrote the agentic modernisation plan and took two structural
decisions with Shawn: **study shape Option A** (OSF preregistration first →
JAS 2023-2026 FAIR census as sampling frame → preregistered confirmatory
reproduction subset) and **docs/ stays at repo root** (wiki/ = process record;
convention promoted to the PA template in a parallel session). Executed the
wiki-layout migration (task B), untracked the committed venv (task A), fixed
lossy de-hyphenation with a frozen-dictionary heuristic (task C; 32/32 tests),
reconciled all stale metadata to v3.0.1, and refreshed README/CHANGELOG.
**Phase 1 build of the modernisation plan is ON HOLD by explicit instruction**
until Shawn reviews the plan. Gotcha for future revivals: the local clone was 8
commits behind origin at session start — fetch before characterising repo state.

- Commits: `11f5734` (metadata reconciliation), `bab66ce` (modernisation plan),
  `5440d12` (venv untrack), `8845a45` (wiki migration), `245d820` (task C fix),
  `3c7313c` (README/CHANGELOG refresh), plus session-close commits
- Key docs: `wiki/planning/agentic-modernisation-plan.md` (v0.2, Option A
  recorded in §6); `extraction-system/scripts/pdf_processing/affix-joined-words.txt`
  (frozen dictionary, regeneration command in header)
- Memories saved: study shape (2026-07-04-856141514e0f), repo-layout convention
  (2026-07-04-e6d2685b35b4), build-on-hold (2026-07-04-f24eccedb145)
- Handoff verdicts (Shawn, 2026-07-06): both working-notes candidates ACCEPTED
  (now Observations 3-4 in `wiki/working-notes.md`); user-obs candidate 1
  accepted, candidates 2-4 discarded. Nothing held over.

### 2026-07-05 — Cosmos grant application framing externalised

From a personal-assistant hub session (cross-repo candidate evaluation deliberately run
there, not here). Decision: this repo is the basis for the Cosmos Institute grant
application (AI x Truth-seeking track, deadline 26 Jul 2026). Full record — grant facts,
portfolio proximity scan (186 grantees, no overlap; Metalens is complementary), pitch
framing (reproduction + FAIR lanes with a sampled human-verification surface; extraction/
credibility lanes as frame and track record, not deliverable), and a brainstorm-grade
budget section — in `wiki/planning/cosmos-grant-application-framing.md`. Also indexed the
agentic modernisation plan + the new doc in `wiki/planning/README.md` (the former was
missing from the index).

### 2026-06-10 — de-hyphenation defect logged (task C)

From a paper-b AB+ co-design session (no code changes to this repo). Building
the first AB+ entry surfaced a lossy-de-hyphenation defect in `_dehyphenate`:
genuinely-hyphenated compounds broken across a line before a lowercase letter
(e.g. `self-\ncorrection`) lose their hyphen in the canonical matching key,
breaking otherwise-valid quote checks. Logged as **pending task C** with a
re-verifiable concrete case and a fix direction. Shawn asked for this to be
recorded here for a proper fix later; paper-b proceeds with the
quote-from-extracted-text + display-cleanup workaround for now.

### 2026-06-07 — seed created

Created this `wiki/continuity.md` as the seed of the wiki migration, from a
session centred on the paper-b repo (matching-grade PDF extractor, merged here
as **PR #1**, `1c4650e`; 24/24 tests; validated on real PDFs). Logged the two
pending infrastructure tasks: untrack the committed `venv/` (2,114 files) and
migrate docs to the wiki layout. No other changes to this repo in that session
beyond PR #1.
