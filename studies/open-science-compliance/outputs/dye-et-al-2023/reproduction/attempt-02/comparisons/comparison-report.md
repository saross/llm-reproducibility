# Comparison Report

## Dye et al. 2023 — Reproduction Verdict: PARTIAL

**Paper:** Dye, T.S., Buck, C.E., DiNapoli, R.J., & Philippe, A. (2023). Bayesian
chronology construction and substance time. *Journal of Archaeological Science*,
153, 105765. <https://doi.org/10.1016/j.jas.2023.105765>

**Date:** 2026-10-03 (run `phase2-shakedown-2026-10`, attempt 02; approved plan
sha256 `7ff05a24d1342b84ebe5f61f2f0e7b15df040baf73ad1c67aa13c63ff49f0f35`)

**Reproduction scope:** this attempt covers the R post-processing (ArchaeoPhases
1.8) of the archived OxCal Markov chain Monte Carlo (MCMC) output `beads-1.csv`,
as printed in the supplement's sections 3-10. Regenerating the OxCal MCMC is out
of scope (a proprietary upstream, assigned to attempt-03). Targets without
author code (paper Fig 2, Supplement Figs 1-3, and the section 11/12 named
values) were tested with clearly labelled verification aids under ruling R1.

The machine-readable record is `comparisons/comparison.json` (34 records, one
per locked target, schema-valid). Value-level detail for each target is in
`comparisons/values/`.

---

### Outcome by locked target

| Target | Display item | Outcome | Testable | Values compared | Values matched |
|--------|--------------|---------|----------|-----------------|----------------|
| T01 | Paper Fig 2 (modes of change, 6 Nökel lattices) | EXACT_MATCH | yes | 78 | 78 |
| T02 | Paper Fig 3 (occurrence plot, 72 interments) | CANNOT_COMPARE | no | 0 | 0 |
| T03 | Paper Fig 4 (tempo plots, 23 bead types) | MINOR_DISCREPANCY | yes | 23 | 23 |
| T04 | Paper Fig 6 (phyletic seriation diagram) | MINOR_DISCREPANCY | yes | 8 | 8 |
| T05 | BE3-Amber to Amethyst and Cowrie "always satisfies" | EXACT_MATCH | yes | 2 | 2 |
| T06 | BE1-Cowrie to BE1-Disc = 0.87 | PAPER_ERROR (suspected; escalated) | yes | 1 | 0 |
| T07 | BE1-CylRound the most probable ancestor of late monochrome types | EXACT_MATCH | yes | 3 | 3 |
| T08 | BE3-Amber the most probable stable-solid ancestor of BE1-Dghnt | EXACT_MATCH | yes | 1 | 1 |
| T09 | Summary of the 54 Bayliss et al. relations | EXACT_MATCH | yes | 2 | 2 |
| T10 | Between-run variability summary | CANNOT_COMPARE | no | 0 | 0 |
| T11 | Supplement Table 1 | CANNOT_COMPARE | no | 0 | 0 |
| T12 | Supplement Table 2 | EXACT_MATCH | yes | 16 | 16 |
| T13 | Supplement Table 3 | EXACT_MATCH | yes | 7 | 7 |
| T14 | Supplement Table 4 | EXACT_MATCH | yes | 5 | 5 |
| T15 | Supplement Table 5 | EXACT_MATCH | yes | 12 | 12 |
| T16 | Supplement Table 6 | EXACT_MATCH | yes | 6 | 6 |
| T17 | Supplement Table 7 | EXACT_MATCH | yes | 2 | 2 |
| T18 | Supplement Table 8 | EXACT_MATCH | yes | 1 | 1 |
| T19 | Supplement Table 9 | EXACT_MATCH | yes | 1 | 1 |
| T20 | Supplement Table 10 | EXACT_MATCH | yes | 4 | 4 |
| T21 | Supplement Fig 1 (analytic and empirical lattices) | MINOR_DISCREPANCY | yes | 26 | 26 |
| T22 | Supplement Fig 2 (histogram of the 54 relations) | MINOR_DISCREPANCY | yes | 10 | 8 |
| T23 | Supplement Fig 3 (expected versus observed lattices) | MINOR_DISCREPANCY | yes | 26 | 26 |
| T24 | Supplement section 10.1 text | EXACT_MATCH | yes | 8 | 8 |
| T25 | Supplement section 10.2 text | EXACT_MATCH | yes | 3 | 3 |
| T26 | Supplement section 10.3 text | EXACT_MATCH | yes | 5 | 5 |
| T27 | Supplement section 10.4 text | EXACT_MATCH | yes | 6 | 6 |
| T28 | Supplement section 10.5 text | EXACT_MATCH | yes | 6 | 6 |
| T29 | Supplement section 10.6 text | EXACT_MATCH | yes | 4 | 4 |
| T30 | Supplement section 10.7 text (0.98) | EXACT_MATCH | yes | 1 | 1 |
| T31 | Supplement section 10.8 text (0.99) | EXACT_MATCH | yes | 1 | 1 |
| T32 | Supplement section 10.9 text | EXACT_MATCH | yes | 5 | 5 |
| T33 | BE1-Dghnt(e)BE1-Dghnt = 1 | EXACT_MATCH | yes | 1 | 1 |
| T34 | BE1-Koch20Wh(poDd)BE1-WhSpiral; overlaps 0.73 | WITHIN_PRECISION | yes | 2 | 2 |

