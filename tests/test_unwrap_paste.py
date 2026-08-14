#!/usr/bin/env python3
"""Self-check for the OSF paste-file unwrap script (plan C5; audit M14-M16).

Regression-anchors each fixed defect and proves idempotence on the lodged
amendment-1 artefact, so the script is verified before any future paste
artefact (amendment 2 included) is generated with it.

Run: ``venv/bin/python -m pytest tests/test_unwrap_paste.py -q``
"""

from __future__ import annotations

import importlib.util
import importlib.machinery
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = (REPO_ROOT / "studies" / "open-science-compliance" / "prereg"
          / "unwrap-paste-file.py")
AMENDMENT_1 = (REPO_ROOT / "studies" / "open-science-compliance" / "prereg"
               / "osf-amendment-1.txt")

_spec = importlib.util.spec_from_loader(
    "unwrap_paste_file",
    importlib.machinery.SourceFileLoader("unwrap_paste_file", str(SCRIPT)))
unwrapper = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(unwrapper)


class UnwrapTests(unittest.TestCase):
    """One regression per audit finding, plus invariants."""

    def test_basic_paragraph_joins(self) -> None:
        text = "First line\nwraps onto a second\nand a third.\n\nNext block.\n"
        self.assertEqual(unwrapper.unwrap(text),
                         "First line wraps onto a second and a third.\n\nNext block.\n")

    def test_m14_indented_bullet_keeps_own_line(self) -> None:
        """M14: an indented list item must not be absorbed into prose."""
        text = "Intro line.\n  - indented item one\n  - indented item two\n"
        result = unwrapper.unwrap(text)
        self.assertIn("\n  - indented item one\n", result)
        self.assertIn("\n  - indented item two", result)

    def test_m15_year_line_is_prose_not_list(self) -> None:
        """M15: '2026. ' opening a wrapped line is a sentence, not item 2026."""
        text = "The study began in\n2026. It continued after\nthat year.\n"
        self.assertEqual(unwrapper.unwrap(text),
                         "The study began in 2026. It continued after that year.\n")

    def test_numbered_list_items_still_protected(self) -> None:
        """M15's fix must not unprotect real numbered items (incl. 3-digit)."""
        text = "1. First item\n2. Second item\n10. Tenth item\n101. Deep item\n"
        self.assertEqual(unwrapper.unwrap(text), text.rstrip("\n") + "\n"
                         if text.endswith("\n") else text)

    def test_m16_table_row_spacing_preserved(self) -> None:
        """M16: deliberate spacing inside protected lines survives."""
        text = "| Col A  | Col B  |\n| 1      | 2      |\n"
        result = unwrapper.unwrap(text)
        self.assertIn("| Col A  | Col B  |", result)
        self.assertIn("| 1      | 2      |", result)

    def test_m16_indented_bullet_indent_preserved(self) -> None:
        text = "  - keep  my  spacing\n"
        self.assertIn("  - keep  my  spacing", unwrapper.unwrap(text))

    def test_m16_prose_double_spaces_still_collapse(self) -> None:
        text = "Joined line \nwith trailing space.\n"
        self.assertEqual(unwrapper.unwrap(text),
                         "Joined line with trailing space.\n")

    def test_word_count_invariant(self) -> None:
        """The docstring's own verification rule, mechanised."""
        text = ("Wrapped prose line one\ncontinues here.\n\n"
                "- bullet item\n1. numbered\n\n2026. Year sentence\njoined.\n")
        self.assertEqual(len(unwrapper.unwrap(text).split()), len(text.split()))

    def test_idempotent_on_lodged_amendment_1(self) -> None:
        """Running the fixed script over the already-unwrapped, lodged
        amendment-1 artefact must change nothing (regression anchor)."""
        if not AMENDMENT_1.is_file():
            self.skipTest(f"lodged artefact not present: {AMENDMENT_1}")
        text = AMENDMENT_1.read_text(encoding="utf-8")
        self.assertEqual(unwrapper.unwrap(text), text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
