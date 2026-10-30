# Comparison Report

## Herskind and Riede 2024 — Reproduction Verdict: SUCCESSFUL (provisional: one PAPER_ERROR escalated)

**Paper:** Herskind, L.L.P. and Riede, F. (2024). A computational linguistic
methodology for assessing semiotic structure in prehistoric art and the
meaning of southern Scandinavian Mesolithic ornamentation. *Journal of
Archaeological Science* 165, 105969. <https://doi.org/10.1016/j.jas.2024.105969>

**Date:** 2026-10-17
**Attempt:** 04 (run gate-1-3-1-pilot-rerun-2026-10); approved plan sha256
`6837cf60785a9b7a1d99ee048b9a5cfc78a00324af15741930aff884b800553d`
**Credited run:** `outputs/run-05/` (sealed in `lane-records/run-05/`)
**Reproduction scope:** all 18 locked targets (8 display items, 10 named
values). The authors' script (Zenodo 10801706, S2.R) ran byte-identical and
produces Fig. 2 (bar panel), Fig. 3, the Fig. 4 skeleton, Tables 1-2, and the
S3 tables. The Fig. 2 map, Fig. 5, Table 3, the Fig. 4 boxes, and several
named values have no authors' code; they were tested with labelled
verification aids (ruling R1) in `verification-aids.R`.

**Coverage: 14 of 18 targets reproduced** (EXACT_MATCH or WITHIN_PRECISION).
Not credited: T01 and T03 (MINOR_DISCREPANCY), T04 (CANNOT_COMPARE,
partially verified), and T05 (PAPER_ERROR, escalated). All four remain in the
denominator.

Machine-readable record: `comparisons/comparison.json`. Value-level detail:
the `comparisons/t*.csv` files, produced by `comparisons/compare.py` from the
sealed run-05 outputs and the transcriptions in `published-values/` (made
before the first run).

---

### Outcome by target

| Target | Display item | Outcome | Values compared / matched | Method as planned |
|--------|--------------|---------|---------------------------|-------------------|
| T01 | Fig. 2 (bars + map) | MINOR_DISCREPANCY | 19 / 19 | yes |
| T02 | Fig. 3 (six panels) | EXACT_MATCH | 256 / 256 | yes |
| T03 | Fig. 4 (heatmap) | MINOR_DISCREPANCY | 457 / 453 | yes |
| T04 | Fig. 5 (cluster map) | CANNOT_COMPARE (partial) | 10 / 10 | yes |
| T05 | Table 1 | PAPER_ERROR (escalated) | 130 / 122 | yes |
| T06 | Table 2 | EXACT_MATCH | 18 / 18 | yes |
| T07 | Table 3 | EXACT_MATCH | 50 / 50 | yes |
| T08 | S3 tables | EXACT_MATCH | 2329 / 2329 | yes |
| T09 | 483 objects | EXACT_MATCH | 1 / 1 | yes |
| T10 | max 15 motifs; k = 13 | EXACT_MATCH | 2 / 2 | yes |
| T11 | two combinations at 44 (~9%) | WITHIN_PRECISION | 3 / 3 | yes |
| T12 | A1-C1, C1-G1 = 44; A1-G1 = 28 | EXACT_MATCH | 3 / 3 | yes |
| T13 | A1, A24, B10, C1, G1, H1 most frequent | EXACT_MATCH | 6 / 6 | **no** (source object substituted; see T13) |
| T14 | Fig. 3b exclusivity 0 / 1 / 9 | EXACT_MATCH | 12 / 12 | yes |
| T15 | maximum culture-specific frequency 5 | EXACT_MATCH | 1 / 1 | yes |
| T16 | Ertebølle cluster C4 C5 C12 C13 D7 | EXACT_MATCH | 21 / 21 | yes |
| T17 | cluster strings on ten objects | EXACT_MATCH | 1 / 1 | yes |
| T18 | antler axes, one antler shaft | EXACT_MATCH | 2 / 2 | yes |

---

### Quantitative Results

#### Fig. 3: six stacked bar panels (T02)

Every one of the 128 bars matches: motif tuple and position, the 4-decimal
PMI label, the bar total, and the four-way chronology composition.

