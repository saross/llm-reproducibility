#!/usr/bin/env python3
"""Replay every committed reconciliation under reconcile-run v1.5 (path rule).

**Purpose (F-010 ruling, 2026-08-29):** the v1.5 path rule changes what an
enumeration (Glob/Grep) access means. Before the rule is relied on, every
committed reconciliation report is re-derived from its original transcript
directory under the new tool and compared with the committed verdicts. The
committed reports are never modified (no-verifier-wins): new reports are
written beside this script, and any verdict flip is a finding to adjudicate,
not a silent update.

Usage (from the repository root):

    venv/bin/python studies/open-science-compliance/outputs/validation/\
reconcile-v1.5-replay-2026-08-29/replay.py

Inputs: every `*reconciliation-report.json` under `outputs/validation/` whose
`run_dir` still exists locally. Flags are inferred per report: post-D3-prep
reports (tool 1.2+, packs declared) replay with `--require-pack` and the
registered contract schema; earlier reports replay with defaults. Receipts
are re-validated against the **manifest of the commit that added the
report** (`git show <commit>:manifest.yaml`), so a spawn scored under
instrument v2.0 / agent v1.0 is not judged against today's registrations —
the receipt layer is untouched by v1.5 and is expected to reproduce exactly.
Gate/push logs come from the committed log slices where present, else the
live hook logs. Outputs: `<cycle>/<arm>/<name>-report.json` per replayed
report and `replay-summary.md` (per-spawn comparison table).

A *flip* is a change in a spawn's `reconciled` verdict or in whether it has
any contaminating access; a contaminating set that is merely re-described
(v1.4 recorded a Glob's base path, v1.5 records root + pattern + returned
paths) is reported as such, not as a flip.
"""

from __future__ import annotations

import importlib.machinery
import importlib.util
import json
import subprocess
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[4]
VALIDATION = HERE.parent
SCRIPT = REPO_ROOT / "scripts" / "reconcile-run.py"
CONTRACT = REPO_ROOT / "assessment-system" / "schema" / "benchmark-fair-output-schema.json"
HOOKS = REPO_ROOT / ".claude" / "hooks"

_spec = importlib.util.spec_from_loader(
    "reconcile_run", importlib.machinery.SourceFileLoader("reconcile_run", str(SCRIPT)))
reconciler = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(reconciler)


def committed_reports() -> list[Path]:
    """Every committed reconciliation report outside this replay directory."""
    return sorted(p for p in VALIDATION.rglob("*reconciliation-report.json")
                  if HERE not in p.parents)


def describe(access: dict) -> str:
    """One access as `tool root [pattern]`; an empty root is the repo root."""
    root = access["target"] or "(repo root)"
    pattern = access.get("pattern")
    return f"{access['tool']} {root}" + (f" [{pattern}]" if pattern else "")


def access_summary(agent: dict) -> dict:
    """The verdict-bearing parts of one spawn's record."""
    return {
        "reconciled": agent["reconciled"],
        "receipts_valid": agent["receipts"]["valid"],
        "receipt_problems": sorted(agent["receipts"].get("problems") or []),
        "contaminating": sorted(describe(a) for a in agent["file_access"]["contaminating"]),
        "unscoped": sorted(describe(a) for a in agent["file_access"].get("unscoped", [])),
    }


def vintage_manifest(report_path: Path) -> tuple[str, dict]:
    """The manifest as registered when this report was first committed."""
    commit = subprocess.run(
        ["git", "log", "--diff-filter=A", "--format=%h", "--", str(report_path)],
        cwd=REPO_ROOT, capture_output=True, text=True, check=True).stdout.split()[-1]
    text = subprocess.run(["git", "show", f"{commit}:manifest.yaml"], cwd=REPO_ROOT,
                          capture_output=True, text=True, check=True).stdout
    return commit, yaml.safe_load(text) or {}


