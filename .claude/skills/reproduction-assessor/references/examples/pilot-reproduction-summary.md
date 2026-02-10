# Pilot Reproduction Summary

Condensed patterns from 4 completed reproductions in the Open Science Compliance Study. Use as a reference for expected challenges, effort levels, and verification strategies.

## Overview

| Paper | Type | Dockerfile | Runtime | Discrepancies | Verdict |
|-------|------|------------|---------|---------------|---------|
| Crema et al. 2024 | B (batch, no good Dockerfile) | Author-provided (2 fixes) | ~18h (MCMC) | 0 (within HPD) | SUCCESSFUL |
| Marwick 2025 | A (batch, Dockerfile + renv) | Author-provided (0 fixes) | ~13 min | 1 (minor) | SUCCESSFUL |
| Herskind & Riede 2024 | C (interactive, no Dockerfile) | Constructed (1 iteration) | ~30s | 0 (exact) | SUCCESSFUL |
| Dye et al. 2023 | C+D (incremental, proprietary upstream) | Constructed (3 iterations) | ~30s | 0 (exact) | SUCCESSFUL |

## Key Patterns

### Effort Scales with Script Type, Not Analysis Complexity

- **Batch-ready + Dockerfile** (Marwick): ~20 min total hands-on
- **Batch-ready + broken Dockerfile** (Crema): ~3h hands-on + compute wait
- **Interactive → wrapper** (Herskind): ~50 min hands-on
- **Incremental sections → wrapper** (Dye): ~1.5h hands-on

### Docker Build Iterations

- Crema: 1 iteration (typo fix + missing package)
- Marwick: 0 iterations (perfect Dockerfile)
- Herskind: 1 iteration (constructed from scratch, straightforward deps)
- Dye: 3 iterations (transitive deps: igraph → libglpk, proj4 → libproj + libgdal)

**Pattern:** Expect 1-3 iterations when constructing Dockerfiles. Transitive system dependencies are the main source of failures.

### Determinism Compensates for Missing Infrastructure

Herskind and Dye both lacked Dockerfiles, renv, and version pinning. Both reproduced exactly because their analyses are deterministic. For stochastic analyses (MCMC, bootstrap), missing infrastructure would likely produce different numerical results.

### Verification Strategy Depends on Analysis Type

- **Deterministic:** Exact match expected and achieved (Herskind: 291/291, Dye: 54/54)
- **Stochastic (pre-computed):** Deterministic if using same MCMC draws (Crema Phase 1)
- **Stochastic (fresh):** Within HPD intervals (Crema Phase 2)
- **Regression:** Minor p-value differences acceptable if conclusions unchanged (Marwick)

### Common Gotchas

1. **Interactive scripts** — Most common barrier. Look for: `View()`, manual parameter changes, no output saving
2. **System dependencies** — R packages with C/C++ backends need system libraries in Docker
3. **Data on personal servers** — Single point of failure for long-term reproducibility
4. **Supplement access** — ScienceDirect blocks programmatic download (HTTP 403)
5. **Column index shifts** — Data processing functions that drop/add columns change positional indices
6. **`.here` sentinel** — Volume-mounted directories lack `.git`, so `here::here()` fails
7. **Font dependencies** — Proprietary fonts unavailable in Docker; accept fallback fonts
8. **Filename characters** — Ampersands and special characters cause Docker mount issues

### Proprietary Upstream Software

Dye et al. 2023 demonstrated that proprietary upstream tools (OxCal) need not block reproduction of the paper's analytical contribution. The key distinction: reproduce the paper's novel analysis, document what upstream processing cannot be reproduced, and use pre-computed intermediates where available.

## Reproduction Type Quick Reference

| Type | Indicators | First Steps |
|------|-----------|-------------|
| **A** | GitHub repo with Dockerfile + renv/DESCRIPTION | Clone, build, run |
| **B** | GitHub repo with scripts, no Dockerfile | Identify R version, construct Dockerfile, resolve deps |
| **C** | Interactive R scripts (supplement or Zenodo) | Write wrapper script, construct Dockerfile |
| **D** | Analysis depends on proprietary tool output | Identify pre-computed intermediates, scope reproduction to open components |
