# Comparison Report

## Herskind and Riede 2024 — Reproduction Verdict: SUCCESSFUL (two PAPER_ERROR calls escalated for human confirmation)

**Paper:** Herskind, L.L.P., Riede, F., 2024. A computational linguistic
methodology for assessing semiotic structure in prehistoric art and the meaning
of southern Scandinavian Mesolithic ornamentation. *Journal of Archaeological
Science* 165, 105969. <https://doi.org/10.1016/j.jas.2024.105969>

**Date:** 2026-10-11
**Attempt:** 03 (run `gate-1-3-pilot-rerun-2026-10`; launch commit
`cd5d54ac890fafc9061547694c7d0fad9c065912`; credited run `run-04`)
**Approved plan:** `reproduction-plan.json`, sha256
`89f2c93784d4e962971fcd19b9ecdee43c9c82258f610e69b25f0d6b73df55b5`, 20 locked
targets (T01-T20)
**Machine-readable record:** `comparisons/comparison.json` (schema 1.1). The
value-level files cited below are in `comparisons/values/`, byte-identical
copies of the sealed `outputs/run-04/files/comparison-out/` files.

**Reproduction scope:** the full deposit (Zenodo 10.5281/zenodo.10801706,
version 2): S2.R run byte-identical on S1.xlsx, with its outputs compared with
Tables 1-3, Figs 2-5, Supplementary Information S3, and twelve named values.
Figures and tables without authors' code were tested with labelled R1
verification aids (read-only S1 lookups; documented ggplot2 and quanteda
functions), as the approved plan specifies.

### Summary by target

| Target | Display item | Outcome | Compared | Matched | Counts toward coverage |
|--------|--------------|---------|----------|---------|------------------------|
| T01 | Table 1 | PAPER_ERROR (escalated) | 130 | 122 | no |
| T02 | Table 2 | EXACT_MATCH | 18 | 18 | yes |
| T03 | Table 3 | EXACT_MATCH | 50 | 50 | yes |
| T04 | Figure 2 | MINOR_DISCREPANCY | 72 | 72 | no |
| T05 | Figure 3 | EXACT_MATCH | 256 | 256 | yes |
| T06 | Figure 4 | PAPER_ERROR (escalated) | 2352 | 2350 | no |
| T07 | Figure 5 | EXACT_MATCH | 129 | 129 | yes |
| T08 | Supplementary S3 | EXACT_MATCH | 2329 | 2329 | yes |
| T09 | 483 objects | EXACT_MATCH | 1 | 1 | yes |
| T10 | maximum 15 motifs | EXACT_MATCH | 1 | 1 | yes |
| T11 | two bigrams at 44 (A1-C1, C1-G1) | EXACT_MATCH | 2 | 2 | yes |
| T12 | approximately 9% | WITHIN_PRECISION | 1 | 1 | yes |
| T13 | A1-G1 third, at 28 | EXACT_MATCH | 2 | 2 | yes |
| T14 | no Fig. 3a bigram confined to one complex | EXACT_MATCH | 1 | 1 | yes |
| T15 | no Fig. 3b bigram exclusive to Maglemose | EXACT_MATCH | 1 | 1 | yes |
| T16 | one Kongemose-specific bigram (B10-F38) | EXACT_MATCH | 2 | 2 | yes |
| T17 | nine Ertebølle-only bigrams | EXACT_MATCH | 2 | 2 | yes |
| T18 | highest frequency among them is five | EXACT_MATCH | 1 | 1 | yes |
| T19 | antler axes barring one antler shaft | EXACT_MATCH | 2 | 2 | yes |
| T20 | ten objects | EXACT_MATCH | 1 | 1 | yes |

**Coverage (coverage-rules v1.1): 17 / 20 = 0.85.** The denominator is the
locked list; no target was added, removed, or redefined.

---

### Quantitative Results

#### T01 — Table 1, frequency of frequencies (p. 4)

Reproduced values come from S2.R Part 4 as printed by the unmodified run
(`stdout.log` lines 162-197, run-04). The comparison script parses that
printed output and checks it against `table()` of the session objects.
Value-level file: `comparisons/values/t01-table1-cells.csv`.

