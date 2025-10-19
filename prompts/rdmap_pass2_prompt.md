# RDMAP Extraction Prompt - PASS 2: Rationalization v2.4

**Version:** 2.4 Pass 2  
**Last Updated:** 2025-10-19  
**Workflow Stage:** Pass 2 of 3 - Consolidate and refine Pass 1 RDMAP extraction

---

## Your Task

Review the Pass 1 RDMAP extraction and apply consolidation principles to produce a rationalized, high-quality extraction. Pass 1 intentionally over-extracted (~40-50% more items than needed). Your job is to consolidate, refine tier assignments, validate cross-references, and verify completeness.

**You have access to:**
1. Pass 1 extraction JSON (likely over-extracted and over-granular)
2. Original section text (for verification and fact-checking)

---

## RATIONALIZATION PHILOSOPHY FOR PASS 2

**Goals:**
- Reduce over-extraction to appropriate granularity (target 15-20% reduction)
- Correct tier assignment errors (Design vs Methods vs Protocols)
- Consolidate redundant or over-granular items without information loss
- Validate cross-reference chains
- Verify expected information completeness
- Finalize reasoning approach classifications
- Ensure consolidation traceability

**NOT expansion:** Pass 2 consolidates and refines. Do not add new items unless clearly missed in Pass 1.

**Expected outcome:**
- 15-20% reduction in total items (may vary by section)
- Clearer three-tier hierarchy
- Appropriate consolidation without information loss
- Valid cross-reference chains
- Complete consolidation_metadata for all consolidated items

---

## Core Consolidation Principles

### The Acid Test: "Would I Assess These Together or Separately?"

**PRIMARY PRINCIPLE:** RDMAP items should be at granularity appropriate for transparency/replicability assessment.

**Ask:** "Would someone assessing methodological transparency need to evaluate these items separately?"
- **Together** → CONSOLIDATE (lump)
- **Separately** → KEEP DISTINCT (split)

**Examples:**

**CONSOLIDATE:**
- Multiple validation steps → comprehensive quality control method
- Sequential protocol steps → unified procedure
- Related sampling decisions → integrated sampling strategy

**KEEP DISTINCT:**
- Different data collection approaches (even if related)
- Methods addressing different research questions
- Protocols using different tools or procedures

---

### Granularity by Tier

**Research Design Level - High-level consolidation:**
- Multiple rationale statements → integrated design rationale
- Related scope definitions → unified scope
- Connected theoretical concepts → coherent framework
- Separate research questions → consolidated if addressing same domain

**Method Level - Moderate consolidation:**
- Sequential workflow steps → unified method
- Related quality control procedures → comprehensive QC approach
- Connected sampling decisions → integrated sampling strategy
- Separate data collection approaches → keep distinct unless truly redundant

**Protocol Level - Preserve operational detail:**
- Consolidate only truly redundant specifications
- Maintain replication-critical detail
- Preserve tool specifications and parameter values
- Keep decision rules and quality checks distinct unless identical

---

## RDMAP-Specific Consolidation Patterns

### Pattern 1: Design Rationale Synthesis

**When to consolidate:** Multiple justifications for same design decision

**Example - Pass 1 extracted:**
- RD003: "Comparative design chosen to assess platform effectiveness"
- RD004: "Comparison enables direct evaluation of recording quality differences"
- RD005: "Comparative approach standard in mobile technology evaluation"

**Consolidate to:**
- RD003: "Comparative design chosen to enable direct assessment of platform effectiveness and recording quality differences, following standard practice in mobile technology evaluation"
- `consolidation_metadata`:
  - `source_items: ["RD003", "RD004", "RD005"]`
  - `consolidation_type: "rationale_synthesis"`
  - `information_preserved: "All three justifications integrated into unified rationale"`

---

### Pattern 2: Scope Definition Consolidation

**When to consolidate:** Separate spatial/temporal/thematic scope statements

**Example - Pass 1 extracted:**
- RD007: "Survey area: 45 hectares around Site X"
- RD008: "Temporal focus: Bronze Age (3000-1200 BCE)"
- RD009: "Thematic scope: Domestic and ritual artifact categories"

