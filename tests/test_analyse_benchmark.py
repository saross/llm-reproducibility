#!/usr/bin/env python3
"""Unit tests for analyse-benchmark-disagreements.py (v1.1).

Covers the v1.1 ``--arms`` extension (explicit arm directories spanning
cycles), the error-direction split, and the two-era guide-presence
detection. The end-to-end case builds a synthetic two-arm corpus with
known stability, concordance, and error-direction answers, plus a
synthetic manifest reference, and checks both stdout figures and the
written disputed-items.json.

Run: ``venv/bin/python -m pytest tests/test_analyse_benchmark.py -q``
"""

from __future__ import annotations

import contextlib
import importlib.machinery
import importlib.util
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

_spec = importlib.util.spec_from_loader(
    "analyse_benchmark",
    importlib.machinery.SourceFileLoader(
        "analyse_benchmark",
        str(REPO_ROOT / "studies" / "open-science-compliance" / "protocol"
            / "validation" / "analyse-benchmark-disagreements.py")))
tool = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(tool)

SLUGS = [f"paper-{n}" for n in range(1, 6)]


def spawn_payload(slug: str, overrides: dict | None = None) -> dict:
    """A spawn scoring 0 everywhere except (artefact, sub) -> 1 overrides."""
    body: dict = {"paper_slug": slug}
    for artefact in tool.ARTEFACTS:
        subs = {}
        for sub in tool.SUB_PRINCIPLES:
            present = int((overrides or {}).get((artefact, sub), 0))
            subs[sub] = {"present": present, "evidence": f"{artefact}/{sub}"}
        body[artefact] = {"sub_principles": subs}
    return body


def write_arm(root: Path, name: str, run_overrides: dict,
              run_record: dict | None = None) -> Path:
    """Write arm-<name> with three runs of five papers.

    ``run_overrides`` maps (run, slug) -> overrides for spawn_payload.
    """
    arm = root / f"arm-{name}"
    for run in (1, 2, 3):
        run_dir = arm / f"run-{run}"
        run_dir.mkdir(parents=True)
        for slug in SLUGS:
            payload = spawn_payload(slug, run_overrides.get((run, slug)))
            (run_dir / f"{slug}.json").write_text(json.dumps(payload))
    if run_record is not None:
        (arm / "run-record.json").write_text(json.dumps(run_record))
    return arm


def write_reference(root: Path, overrides: dict | None = None) -> Path:
    """Write a synthetic manifest + reference files; all-zero + overrides.

    ``overrides`` maps (slug, artefact, sub) -> 1. Returns the manifest
    path. Reference files use absolute paths so REPO_ROOT joining
    resolves to them unchanged.
    """
    items = []
    for slug in SLUGS:
        ref_file = root / f"ref-{slug}.json"
        artefacts = {}
        for artefact in tool.ARTEFACTS:
            leaves = {}
            for sub in tool.SUB_PRINCIPLES:
                present = int((overrides or {}).get((slug, artefact, sub), 0))
                leaves[f"{sub}_synthetic"] = {
                    "present": present, "evidence": "synthetic reference"}
            artefacts[artefact] = {"dim": leaves}
        ref_file.write_text(json.dumps({"fair": artefacts}))
        items.append({"slug": slug, "file": str(ref_file), "fair_key": "fair"})
    manifest = root / "manifest.yaml"
    manifest.write_text(json.dumps(  # JSON is valid YAML
        {"reference_datasets": {"pilot_fair_assessments": {"items": items}}}))
    return manifest


def run_main(argv: list[str]) -> str:
    """Run tool.main() with argv, returning captured stdout."""
    out = io.StringIO()
    old_argv = sys.argv
    sys.argv = ["analyse-benchmark-disagreements.py"] + argv
    try:
        with contextlib.redirect_stdout(out):
            tool.main()
    finally:
        sys.argv = old_argv
    return out.getvalue()


class ResolveArmsTests(unittest.TestCase):
    def test_labels_derive_from_basenames(self):
        with tempfile.TemporaryDirectory() as tmp:
            a = Path(tmp) / "cycle-1" / "arm-sonnet-5"
            b = Path(tmp) / "cycle-2" / "arm-sonnet-5-high"
            a.mkdir(parents=True)
            b.mkdir(parents=True)
            arms = tool.resolve_arms([a, b])
            self.assertEqual(list(arms), ["sonnet-5", "sonnet-5-high"])

    def test_missing_directory_rejected(self):
        with self.assertRaises(SystemExit):
            tool.resolve_arms([Path("/nonexistent/arm-x")])

    def test_non_arm_prefix_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            bad = Path(tmp) / "sonnet-5"
            bad.mkdir()
            with self.assertRaises(SystemExit):
                tool.resolve_arms([bad])

    def test_duplicate_label_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            a = Path(tmp) / "cycle-1" / "arm-opus-5"
            b = Path(tmp) / "cycle-2" / "arm-opus-5"
            a.mkdir(parents=True)
            b.mkdir(parents=True)
            with self.assertRaises(SystemExit):
                tool.resolve_arms([a, b])


