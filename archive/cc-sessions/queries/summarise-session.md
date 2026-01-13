# Session Summary Query

You are analysing a Claude Code session transcript in JSONL format. Each line is a JSON object representing one event in the conversation (human messages, assistant messages, tool calls, tool results, thinking blocks).

## Task

Provide a structured summary including:

### 1. Purpose

What was the user trying to accomplish? (1-2 sentences)

### 2. Key Activities

What major tasks were performed? (bullet list, 3-7 items, in rough chronological order)

### 3. Decisions Made

What significant decisions or conclusions were reached? Include:

- Technical decisions (e.g., "chose Option A over Option B")
- Findings (e.g., "identified 5 issues in document X")
- Agreements (e.g., "will proceed with approach Y")

### 4. Artifacts Produced

What files were created or significantly modified? List with:

- File path
- Brief description of content/purpose

### 5. Open Items

What was left unfinished or flagged for follow-up? (if any)

### 6. Session Statistics

- Duration (from first to last timestamp)
- Approximate turn count
- Notable tool usage patterns

## Output Format

Use markdown with the headers above. Be concise—this is a reference summary, not a complete transcript. Aim for 300-500 words total.

## Session Data

[Paste or attach session.jsonl content]
