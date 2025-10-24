# Consolidation Patterns - When to Lump vs Split

## The Core Principles

**Acid Test: "Would I assess these items TOGETHER or SEPARATELY?"**

- **Together** → CONSOLIDATE
- **Separately** → KEEP DISTINCT

Match granularity to assessment needs, not just to reduce item count.

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
```

**Critical Rule:** Temporal comparisons ALWAYS remain separate, regardless of support pattern identity. The comparison itself is the analytical value.

### When Graph Analysis Is Inconclusive

If evidence items have:
- No claim support (might be project_metadata)
- Complex overlapping patterns (neither identical nor independent)
- Unclear independence (ambiguous citations)

→ Fall back to secondary test: "Would I assess TOGETHER or SEPARATELY?"

---

## SECONDARY: Assessment Compatibility Test

When empirical graph analysis is inconclusive (e.g., no claim support, complex patterns), use the assessment compatibility test.

**The Question:** "Would I assess the credibility of these items TOGETHER or SEPARATELY?"

**Application Notes:**
- This is the fallback when graph analysis doesn't provide clear guidance
- For evidence with clear support patterns, use graph analysis first
- For claims and context items (which don't have "support patterns"), this is the primary test

## Decision Framework

### When to CONSOLIDATE (Lump)

**1. Same Entity Specifications**
- Multiple properties of the same object
- Example: Map scale + source + date → single map specification
- Rationale: Assessed together as compound description

**2. Compound Judgments**
- Multiple quality dimensions assessed together
- Example: "Data are accurate AND complete" → single quality claim
- Rationale: Joint assessment of quality

**3. Joint Capabilities**
- Features that work together as a system
- Example: Multiple software features → platform capabilities
- Rationale: Assessed as integrated functionality

**4. Single Workflows**
- Steps in a coherent process
- Example: Multiple staff tasks in validation → validation workflow
- Rationale: Process evaluated as whole

**5. Profile Consolidation**
- Multiple characteristics of same phenomenon
- Example: Different error types → error profile
- Rationale: Comprehensive characterization

### When to SPLIT (Keep Separate)

**1. Different Claims**
- Items support different assertions
- Example: Accuracy % vs Completeness % → separate (independent dimensions)
- Rationale: Different assessment implications

**2. Different Assessments**
- Items require separate credibility evaluation
- Example: Platform output vs platform efficiency → separate
- Rationale: Different evidence chains

**3. Different Sources**
- Items from different sections or contexts
- Example: Methods description vs Results measurement → separate
- Rationale: Different evidential basis

**4. Different Concerns**
- Items address distinct aspects
- Example: Data quality vs data quantity → separate
- Rationale: Orthogonal dimensions

**5. Temporal Comparisons**
- Year-over-year, before/after, phase-by-phase
- Example: 2017 hours vs 2018 hours → ALWAYS separate
- Rationale: Comparison requires separate items

## Common Patterns

### Evidence Consolidation Patterns

**Granularity Reduction:**
- Multiple measurements → aggregate finding
- Example: Individual GPS points → overall spatial coverage
- Use when: Claim references aggregate, not individuals

**Compound Finding:**
- Related observations → integrated result
- Example: Count + percentage + quality → complete measurement
- Use when: Claim needs full picture

**Analytical View:**
- Same data, different organization
- Example: Staff time by person → staff time by phase
- Use when: Multiple perspectives needed
- Special: Create primary item + analytical_view cross-reference

**Phase Aggregation:**
- Temporal combination (NOT comparison)
- Example: Three seasons → total project timeline
- Use when: Overall scope matters more than phases
- Warning: Do NOT aggregate if comparing phases

### Claim Consolidation Patterns

**Narrative Consolidation:**
- Problem + cause + solution → integrated story
- Example: Supervision challenge + mobile solution + efficiency gain
- Use when: Claims form coherent narrative

**Compound Interpretation:**
- Multiple judgments → integrated assessment
- Example: "Large output" + "high quality" + "low supervision" → "effective system"
- Use when: Combined assessment is the point

**Synthesis:**
- Cross-subsection integration
- Example: Method description + Results findings → Discussion synthesis
- Use when: Overarching conclusion spans sections

## Anti-Patterns (Don't Do This)

**❌ Over-Consolidation:**
- Merging items that need separate assessment
- Example: Combining all platform features into one item
- Problem: Loses ability to assess specific capabilities

**❌ Temporal Consolidation:**
- Combining year-over-year or before/after measurements
- Example: 2017 hours + 2018 hours → "total hours"
- Problem: Destroys comparison basis

**❌ Dimension Mixing:**
- Combining orthogonal quality dimensions
- Example: Accuracy + Completeness → "quality score"
- Problem: Different dimensions need separate evaluation

**❌ Information Loss:**
- Summarizing instead of consolidating exact text
- Example: "Multiple GPS measurements" instead of actual values
- Problem: Cannot verify against source

## Special Cases

### Multi-Dimensional Evidence

**Problem:** Evidence organized by multiple dimensions (e.g., by person AND by phase)

**Solution:** Create analytical views
1. Choose primary dimension (e.g., by person)
2. Create primary evidence item
3. Create analytical view with secondary dimension (e.g., by phase)
4. Link via `related_evidence` field

**Example:**
```json
{
  "evidence_id": "E001",
  "evidence_text": "Supervision time: Alice 40h, Bob 35h",
  "related_evidence": ["E002"]  // Links to phase view
}
{
  "evidence_id": "E002",
  "evidence_text": "Supervision time: 2017 40h, 2018 35h",
  "related_evidence": ["E001"],  // Links back to person view
  "consolidation_metadata": {
    "consolidation_type": "analytical_view"
  }
}
```

### Anchor Numbers in Claims

**Pattern:** Claims can include key numbers for context

**Example:**
```json
Evidence: "Collected 8,343 features"
Claim: "Mobile platform enabled collection of 8,343 features with minimal supervision"
```

**Rationale:** Strategic duplication makes claim interpretable without referring to evidence. The number provides necessary anchor.

**Rule:** Include numbers that make claims meaningful, not full data reproduction.

## Consolidation Metadata

**All consolidated items MUST include:**

```json
"consolidation_metadata": {
  "consolidated_from": ["P1_E001", "P1_E002"],  // Source item IDs
  "consolidation_type": "granularity_reduction",  // Type of consolidation
  "information_preserved": "complete",  // Did we lose information?
  "granularity_available": "Individual GPS points available in source",
  "rationale": "Claim references aggregate coverage, not individual points"
}
```

**Consolidation Types:**

**For Evidence:**
- `granularity_reduction` - Fine → aggregate
- `compound_finding` - Multiple measurements → integrated
- `analytical_view` - Reorganize by different dimension
- `phase_aggregation` - Temporal combination (not comparison)
- `profile_consolidation` - Multiple characteristics → complete profile
- `redundancy_elimination` - Overlapping items merged

**For Claims:**
- `narrative_consolidation` - Problem + solution → story
- `compound_interpretation` - Multiple judgments → integrated
- `synthesis` - Cross-subsection integration

## Quality Checks

**After consolidation, verify:**

1. ✅ All information from source items preserved (or loss documented)
2. ✅ Consolidation type appropriate for content
3. ✅ Consolidation metadata complete
4. ✅ Cross-references updated correctly
5. ✅ Granularity matches assessment needs
6. ✅ No temporal comparisons consolidated
7. ✅ Related evidence links correct for analytical views

## Target Outcomes

**Pass 2 Reduction Targets:**
- Overall: 15-20% reduction in items
- Evidence-heavy sections: May be higher (up to 40%)
- Claim-heavy sections: May be lower (10-15%)

**Balance:**
- Reduce over-extraction from Pass 1
- Maintain assessment-appropriate granularity
- Preserve all critical information
- Document all changes with metadata

## Quick Decision Tree

```
1. Read items being considered
   ↓
2. Apply ACID TEST: "Assess together or separately?"
   ↓
3. If TOGETHER:
   - Same entity? Compound judgment? Joint capability? Single workflow?
   - YES → LUMP with appropriate consolidation_type
   - NO → Check for over-consolidation risk
   ↓
4. If SEPARATELY:
   - Different claims? Different assessments? Different sources? Different concerns?
   - YES → SPLIT or keep separate
   - NO → Reconsider consolidation
   ↓
5. Document decision with consolidation_metadata
   ↓
6. Update all cross-references
```

## Remember

- **Consolidation is about appropriate granularity, not just fewer items**
- **When uncertain, keep separate** - Splitting is harder than lumping
- **Temporal comparisons NEVER consolidate** - Critical assessment pattern
- **All consolidations need complete metadata** - Traceability is essential
- **Preserve exact text** - Don't summarize, consolidate verbatim content
- **Update relationships** - Cross-references must reflect consolidation