**Coverage (coverage-rules v1.0):** 25 of 34 targets were reproduced exactly or
within the pre-stated tolerance (24 EXACT_MATCH and 1 WITHIN_PRECISION), giving
**0.735**. The remaining 9 stay in the denominator: 5 MINOR_DISCREPANCY,
3 CANNOT_COMPARE, and 1 PAPER_ERROR.

---

### Quantitative Results

All probabilities are the `res$observed` matrices from the authors'
`allen_observe_frequency()` code, reported at the published 2 dp using R's
`round()`, the same rounding the authors' code applies. Matrix orientation is
row (relation) column, with the row as ancestor or Earlier type; T05 confirms
this (BE3-Amber(oFD)BE1-Amethyst = 1, converse 0).

#### Main-text branching values (T05; paper p.16)

| Relation / quantity | Published | Reproduced (unrounded) | Reproduced (2 dp) | Match |
|---|---|---|---|---|
| BE3-Amber(oFD)BE1-Amethyst | 1 | 1 | 1 | EXACT_MATCH |
| BE3-Amber(oFD)BE1-Cowrie | 1 | 1 | 1 | EXACT_MATCH |

#### Main-text value (T06; paper p.16)

| Relation / quantity | Published | Reproduced (unrounded) | Reproduced (2 dp) | Match |
|---|---|---|---|---|
| BE1-Cowrie(oFD)BE1-Disc | 0.87 | 0.99967 | 1 | PAPER_ERROR |

#### Supplement Table 2 (T12)

| Relation / quantity | Published | Reproduced (unrounded) | Reproduced (2 dp) | Match |
|---|---|---|---|---|
| BE1-Reticella(p)BE1-Disc | 1 | 0.99917 | 1 | EXACT_MATCH |
| BE1-Reticella(p)BE1-WhSpiral | 0.76 | 0.7605 | 0.76 | EXACT_MATCH |
| BE1-Reticella(p)BE1-WoundSp | 0.54 | 0.5425 | 0.54 | EXACT_MATCH |
| BE1-Reticella(p)BE1-Dghnt | 0.45 | 0.451 | 0.45 | EXACT_MATCH |
| BE1-Reticella(p)BE1-Amethyst | 0.45 | 0.44783 | 0.45 | EXACT_MATCH |
| BE1-Reticella(p)BE1-Cowrie | 0.4 | 0.3955 | 0.4 | EXACT_MATCH |
| BE1-Reticella(p)BE1-Orange | 0.03 | 0.03267 | 0.03 | EXACT_MATCH |
| BE1-Reticella(p)BE2-c Metal | 0.01 | 0.00933 | 0.01 | EXACT_MATCH |
| BE1-Melon(p)BE1-Disc | 1 | 0.99967 | 1 | EXACT_MATCH |
| BE1-Melon(p)BE1-WhSpiral | 0.82 | 0.82183 | 0.82 | EXACT_MATCH |
| BE1-Melon(p)BE1-WoundSp | 0.63 | 0.6295 | 0.63 | EXACT_MATCH |
| BE1-Melon(p)BE1-Dghnt | 0.56 | 0.55967 | 0.56 | EXACT_MATCH |
| BE1-Melon(p)BE1-Amethyst | 0.55 | 0.5535 | 0.55 | EXACT_MATCH |
| BE1-Melon(p)BE1-Cowrie | 0.51 | 0.5055 | 0.51 | EXACT_MATCH |
| BE1-Melon(p)BE1-Orange | 0.06 | 0.065 | 0.06 | EXACT_MATCH |
| BE1-Melon(p)BE2-c Metal | 0.03 | 0.02733 | 0.03 | EXACT_MATCH |

