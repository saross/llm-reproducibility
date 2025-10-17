# Extraction vs Assessment Workflow v1.0

**Version:** 1.0  
**Created:** 2025-10-17  
**Purpose:** Clarify the distinction between extraction (current work) and assessment (future work) to prevent scope creep

---

## Overview: Two Separate Phases

Our methodology separates **identifying what's in the paper** from **evaluating its quality**. This distinction is critical for maintaining focus and enabling systematic development.

### Phase 1: EXTRACTION (Current Focus)
**Goal:** Identify and structure content from the paper  
**Analogy:** Creating an annotated map of what the paper says  
**Status:** Active development (schema v2.2, prompts v2.2)

### Phase 2: ASSESSMENT (Future Work)
**Goal:** Evaluate credibility and quality of extracted content  
**Analogy:** Using the map to judge the quality of the terrain  
**Status:** Schema prepared, rubrics to be developed in Phase 5

**Inspiration:** The repliCATS project explicitly separates these phases:
- Phase 1: Identify claims from papers (extraction)
- Phase 2: IDEA protocol assessment by experts (evaluation)

---

## Phase 1: EXTRACTION

### What We're Doing

**Identifying and structuring content:**
- What claims does the paper make?
- What evidence supports those claims?
- What methods were used?
- How are claims, evidence, and methods related?
- What implicit arguments underlie the reasoning?
- What information is present vs missing?

