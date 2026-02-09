# Reproduction Comparison Report: Crema et al. (2024)

**Paper:** Crema, E.R., Bloxam, A., Stevens, C.J., & Vander Linden, M. (2024). "Modelling
diffusion of innovation curves using radiocarbon data." *Journal of Archaeological Method and
Theory*.

**Repository:** <https://github.com/ercrema/diffusionCurve>

**Reproduction date:** 2026-02-08 to 2026-02-09

---

## Environment

### Original (from paper sessionInfo)

- R 4.3.1
- nimble 1.0.1
- nimbleCarbon 0.2.4
- CPU: Intel Xeon W-2295 (18C/36T), 128 GB RAM
- Estimated runtime: 120-150 hours total

### Reproduction

- R 4.3.3 (via `rocker/rstudio:4.3.3` Docker image)
- nimble 1.1.0
- nimbleCarbon 0.2.5
- CPU: AMD Ryzen 9 7900 (12C/24T), 64 GB RAM
- Docker v28.4.0 on Ubuntu 25.04 (sapphire compute server)
- Actual runtime: ~5-8 hours per analysis (~18h total for 3 parallel runs)

### Environment Differences

| Component | Original | Reproduction | Impact |
|-----------|----------|--------------|--------|
| R version | 4.3.1 | 4.3.3 | Minor patch; no API changes |
| nimble | 1.0.1 | 1.1.0 | Minor version bump |
| nimbleCarbon | 0.2.4 | 0.2.5 | Patch update |
| CPU | Intel Xeon W-2295 | AMD Ryzen 9 7900 | Faster single-thread; ~3-5x speedup |
| OS | Not specified | Ubuntu 25.04 (Docker) | Docker isolates R environment |

The Dockerfile's CRAN snapshot date (2024-04-23) means the reproduction installed package
versions available at that date rather than the exact versions from the paper's sessionInfo.
The nimble minor version bump (1.0.1 to 1.1.0) is the most significant difference but does
not change the MCMC algorithm or model specification.

---

## Table 1: Parameter Comparison

### Japan (Sigmoid Model)

| Parameter | Published (table1.csv) | From Precomputed | Fresh MCMC | Published 90% HPD | Fresh within HPD? |
|-----------|------------------------|------------------|------------|--------------------|--------------------|
| r | 0.1003 | 0.1003 | 0.1011 | 0.0123~0.3378 | Yes |
| m | BC844 | BC844 | BC844 | BC894~BC809 | Yes |
| mu | 0.701 | 0.701 | 0.704 | 0.47~0.934 | Yes |
| phi | 0.75 | 0.75 | 0.75 | 0.18~1.68 | Yes |

### Britain (Sigmoid Model)

| Parameter | Published (table1.csv) | From Precomputed | Fresh MCMC | Published 90% HPD | Fresh within HPD? |
|-----------|------------------------|------------------|------------|--------------------|--------------------|
| r | 0.0135 | 0.0135 | 0.0135 | 0.0016~0.0383 | Yes |
| m | BC4054 | BC4054 | BC4053 | BC4360~BC3849 | Yes |
| mu | 0.182 | 0.182 | 0.182 | 0.009~0.418 | Yes |
| phi | 0.31 | 0.31 | 0.31 | 0.1~0.58 | Yes |

### Interpretation

**Pre-computed results** are identical to published table1.csv, confirming the output pipeline
is deterministic given fixed posteriors.

**Fresh MCMC results** show excellent agreement:

- **Japan r:** 0.1011 vs 0.1003 (0.8% difference) — well within HPD
- **Japan m:** BC844 vs BC844 — identical median
- **Japan mu:** 0.704 vs 0.701 (0.4% difference) — well within HPD
- **Japan phi:** 0.75 vs 0.75 — identical median
- **Britain:** All four parameters match to the reported precision (r, mu, phi identical;
  m differs by 1 year: BC4053 vs BC4054)

The stochastic variation between the original and fresh MCMC runs is minimal, reflecting
the large sample sizes (4 chains x 1M iterations for sigmoid models) which yield stable
posterior summaries.

---

## MCMC Convergence

### Published Rhat Values

| Region | Parameter | Published Rhat | Fresh Rhat |
|--------|-----------|----------------|------------|
| Japan | r | 1 | 1.0007 |
| Japan | m | 1.0003 | 1.0015 |
| Japan | mu | 1 | 1.0002 |
| Japan | phi | 1.0004 | 1.0002 |
| Britain | r | 1.0001 | 1 |
| Britain | m | 1.0005 | 1 |
| Britain | mu | 1.0002 | 1 |
| Britain | phi | 1 | 1.0001 |

All Rhat values are below 1.01 in both published and fresh runs, indicating excellent
convergence. The fresh runs show equivalently good mixing.

---

