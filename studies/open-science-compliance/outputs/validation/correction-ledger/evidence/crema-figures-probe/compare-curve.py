#!/usr/bin/env python3
"""Compare Fig. 2's 95% bands column by column: probe render against deposit PDF.

For ruling L18. Both PDFs come from the same figures_main.R layout, so their
pixel columns align. For panels a and b, each column's band edges are read
and converted to data units with the panel frame (ylim c(0, 1), R's default
4% padding, so the box spans -0.04 to 1.04). The result is the largest
difference in each edge across the whole curve, and where it falls. Panel c
is compared pixel by pixel.

Usage:
    python3 compare-curve.py <probe-figure2.pdf> <deposit-figure2.pdf> <out.json>

Requires pdftoppm (poppler-utils) and Pillow.
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageChops

DPI = 220
LIGHTBLUE = (173, 216, 230)


def render(pdf: Path, stem: Path) -> Image.Image:
    """Rasterise a one-page PDF at DPI and return it as RGB."""
    subprocess.run(["pdftoppm", "-png", "-r", str(DPI), "-singlefile", str(pdf), str(stem)],
                   check=True)
    return Image.open(stem.with_suffix(".png")).convert("RGB")


def frame(img: Image.Image, y0: int, y1: int) -> tuple[float, float]:
    """Return the centre rows of a panel frame's top and bottom lines."""
    w = img.size[0]
    x0, x1 = int(0.2 * w), int(0.8 * w)
    rows = [y for y in range(y0, y1)
            if sum(1 for x in range(x0, x1) if sum(img.getpixel((x, y))) < 150)
            > 0.8 * (x1 - x0)]
    top = [y for y in rows if y < rows[0] + 10]
    bottom = [y for y in rows if y > rows[-1] - 10]
    return sum(top) / len(top), sum(bottom) / len(bottom)


def band_edges(img: Image.Image, col: int, ft: float, fb: float) -> tuple[int, int] | None:
    """Return the band's top and bottom rows in one column, inside the frame."""
    rows = [y for y in range(int(ft) + 3, int(fb) - 2)
            if all(abs(a - b) < 30 for a, b in zip(img.getpixel((col, y)), LIGHTBLUE))]
    return (min(rows), max(rows)) if rows else None


def frame_columns(img: Image.Image, y0: int, y1: int) -> tuple[float, float]:
    """Return the centre columns of a panel frame's left and right lines."""
    h0, h1 = y0 + (y1 - y0) // 4, y1 - (y1 - y0) // 4
    cols = [x for x in range(img.size[0])
            if sum(1 for y in range(h0, h1) if sum(img.getpixel((x, y))) < 150)
            > 0.9 * (h1 - h0)]
    left = [x for x in cols if x < cols[0] + 10]
    right = [x for x in cols if x > cols[-1] - 10]
    return sum(left) / len(left), sum(right) / len(right)


def timing_shift(p: Image.Image, d: Image.Image, y0: int, y1: int,
                 time_range: tuple[int, int]) -> dict:
    """Measure how far the probe's band edges sit from the deposit's in time.

    For values 0.1 to 0.5 on the rising curve, find the first column where
    each render's band edge reaches the value, and convert the column gap to
    years. The x axis spans time_range with R's 4% padding.

    Returns:
        For each edge and value, the probe's crossing minus the deposit's, in
        years (positive: the probe's curve rises later, i.e. nearer the
        present on a BP axis read left to right from older to younger).
    """
    ft, fb = frame(p, y0, y1)
    fl, fr = frame_columns(p, y0, y1)
    t0, t1 = time_range
    pad = 0.04 * (t0 - t1)
    years_per_col = ((t0 + pad) - (t1 - pad)) / (fr - fl)

    def row_of(value: float) -> float:
        return ft + (1.04 - value) / 1.08 * (fb - ft)

    def first_cross(img: Image.Image, edge: int, value: float) -> int | None:
        target = row_of(value)
        for col in range(int(fl) + 2, int(fr) - 1):
            e = band_edges(img, col, ft, fb)
            # Rows grow downwards, so reaching a value means the row is at or above it.
            if e and e[edge] <= target:
                return col
        return None

    out: dict = {}
    for edge_i, edge in ((1, "lower"), (0, "upper")):
        for value in (0.1, 0.2, 0.3, 0.4, 0.5):
            cp, cd = first_cross(p, edge_i, value), first_cross(d, edge_i, value)
            if cp is not None and cd is not None:
                out[f"{edge}_{value}"] = round((cp - cd) * years_per_col)
    return out


def main() -> None:
    """Compare panels a and b column by column, and panel c pixel by pixel."""
    probe_pdf, deposit_pdf, out = (Path(a) for a in sys.argv[1:4])
    with tempfile.TemporaryDirectory() as tmp:
        p = render(probe_pdf, Path(tmp) / "probe")
        d = render(deposit_pdf, Path(tmp) / "deposit")
    assert p.size == d.size, (p.size, d.size)
    w, h = p.size
    results: dict = {"dpi": DPI}
    for panel, (y0, y1) in (("a", (0, h // 3)), ("b", (h // 3, 2 * h // 3))):
        ft, fb = frame(p, y0, y1)
        assert (ft, fb) == frame(d, y0, y1), "frames differ between renders"

        def value(row: float, ft: float = ft, fb: float = fb) -> float:
            """Convert a pixel row in this panel to a data value."""
            return 1.04 - (row - ft) / (fb - ft) * 1.08

        worst = {"lower": (0.0, None), "upper": (0.0, None)}
        compared = 0
        for col in range(w):
            ep, ed = band_edges(p, col, ft, fb), band_edges(d, col, ft, fb)
            if not ep or not ed:
                continue
            compared += 1
            for i, edge in ((1, "lower"), (0, "upper")):
                diff = value(ep[i]) - value(ed[i])
                if abs(diff) > abs(worst[edge][0]):
                    worst[edge] = (round(diff, 3), col)
        results[f"panel_{panel}"] = {
            "columns_compared": compared,
            "value_per_pixel_row": round(1.08 / (fb - ft), 4),
            "largest_difference_probe_minus_deposit": {
                k: {"value": v[0], "column": v[1]} for k, v in worst.items()},
        }
    results["panel_a"]["timing_shift_years"] = timing_shift(p, d, 0, h // 3,
                                                            time_range=(4000, 1700))
    pc = ImageChops.difference(p.crop((0, 2 * h // 3, w, h)), d.crop((0, 2 * h // 3, w, h)))
    results["panel_c"] = {"pixel_identical": pc.getbbox() is None}
    print(json.dumps(results, indent=2))
    out.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