#### Supplement Table 3 (T13)

| Relation / quantity | Published | Reproduced (unrounded) | Reproduced (2 dp) | Match |
|---|---|---|---|---|
| BE1-DotReg(p)BE1-Disc | 0.19 | 0.19383 | 0.19 | EXACT_MATCH |
| BE1-DotReg(p)BE1-WhSpiral | 0 | 0 | 0 | EXACT_MATCH |
| BE1-DotReg(p)BE1-WoundSp | 0 | 0 | 0 | EXACT_MATCH |
| BE1-DotReg(p)BE1-Dghnt | 0 | 0 | 0 | EXACT_MATCH |
| BE1-DotReg(p)BE1-Amethyst | 0 | 0 | 0 | EXACT_MATCH |
| BE1-DotReg(p)BE1-Cowrie | 0 | 0 | 0 | EXACT_MATCH |
| BE1-DotReg(p)BE1-Orange | 0 | 0 | 0 | EXACT_MATCH |

#### Supplement Table 4 (T14)

| Relation / quantity | Published | Reproduced (unrounded) | Reproduced (2 dp) | Match |
|---|---|---|---|---|
| BE1-Koch20Ye(p)BE1-Disc | 0.99 | 0.986 | 0.99 | EXACT_MATCH |
| BE1-Koch20Ye(p)BE1-WhSpiral | 0.17 | 0.16833 | 0.17 | EXACT_MATCH |
| BE1-Koch20Ye(p)BE1-WoundSp | 0.05 | 0.05167 | 0.05 | EXACT_MATCH |
| BE1-Koch20Ye(p)BE1-Dghnt | 0.01 | 0.01467 | 0.01 | EXACT_MATCH |
| BE1-Koch20Ye(p)BE1-Amethyst | 0.01 | 0.014 | 0.01 | EXACT_MATCH |

#### Supplement Table 5 (T15)

| Relation / quantity | Published | Reproduced (unrounded) | Reproduced (2 dp) | Match |
|---|---|---|---|---|
| BE1-CylPen(p)BE1-Disc | 0.99 | 0.98767 | 0.99 | EXACT_MATCH |
| BE1-CylPen(p)BE1-WhSpiral | 0.3 | 0.29967 | 0.3 | EXACT_MATCH |
| BE1-CylPen(p)BE1-WoundSp | 0.12 | 0.12 | 0.12 | EXACT_MATCH |
| BE1-CylPen(p)BE1-Dghnt | 0.05 | 0.053 | 0.05 | EXACT_MATCH |
| BE1-Koch20Wh(p)BE1-Disc | 0.99 | 0.98733 | 0.99 | EXACT_MATCH |
| BE1-Koch20Wh(p)BE1-WhSpiral | 0.27 | 0.26767 | 0.27 | EXACT_MATCH |
| BE1-Koch20Wh(p)BE1-WoundSp | 0.1 | 0.10017 | 0.1 | EXACT_MATCH |
| BE1-Koch20Wh(p)BE1-Dghnt | 0.04 | 0.03883 | 0.04 | EXACT_MATCH |
| BE1-Koch49/50(p)BE1-Disc | 1 | 0.9975 | 1 | EXACT_MATCH |
| BE1-Koch49/50(p)BE1-WhSpiral | 0.67 | 0.67483 | 0.67 | EXACT_MATCH |
| BE1-Koch49/50(p)BE1-WoundSp | 0.46 | 0.458 | 0.46 | EXACT_MATCH |
| BE1-Koch49/50(p)BE1-Dghnt | 0.37 | 0.36967 | 0.37 | EXACT_MATCH |

#### Supplement Table 6 (T16)

| Relation / quantity | Published | Reproduced (unrounded) | Reproduced (2 dp) | Match |
|---|---|---|---|---|
| BE1-Koch34Wh(p)BE1-Disc | 0.93 | 0.933 | 0.93 | EXACT_MATCH |
| BE1-Koch34Wh(p)BE1-WhSpiral | 0.03 | 0.0325 | 0.03 | EXACT_MATCH |
| BE1-Koch34Wh(p)BE1-Dghnt | 0 | 0.00083 | 0 | EXACT_MATCH |
| BE1-Koch34Ye(p)BE1-Disc | 0.99 | 0.9895 | 0.99 | EXACT_MATCH |
| BE1-Koch34Ye(p)BE1-WhSpiral | 0.16 | 0.16433 | 0.16 | EXACT_MATCH |
| BE1-Koch34Ye(p)BE1-Dghnt | 0.01 | 0.01467 | 0.01 | EXACT_MATCH |

