# Phase 2 Preregistration — Draft for OSF Lodgement

**Version:** 0.1 (draft for Shawn's review)
**Date:** 2026-07-14
**Registration type:** OSF Open-Ended Registration (single narrative Summary field;
supporting documents attached to the OSF project and frozen by the registration)
**Status:** DRAFT — not lodged. Decision points marked `[DECISION n]` inline and
collected in the final section. Resolve all before lodgement.
**Sources:** pilot findings report v1.1 §7 (H1–H5); study protocol v1.0 §4, §7.2;
agentic modernisation plan v0.3 §5–6, §9; Cosmos draft v0.3 prereg section (drafting-care
constraints).

---

## OSF metadata (entered in the registration form, not the Summary field)

- **Title:** Open science compliance and computational reproducibility in the
  *Journal of Archaeological Science*, 2023–2026: a FAIR census and preregistered
  reproduction study (Phase 2)
- **Description (one sentence):** Preregistration of five hypotheses about Findable,
  Accessible, Interoperable, Reusable (FAIR) compliance and computational reproducibility
  in *Journal of Archaeological Science* (JAS) papers, tested via a descriptive FAIR
  census of JAS 2023–2026 and Docker-based reproduction of the eligible computational
  subset.
- **Contributors:** Shawn Ross (ORCID: [insert]) `[DECISION 1: sole registrant, or list
  collaborators/LLM-assistance acknowledgement in contributor notes?]`
- **Category:** Project
- **Licence:** CC BY 4.0
- **Subjects:** Archaeology; Science and Technology Studies; Library and Information Science
- **Tags:** reproducibility; FAIR; open science; archaeology; meta-research;
  computational reproduction; preregistration
- **Attachments (frozen with the registration):** pilot findings report v1.1; study
  protocol v1.0 (contains the FAIR instrument, §4); Pass 6 infrastructure prompt
  (operational FAIR scoring implementation); this document.

---

## Registration summary (paste into the Open-Ended Registration Summary field)

### 1. Background and prior work

Phase 1 (exploratory pilot, completed 2026-02) assessed five computational papers from
the *Journal of Archaeological Science* (JAS), 2023–2025, through structured extraction,
credibility assessment, FAIR (Findable, Accessible, Interoperable, Reusable) scoring, and
Docker-based computational reproduction with adversarial review. Results: four SUCCESSFUL
and one PARTIAL reproduction; the sole PARTIAL was caused by data inaccessibility (3 of 13
source datasets retrievable), not code failure. Reproduction detected two calculation
errors in one published paper that peer review had missed. The pilot protocol was
timestamped by git commit before pilot work began (study protocol v1.0, 2025-01-09); its
§7.2 committed to OSF preregistration of Phase 2 hypotheses before Phase 2 corpus
selection. This registration fulfils that commitment.

The five hypotheses below were generated from pilot observations (pilot findings report
v1.1 §7, attached). The five pilot papers are therefore hypothesis-generating data and are
**excluded from all confirmatory tests** (§6). They appear in descriptive census tables
flagged as pilot papers.

### 2. Status of data collection at registration

- Complete and public: all Phase 1 pilot artefacts for five papers (extractions,
  assessments, FAIR scores, reproduction artefacts), in the study repository.
- **Not started:** the JAS 2023–2026 census sweep. No paper beyond the five pilot papers
  has been screened, acquired, extracted, FAIR-scored, or reproduced. No census metadata
  has been collected. FAIR scores are the independent variable in H1 and a predictor
  context for H2; no such scores exist for any non-pilot paper at registration.
- Commitment: no new-corpus data will be touched before this registration is lodged.

### 3. Design overview

Two linked components:

1. **Descriptive FAIR census.** All eligible JAS papers, 2023–2026 (window defined §4),
   scored on the FAIR instrument (§7.1), data and code independently. The census is
   descriptive (no hypothesis tests except H1, which uses census scores) and doubles as
   the sampling frame for component 2.
2. **Confirmatory reproduction study.** The eligible computational subset of the census
   (criteria §5) undergoes the full pipeline: extraction, credibility assessment,
   Docker-based reproduction, and fresh-context adversarial review. H2–H5 are tested on
   this subset.

### 4. Census sampling frame and eligibility

- **Frame construction:** CrossRef and OpenAlex sweep of *Journal of Archaeological
  Science* (main journal only; not JAS: Reports), final publication date 2023-01-01 to
  2026-06-30 inclusive. `[DECISION 2: confirm cutoff date]`
- **Census inclusion:** research articles (excluding editorials, corrigenda, letters,
  review articles without new analysis) with accessible full text, in English.
- **Recorded for every frame paper (including census-excluded):** DOI, publication date,
  received/accepted dates where published, open-access status, presence of data and code
  availability statements, computational-component flag, analysis language(s).
- Screening decisions are logged per paper; the frame and screening log will be published
  with study outputs.

### 5. Reproduction subset eligibility

A census paper enters the reproduction subset if ALL of:

1. Computational component present (analysis producing published numerical/graphical
   results from code).
2. Code available in any form (repository, archive, supplement) — availability claims
   that cannot be fulfilled are recorded as such and the paper is retained with verdict
   BLOCKED (this is an outcome, not an exclusion).
3. Primary analysis in R. Python/Julia/mixed papers are recorded and deferred to a
   documented follow-on (pipeline extension points exist but are untested; deferral
   avoids conflating language support with reproducibility findings).
4. Estimated compute within cap: ≤48 hours wall-clock per paper on available hardware.
   Papers over cap are recorded, not silently dropped. `[DECISION 3: confirm cap]`
5. No study-team co-authorship. Papers co-authored by study personnel are census-included
   (flagged) but excluded from reproduction to avoid self-assessment.

**Data availability is deliberately NOT an eligibility criterion** — it is the H2
predictor and must vary across the subset. Papers with inaccessible data are attempted
and receive PARTIAL/BLOCKED verdicts as the data warrant.

**Resource cap:** if the eligible subset exceeds 25 papers, a simple random sample of 25
is drawn (seeded; seed and sampling code published). If fewer than 15 are eligible, all
are reproduced and the shortfall is reported as a limitation. `[DECISION 4: confirm
15–25 band, inherited from protocol v1.0 §1.3]`

### 6. Hypotheses and tests

All tests two-tailed at α = 0.05 with directional predictions recorded; exact p-values
and effect sizes with 95% confidence intervals reported throughout. Pilot papers excluded
from all tests. Multiplicity handling: H1–H5 address distinct constructs and are treated
as separate families; within-hypothesis multiple comparisons are Holm-corrected as
specified per hypothesis. `[DECISION 5: confirm this multiplicity stance; alternative is
Holm across all primary tests]`

**H1 — Policy effect on FAIR scores.** Papers subject to JAS's mandatory reproducibility
review (policy effective January 2024) have higher FAIR scores than papers not subject
to it.

- *Sample:* full census (minus pilot papers).
- *Cohort assignment:* pre-policy = accepted before 2024-01-01; post-policy = received on
  or after 2024-01-01; transitional = received before, accepted after. Primary test
  compares pre vs post; sensitivity analyses merge the transitional cohort into each side.
  Papers lacking received/accepted dates: assigned by publication year (2023 = pre,
  2025–2026 = post, 2024 = transitional).
- *Measures:* data FAIR /15 and code FAIR /15, tested separately (Holm-corrected pair).
- *Test:* Wilcoxon rank-sum; rank-biserial correlation and Hodges–Lehmann shift estimate.
- *Predicted direction:* post > pre on both scales.

**H2 — Data availability as primary predictor of reproduction outcome.** Data
availability, not code availability, predicts reproduction outcome.

- *Sample:* reproduction subset.
- *Outcome:* SUCCESSFUL vs not-SUCCESSFUL (PARTIAL/FAILED/BLOCKED).
- *Primary test:* Fisher's exact on dichotomised data availability (L1 open-complete vs
  L2–L5, taxonomy §7.3) × outcome.
