#!/usr/bin/env python3
"""Unwrap hard line-breaks in a plain-prose Open Science Framework (OSF) paste file.

OSF form text boxes render pasted line-breaks literally, so hard-wrapped
source lines break mid-sentence. This script joins wrapped lines within each
blank-line-delimited block into a single flowing line, with two exceptions
that always keep their own line:

- list items (``- `` bullets and ``N. `` numbered lines, which also covers
  the plain-prose section headings), and
- table rows (lines starting with ``|``) — markdown tables do not survive
  plain-text paste at all, so the real rule is to keep tables out of
  paste-field content entirely (see README); leaving rows unjoined is only
  damage limitation, learnt from the 2026-07-20 lodgement where the §10
  power table pasted as run-together pipe text.

Verify after running: word count must be unchanged (``wc -w``), and bullet /
numbered-line counts must match the wrapped original.

Usage: python3 unwrap-paste-file.py <file>   (rewrites the file in place)
"""

import re
import sys
from pathlib import Path

KEEP_OWN_LINE = re.compile(r"^(- |[0-9]+\. |\|)")


def unwrap(text: str) -> str:
    """Return text with intra-paragraph line-breaks replaced by spaces.

    Args:
        text: Full file content, blank-line-delimited blocks.

    Returns:
        The unwrapped text; blank lines and protected lines (list items,
        table rows) are preserved as line boundaries.
    """
    out_lines: list[str] = []
    current: str | None = None
    for raw in text.split("\n"):
        line = raw.rstrip()
        if not line.strip():
            if current is not None:
                out_lines.append(current)
                current = None
            out_lines.append("")
        elif current is None or KEEP_OWN_LINE.match(line):
            if current is not None:
                out_lines.append(current)
            current = line
        elif current.startswith("|"):
            # Never append prose onto a table row; start a fresh line.
            # (List items, by contrast, do absorb their wrapped
            # continuation lines.)
            out_lines.append(current)
            current = line
        else:
            current += " " + line.strip()
    if current is not None:
        out_lines.append(current)
    # Collapse any accidental double spaces introduced by the joins.
    return "\n".join(re.sub(r"  +", " ", line) for line in out_lines)


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    path = Path(sys.argv[1])
    path.write_text(unwrap(path.read_text(encoding="utf-8")), encoding="utf-8")


if __name__ == "__main__":
    main()
