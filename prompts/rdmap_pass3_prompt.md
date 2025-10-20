# Validation Prompt - PASS 3: Integrity Checks v2.4

**Version:** 2.4 Pass 3  
**Last Updated:** 2025-10-20  
**Workflow Stage:** Pass 3 of 3 - Automated validation of Pass 2 extraction  
**Skill Context:** This prompt is part of the research-assessor skill

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

## Validation Checklist

Use this checklist as your roadmap. Execute all applicable checks:

**Cross-Reference Integrity:**
- [ ] All referenced IDs exist
- [ ] Bidirectional references consistent
- [ ] No orphaned objects (or appropriately flagged)

**Hierarchy Validation:**
- [ ] RDMAP chains valid (Design → Method → Protocol)
- [ ] Claims hierarchy valid (if claims present)
- [ ] Evidence chains valid (if evidence present)

**Schema Compliance:**
- [ ] Required fields present
- [ ] Enum values valid
- [ ] ID formats correct
- [ ] Location objects structured properly

**Expected Information:**
- [ ] Missing information aggregated by category
- [ ] Critical gaps flagged for assessment blockers
- [ ] TIDieR/CONSORT completeness noted (if applicable)

**Consolidation Metadata:**
- [ ] All Pass 2 consolidations have complete metadata
- [ ] consolidated_from IDs traceable

**Type Consistency:**
- [ ] Design types align with content
- [ ] Method types align with content

---

## Validation Philosophy

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

**Verify all referenced IDs exist in the extraction.**

**Check these reference fields:**

**Research Designs:**
- `enables_methods` → all M### IDs must exist
- `informs_claims` → all C### IDs must exist (if claims extracted)

**Methods:**
- `implements_designs` → all RD### IDs must exist
- `realized_through_protocols` → all P### IDs must exist
- `validated_by_evidence` → all E### IDs must exist (if evidence extracted)
- `justification_claim` → C### ID must exist (if claims extracted)

**Protocols:**
- `implements_methods` → all M### IDs must exist
- `produces_evidence` → all E### IDs must exist (if evidence extracted)

**Claims (if present):**
- `supported_by_evidence` → all E### or M### IDs must exist
- `supports_claims` → all C### IDs must exist (for hierarchical claims)

**Evidence (if present):**
- `supports_claims` → all C### IDs must exist

**Report format:**
```json
"missing_references": [
  {
    "source_id": "M008",
    "field": "validated_by_evidence",
    "missing_id": "E046",
    "severity": "important",
    "note": "Evidence array not present - deferred validation"
  }
]
```

**Deferred validation:** If referenced object type not present (e.g., RDMAP references claims but claims array empty), mark as "deferred validation" with severity "important" rather than "critical".

---

#### Check 1.2: Bidirectional Reference Consistency

**Verify cross-references are bidirectional.**

**Required bidirectional pairs:**
- `research_designs[].enables_methods` ↔ `methods[].implements_designs`
- `methods[].realized_through_protocols` ↔ `protocols[].implements_methods`
- `methods[].validated_by_evidence` ↔ `evidence[].supports_claims`
- `claims[].supported_by_evidence` ↔ `methods[].justification_claim` or `evidence[].supports_claims`
- `claims[].supports_claims` ↔ `claims[].supported_by_evidence` (hierarchical)

**Report format:**
```json
"bidirectional_inconsistencies": [
  {
    "issue": "M008 enables_methods includes M015, but M015 doesn't reference M008",
    "severity": "critical",
    "forward_ref": "M008.realized_through_protocols = [P015]",
    "missing_backward": "P015.implements_methods missing M008"
  }
]
```

---

#### Check 1.3: Orphaned Objects

**Identify objects with no incoming references.**

**Severity classification:**
- **Critical:** Orphaned protocols (must implement at least one method)
- **Critical:** Methods with no design context (should reference at least one design)
- **Minor:** Orphaned designs (may be high-level framing, acceptable)
- **Minor:** Orphaned claims (may be standalone observations, acceptable with note)

**Report format:**
```json
"orphaned_objects": [
  {
    "id": "P023",
    "type": "protocol",
    "severity": "critical",
    "issue": "No method references this protocol"
  }
]
```

---

### 2. Hierarchy Validation

#### Check 2.1: RDMAP Hierarchy Flow

**Verify Design → Method → Protocol chains are valid.**

**Check:**
- Every method in `enables_methods` must exist and link back
- Every protocol in `realized_through_protocols` must exist and link back
- Transitive chains valid (Design enables Method, Method uses Protocol)

**Report format:**
```json
"hierarchy_issues": [
  {
    "chain": "RD003 → M008 → P015",
    "issue": "P015 doesn't reference M008",
    "severity": "critical"
  }
]
```

---

#### Check 2.2: Claims Hierarchy (if claims extracted)

**Verify hierarchical claim relationships valid.**

**Check:**
- Claims in `supports_claims` exist
- No circular references (C001 → C002 → C001)
- Evidence chains resolve (all claims ultimately have evidence support)

---

#### Check 2.3: Evidence Chains (if evidence extracted)

**Verify evidence properly supports claims.**

**Check:**
- All evidence in `supported_by_evidence` exists
- All claims have at least one evidence or method reference
- Evidence doesn't support itself

---

### 3. Schema Compliance

#### Check 3.1: Required Fields Present

**Verify all required fields populated for each object type.**

**All objects require:**
- `*_id` (design_id, method_id, protocol_id, claim_id, evidence_id)
- `*_text` (design_text, method_text, etc.)
- `*_type` (design_type, method_type, etc.)
- `location` object with minimum {section, page}
- `extraction_confidence` (high, medium, low)

