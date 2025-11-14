# Extraction Workflow

Complete guide to the seven-pass extraction workflow for research papers.

**Version:** 2.6
**Last Updated:** 2025-11-13

---

## Overview

This workflow extracts **Claims, Evidence, RDMAP (Research Design, Methods, Protocols), and Infrastructure** from research papers using a systematic multi-pass approach. All extraction passes operate on a **single shared JSON document** that accumulates content as it flows through the pipeline.

---

## Quick Start

### 1. Start with Template

Use the blank template from `extraction-system/templates/blank_template_v2.6.json`

### 2. Run Extraction Passes

**Complete Workflow:**
```
Blank Template (v2.6)
    ↓
Pass 0: Metadata (structure mapping)
    ↓
Pass 1: Claims/Evidence (liberal extraction)
    ↓
Pass 2: Claims/Evidence (rationalisation)
    ↓
Pass 3: RDMAP explicit (liberal extraction)
    ↓
Pass 4: RDMAP implicit (targeted extraction)
    ↓
Pass 5: RDMAP (rationalisation)
    ↓
Pass 6: Infrastructure (PIDs, FAIR, funding, permits)
    ↓
Pass 7: Validation (integrity checks)
```

### 3. Validate

Run Pass 7 validation to check structural integrity after extraction completes.

---

## Extraction Passes

### Pass 0: Metadata Extraction

**Prompt:** [00-metadata_pass0_prompt.md](../../extraction-system/prompts/00-metadata_pass0_prompt.md)

**Purpose:** Extract publication metadata and map paper structure
**Populates:** `metadata` object and `extraction_notes`
**Duration:** 10-15 minutes

**Extracts:**
- Publication details (title, authors, year, journal)
- Paper structure (sections, subsections, key components)
- Document characteristics (length, type, complexity)

**Tips:**
- Establishes foundation for subsequent passes
- Maps section boundaries for targeted extraction
- Identifies methodological approaches early

---

### Phase 1: Claims & Evidence (Passes 1-2)

#### Pass 1: Liberal Extraction

**Prompt:** [01-claims-evidence_pass1_prompt.md](../../extraction-system/prompts/01-claims-evidence_pass1_prompt.md)

**Purpose:** Comprehensively capture all evidence, claims, and implicit arguments
**Strategy:** Over-capture (40-50% more items than final expected)
**Populates:** `evidence`, `claims`, `implicit_arguments` arrays
**Leaves alone:** `research_designs`, `methods`, `protocols`, `infrastructure` arrays
**Duration:** 45-60 minutes (typical paper)

**Tips:**
- Extract liberally, err on side of over-capture
- Preserve granularity (split compound observations)
- Mark uncertainties explicitly
- Don't worry about perfect boundaries yet

#### Pass 2: Rationalisation

**Prompt:** [02-claims-evidence_pass2_prompt.md](../../extraction-system/prompts/02-claims-evidence_pass2_prompt.md)

**Purpose:** Consolidate, refine boundaries, verify relationships
**Target:** 15-20% reduction through consolidation
**Refines:** `evidence`, `claims`, `implicit_arguments` arrays
**Leaves alone:** RDMAP and infrastructure arrays
**Duration:** 30-45 minutes

**Actions:**
- Consolidate redundant items (with metadata)
- Refine evidence/claim boundaries
- Verify cross-references
- Add consolidation_metadata to merged items

---

### Phase 2: RDMAP (Research Design, Methods, Protocols) (Passes 3-5)

#### Pass 3: Explicit RDMAP Extraction

**Prompt:** [03-rdmap_pass1a_explicit_prompt.md](../../extraction-system/prompts/03-rdmap_pass1a_prompt.md)

**Purpose:** Extract explicitly stated research designs, methods, and protocols
**Strategy:** Over-capture with three-tier hierarchy
**Populates:** `research_designs`, `methods`, `protocols` arrays (explicit items only)
**Leaves alone:** Claims/evidence and infrastructure arrays
**Duration:** 60-90 minutes

**Three-Tier Framework:**
- **Research Designs**: Strategic framing and rationale (WHY)
- **Methods**: Tactical approaches (WHAT was done)
- **Protocols**: Operational procedures (HOW specifically)

#### Pass 4: Implicit RDMAP Extraction

**Prompt:** [04-rdmap_pass1b_implicit_prompt.md](../../extraction-system/prompts/04-rdmap_pass1b_implicit_prompt.md)

**Purpose:** Extract implicit, assumed, or inadequately documented methodological information
**Strategy:** Identify gaps and infer standard practices
**Populates:** Additional items in `research_designs`, `methods`, `protocols` arrays
**Marks:** `explicitly_stated: false` for implicit items
**Duration:** 30-45 minutes

**Focus Areas:**
- Standard procedures not explicitly documented
- Assumed methodological conventions
- Implicit theoretical frameworks
- Gaps in operational detail

#### Pass 5: RDMAP Rationalisation

**Prompt:** [05-rdmap_pass2_prompt.md](../../extraction-system/prompts/05-rdmap_pass2_prompt.md)

