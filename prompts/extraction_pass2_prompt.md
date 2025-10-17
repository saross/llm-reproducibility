# Claims Extraction Prompt - PASS 2: Rationalization v2.2

**Version:** 2.2 Pass 2  
**Last Updated:** 2025-10-17  
**Workflow Stage:** Pass 2 of 2 - Consolidate and refine Pass 1 extraction

**Quick Reference:** A scannable version of the core consolidation rules is available in `consolidation_rules_v1.md` for rapid decision lookup during work. This prompt is self-contained and includes all necessary guidance, but the rules document provides a convenient quick reference format.

---

## Your Task

Review the Pass 1 extraction and apply consolidation principles to produce a rationalized, high-quality extraction. Pass 1 intentionally over-extracted (~40-50% more items than needed). Your job is to consolidate, correct, and verify.

---

## RATIONALIZATION PHILOSOPHY FOR PASS 2

**Goals:**
- Reduce over-extraction to appropriate granularity
- Correct evidence/claim boundary errors
- Remove items that don't support claims (move to project_metadata)
- Consolidate redundant or over-granular items
- Add missing implicit generalizations
- Verify all relationships are accurate

**You have access to:**
1. Pass 1 extraction JSON (may be over-extracted and over-granular)
2. Original section text (for verification and fact-checking)

**Expected outcome:**
- 15-20% reduction in total items
- Better evidence/claim boundaries
- Appropriate consolidation without loss of information
- All claims have clear evidential support
- Accurate citations and no hallucinations

---

## Core Consolidation Principles

### The Lumping/Splitting Decision Framework

**ACID TEST:** "Would I assess the credibility of these statements TOGETHER or SEPARATELY?"
- Together → LUMP (consolidate)
- Separately → SPLIT (keep distinct)

### When to LUMP (Consolidate)

**1. Multiple observations specify the same entity**
- Example: Map scale (1:5000) + digitized from paper maps + source date (1920s) → Single "map specifications" evidence
- Rationale: Descriptive details about one thing belong together

**2. Multiple interpretations form a single compound claim**
- Example: "Maps are accurate" + "represent pre-modern landscapes" → Single claim: "Maps accurately represent pre-modern landscapes"
- Rationale: Professional judgment components assessed together

**3. Technical features that jointly support one capability claim**
- Example: Multiple automation features → Single "automation capabilities" evidence
- Rationale: Individual features matter less than overall capability they enable

**4. Process steps that form a single workflow**
- Example: Multiple staff preparation tasks → Single "staff handled geospatial preparation" evidence
- Rationale: Division of labor principle matters, not individual task granularity

### When to SPLIT (Keep Separate)

**1. Different observations support different claims**
- Example: Student hours (efficiency dimension) vs features generated (output dimension)
- Rationale: Different assessment questions require different evidence

**2. Claims have different assessment requirements**
- Example: Accuracy (95.7%) vs completeness (83%) - different quality dimensions
- Rationale: Independent credibility assessments needed

**3. Evidence comes from different sources or methods**
- Example: Direct measurement vs professional judgment
- Rationale: Confidence basis differs, requires separate tracking

**4. Alternative limitations address different concerns**
- Example: ArcGIS connectivity requirement vs multi-app architecture complexity
- Rationale: Support different arguments about why alternatives inadequate

---

## Rationalization Operations

### OPERATION 1: REMOVE

**Remove items that don't support claims** → Move to project_metadata

**What to remove:**
- Timeline information (field seasons, phases)
- Location context (field sites, work settings)
- Resource constraints (equipment limitations)
- Track record (prior uses of method/tool)
- Vague process descriptions without evidential role

**Test:** "Would removing this cause a claim to lose evidential support?"
- NO → Remove to project_metadata
- YES → Keep as evidence

### OPERATION 2: CONSOLIDATE

**Lump over-granular items following the decision framework**

**Category-specific consolidation patterns:**

**Map/Source Specifications:**
- Pattern: Multiple descriptive details → Single specification
- Example: Scale + source type + date + coverage → "Historical maps (1:5000 scale, digitized from 1920s paper sources covering survey region)"

**Platform/Tool Features:**
- Pattern: Individual capabilities → Overall capability claim
- Example: List of 8 automation features → "Platform provides comprehensive automation (feature selection, data validation, workflow management)" + count as evidence

**Staff Work:**
- Pattern: Individual tasks → Role/responsibility summary
- Example: Multiple preparation tasks → "Staff handled geospatial data preparation and quality control"

**Participant Information:**
- Pattern: Keep separate if supporting different claims
- Example: Participation time vs output quantity vs device patterns - each supports different efficiency/preference claims

**Validation Results:**
- Pattern: Keep quality dimensions separate
- Example: Accuracy vs completeness - different assessment dimensions

### OPERATION 3: SPLIT

**Separate over-consolidated items if they serve different assessment purposes**

Rare in Pass 2 (Pass 1 should be granular), but watch for:
- Multiple quality dimensions bundled together
- Different evidence sources conflated
- Distinct claims merged inappropriately

### OPERATION 4: RECLASSIFY

**Correct evidence/claim boundary errors**

**Evidence → Claim when:**
- Requires expertise to assess (e.g., "maps are accurate")
- Involves professional judgment
- Makes inference beyond observation
- Generalizes from specific observation

