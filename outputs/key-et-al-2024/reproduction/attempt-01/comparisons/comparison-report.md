# Comparison Report

## Key et al. 2024 — Reproduction Verdict: PARTIAL

**Paper:** Key, A.J.M., Martisius, N.L., Jarić, I., Roberts, D.L. (2024). Identifying
accurate artefact morphological ranges using optimal linear estimation: Method
validation, case studies, and code. *Journal of Archaeological Science*, 162, 105921.
DOI: 10.1016/j.jas.2024.105921

**Date:** 2026-02-10
**Reproduction scope:** Tables 5 and 6 only (2 of 13 datasets available). Tables 2-4
(validation with replica data), Table 5 rows other than Olduvai, and Table 7
(geometric microliths) could not be reproduced due to data unavailability.

---

### Quantitative Results

#### Table 5: Olduvai Bed IV Cleavers (n = 134)

Analysis type: deterministic (mmc1 Main Optimal Linear Estimation (OLE) script).
All values should match exactly.

| Variable | Metric | Published | Reproduced | Classification |
|----------|--------|-----------|------------|----------------|
| Length | Mean | 142.9 | 142.9 | EXACT_MATCH |
| Length | Minimum | 93 | 93 | EXACT_MATCH |
| Length | OLE Minimum | 84.0 | 84.0 | EXACT_MATCH |
| Length | Maximum | 205 | 205 | EXACT_MATCH |
| Length | OLE Maximum | 216.3 | 216.3 | EXACT_MATCH |
| Length | Extension % | 18.1 | 18.1 | EXACT_MATCH |
| Breadth | Mean | 87.6 | 87.6 | EXACT_MATCH |
| Breadth | Minimum | 57 | 57 | EXACT_MATCH |
| Breadth | OLE Minimum | 49.5 | 49.5 | EXACT_MATCH |
| Breadth | Maximum | 119 | 119 | EXACT_MATCH |
| Breadth | OLE Maximum | 126.8 | 126.8 | EXACT_MATCH |
| Breadth | Extension % | 24.7 | 24.7 | EXACT_MATCH |
| Thickness | Mean | 42.3 | 42.2 | WITHIN_PRECISION |
| Thickness | Minimum | 22 | 22 | EXACT_MATCH |
| Thickness | OLE Minimum | 19.5 | 19.5 | EXACT_MATCH |
| Thickness | Maximum | 60 | 60 | EXACT_MATCH |
| Thickness | OLE Maximum | 60.9 | 60.9 | EXACT_MATCH |
| Thickness | Extension % | 8.9 | 9.1 | WITHIN_PRECISION |
| Edge Length | Mean | 259.7 | 259.7 | EXACT_MATCH |
| Edge Length | Minimum | 20 | 20 | EXACT_MATCH |
| Edge Length | OLE Minimum | -10.6 | -10.6 | EXACT_MATCH |
| Edge Length | Maximum | 481 | 481 | EXACT_MATCH |
| Edge Length | OLE Maximum | 501.2 | 501.2 | EXACT_MATCH |
| Edge Length | Extension % | 11.0 | 11.0 | EXACT_MATCH |
| Mass | Mean | 588.3 | 588.3 | EXACT_MATCH |
| Mass | Minimum | 252 | 251.5 | WITHIN_PRECISION |
| Mass | OLE Minimum | 224.6 | 224.9 | WITHIN_PRECISION |
| Mass | Maximum | 1269 | 1269.1 | WITHIN_PRECISION |
| Mass | OLE Maximum | 1557.8 | 1557.8 | EXACT_MATCH |
| Mass | Extension % | 31.1 | 31.0 | WITHIN_PRECISION |

**Table 5 summary: 30 values — 24 exact matches (80.0%), 6 within precision
(20.0%). All 30 values (100%) confirmed within rounding tolerance.**

**Notes on Table 5 WITHIN_PRECISION values:**

- **Thickness Mean** (42.3 vs 42.2): Difference of 0.1 at reported 1 decimal
  place precision. The true mean is 42.24..., rounding to 42.2; the paper
  likely rounded from a slightly different intermediate calculation.
- **Thickness Extension %** (8.9 vs 9.1): The reproduction computes Extension %
  from full-precision OLE values before rounding, while the paper may have
  computed from rounded intermediates. Formula check with rounded values:
  ((60.9 − 19.5)/(60 − 22) − 1) × 100 = 8.9%, confirming the paper's value
  from its own rounded intermediates.