**Purpose:** Consolidate, verify tier assignments, validate cross-references
**Target:** 15-20% reduction through consolidation
**Refines:** `research_designs`, `methods`, `protocols` arrays (both explicit and implicit)
**Leaves alone:** Claims/evidence and infrastructure arrays
**Duration:** 45-60 minutes

**Actions:**
- Consolidate redundant RDMAP items
- Verify tier assignments (Design vs Method vs Protocol)
- Formalise cross-references to claims/evidence
- Check hierarchy consistency
- Validate explicit/implicit distinctions

---

### Phase 3: Infrastructure (Pass 6)

#### Pass 6: Infrastructure Extraction

**Prompt:** [06-infrastructure_pass6_prompt.md](../../extraction-system/prompts/06-infrastructure_pass6_prompt.md)

**Purpose:** Extract reproducibility infrastructure and research metadata
**Populates:** `infrastructure` object (PIDs, FAIR assessments, funding, permits)
**Leaves alone:** All other arrays
**Duration:** 30-45 minutes

**Extracts:**
- **PIDs**: DOI, ORCID, data/code repository DOIs
- **FAIR Assessment**: Data and code accessibility (Findable, Accessible, Interoperable, Reusable)
- **Funding**: Grant details, funding bodies
- **Permits**: Ethics approvals, access permits, data collection authorisations

**Tips:**
- Check acknowledgements for funding
- Look in methods for ethics statements
- Check references for data availability statements
- Review supplementary material sections

---

### Phase 4: Validation (Pass 7)

#### Pass 7: Integrity Checks

**Prompt:** [07-validation_prompt.md](../../extraction-system/prompts/07-validation_prompt.md)

**Purpose:** Automated structural validation
**Input:** Complete extraction (all phases)
**Output:** Validation report (does NOT modify extraction)
**Duration:** 15-30 minutes

**Checks:**
- Cross-reference integrity (bidirectional consistency)
- Hierarchy validation (Design → Methods → Protocols; Claim chains)
- Schema compliance (required fields, valid enums, ID formats)
- Expected information completeness
- Consolidation metadata presence and validity
- Infrastructure field completeness

**Flexibility:** Works with partial extractions for testing

---

## Key Principles

### Iterative Accumulation

- **Single document** flows through all passes
- Each pass populates or refines specific arrays/objects
- Other arrays remain untouched
- No merging step needed

### Separation of Concerns

- **Pass 0:** Populates metadata only
- **Passes 1-2:** Only touch claims/evidence arrays
- **Passes 3-5:** Only touch RDMAP arrays
- **Pass 6:** Only touches infrastructure object
- **Pass 7:** Reads all, modifies none (validation only)

### Extraction Philosophy

- **Pass 0:** Structural mapping (comprehensive)
- **Passes 1, 3, 4:** Liberal extraction with over-capture (comprehensive)
- **Passes 2, 5:** Rationalisation with consolidation (refined)
- **Pass 6:** Infrastructure extraction (comprehensive)
- **Pass 7:** Validation without modification (structural integrity)

### Cross-Reference Architecture

- Simple string ID arrays (e.g., `["M003", "M007"]`)
- Bidirectional consistency enforced
- Works across object types

---

## Expected Outputs

### After Pass 0 (Metadata)

```json
{
  "metadata": {
    "title": "Paper title",
    "authors": [...],
    "publication_year": 2024,
    ...
  },
  "evidence": [],
  "claims": [],
  "implicit_arguments": [],
  "research_designs": [],
  "methods": [],
  "protocols": [],
  "infrastructure": {}
}
```

### After Passes 1-2 (Claims/Evidence)

```json
{
  "evidence": [40-60 items],
  "claims": [30-50 items],
  "implicit_arguments": [5-15 items],
  "research_designs": [],
  "methods": [],
  "protocols": [],
  "infrastructure": {}
}
```

### After Passes 3-5 (RDMAP)

```json
{
  "evidence": [40-60 items],
  "claims": [30-50 items],
  "implicit_arguments": [5-15 items],
  "research_designs": [8-15 items],
  "methods": [15-30 items],
  "protocols": [10-25 items],
  "infrastructure": {}
}
```

### After Pass 6 (Infrastructure)

```json
{
  "evidence": [40-60 items],
  "claims": [30-50 items],
  "implicit_arguments": [5-15 items],
  "research_designs": [8-15 items],
  "methods": [15-30 items],
  "protocols": [10-25 items],
  "infrastructure": {
    "pids": {...},
    "fair_assessment": {...},
    "funding": [...],
    "permits_and_authorisations": [...]
  }
}
```

### After Pass 7 (Validation)

Separate validation report with:
- Overall status (PASS / PASS_WITH_ISSUES / FAIL)
- Issue counts by severity
- Specific recommendations

---

## Common Scenarios

### Full Paper Extraction (Recommended)

1. Blank template (v2.6)
2. Pass 0 (Metadata - entire paper)
3. Pass 1 (Claims - Results + Discussion sections)
4. Pass 2 (Claims rationalisation)
5. Pass 3 (RDMAP explicit - Methods section)
6. Pass 4 (RDMAP implicit - Methods section)
7. Pass 5 (RDMAP rationalisation)
8. Pass 6 (Infrastructure - entire paper)
9. Pass 7 (Validation)