- *Secondary:* Firth-penalised logistic regression of outcome on data-availability level,
  with code-availability form and environment-specification level (§7.5) as covariates.
  Firth penalisation chosen for expected small N (≤25); if quasi-separation persists,
  report exact logistic regression. The regression is explicitly secondary: at N ≤ 25
  with three predictors it is descriptive, not well-powered.
- *Predicted direction:* higher availability → higher odds of SUCCESSFUL.

**H3 — Pinned dependencies reduce build effort.** Papers with pinned dependency
management require fewer Docker build iterations.

- *Sample:* reproduction subset papers reaching the build stage.
- *Groups:* pinned (renv/packrat lockfile, conda-lock, pinned container digest, or
  equivalent machine-readable pin set) vs unpinned.
- *Measure:* Docker build iterations = 1 + number of failed-build-then-modify cycles
  before first successful build (protocol-defined; logged automatically by the pipeline).
- *Test:* Wilcoxon rank-sum; rank-biserial correlation.
- *Predicted direction:* pinned < unpinned.

**H4 — Determinism enables exact reproduction.** Deterministic analyses reproduce
exactly regardless of environment-specification quality.

- *Sample:* reproduction subset papers with comparable numerical outputs.
- *Classification:* deterministic = no pseudo-random number generation in the verified
  analysis path; stochastic otherwise (seeded stochastic recorded as a subcategory).
