#!/usr/bin/env python3
"""Self-check for the OSF paste-artefact builder (``make-paste-artefact.py``).

Covers each conversion the builder makes, and checks the current amendment-3
draft end to end: the artefact must carry no markdown, section signs,
arrows, decision markers, or tables, and unwrapping it must leave the word
count unchanged.

Run: ``venv/bin/python -m pytest tests/test_make_paste_artefact.py -q``
"""

from __future__ import annotations

import importlib.machinery
import importlib.util
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PREREG = REPO_ROOT / "studies" / "open-science-compliance" / "prereg"


def load(name: str, filename: str):
    """Import a hyphen-named script in the prereg directory as a module."""
    spec = importlib.util.spec_from_loader(
        name, importlib.machinery.SourceFileLoader(name, str(PREREG / filename)))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


builder = load("make_paste_artefact", "make-paste-artefact.py")
unwrapper = load("unwrap_paste_file", "unwrap-paste-file.py")


class ConversionTests(unittest.TestCase):
    """One test per conversion rule."""

    def test_markers_markdown_and_signs(self) -> None:
        text = ("### 4. Rules (v2.1 → v2.2) [D-1]\n\n"
                "See §5(c), §§2–3, and **bold *nested* text** with `code`. "
                "[D-3, ruled] Next.\n")
        self.assertEqual(builder.to_plain(text),
                         "4. Rules (v2.1 to v2.2)\n\n"
                         "See section 5(c), sections 2–3, and bold nested text with code. "
                         "Next.\n")

    def test_amendment_2_arrow_form(self) -> None:
        self.assertEqual(builder.to_plain("the unscoreable → 0 default\n"),
                         "the unscoreable-scores-0 default\n")

    def test_autolink_becomes_bare(self) -> None:
        self.assertEqual(builder.to_plain("at <https://example.org/x>, here\n"),
                         "at https://example.org/x, here\n")

    def test_table_is_refused(self) -> None:
        draft = (f"{builder.START_HEADING}\n\n| a | b |\n|---|---|\n\n"
                 f"{builder.END_HEADING}\n")
        with self.assertRaises(ValueError):
            builder.lodged_portion(draft)

    def test_unknown_arrow_is_refused(self) -> None:
        with self.assertRaises(ValueError):
            builder.to_plain("a→b\n")


class Amendment3Tests(unittest.TestCase):
    """The current amendment-3 draft converts cleanly."""

    def setUp(self) -> None:
        draft = (PREREG / "amendment-3-draft.md").read_text(encoding="utf-8")
        self.plain = builder.to_plain(builder.lodged_portion(draft))

    def test_no_residue(self) -> None:
        for residue in ("§", "→", "[D-", "**", "`", "###"):
            self.assertNotIn(residue, self.plain, residue)

    def test_unwrap_keeps_every_word(self) -> None:
        self.assertEqual(len(unwrapper.unwrap(self.plain).split()), len(self.plain.split()))


if __name__ == "__main__":
    unittest.main()
