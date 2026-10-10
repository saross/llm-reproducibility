#!/usr/bin/env python3
"""Offline checks for the OSF lodgement script (``lodge-osf-amendment.py``).

Tests the pure functions (composing the new Summary, the registry's entity
transform) and the ``lodge`` sequence against a fake OSF: a failed content
check must never reach submit or approve, and a failure once submission has
been attempted must report the revision without calling it private. Nothing
here contacts OSF.

Run: ``venv/bin/python -m pytest tests/test_lodge_osf_amendment.py -q``
"""

from __future__ import annotations

import importlib.machinery
import argparse
import importlib.util
import io
import os
import tempfile
import unittest
from unittest import mock
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


class FakeOsf:
    """A stand-in for ``request`` that plays one registration's API.

    Args:
        previous: The latest approved Summary.
        mangle: Optional function giving the stored Summary from the sent one;
            by default OSF's entity transform.
        keys: The ``updated_response_keys`` the PATCH reports.
        fail: Optional ``(method, path)`` predicate; a matching call raises.
        public: Optional Summary the public copy shows after approval.
        malformed: Optional ``(method, path)`` predicate; a matching call
            returns an empty body instead of OSF's structure.
    """

    RID = "new-revision"

    def __init__(self, previous: str, mangle=None, keys=("summary",), fail=None,
                 public: str | None = None, malformed=None) -> None:
        self.previous, self.mangle, self.keys = previous, mangle, list(keys)
        self.fail, self.public, self.malformed = fail, public, malformed
        self.calls: list[tuple[str, str]] = []
        self.sent: str | None = None
        self.approved = False

    def __call__(self, method: str, path: str, token=None, payload=None) -> dict:
        self.calls.append((method, path))
        if self.fail and self.fail(method, path):
            raise lodger.OsfError(f"{method} {path}: HTTP 500")
        if self.malformed and self.malformed(method, path):
            if path.endswith("/actions/"):
                trigger = payload["data"]["attributes"]["trigger"]
                self.approved = self.approved or trigger == "approve"
            return {}
        if method == "GET" and path.startswith("registrations/"):
            newest = self.RID if self.approved else "old-revision"
            return {"data": [{"id": newest, "attributes": {"reviews_state": "approved"}}]}
        if method == "GET" and path == "schema_responses/old-revision/":
            return {"data": {"attributes": {"revision_responses": {"summary": self.previous}}}}
        if method == "GET" and path == f"schema_responses/{self.RID}/":
            shown = self.public if self.public is not None else lodger.entity_form(self.sent)
            state = "approved" if self.approved else "unapproved"
            return {"data": {"attributes": {"reviews_state": state,
                                            "revision_responses": {"summary": shown}}}}
        if method == "POST" and path == "schema_responses/":
            return {"data": {"id": self.RID, "attributes": {"reviews_state": "in_progress"}}}
        if method == "PATCH":
            attributes = payload["data"]["attributes"]
            self.sent = attributes["revision_responses"]["summary"]
            stored = (self.mangle or lodger.entity_form)(self.sent)
            return {"data": {"attributes": {
                "revision_responses": {"summary": stored},
                "updated_response_keys": self.keys,
                "revision_justification": attributes["revision_justification"]}}}
        if method == "POST" and path.endswith("/actions/"):
            trigger = payload["data"]["attributes"]["trigger"]
            self.approved = self.approved or trigger == "approve"
            return {"data": {"attributes": {"from_state": "a", "to_state": "b"}}}
        raise AssertionError(f"unexpected call {method} {path}")

    def acted(self) -> bool:
        """Whether submit or approve was ever requested."""
        return any(path.endswith("/actions/") for _, path in self.calls)


