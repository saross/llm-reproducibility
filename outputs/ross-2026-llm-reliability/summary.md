# Extraction Summary: Ross and Ballsun-Stanton (2026), pre-submission draft

**Paper:** "Reliability in research with large language models is a property of the
human–AI system"
**Authors:** Shawn A. Ross, Brian Ballsun-Stanton (Macquarie University)
**Paper type:** Meta-research case study (methodological)
**Draft status:** Pre-publication draft dated 2026-07-24, not yet submitted
**Extractor:** Claude Fable 5 (Claude Code, session-per-pass workflow v5.0.0)
**Schema:** v2.6
**Extraction completed:** 2026-07-24 (Sessions A–D)

---

## Purpose of this extraction

This extraction is **not** a corpus assessment of a published paper. It is a
**pre-submission quality check of the authors' own draft**, run through the
`research-assessor` workflow to test the paper's claims against its evidence and to
audit the transparency of its research design, methods, and protocols (RDMAP) before
submission.

The practical deliverable is the **seven pre-submission QA flags** in the section below:
internal inconsistencies detected between the main text and Supplement A during
extraction. Everything else here is the supporting apparatus.

**Deliberately out of scope** (see "Deferrals" below): FAIR scoring, Cluster 3
computational reproducibility, and Passes 8–9.

---

## Pre-submission QA flags (the actionable output)

Seven internal-consistency issues were recorded during Sessions B and C and carried
forward unmodified through validation. They are findings **about the paper**, not
extraction defects, and were deliberately not "repaired" — where a flagged figure was
encountered during extraction it was captured as stated (noted on M042 and M026), so the
extraction faithfully records the inconsistency rather than silently smoothing it.

**1. Tool-discovery totals (one-unit offsets throughout).**
Supplement A.2 reports 243 unique tools / 155 (63.8%) verified / ChatGPT Deep Research
137 of 144 unique-verified (95.1%). Main-text Tables 4–5 report 242 unique / 154
verified / 136 of 143 (95.1%). Reconcile before submission.
*(E239, E240 vs E098, E101, E106)*

**2. ade4 contradiction — model attribution and ground-truth verdict both disagree.**
Section 4.3 says the palaeoecology package ade4 "belonged in scope" and that Claude
flipped it, "settling correctly only with the final version of the prompt". Supplement
A.4 places the flip under the ChatGPT heading, calls ade4 an ecology package correctly
classified as having "no documented applications in archaeology", and calls the
affirmative reclassification confabulated. **This is the most substantive flag: the two
passages disagree about both which model did it and which answer was right.**
*(E131 vs E272)*

**3. Metadata-stage service names.**
Section 4.3 lists OpenAI o3, Claude Sonnet 3.7 (research mode), Gemini 2.5 Pro;
Supplement A.4 lists Claude Research, Google Gemini 2.5 Pro, ChatGPT Deep Research. If
"o3" is a run label (cf. the A.2 footnote), state so. The terse-output profile is
attributed to o3 in 4.3 but to ChatGPT Deep Research in A.4.
*(E127/E129 vs E267/E271)*

**4. JOSS confabulation count (15 vs 14).**
Section 4.2 and Table 5 use 15 ("reduced its confabulations from 15 to none"); the
Supplement A.2 DOI-walking analysis says "all 14 confabulated tools".
*(E115/E103 vs E248, E249)*

**5. Per-journal confabulation denominators.**
Main text quotes per-run rates (JOSS first run 44%, JOAD sole Deep Research run 93%);
the supplement quotes overall rates (JOSS 22%, JOAD 82%) and elsewhere 14 of 18 JOAD
discoveries. Clarify which denominator each figure uses.
*(E107 vs E241, E244)*

**6. Count mismatch in A.4.**
The hyperbolic-titles paragraph says "three distinct interventions" then lists four
(style guide, title-format conventions, system prompt, inline instructions).
*(E275)*

**7. ArboDat accounts.**
Section 4.4 says the model recorded the 1997 statement in notes but reported "no date";
A.4 says it extracted a 2024 metadata timestamp as the development date. If these are
different rows of the same episode, a linking sentence would prevent the appearance of
inconsistency.
*(E157 vs E277)*