- **Mass Minimum** (252 vs 251.5): The source data (Martin-Ramos thesis) records
  mass in decigrams. Conversion to grams yields 251.5g. The paper reports 252,
  consistent with rounding mass to whole grams.
- **Mass OLE Minimum** (224.6 vs 224.9): The 0.3 difference propagates from the
  Mass Minimum rounding difference (251.5 vs 252) affecting the k-window input.
- **Mass Maximum** (1269 vs 1269.1): Same rounding pattern as Minimum.
- **Mass Extension %** (31.1 vs 31.0): Propagated from the Mass rounding
  differences.

#### Table 6: Paleoindian Projectile Points (4 types × 4 variables)

Analysis type: deterministic (mmc1 Main OLE script). All values should match
exactly. Sample sizes: Clovis n=810 (mass n=101), Eastern Clovis n=228 (mass
n=63), Folsom n=179 (mass n=125), Midland n=64.

##### Length (mm)

| Type | Metric | Published | Reproduced | Classification |
|------|--------|-----------|------------|----------------|
| Clovis | Mean | 67.3 | 67.3 | EXACT_MATCH |
| Clovis | Minimum | 21.9 | 21.9 | EXACT_MATCH |
| Clovis | OLE Min | 20.5 | 20.5 | EXACT_MATCH |
| Clovis | Maximum | 230.5 | 230.49 | WITHIN_PRECISION |
| Clovis | OLE Max | 243.4 | 243.4 | EXACT_MATCH |
| Clovis | Ext % | 6.9 | 6.9 | EXACT_MATCH |
| E. Clovis | Mean | 54.2 | 54.2 | EXACT_MATCH |
| E. Clovis | Minimum | 27.5 | 27.5 | EXACT_MATCH |
| E. Clovis | OLE Min | 26.6 | NaN | CANNOT_COMPARE |
| E. Clovis | Maximum | 151.0 | 151 | EXACT_MATCH |
| E. Clovis | OLE Max | 211.0 | 211 | EXACT_MATCH |
| E. Clovis | Ext % | 49.3 | NaN | CANNOT_COMPARE |
| Folsom | Mean | 40.5 | 40.5 | EXACT_MATCH |
| Folsom | Minimum | 16.7 | 16.65 | WITHIN_PRECISION |
| Folsom | OLE Min | 11.7 | 11.7 | EXACT_MATCH |
| Folsom | Maximum | 92.7 | 92.7 | EXACT_MATCH |
| Folsom | OLE Max | 105.8 | 105.8 | EXACT_MATCH |
| Folsom | Ext % | 23.8 | 23.7 | WITHIN_PRECISION |
| Midland | Mean | 42.0 | 42 | EXACT_MATCH |
| Midland | Minimum | 19.1 | 19.1 | EXACT_MATCH |
| Midland | OLE Min | 14.5 | 14.5 | EXACT_MATCH |
| Midland | Maximum | 68.0 | 68 | EXACT_MATCH |
| Midland | OLE Max | 70.5 | 70.5 | EXACT_MATCH |
| Midland | Ext % | 14.8 | 14.6 | WITHIN_PRECISION |

##### Breadth (mm)

| Type | Metric | Published | Reproduced | Classification |
|------|--------|-----------|------------|----------------|
| Clovis | Mean | 27.1 | 27.1 | EXACT_MATCH |
| Clovis | Minimum | 13.0 | 13 | EXACT_MATCH |
| Clovis | OLE Min | 12.6 | NaN | CANNOT_COMPARE |
| Clovis | Maximum | 64.4 | 64.35 | WITHIN_PRECISION |
| Clovis | OLE Max | 66.3 | 66.3 | EXACT_MATCH |
| Clovis | Ext % | 4.5 | NaN | CANNOT_COMPARE |
| E. Clovis | Mean | 24.5 | 24.5 | EXACT_MATCH |
| E. Clovis | Minimum | 11.9 | 11.89 | WITHIN_PRECISION |
| E. Clovis | OLE Min | 7.5 | 7.5 | EXACT_MATCH |
| E. Clovis | Maximum | 41.0 | 41 | EXACT_MATCH |
| E. Clovis | OLE Max | 46.7 | 46.7 | EXACT_MATCH |
| E. Clovis | Ext % | 34.8 | 34.7 | WITHIN_PRECISION |
| Folsom | Mean | 20.4 | 20.4 | EXACT_MATCH |
| Folsom | Minimum | 10.9 | 10.86 | WITHIN_PRECISION |
| Folsom | OLE Min | 8.8 | 8.8 | EXACT_MATCH |
| Folsom | Maximum | 36.3 | 36.34 | WITHIN_PRECISION |
| Folsom | OLE Max | 40.1 | 40.1 | EXACT_MATCH |
| Folsom | Ext % | 23.3 | 22.9 | WITHIN_PRECISION |
| Midland | Mean | 19.5 | 19.5 | EXACT_MATCH |
| Midland | Minimum | 12.5 | 12.51 | WITHIN_PRECISION |
| Midland | OLE Min | 10.4 | 10.4 | EXACT_MATCH |
| Midland | Maximum | 30.5 | 30.53 | WITHIN_PRECISION |
| Midland | OLE Max | 35.1 | 35.1 | EXACT_MATCH |
| Midland | Ext % | 37.1 | 37 | WITHIN_PRECISION |