| Level | Frequency | Published n | Reproduced n | n in S3 (f >= 3) | Match |
|-------|-----------|-------------|--------------|------------------|-------|
| unigram | 136 | 1 | 1 | n/a | EXACT_MATCH |
| unigram | 125 | 1 | 1 | n/a | EXACT_MATCH |
| unigram | 97 | 1 | 1 | n/a | EXACT_MATCH |
| unigram | 69 | 1 | 1 | n/a | EXACT_MATCH |
| unigram | 50 | 1 | 1 | n/a | EXACT_MATCH |
| unigram | 49 | 1 | 1 | n/a | EXACT_MATCH |
| unigram | 36 | 1 | 1 | n/a | EXACT_MATCH |
| unigram | 34 | 1 | 1 | n/a | EXACT_MATCH |
| unigram | 28 | 1 | 1 | n/a | EXACT_MATCH |
| unigram | 26 | 1 | 1 | n/a | EXACT_MATCH |
| unigram | 23 | 1 | 1 | n/a | EXACT_MATCH |
| unigram | 22 | 2 | 2 | n/a | EXACT_MATCH |
| unigram | 21 | 1 | 1 | n/a | EXACT_MATCH |
| unigram | 19 | 1 | 1 | n/a | EXACT_MATCH |
| unigram | 18 | 1 | 1 | n/a | EXACT_MATCH |
| unigram | 17 | 1 | 1 | n/a | EXACT_MATCH |
| unigram | 16 | 2 | 2 | n/a | EXACT_MATCH |
| unigram | 14 | 1 | 1 | n/a | EXACT_MATCH |
| unigram | 13 | 1 | 1 | n/a | EXACT_MATCH |
| unigram | 12 | 1 | 1 | n/a | EXACT_MATCH |
| unigram | 11 | 2 | 2 | n/a | EXACT_MATCH |
| unigram | 10 | 1 | 1 | n/a | EXACT_MATCH |
| unigram | 9 | 2 | 2 | n/a | EXACT_MATCH |
| unigram | 8 | 3 | 3 | n/a | EXACT_MATCH |
| unigram | 7 | 2 | 2 | n/a | EXACT_MATCH |
| unigram | 6 | 7 | 7 | n/a | EXACT_MATCH |
| unigram | 5 | 4 | 4 | n/a | EXACT_MATCH |
| unigram | 4 | 5 | 5 | n/a | EXACT_MATCH |
| unigram | 3 | 20 | 20 | n/a | EXACT_MATCH |
| unigram | 2 | 39 | 39 | n/a | EXACT_MATCH |
| unigram | 1 | 123 | 123 | n/a | EXACT_MATCH |
| bigram | 44 | 2 | 2 | 2 | EXACT_MATCH |
| bigram | 28 | 1 | 1 | 1 | EXACT_MATCH |
| bigram | 22 | 1 | 1 | 1 | EXACT_MATCH |
| bigram | 16 | 1 | 1 | 1 | EXACT_MATCH |
| bigram | 15 | 2 | 2 | 2 | EXACT_MATCH |
| bigram | 14 | 1 | 1 | 1 | EXACT_MATCH |
| bigram | 13 | 2 | 2 | 2 | EXACT_MATCH |
| bigram | 12 | 6 | 6 | 6 | EXACT_MATCH |
| bigram | 10 | 5 | 5 | 5 | EXACT_MATCH |
| bigram | 9 | 5 | 5 | 5 | EXACT_MATCH |
| bigram | 8 | 6 | 5 | 5 | **differs** |
| bigram | 7 | 8 | 9 | 9 | **differs** |
| bigram | 6 | 14 | 14 | 14 | EXACT_MATCH |
| bigram | 5 | 20 | 20 | 20 | EXACT_MATCH |
| bigram | 4 | 32 | 31 | 31 | **differs** |
| bigram | 3 | 59 | 60 | 60 | **differs** |
| bigram | 2 | 154 | 153 | n/a | **differs** |
| bigram | 1 | 1224 | 1225 | n/a | **differs** |
| trigram | 19 | 1 | 1 | 1 | EXACT_MATCH |
| trigram | 8 | 1 | 1 | 1 | EXACT_MATCH |
| trigram | 7 | 4 | 4 | 4 | EXACT_MATCH |
| trigram | 6 | 8 | 8 | 8 | EXACT_MATCH |
| trigram | 5 | 9 | 9 | 9 | EXACT_MATCH |
| trigram | 4 | 27 | 27 | 27 | EXACT_MATCH |
| trigram | 3 | 56 | 56 | 56 | EXACT_MATCH |
| trigram | 2 | 222 | 221 | n/a | **differs** |
| trigram | 1 | 4094 | 4095 | n/a | **differs** |
| quadrigram | 5 | 1 | 1 | 1 | EXACT_MATCH |
| quadrigram | 4 | 3 | 3 | 3 | EXACT_MATCH |
| quadrigram | 3 | 16 | 16 | 16 | EXACT_MATCH |
| quadrigram | 2 | 111 | 111 | n/a | EXACT_MATCH |
| quadrigram | 1 | 8335 | 8335 | n/a | EXACT_MATCH |

