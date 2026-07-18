# Phase 2 Preregistration — Draft for OSF Lodgement

**Version:** 0.4 (lodgement candidate)
**Date:** 2026-07-18
**Registration type:** OSF Open-Ended Registration (single narrative Summary field;
supporting documents attached to the OSF project and frozen by the registration)
**Status:** RESOLVED — all nine decision points resolved (Shawn, 2026-07-15/16; table in
the final section). Awaiting final read-through, then lodgement.
**Sources:** pilot findings report v1.1 §7 (H1–H5); study protocol v1.0 §4, §7.2;
agentic modernisation plan v0.3 §5–6, §9; Cosmos draft v0.3 prereg section (drafting-care
constraints); Marwick 2025 (doi:10.1016/j.jas.2025.106281) for policy scope and trigger.
**Revision provenance:** v0.2 applies the 2026-07-14 `/review-implementation` stress-test:
H2 endpoint de-circularised (coverage, exact trend test); H1 restricted to quantitative
papers with trend-adjusted secondary; JAS: Reports difference-in-differences control arm
added (Shawn approved 2026-07-14); H4 reworded to match its test; blinding, stability
threshold, human-validation subsample, and power table added. v0.3 applies the
2026-07-15/16 decision-point resolutions: compute cap revised (48 h → 168 h on named
reference hardware, with an archived-intermediates partial path in §5); all other draft
positions confirmed; inline decision markers removed. v0.4 (Shawn, 2026-07-18):
census window start moved to 2022-01-01 (two full pre-policy years); H5 and the
credibility-assessment lane reclassified as pre-specified exploratory; *Reports*
control gains a gate-authorised census option.

---

## OSF metadata (entered in the registration form, not the Summary field)

- **Title:** Open science compliance and computational reproducibility in the
  *Journal of Archaeological Science*, 2022–2026: a FAIR census with a controlled
  policy comparison and preregistered reproduction study (Phase 2)
- **Description (one sentence):** Preregistration of four confirmatory hypotheses and
  one pre-specified exploratory analysis about Findable, Accessible, Interoperable,
  Reusable (FAIR) compliance and computational reproducibility in *Journal of
  Archaeological Science* (JAS) papers, tested via a descriptive FAIR census of JAS
  2022–2026 with a difference-in-differences control series from *JAS: Reports*, and
  Docker-based reproduction of the eligible computational subset.
- **Contributors:** Shawn Ross (ORCID: 0000-0002-6492-9025), sole registrant; Large
  Language Model (LLM) assistance is disclosed in Summary §8.
- **Category:** Project
- **Licence:** CC BY 4.0
- **Subjects:** Archaeology; Science and Technology Studies; Library and Information Science
- **Tags:** reproducibility; FAIR; open science; archaeology; meta-research;
  computational reproduction; preregistration; difference-in-differences
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

Policy context: JAS introduced an Associate Editor for Reproducibility (AER) in January
2024, conducting reproducibility reviews of "submissions that mentioned programming
languages such as R or Python in the methods sections" (Marwick 2025,
doi:10.1016/j.jas.2025.106281). Marwick (2025) lists the archaeology journals that added
AERs in 2024 — JAS, *Advances in Archaeological Practice*, *Journal of Field
Archaeology*, and *American Antiquity*; *JAS: Reports* is not among them, which grounds
its use as a control series (§3, §6 H1b).

The five hypotheses below (H1–H4 confirmatory; H5 pre-specified exploratory, §6) were
generated from pilot observations (pilot findings report
v1.1 §7, attached). The five pilot papers are therefore hypothesis-generating data and are
**excluded from all confirmatory tests** (§6). They appear in descriptive census tables
flagged as pilot papers.

### 2. Status of data collection at registration

- Complete and public: all Phase 1 pilot artefacts for five papers (extractions,
  assessments, FAIR scores, reproduction artefacts), in the study repository.
- **Not started:** the JAS 2022–2026 census sweep and the *JAS: Reports* control sample.
  No paper beyond the five pilot papers has been screened, acquired, extracted,
  FAIR-scored, or reproduced, in either journal. No census metadata has been collected.
  FAIR scores are the dependent variable in H1 and the context for H2; no such scores
  exist for any non-pilot paper at registration.
