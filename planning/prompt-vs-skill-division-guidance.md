# Prompt vs Skill Division: Skill-Creator Guidance

**Date**: 2025-10-27
**Context**: Applying skill-creator principles to research-assessor skill architecture
**User Question**: "Looking at the skills-creator skill, what is the guidance for division between prompt and skill (not SKILL.md and references)?"

---

## Skill-Creator Core Principles

### What Skills Provide (From skill-creator)

> "Skills are modular, self-contained packages that extend Claude's capabilities by providing specialized knowledge, workflows, and tools. Think of them as 'onboarding guides' for specific domains or tasks—they transform Claude from a general-purpose agent into a specialized agent equipped with procedural knowledge that no model can fully possess."

**Skills provide:**
1. **Specialized workflows** - Multi-step procedures for specific domains
2. **Tool integrations** - Instructions for working with specific file formats or APIs
3. **Domain expertise** - Company-specific knowledge, schemas, business logic
4. **Bundled resources** - Scripts, references, and assets for complex and repetitive tasks

### Key Architectural Principle

> "Information should live in either SKILL.md or references files, not both. Prefer references files for detailed information unless it's truly core to the skill—this keeps SKILL.md lean while making information discoverable without hogging the context window. Keep only essential procedural instructions and workflow guidance in SKILL.md; move detailed reference material, schemas, and examples to references files."

---

## Research-Assessor Architecture (Current)

Your current architecture (from SKILL.md):

```markdown
This skill provides:
- Core decision frameworks (how to distinguish evidence/claims, assign tiers, consolidate items)
- Schema definitions (object structures, field requirements)
- Reference materials (checklists, examples)

The user provides:
- Extraction prompts (detailed instructions for each pass, provided at runtime)
- Source material (research paper sections to extract from)
- JSON document (template or partially populated from previous passes)

Why this separation? Extraction prompts evolve frequently through testing and refinement.
This architecture allows prompt tuning without modifying the skill package, minimizing versioning conflicts.
```

**This architecture is CORRECT and aligns with skill-creator principles.**

---

## Prompt vs Skill Division Framework

### What Belongs in SKILL (and references/)

✅ **Procedural knowledge** - How to make specific decisions
- Decision frameworks (Evidence vs Claims test)
- Classification systems (RDMAP tiers, reasoning approaches)
- Consolidation patterns (when to lump vs split)
- Verification procedures (source verification steps)

✅ **Domain expertise** - Field-specific knowledge
- Schema definitions and field requirements
- Disciplinary assumptions and patterns
- Domain-specific checklists (TIDieR, CONSORT)
- Expected information standards

✅ **Reusable assets** - Cross-pass resources
- Template scripts
- Schema files
- Example extractions
- Reference guides

✅ **Conceptual frameworks** - Abstract decision models
- 4-level claims hierarchy
- Multi-dimensional evidence pattern
- Description vs Argumentation boundary
- Reasoning approach classification

**KEY TEST**: *"Would this be useful across MULTIPLE passes or use cases?"*
- If YES → Belongs in skill
- If NO → Belongs in prompts

---

### What Belongs in PROMPTS (user-provided at runtime)

✅ **Runtime workflow orchestration** - Pass-specific instructions
- "In Pass 1, DO this, THEN that, THEN this"
- "In Pass 2, consolidate by doing X, Y, Z"
- "In Pass 3, validate by checking A, B, C"
- Sequencing and flow control

✅ **Pass-specific context** - What this pass is for
- "Pass 1 intentionally over-extracts"
- "Pass 2 consolidates and refines"
- "Pass 3 validates structure"
- Pass-specific goals and expectations

✅ **Task framing** - What to do NOW
- "Your task in this pass..."
- "Input: JSON from Pass X"
- "Output: Same JSON with Y rationalized"
- Current task scope and boundaries

✅ **Rapidly evolving instructions** - Frequently tuned content
- Extraction strategies being tested
- Quality thresholds being refined
- New pass-specific patterns emerging from testing
- Temporary scaffolding during development

