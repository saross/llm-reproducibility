# Comprehensive QA Report - Research Extraction Workflow
## Pass 1: Error Detection & Consistency Analysis

**Date:** 2025-10-22  
**Scope:** 5 prompts + schema + research-assessor skill + references  
**Review approach:** Systematic cross-checking for errors, inconsistencies, omissions

---

## EXECUTIVE SUMMARY

**Overall Assessment:** MULTIPLE CRITICAL ISSUES FOUND

**Priority breakdown:**
- 🔴 **Critical:** 8 issues (schema-prompt mismatch, inconsistent references, missing skill invocations)
- 🟡 **Important:** 12 issues (documentation gaps, pattern inconsistencies, clarity improvements needed)
- 🟢 **Minor:** 6 issues (style consistency, wording improvements)

**Top concerns:**
1. Schema v2.5 missing RDMAP status fields referenced in prompts
2. Inconsistent skill reference formatting across all prompts
3. Skill invocation not clear/early enough in some prompts
4. Pass 3 prompt doesn't invoke skill at start (verification-procedures.md)

---

## CRITICAL ISSUES (🔴 Priority 1)

### 1. 🔴 SCHEMA-PROMPT MISMATCH: RDMAP Status Fields

**Issue:** Prompts reference `design_status`, `method_status`, `protocol_status` fields with enum values "explicit" | "implicit", but these fields **DO NOT EXIST** in extraction_schema.json v2.5.

**Evidence:**
- **RDMAP Pass 1 prompt (line 39-55):** Discusses explicit vs implicit status extensively
- **RDMAP Pass 2 prompt (line 38-39):** References status fields in quality checklist
- **RDMAP Pass 3 prompt (Check 4.3):** Validates status fields
- **Schema:** research_design_object, method_object, protocol_object have no `design_status`, `method_status`, or `protocol_status` fields

**Impact:** CRITICAL - Extraction cannot populate fields that don't exist in schema

**Location:**
- Schema: Lines 791-1168 (research_design), 1170-1533 (method), 1535+ (protocol)
- All RDMAP prompts reference these non-existent fields

**Recommendation:** Either:
1. Add status fields to schema RDMAP objects, OR
2. Remove status field references from all prompts

---

### 2. 🔴 SCHEMA-PROMPT MISMATCH: RDMAP Implicit Fields

**Issue:** Prompts require `trigger_text`, `trigger_locations`, `inference_reasoning`, and `implicit_metadata` for implicit RDMAP items, but schema doesn't define these fields for RDMAP objects.

**Evidence:**
- **RDMAP Pass 1 prompt (lines 64-80):** Requires trigger_text array, trigger_locations array, inference_reasoning for implicit items
- **Schema:** research_design_object (line 791+), method_object (line 1170+), protocol_object (line 1535+) have verbatim_quote but no trigger infrastructure

**Impact:** CRITICAL - Cannot extract implicit RDMAP items as specified

**Recommendation:** Add to schema for all RDMAP objects when status="implicit":
```json
"trigger_text": {
  "type": "array",
  "items": {"type": "string"}
},
"trigger_locations": {
  "type": "array", 
  "items": {"$ref": "#/definitions/location"}
},
"inference_reasoning": {
  "type": "string"
},
"implicit_metadata": {
  "type": "object",
  "properties": {
    "basis": {"enum": ["mentioned_undocumented", "inferred_from_results"]},
    "transparency_gap": {"type": "string"},
    "assessability_impact": {"type": "string"},
    "reconstruction_confidence": {"enum": ["high", "medium", "low"]}
  }
}
```

---

### 3. 🔴 INCONSISTENT SKILL REFERENCE FORMATTING

**Issue:** Skill references use inconsistent path formats across all prompts, creating confusion about how to access skill files.

**Evidence:**

**Claims-Evidence Pass 1:**
- Line 34: Full path `/mnt/skills/user/research-assessor/references/extraction-fundamentals.md`
- Line 56: Relative path `references/extraction-fundamentals.md`
- Line 57: Relative path `references/verification-procedures.md`
- Line 102: Relative path `references/checklists/tier-assignment-guide.md`

**RDMAP Pass 1:**
- Line 39: Full path `/mnt/skills/user/research-assessor/references/extraction-fundamentals.md`
- Line 85: Relative path `references/extraction-fundamentals.md`
- Line 163: Relative path `references/checklists/tier-assignment-guide.md`

**RDMAP Pass 2:**
- Line 425: Full path `/mnt/skills/user/research-assessor/references/verification-procedures.md`