#### Supplement Table 7 (T17)

| Relation / quantity | Published | Reproduced (unrounded) | Reproduced (2 dp) | Match |
|---|---|---|---|---|
| BE1-Dot34(p)BE1-Disc | 0.99 | 0.98767 | 0.99 | EXACT_MATCH |
| BE1-Dot34(p)BE1-Dghnt | 0.05 | 0.049 | 0.05 | EXACT_MATCH |

#### Supplement Table 8 (T18)

| Relation / quantity | Published | Reproduced (unrounded) | Reproduced (2 dp) | Match |
|---|---|---|---|---|
| BE1-CylRound(p)BE1-Disc | 0.98 | 0.98467 | 0.98 | EXACT_MATCH |

#### Supplement Table 9 (T19)

| Relation / quantity | Published | Reproduced (unrounded) | Reproduced (2 dp) | Match |
|---|---|---|---|---|
| BE1-SegGlob(p)BE1-Disc | 0.99 | 0.98783 | 0.99 | EXACT_MATCH |

#### Supplement Table 10 (T20)

| Relation / quantity | Published | Reproduced (unrounded) | Reproduced (2 dp) | Match |
|---|---|---|---|---|
| BE1-Orange(p)BE1-Disc | 0.65 | 0.646 | 0.65 | EXACT_MATCH |
| BE1-WhSpiral(p)BE1-Disc | 0.38 | 0.38417 | 0.38 | EXACT_MATCH |
| BE2-c Metal(p)BE1-Disc | 0.65 | 0.65267 | 0.65 | EXACT_MATCH |
| BE1-Koch34Bl(p)BE1-Disc | 0.94 | 0.93783 | 0.94 | EXACT_MATCH |

#### Supplement section 10.1 text (T24)

| Relation / quantity | Published | Reproduced (unrounded) | Reproduced (2 dp) | Match |
|---|---|---|---|---|
| row 1: minimum of the 16 relations | 0.01 | 0.00933 | 0.01 | EXACT_MATCH |
| row 1: maximum of the 16 relations | 1 | 0.99967 | 1 | EXACT_MATCH |
| BE1-Disc certainly preceded by BE1-Reticella | 1 | 0.99917 | 1 | EXACT_MATCH |
| BE1-Disc certainly preceded by BE1-Melon | 1 | 0.99967 | 1 | EXACT_MATCH |
| BE1-Reticella(p)BE2-c | 0.01 | 0.00933 | 0.01 | EXACT_MATCH |
| BE1-Melon(p)BE2-c | 0.03 | 0.02733 | 0.03 | EXACT_MATCH |
| Reticella and Melon precede the other six Later types: minimum | 0.03 | 0.03267 | 0.03 | EXACT_MATCH |
| Reticella and Melon precede the other six Later types: maximum | 0.82 | 0.82183 | 0.82 | EXACT_MATCH |

#### Supplement section 10.2 text (T25)

| Relation / quantity | Published | Reproduced (unrounded) | Reproduced (2 dp) | Match |
|---|---|---|---|---|
| row 2: minimum of the 7 relations | 0 | 0 | 0 | EXACT_MATCH |
| row 2: maximum of the 7 relations | 0.19 | 0.19383 | 0.19 | EXACT_MATCH |
| BE1-Disc is the only Later type with any instance (count of Later types with frequency > 0) | 1 | 1 | 1 | EXACT_MATCH |

#### Supplement section 10.3 text (T26)

| Relation / quantity | Published | Reproduced (unrounded) | Reproduced (2 dp) | Match |
|---|---|---|---|---|
| row 3: minimum of the 5 relations | 0.01 | 0.014 | 0.01 | EXACT_MATCH |
| row 3: maximum of the 5 relations | 0.99 | 0.986 | 0.99 | EXACT_MATCH |
| BE1-Koch20Ye(p)BE1-Disc | 0.99 | 0.986 | 0.99 | EXACT_MATCH |
| other four: minimum | 0.01 | 0.014 | 0.01 | EXACT_MATCH |
| other four: maximum | 0.17 | 0.16833 | 0.17 | EXACT_MATCH |

#### Supplement section 10.4 text (T27)

