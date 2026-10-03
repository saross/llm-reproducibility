#!/usr/bin/env python3
"""Value-identity check (regression criterion check 2): attempt-01 vs attempt-02.

**Version:** 1.0 (2026-10-03)

Applies check 2 of the pre-committed criterion (``regression-criterion.md``):
every published value attempt-01 compared must be located in attempt-02's
value-level evidence with the same reproduced value at published precision.
Operator-side only, run after the blinded agents finished.

- **herskind-riede-2024:** attempt-01 ``outputs/{bigrams,trigrams,
  quadrigrams}.csv`` (its S3-equivalent reproduction, 291 rows) joined on the
  motif tuple to attempt-02 ``outputs/{Bigrams,Trigrams,Quadrigrams}.csv``;
  every numeric cell compared. Plus attempt-01's Table 1 frequency
  distribution (``comparisons/comparison-report.md``, "Frequency
  Distribution") against attempt-02's ``capture-table1-*.csv``.
- **dye-et-al-2023:** attempt-01 ``outputs/summary-stats.txt`` (R-printed
  matrices: section 7 oFD and Bayliss rows 1-9) against attempt-02's
  per-cell evidence (``comparisons/values/T12..T20-*.csv`` for the 54
  Supplement Table 2-10 cells; ``T06-section-07-full-matrix.csv`` for the
  stable-solid oFD matrix), at 2 decimal places.

Usage:
    python3 studies/open-science-compliance/outputs/validation/phase2-shakedown/regression-compare.py
"""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[5]
OUT = REPO / "studies/open-science-compliance/outputs"
HERE = Path(__file__).resolve().parent
NUM = r"(?:NA|-?\d+(?:\.\d+)?)"
ROW_RE = re.compile(rf"^(.*?)\s+({NUM}(?:\s+{NUM})*)\s*$")


def herskind() -> dict:
    """Compare attempt-01 and attempt-02 n-gram tables and Table 1 counts."""
    a1 = OUT / "herskind-riede-2024/reproduction/attempt-01"
    a2 = OUT / "herskind-riede-2024/reproduction/attempt-02"
    result: dict = {"ngram_tables": {}, "table1": {}}
    for old, new, n in (("bigrams", "Bigrams", 2), ("trigrams", "Trigrams", 3),
                        ("quadrigrams", "Quadrigrams", 4)):
        rows1 = list(csv.DictReader((a1 / "outputs" / f"{old}.csv").open()))
        rows2 = list(csv.DictReader((a2 / "outputs" / f"{new}.csv").open()))
        keyf = [f"token{i}" for i in range(1, n + 1)]
        idx2 = {tuple(r[k] for k in keyf): r for r in rows2}
        cells = mismatches = missing = 0
        numeric = [c for c in rows1[0] if c not in keyf]
        for r in rows1:
            other = idx2.get(tuple(r[k] for k in keyf))
            if other is None:
                missing += 1
                continue
            for col in numeric:
                cells += 1
                if abs(float(r[col]) - float(other[col])) > 1e-12 * max(1.0, abs(float(r[col]))):
                    mismatches += 1
        result["ngram_tables"][old] = {"rows_attempt01": len(rows1), "rows_attempt02": len(rows2),
                                      "rows_missing_in_attempt02": missing,
                                      "cells_compared": cells, "cells_differing": mismatches}
    # attempt-01 Table 1 summary (markdown table in its comparison report).
    report = (a1 / "comparisons/comparison-report.md").read_text(encoding="utf-8")
    block = report.split("### Frequency Distribution", 1)[1].split("###", 1)[0]
    a1_counts: dict[str, dict[str, int]] = {"bigram": {}, "trigram": {}, "quadrigram": {}}
    for line in block.splitlines():
        cells = [c.strip().strip("*") for c in line.strip().strip("|").split("|")]
        if len(cells) == 4 and cells[0] and cells[0][0].isdigit() and "≥" not in cells[0]:
            for kind, value in zip(("bigram", "trigram", "quadrigram"), cells[1:]):
                a1_counts[kind][cells[0]] = int(value.replace(",", ""))
    for kind in a1_counts:
        path = a2 / "outputs" / f"capture-table1-{kind}-frequencies.csv"
        rows = list(csv.reader(path.open()))
        header, body = rows[0], rows[1:]
        a2_counts = {str(int(float(r[0]))): int(float(r[1])) for r in body if r and r[0]}
        diffs = {f: (a1_counts[kind][f], a2_counts.get(f)) for f in a1_counts[kind]
                 if a1_counts[kind][f] != a2_counts.get(f)}
        result["table1"][kind] = {"frequencies_compared": sorted(a1_counts[kind], key=int),
                                  "header_attempt02": header, "differences": diffs}
    return result


