# Extraction Launch Prompt

Begin extraction for next paper in queue:

1. **Check queue:** Read `input/queue.yaml` → identify next paper with `status: pending`
2. **Read workflow:** Read `input/WORKFLOW.md` → understand 7-pass process and planning requirements
3. **Review model plan:** Read `extraction-system/EXTRACTION_PLAN_UNIFIED_MODEL.md` → see planning structure and adaptation guidelines
4. **Invoke skill:** Launch `research-assessor` skill and keep invoked throughout
5. **Create comprehensive plan:** Follow planning checklist in WORKFLOW.md

---

## What to Include in Your Plan

**Mandatory components** (from WORKFLOW.md "Planning Mode Requirements"):
- Skill invocation (research-assessor at Pre-Flight, maintained throughout)
- Section structure with word counts (SAME sections for Pass 1 and Pass 3)
- Explicit chunking examples showing splits
- Liberal over-extraction approach stated (40-50% for Pass 1 and Pass 3)
- Equal attention strategy for Pass 3 (all sections, not just Methods)
- Chunking metadata recording plan

**Adaptation strategy** (from EXTRACTION_PLAN_UNIFIED_MODEL.md):
- Identify paper type (empirical/methodological/multi-proxy/short/long)
- Adapt item count targets
- Adapt section structure
- Adapt timeline estimate

---

## Do NOT

- Stop between passes for confirmation (autonomous execution mode)
- Create prescriptive templates (adapt to paper specifics)
- Guess section structure without examining paper
- Over-focus on Methods section in Pass 3
- Use different section groups for Pass 1 vs Pass 3

---

## Files to Reference

**Core workflow:**
- `input/WORKFLOW.md` - Complete 7-pass workflow with planning requirements

**Planning guidance:**
- `extraction-system/EXTRACTION_PLAN_UNIFIED_MODEL.md` - Flexible planning model with adaptation guidelines

**Queue management:**
- `input/queue.yaml` - Paper queue with status tracking

---

**Version:** 1.0.0 | **Date:** 2025-10-31
**Purpose:** Brief primer for autonomous extraction planning
**Principle:** Point to documentation, don't duplicate it; prime thinking, don't prescribe format
