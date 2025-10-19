# Claims & Evidence Extraction Prompt - PASS 2: Rationalization v2.4

**Version:** 2.4 Pass 2  
**Last Updated:** 2025-10-19  
**Workflow Stage:** Pass 2 - Consolidate and refine Pass 1 extraction  
**Update:** Clarified iterative accumulation workflow; integrated v2.3 consolidation metadata and multi-dimensional evidence patterns

---

## Your Task

Review Pass 1 extraction and apply consolidation principles to produce rationalized, high-quality evidence/claims/implicit arguments. Pass 1 intentionally over-extracted (~40-50%). Your job is to consolidate, correct boundaries, and verify relationships.

**Input:** JSON extraction document with evidence/claims/implicit arguments populated from Pass 1
- May also contain RDMAP arrays from separate extraction

**Your responsibility:** Refine these arrays in place:
- `evidence`
- `claims`
- `implicit_arguments`
- `project_metadata`

**Leave untouched:**
- `research_designs`, `methods`, `protocols` (RDMAP arrays - rationalized separately)
- Any other arrays not your responsibility

**Output:** Same JSON document with evidence/claims/implicit arguments rationalized

**You also have access to:** Original section text (for verification)

---

## RATIONALIZATION PHILOSOPHY FOR PASS 2

**Goals:**
- Reduce over-extraction to appropriate granularity (target 15-20% reduction)
- Correct evidence/claim boundary errors
- Remove items that don't support claims (move to project_metadata)
- Consolidate redundant or over-granular items
- Add missing implicit generalizations
- Verify all relationships accurate

**Expected outcome:**
- 15-20% reduction in total items (may be higher for measurement-heavy sections)
- Better evidence/claim boundaries
- Appropriate consolidation without information loss
- All claims have clear evidential support
- Complete consolidation traceability via metadata

**NOT expansion:** Pass 2 consolidates and refines. Do not add new items unless clearly missed in Pass 1.

---

## Core Consolidation Principles

### The Lumping/Splitting Decision Framework

**PRIMARY PRINCIPLE: Match Evidence Granularity to Claim Granularity**

Evidence should be at the same level of detail as the claims they support:
- If claim assesses components **together** → consolidate evidence into compound finding
- If claim assesses components **separately** → keep evidence items separate
- If claims need both views → consider multi-dimensional evidence pattern (see below)

**ACID TEST:** "Would I assess the credibility of these statements TOGETHER or SEPARATELY?"
- Together → CONSOLIDATE
- Separately → KEEP DISTINCT

---

### Anchor Numbers Principle (Strategic Duplication)

**Rule:** Claims can include key quantitative values that provide necessary context, even if these numbers appear in evidence. This is acceptable strategic duplication that makes claims interpretable.

**Good anchor numbers:**
- ✅ Essential context: "System produced 8,343 features at 54 seconds per feature"
- ✅ Scale indicators: "Completed 125.8 person-hours of survey"
- ✅ Key metrics: "Achieved 95.7% accuracy"

**Avoid full duplication:**
- ❌ Reproducing entire evidence verbatim in claim
- ❌ Including every number from evidence in claim

**Balance:** Make claims interpretable while maintaining claim-evidence graph traceability

---

### Multi-Dimensional Evidence Pattern (NEW v2.3)

**Problem:** Some observations contain multiple analytically distinct dimensions that support different claims

**Example:** Supervision time data
- **Dimension 1 (Temporal):** "2.4 hours in 2017, 1.5 hours in 2018" → supports temporal comparison claim
- **Dimension 2 (Total):** "3.9 hours total" → supports efficiency claim

**Solution:** Create "analytical views" of same underlying data

**Primary evidence item:**
```json
{
  "evidence_id": "E001",
  "evidence_text": "Supervision time: 2.4 hours (2017), 1.5 hours (2018), 3.9 hours total",
  "related_evidence": ["E002"]
}
```

**Analytical view:**
```json
{
  "evidence_id": "E002", 
  "evidence_text": "Total supervision time: 3.9 hours across both field seasons",
  "related_evidence": ["E001"],
  "extraction_notes": "Analytical view of E001 emphasizing total rather than temporal progression"
}
```

**When to use:**
- Multiple analytically distinct dimensions in same observation
- Each dimension supports different claim
- Dimensions would be assessed separately

**When NOT to use:**
- Simply redundant measurements → consolidate
- Different observations → keep separate (not views)
- Dimensions assessed together → single consolidated item

---

### Consolidation Metadata (REQUIRED v2.3)

**ALL consolidated items MUST have complete consolidation_metadata.**

```json
"consolidation_metadata": {
  "consolidated_from": ["P1_E001", "P1_E002"],
  "consolidation_type": "granularity_reduction | compound_finding | analytical_view | phase_aggregation | profile_consolidation | redundancy_elimination | narrative_consolidation | compound_interpretation | synthesis",
  "information_preserved": "complete | lossy_granularity | lossy_redundancy",
  "granularity_available": "Description of additional detail available in source",
  "rationale": "Why consolidation appropriate"
}
```

**Consolidation types:**

**Evidence:**
- `granularity_reduction` - Fine measurements → aggregate
- `compound_finding` - Multiple measurements → single finding
- `analytical_view` - Reorganize by different dimension
- `phase_aggregation` - Temporal combination
- `profile_consolidation` - Multiple characteristics → complete profile
- `redundancy_elimination` - Overlapping items merged

