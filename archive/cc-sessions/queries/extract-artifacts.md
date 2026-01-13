# Artifact Extraction Query

You are analysing a Claude Code session to identify all files that were created, modified, or significantly referenced.

## Task

Identify all artifacts (files) involved in the session:

### 1. Files Created

Files that did not exist before and were created during the session.
Look for: `Write` tool calls, `create_file` operations

### 2. Files Modified

Existing files that were changed during the session.
Look for: `Edit` tool calls, `str_replace` operations

### 3. Files Read/Referenced

Files that were examined but not modified.
Look for: `Read` tool calls, `Glob` results, file content appearing in conversation

## Output Format

For each artifact:

| File | Action | Description | Tool Used |
|------|--------|-------------|-----------|
| path/to/file.md | Created | Brief description | Write |
| other/file.json | Modified | What changed | Edit |
| input/doc.md | Read | Why it was read | Read |

## Additional Information

After the table, note:

- Any files that were created then deleted (intermediate artifacts)
- Any failed file operations (attempted but failed)
- File relationships (e.g., "X was created based on template Y")

## Session Data

[Paste or attach session.jsonl content]
