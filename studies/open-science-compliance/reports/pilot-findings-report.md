# Open Science Compliance in *Journal of Archaeological Science*: Phase 1 Pilot Findings

**Version:** 1.1
**Date:** 2026-02-12
**Authors:** Shawn Graham and Claude (Anthropic)
**Study:** Open Science Compliance Study — Phase 1 Exploratory Pilot
**Protocol:** `studies/open-science-compliance/protocol/study-protocol.md` v1.0

## Abstract

We assessed open science compliance across five computational papers published in the *Journal of Archaeological Science* (JAS) between 2023 and 2025. Each paper underwent structured extraction, classification, credibility assessment (adapted from the Collaborative Assessments for Trustworthy Science [repliCATS] framework), Findable, Accessible, Interoperable, Reusable (FAIR) evaluation, and Docker-based computational reproduction. Four of five reproductions succeeded fully; the sole partial verdict resulted from data inaccessibility rather than code or environment failure. We found that data availability — not code availability or environment specification — was the dominant predictor of reproduction outcome. Deterministic analyses reproduced exactly regardless of infrastructure quality, while reproduction attempts uncovered two calculation errors in one paper that peer review had not detected. We propose five hypothesis candidates for a preregistered Phase 2 study of 15–25 papers.

## 1. Introduction

Computational reproducibility has become a central concern in archaeological science. Journals increasingly mandate data and code sharing, yet compliance varies widely and the practical reproducibility of published analyses remains largely untested. We designed this study to move beyond policy rhetoric by empirically assessing whether JAS papers with computational components can actually be reproduced from their published materials.

We selected JAS as our target journal for three reasons. It holds Q1 ranking in archaeological science (Scimago Journal Rank [SJR] 1.242, H-index 159). It introduced mandatory reproducibility reviews in January 2024, with Ben Marwick serving as Reproducibility Specialist. And it launched a Reproducibility Prize programme in 2023, signalling institutional commitment to open science norms. These features make JAS an unusually strong test case: if reproducibility failures persist here, they are likely more severe in journals with weaker infrastructure.

Phase 1 serves as an exploratory pilot. We developed and tested our methodology on five papers, identified patterns in compliance and reproducibility, and generated hypothesis candidates for preregistration before scaling to a confirmatory Phase 2 corpus of 15–25 papers. This report synthesises all Phase 1 findings.

## 2. Corpus and Methods

### 2.1 Paper Selection

We selected five papers spanning diverse computational methods and recognition levels. Selection criteria required publication in JAS between 2023 and 2025, English language, gold open access or repository availability, and a visible computational component (code and/or data mentioned in methods). We deliberately sought method diversity — Bayesian inference, morphometrics, computational linguistics, chronological modelling, and meta-analysis — alongside recognition diversity, including one JAS–Society for Archaeological Sciences (SAS) 2024 award winner and one established CRAN package.

**Table 1. Phase 1 corpus**

| Paper | Year | Method Type | Code Status |
|-------|------|-------------|-------------|
| Crema et al. | 2024 | Bayesian inference (MCMC) | GitHub + Zenodo |
| Marwick | 2025 | Meta-analysis (GAM, text mining) | GitHub + Zenodo |
| Key et al. | 2024 | Morphometrics (OLE point estimation) | Supplement only |
| Herskind & Riede | 2024 | Computational linguistics (n-gram PMI) | Zenodo |
| Dye et al. | 2023 | Chronological modelling (Allen algebra) | CRAN package |

### 2.2 Assessment Pipeline

Each paper underwent a six-stage pipeline: (1) eight-pass structured extraction using the `research-assessor` skill with Claude, capturing evidence, claims, methods, research designs, and reproducibility infrastructure; (2) paper classification by type and research approach; (3) credibility assessment across seven signals adapted from repliCATS for Humanities, Arts, and Social Sciences (HASS); (4) FAIR compliance assessment based on extracted infrastructure fields; (5) Docker-based computational reproduction following a four-session protocol (planning, preparation, execution and verification, adversarial review); and (6) cross-paper synthesis of reproduction findings.