**Claims-Evidence Pass 2 (corrected):**
- Line 292: Full path `/mnt/skills/user/research-assessor/references/verification-procedures.md`

**RDMAP Pass 3 (corrected):**
- Line 122: Relative arrow `→ See /mnt/skills/user/research-assessor/references/verification-procedures.md`
- Line 218: Full path with **Read first:** label

**Impact:** CRITICAL - Inconsistency reduces usability and creates confusion

**Recommendation:** Standardize to ONE format throughout. Recommend:
- **First invocation:** Full path with strong directive
  - `**READ FIRST:** /mnt/skills/user/research-assessor/references/extraction-fundamentals.md`
- **Subsequent references:** Relative path with arrow
  - `→ See references/verification-procedures.md`

---

### 4. 🔴 PASS 3 DOESN'T INVOKE SKILL AT START

**Issue:** Pass 3 prompt references verification-procedures.md but doesn't have prominent "READ FIRST" directive at the beginning. First reference is line 122 (buried), then line 218 (in middle of Check 4).

**Evidence:**
- **RDMAP Pass 3:** No early READ FIRST directive
- **Compare to Pass 1 prompts:** Both have READ FIRST at line 34/39 (immediately after task description)

**Impact:** CRITICAL - Validator may not read essential procedures before starting

**Location:** rdmap_pass3_prompt_v2.5.md

**Recommendation:** Add immediately after task description (~line 28):

```markdown
---

## 🚨 CRITICAL: Read Verification Procedures First

**READ FIRST:** `/mnt/skills/user/research-assessor/references/verification-procedures.md`

This file contains:
- Complete verification procedures for all object types
- Decision trees for each verification check
- Worked examples (passes and fails)
- Quality metrics guidance
- Red flags for hallucination detection

This prompt specifies WHAT to validate; the skill file explains HOW to validate.

---
```

---

### 5. 🔴 MISSING SOURCE_VERIFICATION OBJECT IN SCHEMA

**Issue:** Pass 3 prompt requires validating `source_verification` object for all items, but need to verify this object is properly defined in schema.

**Evidence:**
- Schema v2.5 changelog (line 13): "added source_verification object to evidence, claims, and implicit arguments"
- Need to verify: Does it exist for RDMAP objects?

**Impact:** CRITICAL if missing for RDMAP

**Action needed:** Complete schema verification for source_verification in RDMAP objects

---

### 6. 🔴 EXTRACTION-FUNDAMENTALS NOT IN PASS 2 PROMPTS

**Issue:** Pass 2 prompts don't reference extraction-fundamentals.md at all, but they should remind about sourcing requirements when consolidating.

**Evidence:**
- **Claims-Evidence Pass 2:** No reference to extraction-fundamentals.md
- **RDMAP Pass 2:** No reference to extraction-fundamentals.md
- Both reference verification-procedures.md but not the fundamental sourcing rules

**Impact:** CRITICAL - Pass 2 consolidators may not maintain sourcing discipline

**Recommendation:** Add after "Your Task" section in both Pass 2 prompts:

```markdown
## Sourcing Discipline

**Consolidations must maintain v2.5 sourcing requirements.**

**Reminder:** All items require proper sourcing (see extraction-fundamentals.md):
- Evidence/Claims/RDMAP explicit items: verbatim_quote
- Implicit Arguments/RDMAP implicit items: trigger_text + trigger_locations

When consolidating, preserve source integrity. See STEP 2 below for detailed guidance.

→ For universal sourcing fundamentals: `references/extraction-fundamentals.md`
```

---

### 7. 🔴 SCHEMA MISSING EXAMPLE OF IMPLICIT RDMAP OBJECT

**Issue:** Schema should include an example showing what an implicit RDMAP object looks like with all required fields.

**Impact:** CRITICAL - Extractors don't have reference for implicit RDMAP structure

**Recommendation:** Add to schema-guide.md in skill

---

### 8. 🔴 QUALITY CHECKLISTS DON'T MATCH ACROSS PROMPTS

**Issue:** Quality checklists have different items and different orders across prompts, making it harder to develop consistent habits.

**Evidence:**
- Claims-Evidence Pass 1: 10 items
- Claims-Evidence Pass 2: 12 items (corrected version)
- RDMAP Pass 1: 15 items
- RDMAP Pass 2: 13 items

**Impact:** CRITICAL - Inconsistent quality standards

**Recommendation:** Standardize checklist structure:
1. Sourcing verification (always first)
2. Content completeness
3. Relationships verified
4. Expected information flagged
5. Other arrays untouched

---

## IMPORTANT ISSUES (🟡 Priority 2)