- *Outcome:* precision category — exact (machine precision) / within tolerance /
  material discrepancy (taxonomy §7.4).
- *Test:* Fisher's exact on determinism × (exact vs not-exact).
- *Predicted direction:* deterministic → exact.

**H5 — Literate programming improves transparency.** Papers using literate programming
score higher on the Transparency credibility signal.

- *Sample:* reproduction subset (the Transparency signal is produced by the credibility
  assessment, which runs only on this subset — the census FAIR lane does not produce it).
- *Groups:* literate programming (RMarkdown/Quarto/Jupyter as the primary analysis
  artefact) vs standalone scripts.
- *Measure:* Transparency signal, 0–100 (repliCATS-adapted instrument, pilot-validated).
- *Test:* Wilcoxon rank-sum; rank-biserial correlation.
- *Predicted direction:* literate > standalone.

### 7. Instruments and measures (fixed at registration)

**7.1 FAIR instrument.** 15 binary GO-FAIR sub-principles (F1–F4, A1–A2 incl. A1.1/A1.2,
I1–I3, R1 incl. R1.1–R1.3), scored independently for data (/15) and code (/15); never
aggregated into a combined score. Instrument v2.0 as standardised 2026-02-11 (study
protocol §4, attached), including the A1 completeness rule: A1 requires that a majority
of the research data be retrievable via standard protocol, with an exception for
documented ethical/legal restriction. Rating bands: 13–15 Highly / 9–12 Moderately /
5–8 Minimally / 0–4 Not FAIR. Unscoreable sub-principles score 0 (the instrument scores
evidenced practice).

**7.2 Reproduction verdicts.** SUCCESSFUL (all or nearly all values within tolerance) /
PARTIAL (some analyses reproduced, others could not be) / FAILED (material discrepancies
affecting conclusions) / BLOCKED (reproduction could not be attempted). Definitions as in
the reproduction-assessor protocol used in the pilot.

**7.3 Data availability taxonomy (5 levels).** L1 open-complete: all analysis data in a
public repository with persistent identifier, no access barriers. L2 open-partial:
majority retrievable via standard protocol; remainder gated or missing. L3 gated:
retrievable only via author contact, registration, or institutional access. L4
restricted: documented legal/ethical restriction. L5 absent: not available; includes
unfulfilled availability claims. Assigned at reproduction time from actual retrieval
attempts, not statements alone. `[DECISION 6: approve taxonomy — new instrument, drafted
for this registration per pilot report §8.2]`

**7.4 Precision categories.** Exact = matches to machine precision; within tolerance =
matches within pre-stated per-analysis tolerances (e.g. within published highest posterior
density intervals for Markov chain Monte Carlo outputs), tolerances recorded in each
reproduction plan before execution; material discrepancy = outside tolerance with
potential to affect conclusions.

**7.5 Environment-specification levels (ordinal).** 0 none / 1 language version stated /
2 unpinned dependency list / 3 pinned lockfile / 4 container specification / 5 container
plus pinned lockfile.

### 8. Pipeline, permitted changes, and reliability checks

