#!/usr/bin/env python3
"""Manifest-consistency check for shared instrument content (build item D5).

Verifies that `manifest.yaml` and the repository agree about every canonical
instrument file registered under `shared_content`, per the content-routing
design (`wiki/planning/agent-content-routing-design.md` §4) and the §3.4
hot-reload guard:

1. **Registry ↔ file**: each canonical file exists, is non-empty, carries a
   `**Version:**` line matching the manifest, and ends with a
   `Receipt-token:` line matching the manifest. Receipt tokens must be unique
   across entries (they are consumption evidence — a shared token would let
   one read masquerade as another).
2. **Consumer routing**: each declared consumer is backed by evidence —
   `push`/`pull` consumers must reference the canonical path from an agent
   definition (`.claude/agents/<agent>.md`) or the hook configuration
   (`.claude/settings.json`, `.claude/hooks/*`); `mirror` consumers must name
   a `mirror_file` whose banner cites the registered version and receipt
   token and which contains every normative block of the canonical file
   byte-identically (fenced code blocks and table rows; surrounding prose may
   differ per lane). Consumers marked `status: planned` warn instead of fail.
3. **Agent-definition hashes** (hot-reload guard): every file under
   `.claude/agents/` must be registered in `manifest.yaml agent_definitions`
   with a matching sha256, and vice versa — an ungated edit stops the batch
   rather than silently changing the instrument.

With `--preflight`, additionally fails if `CLAUDE_CODE_SUBAGENT_MODEL` is set
(it silently outranks agent-frontmatter model pins; 2026-07-24 review D-7).

Wired into the pre-commit hook (`scripts/install-git-hooks.sh`) and intended
for the orchestrator pre-flight (`PreToolUse[Agent]` hook). Exit status: 0 on
pass (warnings allowed), 1 on any error, 2 on environment/usage failure.
"""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover - environment defect, not a check failure
    print("check-manifest-consistency: PyYAML is required (pip install pyyaml)", file=sys.stderr)
    sys.exit(2)

# Version line format shared by all instrument files: **Version:** 2.0 (…)
VERSION_LINE_RE = re.compile(r"^\*\*Version:\*\*\s*([^\s(]+)", re.MULTILINE)

# Receipt token line — must be the final non-empty line of the canonical file
# so a header-only read cannot echo it (routing design §3.2).
RECEIPT_LINE_RE = re.compile(r"^Receipt-token:\s*(\S+)\s*$")


def fenced_blocks(text: str) -> list[str]:
    """Return the inner content of every ``` fenced block, in order."""
    blocks: list[str] = []
    current: list[str] | None = None
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            if current is None:
                current = []
            else:
                blocks.append("\n".join(current))
                current = None
        elif current is not None:
            current.append(line)
    return blocks


def table_rows(text: str) -> list[str]:
    """Return stripped markdown table rows (lines shaped like ``| … |``)."""
    rows = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("|") and stripped.endswith("|") and len(stripped) > 2:
            rows.append(stripped)
    return rows


