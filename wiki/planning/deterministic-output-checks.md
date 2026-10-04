---
title: "Deterministic checks on model-produced scoring outputs — planning note"
tags: [validation, census, mechanical-verification]
created: 2026-10-04
updated: 2026-10-04
status: seed
---

# Deterministic checks on model-produced scoring outputs — planning note

**Status: SEED (2026-10-04).** Shawn asked to "start thinking about
mechanical/deterministic checking of outputs to catch errors like
mis-counts". This note collects the evidence so far, candidate checks, and
the questions to settle before anything is built. Nothing here changes a
governed file.

## Why

- **A miscount reached a committed payload.** In Opus 5.5 `medium` run 3,
  `dye-et-al-2023` `code_fair` records `total: 7` while its sub-principle
  items sum to 8. The schema does not tie `total` to the items, and the
  reconciler validates against the schema, so it passed. H13 caught it
  (`../../studies/open-science-compliance/outputs/validation/opus-5-5-arms-2026-10/results-2026-10-04.md`).
- **The standing direction (2026-10-03)** is to replace judgement checks
  with mechanical ones wherever possible (plan,
  `instrument-clarification-plan.md`, "Mechanical verification"; Obs 33).
- **The residual errors are rule-shaped.** Six of Opus 5.5 `medium`'s 10
  gate misses are F2 over-credits (crema, herskind, and marwick, data and
  code). All three runs are unanimous, and every opus-5 run agrees. The F2
  positive threshold (AP-15) is mechanical in principle: creators, title, a
  substantive description, and at least one subject keyword, all
  readable from registry metadata.

## Layer 1: internal consistency (cheap, no external data)

A first exploratory scan of all 135 benchmark payloads (nine arms; probe
script kept in the session scratchpad, not committed):

| Check | Rule | Hits |
|---|---|---|
| C1 | section `total` equals the sum of its 15 items | 1 (opus-5-5 medium, dye r3 `code_fair`: 7 vs 8) |
| C2 | `coverage_percentage` equals accessible / enumerated × 100 | 0 |
| C3 | `coverage_category` matches the instrument's bands (complete 100; substantial 75–99; partial 25–74; minimal 0–24) | 0 |
| C4 | minimal or partial coverage with data A1 = 1 carries an `a1_exception_rationale` | 0 |
| C5 | `available: false` with any item scored 1 | 1 (fable-5, key r1 `data_fair`: 1 item) |
| C6 | every `pack_refs` id exists in the paper's evidence pack | 0 |

These are pure functions of the payload and pack, so they belong beside the
reconciler's schema validation as hard checks. They fail the item. They do
not repair it.

## Layer 2: rule-derived checks (instrument rules applied mechanically)

These need structured inputs, mostly from the evidence packs (registry
responses are already harvested and checksummed):

- **F2 from registry metadata (AP-15).** Creators, title, description
  length or substance, and subject keywords from DataCite or Zenodo
  fields. This is the strongest candidate on current evidence: 6 of 10
  `medium` misses.
- **Platform-row implications.** For example, Row 6 (supplement-only
  deposit) implies F2 = F3 = F4 = A2 = 0. This needs a structured
  deposit-type field. Today the row appears only inside evidence prose.
- **Licence presence and conflict (R1.1)**, from pack `licences` and
  `licence_conflicts`.
- **Identifier presence in the paper's text** (the plan's existing pre-census
  item, Obs 33): every identifier a payload cites must appear in the paper
  or supplement, then resolve, then match its target.

## Layer 3: evidence grounding

- **Quote verification.** Every quoted string in `evidence` should appear
  in the paper's extracted text (normalising hyphenation and line breaks).
  This catches fabricated or misattributed quotations (compare F-001).
- **Location sanity.** Cited pages and lines fall within the document.

## Questions to settle

1. **Flag or override?** A mechanical rule that disagrees with a model
   score could either flag the item for human adjudication or replace the
   model's score. Replacing it changes the scoring method, which is
   probably an amendment matter under the preregistration. Flagging is
   safe now.
2. **Where it runs.** A post-hoc checker over completed payloads fits the
   lane's design (gates advisory, verification on artefacts; WN-p). It
   could run inside `reconcile-run.py` or as a separate pass recorded in
   the run record.
3. **Census or validation scope.** Should Layer 1 run retroactively over
   the committed benchmark arms and be reported, or only from the census
   onwards?
4. **F2 adoption path.** If a mechanical F2 matches the E8-v2 reference on
   the pilots, is it adopted as the F2 scorer (amendment), or kept as a
   check?

## Next step (proposed)

Build Layer 1 as a small tested script (`scripts/check-payload-consistency.py`)
that runs over a run directory or committed arm, plus a prototype of the
F2 rule scored against the E8-v2 reference on the five pilots. No API
spend is needed.