All extraction, FAIR scoring, and reproduction work is LLM-assisted (Claude, Anthropic)
under human oversight, executing inside Docker with deterministic artefact-persistence
gates. Every reproduction receives an adversarial review in a fresh context with no
memory of the reproduction it audits. Human checkpoints: batched approval of reproduction
plans before compute spend; escalation of QUALIFIED/CHALLENGED reviews, paper-error
findings, and cannot-compare calls; spot-check sampling of SUCCESSFUL verdicts.

**Permitted implementation changes.** The pilot ran as a manually-orchestrated
session-per-pass pipeline; Phase 2 will run an agentic implementation of the same
protocol. Implementation changes are permitted **only** if the new pipeline passes a
regression test against pilot artefacts: re-running at least two pilot papers must yield
identical verdicts and identical value-level comparison results (prose differences and
build-iteration counts may drift; verdict or value changes are failures). This gate
touches pilot data only.

**Instrument reliability.** Before census scoring: (a) FAIR scoring stability estimated
by repeated scoring of at least three pilot papers, three runs each, reporting
per-sub-principle agreement; (b) comparability of the census scoring path (lightweight
metadata+infrastructure extraction) against the pilot path (full extraction) on the same
pilot papers. Both checks use pilot papers only and touch no new-corpus data. Thresholds
and outcomes will be reported with study results; instrument changes triggered by these
checks would be lodged as a transparent OSF amendment **before** census scoring begins.
`[DECISION 7: these checks implement plan §9 items 1–2, which await your verdict —
confirm inclusion]`

Prior reliability evidence: a 25-run variability test (5 papers × 5 runs) of the
extraction→credibility pipeline showed 100% classification stability and aggregate score
coefficients of variation of 1.9–3.4%.

### 9. Exclusions, missing data, deviations

- Papers excluded at any stage are logged with reasons; the log is published.
- Missing received/accepted dates: H1 fallback assignment by publication year (§6 H1).
- Papers whose code cannot be obtained at all: retained, verdict BLOCKED (H2 data).
- Withdrawn/corrected papers: census-included with erratum noted; reproduction targets
  the corrected version.
- Any deviation from this registration will be lodged as a dated OSF amendment with
  rationale before the affected analysis runs.

### 10. Power and interpretation constraints

Census N is unknown until the sweep runs (order-of-magnitude expectation: tens to low
hundreds of computational papers); frame size will be reported before any scoring. H1 is
tested at census scale. H2–H5 are tested on ≤25 papers and are acknowledged as
power-limited: effect sizes with confidence intervals are the primary reporting quantity,
p-values secondary. Null results on H2–H5 will not be interpreted as evidence of absence.

### 11. Timeline

Registration July 2026 → reliability checks and pipeline regression test (pilot papers
only) Q3 2026 → census sweep and FAIR scoring Q3 2026 → reproduction subset Q3–Q4 2026 →
analysis and reporting Q4 2026 – Q1 2027.

---

## Decision points before lodgement

| # | Question | Draft position |
|---|----------|----------------|
| 1 | Contributors/LLM acknowledgement on OSF | Shawn Ross sole registrant; LLM assistance disclosed in Summary §8 |
| 2 | Census window cutoff | 2026-06-30 publication date |
| 3 | Per-paper compute cap | 48 h wall-clock |
| 4 | Reproduction subset size band | 15–25; random sample if >25 (seed published) |
| 5 | Multiplicity stance | Per-hypothesis families; Holm only within H1's data/code pair |
| 6 | Data-availability taxonomy L1–L5 | As drafted §7.3 (new instrument) |
| 7 | Commit to FAIR reliability + comparability checks | Included (implements plan §9 items 1–2; awaiting your §9 verdicts) |

Two further notes for review, not in the registration text:

- H3's build-iteration metric is measured uniformly within the confirmatory subset by the
  production pipeline, so pilot-era iteration counts (different harness) never enter the
  test — one more reason pilot papers are excluded from confirmatory analyses.
- The transitional cohort in H1 exists because the policy's application rule (submission
  date vs review date) is not documented publicly; three-way assignment with sensitivity
  analyses is robust to either interpretation.