**Consolidate to:**
- RD007: "Study scope: 45-hectare area around Site X, Bronze Age period (3000-1200 BCE), domestic and ritual artifact categories"
- `consolidation_metadata`:
  - `source_items: ["RD007", "RD008", "RD009"]`
  - `consolidation_type: "scope_integration"`
  - `information_preserved: "All spatial, temporal, and thematic boundaries combined"`

---

### Pattern 3: Workflow Method Aggregation

**When to consolidate:** Sequential procedures that form unified method

**Example - Pass 1 extracted:**
- M015: "Pedestrian survey of transects"
- M016: "Artifact observation and documentation"
- M017: "GPS coordinate recording at artifact locations"
- M018: "Photograph capture for each artifact"

**Decision:** These are **sequential workflow** forming unified data collection method

**Consolidate to:**
- M015: "Pedestrian survey with integrated artifact documentation workflow: transect walking, artifact observation, GPS coordinate recording, and photographic documentation"
- `consolidation_metadata`:
  - `source_items: ["M015", "M016", "M017", "M018"]`
  - `consolidation_type: "workflow_integration"`
  - `information_preserved: "All workflow steps integrated; specific procedures retained in protocol-level objects"`

---

### Pattern 4: Validation Chain Consolidation

**When to consolidate:** Multiple validation steps forming comprehensive QC

**Example - Pass 1 extracted:**
- M022: "Inter-coder reliability testing (Cohen's kappa = 0.87)"
- M023: "Member checking with survey team"
- M024: "Peer debriefing sessions after each field week"

**Consolidate to:**
- M022: "Multi-faceted quality control: inter-coder reliability testing (Cohen's kappa = 0.87), member checking with survey team, and weekly peer debriefing"
- `consolidation_metadata`:
  - `source_items: ["M022", "M023", "M024"]`
  - `consolidation_type: "validation_chain"`
  - `information_preserved: "All QC procedures combined with quantitative metrics preserved"`

---

### Pattern 5: Protocol Specification Consolidation

**When to consolidate:** Redundant tool descriptions scattered across protocols

**Example - Pass 1 extracted:**
- P030: "GPS used for coordinate recording"
- P031: "Garmin GPSMAP 64s handheld GPS"
- P032: "GPS accuracy ±3cm with real-time kinematic correction"
- P033: "GPS configured for WGS84 datum"

**Consolidate to:**
- P030: "GPS coordinate recording: Garmin GPSMAP 64s handheld unit, WGS84 datum, ±3cm accuracy with RTK correction"
- `consolidation_metadata`:
  - `source_items: ["P030", "P031", "P032", "P033"]`
  - `consolidation_type: "tool_specification"`
  - `information_preserved: "All GPS specifications integrated into complete tool description"`

---

### Pattern 6: Parameter Aggregation

**When to consolidate:** Related parameter settings for same protocol

**Example - Pass 1 extracted:**
- P040: "Survey transects spaced 10m apart"
- P041: "Transect width 2m (1m either side of centerline)"
- P042: "Walking speed approximately 1m/s for adequate surface observation"

**Consolidate to:**
- P040: "Survey transect parameters: 10m spacing, 2m width (1m either side), ~1m/s walking speed for adequate observation"
- `consolidation_metadata`:
  - `source_items: ["P040", "P041", "P042"]`
  - `consolidation_type: "parameter_integration"`
  - `information_preserved: "All transect specifications combined into unified protocol"`

---

## Cross-Reference Validation

**Every cross-reference must be valid and bidirectional.**

### Design → Method References

**Check:** Every method in `enables_methods` array should have this design in `implements_designs`

**Example validation:**
- RD001: `enables_methods: ["M008", "M010"]`
- M008: Must have `implements_designs: ["RD001"]` ✓
- M010: Must have `implements_designs: ["RD001"]` ✓

**Fix if broken:** Add missing reference or remove invalid reference

---

### Method → Protocol References

**Check:** Every protocol in `realized_through_protocols` array should have this method in `implements_methods`

**Example validation:**
- M008: `realized_through_protocols: ["P023", "P024"]`
- P023: Must have `implements_methods: ["M008"]` ✓
- P024: Must have `implements_methods: ["M008"]` ✓

---

### Method → Evidence Validation

**Check:** If method claims `validated_by_evidence: ["E046"]`, verify E046 exists and validates this method

**Note:** Evidence objects may not be present if not yet extracted. Mark for future validation.

---

### Method → Claim Justification