The extraction pipeline uses a session-per-pass architecture where each extraction session tackles a focused subset of passes in a fresh context window. A run comparison on Crema et al. demonstrated that this approach yields substantially richer extractions than a single autonomous run (+75% claims, +100% research designs captured). All extraction, classification, and assessment steps are LLM-assisted, with validation against source data at each stage.

## 3. Classification and Credibility

### 3.1 Classification Results

Four papers classify as methodological (analytical method development), while Marwick (2025) is meta-research. Primary research approaches distribute across deductive (Crema, Key), inductive (Marwick, Herskind & Riede), and abductive (Dye). No papers exhibited evidence of Hypothesising After Results are Known (HARKing), and expressed-versus-revealed approach alignment was strong across the corpus — all papers do what they claim to do methodologically.

### 3.2 Credibility Signals

We assessed seven credibility signals on a 100-point scale, organised into three clusters following the repliCATS framework adapted for HASS research.

**Table 2. Credibility signal scores (0–100)**

| Signal | Crema | Marwick | Key | Herskind | Dye |
|--------|-------|---------|-----|----------|-----|
| Comprehensibility | 88 | 85 | 88 | 83 | 88 |
| Transparency | 92 | 90 | 78 | 82 | 85 |
| Plausibility | 82 | 80 | 85 | 78 | 82 |
| Validity | 85 | 78 | 87 | 72 | 78 |
| Robustness | 75 | 68 | 82 | 55 | 58 |
| Generalisability | 78 | 75 | 76 | 70 | 70 |
| Reproducibility | 90 | 90 | 68 | 80 | 80 |
| **Aggregate** | **84** | **81** | **81** | **74** | **77** |

**Table 3. Cluster ratings**

| Cluster | Crema | Marwick | Key | Herskind | Dye |
|---------|-------|---------|-----|----------|-----|
| C1: Foundational Clarity | Strong | Strong | Strong | Strong | Strong |
| C2: Evidential Strength | Strong | Strong | Strong | Good | Good |
| C3: Reproducibility | Strong | Strong | Good | Strong | Strong |

Two papers received Excellent overall verdicts (Crema, Marwick) and three received Good (Key, Herskind & Riede, Dye). All five score Strong on Foundational Clarity — the papers are well-written and clearly structured. Evidential Strength shows the most variation, with Herskind & Riede and Dye scoring lower on Robustness (55, 58) due to limited sensitivity analyses and narrower evidential bases. The gap between Transparency scores (78–92) and Reproducibility scores (68–90) suggests that even transparent papers can lack practical reproducibility infrastructure.

## 4. FAIR Compliance

### 4.1 Infrastructure Inventory

**Table 4. Open science infrastructure**

| Infrastructure | Crema | Marwick | Key | Herskind | Dye |
|----------------|-------|---------|-----|----------|-----|
| Code repository | GitHub | GitHub + Zenodo | Supplement | Zenodo | CRAN |
| Code DOI | Zenodo | Zenodo | — | Zenodo | — |
| Data repository | GitHub + Zenodo | Zenodo | Supplement | Zenodo | ADS |
| Data DOI | Zenodo | Zenodo | — | Zenodo | ADS |
| Author ORCIDs | — | — | — | — | All 4 |
| Environment spec | Dockerfile | Dockerfile + renv | R version only | R version only | — |
| Licence | — | MIT/CC-0/CC-BY | CC BY 4.0 | — | — |
| Code review | Marwick (repro.) | N/A (author) | — | — | — |

The infrastructure inventory reveals a clear gradient. Marwick provides the most comprehensive apparatus: pinned dependencies via renv (169 packages), a working Dockerfile, Zenodo archival with DOI, and explicit licensing for code, data, and figures separately. Crema provides similar infrastructure with a Dockerfile and Zenodo archival, though the Dockerfile contained two bugs (a package name typo and a missing dependency). At the opposite end, Key provides only supplementary R scripts with placeholder file paths and no environment specification whatsoever. Dye and Herskind & Riede occupy intermediate positions — both deposited code in repositories with DOIs but provided no environment specification or dependency pinning.

