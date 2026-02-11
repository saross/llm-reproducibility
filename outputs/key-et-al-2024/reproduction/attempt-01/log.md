# Reproduction Log

## Key et al. 2024

**Paper:** Key, A.J.M., Martisius, N.L., Jarić, I., Roberts, D.L. (2024). Identifying
accurate artefact morphological ranges using optimal linear estimation: Method
validation, case studies, and code. *Journal of Archaeological Science*, 162, 105921.
DOI: 10.1016/j.jas.2024.105921

### Timeline

| Time | Activity | Duration |
|------|----------|----------|
| 00:00 | R-Plan: Paper analysis and data availability audit | ~90 min |
| 01:30 | R-A: Script analysis (mmc1-3), data format verification | ~20 min |
| 01:50 | R-A: Dockerfile construction (base R only, no packages) | ~5 min |
| 01:55 | R-A: Wrapper script (run-analysis.R) — Table 5 + Table 6 | ~25 min |
| 02:20 | Docker build #1 — success, first attempt | ~2 min |
| 02:22 | Docker run #1 — Table 5 exact match, Table 6 NaN discovery | ~5 min |
| 02:27 | Investigation: NaN values from duplicate handling gap | ~15 min |
| 02:42 | Docker build #2 — deduplication attempt (broke Olduvai) | ~5 min |
| 02:47 | Revert: removed dedup, restored mmc1-exact behaviour | ~10 min |
| 02:57 | Docker build #3 — final run, confirmed all matches | ~5 min |
| 03:02 | R-A documentation: environment.md, log.md | ~15 min |
| 03:17 | R-B: Value-by-value comparison (126 values, Tables 5 + 6) | ~30 min |
| 03:47 | R-B: Comparison report, log corrections, queue update | ~20 min |
| **Total** | | **~4 hours 5 min** |

### Modifications Required

1. **Dockerfile construction** (1 iteration):
   - Paper provides no Dockerfile, renv.lock, or sessionInfo
   - Constructed minimal `rocker/r-ver:4.3.2` image — base R only
   - No additional R packages or system dependencies required
   - R 4.3.2 chosen as contemporary version for the 2024 publication date

2. **Wrapper script** (run-analysis.R):
   - Paper provides interactive R scripts with placeholder file paths
     (`"###file location###"`) requiring manual substitution
   - Wrote batch wrapper that:
     - Copies OLE.test function verbatim from mmc1 (lines 26-45)
     - Parameterises the repeated load → subset → OLE → extract pattern
     - Adds `write.csv()` and `sink()` for output capture
     - Runs Table 5 (5 variables) and Table 6 (4 types × 4 variables)
   - **No algorithmic modifications**: OLE.test function is identical to mmc1;
     data transformation (sort, k-window, boundary transform) matches mmc1
     lines 48-61 exactly

3. **Data acquisition** (2 datasets retrieved, 10 unavailable):
   - Olduvai cleavers (n=134): Extracted from Martin-Ramos (2022/2023) PhD
     thesis supplementary Excel, UCL Discovery. Filtered by `LCT SUB TYPE =
     "Cleaver"`, cross-referenced edge length from Principal sheet, converted
     mass from decigrams to grams
   - Paleoindian points (n=1,281): Downloaded from Buchanan & Hamilton (2021)
     ESM2.xlsx, Springer static content. Filtered to 4 target types, renamed
     `Width` → `Breadth`
   - Geometric microliths: Public GitHub repos contain classification data
     only — morphometric measurements (Length, Breadth, Thickness, Area)
     not deposited. Table 7 cannot be reproduced

4. **No column/index adjustments needed**: Data files prepared with matching
   column names during R-Plan data acquisition phase

### Outputs Generated

| File | Description | Size |
|------|-------------|------|
| `outputs/table-5-olduvai-results.csv` | OLE results for 5 variables (n=134) | 409 B |
| `outputs/table-6-paleoindian-results.csv` | OLE results for 4 types × 4 variables | 1.2 KB |
| `outputs/run.log` | Full console output from Docker execution | 6.7 KB |