| Relation / quantity | Published | Reproduced (unrounded) | Reproduced (2 dp) | Match |
|---|---|---|---|---|
| row 4: minimum of the 12 relations | 0.04 | 0.03883 | 0.04 | EXACT_MATCH |
| row 4: maximum of the 12 relations | 1 | 0.9975 | 1 | EXACT_MATCH |
| three Earlier(p)BE1-Disc: minimum | 0.99 | 0.98733 | 0.99 | EXACT_MATCH |
| three Earlier(p)BE1-Disc: maximum | 1 | 0.9975 | 1 | EXACT_MATCH |
| other nine: minimum | 0.04 | 0.03883 | 0.04 | EXACT_MATCH |
| other nine: maximum | 0.67 | 0.67483 | 0.67 | EXACT_MATCH |

#### Supplement section 10.5 text (T28)

| Relation / quantity | Published | Reproduced (unrounded) | Reproduced (2 dp) | Match |
|---|---|---|---|---|
| row 5: minimum of the relations | 0 | 0.00083 | 0 | EXACT_MATCH |
| row 5: maximum of the relations | 0.99 | 0.9895 | 0.99 | EXACT_MATCH |
| two Earlier(p)BE1-Disc: minimum | 0.93 | 0.933 | 0.93 | EXACT_MATCH |
| two Earlier(p)BE1-Disc: maximum | 0.99 | 0.9895 | 0.99 | EXACT_MATCH |
| other four: minimum | 0 | 0.00083 | 0 | EXACT_MATCH |
| other four: maximum | 0.16 | 0.16433 | 0.16 | EXACT_MATCH |

#### Supplement section 10.6 text (T29)

| Relation / quantity | Published | Reproduced (unrounded) | Reproduced (2 dp) | Match |
|---|---|---|---|---|
| row 6: minimum | 0.05 | 0.049 | 0.05 | EXACT_MATCH |
| row 6: maximum | 0.99 | 0.98767 | 0.99 | EXACT_MATCH |
| BE1-Dot34(p)BE1-Disc | 0.99 | 0.98767 | 0.99 | EXACT_MATCH |
| BE1-Dot34(p)BE1-Dghnt | 0.05 | 0.049 | 0.05 | EXACT_MATCH |

#### Supplement section 10.7 text (T30)

| Relation / quantity | Published | Reproduced (unrounded) | Reproduced (2 dp) | Match |
|---|---|---|---|---|
| BE1-CylRound(p)BE1-Disc | 0.98 | 0.98467 | 0.98 | EXACT_MATCH |

#### Supplement section 10.8 text (T31)

| Relation / quantity | Published | Reproduced (unrounded) | Reproduced (2 dp) | Match |
|---|---|---|---|---|
| BE1-SegGlob(p)BE1-Disc | 0.99 | 0.98783 | 0.99 | EXACT_MATCH |

#### Supplement section 10.9 text (T32)

| Relation / quantity | Published | Reproduced (unrounded) | Reproduced (2 dp) | Match |
|---|---|---|---|---|
| row 9: minimum | 0.38 | 0.38417 | 0.38 | EXACT_MATCH |
| row 9: maximum | 0.94 | 0.93783 | 0.94 | EXACT_MATCH |
| BE1-Koch34Bl(p)BE1-Disc | 0.94 | 0.93783 | 0.94 | EXACT_MATCH |
| others: minimum | 0.38 | 0.38417 | 0.38 | EXACT_MATCH |
| others: maximum | 0.65 | 0.65267 | 0.65 | EXACT_MATCH |

**Total quantitative comparisons (matrix-derived values, T05, T06, T12-T20, and
T24-T32): 96 values, 95 exact matches (99.0%).** The one non-match is T06
(suspected paper error, below). Every published Supplement Table cell equals R's
`round(x, 2)` of the reproduced frequency, including edge cases such as
BE1-Melon(p)BE1-Orange = 0.065, which R prints as 0.06 (as published) where
round-half-up would give 0.07.

Across all 34 targets, 276 values or memberships were compared and 273 matched.
The three non-matches are T06 and the two T22 histogram bins.

#### Ordinal and summary named values

- **T07** (`comparisons/values/T07-cylround-ancestor.csv`, section 8, oFD):
  BE1-CylRound is the unique most probable ancestor of BE1-Orange (0.950,
  against CylPen 0.924, Melon 0.842, and SegGlob 0.507), BE1-WoundSp (0.959,
  against 0.875, 0.365, and 0.835), and BE1-Dghnt (0.992, against 0.946, 0.440,
  and 0.908). EXACT_MATCH.