**Observing without judging:**
- Note declared uncertainty (what authors state)
- Note expected information gaps (what's missing from checklists)
- Flag patterns that may affect credibility (single-case generalizations, professional judgment)
- Record extraction confidence (explicit/inferred/ambiguous)

### Fields Populated During Extraction

| Field Category | Field Name | What to Capture |
|----------------|------------|-----------------|
| **Content** | evidence_text, claim_text, argument | The actual content from the paper |
| **Classification** | evidence_type, claim_type, claim_role | How to categorize this content |
| **Basis** | evidence_basis, claim_status | Observable characteristics (measurement/judgment, explicit/implicit) |
| **Author Layer** | declared_uncertainty, author_confidence | What authors explicitly state |
| **Relationships** | supports_claims, supported_by_evidence | How elements connect |
| **Extraction Notes** | extraction_flags, expected_information_missing, extraction_notes | Observations made during extraction |
| **Implicit Content** | implicit_arguments, implicit_evidence | Unstated reasoning and professional judgment |
| **Location** | section, page, paragraph, verbatim_quote | Traceability to source |

### What We're NOT Doing During Extraction

❌ **Judging credibility** - Not evaluating whether claims are trustworthy  
❌ **Assigning quality scores** - Not rating transparency/validity/robustness  
❌ **Evaluating evidence strength** - Not determining if evidence is strong/weak  
❌ **Making assessment recommendations** - Not saying "this claim should be questioned"  

### Extraction Workflow

**Pass 1: Liberal Extraction**
1. Read section text
2. Extract all potentially relevant evidence, claims, implicit arguments
3. When uncertain: INCLUDE IT (over-extraction expected)
4. Flag concerns but don't judge quality
5. Note missing information from checklists

**Pass 2: Rationalization**
1. Review Pass 1 extraction + source text
2. Consolidate over-granular items
3. Correct evidence/claim boundaries
4. Remove non-supportive content to project_metadata
5. Verify relationships and citations
6. Add missing implicit generalizations

**Output:** Structured JSON with all content identified, classified, and linked

---

## Phase 2: ASSESSMENT (Future Work)

### What We'll Be Doing

**Evaluating credibility and quality:**
- How transparent is the methodology?
- Is the evidence valid for the claims made?
- How robust are the findings to assumptions?
- Is the research replicable with provided information?
- Are generalizations appropriately bounded?

**Making evaluative judgments:**
- Assign credibility scores using repliCATS 7-signal framework
- Rate evidence strength (strong/moderate/weak/insufficient)
- Provide rationales for assessments
- Identify specific threats to validity/robustness
- Document what would improve credibility

### Fields Populated During Assessment

| Field Category | Field Name | What to Assign |
|----------------|------------|----------------|
| **Evidence Quality** | evidence_strength (score, rationale, limitations, triangulation) | Evaluative judgment of evidence quality |
| **Claim Credibility** | credibility_assessment (7 signals) | Systematic credibility evaluation |
| **Transparency** | score, rationale, missing_elements | How well methods/data documented |
| **Plausibility** | score, rationale, red_flags | Consistency with domain knowledge |
| **Validity** | score, rationale, threats | Methods appropriate to question |
| **Robustness** | score, rationale, vulnerabilities | Sensitivity to assumptions |
| **Comprehensibility** | score, rationale | Clarity of methods/claims |
| **Replicability** | score, rationale, missing_for_replication | Sufficient detail to replicate |
| **Generalizability** | score, rationale, boundary_issues | Scope appropriately bounded |

### What We'll Need for Assessment

**Domain expertise** - Understanding field-specific standards and practices  
**Scoring rubrics** - Empirically-derived thresholds for high/moderate/low ratings  
**Comparative context** - How this paper compares to disciplinary norms  
**Assessment training** - Calibration on what constitutes good/poor transparency, etc.

### Assessment Workflow (Not Yet Designed)

This will be developed in Phase 5 after:
- 50+ claims extracted and structured
- Domain-specific checklists developed
- Empirical patterns in missing information identified
- Scoring rubrics created from corpus analysis

**Tentative approach:**
1. Review structured extraction output
2. Apply credibility signal rubrics
3. Assign scores with detailed rationales
4. Document specific threats/concerns
5. Note what would improve the score

**Output:** Same JSON structure with assessment fields populated

---

## Key Distinctions

### Extraction Says:
- "The paper claims X based on evidence Y"
- "Expected information Z is missing"
- "This appears to be a single-case generalization"
- "Professional judgment is implicit here"
- "Authors express high confidence"

### Assessment Says:
- "This claim has moderate transparency because methods partially specified"
- "Evidence strength is weak due to single observation"
- "Validity threat: generalization from single case"
- "Robustness is low - sensitive to alternative explanations"
- "Replicability score: low - missing 3 key elements"

---

## Common Pitfalls to Avoid

### During Extraction (Current Work)

**Scope Creep:**
❌ "This evidence seems weak" → ✅ "Evidence basis: professional_judgment; note: no supporting measurements provided"  
❌ "The methods are poorly described" → ✅ "Expected information missing: [sample size, calibration, error margins]"  
❌ "This claim is questionable" → ✅ "Extraction flags: {generalization_from_single_case: true}"

**Over-thinking:**
- Don't agonize over whether evidence is "strong enough" - just capture it
- Don't judge whether missing information is "acceptable" - just note it's missing
- Don't evaluate whether claims are "well-supported" - just map the support relationships

**Key principle:** If you're making an evaluative judgment, you've crossed into assessment territory. Step back and just observe/document.

### During Assessment (Future Work)

**Re-extraction:**
❌ Discovering content not extracted → Should have been caught in extraction phase  
❌ Restructuring relationships → Should have been done in extraction/rationalization  
❌ Adding new evidence/claims → Extraction is complete, work with what's there

**Key principle:** Assessment works with the structured data from extraction. If extraction is incomplete, fix the extraction process, don't patch it during assessment.

---

## Why This Separation Matters

### 1. Cognitive Load Management
Trying to identify content AND evaluate quality simultaneously is overwhelming and leads to both missing content and inconsistent judgments.

### 2. Reproducibility
Separation enables independent verification:
- Others can check: "Did you extract everything relevant?" (extraction)
- Others can check: "Do I agree with your credibility scores?" (assessment)

### 3. Iterative Development
We can refine extraction without redoing assessment, and vice versa:
- Improve extraction prompts → Re-extract with better capture
- Develop better rubrics → Re-assess with better standards

### 4. Expertise Deployment
Extraction can be done by trained annotators; assessment may require domain experts. Separation enables efficient use of expertise.

### 5. Automation Potential
Extraction may be more automatable than assessment. Separation allows us to:
- Automate extraction while keeping human assessment
- Or vice versa: Extract manually, develop automated assessment
- Or gradually automate both independently

---

## Workflow Notes

### Schema Support

**Extraction-time fields:**
- All content fields (evidence_text, claim_text, etc.)
- All classification fields (types, roles, scope)
- All observation fields (flags, notes, missing information)
- All relationship fields (supports, supported_by)

**Assessment-time fields:**
- credibility_assessment object (defaults to "not_yet_assessed")
- evidence_strength object (defaults to "not_yet_assessed")
- All score/rationale/concerns subfields

**Tracking completion:**
```json
"workflow_notes": {
  "extraction_complete": true,
  "extraction_completion_date": "2025-10-20",
  "assessment_complete": false,
  "assessment_completion_date": null
}
```

### Current Status

**✅ Extraction Phase:** Active development
- Schema v2.2 complete
- Two-pass prompts created (Pass 1 + Pass 2)
- Testing in progress
- Refinement ongoing based on empirical results

**⏸️ Assessment Phase:** Prepared but not started
- Schema structure ready (credibility_assessment fields defined)
- Rubrics to be developed after 50+ extractions
- Domain-specific criteria to emerge from corpus analysis
- Target start: After Phase 5 empirical refinement

---

## Quick Reference

### "Should I be doing this during extraction?"

**ASK:** "Am I identifying what's in the paper, or evaluating its quality?"

**Extraction tasks:**
- ✅ Finding claims/evidence/methods
- ✅ Mapping relationships
- ✅ Noting missing information
- ✅ Flagging concerning patterns
- ✅ Recording author confidence

**Assessment tasks:**
- ❌ Scoring credibility signals
- ❌ Rating evidence strength
- ❌ Judging transparency
- ❌ Evaluating validity
- ❌ Determining replicability

### "What do I do with quality concerns during extraction?"

**Use observation fields:**
- `extraction_flags` - Mark concerning patterns
- `expected_information_missing` - List gaps from checklists
- `extraction_notes` - Document concerns without scoring
- `extraction_confidence` - Note ambiguity levels

**Example:**
Instead of: "This claim has low validity" (assessment)  
Write: "Extraction flags: {generalization_from_single_case: true}; Expected information missing: [number of cases, temporal range, geographic scope]; Extraction notes: Based on single field season observation" (extraction)

---

## Next Steps

**After Extraction Complete:**
1. Review corpus of 50+ extracted papers
2. Identify patterns in missing information
3. Develop domain-specific assessment rubrics
4. Calibrate scoring thresholds empirically
5. Design assessment workflow
6. Begin pilot assessments
7. Refine and iterate

**Timeline:**
- Extraction development: Ongoing (current phase)
- Assessment development: Phase 5 (after 10+ papers extracted)
- Full assessment deployment: After rubrics validated

---

**Document Status:** v1.0  
**Last Updated:** 2025-10-17  
**Next Review:** When beginning assessment phase development