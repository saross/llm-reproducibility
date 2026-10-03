# Phase 2 shakedown — deviations and rulings record

**Run:** `phase2-shakedown-2026-10`. This file records every change made
after the pre-committed inputs (`run-config.yaml` v1.0 and
`regression-criterion.md` v1.0, commit `a411e3c`). Per the criterion, a
change is a deviation logged here, never an edit to the criterion. Entries
are append-only.

## D1 — Criterion clarification v1.1 (Shawn, 2026-10-03, before any executor spawn)

**Clarifies check 1 (verdict identity).** Verdict identity is judged on the
targets that attempt-01 tested. A verdict difference that arises solely from
targets enumerated beyond attempt-01's scope is reported as a
**scope-expansion difference**, not a FAIL. The expected case is dye's
Supplement Table 1 and the between-run summary, which need four
unpublished OxCal runs.

**Application.** The operator maps attempt-01's compared values onto
attempt-02's targets. Check 1 passes when attempt-02's outcomes on those
mapped targets support attempt-01's verdict under the
verdicts-and-precision definitions. The full-scope verdict is reported
alongside.

**Why:** the agentic planners enumerate far more completely than the pilot
did. The first plan round gave 14 targets for herskind and 23 for dye,
against the pilot's undeclared scope. Without this clarification, a more
complete denominator could fail a regression test whose subject is the
harness, not the scope.

**Registered-gate note:** preregistration §8 says "identical verdicts". The
registered gate will face the same scope-expansion question and may need an
erratum-log clarification before it runs.

## D2 — First plan round superseded; re-plan with rulings (Shawn, 2026-10-03)

**What happened.** Plan round 1 (`wf_5d10728a-820`, launch commit
`344049d`) returned two OK plans for $2.76 API-equivalent. Its herskind
plan failed the receipt audit: it keyed the invariants receipt as
`invariants`, with the correct version and token. The cause was an
orchestrator defect, not a model error (register F-014). The blinding list
forbade `.claude/projects/`, where the harness had saved each spawn's
pushed-instrument payload. Both planners therefore refused their own
instrument delivery, read the canonical instrument files instead, and
disclosed this.

**Ruling:** fix the defect and re-plan both papers, rather than adjudicate
the receipt.

**Changes before round 2:**

1. The workflows exempt the two harness files an agent may read: its own
   hook-delivery file and its own tool-output spill files. They state the
   exact receipt keys, read from the manifest.
2. `run-config.yaml` gains the rulings R1–R4, which generalise the
   registrant's answers to round 1's questions. R1 allows labelled
   verification aids for no-code targets. R2 keeps targets with unavailable
   inputs in the denominator. R3 sets one target per display item. R4 scores
   against the stated value, under the PAPER_ERROR protocol, where the paper
   is internally inconsistent.
3. Round 1's plans are archived under `superseded-plans/wf_5d10728a-820/`
   before launch, so round 2 cannot anchor on them. Round 1's paper-specific
   target lists are not passed to round 2.

**Rulings on round-1 questions, recorded for comparison with round 2.** The
target scope was accepted as planned: herskind's Fig. 3 as one target; T14
scored against the stated "nine" under PAPER_ERROR; dye's Figs 1, 2, 5, and
6 excluded; dye's T08 and T09 kept in the denominator as
expected-untestable.

## Findings recorded during the run (no deviation)

- **dye corpus mislabel:**
  `~/corpora/llm-reproducibility/dye-et-al-2023/vor.pdf` is the White Rose
  accepted manuscript (eprints.whiterose.ac.uk/197500, "Version: Accepted
  Version", CC BY-NC-ND), not Elsevier's version of record. The corpus
  manifest role `vor` is wrong. The round-1 dye planner found it; the
  operator verified it with pdftotext on 2026-10-03.
- **Paper-level findings from round-1 planning, to be confirmed in
  execution:**
  - herskind's methods give PMI as log₂, but its code and all published
    values use the natural log;
  - herskind's text claims "nine" Ertebølle-exclusive bigrams but lists
    eight;
  - four of the five OxCal runs behind dye's Supplement Table 1 return HTTP
    404 at `tsdye.online/AP/`;
  - dye's supplement hard-codes an author-local path (Sec. 10.4).
