#!/usr/bin/env python3
"""Cell-by-cell diff of herskind-riede-2024 Zenodo v1 vs v2 spreadsheets.

**Version:** 1.0 (2026-10-03)

Pre-committed by the shakedown regression criterion (section "Input-version
drift"): attempt-01 used Zenodo v1 (10.5281/zenodo.10623550) and attempt-02
uses v2 (10.5281/zenodo.10801706) under rule AP-12, and the S1/S3 files
differ in size. Before attempt-01 and attempt-02 values are compared, every
changed cell must be known, so that a value difference can be traced to an
input change (explained input drift) or not (a harness failure).

The script downloads both versions' S1.xlsx and S3.xlsx from the Zenodo
API into a scratch directory, verifies each file against Zenodo's
published md5, and compares every sheet cell by cell (cell values, not
styles). It writes a JSON report and prints a summary.

Operator-side only: the reproduction agents never run or read this.

Usage:
    uv run --with openpyxl python \\
        studies/open-science-compliance/outputs/validation/phase2-shakedown/input-drift-check.py \\
        --scratch <dir> --out <report.json>
"""

from __future__ import annotations

import argparse
import hashlib
import json
import urllib.parse
import urllib.request
from pathlib import Path

import openpyxl

RECORDS = {"v1": "10623550", "v2": "10801706"}
FILES = ("Herskind&Riede_S1.xlsx", "Herskind&Riede_S3.xlsx")


def zenodo_files(record: str) -> dict[str, dict]:
    """Map file key -> {url, md5} from the Zenodo record API."""
    with urllib.request.urlopen(f"https://zenodo.org/api/records/{record}", timeout=60) as r:
        meta = json.load(r)
    out = {}
    for entry in meta.get("files", []):
        key = entry["key"]
        url = (f"https://zenodo.org/api/records/{record}/files/"
               f"{urllib.parse.quote(key)}/content")
        out[key] = {"url": url, "md5": str(entry.get("checksum", "")).replace("md5:", "")}
    return out


def fetch(url: str, dest: Path, md5: str) -> None:
    """Download ``url`` to ``dest`` and verify its md5 (raises on mismatch)."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url, timeout=120) as r:
        data = r.read()
    got = hashlib.md5(data).hexdigest()
    if got != md5:
        raise RuntimeError(f"md5 mismatch for {dest.name}: got {got}, published {md5}")
    dest.write_bytes(data)


def sheet_cells(path: Path) -> dict[str, dict[str, object]]:
    """{sheet: {cell coordinate: value}} for every non-empty cell."""
    book = openpyxl.load_workbook(path, data_only=True, read_only=True)
    cells: dict[str, dict[str, object]] = {}
    for sheet in book.worksheets:
        values = {}
        for row in sheet.iter_rows():
            for cell in row:
                if cell.value is not None and hasattr(cell, "coordinate"):
                    values[cell.coordinate] = cell.value
        cells[sheet.title] = values
    return cells


def diff(old: dict, new: dict) -> dict:
    """Per-sheet changed / added / removed cells between two workbooks."""
    report = {}
    for sheet in sorted(set(old) | set(new)):
        a, b = old.get(sheet, {}), new.get(sheet, {})
        changed = {c: [a[c], b[c]] for c in sorted(set(a) & set(b)) if a[c] != b[c]}
        added = {c: b[c] for c in sorted(set(b) - set(a))}
        removed = {c: a[c] for c in sorted(set(a) - set(b))}
        report[sheet] = {"only_in": ("v2" if sheet not in old else "v1" if sheet not in new
                                     else None),
                         "cells_v1": len(a), "cells_v2": len(b),
                         "changed": changed, "added": added, "removed": removed}
    return report


def main() -> int:
    """Download, verify, diff, and report."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--scratch", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    listings = {v: zenodo_files(rec) for v, rec in RECORDS.items()}
    report = {"check_version": "1.0", "records": RECORDS, "files": {}}
    for name in FILES:
        paths = {}
        for version in RECORDS:
            entry = listings[version][name]
            paths[version] = args.scratch / version / name
            fetch(entry["url"], paths[version], entry["md5"])
        result = diff(sheet_cells(paths["v1"]), sheet_cells(paths["v2"]))
        report["files"][name] = {"md5": {v: listings[v][name]["md5"] for v in RECORDS},
                                 "sheets": result}
        for sheet, d in result.items():
            print(f"{name} [{sheet}]: v1 {d['cells_v1']} cells, v2 {d['cells_v2']} cells; "
                  f"changed {len(d['changed'])}, added {len(d['added'])}, "
                  f"removed {len(d['removed'])}"
                  + (f" (sheet only in {d['only_in']})" if d["only_in"] else ""))
    args.out.write_text(json.dumps(report, indent=2, ensure_ascii=False, default=str) + "\n",
                        encoding="utf-8")
    print(f"wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
