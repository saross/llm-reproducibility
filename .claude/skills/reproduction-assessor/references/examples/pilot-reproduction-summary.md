# Pilot Reproduction Summary

Condensed patterns from 5 completed reproductions in the Open Science Compliance Study.
Use as a reference for expected challenges, effort levels, and verification strategies.

## Overview

| Paper | Type | Dockerfile | Runtime | Discrepancies | Verdict |
|-------|------|------------|---------|---------------|---------|
| Crema et al. 2024 | B (batch, no good Dockerfile) | Author-provided (2 fixes) | ~18h (MCMC) | 0 (within HPD) | SUCCESSFUL |
| Marwick 2025 | A (batch, Dockerfile + renv) | Author-provided (0 fixes) | ~13 min | 1 (minor) | SUCCESSFUL |
| Herskind & Riede 2024 | C (interactive, no Dockerfile) | Constructed (1 iteration) | ~30s | 0 (exact) | SUCCESSFUL |
| Dye et al. 2023 | C+D (incremental, proprietary upstream) | Constructed (3 iterations) | ~30s | 0 (exact) | SUCCESSFUL |
| Key et al. 2024 | C (interactive, aggregated data) | Constructed (1 iteration) | ~5s | 2 (paper errors) + 8 NaN | PARTIAL |

**Summary statistics:** 5 papers attempted, 4 SUCCESSFUL, 1 PARTIAL. Mean hands-on time
~1.8 hours.

## Key Patterns

### Effort Scales with Script Type, Not Analysis Complexity

- **Batch-ready + Dockerfile** (Marwick): ~20 min total hands-on
- **Batch-ready + broken Dockerfile** (Crema): ~3h hands-on + compute wait
- **Interactive → wrapper** (Herskind): ~50 min hands-on
- **Incremental sections → wrapper** (Dye): ~1.5h hands-on
- **Interactive + data scoping** (Key): ~3h hands-on (data inventory + wrapper + verification)

### Docker Build Iterations

- Crema: 1 iteration (typo fix + missing package)
- Marwick: 0 iterations (perfect Dockerfile)
- Herskind: 1 iteration (constructed from scratch, straightforward deps)
- Dye: 3 iterations (transitive deps: igraph → libglpk, proj4 → libproj + libgdal)
- Key: 1 iteration (constructed, base R only — no external packages needed)

**Pattern:** Expect 1-3 iterations when constructing Dockerfiles. Transitive system
dependencies are the main source of failures. Base-R-only papers may need 0-1 iterations.

### Determinism Compensates for Missing Infrastructure

Herskind, Dye, and Key all lacked Dockerfiles, renv, and version pinning. All three
reproduced deterministic analyses exactly because there is no source of variation in a
deterministic pipeline. For stochastic analyses (MCMC, bootstrap), missing infrastructure
would likely produce different numerical results.

### Data Availability as Primary Bottleneck

Key et al. 2024 demonstrated that for papers with aggregated datasets from multiple
sources, data accessibility — not code quality — is the primary bottleneck:

- 13 datasets from 13 different sources
- Only 3 datasets accessible (Level 0): 42.6% of records
- 9 datasets at Level 3 (co-author-held), 1 at Level 4 (never published)
- Result: PARTIAL verdict despite 98.3% match rate on comparable values

**Pattern:** For multi-dataset papers, conduct a data availability inventory during
R-Plan. Use the 5-level access taxonomy (Level 0 = fully accessible through Level 4 =
never published) and quantify both dataset-weighted and record-weighted availability.

### Verification Strategy Depends on Analysis Type

- **Deterministic:** Exact match expected and achieved (Herskind: 291/291, Dye: 54/54,
  Key: 116/118 comparable)
- **Stochastic (pre-computed):** Deterministic if using same MCMC draws (Crema Phase 1)
- **Stochastic (fresh):** Within HPD intervals (Crema Phase 2)
- **Regression:** Minor p-value differences acceptable if conclusions unchanged (Marwick)
- **Cannot compare:** NaN from undocumented preprocessing; classify as CANNOT_COMPARE,
  not MAJOR_DISCREPANCY (Key: 8 NaN values)