**Claim → Evidence when:**
- Direct observation misclassified
- Can be verified without expertise
- No interpretive framing involved

### OPERATION 5: ADD

**Add missing implicit generalizations**

**Pattern: Single-case observation → Domain-level claim**

When Pass 1 has project-specific observation that supports domain claim but didn't extract the implicit generalization:

1. Identify the pattern (e.g., "12/12 students had smartphones")
2. Extract implicit generalization as claim (e.g., "Volunteers prefer mobile devices")
3. Mark `claim_status: "implicit"`
4. Set `extraction_flags.generalization_from_single_case: true`
5. Link evidence to implicit claim, implicit claim to broader claim

### OPERATION 6: VERIFY

**Quality checks:**

1. **Relationship verification**
   - Every claim has evidential support (claims or evidence IDs)
   - Support chains are logical (evidence → supporting → intermediate → core)
   - No orphaned items

2. **Citation accuracy**
   - All verbatim quotes are accurate (check against source text)
   - Page numbers correct
   - No hallucinated content

3. **Boundary clarity**
   - Evidence/claim classifications defensible
   - Uncertain items have `boundary_ambiguous` flag

4. **Completeness**
   - No important content from source text missed
   - Implicit generalizations surfaced
   - Project metadata properly separated

---

## Change Log Format

For each modification, document:

```json
{
  "change_log": [
    {
      "operation": "CONSOLIDATE",
      "item_ids": ["E001", "E005", "E007"],
      "result_id": "E001-CONSOLIDATED",
      "rationale": "Multiple observations specify same entity (map specifications)",
      "consolidated_text": "[The merged text]"
    },
    {
      "operation": "REMOVE",
      "item_ids": ["E012"],
      "moved_to": "project_metadata.timeline",
      "rationale": "Timeline information - doesn't support claims"
    },
    {
      "operation": "RECLASSIFY",
      "item_id": "E003",
      "old_classification": "evidence",
      "new_classification": "claim (INTERPRETATION)",
      "new_id": "C002-NEW",
      "rationale": "Requires professional judgment to assess accuracy"
    },
    {
      "operation": "ADD",
      "new_id": "C-NEW",
      "rationale": "Implicit generalization from single-case observation E018-NEW",
      "linked_to": ["E018-NEW"]
    }
  ]
}
```

---

## Category-Specific Consolidation Guidance

### Map/Source Materials

**Common over-extraction:**
- Scale, source type, date, coverage area, digitization method all as separate items

**Consolidate to:**
- ONE evidence item: Source specifications
- ONE claim (if applicable): Quality/accuracy assessment

**Example:**
Before: E001 (scale), E005 (digitized from paper), E007 (1920s)
After: E001-CONSOLIDATED "Historical maps at 1:5000 scale, digitized from 1920s paper sources"

### Platform/Tool Features

**Common over-extraction:**
- Each individual feature as separate evidence

**Consolidate to:**
- Overall capabilities as evidence
- Implicit claim about capability if generalized

**Example:**
Before: 8 separate automation features
After: E-PLATFORM "Platform provides comprehensive automation for feature selection, validation, and workflow management (8 specific capabilities)"

### Participant Data

**When to keep separate:**
- Different dimensions (time, output, device usage) supporting different claims
- Different metrics requiring independent assessment

**Example - Keep separate:**
- E011: Student hours (supports efficiency claim)
- E012: Features generated (supports output claim)
- E018-NEW: Device ownership (supports preference claim)

### Validation Results

**Always keep separate:**
- Different quality dimensions (accuracy vs completeness)
- Different validation approaches
- Different metrics

**Example - Keep separate:**
- Accuracy: 95.7%
- Completeness: 83%
Rationale: Independent quality assessments

---

## Quality Criteria for Pass 2

Good Pass 2 rationalization demonstrates:
- **Appropriate consolidation:** 15-20% reduction from Pass 1 without information loss
- **Boundary accuracy:** Evidence/claim classifications correct
- **Relationship integrity:** All support chains valid and logical
- **Citation accuracy:** No hallucinations, all quotes verified
- **Completeness:** No important content missed
- **Granularity match:** Items at appropriate level for assessment

---

## Common Rationalization Mistakes to Avoid

1. **Over-consolidation:** Merging items that need separate assessment
2. **Under-consolidation:** Not lumping clearly related specifications
3. **Breaking support chains:** Consolidating evidence but not updating claim links
4. **Citation errors:** Introducing inaccuracies when merging text
5. **Losing implicit content:** Not surfacing single-case generalizations
6. **Removing too much:** Moving supportive evidence to metadata
7. **Hallucination:** Adding content not in source text

---

## Output Format

Produce:
1. **Rationalized JSON** following schema v2.2
2. **Change log** documenting all operations
3. **Summary statistics:**
   - Pass 1 item count
   - Pass 2 item count
   - Reduction percentage
   - Operations breakdown (# consolidated, # removed, # reclassified, # added)

---

## Notes

- Always have source text available for verification
- Default to keeping items separate if uncertain (splitting beats over-lumping)
- Document rationale for major consolidations
- Preserve all important information from Pass 1
- Focus on enabling credibility assessment (appropriate granularity)
- This is still **extraction** work (structuring content), not **assessment** (evaluating credibility)