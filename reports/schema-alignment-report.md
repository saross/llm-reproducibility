# Schema Alignment Report: schema-guide.md vs extraction_schema.json

**Date:** 2025-10-19  
**Status:** ❌ DISCREPANCIES FOUND - Requires correction

---

## Executive Summary

The schema-guide.md in the research-assessor skill has **several field name mismatches** compared to the authoritative extraction_schema.json. These need to be corrected to ensure accurate extraction.

**Severity:** MEDIUM-HIGH  
- Extractors following the guide will use wrong field names
- JSON validation will fail
- Cross-references may break

**Action Required:** Update schema-guide.md to match extraction_schema.json

---

## Discrepancies Found

### 1. ❌ Implicit Argument ID Field Name

**Schema-guide.md says:**
```json
"implicit_argument_id": "IA001"
```

**extraction_schema.json actually uses:**
```json
"implicit_id": "IA001"
```

**Location in guide:** Line 121  
**Impact:** CRITICAL - ID field is required, wrong name breaks extraction  
**Fix:** Change all "implicit_argument_id" → "implicit_id"

---

### 2. ❌ Claim Required Fields - claim_role

**Schema-guide.md says:**
```markdown
**Required fields:**
- `claim_id`: String matching pattern `C###`
- `claim_text`: String stating the assertion
- `claim_type`: `empirical | interpretation | methodological_argument | theoretical`
- `claim_role`: `core | intermediate | supporting`  <-- WRONG
```

**extraction_schema.json actually requires:**
```json
"required": ["claim_id", "claim_text", "claim_type"]
```

**Location in guide:** Lines 80-84  
**Impact:** HIGH - Schema-guide incorrectly marks claim_role as required  
**Fix:** Move claim_role from "Required fields" to "Key fields" section

**Note:** claim_role DOES exist in the schema, it's just not required. It should be listed as an important optional field.

---

### 3. ❌ Claim Evidence Support Field Name

**Schema-guide.md says:**
```json
"supported_by_evidence": ["E001", "E003"]
```

**extraction_schema.json actually uses:**
```json
"supported_by": ["E001", "E003"]
```

**Location in guide:** Line 87, 101  
**Impact:** HIGH - Core cross-reference field, wrong name breaks relationships  
**Fix:** Change "supported_by_evidence" → "supported_by" throughout guide

---

### 4. ❌ Evidence Expected Information Field Name

**Schema-guide.md says:**
```markdown
**Key fields:**
- `expected_uncertainty_missing`: Uncertainty we would expect but is absent
```

**extraction_schema.json actually uses:**
```json
"expected_information_missing": {
  "type": "array",
  "items": {"type": "string"},
  "description": "Information we would expect to see but is absent"
}
```

**Location in guide:** Line 59  
**Impact:** HIGH - Used across all object types  
**Fix:** Change "expected_uncertainty_missing" → "expected_information_missing"

**Note:** The schema uses "expected_information_missing" consistently for ALL object types (evidence, claims, implicit arguments, research designs, methods, protocols).

---

### 5. ❌ Implicit Argument Claim Support Field Name

**Schema-guide.md says:**
```json
"supports_claims": ["C008"]
```

**extraction_schema.json actually uses:**
```json
"enables_claim": [
  "type": "array",
  "items": {"type": "string"},
  "description": "Claim IDs this implicit argument enables"
]
```

**Location in guide:** Line 124  
**Impact:** HIGH - Core cross-reference field  
**Fix:** Change "supports_claims" → "enables_claim"

---

### 6. ⚠️ Implicit Argument Types - Missing "disciplinary_assumption"

**Schema-guide.md lists:**
```markdown
**Types:**
- `logical_implication`: IF explicit claims true THEN X must be true
- `unstated_assumption`: Prerequisites assumed without acknowledgment
- `bridging_claim`: Missing links between evidence and conclusions
- `design_assumption`: Assumptions about research design choices
- `methodological_assumption`: Assumptions about method validity
```

**extraction_schema.json actually has:**
```json
"enum": [
  "logical_implication",
  "unstated_assumption",
  "bridging_claim",
  "design_assumption",
  "methodological_assumption",
  "disciplinary_assumption"  // <-- MISSING FROM GUIDE
]
```

**Location in guide:** Lines 111-116  
**Impact:** MEDIUM - Type exists but not documented  
**Fix:** Add "disciplinary_assumption" to the list

**Note:** The schema defines this as: "Type 3: Shared disciplinary knowledge or paradigmatic commitments"

---

### 7. ✅ Research Design Type Enum - Minor Difference

**Schema-guide.md says:**
```markdown
`design_type`: `research_question | theoretical_framework | study_design | scope_definition | positionality`
```

**extraction_schema.json actually uses:**
```json
"enum": [
  "research_framing",  // <-- Different
  "theoretical_framework",
  "study_design",
  "scope_definition",
  "positionality"
]
```

**Location in guide:** Line 136  
**Impact:** MEDIUM - First enum value is different  
**Fix:** Change "research_question" → "research_framing"

**Note:** The schema clarifies that "research_framing" includes research questions, hypotheses, and emergent findings.

---

## Summary of Required Changes

| **Section** | **Current (WRONG)** | **Correct** | **Priority** |
|-------------|---------------------|-------------|--------------|
| Implicit Argument ID | implicit_argument_id | implicit_id | CRITICAL |
| Claim evidence support | supported_by_evidence | supported_by | HIGH |
| Evidence expected info | expected_uncertainty_missing | expected_information_missing | HIGH |
| IA claim support | supports_claims | enables_claim | HIGH |
| Claim required fields | includes claim_role | only id, text, type | HIGH |
| IA types | missing disciplinary_assumption | add disciplinary_assumption | MEDIUM |
| Design type enum | research_question | research_framing | MEDIUM |

---

## Impact on Current Extractions

**If extractors follow the current schema-guide.md:**

1. ❌ JSON will have wrong field names
2. ❌ Validation against extraction_schema.json will fail
3. ❌ Cross-references may not work (wrong field names)
4. ❌ Required fields may be incorrect (claim_role marked as required when it's not)

**This needs to be fixed before production use.**

---

## Corrected Schema Guide Sections

### Evidence Object (Corrected)

**Required fields:**
- `evidence_id`: String matching pattern `E###` (E001, E002, ...)
- `evidence_text`: String describing the observation
- `evidence_type`: String (will evolve into controlled vocabulary)

