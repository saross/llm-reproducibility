# Claims & Evidence Extraction Prompt - PASS 2: Rationalization v2.5

**Version:** 2.5 Pass 2  
**Last Updated:** 2025-10-21  
**Workflow Stage:** Pass 2 - Consolidate and refine Pass 1 extraction  
**Update:** Added source verification for consolidations

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

---

## Sourcing Discipline Reminder

Pass 2 consolidations must maintain v2.5 sourcing requirements established in Pass 1.

**Quick reminder** (see extraction-fundamentals.md for complete guidance):
- **Evidence/Claims:** Must preserve or synthesize `verbatim_quote` from source items
- **Implicit Arguments:** Must preserve all `trigger_text` passages + `trigger_locations`
- **Consolidation rule:** Combined items must maintain source integrity - don't claim anything beyond what verbatim quotes state

When consolidating, ensure:
- All source quotes come from same general location (or explain if not)
- Synthesized quotes represent actual content, not invention
- Most conservative confidence maintained from source items

**For complete sourcing fundamentals:** → See `references/extraction-fundamentals.md`

---

## Quality Checklist for Pass 2

Use this checklist as your roadmap. Before finalizing:

- [ ] 15-20% reduction achieved (higher for measurement-heavy sections OK)
- [ ] All consolidations have complete consolidation_metadata
- [ ] **Source verification complete for consolidations**
- [ ] **Evidence/claims verbatim_quotes preserved through consolidation**
- [ ] **Implicit argument trigger_text preserved through consolidation**
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

## Rationalization Philosophy

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

### Primary Principle: Match Evidence Granularity to Claims

Evidence should be at the same level of detail as the claims they support:
- If claim assesses components **together** → consolidate evidence into compound finding
- If claim assesses components **separately** → keep evidence items separate
- If claims need both views → consider multi-dimensional evidence pattern (below)

**ACID TEST:** "Would I assess the credibility of these statements TOGETHER or SEPARATELY?"
- Together → CONSOLIDATE
- Separately → KEEP DISTINCT

**For detailed consolidation patterns and guidance:**  
→ See `references/checklists/consolidation-patterns.md`

---

### Strategic Duplication: Anchor Numbers in Claims

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

### Multi-Dimensional Evidence Pattern

**Problem:** Some observations contain multiple analytically distinct dimensions supporting different claims.

**Solution:** Create "analytical views" of same underlying data - one primary item plus view items linked via `related_evidence`.

**Example:** Supervision time has temporal dimension (2017 vs 2018) AND total dimension (3.9 hours) supporting different claims. Create E001 (temporal) linked to E002 (total view).

**When to use:**
- Multiple distinct dimensions in same observation
- Each dimension supports different claim  
- Dimensions assessed separately

**When NOT to use:** Simply redundant → consolidate | Different observations → keep separate | Dimensions assessed together → single item

**For complete guidance with JSON examples and decision framework:**  
→ See `references/checklists/consolidation-patterns.md` (Multi-Dimensional Evidence section)

---

### Consolidation Metadata (REQUIRED)

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

**Common consolidation types:**

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

**For complete consolidation patterns and examples:**  
→ See `references/checklists/consolidation-patterns.md`

---

### Strategic Verbosity in Claims

**Principle:** Contextualized claims are more useful than terse claims

**Good verbosity:** Provides interpretive context
- ✅ "Mobile platform enabled collection of 8,343 features across 22 sites with minimal supervision"
- ❌ "Platform worked well"

**Bad verbosity:** Just longer without adding meaning
- ❌ "The mobile platform that was used enabled the collection of many features"

**Balance:** Make claims interpretable without full evidence reproduction

---

### Calculation Claims vs Evidence

**Rule:** If a claim simply restates arithmetic already clear in evidence → remove it

**Test:** "Does this claim require reasoning beyond straightforward arithmetic?"
- If NO → It's redundant, remove it
- If YES → It's interpretation, keep it

**Examples:**

**Remove this claim:**
- Evidence: "40 hours in 2017, 35 hours in 2018"
- Claim: "Total of 75 hours across both seasons" ← Arithmetic, not interpretation

**Keep this claim:**
- Evidence: "40 hours in 2017, 35 hours in 2018"
- Claim: "Efficiency improved in second season" ← Interpretation requiring judgment

