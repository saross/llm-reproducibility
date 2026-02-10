# Reproduction Plan Guide

**Version:** 1.0.0
**Date:** 2026-02-10
**Purpose:** Flexible planning model for paper-specific reproduction workflows
**Scope:** R-based computational analyses (v1.0)

---

## Overview

This guide provides a flexible framework for planning reproductions across diverse paper types. Each paper presents unique challenges — different code availability, environment specifications, data access patterns, and analytical approaches. The planning session (R-Plan) uses this guide to produce a paper-specific execution plan.

**Key principle:** Universal process with paper-specific adaptation. The same 4-session workflow applies, but the plan within each session varies by paper.

---

## Part 1: Paper Landscape Analysis

Before writing the reproduction plan, analyse the paper's computational landscape.

### 1.1 Code Location

Where is the analysis code?

| Source | Reliability | Example |
|--------|------------|---------|
| GitHub repository | High — version controlled, citable | Crema et al. 2024 |
| Zenodo deposit | High — persistent DOI, archived | Herskind & Riede 2024 |
| Journal supplement (PDF) | Medium — accessible but not machine-actionable | Dye et al. 2023 |
| Personal website | Low — single point of failure | — |
| "Available on request" | Very low — may not be honoured | — |

**Action:** Clone/download the code. Note any access barriers.

### 1.2 Data Availability

Where is the input data?

