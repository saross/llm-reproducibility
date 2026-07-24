"""Shared helpers for the content-routing production hooks (routing design §3).

Used by `subagent-push.py` (SubagentStart), `subagent-receipt-gate.py`
(SubagentStop), and `preflight-agent.py` (PreToolUse[Agent]). All routing
state comes from `manifest.yaml` — the single source of truth the D5
consistency script keeps honest — so the hooks cannot drift from the registry.
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import yaml

HOOKS_DIR = Path(__file__).resolve().parent
REPO_ROOT = HOOKS_DIR.parent.parent
MANIFEST_PATH = REPO_ROOT / "manifest.yaml"
PUSH_RECEIPT_LOG = HOOKS_DIR / "push-receipts.jsonl"
GATE_LOG = HOOKS_DIR / "receipt-gate-log.jsonl"


def load_manifest() -> dict:
    """Load manifest.yaml (raises on failure — callers decide fail-open/closed)."""
    return yaml.safe_load(MANIFEST_PATH.read_text(encoding="utf-8")) or {}


def governed_agents(manifest: dict) -> dict:
    """Return the agent_definitions registry (name → {file, version, model, sha256})."""
    return manifest.get("agent_definitions") or {}


def pushed_instruments(manifest: dict, agent_type: str) -> list[dict]:
    """Return pushed-instrument specs for an agent type.

    Each spec: {name, path, version, token}. Derived from shared_content
    consumer lists with mechanism `push` — planned or active alike, so a
    consumer flip never silently changes what is injected.
    """
    specs = []
    for name, entry in (manifest.get("shared_content") or {}).items():
        for consumer in entry.get("consumers") or []:
            if consumer.get("agent") == agent_type and consumer.get("mechanism") == "push":
                specs.append({
                    "name": name,
                    "path": entry.get("canonical_file", ""),
                    "version": str(entry.get("version", "")),
                    "token": str(entry.get("receipt_token", "")),
                })
    return specs


def sha256_text(text: str) -> str:
    """Return the sha256 hex digest of a string's UTF-8 bytes."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def log_jsonl(path: Path, record: dict) -> None:
    """Append a timestamped record to a JSONL log (best-effort, never raises)."""
    try:
        record = {"ts": datetime.now(timezone.utc).isoformat(), **record}
        with path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    except OSError:
        pass


def extract_json_object(text: str) -> dict | None:
    """Best-effort extraction of a JSON object from an agent's final message.

    Tries the whole text, then each ```json fenced block, then the outermost
    brace span. Returns None if nothing parses to a dict.
    """
    candidates = [text.strip()]
    fence = "```"
    parts = text.split(fence)
    for i in range(1, len(parts), 2):
        block = parts[i]
        if block.startswith("json"):
            block = block[4:]
        candidates.append(block.strip())
    first, last = text.find("{"), text.rfind("}")
    if first != -1 and last > first:
        candidates.append(text[first:last + 1])
    for candidate in candidates:
        try:
            value = json.loads(candidate)
        except (json.JSONDecodeError, ValueError):
            continue
        if isinstance(value, dict):
            return value
    return None