- **T08** (section 9, oFDm): for BE1-Dghnt, BE3-Amber gives 1.000, against
  Amethyst 0.132, Cowrie 0.271, and Disc 0.001. EXACT_MATCH.
- **T09** (54-relation summary): 54 relations, median 0.375, and 20 of 54 at or
  below 0.10, all identical to the published tables. All 12 relations above 0.9
  involve BE1-Disc. EXACT_MATCH.
- **T33** (R1 aid `allen_observe`): P(BE1-Dghnt equals BE1-Dghnt) = 1.
  EXACT_MATCH.
- **T34** (R1 aid `allen_observe`): the non-zero set is {p, o, D, d} = "poDd",
  an exact match. P(overlaps) = 0.725 exactly (4350 of 6000 samples). The
  published 0.73 is its round-half-up value, while R's `round()` gives 0.72.
  The difference of 0.005 lies within rounding of the 2-dp precision, so the
  outcome is WITHIN_PRECISION. The other relations are p 0.268, D 0.006, and
  d 0.001.
- **T22** (`comparisons/values/T22-supp-fig-2-bins.csv`, R1 aid histogram,
  0.1-wide bins from 0):

| Bin | Published bar | Reproduced, unrounded (planned method) | Reproduced, 2 dp, right-closed |
|-----|---------------|----------------------------------------|--------------------------------|
| [0, 0.1] | 20 | 19 | 20 |
| (0.1, 0.2] | 4 | 5 | 4 |
| (0.2, 0.3] | 2 | 2 | 2 |
| (0.3, 0.4] | 3 | 3 | 3 |
| (0.4, 0.5] | 3 | 3 | 3 |
| (0.5, 0.6] | 4 | 4 | 4 |
| (0.6, 0.7] | 4 | 4 | 4 |
| (0.7, 0.8] | 1 | 1 | 1 |
| (0.8, 0.9] | 1 | 1 | 1 |
| (0.9, 1] | 12 | 12 | 12 |

The single difference is BE1-Koch20Wh(p)BE1-WoundSp = 0.10017, which sits on
the 0.1 edge (published in Table 5 as 0.1). The planned method uses unrounded
values and gives 8 of 10 matching bins. Using the published 2-dp values, all 10
match. The difference comes only from an unpublished bin-edge and rounding
convention, so the outcome is MINOR_DISCREPANCY (ruling R1, as pre-stated in the
plan).

---

### Qualitative Results

#### Modes of change (Paper Figure 2, T01): R1 aid

- **Figure type:** diagram of six analytic Nökel lattices.
- **Data equivalence:** the relation memberships were verified numerically
  (`allen_illustrate()` result vectors), 78 of 78
  (`comparisons/values/T01-fig-2-memberships.csv`).
- **Structural match:** the published opaque sets are {o,F,D,d,f,O}, {m,M},
  {m,o,F,D,d,f,O,M}, all 13, {p}, and the 9 concurrent relations
  {o,F,s,D,e,d,S,f,O}. Each equals the corresponding aid output for
  `branching`, `transformation`, `reticulation`, `branch`, `transform`, and
  `reticulate`.
- **Acceptable differences:** panel titles and the plot theme are not scored,
  per the plan.
- **Verdict:** Match (EXACT_MATCH).

#### Occurrence plot (Paper Figure 3, T02)

- **Figure type:** statistical plot.
- **Data equivalence:** none could be checked. The authors' section 4 code stops
  before plotting: `burial.dates <- c(3:5, 7, 9, 12:78)` indexes column 78, but
  `read_oxcal()` returns 77 data columns for the published `beads-1.csv`
  (`outputs/checks/section-04-index-check.txt` and
  `outputs/logs/section-status.csv`).
- **Structural match:** the code's `x_min = 500, x_max = 700` also disagree with
  the published axis (about 400-800). The published figure therefore cannot
  have come from the published code and data as given.
- **Verdict:** CANNOT_COMPARE (code-data mismatch in the published materials;
  not corrected, because changing the indices would change the data selection).

#### Tempo plots (Paper Figure 4, T03)

- **Figure type:** composite panel (23 tempo plots).
- **Data equivalence:** the authors' section 6 code reproduces it
  (`outputs/test-bead-tempos.pdf`). Shape statistics are in
  `comparisons/values/T03-tempo-shape-summary.csv`.
- **Structural match:** the same 23 panels in the same order, with the same
  axes (400-800) and legend.