- unigram: n = 230 published, 230 reproduced (EXACT_MATCH)
- bigram: n = 1543 published, 1543 reproduced (EXACT_MATCH)
- trigram: n = 4422 published, 4422 reproduced (EXACT_MATCH)
- quadrigram: n = 8466 published, 8466 reproduced (EXACT_MATCH)

| Column | Published sum of f x n | Reproduced sum of f x n | Deposited data: sum of choose(tokens, n) |
|--------|------------------------|-------------------------|------------------------------------------|
| bigram | 2516 | 2513 | 2513 |
| trigram | 4962 | 4961 | 4961 |
| quadrigram | 8622 | 8622 | 8622 |

**Total: 130 values (126 cells + 4 totals), 122 exact matches (93.8%).** The
8 differences are compensating pairs. In the reproduction, three bigrams sit
one frequency step lower than in the published table (8 to 7, 4 to 3, and 2 to
1), and so does one trigram (2 to 1). Every distinct-item total and every
unigram and quadrigram count is identical.

#### T02 — Table 2, PMI summary statistics by culture complex (p. 6)

From the authors' `summary()` calls (S2.R lines 318-320; printed output in
`stdout.log` lines 284-295), compared at full precision. Value-level file:
`comparisons/values/t02-table2.csv`.

| Complex | Statistic | Published | Reproduced (unrounded) | Reproduced (2 dp) | Match |
|---------|-----------|-----------|------------------------|-------------------|-------|
| Maglemose | Maximum | 3.12 | 3.11767 | 3.12 | EXACT_MATCH |
| Maglemose | 3rd quartile | 0.97 | 0.97211 | 0.97 | EXACT_MATCH |
| Maglemose | Mean | 0.70 | 0.70409 | 0.70 | EXACT_MATCH |
| Maglemose | Median | 0.56 | 0.55833 | 0.56 | EXACT_MATCH |
| Maglemose | 1st quartile | 0.23 | 0.22863 | 0.23 | EXACT_MATCH |
| Maglemose | Minimum | -1.02 | -1.02144 | -1.02 | EXACT_MATCH |
| Kongemose | Maximum | 2.85 | 2.84574 | 2.85 | EXACT_MATCH |
| Kongemose | 3rd quartile | 1.10 | 1.09832 | 1.10 | EXACT_MATCH |
| Kongemose | Mean | 0.74 | 0.74458 | 0.74 | EXACT_MATCH |
| Kongemose | Median | 0.60 | 0.60200 | 0.60 | EXACT_MATCH |
| Kongemose | 1st quartile | 0.25 | 0.25102 | 0.25 | EXACT_MATCH |
| Kongemose | Minimum | -1.02 | -1.02144 | -1.02 | EXACT_MATCH |
| Ertebølle | Maximum | 4.10 | 4.09850 | 4.10 | EXACT_MATCH |
| Ertebølle | 3rd quartile | 1.30 | 1.29514 | 1.30 | EXACT_MATCH |
| Ertebølle | Mean | 0.90 | 0.90307 | 0.90 | EXACT_MATCH |
| Ertebølle | Median | 0.69 | 0.68993 | 0.69 | EXACT_MATCH |
| Ertebølle | 1st quartile | 0.25 | 0.25102 | 0.25 | EXACT_MATCH |
| Ertebølle | Minimum | -1.02 | -1.02144 | -1.02 | EXACT_MATCH |