## HPD Interval Comparison

### Japan

| Parameter | Published HPD | Fresh HPD | Overlap |
|-----------|---------------|-----------|---------|
| r | 0.0123~0.3378 | 0.0124~0.3405 | Near-identical |
| m | BC894~BC809 | BC894~BC809 | Identical |
| mu | 0.47~0.934 | 0.479~0.938 | Near-identical |
| phi | 0.18~1.68 | 0.18~1.66 | Near-identical |

### Britain

| Parameter | Published HPD | Fresh HPD | Overlap |
|-----------|---------------|-----------|---------|
| r | 0.0016~0.0383 | 0.0013~0.0376 | Near-identical |
| m | BC4360~BC3849 | BC4362~BC3853 | Near-identical |
| mu | 0.009~0.418 | 0.009~0.423 | Near-identical |
| phi | 0.1~0.58 | 0.1~0.58 | Identical |

All HPD intervals show excellent overlap, with differences only in the last reported
significant figure. This is expected stochastic variation for independent MCMC runs.

---

## Figure Comparison

All 5 main figures were regenerated from both pre-computed and fresh MCMC posteriors.

| Figure | Description | Pre-computed | Fresh MCMC | Match |
|--------|-------------|-------------|------------|-------|
| Figure 1 | Diffusion curves (3 panels) | Generated | Generated | Visually identical |
| Figure 2 | Site distribution maps (3 panels) | Generated | Generated | Identical (deterministic) |
| Figure 3 | Japan posterior predictive check | Generated | Generated | Visually identical |
| Figure 4 | Britain posterior predictive check | Generated | Generated | Visually identical |
| Figure 5 | Burial cremation proportions | Generated | Generated | Visually identical |

Figure 2 (site maps) is deterministic and identical between runs. Figures 1, 3-5 show
the expected near-identical patterns: same shapes, same qualitative features, with only
imperceptible differences in the uncertainty envelopes due to stochastic variation in the
posteriors.

---

## Runtime Comparison

| Analysis | Published Estimate | Actual (Sapphire) | Speedup |
|----------|--------------------|--------------------|---------|
| Japan sigmoid | ~24 hours | ~5.5 hours | ~4.4x |
| Britain sigmoid | ~24 hours | ~9 hours | ~2.7x |
| Burial ICAR | ~24 hours | ~5.5 hours | ~4.4x |
| Post-check (Japan) | ~25 min | ~15 min | ~1.7x |
| Post-check (Britain) | ~25 min | ~20 min | ~1.3x |

The Ryzen 9 7900's faster single-threaded performance (compared to the Xeon W-2295)
accounts for the substantial speedup. Britain took longer likely due to its larger dataset.

---

## Dockerfile Issues

Two issues found in the authors' Dockerfile:

1. **Typo:** `RColoBrewer` should be `RColorBrewer` (line 11). Build fails without fix.
2. **Missing package:** `rnaturalearthhires` (GitHub-only data package) required for map
   figures but not installed. Must be installed at runtime via
   `remotes::install_github("ropensci/rnaturalearthhires")`.

Neither issue affects MCMC analyses or Table 1 — only figure generation. Both are trivial
to work around.

---

## Verdict

**Reproduction status: SUCCESSFUL**

All three empirical MCMC case studies (Japan sigmoid, Britain sigmoid, burial ICAR)
reproduce successfully:

1. **Table 1 from pre-computed posteriors** is byte-for-byte identical to the published
   table1.csv
2. **Table 1 from fresh MCMC** shows all parameters within published 90% HPD intervals,
   with most medians matching to 2-3 significant figures
3. **All figures** regenerate without errors from both pre-computed and fresh posteriors
4. **MCMC convergence** (Rhat) is excellent in fresh runs (all < 1.002)
5. **HPD intervals** overlap almost completely between published and fresh results

The minor Dockerfile issues (typo + missing package) are documentation-level problems that
do not affect the substantive reproducibility of the analyses. The code, data, and
computational pipeline are well-structured and produce consistent results across different
hardware and slightly different software versions.

This outcome supports the extraction assessment's Reproducibility score of 90/100 and
overall "Excellent" credibility verdict.

---

## Files

| File | Description |
|------|-------------|
| `outputs/table1-reproduced.csv` | Table 1 from pre-computed posteriors (Phase 1) |
| `outputs/table1-fresh-mcmc.csv` | Table 1 from fresh MCMC posteriors (Phase 2) |
| `outputs/figures-from-precomputed/` | Figures 1-5 + S1-S6 from pre-computed (Phase 1) |
| `outputs/figures-from-fresh-mcmc/` | Figures 1-5 from fresh MCMC (Phase 2) |
| `outputs/logs/` | MCMC log files from all 3 analyses |

---

*Report generated: 2026-02-09*
