#!/usr/bin/env python3
"""Mechanical checks behind the executed-code audit of the five pilots.

**Version:** 1.0 (2026-10-04)

Ruling (Shawn, 2026-10-04, fail-and-uplift follow-on 4): the pilots'
executed code is audited against the authors' originals before the
registered regression gate, to find undeclared repairs like dye's T02.
This script makes the mechanical part of that audit re-runnable. It uses
the gate's own helpers (``scripts/reproduction-lane.py`` v1.1:
``substantive_lines`` and ``lines_changed``), so the audit and gate 1.1
count the same way.

It reports, per pilot attempt:

1. sha256 of every authors' original it can read, and of every executed
   copy kept on disk;
2. for each executed copy that differs from its original, the lines
   changed (difflib opcodes, as the gate counts them);
3. for each reproducer-written code file, how many substantive lines it
   shares with each authors' original (an inlining signal; gate 1.1 flags
   five or more).

Originals that are not in the repository were downloaded from their public
deposits (URLs and sha256 in ``findings.json``) into a directory passed as
``--originals``. Missing inputs are reported as unreadable, never guessed.

Usage:
    venv/bin/python studies/open-science-compliance/outputs/validation/\\
executed-code-audit-2026-10-04/audit-checks.py --originals <dir> [--out FILE]

Expected layout of <dir> (each fetched by the URL recorded in findings.json):
    herskind-v1/Herskind&Riede_S2.R
    key/mmc1.zip
    marwick/web-of-science-archaeology-1.3.zip
    marwick/head/analysis/paper/paper.qmd   (commit 652e542, the executed HEAD)
    crema/diffusionCurve-v1.0.0.zip
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.machinery
import importlib.util
import json
import zipfile
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[5]
OUTPUTS = REPO_ROOT / "studies" / "open-science-compliance" / "outputs"
DYE1 = OUTPUTS / "dye-et-al-2023" / "reproduction" / "attempt-01"
DYE2 = OUTPUTS / "dye-et-al-2023" / "reproduction" / "attempt-02"
HER1 = OUTPUTS / "herskind-riede-2024" / "reproduction" / "attempt-01"
HER2 = OUTPUTS / "herskind-riede-2024" / "reproduction" / "attempt-02"
KEY1 = OUTPUTS / "key-et-al-2024" / "reproduction" / "attempt-01"
KEY_MAIN = "Morphology OLE Script _spl_Main_spl_ Supplementary Information.r"


def load_lane() -> Any:
    """Import the lane tool (hyphenated file name) for its shared helpers."""
    path = REPO_ROOT / "scripts" / "reproduction-lane.py"
    loader = importlib.machinery.SourceFileLoader("reproduction_lane", str(path))
    spec = importlib.util.spec_from_loader("reproduction_lane", loader)
    module = importlib.util.module_from_spec(spec)
    loader.exec_module(module)
    return module


LANE = load_lane()


def sha256(data: bytes) -> str:
    """Hex sha256 of bytes."""
    return hashlib.sha256(data).hexdigest()


def zip_member(archive: Path, suffix: str) -> bytes | None:
    """Bytes of the single member whose path ends with ``suffix``, or None."""
    if not archive.is_file():
        return None
    with zipfile.ZipFile(archive) as handle:
        names = [n for n in handle.namelist() if n.endswith(suffix)]
        return handle.read(names[0]) if len(names) == 1 else None


def compare(original: bytes | None, executed: bytes | None) -> dict[str, Any]:
    """Identity and size of difference between an original and an executed copy."""
    if original is None or executed is None:
        return {"comparable": False}
    same = original == executed
    return {"comparable": True, "identical": same, "original_sha256": sha256(original),
            "executed_sha256": sha256(executed),
            "lines_changed": None if same else LANE.lines_changed(original, executed)}


def embedded(wrapper: Path, originals: dict[str, bytes]) -> dict[str, int]:
    """Substantive lines a reproducer file shares with each authors' original."""
    mine = LANE.substantive_lines(wrapper.read_text(encoding="utf-8", errors="replace"))
    return {oid: len(mine & LANE.substantive_lines(data.decode("utf-8", errors="replace")))
            for oid, data in originals.items()}


def reproducer_files(attempt: Path, exclude: set[Path]) -> list[Path]:
    """Code files in an attempt directory outside outputs/, minus authors' files."""
    return [p for p in sorted(attempt.rglob("*"))
            if p.is_file() and p.relative_to(attempt).parts[0] != "outputs"
            and LANE.is_code_file(p) and p not in exclude]


