# RDMAP Extraction Workflow

**Version:** 2.4  
**Last Updated:** 2025-10-19  
**Status:** Ready for testing

---

## Overview

This workflow extracts **Research Design, Methods, and Protocols (RDMAP)** plus **Claims and Evidence** from research papers using a systematic multi-pass approach. All extraction passes operate on a **single shared JSON document** that accumulates content as it flows through the pipeline.

---

## Quick Start

### 1. Start with Template

Create or use the blank extraction template:

```json
{
  "schema_version": "2.4",
  "extraction_timestamp": "ISO 8601",
  "extractor": "string",
  "evidence": [],
  "claims": [],
  "implicit_arguments": [],
  "research_designs": [],
  "methods": [],
  "protocols": [],
  "extraction_notes": {}
}
```

### 2. Run Extraction Passes

**Option A: Claims/Evidence First**
```
Template → Claims Pass 1 → Claims Pass 2 → RDMAP Pass 1 → RDMAP Pass 2 → Pass 3
```

**Option B: RDMAP First**
```
Template → RDMAP Pass 1 → RDMAP Pass 2 → Claims Pass 1 → Claims Pass 2 → Pass 3
```

Both produce the same final result. Choose based on your workflow preferences.

### 3. Validate

Run Pass 3 validation to check structural integrity before assessment.

---

## Detailed Workflow

### Phase 1: Claims & Evidence Extraction

**Pass 1: Liberal Extraction** (`claims_pass1_v2_4.md`)
- **Input:** JSON document (blank or with RDMAP already extracted)
- **Action:** Extract evidence, claims, and implicit arguments
- **Strategy:** Over-capture (40-50% more items expected)
- **Populates:** `evidence`, `claims`, `implicit_arguments` arrays
- **Leaves alone:** `research_designs`, `methods`, `protocols` arrays
- **Output:** Same JSON with claims/evidence populated

**Pass 2: Rationalization** (`claims_pass2_v2_4.md`)
- **Input:** JSON from Pass 1
- **Action:** Consolidate, refine boundaries, verify relationships
- **Target:** 15-20% reduction in items
- **Refines:** `evidence`, `claims`, `implicit_arguments` arrays
- **Leaves alone:** RDMAP arrays
- **Output:** Same JSON with claims/evidence rationalized

---

### Phase 2: RDMAP Extraction

**Pass 1: Liberal Extraction** (`rdmap_pass1_v2_4.md`)
- **Input:** JSON document (blank or with claims/evidence already extracted)
- **Action:** Extract research designs, methods, and protocols
- **Strategy:** Over-capture with three-tier hierarchy
- **Populates:** `research_designs`, `methods`, `protocols` arrays
- **Leaves alone:** `evidence`, `claims`, `implicit_arguments` arrays
- **Output:** Same JSON with RDMAP populated

**Pass 2: Rationalization** (`rdmap_pass2_v2_4.md`)
- **Input:** JSON from Pass 1
- **Action:** Consolidate, verify tier assignments, validate cross-references
- **Target:** 15-20% reduction in items
- **Refines:** `research_designs`, `methods`, `protocols` arrays
- **Leaves alone:** Claims/evidence arrays
- **Output:** Same JSON with RDMAP rationalized

---

### Phase 3: Validation

**Pass 3: Integrity Checks** (`rdmap_pass3_v2_4.md`)
- **Input:** Complete extraction from Phase 1 and 2
- **Action:** Automated structural validation
- **Validates:** All object types present in document
- **Checks:**
  - Cross-reference integrity (bidirectional consistency)
  - Hierarchy validation (Design → Methods → Protocols; Claim chains)
  - Schema compliance (required fields, valid enums, ID formats)
  - Expected information completeness
  - Consolidation metadata
- **Output:** Validation report (JSON) - **does not modify extraction**
- **Flexibility:** Works with partial extractions (RDMAP-only or claims-only) for testing

---

## File Descriptions

### Extraction Prompts

| File | Purpose | Modifies |
|------|---------|----------|
| `claims_pass1_v2_4.md` | Liberal claims/evidence extraction | `evidence`, `claims`, `implicit_arguments` |
| `claims_pass2_v2_4.md` | Claims/evidence rationalization | `evidence`, `claims`, `implicit_arguments` |
| `rdmap_pass1_v2_4.md` | Liberal RDMAP extraction | `research_designs`, `methods`, `protocols` |
| `rdmap_pass2_v2_4.md` | RDMAP rationalization | `research_designs`, `methods`, `protocols` |
| `rdmap_pass3_v2_4.md` | Validation (all object types) | Nothing (produces separate report) |

### Schema

| File | Purpose |
|------|---------|
| `schema_v2_4.json` | Complete JSON schema defining all object types |

---

## Key Principles

### Iterative Accumulation
- **Single document** flows through all passes
- Each pass populates or refines specific arrays
- Other arrays remain untouched
- No merging step needed

