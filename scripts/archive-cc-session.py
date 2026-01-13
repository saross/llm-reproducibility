#!/usr/bin/env python3
"""
Archive Claude Code (CC) sessions for research transparency.

This script archives CC sessions from ~/.claude/projects/ to the project's
archive/cc-sessions/ directory, with structured metadata for FAIR-aligned
research documentation.

Usage:
    # Archiving
    python scripts/archive-cc-session.py                    # Archive latest session
    python scripts/archive-cc-session.py --session-id UUID  # Archive specific session
    python scripts/archive-cc-session.py --all              # Archive all unarchived
    python scripts/archive-cc-session.py --list             # List sessions and status

    # Metadata management
    python scripts/archive-cc-session.py --list-archives    # Show metadata completion
    python scripts/archive-cc-session.py --summarize ID     # Analyse session for metadata
    python scripts/archive-cc-session.py --update-metadata ID -m meta.json  # Update metadata

The script is designed to run within a CC session so that CC can generate
rich metadata (title, purpose, tags, three_ps summaries) interactively.

Created: 2026-01-08
Updated: 2026-01-13 (v1.2)
Schema version: 1.1

v1.2 additions:
- --list-archives: Show metadata completion status
- --summarize: Analyse session to help generate metadata
- --update-metadata: Update metadata for existing archives
- Fixed null timestamp handling in catalog sort

v1.1 additions:
- thinking_blocks section with ethics metadata (sharing_preference, use_constraints)
- relationships vocabulary (continues, isPartOf, etc.)
- artifacts tracking (created, modified, referenced files)
- tool_outputs byte tracking
- compression metadata fields
- archive-defaults.yaml config file support
"""

import argparse
import gzip
import hashlib
import json
import re
import shutil
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Any

try:
    import yaml
    YAML_AVAILABLE = True
except ImportError:
    YAML_AVAILABLE = False


# =============================================================================
# Configuration
# =============================================================================

SCHEMA_VERSION = "1.1"
CLAUDE_PROJECTS_DIR = Path.home() / ".claude" / "projects"
ARCHIVE_DIR = Path(__file__).parent.parent / "archive" / "cc-sessions"
CATALOG_FILE = ARCHIVE_DIR / "CATALOG.json"
DEFAULTS_FILE = ARCHIVE_DIR / "archive-defaults.yaml"

# v1.1: Default thinking block ethics preferences
DEFAULT_THINKING_SHARING = "research-only"
DEFAULT_THINKING_USE_CONSTRAINTS = [
    "analysis-for-improvement",
    "research-publication-aggregated"
]
DEFAULT_THINKING_EXCLUDED_USES = [
    "training-data",
    "public-display-individual"
]
DEFAULT_THINKING_NATURE_NOTE = (
    "Work-in-progress reasoning traces, not polished output. "
    "May contain abandoned paths and self-corrections."
)

# v1.1: File type mappings for artifact categorisation
FILE_TYPE_MAPPINGS = {
    ".py": "code",
    ".js": "code",
    ".ts": "code",
    ".sh": "code",
    ".r": "code",
    ".R": "code",
    ".sql": "code",
    ".md": "document",
    ".txt": "document",
    ".rst": "document",
    ".json": "data",
    ".csv": "data",
    ".jsonl": "data",
    ".geojson": "data",
    ".yaml": "config",
    ".yml": "config",
    ".toml": "config",
    ".ini": "config",
    ".png": "image",
    ".jpg": "image",
    ".jpeg": "image",
    ".gif": "image",
    ".svg": "image",
    ".tif": "image",
    ".tiff": "image",
}


# =============================================================================
# Project Name Detection
# =============================================================================

def get_project_name() -> str:
    """
    Detect project name using cascading fallback.

    Priority:
        1. CLAUDE.md "# Project: <name>" line
        2. Git remote (owner/repo or just repo)
        3. Directory name

    Returns:
        Project name string (e.g., "vlm-burial-mound-detection")
    """
    project_root = Path(__file__).parent.parent

    # Try CLAUDE.md
    claude_md = project_root / "CLAUDE.md"
    if claude_md.exists():
        content = claude_md.read_text()
        match = re.search(r'^#\s*Project:\s*(.+)$', content, re.MULTILINE | re.IGNORECASE)
        if match:
            return match.group(1).strip()

    # Try git remote
    try:
        result = subprocess.run(
            ["git", "-C", str(project_root), "remote", "get-url", "origin"],
            capture_output=True,
            text=True,
            check=True
        )
        remote_url = result.stdout.strip()
        # Extract repo name from URL (handles both SSH and HTTPS)
        match = re.search(r'[/:]([^/]+)/([^/]+?)(?:\.git)?$', remote_url)
        if match:
            return match.group(2)  # Just repo name, not owner/repo
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass

    # Fallback to directory name
    return project_root.name


def get_project_directory() -> Path:
    """Get the project root directory."""
    return Path(__file__).parent.parent


def get_cc_project_path() -> str:
    """
    Get the path-encoded project identifier used by CC.

    CC encodes paths by replacing '/' with '-', e.g.,
    /home/shawn/Code/map-reader-llm -> -home-shawn-Code-map-reader-llm
    """
    project_dir = get_project_directory().resolve()
    return str(project_dir).replace("/", "-")


# =============================================================================
# Session Discovery
# =============================================================================

def get_session_files() -> list[Path]:
    """
    Find all session JSONL files for this project in ~/.claude/projects/.

    Returns:
        List of Path objects for session files, sorted by modification time
    """
    cc_project_path = get_cc_project_path()
    project_dir = CLAUDE_PROJECTS_DIR / cc_project_path

    if not project_dir.exists():
        print(f"Warning: CC project directory not found: {project_dir}")
        return []

    # Get all JSONL files (both main sessions and agent sessions)
    session_files = list(project_dir.glob("*.jsonl"))
    return sorted(session_files, key=lambda p: p.stat().st_mtime)