**Total: 18 values, 18 exact matches at the published precision (100%).** The
largest unrounded difference is 0.00486 (Ertebølle third quartile, 1.29514 vs
1.30), inside the pre-stated ±0.005. The Ertebølle maximum (4.0985) equals the
top PMI in S3 (I5-I13).

#### T03 — Table 3, the ten cluster objects (p. 7; R1 aid: read-only S1 lookup)

S1 rows were matched by Płonka figure reference (and site). Five elements per
row. The only normalisation applied was case, in the composed S1 "Material +
Artefact type" ("antler axe" vs "Antler axe"); motif sets are compared without
regard to order. Value-level file: `comparisons/values/t03-table3.csv`.

| # | S1 No. | Site | Region | Type (S1 material + type) | Motifs | Figure | Match |
|---|--------|------|--------|---------------------------|--------|--------|-------|
| 1 | 116 | Kolindsund | West Denmark | antler axe | C5 D7 G1 | 145 | 5/5 |
| 2 | 51 | Eskelund | West Denmark | antler axe | C13 C14 C5 | 136:5 | 5/5 |
| 3 | 88 | Horsens "Loddentot" | West Denmark | antler axe | A1 C1 C4 C5 D14 | 159 | 5/5 |
| 4 | 240 | Stensballe Sund | West Denmark | antler axe | C5 D7 | 150:2 | 5/5 |
| 5 | 252 | Torpegård | West Denmark | antler axe | C1 C12 C2 C3 C4 C5 C6 G1 | 153 | 5/5 |
| 6 | 23 | Bogø Nor | West Denmark | antler axe | C1 C12 C13 C4 C5 G1 | 134 | 5/5 |
| 7 | 141 | Korsør, Glasværk | East Denmark | antler axe | A24 C1 C4 C5 | 148 | 5/5 |
| 8 | 225 | Skellingsted Bro | East Denmark | antler axe | C1 C12 C13 C4 C5 D7 E15 E4 F34 | 165 | 5/5 |
| 9 | 278 | Ydernæs 6 (Fiskerhuset) | East Denmark | antler shaft | C12 C13 | 192:1 | 5/5 |
| 10 | 189 | Revlen | East Denmark | antler axe | C1 C12 C13 C14 C7 G1 | 161 | 5/5 |

**Total: 50 values, 50 matches (100%).**

#### T05 — Figure 3, six stacked bar panels (p. 5)

Read from the authors' six ggplot objects with `ggplot_build()` and
`layer_data()` (documented ggplot2 functions, read-only), and compared with
the published labels read at full zoom of the embedded 300 ppi image
(`published-values/fig3.csv`). Value-level files:
`comparisons/values/t05-fig3-bars.csv` and `t05-fig3-vs-s3.csv`.

| Panel | Bars | Identity, rank, and 4-dp PMI label | Bar total | Chronology segments | Published label = S3 at 4 dp |
|-------|------|------------------------------------|-----------|---------------------|------------------------------|
| a Most frequent bigrams | 21 | 21/21 | 21/21 | 21/21 | 21/21 |
| b Bigrams by PMI | 21 | 21/21 | 21/21 | 21/21 | 21/21 |
| c Most frequent trigrams | 23 | 23/23 | 23/23 | 23/23 | 23/23 |
| d Trigrams by PMI | 23 | 23/23 | 23/23 | 23/23 | 23/23 |
| e Most frequent quadrigrams | 20 | 20/20 | 20/20 | 20/20 | 20/20 |
| f Quadrigrams by PMI | 20 | 20/20 | 20/20 | 20/20 | 20/20 |
| **Total** | **128** | **128** | **128** | **128** | **128** |

**Total: 256 declared values (128 label+PMI, 128 totals), 256 exact matches
(100%).** The 128 stack segments also match. Exactly tied PMI values
(e.g. 3.2876 for C5-D7, C4-C12, and C12-C13 in panel b) appear in the
published order, so no tie-order difference arose. The planner's low-resolution
reading of the panel b I5-I13 label as 4.0965 is 4.0985 at full resolution,
equal to S3 and to the reproduction.

#### T08 — Supplementary Information S3 (Zenodo v2)