| Panel | Bars | Identity and order | PMI label | Total | Composition | Match |
|-------|------|--------------------|-----------|-------|-------------|-------|
| a (bigrams by frequency) | 21 | 21/21 | 21/21 | 21/21 | 21/21 | EXACT_MATCH |
| b (bigrams by PMI) | 21 | 21/21 | 21/21 | 21/21 | 21/21 | EXACT_MATCH |
| c (trigrams by frequency) | 23 | 23/23 | 23/23 | 23/23 | 23/23 | EXACT_MATCH |
| d (trigrams by PMI) | 23 | 23/23 | 23/23 | 23/23 | 23/23 | EXACT_MATCH |
| e (quadrigrams by frequency) | 20 | 20/20 | 20/20 | 20/20 | 20/20 | EXACT_MATCH |
| f (quadrigrams by PMI) | 20 | 20/20 | 20/20 | 20/20 | 20/20 | EXACT_MATCH |

The panel b cut-off at 21 bars does not split a tie: ranks 20 and 21
(I1-I5, E1-F14) share PMI 1.9584, and rank 22 (H1-RELIEF) is 1.8807. Detail:
`comparisons/t02-fig3-bars.csv`.

#### Table 1: skipgram frequency distributions (T05)

Unigrams (31 rows) and quadrigrams (5 rows) match exactly, as do the four
header totals. Eight cells differ by one type each:

| Level | Frequency | Published n | Reproduced n | Authors' S3 count | Match |
|-------|-----------|-------------|--------------|-------------------|-------|
| bigrams | 8 | 6 | 5 | 5 | PAPER_ERROR (tier 2) |
| bigrams | 7 | 8 | 9 | 9 | PAPER_ERROR (tier 2) |
| bigrams | 4 | 32 | 31 | 31 | PAPER_ERROR (tier 2) |
| bigrams | 3 | 59 | 60 | 60 | PAPER_ERROR (tier 2) |
| bigrams | 2 | 154 | 153 | not in S3 | PAPER_ERROR (tier 3) |
| bigrams | 1 | 1224 | 1225 | not in S3 | PAPER_ERROR (tier 3) |
| trigrams | 2 | 222 | 221 | not in S3 | PAPER_ERROR (tier 3) |
| trigrams | 1 | 4094 | 4095 | not in S3 | PAPER_ERROR (tier 3) |
| all four levels | header n | 230 / 1543 / 4422 / 8466 | 230 / 1543 / 4422 / 8466 | — | EXACT_MATCH |

All other 55 rows: EXACT_MATCH. Detail: `comparisons/t05-table1.csv`; the
printed tables are lines 50-69 of `outputs/run-05/stdout.log`.

**Total: 130 values, 122 exact (93.8%).**

#### Table 2: PMI summary statistics (T06)

| Statistic | Maglemose pub / rep | Kongemose pub / rep | Ertebølle pub / rep | Match |
|-----------|---------------------|---------------------|---------------------|-------|
| Maximum | 3.12 / 3.1177 | 2.85 / 2.8457 | 4.10 / 4.0985 | EXACT_MATCH |
| 3rd quartile | 0.97 / 0.9721 | 1.10 / 1.0983 | 1.30 / 1.2951 | EXACT_MATCH |
| Mean | 0.70 / 0.7041 | 0.74 / 0.7446 | 0.90 / 0.9031 | EXACT_MATCH |
| Median | 0.56 / 0.5583 | 0.60 / 0.6020 | 0.69 / 0.6899 | EXACT_MATCH |
| 1st quartile | 0.23 / 0.2286 | 0.25 / 0.2510 | 0.25 / 0.2510 | EXACT_MATCH |
| Minimum | −1.02 / −1.0214 | −1.02 / −1.0214 | −1.02 / −1.0214 | EXACT_MATCH |

All 18 reproduced values round (half up, 2 dp) to the published values,
whether rounded from full precision or from `summary()`'s 4-significant-digit
print. Printed at `outputs/run-05/stdout.log` lines 112-117. Detail:
`comparisons/t06-table2.csv`.

#### Table 3: the ten cluster objects (T07, T18)

Verification aid aid-T07 (read-only S1 lookup by Płonka figure number): each
figure number matches exactly one S1 row, and site (typography ignored),
region, artefact type (material + type), motif set, and figure agree in all
50 cells. The artefact types are 9 antler axes and 1 antler shaft (Ydernæs 6),
as stated (T18). Detail: `comparisons/t07-table3.csv`,
`comparisons/t18-artefact-types.csv`.

#### S3 skipgram tables (T08)

| Sheet | Rows (pub / rep) | Row set | Row order | Cells matched |
|-------|------------------|---------|-----------|---------------|
| bigrams | 165 / 165 | identical | identical | 1155 / 1155 |
| trigrams | 106 / 106 | identical | identical | 954 / 954 |
| quadrigrams | 20 / 20 | identical | identical | 220 / 220 |