---

## Final extraction totals

| Array | Count |
|-------|-------|
| Evidence | 283 |
| Claims | 166 |
| Implicit arguments | 20 |
| Research designs | 25 |
| Methods | 44 |
| Protocols | 38 |
| **Total** | **576** |

Claims by role: 22 core, 91 intermediate, 53 supporting.
Methods by type: 12 data collection, 12 validation, 11 analysis, 9 quality control.
RDMAP total: 107 items, of which **14 are implicit (13.1%)** — 1 design, 6 methods,
7 protocols.

---

## Validation (Pass 7)

**Status: PASS_WITH_WARNINGS** — 0 critical, 0 important, 0 minor, 1 informational.

All three shared validators run clean, before and after the Pass 7 write:

| Validator | Result |
|-----------|--------|
| `validate_extraction.py` | 0 errors (schema, references, duplicate IDs, page validity) |
| `check_rdmap_completeness.py` | 0 orphaned methods, 0 orphaned protocols, 100% protocol→method linkage |
| `validate_bidirectional.py` | 0 corrections, 0 conflicts |

Note: `validate_extraction.py` defaults to a schema filename that does not exist
(`extraction_schema.json`). The real file is `extraction-schema-v2.6.json` and must be
passed as the second argument.

**Quote re-verification: 625 of 625 passages (100%).** Every `verbatim_quote` and every
`trigger_text` passage — including the quotes preserved inside consolidation provenance
records — was re-tested as a normalised substring of the page-anchored markdown, using
the same normalisation that gated the original saves (curly quotes to straight, en/em
dash to hyphen, soft hyphen removed, fi/fl ligatures expanded, whitespace collapsed).

**The single informational finding:** 10 of 25 research designs have no implementing
methods. Nine are framing-tier designs (`research_question`, `theoretical_framework`,
`scope_definition`) that set the study's rationale rather than prescribing a procedure,
so having no implementing method is correct. The tenth, **RD029**, is the extraction's
only implicit research design — a "capability-adoption-upon-release strategy" that the
paper follows but never states as a design decision. Its lack of a documented
implementing method *is* the transparency gap it records, not a gap in the extraction.

The validator was negative-controlled: injecting a fabricated quote, a broken reference,
an orphaned method, an out-of-range page, and an invalid enum into a scratch copy caused
all five checks to fire (status FAIL, 8 critical), confirming the clean result is a real
pass rather than a vacuous one.

---

## Conventions validated against (not "fixed")

This extraction deviates from the literal expectations of prompt 07 in five places. Each
deviation is deliberate and recorded in `extraction_notes`; validation checked the
convention actually in use.

1. **No `source_verification` objects exist on any item.** Quotes were verified
   *mechanically at extraction time* by `pass1_lib.py` (evidence, claims, implicit
   arguments) and `rdmap_lib.py` (RDMAP), which abort the save on any quote that is not a
   normalised substring of the source. Pass 7 re-runs that same test rather than looking
   for the field structure prompt 07 Checks 4.1/4.3 describe.
2. **Implicit RDMAP uses sequential `RD###`/`M###`/`P###` IDs** with
   `*_status: "implicit"`, not prompt 04's `IMP` prefixes (recorded in
   `extraction_notes.pass4_extraction`).
3. **Methods mirror `realized_through_protocols` and `implemented_by_protocols`.** Both
   are rebuilt deterministically from forward references by `rdmap_lib.sync_reverse_refs`;
   validation confirms they agree rather than treating the pair as duplication.
4. **Four page-break-spanning quotes were deliberately clipped**, with the omission
   documented on the item. All ten known clip sites still carry their documentation
   (verified in the Pass 7 clip audit). Clipped quotes are a sourcing decision, not a
   sourcing failure; the omitted text is verifiable against the PDF.