class LodgeSequenceTests(unittest.TestCase):
    """The ``lodge`` mode against a fake OSF."""

    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        (root / "artefact.txt").write_text(ARTEFACT, encoding="utf-8")
        (root / "justification.txt").write_text("Amendment 3. Why.\n", encoding="utf-8")
        self.args = argparse.Namespace(
            artefact=str(root / "artefact.txt"), justification=str(root / "justification.txt"),
            amendment=3, date="2026-10-08", out=str(root / "out"))
        patches = [mock.patch.dict(os.environ, {"OSF_API_KEY": "test-token"}),
                   mock.patch.object(lodger, "PAUSE_SECONDS", 0)]
        for patch in patches:
            patch.start()
            self.addCleanup(patch.stop)
        self.addCleanup(self.tmp.cleanup)

    def run_lodge(self, fake: FakeOsf) -> str | None:
        """Run ``lodge`` against the fake; return the exit message, if any."""
        with mock.patch.object(lodger, "request", fake), mock.patch("builtins.print"):
            try:
                lodger.lodge(self.args)
            except SystemExit as exc:
                return str(exc.code)
        return None

    def test_clean_run_submits_then_approves(self) -> None:
        fake = FakeOsf(PREVIOUS)
        self.assertIsNone(self.run_lodge(fake))
        actions = [path for method, path in fake.calls if path.endswith("/actions/")]
        self.assertEqual(len(actions), 2)
        self.assertTrue(fake.approved)

    def test_altered_storage_never_submits(self) -> None:
        fake = FakeOsf(PREVIOUS, mangle=lambda sent: sent + " ")
        message = self.run_lodge(fake)
        self.assertIn("content check failed", message)
        self.assertFalse(fake.acted())

    def test_extra_changed_key_never_submits(self) -> None:
        fake = FakeOsf(PREVIOUS, keys=("summary", "uploader"))
        self.assertIn("content check failed", self.run_lodge(fake))
        self.assertFalse(fake.acted())

    def test_failed_write_never_submits(self) -> None:
        fake = FakeOsf(PREVIOUS, fail=lambda method, path: method == "PATCH")
        message = self.run_lodge(fake)
        self.assertIn("stopped before submission", message)
        self.assertIn(FakeOsf.RID, message)
        self.assertFalse(fake.acted())

    def test_failure_after_submit_is_not_called_private(self) -> None:
        fake = FakeOsf(PREVIOUS, fail=lambda method, path: path.endswith("/actions/")
                       and len([c for c in fake.calls if c[1].endswith("/actions/")]) == 2)
        message = self.run_lodge(fake)
        self.assertIn("after submission was attempted", message)
        self.assertIn(FakeOsf.RID, message)
        self.assertIn("last confirmed state: unapproved", message)
        self.assertNotIn("not public", message)

    def test_malformed_response_after_submit_is_handled(self) -> None:
        # The approve request takes effect but its reply lacks OSF's
        # structure; the state query then fails the same way.
        fake = FakeOsf(PREVIOUS, malformed=lambda method, path: (
            path.endswith("/actions/") and fake.calls.count((method, path)) == 2
            or (method == "GET" and path == f"schema_responses/{FakeOsf.RID}/")))
        message = self.run_lodge(fake)
        self.assertIn("after submission was attempted", message)
        self.assertIn(FakeOsf.RID, message)
        self.assertIn("last confirmed state: unknown (KeyError", message)

    def test_malformed_write_reply_never_submits(self) -> None:
        fake = FakeOsf(PREVIOUS, malformed=lambda method, path: method == "PATCH")
        self.assertIn("stopped before submission", self.run_lodge(fake))
        self.assertFalse(fake.acted())

    def test_public_mismatch_is_reported_after_submission(self) -> None:
        fake = FakeOsf(PREVIOUS, public="something else")
        message = self.run_lodge(fake)
        self.assertIn("after submission was attempted", message)
        self.assertIn("public verification failed", message)


class RequestTests(unittest.TestCase):
    """``request`` turns a non-JSON reply into ``OsfError``."""

    def test_non_json_reply_raises_osf_error(self) -> None:
        reply = mock.MagicMock()
        reply.__enter__.return_value = io.BytesIO(b"<html>maintenance</html>")
        with mock.patch.object(lodger.urllib.request, "urlopen", return_value=reply):
            with self.assertRaises(lodger.OsfError):
                lodger.request("GET", "schema_responses/x/")


if __name__ == "__main__":
    unittest.main()
