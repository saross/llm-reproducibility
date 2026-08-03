# Benchmark disagreement analysis — Phase A1

**Date:** 2026-08-03. **Plan:** `wiki/planning/instrument-clarification-plan.md`
(Phase A1). **Inputs:** the 45 spawn outputs under `arm-*/run-*/`, the three
`run-record.json` files, and the E8-registered pilot reference scores
(`manifest.yaml` `reference_datasets.pilot_fair_assessments`). **Method:**
`../../../protocol/validation/analyse-benchmark-disagreements.py` recomputes
both registered statistics from primary artefacts, then extracts every
disputed item — within-arm disagreement in any arm, or majority-vs-reference
mismatch in any arm — with all evidence strings, to
`disputed-items.json`. All quotations below are verbatim from spawn or
reference evidence fields.

## 1. Verification of published figures

Recomputed from spawn outputs, independent of the run records:

| Arm | Stability (recomputed) | Run-record | Concordance (recomputed) | Summary |
|---|---|---|---|---|
| sonnet-5 | 121/150 = 0.8067 | 121/150 ✓ | 116/150 = 0.7733 | 0.773 ✓ |
| opus-5 | 131/150 = 0.8733 | 131/150 ✓ | 121/150 = 0.8067 | 0.807 ✓ |
| fable-5 | 122/150 = 0.8133 | 122/150 ✓ | 123/150 = 0.8200 | 0.820 ✓ |

The sonnet guideless-minority correlation in the plan's evidence base is
confirmed: 29 two-one splits in the sonnet arm; in 17 the minority vote
comes from a spawn whose receipts lack `fair-principles-guide.md`, against
≈ 11.3 expected by chance (dye had two guideless runs, the other four
papers one each; for the 24 non-dye splits, 13 observed vs 8 expected,
roughly p ≈ 0.015 one-tailed). Real, but secondary to the structural causes
below, which full guide exposure demonstrably does not resolve.

## 2. Scale of dispute

Under the union criterion, **68 of 150 items** are disputed. By
sub-principle (maximum 10 each — 5 papers × 2 artefact types):

A1.2: 10 · R1.3: 8 · I3: 6 · R1.1: 6 · F2: 6 · I1: 5 · F1: 4 · F3: 4 ·
A2: 4 · A1: 3 · A1.1: 3 · R1: 3 · R1.2: 3 · F4: 2 · I2: 1

A1.2 is disputed on every possible item. The spread beyond the
benchmark summary's headline five (A1.2, R1.1, A2, R1.3, F-block) is real
but not independent: reading the evidence strings shows nearly all 68 items
reduce to **three root causes**.

## 3. Root cause 1 — the assessment target is undefined

*Whose FAIR is being measured: the paper's own deposits, or everything the
research relied on?* The instrument never says whether third-party and
upstream resources credit the paper's artefacts. Touches F1, F3, F4, A2,
I2, R1.1, R1.3, and the A1 coverage override — and produces the fable-arm
dye-et-al-2023 data-FAIR flip (totals 6–13 across runs).

- **Upstream datasets.** Dye's principal dataset is a third-party,
  DOI-bearing Archaeological Data Service (ADS) deposit. Opus credits it
  for F1 ("The principal research dataset carries a DOI … 10.5284/1018290");
  sonnet refuses ("Availability statement (p.24) only states 'Data and
  materials are available in the Supplement' with no DOI/accession for the
  Supplement itself"). The reference credits both axes at once ("Paper DOI
  10.1016/j.jas.2023.105765; upstream Anglo-Saxon dataset DOI
  10.5284/1018290").
- **Third-party software.** For dye code R1.3 the reference scores 1 via
  the ArchaeoPhases package ("Follows CRAN package standards"), while fable
  scores the paper's own code ("Conformance evidence exists only for the
  third-party …"). The same split recurs on F4 ("ArchaeoPhases is indexed
  in CRAN" vs "not deposited in a searchable code registry … bundled as an
  Elsevier journal-article supplementary file") and I2.
- **Article-level properties.** Does the article's DOI serve as the
  supplement's persistent identifier (key data F1: reference credits it;
  all nine spawns of two arms score 0)? Does the article's CC BY licence
  cover supplement data (key data R1.1: reference and two arms yes, opus
  split: "no data artefact is released …")?
- **The A1 coverage override inherits the same question.** A1 splits track
  run-to-run variation in the data-completeness denominator — whether
  upstream sources count as the paper's data: crema "complete" vs "partial
  (6/11 upstream sources at Tier 0-2)"; herskind "complete (5/5)" vs
  "partial (50%)" depending on whether the primary source catalogue
  (Płonka 2003) belongs in the denominator.

## 4. Root cause 2 — the admissible evidence basis is undefined

*Under paper-only scoring (amendment 1 §4 read-scope isolation), may the
assessor credit properties that hold by construction of a named platform,
or only what the paper's text states?* Touches F2, F3, A2, F4, I1, R1,
R1.2, and R1.1 — the largest cluster by item count.

- **Platform-inference, accepted:** opus scores herskind F2 = 1 because
  "Code is deposited in Zenodo, which mints structured DataCite metadata
  … for every published record", A2 = 1 via DataCite "tombstone behaviour",
  F3 = 1 "by construction". Fable generally follows.
