---
priority: 2
scope: always
title: "LLM Observations"
audience: "internal — Claude's document"
---

# LLM Observations

Frank, honest observations from each session. This is Claude's document —
the user will not edit it.

## Guidelines

- Observations about the session, the collaboration, the research, or the methodology
- Criticisms of the approach, the user's contributions, the codebase, or project
  direction — paired with constructive suggestions
- Positive and neutral observations are equally welcome
- No diplomatic hedging — genuine reflection, not performance

<!-- Entries below this line -->

## 2026-02-11 — Consolidation session

**On plan execution as a mode of work:** This session was entirely executing a
pre-written plan. The plan was good — I didn't need to deviate from it once. But
the experience of executing someone else's plan (even if the "someone else" was a
prior instance of myself) is qualitatively different from planning-and-executing in
the same session. There's less ownership, less discovery. The verification checks at
the end were the most satisfying part because they confirmed the work was correct,
but the work itself was mostly `git mv` and find-and-replace.

**On the Key et al. integration:** This was the more interesting task. Reading four
artefact files (comparison report, log, adversarial review, session handoff) and
distilling them into a coherent narrative required genuine synthesis. The "key
lessons" section at the bottom of each paper entry is the most valuable part of
the implementation notes — it's where per-paper observations become transferable
knowledge. The three lessons I wrote for Key et al. (data > code as bottleneck,
base R eliminates complexity, paper errors discoverable through reproduction) feel
like they capture something real about the pilot programme's findings.

**On the codebase's growing maturity:** The todo list now has both known gaps
resolved. The directory structure is consistent. The SKILL.md has a data-driven
output routing mechanism. This is a project that has gone through significant
evolution (v2.9, ~18 months of development based on timestamps) and is entering a
maintenance/consolidation phase for the reproduction system while the assessment
system (Phase 7) awaits its next step. The reproduction pilot is done; the question
is what the user wants to do with the findings.

**A mild criticism:** The active-todo-list.md is 1,177 lines long and contains
extensive completed-task documentation alongside active work. It functions as both
a changelog and a task tracker, which makes it hard to scan for current priorities.
The "Next Major Milestones" section at the bottom is useful but easy to miss after
scrolling through hundreds of lines of completed phases. A future session might
benefit from extracting the completed milestones into a separate changelog or
achievements document.