The authors' Part 8 exports (`Bigrams.csv`, `Trigrams.csv`, `Quadrigrams.csv`)
were compared with the deposited `Herskind&Riede_S3.xlsx`, joined on the
motif tuple. Value-level files: `comparisons/values/t08-s3-cells.csv` and
`t08-s3-rows.csv`.

| Sheet | Rows (S3 / reproduced) | Columns | Cells | Matching | Max abs difference | Rows in same position |
|-------|------------------------|---------|-------|----------|--------------------|-----------------------|
| bigrams | 165 / 165 | 7 | 1155 | 1155 | 0 | 165 |
| trigrams | 106 / 106 | 9 | 954 | 954 | 0 | 106 |
| quadrigrams | 20 / 20 | 11 | 220 | 220 | 0 | 20 |
| **Total** | | | **2329** | **2329** | **0** | |

**Total: 2329 values, 2329 exact matches (100%).**

#### T09-T20 — Named values

Value-level file: `comparisons/values/t09-t20-named-values.csv`. T11 and T13
also cite the printed Part 4 bigram table (`stdout.log` lines 169-174).

| Target | Element | Published | Reproduced | Match |
|--------|---------|-----------|------------|-------|
| T09 | objects in corpus (nrow of the authors' data) | 483 | 483 | yes |
| T09 | cross-check: S1 rows with a non-empty No. (R1 aid) | 483 | 483 | yes |
| T10 | max motifs on one object (row sums of S1 columns 31:289; R1 aid) | 15 | 15 | yes |
| T10 | cross-check: max S1 Total column | 15 | 15 | yes |
| T10 | cross-check: max tokens per document (quanteda::ntoken) | 15 | 15 | yes |
| T11 | top bigram frequency | 44 | 44 | yes |
| T11 | bigrams at top frequency | A1 C1;C1 G1 | A1 C1;C1 G1 | yes |
| T11 | cross-check: top frequency in full `bigrams` before Part 7 | 44 | 44 | yes |
| T12 | share of objects carrying each top bigram (%) | approximately 9 | 9.11 | yes |
| T13 | frequency of A1 G1 | 28 | 28 | yes |
| T13 | rank of A1 G1 by descending frequency | 3 | 3 | yes |
| T14 | Fig. 3a bigrams confined to one Chronology class | 0 | 0 | yes |
| T15 | Fig. 3b bigrams exclusive to Maglemose | 0 | 0 | yes |
| T16 | Fig. 3b bigrams specific to Kongemose (count) | 1 | 1 | yes |
| T16 | Fig. 3b bigrams specific to Kongemose (identity) | B10 F38 | B10 F38 | yes |
| T17 | Fig. 3b bigrams unique to Ertebolle (count) | 9 | 9 | yes |
| T17 | the eight listed identities all present | I5 I13;C5 D7;C4 C12;C12 C13;C4 C5;I1 I13;C5 C13;I1 I5 | I5 I13;C5 D7;C4 C12;C12 C13;C4 C5;I1 I13;C5 C13;I1 I5 | yes |
| T17 | unlisted Ertebolle-only bigram(s) (record only) | (not listed in text) | C5 C12 | record only |
| T18 | max co-occurrence frequency among culture-specific Fig. 3b bigrams | 5 | 5 | yes |
| T19 | cluster objects that are antler axes | 9 | 9 | yes |
| T19 | cluster objects that are antler shafts | 1 | 1 | yes |
| T20 | objects carrying >= 2 of C4, C5, C12, C13, D7 (inferred rule) | 10 | 10 | yes |
| T20 | cross-check: that set equals the ten Table 3 objects | Table 3 rows | 23;51;88;116;141;189;225;240;252;278 | yes |

The rows marked "cross-check" confirm the primary values by a second route and
are not counted. T12 is WITHIN_PRECISION: 9.11% against the stated
"approximately 9%", within the pre-stated band of 8.5 to 9.5. T17 is scored
against the stated count of nine (R4). The text lists only eight pairs; the
unlisted ninth is C5-C12, recorded as a text inconsistency, as the approval
ruled. T20's inferred rule (an object carrying at least two of the five
cluster motifs) gives exactly ten objects, and they are the Table 3 objects
(S1 No. 23, 51, 88, 116, 141, 189, 225, 240, 252, 278). The rule therefore
reproduces the printed count and is credited (Q5 ruling).