**Check:** If method has `justification_claim: "C027"`, verify:
- C027 exists
- C027 has `claim_type: "methodological_argument"`
- C027 has `supports_method: "M###"` pointing back

---

### Orphaned Items

**Check for:** Items with no cross-references (orphans)

**Research Designs:** Should enable ≥1 method
- If orphan → verify it's truly strategic-level design
- If actually method-level → reclassify

**Methods:** Should implement ≥1 design AND be realized through ≥1 protocol
- If orphan → verify tier assignment
- May be high-level method without specific protocols (acceptable)

**Protocols:** Should implement ≥1 method
- If orphan → likely wrongly classified
- Consider moving to method level OR linking to appropriate method

---

## Tier Assignment Verification

**Review tier assignments using Why/What/How test.**

### Why → Research Design

**Indicators:**
- Explains rationale or framing
- Strategic decision
- Shapes overall approach
- Research questions, hypotheses, study design, scope, positionality

**Common misclassifications to fix:**
- Specific sampling strategy misclassified as design → move to methods
- Particular tool choice misclassified as design → move to protocol
- Methodological justification misclassified as design → move to claim

---

### What → Method

**Indicators:**
- General approach or strategy
- Tactical-level decisions
- Data collection approaches, sampling, analysis, QC
- Not yet specific about exact procedures

**Common misclassifications to fix:**
- Step-by-step procedures misclassified as method → move to protocol
- Strategic framing misclassified as method → move to design
- Tool specifications misclassified as method → move to protocol

---

### How → Protocol

**Indicators:**
- Specific procedures and steps
- Operational detail
- Tools, parameters, recording standards
- Enough detail for replication

**Common misclassifications to fix:**
- General approaches misclassified as protocol → move to method
- Tool justification misclassified as protocol → move to claim
- High-level strategy misclassified as protocol → move to method

---

## Boundary Accuracy Review

### RDMAP vs Claims Boundary

**RDMAP objects** = What was done (descriptions)
**Claim objects** = Why it was appropriate (arguments)

**Check for misclassified arguments:**

**Example - Should be Claim, not RDMAP:**
- "Stratified sampling was appropriate because it ensured representation"
  - → Extract as claim (methodological_argument)
  - → Link to method via `supports_method`

**Example - Correctly RDMAP:**
- "Stratified random sampling stratified by site zone"
  - → Correctly extracted as method
  - → Justification should be separate claim

**Fix:** Move argumentative statements to claims, keep descriptions in RDMAP

---

## Reasoning Approach Consistency

**Verify reasoning approach classifications are well-supported.**

### Check Claimed vs Inferred Consistency

**If explicit statement present:**
- Should match inferred approach
- If mismatch → note in `extraction_notes`, flag for assessment

**If no explicit statement:**
- Is inference well-supported by indicators?
- Is confidence level appropriate?
- If weak indicators → consider changing to `unclear`

---

### Verify Hypothesis Timing Inference

**Check structural evidence:**
- Hypothesis in intro/methods + presented before results → likely pre-data
- Hypothesis first appears in results/discussion → likely post-data
- Hypothesis phrasing suggests post-hoc ("We found that...") → likely post-data

**Confidence appropriate?**
- Clear structural placement → high confidence
- Ambiguous placement → medium confidence  
- Contradictory indicators → low confidence

---

### Mixed vs Unclear Distinction

**"Mixed" requires:**
- Explicit statement of multiple approaches, OR
- Clear evidence of different reasoning in different phases
- Should NOT be dumping ground for ambiguous cases

**If "mixed" without clear justification → change to "unclear"**

---

## Expected Information Completeness Review

**Aggregate `expected_information_missing` across all RDMAP objects.**

### Categorize Missing Information

**Critical gaps (assessment blockers):**
- Methods without basic description of approach
- Protocols missing core specifications
- Sampling without target population or rationale
- Major analysis approach not described

**Important gaps (reduced confidence):**
- Incomplete TIDieR elements for major methods
- Limited protocol detail for key procedures
- Missing quality control documentation
- Sampling size without justification

**Minor gaps (noted only):**
- Additional technical detail available but not essential
- Nice-to-have information that doesn't block assessment
- Specialized information for specific domains

**Aggregate in Pass 2 extraction_notes:**
```json
"extraction_notes": {
  "pass": 2,
  "expected_information_gaps": {
    "critical": ["M008 missing quality control procedures"],
    "important": ["P023 tool specifications incomplete", "M010 sample size not justified"],
    "minor": ["RD001 alternatives considered not detailed"]
  }
}
```