**Result:** Complete extraction, all arrays populated, full validation

### Methods-Only Extraction

1. Blank template (v2.6)
2. Pass 0 (Metadata)
3. Pass 3 (RDMAP explicit - Methods section)
4. Pass 4 (RDMAP implicit - Methods section)
5. Pass 5 (RDMAP rationalisation)
6. Pass 7 (RDMAP-only validation)

**Result:** Only RDMAP arrays populated, deferred validation for claims cross-references

### Iterative Section Extraction

1. Blank template → Pass 0 (Metadata)
2. Same JSON → Pass 1 (Results section) → Pass 2
3. Same JSON → Pass 1 (Discussion section) → Pass 2
4. Same JSON → Pass 3 (Methods explicit) → Pass 4 (Methods implicit) → Pass 5
5. Same JSON → Pass 6 (Infrastructure)
6. Pass 7 (Validation)

**Result:** Document accumulates content from multiple sections

---

## Troubleshooting

### Pass modified wrong arrays

**Check:** Correct prompt version (v2.6)?
**Fix:** v2.6 prompts have explicit array boundaries and separation of concerns

### Validation reports many missing references

**Check:** All passes completed (0-6)?
**Note:** Partial extractions show "deferred validation" (expected)

### Consolidation metadata missing

**Check:** Passes 2 and 5 run for object types?
**Note:** Only consolidated items need metadata

### Cross-references broken after consolidation

**Check:** Passes 2 or 5 updated all reference arrays?
**Fix:** Re-run rationalisation pass with attention to cross-reference updates

### Infrastructure fields empty despite presence in paper

**Check:** Pass 6 completed?
**Note:** Infrastructure extraction is separate pass, not automatic

---

## Best Practices

### Before You Start

- Read the paper completely first
- Identify key sections (Abstract, Intro, Methods, Results, Discussion)
- Prepare paper text (see [pdf-extraction.md](pdf-extraction.md))
- Copy blank template (v2.6) to working file

### During Extraction

- Follow pass order (0 → 1 → 2 → 3 → 4 → 5 → 6 → 7)
- Don't skip passes (especially Pass 0 and Pass 6)
- Save JSON after each pass
- Spot-check a few items per pass
- Don't aim for perfection in liberal extraction passes (1, 3, 4)

### After Extraction

- Run Pass 7 validation
- Address CRITICAL issues immediately
- Review IMPORTANT issues
- Spot-check sample of items against paper
- Verify cross-references make sense

---

## Quality Expectations

### Pass 0 (Metadata)

- **Completeness:** All publication metadata captured
- **Structure mapping:** All major sections identified
- **Accuracy:** 100% for basic metadata

### Passes 1, 3, 4 (Liberal Extraction)

- **Completeness:** >95% of relevant items captured
- **Precision:** 60-70% (many false positives OK)
- **Over-capture:** 40-50% more items than final

### Passes 2, 5 (Rationalisation)

- **Reduction:** 15-20% through consolidation
- **Precision:** 80-85% (boundary refinement)
- **Metadata:** 100% of consolidated items have metadata

### Pass 6 (Infrastructure)

- **Completeness:** All available infrastructure captured
- **FAIR Assessment:** Evidence-based ratings
- **PID Validation:** All identifiers verified

### Pass 7 (Validation)

- **Critical Issues:** 0 (must fix before proceeding)
- **Important Issues:** <5 (review and address)
- **Cross-reference Integrity:** 100%

---

## Time Estimates

**Typical Methods Paper (15-20 pages):**

- Pass 0 (Metadata): 10-15 minutes
- Pass 1 (Claims liberal): 45-60 minutes
- Pass 2 (Claims rationalisation): 30-45 minutes
- Pass 3 (RDMAP explicit): 60-90 minutes
- Pass 4 (RDMAP implicit): 30-45 minutes
- Pass 5 (RDMAP rationalisation): 45-60 minutes
- Pass 6 (Infrastructure): 30-45 minutes
- Pass 7 (Validation): 15-30 minutes
- **Total:** 5-6.5 hours

**Shorter Papers (5-10 pages):** 3-4 hours
**Longer Papers (>30 pages):** 8-10 hours, consider sectioning

---

## Next Steps After Extraction

1. **Review validation report** - Address CRITICAL and IMPORTANT issues
2. **Spot-check extraction** - Verify sample items for accuracy
3. **Archive your extraction** - Save with clear filename (see [outputs/README.md](../../outputs/README.md))
4. **Proceed to assessment** - Use extraction for transparency/replicability evaluation (future capability)

---

## Related Documentation

- [Getting Started](getting-started.md) - First extraction walkthrough
- [Schema Reference](schema-reference.md) - Understanding object types
- [PDF Extraction](pdf-extraction.md) - Preparing source papers
- [Extraction System Overview](../../extraction-system/README.md) - Technical details
- [Research Assessor Guide](../research-assessor-guide/) - Skill documentation

---

**Ready to extract!** Start with [getting-started.md](getting-started.md) for a step-by-step walkthrough.
