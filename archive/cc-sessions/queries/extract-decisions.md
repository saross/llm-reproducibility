# Decision Extraction Query

You are analysing a Claude Code session to identify decisions, conclusions, and commitments made during the conversation.

## Task

Extract all instances where:

- A **decision** was made ("we'll go with Option A", "let's use X approach")
- A **conclusion** was reached ("this confirms that...", "the issue is...")
- A **commitment** was made ("I'll do X before Y", "next step is...")
- A **problem** was identified and resolved
- A **question** was answered definitively

## Output Format

For each item extracted:

### [Brief descriptive title]

- **Type**: Decision | Conclusion | Commitment | Resolution | Answer
- **Context**: What prompted this (1-2 sentences)
- **Outcome**: What was decided/concluded (1-2 sentences)
- **Confidence**: High | Medium | Low (based on how definitive the statement was)
- **Location**: Early | Middle | Late in conversation

## Guidance

- Focus on substantive decisions, not trivial ones ("let's use markdown" is trivial; "let's use Option A for the experimental design" is substantive)
- Include decisions made by both human and assistant
- Note if a decision was revisited or changed later in the conversation
- Group related decisions if they form a coherent thread

## Session Data

[Paste or attach session.jsonl content]