---

## Consolidation Metadata Requirements

**ALL consolidated items MUST have complete consolidation_metadata.**

Required fields:
```json
"consolidation_metadata": {
  "consolidated_from": ["RD003", "RD004", "RD005"],
  "consolidation_type": "rationale_synthesis",
  "information_preserved": "All three justifications integrated into unified rationale without loss",
  "rationale": "Multiple related rationale statements combined for coherent design justification"
}
```

**Consolidation types:**
- `rationale_synthesis` - Multiple justifications combined
- `scope_integration` - Spatial/temporal/thematic boundaries unified
- `workflow_integration` - Sequential steps forming unified method
- `validation_chain` - Multiple QC procedures combined
- `tool_specification` - Scattered tool details consolidated
- `parameter_integration` - Related parameters unified
- `redundancy_removal` - Duplicate information eliminated

---

## Quality Checks Before Finalizing

### No Over-Consolidation (Information Loss)

**Check:** Does consolidated item preserve all critical information from source items?

**Red flags:**
- Quantitative values lost (e.g., precision specifications)
- Procedural steps missing (e.g., decision rules)
- Rationale simplified away (e.g., justifications)
- Distinct tools conflated (e.g., different instruments treated as one)

**If information lost → split back out**

---

### No Under-Consolidation (Redundancy Remains)

**Check:** Are there still redundant items that should be consolidated?

**Look for:**
- Repeated tool specifications across protocols
- Duplicate rationale statements across designs
- Redundant workflow steps across methods
- Multiple items describing same procedure

**If redundancy remains → consolidate further**

---

### Cross-References Intact

**Check:** Did consolidation break cross-reference chains?

**When consolidating multiple items:**
- Aggregate all cross-references from source items
- Remove duplicates
- Verify bidirectional consistency

**Example:**
- M015, M016, M017 consolidated → M015
- M015 must have all cross-references from M016 and M017
- All items referencing M016 or M017 must be updated to reference M015

---

### Location Fields Preserved

**Check:** Are location fields maintained for consolidated items?

**Rule:** Use location of primary/most comprehensive source item

**Example:**
```json
"location": {
  "section": "Methods",
  "page": 5,
  "paragraph": 2,
  "note": "Consolidated from items spanning pages 5-6"
}
```

---

### Verbatim Quotes Meaningful

**Check:** Do verbatim quotes represent consolidated items well?

**Options:**
1. Use quote from most representative source item
2. Combine key phrases from multiple sources
3. Note consolidation in quote field

**Example:**
```json
"verbatim_quote": "Stratified random sampling [p.5] stratified by site zone [p.5] with 10m transect spacing [p.6]",
"location": {"note": "Quote consolidated from multiple statements"}
```

---

## Consolidation Examples

### Example 1: Good Consolidation (Preserves Information, Improves Structure)

**Pass 1 extracted:**
```json
{
  "method_id": "M025",
  "method_text": "Inter-coder reliability testing",
  "method_type": "quality_control"
},
{
  "method_id": "M026",
  "method_text": "Cohen's kappa calculated at 0.87",
  "method_type": "quality_control"
},
{
  "method_id": "M027",
  "method_text": "Member checking with team",
  "method_type": "validation"
}
```

**Pass 2 consolidated:**
```json
{
  "method_id": "M025",
  "method_text": "Multi-faceted quality control: inter-coder reliability testing (Cohen's kappa = 0.87) and member checking with survey team",
  "method_type": "quality_control",
  "quality_control": {
    "approach": "Triangulated validation through inter-coder reliability and member checking",
    "validation_methods": ["Inter-coder reliability testing", "Member checking"],
    "quantitative_metrics": ["Cohen's kappa = 0.87"]
  },
  "consolidation_metadata": {
    "consolidated_from": ["M025", "M026", "M027"],
    "consolidation_type": "validation_chain",
    "information_preserved": "All QC procedures and quantitative metrics maintained",
    "rationale": "Related validation procedures combined into coherent quality control approach"
  }
}
```

✓ **Good:** Preserves kappa value, maintains validation methods, improves coherence

---

### Example 2: Bad Consolidation (Loses Critical Detail)