One notable gap: only Dye et al. include author ORCIDs in the paper. While JAS policy does not appear to require in-paper ORCID display, persistent identifier (PID) connectivity between authors, data, and code remains weak across the corpus.

### 4.2 FAIR Scores

All five papers were re-scored using a standardised rubric of 15 binary sub-principles from the GO-FAIR specification (v2.0, standardised 2026-02-11). Data and code are assessed independently on the same /15 scale, capturing asymmetries that a combined score would obscure. The original Phase 1 assessments used four different scales (/15, /16, /32, /40) due to infrastructure maturity evolving over 10 months of development; this re-scoring resolves that inconsistency.

**Table 5. Standardised FAIR scores (15 binary sub-principles, independent data/code)**

| Paper | Data FAIR | Code FAIR | Data Rating | Code Rating |
|-------|-----------|-----------|-------------|-------------|
| Crema et al. | 12/15 (80%) | 12/15 (80%) | Moderately FAIR | Moderately FAIR |
| Marwick | 14/15 (93%) | 14/15 (93%) | Highly FAIR | Highly FAIR |
| Key et al. | 8/15 (53%) | 6/15 (40%) | Minimally FAIR | Minimally FAIR |
| Herskind & Riede | 12/15 (80%) | 9/15 (60%) | Moderately FAIR | Moderately FAIR |
| Dye et al. | 9/15 (60%) | 14/15 (93%) | Moderately FAIR | Highly FAIR |

Independent scoring reveals data-code asymmetries invisible in combined metrics. Dye et al. scores 14/15 for code (ArchaeoPhases on CRAN with GPL-3 licence, versioned archive, and JSS publication) but only 9/15 for data (supplement-only without independent DOI). Key et al. shows both low scores: data scores 8/15 because only 3 of 13 datasets (23.1%) are retrievable — the supplement's HTTPS infrastructure scores well on protocol quality, but the A1 (retrievable) criterion now reflects completeness against the full research dataset rather than just the deposited subset. Code scores 6/15, lacking findability or reusability infrastructure. These asymmetries confirm the decision to report data and code FAIR scores separately.

Three patterns emerge from the standardised scores. First, four of five papers score 4/4 on Accessibility for both data and code — open access publication through JAS ensures baseline accessibility regardless of repository choices. Key et al. is the exception: data Accessibility drops to 3/4 because A1 (retrievable via standard protocol) now assesses completeness against the full research dataset. Only 3 of 13 datasets are retrievable; the remaining 10 are gated behind co-author contact, closed monographs, or unpublished status (see correction note below). Second, Interoperable is the weakest dimension across the corpus: no paper uses FAIR vocabularies (I2), and only papers with Zenodo or CRAN deposits score on qualified references (I3). Third, the gap between Marwick's 14/15 and the cluster around 9-12/15 correlates with a specific infrastructure bundle: renv + Dockerfile + Zenodo archival + explicit licensing + literate programming. No single practice accounts for the gap; the combination does.

**Correction (v1.2, 2026-02-12):** Key et al. data FAIR revised from 9/15 to 8/15. The original assessment scored A1=1 because the supplement uses HTTPS, but this evaluated only the deposited subset. Reproduction attempt revealed that 10 of 13 datasets are inaccessible (co-author gatekeeping, closed monographs, unpublished). The A1 criterion now requires that a majority of research data be retrievable via standard protocol, with an exception for ethically restricted data.

## 5. Reproduction Outcomes

### 5.1 Summary

**Table 6. Reproduction verdicts**

| Paper | Verdict | Compute Time | Hands-on Time | Discrepancies | Wrapper Script |
|-------|---------|-------------|---------------|---------------|----------------|
| Crema et al. | SUCCESSFUL | ~18 h | ~3 h | 0 (within HPD) | No |
| Marwick | SUCCESSFUL | ~13 min | ~7 min | 1 (non-material) | No |
| Key et al. | PARTIAL | ~5 min | ~4 h | 2 major + 8 NaN | Yes |
| Herskind & Riede | SUCCESSFUL | ~30 s | ~50 min | 0 (exact) | Yes |
| Dye et al. | SUCCESSFUL | ~30 s | ~1.5 h | 0 (exact) | Yes |

