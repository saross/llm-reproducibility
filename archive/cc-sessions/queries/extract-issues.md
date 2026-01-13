# Error and Issue Extraction Query

You are analysing a Claude Code session to identify errors, issues, problems, and their resolutions.

## Task

Extract all instances of:

### 1. Errors Encountered

- Tool failures
- Code errors
- Parsing failures
- API errors

### 2. Issues Identified

- Problems found in documents/code being reviewed
- Inconsistencies discovered
- Gaps or omissions noted

### 3. Misunderstandings

- Cases where the assistant misunderstood the request
- Cases where clarification was needed
- Incorrect assumptions that were corrected

### 4. Resolutions

For each error/issue, note how it was resolved (if it was).

## Output Format

### Errors Encountered

| Error | Context | Resolution | Resolved? |
|-------|---------|------------|-----------|
| Brief description | What was being attempted | How it was fixed | Yes/No/Partial |

### Issues Identified

| Issue | Severity | Location | Resolution |
|-------|----------|----------|------------|
| Brief description | High/Medium/Low | Where found | How addressed |

### Misunderstandings

| Misunderstanding | Clarification | Impact |
|------------------|---------------|--------|
| What was misunderstood | How it was corrected | Effect on session |

## Session Data

[Paste or attach session.jsonl content]