- Commitment: no new-corpus data will be touched before this registration is lodged.

### 3. Design overview

Three linked components:

1. **Descriptive FAIR census (JAS main).** All eligible quantitative JAS papers,
   2022–2026 (window defined §4), scored on the FAIR instrument (§7.1), data and code
   independently. Doubles as the sampling frame for component 3.
2. **Control series (*JAS: Reports*).** A stratified random sample of quantitative
   *JAS: Reports* papers over the same window, scored on the same instrument by the same
   pipeline — the FAIR lane only. Provides the difference-in-differences (DiD) contrast
   for H1b. Reproduction of *Reports* papers is an **exploratory stretch goal** only:
   resources permitting, never entering confirmatory analyses.
3. **Confirmatory reproduction study.** The eligible computational subset of the JAS
   main census (criteria §5) undergoes the full pipeline: extraction, credibility
   assessment, Docker-based reproduction, and fresh-context adversarial review. H2–H4
   are tested on this subset; H5 is examined on it as a pre-specified exploratory
   analysis (§6). The credibility assessment runs on every subset paper (locked before
   reproduction, §8) as instrument-development work; its outputs are reported for
   discussion, not confirmatory inference.

### 4. Sampling frames and eligibility

- **Frame construction:** CrossRef and OpenAlex sweep of *Journal of Archaeological
  Science* (main journal) and *Journal of Archaeological Science: Reports*, publication
  window 2022-01-01 to 2026-06-30 inclusive. Window membership is defined on the
  **earliest recorded publication date** (online-first or issue) reported by CrossRef;
  both dates are recorded. The two sources are merged as a union; DOI-level
  discrepancies between them are logged and resolved against the publisher record.
- **Census inclusion:** research articles (excluding editorials, corrigenda, letters,
  review articles without new analysis) with accessible full text, in English, that are
  **quantitative** — defined as reporting numerical analysis of data (measurements,
  counts, statistics, or model outputs). Rationale: the H1 sample must be restricted on
  a characteristic the policy cannot influence. Whether a paper mentions or shares code
  is itself a plausible policy outcome, so conditioning the sample on code presence
  would condition on a post-treatment variable; the quantitative nature of the research
  is fixed by its content. Code-sharing prevalence is analysed as an outcome, not used
  as a filter (§6 H1a).
- **Recorded for every frame paper (including census-excluded):** DOI, publication dates
  (online-first and issue), received/accepted dates where published, open-access status,
  presence of data and code availability statements, quantitative flag,
  computational-component flag (code-based analysis), analysis language(s).
- **_Reports_ control sample:** stratified random sample of quantitative *Reports*
  papers, proportional by publication year; target n = 120, floor n = 60 (final n set by
  the pre-scale cost gate and recorded before scoring begins; the gate may lower n
  toward the floor or raise it, up to a full census of eligible quantitative *Reports*
  papers, as frame size and budget permit); seeded sampling, seed and
  code published.
- **Control validity condition:** the DiD design assumes *JAS: Reports* had no
  reproducibility review during the window. Marwick (2025) supports this to 2025;
  current *Reports* author guidelines will be re-checked (and editor confirmation sought
  if ambiguous) before census launch, with the check documented. **Pre-specified
  fallback:** if *Reports* adopted an AER or equivalent during the window, the DiD arm
  is dropped and H1b is reported as a descriptive cross-journal comparison only.
- Screening decisions are logged per paper; frames and screening logs will be published
  with study outputs.

### 5. Reproduction subset eligibility

A JAS main census paper enters the reproduction subset if ALL of:

1. Computational component present (analysis producing published numerical/graphical
   results from code).
2. Code available in any form (repository, archive, supplement) — availability claims
   that cannot be fulfilled are recorded as such and the paper is retained with verdict
   BLOCKED (this is an outcome, not an exclusion).
3. Primary analysis in R. Python/Julia/mixed papers are recorded and deferred to a
   documented follow-on (pipeline extension points exist but are untested; deferral
   avoids conflating language support with reproducibility findings).
