# Claude Code Session Archival â€” Implementation Brief

**Purpose**: Implement automated, reliable capture of all Claude Code interactions for research transparency and publication.

**User context**: Shawn publishes research on LLM use in historical/archaeological research and needs comprehensive chat histories for analysis and transparency.

---

## Problem Statement

Shawn has been manually running `/export` before `/compact` to preserve CC session transcripts, but:
- Sometimes misses auto-compacts (triggered at 95% context capacity)
- Manual process is error-prone
- Unclear what data was actually at risk

---

## Key Research Findings

### 1. Claude Code Already Stores Everything

CC automatically captures all interactions to local JSONL files:

| Location | Content |
|----------|---------|
| `~/.claude/history.jsonl` | Index of all sessions (metadata) |
| `~/.claude/projects/{encoded-path}/` | Full conversation data per project |

Each session JSONL contains:
- All user messages
- All assistant responses  
- Tool executions (file edits, bash commands, searches)
- Tool outputs and results
- Sidechains (subagent/parallel work)
- Session metadata and timestamps

### 2. `/clear` and `/compact` Don't Delete Stored Data

These commands only affect the **active context window** â€” what Claude can "see" in the current session. The JSONL files on disk are **not affected**.

| Action | Context Window | JSONL Files |
|--------|---------------|-------------|
| `/clear` | Wiped | Unchanged |
| `/compact` | Summarized | Unchanged |
| Auto-compact | Summarized | Unchanged |

### 3. Default 30-Day Auto-Deletion

CC silently deletes session files after 30 days by default. This is the actual risk â€” not `/compact`.

**Fix**: Add to `~/.claude/settings.json`:
```json
{
  "cleanupPeriodDays": 99999
}
```

This has already been applied temporarily.

### 4. Manual `/export` is Now Redundant

Since JSONL files persist and contain complete data, manual exports are unnecessary. The JSONL can be converted to human-readable formats at any time.

---

## Recommended Solution

### Architecture

```
~/.claude/projects/     (source - JSONL files, auto-captured)
        â†“
   [cron job - daily]
        â†“
~/claude-archives/      (git repo)
â”œâ”€â”€ jsonl/              (raw JSONL - machine-readable, complete)
â”œâ”€â”€ markdown/           (human-readable transcripts)
â””â”€â”€ archive.log         (processing log)
        â†“
   [git push to GitHub]
```

### Requirements

1. **Preserve raw JSONL** â€” authoritative record, supports future analysis
2. **Generate markdown** â€” human-readable for publication/sharing
3. **Git versioning** â€” change tracking, backup, transparency
4. **GitHub sync** â€” offsite backup, public transparency option
5. **Idempotent** â€” safe to re-run, doesn't duplicate exports
6. **Incremental** â€” only processes new/changed sessions

---

## Recommended Tooling

### Primary: `claude-conversation-extractor`

**Source**: https://github.com/ZeroSumQuant/claude-conversation-extractor

**Install**:
```bash
pipx install claude-conversation-extractor
```

**Key features**:
- Finds CC logs automatically in `~/.claude/projects/`
- Exports to markdown, JSON, or HTML
- `--detailed` flag includes tool use, MCP responses, system messages
- `--all` flag for batch processing
- `--output` flag for custom destination
- Search capability across sessions

**Relevant commands**:
```bash
# List all sessions
claude-extract --list

# Export all to markdown
claude-extract --all --output ~/claude-archives/markdown/

# Export all to JSON (preserves full structure)
claude-extract --all --format json --output ~/claude-archives/json/

# Export with full detail (tool calls, etc.)
claude-extract --all --detailed --output ~/claude-archives/detailed/
```

### Alternative Tools (if needed)

| Tool | Source | Notes |
|------|--------|-------|
| `claude-code-log` | github.com/daaain/claude-code-log | HTML output, TUI browser, date filtering |
| `claude-transcript` | github.com/jflam/claude-transcript | Lightweight, GitHub Gist upload |
| `SpecStory` | docs.specstory.com | `specstory sync claude` command |
| `claude-code-exporter` | npm | Period filtering (`--period=7d`), aggregation |

---

## Implementation Tasks

### 1. Permanent Settings Configuration

Ensure `~/.claude/settings.json` contains:
```json
{
  "cleanupPeriodDays": 99999
}
```

### 2. Create Archive Repository

```bash
mkdir -p ~/claude-archives/{jsonl,markdown}
cd ~/claude-archives
git init
# Create .gitignore if needed (probably want to track everything)
```

### 3. Create Archive Script

Script should:
- Copy new/changed JSONL files to `jsonl/` directory
- Run extractor to generate markdown versions
- Commit changes with timestamp
- Optionally push to GitHub

### 4. Configure Cron Job

Daily execution (e.g., 2am):
```bash
0 2 * * * /path/to/archive-claude-sessions.sh
```

### 5. Initial Backfill

Run extractor on all existing sessions to populate archive with historical data.

---

## Open Questions for Implementation

1. **JSONL handling**: Copy raw files directly, or rely on extractor's JSON output? (Raw preserves everything; extractor output may be cleaner but potentially lossy)

2. **Deduplication**: How to detect already-processed sessions? (By filename? By content hash? By modification time?)

3. **GitHub repo visibility**: Public (maximum transparency) or private (then selectively publish)?

4. **Retention in archive**: Keep everything forever, or implement rotation for very old sessions?

5. **Error handling**: What to do if extraction fails for a session? Log and continue? Alert?

---

## Success Criteria

- [ ] All CC sessions automatically archived within 24 hours
- [ ] Both JSONL (raw) and markdown (readable) formats preserved
- [ ] Archive is git-versioned with meaningful commits
- [ ] Archive syncs to GitHub for offsite backup
- [ ] No manual intervention required
- [ ] Historical sessions backfilled
- [ ] Solution survives CC updates and system restarts

---

## References

- CC stores sessions: `~/.claude/projects/{encoded-path}/*.jsonl`
- CC session index: `~/.claude/history.jsonl`  
- Settings location: `~/.claude/settings.json`
- Extractor repo: https://github.com/ZeroSumQuant/claude-conversation-extractor
- CC settings docs: https://docs.anthropic.com/claude-code/settings