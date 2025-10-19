# RDMAP Validation Prompt - PASS 3: Integrity Checks v2.4

**Version:** 2.4 Pass 3  
**Last Updated:** 2025-10-19  
**Workflow Stage:** Pass 3 of 3 - Automated validation of Pass 2 RDMAP extraction

---

## Your Task

Perform automated integrity checks on the rationalized extraction. Identify structural issues, broken references, schema violations, and completeness gaps. **Do NOT modify the extraction** - produce a validation report only.

**This is NOT quality assessment** - you are checking structural integrity, not methodological quality.

**Input:** JSON extraction document from Pass 2
- May contain only RDMAP arrays (RDMAP-only validation)
- May contain both RDMAP and claims/evidence arrays (unified validation)
- Validation adapts to what's present

**Your responsibility:** Validate whatever object types are present:
- If RDMAP arrays present → validate RDMAP thoroughly
- If claims/evidence arrays present → validate those too
- Cross-references between object types validated when both present
- Note when referenced arrays not yet extracted (deferred validation)

**Output:** Validation report in JSON format with issues categorized by severity

---

## VALIDATION PHILOSOPHY

**Purpose:** Ensure extraction is structurally sound, internally consistent, and schema-compliant.

**Flexible validation:**
- Validates whatever object types are present in the extraction
- RDMAP-only: Validates research_designs, methods, protocols thoroughly
- Unified: Validates RDMAP + claims + evidence + implicit arguments
- Notes when cross-references point to not-yet-extracted arrays (deferred validation)

**Scope:**
- Cross-reference integrity (all IDs exist, bidirectional consistency)
- Hierarchy validation (Design → Methods → Protocols chains; Claims hierarchy)
- Schema compliance (required fields, valid enums, ID formats)
- Expected information completeness (aggregated gaps)
- Consolidation metadata consistency

