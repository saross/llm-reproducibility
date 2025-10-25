# Diagnosis: Why CC Found 0 Implicit Arguments (But 4 Implicit Protocols)

**Date:** 2025-10-25
**Investigation:** Root cause analysis for CC missing implicit arguments while successfully finding implicit protocols
**Context:** Sobotkova et al. 2023 extraction - Chatbot found 10 implicit arguments, CC found 0

---

## Executive Summary

**Finding:** The prompts and skill CLEARLY specify implicit argument extraction, yet CC extracted 0 implicit arguments while the chatbot extracted 10 from the same paper.

**Root Cause:** NOT a prompt/skill issue (guidance is adequate) - appears to be **workflow execution issue**:
1. CC may not have actively looked for implicit arguments during Pass 1
2. No evidence in logs of systematic implicit argument review
3. User asked "were there any implicit claims?" and CC answered "no" without re-checking

**Paradox:** CC successfully found 4 implicit protocols (undocumented procedures), demonstrating capability to identify implicit content. Why the difference?

**Hypothesis:** Implicit protocols are easier to spot (mentioned in Results, not Methods = implicit), while implicit arguments require deeper inferential analysis that may not have happened during section-by-section extraction.

---

## Investigation Findings

### 1. Skill Definition Review

**File:** `.claude/skills/research-assessor/SKILL.md`

**Findings:**
- Line 15: Skill description mentions "Extract observations, measurements, claims, and implicit arguments"
- Line 137: "Claims/Evidence passes: Touch evidence, claims, implicit_arguments arrays ONLY"
- **Assessment:** Skill acknowledges implicit arguments exist, but provides MINIMAL guidance

**Gap:** Skill does not emphasize implicit arguments or provide decision frameworks for them (unlike extensive RDMAP guidance)

---

### 2. Prompt Review

**File:** `extraction-system/prompts/01-claims-evidence_pass1_prompt.md`

**Findings - Implicit arguments ARE specified:**

**Line 12:** "Extract evidence, claims, and implicit arguments from a research paper section"

**Lines 162-184:** Full section on "Implicit Arguments (HIGH-PRIORITY claims only)"

**Four types defined:**
1. Logical Implications - Unstated steps in reasoning chain
2. Unstated Assumptions - Prerequisites assumed without acknowledgment
3. Bridging Claims - Missing links between evidence and conclusions
4. Disciplinary Assumptions - Field-specific taken-for-granted knowledge

**Lines 226-230:** Workflow step 3: "Check for Implicit Arguments (high-priority claims only)"
- Questions provided:
  - "What logical implications are unstated?"
  - "What assumptions must be true?"
  - "Are there bridging claims missing?"
  - "What disciplinary assumptions frame the argument?"

**Line 290:** Checklist item: "All implicit arguments have trigger_text, trigger_locations, inference_reasoning"

**Assessment:** Prompt is COMPREHENSIVE and CLEAR about implicit arguments

---

### 3. Prompt Comparison: Claims vs RDMAP Implicit Items

**Pass 1 Claims (01-claims-evidence_pass1_prompt.md):**
- Section 4 covers implicit arguments
- Instructions: "Extract implicit arguments ONLY for core and key intermediate claims"
- Workflow step 3: "Check for Implicit Arguments"
- Restriction: HIGH-PRIORITY claims only

**Pass 1 RDMAP (03-rdmap_pass1_prompt.md):**
- Extensive guidance on explicit vs implicit status
- Decision tree at lines 82-83:
  ```
  ├─ YES → Status = "implicit", extract with trigger_text
  └─ NO → DO NOT EXTRACT (absent, not implicit)
  ```
- Lines 107-110: THREE checklist items for implicit RDMAP
- Line 86: "Basis classification for implicit RDMAP"

**KEY DIFFERENCE:**
- **RDMAP implicit detection:** Procedural test ("Is it mentioned but not described in Methods?")
- **Arguments implicit detection:** Inferential analysis ("What assumptions enable this claim?")

**Hypothesis:** Procedural tests are easier to apply systematically during extraction than inferential analysis.

---

### 4. Workflow Review

**File:** `input/WORKFLOW.md`

