# ARCHIVED: Future Task: Remove Sobotkova-Specific Metrics

**Archive Date:** 2025-10-31
**Original Location:** planning/future-task-remove-sobotkova-specific-metrics.md
**Merged Into:** planning/active-todo-list.md (Section 5: Remove Sobotkova-Specific Metrics)
**Archival Reason:** Task consolidated into active todo list for better tracking

---

**Date Identified**: 2025-10-27
**Priority**: MEDIUM
**Context**: During Phase A + B-1 implementation, identified that some extraction guidance may be calibrated to Sobotkova et al. 2023

---

## Issue

Extraction prompts and/or skill may contain metrics, targets, or patterns based on a single paper (Sobotkova et al. 2023) rather than generalizable across diverse fieldwork-based research.

**User concern**: "There should be nothing *specific* to Sobotkova et al in the prompts or skill. I'm concerned about target metrics for extraction based on this paper."

---

## Known Examples to Audit

### Research Design Count Guidance

**Location**: Prompt 03 (RDMAP Pass 1), likely in quality checklist

**Potential issue**: Guidance like "expect 4-6 Research Designs" may be calibrated to Sobotkova et al. 2023, not generalizable.

**Action needed**:
- Audit all Research Design count guidance
- Replace specific numbers with principles
- E.g., "If <3: review for under-extraction; if >10: review for over-extraction; quality over count"

### Expected Information Patterns

**Location**: Potentially in expected-information.md or prompts

**Potential issue**: Completeness checklists may reflect what Sobotkova et al. 2023 did/didn't document, not general standards.

**Action needed**:
- Verify checklists based on domain standards (TIDieR, CONSORT, etc.), not single paper
- Ensure patterns are generalizable

### Consolidation Targets

**Location**: Pass 2 prompts, quality checklists

**Potential issue**: "Target 15-20% reduction" may be based on Sobotkova over-extraction rate, not universal.

**Action needed**:
- Verify reduction targets are principles-based, not paper-specific
- May need to adjust based on multi-paper testing

### Examples in Reference Files

**Location**: references/ files being created/enhanced

**Potential issue**: Examples drawn only from Sobotkova et al. 2023

**Action needed**:
- When possible, include examples from multiple papers
- Clearly label examples with paper source
- Ensure patterns described are generalizable even if examples from one paper

---

## Audit Locations

**High Priority**:
- [ ] Prompt 03 (RDMAP Pass 1) - Research Design count guidance
- [ ] Prompt 04 (RDMAP Pass 2) - Consolidation targets
- [ ] Prompt 02 (Claims/Evidence Pass 2) - Consolidation targets
- [ ] references/checklists/expected-information.md - Completeness patterns
- [ ] .claude/skills/research-assessor/SKILL.md - Any metrics/targets

**Medium Priority**:
- [ ] Prompt 01 - Evidence/claims extraction targets
- [ ] Prompt 05 - Validation thresholds
- [ ] All new reference files created in Phase A/B - Examples and patterns

---

## Principles for Generalizability

### Replace Specific Numbers with Principles

**Bad** (paper-specific):
- "Expect 4-6 Research Designs per paper"
- "Target 15-20% reduction in Pass 2"

**Good** (principle-based):
- "Quality over count - extract what's genuinely present. If <3: review for under-extraction. If >10: review for over-extraction."
- "Target appropriate granularity - typically 15-20% reduction, but may vary by paper structure"

### Use Multiple Examples

**Bad** (single-source):
- All examples from Sobotkova et al. 2023

**Good** (diverse):
- Examples from multiple papers when possible
- Label example source: "Example from Sobotkova et al. 2023:"
- Explain generalizability: "This pattern applies to..."

### Base Standards on Domain Knowledge

**Bad** (paper-derived):
- Checklist based on what one paper documented

**Good** (standard-derived):
- TIDieR checklist (10 elements, published standard)
- CONSORT-Outcomes (8 elements, published standard)
- Disciplinary norms, not single paper

---

## Implementation Plan (Future)

**When**: After Phase A/B/C implementation complete and multi-paper testing begins

**Approach**:
1. Systematic audit of all locations above
2. Replace specific metrics with principles
3. Add diverse examples where possible
4. Test on 5-10 diverse papers to validate generalizability
5. Refine based on multi-paper results

**Estimated effort**: 3-4 hours audit + 2-3 hours refinement

---

## Notes

- This task deferred until after Phase A/B-1/B-2 implementation
- Multi-paper testing (5-10 papers) will naturally surface paper-specific patterns
- Some calibration to Sobotkova is acceptable during development, but should be validated/refined with diverse papers
- The goal is generalizable frameworks, not Sobotkova-optimised frameworks

---

## Status

**Current**: DEFERRED - noted for future action
**Next**: Will be addressed during/after multi-paper testing phase
