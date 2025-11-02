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
- [ ] Systematic implicit argument completeness review complete (STEP 3)
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

**Follow the consolidation hierarchy defined in the skill and reference materials:**

### Consolidation Hierarchy

**For Evidence Items:**

1. **Empirical Graph Analysis** (PRIMARY)
   - Identify evidence with identical claim support patterns
   - See `references/checklists/consolidation-patterns.md` for complete algorithm and examples
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
→ See `references/checklists/consolidation-patterns.md`

**Quick workflow:**
```
Step 1: Map evidence support patterns → Find identical patterns
Step 2: Verify no temporal comparison → Consolidate as identical_support_pattern
Step 3: For remaining items, apply assessment compatibility test
Step 4: Document all consolidations with complete metadata
```

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
  "consolidation_type": "identical_support_pattern | granularity_reduction | compound_finding | analytical_view | phase_aggregation | profile_consolidation | redundancy_elimination | narrative_consolidation | compound_interpretation | synthesis",
  "information_preserved": "complete | lossy_granularity | lossy_redundancy",
  "granularity_available": "Description of additional detail available in source",
  "rationale": "Why consolidation appropriate"
}
```

**Common consolidation types:**

**PRIMARY (Evidence):**
- `identical_support_pattern` - Items with identical claim support patterns, never cited independently (empirical graph analysis)

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

### STEP 3: Implicit Argument Completeness Review

**Systematic review for implicit arguments missed in Pass 1:**

With full-paper context, review all CORE claims for implicit arguments using the 4-type framework:

**Type 1 - Logical Implications:** "If this claim is true, what MUST also be true?"
**Type 2 - Unstated Assumptions:** "What must be true for this claim to hold?"
**Type 3 - Bridging Claims:** "How do they get from evidence to this claim?"
**Type 4 - Disciplinary Assumptions:** "What field-specific knowledge is taken for granted?"

**Focus areas for Pass 2 cross-section synthesis:**
- Assumptions spanning multiple sections (e.g., threshold criteria used throughout)
- Comparative interpretations (implicit judgments about relative performance)
- Methodological assumptions visible only when seeing full argument arc

**Quality check:** If <3 implicit arguments total and paper makes complex arguments, verify reasoning is genuinely explicit (rare). Document verification in extraction_notes.

**🚨 Source Verification (REQUIRED)**

**For ALL items (consolidated or not), verify:**

1. **Consolidation integrity** (if item was consolidated):
   - Verbatim_quote/trigger_text preserves or synthesizes source appropriately
   - No information invented
   - Most conservative confidence maintained

2. **Quote compliance** (all explicit items):
   - Read if uncertain: `references/verbatim-quote-requirements.md`
   - Complete sentences only (no mid-sentence fragments)
   - Exact text from paper (no paraphrasing)
   - Verify quote exists: "Can I find this EXACT text in paper?"

3. **Multi-location sourcing** (any item with discontinuous sources):
   - **If item draws from multiple distinct locations → include quotes/trigger_text from ALL locations**
   - This applies to: consolidated evidence, cross-subsection implicit arguments, synthesized claims
   - Document all locations in source_location/trigger_locations
   - Example: Evidence consolidated from paragraphs on pages 3 and 7 needs verbatim_quote text from both locations

4. **Fix if needed:**
   - Missing sentence start → Add context to complete sentence
   - Paraphrased text → Replace with actual verbatim text
   - Incomplete multi-location sourcing → Add missing quotes/trigger_text
   - Quote not found → Locate and update
   - Cannot verify → Mark `extraction_confidence: "low"` with note

**Adding implicit arguments in Pass 2:**

Pass 2 systematically reviews for implicit arguments missed in Pass 1 (see STEP 3), particularly:
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

### STEP 3: Relationship Verification & Bidirectional Consistency

**🚨 CRITICAL: All mappings must be BIDIRECTIONAL**

Every relationship between entities must be recorded in BOTH directions. This is mandatory for data integrity and analysis.

**Bidirectional mapping pairs:**
- Claim→Evidence: `claims.supported_by` ↔ `evidence.supports_claims`
- Claim→Claim: `claims.supports_claims` (parent→child)
- Evidence→Evidence: `evidence.related_evidence` (bidirectional peer relationship)

**When creating or updating mappings:**
1. **Forward reference created** → Immediately create reverse reference
   - Example: Add E005 to C001.supported_by → Add C001 to E005.supports_claims
2. **Consolidation performed** → Update BOTH directions
   - Example: Consolidate E005+E006→E005 → Update all claims referencing E006 to E005 AND update E005.supports_claims to include all claims from both items
3. **Reference removed** → Remove from BOTH directions
   - Example: Remove E005 from C001.supported_by → Remove C001 from E005.supports_claims

**Verification checklist:**
- [ ] Every ID in `claims.supported_by` has corresponding entry in `evidence.supports_claims`
- [ ] Every ID in `evidence.supports_claims` has corresponding entry in `claims.supported_by`
- [ ] No orphaned references (referencing non-existent IDs)
- [ ] No duplicate IDs within arrays
- [ ] Hierarchical claim structures valid (no circular references)
- [ ] Analytical view cross-references (`related_evidence`) symmetrical

**🚨 CRITICAL: Cross-Reference Repair After Consolidation**

When consolidating items, cross-references in OTHER arrays must be updated to point to the new consolidated IDs. This is MANDATORY to prevent broken references.

**Consolidation algorithm:**
1. Identify all arrays that reference the items being consolidated
2. Replace old IDs with new consolidated ID in ALL locations
3. Update reverse mappings in the consolidated item
4. Verify bidirectional consistency after consolidation

**For complete cross-reference repair procedure (including algorithm and validation):**
→ See `references/checklists/consolidation-patterns.md` (Cross-Reference Repair After Consolidation section, lines 411-520)

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