def get_archived_session_ids() -> set[str]:
    """
    Get set of session IDs that have already been archived.

    Returns:
        Set of session ID strings from CATALOG.json
    """
    if not CATALOG_FILE.exists():
        return set()

    try:
        catalog = json.loads(CATALOG_FILE.read_text())
        return {s["id"] for s in catalog.get("sessions", [])}
    except (json.JSONDecodeError, KeyError):
        return set()


def get_session_id(session_path: Path) -> str:
    """
    Extract session ID from filename.

    Main sessions: UUID (e.g., 550e8400-e29b-41d4-a716-446655440000.jsonl)
    Agent sessions: agent-<short_id> (e.g., agent-a37c175.jsonl)
    """
    return session_path.stem


# =============================================================================
# Session Statistics Extraction
# =============================================================================

def extract_session_stats(session_path: Path) -> dict[str, Any]:
    """
    Extract statistics from a session JSONL file.

    Returns:
        Dictionary with session statistics including:
        - timestamps (start, end, duration)
        - message counts (human, assistant, turns)
        - thinking block count
        - tool call counts by type
        - token counts (if available)
        - model information
    """
    stats = {
        "turns": 0,
        "human_messages": 0,
        "assistant_messages": 0,
        "thinking_blocks": 0,
        "tool_calls": {"total": 0, "by_type": {}},
        "tokens": {"input": 0, "output": 0, "cache_read": 0},
        "model": None,
        "timestamps": []
    }

    with open(session_path, 'r') as f:
        for line in f:
            if not line.strip():
                continue

            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue

            # Extract timestamp
            ts = entry.get("timestamp")
            if ts:
                stats["timestamps"].append(ts)

            # Skip non-message entries
            if entry.get("type") == "file-history-snapshot":
                continue

            # Process message content
            message = entry.get("message", {})
            role = message.get("role", entry.get("type", ""))

            if role == "user":
                stats["human_messages"] += 1
                stats["turns"] += 1

            elif role == "assistant":
                stats["assistant_messages"] += 1
                content = message.get("content", [])

                if isinstance(content, list):
                    for block in content:
                        if isinstance(block, dict):
                            block_type = block.get("type")

                            if block_type == "thinking":
                                stats["thinking_blocks"] += 1

                            elif block_type == "tool_use":
                                tool_name = block.get("name", "unknown")
                                stats["tool_calls"]["total"] += 1
                                stats["tool_calls"]["by_type"][tool_name] = \
                                    stats["tool_calls"]["by_type"].get(tool_name, 0) + 1

                # Extract model from response metadata
                if not stats["model"]:
                    model = message.get("model")
                    if model:
                        stats["model"] = model

            # Extract token usage from assistant messages
            usage = entry.get("usage", {})
            if usage:
                stats["tokens"]["input"] += usage.get("input_tokens", 0)
                stats["tokens"]["output"] += usage.get("output_tokens", 0)
                stats["tokens"]["cache_read"] += usage.get("cache_read_input_tokens", 0)

    # Compute derived values
    if stats["timestamps"]:
        stats["started_at"] = min(stats["timestamps"])
        stats["ended_at"] = max(stats["timestamps"])
        try:
            start = datetime.fromisoformat(stats["started_at"].replace("Z", "+00:00"))
            end = datetime.fromisoformat(stats["ended_at"].replace("Z", "+00:00"))
            stats["duration_minutes"] = int((end - start).total_seconds() / 60)
        except (ValueError, TypeError):
            stats["duration_minutes"] = 0
    else:
        stats["started_at"] = None
        stats["ended_at"] = None
        stats["duration_minutes"] = 0

    # Clean up
    del stats["timestamps"]

    return stats


def estimate_cost(stats: dict[str, Any]) -> float:
    """
    Estimate API cost based on token usage.

    Uses approximate pricing for Claude Sonnet (may vary by model).
    """
    # Approximate pricing per 1M tokens (USD)
    input_price = 3.0
    output_price = 15.0
    cache_price = 0.3  # Cache reads are cheaper

    input_tokens = stats["tokens"].get("input", 0)
    output_tokens = stats["tokens"].get("output", 0)
    cache_tokens = stats["tokens"].get("cache_read", 0)

    cost = (
        (input_tokens / 1_000_000) * input_price +
        (output_tokens / 1_000_000) * output_price +
        (cache_tokens / 1_000_000) * cache_price
    )

    return round(cost, 2)


# =============================================================================
# v1.1: Defaults Configuration
# =============================================================================

def load_defaults() -> dict[str, Any]:
    """
    Load default configuration from archive-defaults.yaml.

    Returns:
        Dictionary of defaults, or empty dict if file not found or YAML unavailable
    """
    if not YAML_AVAILABLE:
        return {}

    if not DEFAULTS_FILE.exists():
        return {}

    try:
        with open(DEFAULTS_FILE, 'r') as f:
            return yaml.safe_load(f) or {}
    except (yaml.YAMLError, OSError) as e:
        print(f"Warning: Could not load defaults: {e}")
        return {}


# =============================================================================
# v1.1: Thinking Block Token Extraction
# =============================================================================

def extract_thinking_block_tokens(session_path: Path) -> dict[str, Any]:
    """
    Extract thinking block statistics including token estimates.

    The JSONL may not include per-block token counts, so we estimate
    using len(text) / 4 as a rough approximation.

    Args:
        session_path: Path to the session JSONL file

    Returns:
        Dictionary with:
        - count: Number of thinking blocks
        - total_tokens: Estimated total tokens (may be from usage stats)
        - token_count_method: 'actual' or 'estimated'
    """
    thinking_count = 0
    estimated_tokens = 0
    actual_tokens_from_usage = None

    with open(session_path, 'r') as f:
        for line in f:
            if not line.strip():
                continue

            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue

            message = entry.get("message", {})
            content = message.get("content", [])

            if isinstance(content, list):
                for block in content:
                    if isinstance(block, dict) and block.get("type") == "thinking":
                        thinking_count += 1
                        thinking_text = block.get("thinking", "")
                        # Estimate tokens as ~4 chars per token
                        estimated_tokens += len(thinking_text) // 4

    return {
        "count": thinking_count,
        "total_tokens": estimated_tokens,
        "token_count_method": "estimated"
    }


