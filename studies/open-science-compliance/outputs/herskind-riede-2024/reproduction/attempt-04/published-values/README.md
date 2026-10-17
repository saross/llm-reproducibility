# Published values: Herskind and Riede (2024)

Transcribed from the version of record (Journal of Archaeological Science
165, 105969; corpus store `vor.pdf`, sha256
`5c60cc3d6fce9f297c44fc62384e0caada1251416066d872ea020feec145fad0`) and the
deposit's S3 file, **before the first `run-container` call** (executor v1.7,
F6). Transcription completed 2026-10-17 around 05:28 UTC; no image build or
run had taken place.

Figures in the paper are raster images. They were extracted at their native
300 pixels per inch (ppi) with `pdfimages -png` into the executor's scratch
directory (publisher content, kept out of the repository) and read there.

| File | Target(s) | Source | Method |
|------|-----------|--------|--------|
| `table1-published.csv`, `table1-totals-published.csv` | T05 | Table 1, p. 4 (text layer) | Copied cell by cell; row sums checked against the printed n (230, 1543, 4422, 8466) |
| `table2-published.csv` | T06 | Table 2, p. 6 (text layer) | Copied |
| `table3-published.csv` | T07, T17, T18 | Table 3, p. 7 (text layer) | Copied |
| `fig3-published.csv` | T02, T11, T12, T14, T15 | Fig. 3, p. 5 | PMI labels (four decimals) and motif tuples read by eye from 3x enlargements; bar totals and chronology segments measured from pixel colours by `measure_fig3_bars.py` (largest rounding residual 0.12 of one unit); totals agree with Table 1's frequency distribution |
| `fig2-bars-published.csv` | T01 | Fig. 2 bar panel, p. 3 | Category order read by eye; segments measured by `measure_fig3_bars.py --fig2` at 3.2 px per object, so counts are approximate (about +/-1 per segment); "slotted point" read by eye |
| `fig4-axis-and-large-boxes.csv`, `fig4-boxes-published.csv` | T03, T16 | Fig. 4, p. 6 | Axis order read by eye; the 290 small boxes detected by `detect_fig4_boxes.py` and checked by overlaying the detections on the figure (every box marked, no false marks) |
| `fig5-published.csv` | T04 | Fig. 5, p. 7 | Pie colours read by eye against the legend (C4 red, C5 green, C12 yellow, C13 orange, D7 purple); positions in pixels of a 2x enlargement of the crop (100, 150)-(750, 850) |
| `named-values-published.csv` | T09-T18 | Text, pp. 2-7 | Copied |

T08's published values are the deposited `deposit/Herskind&Riede_S3.xlsx`
itself (Zenodo record 10801706), compared cell by cell.

## Fig. 2 map panel (T01, visual)

Several hundred points across Denmark, southern Sweden (Scania), and
northernmost Germany and Poland, coloured by chronology: Maglemose (purple)
dense on Zealand and widespread inland, Ertebølle (yellow) widespread and
largely coastal, Kongemose (red) and Kongemose/Ertebølle (orange) sparse.
Basemap, scale bar (0-150 km), and north arrow.

## Observations made during transcription

- Fig. 3b shows **nine** all-yellow (Ertebølle-only) bars: the eight the
  text lists (p. 4) plus C5-C12 (PMI 2.1890). The text's stated count (nine)
  agrees with the figure; its list omits C5-C12.
- Fig. 3b's last two bars, I1-I5 and E1-F14, share the label 1.9584, so the
  21-bar cut-off may sit in a PMI tie.
- Fig. 4 carries 290 small boxes, more than the 165 bigrams with observed
  frequency of 3 or more that the code plots. The boxes therefore mark
  culture-exclusive pairs at any frequency, not only the plotted pairs. The
  paper does not state the box criterion.
- Fig. 4's colour scale maps every PMI at or below 0.5 to white
  (`scale_fill_gradient2(mid = "white", midpoint = 0.5)` in S2.R), so a white
  cell may hold a plotted pair.