**NOT in scope:**
- Quality of methodology (that's assessment phase)
- Completeness of extraction (Pass 1/2 handled that)
- Scientific validity of claims (that's assessment phase)

---

## Validation Checks

### 1. Cross-Reference Integrity

#### Check 1.1: Referenced IDs Exist

**For each RDMAP object, verify all referenced IDs exist in the extraction.**

**Check these arrays:**

**Research Designs:**
- `enables_methods` → all M### IDs must exist
- `informs_claims` → all C### IDs must exist (if claims extracted)
- `implicit_assumptions` → all IA### IDs must exist (if implicit args extracted)

**Methods:**
- `implements_designs` → all RD### IDs must exist
- `realized_through_protocols` → all P### IDs must exist
- `validated_by_evidence` → all E### IDs must exist (if evidence extracted)
- `justification_claim` → C### ID must exist (if claims extracted)
- `implicit_assumptions` → all IA### IDs must exist (if implicit args extracted)

**Protocols:**
- `implements_methods` → all M### IDs must exist
- `produces_evidence` → all E### IDs must exist (if evidence extracted)
- `adapted_from` → P### ID must exist

**Report:**
```json
"missing_references": [
  {
    "source_id": "M008",
    "field": "validated_by_evidence",
    "missing_id": "E046",
    "severity": "important",
    "note": "Evidence array not present in extraction - deferred validation until claims/evidence extracted"
  }
]
```

**Note:** If referenced object type not present in extraction (e.g., RDMAP references claims but claims array empty), mark as "deferred validation" with severity "important" rather than "critical". This allows RDMAP-only validation during testing.

---

#### Check 1.2: Bidirectional Reference Consistency

**Verify cross-references are bidirectional.**

**Design ↔ Method:**
- If RD001 has `enables_methods: ["M008"]`
- Then M008 must have `implements_designs: ["RD001"]`

**Method ↔ Protocol:**
- If M008 has `realized_through_protocols: ["P023", "P024"]`
- Then P023 and P024 must have `implements_methods: ["M008"]`

**Method ↔ Evidence:**
- If M008 has `validated_by_evidence: ["E046"]`
- Then E046 should have `validates_methods: ["M008"]` (if evidence extracted)

**Method ↔ Claim:**
- If M008 has `justification_claim: "C027"`
- Then C027 should have `supports_method: "M008"` (if claims extracted)

**Report:**
```json
"bidirectional_inconsistencies": [
  {
    "type": "design_method",
    "forward": {"id": "RD001", "field": "enables_methods", "references": ["M008", "M010"]},
    "backward": {"id": "M008", "field": "implements_designs", "references": ["RD001"], "status": "✓"},
    "backward": {"id": "M010", "field": "implements_designs", "references": [], "status": "✗ MISSING"},
    "severity": "critical"
  }
]
```

---

#### Check 1.3: Orphaned Objects

**Find objects with no cross-references.**

**Research Designs:**
- Should have `enables_methods` with ≥1 item
- If orphan → flag for review (may be high-level framing with no specific methods)

**Methods:**
- Should have `implements_designs` with ≥1 item
- Should have `realized_through_protocols` with ≥1 item OR be high-level method
- If no design reference → critical issue

**Protocols:**
- Should have `implements_methods` with ≥1 item
- If orphan → likely tier misclassification

**Report:**
```json
"orphaned_objects": [
  {
    "id": "P045",
    "type": "protocol",
    "issue": "No method references",
    "severity": "critical",
    "suggestion": "Likely misclassified - consider moving to method tier"
  }
]
```

---

### 2. Hierarchy Validation

#### Check 2.1: RDMAP Hierarchy Flow

**Verify Design → Methods → Protocols chains are logical.**

**For each method:**
- Must implement ≥1 design (unless high-level organizing method)
- Should be realized through ≥1 protocol (unless high-level method)

**For each protocol:**
- Must implement ≥1 method
- Should not skip tiers (protocol implementing design directly is suspicious)

**Report:**
```json
"hierarchy_issues": [
  {
    "type": "method_without_design",
    "id": "M012",
    "issue": "Method implements no research design",
    "severity": "critical",
    "suggestion": "Link to appropriate design or reclassify"
  },
  {
    "type": "tier_skipping",
    "id": "P030",
    "issue": "Protocol references design RD001 directly without method intermediary",
    "severity": "important",
    "suggestion": "Should implement method, which implements design"
  }
]
```

---

#### Check 2.2: Claims Hierarchy (if claims extracted)

**Verify methodological argument claims are properly linked.**

**For each claim with `claim_type: "methodological_argument"`:**
- Should have `supports_method` or `supports_design` or `supports_protocol`
- Supported RDMAP object should reference this claim

**Report:**
```json
"claim_link_issues": [
  {
    "claim_id": "C027",
    "claim_type": "methodological_argument",
    "supports_method": "M008",
    "issue": "M008 does not reference C027 in justification_claim field",
    "severity": "important"
  }
]
```

---

#### Check 2.3: Evidence Chains (if evidence extracted)

**Verify evidence properly links to methods/protocols.**

**For evidence validating methods:**
- Method should reference evidence
- Evidence should reference method

**For evidence produced by protocols:**
- Protocol should reference evidence
- Evidence should note protocol source

**Report:**
```json
"evidence_chain_issues": [
  {
    "evidence_id": "E046",
    "validates_methods": ["M008"],
    "issue": "M008 does not list E046 in validated_by_evidence",
    "severity": "important"
  }
]
```

---

### 3. Schema Compliance

#### Check 3.1: Required Fields Present

**Verify all required fields populated for each object type.**

**All RDMAP objects require:**
- `*_id` (design_id, method_id, protocol_id)
- `*_text`
- `*_type` (design_type, method_type, protocol_type)
- `location` object with at minimum {section, page}
- `extraction_confidence`

**Report:**
```json
"missing_required_fields": [
  {
    "id": "M015",
    "missing_fields": ["extraction_confidence"],
    "severity": "critical"
  }
]
```

---

#### Check 3.2: Enum Values Valid

**Check enum fields against schema v2.4 allowed values.**

**Reasoning approaches:**
- Valid: inductive, abductive, deductive, mixed, unclear
- Invalid: anything else

**Study designs (open list):**
- Common: survey, excavation, ethnographic, experimental, comparative, longitudinal, case_study, mixed_methods
- Accept free text but flag uncommon values for review

**Sampling types (open list):**
- Common probability: simple_random, stratified_random, systematic_random, cluster
- Common non-probability: purposive, convenience, theoretical, snowball, judgmental
- Accept free text but flag uncommon values

**Analysis populations:**
- Valid: all_collected, quality_filtered, outliers_excluded, complete_cases_only
- Invalid: anything else

**Report:**
```json
"invalid_enum_values": [
  {
    "id": "RD003",
    "field": "reasoning_approach.approach",
    "value": "exploratory",
    "severity": "critical",
    "valid_values": ["inductive", "abductive", "deductive", "mixed", "unclear"],
    "suggestion": "Use 'inductive' for exploratory pattern-seeking"
  }
]
```

---

#### Check 3.3: ID Format Correctness

**Verify ID formats follow schema pattern.**

**Format rules:**
- Research Design: `RD###` (RD001, RD002, etc.)
- Method: `M###` (M001, M002, etc.)
- Protocol: `P###` (P001, P002, etc.)
- Claims: `C###` (C001, C002, etc.)
- Evidence: `E###` (E001, E002, etc.)
- Implicit Arguments: `IA###` (IA001, IA002, etc.)

**Report:**
```json
"id_format_errors": [
  {
    "id": "Method-008",
    "severity": "critical",
    "issue": "Incorrect format - should be M008"
  }
]
```

---

#### Check 3.4: Location Object Structure

**Verify location objects have required fields.**

**Minimum required:**
- `section` (string)
- `page` (number)

**Recommended:**
- `paragraph` (number)
- `sentence_start` (number)
- `sentence_end` (number)

**Report:**
```json
"location_issues": [
  {
    "id": "P023",
    "issue": "Location missing required 'page' field",
    "severity": "important"
  }
]
```

---

### 4. Expected Information Completeness

#### Check 4.1: Aggregate Missing Information

**Compile all `expected_information_missing` across RDMAP objects.**

**Categorize by severity:**

**Critical gaps (assessment blockers):**
- Methods without basic approach description
- Protocols missing core specifications
- Sampling without target population or rationale
- Major tools without specifications
- Quality control absent for major methods

**Important gaps (reduced confidence):**
- Incomplete TIDieR elements (missing >3 of 10)
- Incomplete CONSORT-Outcomes elements (missing >2 of 8)
- Sample size without justification
- Missing modification/adaptation documentation

**Minor gaps (noted only):**
- Additional technical detail
- Non-essential specifications
- Nice-to-have documentation

**Report:**
```json
"expected_information_gaps": {
  "critical": [
    {"id": "M008", "missing": "Quality control procedures entirely absent"},
    {"id": "P023", "missing": "Tool specifications incomplete - no version or configuration"}
  ],
  "important": [
    {"id": "M010", "missing": "Sample size justification"},
    {"id": "M015", "missing": "Personnel training and expertise (TIDieR Who element)"}
  ],
  "minor": [
    {"id": "RD001", "missing": "Alternatives considered not detailed"}
  ],
  "summary": {
    "methods_with_critical_gaps": 2,
    "methods_with_important_gaps": 5,
    "protocols_with_critical_gaps": 1,
    "incomplete_TIDieR_checklists": 3
  }
}
```

---

#### Check 4.2: TIDieR Checklist Completeness

**For each method with TIDieR-applicable approach, check completeness.**

**10 TIDieR elements:**
1. Rationale (Why)
2. Materials (What - physical)
3. Procedures (What - actions)
4. Personnel (Who)
5. Mode (How)
6. Setting (Where)
7. Schedule (When/How Much)
8. Tailoring (Planned adaptations)
9. Modifications (Actual changes)
10. Fidelity (Quality assurance)

**Report methods with <7 of 10 elements.**

---

#### Check 4.3: CONSORT-Outcomes Completeness

**For each protocol with measurement/observation, check completeness.**

**8 CONSORT-Outcomes elements:**
1. Domain (what measured)
2. Instrument (tool/method)
3. Metric (units/scale)
4. Aggregation (how combined)
5. Time points (when measured)
6. Reporter/Observer (who)
7. Precision (error/accuracy)
8. Quality control (validation)

**Report protocols with <6 of 8 elements.**

---

### 5. Consolidation Metadata Verification

#### Check 5.1: Consolidation Metadata Consistency

**For all items with `consolidation_metadata`, verify:**

**Required fields present:**
- `consolidated_from` (array of source IDs)
- `consolidation_type` (valid type)
- `information_preserved` (description)

**Source items documented:**
- All IDs in `consolidated_from` are valid format
- Number of source items >1 (consolidation should combine ≥2 items)

**Report:**
```json
"consolidation_issues": [
  {
    "id": "M015",
    "issue": "Has consolidation_metadata but consolidated_from has only 1 item",
    "severity": "minor",
    "suggestion": "Remove consolidation_metadata if not actually consolidated"
  },
  {
    "id": "P030",
    "issue": "consolidation_type 'merged' not recognized",
    "severity": "important",
    "valid_types": ["rationale_synthesis", "scope_integration", "workflow_integration", "validation_chain", "tool_specification", "parameter_integration", "redundancy_removal"]
  }
]
```

---

### 6. Type Consistency Checks

#### Check 6.1: Design Type Alignment

**Verify design_type and populated type-specific structures align.**

**Examples:**
- If `design_type: "research_question"` → should have `research_questions` array
- If `design_type: "study_design"` → should have `study_design` object
- If `design_type: "theoretical_framework"` → should have `theoretical_framework` object

**Report type/structure mismatches.**

---

#### Check 6.2: Method Type Alignment

**Verify method_type and populated type-specific structures align.**

**Examples:**
- If `method_type: "data_collection"` → should have `data_collection_approach`
- If `method_type: "sampling"` → should have `sampling_strategy`
- If `method_type: "analysis"` → should have `analytical_approach`
- If `method_type: "quality_control"` → should have `quality_control`

**Report type/structure mismatches.**

---

## Validation Report Format

**Produce validation report as JSON:**

```json
{
  "validation_version": "2.4",
  "validation_timestamp": "ISO 8601",
  "extraction_validated": {
    "schema_version": "2.4",
    "extraction_timestamp": "ISO 8601",
    "total_items": {
      "research_designs": 12,
      "methods": 35,
      "protocols": 28
    }
  },
  
  "validation_summary": {
    "critical_issues": 3,
    "important_issues": 8,
    "minor_issues": 15,
    "warnings": 5,
    "overall_status": "PASS_WITH_ISSUES"
  },
  
  "cross_reference_integrity": {
    "missing_references": [...],
    "bidirectional_inconsistencies": [...],
    "orphaned_objects": [...]
  },
  
  "hierarchy_validation": {
    "hierarchy_issues": [...],
    "claim_link_issues": [...],
    "evidence_chain_issues": [...]
  },
  
  "schema_compliance": {
    "missing_required_fields": [...],
    "invalid_enum_values": [...],
    "id_format_errors": [...],
    "location_issues": [...]
  },
  
  "expected_information_completeness": {
    "critical": [...],
    "important": [...],
    "minor": [...],
    "summary": {...}
  },
  
  "consolidation_verification": {
    "consolidation_issues": [...]
  },
  
  "type_consistency": {
    "design_type_mismatches": [...],
    "method_type_mismatches": [...]
  },
  
  "recommendations": [
    "Fix 3 critical cross-reference issues before assessment",
    "Review 2 orphaned protocols for tier reclassification",
    "Address missing quality control documentation for M008 and M015"
  ]
}
```

---

## Severity Levels

**Critical:**
- Broken cross-references (referenced IDs don't exist)
- Missing required fields
- Invalid ID formats
- Orphaned protocols (no method link)
- Methods without design link
- Bidirectional reference inconsistencies

**Important:**
- Incomplete bidirectional references (forward exists, backward missing)
- Invalid enum values
- Missing location details
- Incomplete consolidation metadata
- Critical expected information gaps (assessment blockers)
- Type/structure mismatches

**Minor:**
- Orphaned designs (high-level framing may be acceptable)
- Location objects missing recommended fields
- Minor expected information gaps
- Consolidation metadata for single-item "consolidations"

**Warnings (not issues, just flagging):**
- Uncommon study design or sampling type values (open list)
- Very high or very low expected information missing counts
- Unusual reasoning approach combinations

---

## Overall Status Determination

**PASS:** No critical issues, <5 important issues, extraction ready for assessment

**PASS_WITH_ISSUES:** No critical issues, 5-15 important issues, extraction usable but should address issues

**FAIL:** ≥1 critical issue, extraction needs fixes before assessment

---

## Usage

**Input:** Rationalized extraction JSON (from Pass 2)
- May be RDMAP-only (for testing RDMAP extraction independently)
- May be unified (RDMAP + claims/evidence for full paper validation)

**Process:**
1. Detect which object types are present
2. Run all validation checks systematically for present types
3. Mark cross-references to absent types as "deferred validation"
4. Categorize issues by severity
5. Aggregate expected information gaps
6. Generate recommendations
7. Determine overall status

**Output:** Validation report JSON (do not modify extraction)

**Next step:** 
- If PASS or PASS_WITH_ISSUES → proceed to assessment (or next extraction phase)
- If FAIL → return to Pass 2 for fixes

---

## Remember

**Pass 3 validates STRUCTURE, not QUALITY.**

- Check integrity, not methodology
- Report issues, don't fix them
- Categorize severity appropriately
- Enable human review of flagged items

**Your goal:** Ensure extraction is structurally sound and ready for methodological assessment.