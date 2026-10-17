#!/usr/bin/env python3
"""Measure the stacked bars of the published Fig. 3 (transcription aid).

Purpose
-------
Herskind and Riede (2024), Journal of Archaeological Science 165, 105969,
Fig. 3 is a raster image (six stacked bar panels). Its 4-decimal Pointwise
Mutual Information (PMI) labels were transcribed by eye into
``fig3-published.csv``; this script measures, from pixel colours, each bar's
total length and the length of each chronology segment, so that the published
bar totals and stacked compositions are transcribed mechanically rather than
by eye. It reads only the published figure (extracted from the version of
record with ``pdfimages -png``, page 5, kept outside the repository because it
is publisher content) and never touches reproduction outputs.

Method
------
1. Each panel occupies one sixth of the 1836 x 2294 px image (2 columns x 3
   rows).
2. Pixels are classified by nearest palette colour (the authors' fill values
   #FAD02E Ertebolle, #D98888 Kongemose, #E8BB8B Kongemose/Ertebolle,
   #B4A1C1 Maglemose), within a tolerance.
3. Bars are runs of rows holding palette pixels; each bar is scanned on a row
   two pixels inside its top edge, where the black PMI label text does not
   reach.
4. The axis scale comes from the white vertical gridlines in the gap between
   the first two bars (major and minor lines alternate, so the spacing is half
   a major interval; the major interval is read from the axis labels).
5. Segment lengths are divided by the unit length and rounded; the residual is
   reported so that a reader can judge the rounding.

Usage
-----
    python3 -I measure_fig3_bars.py <fig3.png> <out.csv>
    python3 -I measure_fig3_bars.py --fig2 <fig2.png> <out.csv>

The ``--fig2`` mode measures the bar panel of Fig. 2 (page 3; the left
560 x 905 px of the extracted image, axis major interval 25) the same way.
At 3.2 px per object its counts are approximate (about +/-1 per segment),
and a bar narrower than the 15-pixel row threshold is missed.

Returns a CSV with one row per bar: panel, rank (top to bottom), total,
per-chronology counts, and the largest rounding residual.
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

from PIL import Image

# Authors' fill colours (S2.R scale_fill_manual) and their chronology levels.
PALETTE = {
    "Ertebolle": (250, 208, 46),
    "Kongemose": (217, 136, 136),
    "Kongemose/Ertebolle": (232, 187, 139),
    "Maglemose": (180, 161, 193),
}
TOLERANCE = 24  # maximum per-channel difference for a palette match
# Major axis interval per panel, read from the printed axis labels.
MAJOR = {"a": 10, "b": 2, "c": 5, "d": 1, "e": 1, "f": 1, "fig2": 25}


def classify(pixel: tuple[int, int, int]) -> str | None:
    """Return the chronology whose palette colour matches the pixel, if any.

    Args:
        pixel: An RGB triple.

    Returns:
        The chronology name, or None for background, gridline, or text.
    """
    for name, ref in PALETTE.items():
        if all(abs(a - b) <= TOLERANCE for a, b in zip(pixel, ref)):
            return name
    return None


def measure_panel(img: Image.Image, box: tuple[int, int, int, int], label: str) -> list[dict]:
    """Measure every bar in one panel.

    Args:
        img: The full figure image (RGB).
        box: (x0, y0, x1, y1) of the panel.
        label: Panel letter (a-f).

    Returns:
        One dict per bar, top to bottom.
    """
    px = img.load()
    x0, y0, x1, y1 = box
    # Rows holding a bar: more than 15 palette pixels left of the legend
    # (panel a's legend keys share the palette and sit at x >= x0 + 600).
    bar_rows = [y for y in range(y0, y1)
                if sum(classify(px[x, y]) is not None for x in range(x0, x0 + 600)) > 15]
    bars: list[list[int]] = []
    for y in bar_rows:
        if bars and y - bars[-1][1] <= 1:
            bars[-1][1] = y
        else:
            bars.append([y, y])
    bars = [b for b in bars if b[1] - b[0] >= 10]
    # Zero of the axis: the most common first palette pixel on the bars'
    # scan rows (every bar starts at zero).
    scan_rows = [b[0] + 2 for b in bars]
    starts = []
    for y in scan_rows:
        for x in range(x0 + 100, x1):
            if classify(px[x, y]) is not None:
                starts.append(x)
                break
    zero = max(set(starts), key=starts.count)
    # Gridlines in the gap between the first two bars.
    gap_y = (bars[0][1] + bars[1][0]) // 2
    white = [x for x in range(zero, x1) if all(v >= 250 for v in px[x, gap_y])]
    lines: list[list[int]] = []
    for x in white:
        if lines and x - lines[-1][-1] <= 1:
            lines[-1].append(x)
        else:
            lines.append([x])
    centres = [sum(g) / len(g) for g in lines]
    spacings = [b - a for a, b in zip(centres, centres[1:])]
    half_major = sorted(spacings)[len(spacings) // 2]
    unit = 2 * half_major / MAJOR[label]
    out = []
    for rank, (top, _bottom) in enumerate(bars, 1):
        y = top + 2
        runs: list[list] = []
        for x in range(zero, x1):
            name = classify(px[x, y])
            if name is None:
                # A gap of more than 3 px ends the bar (legend keys follow).
                if runs and x - runs[-1][2] > 3:
                    break
                continue
            if runs and runs[-1][0] == name and x - runs[-1][2] <= 3:
                runs[-1][2] = x
            else:
                runs.append([name, x, x])
        counts = {name: 0 for name in PALETTE}
        residual = 0.0
        for name, start, end in runs:
            length = (end - start + 1) / unit
            counts[name] += round(length)
            residual = max(residual, abs(length - round(length)))
        end_x = runs[-1][2] + 1 if runs else zero
        total_units = (end_x - zero) / unit
        out.append({"panel": label, "rank": rank, "total": round(total_units),
                    "total_residual": round(abs(total_units - round(total_units)), 3),
                    **{k: v for k, v in counts.items()},
                    "max_segment_residual": round(residual, 3),
                    "unit_px": round(unit, 2), "zero_px": zero})
    return out


def main() -> int:
    """Measure all six Fig. 3 panels (or the Fig. 2 bar panel) and write the CSV."""
    args = sys.argv[1:]
    fig2 = args[0] == "--fig2"
    if fig2:
        args = args[1:]
    src, dest = Path(args[0]), Path(args[1])
    img = Image.open(src).convert("RGB")
    width, height = img.size
    rows = []
    if fig2:
        rows += measure_panel(img, (0, 0, 560, height), "fig2")
    else:
        letters = iter("abcdef")
        for r in range(3):
            for c in range(2):
                box = (c * width // 2, r * height // 3, (c + 1) * width // 2,
                       (r + 1) * height // 3)
                rows += measure_panel(img, box, next(letters))
    with dest.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"{len(rows)} bars measured -> {dest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
