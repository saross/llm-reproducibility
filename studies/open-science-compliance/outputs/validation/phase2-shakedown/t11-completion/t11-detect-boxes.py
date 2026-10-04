#!/usr/bin/env python3
"""Detect the culture boxes in herskind-riede-2024's published Fig. 4 and compare.

Operator deviation (Shawn's ruling, 2026-10-04, shakedown human queue item 4):
completes T11 by testing every displayed Fig. 4 cell, not only the
observed > 2 cells the executor's approved aid covered.

Method
------
1. The published Fig. 4 is a 300 ppi raster embedded in the paper PDF. Extract
   it outside the repository (publisher content stays in the corpus store):

       pdfimages -f 6 -l 6 -j ~/corpora/llm-reproducibility/\
herskind-riede-2024/vor.pdf <scratch>/fig4

2. Locate the 49 row and 49 column tick marks (dark runs at fixed x and y);
   their centres give the cell grid.
3. For every displayed cell (the upper-left triangle: row motif later on the
   axis than the column motif), test the four sides of a box outline. A side
   is present for a colour class when at least ``SIDE_MIN`` of its scan lines
   contain a pixel of that class. A box is detected when all four sides are
   present; neighbouring boxes can supply one side but never four.
4. Compare with ``t11-expected-boxes-all-bigrams.csv`` (the authors'
   createResultTable over all bigrams, from ``t11-all-bigrams.R``).

Colour classes were calibrated on known boxes (yellow ~(251, 210, 43), purple
~(179, 160, 195), red ~(213, 115, 117)); PMI fill (R = 255, G > B) falls in
none of them.

Usage
-----
    python3 t11-detect-boxes.py <fig4.jpg> [--overlay <out.png>]

Writes ``t11-cell-comparison.csv`` beside this script and prints a summary.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

HERE = Path(__file__).resolve().parent

# The authors' manual chronological order (S2.R Part 7), bottom/left to top/right.
AXIS = [
    "A14", "B3", "A24", "B10", "B2", "B12", "E4", "A5", "D5", "B13", "B4", "B1",
    "A1", "A3", "ANT", "F12", "E1", "B6", "E5", "F5", "F13", "F38", "D29", "B8",
    "D33", "H1", "G2", "C1", "F14", "I1", "F35", "ZOO", "D19", "G1", "D3", "D15",
    "F15", "C12", "C14", "C5", "C13", "C4", "C6", "D7", "F55", "G7", "I13", "I5",
    "RELIEF",
]

SIDE_MIN = 0.6  # fraction of a side's scan lines that must hit the colour

# Side bands relative to the cell centre (pixels), calibrated on known boxes:
# outline edges sit at about -11..-8 / +8..+11 horizontally and -13..-11 /
# +9..+11 vertically; neighbouring cells' edges start beyond +/-12.8 (x) and
# +/-13 (y).
BAND_X = {"left": (-12, -8), "right": (7, 11)}
BAND_Y = {"top": (-14, -9), "bottom": (7, 12)}
ALONG = 5  # half-length of each side segment tested (avoids the corners)


def classify(img: np.ndarray) -> dict[str, np.ndarray]:
    """Return boolean masks for the three box-outline colour classes.

    Args:
        img: H x W x 3 integer RGB array.

    Returns:
        Mapping of colour name to a boolean H x W mask.
    """
    r, g, b = img[..., 0], img[..., 1], img[..., 2]
    return {
        "yellow": (r >= 225) & (g >= 170) & (g <= 240) & (b <= 130),
        "purple": (r >= 150) & (r <= 205) & (g >= 130) & (g <= 185)
        & (b >= 175) & (b <= 220) & (b > r) & (r > g),
        "red": (r >= 190) & (r <= 235) & (g >= 90) & (g <= 160)
        & (b >= 90) & (b <= 160) & (np.abs(g - b) <= 20),
    }


def tick_centres(line: np.ndarray) -> list[float]:
    """Return the centres of dark runs along a 1-D greyscale profile."""
    idx = np.where(line < 120)[0]
    runs, start, prev = [], idx[0], idx[0]
    for i in idx[1:]:
        if i != prev + 1:
            runs.append((start + prev) / 2)
            start = i
        prev = i
    runs.append((start + prev) / 2)
    return runs


def side_score(mask: np.ndarray, cx: float, cy: float, side: str) -> float:
    """Fraction of scan lines across one side band that contain a mask pixel.

    Args:
        mask: Boolean colour mask.
        cx: Cell centre x (pixels).
        cy: Cell centre y (pixels).
        side: One of left, right, top, bottom.

    Returns:
        Hit fraction in [0, 1].
    """
    x0, y0 = round(cx), round(cy)
    if side in BAND_X:
        lo, hi = BAND_X[side]
        lines = [mask[y, x0 + lo:x0 + hi + 1].any()
                 for y in range(y0 - ALONG, y0 + ALONG + 1)]
    else:
        lo, hi = BAND_Y[side]
        lines = [mask[y0 + lo:y0 + hi + 1, x].any()
                 for x in range(x0 - ALONG, x0 + ALONG + 1)]
    return float(np.mean(lines))


def main() -> None:
    """Detect boxes, compare with the expected set, and write the CSV."""
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("image", type=Path, help="Fig. 4 raster extracted from the PDF")
    ap.add_argument("--overlay", type=Path, help="optional QA overlay PNG (keep out of git)")
    args = ap.parse_args()

    img = np.asarray(Image.open(args.image).convert("RGB")).astype(int)
    grey = img.mean(axis=2)
    masks = classify(img)

    # Grid from tick marks: row ticks at x = 76, column ticks at y = 78.
    ys = tick_centres(grey[:, 76])  # top (RELIEF) to bottom (A14)
    xs = tick_centres(grey[78, :])  # left (A14) to right (RELIEF)
    assert len(ys) == 49 and len(xs) == 49, (len(ys), len(xs))
    ys = ys[::-1]  # index 0 = A14 (bottom row)

    expected = {}
    with open(HERE / "t11-expected-boxes-all-bigrams.csv", encoding="utf-8") as fh:
        for rec in csv.DictReader(fh):
            expected[(rec["row"], rec["col"])] = rec

    rows_out = []
    for ri, row in enumerate(AXIS):
        for ci, col in enumerate(AXIS[:ri]):  # displayed triangle only
            cx, cy = xs[ci], ys[ri]
            best, best_min = "", 0.0
            for colour, mask in masks.items():
                m = min(side_score(mask, cx, cy, s) for s in ("left", "right", "top", "bottom"))
                if m >= SIDE_MIN and m > best_min:
                    best, best_min = colour, m
            exp = expected.get((row, col))
            exp_box = (exp["expected_box"] if exp and exp["expected_box"] != "NA" else "")
            rows_out.append({
                "row": row, "col": col,
                "observed_freq": exp["observed_freq"] if exp else "0",
                "levels": exp["levels"] if exp else "",
                "expected_box": exp_box, "detected_box": best,
                "side_min_score": round(best_min, 2),
                "match": exp_box == best,
                "cx": round(cx, 1), "cy": round(cy, 1),
            })

    out = HERE / "t11-cell-comparison.csv"
    with open(out, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows_out[0]))
        w.writeheader()
        w.writerows(rows_out)

    # Summary.
    n = len(rows_out)
    mism = [r for r in rows_out if not r["match"]]
    print(f"displayed cells: {n}; expected boxes: "
          f"{sum(bool(r['expected_box']) for r in rows_out)}; detected boxes: "
          f"{sum(bool(r['detected_box']) for r in rows_out)}; mismatches: {len(mism)}")
    for r in mism:
        print(f"  {r['row']:>6}/{r['col']:<6} freq={r['observed_freq']:>2} "
              f"levels={r['levels'] or '-':<32} expected={r['expected_box'] or '-':<7}"
              f" detected={r['detected_box'] or '-'}")

    if args.overlay:
        canvas = Image.open(args.image).convert("RGB")
        draw = ImageDraw.Draw(canvas)
        for r in rows_out:
            if not r["match"]:
                x, y = r["cx"], r["cy"]
                draw.ellipse([x - 14, y - 14, x + 14, y + 14], outline=(0, 160, 255), width=3)
        canvas.save(args.overlay)


if __name__ == "__main__":
    main()
