# Comparison Report — Herskind & Riede 2024

## Verdict: SUCCESSFUL

All 291 n-gram entries (165 bigrams + 106 trigrams + 20 quadrigrams) match the authors'
pre-computed reference data (S3.xlsx) to full IEEE 754 double-precision floating-point
accuracy. Row counts, motif keys, token frequencies, observed frequencies, expected
frequencies, PMI values, and sort ordering are all identical.

---

## Paper Information

- **Title:** A computational linguistic methodology for assessing semiotic structure in
  prehistoric art and the meaning of southern Scandinavian Mesolithic ornamentation
- **Authors:** Herskind, L.L.P. & Riede, F.
- **Journal:** Journal of Archaeological Science, 165, 105969 (2024)
- **DOI:** 10.1016/j.jas.2024.105969
- **Zenodo deposit:** https://doi.org/10.5281/zenodo.10623550

## Methodology

### What Was Reproduced

The analysis applies k-skip-n-gram models (k=0:13) at three n-gram levels (bigrams,
trigrams, quadrigrams) to a corpus of 483 Mesolithic decorated objects from southern
Scandinavia. For each n-gram, Pointwise Mutual Information (PMI) is calculated as
`log(observed_freq / expected_freq)`, where expected frequency is derived from individual
motif frequencies under an independence assumption.

### How It Was Reproduced

1. **Downloaded** all 3 files from Zenodo deposit (S1.xlsx, S2.R, S3.xlsx)
2. **Examined** the original R script (S2.R) — found it was designed for interactive
   execution, not batch mode
3. **Constructed** a Docker environment using `rocker/r-ver:4.2.2` with 6 R packages
   (no Docker or environment specification was provided by the authors)
4. **Wrote** an automated wrapper script (`run-analysis.R`) that encapsulates the
   interactive workflow into callable functions
5. **Executed** the wrapper script in Docker
6. **Compared** all outputs against the pre-computed S3.xlsx reference data

### Modifications Required

| Modification | Type | Impact |
|-------------|------|--------|
| Wrapper script written | Structural | Automates interactive workflow; no algorithmic changes |
| Font fallback (Gill Sans MT → sans) | Aesthetic | Visual only; no computational impact |
| File renamed (S1.xlsx) | Practical | Docker compatibility; no analytical impact |

**No algorithmic modifications were made.** All mathematical operations (tokenisation,
skip-gram generation, frequency counting, PMI calculation) are identical to the original
S2.R.

## Quantitative Comparison

### Table Verification (S3.xlsx Reference)

| N-gram Level | Reference Rows | Reproduction Rows | Matched | Max |PMI diff| |
|-------------|---------------|-------------------|---------|------------------|
| Bigrams | 165 | 165 | 165 | 5.03 × 10⁻¹⁷ |
| Trigrams | 106 | 106 | 106 | 0.00 |
| Quadrigrams | 20 | 20 | 20 | 0.00 |

All differences are below IEEE 754 machine epsilon (~1.11 × 10⁻¹⁶). The reproduction
is exact.

### Top PMI Values (Verification)

| Rank | N-gram | Motifs | PMI | Observed Freq |
|------|--------|--------|-----|---------------|
| 1 | Quadrigram | C1, C4, C5, C12 | 7.925 | 3 |
| 2 | Trigram | C4, C5, C12 | 6.575 | 3 |
| 3 | Bigram | I5, I13 | 4.099 | 3 |
| 4 | Bigram | C4, C12 | 3.288 | 3 |
| 5 | Bigram | C12, C13 | 3.288 | 4 |

All match the reference exactly.

### Frequency Distribution (Table 1 Equivalent)

| Observed Freq | Bigrams | Trigrams | Quadrigrams |
|---------------|---------|----------|-------------|
| 1 | 1225 | 4095 | 8335 |
| 2 | 153 | 221 | 111 |
| 3 | 60 | 56 | 16 |
| 4 | 31 | 27 | 3 |
| 5 | 20 | 9 | 1 |
| ≥6 | 54 | 14 | 0 |
| **Total unique** | **1543** | **4422** | **8466** |

### PMI Summary Statistics by Period