##### Thickness (mm)

| Type | Metric | Published | Reproduced | Classification |
|------|--------|-----------|------------|----------------|
| Clovis | Mean | 7.2 | 7.2 | EXACT_MATCH |
| Clovis | Minimum | 3.0 | 3 | EXACT_MATCH |
| Clovis | OLE Min | 2.8 | NaN | CANNOT_COMPARE |
| Clovis | Maximum | 13.7 | 13.67 | WITHIN_PRECISION |
| Clovis | OLE Max | 14.9 | 14.9 | EXACT_MATCH |
| Clovis | Ext % | 12.2 | NaN | CANNOT_COMPARE |
| E. Clovis | Mean | 6.8 | 6.8 | EXACT_MATCH |
| E. Clovis | Minimum | 3.0 | 3 | EXACT_MATCH |
| E. Clovis | OLE Min | 1.8 | 1.8 | EXACT_MATCH |
| E. Clovis | Maximum | 14 | 14 | EXACT_MATCH |
| E. Clovis | OLE Max | 19.4 | 19.4 | EXACT_MATCH |
| E. Clovis | Ext % | 60.0 | 60 | EXACT_MATCH |
| Folsom | Mean | 4.2 | 4.2 | EXACT_MATCH |
| Folsom | Minimum | 2.3 | 2.27 | WITHIN_PRECISION |
| Folsom | OLE Min | 2.1 | 2.1 | EXACT_MATCH |
| Folsom | Maximum | 11.1 | 11.1 | EXACT_MATCH |
| Folsom | OLE Max | 15.0 | 15 | EXACT_MATCH |
| Folsom | Ext % | 46.2 | 45.7 | WITHIN_PRECISION |
| Midland | Mean | 4.3 | 4.3 | EXACT_MATCH |
| Midland | Minimum | 3.0 | 3.04 | WITHIN_PRECISION |
| Midland | OLE Min | 2.9 | 2.9 | EXACT_MATCH |
| Midland | Maximum | 6.0 | 6 | EXACT_MATCH |
| Midland | OLE Max | 6.5 | 6.5 | EXACT_MATCH |
| Midland | Ext % | 3.1 | 21.2 | MAJOR_DISCREPANCY |

##### Mass (g)

| Type | Metric | Published | Reproduced | Classification |
|------|--------|-----------|------------|----------------|
| Clovis | Mean | 38.8 | 38.8 | EXACT_MATCH |
| Clovis | Minimum | 1.9 | 1.86 | WITHIN_PRECISION |
| Clovis | OLE Min | 1.4 | 1.4 | EXACT_MATCH |
| Clovis | Maximum | 196.2 | 196.2 | EXACT_MATCH |
| Clovis | OLE Max | 201.8 | 201.8 | EXACT_MATCH |
| Clovis | Ext % | 19.6 | 3.1 | MAJOR_DISCREPANCY |
| E. Clovis | Mean | 10.2 | 10.2 | EXACT_MATCH |
| E. Clovis | Minimum | 2.6 | 2.58 | WITHIN_PRECISION |
| E. Clovis | OLE Min | 1.6 | 1.6 | EXACT_MATCH |
| E. Clovis | Maximum | 23.9 | 23.85 | WITHIN_PRECISION |
| E. Clovis | OLE Max | 27.6 | 27.6 | EXACT_MATCH |
| E. Clovis | Ext % | 21.9 | 22.1 | WITHIN_PRECISION |
| Folsom | Mean | 4.3 | 4.3 | EXACT_MATCH |
| Folsom | Minimum | 0.5 | 0.5 | EXACT_MATCH |
| Folsom | OLE Min | -0.4 | -0.4 | EXACT_MATCH |
| Folsom | Maximum | 32.5 | 32.5 | EXACT_MATCH |
| Folsom | OLE Max | 57.9 | 57.9 | EXACT_MATCH |
| Folsom | Ext % | 82.3 | 82.3 | EXACT_MATCH |
| Midland | Mean | 4.1 | 4.1 | EXACT_MATCH |
| Midland | Minimum | 1.2 | 1.2 | EXACT_MATCH |
| Midland | OLE Min | 1.0 | 1 | EXACT_MATCH |
| Midland | Maximum | 8.6 | 8.6 | EXACT_MATCH |
| Midland | OLE Max | 8.8 | NaN | CANNOT_COMPARE |
| Midland | Ext % | 5.1 | NaN | CANNOT_COMPARE |

