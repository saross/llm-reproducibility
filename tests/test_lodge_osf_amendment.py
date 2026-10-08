#!/usr/bin/env python3
"""Offline checks for the OSF lodgement script (``lodge-osf-amendment.py``).

Only the pure functions are tested: composing the new Summary and the
registry's entity transform. Nothing here contacts OSF.

Run: ``venv/bin/python -m pytest tests/test_lodge_osf_amendment.py -q``
"""

from __future__ import annotations

import importlib.machinery
import importlib.util
import unittest
from pathlib import Path

PREREG = Path(__file__).resolve().parent.parent / "studies" / "open-science-compliance" / "prereg"

_loader = importlib.machinery.SourceFileLoader(
    "lodge_osf_amendment", str(PREREG / "lodge-osf-amendment.py"))
_spec = importlib.util.spec_from_loader(_loader.name, _loader)
lodger = importlib.util.module_from_spec(_spec)
_loader.exec_module(lodger)

PREVIOUS = ("Body.\n\n" + "=" * 40 + "\n\nAMENDMENT 1 (2026-08-03)\n\nA1.\n\n"
            + "=" * 40 + "\n\nAMENDMENT 2 (2026-08-17)\n\nA2 post &gt; pre.")
ARTEFACT = "Registration: ... Amendment 3 lodged 2026-10-08; artefact set ...\n\nText.\n"


class ComposeTests(unittest.TestCase):
    """The new Summary keeps the old one and appends under the banner."""

    def test_appends_in_the_lodged_layout(self) -> None:
        new = lodger.compose_summary(PREVIOUS, ARTEFACT, 3, "2026-10-08")
        self.assertTrue(new.startswith(PREVIOUS))
        self.assertEqual(new[len(PREVIOUS):], "\n\n" + "=" * 40 + "\n\nAMENDMENT 3 (2026-10-08)"
                         "\n\n" + ARTEFACT.rstrip("\n"))

    def test_refuses_a_second_lodgement(self) -> None:
        with self.assertRaises(ValueError):
            lodger.compose_summary(PREVIOUS, ARTEFACT.replace("3", "2"), 2, "2026-10-08")

    def test_refuses_a_missing_predecessor(self) -> None:
        with self.assertRaises(ValueError):
            lodger.compose_summary("Body.", ARTEFACT, 3, "2026-10-08")

    def test_refuses_an_artefact_dated_otherwise(self) -> None:
        with self.assertRaises(ValueError):
            lodger.compose_summary(PREVIOUS, ARTEFACT, 3, "2026-10-09")

    def test_entity_form_leaves_stored_entities_alone(self) -> None:
        # The previous Summary already holds entities; only new literals change.
        self.assertEqual(lodger.entity_form("a &gt; b < c"), "a &gt; b &lt; c")

    def test_current_artefact_needs_no_transform(self) -> None:
        artefact = (PREREG / "osf-amendment-3.txt").read_text(encoding="utf-8")
        self.assertEqual(lodger.entity_form(artefact), artefact)


if __name__ == "__main__":
    unittest.main()