**Pass 1 extracted:**
```json
{
  "protocol_id": "P035",
  "protocol_text": "GPS coordinates recorded at ±3cm accuracy",
  "parameters": {"accuracy": {"value": 3, "unit": "cm"}}
},
{
  "protocol_id": "P036", 
  "protocol_text": "RTK correction applied for high precision",
  "parameters": {"correction_method": {"value": "RTK"}}
}
```

**Bad Pass 2:**
```json
{
  "protocol_id": "P035",
  "protocol_text": "GPS coordinates recorded with high precision",
  "consolidation_metadata": {
    "consolidated_from": ["P035", "P036"]
  }
}
```

✗ **Bad:** Lost accuracy specification (±3cm) and correction method (RTK) - critical replication info

**Correct Pass 2:**
```json
{
  "protocol_id": "P035",
  "protocol_text": "GPS coordinates recorded at ±3cm accuracy using RTK correction",
  "parameters": {
    "accuracy": {"value": 3, "unit": "cm", "criticality": "high"},
    "correction_method": {"value": "RTK", "criticality": "high"}
  },
  "consolidation_metadata": {
    "consolidated_from": ["P035", "P036"],
    "consolidation_type": "parameter_integration",
    "information_preserved": "Both accuracy specification and correction method maintained"
  }
}
```

✓ **Good:** Preserves all critical parameters

---

### Example 3: Tier-Specific Consolidation Patterns

**Design-level (High-level consolidation):**
```json
// Multiple related rationales → unified rationale
"study_design": {
  "design_type": "comparative",
  "rationale": "Direct comparison enables assessment of platform effectiveness, recording quality differences, and follows standard mobile technology evaluation practice"
}
```

**Method-level (Moderate consolidation):**
```json
// Workflow steps → integrated method, but preserve distinctness of approaches
"data_collection_approach": {
  "approach": "survey",
  "domain_specific_type": "pedestrian archaeological survey with integrated documentation workflow"
}
```

**Protocol-level (Minimal consolidation, preserve detail):**
```json
// Only consolidate truly redundant specs, keep distinct procedures separate
"tools": [
  {
    "tool_name": "Garmin GPSMAP 64s",
    "specifications": {
      "accuracy": "±3cm with RTK",
      "datum": "WGS84",
      "satellite_minimum": 4,
      "hdop_threshold": 2.0
    }
  }
]
```

---

## Output Format

Provide rationalized extraction as JSON following schema v2.4:

```json
{
  "schema_version": "2.4",
  "extraction_timestamp": "ISO 8601",
  "extractor": "Claude Sonnet 4.5",
  
  "research_designs": [research_design_object],
  "methods": [method_object],
  "protocols": [protocol_object],
  
  "extraction_notes": {
    "pass": 2,
    "section_extracted": "string",
    "items_before_rationalization": 85,
    "items_after_rationalization": 69,
    "reduction_percentage": 18.8,
    "consolidations_performed": 16,
    "tier_reclassifications": 3,
    "cross_reference_fixes": 5,
    "expected_information_gaps": {
      "critical": ["string"],
      "important": ["string"],
      "minor": ["string"]
    },
    "items_flagged_for_review": ["string"]
  }
}
```

---

## Quality Checklist for Pass 2

Before finalizing rationalization:

- [ ] 15-20% reduction achieved (acceptable range 10-25%)
- [ ] All consolidations have complete consolidation_metadata
- [ ] No information loss from consolidations (verify with checklist)
- [ ] No remaining redundancy (check for duplicates)
- [ ] All tier assignments verified with Why/What/How test
- [ ] Cross-reference chains validated bidirectionally
- [ ] Orphaned items reviewed and addressed
- [ ] RDMAP vs claims boundary checked
- [ ] Reasoning approach classifications consistent
- [ ] Hypothesis timing inferences well-supported
- [ ] Expected information gaps categorized (critical/important/minor)
- [ ] Location fields preserved for all items
- [ ] Verbatim quotes represent consolidated items accurately

---

## Remember

**Pass 2 is about CONSOLIDATION AND REFINEMENT, not expansion.**

- Reduce granularity appropriately
- Preserve all critical information
- Validate cross-references
- Finalize tier assignments
- Document all consolidations
- Prepare for Pass 3 validation

**Your goal:** Produce a rationalized, high-quality extraction ready for validation and assessment.