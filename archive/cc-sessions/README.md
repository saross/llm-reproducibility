# CC Session Archive

This directory contains archived Claude Code (CC) session transcripts for research transparency and reproducibility, following FAIR (Findable, Accessible, Interoperable, Reusable) principles.

## Overview

Claude Code sessions are stored as JSONL (JSON Lines) files in `~/.claude/projects/`. This archive captures complete session transcripts including:

- Human-assistant conversation turns
- Thinking traces (extended thinking blocks)
- Tool calls and their outputs
- Token usage and timing metadata

## Directory Structure

```text
archive/cc-sessions/
├── README.md                           # This file
├── CATALOG.json                        # Machine-readable session index
├── queries/                            # LLM query prompts
│   ├── README.md
│   ├── summarise-session.md
│   ├── extract-decisions.md
│   ├── extract-artifacts.md
│   ├── extract-methodology.md
│   ├── extract-issues.md
│   └── populate-metadata.md            # Generate metadata via LLM
└── {project-name}/                     # Sessions grouped by project
    └── {YYYY-MM-DDTHH-MM}_{id}/        # Session directory (timestamp + ID)
        ├── session.jsonl               # Full session transcript
        └── session.meta.json           # Structured metadata (v1.1)
```

## Using the Archive

### Archiving Sessions

Archive CC sessions using the provided script:

```bash
# Archive the latest session
python3 scripts/archive-cc-session.py

# Archive a specific session
python3 scripts/archive-cc-session.py --session-id UUID

# Archive all unarchived sessions
python3 scripts/archive-cc-session.py --all

# List sessions and archive status
python3 scripts/archive-cc-session.py --list
```

**Note**: The current/active session cannot be archived until it ends. Run the archive script in a new session to archive previous ones.

### Managing Session Metadata

The archive script includes commands for managing session metadata:

```bash
# List archives and their metadata status
python3 scripts/archive-cc-session.py --list-archives

# Summarise a session for metadata generation
python3 scripts/archive-cc-session.py --summarize SESSION_ID

# Update metadata for an archived session
python3 scripts/archive-cc-session.py --update-metadata SESSION_ID -m metadata.json
```

### Populating Metadata with LLM Assistance

The recommended workflow for generating session metadata:

1. **Summarise the session** to get key information:
   ```bash
   python3 scripts/archive-cc-session.py --summarize SESSION_ID
   ```

2. **Generate metadata using Claude Code** by reading the transcript and applying the prompt from `queries/populate-metadata.md`:
   - Read the session transcript (`session.jsonl`)
   - Apply the populate-metadata.md prompt
   - Claude generates structured metadata JSON

3. **Apply the generated metadata**:
   ```bash
   python3 scripts/archive-cc-session.py --update-metadata SESSION_ID -m /tmp/metadata.json
   ```

See `queries/populate-metadata.md` for the full prompt and JSON schema.

### Querying Sessions with LLMs

Rather than pre-generating views, use the query prompts in `queries/` to extract information on demand:

1. Open a session JSONL file in Claude (or provide it as context)
2. Include the appropriate query prompt
3. The LLM will extract the requested information

Available queries:

- `summarise-session.md` - Executive summary
- `extract-decisions.md` - Decisions, conclusions, commitments
- `extract-artifacts.md` - Files created/modified/referenced
- `extract-methodology.md` - Methods documentation for papers
- `extract-issues.md` - Errors, issues, resolutions
- `populate-metadata.md` - Generate metadata for archiving

## Session Metadata (v1.1)

Each `session.meta.json` contains the following structure:

