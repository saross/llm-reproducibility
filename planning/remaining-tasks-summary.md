# Remaining Tasks: Implicit RDMAP & Comprehensive Extraction

**Date:** 2025-10-28
**Context:** Post-split-architecture implementation
**Status:** Phase 1 complete, Phases 2-3 pending

---

## Overview

The split architecture (5→6 passes) addressed Phase 1 of the implicit RDMAP extraction fixes through a **different architectural approach** than originally planned:

**Original Plan:** Integrate implicit RDMAP into Prompt 03 with Phase A/B structure (840 lines)
**Implemented:** Split into dedicated Prompt 04 (368 + 273 lines)

**Rationale:** Cognitive model separation provides higher reliability than integrated approach.

---

## A. Implicit RDMAP Extraction - Remaining Work

### ✅ Phase 1: Immediate Fixes (COMPLETE via Split Architecture)

The split architecture implementation accomplishes Phase 1 goals differently:

**Originally Planned (Integrated):**
- [x] Fix 1: Phase A/B structure in single prompt
- [x] Fix 2: Iteration instructions
- [x] Fix 5: HIGH-PRIORITY elevation
- [x] Fix 8: Worked example

**Actually Implemented (Split):**
- [x] Prompt 03: Explicit RDMAP only (368 lines) with clear focus
- [x] Prompt 04: Implicit RDMAP only (273 lines) with 4-pattern scanning
- [x] Natural quality gate between explicit and implicit
- [x] Dedicated singular focus per prompt (reduces cognitive load)

**Status:** ✅ Complete - Ready for testing

---

### 🔧 Phase 2: Medium-Term Improvements (PENDING)

These improvements strengthen implicit RDMAP extraction quality and should be implemented in **Prompt 04** (implicit RDMAP prompt):

#### Fix 3: Replace Checkbox with Quality Gate

**File:** `extraction-system/prompts/04-rdmap_pass1b_implicit_prompt.md`
**Location:** Quality Checkpoints section (currently lines 250-262)

**Current:**
```markdown
- [ ] Completed 4-pattern scan for research designs across ALL major sections
- [ ] Completed 4-pattern scan for methods across ALL major sections
- [ ] Completed 4-pattern scan for protocols across ALL major sections
```

**Enhance to:**
```markdown
- [ ] **Systematic implicit RDMAP scan completed for EACH major section (Abstract, Intro, Methods, Results, Discussion)**
- [ ] **For each section, documented implicit scan methodology in extraction_notes OR implicit items found**
- [ ] **If zero implicit RDMAP items across all sections: extraction_notes explains why** (e.g., "Exceptionally well-documented Methods section...")
```

**Why:** Requires evidence of scanning, not just field population.

**Estimated time:** 30 minutes
**Priority:** Medium (strengthens validation)

---

#### Fix 4: Reframe from Transparency to Content

**File:** `extraction-system/prompts/04-rdmap_pass1b_implicit_prompt.md`
**Location:** Section "Why This Pass Matters" (lines 35-45)

**Current framing:**
- Focuses on "transparency gaps" and "assessment-critical"
- May position implicit extraction as secondary metadata

**Reframe to:**
```markdown
**Implicit RDMAP extraction is PRIMARY CONTENT, not optional metadata.**

Many papers mention procedures without documenting them, or imply methods through results. These undocumented procedures are as important as explicit RDMAP because:
- They represent actual work performed
- They affect reproducibility (procedures exist but can't be replicated)
- They impact credibility (decisions affecting results are undocumented)
- They reveal what methods documentation should contain

Extract implicit RDMAP items systematically. Do not skip implicit scanning because Methods section exists.
```

**Why:** Positions implicit RDMAP as equally important content, not "gap documentation"

**Estimated time:** 30 minutes
**Priority:** Medium (improves executor mindset)

---

#### Fix 6: Move Recognition Patterns to Main Prompt

