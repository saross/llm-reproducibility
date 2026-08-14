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
   token, which contains every normative block of the canonical file
   byte-identically (fenced code blocks and table rows), and whose
   marker-delimited region is byte-identical to the canonical region.
   Consumers marked `status: planned` warn instead of fail.
3. **Agent-definition hashes** (hot-reload guard): every file under
   `.claude/agents/` must be registered in `manifest.yaml agent_definitions`
   with a matching sha256, and vice versa — an ungated edit stops the batch
   rather than silently changing the instrument.
4. **Reverse sweep**: every `*.md` in a directory listed under
   `shared_content_policy.scan_directories` must be registered, so an
   instrument nobody added to the manifest fails loudly instead of being
   invisible to a registry that only checks the files it already names.

Checks 2 (region comparison) and 4 were added 2026-07-27 after the structural
mirror check passed a Pass 6 prompt that had dropped four normative statements
from preregistration §7.1 (erratum-log Entry 2), and after an unregistered file
placed in the instruments directory went undetected.

5. **Entity checks** (monitoring plan Phase 2, 2026-08-03): every registered
   entity must have an `entity_checks` declaration, and every declaration is
   verified per its class — E1/E2 map to the implemented checks above;
   E3 compares a version carrier (markdown header, custom header label, or
   skill frontmatter) against the manifest with declared normalisation;
   E4 compares a JSON version field; E5 verifies the declared axis's pattern
   without ever comparing the other axis; E6 verifies existence of files
   declared unversioned; E8 enumerates a reference dataset from the registry,
   resolving each item's declared key and asserting cardinality. Undeclared
   entities and unresolvable declarations both fail — the "7 of 25" scope gap
   (plan §1a) cannot silently recur.

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

# Marker pairs delimiting the mirrorable region in the canonical file and its
# mirror. HTML comments: invisible in rendered markdown, inert to a model
# reading either file. Added 2026-07-27 — see check_mirror_region.
CANON_BEGIN = "<!-- canon-begin: {name} -->"
CANON_END = "<!-- canon-end: {name} -->"
MIRROR_BEGIN = "<!-- mirror-begin: {name} -->"
MIRROR_END = "<!-- mirror-end: {name} -->"


def segment_ids(text: str, name: str, kind: str) -> list[str]:
    """Return the segment suffixes of every marker for `name` in `text`.

    A mirror whose canonical content is distributed across several sections of
    the consuming document uses named segments — `<!-- canon-begin: id#part -->`
    — so each part stays byte-exact where it naturally belongs. An unsegmented
    marker yields [""], the single-region case.
    """
    pattern = re.compile(
        rf"<!-- {kind}-begin: {re.escape(name)}(#[A-Za-z0-9_-]+)? -->")
    return [m.group(1) or "" for m in pattern.finditer(text)]


def marked_region(text: str, begin: str, end: str) -> str | None:
    """Return the text strictly between two marker lines, or None if absent.

    Excludes the markers and the newline terminating the begin marker, so a
    canonical region and its mirror compare byte for byte regardless of the
    prose surrounding each.
    """
    start = text.find(begin)
    if start == -1:
        return None
    start += len(begin)
    if text[start:start + 1] == "\n":
        start += 1
    stop = text.find(end, start)
    if stop == -1:
        return None
    return text[start:stop]


def first_difference(left: str, right: str) -> str:
    """One-line description of where two regions diverge, for the report."""
    left_lines, right_lines = left.splitlines(), right.splitlines()
    for index, (a, b) in enumerate(zip(left_lines, right_lines), start=1):
        if a != b:
            return (f"first difference at region line {index}: "
                    f"{a.strip()[:60]!r} vs {b.strip()[:60]!r}")
    if len(left_lines) != len(right_lines):
        return f"canon has {len(left_lines)} lines, mirror has {len(right_lines)}"
    return "regions differ in trailing whitespace"


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
        # Coverage self-report (monitoring plan §6): generated from the
        # registry each run, never hand-maintained, so the SCOPE of the
        # assurance is visible in the same breath as the verdict.
        self.coverage: str = "coverage not computed"

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
        # Configuration files only: runtime logs (*.jsonl) are gitignored local
        # state and must not satisfy a routing check (audit 2026-08-03 M2).
        candidates.extend(p for p in sorted(hooks_dir.iterdir())
                          if p.is_file() and p.suffix in (".py", ".json"))
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

    mode = str(consumer.get("mirror_mode", "region")).strip().lower()
    if mode == "region":
        check_mirror_region(name, canonical_text, mirror_text, mirror_rel, report)
    elif mode == "structural":
        # Declared-weaker mode for mirrors that cannot be one contiguous region
        # (e.g. canonical tables distributed across several sections of a
        # skill's workflow). The guarantee is announced rather than assumed:
        # prose divergence is NOT detected in this mode, so the warning is the
        # honest statement of what the gate does and does not cover.
        report.warn(f"{name}: mirror {mirror_rel} is checked in 'structural' mode "
                    f"(fenced blocks and table rows only) — prose divergence between "
                    f"canon and this mirror is NOT detected; see erratum-log Entry 2 "
                    f"for why that gap matters")
    else:
        report.error(f"{name}: unknown mirror_mode {mode!r} for {mirror_rel} "
                     f"(expected 'region' or 'structural')")


