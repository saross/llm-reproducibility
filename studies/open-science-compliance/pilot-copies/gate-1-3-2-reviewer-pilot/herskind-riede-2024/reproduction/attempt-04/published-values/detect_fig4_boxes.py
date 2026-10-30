#!/usr/bin/env python3
"""Detect the small culture-exclusive boxes on the published Fig. 4 (transcription aid).

Purpose
-------
Herskind and Riede (2024) Fig. 4 is a 49 x 49 Pointwise Mutual Information
(PMI) heatmap whose small coloured boxes (added in GIMP) mark motif pairs
"limited to one specific culture complex" (purple Maglemose, red Kongemose,
yellow Ertebolle). This script transcribes which cells carry a box, and in
which colour, from pixel colours, so that the box placement can be compared
with a read-only lookup in the deposited data. It reads only the published
figure (extracted with ``pdfimages -png`` from page 6 of the version of
record, kept outside the repository).

Method
------
1. Box outline pixels are classified by colour (yellow, red, purple); heatmap
   fills are excluded because their red channel is saturated (white-to-red
   gradient), unlike the box red.
2. Connected components of one box colour with a single-cell bounding box
   (about 20-28 px) give box centres; a linear fit of centre against integer
   cell index gives the grid origin and pitch on each axis.
3. Each cell of the 49 x 49 grid is tested: a box is recorded when at least
   three of the four sides of its border band (1 px outside to 5 px inside
   the cell edge) are at least 25 % one box colour.
4. Cells are named by the axis order printed on the figure (x left to right,
   y bottom to top; the same order on both axes).

Usage
-----
    python3 -I detect_fig4_boxes.py <fig4.png> <out.csv>
"""
from __future__ import annotations

import csv
import sys
from collections import deque
from pathlib import Path

from PIL import Image

# Axis order as printed on Fig. 4 (left to right; bottom to top).
ORDER = ["A14", "B3", "A24", "B10", "B2", "B12", "E4", "A5", "D5", "B13", "B4", "B1",
         "A1", "A3", "ANT", "F12", "E1", "B6", "E5", "F5", "F13", "F38", "D29", "B8",
         "D33", "H1", "G2", "C1", "F14", "I1", "F35", "ZOO", "D19", "G1", "D3", "D15",
         "F15", "C12", "C14", "C5", "C13", "C4", "C6", "D7", "F55", "G7", "I13", "I5",
         "RELIEF"]
COLOURS = {"Ertebolle": (247, 205, 40), "Kongemose": (208, 120, 122),
           "Maglemose": (178, 158, 200)}


def box_colour(p: tuple[int, int, int]) -> str | None:
    """Return the culture whose box colour matches pixel p, if any."""
    best, dist = None, 10 ** 9
    for name, ref in COLOURS.items():
        d = sum((a - b) ** 2 for a, b in zip(p, ref))
        if d < dist:
            best, dist = name, d
    return best if dist <= 45 ** 2 else None


def components(img: Image.Image) -> list[tuple[str, int, int, int, int]]:
    """Connected components of box-coloured pixels: (colour, x0, y0, x1, y1)."""
    w, h = img.size
    px = img.load()
    label = [[None] * w for _ in range(h)]
    for y in range(h):
        for x in range(w):
            label[y][x] = box_colour(px[x, y])
    seen = [[False] * w for _ in range(h)]
    out = []
    for y in range(h):
        for x in range(w):
            if label[y][x] is None or seen[y][x]:
                continue
            colour = label[y][x]
            queue = deque([(x, y)])
            seen[y][x] = True
            xs, ys = [x], [y]
            while queue:
                cx, cy = queue.popleft()
                for nx, ny in ((cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)):
                    if 0 <= nx < w and 0 <= ny < h and not seen[ny][nx] \
                            and label[ny][nx] == colour:
                        seen[ny][nx] = True
                        queue.append((nx, ny))
                        xs.append(nx)
                        ys.append(ny)
            out.append((colour, min(xs), min(ys), max(xs), max(ys)))
    return out


def fit(centres: list[float], guess0: float, pitch: float) -> tuple[float, float]:
    """Least-squares fit of centre = origin + pitch * index, indices by rounding."""
    for _ in range(3):
        pairs = [(round((c - guess0) / pitch), c) for c in centres]
        n = len(pairs)
        mk = sum(k for k, _ in pairs) / n
        mc = sum(c for _, c in pairs) / n
        sxx = sum((k - mk) ** 2 for k, _ in pairs)
        pitch = sum((k - mk) * (c - mc) for k, c in pairs) / sxx
        guess0 = mc - pitch * mk
    return guess0, pitch


def main() -> int:
    """Detect boxes and write one row per boxed cell."""
    src, dest = Path(sys.argv[1]), Path(sys.argv[2])
    img = Image.open(src).convert("RGB")
    px = img.load()
    comps = [c for c in components(img)
             if 18 <= c[3] - c[1] <= 30 and 18 <= c[4] - c[2] <= 30]
    cx = [(c[1] + c[3]) / 2 for c in comps]
    cy = [(c[2] + c[4]) / 2 for c in comps]
    # First guesses from the printed tick positions (A14 column, RELIEF row).
    x0, px_pitch = fit(cx, 90.0, 23.8)
    y0, py_pitch = fit(cy, 97.5, 26.25)   # y index 0 is the top row (RELIEF)
    rows = []
    for i in range(49):            # column index, left to right
        for j in range(49):        # row index, top to bottom
            xc, yc = x0 + px_pitch * i, y0 + py_pitch * j
            hx, hy = px_pitch / 2, py_pitch / 2
            sides = {
                "top": [(int(xc + t), int(yc - hy + d)) for t in range(-8, 9) for d in range(-1, 6)],
                "bottom": [(int(xc + t), int(yc + hy - d)) for t in range(-8, 9) for d in range(-1, 6)],
                "left": [(int(xc - hx + d), int(yc + t)) for t in range(-8, 9) for d in range(-1, 6)],
                "right": [(int(xc + hx - d), int(yc + t)) for t in range(-8, 9) for d in range(-1, 6)],
            }
            votes: dict[str, int] = {}
            for points in sides.values():
                tally: dict[str, int] = {}
                for x, y in points:
                    if 0 <= x < img.width and 0 <= y < img.height:
                        name = box_colour(px[x, y])
                        if name:
                            tally[name] = tally.get(name, 0) + 1
                for name, count in tally.items():
                    # Each side band runs from 1 px outside the cell edge to
                    # 5 px inside it (7 rows of 17 points); the 3 px outline,
                    # drawn 1-4 px inside the edge, fills about 40 % of it,
                    # while a neighbour's outline lies beyond the band.
                    if count >= 0.25 * len(points):
                        votes[name] = votes.get(name, 0) + 1
            hits = [n for n, v in votes.items() if v >= 3]
            if hits:
                col_token, row_token = ORDER[i], ORDER[48 - j]
                rows.append({"x_token": col_token, "y_token": row_token,
                             "pair": " ".join(sorted([col_token, row_token])),
                             "colour_culture": "|".join(sorted(hits))})
    with dest.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"grid x0={x0:.2f} pitch={px_pitch:.3f}; y0={y0:.2f} pitch={py_pitch:.3f}; "
          f"{len(comps)} single-cell components; {len(rows)} boxed cells -> {dest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