**Findings - Implicit arguments mentioned:**

**Line 15:** "Populates: evidence, claims, implicit_arguments"

**Lines 140-143:** Pass 2 guidance mentions implicit arguments
- "Add missing implicit generalizations"
- Pass 2 may identify implicit arguments missed in Pass 1

**Assessment:** Workflow acknowledges implicit arguments but provides MINIMAL emphasis or process guidance

**Gap:** No specific step like "After extracting claims, systematically review for implicit arguments"

---

### 5. CC Interaction Log Review

**File:** `archive/cc-interactions/2025-10-25-a.txt` (Pass 1 extraction)

**Search results:**
- "implicit_arguments": [] appears multiple times in JSON templates
- NO evidence of active implicit argument extraction during Pass 1
- NO mentions like "checking for implicit arguments" or "no implicit arguments found"

**File:** `archive/cc-interactions/2025-10-25-b.txt` (continued extraction + user question)

**Critical exchange (lines 257-296):**

**User (line 257):** "Can you tell me, were there any implicit claims?"

**CC (line 259):** "Looking at the extraction results, no, there were no implicit arguments extracted."

**CC explained (lines 265-296):**
- What WAS extracted as implicit: 5 implicit RDMAP items (RD002, M001, P009, P010, P011)
- What implicit arguments WOULD BE: Unstated assumptions, implicit inferential steps, bridging claims
- Example provided: "Since crowdsourcing worked for burial mounds..."
- Why no implicit arguments: "Paper is unusually explicit in its reasoning... methodological choices all have explicit justification"

**PROBLEM:** CC answered based on extraction results WITHOUT actively re-reviewing the paper for implicit arguments

**No evidence CC performed systematic implicit argument review during OR after Pass 1**

---

### 6. Why Implicit Protocols Succeeded But Implicit Arguments Failed

**CC successfully identified 4 implicit protocols:**
1. P009: Volunteer training (mentioned "minutes of training" but no protocol documented)
2. P010: GPS coordinate extraction automation (mentioned in Results, not Methods)
3. P011: Performance mitigation (export/reset when degraded - applied but undocumented)
4. P012: Data correction protocol (spatial omission fixes - mentioned but not described)

**Why these were caught:**
- **Procedural test:** "Is this procedure mentioned somewhere but not documented in Methods?"
- **Location-based:** Results section mentions procedure → implicit
- **Observable gap:** Paper says "we did X" but Methods doesn't describe how

**Why implicit arguments were missed:**
- **Requires inference:** "What assumptions must be true for this claim to hold?"
- **Not location-based:** Could be anywhere in the reasoning chain
- **Abstract analysis:** Not directly observable from text gaps

**Pattern:** CC successfully applied **procedural tests** but may not have applied **inferential analysis**

---

### 7. Chatbot's 10 Implicit Arguments (What CC Missed)

**For reference, chatbot extracted:**

1. **IA001:** Feature density affects digitization rates → unstated assumption
2. **IA002:** Staff time is appropriate optimization criterion → disciplinary assumption
3. **IA003:** Volunteer retention differs (desktop vs mobile) → comparative assumption
4. **IA004:** Linear extrapolation from measurements valid → scaling assumption
5. **IA005:** ML expertise unavailable to small HASS projects → barrier assumption
6. **IA006:** Urban Occupations is reasonable ML benchmark → comparability assumption
7. **IA007:** 6% error rate is acceptable quality → threshold assumption
8. **IA008:** Volunteer satisfaction matters → evaluation assumption
9. **IA009:** In-field time more constrained → temporal assumption
10. **IA010:** ML requires manual training data → approach assumption

**What these have in common:**
- All are **assumptions enabling claims**, not directly stated
- All require **inferential reasoning** to identify
- All are **disciplinary norms** or **unstated premises**
- None are simple "mentioned but not documented" gaps

**These SHOULD have been caught by CC per prompt lines 162-184 and 226-230**

---

## Root Cause Analysis

### What Went Wrong?

**NOT a documentation issue:**
- ✅ Prompt 01 clearly specifies implicit argument extraction
- ✅ Four types defined with examples
- ✅ Workflow step included
- ✅ Checklist item present

