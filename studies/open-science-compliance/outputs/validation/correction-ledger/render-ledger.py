#!/usr/bin/env python3
"""Render the correction-ledger JSON as a Markdown review document.

Purpose
-------
The ledger's JSON (``correction-ledger.json``) is the artefact that will be
ruled, frozen, and hashed (amendment 3 §9). This script renders it as
``correction-ledger.md`` so the registrant can review it target by target.
The Markdown is derived output: edit the JSON, never the Markdown, and
re-render.

Usage
-----
    python3 render-ledger.py [--ledger correction-ledger.json]
                             [--out correction-ledger.md]

Requires: Python 3.10+ (standard library only).
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def esc(value: object) -> str:
    """Make a value safe inside a Markdown table cell."""
    text = "" if value is None else str(value)
    return text.replace("|", "\\|").replace("\n", " ")


def render_target(t: dict) -> list[str]:
    """Render one target as a Markdown subsection.

    Args:
        t: a target record from the ledger.

    Returns:
        Lines of Markdown.
    """
    corr = t.get("correction", {})
    lines = [f"#### {t['id']} — {t['display_item']}", ""]
    loc = t.get("location", {})
    where = loc.get("source", "")
    if loc.get("page_pdf"):
        where += f", PDF p. {loc['page_pdf']}"
    if loc.get("page_printed"):
        where += f" (printed p. {loc['page_printed']})"
    rows = [
        ("Pilot item", t.get("pilot_item")),
        ("Location", where),
        ("Analysis type", t.get("analysis_type")),
        ("Gate scope", t.get("gate_scope")),
        ("Elements", "; ".join(f"{k}: {v}" for k, v in t.get("element_count", {}).items())),
        ("Tolerance", f"{t['tolerance'].get('category')} (basis: "
                      f"{t['tolerance'].get('basis')})"),
        ("Pilot outcome", t["pilot"].get("outcome")),
        ("Set", corr.get("set")),
        ("Correction", corr.get("what")),
        ("Scope change", corr.get("scope_change")),
        ("Printed value corrected", corr.get("printed_value_corrected")),
        ("Corrected expected value", corr.get("corrected_expected")),
        ("Evidence tier", corr.get("evidence_tier")),
        ("Ruling", corr.get("ruling")),
        ("Caveat", corr.get("caveat")),
        ("Repair class and status", "; ".join(t["repair"].get("findings", []))
         + f". Status: {t['repair'].get('status')}"),
        ("Credit eligibility", f"pilot: {t['credit_eligibility'].get('pilot')}; gate: "
                               f"{t['credit_eligibility'].get('gate')}"),
        ("Coverage", f"expected-untestable: {t['coverage'].get('expected_untestable')}; "
                     f"comparison: {t['coverage'].get('comparison')}"),
        ("Expected outcome", t.get("expected_outcome")),
        ("Rulings needed", ", ".join(t.get("rulings", [])) or "none"),
        ("Note", t.get("note")),
    ]
    lines += ["| Field | Value |", "|---|---|"]
    lines += [f"| {k} | {esc(v)} |" for k, v in rows if v not in (None, "", [])]
    lines.append("")
    els = t.get("elements", [])
    if els:
        lines += ["| Element | Printed | Page | Pilot value | Pilot outcome | Expected | "
                  "Expected outcome |", "|---|---|---|---|---|---|---|"]
        for e in els:
            lines.append("| " + " | ".join(esc(x) for x in (
                e["label"], e["printed"], e.get("page_pdf"), e.get("pilot_value"),
                e.get("pilot_outcome"), e.get("expected"),
                e.get("expected_outcome") or e.get("rebased_outcome"))) + " |")
        lines.append("")
    if t.get("elements_reference"):
        ref = t["elements_reference"]
        lines += [f"Elements by reference: {esc(ref.get('file'))}, sha256 "
                  f"`{ref.get('sha256')}`. {esc(ref.get('v1_identity', ''))}", ""]
    return lines


def render(ledger: dict) -> str:
    """Render the whole ledger.

    Args:
        ledger: the parsed ledger JSON.

    Returns:
        The Markdown document as a string.
    """
    out = [f"# {ledger['title']}", "",
           f"**Status:** {ledger['status']}", "",
           f"**Ledger version:** {ledger['ledger_version']}. **Drafted:** "
           f"{ledger['drafted']['date']} by {ledger['drafted']['by']}.", "",
           "This file is rendered from `correction-ledger.json` by `render-ledger.py`. "
           "Edit the JSON, never this file.", "",
           "## Summary by paper", "",
           "| Paper | Pilot verdict | Expected verdict | In-gate targets | Unchanged "
           "(testable) | Corrected | Scope-changed | Expected-untestable | Outside the "
           "gate or conditional | Gate role |",
           "|---|---|---|---|---|---|---|---|---|---|"]
    for p in ledger["papers"]:
        s = p["sets"]
        out.append("| " + " | ".join(esc(x) for x in (
            p["slug"], p["pilot"]["verdict"], p["expected_verdict"]["verdict"],
            s["in_gate"], f"{s['unchanged']} ({s['unchanged_testable']})", s["corrected"],
            s["scope_changed"], s["expected_untestable"], s["not_in_gate"],
            p["gate_role"])) + " |")
    out += ["", "## Rulings needed", ""]
    for r in ledger["rulings_needed"]:
        out += [f"### {r['id']}. {r['question']}", ""]
        out += [f"- **{o['key']}** {o['text']}" for o in r["options"]]
        out += ["", f"**Recommendation:** {r['recommendation']}", ""]
        if r.get("affects"):
            out += [f"Affects: {', '.join(r['affects'])}.", ""]
    out += ["## Definitions", ""]
    out += [f"- **{k}:** {v}" for k, v in ledger["definitions"].items()]
    out.append("")
    for p in ledger["papers"]:
        out += [f"## {p['slug']}", "", p["citation"], ""]
        dep = p["sources"].get("selected_deposit", {})
        out += [f"- **Selected (AP-12) version:** {esc(dep.get('ap12_version'))}"
                + (f", {dep['doi']}" if dep.get("doi") else "")]
        if dep.get("archive"):
            out.append(f"- **Deposit archive:** sha256 `{dep['archive']['sha256']}`; "
                       f"{esc(dep['archive'].get('verified'))}")
        for f in dep.get("files", []):
            out.append(f"- `{f['path']}`: sha256 `{f['sha256']}`"
                       + (f" ({esc(f['note'])})" if f.get("note") else ""))
        out += [f"- **Pilot:** {p['pilot']['attempt']}, verdict {p['pilot']['verdict']}; "
                f"executed {esc(p['pilot']['executed_version'])}; audit findings "
                f"{', '.join(p['pilot']['audit_findings'])}.",
                f"- **Expected verdict:** {p['expected_verdict']['verdict']}. "
                f"{esc(p['expected_verdict']['derivation'])}", ""]
        out += ["### Targets", ""]
        for t in p["targets"]:
            out += render_target(t)
        if p.get("excluded_pilot_items"):
            out += ["### Pilot items excluded from the target list", "",
                    "| Pilot item | Reason | Ruling |", "|---|---|---|"]
            out += [f"| {esc(x['pilot_item'])} | {esc(x['reason'])} | "
                    f"{esc(x.get('ruling', ''))} |" for x in p["excluded_pilot_items"]]
            out.append("")
        if p.get("notes"):
            out += ["### Notes", ""] + [f"- {esc(n)}" for n in p["notes"]] + [""]
    return "\n".join(out).rstrip() + "\n"


def main() -> None:
    """Parse arguments and write the Markdown."""
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--ledger", type=Path, default=HERE / "correction-ledger.json")
    ap.add_argument("--out", type=Path, default=HERE / "correction-ledger.md")
    a = ap.parse_args()
    ledger = json.loads(a.ledger.read_text(encoding="utf-8"))
    a.out.write_text(render(ledger), encoding="utf-8")
    print(f"wrote {a.out}")


if __name__ == "__main__":
    main()