- **Scientific content:** every panel's mean curve and credible band match the
  published shapes by eye (200 dpi render). The text's two shape classes
  separate cleanly. Every "early" type (polychrome glass, amber, CylPen,
  CylRound, and BE2-c) has its median event at or before 590, and every "late"
  type (Cowrie, Disc, Amethyst, Dghnt, Orange, and WoundSp) at or after 626.
  BE1-Disc runs from 665 to 756, the later 7th to mid-8th century.
- **Acceptable differences:** the reproduction uses ggplot2's default grey panel
  background, while the published figure has white panels. That theme setting
  is not published.
- **Verdict:** Minor visual differences (MINOR_DISCREPANCY: the plan classes
  style differences this way).

#### Phyletic seriation diagram (Paper Figure 6, T04)

- **Figure type:** hand-composed diagram.
- **Data equivalence:** all 8 depicted links are supported by the reproduced
  probabilities (`comparisons/values/T04-fig-6-links.csv`):
  - CylRound(oFD): Orange 0.95, SegGlob 1.00, WoundSp 0.96, Dghnt 0.99;
  - Amber(oFDm)Dghnt: 1;
  - Amber(oFD): Cowrie 1, Amethyst 1;
  - Cowrie(oFD)Disc: 1.00.
- **Scientific content:** relative temporal placement agrees: early columns
  (Melon, CylPen, CylRound, Amber) are low, and the late types are high. The
  illustration-box positions were measured on a 400 dpi render and compared
  with the reproduced first and last event years
  (`comparisons/values/T04-fig-6-placements.csv`). The largest differences, in
  years, are: Disc lower box 47, Cowrie upper 42, Amethyst upper 41, WoundSp
  upper 34, Orange 33, and Dghnt upper 28; all others are within 20 years. The
  placement convention ("approximate median date") is not published.
- **Verdict:** Minor differences (MINOR_DISCREPANCY: placement differences
  within a few decades, as pre-stated).

#### Analytic and empirical lattices (Supplement Figure 1, T21): R1 aids

- **Data equivalence:** 26 of 26 memberships match: the top panel shows all 13
  relations, and the bottom panel only "equals", with P = 1 and the identical
  title "BE1-Dghnt(e)BE1-Dghnt".
- **Acceptable differences:** the reproduction has a grey panel background, and
  its top panel carries a one-value legend that the published panel lacks.
- **Verdict:** Minor visual differences (MINOR_DISCREPANCY, styling and legend,
  per the plan).

#### Expected versus observed lattices (Supplement Figure 3, T23): R1 aids

- **Data equivalence:** 26 of 26 memberships match. In the right panel
  (`allen_observe`), the title "BE1-Koch20Wh(poDd)BE1-WhSpiral" and the legend
  breaks (0.0 to 0.6) are identical, and "overlaps" is the most opaque label.
  The left panel {p} is rendered with the documented
  `allen_illustrate("transform")` (composition m∘m = p), so the plan's feared
  CANNOT_COMPARE for that panel did not arise.
- **Acceptable differences:** grey panel background.
- **Verdict:** Minor visual differences (MINOR_DISCREPANCY).

---

### Methodology

1. **Environment:** Docker image `llmr-dye-et-al-2023-attempt-02`, built from
   `rocker/r-ver:4.2.3` with CRAN pinned to the Posit Package Manager snapshot
   of 2023-03-23 and ArchaeoPhases 1.8 from the CRAN archive (sha256-verified).
   It built in one iteration and every run used `--network none` (see
   `environment.md`).
2. **Data:** `beads-1.csv` from `https://tsdye.online/AP/beads-1.csv`, sha256
   `02cf52d4…9051`, identical to the planner's copy and checked again at the
   start of every run (`outputs/logs/input-checksum.txt`).
3. **Analysis:** the authors' printed R code (supplement sections 4-10) was
   transcribed (`tools/transcribe_supplement.py`, then `authors-code/`) with
   path-only edits, and run in batch in one R session by `run-analysis.R`.
   Section 3 was not executed because four inputs are missing. All steps are
   deterministic given the fixed MCMC file.
4. **Comparison:** published values were transcribed from paper pp. 7-21 and
   supplement pp. 23-49 (`comparisons/published-values.csv`, with figure
   readings encoded in `scripts/compare.R`). They were compared value by value
   by `scripts/compare.R` inside Docker. Figures were compared visually against
   high-resolution renders of the published pages. R1 aids live in
   `scripts/verification-aids.R`, separate from the authors' code.

### Why Exact Matches Are Expected

