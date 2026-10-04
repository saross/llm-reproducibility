#!/usr/bin/env python3
"""Replay per-request token usage into committed FAIR arm records (F-013).

**Version:** 1.0 (2026-10-04)

Register F-013 (ruled 2026-10-04): the arm assembler up to v1.5 summed
``message.usage`` once per transcript entry, but the harness repeats a
response's usage on every content block, so ``usage_contract_metric``
over-counts by 1.9-2.9x, depending on the model. The ruling keeps every
recorded value (no-verifier-wins) and adds corrected values beside it.

For each arm record, this script recounts every spawn's transcript with
assembler v1.6's ``transcript_tokens`` (once per API request) and writes:

- ``spawns[i].usage_per_request``, beside the untouched ``spawns[i].usage``;
- a top-level ``usage_per_request`` block, beside the untouched
  ``usage_contract_metric``, recording the method and replay date.

Transcripts are located under the harness's per-session directories by
workflow run id (the record's ``workflow_run_id`` plus ``extra_run_dirs``).
A spawn whose transcript cannot be found is a hard error, and nothing is
written.

Usage:
    venv/bin/python scripts/replay-arm-usage.py            # dry run: print totals
    venv/bin/python scripts/replay-arm-usage.py --write    # write the records
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
VALIDATION = REPO / "studies/open-science-compliance/outputs/validation"
PROJECTS = Path.home() / ".claude/projects/-home-shawn-Code-llm-reproducibility"

ARM_RECORDS = [
    "benchmark-2026-08-17/arm-sonnet-5",
    "benchmark-2026-08-17/arm-opus-5",
    "benchmark-2026-08-17/arm-fable-5",
    "effort-study-2026-08-17/arm-sonnet-5-high",
    "effort-study-2026-08-17/arm-sonnet-5-max",
    "effort-study-2026-08-17/arm-opus-5-high",
]


def load_assembler():
    """Import scripts/assemble-arm-record.py (hyphenated filename)."""
    spec = importlib.util.spec_from_file_location(
        "assemble_arm_record", REPO / "scripts/assemble-arm-record.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_dirs(record: dict) -> list[Path]:
    """Transcript directories for a record's workflow run and its extras."""
    dirs = []
    for run_id in [record["workflow_run_id"], *record.get("extra_run_dirs", [])]:
        found = sorted(PROJECTS.glob(f"*/subagents/workflows/{run_id}"))
        if len(found) != 1:
            raise SystemExit(f"{run_id}: expected one transcript directory, found {len(found)}")
        dirs.append(found[0])
    return dirs


def replay(assembler, arm_dir: Path) -> tuple[dict, dict]:
    """Return (updated record, per-request arm totals) for one arm record."""
    path = arm_dir / "run-record.json"
    record = json.loads(path.read_text(encoding="utf-8"))
    transcripts = {t.stem.replace("agent-", ""): t
                   for d in run_dirs(record) for t in d.glob("agent-*.jsonl")}
    keys = ("input_tokens", "output_tokens", "cache_creation_input_tokens",
            "cache_read_input_tokens", "contract_metric_tokens", "api_requests")
    totals = dict.fromkeys(keys, 0)
    for spawn in record["spawns"]:
        transcript = transcripts.get(spawn["agent_id"])
        if transcript is None:
            raise SystemExit(f"{arm_dir.name}: no transcript for spawn {spawn['agent_id']}")
        usage = assembler.transcript_tokens(
            transcript.read_text(encoding="utf-8").splitlines())
        spawn["usage_per_request"] = {k: usage[k] for k in keys}
        for k in keys:
            totals[k] += usage[k]
    record["usage_per_request"] = {
        "definition": "input+output+cache_creation (contract_metric_tokens) and "
                      "component fields, counted once per API request over "
                      "every spawn in this record (assembler v1.6 "
                      "transcript_tokens); usage_contract_metric is the "
                      "recorded per-entry value, kept unchanged (F-013)",
        "replayed": date.today().isoformat(),
        "method": "scripts/replay-arm-usage.py v1.0",
        **totals,
    }
    return record, totals


def main() -> int:
    """Replay every arm record; write only with --write."""
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--write", action="store_true", help="write the updated records")
    args = ap.parse_args()
    assembler = load_assembler()
    for rel in ARM_RECORDS:
        arm_dir = VALIDATION / rel
        record, totals = replay(assembler, arm_dir)
        recorded = record["usage_contract_metric"]["contract_metric_tokens"]
        ratio = recorded / totals["contract_metric_tokens"]
        print(f"{rel:42} spawns={len(record['spawns']):2} requests={totals['api_requests']:5} "
              f"per-request={totals['contract_metric_tokens']:>11,} "
              f"recorded={recorded:>11,} ratio={ratio:.2f}")
        if args.write:
            (arm_dir / "run-record.json").write_text(
                json.dumps(record, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    if not args.write:
        print("dry run: nothing written (use --write)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
