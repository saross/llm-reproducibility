# RDMAP Extraction Prompt - PASS 2: Rationalization v2.4

**Version:** 2.4 Pass 2  
**Last Updated:** 2025-10-20  
**Workflow Stage:** Pass 2 of 3 - Consolidate and refine Pass 1 RDMAP extraction  
**Skill Context:** This prompt is part of the research-assessor skill

---

## Your Task

Review Pass 1 RDMAP extraction and apply consolidation principles to produce rationalized, high-quality research designs, methods, and protocols. Pass 1 intentionally over-extracted (~40-50%). Your job is to consolidate, correct tier boundaries, and verify relationships.

**Input:** JSON extraction document with RDMAP arrays populated from Pass 1
- May also contain claims/evidence arrays from separate extraction

**Your responsibility:** Refine these arrays in place:
- `research_designs`
- `methods`
- `protocols`

**Leave untouched:**
- `evidence`, `claims`, `implicit_arguments` (rationalized separately)
- Any other arrays not your responsibility

**Output:** Same JSON document with RDMAP arrays rationalized

---

## Quality Checklist for Pass 2

Use this checklist as your roadmap. Before finalizing:

- [ ] 15-20% reduction achieved (may vary by section type)
- [ ] All consolidations have complete consolidation_metadata
- [ ] No information loss from consolidations
- [ ] No remaining redundancy (check for duplicate tool specs, repeated rationales)
- [ ] Tier assignments accurate (WHY → Design, WHAT → Method, HOW → Protocol)
- [ ] All cross-references bidirectional and valid
- [ ] RDMAP vs claims boundary accurate (descriptions vs arguments)
- [ ] Reasoning approach consistent (claimed vs inferred match)
- [ ] Expected information gaps flagged appropriately
- [ ] Location fields preserved through consolidation
- [ ] Other arrays (claims/evidence) untouched

---

## Rationalization Philosophy

**Goals:**
- Reduce over-extraction to appropriate granularity (target 15-20% reduction)
- Correct tier assignment errors (WHY vs WHAT vs HOW)
- Consolidate redundant methodological descriptions
- Verify boundary accuracy (RDMAP vs claims)
- Validate all cross-references
- Complete expected information review

**Expected outcome:**
- 15-20% reduction in total items
- Better tier boundaries (Design vs Method vs Protocol)
- Appropriate consolidation without information loss
- All cross-references bidirectional and valid
- Complete traceability via metadata

**NOT expansion:** Pass 2 consolidates and refines. Do not add new items unless clearly missed in Pass 1.

---

## Core Consolidation Principles

### The Acid Test: "Would I Assess These Together or Separately?"

**PRIMARY PRINCIPLE:** Match granularity to assessment needs

For any potential consolidation, ask:
**"Would I assess the credibility/transparency/replicability of these statements TOGETHER or SEPARATELY?"**

- **Together** → CONSOLIDATE
- **Separately** → KEEP DISTINCT

**Test scenarios:**
- Multiple rationales for same design choice → Together (rationale synthesis)
- Scope boundaries (spatial + temporal + thematic) → Together (scope integration)
- Sequential workflow steps → Together if single method, separate if different methods
- GPS specs scattered across protocols → Together (tool specification)
- Different tools for different purposes → Separate (different assessment implications)

**For detailed consolidation patterns and anti-patterns:**  
→ See `references/checklists/consolidation-patterns.md`

---

### Granularity by Tier

**Consolidation intensity varies by tier:**

**Research Designs (High-level consolidation appropriate)**
- Consolidate multiple rationales for same decision
- Combine spatial/temporal/thematic scope statements
- Integrate related research questions
- Preserve distinct hypotheses (especially if different timing)

**Methods (Moderate consolidation)**
- Consolidate workflow sequences into unified methods
- Combine related validation procedures
- Keep different analytical approaches separate
- Preserve sampling strategies as distinct methods

**Protocols (Minimal consolidation)**
- Only consolidate truly redundant specifications
- Preserve measurement precision and parameters
- Keep distinct procedures separate
- Maintain replication-critical details

**Principle:** The more operational (Protocol), the more detail to preserve

---

## RDMAP-Specific Consolidation Patterns

### Pattern 1: Design Rationale Synthesis
**Consolidate:** Multiple justifications for same design decision  
**Example:** Three separate rationale statements → unified comprehensive rationale  
**Type:** `rationale_synthesis`

### Pattern 2: Scope Definition Consolidation
**Consolidate:** Separate spatial/temporal/thematic scope statements  
**Example:** Location + time period + artifact types → complete scope definition  
**Type:** `scope_integration`