**KEY TEST**: *"Is this about WHAT to do in THIS specific pass, or HOW to make decisions?"*
- WHAT to do → Prompts
- HOW to decide → Skill

---

## Skill-Creator Principles Applied

### Principle 1: Progressive Disclosure

**Application**:
- SKILL.md: Brief overview, navigation to references
- References: Detailed frameworks, comprehensive guides
- Prompts: Workflow with pointers to skill references

**Example**:
```markdown
# PROMPT (lean, workflow-focused)
## Step 1: Evidence vs Claims Classification
Classify each item as evidence or claim using the test in evidence-vs-claims-guide.md.

# SKILL REFERENCE (comprehensive, decision-focused)
## Evidence vs Claims Test
**Test**: "Does this item make an argument or present an observation?"
[... detailed framework with examples, edge cases, decision tree ...]
```

### Principle 2: Avoid Duplication

**Violation** (current state):
```text
Evidence vs Claims distinction appears in:
1. SKILL.md lines 148-160 (13 lines)
2. Prompt 01 lines 106-122 (17 lines)
3. ❌ DUPLICATION - should be ONE canonical version
```

**Correct application**:
```text
Evidence vs Claims distinction appears in:
1. references/checklists/evidence-vs-claims-guide.md (canonical, comprehensive)
2. SKILL.md (brief pointer with 2-line summary)
3. Prompt 01 (reference to guide when needed)
```

### Principle 3: Separation of Concerns

**Reusable Knowledge** (Skill):
- "How do I distinguish evidence from claims?" → Decision framework
- "What makes something a Research Design vs Method?" → Classification system
- "When should I consolidate items?" → Consolidation patterns

**Runtime Workflow** (Prompts):
- "In Pass 1, classify EACH item as evidence or claim" → Orchestration
- "In Pass 2, consolidate items using consolidation patterns" → Sequencing
- "In Pass 3, validate cross-references" → Current task

### Principle 4: Optimise for Change Frequency

**Why separate prompts from skill?**

Your rationale (from SKILL.md):
> "Extraction prompts evolve frequently through testing and refinement. This architecture allows prompt tuning without modifying the skill package, minimizing versioning conflicts."

**This is EXCELLENT reasoning** and aligns with skill-creator principles:

**Changes frequently** (Prompts):
- Pass workflow refinements
- Quality threshold adjustments
- New pass-specific strategies
- Temporary scaffolding during testing
- → Keep in prompts for easy iteration

**Changes rarely** (Skill):
- Core decision frameworks
- Schema definitions
- Classification systems
- Domain knowledge
- → Keep in skill for stability and reuse

---

## Application to Current Migration

### Analysis: What Should Move from Prompts to Skill?

Using the framework above, assess each candidate:

#### Evidence vs Claims Distinction (30 lines)

- **Is it procedural knowledge?** YES - Decision framework
- **Is it reusable across passes?** YES - Used in Pass 1, Pass 2, verification
- **Is it conceptual framework?** YES - Core boundary definition
- **Does it change frequently?** NO - Stable framework
- **Conclusion**: **SHOULD BE IN SKILL** ✅

#### Claims Hierarchy (22 lines)

- **Is it procedural knowledge?** YES - Classification framework
- **Is it reusable across passes?** YES - Used in Pass 1, Pass 2
- **Is it conceptual framework?** YES - 4-level hierarchy system
- **Does it change frequently?** NO - Stable classification
- **Conclusion**: **SHOULD BE IN SKILL** ✅

#### Multi-Dimensional Evidence Pattern (35 lines)

- **Is it procedural knowledge?** YES - Consolidation decision framework
- **Is it reusable across passes?** YES - Any consolidation decision
- **Is it conceptual framework?** YES - Pattern for handling complex cases
- **Does it change frequently?** NO - Stable pattern
- **Conclusion**: **SHOULD BE IN SKILL** ✅

#### RDMAP Consolidation Patterns (45 lines, 6 patterns)

- **Is it procedural knowledge?** YES - Consolidation frameworks
- **Is it reusable across passes?** YES - Pass 2 and beyond
- **Is it conceptual framework?** YES - 6 decision patterns
- **Does it change frequently?** NO - Stable patterns
- **Conclusion**: **SHOULD BE IN SKILL** ✅

