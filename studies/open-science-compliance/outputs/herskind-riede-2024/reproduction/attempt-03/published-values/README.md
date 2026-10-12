# Published values transcribed for comparison (attempt 03)

Values transcribed from Herskind and Riede (2024), Journal of Archaeological
Science 165, 105969 (version of record, corpus store `vor.pdf`, sha256
`5c60cc3d6fce9f297c44fc62384e0caada1251416066d872ea020feec145fad0`), for the
locked targets of the approved plan. The paper itself is publisher content
and is not stored here; these files hold only the printed values needed for
the comparison, which `compare-results.R` reads inside the lane container.

| File | Target | Source and method |
|------|--------|-------------------|
| `table1.csv`, `table1-totals.csv` | T01 | Table 1 (p. 4), from the PDF text layer (`pdftotext -layout`) |
| `table2.csv` | T02 | Table 2 (p. 6), from the PDF text layer |
| `table3.csv` | T03 | Table 3 (p. 7), from the PDF text layer |
| `fig3.csv` | T05 | Fig. 3 (p. 5), raster figure: labels and PMI values read at full zoom of the embedded 300 ppi image; bar totals and per-chronology segments read against the frequency gridlines |
| `fig2-left.csv` | T04 | Fig. 2 left panel (p. 3): segments measured with `tools/read-published-fig2.py` on the embedded 300 ppi image |
| `fig4-cells.csv` | T06 | Fig. 4 (p. 6): box state and centre colour of every lower-triangle cell, read with `tools/read-published-fig4.py`; the two cells that disagree with the lookup were checked by eye at 4x zoom |
| `fig5-pies.csv` | T07 | Fig. 5 (p. 7): pie-chart motif membership read by eye at 4x zoom; pie centres in pixels of the embedded image (approximate, for relative position only) |
| `named-values.csv` | T09-T20 | Named values in the text (pp. 2-7), as stated |

The embedded images were extracted with `pdfimages -j` into a scratch
directory outside the repository (Fig. 2: page 3; Fig. 3: page 5; Fig. 4:
page 6; Fig. 5: page 7).