**LIKELY an execution issue:**
- ❌ No evidence CC performed systematic implicit argument review during Pass 1
- ❌ Section-by-section extraction may prioritize explicit content extraction over inferential analysis
- ❌ User question answered from extraction results, not from paper re-review
- ❌ Implicit arguments treated as optional ("HIGH-PRIORITY claims only") vs RDMAP implicit treated as mandatory check

### Why the Differential Success?

**Implicit Protocols (4 found):**
- Procedural, observable test: "mentioned but not documented"
- Location-based: Results mentions → Methods doesn't → implicit
- Concrete gap: specific procedure named but not described
- **Easy to spot during section-by-section extraction**

**Implicit Arguments (0 found):**
- Inferential, analytical task: "what assumptions enable this claim?"
- Not location-based: requires understanding full argument structure
- Abstract gap: premises, not procedures
- **Hard to spot during section-by-section extraction without dedicated focus**

---

## Hypotheses (Ranked by Likelihood)

### Hypothesis 1: Section-by-Section Extraction Pattern ⭐⭐⭐⭐⭐ (MOST LIKELY)

**Theory:** Section-by-section extraction optimizes for explicit content extraction within each section. Implicit arguments often span sections or require whole-paper argument structure understanding.

**Evidence:**
- CC extracted section-by-section (Abstract+Intro, Methods, Results, Discussion)
- Implicit protocols found in section-by-section mode (local text gaps: "mentioned here but not described in Methods")
- Implicit arguments require cross-section reasoning (e.g., Discussion claim depends on unstated Introduction assumption)
- Chatbot may have done more holistic/synthetic extraction allowing cross-cutting inference

**If true:** Implicit argument extraction needs dedicated pass after full-paper extraction complete

---

### Hypothesis 2: "HIGH-PRIORITY only" Weakened Emphasis ⭐⭐⭐⭐ (LIKELY)

**Theory:** Prompt restricts implicit arguments to "high-priority claims only" which may have been interpreted as optional.

**Evidence:**
- Line 164: "Extract implicit arguments ONLY for core and key intermediate claims"
- Line 226: "(high-priority claims only)" in parentheses
- RDMAP implicit detection has no such restriction - ALL mentioned procedures checked
- CC may have de-prioritized implicit argument search

**If true:** Remove "only" restriction or add emphasis "REQUIRED for core claims"

---

### Hypothesis 3: Timing in Workflow ⭐⭐⭐ (POSSIBLE)

**Theory:** Implicit arguments should be extracted AFTER claims rationalization (Pass 2) when core claims are finalized, not during Pass 1.

**Evidence:**
- Pass 1 liberal extraction may not yet know which claims are "core"
- Pass 2 prompt (lines 310-320) mentions "Pass 2 may identify implicit arguments missed in Pass 1"
- But CC didn't add any in Pass 2 either

**If true:** Make Pass 2 the primary implicit argument extraction point

---

### Hypothesis 4: Skill Persistent After Auto-Compact ⭐⭐ (LESS LIKELY)

**Theory:** Auto-compact may have dropped skill context mid-extraction.

**Evidence:**
- User asked to check if skill was loaded throughout extraction
- Would explain gap IF skill was lost
- BUT: CC successfully extracted implicit protocols AFTER potential compact
- Suggests skill remained active

**Check needed:** Review interaction logs for skill re-loading after compact

**If false:** Rules out this hypothesis

---

### Hypothesis 5: Cognitive Load During Extraction ⭐ (UNLIKELY)

**Theory:** CC was focused on comprehensive evidence/claims extraction and didn't have capacity for inferential analysis.

**Evidence:**
- CC extracted 36 evidence, 31 claims (very comprehensive)
- Implicit protocols are simpler checks, lower cognitive load
- Implicit arguments require deeper reasoning

**If true:** Reduce cognitive load by separating passes more clearly

---

## Recommendations

### Immediate Actions (Before Next Extraction)

**1. Add Dedicated Implicit Argument Review Step**

**Where:** After Pass 2 (claims rationalization) complete

**Why:**
- Core claims are finalized
- Full-paper argument structure visible
- Can systematically review each core claim