- **Platform-inference, refused:** sonnet scores the same items
  "Unscoreable: … cannot verify without visiting the withheld/external
  record", applying the registered unscoreable→0 default.
- The guide licenses the inference only implicitly, via a worked example —
  opus cites it as calibration: "consistent with the pulled guide's worked
  example ('licence captured in Zenodo metadata' → R1.1 = 1)". An example
  is not a rule, and sonnet reads the same guide the other way.
- The same divide drives I1 (format inferable from a described R pipeline
  vs "the paper never states the file format(s)") and R1/R1.2 (do rich
  prose method descriptions count as the *artefact's* documentation and
  provenance, or must documentation attach to the deposit?).
- **This is also the mechanism behind the unanimity-without-concordance
  pattern:** where all three arms agree and still miss the reference, the
  reference typically encodes platform or repository knowledge the
  paper-only lane cannot reach (e.g. marwick I3 reference "DOI links to
  paper and related resources" vs all nine spawns finding no
  machine-actionable link evidence in the text).

## 5. Root cause 3 — semantic gaps in individual sub-principles

- **A1.2 (all 10 items disputed).** The instrument and guide cover
  restricted-with-justification and closed-without-justification, but not
  the case every pilot paper presents: fully open, no authentication
  needed. Two stable readings coexist, sometimes within one arm: "fully
  open sharing satisfies A1.2 vacuously (no auth barrier imposed where
  none is necessary)" vs "no explicit authentication/authorisation
  mechanism is described … unscoreable, scored 0 per instrument default".
- **R1.3 (8 items).** "Domain-relevant community standards" is read as
  methodological standards (IntCal20, OxCal, NIMBLE — "all established
  community-standard tools/practices in computational radiocarbon
  archaeology") or as deposit-level metadata/packaging standards ("No
  domain data standard (ARIADNEplus, Dublin Core, Darwin Core, CIDOC-CRM)
  is cited as having been used to structure or describe the … datasets").
  On dye data R1.3 all three arms unanimously take the first reading and
  the reference takes the second — a guaranteed concordance failure
  independent of run noise.

## 6. Reference-score findings (Phase B implications)

The mining also surfaced properties of the E8 reference set itself:

1. **It encodes repository-informed knowledge** unavailable to the
   paper-only lane (Zenodo metadata fields, CRAN package internals,
   White Rose repository holdings) — the structural concordance confound
   the benchmark summary identified, now visible item by item.
2. **It takes both sides of root cause 1 across papers:** key data F1 = 1
   via the article DOI, while dye data F3 = 0 for having "No separate data
   DOI; data only in publisher supplement"; dye code R1.3/R1.1 credit a
   third-party package's standards and licence, while herskind and key
   code R1.3 = 0 for lacking deposit-level standards of their own.
3. Whatever Phase A2 decides on the three root causes will therefore
   invalidate part of the reference set as-is — strengthening the plan's
   Phase B1 preference (re-derive references under the clarified
   instrument and census configuration) over retrofitting.

## 7. Decision points for Phase A2 (each a registrant call)

| # | Question | Resolves | Claude's starting recommendation |
|---|---|---|---|
| 1 | Assessment target: do upstream datasets, third-party software, and article-level properties credit the paper's artefact scores? | Root cause 1; dye flip | Score the paper's own deposits only; upstream sources are handled by the existing data-completeness lane; add an explicit rule for papers whose principal dataset is someone else's published deposit |
| 2 | Evidence basis: define an admissibility ladder for paper-only scoring — (i) paper text; (ii) by-construction properties of named platforms (closed list: DataCite DOI, Zenodo, CRAN, ADS, …); (iii) nothing further | Root cause 2 (largest cluster) | Admit (ii) with a closed, instrument-listed platform table; below the ladder, unscoreable→0 applies |
| 3 | A1.2: does fully-open-no-authentication-needed score 1? | All 10 A1.2 items | Yes (vacuous satisfaction), stated in instrument text |
| 4 | R1.3: enumerate qualifying standard types per artefact class; do methodological standards count? | 8 R1.3 items | Deposit-level standards only; methodological standards excluded |
| 5 | R1.1: (a) does the article licence extend to publisher-hosted supplements? (b) does an unnamed platform licence field count? (c) third-party dependency licences? | 6 R1.1 items | (a) Shawn's FAIR expertise; (b) no — licence must be named; (c) no |
| 6 | F1: does the article DOI serve as a supplement-only artefact's identifier? | 4 F1 + knock-on F3 | No — F1 requires a resource-level identifier |
| 7 | Restate the unscoreable→0 default's boundary in terms of the #2 ladder | Root cause 2 tail | Unscoreable only after the ladder is exhausted |
| 8 | Coverage-denominator rule: which upstream sources enter the data-completeness denominator (drives the A1 override) | 3 A1 items | Tighten alongside #1; same target definition |

Items not covered by these eight (a residue of genuine borderline
judgements, e.g. single-run outliers on I2) are expected to fall within
ordinary rater noise once the structural causes are removed; the post-fix
re-benchmark measures whether that expectation holds.