**File:** `extraction-system/prompts/04-rdmap_pass1b_implicit_prompt.md`
**Location:** Currently references external patterns (line 260: "See references/extraction-fundamentals.md")

**Current:** External reference only
**Proposed:** Embed concise patterns directly in prompt

**Add inline patterns:**
```markdown
### Quick Reference: 4-Pattern Recognition

**Pattern 1 - Mentioned Procedure:**
- Verbs without procedures: "cleaned", "validated", "checked", "assigned"
- Example: "Data were cleaned" → implicit cleaning method
- Basis: mentioned_undocumented

**Pattern 2 - Effects Implying Causes:**
- Thresholds detected → monitoring, accuracy metrics → validation
- Example: "Performance degraded at 2,500 records" → monitoring protocol
- Basis: inferred_from_results

**Pattern 3 - Mentions Without Descriptions:**
- "GPS used" (no specs), "maps assigned" (no allocation method)
- Example: "Students assigned specific tiles" → assignment protocol
- Basis: mentioned_undocumented

**Pattern 4 - Strategic Positioning:**
- Paper positions relative to alternatives without design statement
- Example: Compares to ML throughout but doesn't state as design goal
- Basis: inferred_from_results

For detailed examples → `references/extraction-fundamentals.md`
```

**Why:** Reduces cognitive load (no file switching during execution)

**Estimated time:** 45 minutes
**Priority:** Medium (improves usability)

---

### 🔮 Phase 3: Long-Term Enhancements (DEFERRED)

#### Fix 7: Add Mid-Section Checkpoints

**File:** Potentially both Prompts 03 and 04
**Purpose:** Process monitoring with ratio checks

**Proposed checkpoint (after each section group):**
```markdown
### Mid-Section Checkpoint

**Count current RDMAP items:**
```bash
jq '{designs: (.research_designs|length), methods: (.methods|length), protocols: (.protocols|length), explicit: [.research_designs[], .methods[], .protocols[]] | map(select(.*_status == "explicit")) | length, implicit: [.research_designs[], .methods[], .protocols[]] | map(select(.*_status == "implicit")) | length}' extraction.json
```

**Expected ratios at this checkpoint:**
- Implicit RDMAP: Should be accumulating (not zero after Results/Discussion sections)
- Protocols > Methods > Designs (typical hierarchy)

**If implicit items = 0 after Results section:**
- Re-scan Results for undocumented procedures mentioned
- Check for verb phrases without procedures ("cleaned", "validated", "assigned")
- Document why zero is accurate in extraction_notes

Continue to next section...
```

**Why:** Self-correction during execution, prevents zero-implicit completion

**Estimated time:** 1-2 hours (requires testing optimal placement)
**Priority:** Low (architectural split may make this unnecessary)
**Note:** May not be needed with split architecture - implicit pass is shorter and more focused

---

## B. Comprehensive Extraction Reliability - Remaining Work

**Source:** `planning/liberal-extraction-execution-guide.md` and `planning/future-workflow-improvements.md`

### 🔧 High Priority: Systematic Process Indicators

These improvements make comprehensive extraction more reliable across varied papers.

#### Improvement 1: Make Fundamentals Reading Mandatory

**Files:** Prompts 01 and 03 (liberal extraction passes)
**Priority:** HIGH
**Impact:** Prevents 40-50% of sourcing failures

**Add to start of Pass 1 (Claims/Evidence) and Pass 3 (RDMAP Explicit):**
```markdown
## STEP 0: MANDATORY Pre-Extraction (DO THIS FIRST)

Before extraction begins, you MUST:

1. **Read extraction fundamentals:**
   - File: `references/extraction-fundamentals.md`
   - Focus: Internalise the sourcing test: "Can I point to exact text?"

2. **Acknowledge understanding:**
   - State: "I have read extraction fundamentals and understand the sourcing discipline"

3. **Only then proceed to extraction**

**WITHOUT completing Step 0, extraction will fail sourcing requirements.**

---
```

**Why:** Forces fundamentals reading before extraction, establishes sourcing discipline early