4. Estimated compute within cap: ≤168 hours (7 days) wall-clock per paper on the study's
   reference hardware (hardware documented per run in `environment.md`). The cap bounds
   scope, not membership: where a paper's full analysis exceeds the cap but the paper
   archives intermediate outputs (e.g. posterior draws or fitted model objects),
   downstream verification targets are regenerated from those archives — the
   table-regeneration path exercised by the §8 regression gate — and coverage is scored
   on the testable targets. Papers over cap with no archived intermediates are recorded
   as over-cap, not silently dropped.
5. No study-team co-authorship. Papers co-authored by study personnel are census-included
   (flagged) but excluded from reproduction to avoid self-assessment.

**Data availability is deliberately NOT an eligibility criterion** — it is the H2
predictor and must vary across the subset. Papers with inaccessible data are attempted
and their coverage and verdicts recorded as the data warrant.

**Resource cap:** if the eligible subset exceeds 25 papers, a simple random sample of 25
is drawn (seeded; seed and sampling code published). If fewer than 15 are eligible, all
are reproduced and the shortfall is reported as a limitation (band inherited from
protocol v1.0 §1.3).

### 6. Hypotheses and tests

Unless stated otherwise: tests two-tailed at α = 0.05 with directional predictions
recorded; exact p-values and effect sizes with 95% confidence intervals reported
throughout. Pilot papers excluded from all tests. Multiplicity handling: H1–H4 address
distinct constructs and are treated as separate families; within-hypothesis multiple
comparisons are Holm-corrected as specified per hypothesis. H5 is pre-specified but
exploratory (see its entry below) and sits outside the confirmatory structure. H1b and
all secondary
analyses are estimation-focused (point estimate + interval), not gated on significance.

Given the sample sizes in §10, H2–H5 are acknowledged at the outset as power-limited:
effect sizes with confidence intervals are the primary reporting quantity, p-values
secondary, and null results will not be interpreted as evidence of absence.

**H1 — Policy effect on FAIR scores.** Papers subject to JAS's reproducibility review
regime (policy effective January 2024) have higher FAIR scores than papers not subject
to it.

*H1a — within-journal cohort comparison (JAS main).*

- *Sample:* quantitative census papers (minus pilot papers).
- *Cohort assignment:* pre-policy = accepted before 2024-01-01; post-policy = received on
  or after 2024-01-01; transitional = received before, accepted after. Primary test
  compares pre vs post; sensitivity analyses merge the transitional cohort into each
  side. Papers lacking received/accepted dates: assigned by publication year (2022–2023
  = pre, 2025–2026 = post, 2024 = transitional).
- *Measures:* data FAIR /15 on all quantitative papers; code FAIR /15 on papers with any
  code artefact (interpreted with the conditioning caveat above, since code presence is
  policy-responsive). Tested separately; Holm-corrected pair.
- *Test:* Wilcoxon rank-sum; rank-biserial correlation and Hodges–Lehmann shift estimate.
- *Additional pre-specified outcome:* code-sharing prevalence — proportion of
  quantitative papers with any code artefact, pre vs post (two-proportion test, odds
  ratio with 95% CI).
- *Trend-adjusted secondary:* regression of FAIR score on continuous publication time
  plus a policy-period term (segmented form), heteroscedasticity-consistent (HC3)
  standard errors. Interpretive caveat stated in advance: with a short pre-policy
  series (two years, 2022–2023), the within-journal design cannot fully separate the
  policy from the secular trend —
  that is what H1b is for.
- *Predicted direction:* post > pre on all measures.

*H1b — difference-in-differences (JAS main vs JAS: Reports).*

- *Estimand:* the journal × period interaction on data FAIR score among quantitative
  papers — the policy effect net of the secular trend common to both journals.
- *Estimator:* ordinary least squares with journal, period (as in H1a; transitional
  excluded from the primary, sensitivity analyses as in H1a), and their interaction;
  HC3 standard errors. Reported as point estimate with 95% CI; estimation-focused.
- *Assumptions, stated in advance:* (a) parallel trends — partially checkable with two
  pre-policy years: 2022–2023 annual and monthly FAIR-score trends in both journals
  will be inspected before the interaction is interpreted, and the shortness of the
  pre-series is stated as a limitation; (b) no spillover —
  authors publishing in both journals may carry practices across; violation biases the
  interaction toward null (conservative); (c) stable composition — method-type profiles
  of both journals over time reported descriptively as a check.
