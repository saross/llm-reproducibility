#!/usr/bin/env python3
"""Assemble one benchmark arm's committed artefact set (D3 run contract H6).

**Version:** 1.4

From a completed arm workflow's transcript directory, produce the committed
arm directory: per-run score payloads (`run-<N>/<slug>.json` — the only
input to stability, audit F9), the authoritative reconciliation report and
gate/push log slices (audit F10), and `run-record.json` carrying per-spawn
identity, receipts, and the contract-defined spend recount (transcript
tokens excluding cache reads — hardening H4's reproducible unit).

v1.4 (effort pinning, 2026-08-17): the workflow (v1.5) injects a
``Provenance: launch commit <hash>; reasoning effort pinned: <level>.``
line into every scoring prompt. The assembler parses it back from the
transcripts — the record's ``provenance_pinned`` block is artefact-derived,
unlike the operator-attested ``run_environment`` values. Mixed values
across an arm's scoring spawns are a hard error (mixed-vintage, the H12
analogue); ``--expect-effort`` / ``--expect-launch-commit`` let the
operator assert the intended pin. Pre-pinning transcripts (the 2026-08-17
D3 arms and earlier) carry no Provenance line and assemble with the block
null-valued.

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

# Effort pinning (v1.4): format truth lives in the workflow's scorePrompt
# (fair-benchmark-arm.workflow.js v1.5) — change both together;
# tests/test_effort_pinning.py cross-checks the two files.
PROVENANCE_RE = re.compile(
    r"Provenance: launch commit ([0-9a-f]{40}); "
    r"reasoning effort pinned: (low|medium|high|xhigh|max)\.")


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


def transcript_provenance(text: str) -> tuple[str, str] | None:
    """(launch_commit, effort) parsed from the scoring prompt's Provenance
    line, or None for pre-pinning transcripts (v1.4)."""
    match = PROVENANCE_RE.search(text)
    if not match:
        return None
    return match.group(1), match.group(2)


def derive_arm_provenance(
        per_spawn: list[tuple[str, str] | None]) -> tuple[str | None, str | None]:
    """Arm-level (launch_commit, effort) from non-superseded scoring spawns.

    All-absent (a pre-pinning run) derives (None, None); any mix — absent
    beside present, or differing values — is a hard error, the
    mixed-vintage condition (contract H12 analogue).

    Raises:
        ValueError: on mixed provenance across the arm's scoring spawns.
    """
    distinct = set(per_spawn)
    if distinct == {None}:
        return None, None
    if len(distinct) != 1:
        raise ValueError(
            f"mixed scoring-spawn provenance across the arm: {sorted(map(str, distinct))}")
    return distinct.pop()


def transcript_telemetry(lines: list[str]) -> dict:
    """Artefact-derived spawn telemetry (v1.3, operator directive
    2026-08-17): validator retry count (errored StructuredOutput results),
    thinking-block count, and wall-clock from first/last entry timestamps."""
    structured_ids: set[str] = set()
    retries = 0
    thinking_blocks = 0
    first_ts = last_ts = None
    for line in lines:
        try:
            entry = json.loads(line)
        except json.JSONDecodeError:
            continue
        ts = entry.get("timestamp")
        if isinstance(ts, str) and ts:
            first_ts = first_ts or ts
            last_ts = ts
        content = ((entry.get("message") or {}).get("content")
                   if isinstance(entry.get("message"), dict) else None)
        if not isinstance(content, list):
            continue
        for blk in content:
            if not isinstance(blk, dict):
                continue
            if blk.get("type") == "thinking":
                thinking_blocks += 1
            elif (blk.get("type") == "tool_use"
                  and blk.get("name") == "StructuredOutput"):
                structured_ids.add(str(blk.get("id")))
            elif (blk.get("type") == "tool_result"
                  and str(blk.get("tool_use_id")) in structured_ids
                  and blk.get("is_error")):
                retries += 1
    wallclock = None
    if first_ts and last_ts:
        try:
            from datetime import datetime as _dt
            parse = lambda s: _dt.fromisoformat(s.replace("Z", "+00:00"))
            wallclock = round((parse(last_ts) - parse(first_ts)).total_seconds(), 1)
        except ValueError:
            pass
    return {"structured_output_retries": retries,
            "thinking_blocks": thinking_blocks,
            "wallclock_seconds": wallclock,
            "started_at": first_ts, "finished_at": last_ts}


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
    parser.add_argument("--extra-dir", action="append", default=[], type=Path,
                        help="replacement-run transcript directory (repeatable; "
                             "contract H11 split provenance)")
    parser.add_argument("--supersede", action="append", default=[],
                        metavar="AGENT_ID",
                        help="superseded scoring spawn in the primary dir "
                             "(excluded from payloads and clean requirement; "
                             "its spend still counts against the wire)")
    parser.add_argument("--expect-effort",
                        choices=["low", "medium", "high", "xhigh", "max"],
                        default=None,
                        help="assert the artefact-derived effort pin matches "
                             "this value (error on mismatch or absence)")
    parser.add_argument("--expect-launch-commit", default=None,
                        metavar="COMMIT",
                        help="assert the artefact-derived launch commit "
                             "matches this full hash (error on mismatch or "
                             "absence)")
    parser.add_argument("--environment", action="append", default=[],
                        metavar="KEY=VALUE",
                        help="run-environment attestation (repeatable): "
                             "effort/thinking level, harness route, billing "
                             "route. Recorded verbatim under run_environment "
                             "as session/operator-attested values — the "
                             "harness persists none of these itself "
                             "(v1.1, operator directive 2026-08-17)")
    args = parser.parse_args()
    run_dir = args.run_dir.expanduser().resolve()
    out_dir = args.out_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    superseded = set(args.supersede)
    all_dirs = [run_dir] + [d.expanduser().resolve() for d in args.extra_dir]
    reports = []
    for directory in all_dirs:
        report_path = directory / "reconciliation-authoritative" / "reconciliation-report.json"
        if not report_path.is_file():
            print(f"ERROR: authoritative reconciliation missing: {report_path}",
                  file=sys.stderr)
            return 1
        reports.append(json.loads(report_path.read_text()))
    # Contract H1 as amended by H11: every NON-superseded governed spawn
    # across all directories must reconcile; superseded spawns are excluded
    # from acceptance but named in the record.
    unreconciled = [a["agent_id"] for r in reports for a in r["agents"]
                    if not a["reconciled"] and a["agent_id"] not in superseded]
    if unreconciled:
        print(f"ERROR: unreconciled non-superseded spawns: {unreconciled} — "
              f"assembly refused (contract hardenings 1/11)", file=sys.stderr)
        return 1
    report = reports[0]

    spawns = []
    arm_tokens = {"input_tokens": 0, "output_tokens": 0,
                  "cache_creation_input_tokens": 0,
                  "cache_read_input_tokens": 0, "contract_metric_tokens": 0}
    payload_count = 0
    provenance_values: list[tuple[str, str] | None] = []
    transcripts = [tr for directory in all_dirs
                   for tr in sorted(directory.glob("agent-*.jsonl"))]
    for transcript in transcripts:
        agent_id = transcript.stem.replace("agent-", "")
        meta_path = transcript.parent / f"{transcript.stem}.meta.json"
        meta = json.loads(meta_path.read_text()) if meta_path.is_file() else {}
        text = transcript.read_text(encoding="utf-8")
        lines = text.splitlines()
        tokens = transcript_tokens(lines)
        for key in arm_tokens:
            arm_tokens[key] += tokens[key]
        agent_type = str(meta.get("agentType") or "")
        record = {"agent_id": agent_id, "agent_type": agent_type,
                  "usage": tokens, "telemetry": transcript_telemetry(lines)}
        if agent_id in superseded:
            record["superseded"] = True
            spawns.append(record)
            continue
        if agent_type.startswith("fair-assessor-"):
            identity = transcript_identity(text)
            payload = transcript_payload(lines)
            if identity is None or payload is None:
                print(f"ERROR: scoring transcript {agent_id} lacks identity "
                      f"or payload", file=sys.stderr)
                return 1
            _, run, slug = identity
            provenance = transcript_provenance(text)
            provenance_values.append(provenance)
            record.update({"run": run, "slug": slug,
                           "status": payload.get("status"),
                           "launch_commit": provenance[0] if provenance else None,
                           "effort_pinned": provenance[1] if provenance else None})
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

    try:
        arm_commit, arm_effort = derive_arm_provenance(provenance_values)
    except ValueError as exc:
        print(f"ERROR: {exc} — assembly refused (mixed-vintage)",
              file=sys.stderr)
        return 1
    if args.expect_effort and arm_effort != args.expect_effort:
        print(f"ERROR: --expect-effort {args.expect_effort} but transcripts "
              f"derive {arm_effort!r}", file=sys.stderr)
        return 1
    if args.expect_launch_commit and arm_commit != args.expect_launch_commit:
        print(f"ERROR: --expect-launch-commit {args.expect_launch_commit} "
              f"but transcripts derive {arm_commit!r}", file=sys.stderr)
        return 1

    recon_out = out_dir / "reconciliation"
    recon_out.mkdir(exist_ok=True)
    for name in ("reconciliation-report.json", "gate-log-slice.jsonl",
                 "push-log-slice.jsonl"):
        source = run_dir / "reconciliation-authoritative" / name
        if source.is_file():
            shutil.copy2(source, recon_out / name)
    for index, directory in enumerate(all_dirs[1:], start=1):
        for name in ("reconciliation-report.json", "gate-log-slice.jsonl",
                     "push-log-slice.jsonl"):
            source = directory / "reconciliation-authoritative" / name
            if source.is_file():
                shutil.copy2(source, recon_out / f"extra-{index}-{name}")

    import subprocess
    try:
        claude_version = subprocess.run(
            ["claude", "--version"], capture_output=True, text=True,
            timeout=10).stdout.strip() or "unavailable"
    except (OSError, subprocess.TimeoutExpired):
        claude_version = "unavailable"

    import platform as _platform
    platform_info = {"os": " ".join(_platform.uname()[:3]),
                     "python": _platform.python_version()}

    receipted = [a["receipts"].get("receipted") for r in reports
                 for a in r["agents"]
                 if a["agent_id"] not in superseded and a["reconciled"]]
    model_ids = sorted({r["model_id"] for r in receipted if r})
    # Served-variant markers (v1.3): bracket suffixes in receipted ids name
    # the served variant (e.g. claude-opus-5[1m] = 1M-context) — surfaced
    # explicitly rather than left for a reader to notice.
    variants = sorted({m[m.index("["):] for m in model_ids if "[" in m})
    record = {
        "arm": args.arm,
        "workflow_run_id": run_dir.name,
        "extra_run_dirs": [d.name for d in all_dirs[1:]],
        "superseded_spawns": sorted(superseded),
        "assembled_at": datetime.now(timezone.utc).isoformat(),
        "spawns": spawns,
        "score_payloads": payload_count,
        "model_ids_receipted": model_ids,
        "served_variant_markers": variants,
        "platform": platform_info,
        "reconciliation": {
            "accepted_rule": "every non-superseded governed spawn across all "
                             "directories reconciled (H1/H11)",
            "spawns_total": sum(r["spawns"] for r in reports),
            "spawns_reconciled": sum(r["spawns_reconciled"] for r in reports),
            "superseded": len(superseded),
            "skipped_ungoverned": sum(len(r.get("skipped_ungoverned", []))
                                      for r in reports),
            "reports": ["reconciliation/reconciliation-report.json"]
                       + [f"reconciliation/extra-{i+1}-reconciliation-report.json"
                          for i in range(len(reports) - 1)],
        },
        "provenance_pinned": {
            "note": "artefact-derived: parsed from the Provenance line the "
                    "workflow (v1.5+) injects into every scoring prompt; "
                    "null values mean a pre-pinning run (effort was "
                    "session-inherited and attestation-only)",
            "effort": arm_effort,
            "launch_commit": arm_commit,
        },
        "run_environment": {
            "note": "session/operator-attested values plus auto-captured "
                    "harness version; the spawn metadata records no effort "
                    "field, so these are attestations, not artefact-derived "
                    "— for effort, provenance_pinned supersedes these when "
                    "non-null",
            "claude_code_version": claude_version,
            **{kv.split("=", 1)[0]: kv.split("=", 1)[1]
               for kv in args.environment if "=" in kv},
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
    pin_note = (f"effort {arm_effort}, commit {arm_commit[:12]}"
                if arm_effort else "no provenance pin (pre-pinning run)")
    print(f"arm {args.arm}: {payload_count} payloads, "
          f"{record['usage_contract_metric']['contract_metric_tokens']:,} "
          f"contract-metric tokens, {pin_note} -> {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