**How:** Either:
- **Option A:** Add Pass 2.5 - Implicit Argument Extraction (dedicated pass)
- **Option B:** Expand Pass 2 to require explicit "Step 5: Review core claims for implicit arguments"

**2. Strengthen Prompt Emphasis**

**Changes to `01-claims-evidence_pass1_prompt.md`:**
- Line 164: Change "ONLY for core and key intermediate claims" to "REQUIRED for all core claims, recommended for key intermediate claims"
- Add checklist at end: "[ ] Systematically reviewed all core claims for implicit arguments (Types 1-4)"
- Add example: Show one of chatbot's 10 implicit arguments as worked example

**Changes to `02-claims-evidence_pass2_prompt.md`:**
- Lines 310-320: Strengthen implicit argument review requirement
- Add: "After rationalization, systematically review each CORE claim and ask: What assumptions must be true? What inferential steps are unstated?"

**3. Update WORKFLOW.md**

**Add section:**
```markdown
### Implicit Argument Extraction Guidance

**When:** After Pass 2 claims rationalization (or dedicated Pass 2.5)

**Process:**
1. Identify all CORE claims (claim_role = "core")
2. For each core claim, systematically ask:
   - Type 1: What logical implications are unstated?
   - Type 2: What assumptions must be true?
   - Type 3: Are there bridging claims missing?
   - Type 4: What disciplinary assumptions frame this?
3. Extract as implicit_argument objects with trigger_text from passages implying the assumption

**Goal:** 8-15 implicit arguments for typical paper (10-15% of claims count)
```

---

### Testing & Validation

**1. Manual Test on Sobotkova**

**Task:** Manually extract implicit arguments using chatbot's 10 as reference
- Read Discussion section claims
- Systematically apply 4-type framework to each core claim
- See if CC can identify similar implicit arguments when explicitly prompted

**Goal:** Verify capability exists, just needs activation

**2. Prompt A/B Test**

**Test:** Try both options on same paper section:
- **Version A:** Current prompt (high-priority only)
- **Version B:** Strengthened prompt (required for core)

**Measure:** Count of implicit arguments extracted

**3. Workflow Position Test**

**Test:** Try implicit extraction at different points:
- **Position A:** During Pass 1 (current)
- **Position B:** During Pass 2 (after rationalization)
- **Position C:** Dedicated Pass 2.5 (after full extraction)

**Measure:** Quality and count of implicit arguments

---

## Open Questions

1. **Was the skill actually loaded throughout extraction after auto-compact?**
   - Check logs for skill re-invocation
   - Verify skill context persisted

2. **Did chatbot use different workflow structure?**
   - When did chatbot extract implicit arguments?
   - Dedicated pass or integrated?

3. **What if we explicitly prompt for each of chatbot's 10 implicit arguments?**
   - Can CC identify them when specifically asked?
   - Tests capability vs workflow issue

4. **Would whole-paper review help vs section-by-section?**
   - Try Pass 2.5 with entire paper re-read for implicit arguments
   - Compare to section-by-section results

---

## Conclusion

**Primary Diagnosis:** Workflow execution issue, not prompt/skill deficiency

**Evidence:**
- Prompts clearly specify implicit argument extraction
- CC successfully extracted implicit protocols (demonstrates capability)
- No evidence of systematic implicit argument review in logs
- Section-by-section extraction pattern may not suit inferential analysis

**Recommended Fix:** Add dedicated implicit argument review step AFTER Pass 2 claims rationalization, with strengthened emphasis and systematic 4-type framework application to all core claims.

**Confidence:** HIGH - This is a process gap, not a capability gap.

**Next Steps:**
1. Manual validation test on Sobotkova (can CC find chatbot's 10 with explicit prompting?)
2. Implement Pass 2.5 implicit argument extraction in WORKFLOW.md
3. Strengthen Pass 1 & 2 prompts with emphasis and examples
4. Test on new paper with updated workflow

---

**Document Status:** Diagnosis complete, ready for implementation planning
**Owner:** Shawn + CC
**Next Action:** Decide between Pass 2.5 vs expanded Pass 2 approach
