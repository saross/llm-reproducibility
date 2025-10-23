# Extraction Workflow

Complete guide to the five-pass extraction workflow for research papers.

**Version:** 2.5
**Last Updated:** 2025-10-23

---

## Overview

This workflow extracts **Claims, Evidence, and RDMAP (Research Design, Methods, Protocols)** from research papers using a systematic multi-pass approach. All extraction passes operate on a **single shared JSON document** that accumulates content as it flows through the pipeline.

---

## Quick Start

### 1. Start with Template

Use the blank template from [../../examples/blank_template_v2.5.json](../../examples/blank_template_v2.5.json)

### 2. Run Extraction Passes

**Recommended Order:**
```
Blank Template
    ↓
Claims/Evidence Pass 1 (Liberal extraction)
    ↓
Claims/Evidence Pass 2 (Rationalization)
    ↓
RDMAP Pass 1 (Liberal extraction)
    ↓
RDMAP Pass 2 (Rationalization)
    ↓
Pass 3 Validation (Integrity checks)
```

**Alternative:** RDMAP first, then Claims/Evidence (both produce same result)

### 3. Validate

Run Pass 3 validation to check structural integrity before assessment.

---

## Extraction Passes

### Phase 1: Claims & Evidence

#### Pass 1: Liberal Extraction
**Prompt:** [claims-evidence_pass1_prompt.md](../../extraction-system/prompts/claims-evidence_pass1_prompt.md)

**Purpose:** Comprehensively capture all evidence, claims, and implicit arguments
**Strategy:** Over-capture (40-50% more items than final expected)
**Populates:** `evidence`, `claims`, `implicit_arguments` arrays
**Leaves alone:** `research_designs`, `methods`, `protocols` arrays

**Tips:**
- Extract liberally, err on side of over-capture
- Preserve granularity (split compound observations)
- Mark uncertainties explicitly
- Don't worry about perfect boundaries yet

#### Pass 2: Rationalization
**Prompt:** [claims-evidence_pass2_prompt.md](../../extraction-system/prompts/claims-evidence_pass2_prompt.md)

**Purpose:** Consolidate, refine boundaries, verify relationships
**Target:** 15-20% reduction through consolidation
**Refines:** `evidence`, `claims`, `implicit_arguments` arrays
**Leaves alone:** RDMAP arrays

**Actions:**
- Consolidate redundant items (with metadata)
- Refine evidence/claim boundaries
- Verify cross-references
- Add consolidation_metadata to merged items

---

### Phase 2: RDMAP (Research Design, Methods, Protocols)

#### Pass 1: Liberal Extraction
**Prompt:** [rdmap_pass1_prompt.md](../../extraction-system/prompts/rdmap_pass1_prompt.md)

**Purpose:** Extract research designs, methods, and protocols
**Strategy:** Over-capture with three-tier hierarchy
**Populates:** `research_designs`, `methods`, `protocols` arrays
**Leaves alone:** `evidence`, `claims`, `implicit_arguments` arrays

**Three-Tier Framework:**
- **Research Designs**: Strategic framing and rationale (WHY)
- **Methods**: Tactical approaches (WHAT was done)
- **Protocols**: Operational procedures (HOW specifically)

#### Pass 2: Rationalization
**Prompt:** [rdmap_pass2_prompt.md](../../extraction-system/prompts/rdmap_pass2_prompt.md)

**Purpose:** Consolidate, verify tier assignments, validate cross-references
**Target:** 15-20% reduction through consolidation
**Refines:** `research_designs`, `methods`, `protocols` arrays
**Leaves alone:** Claims/evidence arrays

**Actions:**
- Consolidate redundant RDMAP items
- Verify tier assignments (Design vs Method vs Protocol)
- Formalize cross-references to claims/evidence
- Check hierarchy consistency

---

### Phase 3: Validation

#### Pass 3: Integrity Checks
**Prompt:** [rdmap_pass3_prompt.md](../../extraction-system/prompts/rdmap_pass3_prompt.md)

**Purpose:** Automated structural validation
**Input:** Complete extraction (all phases)
**Output:** Validation report (does NOT modify extraction)

**Checks:**
- Cross-reference integrity (bidirectional consistency)
- Hierarchy validation (Design → Methods → Protocols; Claim chains)
- Schema compliance (required fields, valid enums, ID formats)
- Expected information completeness
- Consolidation metadata presence and validity

**Flexibility:** Works with partial extractions for testing

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
- Works across object types

---

## Expected Outputs

