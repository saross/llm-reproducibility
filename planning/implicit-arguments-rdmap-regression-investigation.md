# Implicit Arguments & RDMAP Regression Investigation
## Debugging Session 2025-10-26

**Status:** ROOT CAUSE IDENTIFIED - Ready for implementation
**Next Actions:** Fix file operations bug, test restoration
**Priority:** P0 - Critical (data loss in production runs)

---

## EXECUTIVE SUMMARY

### What We Found

**Four regressions identified (not two):**
1. ✅ Research Design granularity: 5→2→6 (FIXED in current)
2. ✅ Protocol-Method linking: 100%→0%→100% (FIXED in current)
3. ❌ Implicit Arguments: 7→0 (NOT FIXED - **file operation bug**)
4. ❌ Implicit RDMAP items: 3→0 (NOT FIXED - needs investigation)

**Root cause for #3:** File management error during Pass 1
- Current run successfully extracted 4 IAs from Abstract + Introduction
- Write operation with partial Read (14 lines) overwrote entire file
- Lost all claims + IAs (367 line deletion)
- Never recovered

**NOT caused by:**
- ❌ Workflow complexity (chatbot + RUN-02 proved coexistence works)
- ❌ Missing prompts (prompts already improved per chatbot recommendations)
- ❌ Human guidance (chatbot was single-shot, no corrections)
- ❌ Removed features (nothing changed between RUN-02 and current)

**Caused by:**
- ✅ Single file operation bug: `Read(file, limit=14)` → `Write(file)` = data loss

---

## DETAILED FINDINGS

### Cross-Run Comparison

| Run | Evidence | Claims | **IAs** | **RD** | M | P | **Impl RDMAP** | Notes |
|-----|----------|--------|---------|--------|---|---|----------------|-------|
| Chatbot | 46 | 60 | **8-10** ✓ | 5 ✓ | 7 | 13 | N/A | All features working |
| RUN-01 | 36 | 31 | 0 | 2 | 6 | 10 | 4 items | v2.5 baseline |
| RUN-02 | 33 | 46 | **7** ✓ | 2 | 9 | 15 | **3 items** | IAs working |
| Current | 63 | 26 | **0** ❌ | 6 ✓ | 6 | 8 | **0 items** ❌ | File bug |

### Target Achievement Status

| Metric | Target | Chatbot | RUN-02 | Current | Status |
|--------|--------|---------|--------|---------|---------|
| Implicit Arguments | 8-12 | ✓ 8-10 | ✓ 7 | ❌ 0 | **REGRESSION** |
| Research Designs | 3-6 | ✓ 5 | ❌ 2 | ✓ 6 | **FIXED** |
| Protocol→Method Link | 100% | ✓ 100% | ❌ 0% | ✓ 100% | **FIXED** |
| Sourcing Quality | 100% | ❌ ~10% | ✓ 100% | ✓ 100% | MAINTAINED |
| **TOTAL** | 4/4 | 3/4 | 2/4 | **2/4** | **INCOMPLETE** |

**No single run achieved all four targets.**

---

## FILE OPERATION BUG - DETAILED

### The Fatal Sequence (archive/cc-interactions/2025-10-25-h.txt)

**Line 2655 - Write #1: SUCCESS ✓**
```
Write(outputs/sobotkova-et-al-2023/extraction.json)
  Updated with 752 additions and 9 removals

Result: Created 750+ line file with:
  - 10 Evidence items
  - 17 Claims (3 core)
  - 4 Implicit Arguments ✓
  - Complete Abstract + Introduction extraction
```

**Line 3580 - Read: PARTIAL ❌**
```
Read(outputs/sobotkova-et-al-2023/extraction.json)
  Read 14 lines

Problem: File has 750+ lines, only read first 14 (header only)
```

**Line 3584 - Write #2: CATASTROPHIC ❌**
```
Write(outputs/sobotkova-et-al-2023/extraction.json)
  Updated with 458 additions and 367 removals

Lost:
  - Lines 209-262: Entire claims array (17 claims deleted)
  - Lines 717-806: Entire implicit_arguments array (4 IAs deleted)
  - Most evidence items

Kept:
  - Lines 1-14: Schema header
  - New evidence from Methods section

Result: 367 deletions = complete data loss for claims + IAs
```

### Why This Happened

**Assistant's error pattern:**
1. Wanted to add Methods section content
2. Read file with `limit=14` to check structure
3. **Used Write (not Edit) with only partial context**
4. Write operation replaced entire file with partial data

**Correct pattern:**
```
Option A: Read(file) [no limit] → modify → Write(file)
Option B: Edit(file, old_string, new_string)
Option C: Backup → Read → Write → Validate
```

**What happened:**
```
Read(file, limit=14) → modify → Write(file) = DATA LOSS
```