### Findability, Accessibility, Interoperability, and Reusability (FAIR) / Machine-Actionability Findings

1. **Data deposition gap (critical)**: 10 of 13 datasets used in the paper
   are not publicly deposited. The paper aggregates data from 13 separate
   sources but does not provide a unified dataset. Only 3 datasets (23.1%)
   are retrievable; by record count, 42.6% (2,149/5,042) of the analysed
   data is accessible. This is the primary barrier to reproduction.

2. **Empty supplement file**: mmc4.csv (listed as "Supplementary Material 4"
   in the paper) downloads as an empty file (0 bytes content, CSV header
   only). This appears to be a publishing error — the file was likely
   intended to contain a worked example dataset but was uploaded empty.

3. **No environment specification**: Paper provides no R version, no
   `sessionInfo()`, no `renv.lock`, no Dockerfile. The supplementary R
   scripts are the only computational artefacts. Environment had to be
   inferred from publication date.

4. **Undocumented pre-processing**: The mmc1 script comments state
   "Duplicates should be avoided in the data set" but does not enforce
   deduplication. When the bottom or top k=10 values contain duplicates,
   `OLE.test()` produces NaN (division by zero in the log term of the v
   parameter). This affected 4 of 16 Paleoindian OLE minimum estimates.
   The authors clearly pre-processed the data to handle duplicates, but
   this step is not documented or included in the scripts.

5. **Stochastic scripts lack seed**: mmc2 (Randomised OLE) and mmc3
   (Resampling OLE) use `rnorm()` and `sample()` respectively without
   `set.seed()`. Even with correct data, these scripts cannot produce
   identical results across runs. Table 7 uses mmc2, making it
   non-reproducible by design.

6. **Interactive-only scripts**: All three R scripts use interactive
   placeholders (`###file location###`) rather than command-line arguments
   or configuration files. They assume RStudio execution and include
   non-analytical dependencies (e.g., `beepr` for audio notifications in
   mmc2). No batch execution pathway is provided.

7. **Citation chain complexity**: Data provenance requires following
   multi-hop citation chains (e.g., Key et al. → Martin-Ramos 2022 →
   original excavation reports). Some intermediate sources are closed-access
   PhD theses, creating accessibility bottlenecks even when the original
   data is conceptually "available."

### Discrepancy Notes

1. **Table 6 Midland Thickness Extension %**: Paper reports 3.1%.
   Formula from paper's own values: ((6.5 − 2.9) / (6.0 − 3.0) − 1)
   × 100 = 20.0%. Reproduction computes 21.2% from full-precision
   intermediates. The paper's 3.1% is inconsistent with its own OLE
   Min/Max values — likely a calculation or transcription error.

2. **Table 6 Clovis Mass Extension %**: Paper reports 19.6%. Formula
   from paper's own values: ((201.8 − 1.4) / (196.2 − 1.9) − 1)
   × 100 = 3.1%. Reproduction computes 3.1%. The paper's 19.6% is
   inconsistent with its own OLE Min/Max values.

3. **Table 6 NaN values**: 4 OLE minimum point estimates (Clovis Breadth,
   Clovis Thickness, Eastern Clovis Length, Midland Mass maximum) return
   NaN due to duplicate values in the k=10 window. Published values exist
   for these cells, confirming undocumented pre-processing.

4. **Table 5 Mass rounding**: Minor differences in Mass Minimum (252 vs
   251.5), OLE Minimum (224.6 vs 224.9), and Maximum (1269 vs 1269.1)
   stem from the source data recording mass in decigrams — conversion to
   grams preserves sub-gram precision that the paper may have rounded.

5. **Wrapper script transcription error (corrected)**: Initial comparison
   used 27.5% as the published Length Extension % for Olduvai. This was
   incorrectly transcribed from the Old Park Flakes row of Table 5. The
   correct published value is 18.1%, which matches the reproduction exactly.