**Total: 2329 cells, 2329 EXACT_MATCH** (tokens and integer frequencies
exact; expected frequency and PMI identical at S3's 15-digit precision,
maximum absolute difference 0). Detail: `comparisons/t08-s3-cells.csv`.

#### Fig. 4 matrix m (T03, numerical part)

165 non-zero pair values: 163 agree with S3 to 15 significant digits; 2
(A24-ANT and I5-I13) differ by at most 5.3×10⁻¹⁵. The authors' `fwrite`
export rounded these two at the 15th digit (for example, I5-I13 is
4.098502572370765 in memory and 4.09850257237077 in S3), which the plan
classes as WITHIN_PRECISION. The 49 axis tokens are exactly the published
order. Detail: `comparisons/t03-matrix-vs-s3.csv`.

#### Fig. 4 culture-exclusive boxes (T03, annotation part)

| Comparison over all 1176 pairs of the 49 axis motifs | Cells |
|-------------------------------------------------------|-------|
| Published boxes (detected from the figure) | 290 (Ertebølle 125, Kongemose 105, Maglemose 60) |
| Box agrees with the S1 lookup (pair exclusive to that complex) | 289 |
| Box colour differs from the lookup | 1: C5-F13 boxed Ertebølle; S1's single bearing object is Kongemose |
| Exclusive pair with no box | 1: B1-B2 (one Maglemose object) |
| Box on a pair that is not exclusive | 0 |

The 290 boxes exceed the 165 plotted pairs, so the authors boxed
culture-exclusive pairs at any frequency; the paper does not state the
criterion. Both disagreeing cells are single-object pairs that the heatmap
does not plot. Detail: `comparisons/t03-boxes-vs-lookup.csv`.

#### Named values (T09-T18)

