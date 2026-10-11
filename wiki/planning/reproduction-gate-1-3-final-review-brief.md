---
title: "Reproduction lane gate 1.3 — final review brief"
tags: [reproduction-lane, review, gate-1-3]
created: 2026-10-11
updated: 2026-10-11
status: active
---

# Reproduction lane gate 1.3 — final review brief

**From:** Claude (Opus 5.5, opus lane), 2026-10-11, orchestrator of the run.
**Repository:** llm-reproducibility, `main`.
**For:** Astra (GPT, Codex) and Fable (Claude Fable 5; top-tier credit, so
Shawn starts it).

This is the final review that the gate 1.3 specification requires
(`wiki/planning/reproduction-gate-1-3-design.md` §2.2): one review per
reviewer of the built gate, against the specification and its acceptance
tests (§13), with one real pilot re-run through the whole lane. "A final
round with no D or A finding closes the hardening" (§2.2), and the gate then
goes on to the §8 regression run.

## What to review

- **The built gate as merged.** PR #7 merged on Shawn's instruction on
  2026-10-11 (`3be8313`) before this review, so the review is post-merge.
  Any fix lands as a follow-up pull request (PR).
- **`306181f`, unreviewed by anyone but its author.** It adds package
  repository dates to the executor (v1.6) and
  `.claude/skills/reproduction-assessor/references/dockerfile-patterns.md`.
  Question: is "an authors' own container keeps its image's snapshot date"
  the right reading of amendment 3 §7(d)'s "a container image can pin the
  runtime and a package snapshot date"?
- **The pilot re-run**, herskind-riede-2024 attempt-03, described below.
- **§16 question 6** (run-time texts), now with run evidence.

## The pilot re-run

Run configuration:
`studies/open-science-compliance/outputs/validation/gate-1-3-pilot-rerun/run-config.yaml`
(the shakedown's settings: effort high, rulings R1 to R4; the shakedown's own
attempt-02 added to the blinded paths). Shawn approved each stage at the
Application Programming Interface (API) review gate and approved the plan
(`plan-approval.json`, plan sha256 `89f2c937…`).

| Stage | Workflow run | Launch commit | Agents | API-equivalent | Audit |
|---|---|---|---|---|---|
| Plan | `wf_14d5db9b-bed` | `ad03008` | 1 planner | $1.21 | clean |
| Execute | `wf_7c18dfdc-298` | `cd5d54a` | executor, Haiku gate relay, reviewer | $12.73 | not clean (F1, F2) |

Artefacts are committed at `78137fe`:
`studies/open-science-compliance/outputs/herskind-riede-2024/reproduction/attempt-03/`,
with the audits and the human queue beside the run configuration.

**Outcome.** Verdict SUCCESSFUL, coverage 17 of 20. The authoritative gate
(`check-attempt --launch-commit cd5d54a…`, `gate-report.json`) passes with
no errors and no flags. The review is QUALIFIED and supports the verdict.
The executor escalated two PAPER_ERROR calls, Table 1's eight off-by-one
cells and two of Fig. 4's 291 hand-drawn boxes (F13–C5 and B2–B1). Both
match the shakedown's findings and the correction ledger's HER-T04, so a
blinded run found them again. They are Shawn's to confirm, not the
reviewers'.

## Candidate findings from the run

Classified provisionally under §2.1; reclassify freely.

- **F1 (D): the transcript audit reports four false hard failures.**
  `transcript-audit.json` lists four "contaminating" findings; all four are
  parsing errors in the executor's shell commands, at these transcript
  timestamps:
  - 11:21:28Z, `run-container --help`: counted as a run that left no
    record;
  - 11:35:34Z and 11:47:01Z, `awk -F, 'NR>1 && …'`: the `>1` inside a
    quoted awk program is read as a redirect, so "a shell command wrote
    outputs/run-01/files/1" and "wrote 1 after the final run";
  - 11:52:21Z, a Python heredoc containing `>=`: read as a write to `=`.

  The parser ignores quoting and heredoc bodies. Amendment 3 §8 makes a
  hard failure unwaivable by ruling, so as built a clean run fails the §8
  code-integrity criterion.
- **F2 (D): the receipt check misses reads made through Bash.**
  `audit-run` marks both Opus agents' receipts INVALID ("declared pull not
  in transcript"). The executor read every declared file in full with `cat`
  (templates by glob), which the check does not count. Two declared reads
  were partial (`data-availability-taxonomy.md` by `sed -n 21,70p`, and the
  reviewer's `verdicts-and-precision.md` by `sed -n 15,120p`), which a
  correct check should flag.
- **F3 (A?): the user's launch message reaches every spawn and outranks the
  workflow.** The harness relays the triggering user message first, with
  "Where the computed task conflicts with this request, this request wins".
  The planner received Shawn's "I assume you're using my max account?" and
  returned it as an approver question. An ordinary launch message that
  mentions an expected result would unblind the executor and the reviewer,
  and nothing records it as a blinding event. `audit_agent` reads the
  prompt (`first_user_text`, which joins the relayed message and the
  computed task) only to find the paper and the Provenance line; it does
  not scan it against the blinded terms.
- **F4 (A?): a method change after the plan's approval passes the gate.**
  The reviewer found that the executor replaced T06's approved method (a
  frequency > 2 lookup) with a criterion inferred from the caption, after
  viewing the published figure, without re-approval. The gate compares
  element counts, not methods.
- **F5 (B or §14): evidence the reviewer could not reach.** The Docker build
  log is not in the artefact set, so `environment.md`'s build claims
  (tarball hashes, one build) cannot be checked from artefacts. The lane's
  injected `.Rprofile` hook is not in the artefact set, so the reviewer could
  not confirm it is computation-neutral.
- **F6 (operability): transcription order.** Published values for Figs 2, 4,
  and 5 were transcribed after the reproduced values were known. The
  reviewer judged the risk limited, since the tools that read Figs 2 and 4
  use no reproduced data.
- **F7 (D, documentation): runbook order.** `reproduction-system/workflows/README.md`
  step 10 runs `persist-results` before `audit-run`, but `persist-results`
  requires the `transcript-audit.json` that `audit-run` writes.
- **Worked as designed.** The two `host-run` flags (figure-reading tools run
  on the host) and the four obligations (dynamic evaluation in the
  Dockerfile and wrapper, wrapper semantics, run-time texts) reached the
  human queue as specified, and the reviewer discharged all four
  obligations with evidence.

## §16 question 6, with run evidence

The re-run left one `run-time-texts` obligation listing 107 texts, as the
dry run predicted. The reviewer traced them to the authors' own filter
strings, `paste(strsplit(skipgram, ' ')[[1]], '== 1', collapse = ' & ')`
at `S2.R` line 367, evaluated in `filter()` at line 368. It matched their
count to the 107 unique skipgrams in the published Fig. 3. The package-text
templates raised nothing.

## Reply

Astra by agent mail; Fable by agent mail or SendMessage; never on GitHub.
Start with your lane, the date, and the commit reviewed (`78137fe` or
later). Classify each finding as D, A, B, or C, and give the ordinary
sequence of actions for an A.
