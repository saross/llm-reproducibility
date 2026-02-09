# CC Session Query Prompts

This directory contains prompts for extracting information from archived CC sessions using LLM-intermediated access.

## Philosophy

Rather than pre-generating multiple views of each session (summaries, decision logs, artifact lists), we store the complete JSONL transcript and extract information on demand using these query prompts. This approach:

- Avoids information loss from premature summarisation
- Allows context-sensitive extraction
- Enables new query types without re-processing archives
- Supports researcher-specific information needs

## Available Queries

| Query | Purpose | Use When |
|-------|---------|----------|
| `summarise-session.md` | Executive summary | Quick overview of session content |
| `extract-decisions.md` | Decisions, conclusions, commitments | Documenting choices made |
| `extract-artifacts.md` | Files created/modified/referenced | Tracking code changes |
| `extract-methodology.md` | Methods documentation | Writing papers/reports |
| `extract-issues.md` | Errors, issues, resolutions | Debugging, retrospectives |
| `populate-metadata.md` | Fill empty metadata fields | Enriching session.meta.json |

## How to Use

### Method 1: Direct LLM Input

1. Open the session JSONL file in Claude (claude.ai or API)
2. Copy and paste the query prompt content
3. The LLM will process the session and provide the requested information

### Method 2: With Claude Code

1. Start a Claude Code session
2. Read the session file: "Read archive/cc-sessions/{project}/{timestamp}/session.jsonl"
3. Provide the query prompt

### Method 3: Programmatic Access

```python
import json
from pathlib import Path

# Load session
session_path = Path("archive/cc-sessions/project/2025-12-22T03-05/session.jsonl")
with open(session_path) as f:
    entries = [json.loads(line) for line in f if line.strip()]

# Load query prompt
query_path = Path("archive/cc-sessions/queries/extract-decisions.md")
query = query_path.read_text()

# Send to Claude API with session content
# (Implementation depends on your API setup)
```

## Query Output Formats

Each query specifies its expected output format. Common formats include:

- **Markdown tables**: Structured data (artifacts, issues)
- **Bullet lists**: Summaries, key points
- **Prose**: Methodology sections
- **JSON**: Machine-readable output (if requested)

## Creating Custom Queries

To create a custom query:

1. Copy an existing query as a template
2. Specify:
   - What information to extract
   - What context/details to include
   - Desired output format
3. Test with a sample session
4. Save in this directory with descriptive name

## Tips for Effective Queries

- Be specific about what you want extracted
- Specify the output format explicitly
- Include examples in the prompt if helpful
- Request structured output (tables, lists) for later processing
- Ask for context/reasoning when decisions need justification

## Token Considerations

Session JSONL files can be large (10MB+). When querying:

- Consider using Claude's large context window
- For very large sessions, extract relevant portions first
- Use `cc-session summarise SESSION_ID` to get a session overview

---

*These query prompts support LLM-intermediated access to CC session archives.*