- *Predicted direction:* positive interaction (JAS main improves more than *Reports*
  post-2024).

**H2 — Data availability as primary predictor of reproduction success.** Data
availability, not code availability or environment specification, determines how much of
a paper's results can be reproduced.

*Known coupling, stated in advance:* reproduction verdicts (§7.2) are partially defined
by data access (a data-caused PARTIAL is a definitional link, not an empirical finding).
The primary endpoint is therefore **verification-target coverage** (§7.6), which
separates how much could be checked (data-side) from whether checked values matched
(code-side). The verdict-based test is retained only as a consistency check.

- *Sample:* reproduction subset.
- *Primary endpoint:* coverage — the proportion of pre-enumerated verification targets
  reproduced within tolerance (§7.6). BLOCKED papers score 0 with targets enumerated
  from the paper text.
- *Primary test:* exact (permutation) Jonckheere–Terpstra trend test of coverage across
  ordered availability levels, collapsed to three (open = L1–L2; gated = L3;
  restricted/absent = L4–L5; taxonomy §7.3). Effect size: Somers' d
  (availability → coverage) with bias-corrected bootstrap 95% CI; medians and
  interquartile ranges reported per level.
- *Model-choice rationale (recorded so the choice is auditable):* the unit is the paper
  (N ≤ 25) and coverage is bounded with expected point masses at 0 and 1. Beta
  regression cannot accept boundary values without ad hoc transformation;
  zero-one-inflated beta is over-parameterised at this N; aggregated binomial models
  weight papers by their target counts (papers with many targets would dominate) and
  require fragile cluster corrections. An exact rank-based trend test is
  assumption-light, exact at this N, and respects the paper as the unit.
- *Secondary (estimation only):* fractional logistic regression (quasi-binomial, logit
  link; Papke–Wooldridge 1996) of coverage on availability level (ordinal score), code
  availability form, and environment-specification level (§7.5).
- *Consistency check:* Fisher's exact test on dichotomised availability (L1–L2 vs L3–L5)
  × verdict (SUCCESSFUL vs not), reported with the coupling caveat.
- *Predicted direction:* higher availability → higher coverage; code availability and
  environment specification predict coverage weakly or not at all once availability is
  accounted for.

**H3 — Pinned dependencies reduce build effort.** Papers with pinned dependency
management require fewer Docker build iterations. **Framed as effect-size estimation**:
at pilot base rates (~20% pinned) the pinned group is expected to number ~5 papers, so
hypothesis testing is nominal (§10).

- *Sample:* reproduction subset papers reaching the build stage.
- *Groups:* pinned (renv/packrat lockfile, conda-lock, pinned container digest, or
  equivalent machine-readable pin set) vs unpinned.
- *Measure:* Docker build iterations = 1 + number of failed-build-then-modify cycles
  before first successful build (logged automatically by the pipeline).
- *Analysis:* medians per group; Hodges–Lehmann difference with exact 95% CI; exact
  Wilcoxon rank-sum reported secondarily.
- *Interpretive limit, stated in advance:* pinning co-occurs with Dockerfiles and
  literate programming (pilot §4.2 found an infrastructure bundle); this design cannot
  isolate pinning from the bundle.
- *Predicted direction:* pinned < unpinned.

**H4 — Determinism and exact reproduction.** Deterministic analyses are more likely to
reproduce exactly than stochastic analyses.

- *Sample:* reproduction subset papers with comparable numerical outputs.
- *Classification:* deterministic = no pseudo-random number generation in the verified
  analysis path; stochastic otherwise. Seeded-stochastic (PRNG use fully seeded in the
  published code) recorded as a subcategory.
- *Primary test:* Fisher's exact on determinism × precision category (exact vs
  not-exact; §7.4).
- *Sensitivity:* primary test repeated excluding seeded-stochastic papers (fixed seeds
  in a matched environment can legitimately yield exact reproduction, diluting the
  association).
