#!/usr/bin/env python3
"""Compare marwick's Fig. 2 as redrawn by the probe with the authors' image.

For ruling L17. Both images come from the supplement's fig-smooth-plots-paper
chunk (ggsave at 1,000 dots per inch, 5,000 by 3,000 pixels), so their
panels align. The figure is a 3 by 2 grid with five panels; each draws a
purple trend line (the fitted conditional effect of year) over the
articles' points.

The script reports, for each panel:

- the trend line's top and bottom edge in every pixel column, in both
  images, and the largest difference between them;
- how many pixels differ at all, and how many by 60 or more grey levels.

Over the whole figure it then counts the strong differences (60 or more
grey levels) that lie more than four pixels from any text, frame, tick,
or trend-line pixel in either image. Zero means the data points are
identical and every strong difference is in text rendering or a line edge.

The Pseudo R-squared labels are read by eye, since they are text.

Usage:
    python3 compare-trend.py <probe.png> <deposited.png> <out.json>

Requires Pillow.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from PIL import Image, ImageChops, ImageFilter

PURPLE = (117, 112, 179)
TOLERANCE = 12
STRONG = 60
PANELS = {
    "recency": (0, 0), "diversity": (0, 1), "title_length": (0, 2),
    "authors": (1, 0), "pages": (1, 1),
}


def line_edges(img: Image.Image, col: int, y0: int, y1: int) -> tuple[int, int] | None:
    """Return the top and bottom rows of the purple line in one column, if any."""
    rows = [y for y in range(y0, y1)
            if all(abs(a - b) <= TOLERANCE for a, b in zip(img.getpixel((col, y)), PURPLE))]
    return (min(rows), max(rows)) if rows else None


def compare_panel(p: Image.Image, d: Image.Image, box: tuple[int, int, int, int]) -> dict:
    """Compare one panel's trend line column by column, and count differing pixels."""
    x0, y0, x1, y1 = box
    worst = {"top": 0, "bottom": 0}
    compared = differing_cols = 0
    thickness = []
    for col in range(x0, x1):
        ep, ed = line_edges(p, col, y0, y1), line_edges(d, col, y0, y1)
        if not ep or not ed:
            continue
        compared += 1
        thickness.append(ed[1] - ed[0] + 1)
        dt, db = ep[0] - ed[0], ep[1] - ed[1]
        if dt or db:
            differing_cols += 1
        worst["top"] = max(worst["top"], abs(dt))
        worst["bottom"] = max(worst["bottom"], abs(db))
    diff = ImageChops.difference(p.crop(box), d.crop(box)).convert("L")
    hist = diff.histogram()
    return {
        "line_columns_compared": compared,
        "line_columns_with_any_edge_difference": differing_cols,
        "largest_edge_difference_px": worst,
        "median_line_thickness_px": sorted(thickness)[len(thickness) // 2] if thickness else None,
        "pixels_differing": sum(hist[1:]),
        "pixels_differing_by_60_or_more": sum(hist[STRONG:]),
        "panel_pixels": (x1 - x0) * (y1 - y0),
    }


def marks(img: Image.Image) -> Image.Image:
    """Mask the trend line and neutral grey or black marks (text, frames, ticks).

    The mask is widened by four pixels on each side (a 9 by 9 maximum filter),
    so that anti-aliased edges fall inside it.
    """
    w, h = img.size
    src = img.load()
    out = Image.new("L", (w, h), 0)
    dst = out.load()
    for y in range(h):
        for x in range(w):
            r, g, b = src[x, y]
            purple = abs(r - PURPLE[0]) + abs(g - PURPLE[1]) + abs(b - PURPLE[2]) < 120
            neutral = max(r, g, b) - min(r, g, b) < 25 and r < 200
            if purple or neutral:
                dst[x, y] = 255
    return out.filter(ImageFilter.MaxFilter(9))


def strong_differences_away_from_marks(p: Image.Image, d: Image.Image) -> dict:
    """Count strong differences, and those not near any mark in either image."""
    strong = ImageChops.difference(p, d).convert("L").point(
        lambda v: 255 if v >= STRONG else 0)
    rest = ImageChops.subtract(strong, ImageChops.lighter(marks(p), marks(d)))
    return {
        "strong_differences": sum(1 for v in strong.getdata() if v),
        "strong_differences_not_near_text_frame_or_line": sum(
            1 for v in rest.getdata() if v),
    }


def main() -> None:
    """Compare the five panels and write the results as JSON."""
    probe_png, deposited_png, out = (Path(a) for a in sys.argv[1:4])
    p = Image.open(probe_png).convert("RGB")
    d = Image.open(deposited_png).convert("RGB")
    assert p.size == d.size, (p.size, d.size)
    w, h = p.size
    results: dict = {"size_px": [w, h], "panels": {}}
    for name, (r, c) in PANELS.items():
        box = (c * w // 3, r * h // 2, (c + 1) * w // 3, (r + 1) * h // 2)
        results["panels"][name] = compare_panel(p, d, box)
    empty = (2 * w // 3, h // 2, w, h)
    results["empty_sixth_cell_identical"] = (
        ImageChops.difference(p.crop(empty), d.crop(empty)).getbbox() is None)
    results["whole_figure"] = strong_differences_away_from_marks(p, d)
    print(json.dumps(results, indent=2))
    out.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