---

### Qualitative Results

#### T04 — Figure 2 (p. 3): bar chart (authors' code) and map (R1 aid)

- **Figure type:** composite: a stacked bar chart (S2.R Part 2) and a map
  made outside R.
- **Data equivalence (bar chart):** verified numerically. The authors' plot
  gives 18 bars × 4 chronology segments (`layer_data()`). The published
  segments were measured on the 300 ppi image with
  `tools/read-published-fig2.py`, calibrated on the panel's gridlines. All 72
  segment counts agree, and so do the bar order and the 483-object total
  (`comparisons/values/t04-fig2-left-compare.csv`).
- **Structural difference:** the 7 bars holding both Kongemose and
  Kongemose/Ertebølle objects (axe, shaft, pendant, knife, point, core, other)
  stack differently. The published order, left to right, is Maglemose >
  Kongemose > Kongemose/Ertebølle > Ertebølle. The authors' deposited code
  gives Maglemose > Kongemose/Ertebølle > Kongemose > Ertebølle: ggplot2's
  default stacking by factor level, which the published Fig. 3 also shows.
  Segment sizes and colours are the same. No code in the deposit produces the
  published order, which suggests a different code state or manual editing
  (the panels were composed in GIMP).
- **Map (R1 aid, approved as full scope):** S1 coordinates plotted by
  Chronology (`aid-plots/t04-fig2-map-aid.png`) reproduce the published
  pattern. Ertebølle objects concentrate in Jutland, Maglemose and Kongemose
  objects on Zealand, Kongemose points appear in Scania and Bohuslän, and
  scattered Maglemose and Kongemose/Ertebølle points lie along the Polish
  coast. 466 objects have coordinates. The 17 that do not are all "Unknown"
  sites with "-" coordinates, so they cannot appear on any map
  (`t04-fig2-map-unplotted.csv`).
- **Acceptable differences:** typography (Gill Sans MT unavailable), basemap,
  projection, and symbol styling (unpublished cartographic conventions).
- **Verdict:** MINOR_DISCREPANCY. The scientific content (counts per type per
  complex, spatial pattern) matches exactly. The only difference is the
  presentation order of two segments within seven bars.

#### T06 — Figure 4 (p. 6): PMI heatmap with culture-exclusive boxes

- **Figure type:** heatmap (S2.R Part 7 skeleton) with box annotations and
  inset drawings added in GIMP.