def main() -> None:
    """Run every check and write the JSON summary."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--originals", type=Path, required=True)
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args()
    orig = args.originals
    result: dict[str, Any] = {"audit_checks_version": "1.0",
                              "embedded_lines_flag": LANE.EMBEDDED_LINES_FLAG}

    # dye: the authors' code exists only as listings in supplement mmc1.pdf;
    # authors-code-raw/ is the deterministic transcription (re-derived by the
    # audit from the corpus-store PDF and found byte-identical).
    raw = {p.name: p.read_bytes() for p in sorted((DYE2 / "authors-code-raw").glob("*.R"))}
    dye2 = {"executed_vs_transcription": {
        name: compare(data, (DYE2 / "authors-code" / name).read_bytes())
        for name, data in raw.items()}}
    authors_files = {p.resolve() for p in (DYE2 / "authors-code").glob("*.R")} | \
        {p.resolve() for p in (DYE2 / "authors-code-raw").glob("*.R")}
    dye2["reproducer_files"] = {
        str(p.relative_to(DYE2)): {k: v for k, v in embedded(p, raw).items() if v}
        for p in reproducer_files(DYE2, authors_files)}
    result["dye-et-al-2023/attempt-02"] = dye2
    result["dye-et-al-2023/attempt-01"] = {"reproducer_files": {
        str(p.relative_to(DYE1)): {k: v for k, v in embedded(p, raw).items() if v}
        for p in reproducer_files(DYE1, set())}}

    # herskind: v2 S2.R is kept in attempt-02/data (md5 equals Zenodo's
    # published checksum); v1 S2.R was downloaded from Zenodo record 10623550.
    s2_v2 = (HER2 / "data" / "Herskind&Riede_S2.R").read_bytes()
    v1_path = orig / "herskind-v1" / "Herskind&Riede_S2.R"
    s2_v1 = v1_path.read_bytes() if v1_path.is_file() else None
    her_originals = {"S2.R v2": s2_v2}
    if s2_v1 is not None:
        her_originals["S2.R v1"] = s2_v1
    result["herskind-riede-2024/attempt-02"] = {
        "executed": {"data/Herskind&Riede_S2.R": {"sha256": sha256(s2_v2)}},
        "reproducer_files": {
            str(p.relative_to(HER2)): embedded(p, her_originals)
            for p in reproducer_files(HER2, {(HER2 / "data" / "Herskind&Riede_S2.R")
                                             .resolve()})}}
    result["herskind-riede-2024/attempt-01"] = {
        "s2_v1_sha256": sha256(s2_v1) if s2_v1 else None,
        "reproducer_files": {str(p.relative_to(HER1)): embedded(p, her_originals)
                             for p in reproducer_files(HER1, set())}}

    # key: supplement mmc1.zip holds the main OLE script; attempt-01/scripts/
    # keeps byte-identical copies, which the run never executed.
    main_script = zip_member(orig / "key" / "mmc1.zip", KEY_MAIN)
    kept = (KEY1 / "scripts" / KEY_MAIN).read_bytes()
    result["key-et-al-2024/attempt-01"] = {
        "kept_copy_vs_supplement": compare(main_script, kept),
        "reproducer_files": {
            str(p.relative_to(KEY1)): embedded(p, {"mmc1 main": main_script or kept})
            for p in reproducer_files(KEY1, {q.resolve() for q in
                                             (KEY1 / "scripts").glob("*")})}}

    # marwick: the executed HEAD (652e542) against the AP-12 version (1.3).
    qmd_13 = zip_member(orig / "marwick" / "web-of-science-archaeology-1.3.zip",
                        "analysis/paper/paper.qmd")
    head_path = orig / "marwick" / "head" / "analysis" / "paper" / "paper.qmd"
    qmd_head = head_path.read_bytes() if head_path.is_file() else None
    result["marwick-2025/attempt-01"] = {"paper.qmd v1.3 vs executed HEAD":
                                         compare(qmd_13, qmd_head)}

    # crema: the executed copies live in the sapphire image diffusion-curve:run
    # (git tag v2.0.0 plus a Dockerfile edit); their hashes were taken there.
    crema_zip = orig / "crema" / "diffusionCurve-v1.0.0.zip"
    if crema_zip.is_file():
        with zipfile.ZipFile(crema_zip) as handle:
            root = handle.namelist()[0].split("/")[0] + "/"
            result["crema-et-al-2024/attempt-01"] = {"v1.0.0_member_sha256": {
                n[len(root):]: sha256(handle.read(n)) for n in handle.namelist()
                if not n.endswith("/") and LANE.is_code_file(Path(n))}}
    text = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.out:
        args.out.write_text(text, encoding="utf-8")
        print(f"wrote {args.out}")
    else:
        print(text)


if __name__ == "__main__":
    main()