| Period | N Objects | N-grams (obs>2) | PMI Min | PMI Median | PMI Max |
|--------|-----------|-----------------|---------|------------|---------|
| Full dataset | 483 | 20 | 1.425 | 3.078 | 7.925 |
| Maglemose | 205 | 9 | 1.745 | 3.146 | 5.618 |
| Kongemose | 87 | 18 | 1.425 | 3.078 | 5.618 |
| Ertebølle | 168 | 10 | 1.425 | 2.777 | 7.925 |

### Figure Comparison

| Figure | Status | Notes |
|--------|--------|-------|
| Figure 3 (Maglemose patterns) | Structural match | Bar heights match table values; font differs |
| Figure 4 (Kongemose patterns) | Structural match | Bar heights match table values; font differs |
| Figure 5 (Ertebølle patterns) | Structural match | Bar heights match table values; font differs |
| PMI heatmap | Computational match | Matrix values identical; GIMP post-processing not reproduced |

The published figures use `Gill Sans MT` font and manual GIMP post-processing on the
heatmap. Our reproduction uses `sans` font and no post-processing. The underlying
data is identical.

## Runtime Comparison

| | Original | Reproduction |
|---|---------|-------------|
| Compute | Unknown (interactive RStudio) | ~30 seconds (batch Docker) |
| Environment setup | Unknown | ~20 min (Docker build + wrapper writing) |
| Total hands-on | Unknown | ~50 min |

## Assessment: "Zenodo-Only" Reproducibility

This reproduction tests the scenario where authors deposit code and data on Zenodo
**without any environment specification** (no Docker, no renv, no conda, no session
info). Key findings:

### What Worked

1. **The analysis is fully deterministic.** Frequency counts and logarithms produce
   identical results regardless of package version, making this maximally robust to
   environment variation.

2. **The quanteda API remained stable.** `tokens_ngrams()` with the same parameters
   produces identical output across versions 3.x.

3. **Data format was straightforward.** Standard xlsx files with clear column naming.

4. **The deposit was complete.** All necessary input data and verification targets were
   included.

### What Didn't Work

1. **The script cannot be run end-to-end.** It requires manual re-execution with
   parameter changes, commenting/uncommenting lines, and renaming intermediate objects.
   A reproducer must understand the workflow deeply before attempting.

2. **No environment specification.** We cannot verify we used the same package versions.
   For this analysis it didn't matter; for analyses involving stochastic elements or
   API-sensitive operations, it could produce different results.

3. **Proprietary font dependency.** `Gill Sans MT` is not freely available, making exact
   visual reproduction impossible on Linux without purchasing the font.

4. **No output saving.** Most plots use interactive `print()` only. Without modification,
   a batch reproducer cannot capture figure outputs.

### Comparison with Previous Reproductions

| Aspect | Crema 2024 | Marwick 2025 | Herskind 2024 |
|--------|-----------|--------------|---------------|
| Containerisation | Dockerfile (2 fixes) | Dockerfile (0 fixes) | **None (we built it)** |
| Dependency management | install.packages() | renv.lock (169 pkgs) | **None (6 packages listed)** |
| Script mode | Batch-ready | Literate (Quarto) | **Interactive (manual re-runs)** |
| Runtime | ~18h (MCMC) | ~13 min (render) | **~30 sec (deterministic)** |
| Modifications needed | 2 (typo + missing pkg) | 0 | **Wrapper script required** |
| Numerical match | Within HPD intervals | Exact (1 minor stat) | **Exact (machine epsilon)** |
| Effort to reproduce | ~3h hands-on | ~20 min hands-on | **~50 min hands-on** |

### Reproducibility Verdict

**SUCCESSFUL** — but with the important caveat that success required **writing a wrapper
script** to automate the interactive workflow. A researcher unfamiliar with the analysis
would need to carefully read the script comments and understand the intended execution
sequence before being able to reproduce the results. The deposit provides everything
needed for reproduction, but the assembly instructions are implicit rather than explicit.

---

*Report generated: 2026-02-10*
*Reproduction attempt: 01*
*Reproducer: Shawn + Claude Code*