---

## Pass 2 Addition Patterns

Pass 1 consistently under-extracts certain claim types. **Actively look for and add these in Pass 2:**

### Pattern 1: Implicit Comparisons
- **Trigger:** Evidence compares values but no explicit comparison claim
- **Look for:** Measurements side-by-side with implicit "better/worse" framing
- **Example:** Platform differences with no explicit superiority claim
- **Test:** "Is there an implicit judgment being made without explicit claim?"

### Pattern 2: Overlooked Explicit Content
- **Trigger:** Explicit recommendations or forward-looking statements missed in Pass 1
- **Look for:** "Should," "would likely," "future work," "recommendations" language
- **Example:** Final paragraph recommendation about QA methods
- **Test:** "Did I capture all explicit recommendations and forward-looking statements?"

### Pattern 3: Cross-Subsection Synthesis
- **Trigger:** Pass 1 focuses on local claims, misses global integration
- **Look for:** Overarching messages spanning multiple subsections
- **Example:** Integration of output + quality + efficiency findings
- **Test:** "What's the overall takeaway integrating findings across this section?"

---

## Consolidation Workflow

### STEP 1: Boundary Verification
- Check evidence/claim classifications (see Pass 1 prompt if unclear)
- Move misclassified arguments to claims
- Move context to project_metadata
- Reclassify professional judgment claims

### STEP 2: Consolidation
- Apply lumping/splitting acid test
- Match evidence granularity to claims
- Create analytical views where appropriate
- Document all consolidations with metadata
- Add missing synthesis/comparison/recommendation claims
- Remove redundant calculation claims

**🚨 Source Verification for Consolidations (v2.5)**

When consolidating evidence/claims/implicit arguments, verify source integrity:

**For evidence and claims (explicit items):**
- Ensure consolidated `verbatim_quote` preserves or synthesizes source text
- All source quotes should come from same general location
- Don't claim anything beyond what's in the verbatim quotes
- If quotes conflict, flag in consolidation_metadata

**For implicit arguments:**
- Preserve all `trigger_text` passages when consolidating
- Update `trigger_locations` to include all source locations
- Update `inference_reasoning` to reflect consolidated understanding
- Maintain most conservative confidence from sources

**Adding implicit arguments in Pass 2:**

Pass 2 may identify implicit arguments missed in Pass 1, particularly:
- **Cross-subsection synthesis** - Unstated assumptions spanning multiple findings
- **Overlooked logical implications** - Implicit reasoning not explicitly stated
- **Comparative interpretations** - Implicit judgments about relative performance

**If adding implicit arguments in Pass 2:**
1. Must have `trigger_text` array with verbatim passages
2. Must have `trigger_locations` for each passage
3. Must have `inference_reasoning` explaining the inference
4. Must explain in extraction_notes why missed in Pass 1

**Verification Reference:**

**For detailed verification procedures:**  
→ See `references/verification-procedures.md`

**Pass 2 verification focuses:**
- Consolidated items preserve source integrity
- No information invented during consolidation
- Verbatim_quotes and trigger_text updated appropriately
- All claims maintain evidential support

**Remember:** Pass 2 consolidates and refines, but maintains same sourcing discipline established in Pass 1.

### STEP 3: Relationship Verification
- Update `supports_claims` arrays after consolidation
- Check `supported_by_evidence` links
- Verify hierarchical claim structure (`supports_claims` within claims array)
- Validate analytical view cross-references (`related_evidence`)

### STEP 4: Quality Checks
- No hallucinations
- **All evidence/claims have verified verbatim_quotes**
- **All implicit arguments have verified trigger_text and trigger_locations**
- **Consolidated items preserve source integrity**
- Support chain integrity maintained
- Consolidation traceability complete
- Information preservation verified
- Strategic verbosity applied
- Other arrays (RDMAP) untouched

---

## Output Format

**Return the same JSON document with these arrays rationalized:**

```json
{
  "schema_version": "2.5",
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

**For complete object structure and field definitions:**  
→ See `references/schema/schema-guide.md`

---

## Pass 2 Goal

Produce rationalized, high-quality extraction with:
- Appropriate granularity matched to claims
- Complete consolidation traceability
- Verified relationships
- No information loss
- Ready for validation (Pass 3)