def sha256_of(path: Path) -> str:
    """Return the sha256 hex digest of a file's bytes."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


class Report:
    """Accumulates errors (fatal) and warnings (advisory) with a common prefix."""

    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)


def routing_evidence_files(root: Path, agent: str) -> list[Path]:
    """Files that may carry routing evidence for a push/pull consumer.

    The agent's own definition plus the hook configuration — the places the
    design expects pushed/pulled paths to appear (§4 'grep agent definitions
    and hook config').
    """
    candidates = [root / ".claude" / "agents" / f"{agent}.md",
                  root / ".claude" / "settings.json"]
    hooks_dir = root / ".claude" / "hooks"
    if hooks_dir.is_dir():
        candidates.extend(p for p in sorted(hooks_dir.iterdir()) if p.is_file())
    return [p for p in candidates if p.is_file()]


def check_canonical_entry(name: str, entry: dict, root: Path, report: Report) -> None:
    """Check one shared_content entry: file presence, version line, receipt token."""
    rel = entry.get("canonical_file")
    if not rel:
        report.error(f"{name}: no canonical_file registered")
        return
    path = root / rel
    if not path.is_file():
        report.error(f"{name}: canonical file missing: {rel}")
        return
    text = path.read_text(encoding="utf-8")
    if not text.strip():
        report.error(f"{name}: canonical file is empty: {rel}")
        return

    want_version = str(entry.get("version", "")).strip()
    got = VERSION_LINE_RE.search(text)
    if not got:
        report.error(f"{name}: no '**Version:**' line in {rel}")
    elif got.group(1) != want_version:
        report.error(f"{name}: version drift — manifest {want_version!r}, file {got.group(1)!r}")

    want_token = str(entry.get("receipt_token", "")).strip()
    last_line = next((ln for ln in reversed(text.splitlines()) if ln.strip()), "")
    token_match = RECEIPT_LINE_RE.match(last_line.strip())
    if not token_match:
        report.error(f"{name}: final non-empty line of {rel} is not a 'Receipt-token:' line")
    elif token_match.group(1) != want_token:
        report.error(f"{name}: receipt-token drift — manifest {want_token!r}, "
                     f"file {token_match.group(1)!r}")


def check_mirror(name: str, entry: dict, consumer: dict, root: Path, report: Report) -> None:
    """Check a mirror consumer: banner cites version+token; normative blocks match."""
    mirror_rel = consumer.get("mirror_file")
    if not mirror_rel:
        report.error(f"{name}: mirror consumer {consumer.get('agent')!r} has no mirror_file")
        return
    mirror_path = root / mirror_rel
    if not mirror_path.is_file():
        report.error(f"{name}: mirror file missing: {mirror_rel}")
        return
    mirror_text = mirror_path.read_text(encoding="utf-8")

    version = str(entry.get("version", "")).strip()
    token = str(entry.get("receipt_token", "")).strip()
    if token and token not in mirror_text:
        report.error(f"{name}: mirror {mirror_rel} does not cite receipt token {token!r}")
    if version and f"v{version}" not in mirror_text and version not in mirror_text:
        report.error(f"{name}: mirror {mirror_rel} does not cite version {version!r}")

    canonical_path = root / entry.get("canonical_file", "")
    if not canonical_path.is_file():
        return  # missing canonical file already reported by check_canonical_entry
    canonical_text = canonical_path.read_text(encoding="utf-8")
    for i, block in enumerate(fenced_blocks(canonical_text), start=1):
        if block.strip() and block not in mirror_text:
            first = block.strip().splitlines()[0]
            report.error(f"{name}: mirror {mirror_rel} lacks canonical fenced block "
                         f"{i} (starts: {first!r})")
    mirror_rows = set(table_rows(mirror_text))
    for row in table_rows(canonical_text):
        if row not in mirror_rows:
            report.error(f"{name}: mirror {mirror_rel} lacks canonical table row: {row}")


def check_consumers(name: str, entry: dict, root: Path, report: Report) -> None:
    """Check each declared consumer has routing evidence for its mechanism."""
    for consumer in entry.get("consumers", []) or []:
        agent = consumer.get("agent", "<unnamed>")
        mechanism = consumer.get("mechanism")
        planned = str(consumer.get("status", "")).strip().lower() == "planned"

        if mechanism == "mirror":
            check_mirror(name, entry, consumer, root, report)
        elif mechanism in ("push", "pull"):
            rel = entry.get("canonical_file", "")
            evidence = [p for p in routing_evidence_files(root, agent)
                        if rel and rel in p.read_text(encoding="utf-8", errors="replace")]
            if not evidence:
                message = (f"{name}: no routing evidence for {mechanism} consumer {agent!r} "
                           f"(path {rel!r} not referenced from its agent definition or "
                           f"hook config)")
                if planned:
                    report.warn(message + " — consumer marked planned")
                else:
                    report.error(message)
        else:
            report.error(f"{name}: consumer {agent!r} has unknown mechanism {mechanism!r}")


def check_agent_hashes(manifest: dict, root: Path, report: Report) -> None:
    """Hot-reload guard (§3.4): .claude/agents/ contents ↔ manifest hash registry."""
    registry: dict = manifest.get("agent_definitions") or {}
    agents_dir = root / ".claude" / "agents"
    on_disk = sorted(agents_dir.glob("*.md")) if agents_dir.is_dir() else []

    registered_paths = set()
    for agent_name, info in registry.items():
        rel = info.get("file", "")
        registered_paths.add(rel)
        path = root / rel
        if not path.is_file():
            report.error(f"agent_definitions.{agent_name}: registered file missing: {rel}")
            continue
        want = str(info.get("sha256", "")).strip()
        got = sha256_of(path)
        if got != want:
            report.error(f"agent_definitions.{agent_name}: hash mismatch for {rel} — "
                         f"manifest {want[:16]}…, file {got[:16]}… (ungated edit? "
                         f"regression gate + manifest update required)")

    for path in on_disk:
        rel = str(path.relative_to(root))
        if rel not in registered_paths:
            report.error(f"unregistered agent definition: {rel} (hot-reload guard — "
                         f"register hash in manifest.yaml agent_definitions)")


def run_checks(manifest_path: Path, root: Path, preflight: bool) -> Report:
    """Run all consistency checks; return the populated report."""
    report = Report()
    try:
        manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        report.error(f"cannot load manifest {manifest_path}: {exc}")
        return report

    shared: dict = manifest.get("shared_content") or {}
    if not shared:
        report.warn("manifest has no shared_content entries — nothing to verify")

    tokens: dict[str, str] = {}
    for name, entry in shared.items():
        check_canonical_entry(name, entry, root, report)
        token = str(entry.get("receipt_token", "")).strip()
        if token in tokens:
            report.error(f"{name}: receipt token duplicates {tokens[token]!r} — "
                         f"tokens must be unique per instrument")
        elif token:
            tokens[token] = name
        check_consumers(name, entry, root, report)

    check_agent_hashes(manifest, root, report)

    if preflight and os.environ.get("CLAUDE_CODE_SUBAGENT_MODEL"):
        report.error("CLAUDE_CODE_SUBAGENT_MODEL is set — it silently outranks agent "
                     "model pins; unset it before spawning scoring agents (design §3.3)")
    return report


def main() -> int:
    """CLI entry point."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", type=Path,
                        default=Path(__file__).resolve().parent.parent,
                        help="repository root (default: parent of scripts/)")
    parser.add_argument("--manifest", type=Path, default=None,
                        help="manifest path (default: <root>/manifest.yaml)")
    parser.add_argument("--preflight", action="store_true",
                        help="add orchestrator pre-flight checks (model env override)")
    parser.add_argument("--quiet", action="store_true",
                        help="print only errors (pre-commit mode)")
    args = parser.parse_args()

    root = args.root.resolve()
    manifest_path = (args.manifest or root / "manifest.yaml").resolve()
    report = run_checks(manifest_path, root, args.preflight)

    for message in report.errors:
        print(f"ERROR: {message}")
    if not args.quiet:
        for message in report.warnings:
            print(f"warning: {message}")
        verdict = "FAIL" if report.errors else "PASS"
        print(f"manifest consistency: {verdict} "
              f"({len(report.errors)} error(s), {len(report.warnings)} warning(s))")
    return 1 if report.errors else 0


if __name__ == "__main__":
    sys.exit(main())