### Separation of Concerns
- **Claims/Evidence prompts:** Don't touch RDMAP arrays
- **RDMAP prompts:** Don't touch claims/evidence arrays
- **Validation prompt:** Reads all, modifies none

### Extraction Philosophy
- **Pass 1:** Liberal extraction with over-capture (comprehensive)
- **Pass 2:** Rationalization with consolidation (refined)
- **Pass 3:** Validation without modification (structural integrity)

### Cross-Reference Architecture
- Simple string ID arrays (e.g., `["M003", "M007"]`)
- Bidirectional consistency enforced
- Works across object types (methods reference claims, protocols reference evidence)

---

## Testing vs Production

### For Testing
**Start with blank template:**
- Test any extraction independently
- Test with pre-populated arrays to simulate realistic conditions
- Validate partial extractions (RDMAP-only during development)

### For Production
**Follow full pipeline:**
1. Start with blank template
2. Run all passes in sequence
3. Validate complete extraction
4. Proceed to assessment phase

---

## Expected Outputs

### After Claims/Evidence Extraction
```json
{
  "evidence": [40-60 items],           // Populated
  "claims": [30-50 items],             // Populated
  "implicit_arguments": [5-15 items],  // Populated
  "research_designs": [],              // Empty (not yet extracted)
  "methods": [],                       // Empty
  "protocols": []                      // Empty
}
```

### After RDMAP Extraction
```json
{
  "evidence": [40-60 items],           // From earlier pass
  "claims": [30-50 items],             // From earlier pass
  "implicit_arguments": [5-15 items],  // From earlier pass
  "research_designs": [10-15 items],   // Newly populated
  "methods": [20-30 items],            // Newly populated
  "protocols": [15-25 items]           // Newly populated
}
```

### After Validation
Separate validation report:
```json
{
  "validation_summary": {
    "overall_status": "PASS | PASS_WITH_ISSUES | FAIL",
    "critical_issues": 0,
    "important_issues": 5,
    "minor_issues": 12
  },
  "recommendations": [...]
}
```

---

## Common Scenarios

### Scenario 1: Extract Methods Section Only

```
1. Blank template → RDMAP Pass 1 (Methods) → RDMAP Pass 2 → Pass 3 (RDMAP-only validation)
```

Claims/evidence arrays remain empty. Validation notes deferred validation for cross-references.

### Scenario 2: Full Paper Extraction

```
1. Blank template
2. Claims Pass 1 (Results + Discussion) → Claims Pass 2
3. RDMAP Pass 1 (Methods) → RDMAP Pass 2
4. Pass 3 (unified validation)
```

All arrays populated, complete validation.

### Scenario 3: Iterative Section Extraction

```
1. Blank template → Claims Pass 1 (Results) → Claims Pass 2
2. Same JSON → Claims Pass 1 (Discussion) → Claims Pass 2
3. Same JSON → RDMAP Pass 1 (Methods) → RDMAP Pass 2
4. Pass 3 (unified validation)
```

Document accumulates content from multiple sections.

---

## Troubleshooting

### Issue: Pass modified wrong arrays
**Check:** Did you use the correct prompt version (v2.4)?  
**Fix:** v2.4 prompts have explicit array boundaries documented

### Issue: Validation reports many missing references
**Check:** Did you run both claims/evidence AND RDMAP extraction?  
**Note:** Partial extractions will show "deferred validation" - this is expected

### Issue: Consolidation metadata missing
**Check:** Did you run Pass 2 (rationalization)?  
**Note:** Only consolidated items need consolidation_metadata

### Issue: Cross-references broken after consolidation
**Check:** Did Pass 2 update all reference arrays when consolidating?  
**Fix:** Re-run Pass 2 with attention to cross-reference updates

---

## Next Steps After Extraction

1. **Review validation report** - Address any CRITICAL or IMPORTANT issues
2. **Spot-check extraction** - Verify a sample of items for accuracy
3. **Proceed to assessment** - Use extraction as input for transparency/replicability evaluation

---

## Version History

- **v2.4 (2025-10-19):** Unified claims/evidence and RDMAP extraction with iterative accumulation workflow
- **v2.3 (2025-10-18):** Added consolidation metadata and multi-dimensional evidence pattern to claims/evidence
- **v2.2 (2025-10-17):** Two-pass workflow for claims/evidence
- **v2.0-2.1 (2025-10-16):** Initial claims/evidence extraction system

---

## Support & Documentation

**Brief overview:** This README  
**Detailed guidance:** See individual prompt files  
**Schema specification:** `schema_v2_4.json`  
**Test data:** Sobotkova et al. 2023 (archaeological survey paper)

**Questions or issues?** This is a development system under active refinement. Testing and feedback welcome.

---

**Ready to extract!** Start with the blank template and run your first pass.