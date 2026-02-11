# Reproduction Log — Herskind & Riede 2024

## Reproduction Metadata

- **Paper:** Herskind, L.L.P. & Riede, F. (2024) "A computational linguistic methodology for
  assessing semiotic structure in prehistoric art and the meaning of southern Scandinavian
  Mesolithic ornamentation." *Journal of Archaeological Science*, 165, 105969.
- **Zenodo deposit:** https://doi.org/10.5281/zenodo.10623550 (CC-BY 4.0)
- **Date:** 2026-02-10
- **Reproducer:** Shawn + Claude Code
- **Attempt:** 01
- **Compute:** Local Docker (AMD desktop)

## Timeline

| Time | Duration | Step |
|------|----------|------|
| 08:23 | 2 min | Downloaded Zenodo deposit (3 files, 493 KB) |
| 08:25 | 5 min | Examined S2.R script — identified interactive design |
| 08:25 | 5 min | Examined S1.xlsx (483 objects, 290 columns) and S3.xlsx (pre-computed output) |
| 08:28 | 2 min | Created Dockerfile and reproduction directory structure |
| 08:28 | 15 min | Wrote automated wrapper script (run-analysis.R) |
| 08:30 | 4 min | Docker build (rocker/r-ver:4.2.2 + 6 packages + fonts) |
| 08:33 | 1 min | Executed analysis — completed in ~30 seconds |
| 08:34 | 5 min | Compared outputs against S3.xlsx reference |
| 08:35 | 10 min | Wrote documentation |
| **Total** | **~50 min** | |

## Script Modifications Required

The original S2.R **could not be run end-to-end in batch mode**. A wrapper script
(`run-analysis.R`) was written to automate the analysis. The following issues necessitated this:

### 1. Interactive Design (Major)

The script is designed for interactive (RStudio) execution with manual re-running:

- Part 1 must be re-run 3 times with `n` changed to 2, 3, and 4
- Lines 80-83 and 92-94 are conditionally included for trigrams/quadrigrams only
  (controlled by manually commenting/uncommenting)
- Part 2 requires re-running Part 1 for each cultural period subset
- The script comments say "CHANGE FILE NAME", "alter title depending on analysis level"

**Resolution:** Wrote wrapper with a `generate_skipgram_pmi()` function that accepts `n_value`
and `input_data` as parameters, then calls it systematically for all combinations.

### 2. No Output File Saving (Moderate)

Bar plots use `print()` only (interactive display), not `ggsave()`. Only the heatmap has a
`ggsave()` call. CSV export uses a generic filename `_grams.csv`.

**Resolution:** Added `ggsave()` calls for all plots with descriptive filenames.

### 3. Font Unavailability (Minor — Aesthetic Only)

Script requires `Gill Sans MT` (proprietary). Not available in Docker.

**Resolution:** Fallback to `sans` font. No computational impact.

### 4. File Path with Ampersand (Minor — Docker-Specific)

Original filename `Herskind&Riede_S1.xlsx` caused Docker volume mount issues.

**Resolution:** Renamed to `S1.xlsx` for Docker compatibility. Updated `read_excel()` call.

## Outputs Generated

| File | Size | Description |
|------|------|-------------|
| `bigrams.csv` | 8.3 KB | 165 bigrams (obs_freq > 2), sorted by PMI |
| `trigrams.csv` | 6.1 KB | 106 trigrams (obs_freq > 2), sorted by PMI |
| `quadrigrams.csv` | 1.4 KB | 20 quadrigrams (obs_freq > 2), sorted by PMI |
| `freq_bigrams.png` | 212 KB | Bigrams sorted by frequency, stacked by period |
| `pmi_bigrams.png` | 190 KB | Bigrams sorted by PMI, stacked by period |
| `freq_trigrams.png` | 87 KB | Trigrams sorted by frequency, stacked by period |
| `pmi_trigrams.png` | 67 KB | Trigrams sorted by PMI, stacked by period |
| `heatmapPMI.png` | 170 KB | Bigram PMI co-occurrence heatmap |
| `pmi-matrix.csv` | 10.6 KB | Full PMI matrix (49 × 49 tokens) |
| `summary-stats.txt` | 926 B | PMI summary statistics by period |
| `run.log` | 4.2 KB | Complete execution log |

## Key Observations

1. **Data encoding:** The Ertebølle period uses the `ø` character in the data (UTF-8), which
   worked correctly in the Docker environment.

2. **Object count:** 483 objects loaded, but `t = 482` in the original script because one
   object ("painted bands and fields") has an empty motif string and is excluded from
   frequency calculations. Our wrapper dynamically calculates this.

3. **Chronology values:** Four values present: Maglemose (205), Kongemose (87),
   Ertebølle (168), Kongemose/Ertebølle (23). The 23 "Kongemose/Ertebølle" objects are
   excluded from period-specific analyses (matching the original script's subsetting).

4. **Warning messages:** `NA is replaced by empty string` — expected behaviour from quanteda
   when processing the one empty motif string. Identical to what the original script notes
   in its comments.

5. **Runtime:** ~30 seconds for all n-gram levels plus all plots. This is a trivially fast
   analysis — the computational cost is negligible.

## Verification Summary

- 165/165 bigrams: **exact match** (max |PMI diff| = 5.03 × 10⁻¹⁷)
- 106/106 trigrams: **exact match** (max |PMI diff| = 0.00)
- 20/20 quadrigrams: **exact match** (max |PMI diff| = 0.00)
- All observed frequencies: **exact integer match**
- All expected frequencies: **exact match** (within machine epsilon)
- Sort ordering: **identical** across all three n-gram types
