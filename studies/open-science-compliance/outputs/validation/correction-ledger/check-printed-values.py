#!/usr/bin/env python3
"""Check every printed value in the correction-ledger draft against its source PDF.

Purpose
-------
Amendment 3 §9 requires each ledger value to cite the paper or the selected
deposit. This script re-checks the citations mechanically: for every target
element whose ``source`` is a corpus-store PDF (``vor``, ``supplement-1``,
``preprint``), it extracts the text of the cited PDF page with Poppler's
``pdftotext`` and confirms that the printed value (or the element's
``text_layer`` string, where the PDF's text layer renders the value
differently, e.g. a superscript exponent) occurs on that page.

Values drawn inside a raster figure have no text layer; such elements carry a
``raster`` note saying how they were read, and are counted but not checked.
Elements read from a deposit file (``source`` beginning ``deposit:``) are
counted but not checked here, because the deposits are not held in the
corpus store yet (executed-code audit Q10).

The check is a guard against transcription and page errors, not a proof that
a value means what the ledger says it means. A value that occurs elsewhere on
the page passes too, so short values (``1``, ``0``) are weak evidence.

Usage
-----
    python3 check-printed-values.py [--ledger correction-ledger.json]
                                    [--corpus-root ~/corpora/llm-reproducibility]

``CORPUS_ROOT`` in the environment overrides the default corpus root, as in
``scripts/fetch-corpus.py``. Exit status 0 when every checkable element is
found, 1 otherwise.

Requires: Python 3.10+, Poppler's ``pdftotext`` on PATH.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from functools import cache
from pathlib import Path

HERE = Path(__file__).resolve().parent
PDF_SOURCES = {"vor": "vor.pdf", "supplement-1": "supplement-1.pdf",
               "preprint": "preprint.pdf"}


@cache
def page_text(pdf: Path, page: int, layout: bool) -> str:
    """Return one page's text with runs of whitespace collapsed.

    Args:
        pdf: path to the PDF.
        page: 1-based physical page index.
        layout: True for ``pdftotext -layout`` (keeps table columns), False for
            reading order (keeps sentences that wrap across lines together).

    Returns:
        The page text, whitespace-normalised.
    """
    args = ["pdftotext", "-f", str(page), "-l", str(page)]
    if layout:
        args.append("-layout")
    out = subprocess.run(args + [str(pdf), "-"], capture_output=True, text=True,
                         check=True).stdout
    return re.sub(r"\s+", " ", out)


def found(needle: str, pdf: Path, page: int) -> bool:
    """True if ``needle`` occurs on the page in either text extraction mode."""
    n = re.sub(r"\s+", " ", needle).strip()
    return any(n in page_text(pdf, page, layout) for layout in (True, False))


def main() -> int:
    """Run the check and print one line per failure plus a summary."""
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--ledger", type=Path, default=HERE / "correction-ledger.json")
    ap.add_argument("--corpus-root", type=Path,
                    default=Path(os.environ.get("CORPUS_ROOT",
                                                "~/corpora/llm-reproducibility")))
    a = ap.parse_args()
    ledger = json.loads(a.ledger.read_text(encoding="utf-8"))
    root = a.corpus_root.expanduser()

    checked = passed = skipped = raster = 0
    for paper in ledger["papers"]:
        for target in paper["targets"]:
            for el in target.get("elements", []):
                src = el.get("source", "")
                if src not in PDF_SOURCES:
                    skipped += 1
                    continue
                if el.get("raster"):
                    # A value drawn inside a figure has no text layer; the ledger
                    # records how it was read instead (``raster``).
                    raster += 1
                    continue
                pdf = root / paper["slug"] / PDF_SOURCES[src]
                needle = el.get("text_layer") or el["printed"]
                checked += 1
                if found(needle, pdf, el["page_pdf"]):
                    passed += 1
                else:
                    print(f"NOT FOUND  {target['id']}  {el['label']!r}: {needle!r} on "
                          f"{src} p. {el['page_pdf']}")
    print(f"{passed}/{checked} printed elements found on their cited page; "
          f"{raster} raster figure labels read visually (see each element's 'raster'); "
          f"{skipped} deposit elements not checked here")
    return 0 if passed == checked else 1


if __name__ == "__main__":
    sys.exit(main())