# =============================================================================
# v1.1: Tool Output Byte Tracking
# =============================================================================

def extract_tool_output_bytes(session_path: Path) -> dict[str, Any]:
    """
    Extract tool output byte statistics for storage analysis.

    Parses tool_result blocks from JSONL and sums byte counts by tool type.

    Args:
        session_path: Path to the session JSONL file

    Returns:
        Dictionary with:
        - total_bytes: Total bytes across all tool outputs
        - by_type: Breakdown by tool type {tool_name: {count: N, bytes: N}}
        - largest_single_output_bytes: Size of largest single output
    """
    by_type: dict[str, dict[str, int]] = {}
    total_bytes = 0
    largest_output = 0

    # Track which tool_use_id maps to which tool name
    tool_use_names: dict[str, str] = {}

    with open(session_path, 'r') as f:
        for line in f:
            if not line.strip():
                continue

            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue

            message = entry.get("message", {})
            content = message.get("content", [])

            if isinstance(content, list):
                for block in content:
                    if not isinstance(block, dict):
                        continue

                    block_type = block.get("type")

                    # Map tool_use IDs to tool names
                    if block_type == "tool_use":
                        tool_id = block.get("id")
                        tool_name = block.get("name", "unknown")
                        if tool_id:
                            tool_use_names[tool_id] = tool_name

                    # Count tool_result bytes
                    elif block_type == "tool_result":
                        tool_id = block.get("tool_use_id")
                        tool_name = tool_use_names.get(tool_id, "unknown")

                        # Get content size
                        result_content = block.get("content", "")
                        if isinstance(result_content, str):
                            output_bytes = len(result_content.encode('utf-8'))
                        elif isinstance(result_content, list):
                            # Handle list of content blocks
                            output_bytes = sum(
                                len(json.dumps(item).encode('utf-8'))
                                for item in result_content
                            )
                        else:
                            output_bytes = len(str(result_content).encode('utf-8'))

                        # Update statistics
                        total_bytes += output_bytes
                        largest_output = max(largest_output, output_bytes)

                        if tool_name not in by_type:
                            by_type[tool_name] = {"count": 0, "bytes": 0}
                        by_type[tool_name]["count"] += 1
                        by_type[tool_name]["bytes"] += output_bytes

    return {
        "total_bytes": total_bytes,
        "by_type": by_type,
        "largest_single_output_bytes": largest_output
    }


# =============================================================================
# v1.1: Artifacts Tracking
# =============================================================================

def get_file_type(file_path: str) -> str:
    """
    Determine file type from extension.

    Args:
        file_path: Path to the file

    Returns:
        File type string: code, document, data, config, image, or other
    """
    ext = Path(file_path).suffix.lower()
    return FILE_TYPE_MAPPINGS.get(ext, "other")


def extract_artifacts(session_path: Path) -> dict[str, list[dict[str, str]]]:
    """
    Extract artifacts (files created, modified, referenced) from session.

    Parses tool calls to identify file operations:
    - Write → created
    - Edit → modified
    - Read → referenced

    Applies deduplication priority:
    - created + modified → created only (it was new)
    - read + modified → modified only (read was context)
    - read only → referenced

    Filters out files outside project directory.

    Args:
        session_path: Path to the session JSONL file

    Returns:
        Dictionary with created, modified, referenced lists
    """
    project_dir = str(get_project_directory().resolve())

    # Track all file operations
    written_files: set[str] = set()
    edited_files: set[str] = set()
    read_files: set[str] = set()

    with open(session_path, 'r') as f:
        for line in f:
            if not line.strip():
                continue

            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue

            message = entry.get("message", {})
            content = message.get("content", [])

            if isinstance(content, list):
                for block in content:
                    if not isinstance(block, dict):
                        continue

                    if block.get("type") != "tool_use":
                        continue

                    tool_name = block.get("name", "")
                    tool_input = block.get("input", {})

                    # Extract file path based on tool type
                    file_path = None

                    if tool_name == "Write":
                        file_path = tool_input.get("file_path")
                        if file_path:
                            written_files.add(file_path)

                    elif tool_name == "Edit":
                        file_path = tool_input.get("file_path")
                        if file_path:
                            edited_files.add(file_path)

                    elif tool_name == "Read":
                        file_path = tool_input.get("file_path")
                        if file_path:
                            read_files.add(file_path)

    # Apply deduplication priority and filter by project directory
    def is_in_project(path: str) -> bool:
        """Check if path is within project directory."""
        try:
            resolved = str(Path(path).resolve())
            return resolved.startswith(project_dir)
        except (OSError, ValueError):
            return False

    def make_relative(path: str) -> str:
        """Convert absolute path to project-relative path."""
        try:
            resolved = Path(path).resolve()
            return str(resolved.relative_to(project_dir))
        except (OSError, ValueError):
            return path

    # Apply deduplication logic:
    # - created + modified → created only
    # - read + modified → modified only
    # - read only → referenced
    created = written_files
    modified = edited_files - written_files  # Don't include if also written (was new)
    referenced = read_files - edited_files - written_files  # Only if not modified or written

    # Build output lists with filtering
    result: dict[str, list[dict[str, str]]] = {
        "created": [],
        "modified": [],
        "referenced": []
    }

    for path in sorted(created):
        if is_in_project(path):
            rel_path = make_relative(path)
            result["created"].append({
                "path": rel_path,
                "type": get_file_type(path),
                "description": ""  # Can be filled by LLM later
            })

    for path in sorted(modified):
        if is_in_project(path):
            rel_path = make_relative(path)
            result["modified"].append({
                "path": rel_path,
                "type": get_file_type(path),
                "description": ""
            })

    for path in sorted(referenced):
        if is_in_project(path):
            rel_path = make_relative(path)
            result["referenced"].append({
                "path": rel_path,
                "type": get_file_type(path),
                "description": ""
            })

    return result