**For complete field requirements:**  
→ See `references/schema/schema-guide.md`

**Report format:**
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

**Critical enums (closed lists):**
- **Reasoning approaches:** inductive, abductive, deductive, mixed, unclear
- **Analysis populations:** all_collected, quality_filtered, outliers_excluded, complete_cases_only
- **Extraction confidence:** high, medium, low

**Open lists (flag uncommon but don't fail):**
- Study designs (survey, excavation, ethnographic, experimental, comparative, etc.)
- Sampling types (simple_random, stratified_random, purposive, convenience, etc.)

**Report format:**
```json
"invalid_enum_values": [
  {
    "id": "RD003",
    "field": "reasoning_approach.approach",
    "value": "exploratory",
    "severity": "critical",
    "suggestion": "Use 'inductive' for exploratory pattern-seeking"
  }
]
```

---

#### Check 3.3: ID Format Correctness

**Verify ID formats follow schema pattern.**

**Format rules:**
- Research Design: `RD###`
- Method: `M###`
- Protocol: `P###`
- Claims: `C###`
- Evidence: `E###`
- Implicit Arguments: `IA###`

**Report format:**
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

**Required:**
- `section` (string)
- `page` (number)

**Recommended:**
- `paragraph` (number)
- `sentence_start` (number)
- `sentence_end` (number)

---

### 4. Expected Information Completeness

#### Check 4.1: Aggregate Missing Information

**Aggregate all `expected_information_missing` arrays across objects.**

**Categorize by severity:**
- **Critical:** Assessment-blocking gaps (e.g., no sample size for quantitative claim, no tool specification for replication)
- **Important:** Transparency gaps (e.g., missing quality control procedures, no alternative methods considered)
- **Minor:** Recommended information (e.g., missing inter-observer reliability for qualitative data)

**Report format:**
```json
"expected_information_completeness": {
  "critical": [
    {"issue": "Sample size justification", "affects": ["M008", "M015"], "count": 2}
  ],
  "important": [
    {"issue": "Quality control procedures", "affects": ["M022"], "count": 1}
  ],
  "summary": {
    "total_gaps": 12,
    "critical": 2,
    "important": 5,
    "minor": 5
  }
}
```

---

#### Check 4.2: TIDieR/CONSORT Completeness (Optional)

**If methods reference TIDieR or CONSORT checklists, verify completeness.**

**TIDieR elements (10):** Rationale, Materials, Procedures, Personnel, Mode, Setting, Schedule, Tailoring, Modifications, Fidelity

**CONSORT-Outcomes elements (8):** Domain, Instrument, Metric, Aggregation, Time points, Reporter, Precision, Quality control

**Report as information, not failure.**

**For complete domain-specific checklists:**  
→ See `references/checklists/expected-information.md`

---

### 5. Consolidation Metadata Verification

#### Check 5.1: Consolidation Metadata Present and Complete

**For all objects with `consolidation_metadata`, verify:**
- `consolidated_from` array not empty
- `consolidation_type` specified
- `information_preserved` specified
- `rationale` provided

**Exception:** Single-item "consolidations" (consolidated_from has 1 item) are minor issues

**Report format:**
```json
"consolidation_issues": [
  {
    "id": "M025",
    "issue": "Missing consolidation_type",
    "severity": "important"
  }
]
```

---

### 6. Type Consistency Checks

#### Check 6.1: Design Type Alignment

**Verify design_type aligns with content.**

**If design_type = "research_question":**
- Should have `research_questions` array populated

**If design_type = "hypothesis":**
- Should have `hypotheses` array populated

**If design_type = "study_design":**
- Should have `study_design` object populated

---

#### Check 6.2: Method Type Alignment

**Verify method_type aligns with fields populated.**

**If method_type = "data_collection":**
- Should have `data_collection_approach` populated

**If method_type = "sampling":**
- Should have `sampling_strategy` populated

**If method_type = "analysis":**
- Should have `analytical_approach` populated

---

## Validation Report Format

**Produce validation report as JSON:**

```json
{
  "validation_version": "2.4",
  "validation_timestamp": "ISO 8601",
  "extraction_validated": {
    "schema_version": "2.4",
    "total_items": {
      "research_designs": 12,
      "methods": 35,
      "protocols": 28,
      "claims": 45,
      "evidence": 67
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
    "Review 2 orphaned protocols for tier reclassification"
  ]
}
```

---

## Severity Levels

**Critical (blocks assessment):**
- Broken cross-references (referenced IDs don't exist)
- Missing required fields
- Invalid ID formats
- Orphaned protocols or methods without design
- Bidirectional reference inconsistencies
- Invalid closed-list enum values

**Important (should fix but not blocking):**
- Incomplete bidirectional references
- Missing location details
- Incomplete consolidation metadata
- Critical expected information gaps
- Type/structure mismatches

**Minor (good to fix):**
- Orphaned designs (may be acceptable)
- Location objects missing recommended fields
- Minor expected information gaps

**Warnings (informational only):**
- Uncommon open-list enum values
- Very high/low expected information counts
- Unusual reasoning approach combinations

---

## Overall Status Determination

**PASS:** No critical or important issues  
**PASS_WITH_ISSUES:** Critical or important issues present but extraction usable  
**FAIL:** Critical issues make extraction unusable for assessment

**Note:** Deferred validation (references to not-yet-extracted arrays) should not cause FAIL status during partial extraction testing.

---

## Validation Goal

Produce comprehensive validation report identifying:
- All structural integrity issues
- Cross-reference problems
- Schema compliance violations
- Completeness gaps for transparency assessment
- Clear severity classifications
- Actionable recommendations for fixes

**Remember:** You are checking structure, not assessing methodology quality.