def check_mirror_region(name: str, canonical_text: str, mirror_text: str,
                        mirror_rel: str, report: Report) -> None:
    """Byte-compare the marker-delimited mirror region against canon.

    The fenced-block and table-row checks above verify that the *structured*
    normative content survives into the mirror, but they cannot see prose. That
    gap was not theoretical: on 2026-07-27 the Pass 6 prompt was missing three
    normative sentences from preregistration §7.1 (unscoreable sub-principles
    score 0; scores are never aggregated; the A1 majority rule) plus the FAIR4RS
    scope statement, while every fenced block and table row matched — so the
    structural check passed a mirror that had silently dropped the
    scoring-relevant text. Erratum-log Entry 2 records the correction.

    A missing marker pair is an error rather than a skip: an unverifiable
    mirror is exactly the state the banner claims cannot exist, and treating it
    as passing would reinstate the defect this check exists to catch.
    """
    canon_segments = segment_ids(canonical_text, name, "canon")
    mirror_segments = segment_ids(mirror_text, name, "mirror")

    if not canon_segments:
        report.error(f"{name}: canonical file carries no "
                     f"'<!-- canon-begin: {name} -->' marker — mirror unverifiable")
    if not mirror_segments:
        report.error(f"{name}: mirror {mirror_rel} carries no "
                     f"'<!-- mirror-begin: {name} -->' marker — mirror unverifiable")
    if not canon_segments or not mirror_segments:
        return

    for missing in sorted(set(canon_segments) - set(mirror_segments)):
        report.error(f"{name}: mirror {mirror_rel} is missing canonical segment "
                     f"'{name}{missing}' — that content is not in the human lane")
    for extra in sorted(set(mirror_segments) - set(canon_segments)):
        report.error(f"{name}: mirror {mirror_rel} declares segment '{name}{extra}' "
                     f"which does not exist in the canonical file")

    for segment in sorted(set(canon_segments) & set(mirror_segments)):
        label = f"{name}{segment}"
        canonical_region = marked_region(
            canonical_text, CANON_BEGIN.format(name=label), CANON_END.format(name=label))
        mirror_region = marked_region(
            mirror_text, MIRROR_BEGIN.format(name=label), MIRROR_END.format(name=label))
        if canonical_region is None:
            report.error(f"{name}: canonical segment '{label}' has no closing "
                         f"'{CANON_END.format(name=label)}'")
            continue
        if mirror_region is None:
            report.error(f"{name}: mirror segment '{label}' has no closing "
                         f"'{MIRROR_END.format(name=label)}'")
            continue
        if canonical_region != mirror_region:
            report.error(f"{name}: mirror {mirror_rel} segment '{label}' is not "
                         f"byte-identical to canon "
                         f"({first_difference(canonical_region, mirror_region)})")


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


FRONTMATTER_KEY_RE = {
    "model": re.compile(r"^model:\s*(\S+)\s*$", re.MULTILINE),
    "memory": re.compile(r"^memory:", re.MULTILINE),
}


def frontmatter_of(text: str) -> str:
    """Return the YAML frontmatter block of an agent definition ('' if none)."""
    if not text.startswith("---"):
        return ""
    end = text.find("\n---", 3)
    return text[:end] if end != -1 else ""


