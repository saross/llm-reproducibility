---
name: reflect
description: "End-of-session reflection protocol for llm-reproducibility. This skill should be used when the user invokes /reflect or asks to reflect on this session, do end-of-session reflections, or similar. It guides Claude through updating reflection documents in priority order, answering structured prompts, and maintaining research observation logs."
---

# End-of-Session Reflection

Update the project's reflection and observation documents following the established
protocol. Work through the documents in priority order. If context is limited,
prioritise the top of the list.

## Important: Instance Boundary

Reflections are most valuable when written by the instance that did the session's work.
If this invocation follows a compaction or continuation (i.e., the current instance is
working from a conversation summary rather than direct experience), flag this explicitly
in the reflection entries. Distinguish between genuine first-person observations and
plausible reconstructions from summaries.

## Protocol

Process all `.md` files in the reflections directory (`docs/notes/reflections`), sorted by
the `priority` field in their YAML frontmatter (lowest number = highest priority).

For each document: **read it first** to understand the current structure, entry
numbering, and conventions, then append a new dated section continuing the established
format.

### Conditional documents

Some documents have `scope: conditional` in their frontmatter with a `conditions` field
describing when they should be updated. For these documents, evaluate whether the current
session meets the conditions. If not, explicitly state the assessment and skip.

## Standards

- UK/Australian English throughout
- Concise but substantive — these are research documents
- Continue existing numbering sequences (do not restart)
- Include dated section headers matching the established format
- Update document footers/timestamps where they exist
