# Comparison Report

## Herskind and Riede 2024 — Reproduction Verdict: SUCCESSFUL

**Paper:** Herskind, L.L.P., Riede, F., 2024. A computational linguistic
methodology for assessing semiotic structure in prehistoric art and the meaning
of southern Scandinavian Mesolithic ornamentation. *Journal of Archaeological
Science* 165, 105969. <https://doi.org/10.1016/j.jas.2024.105969>

**Date:** 2026-10-03
**Plan:** `reproduction-plan.json`, sha256
`5cdc80717f2f50faf21f5ec1eb876f642e391605e11b4e6ff90286b0b7abaf63` (approved
by Shawn Ross, 2026-10-03). There are 15 locked targets, T01–T15.
**Reproduction scope:** the authors' complete S2.R (Parts 1–8) ran unmodified
in Docker on the Zenodo v2 data. The items with no authors' code were tested
with verification aids under ruling R1, in the separate script
`comparisons/compare.R`. They are targets T01, T03, T12, T13, and T14, plus
the T02 map panel and the T11 boxes.

**Pending human confirmation:** two PAPER_ERROR calls (T04; T08 text list) and
one CANNOT_COMPARE call (T14). See "Escalations" below.

---

### Summary by target

| Target | Display item | Outcome | Values (matched / compared) | Evidence |
|--------|--------------|---------|-----------------------------|----------|
| T01 | Corpus size 483 | EXACT_MATCH | 1 / 1 | `results/t01-corpus-size.csv` |
| T02 | Fig. 2 (bars + map) | MINOR_DISCREPANCY | visual (bar stack order differs) | `results/t02-fig2-visual-check.csv` |
| T03 | Max 15 motifs per object | EXACT_MATCH | 1 / 1 | `results/t03-max-motifs.csv` |
| T04 | Table 1 | PAPER_ERROR | 122 / 130 | `results/t04-table1.csv`, `results/t04-occurrence-check.csv` |
| T05 | A1-C1 and C1-G1 = 44, ~9% | WITHIN_PRECISION | 3 / 3 | `results/t05-a1c1-c1g1.csv` |
| T06 | A1-G1 third, 28 | EXACT_MATCH | 1 / 1 | `results/t06-a1g1.csv` |
| T07 | Fig. 3 (6 panels, 128 PMI labels) | EXACT_MATCH | 128 / 128 | `results/t07-fig3-labels.csv` |
| T08 | Culture-exclusive salient bigrams 0/1/9 | EXACT_MATCH | 3 / 3 | `results/t08-culture-exclusive-counts.csv` |
| T09 | Max exclusive frequency 5 | EXACT_MATCH | 1 / 1 | `results/t09-max-exclusive-frequency.csv` |
| T10 | Table 2 | WITHIN_PRECISION | 18 / 18 | `results/t10-table2.csv` |
| T11 | Fig. 4 heatmap and boxes | WITHIN_PRECISION | 32 / 32 aid cells (visual) | `results/t11-fig4-visual-box-check.csv` |
| T12 | Table 3 | EXACT_MATCH | 50 / 50 | `results/t12-table3.csv` |
| T13 | Ten objects; 9 axes + 1 shaft | EXACT_MATCH | 2 / 2 | `results/t13-cluster-objects.csv` |
| T14 | Fig. 5 | CANNOT_COMPARE | 10 / 10 pies; patches untestable | `results/t14-fig5-pies.csv` |
| T15 | Supplementary S3 | EXACT_MATCH | 1601 / 1601 | `results/t15-s3-cells.csv` |

**Coverage** (coverage-rules v1.0): targets reproduced exactly or within the
pre-stated tolerance = 12 of 15 (0.80). The three not counted are T02
(MINOR_DISCREPANCY), T04 (PAPER_ERROR), and T14 (CANNOT_COMPARE). All 15 stay
in the denominator.

---

### Quantitative Results

#### Table 1 — skipgram frequency distributions (T04)

Source: the console output of S2.R Part 4 (`outputs/run-console.log`, lines
256–298; `outputs/capture-table1-*.csv`).