def check_agent_hashes(manifest: dict, root: Path, report: Report) -> None:
    """Hot-reload guard (§3.4): .claude/agents/ contents ↔ manifest hash registry.

    Also enforces two per-agent governance rules from the routing design:
    §3.3 — every agent pins a model in frontmatter, matching the manifest's
    recorded pin and never the uncontrolled default 'inherit'; §3.9 — no
    `memory:` frontmatter on any registered agent (cross-session memory would
    quietly violate the fixed-instrument assumption).
    """
    registry: dict = manifest.get("agent_definitions") or {}
    agents_dir = root / ".claude" / "agents"
    on_disk = sorted(agents_dir.rglob("*.md")) if agents_dir.is_dir() else []

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

        frontmatter = frontmatter_of(path.read_text(encoding="utf-8"))
        model_match = FRONTMATTER_KEY_RE["model"].search(frontmatter)
        if not model_match:
            report.error(f"agent_definitions.{agent_name}: no 'model:' pin in "
                         f"frontmatter of {rel} (design §3.3 — 'inherit' default "
                         f"is uncontrolled)")
        else:
            pinned = model_match.group(1)
            want_model = str(info.get("model", "")).strip()
            if pinned == "inherit":
                report.error(f"agent_definitions.{agent_name}: model pin is 'inherit' "
                             f"in {rel} — pin an exact model ID (design §3.3)")
            elif want_model and pinned != want_model:
                report.error(f"agent_definitions.{agent_name}: model-pin drift — "
                             f"manifest {want_model!r}, frontmatter {pinned!r}")
        if FRONTMATTER_KEY_RE["memory"].search(frontmatter):
            report.error(f"agent_definitions.{agent_name}: 'memory:' frontmatter is "
                         f"prohibited on registered agents (design §3.9 — "
                         f"fixed-instrument assumption)")

    for path in on_disk:
        rel = str(path.relative_to(root))
        if rel not in registered_paths:
            report.error(f"unregistered agent definition: {rel} (hot-reload guard — "
                         f"register hash in manifest.yaml agent_definitions)")


def check_unregistered_instruments(manifest: dict, root: Path, report: Report) -> None:
    """Reverse sweep: every file in an instrument directory must be registered.

    The registry-to-file checks above can only verify files the registry names,
    so they are structurally blind to an instrument nobody registered — a new
    canonical file lands, the manifest is never updated, and the gate keeps
    reporting PASS. This is the same class of blindness the registry itself was
    created to fix, one level up. `.claude/agents/` already has an equivalent
    sweep in check_agent_hashes; this extends it to instrument content.

    Directories come from `shared_content_policy.scan_directories`. Pull-class
    reference libraries (`.claude/skills/**/references/`) are deliberately not
    swept: unregistered files there are the normal case, and only the few
    promoted to instrument status appear in the registry.
    """
    policy = manifest.get("shared_content_policy") or {}
    directories = policy.get("scan_directories") or []
    if not directories:
        report.warn("shared_content_policy.scan_directories is unset — no reverse sweep "
                    "for unregistered instrument files")
        return
    exclusions = set(policy.get("scan_exclusions") or [])
    registered = {entry.get("canonical_file")
                  for entry in (manifest.get("shared_content") or {}).values()}

    for rel_dir in directories:
        directory = root / rel_dir
        if not directory.is_dir():
            report.warn(f"scan directory does not exist: {rel_dir}")
            continue
        for path in sorted(directory.rglob("*")):
            if not path.is_file() or path.name in exclusions:
                continue
            # Editor/OS droppings must not block every commit and governed
            # spawn (re-audit M-6): skip dotfiles, dot-directories, and
            # __pycache__ — none is a registrable instrument.
            if any(part.startswith(".") or part == "__pycache__"
                   for part in path.relative_to(directory).parts):
                continue
            rel = str(path.relative_to(root))
            if rel not in registered:
                report.error(f"unregistered instrument file: {rel} (in scanned directory "
                             f"{rel_dir} — add it to manifest.yaml shared_content, or "
                             f"list it in shared_content_policy.scan_exclusions)")


# --- Entity checks (monitoring plan Phase 2) --------------------------------

# Frontmatter version line in a SKILL.md (quoted or bare).
FRONTMATTER_VERSION_RE = re.compile(r'^version:\s*"?([^"\s]+)"?\s*$', re.MULTILINE)