### After Claims/Evidence Extraction
```json
{
  "evidence": [40-60 items],
  "claims": [30-50 items],
  "implicit_arguments": [5-15 items],
  "research_designs": [],
  "methods": [],
  "protocols": []
}
```

### After RDMAP Extraction
```json
{
  "evidence": [40-60 items],
  "claims": [30-50 items],
  "implicit_arguments": [5-15 items],
  "research_designs": [8-15 items],
  "methods": [15-30 items],
  "protocols": [10-25 items]
}
```

### After Validation
Separate validation report with:
- Overall status (PASS / PASS_WITH_ISSUES / FAIL)
- Issue counts by severity
- Specific recommendations

---

## Common Scenarios

### Full Paper Extraction (Recommended)

1. Blank template
2. Claims Pass 1 (Results + Discussion sections)
3. Claims Pass 2
4. RDMAP Pass 1 (Methods section)
5. RDMAP Pass 2
6. Pass 3 (validation)

**Result:** Complete extraction, all arrays populated, full validation

### Methods-Only Extraction

1. Blank template
2. RDMAP Pass 1 (Methods section)
3. RDMAP Pass 2
4. Pass 3 (RDMAP-only validation)

**Result:** Only RDMAP arrays populated, deferred validation for claims cross-references

### Iterative Section Extraction

1. Blank template → Claims Pass 1 (Results) → Claims Pass 2
2. Same JSON → Claims Pass 1 (Discussion) → Claims Pass 2
3. Same JSON → RDMAP Pass 1 (Methods) → RDMAP Pass 2
4. Pass 3

**Result:** Document accumulates content from multiple sections

---

## Troubleshooting

### Pass modified wrong arrays
**Check:** Correct prompt version (v2.5)?
**Fix:** v2.5 prompts have explicit array boundaries

### Validation reports many missing references
**Check:** Both claims/evidence AND RDMAP extracted?
**Note:** Partial extractions show "deferred validation" (expected)

### Consolidation metadata missing
**Check:** Pass 2 run for that object type?
**Note:** Only consolidated items need metadata

### Cross-references broken after consolidation
**Check:** Pass 2 updated all reference arrays?
**Fix:** Re-run Pass 2 with attention to cross-reference updates

---

## Best Practices

### Before You Start
- Read the paper completely first
- Identify key sections (Methods, Results, Discussion)
- Prepare paper text (see [pdf-extraction.md](pdf-extraction.md))
- Copy blank template to working file

### During Extraction
- Follow pass order (don't skip ahead)
- Save JSON after each pass
- Spot-check a few items per pass
- Don't aim for perfection in Pass 1

### After Extraction
- Run Pass 3 validation
- Address CRITICAL issues immediately
- Review IMPORTANT issues
- Spot-check sample of items against paper
- Verify cross-references make sense

---

## Quality Expectations

### Pass 1 (Liberal Extraction)
- **Completeness:** >95% of relevant items captured
- **Precision:** 60-70% (many false positives OK)
- **Over-capture:** 40-50% more items than final

### Pass 2 (Rationalization)
- **Reduction:** 15-20% through consolidation
- **Precision:** 80-85% (boundary refinement)
- **Metadata:** 100% of consolidated items have metadata

### Pass 3 (Validation)
- **Critical Issues:** 0 (must fix before proceeding)
- **Important Issues:** <5 (review and address)
- **Cross-reference Integrity:** 100%

---

## Time Estimates

**Typical Methods Paper (15-20 pages):**
- Claims Pass 1: 45-60 minutes
- Claims Pass 2: 30-45 minutes
- RDMAP Pass 1: 60-90 minutes
- RDMAP Pass 2: 45-60 minutes
- Pass 3: 15-30 minutes
- **Total:** 4-5 hours

**Shorter Papers:** 2-3 hours
**Longer Papers (>30 pages):** 6-8 hours, consider sectioning

---

## Next Steps After Extraction

1. **Review validation report** - Address CRITICAL and IMPORTANT issues
2. **Spot-check extraction** - Verify sample items for accuracy
3. **Archive your extraction** - Save with clear filename
4. **Proceed to assessment** - Use extraction for transparency/replicability evaluation (future)

---

## Related Documentation

- [Getting Started](getting-started.md) - First extraction walkthrough
- [Schema Reference](schema-reference.md) - Understanding object types
- [PDF Extraction](pdf-extraction.md) - Preparing source papers
- [Skill Documentation](../skill-documentation/) - Technical details

---

**Ready to extract!** Start with [getting-started.md](getting-started.md) for a step-by-step walkthrough.
