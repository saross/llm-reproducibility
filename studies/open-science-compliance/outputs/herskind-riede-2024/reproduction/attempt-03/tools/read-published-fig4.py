"""Read the published Fig. 4 heatmap cell by cell (transcription aid, host-side).

Purpose
    Transcribe two things from the published Herskind & Riede (2024) Fig. 4
    image for comparison target T06, so that the comparison itself can run in
    the lane container against the authors' outputs:
      1. the small culture-exclusive boxes (yellow = Ertebolle, red =
         Kongemose, purple = Maglemose, per the figure caption), and
      2. each cell's centre colour (the heatmap fill).
    It reads only the publisher's figure image; it runs no authors' code and
    computes nothing from the data. It is a reading tool, like zooming in.

Input
    The figure's embedded image, extracted from the paper PDF (publisher
    content, never stored in the repository):
        pdfimages -j -f 6 -l 6 <corpus>/herskind-riede-2024/vor.pdf fig
    gives fig-000.jpg (1423 x 1375 px, 300 ppi), the Fig. 4 image.

Method
    Grid: the 49 x 49 cell centres, fitted from cell-sized outline boxes
    found as connected components of box-outline colours: column c at
    x = 94.0 + (c - 1) * 23.74 px; row r (A14 = 1 at the bottom, RELIEF = 49
    at the top) at y = 97.2 + (49 - r) * 26.23 px. Axis order as printed on
    the figure (identical to S2.R lines 651-658).
    Boxes: for each lower-triangle cell (column position < row position),
    each of the four sides of a small inset square is tested for the three
    outline colours; a box is read when every side has a pixel line that is
    at least 50% one colour. Requiring all four sides excludes the edges of
    the large GIMP grouping boxes, which cross only one side of a cell.
    Centre colour: mean RGB of the 5 x 5 px at the cell centre; a cell is
    flagged occluded when its 15 x 15 px centre window contains dark pixels
    (inset line drawings).

Usage
    python3 -I tools/read-published-fig4.py <fig-000.jpg> > published-values/fig4-cells.csv
"""
import csv
import sys

import numpy as np
from PIL import Image

AXIS = ["a14", "b3", "a24", "b10", "b2", "b12", "e4", "a5", "d5", "b13", "b4", "b1", "a1",
        "a3", "ant", "f12", "e1", "b6", "e5", "f5", "f13", "f38", "d29", "b8", "d33", "h1",
        "g2", "c1", "f14", "i1", "f35", "zoo", "d19", "g1", "d3", "d15", "f15", "c12", "c14",
        "c5", "c13", "c4", "c6", "d7", "f55", "g7", "i13", "i5", "relief"]
X0, PX = 94.0, 23.74   # column 1 centre and column pitch (px)
Y49, PY = 97.2, 26.23  # row 49 (RELIEF) centre and row pitch (px)


def masks(rgb: np.ndarray) -> dict[str, np.ndarray]:
    """Boolean masks of the three box-outline colours."""
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    return {
        "Ertebølle": (r > 215) & (g > 165) & (b < 110) & (r - b > 120),
        "Kongemose": ((r > 160) & (r < 235) & (g > 80) & (g < 150) & (b > 80) & (b < 150)
                      & (r - g > 50)),
        "Maglemose": ((b > 150) & (r > 120) & (r < 200) & (g > 110) & (g < 175)
                      & (b - g > 25)),
    }


def side_score(mask: np.ndarray, cx: int, cy: int) -> float:
    """Smallest, over the four sides, of the best line's outline fraction."""
    bands = {
        "left": mask[cy - 7:cy + 8, cx - 12:cx - 7].mean(axis=0),
        "right": mask[cy - 7:cy + 8, cx + 8:cx + 13].mean(axis=0),
        "top": mask[cy - 13:cy - 7, cx - 7:cx + 8].mean(axis=1),
        "bottom": mask[cy + 8:cy + 14, cx - 7:cx + 8].mean(axis=1),
    }
    return float(min(v.max() for v in bands.values()))


def main(path: str) -> None:
    """Write one CSV row per lower-triangle cell to standard output."""
    rgb = np.asarray(Image.open(path).convert("RGB")).astype(int)
    outline = masks(rgb)
    dark = rgb.sum(axis=2) < 240
    out = csv.writer(sys.stdout, lineterminator="\n")
    out.writerow(["x_motif", "y_motif", "box_class", "box_score", "centre_r", "centre_g",
                  "centre_b", "occluded"])
    for r in range(1, 50):
        for c in range(1, r):
            cx = int(round(X0 + (c - 1) * PX))
            cy = int(round(Y49 + (49 - r) * PY))
            scores = {k: side_score(m, cx, cy) for k, m in outline.items()}
            best = max(scores, key=scores.get)
            box = best if scores[best] >= 0.5 else ""
            centre = rgb[cy - 2:cy + 3, cx - 2:cx + 3].reshape(-1, 3).mean(axis=0)
            occluded = bool(dark[cy - 7:cy + 8, cx - 7:cx + 8].any())
            out.writerow([AXIS[c - 1].upper(), AXIS[r - 1].upper(), box,
                          round(scores[best], 2), *[int(round(v)) for v in centre],
                          str(occluded).upper()])


if __name__ == "__main__":
    main(sys.argv[1])