# Known normalisation rules. "strip-pass-suffix" was removed 2026-08-03: the
# header capture stops at the first space, so "2.7 Pass 1" already reads as
# "2.7" and the rule was unreachable dead code (audit finding). An unknown
# declared rule is an error, not a silent no-op.
KNOWN_NORMALISE_RULES = {"strip-v-prefix"}


def normalise_version(value: str, rules) -> str:
    """Apply declared normalisation rules to a version string read from a file."""
    if rules is None:
        rules = []
    elif isinstance(rules, str):
        rules = [rules]
    value = value.strip()
    for rule in rules:
        if rule == "strip-v-prefix" and re.match(r"v\d", value):
            value = value[1:]
    return value


def normalise_rules_of(decl: dict) -> list:
    """Return the declaration's normalise rules as a list.

    A non-string scalar or other unexpected shape yields an '<invalid>'
    sentinel so the unknown-rule error fires instead of a crash (re-audit
    M-7): a malformed declaration must fail loudly, not take down the gate.
    """
    rules = decl.get("normalise")
    if rules is None:
        return []
    if isinstance(rules, str):
        return [rules]
    if isinstance(rules, list):
        return [rule if isinstance(rule, str) else "<invalid>" for rule in rules]
    return ["<invalid>"]


def enumerate_entities(manifest: dict) -> dict[str, tuple[str, object]]:
    """Return every registered entity as {dotted_path: (kind, data)}.

    This is the Phase 0 enumeration made executable: shared_content and
    agent_definitions keys; every versioned dict carrying `file` or `path`
    under components/assessment/reproduction; the documentation, template,
    and queue-file path scalars (other `corpus` keys are counts and output
    locations — metadata, not artefacts); the workflow_passes prompt list;
    and reference_datasets. The undeclared-entity check below runs over
    exactly this set, so an entity added to the manifest without a check
    declaration fails the gate rather than joining a silent remainder.
    """
    entities: dict[str, tuple[str, object]] = {}
    for key in (manifest.get("shared_content") or {}):
        entities[f"shared_content.{key}"] = ("shared-content", None)
    for key in (manifest.get("agent_definitions") or {}):
        entities[f"agent_definitions.{key}"] = ("agent-definition", None)

    def walk(node: object, path: str) -> None:
        if isinstance(node, list):
            # Walk list entries too (re-audit M-5): a file-carrying dict
            # inside a list must not escape enumeration.
            for index, item in enumerate(node):
                walk(item, f"{path}[{index}]")
            return
        if not isinstance(node, dict):
            return
        if "file" in node or "path" in node:
            kind = "versioned" if "version" in node else "file-unversioned"
            entities[path] = (kind, node)
        for key, value in node.items():
            walk(value, f"{path}.{key}")

    # Walk every top-level section not handled specially above/below, so a
    # new section (or a file entry without a version) cannot silently escape
    # enumeration (audit 2026-08-03 C2 — the "7 of 25" recurrence path).
    # Only sections that produce their own entity kinds are excluded
    # (re-audit M-5: the old set also skipped project, corpus,
    # version_history, licences, documentation, and shared_content_policy
    # wholesale, so file-carrying entries there escaped entirely). The
    # dedicated path-scalar loops below keep their jobs; anything
    # file-shaped added to a walked section now fails as undeclared
    # instead of vanishing.
    specially_handled = {"shared_content", "agent_definitions",
                         "workflow_passes", "reference_datasets",
                         "entity_checks"}
    for section, node in manifest.items():
        if section not in specially_handled:
            walk(node, section)

    for key, value in (manifest.get("documentation") or {}).items():
        entities[f"documentation.{key}"] = ("path-scalar", value)
    for key, value in ((manifest.get("reproduction") or {}).get("templates") or {}).items():
        entities[f"reproduction.templates.{key}"] = ("path-scalar", value)
    queue_file = (manifest.get("corpus") or {}).get("queue_file")
    if queue_file:
        entities["corpus.queue_file"] = ("path-scalar", queue_file)
    for index, item in enumerate(manifest.get("workflow_passes") or []):
        if isinstance(item, dict):
            entities[f"workflow_passes.pass-{item.get('pass', index)}"] = ("pass-prompt", item)
    for key, value in (manifest.get("reference_datasets") or {}).items():
        entities[f"reference_datasets.{key}"] = ("reference-dataset", value)
    return entities