All five papers' code ran successfully once we constructed an appropriate environment. The single PARTIAL verdict (Key et al.) stems entirely from data inaccessibility: only 3 of 13 datasets were publicly available, limiting reproduction to 2 of 7 results tables. Where data was available, the core Optimal Linear Estimation (OLE) outputs matched — the discrepancies were calculation errors in the paper's derived column, not reproduction failures.

### 5.2 Paper-by-Paper Narratives

**Crema et al. (2024)** provided a Dockerfile requiring two fixes (an `RColoBrewer` typo and a missing `rnaturalearthhires` package). We ran three Markov chain Monte Carlo (MCMC) case studies in parallel on a dedicated compute server. All posterior estimates fell within published 90% highest posterior density (HPD) intervals, and table values regenerated from pre-computed posteriors were byte-identical to the repository originals. The ~18-hour compute time reflects inherent MCMC demands, not infrastructure friction.

**Marwick (2025)** reproduced in 13 minutes with zero Dockerfile modifications — `docker build` triggered renv restore and manuscript rendering in a single step. The only discrepancy was a Kendall's tau p-value (4.08 × 10⁻⁷ reproduced vs 2.67 × 10⁻⁶ published), likely reflecting a minor data revision between drafting and final deposit. Both values are highly significant and the substantive conclusion is unaffected. This paper represents best-in-class reproducibility infrastructure.

**Key et al. (2024)** posed the greatest challenge. The supplementary R scripts use placeholder file paths (`"###file location###"`), assume interactive RStudio execution, and include non-analytical dependencies (the `beepr` package for audio notifications). We constructed a wrapper script to parameterise the OLE function across datasets. Of 13 datasets, only 3 (23.1%) were publicly accessible — the remainder sat behind co-author gatekeeping, closed-access monographs, or unpublished collections. Additionally, one supplement file (mmc4.csv) was empty (75 bytes, header only), representing a probable publishing error. Where data was available, we reproduced 116 of 118 comparable values (98.3%). The two discrepancies were Extension percentage calculation errors in Table 6: Midland Thickness reports 3.1% where the formula yields ~21%, and Clovis Mass reports 19.6% where the formula yields ~3.1%. These values appear transposed. Our adversarial review independently confirmed both as paper errors.

**Herskind & Riede (2024)** provided no Dockerfile or dependency management, but the analysis — frequency counts and pointwise mutual information (PMI) — is fully deterministic. We constructed a Docker image with R 4.2.2 and six packages, then wrote a wrapper to automate the interactive workflow (the original script requires manual re-execution with parameter changes). All 291 n-gram entries matched the published supplementary table to machine epsilon. The reproducibility here is a function of analytical simplicity rather than infrastructure quality.

**Dye et al. (2023)** required three Docker build iterations to resolve transitive system dependencies (ArchaeoPhases pulls in `igraph` and `proj4`, each requiring system libraries). The supplement's 38 incremental code sections, designed for interactive execution, needed assembly into a batch script. All 54 Allen algebra probability values matched Tables 2–10 exactly. The upstream OxCal dependency (proprietary) did not block reproduction because the paper's contribution is the ArchaeoPhases post-processing methodology; we verified this using the authors' pre-computed MCMC output.

### 5.3 Cross-Paper Findings

**Finding 1: Code ran in all five cases once we constructed an appropriate environment.** Data availability was the only barrier to full reproduction. This suggests that computational reproducibility failures in archaeology stem primarily from data access, not from broken code or inadequate environment specification.

**Finding 2: Deterministic analyses reproduce exactly regardless of environment specification quality.** Herskind & Riede (no Docker, no renv, no session info) and Dye et al. (no Docker, no version pinning) both reproduced to machine epsilon because their computations involve only deterministic operations. For stochastic analyses (MCMC, bootstrapping), environment under-specification would likely produce different numerical results. The implication is that environment specification requirements should be calibrated to analytical complexity.

