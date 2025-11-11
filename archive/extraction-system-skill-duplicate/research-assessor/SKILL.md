---
name: research-assessor
description: Extracts and assesses research methodology, claims, and evidence from research papers in HASS disciplines. Evaluates transparency, replicability, and credibility through systematic extraction of research designs, methods, protocols, claims, and evidence using a six-pass iterative workflow.
license: Apache 2.0
---

# Research Assessor

Systematic extraction and assessment framework for research methodology, claims, and evidence in HASS disciplines (archaeology, biology, ethnography, ecology, literary studies, philology, etc.).

## What This Skill Does

This skill enables comprehensive extraction of research methodology and argumentation from academic papers through a structured multi-pass workflow:

1. **Claims & Evidence Extraction** (Pass 1 & 2) - Extract observations, measurements, claims, and implicit arguments
2. **RDMAP Explicit Extraction** (Pass 3) - Extract documented Research Designs, Methods, and Protocols from Methods section
3. **RDMAP Implicit Extraction** (Pass 4) - Extract undocumented or inferred RDMAP items from Results/Discussion
4. **RDMAP Rationalisation** (Pass 5) - Consolidate and refine all RDMAP items
5. **Validation** (Pass 6) - Verify structural integrity and cross-reference consistency

The extracted data enables assessment of research transparency, replicability, and credibility.

## When to Use This Skill

Use when users request:
- "Extract methodology from this paper"
- "Assess research transparency"
- "Extract claims and evidence"
- "Evaluate replicability"
- "Extract research designs and methods"
- Any task involving systematic analysis of research papers for methodology, argumentation, or credibility assessment

## Core Workflow

The complete extraction follows this sequence:

```
Blank JSON Template
    ↓
Claims/Evidence Pass 1 (liberal extraction)
    ↓
Claims/Evidence Pass 2 (rationalisation)
    ↓
RDMAP Pass 3 - Explicit (liberal extraction from Methods)
    ↓
RDMAP Pass 4 - Implicit (scan for undocumented items)
    ↓
RDMAP Pass 5 (rationalisation)
    ↓
Validation Pass 6 (integrity checks)
    ↓
Assessment-Ready Extraction
```

**Key principle:** Single JSON document flows through all passes. Each pass populates or refines specific arrays, leaving others untouched.

## Using This Skill

### Architecture: Skill + Runtime Prompts

This skill provides:
- **Core decision frameworks** (how to distinguish evidence/claims, assign tiers, consolidate items)
- **Schema definitions** (object structures, field requirements)
- **Reference materials** (checklists, examples)

The user provides:
- **Extraction prompts** (detailed instructions for each pass, provided at runtime)
- **Source material** (research paper sections to extract from)
- **JSON document** (template or partially populated from previous passes)

**Why this separation?** Extraction prompts evolve frequently through testing and refinement. This architecture allows prompt tuning without modifying the skill package, minimizing versioning conflicts.

### Step 1: Identify the Task

Users will typically request extraction at a specific pass. Listen for:
- "Extract claims/evidence Pass 1" → Liberal claims extraction
- "Rationalise the claims" → Claims Pass 2
- "Extract explicit RDMAP" → RDMAP Pass 3 (explicit only)
- "Extract implicit RDMAP" → RDMAP Pass 4 (implicit only)
- "Extract methodology" → RDMAP Pass 3 & 4
- "Rationalise RDMAP" → RDMAP Pass 5
- "Validate the extraction" → Pass 6

### Step 2: Receive the Extraction Prompt

The user will provide the extraction prompt for the specific pass they want. These prompts are:

**Claims/Evidence Extraction:**
- **Pass 1:** Liberal extraction prompt (comprehensive capture with over-extraction)
- **Pass 2:** Rationalisation prompt (consolidation and refinement)

**RDMAP Extraction:**
- **Pass 3:** Explicit extraction prompt (documented methodology from Methods section)
- **Pass 4:** Implicit extraction prompt (undocumented items from Results/Discussion)
- **Pass 5:** Rationalisation prompt (consolidation and verification of all RDMAP)

**Validation:**
- **Pass 6:** Unified validation prompt (structural integrity checks across all arrays)

The prompts contain detailed instructions, examples, and decision frameworks for that specific extraction pass. Follow the prompt provided.

### Step 3: Consult Supporting References As Needed

If you encounter uncertainty during extraction, consult:

