#!/usr/bin/env python3
"""Transcribe the R code blocks printed in the Dye et al. (2023) supplement.

Purpose
-------
The authors' R code exists only as numbered code listings inside the journal
supplement PDF (mmc1.pdf, sections 3-10). This tool converts the
``pdftotext -layout`` rendering of that PDF into plain R source, one file per
supplement section, so that the code can be run in batch inside Docker.

It performs only *typographic* restoration, never code changes:

1. keeps listing lines (``<line number><spaces><code>``) inside each section's
   line range and drops interleaved prose, page numbers, and blank lines;
2. strips the listing line numbers;
3. rejoins PDF line wraps (``↪`` continuation marks) to the previous line with a
   single space — the listings break only at whitespace, so the space restores
   the original character (verified by the label check in
   ``scripts/check-labels.R``);
4. replaces typographic quotes (U+201C, U+201D) with ASCII double quotes, which
   the PDF typesetting substituted for the R string delimiters.

Path substitutions (remote URL, author-local path, ``/path/to`` placeholders)
are *not* made here; they are made explicitly, and logged, in the transcribed
files under ``authors-code/`` (see ``log.md``, Modifications Required).

Usage
-----
    pdftotext -layout supplement-1.pdf supp.txt
    python3 tools/transcribe_supplement.py supp.txt authors-code-raw/

The supplement PDF is publisher content and is never copied into the attempt
directory; it is read from the corpus store by path.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

# Section name -> inclusive 1-based line range in the pdftotext -layout output
# of supplement-1.pdf (sha256 9b497fc2...7018b71), located by reading the text.
SECTIONS: dict[str, tuple[int, int]] = {
    "section-03-replicability": (987, 1032),
    "section-04-occurrence-plot": (1146, 1153),
    "section-05-bead-classification": (1168, 1428),
    "section-06-tempo-plot": (1441, 1450),
    "section-07-stable-branching": (1463, 1471),
    "section-08-monochrome-branching": (1487, 1500),
    "section-09-dghnt-reticulation": (1517, 1526),
    "section-10-1-row-1": (1568, 1583),
    "section-10-2-row-2": (1620, 1633),
    "section-10-3-row-3": (1668, 1683),
    "section-10-4-row-4": (1713, 1730),
    "section-10-5-row-5": (1767, 1777),
    "section-10-6-row-6": (1813, 1821),
    "section-10-7-row-7": (1856, 1863),
    "section-10-8-row-8": (1896, 1903),
    "section-10-9-row-9": (1935, 1945),
}

# A listing line: at most two leading spaces, a 1-2 digit line number, at least
# two spaces, then code. Prose lines are indented four or more spaces.
CODE_LINE = re.compile(r"^ {0,2}(\d{1,2}) {2,}(.*)$")
# A continuation line produced by the listing's automatic line breaking.
CONT_LINE = re.compile(r"^\s+↪\s+(.*)$")
# Subsection headings inside section 5 (kept as comments for traceability).
SUBHEAD = re.compile(r"^\s{2,}(5\.\d+ .+)$")


def normalise_quotes(text: str) -> str:
    """Replace typographic double quotes with ASCII double quotes.

    Args:
        text: one line of transcribed code.

    Returns:
        The line with U+201C and U+201D replaced by '"'.
    """
    return text.replace("”", '"').replace("“", '"')


def transcribe(lines: list[str], start: int, end: int) -> list[str]:
    """Extract and rejoin the listing lines within one section range.

    Args:
        lines: the full pdftotext output, one string per line.
        start: first line of the section (1-based, inclusive).
        end: last line of the section (1-based, inclusive).

    Returns:
        A list of R source lines, with subsection headings as comments.
    """
    out: list[str] = []
    for raw in lines[start - 1:end]:
        # pdftotext prefixes the first line of each page with a form feed;
        # strip it so a listing line at the top of a page is recognised.
        raw = raw.rstrip("\n").lstrip("\f")
        if m := CODE_LINE.match(raw):
            out.append(normalise_quotes(m.group(2).rstrip()))
        elif m := CONT_LINE.match(raw):
            if not out:
                raise ValueError(f"continuation with no preceding code: {raw!r}")
            out[-1] = out[-1] + " " + normalise_quotes(m.group(1).rstrip())
        elif m := SUBHEAD.match(raw):
            out.append(f"## --- Supplement {m.group(1).strip()} ---")
    return out


def main() -> None:
    """Write one raw transcription file per supplement section."""
    src = Path(sys.argv[1])
    dest = Path(sys.argv[2])
    dest.mkdir(parents=True, exist_ok=True)
    # Split on "\n" only: str.splitlines() would also split on the form feeds
    # pdftotext emits at page breaks, shifting the line ranges above.
    lines = src.read_text(encoding="utf-8").split("\n")
    for name, (start, end) in SECTIONS.items():
        code = transcribe(lines, start, end)
        (dest / f"{name}.R").write_text("\n".join(code) + "\n", encoding="utf-8")
        print(f"{name}: {len(code)} lines")


if __name__ == "__main__":
    main()