**Claims:**
- `narrative_consolidation` - Problem + cause + solution → story
- `compound_interpretation` - Multiple judgments → integrated assessment
- `synthesis` - Cross-subsection integration → overarching conclusion

---

### Strategic Verbosity in Claims (NEW v2.3)

**Principle:** Contextualized claims are more useful than terse claims

**Good verbosity:** Provides interpretive context
- ✅ "Mobile platform enabled collection of 8,343 features across 22 sites with minimal supervision"
- ❌ "Platform worked well"

**Bad verbosity:** Just longer without adding meaning
- ❌ "The mobile platform that was used enabled the collection of many features"

**Balance:** Make claims interpretable without full evidence reproduction

---

### Calculation Claims vs Evidence (NEW v2.3)

**Rule:** If a claim simply restates arithmetic already clear in evidence → remove it

**Test:** "Does this claim require reasoning beyond straightforward arithmetic?"
- If NO → It's redundant, remove it
- If YES → It's interpretation, keep it

**Example - Remove:**
- Evidence: "40 hours in 2017, 35 hours in 2018"
- Claim: "Total of 75 hours across both seasons" ← This is arithmetic, not interpretation

**Example - Keep:**
- Evidence: "40 hours in 2017, 35 hours in 2018"
- Claim: "Efficiency improved in second season" ← This is interpretation requiring judgment

---

## Pass 2 Addition Patterns (NEW v2.3)

Pass 1 consistently under-extracts certain claim types. **Actively look for and add these in Pass 2:**

**Pattern 1: Implicit Comparisons**
- **Trigger:** Evidence compares values but no explicit comparison claim
- **Look for:** Measurements side-by-side with implicit "better/worse" framing
- **Example:** Platform differences with no explicit superiority claim
- **Test:** "Is there an implicit judgment being made without explicit claim?"

**Pattern 2: Overlooked Explicit Content**
- **Trigger:** Explicit recommendations or forward-looking statements missed in Pass 1
- **Look for:** "Should," "would likely," "future work," "recommendations" language
- **Example:** Final paragraph recommendation about QA methods
- **Test:** "Did I capture all explicit recommendations and forward-looking statements?"

**Pattern 3: Cross-Subsection Synthesis**
- **Trigger:** Pass 1 focuses on local claims, misses global integration
- **Look for:** Overarching messages spanning multiple subsections
- **Example:** Integration of output + quality + efficiency findings
- **Test:** "What's the overall takeaway integrating findings across this section?"

---

## Consolidation Workflow

### STEP 1: Boundary Verification
- Check evidence/claim classifications
- Move misclassified arguments to claims
- Move context to project_metadata
- Reclassify professional judgment claims

### STEP 2: Consolidation
- Apply lumping/splitting test
- Match evidence granularity to claims
- Create analytical views where appropriate
- Document all consolidations with metadata
- Add missing synthesis/comparison/recommendation claims
- Remove redundant calculation claims

### STEP 3: Relationship Verification
- Update supports_claims arrays after consolidation
- Check supported_by_evidence links
- Verify hierarchical claim structure
- Validate analytical view cross-references

### STEP 4: Quality Checks
- No hallucinations
- All verbatim_quotes verified
- Support chain integrity
- Consolidation traceability
- Information preservation verified
- Strategic verbosity applied
- Other arrays (RDMAP) untouched

---

## Output Format

**Return the same JSON document with these arrays rationalized:**

```json
{
  "schema_version": "2.4",
  "extraction_timestamp": "ISO 8601",
  "extractor": "Claude Sonnet 4.5",
  
  "evidence": [evidence_object],          // Rationalized
  "claims": [claim_object],               // Rationalized
  "implicit_arguments": [IA_object],      // Rationalized
  "project_metadata": {...},              // Rationalized
  
  // These arrays remain unchanged:
  "research_designs": [...],              // Leave untouched
  "methods": [...],                       // Leave untouched
  "protocols": [...],                     // Leave untouched
  
  "extraction_notes": {
    "pass": 2,
    "section_extracted": "string",
    "items_before_rationalization": 85,
    "items_after_rationalization": 69,
    "reduction_percentage": 18.8,
    "consolidations_performed": 16,
    "additions_performed": 3,
    "boundary_corrections": 2
  }
}
```

---

## Quality Checklist for Pass 2

Before finalizing:

- [ ] 15-20% reduction achieved (higher for measurement-heavy sections OK)
- [ ] All consolidations have complete consolidation_metadata
- [ ] No information loss from consolidations
- [ ] No remaining redundancy
- [ ] Evidence/claim boundaries accurate
- [ ] All claims have evidential support
- [ ] Multi-dimensional evidence appropriately handled
- [ ] Anchor numbers appropriately included in claims
- [ ] Redundant calculation claims removed
- [ ] Strategic verbosity applied
- [ ] Addition patterns checked (comparisons, recommendations, synthesis)
- [ ] All relationships verified and bidirectional
- [ ] Other arrays (RDMAP) untouched

---

## Remember

**Pass 2 is about CONSOLIDATION AND REFINEMENT, not expansion.**

- Reduce granularity appropriately
- Preserve all critical information
- Document all consolidations
- Verify all relationships
- **Don't touch RDMAP arrays** - those are rationalized separately

**Your goal:** Produce rationalized, high-quality extraction ready for validation and assessment.