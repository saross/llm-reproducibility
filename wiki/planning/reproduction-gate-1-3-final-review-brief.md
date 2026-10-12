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
match the correction ledger's HER-T04 and its evidence, so a blinded run
found them again. They are Shawn's to confirm, not the reviewers'.
*Corrected 2026-10-12 (Fable's review):* the Table 1 cells match the
shakedown's agentic result; the Fig. 4 boxes match the operator's
`t11-completion` run, which the ledger cites, not the shakedown agent's
(its T11 was WITHIN_PRECISION, 32 of 32 boxes). The re-run found them by
departing from its approved T06 method (F4).

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

  The parser ignores quoting and heredoc bodies. Amendment 3 §9 makes a
  hard failure unwaivable by ruling, so as built a clean run fails the
  code-integrity condition of the registration's §8 gate. (*Corrected
  2026-10-12, Astra's review:* the brief first said amendment 3 §8.)
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

## Review outcome (2026-10-12)

Both reviews are in, and both find that the round does not close the
hardening (§2.2): Fable's (Claude Fable 5.1,
`~/agent-mail/claude/outbox/claude/20261012T032928.805148Z-claude-gate13-final-review-fable.md`,
with two scripts beside it) and Astra's
(`~/agent-mail/codex/outbox/claude/2026-10-12-codex-gate13-final-review.md`,
probes under `~/agent-mail/codex/review-evidence/2026-10-12-llmr-gate13/`).
Both reviewed `main` at `8b8b4d8`. Neither found a D or A that needs a paid
run to fix or to test; one pilot re-run follows the fixes, because A-new-1
changes what executors are told to write.

| Finding | Fable | Astra | Closure, in short |
|---|---|---|---|
| F1 transcript audit's false hard failures | D | D | Shell-aware parsing (quotes, heredoc bodies, working directory); `--help` and other non-executing lane calls are no run; real redirects stay caught; re-audit the pilot's transcript, never waive |
| F2 receipt check misses Bash reads | D | D | Count complete Bash reads (globs, spill files); report partial, truncated, failed, and grep-only reads; the live hook's ESCALATE passthrough must not skip the check |
| F3 relayed launch message | A | A | Record the relayed text separately in the audit; raise an issue unless it is a fixed, reviewed launch phrase |
| F4 method change after approval | A | A | Per-target method-deviation field and flag for a ruling; the reviewer compares each method with the plan; a plan-against-ledger check at approval for §8 |
| F5 build evidence | B | A | A lane-owned `build-image` that keeps the build log and computes the Dockerfile label; absent evidence is an open issue |
| F5 hook access | D | D | Give the reviewer the commit-bound `reproduction-system/runtime/hook.R` and its neutrality evidence |
| F6 transcription order | operability | A risk | Flag writes to published-values files after the first run; source-only transcription where practicable |
| F7 runbook order | D | D | Audit before persistence, in the runbook and the execute workflow's closing message |
| A-new-1 parse-and-evaluate statements are self-reported (Fable; verified by a lane run: an altered statement passed as `identical`) | A | — | A lane-owned evaluator in the hook binding each evaluated statement to a parsed one: altered fails, skipped and tolerated are flags |
| F8 / D-new-1 admission ignores the workflow audit and the review and escalation queue | D | D | Bind admission to a clean audit, the required roles, and recorded dispositions; `human-queue` lists the full set |
| F9 declared element counts not compared (Astra) | — | D | Compare the plan's `n_values` with `values_compared`; a shortfall cannot be credited in full |
| D-new-2 runbook still describes gate 1.2 | D | (stale) | Rewrite `reproduction-system/workflows/README.md` for gate 1.3 |
| D-new-3 smaller documentation defects | D | — | `dockerfile-patterns.md` snippet never passes `repos = SNAPSHOT`; `01-preparation.md` host `parse` instruction; Haiku 5.5 unpriced in the run configuration |

**`306181f`.** Both accept the reading. Add the cases it does not cover: an
unversioned image tag pins no date; an authors' `repos` override to a
floating mirror leaves those packages unspecified; a GitHub-only package
with no releases takes §7(d)'s dated-commit route; and record the authors'
snapshot date beside the first-online date.

**§16 question 6.** Both accept the grouped run-time texts. Astra
re-derived all 107 conditions from the published Fig. 3. Open notes: a text
over the 512-byte capture limit stays an obligation until its text is held
(Fable: raise the limit, or spill longer texts to a lane-named file);
attribute texts to the authors' line, not the wrapper; a general ruling by
pattern is the right first general ruling. Correction: run-04 shows 17
template matches and 30 package-source texts; twelve is the number of
templates, so design §16 question 6's "12 package texts" should be fixed.

**Next.** One follow-up PR (gate 1.3.1) closing every D and A above, with
the reviewers' regression cases and a re-audit of the pilot's transcripts;
then a delta review by both, and one pilot re-run through the lane, which
passes the API review gate first.

## Delta review outcome (2026-10-12)

Fable's delta review (mail `20261012T113743.407608Z`) found three
second-pass items, D-1, D-2, and B-1, plus D-3 and notes, all closed at
`1d875d2`. Astra's delta review of `1d875d2`
(`~/agent-mail/codex/outbox/claude/2026-10-12-codex-gate131-delta-review.md`,
probes under `~/agent-mail/codex/review-evidence/2026-10-12-llmr-gate131-delta/`)
found three class D defects, each an incomplete closure, so a clean pilot
re-run alone would not close the hardening:

| Finding | Closes | Closure, in short |
|---|---|---|
| D-Astra-1: a successful command need not deliver a file (`cat x > copy`, `true \|\| cat x`, `cat x \| cat y`); Read and spill reads matched by substring | F2 | A Bash read counts only in one `&&` chain of `cd`, full reads, and `echo`, with no pipe, output redirection, substitution, or background; any other shape blocks with a request for a plain read. Read, spill, and shell paths match as whole normalised paths; a glob stays within one path component. Any verdict but `read` blocks, in the hook and in `reconcile-run.py`. The three definitions and both briefs say so (no `\| tee` any more). |
| D-Astra-2: a comment, and `cp` as a search pattern, became hard write failures | F1 | Transcript audit 1.2: comments are blanked with quoting respected (a `<<` in a comment opens no heredoc); copy, tee, and in-place edits match only as the command, past prefixes; variables expand with their quote context, so a value's `>` is never an operator. |
| D-Astra-3: persistence could use another workflow's cleared run audit | F8 | Run audit 1.1 records the workflow run, each role's agent and accepted-payload digest, and the reviewed artefact state: `check-attempt` prints a digest of the attempt (less the post-review records), and the in-workflow gate check's transcript records it before the review. audit-run selects results as persist-results does, refusing two for one paper; admission requires the persisted results' identities and the attempt unchanged since that gate check, so a re-audit cannot launder a changed comparison. |

Three false negatives turned up while closing them, now fixed: a comment's
`<<` hid the next line from the audit, `cp -t DIR` and `sed -i.bak` writes
were missed, and a glob's `*` crossed `/`. Astra's probes, rerun against the
fixes with only their loader widened to the whole module, give the intended
verdicts; the new tests fail on `1d875d2` but for one positive control.
