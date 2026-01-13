# Extraction Launch Prompt

## Session-per-Pass Approach

Extraction is organised into 4 focused sessions:

| Session | Passes | Focus |
|---------|--------|-------|
| **A** | Pre-Flight + Pass 0 + Pass 6 | Metadata + Infrastructure |
| **B** | Pass 1-2 + Phase 2b | Claims/Evidence |
| **C** | Pass 3-5 + Phase 5b | RDMAP |
| **D** | Pass 7 + FAIR | Validation |

## Starting a New Paper (Session A)

1. **Check queue:** Read `input/queue.yaml` → identify next paper with `status: pending`
2. **Read workflow:** Read `input/workflow.md` → understand session structure
3. **Invoke skill:** Launch `research-assessor` skill
4. **Run Session A:** Pre-Flight → Pass 0 → Pass 6 → Handoff summary

## Continuing an Existing Paper (Sessions B/C/D)

1. **Read extraction.json:** Check `extraction_notes.passes_completed`
2. **Read queue.yaml:** Verify paper status and checkpoint
3. **Read paper text:** For extraction passes (B/C)
4. **Run next session:** Complete all passes in session → Handoff summary

---

## Session Execution Rules

**Within each session:**
- Work autonomously without stopping
- Complete all passes in the session
- Save to extraction.json after each pass

**At session end:**
- Provide handoff summary with counts
- Stop and wait for next session to be initiated

---

## Planning (Session B/C)

**Mandatory components** (from WORKFLOW.md):
- Section structure with word counts (SAME sections for Pass 1 and Pass 3)
- Liberal over-extraction approach (40-50%)
- Equal attention to all sections in Pass 3 (not just Methods)

**Adaptation** (from `extraction-system/extraction-plan-unified-model.md`):
- Identify paper type (empirical/methodological/multi-proxy)
- Adapt item count targets accordingly

---

## Do NOT

- Run all 8 passes in one session (use session-per-pass)
- Stop within a session for confirmation
- Over-focus on Methods section in Pass 3
- Use different section groups for Pass 1 vs Pass 3

---

## Files to Reference

- `input/workflow.md` - Complete workflow with session boundaries
- `extraction-system/extraction-plan-unified-model.md` - Planning guidelines
- `input/queue.yaml` - Paper queue with status tracking

---

**Version:** 2.0.0 | **Date:** 2026-01-13
**Purpose:** Brief primer for session-per-pass extraction
**Principle:** 4 focused sessions produce higher quality than single autonomous run
