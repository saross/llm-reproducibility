# Research Extraction Workflow - Prompts Reference

**Version:** 2.6
**Last Updated:** 2025-11-18
**Status:** Production ready

---

## Overview

This workflow extracts **Research Design, Methods, and Protocols (RDMAP)** plus **Claims and Evidence** from research papers using a systematic 8-pass approach. All extraction passes operate on a **single shared JSON document** that accumulates content as it flows through the pipeline.

**Current Schema:** v2.6
**Total Passes:** 8 (Passes 0-7)

---

## Quick Start

### 1. Start with Template

Create or use the blank extraction template:

```json
{
  "schema_version": "2.6",
  "extraction_timestamp": "ISO 8601",
  "extractor": "string",
  "project_metadata": {},
  "evidence": [],
  "claims": [],
  "implicit_arguments": [],
  "research_designs": [],
  "methods": [],
  "protocols": [],
  "reproducibility_infrastructure": {},
  "extraction_notes": {}
}
```

### 2. Run Extraction Passes (Sequential)

```
Pass 0: Metadata extraction
  ↓
Pass 1: Liberal claims/evidence extraction
  ↓
Pass 2: Claims/evidence rationalization
  ↓
Phase 2b: Bidirectional mapping reconciliation (automated script)
  ↓
Pass 3: Liberal RDMAP extraction
  ↓
Pass 4: Implicit RDMAP extraction
  ↓
Pass 5: RDMAP rationalization
  ↓
Phase 5b: Bidirectional mapping reconciliation (automated script)
  ↓
Pass 6: Infrastructure extraction (PIDs, FAIR, funding, ethics)
  ↓
Pass 7: Validation (structural integrity checks)
```

---

## Detailed Workflow

### Pass 0: Metadata Extraction

**Prompt:** `00-metadata_pass0_prompt.md`

- **Input:** First 2-3 pages of PDF (title page, abstract, headers)
- **Action:** Extract bibliographic metadata
- **Populates:** `project_metadata` object (8 fields: title, authors, year, journal, DOI, paper_type, discipline, research_context)
- **Leaves alone:** All other arrays
- **Output:** JSON with metadata populated

---

### Pass 1: Liberal Claims & Evidence Extraction

**Prompt:** `01-claims-evidence_pass1_prompt.md`

- **Input:** Entire paper, processed in section groups (~1000 word chunks)
- **Action:** Extract evidence, claims, and implicit arguments
- **Strategy:** Over-capture (40-50% more items expected)
- **Populates:** `evidence`, `claims`, `implicit_arguments` arrays
- **Leaves alone:** `research_designs`, `methods`, `protocols`, `reproducibility_infrastructure`
- **Output:** JSON with claims/evidence populated

**Target counts:**
- Evidence: 30-60 items
- Claims: 60-100 items
- Implicit Arguments: 10-30 items

---

### Pass 2: Rationalize Claims & Evidence

**Prompt:** `02-claims-evidence_pass2_prompt.md`

- **Input:** JSON from Pass 1
- **Action:** Consolidate, refine boundaries, verify relationships
- **Target:** 15-20% reduction in items
- **Refines:** `evidence`, `claims`, `implicit_arguments` arrays
- **Leaves alone:** RDMAP arrays, infrastructure
- **Output:** JSON with claims/evidence rationalized

---

### Phase 2b: Bidirectional Mapping Reconciliation

**Script:** `extraction-system/scripts/validate_bidirectional.py`

- **Input:** JSON from Pass 2
- **Action:** Auto-correct bidirectional claim↔evidence mappings
- **Validates:** `claims.supported_by` ↔ `evidence.supports_claims`
- **Auto-corrects:** Missing reverse mappings
- **Reports:** Conflicts requiring manual resolution
- **Output:** JSON with corrected mappings

**Run:** `python3 extraction-system/scripts/validate_bidirectional.py outputs/{slug}/extraction.json`

---

### Pass 3: Liberal RDMAP Extraction

**Prompt:** `03-rdmap_pass1a_prompt.md`