```json
{
  "schema_version": "1.1",
  "session": {
    "id": "UUID",
    "started_at": "ISO8601",
    "ended_at": "ISO8601",
    "duration_minutes": 150
  },
  "project": {
    "name": "project-name",
    "directory": "/path/to/project"
  },
  "model": {
    "provider": "anthropic",
    "model_id": "claude-opus-4-5-20251101",
    "access_method": "claude-code-cli"
  },
  "thinking_blocks": {
    "included": true,
    "count": 89,
    "total_tokens": 67000,
    "token_count_method": "estimated",
    "sharing_preference": "research-only",
    "use_constraints": ["analysis-for-improvement", "research-publication-aggregated"],
    "excluded_uses": ["training-data", "public-display-individual"],
    "nature_note": "Work-in-progress reasoning traces..."
  },
  "relationships": {
    "continues": null,
    "continuedBy": null,
    "isPartOf": ["project-name"],
    "isParallelTo": [],
    "supersedes": null,
    "references": [],
    "branchesFrom": null
  },
  "artifacts": {
    "created": [{"path": "scripts/new.py", "type": "code", "description": "..."}],
    "modified": [{"path": "README.md", "type": "document", "description": "..."}],
    "referenced": [{"path": "docs/spec.md", "type": "document", "description": "..."}]
  },
  "statistics": {
    "turns": 47,
    "human_messages": 24,
    "assistant_messages": 23,
    "thinking_blocks": 89,
    "tool_calls": { "total": 156, "by_type": {"Read": 45, "Edit": 32, "Bash": 67} },
    "tokens": {
      "input": 125000,
      "output": 45000,
      "cache_read": 80000
    },
    "estimated_cost_usd": 0.85,
    "tool_outputs": {
      "total_bytes": 4567890,
      "by_type": {"Read": {"count": 45, "bytes": 2345678}, "...": "..."},
      "largest_single_output_bytes": 234567
    }
  },
  "auto_generated": {
    "title": "Brief descriptive title",
    "purpose": "What the user was trying to accomplish",
    "tags": ["tag1", "tag2"]
  },
  "three_ps": {
    "prompt_summary": "What was asked (Prompt)",
    "process_summary": "How the tool was used (Process)",
    "provenance_summary": "Role in research workflow (Provenance)"
  },
  "archive": {
    "jsonl_path": "session.jsonl",
    "jsonl_sha256": "...",
    "jsonl_bytes": 1234567,
    "archived_at": "ISO8601"
  }
}
```

### The Three Ps Framework

The `three_ps` section captures documentation at three complementary levels:

- **Prompt**: What was asked - the user's goals and requests
- **Process**: How the tool was used - methods and approaches taken
- **Provenance**: Role in research workflow - how this session fits into larger project context

This framework supports research transparency by documenting not just the outputs but the context in which they were produced.

### v1.1 Schema Additions

The v1.1 schema adds several new sections:

**thinking_blocks**: Ethics metadata for extended thinking traces

- `sharing_preference`: One of `full`, `research-only`, `project-only`, `redacted`, `excluded`
- `use_constraints`: Permitted uses (e.g., `analysis-for-improvement`)
- `excluded_uses`: Explicitly prohibited uses (e.g., `training-data`)

**relationships**: Session linking using RDF-style predicates

- `continues`/`continuedBy`: Session continuation chains
- `isPartOf`: Project/sprint groupings
- `supersedes`/`references`: Cross-references

**artifacts**: Files created, modified, or referenced during the session

- Automatic deduplication (created+modified → created only)
- Paths filtered to project directory only

**tool_outputs**: Storage analysis for tool results

- Byte counts by tool type
- Useful for analysing session size contributors

## Storage Considerations

- Session JSONL files can grow to 10MB+ for long sessions
- Files are tracked with Git LFS (see `.gitattributes`)
- Optional gzip compression: `--gzip` flag when archiving

## FAIR Principles

This archive aligns with FAIR data principles:

- **Findable**: Sessions indexed in CATALOG.json with searchable metadata
- **Accessible**: Standard formats (JSONL, JSON, Markdown)
- **Interoperable**: Self-describing schema with version tracking
- **Reusable**: Complete transcripts enabling reproduction of AI-assisted work

## Related Documentation

- [Query Prompts](queries/README.md)

---

*This archive supports research transparency for AI-assisted scientific work.*
