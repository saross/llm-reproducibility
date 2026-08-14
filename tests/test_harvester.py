#!/usr/bin/env python3
"""Unit tests for the artefact-metadata harvester (plan C6).

All network access is mocked — the suite proves routing, record shape,
hashing, conflict detection, and honest-gap behaviour without touching any
endpoint. The live harvest is a separate, deliberate operator action.

Run: ``venv/bin/python -m pytest tests/test_harvester.py -q``
"""

from __future__ import annotations

import hashlib
import importlib.machinery
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = REPO_ROOT / "scripts" / "harvest-artefact-metadata.py"

_spec = importlib.util.spec_from_loader(
    "harvest_artefact_metadata",
    importlib.machinery.SourceFileLoader("harvest_artefact_metadata", str(SCRIPT)))
harvester = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(harvester)


class RoutingTests(unittest.TestCase):
    """classify() maps declared links to the ratified endpoints."""

    def test_zenodo_doi_routes_to_both_datacite_and_zenodo(self) -> None:
        steps = harvester.classify("10.5281/zenodo.10782942")
        self.assertEqual([s[0] for s in steps], ["datacite", "zenodo"])
        self.assertIn("api.datacite.org", steps[0][1])
        self.assertIn("zenodo.org/api/records/10782942", steps[1][1])

    def test_elsevier_article_doi_routes_to_crossref(self) -> None:
        steps = harvester.classify("10.1016/j.jas.2024.105962")
        self.assertEqual([s[0] for s in steps], ["crossref"])

    def test_other_doi_routes_to_datacite(self) -> None:
        steps = harvester.classify("10.5284/1018290")
        self.assertEqual([s[0] for s in steps], ["datacite"])

    def test_github_url_routes_to_repos_api(self) -> None:
        steps = harvester.classify("https://github.com/ercrema/diffusionCurve")
        self.assertEqual(steps[0][0], "github")
        self.assertEqual(steps[0][1],
                         "https://api.github.com/repos/ercrema/diffusionCurve")

    def test_cran_url_is_flagged_not_resolved(self) -> None:
        steps = harvester.classify("https://cran.r-project.org/package=ArchaeoPhases")
        self.assertEqual(steps, [("cran", "")])

    def test_unknown_host_is_unrouted(self) -> None:
        steps = harvester.classify("https://example.com/dataset")
        self.assertEqual(steps, [("unrouted", "")])

    def test_trailing_dot_stripped(self) -> None:
        steps = harvester.classify("10.5281/zenodo.10801706.")
        self.assertEqual([s[0] for s in steps], ["datacite", "zenodo"])


class CanonicalLicenceTests(unittest.TestCase):
    """Licence URLs canonicalise to short ids where mechanically safe."""

    def test_cc_by_url_canonicalises(self) -> None:
        self.assertEqual(harvester.canonical_licence(
            "http://creativecommons.org/licenses/by/4.0/"), "cc-by-4.0")

    def test_cc_zero_url_canonicalises(self) -> None:
        self.assertEqual(harvester.canonical_licence(
            "https://creativecommons.org/publicdomain/zero/1.0/"), "cc0-1.0")

    def test_unknown_licence_passes_through(self) -> None:
        self.assertEqual(harvester.canonical_licence(
            "https://www.elsevier.com/tdm/userlicense/1.0/"),
            "https://www.elsevier.com/tdm/userlicense/1.0/")


class ConflictTests(unittest.TestCase):
    """Licence conflict detection is conservative but not trigger-happy."""

    def test_matching_licence_no_conflict(self) -> None:
        self.assertFalse(harvester.licences_conflict("CC BY", ["cc-by-4.0"]))

    def test_live_false_positive_regression(self) -> None:
        """The key-et-al case from the first live harvest: 'CC BY' asserted
        against a canonicalised Crossref licence list is NOT a conflict."""
        self.assertFalse(harvester.licences_conflict(
            "CC BY", ["cc-by-4.0", "https://www.elsevier.com/legal/tdmrep-license",
                      "https://www.elsevier.com/tdm/userlicense/1.0/"]))

    def test_multi_licence_vs_single_field_conflicts(self) -> None:
        self.assertTrue(harvester.licences_conflict(
            "MIT (code); CC0 (data); CC BY (figures)", ["cc-zero"]))

    def test_no_service_record_no_conflict(self) -> None:
        self.assertFalse(harvester.licences_conflict("CC BY", []))

    def test_no_assertion_no_conflict(self) -> None:
        self.assertFalse(harvester.licences_conflict("", ["mit"]))