- **Input:** Entire paper (SAME section groups as Pass 1)
- **Action:** Extract research designs, methods, and protocols
- **Strategy:** Over-capture with three-tier hierarchy, EQUAL ATTENTION TO ALL SECTIONS
- **Populates:** `research_designs`, `methods`, `protocols` arrays
- **Leaves alone:** `evidence`, `claims`, `implicit_arguments`, `infrastructure`
- **Output:** JSON with explicit RDMAP populated

**Target counts:**
- Research Designs: 3-6 items
- Methods: 8-15 items
- Protocols: 15-30 items

---

### Pass 4: Implicit RDMAP Extraction

**Prompt:** `04-rdmap_pass1b_implicit_prompt.md`

- **Input:** Entire paper (whole-paper scan)
- **Action:** Identify mentioned-but-undocumented procedures
- **Strategy:** Pattern recognition for unstated methodologies
- **Populates:** Adds implicit items to `methods` and `protocols` arrays
- **Leaves alone:** All other arrays
- **Output:** JSON with implicit RDMAP added

**Typical implicit RDMAP:** 10-30% of total RDMAP

---

### Pass 5: Rationalize RDMAP

**Prompt:** `05-rdmap_pass2_prompt.md`

- **Input:** JSON from Passes 3-4
- **Action:** Consolidate, verify tier assignments, validate hierarchy
- **Target:** 15-20% reduction in RDMAP items
- **Refines:** `research_designs`, `methods`, `protocols` arrays
- **Leaves alone:** Claims/evidence arrays, infrastructure
- **Output:** JSON with RDMAP rationalized

---

### Phase 5b: Bidirectional RDMAP Reconciliation

**Script:** `extraction-system/scripts/validate_bidirectional.py`

- **Input:** JSON from Pass 5
- **Action:** Auto-correct bidirectional RDMAP hierarchy mappings
- **Validates:**
  - `methods.implements_designs` ↔ `research_designs.implemented_by_methods`
  - `protocols.implements_methods` ↔ `methods.implemented_by_protocols`
- **Auto-corrects:** Missing reverse mappings
- **Output:** JSON with corrected RDMAP mappings

---

### Pass 6: Infrastructure Extraction

**Prompt:** `06-infrastructure_pass6_prompt.md`

- **Input:** Entire paper (focus on front matter, back matter, acknowledgements)
- **Action:** Extract reproducibility infrastructure and assess FAIR compliance
- **Populates:** `reproducibility_infrastructure` object with 13 sections:
  1. `persistent_identifiers` (PIDs + PID graph analysis)
  2. `funding`
  3. `data_availability`
  4. `code_availability`
  5. `author_contributions`
  6. `conflicts_of_interest`
  7. `ethics_approval`
  8. `permits_and_authorizations`
  9. `preregistration`
  10. `supplementary_materials`
  11. `references_completeness`
  12. `fair_assessment` (Findable, Accessible, Interoperable, Reusable - scored 0-40)
  13. `extraction_metadata`
- **Leaves alone:** All content extraction arrays
- **Output:** JSON with infrastructure populated

---

### Pass 7: Validation

**Prompt:** `07-validation_prompt.md`

- **Input:** Complete extraction from Passes 0-6
- **Action:** Comprehensive structural validation
- **Validates:** All object types present in document
- **Checks:**
  - Cross-reference integrity (bidirectional consistency)
  - Hierarchy validation (Design → Methods → Protocols; Claim chains)
  - Schema compliance (required fields, valid enums, ID formats)
  - Sourcing completeness (100% verbatim_quote or trigger_text)
  - Metadata completeness
  - Infrastructure completeness
  - Expected information completeness
  - Consolidation metadata
- **Output:** Validation report (produces separate report, does NOT modify extraction.json)
- **Status:** PASS | PASS_WITH_WARNINGS | FAIL

---

## File Listing

### Extraction Prompts (8 passes)