| Source | Reliability | Action |
|--------|------------|--------|
| Included in repository | High | Verify completeness |
| Zenodo/Figshare deposit | High | Download, verify checksums |
| Remote server (author's) | Low | Download local copy, note persistence risk |
| Journal supplement | Medium | Download, note access method |
| External database with DOI | High | Document retrieval steps |
| Proprietary/restricted | Blocking | Assess whether pre-computed intermediates exist |

### 1.3 Environment Specification

What environment information does the paper provide?

| Level | What It Provides | Example |
|-------|-----------------|---------|
| Dockerfile + renv.lock | Complete reproducible environment | Marwick 2025 |
| Dockerfile only | System deps + R version, packages may drift | Crema et al. 2024 |
| renv.lock only | Package versions, no system deps | — |
| DESCRIPTION file | Package list, minimal versions | — |
| sessionInfo() in paper | R version + loaded packages | — |
| R version in text | R version only | Herskind & Riede 2024 |
| Nothing | Must infer from paper date and package versions | Dye et al. 2023 |

### 1.4 Script Execution Mode

How is the analysis designed to be run?

| Mode | Indicators | Adaptation Needed |
|------|-----------|-------------------|
| Batch-ready | `Rscript analysis.R` works | None |
| Literate programming | `.Rmd` / `.qmd` with inline code | `rmarkdown::render()` |
| Interactive (RStudio) | `View()`, manual parameter changes, commenting | Wrapper script |
| Incremental sections | Numbered code blocks in supplement PDF | Assemble + wrapper |

---

## Part 2: Reproduction Type Classification

Based on the landscape analysis, classify the reproduction into one or more types:

### Type A: Batch-Ready with Dockerfile

**Indicators:** GitHub repo with Dockerfile (and ideally renv.lock). Scripts designed for command-line execution.

**Effort:** Lowest. Build Docker image, run analysis, compare.

**Plan focus:** Verify Dockerfile builds. Identify any missing packages. Set up output comparison.

**Example:** Marwick 2025 — `docker build` renders the manuscript with zero modifications.

### Type B: Batch-Ready without Dockerfile

**Indicators:** GitHub repo with R scripts. No Dockerfile but scripts run from command line.

**Effort:** Moderate. Construct Dockerfile, resolve dependencies, then run.

**Plan focus:** Identify R version. Map package dependencies. Construct Dockerfile iteratively.

**Example:** Crema et al. 2024 — author Dockerfile had 2 issues; scripts were batch-ready.

### Type C: Interactive Scripts without Dockerfile

**Indicators:** R scripts designed for RStudio. Parameters changed by editing script. No output saving.

**Effort:** Higher. Write wrapper script for batch execution, construct Dockerfile.

**Plan focus:** Understand the interactive workflow. Design parameterised wrapper. Identify all output targets.

**Examples:** Herskind & Riede 2024 (parameter-change pattern), Dye et al. 2023 (incremental sections).

### Type D: Proprietary Upstream

**Indicators:** Analysis depends on output from proprietary/commercial software (e.g., OxCal, ArcGIS).

**Effort:** Variable. Depends on whether pre-computed intermediates are available.

**Plan focus:** Define reproduction scope boundary. Identify pre-computed intermediates. Document what cannot be reproduced and why.

**Example:** Dye et al. 2023 — OxCal MCMC generation not reproduced; ArchaeoPhases post-processing fully verified.

**Note:** A paper may be multiple types (e.g., Dye is both C and D).

---

## Part 3: Verification Target Identification

Enumerate every quantitative and qualitative result to verify.

### 3.1 Quantitative Targets

For each paper table, figure, or reported statistic:

| Target | Location | Type | Values | Classification |
|--------|----------|------|--------|----------------|
| Table 1: Summary statistics | p. 5 | Table | 12 values | Deterministic |
| Figure 3: PCA biplot | p. 8 | Figure | Visual | Deterministic |
| p-value for Kendall's tau | p. 6, Results | Statistic | 1 value | Stochastic (GAM) |
| Table 7.18: Allen algebra | Supplement | Table | 54 values | Deterministic |

### 3.2 Classification Rationale

For each target, determine whether it is deterministic or stochastic:

- **Deterministic:** Frequency counts, proportions, logarithms, post-processing of fixed inputs, exact algorithms
- **Stochastic:** MCMC posteriors, bootstrap statistics, cross-validation, permutation tests, random forest importance

### 3.3 Priority Ordering

If time-constrained, which targets are most important?

1. Core results tables (the paper's main contribution)
2. Key statistics reported in the abstract or conclusions
3. Supplementary tables and figures
4. Intermediate results (only if discrepancies found in final outputs)

---

## Part 4: Risk Identification

### Common Risks

| Risk | Likelihood | Mitigation |
|------|-----------|------------|
| Missing system dependencies | High (Types B, C) | Iterative Docker builds; common deps table |
| Data on personal server | Medium | Download local copy; note persistence risk |
| Supplement behind paywall | Medium | Try CDN URL patterns; manual download |
| Interactive script design | High (Type C) | Write parameterised wrapper |
| Proprietary upstream | Low-Medium | Scope to open components; use intermediates |
| Long compute time (>24h) | Low | Use sapphire; detached Docker containers |
| R version mismatch | Low | Usually warning, not failure |
| Package removed from CRAN | Very low | Check CRAN archive; use r-universe |

### Paper-Specific Risks

Identify risks unique to this paper. Examples from pilot:

- Dye: MCMC data on personal domain (tsdye.online)
- Dye: Supplement on ScienceDirect (HTTP 403 for programmatic access)
- Herskind: Ampersand in original filenames
- Crema: Missing rnaturalearthhires (not on CRAN)

---

## Part 5: Compute Estimation

### Runtime Categories

| Category | Estimate | Resource |
|----------|----------|----------|
| Trivial | < 5 minutes | Local Docker |
| Quick | 5-60 minutes | Local Docker |
| Moderate | 1-6 hours | Local or sapphire |
| Long | 6-24 hours | Sapphire |
| Very long | 24+ hours | Sapphire (detached) |

### Resource Requirements

- **CPU:** Single-threaded R unless explicitly parallelised. MCMC chains typically use ~100% per chain.
- **Memory:** Most R analyses use < 8 GB. Large spatial/genomic analyses may need more.
- **Disk:** Volume mounts for output persistence. Check data file sizes.

---

## Part 6: Plan Document Output

The planning session produces a concrete plan document with these sections:

### Plan Template

```markdown
# Reproduction Plan: {paper-slug}

## Paper
{Full citation with DOI}

## Classification
- **Type:** {A/B/C/D or combination}
- **Determinism:** {Deterministic / Stochastic / Mixed}
- **Runtime estimate:** {category}
- **Resource:** {Local / Sapphire}

## Materials
- **Code:** {location, access method}
- **Data:** {location, access method, size}
- **Supplements:** {location, access method}
- **Environment spec:** {what the paper provides}

## Execution Steps (Session R-A)
1. {Numbered step with expected output}
2. {Next step}
...

## Verification Targets (Session R-B)
| Target | Location | Values | Classification |
|--------|----------|--------|----------------|
| {target} | {page/table} | {N} | {det/stoch} |

## Risks and Mitigations
| Risk | Mitigation |
|------|------------|
| {risk} | {mitigation} |

## Scope Limitations
- {What will NOT be reproduced and why}
```

**This plan is reviewed and approved by the user before execution begins.**

---

## Extension Points (Future Versions)

### Python Support (v2.0)

- Base images: `python:{version}-slim` or `jupyter/scipy-notebook`
- Environment: `requirements.txt`, `environment.yml` (conda), `pyproject.toml`
- Execution: `python analysis.py` or `jupyter nbconvert --execute`
- Package management: pip, conda, poetry

### Julia Support (v2.0)

- Base images: `julia:{version}`
- Environment: `Project.toml` + `Manifest.toml`
- Execution: `julia --project=. analysis.jl`
- Package management: Pkg.instantiate()

---

*Last updated: 2026-02-10*
