# herskind-riede-2024 T11 completion (operator deviation, 2026-10-04)

**Why this exists.** The executor's approved verification aid for T11 (paper
Fig. 4, the culture-exclusive boxes) covered only bigrams with observed
frequency > 2. It found 32 single-culture cells, and all 32 carried a
matching box. But the Fig. 4 caption covers every displayed pair: "Motif
combinations limited to one specific culture complex are marked with a small,
coloured box". The executor scored T11 WITHIN_PRECISION with the observed
≤ 2 cells untested. The reviewer flagged the inconsistency with T14. Shawn
ruled (2026-10-04, shakedown human queue item 4) that the check should be
completed, and that **a check's planned scope must cover the target's full
tolerance**.

This is an operator action after execution, not an executor artefact. The
attempt-02 directory is untouched; inputs were mounted read-only.

## Method

1. `t11-all-bigrams.R` applies the authors' `createResultTable()`, parsed
   verbatim from S2.R exactly as the executor's `compare.R` does, to **all**
   467 bigrams whose motifs are both on the 49-motif Fig. 4 axis. It ran in
   the kept image `llmr-herskind-riede-2024-attempt-02`. Output:
   `t11-expected-boxes-all-bigrams.csv` (291 single-culture pairs).
2. `t11-detect-boxes.py` locates the cell grid from the published figure's
   tick marks: 49 rows about 26.2 px apart and 49 columns about 23.8 px apart,
   at 300 ppi. It then tests all four sides of a box outline in each of the
   1,176 displayed cells against three calibrated outline colours. Output:
   `t11-cell-comparison.csv`. The published raster is publisher content and
   is not committed; the script's docstring gives the `pdfimages` command
   that extracts it from the corpus store.
3. Both mismatches were confirmed by eye on enlarged crops.

## Result

| Cells | Expected | Agree |
|---|---|---|
| Single-culture, observed > 2 | 32 | 32 |
| Single-culture, observed ≤ 2 | 259 | 257 |
| No box expected | 885 | 885 (no spurious boxes) |
| **All displayed cells** | **1,176** | **1,174** |

The two disagreements are both in the hand-drawn (GIMP) layer, and both
involve bigrams observed once:

- **B1/B2:** Maglemose-only in the authors' data, so a purple box is
  expected. The published cell has no box.
- **C5/F13:** Kongemose-only in the authors' data, so a red box is expected.
  The published box is yellow.

The published figure treats S1's mixed `Kongemose/Ertebølle` level as a level
of its own, exactly as the authors' function does (15 cells, all agree).

## Classification (Shawn, 2026-10-04)

**PAPER_ERROR**, on the T04 standard: the figure disagrees with the authors'
deposited data under the authors' own function. The plan's tolerance requires
culture-exclusive assignments to match, so T11 leaves WITHIN_PRECISION.
PAPER_ERROR is outside the coverage numerator (`REPRODUCED_OUTCOMES` in
`scripts/reproduction-lane.py`), so **herskind coverage is 11/15 = 0.733**.
