# Transparency Metric Documentation Gap

**Date:** 2025-10-25
**Status:** DEFERRED - Implement during assessment phase development
**Context:** Extraction phase near completion, assessment phase upcoming

---

## Issue Identified

During Sobotkova et al. 2023 extraction review, a transparency metric appeared in outputs:
- **89% transparency** (100 explicit / 112 total items)
- Breakdown by category (e.g., Methods: 67%, Protocols: 87%)

This metric is conceptually sound but **not formally documented** in schema, prompts, or skill references.

---

## Key Discussion Points

### 1. Assessment Scope Clarification

**User clarification:** The purpose of extraction is to **assess papers as published**, not to improve them.

> "I think this approach could ultimately be used as a tool by authors to *self-assess* and revise before publication, but *for now* we are focusing on already published papers, so we're not considering what becomes explicit through extractions."

**Implication:** Implicit items represent transparency gaps in the published paper, regardless of whether the extraction makes them explicit.

### 2. Implicit Arguments as Transparency Gaps

**Question raised:** Should Implicit Arguments count against transparency scores?

**Answer:** Yes. Implicit Arguments are definitionally unstated reasoning—things the authors relied on but didn't explicitly state. They represent transparency gaps just like implicit methods/protocols.

**Current calculation (correct):**
- **Implicit items (12):** 7 Implicit Arguments + 3 Methods (implicit) + 2 Protocols (implicit)
- **Explicit items (100):** 33E + 46C + 2RD + 6M + 13P
- **Transparency:** 100/112 = 89%

### 3. Documentation Gap Identified

**Schema ✅ Conceptually correct:**
- Implicit Arguments defined as "unstated assumptions, logical implications, or bridging claims" (schema line 598)
- `verbatim_quote: null` because not explicitly stated (schema lines 714-717)
- RDMAP items have `design_status`, `method_status`, `protocol_status` (explicit/implicit)
- Implicit RDMAP items require `implicit_metadata.transparency_gap` field

**Prompts ✅ Conceptually correct:**
- Systematic extraction of Implicit Arguments as reasoning gaps
- RDMAP items marked explicit/implicit based on documentation
- "Transparency gaps" terminology used throughout

**❌ Missing from documentation:**
- Formal specification of transparency calculation methodology
- Explicit statement that Implicit Arguments count as implicit items
- Formula: `(explicit items) / (total items) × 100`
- Guidance on category-specific breakdowns

---

## Recommended Actions (Deferred to Assessment Phase)

### 1. Add to Pass 5 Validation Prompt

Add section requiring transparency calculation:

```markdown
## Transparency Calculation

Calculate transparency metrics for final summary:

**Overall transparency:**
- Count explicit items: Evidence + Claims + RD (explicit) + M (explicit) + P (explicit)
- Count implicit items: Implicit Arguments + RD (implicit) + M (implicit) + P (implicit)
- Formula: explicit_count / (explicit_count + implicit_count) × 100

**Category breakdown:**
- Methods transparency: explicit_methods / total_methods × 100
- Protocols transparency: explicit_protocols / total_protocols × 100
- Overall RDMAP transparency: explicit_rdmap / total_rdmap × 100

**Note:** Evidence and Claims are always explicit (have verbatim quotes). Implicit Arguments are always implicit (by definition).
```

### 2. Create Skill Reference Document

Add `references/assessment/transparency-metrics.md`:

**Content outline:**
- Definition: Transparency = proportion of research process explicitly documented
- Conceptual basis: Assessing papers as published
- Calculation methodology
- Interpretation guidelines
- Category-specific metrics
- Relationship to replicability and credibility assessment

### 3. Update Schema Documentation

Add comment block to schema explaining transparency implications:

```json
"_comment_transparency_assessment": {
  "description": "Implicit Arguments and implicit RDMAP items represent transparency gaps",
  "calculation": "transparency_percent = explicit_items / total_items × 100",
  "implicit_items": "Implicit Arguments + RD(implicit) + M(implicit) + P(implicit)",
  "explicit_items": "Evidence + Claims + RD(explicit) + M(explicit) + P(explicit)"
}
```

---

## Current Behavior

The transparency metric **is being calculated correctly** in practice (as seen in Sobotkova extraction), but the methodology is not formally documented. This works through implicit understanding but should be codified for:

1. Consistency across extractions
2. Reproducibility of assessment
3. Training new users/models
4. Methodological transparency in our own work

---

## Next Steps

**When beginning assessment phase:**
1. Review this document
2. Implement documentation updates (Pass 5 prompt, skill reference, schema comments)
3. Validate transparency calculations across existing extractions
4. Integrate transparency metrics into formal assessment framework

---

## Related Files

- `extraction-system/prompts/05-rdmap_pass3_prompt.md` (validation prompt)
- `extraction-system/schema/extraction_schema.json`
- `.claude/skills/research-assessor/SKILL.md`
- `outputs/sobotkova-et-al-2023/summary.md` (transparency metric example)

---

**Priority:** Medium (works correctly in practice, but needs formal documentation)
**Complexity:** Low (add documentation, no schema/logic changes needed)
**Impact:** High (core metric for assessment phase)