def read_declared_version(path: Path, decl: dict, report: Report,
                          label_prefix: str) -> str | None:
    """Extract the version a file carries, per the declared version_source."""
    if not path.is_file():
        report.error(f"{label_prefix}: file missing: {path}")
        return None
    text = path.read_text(encoding="utf-8", errors="replace")
    source = str(decl.get("version_source", "markdown-header"))

    if source == "markdown-header":
        label = str(decl.get("header_label", "Version"))
        match = re.search(rf"^\*\*{re.escape(label)}:\*\*\s*([^\s(|]+)",
                          text, re.MULTILINE)
        if not match:
            report.error(f"{label_prefix}: no '**{label}:**' line in {path.name}")
            return None
        return match.group(1)
    if source == "skill-frontmatter":
        match = FRONTMATTER_VERSION_RE.search(frontmatter_of(text))
        if not match:
            report.error(f"{label_prefix}: no 'version:' in frontmatter of {path.name}")
            return None
        return match.group(1)
    report.error(f"{label_prefix}: unknown version_source {source!r}")
    return None


def check_entity_declarations(manifest: dict, root: Path, report: Report) -> None:
    """Verify entity_checks coverage in both directions, then each declaration."""
    checks = manifest.get("entity_checks")
    if checks is None:
        report.error("manifest has no entity_checks section — every registered "
                     "entity must declare its check class (monitoring plan Phase 1)")
        return
    entities = enumerate_entities(manifest)

    if not isinstance(checks, dict):
        report.error("entity_checks must be a mapping of dotted registry paths to "
                     "check declarations")
        return
    valid_declaration = {
        path for path in entities
        if isinstance(checks.get(path), dict)
        and str(checks[path].get("class", "")).strip()
    }
    declared = len(valid_declaration)
    by_class: dict[str, int] = {}
    for path in valid_declaration:
        cls = str(checks[path]["class"]).strip()
        by_class[cls] = by_class.get(cls, 0) + 1
    class_counts = " ".join(f"{cls}:{n}" for cls, n in sorted(by_class.items()))
    report.coverage = (f"{declared}/{len(entities)} entities checked "
                       f"({class_counts}), {len(entities) - declared} undeclared")

    for path in entities:
        if path not in checks:
            report.error(f"undeclared entity: {path} has no entity_checks entry "
                         f"(monitoring plan §5 — no entity may lack a check)")
        elif path not in valid_declaration:
            report.error(f"entity_checks.{path}: declaration must be a mapping with a "
                         f"'class' — a malformed declaration silently disables the "
                         f"check (audit 2026-08-03 C1)")
    for path in checks:
        if path not in entities:
            report.error(f"entity_checks.{path}: does not resolve to a registered "
                         f"entity — stale or mistyped registry path")

    kind_for_class = {
        "E1": ("shared-content",),
        "E2": ("agent-definition",),
        "E3": ("versioned", "pass-prompt"),
        "E4": ("versioned",),
        "E5": ("versioned",),
        "E6": ("path-scalar", "versioned", "file-unversioned"),
        "E8": ("reference-dataset",),
    }
    for path, decl in checks.items():
        data = entities.get(path)
        if data is None or not isinstance(decl, dict):
            continue  # unresolvable and malformed declarations reported above
        kind, node = data
        cls = str(decl.get("class", "")).strip()
        prefix = f"entity_checks.{path}"

        allowed = kind_for_class.get(cls)
        if allowed is not None and kind not in allowed:
            report.error(f"{prefix}: class {cls} declared for a {kind} entity — "
                         f"declaration/entity mismatch (audit 2026-08-03 M1)")
            continue
        unknown_rules = [r for r in normalise_rules_of(decl)
                         if r not in KNOWN_NORMALISE_RULES]
        if unknown_rules:
            report.error(f"{prefix}: unknown normalise rule(s) {unknown_rules!r} — "
                         f"a typo here silently disables normalisation")
            continue

        if cls == "E1":
            pass  # kind check above; hard checks run in check_canonical_entry
        elif cls == "E2":
            pass  # kind check above; hard checks run in check_agent_hashes
        elif cls == "E3":
            want = str(decl.get("version") or node.get("version") or "").strip()
            rel = (decl.get("version_file")
                   or node.get("file")
                   or (node.get("prompt") if kind == "pass-prompt" else None))
            if not want or not rel:
                report.error(f"{prefix}: E3 needs a version and a file "
                             f"(or version_file for path-registered entities)")
                continue
            got = read_declared_version(root / str(rel), decl, report, prefix)
            if got is not None:
                normalised = normalise_version(got, decl.get("normalise"))
                if normalised != want:
                    report.error(f"{prefix}: version drift — manifest {want!r}, "
                                 f"file carries {got!r} (normalised {normalised!r})")
        elif cls == "E4":
            import json as _json
            want = str(node.get("version", "")).strip()
            rel = str(node.get("file", ""))
            json_path = str(decl.get("json_path", "$.version"))
            file_path = root / rel
            if not file_path.is_file():
                report.error(f"{prefix}: file missing: {rel}")
                continue
            try:
                document = _json.loads(file_path.read_text(encoding="utf-8"))
            except _json.JSONDecodeError as exc:
                report.error(f"{prefix}: {rel} is not valid JSON ({exc})")
                continue
            if not json_path.startswith("$.") or "." in json_path[2:]:
                report.error(f"{prefix}: unsupported json_path {json_path!r} — only "
                             f"top-level $.key paths are implemented")
                continue
            if not isinstance(document, dict):
                report.error(f"{prefix}: {rel} JSON top level is "
                             f"{type(document).__name__}, expected an object")
                continue
            got = document.get(json_path[2:])
            if got is None:
                report.error(f"{prefix}: {rel} has no {json_path} field")
            elif str(got) != want:
                report.error(f"{prefix}: version drift — manifest {want!r}, "
                             f"{json_path} is {got!r}")
        elif cls == "E5":
            want = str(node.get("version", "")).strip()
            rel = str(node.get("file", ""))
            pattern = decl.get("pattern")
            file_path = root / rel
            if not pattern:
                report.error(f"{prefix}: E5 declaration has no pattern")
                continue
            if not file_path.is_file():
                report.error(f"{prefix}: file missing: {rel}")
                continue
            needle = str(pattern).replace("{version}", want)
            if needle not in file_path.read_text(encoding="utf-8", errors="replace"):
                report.error(f"{prefix}: declared axis pattern {needle!r} not found "
                             f"in {rel} — the tracked axis has drifted (the file's "
                             f"other version axis is deliberately not compared)")
        elif cls == "E6":
            rel = node if isinstance(node, str) else (node or {}).get("file", "")
            if not rel or not (root / rel).is_file():
                report.error(f"{prefix}: declared-unversioned file missing: {rel!r}")
        elif cls == "E8":
            import json as _json
            spec = node or {}
            items = spec.get("items") or []
            want_n = spec.get("cardinality")
            if decl.get("assert_cardinality") and len(items) != want_n:
                report.error(f"{prefix}: cardinality drift — declared {want_n}, "
                             f"registry lists {len(items)} item(s)")
            for item in items:
                if not isinstance(item, dict):
                    report.error(f"{prefix}: reference item {item!r} is not a mapping")
                    continue
                slug = item.get("slug", "<unnamed>")
                item_path = root / item.get("file", "")
                if not item_path.is_file():
                    report.error(f"{prefix}: item {slug!r} file missing: "
                                 f"{item.get('file')}")
                    continue
                try:
                    document = _json.loads(item_path.read_text(encoding="utf-8"))
                except _json.JSONDecodeError as exc:
                    report.error(f"{prefix}: item {slug!r} is not valid JSON ({exc})")
                    continue
                key_node = document
                for part in str(item.get("fair_key", "")).split("."):
                    key_node = key_node.get(part) if isinstance(key_node, dict) else None
                if key_node is None:
                    report.error(f"{prefix}: item {slug!r} declared key "
                                 f"{item.get('fair_key')!r} does not resolve in "
                                 f"{item.get('file')}")
        else:
            report.error(f"{prefix}: unknown check class {cls!r}")


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
    check_unregistered_instruments(manifest, root, report)
    check_entity_declarations(manifest, root, report)

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
    print(f"manifest consistency: {verdict} — {report.coverage} "
          f"({len(report.errors)} error(s), {len(report.warnings)} warning(s))")
    return 1 if report.errors else 0


if __name__ == "__main__":
    sys.exit(main())
