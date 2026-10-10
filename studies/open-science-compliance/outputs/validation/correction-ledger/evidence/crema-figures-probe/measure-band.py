#!/usr/bin/env python3
"""Measure Fig. 2 panel a's 95% band at its right-hand end, in data units.

Crema's Fig. 2 panel a (simulation 1a) plots the posterior mean and 95% band
of a sigmoid whose plateau is the parameter mu_k. This script reads the
band's edges at the late end of the curve in four images: the probe's render
from v1.0.0's archive, the deposit's own figure2.pdf, the pilot's render from
v2.0.0's archive, and the version of record (VoR, page 6, vector graphics).

Calibration uses the panel's frame. figures_main.R plots with ylim = c(0, 1)
and R's default y-axis style ('r'), which pads the range by 4%, so the box
runs from -0.04 (bottom) to 1.04 (top). The probe's value can be checked
against posterior-plateau-output.log (0.5905 to 0.7339 at 1700 BP).

Usage:
    python3 measure-band.py <probe-figure2.pdf> <deposit-figure2.pdf> \
        <pilot-figure2.pdf> <vor.pdf> <out.json>

Requires pdftoppm (poppler-utils) and Pillow.
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image

LIGHTBLUE = (173, 216, 230)  # R's 'lightblue', the band's fill
VOR_PAGE = 6
# Panel a's region on the VoR page, as fractions of the page (x0, y0, x1, y1).
VOR_PANEL_A = (0.28, 0.32, 0.76, 0.47)


def render(pdf: Path, out_stem: Path, dpi: int, page: int = 1) -> Image.Image:
    """Rasterise one page of a PDF.

    Args:
        pdf: the PDF to render.
        out_stem: output path without extension; pdftoppm adds ".png".
        dpi: render resolution.
        page: the 1-based page number.

    Returns:
        The page as an RGB image.
    """
    subprocess.run(["pdftoppm", "-png", "-r", str(dpi), "-f", str(page), "-l", str(page),
                    "-singlefile", str(pdf), str(out_stem)], check=True)
    return Image.open(out_stem.with_suffix(".png")).convert("RGB")


def is_band(px: tuple[int, int, int]) -> bool:
    """Return True if a pixel has the band's fill colour."""
    return all(abs(a - b) < 30 for a, b in zip(px, LIGHTBLUE))


def frame(img: Image.Image, x0: int, x1: int, y0: int, y1: int) -> tuple[float, float]:
    """Locate the panel frame's top and bottom lines inside a region.

    A frame line is a row that is dark across at least 80% of the scanned
    width, which only the box's horizontal edges are. Each line is a few
    pixels thick, so its centre row is returned.

    Args:
        img: the image.
        x0, x1: the column range to scan, inside the box's horizontal extent.
        y0, y1: the row range to scan, containing exactly one panel.

    Returns:
        The centre rows of the top and bottom frame lines.
    """
    rows = [y for y in range(y0, y1)
            if sum(1 for x in range(x0, x1) if sum(img.getpixel((x, y))) < 150)
            > 0.8 * (x1 - x0)]
    top = [y for y in rows if y < rows[0] + 10]
    bottom = [y for y in rows if y > rows[-1] - 10]
    return sum(top) / len(top), sum(bottom) / len(bottom)


def measure(img: Image.Image, region: tuple[int, int, int, int]) -> dict:
    """Read the band's edges, in data units, near its right-hand end.

    Args:
        img: the image.
        region: (x0, y0, x1, y1) containing panel a only.

    Returns:
        The frame rows, the column read, and the band's lower and upper edges.
    """
    x0, y0, x1, y1 = region
    ft, fb = frame(img, x0 + (x1 - x0) // 10, x1 - (x1 - x0) // 10, y0, y1)
    cols = [x for x in range(x0, x1)
            if any(is_band(img.getpixel((x, y))) for y in range(int(ft), int(fb)))]
    col = max(cols) - 10  # just inside the band's right-hand end
    rows = [y for y in range(int(ft), int(fb)) if is_band(img.getpixel((col, y)))]

    def value(row: float) -> float:
        """Convert a pixel row to a data value (box spans -0.04 to 1.04)."""
        return 1.04 - (row - ft) / (fb - ft) * 1.08

    return {"frame_rows": [ft, fb], "column": col,
            "band": [round(value(max(rows)), 3), round(value(min(rows)), 3)]}


def main() -> None:
    """Measure panel a in all four images and write the results as JSON."""
    probe, deposit, pilot, vor, out = (Path(a) for a in sys.argv[1:6])
    results: dict = {}
    with tempfile.TemporaryDirectory() as tmp:
        for name, pdf in (("probe_v1.0.0", probe), ("deposit_pdf", deposit),
                          ("pilot_v2.0.0", pilot)):
            # Dots in the name would be read as a file extension by with_suffix().
            img = render(pdf, Path(tmp) / name.replace(".", "-"), dpi=220)
            w, h = img.size
            # Panel a is the top third of the three-panel figure.
            results[name] = measure(img, (int(0.08 * w), 0, int(0.99 * w), h // 3))
        img = render(vor, Path(tmp) / "vor", dpi=300, page=VOR_PAGE)
        w, h = img.size
        fx0, fy0, fx1, fy1 = VOR_PANEL_A
        results["vor_p6"] = measure(img, (int(fx0 * w), int(fy0 * h), int(fx1 * w),
                                          int(fy1 * h)))
    for name, r in results.items():
        print(f"{name}: band {r['band'][0]:.3f} to {r['band'][1]:.3f}")
    out.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