**Estimated time:** 30 minutes (both prompts)
**Priority:** HIGH

---

#### Improvement 2: Strengthen Liberal Extraction Mental Model

**Files:** Prompts 01 and 03
**Priority:** MEDIUM
**Impact:** Reduces over-consolidation and missed items

**Add early in Extraction Workflow section:**
```markdown
## Liberal Extraction Mental Model

**Pass 1/3 job:** CAPTURE (comprehensively)
**Pass 2/5 job:** CONSOLIDATE (rationally)

**Active rules during liberal passes:**
✓ When uncertain: EXTRACT IT
✓ When granular: KEEP IT SEPARATE
✓ When related items: DON'T CONSOLIDATE YET

**Never think during liberal passes:**
✗ "This seems too detailed for final output"
✗ "These should probably merge"
✗ "I'm over-extracting"

**Remember:** Pass 2/5 can merge. Pass 1/3 cannot recover missed items.

---
```

**Why:** Sets correct mental model (comprehensive > precise during liberal passes)

**Estimated time:** 30 minutes (both prompts)
**Priority:** MEDIUM

---

#### Improvement 3: Emphasise Relationship Mapping During Extraction

**Files:** Prompts 01 and 03
**Priority:** MEDIUM
**Impact:** Improves extraction quality and coverage

**Add to Extraction Workflow section:**
```markdown
### Relationship Mapping Discipline

**For EACH item, immediately ask:**
- Evidence: "What claims does this support?" → `supports_claims`
- Claims: "What evidence supports this?" → `supported_by_evidence`
- RDMAP: "Which designs/methods does this implement?" → cross-references

**Why map relationships during extraction (not after):**
- Understand each item's role in argumentation
- Notice gaps in support (missing evidence/protocols)
- Prepare for efficient Pass 2/5 consolidation

**Do NOT defer relationship mapping to Pass 2/5.** Map as you extract.

---
```

**Why:** Forces understanding of argumentative structure, improves item selection

**Estimated time:** 45 minutes (both prompts)
**Priority:** MEDIUM

---

#### Improvement 4: Add Verbatim Quote Quality Standards

**File:** Prompt 01 (Claims/Evidence)
**Priority:** MEDIUM
**Impact:** Reduces validation failures

**Enhance verbatim quote section with self-check:**
```markdown
### Verbatim Quote Self-Check (Before Writing to JSON)

For EACH quote you extract, ask:

1. **"Can I find this EXACT text in the paper with simple search?"**
   - If NO → Fix quote or mark as implicit

2. **"Is this a complete sentence?"**
   - If NO → Expand to grammatical unit

3. **"Did I copy-paste or reconstruct from memory?"**
   - If reconstructed → Re-read paper and copy exact text

4. **"Does this come from single location or synthesised?"**
   - If synthesised → Split into multiple items

**Quality target:** >95% of quotes pass Pass 6 verification
```

**Why:** Prevents verbatim quote failures at validation stage

**Estimated time:** 30 minutes
**Priority:** MEDIUM

---

#### Improvement 5: Add Scope Management Guidance

**Files:** Prompts 01 and 03
**Priority:** LOW
**Impact:** Prevents over-extraction of literature review content

**Add early warning:**
```markdown
### Scope: Extract THIS Paper's Work Only

**Extract:**
✓ Current study's evidence, claims, methods
✓ Current study's interpretation of their results
✓ Current study's methodological choices

**Do NOT extract:**
✗ Literature review summaries (what prior papers found)
✗ Citations to others' claims (unless adopted as current paper's claim)
✗ Prior papers' methodologies (unless current paper uses them)

**Test:** Does this describe/support the CURRENT paper's work?
- If YES → Extract
- If NO → It's background, skip

**Exception:** Extract prior work if current paper builds directly on it (e.g., "We adopt Smith's framework" → extract framework as current paper's design decision).
```

**Why:** Prevents literature review over-extraction