**Finding 3: Infrastructure practices reduce hands-on effort but do not determine success or failure.** Marwick's comprehensive infrastructure (renv + Dockerfile + literate programming) yielded a 7-minute hands-on reproduction. Key's minimal infrastructure required 4 hours of wrapper script development. Yet both produced usable results where data was available. Infrastructure affects efficiency, not feasibility.

**Finding 4: Paper errors are discoverable through reproduction.** The two Extension percentage errors in Key et al. Table 6 would likely evade conventional peer review — they are in a derived column of a large results table. Value-by-value comparison during reproduction provides an effective error-detection mechanism that complements traditional review.

**Finding 5: ScienceDirect supplement access barriers affect machine-actionability.** Two papers (Key et al. and Dye et al.) host supplementary materials exclusively on ScienceDirect, which returns HTTP 403 for programmatic download. This forces manual retrieval and undermines automated reproduction pipelines. Supplements deposited in open repositories (Zenodo, GitHub) do not face this barrier.

## 6. Patterns and Observations

Three spectra emerged across the five papers that may structure Phase 2 analysis.

**Data availability** ranges from fully open to mostly inaccessible. Crema and Marwick deposit all analysis data in Zenodo alongside code. Herskind & Riede and Dye provide data through Zenodo and the Archaeology Data Service (ADS) respectively. Key aggregates datasets from 13 external sources, of which only 3 are publicly accessible — the remainder require tracing multi-hop citation chains through co-author collections and closed-access monographs. The strongest predictor of dataset accessibility across these five papers was independent publication in a repository subject to a data-sharing mandate, rather than aggregation from unpublished or gated sources.

**Environment specification** ranges from Dockerfile plus renv lockfile (Marwick) through Dockerfile alone with manual package installation (Crema), to R version stated in text (Key, Herskind & Riede), to nothing at all (Dye). Yet this gradient did not predict reproduction success in our pilot. It did predict hands-on effort: the two papers with Dockerfiles (Crema, Marwick) required the least human intervention to reproduce.

**Script design** ranges from literate programming that renders the manuscript inline (Marwick) through batch-ready scripts (Crema), to interactive scripts requiring parameter changes and manual re-execution (Herskind & Riede, Key), to incremental supplement sections needing assembly (Dye). Three of five papers required us to write wrapper scripts — a consistent friction point that literate programming and batch-ready design eliminate.

With only five papers, we cannot draw statistical conclusions about relationships between FAIR scores and reproduction effort. Qualitatively, Marwick's high FAIR scores (data 14/15, code 14/15) correlate with the lowest reproduction effort (7 minutes hands-on), while papers scoring 9-12/15 required 50 minutes to 4 hours. Whether this relationship holds at scale is a Phase 2 question.

## 7. Hypothesis Candidates for Phase 2

We propose five hypotheses derived from Phase 1 observations, each to be preregistered on the Open Science Framework (OSF) before Phase 2 corpus selection.

**H1: Policy effect on FAIR scores.** Papers published after JAS's January 2024 mandatory reproducibility review policy will have higher FAIR scores than papers published before the policy took effect. *Rationale:* Our corpus straddles the policy boundary (Dye 2023 pre-policy; Crema, Key, Herskind 2024 transitional; Marwick 2025 post-policy), and the highest FAIR score belongs to the most recent paper. *Proposed test:* Compare mean FAIR scores (data /15 and code /15, independently) between pre-policy and post-policy cohorts using the standardised v2.0 binary sub-principle scale.

**H2: Data availability as primary predictor.** Data availability (not code availability) will be the primary predictor of reproduction outcome. *Rationale:* All five pilot papers provided code in some form, yet the only PARTIAL verdict resulted from data inaccessibility. Code always ran once an environment was constructed. *Proposed test:* Logistic regression of reproduction verdict on data availability category, controlling for code availability and environment specification.

**H3: Pinned dependencies reduce build effort.** Papers with pinned dependency management (renv, conda-lock, or equivalent) will require fewer Docker build iterations than papers with ad hoc dependency specification. *Rationale:* Marwick's renv lockfile built without errors in one iteration; Dye's unmanaged dependencies required three iterations to resolve transitive system library requirements. *Proposed test:* Compare Docker build iteration counts between papers with and without pinned dependency management.