### Pattern 3: Workflow Method Aggregation
**Consolidate:** Sequential procedures forming unified method  
**Example:** Survey + observation + documentation + GPS recording → integrated survey method  
**Type:** `workflow_integration`  
**Note:** Keep as separate methods if assessed independently

### Pattern 4: Validation Chain Consolidation
**Consolidate:** Multiple QC steps forming comprehensive validation  
**Example:** Inter-coder reliability + member checking + peer debriefing → multi-faceted QC  
**Type:** `validation_chain`

### Pattern 5: Protocol Specification Consolidation
**Consolidate:** Redundant tool descriptions across protocols  
**Example:** GPS device + model + accuracy + datum → complete GPS specification  
**Type:** `tool_specification`

### Pattern 6: Parameter Aggregation
**Consolidate:** Related parameter settings for same protocol  
**Example:** Transect spacing + width + walking speed → complete transect parameters  
**Type:** `parameter_integration`

**Critical:** All consolidations must preserve quantitative values and replication-critical details

---

## Verification Tasks

### 1. Tier Assignment Verification

**Check each RDMAP item against tier criteria:**

**Research Design indicators:**
- Explains WHY research framed this way
- Contains research questions, hypotheses, theoretical frameworks
- Provides study design rationale
- Defines scope and boundaries

**Method indicators:**
- Explains WHAT was done at high level
- Describes data collection approach, sampling strategy, analysis technique
- General approach without implementation details

**Protocol indicators:**
- Explains HOW specifically implemented
- Contains exact procedures, tool configurations, parameter values
- Sufficient detail for replication

**If misclassified:** Move to correct tier and update cross-references

**For detailed tier assignment guidance:**  
→ See `references/checklists/tier-assignment-guide.md`

---

### 2. Cross-Reference Validation

**Verify bidirectional consistency for all cross-references:**

**Design → Method:**
- `research_designs[].enables_methods` ↔ `methods[].design_context`
- Check: Every enabled method references back to design

**Method → Protocol:**
- `methods[].uses_protocols` ↔ `protocols[].implements_method`
- Check: Every used protocol references back to method

**Method → Evidence/Claims:**
- `methods[].supports_claims` ↔ `claims[].supported_by_evidence`
- Verify method descriptions not making claims (boundary accuracy)

**After consolidation:** Update all affected cross-references

---

### 3. Boundary Accuracy Review

**RDMAP vs Claims distinction:**

**RDMAP (methodological descriptions):**
- ✓ "Used stratified random sampling with 30% coverage"
- ✓ "GPS coordinates recorded at ±3cm accuracy"
- ✓ "Inter-coder reliability testing with Cohen's kappa"

**Claims (assertions about effectiveness):**
- ✗ "Stratified sampling proved more efficient"
- ✗ "High-accuracy GPS enabled better site mapping"
- ✗ "Inter-coder reliability was excellent"

**Test:** "Is this describing HOW research was done, or ARGUING about how well it worked?"
- Describing → RDMAP
- Arguing → Move to claims array

---

### 4. Reasoning Approach Consistency

**For Research Designs, verify reasoning approach classification:**

**Check claimed vs inferred consistency:**
- If `explicit_statement` present → should match `inferred_approach`
- If mismatch → document in `extraction_notes`, flag for review

**Verify hypothesis timing inference:**
- Pre-data: Stated in Introduction/Methods before Results
- Post-data: First mentioned in Results/Discussion, or marked as "emerged"
- Check timing basis and confidence level

**Mixed vs Unclear distinction:**
- Mixed requires evidence of BOTH exploratory AND confirmatory
- Don't default to "mixed" - use "unclear" if insufficient information

---

### 5. Expected Information Review

**Flag missing information in `expected_information_missing` arrays:**

**Common gaps to check:**
- Sample size justification
- Tool specifications and versions
- Parameter settings and values
- Quality control procedures
- Alternative methods considered
- Stopping rules for data collection

**Don't penalize absence - just document for transparency assessment**

**For comprehensive domain-specific checklists:**  
→ See `references/checklists/expected-information.md`

---

## Consolidation Metadata (REQUIRED)

**ALL consolidated items MUST have complete consolidation_metadata:**

```json
"consolidation_metadata": {
  "consolidated_from": ["P1_RD003", "P1_RD004"],
  "consolidation_type": "rationale_synthesis | scope_integration | workflow_integration | validation_chain | tool_specification | parameter_integration",
  "information_preserved": "complete | lossy_granularity | lossy_redundancy",
  "granularity_available": "Description of additional detail in source",
  "rationale": "Why consolidation appropriate"
}
```

**Information preservation values:**
- `complete`: No information lost
- `lossy_granularity`: Fine detail removed but aggregate preserved
- `lossy_redundancy`: Redundant statements merged