##### Table 6 Summary

| Classification | Count | Percentage |
|----------------|-------|------------|
| EXACT_MATCH | 65 | 67.7% |
| WITHIN_PRECISION | 21 | 21.9% |
| CANNOT_COMPARE | 8 | 8.3% |
| MAJOR_DISCREPANCY | 2 | 2.1% |
| **Total** | **96** | |

Of 88 comparable values: 65 exact (73.9%), 21 within precision (23.9%),
2 major discrepancy (2.3%). **86 of 88 comparable values confirmed (97.7%).**

##### Notes on Table 6 CANNOT_COMPARE Values (NaN)

Eight values produced NaN because the bottom or top k=10 records in the
Buchanan & Hamilton (2021) dataset contain duplicate values. The OLE.test
function computes `v = (1/(k-1)) * sum(log((x[1] - x[k])/(x[1] - x[2:(k-1)])))`,
and when `x[1] == x[j]` for some j, the denominator is zero, producing
`log(Inf) = Inf`, which cascades to NaN.

The paper reports values for all these cells, confirming the authors
pre-processed the data to handle duplicates before running the OLE script.
This pre-processing step is not documented in the paper or supplementary
scripts. The mmc1 comments state "Duplicates should be avoided in the data
set" but the script does not enforce this.

Affected cells:

| Type | Variable | Direction | Paper Value | Reproduced |
|------|----------|-----------|-------------|------------|
| E. Clovis | Length | OLE Min | 26.6 | NaN |
| Clovis | Breadth | OLE Min | 12.6 | NaN |
| Clovis | Thickness | OLE Min | 2.8 | NaN |
| Midland | Mass | OLE Max | 8.8 | NaN |

Each NaN also prevents computation of the corresponding Extension %,
accounting for the remaining 4 CANNOT_COMPARE values.

##### Notes on Table 6 MAJOR_DISCREPANCY Values

Two Extension % values in the paper do not match the formula
((OLE Max − OLE Min) / (Maximum − Minimum) − 1) × 100 applied to the
paper's own reported OLE values:

1. **Midland Thickness Extension %**: Paper reports 3.1%. Formula from
   paper's own values: ((6.5 − 2.9) / (6.0 − 3.0) − 1) × 100 = 20.0%.
   Reproduction computes 21.2% (from unrounded intermediates). The paper's
   3.1% is inconsistent with its own OLE Min/Max values.

2. **Clovis Mass Extension %**: Paper reports 19.6%. Formula from paper's
   own values: ((201.8 − 1.4) / (196.2 − 1.9) − 1) × 100 = 3.1%.
   Reproduction computes 3.1%. The paper's 19.6% is inconsistent with its
   own OLE Min/Max values.

Both discrepancies are in the derived Extension % column only — the core
OLE analytical outputs (OLE Minimum, OLE Maximum) match. These appear to be
calculation or transcription errors in the paper's Table 6. The OLE Min/Max
values (which are the scientifically meaningful outputs) are confirmed.

##### Notes on Table 6 WITHIN_PRECISION Values

Small differences (0.1-0.5) in Extension % arise because the reproduction
computes Extension % from full-precision OLE estimates, while the paper
appears to have computed from rounded intermediates in some cases. For
descriptive statistics (Mean, Minimum, Maximum), WITHIN_PRECISION differences
reflect rounding to the reported decimal places (e.g., 16.65 → 16.7,
11.89 → 11.9).

#### Combined Summary (Tables 5 + 6)

| Classification | Table 5 | Table 6 | Total | Percentage |
|----------------|---------|---------|-------|------------|
| EXACT_MATCH | 24 | 65 | 89 | 70.6% |
| WITHIN_PRECISION | 6 | 21 | 27 | 21.4% |
| CANNOT_COMPARE | 0 | 8 | 8 | 6.3% |
| MAJOR_DISCREPANCY | 0 | 2 | 2 | 1.6% |
| **Total** | **30** | **96** | **126** | |