---

## CORRECTED UNDERSTANDING

### What I Initially Said (WRONG)

> "Chatbot succeeded because of iterative human guidance and mid-course corrections"

### What User Clarified (CORRECT)

- Chatbot: Manual prompt copy-paste, **single-shot, NO corrections**
- RUN-02: Automated execution, **single-shot, NO corrections**
- Current: Automated execution, **single-shot, NO corrections**

**All three were single-shot!**

### The Real Difference

| Run | File Operations | Result |
|-----|----------------|---------|
| Chatbot | Proper (no partial Read→Write) | ✅ 8 IAs |
| RUN-02 | Proper (no partial Read→Write) | ✅ 7 IAs |
| Current | **Bug: partial Read→Write** | ❌ 0 IAs |

### User's Key Corrections

1. **"Section-by-section extraction is not new"** - All runs used it
2. **"I did NOT provide mid-course corrections"** - Chatbot was single-shot
3. **"Nothing was removed from RUN-02"** - Same prompts/skill/schema
4. **"That's never happened before!"** - This file bug is unprecedented

---

## PROMPT IMPROVEMENTS STATUS

### ✅ Already Implemented (Chatbot Recommendations)

**Pass 1 Prompt (line 164):**
```markdown
Extract implicit arguments for all core claims (REQUIRED systematic search)
and key intermediate claims (as applicable).
```
- ✓ Replaced vague "HIGH-PRIORITY" with specific "all core claims"
- ✓ Made systematic search REQUIRED

**Pass 2 Prompt (lines 283-300):**
```markdown
### STEP 3: Implicit Argument Completeness Review

Systematic review for implicit arguments missed in Pass 1:
- Cross-subsection synthesis
- Overlooked logical implications
- Comparative interpretations

Quality check: If <3 implicit arguments total and paper makes
complex arguments, verify reasoning is genuinely explicit (rare).
```
- ✓ Complete discovery instructions
- ✓ 4-type framework review
- ✓ Quality check for suspiciously low IA counts

**Chatbot's recommendations were already incorporated before current run.**

---

## NEXT ACTIONS

### P0 - Critical (Fix File Operations)

**1. Implement Prevention Rules**

Add to extraction workflow/prompts:

```markdown
## CRITICAL: File Operation Safety Rules

❌ NEVER: Read(file, limit=N) followed by Write(file)
✅ ALWAYS: Read(file) [no limit] before Write(file)
✅ PREFER: Edit(file) for incremental additions

Before any Write operation:
1. Backup current file (timestamped)
2. Read FULL file (no limit)
3. Modify in memory
4. Write complete file
5. Validate: jq '{e: .evidence|length, c: .claims|length, ia: .implicit_arguments|length}'
6. If validation fails: Restore backup + alert
```

**2. Add Post-Write Validation**

After every Write to extraction.json:
```bash
counts=$(jq '{
  evidence: (.evidence | length),
  claims: (.claims | length),
  ias: (.implicit_arguments | length),
  rd: (.research_designs | length)
}' extraction.json)

# Alert if critical arrays empty after Pass 1
if pass >= 1:
  if counts.ias == 0: ALERT "IAs disappeared!"
  if counts.claims == 0: ALERT "Claims disappeared!"
```

**3. Test Restoration**

Re-run Sobotkova extraction with fixes:
- Verify IAs survive all passes
- Confirm 4-7 IAs achievable
- Check implicit RDMAP items also preserved
- Target: All 4 metrics in single run

### P1 - High (Investigate Implicit RDMAP)

**Current status:** 0/6 methods implicit, 0/8 protocols implicit

**Was this also file bug or separate issue?**

Need to check:
1. Were implicit RDMAP items extracted then deleted (file bug)?
2. Or never extracted (prompt/execution issue)?
3. Check RUN-02 transcript for implicit RDMAP extraction pattern

**Hypothesis:** Same file bug may have affected RDMAP items

### P2 - Medium (Long-term Prevention)

**Add checkpoint system:**
- Save pass completion states (PASS1_COMPLETE.json, PASS2_COMPLETE.json)
- Enable rollback if corruption detected
- Automatic validation between passes

**Add workflow safeguards:**
- Inter-pass validation: "Did we lose data?"
- Checklist completion before advancing
- State tracking: "Which arrays should be populated by now?"

---

## TESTING PLAN

### Phase 1: Verify Fix (Sobotkova Paper)

**Expected outcome:**
- Evidence: ~60 items
- Claims: ~30 items
- **Implicit Arguments: 4-7 items** ✓
- Research Designs: 6 items ✓
- Methods: 6 items (1-2 implicit)
- Protocols: 8-15 items (2-3 implicit)
- Protocol-Method linking: 100% ✓