- **Matrix and colours:** the axis order is identical to the published axes
  (49 motifs). Each published cell's centre colour was read from the 300 ppi
  image with `tools/read-published-fig4.py` and compared with the fill the
  authors' `heatmap` object assigns (`layer_data()`). **1176 of 1176 cells
  agree.** The 58 visibly coloured cells have exactly the authors' RGB values
  (e.g. I5-I13 #FF0000; C12-C13, C4-C12, C5-D7 #FF6240). The flat JPEG cell
  interiors kept the exact colours.
- **Boxes (R1 aid, read-only S1 lookup):** the plan's frequency > 2 lookup
  (32 single-complex bigrams) turned out to be only part of the published
  boxes, which also surround blank cells. The caption's criterion ("motif
  combinations limited to one specific culture complex") was therefore
  applied to every co-occurring pair of the 49 axis motifs, at any frequency.
  That gives 291 single-complex pairs (Ertebølle 124, Kongemose 106, Maglemose
  61; no pair is confined to Kongemose/Ertebølle). The tool read 290 published
  boxes (Ertebølle 125, Kongemose 105, Maglemose 60). **289 of 291 agree in
  presence and colour.** The two disagreements were confirmed by eye at 4x
  zoom:
  - **F13-C5:** the published box is yellow (Ertebølle). The only S1 object
    carrying both motifs is No. 96, Jordløse Mose (East Denmark), recorded
    as Kongemose.
  - **B2-B1:** the published figure has no box. The only S1 object carrying
    both motifs is No. 367, Lundby II, recorded as Maglemose, so the pair is
    confined to one complex.
  Value-level files: `comparisons/values/t06-fig4-cells.csv`,
  `t06-fig4-all-pairs-lookup.csv`, and `t06-fig4-box-disagreements.csv`.
- **Large boxes:** the caption's "particularly high PMI" threshold is
  unpublished, so the large boxes are not scored separately. The five-motif
  Ertebølle cluster (C4, C5, C12, C13, D7) is reproduced as high-PMI and
  Ertebølle-only (C4-C12, C12-C13, C5-D7 at 3.2876; C4-C5 at 3.1053).
- **Verdict:** PAPER_ERROR (see below). 2350 of 2352 cell states match.

#### T07 — Figure 5 (p. 7): map of the ten cluster objects (R1 aid)

- **Figure type:** hand-made map with pie charts and motif-extent patches; no
  authors' code.
- **Pie membership:** the published pies, read at 4x zoom
  (`published-values/fig5-pies.csv`), match the S1 lookup for all 10 objects ×
  5 motifs = **50/50** (`comparisons/values/t07-fig5-membership.csv`).
- **Relative positions:** the published pie centres are consistent with the
  S1 coordinates in **79 of 79** pairwise east-west and north-south orderings,
  for pairs at least 0.15° apart (`t07-fig5-relative-positions.csv`).
  Objects 3 and 4, 0.02° apart, are drawn side by side in the published map.
- **Motif extents:** S1 points for each motif (C4 6, C5 18, C12 9, C13 8, D7 3
  objects) were compared by eye with the published patches
  (`aid-plots/t07-fig5-aid.png`). Each point lies within its motif's patch,
  for example C12 from Als north-east toward Scania and D7 at objects 1, 4,
  and 8. The paper's spatial claim (C12 and C13 east, C4, C5, and D7 west)
  holds.
- **Acceptable differences:** basemap, projection, and patch geometry
  (unpublished construction).
- **Verdict:** EXACT_MATCH. Every checked element agrees.

---

### Methodology

1. **Environment:** Docker image `llmr-herskind-riede-2024-attempt-03`
   (`rocker/r-ver:4.3.2` pinned by digest), R 4.3.2, and the seven README pins
   built from CRAN Archive source: quanteda 3.3.1, readxl 1.4.3, ggplot2 3.5.0,
   dplyr 1.1.4, data.table 1.15.0, forcats 1.0.0, extrafont 0.19. Packages the
   authors left unspecified came from the P3M snapshot of 2024-04-03. Pins
   were honoured in full, with 0 fallbacks (`environment.md`).
2. **Data:** S1.xlsx from Zenodo 10.5281/zenodo.10801706 (version 2), md5
   matching the record; 483 objects. Data availability is L1.
3. **Analysis:** deterministic (closed-form counting and natural-log PMI; no
   random-number generator). S2.R ran byte-identical through the lane's
   `run-container`, with the gate's `code_integrity` = `identical` and all four
   provenance anchors verified against the committed evidence pack.
4. **Comparison:** `compare-results.R` runs in the container after the
   analysis, in a separate R process. Published values were transcribed
   from the PDF text layer (Tables 1-3, named values), from the embedded
   300 ppi figure images by eye at zoom (Fig. 3 labels, Fig. 5 pies), and with
   measuring tools (Fig. 2 segments, Fig. 4 cells). Method and file
   provenance: `published-values/README.md`.

### Why Exact Matches Are Expected

The analysis is deterministic. Skipgram counts and PMI are closed-form
functions of the deposited presence/absence data, with no sampling and no
optimisation, and the environment matches the authors' supplied pins. Every
value computed by the authors' code therefore reproduces exactly (Table 2, Fig.
3, S3, the Fig. 4 matrix). The remaining differences sit where a human step
stood between the code and the paper: hand transcription into Word (Table 1)
and hand annotation in GIMP (Figs 2 and 4).

### Paper Errors Identified

Both calls are escalated for human confirmation before they enter study data
(verdicts-and-precision v1.1, paper error handling). Under that protocol the
reproduction must be internally consistent and the authors' own materials
must support the reproduced value. Both conditions hold here.