| Pass | File | Purpose | Populates |
|------|------|---------|-----------|
| 0 | `00-metadata_pass0_prompt.md` | Metadata extraction | `project_metadata` |
| 1 | `01-claims-evidence_pass1_prompt.md` | Liberal claims/evidence | `evidence`, `claims`, `implicit_arguments` |
| 2 | `02-claims-evidence_pass2_prompt.md` | Claims/evidence rationalization | Refines Pass 1 arrays |
| 3 | `03-rdmap_pass1a_prompt.md` | Liberal RDMAP extraction | `research_designs`, `methods`, `protocols` |
| 4 | `04-rdmap_pass1b_implicit_prompt.md` | Implicit RDMAP extraction | Adds to `methods`, `protocols` |
| 5 | `05-rdmap_pass2_prompt.md` | RDMAP rationalization | Refines Pass 3-4 arrays |
| 6 | `06-infrastructure_pass6_prompt.md` | Infrastructure extraction | `reproducibility_infrastructure` |
| 7 | `07-validation_prompt.md` | Validation | Nothing (produces separate report) |

### Supporting Prompts

| File | Purpose |
|------|---------|
| `qa-qi-prompt-v3.md` | Quality assurance and quality improvement guidance |

---

## Key Principles

### Iterative Accumulation
- **Single document** flows through all 8 passes
- Each pass populates or refines specific sections
- Other sections remain untouched
- No merging step needed

### Separation of Concerns
- **Pass 0:** Metadata only
- **Passes 1-2:** Claims/evidence only
- **Phases 2b, 5b:** Bidirectional mapping validation (automated scripts)
- **Passes 3-5:** RDMAP only
- **Pass 6:** Infrastructure only
- **Pass 7:** Validation (reads all, modifies none)

### Extraction Philosophy
- **Liberal passes (1, 3, 4):** Over-capture with 40-50% surplus (comprehensive)
- **Rationalization passes (2, 5):** Consolidate with 15-20% reduction (refined)
- **Automated reconciliation (2b, 5b):** Bidirectional mapping integrity
- **Infrastructure pass (6):** Systematic infrastructure capture
- **Validation pass (7):** Structural integrity without modification

### Cross-Reference Architecture
- Simple string ID arrays (e.g., `["M003", "M007"]`)
- Bidirectional consistency enforced by automated scripts
- Works across object types (methods reference claims, protocols reference evidence)

---

## Testing vs Production

### For Testing
**Start with blank template:**
- Test any extraction independently
- Test with pre-populated arrays to simulate realistic conditions
- Validate partial extractions (RDMAP-only or claims-only during development)

### For Production
**Follow full pipeline:**
1. Start with blank template
2. Run all passes in sequence (0-7)
3. Run bidirectional reconciliation scripts after Passes 2 and 5
4. Validate complete extraction (Pass 7)
5. Proceed to assessment phase (Passes 8-9)

---

## Expected Outputs

### After Metadata Extraction (Pass 0)
```json
{
  "project_metadata": {
    "paper_title": "...",
    "authors": ["..."],
    "publication_year": 2023,
    "journal": "...",
    "doi": "...",
    "paper_type": "research_article",
    "discipline": "archaeology",
    "research_context": "..."
  }
}
```

### After Claims/Evidence Extraction (Passes 1-2)
```json
{
  "evidence": [30-60 items],           // Populated
  "claims": [60-100 items],            // Populated
  "implicit_arguments": [10-30 items], // Populated
  "research_designs": [],              // Empty (not yet extracted)
  "methods": [],                       // Empty
  "protocols": []                      // Empty
}
```

### After RDMAP Extraction (Passes 3-5)
```json
{
  "evidence": [30-60 items],           // From Passes 1-2
  "claims": [60-100 items],            // From Passes 1-2
  "implicit_arguments": [10-30 items], // From Passes 1-2
  "research_designs": [3-6 items],     // Newly populated
  "methods": [8-15 items],             // Newly populated
  "protocols": [15-30 items]           // Newly populated
}
```