**Success criteria:**
- All 4 target metrics achieved in single run
- 100% sourcing maintained
- No data loss during any Write operation

### Phase 2: Prevention Testing

**Create dummy extraction:**
- 10E, 5C, 3IA initial state
- Attempt section 2 addition with:
  - ✅ Full Read → Write (should work)
  - ✅ Edit for arrays (should work)
  - ❌ Partial Read → Write (should be blocked or caught)

**Verify:**
- ✅ patterns preserve all data
- ❌ pattern triggers validation alert

### Phase 3: Batch Processing

Once fix validated:
- Run on 2-3 additional papers
- Verify consistent IA extraction (4-10 per paper)
- Confirm no regressions in any metric
- Validate autonomous 5-pass workflow stability

---

## OPEN QUESTIONS

### For User Decision

1. **Which prevention tier to prioritize?**
   - Tier 1: Tool usage rules (requires discipline)
   - Tier 2: Post-write validation (catches errors)
   - Tier 3: Checkpoint backups (enables recovery)

2. **Should we modify workflow prompts?**
   - Add explicit file operation safety warnings?
   - Require validation checklist after each Write?
   - Add backup/restore procedures?

3. **Investigation scope:**
   - Focus only on IAs regression?
   - Or also investigate implicit RDMAP items (0 in current)?
   - Priority order?

### Technical Questions

1. **Why did chatbot/RUN-02 avoid this bug?**
   - Different file operation pattern?
   - Fewer intermediate writes?
   - Better Read-before-Write discipline?

2. **Implicit RDMAP regression:**
   - Same root cause (file bug)?
   - Or separate issue (prompt/extraction)?
   - Needs transcript analysis

3. **Evidence/Claims distribution shift:**
   - Current: 63E, 26C (ratio 2.42:1)
   - RUN-02: 33E, 46C (ratio 0.72:1)
   - Which is more accurate for this paper?

---

## FILES AFFECTED

### Current State

**outputs/sobotkova-et-al-2023/**
- `extraction.json` - 109 items, 0 IAs, 0 implicit RDMAP
- `extraction_backup.json` - Incomplete backup (40 evidence only)
- `summary.md` - Current run summary
- `validation-pass5.md` - Validation report

### Archive

**archive/output/cc-sonnet45/**
- `sobotkova-et-al-2023-RUN-01/` - 85 items, 0 IAs
- `sobotkova-et-al-2023-RUN-02/` - 112 items, **7 IAs**, 3 implicit RDMAP
- Current outputs (when fixed) will go here as RUN-03

**archive/output/chatbot-sonnet45/**
- `with-skill/extraction-02/` - 139-141 items, **8-10 IAs**

### Transcripts

**archive/cc-interactions/**
- `2025-10-25-g.txt` - RUN-02 transcript (successful IA extraction)
- `2025-10-25-h.txt` - Current run transcript (file bug documented)
- `2025-10-26-a.txt` - This debugging session (if created)

---

## CONTEXT FOR NEXT SESSION

### What You Need to Know

1. **The workflow is NOT too complex** - Proven by chatbot and RUN-02 success
2. **Both target improvements were already implemented** - Prompts updated per chatbot
3. **This is a file operation bug** - Not a systematic workflow failure
4. **Section-by-section is standard** - All runs use it (my earlier analysis was wrong)
5. **No human corrections were made** - All runs were single-shot (my assumption was wrong)

### What Still Needs Investigation

1. **Implicit RDMAP items regression** (3→0)
   - Same file bug or different cause?
   - Check RUN-02 transcript for extraction pattern

2. **Evidence/Claims distribution shift**
   - Manual review to determine accuracy
   - May inform consolidation guidance

3. **Why this bug is unprecedented**
   - What changed in execution pattern?
   - How did previous runs avoid it?

### User's Specific Feedback

- ✓ "Section-by-section extraction is not new"
- ✓ "I did NOT review intermediate outputs or offer corrections"
- ✓ "Nothing was removed from RUN-02"
- ✓ "That's never happened before!"

These corrections fundamentally changed my analysis from "workflow complexity" to "single file operation bug."

---

## IMMEDIATE NEXT STEPS

1. **After CC restart with skills:**
   - Review this planning document
   - Confirm fix strategy
   - Begin implementation

2. **Implementation order:**
   - Add file operation safety rules
   - Add post-write validation
   - Test on Sobotkova extraction
   - Verify all 4 metrics achievable

3. **Success criteria:**
   - 7 IAs + 6 RDs + 100% linking + 100% sourcing in single run
   - No data loss during any Write operation
   - Validation catches any future partial Read→Write attempts

---

**Document created:** 2025-10-26
**Investigation completed by:** Claude Code (Sonnet 4.5)
**Next session:** Implementation and testing
**Priority:** P0 - Critical data loss bug requiring immediate fix
