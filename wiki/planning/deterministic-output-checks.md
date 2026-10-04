---
title: "Deterministic checks on model-produced scoring outputs — planning note"
tags: [validation, census, mechanical-verification]
created: 2026-10-04
updated: 2026-10-04
status: active
---

# Deterministic checks on model-produced scoring outputs — planning note

**Status: ACTIVE — policy RULED 2026-10-04.** Shawn: "I agree with your
policy for mechanical checks, implement as written". Build sequence:
(A) Layer 1 checker, computing derived fields; (B) the F2 rule,
validated as a hybrid scorer; (C) Layer 3 flag-only evidence checks.

*Seed (2026-10-04):* Shawn asked to "start thinking about
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

*Questions 1 and 4 are answered by the disagreement policy below
(ruled 2026-10-04). Questions 2 and 3 stay open; the operator's default
is a separate post-hoc pass whose report is committed beside each run
(2), run retroactively over the committed benchmark arms and reported
(3).*

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

## Disagreement policy (proposed by Claude; RULED by Shawn 2026-10-04, adopted as written)

Shawn (2026-10-04): open to an amendment; "cases like incorrect arithmetic
seem like we should defer to the mechanistic check". Proposal: decide by
**what kind of quantity it is**.

1. **Derived quantities: compute them; don't merely check them.**
   - **Scope:** totals, `coverage_percentage`, and `coverage_category`.
     Each is defined as a function of other fields, so the model should
     not be their source.
   - **Rule:** the pipeline computes them from the scored items and
     counts. The model's value is kept only as a consistency signal. On
     disagreement the computed value governs automatically, and the
     disagreement is logged.
   - **Status:** this implements the registered definition (total = the
     item sum) rather than changing the method. It should still be
     disclosed in one line of amendment 3.
   - **Review:** a miscount can also mean the model wavered on an item
     (dye r3: total 7, items 8). So the item gets a spot check, not a
     block. The items are what the gates validated.
2. **Rule-determined items with structured inputs: validate first, then
   amend to make the rule authoritative.**
   - **Scope:** F2 under AP-15 (registry creators, title, description, and
     keywords), and platform-row implications such as Row 6.
   - **Validation (no API spend):** score the rule against the E8-v2
     reference on the five pilots. Then recompute both gate statistics
     for the **hybrid** scorer (mechanical F2, model elsewhere), because
     the gates validated the model, not the hybrid.
   - **Adoption:** if the hybrid clears the gates and the rule matches the
     reference at least as well as the model, amend so that the rule
     governs those items.
   - **Fallback:** where structured inputs are missing (no registry
     record), the model's score stands and is flagged.
   - **Reporting:** model–rule disagreement rates are reported as a study
     finding.
   - **Until amended:** flag only, with disagreements going to human
     adjudication.
3. **Judgement items with evidence checks: flag; never override.**
   - **Scope:** quote verification and identifier-in-text checks.
   - **Rule:** a failed check sends the item for re-scoring or
     adjudication; it is never auto-zeroed. A paraphrase is not a
     fabrication, and the check cannot make the FAIR judgement.
4. **Always record both values,** the rule's version, and which one
   governed, so that every override can be audited.

**Timing:** amendment 3 is still open. It could carry (1) as a disclosure,
and (2) either as an adopted rule, if validation finishes before lodgement,
or as a planned rule with its validation criteria declared in advance.

## Next step (proposed)

Build Layer 1 as a small tested script (`scripts/check-payload-consistency.py`)
that runs over a run directory or committed arm, plus a prototype of the
F2 rule scored against the E8-v2 reference on the five pilots. No API
spend is needed.
