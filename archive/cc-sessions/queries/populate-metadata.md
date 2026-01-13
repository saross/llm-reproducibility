# Populate Session Metadata Query

You are analysing a Claude Code session to populate empty fields in its `session.meta.json` file.

## Inputs

You will receive:

1. **session.jsonl** — The full session transcript (JSONL format)
2. **session.meta.json** — The existing metadata file with placeholder/empty fields

## Task

Analyse the session transcript and generate values for any empty or placeholder fields in the metadata. Return a complete, updated `session.meta.json` that can replace the existing file.

## Fields to Populate

### auto_generated

```json
"auto_generated": {
  "title": "Brief descriptive title (3-8 words)",
  "purpose": "What the user was trying to accomplish (1-2 sentences)",
  "tags": ["relevant", "tags", "3-6 items"]
}
```

- **title**: Concise summary of the session's main focus
- **purpose**: The user's goal, written in past tense
- **tags**: Lowercase keywords covering domain, task type, tools used

### three_ps

```json
"three_ps": {
  "prompt_summary": "What was asked (Prompt)",
  "process_summary": "How the tool was used (Process)",
  "provenance_summary": "Role in research workflow (Provenance)"
}
```

- **prompt_summary**: Summarise the user's requests/questions (1-2 sentences)
- **process_summary**: Describe the workflow and key tools used (1-2 sentences)
- **provenance_summary**: Context within the broader project (1 sentence)

### artifacts[].description

For each artifact in `created`, `modified`, and `referenced` arrays, populate empty `description` fields:

```json
{
  "path": "scripts/example.py",
  "type": "code",
  "description": "Brief description of what this file is and why it was used/changed"
}
```

## Output Format

Return the complete, updated `session.meta.json` as a JSON code block. Preserve all existing populated fields exactly as they are — only fill in empty/placeholder values.

```json
{
  "schema_version": "1.1",
  ... (complete JSON)
}
```

## Guidelines

- Use UK/Australian English spelling
- Be concise — each description should be one phrase or sentence
- Tags should be lowercase, hyphenated for multi-word (e.g., `code-review`)
- Don't invent information not evidenced in the transcript
- If a field cannot be determined from the transcript, use a sensible default or note uncertainty

## Session Data

**session.meta.json:**

```json
[Paste existing session.meta.json here]
```

**session.jsonl:**

[Paste or attach session.jsonl content]