5. **`consolidation_metadata` uses two valid forms.** Pass 2 (claims/evidence) lists all
   pre-consolidation IDs in `consolidated_from` *including the surviving item's own ID*,
   with absorbed quotes in `absorbed_items`; Pass 5 (RDMAP) lists only absorbed IDs, with
   quotes in `merged_sources`. Both are provenance records. No absorbed item was found
   still living in the content arrays.

---

## Extraction workflow

| Session | Passes | Outcome |
|---------|--------|---------|
| A | Pre-flight, Pass 0, Pass 6 | Metadata and infrastructure |
| B | Pass 1–2, Phase 2b | Claims and evidence |
| C | Pass 3–5, Phase 5b | RDMAP |
| D | Pass 7 | Validation |

**Pass 1–2 (claims and evidence).** Liberal extraction across 18 section groups, then
conservative consolidation: 500 items → 469. Claims 192 → 166 (**13.5% reduction**);
evidence 288 → 283 (**1.7% reduction**). 30 consolidations, 1 boundary correction. The
13.5% claims reduction sits at the lower edge of the 15–20% target, which suits a
methodological paper with genuinely well-differentiated design principles.

**Pass 3–5 (RDMAP).** Liberal explicit extraction across the *same* 18 section groups
with equal attention to all of them (not Methods-weighted), then implicit RDMAP scanning,
then rationalisation: 123 items → 107 (**13.0% reduction**, 16 consolidations, 1 boundary
correction).

**Pass 7 (validation).** Reported above. No repairs were required, so no
`pass7_repair_references.py` was written.

---

## Deferrals (deliberate, not gaps)

Because this is a pre-submission draft whose repositories and DOIs are not final:

- **FAIR assessment — deferred.** `reproducibility_infrastructure.fair_assessment` is
  recorded as `status: "not_assessed"` with all four dimension scores null. Scoring a
  draft's FAIR compliance would measure the state of an unfinished deposit, not the
  paper.
- **Cluster 3 (computational reproducibility) — deferred.** Requires final deposited
  materials, which do not yet exist.
- **Passes 8–9 (research approach classification, credibility assessment) — not run.**
  Out of scope for this extraction.

Related, and expected rather than deficient: data availability, code availability,
preregistration, funding, contributions, and conflict-of-interest statements are absent
from the draft by design. Author ORCIDs are present. These absences are recorded in
`extraction_notes.known_limitations` as artefacts of draft status, not transparency
failures.

---

## Methodological notes

**Source handling.** Extraction worked from a page-anchored markdown rendering
(`input/sources/processed-md/ross-2026-llm-reliability.md`, 39 pages, `--- page N ---`
markers, 1-based) with the PDF available for verification. Page markers are the
authoritative locators; section hints in the markdown are advisory, since headings were
detected from text alone.

**Known source-format limitations.** The paper's ten numbered tables flatten into linear
prose in the markdown rendering, so table layout must be verified against the PDF.

**What worked.** Mechanical quote verification at save time — rather than as a
post-hoc validation step — meant Session D found zero sourcing failures across 625
passages. Verification that can only pass by construction is cheaper than verification
that has to find and repair defects afterwards. Deterministic reverse-reference
rebuilding (`sync_reverse_refs`) had the same effect on cross-references: Phase 5b and
Pass 7 both had nothing to repair.

---

## Files

| File | Contents |
|------|----------|
| `extraction.json` | Complete extraction, Passes 0–7 |
| `pass1_lib.py`, `rdmap_lib.py` | Shared verification helpers (quote normalisation, reverse-reference sync) |
| `pass1_g01.py`–`pass1_g18.py` | Pass 1 section-group extraction |
| `pass2_rationalisation.py` | Pass 2 consolidation |
| `pass3_g01.py`–`pass3_g18.py` | Pass 3 RDMAP extraction |
| `pass4_implicit_rdmap.py` | Pass 4 implicit RDMAP scan |
| `pass5_rdmap_rationalisation.py` | Pass 5 RDMAP consolidation |
| `pass7_validation.py` | Pass 7 validation |
| `summary.md` | This document |

The validation report is stored in `extraction_notes.pass7_validation`; the
session-by-session narrative is in `extraction_notes.session_log`.
