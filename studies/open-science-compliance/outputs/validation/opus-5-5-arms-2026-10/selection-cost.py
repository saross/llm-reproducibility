#!/usr/bin/env python3
"""API-equivalent cost of the gate-eligible arms, Opus 5.5 block (2026-10).

Selection input for the Opus 5.5 validation arms (design note Q4). It
extends `../gates-ruling-2026-10-04/selection-cost.py`, which stays as the
committed record behind the 2026-10-04 ruling, in three ways:

1. **An Opus 5.5 price row.** `claude-opus-5-5` costs $4 / $20 per million
   tokens.
2. **A per-model cache-read multiplier.** Cache reads are 0.05x input on
   Opus 5.5 ($0.20 per million tokens) and 0.1x on Opus 5 and Haiku 4.5.
   Cache writes are 1.25x input (5-minute TTL) or 2x (1-hour TTL) on every
   model.
3. **Bounds for unpersisted final usage** (register candidate, 2026-10-04).
   The harness writes one transcript entry per content block. Usually the
   last one carries the request's final `usage` and a `stop_reason`, but
   in some requests no entry does. Every entry then holds the
   streaming-start snapshot, so `output_tokens` is a placeholder (often
   8), while input and cache fields are already final. This script counts
   those requests and re-prices each arm three ways:
   - `recorded`: the transcript figures as they stand, a lower bound;
   - `central`: each affected request's output imputed as the median
     output of complete requests of the same model and kind (a
     `StructuredOutput` request, or any other) in the same arm;
   - `upper`: the same, but at the maximum of those complete requests.

Usage is counted once per API request, never per transcript entry, taking
each field's maximum within a request. That is `transcript_usage()` in
`scripts/reproduction-lane.py` (the F-013 fix), which this script imports
and uses to cross-check its own per-request parse.

Prices (USD per million tokens) come from the claude-api skill's model table
and prompt-caching notes (cached 2026-09-25): Opus 5 $5 / $25, Opus 5.5
$4 / $20, Haiku 4.5 $1 / $5.

Usage:
    python3 selection-cost.py            # default arms and paths
    python3 selection-cost.py --json out.json
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import statistics
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[5]
VALIDATION = REPO / "studies/open-science-compliance/outputs/validation"
ARMS_DIR = VALIDATION / "opus-5-5-arms-2026-10"
PROJECTS = Path.home() / ".claude/projects/-home-shawn-Code-llm-reproducibility"
THIS_SESSION = PROJECTS / "c5ee7a27-c9d0-4641-8bb3-6a5fdcc3ddce/subagents/workflows"

# Arm label -> (run-record directory, workflow transcript directory). The two
# registered opus-5 arms are the eligible registered configurations under the
# 2026-10-04 ruling (fable-5 is eligible but not selectable on price).
DEFAULT_ARMS = {
    "opus-5 (xhigh)": (
        VALIDATION / "benchmark-2026-08-17/arm-opus-5",
        PROJECTS / "6e8352ed-2013-4674-8720-85245d97fbc7/subagents/workflows/wf_67cd3484-a08",
    ),
    "opus-5 (high)": (
        VALIDATION / "effort-study-2026-08-17/arm-opus-5-high",
        PROJECTS / "f605c78a-e90b-4d9d-bbec-1fd3903ced31/subagents/workflows/wf_d691e836-2f2",
    ),
    "opus-5-5 (high)": (
        ARMS_DIR / "arm-opus-5-5-high",
        THIS_SESSION / "wf_965c388c-bfb",
    ),
    "opus-5-5 (medium)": (
        ARMS_DIR / "arm-opus-5-5-medium",
        THIS_SESSION / "wf_0f3600c3-5ef",
    ),
    "opus-5-5 (xhigh)": (
        ARMS_DIR / "arm-opus-5-5-xhigh",
        THIS_SESSION / "wf_3863b134-e26",
    ),
}

# Published prices, USD per million tokens, with each model's cache-read
# multiplier on its input price.
PRICES = {
    "claude-opus-5-5": {"input": 4.0, "output": 20.0, "read": 0.05},
    "claude-opus-5": {"input": 5.0, "output": 25.0, "read": 0.1},
    "claude-haiku-4-5": {"input": 1.0, "output": 5.0, "read": 0.1},
}
WRITE_5M, WRITE_1H = 1.25, 2.0  # multipliers on the input price, every model
FIELDS = ("input_tokens", "output_tokens", "cache_write_5m", "cache_write_1h",
          "cache_read_input_tokens")
STRUCTURED = "StructuredOutput"


def load_lane():
    """Import scripts/reproduction-lane.py (hyphenated, so not importable by name)."""
    spec = importlib.util.spec_from_file_location("lane", REPO / "scripts/reproduction-lane.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def price_key(models: set[str]) -> str:
    """Map the model ids seen in one transcript to a price-table key.

    Opus 5.5 is tested first, because "claude-opus-5" is a prefix of
    "claude-opus-5-5".
    """
    joined = " ".join(sorted(models))
    if "opus-5-5" in joined:
        return "claude-opus-5-5"
    if "opus-5" in joined:
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
            + tokens["cache_read_input_tokens"] * p["input"] * p["read"]) / 1e6


def parse_requests(lines: list[str]) -> list[dict]:
    """Per-request usage, mirroring `transcript_usage()`, plus completeness flags.

    Each request records its field maxima, whether any entry carries a
    `stop_reason` (`complete`), and whether it emits `StructuredOutput`.

    Args:
        lines: The transcript's JSONL lines.

    Returns:
        One dict per API request.
    """
    requests: dict[str, dict] = {}
    for index, line in enumerate(lines):
        try:
            entry = json.loads(line)
        except json.JSONDecodeError:
            continue
        message = entry.get("message")
        if not isinstance(message, dict) or not isinstance(message.get("usage"), dict):
            continue
        usage = message["usage"]
        key = str(entry.get("requestId") or message.get("id") or f"line-{index}")
        split = usage.get("cache_creation") if isinstance(usage.get("cache_creation"),
                                                          dict) else {}
        created = int(usage.get("cache_creation_input_tokens") or 0)
        one_hour = int(split.get("ephemeral_1h_input_tokens") or 0)
        values = {"input_tokens": int(usage.get("input_tokens") or 0),
                  "output_tokens": int(usage.get("output_tokens") or 0),
                  "cache_read_input_tokens": int(usage.get("cache_read_input_tokens") or 0),
                  "cache_write_1h": one_hour,
                  "cache_write_5m": max(created - one_hour, 0)}
        row = requests.setdefault(key, {**{f: 0 for f in FIELDS}, "complete": False,
                                        "structured": False})
        for name in FIELDS:
            row[name] = max(row[name], values[name])
        if message.get("stop_reason"):
            row["complete"] = True
        content = message.get("content")
        if isinstance(content, list) and any(
                isinstance(block, dict) and block.get("type") == "tool_use"
                and block.get("name") == STRUCTURED for block in content):
            row["structured"] = True
    return list(requests.values())


def price_arm(lane, record_dir: Path, transcript_dir: Path) -> dict:
    """Sum per-request usage and cost over an arm's recorded spawns, by model.

    Args:
        lane: The imported reproduction-lane module (for the cross-check).
        record_dir: The arm's committed directory holding `run-record.json`.
        transcript_dir: The workflow transcript directory for the arm.

    Returns:
        Mapping price key -> totals, request counts, and the three cost bounds.
    """
    record = json.loads((record_dir / "run-record.json").read_text(encoding="utf-8"))
    ids = {s["agent_id"] for s in record["spawns"]}
    by_model: dict[str, list[dict]] = defaultdict(list)
    spawns: dict[str, int] = defaultdict(int)
    matched = set()
    for path in sorted(transcript_dir.rglob("*.jsonl")):
        hit = [i for i in ids if i in path.name]
        if not hit:
            continue
        matched.update(hit)
        lines = path.read_text(encoding="utf-8").splitlines()
        usage = lane.transcript_usage(lines)
        models = usage["models"]
        key = price_key(set(models.values() if isinstance(models, dict) else models))
        requests = parse_requests(lines)
        # Cross-check: this parse must reproduce the lane's per-request totals.
        for name in FIELDS:
            mine = sum(r[name] for r in requests)
            if mine != usage[name]:
                raise SystemExit(f"{path.name}: {name} {mine} != lane {usage[name]}")
        by_model[key].extend(requests)
        spawns[key] += 1
    if matched != ids:
        raise SystemExit(f"{record_dir.name}: {len(ids - matched)} spawn transcripts missing")

    out = {}
    for key, requests in by_model.items():
        totals = {f: sum(r[f] for r in requests) for f in FIELDS}
        # Reference distributions from complete requests, by kind.
        reference = {}
        for kind in (True, False):
            pool = [r["output_tokens"] for r in requests
                    if r["complete"] and r["structured"] == kind]
            reference[kind] = ((statistics.median(pool), max(pool)) if pool else None)
        missing = [r for r in requests if not r["complete"]]
        bounds = {}
        for label, pick in (("central", 0), ("upper", 1)):
            output = totals["output_tokens"]
            for r in missing:
                ref = reference[r["structured"]]
                if ref is None:
                    continue  # no complete request of this kind to impute from
                output += max(r["output_tokens"], int(ref[pick])) - r["output_tokens"]
            bounds[label] = {"output_tokens": output,
                             "usd": round(cost({**totals, "output_tokens": output}, key), 2)}
        out[key] = {
            "spawns": spawns[key],
            "requests": len(requests),
            "requests_missing_final": len(missing),
            "structured_missing_final": sum(1 for r in missing if r["structured"]),
            **totals,
            "usd": round(cost(totals, key), 2),
            "imputed": bounds,
        }
    return out


def main() -> None:
    """Price every arm and print (optionally write) the comparison."""
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--json", type=Path, help="write the results as JSON")
    args = ap.parse_args()
    lane = load_lane()
    results = {arm: price_arm(lane, rec, wd) for arm, (rec, wd) in DEFAULT_ARMS.items()}
    for arm, rows in results.items():
        for key, row in sorted(rows.items()):
            print(f"{arm:18} {key:17} spawns={row['spawns']:2} "
                  f"req={row['requests']:3} miss={row['requests_missing_final']:3}"
                  f" (SO {row['structured_missing_final']:2}) "
                  f"out={row['output_tokens']:>8,} write5m={row['cache_write_5m']:>9,} "
                  f"read={row['cache_read_input_tokens']:>10,} "
                  f"${row['usd']:.2f} [central ${row['imputed']['central']['usd']:.2f},"
                  f" upper ${row['imputed']['upper']['usd']:.2f}]")
    if args.json:
        args.json.write_text(json.dumps({"prices_usd_per_mtok": PRICES,
                                         "multipliers": {"write_5m": WRITE_5M,
                                                         "write_1h": WRITE_1H,
                                                         "read": "per model, in prices"},
                                         "arms": results}, indent=1) + "\n",
                             encoding="utf-8")


if __name__ == "__main__":
    main()
