#!/usr/bin/env python3
"""Compare the crema pilot's figures with the deposit's own v1.0.0 figures.

Ruling L5 (c) brings crema's five main figures (CREMA-T03 to T07) into the
registered archived-posterior leg. Under ruling L4 (a) a target stays
"unchanged" only if its expected outcome and value both equal the pilot's.
The pilot drew its figures from version 2.0.0's archived results; the gate
draws them from version 1.0.0's. This script tests whether the two give the
same figure content.

Both sets of PDFs are rasterised with pdftoppm at the same resolution and
compared pixel by pixel. A figure whose renders are pixel-identical has an
unchanged value. figures_main.R at v1.0.0 draws no random numbers, so any
difference comes from the archived inputs or the plotting functions, not from
the run.

Usage:
    python3 compare-figures.py <pilot-figure-dir> <deposit-figure-dir> <out.json>

    <pilot-figure-dir>: attempt-01 outputs/figures-from-precomputed
    <deposit-figure-dir>: figures_and_tables/ inside crema's v1.0.0 zip

Requires pdftoppm (poppler-utils) and Pillow.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageChops

DPI = 110
FIGURES = {1: "CREMA-T03", 2: "CREMA-T04", 3: "CREMA-T05", 4: "CREMA-T06", 5: "CREMA-T07"}


def sha256(path: Path) -> str:
    """Return the sha256 hex digest of a file.

    Args:
        path: the file to hash.

    Returns:
        The 64-character hex digest.
    """
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rasterise(pdf: Path, stem: Path) -> Image.Image:
    """Render the first page of a PDF to an RGB image.

    Args:
        pdf: the PDF to render.
        stem: output path without extension; pdftoppm adds ".png".

    Returns:
        The rendered page as an RGB image.
    """
    subprocess.run(["pdftoppm", "-png", "-r", str(DPI), "-singlefile", str(pdf), str(stem)],
                   check=True)
    return Image.open(stem.with_suffix(".png")).convert("RGB")


def compare(pilot_pdf: Path, deposit_pdf: Path, work: Path) -> dict:
    """Compare one figure's two renders.

    Args:
        pilot_pdf: the pilot's PDF of the figure.
        deposit_pdf: the deposit's PDF of the same figure.
        work: a scratch directory for the renders.

    Returns:
        A record of both files' hashes, the render size, the number and share
        of differing pixels, and the bounding box of the differences.
    """
    a = rasterise(pilot_pdf, work / f"pilot-{pilot_pdf.stem}")
    b = rasterise(deposit_pdf, work / f"deposit-{deposit_pdf.stem}")
    record: dict = {
        "pilot_pdf_sha256": sha256(pilot_pdf),
        "deposit_pdf_sha256": sha256(deposit_pdf),
        "render_dpi": DPI,
    }
    if a.size != b.size:
        record["result"] = f"render sizes differ: {a.size} against {b.size}"
        return record
    diff = ImageChops.difference(a, b)
    # A pixel differs if any channel differs.
    differing = sum(1 for px in diff.getdata() if px != (0, 0, 0))
    total = a.size[0] * a.size[1]
    record.update({
        "render_size": list(a.size),
        "differing_pixels": differing,
        "differing_share_pct": round(100 * differing / total, 3),
        "difference_bbox": list(diff.getbbox()) if diff.getbbox() else None,
        "result": "pixel-identical" if differing == 0 else "content differs",
    })
    return record


def main() -> None:
    """Compare figures 1 to 5 and write the results as JSON."""
    pilot_dir, deposit_dir, out = (Path(a) for a in sys.argv[1:4])
    results = {}
    with tempfile.TemporaryDirectory() as tmp:
        for n, target in FIGURES.items():
            name = f"figure{n}.pdf"
            results[target] = {"figure": name,
                               **compare(pilot_dir / name, deposit_dir / name, Path(tmp))}
            print(target, results[target]["result"],
                  results[target].get("differing_share_pct", ""))
    out.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