class ErrorDirectionTests(unittest.TestCase):
    def test_match_is_none(self):
        self.assertIsNone(tool.error_direction(1, 1))
        self.assertIsNone(tool.error_direction(0, 0))

    def test_over_credit(self):
        self.assertEqual(tool.error_direction(1, 0), "over_credit")

    def test_under_credit(self):
        self.assertEqual(tool.error_direction(0, 1), "under_credit")


class GuidePresenceTests(unittest.TestCase):
    def test_pull_era_detected(self):
        payload = {"receipts": {"pulled_files_read": [
            "/skills/x/fair-principles-guide.md"]}}
        self.assertTrue(tool.pulled_guide(payload))

    def test_push_era_detected(self):
        payload = {"receipts": {"instrument_receipts": {
            "fair-principles-guide": "sha256:abc"}}}
        self.assertTrue(tool.pulled_guide(payload))

    def test_guideless(self):
        payload = {"receipts": {"pulled_files_read": ["/papers/vor.pdf"],
                                "instrument_receipts": {"fair-instrument": "x"}}}
        self.assertFalse(tool.pulled_guide(payload))


class EndToEndTests(unittest.TestCase):
    """Two synthetic arms with known answers, run through main()."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        tmp = Path(self._tmp.name)
        # Reference: all zero except paper-1 data_fair F1 = 1.
        self._old_manifest = tool.MANIFEST
        tool.MANIFEST = write_reference(
            tmp, {("paper-1", "data_fair", "F1"): 1})
        # Arm alpha: run-2 flips paper-1 data_fair A1 -> one 2-1 split;
        # every majority is 0, so the only mismatch is F1 (under-credit).
        self.alpha = write_arm(
            tmp, "alpha",
            {(2, "paper-1"): {("data_fair", "A1"): 1}},
            run_record={"stability": {"agreed": 149, "items": 150}})
        # Arm beta: all runs score paper-1 data_fair F2 = 1 -> unanimous
        # over-credit at F2, plus the shared F1 under-credit. No record
        # stability (the fresh-cycle path).
        self.beta = write_arm(
            tmp, "beta",
            {(run, "paper-1"): {("data_fair", "F2"): 1} for run in (1, 2, 3)},
            run_record={})
        self.out_dir = tmp / "analysis"

    def tearDown(self):
        tool.MANIFEST = self._old_manifest
        self._tmp.cleanup()

    def run_tool(self, extra: list[str] | None = None) -> tuple[str, dict]:
        stdout = run_main(["--arms", str(self.alpha), str(self.beta),
                           "--out-dir", str(self.out_dir)] + (extra or []))
        written = json.loads((self.out_dir / "disputed-items.json").read_text())
        return stdout, written

    def test_stability_and_concordance_figures(self):
        stdout, _ = self.run_tool()
        self.assertIn("alpha: stability 149/150 = 0.9933 "
                      "(run-record 149/150) OK", stdout)
        self.assertIn("beta: stability 150/150 = 1.0000 "
                      "(fresh cycle — no published figure", stdout)
        self.assertIn("alpha: concordance 149/150 = 0.9933", stdout)
        self.assertIn("errors: 0 over-credit, 1 under-credit", stdout)
        self.assertIn("beta: concordance 148/150 = 0.9867", stdout)
        self.assertIn("errors: 1 over-credit, 1 under-credit", stdout)

    def test_disputed_items_and_directions(self):
        _, written = self.run_tool()
        keys = {(i["paper"], i["artefact"], i["sub_principle"])
                for i in written["items"]}
        self.assertEqual(keys, {("paper-1", "data_fair", "F1"),
                                ("paper-1", "data_fair", "F2"),
                                ("paper-1", "data_fair", "A1")})
        by_sub = {i["sub_principle"]: i for i in written["items"]}
        self.assertEqual(by_sub["F1"]["arms"]["alpha"]["error_direction"],
                         "under_credit")
        self.assertEqual(by_sub["F2"]["arms"]["beta"]["error_direction"],
                         "over_credit")
        self.assertIsNone(by_sub["A1"]["arms"]["alpha"]["error_direction"])
        self.assertEqual(written["arms"]["alpha"], str(self.alpha))
        self.assertEqual(written["reference_key"], "pilot_fair_assessments")

    def test_stability_only_suppresses_concordance(self):
        stdout, written = self.run_tool(["--stability-only"])
        self.assertIn("concordance SUPPRESSED", stdout)
        self.assertNotIn("over-credit", stdout)
        self.assertTrue(written["stability_only"])

    def test_arms_requires_out_dir(self):
        with self.assertRaises(SystemExit):
            run_main(["--arms", str(self.alpha)])

    def test_arms_excludes_bench_dir(self):
        with self.assertRaises(SystemExit):
            run_main(["--arms", str(self.alpha), "--out-dir",
                      str(self.out_dir), "--bench-dir", str(self.alpha.parent)])

    def test_unknown_reference_key_rejected(self):
        with self.assertRaises(SystemExit):
            self.run_tool(["--reference-key", "no-such-reference"])


if __name__ == "__main__":
    unittest.main()
