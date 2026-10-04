#!/usr/bin/env python3
"""API-equivalent cost of the gate-eligible arms, counted once per request.

D4 arm-choice input (gates ruling, 2026-10-04). Amendment 1 §3 selects the
cheapest gate-eligible arm, "evaluated at selection time from the provider's
published per-token prices". This script prices each eligible arm's benchmark
spawns from their transcripts. Usage is counted once per API request
(`transcript_usage()` in `scripts/reproduction-lane.py`, the F-013 fix),
never per transcript entry, because the per-entry contract metric over-counts
by 1.9-2.9x in a model-dependent way.

Each request is priced by the model that actually served it. The scoring
spawns are the arm's model. The reconciliation spawns run on Haiku 4.5 in
every arm, so they are reported separately and do not bear on the choice.

Prices (USD per million tokens) come from the claude-api skill's model table
(cached 2026-09-25), with cache writes at 1.25x input (5-minute TTL) or 2x
(1-hour TTL) and cache reads at 0.1x input:

- claude-opus-5: input 5, output 25.
- claude-haiku-4-5: input 1, output 5.

The transcripts sit outside the repository, in the harness's per-session
directory. Pass different paths with --arm if they move into the archive.

Usage:
    python3 selection-cost.py            # default arms and paths
    python3 selection-cost.py --json out.json
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[5]
VALIDATION = REPO / "studies/open-science-compliance/outputs/validation"
PROJECTS = Path.home() / ".claude/projects/-home-shawn-Code-llm-reproducibility"

# Arm label -> (run-record directory, workflow transcript directory).
DEFAULT_ARMS = {
    "opus-5 (xhigh)": (
        VALIDATION / "benchmark-2026-08-17/arm-opus-5",
        PROJECTS / "6e8352ed-2013-4674-8720-85245d97fbc7/subagents/workflows/wf_67cd3484-a08",
    ),
    "opus-5 (high)": (
        VALIDATION / "effort-study-2026-08-17/arm-opus-5-high",
        PROJECTS / "f605c78a-e90b-4d9d-bbec-1fd3903ced31/subagents/workflows/wf_d691e836-2f2",
    ),
}

# Published prices, USD per million tokens.
PRICES = {
    "claude-opus-5": {"input": 5.0, "output": 25.0},
    "claude-haiku-4-5": {"input": 1.0, "output": 5.0},
}
WRITE_5M, WRITE_1H, READ = 1.25, 2.0, 0.1  # multipliers on the input price


def load_lane():
    """Import scripts/reproduction-lane.py (hyphenated, so not importable by name)."""
    spec = importlib.util.spec_from_file_location("lane", REPO / "scripts/reproduction-lane.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def price_key(models: set[str]) -> str:
    """Map the model ids seen in one transcript to a price-table key."""
    joined = " ".join(sorted(models))
    if "opus-5" in joined and "opus-5-5" not in joined:
        return "claude-opus-5"
    if "haiku-4-5" in joined:
        return "claude-haiku-4-5"
    raise ValueError(f"no price for models {sorted(models)}")


def cost(tokens: dict[str, int], key: str) -> float:
    """API-equivalent USD for summed per-request usage under one price row."""
    p = PRICES[key]
    return (tokens["input_tokens"] * p["input"]
            + tokens["output_tokens"] * p["output"]
            + tokens["cache_write_5m"] * p["input"] * WRITE_5M
            + tokens["cache_write_1h"] * p["input"] * WRITE_1H
            + tokens["cache_read_input_tokens"] * p["input"] * READ) / 1e6


def price_arm(lane, record_dir: Path, transcript_dir: Path) -> dict:
    """Sum per-request usage and cost over an arm's recorded spawns, by model."""
    record = json.loads((record_dir / "run-record.json").read_text(encoding="utf-8"))
    ids = {s["agent_id"] for s in record["spawns"]}
    fields = ("input_tokens", "output_tokens", "cache_write_5m", "cache_write_1h",
              "cache_read_input_tokens")
    by_model: dict[str, dict] = defaultdict(lambda: {"spawns": 0, **{f: 0 for f in fields}})
    matched = set()
    for path in sorted(transcript_dir.rglob("*.jsonl")):
        hit = [i for i in ids if i in path.name]
        if not hit:
            continue
        matched.update(hit)
        usage = lane.transcript_usage(path.read_text(encoding="utf-8").splitlines())
        models = usage["models"]
        key = price_key(set(models.values() if isinstance(models, dict) else models))
        row = by_model[key]
        row["spawns"] += 1
        for f in fields:
            row[f] += usage[f]
    if matched != ids:
        raise SystemExit(f"{record_dir.name}: {len(ids - matched)} spawn transcripts missing")
    for key, row in by_model.items():
        row["usd"] = round(cost(row, key), 2)
    return dict(by_model)


def main() -> None:
    """Price every arm and print (optionally write) the comparison."""
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--json", type=Path, help="write the results as JSON")
    args = ap.parse_args()
    lane = load_lane()
    results = {arm: price_arm(lane, rec, wd) for arm, (rec, wd) in DEFAULT_ARMS.items()}
    for arm, rows in results.items():
        for key, row in sorted(rows.items()):
            print(f"{arm:15} {key:17} spawns={row['spawns']:2} out={row['output_tokens']:>8,} "
                  f"write5m={row['cache_write_5m']:>9,} read={row['cache_read_input_tokens']:>10,}"
                  f" ${row['usd']:.2f}")
    if args.json:
        args.json.write_text(json.dumps({"prices_usd_per_mtok": PRICES,
                                         "multipliers": {"write_5m": WRITE_5M,
                                                         "write_1h": WRITE_1H,
                                                         "read": READ},
                                         "arms": results}, indent=1) + "\n",
                             encoding="utf-8")


if __name__ == "__main__":
    main()
