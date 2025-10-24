# Consolidation Refinement - Complete Implementation Guide

**Purpose:** Implement empirical graph-based consolidation as primary consolidation decision framework

**Terminology:** `identical_support_pattern` - Evidence items with identical claim support patterns that function as inseparable analytical units

---

## Table of Contents

1. [Schema Changes](#schema-changes)
2. [SKILL.md Changes](#skillmd-changes)
3. [consolidation-patterns.md Changes](#consolidation-patternsmd-changes)
4. [claims-evidence_pass2_prompt.md Changes](#claims-evidence_pass2_promptmd-changes)
5. [rdmap_pass2_prompt.md Changes](#rdmap_pass2_promptmd-changes)

---

## Schema Changes

### consolidation_metadata.consolidation_type Enum

**Current values:**
```
granularity_reduction | compound_finding | analytical_view | 
phase_aggregation | profile_consolidation | redundancy_elimination | 
narrative_consolidation | compound_interpretation | synthesis
```

**Add new value:**
```
identical_support_pattern
```

**Updated enum:**
```
granularity_reduction | compound_finding | analytical_view | 
phase_aggregation | profile_consolidation | redundancy_elimination | 
narrative_consolidation | compound_interpretation | synthesis | 
identical_support_pattern
```

**Definition:**
- `identical_support_pattern` - Evidence items consolidated because they have identical claim support patterns (support exactly the same set of claims) and are never cited independently. Identified through empirical graph analysis rather than semantic judgment.

**Usage example:**
```json
"consolidation_metadata": {
  "consolidated_from": ["P1_E032", "P1_E033"],
  "consolidation_type": "identical_support_pattern",
  "information_preserved": "complete",
  "granularity_available": "Map preparation (6min/map) and redeployment time (1h) preserved",
  "rationale": "Both items only support C063, never cited independently. Empirical graph analysis identified identical support pattern [C063]."
}
```

---

## SKILL.md Changes

### Location
Replace lines 181-190 (current "Consolidation Logic" section)

### Replacement Text

```markdown
### Consolidation Logic

**PRIMARY: Empirical Graph Analysis (Identical Support Patterns)**

For assessment-focused extraction, evidence items that are always used together should be consolidated.

**The Rule:** If evidence items have identical claim support patterns and are never cited independently → CONSOLIDATE

**How to identify:**
1. Map each evidence item to claims it supports: `E001 → [C003, C005]`
2. Find items with identical support patterns: `E002 → [C003, C005]`
3. Verify neither item is cited independently in other claims
4. If patterns match and no independent citations → consolidate as compound finding
5. Document with consolidation_type: `identical_support_pattern`

**Example:**
```
E032 → [C063] only
E033 → [C063] only
→ Identical patterns, never cited separately
→ CONSOLIDATE as compound finding
```

**Rationale:** For credibility assessment, what matters is the analytical unit. If E001 and E002 are never assessed separately—always invoked together as joint support—they function as a single analytical unit and should be consolidated.

**SECONDARY: Assessment Compatibility Test**

When empirical graph analysis is inconclusive (e.g., no claim support, complex patterns), ask:

*"Would I assess the credibility of these items TOGETHER or SEPARATELY?"*

- Together → Consider consolidation
- Separately → Keep distinct

**Common patterns:**
- Multiple rationales for same decision → Together
- Problem + solution narrative → Together
- Temporal comparisons (2017 vs 2018) → Separately (ALWAYS)
- Different assessment implications → Separately

**CRITICAL:** Temporal comparisons always separate—comparison requires distinct items, even if they have identical support patterns.

**For detailed patterns, examples, and edge cases:**  
→ See `references/checklists/consolidation-patterns.md`
```

**Net change:** +25 lines (9 lines → 34 lines)

---

## consolidation-patterns.md Changes

### Location
Insert new section after line 11 ("Match granularity to assessment needs..."), before "## Decision Framework"

### New Section to Insert

```markdown

---

## PRIMARY: Empirical Graph Analysis (Identical Support Patterns)

**For assessment-focused extraction, use evidence graph structure as primary consolidation decision.**

### The Rule

Evidence items with **identical claim support patterns** that are **never cited independently** should be consolidated.

This is an **empirical, objective test** based on the actual claim-evidence graph in the extraction, not semantic judgment about what "should" go together.

### The Algorithm

```
For each evidence item:
  1. Build support pattern: Set of claims this evidence supports
     Example: E001 → {C003, C005}
  
  2. Group evidence items by support pattern
     Example: Pattern {C003, C005} → [E001, E002]
  
  3. For each group with 2+ items (potential consolidation):
     - Verify pattern is identical (not subset/superset)
     - Verify no temporal comparison (2017 vs 2018)
     - Verify items never cited independently
     - If all conditions met → CONSOLIDATE
  
  4. Document with consolidation_type: "identical_support_pattern"
```

### Examples

#### CONSOLIDATE - Identical Patterns

**Example 1: Setup efficiency**
```
E032 supports: [C063]
E033 supports: [C063]

Analysis:
- Identical pattern: Both only support C063
- Never cited independently: No other claim references either item
- Not temporal comparison: Both measure same time period

Decision: CONSOLIDATE
Result: "Map preparation requires 6min/map; 2018 redeployment required only 1h"
Type: identical_support_pattern
```

**Example 2: ML training overhead**
```
E034 supports: [C067, C068]
E035 supports: [C067, C068]

Analysis:
- Identical pattern: Both support exactly [C067, C068]
- Never cited independently: Always used together
- Not temporal comparison: Different aspects (manual work, expert time)

Decision: CONSOLIDATE
Result: "ML training required 1,250h manual digitisation plus 7 days expert fine-tuning"
Type: identical_support_pattern
```

#### KEEP SEPARATE - Different Patterns

**Example 1: Overlapping but not identical**
```
E001 supports: [C001, C002, C011]
E002 supports: [C002, C003, C012]

Analysis:
- Different patterns: E001 has {C001, C011} unique, E002 has {C003, C012} unique
- Independent citations: E001 independently supports C001, E002 independently supports C003
- Different analytical roles in the paper

Decision: KEEP SEPARATE
Rationale: Each item has independent analytical function
```

**Example 2: Subset pattern**
```
E006 supports: [C040, C041]
E012 supports: [C041]

Analysis:
- Subset pattern: E012's support is proper subset of E006's
- E006 independently supports C040: Has additional analytical role
- Different granularity: E006 is complete profile, E012 is specific aspect

Decision: KEEP SEPARATE (usually)
Rationale: Subset patterns typically indicate different analytical granularity
Exception: If E012 adds no independent value and C041 always assessed with C040, consider consolidation
```

#### KEEP SEPARATE - Temporal Comparisons (Critical Exception)

**Example: Year-over-year comparison**
```
E017_2017 supports: [C015, C016]  (2017 supervision hours)
E017_2018 supports: [C015, C016]  (2018 supervision hours)

Analysis:
- Identical pattern: Both support [C015, C016]
- Temporal comparison: Comparing 2017 vs 2018

Decision: KEEP SEPARATE (ALWAYS)
Rationale: Comparison is the analytical point—requires separate items even with identical support
Critical: Temporal comparisons override identical pattern rule
```

**Other temporal patterns that must stay separate:**
- Before/after interventions
- Phase-by-phase progression
- Sequential time periods
- Pre/post measurements

### Why This Is Primary

Empirical graph analysis is prioritized because it:

1. **Objective**: Based on actual graph structure, not subjective judgment
2. **Empirical**: Uses the paper's own claim-evidence relationships
3. **Assessment-focused**: Identifies the analytical units the paper actually uses
4. **Reliable**: Reduces over/under-consolidation from intuition errors
5. **Verifiable**: Can be programmatically checked and validated

### When Graph Analysis Is Inconclusive

Use secondary heuristics when:
- Evidence has no claim support (contextual information)
- Complex overlapping patterns (many partial overlaps)
- Claims consolidation (claims don't have "support patterns" in same way)
- RDMAP consolidation (design/method/protocol relationships differ)

In these cases, fall back to: *"Would I assess these TOGETHER or SEPARATELY?"*

---
```

**Net change:** +115 lines inserted after line 11

### Also Update Line 3-9 Section

**Current text (lines 3-9):**
```markdown
## The Core Principle

**Acid Test: "Would I assess these items TOGETHER or SEPARATELY?"**

- **Together** → CONSOLIDATE
- **Separately** → KEEP DISTINCT

Match granularity to assessment needs, not just to reduce item count.
```

**Replace with:**
```markdown
## The Core Principles

### For Evidence: Use Empirical Graph Analysis First

Evidence consolidation should prioritize **identical support patterns** (see below) identified through empirical graph analysis. Use assessment compatibility test as secondary heuristic.

### For Claims and Context: Use Assessment Compatibility

*"Would I assess these items TOGETHER or SEPARATELY?"*

- **Together** → CONSOLIDATE
- **Separately** → KEEP DISTINCT

Match granularity to assessment needs, not just to reduce item count.
```

**Net change:** +3 lines (7 lines → 10 lines)

---

## claims-evidence_pass2_prompt.md Changes

### Location
Replace lines 93-107 (current "Core Consolidation Principles" section header and "Primary Principle" subsection)

### Replacement Text

```markdown
## Core Consolidation Principles

**Follow the consolidation hierarchy defined in the skill and reference materials:**

### Consolidation Hierarchy

**For Evidence Items:**

1. **Empirical Graph Analysis** (PRIMARY)
   - Identify evidence with identical claim support patterns
   - See SKILL.md lines 183-212 for complete algorithm
   - See consolidation-patterns.md "PRIMARY: Empirical Graph Analysis" section for examples

2. **Assessment Compatibility Test** (SECONDARY)  
   - When graph analysis inconclusive: "Would I assess TOGETHER or SEPARATELY?"
   - See consolidation-patterns.md for detailed patterns

3. **Preserve Critical Distinctions** (ALWAYS)
   - Temporal comparisons: NEVER consolidate (2017 vs 2018, before/after)
   - Different assessment implications: Keep separate
   - Subset patterns: Usually separate

**For Claims:**
- Graph analysis doesn't apply (claims don't have "support patterns")
- Use Assessment Compatibility Test
- Common patterns: narrative consolidation, compound interpretation, synthesis

**For detailed patterns and examples:**  
→ See `/mnt/skills/user/research-assessor/references/checklists/consolidation-patterns.md`

**Quick workflow:**
```
Step 1: Map evidence support patterns → Find identical patterns
Step 2: Verify no temporal comparison → Consolidate as identical_support_pattern
Step 3: For remaining items, apply assessment compatibility test
Step 4: Document all consolidations with complete metadata
```

---
```

**Net change:** -10 lines (replaces 14 lines with 4 lines of header + reference)

### Update Line 155 (consolidation_type enum in metadata example)

**Current line 155:**
```
"consolidation_type": "granularity_reduction | compound_finding | analytical_view | phase_aggregation | profile_consolidation | redundancy_elimination | narrative_consolidation | compound_interpretation | synthesis",
```

**Replace with:**
```
"consolidation_type": "identical_support_pattern | granularity_reduction | compound_finding | analytical_view | phase_aggregation | profile_consolidation | redundancy_elimination | narrative_consolidation | compound_interpretation | synthesis",
```

### Update Lines 162-178 (consolidation_type descriptions)

**Add after line 163 ("**Common consolidation types:**"):**

```markdown

**PRIMARY (Evidence):**
- `identical_support_pattern` - Items with identical claim support patterns, never cited independently (empirical graph analysis)

```

**Existing Evidence types remain the same, now listed as SECONDARY patterns**

---

## rdmap_pass2_prompt.md Changes

### Location
Similar to claims-evidence prompt, update the "Core Consolidation Principles" section

### Find and Replace

**Find:** The "Core Consolidation Principles" section (approximately lines 93-176)

**Replace with:**

```markdown
## Core Consolidation Principles

**Follow the consolidation hierarchy defined in the skill and reference materials:**

### Consolidation Hierarchy

**For RDMAP Items:**

**PRIMARY:** Assessment Compatibility Test
- RDMAP items (designs, methods, protocols) don't have "support patterns" like evidence
- Use: *"Would I assess these TOGETHER or SEPARATELY?"*
- Design rationale synthesis: Together
- Workflow method sequences: Together if assessed as unified method
- Protocol specifications: Together if describing same tool/procedure
- Temporal comparisons: ALWAYS separate

**For detailed patterns and examples:**  
→ See `/mnt/skills/user/research-assessor/references/checklists/consolidation-patterns.md`

**RDMAP-Specific Guidance:**

**Research Designs** (High-level consolidation appropriate)
- Consolidate multiple rationales for same decision
- Combine spatial/temporal/thematic scope statements
- Preserve distinct hypotheses (especially if different timing)

**Methods** (Moderate consolidation)
- Consolidate workflow sequences into unified methods
- Combine related validation procedures
- Keep different analytical approaches separate

**Protocols** (Minimal consolidation)
- Only consolidate truly redundant specifications
- Preserve measurement precision and parameters
- Keep distinct procedures separate

**CRITICAL:** Temporal comparisons (before/after, phase-by-phase) NEVER consolidate

**Quick workflow:**
```
Step 1: Apply assessment compatibility test (Would I assess together?)
Step 2: Check tier-specific guidance (Design/Method/Protocol)
Step 3: Verify no temporal comparison
Step 4: Document all consolidations with complete metadata
```

---
```

### Update consolidation_type enum (similar location as claims prompt)

Add `identical_support_pattern` to the enum, even though RDMAP rarely uses it:

```
"consolidation_type": "identical_support_pattern | rationale_synthesis | scope_integration | workflow_integration | validation_chain | tool_specification | parameter_integration",
```

**Note:** RDMAP items rarely have identical support patterns since they describe methodology rather than evidence. Include the type for schema consistency, but note it's primarily for evidence consolidation.

---

## Implementation Checklist

### Schema Updates
- [ ] Add `identical_support_pattern` to consolidation_type enum
- [ ] Update schema documentation with definition
- [ ] Update schema version if needed

### Skill Updates  
- [ ] Replace SKILL.md lines 181-190 with new Consolidation Logic section
- [ ] Test skill loading and reference functionality

### Reference Documentation Updates
- [ ] Insert new "PRIMARY: Empirical Graph Analysis" section in consolidation-patterns.md after line 11
- [ ] Update "The Core Principle" section title to "The Core Principles" (lines 3-9)
- [ ] Add distinction between evidence (graph analysis) and claims/context (compatibility test)

### Prompt Updates
- [ ] Update claims-evidence_pass2_prompt.md "Core Consolidation Principles" section
- [ ] Update consolidation_type enum in claims-evidence_pass2_prompt.md
- [ ] Add `identical_support_pattern` to type descriptions
- [ ] Update rdmap_pass2_prompt.md "Core Consolidation Principles" section  
- [ ] Update consolidation_type enum in rdmap_pass2_prompt.md

### Testing
- [ ] Re-run Pass 2 on sobotkova extraction with updated skill/prompts
- [ ] Verify 4 additional consolidations identified (E032+E033, E034+E035, E038+E039, E044+E045+E046)
- [ ] Verify consolidation_metadata.consolidation_type = "identical_support_pattern" used correctly
- [ ] Check reduction percentage reaches 14%+ (closer to 15-20% target)

### Documentation
- [ ] Update skill README if applicable
- [ ] Document this refinement in project change log
- [ ] Note impact on consolidation targets (expect higher reduction with graph analysis)

---

## Expected Impact

### Quantitative
- **Current Pass 2:** 114 → 103 items (9.6% reduction)
- **With graph analysis:** 114 → 98 items (14.0% reduction)
- **Additional consolidations:** 4 (9 evidence items → 4)

### Qualitative
- More objective, verifiable consolidation decisions
- Better alignment with assessment use case
- Reduced reliance on subjective judgment
- Clearer consolidation rationale in metadata

### Architecture
- Foundational logic in skill (stable)
- Detailed patterns in reference docs (expandable)
- Minimal procedural guidance in prompts (maintainable)

---

## Terminology Rationale

**Why `identical_support_pattern` rather than `lego_block` or `empirical_graph`?**

- **Precise:** Describes exactly what the test identifies (identity of support patterns)
- **Technical:** Appropriate for schema/code level terminology
- **Clear:** Unambiguous meaning for future maintainers
- **Descriptive:** Name explains the consolidation logic
- **Searchable:** Easy to find in codebase and documentation

**Alternative considered:**
- `lego_block_support` - Metaphorical, less precise
- `graph_based_consolidation` - Too generic
- `unified_support` - Unclear what makes support "unified"
- `identical_support_pattern` - ✓ Most precise and descriptive

The full phrase "empirical graph analysis" is used in documentation to explain the *methodology*, while `identical_support_pattern` describes the *result* (what was found through that analysis).

---

**End of Implementation Guide**