### Paper Error Detection

Reproductions can reveal errors in published papers. Key et al. 2024 found 2 Extension%
values in Table 6 that are internally inconsistent with the paper's own tabulated
min/max values:

- Midland Thickness Extension: paper reports 3.1%, formula yields ~20%
- Clovis Mass Extension: paper reports 19.6%, formula yields ~3.1%

**Pattern:** When a reproduced value disagrees with a published value, verify
independently by applying the stated formula to the paper's own tabulated inputs. If the
formula produces the reproduced value, classify as PAPER_ERROR (not MAJOR_DISCREPANCY).

### Common Gotchas

1. **Interactive scripts** — Most common barrier. Look for: `View()`, manual parameter
   changes, no output saving
2. **System dependencies** — R packages with C/C++ backends need system libraries in
   Docker
3. **Data on personal servers** — Single point of failure for long-term reproducibility
4. **Supplement access** — ScienceDirect blocks programmatic download (HTTP 403)
5. **Column index shifts** — Data processing functions that drop/add columns change
   positional indices
6. **`.here` sentinel** — Volume-mounted directories lack `.git`, so `here::here()` fails
7. **Font dependencies** — Proprietary fonts unavailable in Docker; accept fallback fonts
8. **Filename characters** — Ampersands and special characters cause Docker mount issues
9. **Empty supplement files** — Publishing errors can produce empty or header-only files
   (Key: mmc4.csv, 75 bytes)
10. **Interactive placeholders** — Supplement scripts may use placeholder patterns like
    `###file location###` that require manual substitution
11. **Undocumented preprocessing** — Original analyses may include undocumented data
    cleaning steps (duplicate removal, outlier filtering) that are not captured in the
    published scripts
12. **Missing `set.seed()`** — Stochastic scripts without fixed random seeds cannot be
    exactly reproduced; use distributional checks instead

### Proprietary Upstream Software

Dye et al. 2023 demonstrated that proprietary upstream tools (OxCal) need not block
reproduction of the paper's analytical contribution. The key distinction: reproduce the
paper's novel analysis, document what upstream processing cannot be reproduced, and use
pre-computed intermediates where available.

### Scope Limitation Categories

Four distinct categories emerged from the pilot:

1. **Proprietary upstream** (Dye → OxCal) — not a FAIR failure
2. **Data unavailability** (Key → 10/13 datasets) — FAIR failure
3. **Stochastic non-reproducibility** (Key → no `set.seed()`) — design limitation
4. **Publishing errors** (Key → mmc4.csv empty) — journal process failure

Each has different implications for the verdict and documentation. See the verification
strategies reference for detailed guidance.

## Reproduction Type Quick Reference

| Type | Indicators | First Steps |
|------|-----------|-------------|
| **A** | GitHub repo with Dockerfile + renv/DESCRIPTION | Clone, build, run |
| **B** | GitHub repo with scripts, no Dockerfile | Identify R version, construct Dockerfile, resolve deps |
| **C** | Interactive R scripts (supplement or Zenodo) | Write wrapper script, construct Dockerfile |
| **D** | Analysis depends on proprietary tool output | Identify pre-computed intermediates, scope reproduction to open components |

## Notes on Pilot Coverage

Crema et al. 2024 and Marwick 2025 were reproduced before the reproduction-assessor skill
v1.0 was formalised. Their queue.yaml entries record verdicts and metadata but their
artefact directories were not persisted to the repository. These reproductions also
predate the adversarial review (R-C) session requirement.

Herskind & Riede 2024 and Dye et al. 2023 have complete R-A and R-B artefacts but
predate the R-C formalisation.

Key et al. 2024 is the only paper with the complete 4-session workflow including the
adversarial review.