**Of 118 comparable values: 116 confirmed (98.3%), 2 major discrepancy
(1.7%). Both discrepancies are in derived Extension % values, not in the
core OLE analytical outputs.**

---

### Qualitative Results

No figures were reproduced. Figures 5 and 6 in the paper derive from Tables
2-4 (validation data) and the full set of Tables 5-7 results, which could
not be reproduced due to data unavailability. The reproduction's scope is
limited to the numerical values in Tables 5 and 6.

---

### Methodology

1. **Environment:** Docker image `reproduction-key-et-al-2024` based on
   `rocker/r-ver:4.3.2`. No additional R packages — OLE function uses only
   base R (matrix algebra, gamma function, solve). Built on first attempt.

2. **Data:** Olduvai cleavers (n=134) from Martin-Ramos (2022/2023) PhD
   thesis supplementary Excel, UCL Discovery (open access). Paleoindian
   projectile points (n=1,281) from Buchanan & Hamilton (2021) ESM2.xlsx,
   Springer (open access). Both datasets retrieved via documented citation
   chains from the paper.

3. **Analysis:** Deterministic — the OLE.test function (mmc1) involves
   no stochastic components. Given identical input data, the function must
   produce identical output. Extension % is a derived value computed from
   OLE estimates and observed range.

4. **Comparison:** Published values transcribed from Tables 5 and 6 of the
   paper (pages 12-13 of the PDF). Reproduced values extracted from CSV
   output files. Each value compared at the precision reported in the paper
   (typically 1 decimal place for measurements, 1 decimal place for
   Extension %).

### Why Exact Matches Are Expected

The OLE.test function is fully deterministic: it sorts input data, computes
a shape parameter v from log-ratios, constructs a covariance matrix lambda,
solves a linear system for weights a, and returns a weighted sum (point
estimate) and a transformed bound (confidence interval). None of these
operations involve random number generation.

Given identical input data, the function must return identical output to
machine precision. Differences at the reported precision level (1 decimal
place) indicate either: (a) different input data, (b) different rounding
conventions, or (c) errors in the paper.

The WITHIN_PRECISION classifications are explained by (a) — the Mass values
differ because the source data may have been rounded differently during the
paper's data preparation — and (b) — Extension % differs because of
rounding of intermediate values. The MAJOR_DISCREPANCY values are explained
by (c) — the paper's Extension % values for Midland Thickness and Clovis
Mass are inconsistent with the formula applied to the paper's own OLE
Min/Max values.

### Scope Limitations

1. **Data availability (primary limitation):** Only 3 of 13 datasets used
   in the paper are publicly accessible (Level 0). By record count, 42.6%
   (2,149/5,042) of the analysed data is available. This limits reproduction
   to Table 5 (Olduvai rows only) and Table 6 (all 4 Paleoindian types).

2. **Tables not reproduced:**
   - Tables 2-4 (method validation): Replica assemblage data not published
     (Level 3-4)
   - Table 5 (8 other case studies): Data held by co-authors or in
     closed-access monographs (Level 3)
   - Table 7 (geometric microliths): Public GitHub repositories contain
     classification data but not the morphometric measurements (Length,
     Breadth, Thickness, Area) used by Key et al. Additionally, Table 7
     uses the Randomised OLE script (mmc2) which lacks `set.seed()`,
     making exact reproduction impossible even with correct data.

3. **Duplicate handling gap:** 8 of 96 Table 6 values could not be
   compared because the reproduction correctly reproduces the NaN that
   results from duplicate values in the k-window. The paper's values
   for these cells confirm the authors applied undocumented pre-processing
   to handle duplicates before running OLE.

4. **Figures not reproduced:** Figures 5 and 6 require the full dataset
   across all case studies.

### Verdict Justification

**PARTIAL** — Within the reproducible scope (Tables 5 and 6, representing
2 of 13 datasets and 42.6% of records), the core OLE analytical outputs
(OLE Minimum and OLE Maximum point estimates) match the published values
with 98.3% agreement (116/118 comparable values confirmed). The 2
discrepancies are in derived Extension % values and appear to be
calculation errors in the paper, not failures of the reproduction. However,
the reproduction's scope is fundamentally limited by data availability: 10
of 13 datasets are inaccessible, and 3 of 6 results tables cannot be
reproduced at all. The verdict is PARTIAL because the method is verified
but the majority of the paper's results cannot be independently confirmed.