class HarvestLinkTests(unittest.TestCase):
    """harvest_link() with fetch mocked: record shape, hashing, statuses."""

    def setUp(self) -> None:
        self.original_fetch = harvester.fetch
        harvester._FETCH_CACHE.clear()

    def tearDown(self) -> None:
        harvester.fetch = self.original_fetch
        harvester._FETCH_CACHE.clear()

    def test_resolved_record_shape_and_hash(self) -> None:
        body = json.dumps({"message": {"DOI": "10.1016/j.jas.2024.105962",
                                       "type": "journal-article",
                                       "publisher": "Elsevier BV",
                                       "license": [{"URL": "https://tdm.example/licence"}]}}
                          ).encode("utf-8")
        harvester.fetch = lambda url, headers=None: (200, body)
        records = harvester.harvest_link(
            {"id": "article", "type": "article", "link": "10.1016/j.jas.2024.105962"})
        self.assertEqual(len(records), 1)
        record = records[0]
        self.assertEqual(record["status"], "resolved")
        self.assertEqual(record["record_id"], "crossref:10.1016/j.jas.2024.105962")
        self.assertEqual(record["declared_by"],
                         [{"declared_id": "article", "artefact_type": "article"}])
        self.assertEqual(record["response_sha256"],
                         hashlib.sha256(body).hexdigest())
        self.assertEqual(record["fields"]["doi"], "10.1016/j.jas.2024.105962")
        self.assertTrue(record["fields"]["metadata_record"])
        self.assertEqual(record["fields"]["licences"], ["https://tdm.example/licence"])

    def test_http_404_is_unresolved_not_silent(self) -> None:
        harvester.fetch = lambda url, headers=None: (404, b"{}")
        records = harvester.harvest_link(
            {"id": "gone", "type": "data", "link": "10.5284/0000000"})
        self.assertEqual(records[0]["status"], "unresolved")
        self.assertIn("404", records[0]["note"])

    def test_transport_failure_is_unresolved(self) -> None:
        harvester.fetch = lambda url, headers=None: (0, b"")
        records = harvester.harvest_link(
            {"id": "dead", "type": "data", "link": "10.5284/0000000"})
        self.assertEqual(records[0]["status"], "unresolved")
        self.assertIn("transport", records[0]["note"])

    def test_flagged_endpoint_records_honest_gap_without_fetch(self) -> None:
        def forbidden(url, headers=None):  # pragma: no cover - must not run
            raise AssertionError("flagged endpoints must not be fetched")
        harvester.fetch = forbidden
        records = harvester.harvest_link(
            {"id": "pkg", "type": "code",
             "link": "https://cran.r-project.org/package=ArchaeoPhases"})
        self.assertEqual(records[0]["status"], "endpoint-flagged")
        self.assertIn("flagged", records[0]["note"])

    def test_conflict_flag_attached_when_asserted_licence_differs(self) -> None:
        body = json.dumps({"id": 14897252, "doi": "10.5281/zenodo.14897252",
                           "metadata": {"license": {"id": "cc-zero"},
                                        "access_right": "open"}}).encode("utf-8")
        harvester.fetch = lambda url, headers=None: (200, body)
        records = harvester.harvest_link(
            {"id": "compendium", "type": "data+code",
             "link": "https://zenodo.org/records/14897252",
             "paper_asserted_licence": "MIT (code); CC0 (data); CC BY (figures)"})
        flag = records[0]["licence_conflicts"][0]
        self.assertTrue(flag["conflict"])
        self.assertEqual(flag["service_recorded"], ["cc-zero"])
        self.assertIn("most restrictive", flag["rule"])

    def test_shared_identifier_deduplicates_within_pack(self) -> None:
        """Two registry entries naming one identifier (article + supplement)
        merge into one record with both declarers — record_id stays unique
        (live-harvest regression: dye's pack carried duplicate records)."""
        body = json.dumps({"message": {"DOI": "10.1016/j.x", "type": "journal-article",
                                       "publisher": "P", "license": []}}).encode()
        harvester.fetch = lambda url, headers=None: (200, body)
        pack = harvester.harvest_paper("fixture", {"links": [
            {"id": "article", "type": "article", "link": "10.1016/j.x"},
            {"id": "supplement", "type": "supplement", "link": "10.1016/j.x"},
        ]})
        self.assertEqual(len(pack["records"]), 1)
        self.assertEqual([d["declared_id"] for d in pack["records"][0]["declared_by"]],
                         ["article", "supplement"])


class TokenTests(unittest.TestCase):
    """The env-file token loader parses without ever printing the value."""

    def test_token_parsed_from_synthetic_env(self) -> None:
        with tempfile.NamedTemporaryFile("w", suffix=".env", delete=False) as f:
            f.write("OTHER=1\nGITHUB_API_TOKEN_LLMR=synthetic-test-value\n")
            path = Path(f.name)
        self.addCleanup(path.unlink)
        original = harvester.ENV_PATH
        harvester.ENV_PATH = path
        try:
            self.assertEqual(harvester.github_token(), "synthetic-test-value")
        finally:
            harvester.ENV_PATH = original

    def test_absent_env_file_returns_none(self) -> None:
        original = harvester.ENV_PATH
        harvester.ENV_PATH = Path("/nonexistent/.env")
        try:
            self.assertIsNone(harvester.github_token())
        finally:
            harvester.ENV_PATH = original


if __name__ == "__main__":
    unittest.main(verbosity=2)