| Target | Item | Published | Reproduced | Match |
|--------|------|-----------|------------|-------|
| T09 | Objects in the corpus | 483 | 483 (S1 rows; `ndoc` of the authors' corpus) | EXACT_MATCH |
| T10 | Maximum motifs on one object | 15 | 15 | EXACT_MATCH |
| T10 | Skip distance k | 13 | 13 (`k <- 0:13`) | EXACT_MATCH |
| T11 | Combinations occurring 44 times | 2 | 2 | EXACT_MATCH |
| T11 | Their frequency | 44 | 44 (the maximum) | EXACT_MATCH |
| T11 | Share of objects | ~9% | 44/483 = 9.1% | WITHIN_PRECISION |
| T12 | The two at 44 | A1-C1, C1-G1 | A1-C1, C1-G1 | EXACT_MATCH |
| T12 | Third highest | A1-G1 | A1-G1 | EXACT_MATCH |
| T12 | Its frequency | 28 | 28 | EXACT_MATCH |
| T13 | Six most frequent motifs | A1, A24, B10, C1, G1, H1 | A1 136, C1 125, G1 97, A24 69, B10 50, H1 49 | EXACT_MATCH |
| T14 | Fig. 3b bigrams exclusive to Maglemose | 0 | 0 | EXACT_MATCH |
| T14 | Specific to Kongemose | 1 (B10-F38) | 1 (B10-F38) | EXACT_MATCH |
| T14 | Unique to Ertebølle (stated count) | 9 | 9 | EXACT_MATCH |
| T14 | The eight listed Ertebølle bigrams | I5-I13, C5-D7, C4-C12, C12-C13, C4-C5, I1-I13, C5-C13, I1-I5 | all eight present; the ninth is C5-C12 | EXACT_MATCH |
| T15 | Highest frequency among culture-specific Fig. 3b bigrams | 5 | 5 (C4-C5) | EXACT_MATCH |
| T16 | Cluster motifs | C4, C5, C12, C13, D7 | the five motifs; 6 plotted pair PMIs agree with S3; all 10 pairs only on Ertebølle objects | EXACT_MATCH |
| T17 | Objects bearing the cluster strings | 10 | 10, exactly the Table 3 set | EXACT_MATCH |
| T18 | Artefact types | all antler axes but one antler shaft | 9 antler axes, 1 antler shaft | EXACT_MATCH |

Detail: `comparisons/t09-t18-named-values.csv`,
`comparisons/t16-cluster-pairs.csv`,
`comparisons/t17-cluster-objects-vs-table3.csv`.

**Total quantitative comparisons: 3,321 values, 3,309 matched (99.6%).** The
twelve unmatched values are the 8 Table 1 cells (PAPER_ERROR), the 2 Fig. 4
box cells, and the 2 Fig. 4 matrix cells that agree with S3 only within its
storage precision (counted as unmatched in T03's tally of 453 of 457).

---

### Qualitative Results

#### Fig. 2 bar panel (T01)

- **Figure type:** horizontal stacked bar chart (authors' code, S2 Part 2)
- **Data equivalence:** counts from the plot's built layer data,
  compared with pixel measurements of the published bars
- **Structural match:** 18 categories in the published order
  (axe … slotted point, other)
- **Scientific content:** every bar's chronology segments within one object
  of the published bars (the raster's resolution is 3.2 px per object); the
  reproduced bars sum to 483 objects
- **Acceptable differences:** font (Gill Sans MT unavailable)
- **Verdict:** Match

#### Fig. 2 map panel (T01, verification aid)

- **Figure type:** point map (no authors' code)
- **Data equivalence:** aid-T01 plots S1 Coord.Long/Coord.Lat by Chronology
  in the authors' colours; 466 of 483 objects have coordinates (17 are "-" in
  S1: 8 Maglemose, 4 Kongemose, 1 Kongemose/Ertebølle, 4 Ertebølle)
- **Structural match:** same extent (about 8-19° E, 53-58.3° N)
- **Scientific content:** same distribution: Ertebølle concentrated in
  Jutland, the dense Maglemose cluster on Zealand, Kongemose points in Scania
  and southern Sweden, Kongemose/Ertebølle points on the Polish coast
- **Acceptable differences:** no basemap, projection, scale bar, or north
  arrow (unpublished conventions); per the plan, MINOR_DISCREPANCY
- **Verdict:** Minor visual differences

#### Fig. 4 heatmap (T03)

- **Figure type:** 49 × 49 PMI heatmap; the authors' skeleton was edited
  in GIMP
- **Data equivalence:** matrix values verified numerically (above)
- **Structural match:** axis order identical; the published figure shows
  one triangle (GIMP); the skeleton shows the symmetric matrix
- **Scientific content:** colour pattern matches: I5-I13 the deepest red; the
  C4/C5/C12/C13/D7 block; F14-F35, E4-E5, D5-ANT, B10-F38 prominent. All five
  large boxes (I5-I13; C4 C5 C12 C13 D7; D33-H1; B10-F38; A14-A24) mark pairs
  that the lookup finds culture-exclusive (their PMI threshold is unpublished)
- **Acceptable differences:** GIMP styling (masked half, boxes, motif drawings)
- **Verdict:** Minor difference: 2 of 1176 box cells disagree with S1

#### Fig. 5 cluster map (T04, verification aid)

- **Figure type:** map with pie charts and coloured motif-extent patches (no
  authors' code)
- **Data equivalence:** aid-T04 (S1 lookup) gives each Table 3 object's
  cluster motifs and coordinates
- **Structural match:** numbering as Table 3; all ten pies show exactly the
  S1 motif set (10/10); positions agree with S1 coordinates (Spearman 0.997
  for x vs longitude, 1.000 for y vs latitude)
- **Scientific content:** motif-extent patches cannot be compared (no code,
  no stated method)
- **Verdict:** Partially verified (CANNOT_COMPARE for the patches, as the plan
  pre-declared)

---

### Methodology

1. **Environment:** `rocker/r-ver:4.3.2` built through the lane
   (`llmr-herskind-riede-2024-attempt-04`); R 4.3.2; quanteda 3.3.1, readxl
   1.4.3, ggplot2 3.5.0, dplyr 1.1.4, data.table 1.15.0, forcats 1.0.0,
   extrafont 0.19, all at the README's pins (0 fallbacks); unspecified
   dependencies from the Posit snapshot of 2024-04-03 (`environment.md`).
2. **Data:** `Herskind&Riede_S1.xlsx` from Zenodo 10801706 (md5 matches the
   published checksum), 483 objects.
3. **Analysis:** deterministic (skipgram counting, PMI, subsetting, no
   random numbers). The authors' S2.R ran byte-identical through the lane's
   evaluator with one declared tolerance (line 27, `font_import`, which
   fired; it computes nothing).
4. **Comparison:** published values were transcribed from the version of
   record before the first run (`published-values/README.md`); reproduced
   values were read only from the sealed run-05 outputs; S3 was compared
   cell by cell. Visual targets were compared by viewing the reproduced and
   published images side by side.

### Why Exact Matches Are Expected

The analysis is a deterministic count-and-transform pipeline: quanteda's
skipgram generation, column sums, a closed-form PMI, and table and summary
operations, on a fixed spreadsheet. With the pinned package versions, no
source of variation remains, so every value should match exactly. That is
what the authors' code delivered for Fig. 3, Table 2, S3, and the matrix m.
The Table 1 differences cannot be variation; they mark a disagreement
between the paper's table and the authors' own deposit.

### Paper Errors Identified

#### Table 1 bigram and trigram frequency distributions (T05)

1. **Published values (Table 1, p. 4):** bigram frequency classes 8, 7, 4,
   3, 2, 1 with n = 6, 8, 32, 59, 154, 1224; trigram classes 2, 1 with
   n = 222, 4094.
2. **Reproduced values:** 5, 9, 31, 60, 153, 1225; and 221, 4095. Each is one
   type off, in compensating pairs, so every header total (1543, 4422) is
   unchanged.
3. **Verification.** The table is internally consistent: each column sums
   to its stated n. The authors' own materials support the reproduction:
   - **Tier 2 (the authors' deposited data for this analysis):** the
     deposited S3 bigrams sheet, the authors' export of every bigram with
     observed frequency of 3 or more, has 5 bigrams at frequency 8, 9 at 7,
     31 at 4, and 60 at 3. That agrees with the reproduction, not with
     Table 1. The same reproduced counts also give exactly 165 bigrams of
     frequency 3 or more, matching S3's 165 rows.
   - **Tier 3 (the authors' code run unmodified on the authors' data):**
     the frequency-1 and -2 classes, which S3 does not cover.
   - The reproduction's own re-implementation is not used as evidence: the
     counts come from the authors' `table(bigramfreqs)` and
     `table(trigramfreqs)` prints.
4. **Classification:** PAPER_ERROR (tiers 2 and 3). It is escalated for
   human confirmation before entering study data. A likely cause, which this
   reproduction did not test (AP-12 excludes version 1): the paper's methods
   cite Zenodo record 10623550, whose S1.xlsx differs from the version of
   record (md5 `307f2813…` vs `0bcde6d1…`, 442,501 vs 442,983 bytes in the
   evidence pack). Table 1 may have been produced from that earlier data and
   not updated. The paper's conclusions are unaffected.

#### Other internal inconsistencies noted (not scored as errors)

- **T14:** the text states nine Ertebølle-unique bigrams but lists eight.
  The figure and the reproduction both give nine; the unlisted one is
  C5-C12. Scored against the stated count (R4), which matches.
- **Methods description (not a target, per the approval):** the PMI formula
  is printed with log₂, but the code and S3 use the natural log; the
  expected-frequency formula names t as the number of objects (483), but the
  code uses t = 482. The printed figures and tables follow the code.

### Scope Limitation(s)

- **Unscripted outputs (no code; tested with verification aids, ruling
  R1):** the Fig. 2 map, Fig. 5, Table 3, the Fig. 4 boxes, and T09, T10,
  T13, T14, T16, T17, T18 in part. Every aid is in `verification-aids.R`,
  labelled, and separate from the authors' code.
- **Unpublished method:** the Fig. 5 motif-extent patches (T04,
  CANNOT_COMPARE, partial; counts against coverage).
- **Proprietary appearance only:** the Gill Sans MT font and the GIMP
  post-processing affect presentation, not values.
- **Version selection:** only Zenodo 10801706 was used (AP-12), so the
  earlier-version explanation for T05 is untested.

### Verdict Justification

**SUCCESSFUL (provisional)** — The authors' unmodified script reproduced every
value it computes exactly, or within S3's 15-digit storage precision: Fig. 3,
Table 2, all 2329 S3 cells, and the Fig. 4 matrix. Every named value and
Table 3 matched. The remaining departures leave the paper's conclusions
unchanged: 8 of 130 Table 1 cells disagree by one type each, with the
authors' own S3 supporting the reproduction (PAPER_ERROR, awaiting human
confirmation); 2 of 1176 hand-drawn box cells in Fig. 4 disagree with S1;
the map aid lacks a basemap; and Fig. 5's extent patches have no method.
Coverage is 14/18. If a human ruling does not confirm the PAPER_ERROR, T05
would become a discrepancy. Because each cell differs by one type and the
conclusions are unchanged, it would most likely be MINOR_DISCREPANCY, and
the verdict would stand.