# =============================================================================
# v1.1: Relationship Detection
# =============================================================================

def detect_relationship_hints(session_path: Path) -> dict[str, Any]:
    """
    Detect potential session relationships from conversation context.

    Looks for mentions of:
    - Previous sessions ("continuing from", session IDs)
    - Session references
    - Continuation patterns

    These are hints for user confirmation, not auto-applied relationships.

    Args:
        session_path: Path to the session JSONL file

    Returns:
        Dictionary with detected relationship hints
    """
    hints = {
        "continues_hint": None,
        "references_hints": [],
        "detection_notes": []
    }

    # Patterns to detect session references
    uuid_pattern = re.compile(
        r'\b([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})\b',
        re.IGNORECASE
    )
    continuation_patterns = [
        r'continu(?:e|ing|ed)\s+from',
        r'pick(?:ing)?\s+up\s+(?:from\s+)?where',
        r'previous\s+session',
        r'last\s+session',
        r'earlier\s+(?:session|conversation)',
    ]

    with open(session_path, 'r') as f:
        for line in f:
            if not line.strip():
                continue

            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue

            message = entry.get("message", {})
            role = message.get("role", "")

            # Only check human messages for relationship hints
            if role != "user":
                continue

            content = message.get("content", "")
            if isinstance(content, list):
                # Extract text from content blocks
                content = " ".join(
                    block.get("text", "")
                    for block in content
                    if isinstance(block, dict) and block.get("type") == "text"
                )

            if not isinstance(content, str):
                continue

            # Look for session UUIDs
            for match in uuid_pattern.finditer(content):
                uuid_str = match.group(1)
                if uuid_str not in hints["references_hints"]:
                    hints["references_hints"].append(uuid_str)
                    hints["detection_notes"].append(
                        f"Found session ID reference: {uuid_str}"
                    )

            # Look for continuation language
            for pattern in continuation_patterns:
                if re.search(pattern, content, re.IGNORECASE):
                    if not hints["continues_hint"]:
                        hints["detection_notes"].append(
                            f"Found continuation language: '{pattern}'"
                        )
                        # Could potentially set continues_hint here if a session ID
                        # is found nearby, but we leave it for manual confirmation

    return hints


# =============================================================================
# Metadata Generation
# =============================================================================

def generate_metadata_prompt(session_id: str, stats: dict[str, Any]) -> str:
    """
    Generate a prompt for CC to create session metadata.

    This is printed to stdout so CC can respond with the metadata JSON.
    """
    prompt = f"""
I need you to generate metadata for archiving the CC session that just completed.

**Session ID**: {session_id}
**Duration**: {stats['duration_minutes']} minutes
**Turns**: {stats['turns']} ({stats['human_messages']} human, {stats['assistant_messages']} assistant)
**Thinking blocks**: {stats['thinking_blocks']}
**Tool calls**: {stats['tool_calls']['total']} ({', '.join(f"{k}: {v}" for k, v in stats['tool_calls']['by_type'].items())})
**Tokens**: {stats['tokens']['input']:,} input, {stats['tokens']['output']:,} output

Based on our conversation, please provide the following in JSON format:

```json
{{
  "title": "Brief descriptive title (5-10 words)",
  "purpose": "What the user was trying to accomplish (1-2 sentences)",
  "tags": ["tag1", "tag2", "tag3"],
  "three_ps": {{
    "prompt_summary": "What was asked (Prompt) - 1-2 sentences",
    "process_summary": "How the tool was used (Process) - 1-2 sentences",
    "provenance_summary": "Role in research workflow (Provenance) - 1 sentence"
  }}
}}
```

Please respond with ONLY the JSON block, no other text.
"""
    return prompt.strip()