**Key fields:**
- `declared_uncertainty`: Author-stated uncertainty (ranges, confidence intervals)
- `expected_information_missing`: Information we would expect but is absent  ← CORRECTED
- `supports_claims`: Array of claim IDs `["C001", "C005"]`
- `related_evidence`: Array for analytical views `["E002"]`
- `validates_methods`: Array of method IDs (NEW v2.4)
- `validates_protocols`: Array of protocol IDs (NEW v2.4)
- `location`: `{section, page, paragraph}`
- `consolidation_metadata`: Traceability for consolidated items

---

### Claim Object (Corrected)

**Required fields:**
- `claim_id`: String matching pattern `C###`
- `claim_text`: String stating the assertion
- `claim_type`: `empirical | interpretation | methodological_argument | theoretical`

**Key fields:**
- `claim_role`: `core | intermediate | supporting | synthesis` (IMPORTANT but not required)
- `supported_by`: Array of evidence IDs `["E001", "E003"]`  ← CORRECTED
- `supported_by_claims`: Array of supporting claim IDs
- `supports_claims`: Array of claims this supports
- `supports_method`: Method ID this justifies (NEW v2.4)
- `supports_protocol`: Protocol ID this justifies (NEW v2.4)
- `supports_design`: Design ID this justifies (NEW v2.4)
- `implicit_assumptions`: Array of implicit argument IDs `["IA001"]`
- `author_confidence`: `definite | probable | speculative | hedged`
- `expected_information_missing`: Gaps in justification

---

### Implicit Argument Object (Corrected)

**Required fields:**
- `implicit_id`: String matching pattern `IA###` (IA001, IA002, ...)  ← CORRECTED
- `implicit_text`: Statement of the implicit content
- `type`: Enum of implicit argument types

**Types:**
- `logical_implication`: IF explicit claims true THEN X must be true
- `unstated_assumption`: Prerequisites assumed without acknowledgment
- `bridging_claim`: Missing links between evidence and conclusions
- `design_assumption`: Assumptions about research design choices (NEW v2.4)
- `methodological_assumption`: Assumptions about method validity (NEW v2.4)
- `disciplinary_assumption`: Shared disciplinary knowledge or paradigmatic commitments  ← ADDED

**Key fields:**
- `enables_claim`: Array of claim IDs this argument enables  ← CORRECTED
- `connects_evidence`: Array of evidence IDs this argument connects
- `supports_design`: Design ID this assumes (NEW v2.4)
- `supports_method`: Method ID this assumes (NEW v2.4)
- `supports_protocol`: Protocol ID this assumes (NEW v2.4)

**Example (Corrected):**
```json
{
  "implicit_id": "IA001",
  "implicit_text": "GPS accuracy is sufficient for archaeological survey purposes",
  "type": "methodological_assumption",
  "enables_claim": ["C008"],
  "disciplinary_context": "archaeology"
}
```

---

### Research Design Object (Corrected)

**Required fields:**
- `design_id`: String matching pattern `RD###`
- `design_text`: Description of the design decision
- `design_type`: `research_framing | theoretical_framework | study_design | scope_definition | positionality`  ← CORRECTED

**Note:** "research_framing" replaces "research_question" and includes research questions, hypotheses, and emergent findings.

---

## Recommendations

### Immediate Actions:

1. **Update schema-guide.md** with all corrections above
2. **Test extraction** with corrected field names on sample paper
3. **Validate JSON** against extraction_schema.json to ensure compliance
4. **Update SKILL.md** if it references any incorrect field names
5. **Check all 5 prompts** for any references to incorrect field names

### Quality Assurance:

1. **Cross-reference checker script:** Create validation that checks field names match schema
2. **Schema sync process:** Establish workflow to keep guide synced with schema updates
3. **Version control:** Both files should have matching version numbers and update dates

---

## Next Steps

1. ✅ Review this report
2. ⏭️ Update schema-guide.md with corrections
3. ⏭️ Re-package skill with corrected guide
4. ⏭️ Test extraction with corrected field names
5. ⏭️ Proceed with prompt revisions for other 4 prompts

---

**Critical:** These field name mismatches will cause JSON validation failures and break cross-references. Must be corrected before production use.