### After Infrastructure Extraction (Pass 6)
```json
{
  "reproducibility_infrastructure": {
    "persistent_identifiers": {...},
    "funding": {...},
    "data_availability": {...},
    "code_availability": {...},
    "fair_assessment": {
      "fair_total_score": 35,
      "findable_score": 9,
      "accessible_score": 10,
      "interoperable_score": 8,
      "reusable_score": 8
    }
  }
}
```

### After Validation (Pass 7)
Separate validation report:
```json
{
  "validation_summary": {
    "overall_status": "PASS | PASS_WITH_WARNINGS | FAIL",
    "critical_issues": 0,
    "important_issues": 0,
    "minor_issues": 5
  },
  "recommendations": [...]
}
```

---

## Common Scenarios

### Scenario 1: Full Paper Extraction (Production)

```
1. Pass 0: Metadata
2. Pass 1: Liberal claims/evidence (all sections)
3. Pass 2: Rationalize claims/evidence
4. Phase 2b: Bidirectional reconciliation script
5. Pass 3: Liberal RDMAP (all sections)
6. Pass 4: Implicit RDMAP
7. Pass 5: Rationalize RDMAP
8. Phase 5b: Bidirectional reconciliation script
9. Pass 6: Infrastructure extraction
10. Pass 7: Validation
```

All arrays populated, infrastructure complete, validation PASS.

### Scenario 2: Testing RDMAP Extraction Only

```
1. Blank template → Pass 3 (RDMAP) → Pass 4 (Implicit) → Pass 5 (Rationalize) → Pass 7 (RDMAP-only validation)
```

Claims/evidence arrays remain empty. Validation notes deferred validation for cross-references to claims/evidence.

---

## Troubleshooting

### Issue: Validation fails with broken references

**Cause:** Consolidation in Pass 2 or Pass 5 didn't update all cross-references
**Fix:** Run bidirectional reconciliation scripts (Phase 2b or 5b) - auto-corrects most issues

### Issue: Bidirectional script reports conflicts

**Cause:** Contradictory forward and reverse references
**Fix:** Manually inspect conflicting mappings in extraction.json, resolve contradictions, re-run script

### Issue: Validation reports many missing references

**Check:** Did you run both claims/evidence AND RDMAP extraction?
**Note:** Partial extractions will show "deferred validation" - this is expected during testing

### Issue: Consolidation metadata missing

**Check:** Did you run Pass 2 or Pass 5 (rationalization)?
**Note:** Only consolidated items need consolidation_metadata

### Issue: Infrastructure section empty

**Check:** Did you run Pass 6 (Infrastructure extraction)?
**Note:** Pass 6 was added in v2.6 - older extractions may not have infrastructure data

---

## Next Steps After Extraction

1. **Review validation report** - Address any CRITICAL or IMPORTANT issues
2. **Spot-check extraction** - Verify a sample of items for accuracy
3. **Run assessment workflow** - Pass 8 (Classification), Pass 9 (Credibility assessment)

---

## Version History

- **v2.6 (2025-11-18):** Added Pass 6 (Infrastructure extraction), updated to 8-pass workflow (0-7), added bidirectional reconciliation phases (2b, 5b), updated schema to v2.6
- **v2.5 (2025-10-30):** Added Pass 0 (Metadata extraction), updated to 7-pass workflow (0-6)
- **v2.4 (2025-10-19):** Unified claims/evidence and RDMAP extraction with iterative accumulation workflow
- **v2.3 (2025-10-18):** Added consolidation metadata and multi-dimensional evidence pattern
- **v2.2 (2025-10-17):** Two-pass workflow for claims/evidence
- **v2.0-2.1 (2025-10-16):** Initial claims/evidence extraction system

---

## Support & Documentation

**Brief overview:** This README
**Detailed guidance:** See individual prompt files
**Canonical workflow:** `input/workflow.md`
**Planning guide:** `extraction-system/extraction-plan-unified-model.md`
**Schema specification:** `extraction-system/schema/`
**Research assessor skill:** `.claude/skills/research-assessor/SKILL.md`

**Questions or issues?** This is a production system under continuous refinement. Testing and feedback welcome.

---

**Ready to extract!** Start with Pass 0 and proceed sequentially through Pass 7.