- *Descriptive extension (no test):* the pilot's stronger conjecture — that determinism
  yields exact reproduction *regardless of environment-specification quality* — is an
  equivalence claim this sample cannot test. It is examined descriptively via a
  stratified table of precision category by environment-specification level within the
  deterministic stratum.
- *Predicted direction:* deterministic → exact.

**H5 (pre-specified exploratory) — Literate programming and transparency.** Papers using
literate programming score higher on the Transparency credibility signal.

*Exploratory status, stated in advance:* the repliCATS-adapted credibility instrument
has evidenced run-to-run stability (§8) but no external validation against human
raters or outcomes. The credibility-assessment lane is instrument-development work;
its outputs (including this analysis) are presented for discussion, not confirmatory
inference. The analysis below is nonetheless fully pre-specified to constrain
analytical flexibility.

- *Sample:* reproduction subset (the Transparency signal is produced by the credibility
  assessment, which runs only on this subset).
- *Groups:* literate programming (RMarkdown/Quarto/Jupyter as the primary analysis
  artefact) vs standalone scripts.
- *Measure:* Transparency signal, 0–100 (repliCATS-adapted instrument, pilot-validated).
- *Test:* Wilcoxon rank-sum; rank-biserial correlation.
- *Known criterion overlap, stated in advance:* the Transparency rubric rewards visible
  analytical decision-making, which literate programming provides directly; the scorer
  necessarily sees the paper's code style. H5 is therefore a test of whether the
  instrument registers the practice, not an independent causal claim. Procedural
  defence: assessment-before-reproduction blinding (§8) ensures no reproduction-outcome
  knowledge contaminates the score.
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
public repository with persistent identifier, no access barriers. L2 open-partial: more
than 50% of the paper's datasets (counting unit: distinct datasets enumerated in the
paper's data availability statement and methods) retrievable via standard protocol;
remainder gated or missing. L3 gated: retrievable only via author contact, registration,
or institutional access. L4 restricted: documented legal/ethical restriction. L5 absent:
not available; includes unfulfilled availability claims. Assigned at reproduction time
from actual retrieval attempts, not statements alone. For analysis, collapsed to three
ordered levels: open (L1–L2), gated (L3), restricted/absent (L4–L5). (New instrument,
drafted for this registration per pilot report §8.2.)

**7.4 Precision categories.** Exact = matches to machine precision; within tolerance =
matches within pre-stated per-analysis tolerances (e.g. within published highest posterior
density intervals for Markov chain Monte Carlo outputs), tolerances recorded in each
reproduction plan before execution; material discrepancy = outside tolerance with
potential to affect conclusions.

**7.5 Environment-specification levels (ordinal).** 0 none / 1 language version stated /
2 unpinned dependency list / 3 pinned lockfile / 4 container specification / 5 container
plus pinned lockfile.

**7.6 Verification-target coverage.** For each reproduction-subset paper, the approved
reproduction plan enumerates verification targets (published tables, figures, and named
values) **before execution begins**; this locked list is the denominator. Coverage =
(targets reproduced exactly or within pre-stated tolerance) / (targets enumerated).
Targets that cannot be tested (missing data, unbuildable environment) count against
coverage. BLOCKED papers: targets enumerated from the paper text; coverage 0. The
denominator lock prevents post hoc redefinition of scope.

### 8. Pipeline, permitted changes, and reliability checks

All extraction, FAIR scoring, and reproduction work is LLM-assisted (Claude, Anthropic)
under human oversight, executing inside Docker with deterministic artefact-persistence
gates. Every reproduction receives an adversarial review in a fresh context with no
memory of the reproduction it audits. Human checkpoints: batched approval of reproduction
plans before compute spend; escalation of QUALIFIED/CHALLENGED reviews, paper-error
findings, and cannot-compare calls; spot-check sampling of SUCCESSFUL verdicts.

**Assessment-before-reproduction blinding.** For every reproduction-subset paper, FAIR
scoring and credibility assessment are completed and locked (committed to the study
repository) **before** reproduction execution begins for that paper. Assessment and
reproduction run as architecturally separate agents with no shared context, so no
knowledge of reproduction outcomes can contaminate scores (relevant to H2 covariates and
H5).