**Estimated time:** 30 minutes (both prompts)
**Priority:** LOW (hasn't been major issue)

---

## Implementation Roadmap

### Next Immediate Steps (Before Testing)

**Option A: Test split architecture first (recommended)**
1. ✅ Split architecture complete
2. ⏭️ Test Prompt 03 + 04 on Sobotkova paper
3. ⏭️ Validate implicit RDMAP items > 0
4. ⏭️ Then implement Phase 2 improvements if needed

**Option B: Add Phase 2 improvements before testing**
1. ✅ Split architecture complete
2. ⏭️ Implement Fixes 3, 4, 6 in Prompt 04
3. ⏭️ Test on Sobotkova paper
4. ⏭️ Validate improvements

**Recommendation:** Option A - Test split architecture first to establish baseline, then add improvements if issues remain.

---

### After Split Architecture Validation

**Phase 2 Implicit RDMAP Improvements (1.5-2 hours):**
1. Fix 3: Quality gates in Prompt 04
2. Fix 4: Reframe to content focus in Prompt 04
3. Fix 6: Embed patterns in Prompt 04

**Comprehensive Extraction Improvements (2-3 hours):**
1. Improvement 1: Mandatory fundamentals (Prompts 01, 03) - HIGH
2. Improvement 2: Liberal mental model (Prompts 01, 03) - MEDIUM
3. Improvement 3: Relationship mapping (Prompts 01, 03) - MEDIUM
4. Improvement 4: Quote quality (Prompt 01) - MEDIUM
5. Improvement 5: Scope management (Prompts 01, 03) - LOW

**Total estimated time:** 3.5-5 hours

---

### Long-Term Considerations

**Fix 7 (Mid-section checkpoints):**
- May not be needed with split architecture
- Deferred until after testing Phase 2 improvements
- Re-evaluate if implicit extraction shows inconsistency

**Additional monitoring:**
- Track implicit RDMAP extraction across multiple papers
- Monitor comprehensive extraction consistency
- Validate improvements work for varied paper types

---

## Success Metrics

### Implicit RDMAP Extraction

**Pass criteria:**
- [ ] Implicit RDMAP items > 0 for typical empirical papers
- [ ] Implicit ratio: 20-40% of total RDMAP items
- [ ] extraction_notes documents systematic scanning methodology
- [ ] All 4 recognition patterns represented in findings
- [ ] Complete sourcing (trigger_text, implicit_metadata)

### Comprehensive Extraction

**Pass criteria:**
- [ ] Pass 1 extracts 40-50% more items than Pass 2 (over-capture working)
- [ ] Evidence:Claims ratio typically 1.0-2.0 for empirical papers
- [ ] RDMAP hierarchy shows Methods > Designs, Protocols > Methods
- [ ] Zero implicit items accompanied by extraction_notes explanation
- [ ] >95% of verbatim quotes pass Pass 6 verification

---

## Priority Summary

### Critical (Before Production Use)
- [x] Phase 1: Split architecture (COMPLETE)
- [ ] Test split architecture on Sobotkova paper
- [ ] Validate implicit RDMAP extraction works

### High Priority (Next Implementation Cycle)
- [ ] Improvement 1: Mandatory fundamentals reading (Prompts 01, 03)
- [ ] Fix 3: Quality gates in Prompt 04

### Medium Priority (After Testing Validates Need)
- [ ] Fix 4: Reframe to content focus (Prompt 04)
- [ ] Fix 6: Embed patterns (Prompt 04)
- [ ] Improvement 2: Liberal mental model (Prompts 01, 03)
- [ ] Improvement 3: Relationship mapping (Prompts 01, 03)
- [ ] Improvement 4: Quote quality standards (Prompt 01)

### Low Priority (Deferred)
- [ ] Fix 7: Mid-section checkpoints (may not be needed)
- [ ] Improvement 5: Scope management (Prompts 01, 03)

---

**Version:** 1.0
**Date:** 2025-10-28
**Status:** Planning document
**Next Action:** Test split architecture implementation