def create_session_metadata(
    session_id: str,
    session_path: Path,
    stats: dict[str, Any],
    auto_generated: dict[str, Any] | None = None,
    thinking_block_stats: dict[str, Any] | None = None,
    tool_output_stats: dict[str, Any] | None = None,
    artifacts: dict[str, list] | None = None,
    relationship_hints: dict[str, Any] | None = None,
    compression_info: dict[str, Any] | None = None,
    defaults: dict[str, Any] | None = None
) -> dict[str, Any]:
    """
    Create the complete session.meta.json structure (v1.1 schema).

    Args:
        session_id: Session identifier
        session_path: Path to source JSONL file
        stats: Extracted session statistics
        auto_generated: CC-generated metadata (title, purpose, tags, three_ps)
        thinking_block_stats: v1.1 - Thinking block token statistics
        tool_output_stats: v1.1 - Tool output byte statistics
        artifacts: v1.1 - Files created/modified/referenced
        relationship_hints: v1.1 - Detected relationship hints (for confirmation)
        compression_info: v1.1 - Compression metadata (if using gzip)
        defaults: v1.1 - Loaded defaults from archive-defaults.yaml

    Returns:
        Complete metadata dictionary
    """
    defaults = defaults or {}
    thinking_defaults = defaults.get("thinking_blocks", {})
    relationship_defaults = defaults.get("relationships", {})

    # Compute file hash (of uncompressed content)
    sha256_hash = hashlib.sha256()
    with open(session_path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha256_hash.update(chunk)

    project_name = get_project_name()
    project_dir = get_project_directory()

    # Build thinking_blocks section (v1.1)
    thinking_stats = thinking_block_stats or {"count": 0, "total_tokens": 0}
    thinking_blocks = {
        "included": True,
        "count": thinking_stats.get("count", stats.get("thinking_blocks", 0)),
        "total_tokens": thinking_stats.get("total_tokens", 0),
        "token_count_method": thinking_stats.get("token_count_method", "estimated"),
        "sharing_preference": thinking_defaults.get(
            "sharing_preference", DEFAULT_THINKING_SHARING
        ),
        "use_constraints": thinking_defaults.get(
            "use_constraints", DEFAULT_THINKING_USE_CONSTRAINTS
        ),
        "excluded_uses": thinking_defaults.get(
            "excluded_uses", DEFAULT_THINKING_EXCLUDED_USES
        ),
        "nature_note": DEFAULT_THINKING_NATURE_NOTE
    }

    # Build relationships section (v1.1)
    # Default isPartOf from config, else use project name
    default_is_part_of = relationship_defaults.get(
        "default_isPartOf", [project_name]
    )
    relationships = {
        "continues": None,  # To be confirmed by user if hints detected
        "continuedBy": None,  # Populated later by catalog
        "isPartOf": default_is_part_of,
        "isParallelTo": [],
        "supersedes": None,
        "references": [],
        "branchesFrom": None
    }

    # Include relationship hints for user review (but don't auto-apply)
    relationship_hints_info = relationship_hints or {}

    # Build statistics section with tool_outputs (v1.1)
    tool_outputs = tool_output_stats or {
        "total_bytes": 0,
        "by_type": {},
        "largest_single_output_bytes": 0
    }

    statistics = {
        "turns": stats["turns"],
        "human_messages": stats["human_messages"],
        "assistant_messages": stats["assistant_messages"],
        "thinking_blocks": stats["thinking_blocks"],
        "tool_calls": stats["tool_calls"],
        "tokens": stats["tokens"],
        "estimated_cost_usd": estimate_cost(stats),
        "tool_outputs": tool_outputs  # v1.1
    }

    # Build archive section with compression support (v1.1)
    archive = {
        "jsonl_path": "session.jsonl",
        "jsonl_sha256": sha256_hash.hexdigest(),
        "jsonl_bytes": session_path.stat().st_size,
        "archived_at": datetime.now().isoformat()
    }

    # Add compression metadata if using gzip (v1.1)
    if compression_info:
        archive["jsonl_path"] = compression_info.get("path", "session.jsonl.gz")
        archive["jsonl_compression"] = compression_info.get("compression", "gzip")
        archive["jsonl_bytes_compressed"] = compression_info.get("compressed_bytes", 0)
        archive["jsonl_bytes_uncompressed"] = compression_info.get(
            "uncompressed_bytes", session_path.stat().st_size
        )
        archive["jsonl_sha256_uncompressed"] = sha256_hash.hexdigest()
        # Compressed hash will be added by caller after compression
        if "compressed_sha256" in compression_info:
            archive["jsonl_sha256"] = compression_info["compressed_sha256"]

    metadata = {
        "schema_version": SCHEMA_VERSION,
        "session": {
            "id": session_id,
            "started_at": stats["started_at"],
            "ended_at": stats["ended_at"],
            "duration_minutes": stats["duration_minutes"]
        },
        "project": {
            "name": project_name,
            "directory": str(project_dir)
        },
        "model": {
            "provider": "anthropic",
            "model_id": stats.get("model", "unknown"),
            "access_method": "claude-code-cli"
        },
        "thinking_blocks": thinking_blocks,  # v1.1
        "relationships": relationships,  # v1.1
        "artifacts": artifacts or {  # v1.1
            "created": [],
            "modified": [],
            "referenced": []
        },
        "statistics": statistics,
        "auto_generated": auto_generated or {
            "title": "Untitled Session",
            "purpose": "No description provided",
            "tags": []
        },
        "three_ps": (auto_generated or {}).get("three_ps", {
            "prompt_summary": "",
            "process_summary": "",
            "provenance_summary": ""
        }),
        "archive": archive
    }

    # Add relationship hints as separate field for user review (not in schema)
    # These are hints only, not auto-applied relationships
    if relationship_hints_info.get("detection_notes"):
        metadata["_relationship_hints"] = relationship_hints_info

    return metadata


# =============================================================================
# Archive Operations
# =============================================================================

def get_archive_directory(session_id: str, stats: dict[str, Any]) -> Path:
    """
    Determine the archive directory for a session.

    Format: archive/cc-sessions/{project}/{timestamp}_{id}/
    Timestamp: YYYY-MM-DDTHH-MM (from session start)
    ID: First 8 characters of session ID for uniqueness
    """
    project_name = get_project_name()

    # Get short ID for uniqueness (handles both UUID and agent-xxx formats)
    if session_id.startswith("agent-"):
        short_id = session_id  # Keep full agent ID (already short)
    else:
        short_id = session_id[:8]  # First 8 chars of UUID

    # Parse timestamp for directory name
    if stats["started_at"]:
        try:
            dt = datetime.fromisoformat(stats["started_at"].replace("Z", "+00:00"))
            timestamp_dir = f"{dt.strftime('%Y-%m-%dT%H-%M')}_{short_id}"
        except (ValueError, TypeError):
            timestamp_dir = short_id
    else:
        timestamp_dir = short_id

    return ARCHIVE_DIR / project_name / timestamp_dir


def archive_session(
    session_path: Path,
    dry_run: bool = False,
    stats_only: bool = False,
    use_gzip: bool = False
) -> dict[str, Any] | None:
    """
    Archive a single session with v1.1 schema.

    Args:
        session_path: Path to source JSONL file
        dry_run: If True, print what would be done without archiving
        stats_only: If True, skip CC metadata generation
        use_gzip: If True, compress the JSONL file

    Returns:
        Session metadata dict, or None if skipped
    """
    session_id = get_session_id(session_path)
    stats = extract_session_stats(session_path)
    archive_dir = get_archive_directory(session_id, stats)

    # Load defaults from config file (v1.1)
    defaults = load_defaults()

    print(f"\nSession: {session_id}")
    print(f"  Source: {session_path}")
    print(f"  Archive: {archive_dir}")
    print(f"  Duration: {stats['duration_minutes']} min, {stats['turns']} turns")
    print(f"  Model: {stats.get('model', 'unknown')}")

    if dry_run:
        print("  [DRY RUN] Would archive this session")
        return None

    # Extract v1.1 statistics
    print("  Extracting v1.1 metadata...")
    thinking_block_stats = extract_thinking_block_tokens(session_path)
    tool_output_stats = extract_tool_output_bytes(session_path)
    artifacts = extract_artifacts(session_path)
    relationship_hints = detect_relationship_hints(session_path)

    # Print v1.1 extraction summary
    print(f"    Thinking blocks: {thinking_block_stats['count']} "
          f"(~{thinking_block_stats['total_tokens']:,} tokens estimated)")
    print(f"    Tool outputs: {tool_output_stats['total_bytes']:,} bytes total")
    print(f"    Artifacts: {len(artifacts['created'])} created, "
          f"{len(artifacts['modified'])} modified, "
          f"{len(artifacts['referenced'])} referenced")

    if relationship_hints.get("detection_notes"):
        print("    Relationship hints detected:")
        for note in relationship_hints["detection_notes"][:3]:  # Show first 3
            print(f"      - {note}")

    # Create archive directory
    archive_dir.mkdir(parents=True, exist_ok=True)

    # Copy JSONL file with compression handling (v1.1)
    compression_info = None
    dest_jsonl = archive_dir / "session.jsonl"

    if use_gzip:
        dest_jsonl = archive_dir / "session.jsonl.gz"
        uncompressed_size = session_path.stat().st_size

        # Compress the file
        with open(session_path, 'rb') as f_in:
            with gzip.open(dest_jsonl, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

        # Compute hash of compressed file
        compressed_hash = hashlib.sha256()
        with open(dest_jsonl, 'rb') as f:
            for chunk in iter(lambda: f.read(8192), b""):
                compressed_hash.update(chunk)

        compression_info = {
            "path": "session.jsonl.gz",
            "compression": "gzip",
            "compressed_bytes": dest_jsonl.stat().st_size,
            "uncompressed_bytes": uncompressed_size,
            "compressed_sha256": compressed_hash.hexdigest()
        }
        print(f"  Compressed to: {dest_jsonl} "
              f"({compression_info['compressed_bytes']:,} bytes, "
              f"{compression_info['compressed_bytes'] / uncompressed_size * 100:.1f}% of original)")
    else:
        shutil.copy2(session_path, dest_jsonl)
        print(f"  Copied to: {dest_jsonl}")

    # Generate metadata
    auto_generated = None
    if not stats_only:
        print("\n" + "=" * 60)
        print("METADATA GENERATION")
        print("=" * 60)
        print(generate_metadata_prompt(session_id, stats))
        print("=" * 60)
        print("\nPlease provide the JSON metadata above, or press Enter to skip.")
        print("(The script will wait for your input...)\n")

        # In interactive mode, we'd read from stdin here
        # For now, we'll use placeholder metadata
        auto_generated = {
            "title": "Untitled Session",
            "purpose": "Metadata generation requires interactive CC session",
            "tags": [],
            "three_ps": {
                "prompt_summary": "",
                "process_summary": "",
                "provenance_summary": ""
            }
        }

    # Create v1.1 metadata with all extracted information
    metadata = create_session_metadata(
        session_id=session_id,
        session_path=session_path,
        stats=stats,
        auto_generated=auto_generated,
        thinking_block_stats=thinking_block_stats,
        tool_output_stats=tool_output_stats,
        artifacts=artifacts,
        relationship_hints=relationship_hints,
        compression_info=compression_info,
        defaults=defaults
    )

    # Save metadata
    metadata_path = archive_dir / "session.meta.json"
    metadata_path.write_text(json.dumps(metadata, indent=2))
    print(f"  Metadata: {metadata_path}")

    return metadata


def update_catalog(new_sessions: list[dict[str, Any]]) -> None:
    """
    Update CATALOG.json with newly archived sessions.

    Args:
        new_sessions: List of session metadata dictionaries
    """
    # Load existing catalog
    if CATALOG_FILE.exists():
        try:
            catalog = json.loads(CATALOG_FILE.read_text())
        except json.JSONDecodeError:
            catalog = {"schema_version": SCHEMA_VERSION, "sessions": []}
    else:
        catalog = {"schema_version": SCHEMA_VERSION, "sessions": []}

    # Add new sessions
    existing_ids = {s["id"] for s in catalog["sessions"]}
    for session in new_sessions:
        if session["session"]["id"] not in existing_ids:
            catalog["sessions"].append({
                "id": session["session"]["id"],
                "title": session["auto_generated"]["title"],
                "directory": str(get_archive_directory(
                    session["session"]["id"],
                    {"started_at": session["session"]["started_at"]}
                ).relative_to(ARCHIVE_DIR)),
                "started_at": session["session"]["started_at"],
                "duration_minutes": session["session"]["duration_minutes"],
                "tags": session["auto_generated"]["tags"],
                "purpose": session["auto_generated"]["purpose"]
            })

    # Update metadata
    catalog["generated_at"] = datetime.now().isoformat()
    catalog["project"] = get_project_name()
    catalog["total_sessions"] = len(catalog["sessions"])

    # Sort by date (handle None values by putting them last)
    catalog["sessions"].sort(key=lambda s: s.get("started_at") or "", reverse=True)

    # Save
    CATALOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    CATALOG_FILE.write_text(json.dumps(catalog, indent=2))
    print(f"\nCatalog updated: {CATALOG_FILE}")


# =============================================================================
# CLI Commands
# =============================================================================

def cmd_list(args: argparse.Namespace) -> None:
    """List all sessions and their archive status."""
    session_files = get_session_files()
    archived_ids = get_archived_session_ids()

    print(f"Sessions for project: {get_project_name()}")
    print(f"Source: {CLAUDE_PROJECTS_DIR / get_cc_project_path()}")
    print()

    if not session_files:
        print("No sessions found.")
        return

    print(f"{'ID':<45} {'Size':>10} {'Modified':>20} {'Archived':>10}")
    print("-" * 90)

    for session_path in session_files:
        session_id = get_session_id(session_path)
        size_mb = session_path.stat().st_size / (1024 * 1024)
        modified = datetime.fromtimestamp(session_path.stat().st_mtime).strftime("%Y-%m-%d %H:%M")
        archived = "Yes" if session_id in archived_ids else "No"

        print(f"{session_id:<45} {size_mb:>9.2f}M {modified:>20} {archived:>10}")

    print()
    print(f"Total: {len(session_files)} sessions, {len(archived_ids)} archived")


def cmd_archive(args: argparse.Namespace) -> None:
    """Archive sessions based on arguments."""
    session_files = get_session_files()
    archived_ids = get_archived_session_ids()

    if not session_files:
        print("No sessions found.")
        return

    # Determine which sessions to archive
    if args.session_id:
        # Archive specific session
        target_sessions = [p for p in session_files if get_session_id(p) == args.session_id]
        if not target_sessions:
            print(f"Session not found: {args.session_id}")
            return
    elif args.all:
        # Archive all unarchived sessions (or all if --force)
        if args.force:
            target_sessions = session_files
        else:
            target_sessions = [
                p for p in session_files
                if get_session_id(p) not in archived_ids
            ]
    else:
        # Archive latest session only
        target_sessions = [session_files[-1]]

    if not target_sessions:
        print("No sessions to archive (all already archived).")
        print("Use --force to re-archive existing sessions.")
        return

    print(f"Archiving {len(target_sessions)} session(s)...")

    # Archive each session
    new_sessions = []
    for session_path in target_sessions:
        result = archive_session(
            session_path,
            dry_run=args.dry_run,
            stats_only=args.stats_only,
            use_gzip=args.gzip
        )
        if result:
            new_sessions.append(result)

    # Update catalog
    if new_sessions and not args.dry_run:
        update_catalog(new_sessions)

    print("\nDone!")


def find_archive_by_id(session_id: str) -> Path | None:
    """Find an archive directory by session ID (full or partial match)."""
    if not ARCHIVE_DIR.exists():
        return None

    project_dir = ARCHIVE_DIR / get_project_name()
    if not project_dir.exists():
        return None

    # Look for directories containing the session ID
    for archive_dir in project_dir.iterdir():
        if archive_dir.is_dir() and session_id in archive_dir.name:
            return archive_dir

    return None


def cmd_update_metadata(args: argparse.Namespace) -> None:
    """Update metadata for an archived session."""
    session_id = args.update_metadata

    # Find the archive
    archive_dir = find_archive_by_id(session_id)
    if not archive_dir:
        print(f"Archive not found for session: {session_id}")
        print("Use --list to see archived sessions.")
        return

    meta_file = archive_dir / "session.meta.json"
    if not meta_file.exists():
        print(f"Metadata file not found: {meta_file}")
        return

    # Load existing metadata
    meta = json.loads(meta_file.read_text())
    print(f"Updating metadata for: {archive_dir.name}")
    print(f"Current title: {meta.get('auto_generated', {}).get('title', 'None')}")

    # Read new metadata from stdin or file
    if args.metadata_file:
        new_meta = json.loads(Path(args.metadata_file).read_text())
    else:
        print("\nEnter metadata JSON (Ctrl+D when done):")
        import sys
        try:
            new_meta = json.loads(sys.stdin.read())
        except json.JSONDecodeError as e:
            print(f"Invalid JSON: {e}")
            return

    # Update fields
    if "title" in new_meta:
        meta["auto_generated"]["title"] = new_meta["title"]
    if "purpose" in new_meta:
        meta["auto_generated"]["purpose"] = new_meta["purpose"]
    if "tags" in new_meta:
        meta["auto_generated"]["tags"] = new_meta["tags"]
    if "three_ps" in new_meta:
        meta["three_ps"] = new_meta["three_ps"]

    # Save updated metadata
    if not args.dry_run:
        meta_file.write_text(json.dumps(meta, indent=2))
        print(f"\nUpdated: {meta_file}")

        # Update catalog
        update_catalog_entry(session_id, meta)
        print("Catalog updated.")
    else:
        print("\n[DRY RUN] Would update metadata to:")
        print(json.dumps(meta["auto_generated"], indent=2))


def update_catalog_entry(session_id: str, meta: dict[str, Any]) -> None:
    """Update a single session's entry in the catalog."""
    if not CATALOG_FILE.exists():
        return

    catalog = json.loads(CATALOG_FILE.read_text())

    for session in catalog.get("sessions", []):
        if session_id in session.get("id", ""):
            session["title"] = meta.get("auto_generated", {}).get("title", "Untitled")
            session["purpose"] = meta.get("auto_generated", {}).get("purpose", "")
            session["tags"] = meta.get("auto_generated", {}).get("tags", [])
            break

    catalog["generated_at"] = datetime.now().isoformat()
    CATALOG_FILE.write_text(json.dumps(catalog, indent=2))


def cmd_summarize(args: argparse.Namespace) -> None:
    """Extract summary information from a session to help generate metadata."""
    session_id = args.summarize

    # Find the archive
    archive_dir = find_archive_by_id(session_id)
    if not archive_dir:
        print(f"Archive not found for session: {session_id}")
        return

    # Find the session file (jsonl or jsonl.gz)
    session_file = archive_dir / "session.jsonl"
    if not session_file.exists():
        session_file = archive_dir / "session.jsonl.gz"
        if not session_file.exists():
            print(f"Session file not found in: {archive_dir}")
            return

    # Load and parse
    print(f"Analysing: {archive_dir.name}")
    print("=" * 60)

    if session_file.suffix == ".gz":
        with gzip.open(session_file, "rt", encoding="utf-8") as f:
            lines = f.readlines()
    else:
        lines = session_file.read_text().splitlines()

    # Extract key information
    first_human_msg = None
    last_human_msg = None
    human_messages = []
    tool_types = set()
    files_modified = set()

    for line in lines:
        if not line.strip():
            continue
        try:
            entry = json.loads(line)
            msg_type = entry.get("type")

            # Handle user messages (type: "user" with userType: "external")
            if msg_type == "user" and entry.get("userType") == "external":
                message = entry.get("message", {})
                content = message.get("content", "") if isinstance(message, dict) else ""
                if isinstance(content, str) and content.strip():
                    if first_human_msg is None:
                        first_human_msg = content[:500]
                    last_human_msg = content[:500]
                    human_messages.append(content[:200])
                # Also handle list content (multimodal messages)
                elif isinstance(content, list):
                    for block in content:
                        if isinstance(block, dict) and block.get("type") == "text":
                            text = block.get("text", "")
                            if text.strip():
                                if first_human_msg is None:
                                    first_human_msg = text[:500]
                                last_human_msg = text[:500]
                                human_messages.append(text[:200])
                                break

            elif msg_type == "assistant":
                message = entry.get("message", {})
                for content_block in message.get("content", []):
                    if content_block.get("type") == "tool_use":
                        tool_name = content_block.get("name", "")
                        tool_types.add(tool_name)
                        # Track file modifications
                        if tool_name in ("Edit", "Write"):
                            inp = content_block.get("input", {})
                            if "file_path" in inp:
                                files_modified.add(inp["file_path"])

        except json.JSONDecodeError:
            continue

    # Print summary
    print(f"\n**First user message:**\n{first_human_msg}\n")
    print(f"**Last user message:**\n{last_human_msg}\n")
    print(f"**Tools used:** {', '.join(sorted(tool_types)) or 'None'}")
    print(f"**Files modified:** {len(files_modified)}")
    if files_modified and len(files_modified) <= 20:
        for f in sorted(files_modified)[:20]:
            print(f"  - {f}")

    # Load existing metadata for context
    meta_file = archive_dir / "session.meta.json"
    if meta_file.exists():
        meta = json.loads(meta_file.read_text())
        stats = meta.get("statistics", {})
        print(f"\n**Statistics:**")
        print(f"  Turns: {stats.get('turns', 'N/A')}")
        print(f"  Duration: {meta.get('session', {}).get('duration_minutes', 'N/A')} minutes")
        print(f"  Tool calls: {stats.get('tool_calls', {}).get('total', 'N/A')}")

    # Suggest metadata template
    print("\n" + "=" * 60)
    print("**Suggested metadata template:**")
    print("=" * 60)
    print("""
{
  "title": "[TODO: Brief title based on above]",
  "purpose": "[TODO: 1-2 sentence purpose]",
  "tags": ["llm-reproducibility", "TODO"],
  "three_ps": {
    "prompt_summary": "[TODO: What was asked]",
    "process_summary": "[TODO: How the tool was used]",
    "provenance_summary": "[TODO: Role in research workflow]"
  }
}
""")


def cmd_list_archives(args: argparse.Namespace) -> None:
    """List archived sessions with their metadata status."""
    project_dir = ARCHIVE_DIR / get_project_name()
    if not project_dir.exists():
        print("No archives found.")
        return

    print(f"Archived sessions for: {get_project_name()}")
    print(f"Location: {project_dir}")
    print()

    # Header
    print(f"{'Directory':<50} {'Title':<30} {'Complete':<10}")
    print("-" * 90)

    incomplete_count = 0
    for archive_dir in sorted(project_dir.iterdir()):
        if not archive_dir.is_dir():
            continue

        meta_file = archive_dir / "session.meta.json"
        title = "N/A"
        complete = "No"

        if meta_file.exists():
            meta = json.loads(meta_file.read_text())
            title = meta.get("auto_generated", {}).get("title", "Untitled")
            # Check if metadata is complete
            three_ps = meta.get("three_ps", {})
            if (title != "Untitled Session" and
                three_ps.get("prompt_summary") and
                three_ps.get("process_summary")):
                complete = "Yes"
            else:
                incomplete_count += 1

        # Truncate for display
        dir_name = archive_dir.name[:48]
        title_display = title[:28] if title else "N/A"

        print(f"{dir_name:<50} {title_display:<30} {complete:<10}")

    print()
    print(f"Total: {len(list(project_dir.iterdir()))} archives, {incomplete_count} need metadata")


# =============================================================================
# Main
# =============================================================================

def main() -> None:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Archive Claude Code sessions for research transparency",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                    Archive the latest session
  %(prog)s --list             List all sessions and archive status
  %(prog)s --all              Archive all unarchived sessions
  %(prog)s --session-id UUID  Archive a specific session
  %(prog)s --dry-run          Preview without archiving

Note: Run this script within a CC session for interactive metadata generation.
The current/active session cannot be archived until it ends.
        """
    )

    parser.add_argument(
        "--list", "-l",
        action="store_true",
        help="List all sessions and their archive status"
    )
    parser.add_argument(
        "--session-id", "-s",
        help="Archive a specific session by ID"
    )
    parser.add_argument(
        "--all", "-a",
        action="store_true",
        help="Archive all unarchived sessions"
    )
    parser.add_argument(
        "--force", "-f",
        action="store_true",
        help="Re-archive sessions even if already archived"
    )
    parser.add_argument(
        "--dry-run", "-n",
        action="store_true",
        help="Preview what would be done without archiving"
    )
    parser.add_argument(
        "--stats-only",
        action="store_true",
        help="Skip CC metadata generation (use placeholder metadata)"
    )
    parser.add_argument(
        "--gzip", "-z",
        action="store_true",
        help="Compress JSONL files with gzip"
    )

    # Metadata management commands
    parser.add_argument(
        "--update-metadata", "-u",
        metavar="SESSION_ID",
        help="Update metadata for an archived session"
    )
    parser.add_argument(
        "--metadata-file", "-m",
        metavar="FILE",
        help="JSON file containing metadata (use with --update-metadata)"
    )
    parser.add_argument(
        "--summarize",
        metavar="SESSION_ID",
        help="Analyse a session and suggest metadata"
    )
    parser.add_argument(
        "--list-archives",
        action="store_true",
        help="List archived sessions with metadata completion status"
    )

    args = parser.parse_args()

    print("=" * 60)
    print("CC Session Archiver")
    print("=" * 60)
    print(f"Project: {get_project_name()}")
    print()

    if args.list:
        cmd_list(args)
    elif args.list_archives:
        cmd_list_archives(args)
    elif args.update_metadata:
        cmd_update_metadata(args)
    elif args.summarize:
        cmd_summarize(args)
    else:
        cmd_archive(args)


if __name__ == "__main__":
    main()