---

## Key Consolidation Examples

### Example 1: Good Consolidation (Preserves Detail)

**Pass 1 extracted:**
```json
{"method_id": "M025", "method_text": "Inter-coder reliability testing"},
{"method_id": "M026", "method_text": "Cohen's kappa calculated at 0.87"},
{"method_id": "M027", "method_text": "Member checking with team"}
```

**Pass 2 consolidated:**
```json
{
  "method_id": "M025",
  "method_text": "Multi-faceted quality control: inter-coder reliability testing (Cohen's kappa = 0.87) and member checking with survey team",
  "consolidation_metadata": {
    "consolidated_from": ["M025", "M026", "M027"],
    "consolidation_type": "validation_chain",
    "information_preserved": "complete",
    "rationale": "Related validation procedures combined into coherent QC approach"
  }
}
```

**Why good:** Preserves kappa value, maintains all validation methods, improves coherence

---

### Example 2: Bad Consolidation (Loses Critical Detail)

**Pass 1 extracted:**
```json
{"protocol_id": "P035", "protocol_text": "GPS coordinates at ±3cm accuracy"},
{"protocol_id": "P036", "protocol_text": "RTK correction for high precision"}
```

**Bad Pass 2:**
```json
{
  "protocol_id": "P035",
  "protocol_text": "GPS coordinates with high precision"  // Lost ±3cm and RTK!
}
```

**Correct Pass 2:**
```json
{
  "protocol_id": "P035",
  "protocol_text": "GPS coordinates at ±3cm accuracy using RTK correction",
  "consolidation_metadata": {
    "consolidated_from": ["P035", "P036"],
    "consolidation_type": "parameter_integration",
    "information_preserved": "complete"
  }
}
```

**Critical:** Never lose quantitative values or replication-critical specifications

---

### Example 3: Tier-Specific Granularity

**Design (high-level):**
```json
// Consolidate multiple rationales
"rationale": "Comparative design enables direct assessment of platform effectiveness, recording quality differences, and follows standard mobile technology evaluation practice"
```

**Method (moderate):**
```json
// Consolidate workflow but preserve approach distinctness
"data_collection_approach": {
  "approach": "survey",
  "domain_specific_type": "pedestrian archaeological survey with integrated documentation"
}
```

**Protocol (detailed):**
```json
// Minimal consolidation, preserve specifications
"tools": [{
  "tool_name": "Garmin GPSMAP 64s",
  "specifications": {"accuracy": "±3cm with RTK", "datum": "WGS84"}
}]
```

---

## Consolidation Workflow

### STEP 1: Tier Verification
- Check Design/Method/Protocol classifications
- Move misclassified items to correct tier
- Update cross-references after moves

### STEP 2: Consolidation
- Apply acid test to identify consolidation opportunities
- Use RDMAP-specific patterns where appropriate
- Document all consolidations with complete metadata
- Preserve quantitative values and critical parameters

### STEP 3: Cross-Reference Validation
- Verify bidirectional consistency
- Update references after consolidation
- Check design → method → protocol chains
- Validate method → claim boundaries

### STEP 4: Boundary and Consistency Checks
- Verify RDMAP vs claims boundary
- Check reasoning approach consistency
- Review hypothesis timing inference
- Flag expected information gaps

### STEP 5: Quality Verification
- No information loss (or documented as lossy)
- No remaining redundancy
- All consolidation_metadata complete
- Location fields preserved
- Other arrays (claims/evidence) untouched

---

## Output Format

**Return the same JSON document with RDMAP arrays rationalized:**

```json
{
  "schema_version": "2.4",
  "extraction_timestamp": "ISO 8601",
  "extractor": "Claude Sonnet 4.5",
  
  // Rationalize these arrays:
  "research_designs": [design_object],    
  "methods": [method_object],             
  "protocols": [protocol_object],         
  
  // Leave these untouched:
  "evidence": [...],                      
  "claims": [...],                        
  "implicit_arguments": [...],            
  
  "extraction_notes": {
    "pass": 2,
    "section_extracted": "string",
    "items_before_rationalization": 47,
    "items_after_rationalization": 38,
    "reduction_percentage": 19.1,
    "consolidations_performed": 9,
    "tier_corrections": 2,
    "boundary_corrections": 1
  }
}
```

**For complete object structure and field definitions:**  
→ See `references/schema/schema-guide.md`

---

## Pass 2 Goal

Produce rationalized RDMAP extraction with:
- Appropriate granularity by tier (Design high-level, Protocol detailed)
- Accurate tier assignments (WHY/WHAT/HOW verified)
- Complete consolidation traceability
- Verified bidirectional cross-references
- No information loss
- Ready for validation (Pass 3)