#### Reasoning Approach Classification (29 lines)

- **Is it procedural knowledge?** YES - Classification framework
- **Is it reusable across passes?** YES - Pass 1 extraction, Pass 2 verification
- **Is it conceptual framework?** YES - 5-category system
- **Does it change frequently?** NO - Stable framework
- **Conclusion**: **SHOULD BE IN SKILL** ✅

#### "Strategic Verbosity in Claims" (14 lines in Prompt 02)

- **Is it procedural knowledge?** Somewhat - Writing guidance
- **Is it reusable across passes?** NO - Specifically about Pass 2 consolidation
- **Is it conceptual framework?** NO - Pass-specific guidance
- **Does it change frequently?** YES - Being refined through testing
- **Conclusion**: **KEEP IN PROMPT** ✅

#### "Pass 2 Addition Patterns" (23 lines in Prompt 02)

- **Is it procedural knowledge?** YES - But pass-specific
- **Is it reusable across passes?** NO - Specifically about what Pass 2 should ADD
- **Is it conceptual framework?** NO - Pass 2 workflow orchestration
- **Does it change frequently?** YES - Evolving with testing
- **Conclusion**: **KEEP IN PROMPT** ✅

---

## Decision Framework Summary

### Move to Skill When:

1. ✅ **Reusable** across multiple passes or use cases
2. ✅ **Conceptual framework** or decision model
3. ✅ **Stable** (changes infrequently)
4. ✅ **Procedural knowledge** (how to decide/classify)
5. ✅ **Domain expertise** (field-specific standards)

### Keep in Prompt When:

1. ✅ **Pass-specific** workflow orchestration
2. ✅ **Task framing** (what to do NOW)
3. ✅ **Sequencing** instructions (do this, then that)
4. ✅ **Evolving rapidly** through testing
5. ✅ **Context-specific** to this particular pass

### Quick Decision Tests

**Test 1: Reusability**
- "Would another pass need this?" → YES = Skill, NO = Prompt

**Test 2: Abstraction Level**
- "Is this HOW to decide or WHAT to do?" → HOW = Skill, WHAT = Prompt

**Test 3: Change Frequency**
- "How often does this change?" → Rarely = Skill, Often = Prompt

**Test 4: Knowledge Type**
- "Is this a framework or a workflow?" → Framework = Skill, Workflow = Prompt

---

## Validation Against Skill-Creator Principles

### ✅ Alignment Confirmed

Your proposed architecture **STRONGLY aligns** with skill-creator principles:

1. **Skills provide specialized knowledge** ✅
   - Decision frameworks, schemas, classification systems → In skill references

2. **Skills provide domain expertise** ✅
   - Field-specific patterns, expected information standards → In skill references

3. **Skills are reusable** ✅
   - Frameworks used across multiple passes → In skill, not duplicated

4. **Progressive disclosure** ✅
   - SKILL.md lean, references detailed, prompts reference as needed

5. **Avoid duplication** ✅
   - Moving duplicated content to single canonical location in skill

6. **Separation of concerns** ✅
   - Knowledge (skill) vs workflow (prompts)
   - Stable (skill) vs evolving (prompts)

### User's Architecture Rationale is Sound

> "Extraction prompts evolve frequently through testing and refinement. This architecture allows prompt tuning without modifying the skill package, minimizing versioning conflicts."

**This rationale is EXCELLENT** because it:
- Recognises change frequency differences
- Enables rapid iteration on prompts without skill versioning
- Maintains stability of reusable knowledge
- Reduces coordination overhead

**Skill-creator would endorse this approach.**

---

## Recommendations Based on Skill-Creator Principles

### 1. Proceed with Confidence

The proposed migration **follows skill-creator best practices**:
- Move conceptual frameworks to skill (reusable knowledge)
- Keep workflow orchestration in prompts (runtime instructions)
- Eliminate duplication (single source of truth)
- Use progressive disclosure (references loaded as needed)