def parse_r_matrices(text: str) -> dict[str, dict[tuple[str, str], float | None]]:
    """Parse R-printed (possibly column-wrapped) matrices into section dicts."""
    sections: dict[str, dict[tuple[str, str], float | None]] = {}
    current = None
    lines = text.splitlines()
    row_labels: set[str] = set()
    for line in lines:  # first pass: every row label anywhere
        m = ROW_RE.match(line)
        if m and m.group(1).strip() and not line.startswith(" "):
            row_labels.add(m.group(1).strip())
    header: list[str] = []
    for line in lines:
        if line.startswith("===") or re.match(r"^Row \d+", line):
            current = line.strip("= ").split(" (")[0]
            sections.setdefault(current, {})
            header = []
            continue
        if current is None or not line.strip():
            continue
        if line.startswith(" "):  # a header line: split by known labels
            rest, header = line.strip(), []
            while rest:
                label = max((lab for lab in row_labels if rest.startswith(lab)),
                            key=len, default=None)
                if label is None:
                    break
                header.append(label)
                rest = rest[len(label):].strip()
            continue
        m = ROW_RE.match(line)
        if m and header:
            values = m.group(2).split()
            for col, value in zip(header, values):
                sections[current][(m.group(1).strip(), col)] = (None if value == "NA"
                                                                else float(value))
    return sections


def dye() -> dict:
    """Compare attempt-01 printed matrices with attempt-02 per-cell evidence."""
    a1 = OUT / "dye-et-al-2023/reproduction/attempt-01/outputs/summary-stats.txt"
    a2 = OUT / "dye-et-al-2023/reproduction/attempt-02/comparisons/values"
    sections = parse_r_matrices(a1.read_text(encoding="utf-8"))
    rows_map = {f"T{12 + i}": f"Row {i + 1}" for i in range(9)}
    result: dict = {"supplement_tables": {}, "section7_oFD": {}}
    total = diffs = notfound = 0
    detail = []
    for target, row in rows_map.items():
        path = next(a2.glob(f"{target}-*.csv"))
        for rec in csv.DictReader(path.open()):
            if rec.get("kind") != "cell":
                continue
            total += 1
            old = sections.get(row, {}).get((rec["row"], rec["col"]))
            # Use attempt-02's own R-rounded value: both attempts round in R,
            # and Python's round() disagrees on binary ties (0.065 -> 0.07 in
            # Python, 0.06 in R; caught 2026-10-03 as a false difference).
            new = float(rec["reproduced_round2"])
            if old is None:
                notfound += 1
                detail.append([target, rec["row"], rec["col"], None, new])
            elif old != new:
                diffs += 1
                detail.append([target, rec["row"], rec["col"], old, new])
    result["supplement_tables"] = {"cells_compared": total, "cells_differing": diffs,
                                   "cells_not_found_in_attempt01": notfound,
                                   "detail": detail}
    stable = sections.get("Stable Solid Branching", {})
    compared = differing = 0
    for rec in csv.DictReader((a2 / "T06-section-07-full-matrix.csv").open()):
        old = stable.get((rec["ancestor_row"], rec["descendant_col"]))
        if old is None:
            continue
        compared += 1
        if round(old, 2) != float(rec["p_oFD_round2"]):
            differing += 1
    result["section7_oFD"] = {"cells_compared": compared, "cells_differing": differing}
    return result


def main() -> int:
    """Run both comparisons, write regression-value-check.json, print a summary."""
    report = {"check": "regression criterion check 2 (value identity)", "version": "1.0",
              "herskind-riede-2024": herskind(), "dye-et-al-2023": dye()}
    out = HERE / "regression-value-check.json"
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in report.items() if k != "dye-et-al-2023"}, indent=1)[:2500])
    d = report["dye-et-al-2023"]
    print("dye supplement tables:", {k: v for k, v in d["supplement_tables"].items()
                                     if k != "detail"}, "| section 7 oFD:", d["section7_oFD"])
    print(f"wrote {out.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