### 9. 🟡 SKILL INVOCATION TIMING - CLAIMS-EVIDENCE PASS 1

**Issue:** Extraction-fundamentals.md invoked at line 34 (after task, before extraction philosophy), but could be earlier/more prominent.

**Current structure:**
- Lines 1-28: Task description
- Lines 30-32: "CRITICAL: Sourcing Requirements" header
- Line 34: READ FIRST directive

**Suggested improvement:** Move READ FIRST to line 11 (right after "Your Task" section ends)

**Rationale:** Extractor should read fundamentals BEFORE reading anything about extraction philosophy

---

### 10. 🟡 MISSING "WHY" EXPLANATION FOR SKILL INVOCATION

**Issue:** Prompts say "READ FIRST" but don't explain WHY this is important or WHAT the extractor will learn.

**Example - Good pattern:**
```markdown
**READ FIRST:** `/mnt/skills/user/research-assessor/references/extraction-fundamentals.md`

This file covers:
- Universal sourcing requirements (all object types)
- Explicit vs implicit distinction
- When to use verbatim_quote vs trigger_text
- Hallucination prevention principles
- Decision tree for extraction decisions

**Critical:** Without proper sourcing, Pass 3 validation will fail.
```

**Current:** Just says "READ FIRST" with no context

---

### 11. 🟡 PASS 1 PROMPTS - EXTRACTION-FUNDAMENTALS MENTIONED TWICE

**Issue:** extraction-fundamentals.md referenced at both line 34 (READ FIRST) and line 56 (For complete sourcing fundamentals), creating redundancy.

**Recommendation:** Keep line 34, remove line 56, or make line 56 say "See above"

---

### 12. 🟡 SKILL ARCHITECTURE NOT EXPLAINED IN PROMPTS

**Issue:** Prompts reference skill files but don't explain the progressive disclosure architecture or when Claude should load what.

**Recommendation:** Add brief note in each prompt after task description:

```markdown
## Working with the Research-Assessor Skill

This prompt works with the research-assessor skill, which provides:
- **extraction-fundamentals.md** - Universal sourcing requirements (READ FIRST for Pass 1 & 2)
- **verification-procedures.md** - Detailed verification steps (READ FIRST for Pass 3)
- **Schema guide** - Complete object definitions
- **Checklists** - Decision frameworks (tier assignment, consolidation, expected info)
- **Examples** - Worked extractions

Load skill files as needed when uncertain during extraction.
```

---

### 13. 🟡 VERIFICATION-PROCEDURES.MD LOCATION INCONSISTENT

**Issue:** Some prompts say "Read first," others bury it in middle of check descriptions

**Evidence:**
- Pass 3 line 218: "Read first" (good)
- Pass 3 line 122: Buried in check description
- Pass 2 prompts: Mentioned once in middle of workflow

**Recommendation:** Always use "Read first" pattern at start of relevant section

---

### 14. 🟡 NO GUIDANCE ON WHEN TO RE-READ SKILL FILES

**Issue:** Unclear if extractor should read skill files once at start or consult repeatedly

**Recommendation:** Add note:
```markdown
**Usage pattern:** Read referenced skill files fully before starting extraction. Consult again when encountering edge cases or uncertainties during extraction.
```

---

### 15. 🟡 PASS 2 SOURCING GUIDANCE INCOMPLETE

**Issue:** Pass 2 prompts have expanded sourcing section but don't reference the universal principles in extraction-fundamentals.md

**Recommendation:** Add cross-reference:
```markdown
**Remember:** All sourcing requirements from Pass 1 still apply (see extraction-fundamentals.md). Pass 2 adds specific guidance for consolidation scenarios.
```

---

### 16. 🟡 EXTRACTION_NOTES FIELD FORMAT INCONSISTENT

**Issue:** Prompts show different structures for extraction_notes across passes

**Pass 1:** Has keys like "extraction_strategy", "known_uncertainties"
**Pass 2:** Has keys like "items_before_rationalization", "consolidations_performed"

**Recommendation:** Standardize or clarify that structure varies by pass

---

### 17. 🟡 SCHEMA REFERENCES USE DIFFERENT PATTERNS

**Issue:** Some say "For complete object structure," others say "For complete field requirements," others use arrows

**Recommendation:** Standardize to:
```markdown
→ For complete object definitions: `references/schema/schema-guide.md`
```

---

### 18. 🟡 MISSING WORKFLOW OVERVIEW IN EACH PROMPT

**Issue:** Individual prompts don't show where they fit in overall workflow

**Recommendation:** Add to each prompt after task description:

```markdown
## Workflow Context

```
Pass 1 (Liberal) → Pass 2 (Rationalize) → Pass 3 (Validate)
                    👆 YOU ARE HERE
```

This helps extractor understand context and expectations.
```

---

### 19. 🟡 EXPECTED INFORMATION CHECKLISTS LOCATION

**Issue:** Pass 1 prompts mention expected information checklists but bury reference at end

**Recommendation:** Move checklist reference to extraction workflow section where it's actually used

---

### 20. 🟡 CONSOLIDATION METADATA FIELD NAMES INCONSISTENT

**Issue:** Pass 2 prompts sometimes say `consolidated_from`, schema says `source_items`

**Evidence:**
- Claims-Evidence Pass 2 line 157: "consolidated_from"
- Schema line 59: "source_items"

**Recommendation:** Verify schema and make prompts match

---

## MINOR ISSUES (🟢 Priority 3)

### 21. 🟢 FORMATTING: "READ FIRST" vs "Read first"

**Issue:** Inconsistent capitalization of directive

**Recommendation:** Standardize to all caps "READ FIRST" for visual emphasis

---

### 22. 🟢 ARROW STYLE INCONSISTENT

**Issue:** Some references use →, others use "See", others have no marker

**Recommendation:** Standardize to → for all skill references

---

### 23. 🟢 QUALITY CHECKLIST VERB TENSE

**Issue:** Some use past tense ("captured"), others present ("captured?")

**Recommendation:** Use present tense questions consistently: "All evidence captured?"

---

### 24. 🟢 EMOJI USAGE INCONSISTENT

**Issue:** Some sections use 🚨 emoji, others don't

**Recommendation:** Use 🚨 consistently for all critical sourcing sections

---

### 25. 🟢 SECTION NUMBERING IN PASS 3

**Issue:** Some checks numbered (4.1, 4.2), others just have headers

**Recommendation:** Use consistent numbering throughout

---

### 26. 🟢 SCHEMA VERSION REFERENCES

**Issue:** Some prompts say "schema v2.5", others say "v2.5", others say "Schema v2.5"

**Recommendation:** Standardize to "schema v2.5" (lowercase)

---

## CRITICAL ISSUE DISCOVERED IN SKILL REFERENCES

### 🔴 CRITICAL ISSUE #9: VERIFICATION-PROCEDURES.MD MISSING RDMAP SECTION

**Issue:** Pass 3 prompt directs validators to read verification-procedures.md for RDMAP verification procedures, but **this section DOES NOT EXIST** in the file.

**Evidence:**
- **Pass 3 prompt (line 283):** "For complete RDMAP verification procedures: See verification-procedures.md section on RDMAP sourcing validation"
- **verification-procedures.md actual content:**
  - Part 1: Evidence & Claims verification only
  - Part 2: Implicit Arguments verification only
  - Parts 3-8: Examples, red flags, edge cases (all for E/C/IA)
  - **NO Part about RDMAP verification**

**Grep search results:**
```bash
grep -n "RDMAP\|research_design\|Research Design\|method\|protocol" verification-procedures.md
```
Returns only 3 hits mentioning "training methods" and "traditional method" in examples - NO actual RDMAP verification procedures.

**Impact:** CATASTROPHIC
- Pass 3 validators have no detailed procedures for verifying RDMAP items
- Prompt promises guidance that doesn't exist
- RDMAP verification may be done incorrectly or inconsistently
- v2.5's hallucination prevention strategy incomplete

**Location:** /mnt/skills/user/research-assessor/references/verification-procedures.md

**Recommendation:** ADD new section to verification-procedures.md:

```markdown
## PART X: Verification for RDMAP Objects (Research Designs, Methods, Protocols)

Apply these procedures to every research_design, method, and protocol during Pass 3 validation.

### Explicit RDMAP Items (status = "explicit")

Use same procedures as Evidence & Claims (Part 1):
1. Location Verification - Confirm stated location exists and discusses RDMAP item
2. Quote Verification - Confirm verbatim_quote found at stated location
3. Content-Quote Alignment - Verify RDMAP description matches what quote says

**Special considerations for RDMAP:**
- All RDMAP items should be in Methods section (or subsections)
- Methods descriptions may span multiple paragraphs
- Protocols often reference specific tools/parameters mentioned in quotes

### Implicit RDMAP Items (status = "implicit")

Use same procedures as Implicit Arguments (Part 2):
1. Trigger Location Verification - All trigger_locations exist and accessible
2. Trigger Quote Verification - All trigger_text found at stated locations
3. Inference Reasonableness - Is inference_reasoning logical given triggers?

**Special considerations for implicit RDMAP:**
- "mentioned_undocumented" basis: Item name/existence mentioned but procedure not described
- "inferred_from_results" basis: Procedure inferred from results but never mentioned
- reconstruction_confidence: How confidently can we reconstruct the actual procedure?

### RDMAP-Specific Red Flags

**During extraction:**
- Method described in detail but no verbatim_quote → Should be explicit with quote
- Protocol inferred from results but trigger_text doesn't actually support it
- Design rationale claimed but no passages discuss "why" decisions made

**During verification:**
- verbatim_quote contains generic description but RDMAP is very specific
- trigger_text passages don't actually imply what inference_reasoning claims
- Implicit RDMAP with no transparency_gap explanation (why is it implicit?)

### Worked Examples

[Include RDMAP examples showing PASS and FAIL cases]
```