**H4: Determinism enables exact reproduction.** Deterministic analyses will reproduce exactly (within floating-point precision) regardless of environment specification quality. *Rationale:* Both Herskind & Riede (no environment specification) and Dye (no version pinning) reproduced to machine epsilon because their computations are deterministic. Crema's stochastic MCMC analysis produced expected variation. *Proposed test:* Cross-tabulate analytical determinism against reproduction precision category (exact match / within tolerance / material discrepancy).

**H5: Literate programming improves transparency.** Papers using literate programming (RMarkdown, Quarto, Jupyter) will score higher on the Transparency credibility signal than papers with standalone scripts. *Rationale:* Marwick's literate programming approach achieved the highest Transparency score (90) and the lowest reproduction effort. Literate programming weaves narrative and code, making analytical decisions visible in context. *Proposed test:* Compare Transparency signal scores between literate programming and standalone script groups.

## 8. Methodological Reflections

### 8.1 What Worked

The Docker-based reproduction protocol with structured comparison proved effective for all five papers. Containerisation isolated each reproduction from the host environment, making results portable and auditable. The four-session reproduction workflow — planning, preparation, execution and verification, adversarial review — provided natural checkpoints and forced fresh-context sceptical evaluation of results.

Session-per-pass extraction delivered richer structured data than single-session autonomous extraction. The run comparison on Crema et al. demonstrated 75% more claims and 100% more research designs captured. Each focused session produces deeper engagement with specific extraction targets. A 25-run variability test (5 papers × 5 runs) confirmed the reliability of this approach: classification was 100% stable across runs, and aggregate credibility scores showed coefficients of variation of 1.9–3.4%.

### 8.2 What Needs Refinement

Two areas require attention before Phase 2. First, wrapper script effort needs systematic documentation as a reproduction metric; three of five papers required substantial wrapper development, and this effort should be captured quantitatively. Second, a data availability taxonomy would strengthen H2 testing — our current categories (open, gated, unavailable) are insufficiently granular to capture the multi-hop provenance chains we encountered with Key et al. A third issue — FAIR scoring scale standardisation — has been resolved: all five pilot papers have been re-scored using 15 binary GO-FAIR sub-principles with independent data/code assessments (see Section 4.2).

## 9. Limitations

This pilot assessed five papers from a single journal, selected with deliberate bias toward papers with visible computational components. The corpus is too small for inferential statistics, and our selection strategy likely overrepresents papers with better-than-average open science practices — papers without any code or data mention were excluded by design. Phase 2 should include a random sampling component alongside purposive selection.

All assessments were conducted by a single assessor using LLM-assisted extraction. While the 25-run variability test demonstrates high reliability (100% classification stability, aggregate score CV 1.9–3.4%), we have not established inter-rater reliability against human assessors. All reproductions were limited to R-based analyses; our pipeline has not been tested against Python, Julia, or mixed-language projects. FAIR scores have been standardised to a 15-point binary sub-principle scale with independent data/code scoring (v1.1), resolving the scale inconsistency present in v1.0 of this report.

## Appendix References

Per-paper reproduction detail is available in:

- `studies/open-science-compliance/outputs/crema-et-al-2024/reproduction/attempt-01/comparisons/comparison-report.md`
- `studies/open-science-compliance/outputs/marwick-2025/reproduction/attempt-01/comparisons/comparison-report.md`
- `studies/open-science-compliance/outputs/key-et-al-2024/reproduction/attempt-01/comparisons/comparison-report.md`
- `studies/open-science-compliance/outputs/herskind-riede-2024/reproduction/attempt-01/comparisons/comparison-report.md`
- `studies/open-science-compliance/outputs/dye-et-al-2023/reproduction/attempt-01/comparisons/comparison-report.md`

Per-paper credibility assessments are in each paper's `assessment/` directory.

Cross-paper reproduction synthesis: `planning/reproduction-implementation-notes.md`