- **Unigrams:** all 31 frequency/n rows match exactly.
- **Quadrigrams:** all 5 rows match exactly.
- **Column totals:** all four match (230, 1543, 4422, 8466).
- **Frequency levels:** all 63 levels are identical in both versions.
- **n values:** eight cells differ, each by exactly 1.

| Column | Frequency | Published n | Reproduced n | S3 deposit (authors' own Part 8 output) | Match |
|--------|-----------|-------------|--------------|------------------------------------------|-------|
| bigrams | 8 | 6 | 5 | 5 | PAPER_ERROR |
| bigrams | 7 | 8 | 9 | 9 | PAPER_ERROR |
| bigrams | 4 | 32 | 31 | 31 | PAPER_ERROR |
| bigrams | 3 | 59 | 60 | 60 | PAPER_ERROR |
| bigrams | 2 | 154 | 153 | (S3 lists observed > 2 only) | PAPER_ERROR |
| bigrams | 1 | 1224 | 1225 | (S3 lists observed > 2 only) | PAPER_ERROR |
| trigrams | 2 | 222 | 221 | (S3 lists observed > 2 only) | PAPER_ERROR |
| trigrams | 1 | 4094 | 4095 | (S3 lists observed > 2 only) | PAPER_ERROR |
| all other 55 n cells, 63 levels, 4 totals | — | — | — | — | EXACT_MATCH |

**Total quantitative comparisons: 130 values, 122 exact matches (93.8%).**

#### Table 2 — PMI summary statistics by culture complex (T10)

Source: the three `summary()` calls in S2.R Part 5
(`outputs/capture-table2-pmi-summary.csv`, full precision). The tolerance is
|difference| ≤ 0.005 (rounding at 2 decimals).

| Statistic | Maglemose pub / rep | Kongemose pub / rep | Ertebølle pub / rep |
|-----------|---------------------|---------------------|---------------------|
| Maximum | 3.12 / 3.1177 | 2.85 / 2.8457 | 4.10 / 4.0985 |
| 3rd quartile | 0.97 / 0.9721 | 1.10 / 1.0983 | 1.30 / 1.2951 |
| Mean | 0.70 / 0.7041 | 0.74 / 0.7446 | 0.90 / 0.9031 |
| Median | 0.56 / 0.5583 | 0.60 / 0.6020 | 0.69 / 0.6899 |
| 1st quartile | 0.23 / 0.2286 | 0.25 / 0.2510 | 0.25 / 0.2510 |
| Minimum | −1.02 / −1.0214 | −1.02 / −1.0214 | −1.02 / −1.0214 |

**18 values, 18 within precision (100%).** The largest absolute difference,
0.00486 (Ertebølle 3rd quartile), is correct rounding of 1.29514 to 1.30. The
subset sizes are 106, 129, and 113 bigrams with observed > 2.

#### Figure 3 PMI labels (T07)

All **128 / 128** published four-decimal labels match `sprintf("%.4f", PMI)`
from the authors' plot objects. They were matched by skipgram identity
(`results/t07-fig3-labels.csv`). The bar order also matches at all 128
positions, including the tied PMI groups (panel b: 3.2876 ×3, 2.0454 ×2,
1.9584 ×2; panel f: 2.2257 ×2). Published values were transcribed from 400 dpi
renders of p. 5.

#### Named values (T01, T03, T05, T06, T08, T09, T13)

| Target | Item | Published | Reproduced | Match |
|--------|------|-----------|------------|-------|
| T01 | objects / ornamentation strings | 483 | 483 S1 rows; 483 corpus documents (`t = 482` in code) | EXACT_MATCH |
| T03 | max individual motifs on one object | 15 | 15 (S1 `Total`; row sums of columns 31:289) | EXACT_MATCH |
| T05 | A1-C1 observed | 44 | 44 | EXACT_MATCH |
| T05 | C1-G1 observed | 44 | 44 | EXACT_MATCH |
| T05 | share of objects | "approximately 9%" | 9.11% (44/483); 9.13% (44/482) | WITHIN_PRECISION |
| T06 | A1-G1 frequency, rank | 28, third | 28, third | EXACT_MATCH |
| T08 | exclusive to Maglemose / Kongemose / Ertebølle | 0 / 1 / 9 | 0 / 1 / 9 | EXACT_MATCH |
| T08 | named Kongemose bigram | B10-F38 | B10 F38 | EXACT_MATCH |
| T08 | eight named Ertebølle bigrams exclusive | yes | yes; the ninth is **C5-C12** (not named in text) | see Paper Errors |
| T09 | max frequency among exclusive bigrams | 5 | 5 (C4-C5) | EXACT_MATCH |
| T13 | objects bearing the cluster | 10 | 10 (exactly the Table 3 objects) | EXACT_MATCH |
| T13 | antler axes / shafts | 9 / 1 | 9 / 1 | EXACT_MATCH |

#### Table 3 (T12)

All **50 / 50** fields match S1 (`results/t12-table3.csv`). The ten objects
resolve to S1 `No.` 116, 51, 88, 240, 252, 23, 141, 225, 278, and 189. Table 3's
"Artefact type" is S1 `Material` + `Artefact type` in sentence case (for
example "Antler axe" = "antler" + "axe"). Site, region, motif list, and Płonka
figure match verbatim. The selection rule is not published, but S1 contains
exactly ten objects carrying at least two of C4/C5/C12/C13/D7, and they are
precisely these ten.

#### Supplementary S3 (T15)

The reproduced `Bigrams.csv`, `Trigrams.csv`, and `Quadrigrams.csv` (Part 8)
were joined to the S3 sheets on the motif tuple. Row membership is identical
(165 / 106 / 20). Row order is also identical, and **1601 / 1601 numeric cells
are equal to machine precision** (maximum absolute difference 0).

---

### Qualitative Results

#### Figure 2 (T02) — MINOR_DISCREPANCY

- **Figure type:** composite; horizontal stacked bar chart (S2.R Part 2) and a
  point map (no code).
- **Data equivalence:** the per-type × chronology counts were tabulated from
  the authors' `DS` object
  (`outputs/capture-fig2-artefact-type-by-chronology.csv`; axe 103, shaft 58,
  pendant 54, other 76, and so on).
- **Structural match:** the 18 bar levels and their order are identical, and so
  is the colour mapping (Maglemose purple, Kongemose red, Kongemose/Ertebølle
  beige, Ertebølle yellow).
- **Difference:** the **stack order within bars** differs. The published panel
  stacks Maglemose | Kongemose | Kongemose/Ertebølle | Ertebølle
  (chronological). The deposited code stacks Maglemose | Kongemose/Ertebølle |
  Kongemose | Ertebølle (the default alphabetical factor levels, reversed).
  Segment sizes agree (for example, axe 10 / 31 / 2 / 60). This is an
  unpublished level-ordering convention, so it is MINOR_DISCREPANCY under the
  pre-stated tolerance. Fig. 3, built by the same deposited code, matches the
  code's order.
- **Map panel (aid):** an S1 coordinate point plot
  (`aids/fig2-map-points-aid.png`; 466 of 483 objects have numeric
  coordinates). It shows the same distribution and colouring as the published
  map: the Zealand cluster, Ertebølle-dominated Jutland, and outliers in Norway,
  Öland, Scania, northern Germany, and Poland. The base map, scale bar, and
  north arrow are not reproducible and not scored.
- **Verdict:** minor visual difference (stack order); scientific content
  matches.

#### Figure 3 (T07) — EXACT_MATCH

- **Data equivalence:** verified numerically. All labels, bar membership, and
  bar order match. Per-chronology stacks (`results/t07-fig3-bar-stacks.csv`)
  were spot-checked against the published panels, for example A1-C1 9/2/18/15,
  E1-F14 1/1/2, and A1-C1-G1 2/1/9/7. All agree.
- **Acceptable differences:** GIMP compositing, fonts, and panel letters.

#### Figure 4 (T11) — WITHIN_PRECISION (visual)

- **Skeleton:** the reproduced `outputs/heatmapPMI.png` has the published
  49-motif axis order (A14 … RELIEF) and the same populated cells and relative
  intensities. Examples include I5-I13 (4.10), the C4/C5/C12/C13/D7 cluster,
  F14-F35, E4-E5, D5-ANT, and B10-F38. The published figure shows only the
  upper-left triangle of the authors' symmetric matrix (GIMP crop).
- **Boxes (approved aid, ruling 6):** the authors' `createResultTable()` was
  applied read-only to the 165 bigrams with observed > 2. It found 32
  single-culture cells (21 Ertebølle, 6 Maglemose, 5 Kongemose). Each was
  located in the published figure at 400 dpi, and **all 32 carry a box of the
  matching colour** (`results/t11-fig4-visual-box-check.csv`,
  `aids/fig4-exclusive-boxes-aid.png`). Filled high-PMI cells the aid leaves
  unboxed (ANT/D5, E5/E4, F35/F14, C5/C1) are also unboxed in the paper.
- **Not covered:** the published figure also boxes many cells with **no PMI
  fill**, that is, bigrams with observed ≤ 2 (for example, most of the RELIEF,
  C14, and G1 rows). The approved aid is limited to observed > 2, so those
  boxes were not verified. Motif drawings are GIMP illustrations and were not
  scored.
- **Verdict:** scientific content within the pre-stated visual tolerance for
  everything the approved method tests. The planning-stage assumption that
  boxes mark only observed > 2 cells was wrong, and this is recorded as a
  deviation (escalation, kind OTHER).

#### Figure 5 (T14) — CANNOT_COMPARE

- **Pie compositions (aid, S1 lookup):** 10 / 10 match. Objects 1 and 4 are
  C5+D7; 2 is C5+C13; 3 and 7 are C4+C5; 5 is C4+C5+C12; 6 is
  C4+C5+C12+C13; 8 has all five; 9 and 10 are C12+C13.
- **Relative positions (aid):** S1 coordinates (`aids/fig5-object-positions-aid.png`)
  reproduce the published arrangement. Object 1 is north; 2 is north-west; 3
  and 4 are adjacent in the west; 5 is south-west; 6 is south; 7 is central; 8
  is north-east of 7; 9 is south-east; 10 is east.
- **Untestable component:** the coloured patches showing "the known extent of
  each individual motif" are a substantive data layer with no stated source,
  code, or deposited input. They cannot be compared (data unavailability for
  that component).
- **Verdict:** the testable components match fully. The target is classified
  CANNOT_COMPARE because a substantive data layer of the figure cannot be
  compared, and it is escalated for human confirmation (see below).

---

### Methodology

1. **Environment:** Docker `rocker/r-ver:4.3.2` with quanteda 3.3.1, readxl
   1.4.3, ggplot2 3.5.0, dplyr 1.1.4, data.table 1.15.0, forcats 1.0.0, and
   extrafont 0.19 (all README pins, asserted at build). See `environment.md`.
2. **Data:** Zenodo 10.5281/zenodo.10801706 v2. The S1, S2, S3, and README
   files were md5-verified against the published checksums.
3. **Analysis:** deterministic (frequency counting, PMI arithmetic, and
   `summary()`; no random number generation). Two runs were byte-identical.
4. **Comparison:** published values were transcribed from the PDF of record
   (pp. 2–7; Fig. 3 labels from 400 dpi renders) into
   `comparisons/published-values/`. `comparisons/compare.R` was run in Docker
   and writes `comparisons/results/`. S3 values come from the deposit itself.

### Why Exact Matches Are Expected

Every computed result is deterministic integer counting or closed-form
arithmetic on those counts. With pinned package versions the reproduction
should match to machine precision, and it does wherever the published value
was produced from the deposited code and data. That includes all 1601 S3
cells, all 128 Fig. 3 labels, and all 18 Table 2 values. The only
non-matching numeric cells (Table 1, eight n values) are therefore not
explained by environment variation (see below).

### Paper Errors Identified

1. **Table 1 (T04): eight n values off by one.**
   - **Published (p. 4):** the bigram column gives n = 6, 8, 32, 59, 154, 1224
     at frequencies 8, 7, 4, 3, 2, 1. The trigram column gives 222 and 4094
     at frequencies 2 and 1.
   - **Reproduced:** 5, 9, 31, 60, 153, 1225 and 221, 4095.
   - **Independent verification from the paper's own data (1):** the authors'
     deposited S3 (their own Part 8 output) tabulates 60 / 31 / 9 / 5 bigrams
     at frequencies 3 / 4 / 7 / 8. That agrees with the reproduction, not with
     Table 1.
   - **Independent verification (2), formula applied to the paper's inputs:**
     with k = 13 and at most 15 motifs per object, every motif pair (triple) on
     an object is a skipgram. So Σ frequency × n must equal Σ C(m, 2)
     (Σ C(m, 3)) over S1's `Total` column. S1 gives 2513 bigram and 4961
     trigram occurrences, and the reproduction gives the same 2513 and 4961.
     Table 1 implies 2516 and 4962, which is inconsistent with the deposited
     data (`results/t04-occurrence-check.csv`).
   - **Classification:** PAPER_ERROR, not MAJOR_DISCREPANCY. The reproduction
     is internally consistent, and the paper's own tabulated data support it.
     The pattern (paired ±1 shifts with unchanged totals) suggests either a
     transcription slip or a table made from an earlier data state; the
     methods cite Zenodo v1. The run note forbids using v1, so the cause was
     not investigated. Column totals and every conclusion are unaffected.
     **Escalated for human confirmation.**
2. **Section 3 text (T08 list): "nine are unique for the Ertebølle period"
   but only eight are named.** The reproduction confirms nine. The omitted one
   is **C5-C12** (3 objects, all Ertebølle; PMI 2.1890; visible in Fig. 3b).
   The stated counts are scored and match (R4), so T08 is EXACT_MATCH. The
   incomplete list is a text error. **Escalated for human confirmation.**
3. **Documented findings, not scored** (approval rulings 3 and 4):
   - The PMI formula is printed as log2 (p. 3), but the code and every
     published PMI value use the natural log. I5-I13 = ln(3/0.0497925) =
     4.0985, against log2 = 5.913.
   - The paper states R v.4.2.2; the deposit README states R 4.3.2.

### Scope Limitation(s)

- **Data unavailability (component level):** the Fig. 5 motif-extent patches
  (T14) and the Fig. 2 / Fig. 5 base maps have no source. T14 counts against
  coverage; the base map is not scored for T02.
- **Proprietary upstream (presentation only):** GIMP compositing and boxes
  (Figs 3–4) and Word/Excel transcription (Tables 1–2, S3). The R outputs
  underlying them were reproduced.
- **Aid scope:** the Fig. 4 boxes on observed ≤ 2 cells were not verified
  (approved aid limited to observed > 2).
- **Fonts:** Gill Sans MT is unavailable (DejaVu Sans substitute); typography
  is not scored.

### Escalations (for human confirmation)

1. **PAPER_ERROR — T04:** Table 1 n values (8 cells) are inconsistent with the
   deposited S1 and S3. Verified twice, as set out above.
2. **PAPER_ERROR — T08:** the text names 8 of the 9 Ertebølle-exclusive
   bigrams and omits C5-C12. The score is unaffected.
3. **CANNOT_COMPARE — T14:** the motif-extent patches have no deposited
   input. Pies (10/10) and positions match. The reviewer may decide whether the
   patches are scientific content (keep CANNOT_COMPARE) or cartography
   (reclassify as within tolerance).
4. **OTHER — T11:** the published boxes extend to observed ≤ 2 cells, which
   is outside the approved aid. The 32 tested cells all match. Decide whether
   the planning assumption needs a documented deviation, or whether a further
   check is wanted.

### Verdict Justification

**SUCCESSFUL.** The authors' unmodified code reproduced every code-generated
result to machine precision:

- all 1601 S3 cells;
- all 128 Fig. 3 labels, with bar order;
- all 18 Table 2 values;
- all Table 1 values except eight n cells, which the paper's own deposited
  data show to be a paper error.

All named values, Table 3, and the testable parts of the Fig. 2, Fig. 4, and
Fig. 5 checks also match. The remaining items are a cosmetic stack-order
convention (T02) and an unsourced map layer (T14). The paper's conclusions are
confirmed. Coverage is 12 / 15 (0.80); the verdict is conditional on human
confirmation of the two PAPER_ERROR calls and the CANNOT_COMPARE call.