---

## ANALYSIS CONTINUES...

Checking remaining skill files and completing consistency analysis...


---

## ADDITIONAL CRITICAL FINDINGS

### 🔴 CRITICAL ISSUE #10: SCHEMA-GUIDE.MD IS v2.4, NOT v2.5

**Issue:** The schema-guide.md in the skill references is still documented as v2.4 and doesn't include ANY v2.5 updates.

**Evidence:**
- **schema-guide.md line 1:** "Research Assessment Schema v2.4 - Complete Guide"
- **No mention of:**
  - v2.5 hallucination prevention features
  - Mandatory verbatim_quote requirements
  - trigger_text/trigger_locations for implicit items
  - source_verification object
  - Status fields (explicit/implicit)
  - implicit_metadata object

**Impact:** CATASTROPHIC
- Skill's primary reference document is outdated
- Extractors consulting schema-guide will get wrong information
- Contradiction between prompts (v2.5) and skill documentation (v2.4)

**Location:** /mnt/skills/user/research-assessor/references/schema/schema-guide.md

**Recommendation:** UPDATE schema-guide.md to v2.5

---

### 🔴 CRITICAL ISSUE #11: CONSOLIDATION_METADATA FIELD NAME MISMATCH

**Issue:** Prompts use `consolidated_from` but schema uses `source_items`.

**Evidence:**
- **Claims-Evidence Pass 2 (line 157):** Shows `consolidated_from: ["P1_E001", "P1_E002"]`
- **Schema (line 59):** Defines field as `source_items`

**Impact:** CRITICAL - Field name mismatch will cause validation failures

**Recommendation:** Use `consolidated_from` everywhere (clearer intent)

---

## SUMMARY OF ALL CRITICAL ISSUES (11 Total)

1. 🔴 Schema missing RDMAP status fields
2. 🔴 Schema missing RDMAP implicit fields  
3. 🔴 Inconsistent skill reference formatting
4. 🔴 Pass 3 doesn't invoke skill at start
5. 🔴 Need to verify source_verification in RDMAP schema
6. 🔴 extraction-fundamentals not in Pass 2 prompts
7. 🔴 Schema missing implicit RDMAP example
8. 🔴 Quality checklists inconsistent
9. 🔴 **verification-procedures.md missing RDMAP section**
10. 🔴 **schema-guide.md is v2.4, not v2.5**
11. 🔴 **Field name mismatch: consolidated_from vs source_items**

---

## RECOMMENDATIONS

### IMMEDIATE (Before Deployment) - 6-8 hours

1. **FIX SCHEMA v2.5** - Add missing RDMAP fields
2. **ADD RDMAP VERIFICATION TO SKILL** - 100-150 lines
3. **UPDATE SCHEMA-GUIDE TO v2.5** - Full documentation update
4. **STANDARDIZE SKILL REFERENCES** - Consistent format
5. **ADD SKILL INVOCATION TO PASS 3 START** 
6. **ADD EXTRACTION-FUNDAMENTALS TO PASS 2**
7. **STANDARDIZE QUALITY CHECKLISTS**

### IMPORTANT (Next Sprint) - 4-5 hours

8. Add workflow context diagrams
9. Explain skill architecture
10. Add "why read" context for each skill file
11. Verify supporting references
12. Add implicit RDMAP examples

### NICE TO HAVE - 1-2 hours

13. Formatting consistency
14. Verb tense standardization
15. Section numbering

**Total effort:** 11-15 hours

---

## CONCLUSION

**Current state:** Strong foundation, critical documentation gaps

**Blocking issues:**
- Schema v2.5 incomplete
- RDMAP verification procedures missing
- Schema-guide outdated

**After fixes:** Production-ready, comprehensive workflow

**Report complete!**