**Permitted implementation changes.** The pilot ran as a manually-orchestrated
session-per-pass pipeline; Phase 2 will run an agentic implementation of the same
protocol. Implementation changes are permitted **only** if the new pipeline passes a
regression test against pilot artefacts: re-running at least two pilot papers must yield
identical verdicts and identical value-level comparison results (prose differences and
build-iteration counts may drift; verdict or value changes are failures). The gate
includes a stochastic-path leg: regeneration of published tables from the Crema et al.
archived posteriors (minutes of compute), exercising the table-regeneration path used
for long-running Markov chain Monte Carlo papers. The full-MCMC path (~18 h) is not
re-run; this scope limit is stated rather than silent. The gate touches pilot data only.

**Instrument reliability.** Before census scoring: (a) FAIR scoring stability estimated
by repeated scoring of at least three pilot papers, three runs each. **Acceptance
threshold:** mean per-sub-principle agreement ≥ 0.90 across runs. If below threshold,
the census is scored by majority vote of three independent runs per paper (a ~3× cost
multiplier on the cheap lane, priced by the pre-scale cost gate). (b) Comparability of
the census scoring path (lightweight metadata+infrastructure extraction) against the
pilot path (full extraction) on the same pilot papers. Both checks use pilot papers only
and touch no new-corpus data. Outcomes reported with study results; instrument changes
triggered by these checks would be lodged as a transparent OSF amendment **before**
census scoring begins. (These checks implement agentic-modernisation plan §9 items 1–2;
verdicts delivered 2026-07-15/16.)

**Human validation subsample.** A seeded random subsample of 12 census papers will be
independently hand-scored on both FAIR instruments by the registrant, blinded to machine
scores. Per-sub-principle percent agreement and Cohen's kappa reported with study
results. This is validation evidence, not a gate; no published work validates LLM
scoring of GO-FAIR sub-principles against human raters (cf. Candela et al. 2024,
doi:10.5334/dsj-2024-033), and this subsample addresses that gap directly.

Prior reliability evidence: a 25-run variability test (5 papers × 5 runs) of the
extraction→credibility pipeline showed 100% classification stability and aggregate score
coefficients of variation of 1.9–3.4%.

### 9. Exclusions, missing data, deviations

- Papers excluded at any stage are logged with reasons; the log is published.
- Missing received/accepted dates: H1 fallback assignment by publication year (§6 H1a).
- Papers whose code cannot be obtained at all: retained, verdict BLOCKED, coverage 0
  (H2 data).
- Withdrawn/corrected papers: census-included with erratum noted; reproduction targets
  the corrected version.
- If *JAS: Reports* is found to have adopted a reproducibility review during the window,
  the DiD arm is dropped per the pre-specified fallback (§4).
- Any deviation from this registration will be lodged as a dated OSF amendment with
  rationale before the affected analysis runs.

### 10. Power and interpretation constraints

Approximate power at α = 0.05 two-tailed (H1a at α = 0.025 for the Holm pair;
z-approximations with pilot-informed group splits; full assumptions in the analysis
plan):

| Test | Assumed split | Detectable at 80% power |
|------|--------------|------------------------|
| H1a rank-sum, census ~160 quantitative papers (2022–2026 window) | 80 pre / 80 post | Cliff's δ ≈ 0.28 (moderate) |
| H1a if census ~80 | 40 / 40 | δ ≈ 0.40 (large) |
| H1b DiD interaction | ~160 + ~120 | interaction terms need ~4× the N of main effects; estimation-focused by design |
| H2 exact trend, n ≤ 25 across 3 levels | ~12 / 6 / 7 | large monotone trends only (pilot-sized effects) |
| H3 | ~5 pinned / 20 unpinned | δ ≈ 0.7 (near-separation); estimation only |
| H4 Fisher | ~10 / 15 | very large associations only |
| H5 rank-sum (exploratory) | ~8 / 17 | δ ≈ 0.6 (large) |

Census and *Reports* frame sizes are unknown until the sweep runs; frame sizes will be
reported before any scoring. Additional stated limitations: author-cluster
non-independence (prolific authors contribute multiple papers; noted as a limitation,
with a descriptive author-overlap check); single-assessor LLM pipeline (mitigated by the
reliability checks and human validation subsample, §8); R-only reproduction scope.