`allen_observe_frequency()` is a deterministic tally over the 6,000 archived
MCMC samples, and `tempo_plot()` and `allen_observe()` likewise summarise fixed
draws without random numbers. Given the same `beads-1.csv`, the same column
labels, and the same function definitions, every value must match exactly at
the published precision. Any difference therefore points to a transcription,
version, or input problem, or to a paper error, not to Monte Carlo variation.
The 95 of 96 exact matches, including R-specific rounding edge cases, confirm
that the inputs and code are identical to the authors'. This sharpens the one
discrepancy (T06).

### Paper Errors Identified

**T06 — BE1-Cowrie(oFD)BE1-Disc (suspected PAPER_ERROR; escalated for human
confirmation).**

1. **Published:** paper p.16, l.374-376: "bead type BE1-Disc most likely
   descended from bead type BE1-Cowrie; their relation satisfies the expected
   branching relation with a probability of 0.87."
2. **Reproduced:** the authors' supplement section 7 code on the published
   `beads-1.csv` gives P(BE1-Cowrie oFD BE1-Disc) = 0.99967, which is 1.00 at
   2 dp.
3. **Independent verification:**
   - The published 0.87 is present in the same section 7 matrix, as
     P(BE1-Amethyst oFD BE1-Disc) = 0.86717
     (`comparisons/values/T06-section-07-full-matrix.csv`). The most plausible
     explanation is a misread row.
   - Applying the same published code to the same published data reproduces
     every one of the 54 tabulated values in Supplement Tables 2-10 exactly, so
     the computation pipeline is the authors'.
   - Matrix orientation is fixed by the paper's own T05 statement
     (BE3-Amber(oFD)BE1-Amethyst = 1, converse 0).
   - The paper's qualitative inference is unaffected, and indeed stronger: Disc
     is most likely descended from Cowrie (1.00), ahead of Amethyst (0.87) and
     Amber (0.83).
   - The residual alternative is that the text value came from an unpublished
     MCMC run. The between-run variability the supplement reports (p.23: mean 1.3 years)
     makes a shift from 1.00 to 0.87 implausible, but T10 and T11 cannot be
     tested.
4. **Classification:** PAPER_ERROR, per the paper-error rule of
   verdicts-and-precision v1.0. It must not enter study data before human
   confirmation.

**Recorded finding, not a target (approver ruling):** supplement section 10.5
states "The nine Earlier(p)Later relations" (p.42), while the same subsection
says "Each of the six relations" (p.41). Table 6 has 6 cells and the
reproduction gives 6, so "nine" is an internal slip.

### Scope Limitation(s)

- **Proprietary upstream:** OxCal 4.4.2 MCMC generation (`beads.oxcal`,
  mmc2.zip) is not reproduced here; it is out of scope by run-note ruling and
  handled by attempt-03. The archived `beads-1.csv` substitutes for it.
- **Data unavailability:** the five-run replicability analysis (T10 and T11:
  Supplement Table 1 with 462 values and its summary) needs `beads-0/2/3/4.csv`.
  These are unpublished and return HTTP 404 at the author's server. They are
  untestable and count against coverage (ruling R2). Data availability is L6
  under the plan's two-dataset enumeration (see `environment.md`).
- **Publishing error (code-data mismatch):** paper Fig 3 (T02) cannot be
  produced, because the published section 4 code does not fit the published
  data file.
- **No author code:** paper Fig 2 and Supplement Figs 1-3 (T01, T21-T23) and
  the section 11/12 values (T33, T34) were tested with R1 verification aids
  only.
- **Version of record:** page references follow the White Rose accepted
  manuscript (corpus `vor.pdf`); the approver accepted this for the attempt.

### Verdict Justification

**PARTIAL.** Every computational result the supplement tabulates reproduces
exactly from the authors' own code and archived MCMC output: 95 of 96 numeric
values and all ordinal inferences. The tempo plots and lattice figures match in
scientific content, differing only in unpublished styling and bin-edge
conventions. Two analyses could not be reproduced, however:

- the occurrence plot (Fig 3), whose published code fails on the published
  data;
- the five-run replicability analysis (Supplement Table 1), whose inputs are
  unavailable.

In addition, one main-text probability (T06) appears to be misreported, though
without affecting the conclusion. Coverage is 25 of 34 (0.735). Because these
substantive analyses are missing, the verdict is PARTIAL rather than
SUCCESSFUL, and it is provisional pending human confirmation of the T06
PAPER_ERROR call and the T02, T10, and T11 CANNOT_COMPARE calls.