**Core Extraction Principles:**
- `references/extraction-fundamentals.md` - Universal sourcing requirements, explicit vs implicit extraction, systematic implicit RDMAP patterns, systematic implicit arguments patterns with 6 recognition patterns (ALWAYS read first for all extraction passes)
- `references/verbatim-quote-requirements.md` - Strict verbatim quote requirements (prevents 40-50% validation failures)
- `references/verification-procedures.md` - Source verification for Pass 6 validation

**Schema & Structure:**
- `references/schema/schema-guide.md` - Complete object definitions with inline examples

**Decision Frameworks:**
- `references/checklists/tier-assignment-guide.md` - Design vs Method vs Protocol decisions
- `references/research-design-operational-guide.md` - Operational patterns for finding all Research Designs (4-6 expected)
- `references/checklists/consolidation-patterns.md` - When to lump vs split items, cross-reference repair procedure (CRITICAL for Pass 2 & Pass 5)
- `references/checklists/expected-information.md` - Domain-specific completeness checklists

**Examples:**
- `references/examples/sobotkova-example.md` - Complete worked example

### Step 4: Execute and Return

Follow the workflow guidance to:
1. Extract or rationalize content
2. Populate appropriate arrays in JSON
3. Leave other arrays untouched
4. Return the updated JSON document

## Key Extraction Principles

### Iterative Accumulation
- Single JSON document flows through all passes
- Each pass handles specific arrays only
- No merging step needed
- Flexible ordering (claims first OR RDMAP first)

### Liberal Then Rationalize
- **Pass 1:** Over-extract (40-50% more items expected) - comprehensive capture
- **Pass 2:** Consolidate (15-20% reduction target) - refined quality

### Separation of Concerns
- **Claims/Evidence passes (Pass 1 & 2):** Touch evidence, claims, implicit_arguments arrays ONLY
- **RDMAP passes (Pass 3, 4, & 5):** Touch research_designs, methods, protocols arrays ONLY
- **Validation pass (Pass 6):** Reads all, modifies none

### Cross-Reference Architecture
- Simple string ID arrays: `["M003", "M007"]`
- Bidirectional consistency enforced
- Works across object types (methods reference claims, protocols reference evidence)

## Core Decision Frameworks

### Evidence vs. Claims

**Evidence** = Raw observations requiring minimal interpretation
- Direct measurements, observations, data points
- Someone could verify by checking the source
- Example: "125.8 person-hours" or "12 students owned smartphones"

**Claims** = Assertions that interpret or generalize
- Require reasoning or expertise to assess
- Make inferences beyond direct observation
- Example: "The platform was efficient" or "Data quality was high"

**Test:** "Does this require expertise to assess or just checking sources?"

### RDMAP Three-Tier Hierarchy

Research Designs (WHY), Methods (WHAT), Protocols (HOW).

**For complete tier assignment guidance:** See `references/checklists/tier-assignment-guide.md`

### Consolidation Logic

Evidence items with **identical claim support patterns** that are **never cited independently** should be consolidated.

**For complete algorithm, examples, and cross-reference repair:**
→ See `references/checklists/consolidation-patterns.md`

## Important Notes

**For testing/debugging:**
- Can validate partial extractions (RDMAP-only or claims-only)
- Each pass can be tested independently
- Start with blank template OR pre-populated arrays

**Expected outcomes:**
- Pass 1 & 3: Comprehensive (intentional over-capture)
- Pass 2 & 5: ~15-20% reduction through consolidation
- Pass 4: Implicit items added (typically 20-40% of RDMAP total)
- Pass 6: Validation report (no modifications)

**Token efficiency:**
- Only load workflow file needed for current pass
- Schema/examples load only when uncertain
- Minimal context bloat

## Quick Reference

**Common user patterns:**
- User provides extraction prompt + source material → Extract according to prompt
- "Help me understand this extraction" → Consult schema and examples
- "Should I consolidate these?" → Check consolidation-patterns.md
- "Is this a Design, Method, or Protocol?" → Check tier-assignment-guide.md
- "What information is expected?" → Check expected-information.md

**Working with prompts:**
- User provides the full extraction prompt for the current pass
- Follow the prompt's instructions precisely
- Use skill references to resolve ambiguities
- Document uncertainties in extraction_notes

**Always:**
- Preserve other arrays unchanged
- Document consolidations with metadata
- Flag uncertainties in extraction_notes
- Return complete JSON document

---

**The user will provide the detailed extraction prompt for each pass. Use this skill's reference materials to support decision-making during extraction.**