### 11. Timeline

Registration July 2026 → reliability checks and pipeline regression test (pilot papers
only) Q3 2026 → *Reports* policy-scope re-verification, census sweep, and FAIR scoring
(both journals) Q3 2026 → reproduction subset Q3–Q4 2026 → analysis and reporting
Q4 2026 – Q1 2027.

---

## Decision points — all RESOLVED (Shawn, 2026-07-15/16)

| # | Question | Resolution |
|---|----------|------------|
| 1 | Contributors/LLM acknowledgement on OSF | Sole registrant; LLM assistance disclosed in Summary §8 — as drafted |
| 2 | Census window cutoff | 2026-06-30, earliest publication date — as drafted |
| 3 | Per-paper compute cap | **REVISED:** 48 h → 168 h wall-clock on named reference hardware; archived-intermediates partial path added to §5 criterion 4 (the cap bounds scope, not membership) |
| 4 | Reproduction subset size band | 15–25; random sample if >25 (seed published) — as drafted |
| 5 | Multiplicity stance | Per-hypothesis families; Holm only within H1a's data/code pair — as drafted |
| 6 | Data-availability taxonomy L1–L5 + 3-level collapse | Approved as drafted (§7.3) |
| 7 | FAIR reliability + comparability checks, 0.90 threshold | Confirmed — included; implements agentic-modernisation plan §9 items 1–2 (verdicts delivered 2026-07-15/16) |
| 8 | *Reports* control sample size | Target 120, floor 60, stratified by year — as drafted |
| 9 | Human validation subsample size | n = 12, seeded, blinded — as drafted |

Resolved this revision (Shawn, 2026-07-14): H1 sample restriction is **quantitative**
(not computational) — restriction must be policy-invariant; code presence is
post-treatment. DiD control arm **approved** — FAIR lane, reproduction as exploratory
stretch goal.

Post-resolution revisions (Shawn, 2026-07-18, pre-lodgement):

- Census window start 2023-01-01 → **2022-01-01**, giving two full pre-policy years.
  Rationale: the pre-group roughly doubles (H1a power), and H1b's parallel-trends
  assumption becomes partially checkable (2022–2023 pre-trends in both journals).
  2022 was chosen over a symmetrical mid-2021 start to keep full-year strata and to
  limit exposure to COVID-era compositional shifts in the submission cohorts.
- **H5 and the credibility-assessment lane reclassified pre-specified exploratory**
  (instrument stable across runs but not externally validated; presented for
  discussion). Confirmatory structure is now H1–H4.
- ***Reports* control:** the pre-scale cost gate may raise n above the 120 target, up
  to a full census of eligible quantitative *Reports* papers, as frame size and budget
  permit.

Notes for review, not in the registration text:

- D3 rationale (v0.3): a pre-specified compute rule prevents discretionary in-flight
  drops ("this one is taking too long"), which would systematically exclude
  Bayesian/Markov chain Monte Carlo papers — exactly H4's stochastic side and H2's
  hardest tail. The worst observed pilot runtime was ~18 h, so 48 h offered thin
  headroom; 168 h binds only genuinely extreme papers, and the archived-intermediates
  path turns even those into partial data rather than exclusions.
- H2's model choice was investigated before selection (v0.2): exact rank-based trend
  primary; fractional logit secondary; beta-family and aggregated-binomial models
  rejected for boundary-mass, over-parameterisation, and unit-weighting reasons recorded
  in §6 H2.
- H3's build-iteration metric is measured uniformly within the confirmatory subset by
  the production pipeline, so pilot-era iteration counts (different harness) never enter
  the analysis — one more reason pilot papers are excluded from confirmatory analyses.
- The transitional cohort in H1a exists because the policy's application rule
  (submission date vs review date) is not documented publicly; three-way assignment with
  sensitivity analyses is robust to either interpretation.
- The *Reports* AER-absence evidence is Marwick 2025's list of 2024 AER adoptions (JAS,
  Advances in Archaeological Practice, Journal of Field Archaeology, American
  Antiquity); *Reports* absent. Re-verify guidelines before launch per §4.