### 2. Conceptual Frameworks SHOULD Be in Skill

**Clear guidance from skill-creator**:
> "Skills are modular, self-contained packages that extend Claude's capabilities by providing specialized knowledge, workflows, and tools."

**Specialized knowledge includes**:
- Decision frameworks ✅
- Classification systems ✅
- Consolidation patterns ✅
- Domain expertise ✅

**All candidates in Phase A and Phase B qualify as "specialized knowledge"** → SHOULD BE IN SKILL

### 3. Prompts Should Be Workflow-Only

**After migration, prompts should contain**:
- Pass-specific task framing
- Workflow sequencing (Step 1, Step 2, Step 3)
- References to skill frameworks
- Pass-specific quality checks
- Evolving instructions under active testing

**Prompts should NOT contain**:
- Decision frameworks (→ skill references)
- Classification systems (→ skill references)
- Schema definitions (→ skill references)
- Duplicated content (→ single source in skill)

### 4. Accept Medium Risk for High-Value Alignment

**Skill-creator principle**: Skills provide "procedural knowledge that no model can fully possess"

**Your conceptual frameworks ARE procedural knowledge**:
- Evidence vs Claims test → Procedural knowledge
- RDMAP tier assignment → Procedural knowledge
- Consolidation patterns → Procedural knowledge
- Reasoning approach classification → Procedural knowledge

**Conclusion**: Moving these to skill is not just "nice to have" - it's **architecturally correct** per skill-creator principles.

The MEDIUM risk in Phase B-2 is **worth accepting** because it achieves proper architecture alignment.

---

## Answers to User's Specific Questions

### Q1: What is the guidance for division between prompt and skill?

**Answer**:
- **SKILL**: Reusable procedural knowledge, decision frameworks, classification systems, domain expertise, schemas
- **PROMPTS**: Runtime workflow orchestration, pass-specific task framing, sequencing instructions, rapidly evolving strategies

**Test**: "Is this HOW to decide (skill) or WHAT to do in this pass (prompt)?"

### Q2: Should conceptual frameworks be in skill?

**Answer**: **YES** - Conceptual frameworks are "specialized knowledge" and "procedural knowledge" that skills are designed to provide.

**Examples from your work**:
- Evidence vs Claims test → Framework, should be in skill ✅
- Claims Hierarchy → Framework, should be in skill ✅
- Consolidation patterns → Framework, should be in skill ✅
- RDMAP tier assignment → Framework, should be in skill ✅

### Q3: Should prompts be workflow-only?

**Answer**: **YES** - After migration, prompts should focus on:
- "In THIS pass, DO these steps in this order"
- "Your task NOW is..."
- "See skill reference X for guidance on decision Y"

**Keep in prompts**:
- Workflow orchestration ✅
- Pass-specific context ✅
- Quality expectations for THIS pass ✅
- Evolving strategies under testing ✅

### Q4: Does the proposed migration align with skill-creator principles?

**Answer**: **YES** - The migration strongly aligns with:
- Progressive disclosure ✅
- Avoiding duplication ✅
- Separation of concerns ✅
- Reusable knowledge in skills ✅
- Runtime instructions in prompts ✅

---

## Conclusion

**Skill-creator guidance is clear**: Your proposed prompt-to-skill migration is **architecturally correct** and **aligns with best practices**.

**Key principles validated**:
1. ✅ Skills provide procedural knowledge and decision frameworks
2. ✅ Prompts provide runtime workflow orchestration
3. ✅ Conceptual frameworks belong in skill references
4. ✅ No duplication - single source of truth
5. ✅ Separation by change frequency (stable vs evolving)
6. ✅ Progressive disclosure (SKILL.md → references → prompts reference)

**Your architectural rationale is sound**:
> "Extraction prompts evolve frequently through testing and refinement. This architecture allows prompt tuning without modifying the skill package, minimizing versioning conflicts."

**Recommendation**: **PROCEED** with the proposed migration. The medium risk in Phase B-2 is justified by achieving proper skill-creator architectural alignment. The gains in maintainability, reusability, and separation of concerns are worth the carefully managed risk.
