#!/usr/bin/env python3
"""Assemble one benchmark arm's committed artefact set (D3 run contract H6).

**Version:** 1.0

From a completed arm workflow's transcript directory, produce the committed
arm directory: per-run score payloads (`run-<N>/<slug>.json` — the only
input to stability, audit F9), the authoritative reconciliation report and
gate/push log slices (audit F10), and `run-record.json` carrying per-spawn
identity, receipts, and the contract-defined spend recount (transcript
tokens excluding cache reads — hardening H4's reproducible unit).

Usage:
    venv/bin/python scripts/assemble-arm-record.py <run_dir> <arm> <out_dir>
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

# The prompt sits inside a JSON string in the transcript, so the newline
# appears as an escaped \n two-character sequence; accept both forms.
PROMPT_RE = re.compile(r"arm (\S+), run (\d) of 3\)\.(?:\\n|\n)Paper: ([A-Za-z0-9-]+)\.")


def transcript_payload(lines: list[str]) -> dict | None:
    """Last StructuredOutput tool_use input in a transcript."""
    payload = None
    for line in lines:
        try:
            entry = json.loads(line)
        except json.JSONDecodeError:
            continue
        content = ((entry.get("message") or {}).get("content")
                   if isinstance(entry.get("message"), dict) else None)
        if not isinstance(content, list):
            continue
        for blk in content:
            if isinstance(blk, dict) and blk.get("type") == "tool_use" \
                    and blk.get("name") == "StructuredOutput":
                payload = blk.get("input")
    return payload


def transcript_identity(text: str) -> tuple[str, int, str] | None:
    """(arm, run, slug) parsed from the scoring prompt."""
    match = PROMPT_RE.search(text)
    if not match:
        return None
    return match.group(1), int(match.group(2)), match.group(3)


def transcript_tokens(lines: list[str]) -> dict:
    """Contract H4 spend metric: sum usage excluding cache_read_input_tokens."""
    totals = {"input_tokens": 0, "output_tokens": 0,
              "cache_creation_input_tokens": 0, "cache_read_input_tokens": 0}
    for line in lines:
        try:
            entry = json.loads(line)
        except json.JSONDecodeError:
            continue
        usage = ((entry.get("message") or {}).get("usage")
                 if isinstance(entry.get("message"), dict) else None)
        if isinstance(usage, dict):
            for key in totals:
                value = usage.get(key)
                if isinstance(value, (int, float)):
                    totals[key] += int(value)
    totals["contract_metric_tokens"] = (totals["input_tokens"]
                                        + totals["output_tokens"]
                                        + totals["cache_creation_input_tokens"])
    return totals


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("run_dir", type=Path)
    parser.add_argument("arm")
    parser.add_argument("out_dir", type=Path)
    args = parser.parse_args()
    run_dir = args.run_dir.expanduser().resolve()
    out_dir = args.out_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    report_path = run_dir / "reconciliation-authoritative" / "reconciliation-report.json"
    if not report_path.is_file():
        print(f"ERROR: authoritative reconciliation missing: {report_path}",
              file=sys.stderr)
        return 1
    report = json.loads(report_path.read_text())
    if not report.get("clean"):
        print("ERROR: authoritative reconciliation is not clean — "
              "assembly refused (contract hardening 1)", file=sys.stderr)
        return 1

    spawns = []
    arm_tokens = {"input_tokens": 0, "output_tokens": 0,
                  "cache_creation_input_tokens": 0,
                  "cache_read_input_tokens": 0, "contract_metric_tokens": 0}
    payload_count = 0
    for transcript in sorted(run_dir.glob("agent-*.jsonl")):
        agent_id = transcript.stem.replace("agent-", "")
        meta_path = run_dir / f"{transcript.stem}.meta.json"
        meta = json.loads(meta_path.read_text()) if meta_path.is_file() else {}
        text = transcript.read_text(encoding="utf-8")
        lines = text.splitlines()
        tokens = transcript_tokens(lines)
        for key in arm_tokens:
            arm_tokens[key] += tokens[key]
        agent_type = str(meta.get("agentType") or "")
        record = {"agent_id": agent_id, "agent_type": agent_type,
                  "usage": tokens}
        if agent_type.startswith("fair-assessor-"):
            identity = transcript_identity(text)
            payload = transcript_payload(lines)
            if identity is None or payload is None:
                print(f"ERROR: scoring transcript {agent_id} lacks identity "
                      f"or payload", file=sys.stderr)
                return 1
            _, run, slug = identity
            record.update({"run": run, "slug": slug,
                           "status": payload.get("status")})
            run_out = out_dir / f"run-{run}"
            run_out.mkdir(exist_ok=True)
            (run_out / f"{slug}.json").write_text(
                json.dumps(payload, indent=1, sort_keys=True) + "\n")
            payload_count += 1
        spawns.append(record)

    if payload_count != 15:
        print(f"ERROR: expected 15 score payloads, wrote {payload_count}",
              file=sys.stderr)
        return 1

    recon_out = out_dir / "reconciliation"
    recon_out.mkdir(exist_ok=True)
    for name in ("reconciliation-report.json", "gate-log-slice.jsonl",
                 "push-log-slice.jsonl"):
        source = run_dir / "reconciliation-authoritative" / name
        if source.is_file():
            shutil.copy2(source, recon_out / name)

    receipted = [a["receipts"].get("receipted") for a in report["agents"]]
    model_ids = sorted({r["model_id"] for r in receipted if r})
    record = {
        "arm": args.arm,
        "workflow_run_id": run_dir.name,
        "assembled_at": datetime.now(timezone.utc).isoformat(),
        "spawns": spawns,
        "score_payloads": payload_count,
        "model_ids_receipted": model_ids,
        "reconciliation": {
            "clean": report["clean"],
            "spawns": report["spawns"],
            "spawns_reconciled": report["spawns_reconciled"],
            "skipped_ungoverned": len(report.get("skipped_ungoverned", [])),
            "report": "reconciliation/reconciliation-report.json",
        },
        "usage_contract_metric": {
            "definition": "sum of transcript usage input+output+cache_creation, "
                          "excluding cache_read_input_tokens, over all arm "
                          "spawns (D3 contract hardening 4)",
            **arm_tokens,
        },
    }
    (out_dir / "run-record.json").write_text(
        json.dumps(record, indent=1, sort_keys=True) + "\n")
    print(f"arm {args.arm}: {payload_count} payloads, "
          f"{record['usage_contract_metric']['contract_metric_tokens']:,} "
          f"contract-metric tokens -> {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