1. **T01, Table 1 (p. 4).**
   - **Published:** 6, 8, 32, 59, 154, and 1224 bigrams at frequencies 8, 7, 4,
     3, 2, and 1; 222 and 4094 trigrams at frequencies 2 and 1.
   - **Reproduced:** 5, 9, 31, 60, 153, 1225; 221, 4095.
   - **Evidence, tier 2 (authors' deposited data for this analysis):** the
     deposited S3 tables, which list every skipgram with frequency above 2,
     contain 5, 9, 31, and 60 bigrams at frequencies 8, 7, 4, and 3. These are
     the reproduced values, not the published ones.
   - **Evidence, tier 3 (authors' code run unmodified on the authors' data):**
     S2.R Part 4 prints the reproduced values (`stdout.log` lines 169-180).
   - **Consistency check on the paper's own table:** with k = 13 and at most
     15 motifs per object, every combination of an object's motifs is a
     skipgram. So Σ(frequency × n) in each column must equal Σ over objects of
     C(tokens, n). The published bigram and trigram columns give 2516 and
     4962; the deposited data give 2513 and 4961, as the reproduction does. The
     quadrigram column agrees (8622).
   - **Hypothesis (not testable here):** Table 1 was transcribed from an
     earlier state of the data or code. Version 1 of the deposit is excluded
     by AP-12, so this was not checked.
   - **Classification:** PAPER_ERROR (not MAJOR_DISCREPANCY). The conclusions
     drawn from Table 1 (few combinations recur; recurrence falls with each
     n-gram step) are unaffected.
2. **T06, Figure 4 box annotations (p. 6).**
   - **Published:** cell F13-C5 boxed as Ertebølle-only; cell B2-B1 unboxed.
   - **Reproduced (R1 lookup in the deposited S1; evidence tier 2):** F13-C5's
     only co-occurrence is on S1 No. 96 (Jordløse Mose), Kongemose. B2-B1's
     only co-occurrence is on S1 No. 367 (Lundby II), Maglemose, which the
     caption's criterion would box purple.
   - **Context:** the criterion is inferred from the caption, and it
     reproduces the other 289 boxes exactly. These two cells are the printed
     values it does not reproduce, so under the Q5 ruling they go to this
     protocol.
   - **Classification:** PAPER_ERROR (hand annotation in GIMP). The figure's
     scientific content (the matrix, its colours, and the Ertebølle cluster)
     is unaffected.

### Documentation findings (not targets)

- **PMI formula:** the paper (p. 3) writes PMI = log2(observed/expected). S2.R
  uses the natural log, and every published PMI is natural-log (e.g. I5-I13:
  observed 3, expected 6 × 4 / 482 = 0.0498, ln(60.25) = 4.0985). Recorded as
  a documentation finding, per the approval.
- **R version:** the paper says R 4.2.2; the deposit README says 4.3.2 (used).
- **Deposit version:** the paper's methods cite Zenodo version 1; its
  data-availability statement cites version 2 (reproduced, per AP-12).
- **T17 wording:** "nine are unique for the Ertebølle period" is followed by
  eight pairs; the ninth is C5-C12.

### Scope Limitation(s)

- **Proprietary upstream (typography only):** Gill Sans MT is unavailable, so
  figures render in DejaVu. This is not scored and is not a FAIR failure.
- **No authors' code for the Fig. 2 map, Fig. 5, the Fig. 4 boxes, or Table 3:**
  these were tested with labelled R1 verification aids (read-only S1
  lookups and plotting of deposited coordinates), approved as full-scope
  checks. Patch geometry in Fig. 5 and the large Fig. 4 boxes rest on
  unpublished conventions and were compared by pattern only.
- **Version 1 of the deposit** was deliberately not used (AP-12), so the
  hypothesis that Table 1 reflects an earlier data state was not tested.

### Verdict Justification

**SUCCESSFUL.** The authors' unmodified code, in the environment they
specified, reproduced every value it computes exactly: Table 2, all 128 Fig. 3
bars, all 2329 S3 cells, the Fig. 4 matrix and colours, and all twelve named
values. 17 of the 20 locked targets are within tolerance (coverage 0.85). The
other three do not contradict the paper's findings. Two are suspected paper
errors in hand-made steps, where the authors' own deposited data and code
support the reproduction (Table 1: 8 counts off by one; Fig. 4: 2 of 291 box
annotations). The third is a stacking-order difference in Fig. 2. The
conclusions, including the Ertebølle C4/C5/C12/C13/D7 cluster and its spatial
pattern, are confirmed. The verdict is provisional until a human confirms the
two PAPER_ERROR calls.