def replay_one(report_path: Path) -> dict:
    """Re-run reconciliation for one committed report; return the comparison."""
    committed = json.loads(report_path.read_text(encoding="utf-8"))
    run_dir = Path(committed["run_dir"])
    commit, manifest = vintage_manifest(report_path)
    prefix = report_path.name.replace("reconciliation-report.json", "")
    slice_dir = report_path.parent
    gate_log = slice_dir / f"{prefix}gate-log-slice.jsonl"
    push_log = slice_dir / f"{prefix}push-log-slice.jsonl"
    if not gate_log.is_file():
        gate_log = HOOKS / "receipt-gate-log.jsonl"
    if not push_log.is_file():
        push_log = HOOKS / "push-receipts.jsonl"
    packs_era = any(reconciler.declared_pack(
        t.read_text(encoding="utf-8").splitlines()) for t in run_dir.glob("agent-*.jsonl"))
    contract = json.loads(CONTRACT.read_text(encoding="utf-8")) if packs_era else None
    report = reconciler.reconcile(
        run_dir, reconciler.DEFAULT_ALLOWED_PREFIXES, gate_log, push_log,
        manifest=manifest, expect_spawns=committed["spawns"],
        require_pack=packs_era, contract_schema=contract)
    rel = report_path.relative_to(VALIDATION)
    out_path = HERE / rel.parent / report_path.name.replace(
        "reconciliation-report.json", "v1.5-report.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(report, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
                        encoding="utf-8")
    old = {a["agent_id"]: access_summary(a) for a in committed["agents"]}
    new = {a["agent_id"]: access_summary(a) for a in report["agents"]}
    rows = []
    for agent_id in sorted(set(old) | set(new)):
        before, after = old.get(agent_id), new.get(agent_id)
        flip = (before is None or after is None
                or before["reconciled"] != after["reconciled"]
                or bool(before["contaminating"]) != bool(after["contaminating"]))
        redescribed = (not flip and before is not None and after is not None
                       and before["contaminating"] != after["contaminating"])
        receipts_changed = (before is not None and after is not None
                            and (before["receipts_valid"] != after["receipts_valid"]
                                 or before["receipt_problems"] != after["receipt_problems"]))
        rows.append({"agent_id": agent_id, "before": before, "after": after,
                     "flip": flip, "redescribed": redescribed,
                     "receipts_changed": receipts_changed})
    return {"report": str(rel), "run_dir": str(run_dir), "packs_era": packs_era,
            "gate_log": str(gate_log.relative_to(REPO_ROOT)),
            "manifest_commit": commit,
            "committed_version": committed["reconciliation_version"],
            "committed_clean": committed["clean"], "replay_clean": report["clean"],
            "rows": rows, "out": str(out_path.relative_to(REPO_ROOT))}


def main() -> int:
    results = [replay_one(p) for p in committed_reports()]
    lines = ["# reconcile-run v1.5 replay — comparison with committed reports", "",
             "Generated by `replay.py` (this directory). Committed reports untouched.",
             "A **FLIP** is a spawn whose `reconciled` verdict, or whether it has any",
             "contaminating access, differs between the committed report and the v1.5",
             "replay; *re-described* means the same contamination verdict now names",
             "root + pattern + returned paths instead of the v1.4 base path. Receipts",
             "are re-validated against the manifest of the report's own commit.", ""]
    total = flips = redescribed = receipt_changes = 0
    for res in results:
        n_flip = sum(r["flip"] for r in res["rows"])
        n_re = sum(r["redescribed"] for r in res["rows"])
        n_rc = sum(r["receipts_changed"] for r in res["rows"])
        total += len(res["rows"])
        flips += n_flip
        redescribed += n_re
        receipt_changes += n_rc
        lines += [f"## `{res['report']}`", "",
                  f"- committed tool stamp v{res['committed_version']}, "
                  f"clean={res['committed_clean']}; "
                  f"replay clean={res['replay_clean']}; spawns {len(res['rows'])}; "
                  f"flips {n_flip}; re-described {n_re}; receipt-verdict changes {n_rc}; "
                  f"packs-era={res['packs_era']}; manifest @ `{res['manifest_commit']}`; "
                  f"gate log `{res['gate_log']}`",
                  f"- replay report: `{res['out']}`", ""]
        for row in res["rows"]:
            b, a = row["before"], row["after"]
            if row["flip"] or row["redescribed"] or row["receipts_changed"] \
                    or (a and (a["contaminating"] or a["unscoped"])):
                lines += [f"- `{row['agent_id']}` — before: reconciled={b and b['reconciled']} "
                          f"contaminating={b and b['contaminating']}; after: "
                          f"reconciled={a and a['reconciled']} "
                          f"contaminating={a and a['contaminating']} "
                          f"unscoped={a and a['unscoped']}"
                          + (" **FLIP**" if row["flip"] else "")
                          + (" *(re-described)*" if row["redescribed"] else "")
                          + (f" (receipt problems before {b['receipt_problems']} / after "
                             f"{a['receipt_problems']})" if row["receipts_changed"] else "")]
        lines.append("")
    lines += ["## Totals", "",
              f"- reports replayed: {len(results)}; spawns compared: {total}; "
              f"verdict flips: {flips}; re-described: {redescribed}; "
              f"receipt-verdict changes: {receipt_changes}", ""]
    (HERE / "replay-summary.md").write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines[-3:]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
