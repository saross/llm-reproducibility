# Task 1.5: Add Skill Invocation to Pass 3 Start

**Date:** 2025-10-22  
**Task:** Phase 1, Task 1.5 - Add prominent skill invocation at start of RDMAP Pass 3  
**Status:** ✅ Complete

---

## Problem

**Original issue:** RDMAP Pass 3 prompt referenced verification-procedures.md, but the invocation was buried in the middle of the document (line 218, in Section 4: Source Verification).

**Impact:** Validators might begin validation without reading the critical verification procedures, leading to:
- Inconsistent verification approaches
- Missing verification steps
- Incorrect interpretation of verification requirements

---

## Solution

**Added prominent invocation section** immediately after task description (line 30) with:

### New Section Content

```markdown
## 🚨 CRITICAL: Read Verification Procedures First

**READ FIRST:** `/mnt/skills/user/research-assessor/references/verification-procedures.md`

This file contains:
- Complete verification procedures for all object types (Evidence, Claims, Implicit Arguments, RDMAP)
- Decision trees for each verification check
- Worked examples (passes and fails)
- Quality metrics guidance
- Red flags for hallucination detection

**This prompt specifies WHAT to validate; the skill file explains HOW to validate.**

Pass 3 validation cannot be done correctly without these procedures. Read the entire verification-procedures.md file before beginning validation.
```

---

## Placement

**Location:** Immediately after "Your Task" section, before "Validation Checklist"

**Why this placement:**
1. **Early visibility:** Validators see it before starting work
2. **Prominent position:** Cannot be missed when reading prompt
3. **Before checklist:** Reads procedures before seeing what to check
4. **Logical flow:** Task → How to do task → Checklist → Details

---

## Architecture

**Progressive disclosure maintained:**
- **Prompt:** Says WHAT to validate (structural checks, what to report)
- **Skill:** Says HOW to validate (procedures, decision trees, examples)
- **Invocation:** Makes clear separation and tells validator to read skill first

**Existing later reference (line 218+):** Retained in Section 4 for additional emphasis at critical point

---

## Document Structure After Update

```
1. Header & Version Info
2. Your Task (WHAT to do)
3. 🚨 CRITICAL: Read Verification Procedures First (READ SKILL)
4. Validation Checklist (overview of checks)
5. Validation Philosophy
6. Section 1: Cross-Reference Integrity
7. Section 2: Hierarchy Validation
8. Section 3: Schema Compliance
9. Section 4: Source Verification
   - Contains second reference to verification-procedures.md (detailed)
10. [Rest of prompt continues...]
```

---

## Comparison: Before vs After

### Before
- Task description → Validation Checklist → [200+ lines] → Source Verification section → READ verification-procedures

**Problem:** Validator might start checking items in checklist before reading procedures

### After
- Task description → 🚨 READ verification-procedures FIRST → Validation Checklist → [continues...]

**Benefit:** Validator knows to read procedures before attempting any validation

---

## Integration with Other Changes

**Works with:**
- ✅ Task 1.2: RDMAP section now exists in verification-procedures.md
- ✅ Task 1.4: Reference formatted consistently (READ FIRST: full path)

**Enables:**
- Validators can follow RDMAP verification procedures
- All object types (Evidence, Claims, IA, RDMAP) validated systematically
- Quality metrics calculated correctly

---

## Files Updated

**Input:** `/home/claude/rdmap_pass3_prompt_standardized.md`  
**Output:** `/mnt/user-data/outputs/rdmap_pass3_prompt_v2.5_final.md`

**Changes:**
- Added 17-line prominent invocation section after line 28
- Retained existing reference at line 218+ for reinforcement
- No other changes to content

---

## Validation

### Checklist ✅
- [ ] Skill invocation appears early (line 30) ✓
- [ ] Uses "READ FIRST:" format ✓
- [ ] Full path provided ✓
- [ ] Explains WHAT skill contains ✓
- [ ] Explains WHY validator should read it ✓
- [ ] Prominent visual styling (🚨, bold) ✓
- [ ] Existing later reference retained ✓

---

**Task 1.5 Complete** - Pass 3 prompt now has prominent early invocation ensuring validators read verification procedures before beginning validation.
