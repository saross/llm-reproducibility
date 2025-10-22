# QA Remediation Plan - Prioritized Action Items

**Date:** 2025-10-22  
**Estimated total effort:** 11-15 hours  
**Priority:** BLOCKING issues must be fixed before deployment

---

## PHASE 1: BLOCKING ISSUES (Must Do First) - 6-8 hours

### Task 1.1: Fix extraction_schema.json (2-3 hours)

**Add RDMAP status fields:**
```json
// Add to research_design_object, method_object, protocol_object:
"design_status": {
  "type": "string",
  "enum": ["explicit", "implicit"],
  "description": "Whether documented in Methods (explicit) or inferred (implicit)"
}
```

**Add RDMAP implicit fields:**
```json
// Add to all RDMAP objects:
"trigger_text": {
  "type": ["array", "null"],
  "items": {"type": "string"},
  "description": "Verbatim passages implying this RDMAP item (for implicit items)"
},
"trigger_locations": {
  "type": ["array", "null"],
  "items": {"$ref": "#/definitions/location"}
},
"inference_reasoning": {
  "type": ["string", "null"],
  "description": "Explanation of how triggers support inference (for implicit)"
},
"implicit_metadata": {
  "type": ["object", "null"],
  "properties": {
    "basis": {"enum": ["mentioned_undocumented", "inferred_from_results"]},
    "transparency_gap": {"type": "string"},
    "assessability_impact": {"type": "string"},
    "reconstruction_confidence": {"enum": ["high", "medium", "low"]}
  }
}
```

**Fix field names:**
- Change `source_items` → `consolidated_from` in consolidation_metadata definition

**Verify source_verification object exists for RDMAP**

---

### Task 1.2: Add RDMAP Section to verification-procedures.md (2 hours)

**Location:** /mnt/skills/user/research-assessor/references/verification-procedures.md

**Add after Part 2 (before Part 3: Worked Examples):**

```markdown
## PART 3: Verification for RDMAP Objects (Research Designs, Methods, Protocols)

### Explicit RDMAP Items (status = "explicit")

Follow same 3-step procedure as Evidence & Claims:

**Step 1: Location Verification**
- Navigate to stated location (should be Methods section or subsections)
- Verify section/subsection exists
- Confirm paragraph discusses this RDMAP item

**Step 2: Quote Verification**
- Find verbatim_quote in stated location
- RDMAP quotes often span multiple sentences
- Methods descriptions may reference multiple paragraphs

**Step 3: Content-Quote Alignment**
- Does RDMAP item description match quote content?
- Watch for: Adding specificity not in quote
- Watch for: Over-interpreting vague method descriptions

### Implicit RDMAP Items (status = "implicit")

Follow same 3-step procedure as Implicit Arguments:

**Step 1: Trigger Location Verification**
**Step 2: Trigger Quote Verification**
**Step 3: Inference Reasonableness**

**Special considerations:**
- "mentioned_undocumented": Name mentioned but procedure not described
- "inferred_from_results": Procedure inferred from results section
- reconstruction_confidence: Can we reconstruct actual procedure?

### RDMAP-Specific Red Flags

[Include red flags specific to RDMAP items]

### Worked Examples

**Example 1: Explicit Method - PASS**
[Include example]

**Example 2: Implicit Protocol - PASS**
[Include example]

**Example 3: Implicit Method - FAIL (Weak Inference)**
[Include example]
```

**Renumber:** Part 3 becomes Part 4, etc.

---

### Task 1.3: Update schema-guide.md to v2.5 (1-2 hours)

**Location:** /mnt/skills/user/research-assessor/references/schema/schema-guide.md

**Changes needed:**
1. Line 1: Change "v2.4" → "v2.5"
2. Add new section after overview:

```markdown
## v2.5 Updates: Hallucination Prevention

Schema v2.5 introduces mandatory sourcing requirements:

### For Evidence & Claims
- **verbatim_quote** now REQUIRED (was optional)
- Must contain exact text stating this content
- If quote doesn't exist → don't extract

### For Implicit Arguments
- **trigger_text** array REQUIRED
- **trigger_locations** array REQUIRED (parallel to trigger_text)
- **inference_reasoning** REQUIRED
- Must have passages that together imply the argument

### For RDMAP Objects
**Explicit items (status = "explicit"):**
- Documented in Methods section
- Requires verbatim_quote

**Implicit items (status = "implicit"):**
- Not documented in Methods
- Requires trigger_text + trigger_locations + inference_reasoning
- Requires implicit_metadata object

### Source Verification Object
All items have source_verification for Pass 3 validation:
[Document structure and fields]
```

3. Update Evidence Object section to show verbatim_quote as REQUIRED
4. Update Claims Object section similarly
5. Update Implicit Arguments section with trigger infrastructure
6. Add new sections for RDMAP explicit vs implicit
7. Add worked example of implicit RDMAP object

---

## PHASE 2: HIGH-PRIORITY FIXES (Do Next) - 3-4 hours

### Task 2.1: Standardize Skill References (30 min)

**Pattern to use:**
- **First mention:** `**READ FIRST:** /mnt/skills/user/research-assessor/references/[file].md`
- **Subsequent:** `→ See references/[file].md`

**Files to update:**
- claims-evidence_pass1_prompt.md
- rdmap_pass1_prompt.md
- claims-evidence_pass2_prompt.md (corrected)
- rdmap_pass2_prompt.md
- rdmap_pass3_prompt_v2.5.md (corrected)

---

### Task 2.2: Add Skill Invocation to Pass 3 Start (15 min)

**Location:** rdmap_pass3_prompt_v2.5.md after line 28

**Add:**
```markdown
---

## 🚨 CRITICAL: Read Verification Procedures First

**READ FIRST:** `/mnt/skills/user/research-assessor/references/verification-procedures.md`

This file contains:
- Complete verification procedures for all object types (E/C/IA/RDMAP)
- Decision trees for each verification check
- Worked examples (passes and fails)
- Quality metrics guidance
- Red flags for hallucination detection

This prompt specifies WHAT to validate; the skill file explains HOW.

---
```

---

### Task 2.3: Add extraction-fundamentals to Pass 2 Prompts (30 min)

**Files:** claims-evidence_pass2_prompt.md, rdmap_pass2_prompt.md

**Add after "Your Task" section:**
```markdown
## Sourcing Discipline Reminder

Pass 2 consolidations must maintain v2.5 sourcing requirements.

**Quick reminder** (see extraction-fundamentals.md for details):
- Evidence/Claims/RDMAP explicit: Requires verbatim_quote
- Implicit Arguments/RDMAP implicit: Requires trigger_text + trigger_locations

When consolidating, preserve source integrity. See STEP 2 workflow for consolidation-specific guidance.

→ For complete sourcing fundamentals: `references/extraction-fundamentals.md`
```

---

### Task 2.4: Standardize Quality Checklists (1 hour)

**Create standard structure:**
1. **Sourcing verified** (always first)
2. **Content completeness**
3. **Relationships correct**
4. **Expected information flagged**
5. **Other arrays untouched** (always last)

**Update all 5 prompts** to use this structure

---

### Task 2.5: Add Workflow Context Diagrams (30 min)

**Add to each prompt after task description:**
```markdown
## Workflow Context

Pass 1 (Liberal) → Pass 2 (Rationalize) → Pass 3 (Validate)
                    👆 YOU ARE HERE
```

---

### Task 2.6: Explain Skill Architecture (30 min)

**Add to each prompt:**
```markdown
## Working with the Research-Assessor Skill

This prompt references the research-assessor skill files:
- **extraction-fundamentals.md** - Universal sourcing (Pass 1 & 2)
- **verification-procedures.md** - Validation steps (Pass 3)
- **schema-guide.md** - Complete object definitions
- **Checklists** - Tier assignment, consolidation, expected info
- **Examples** - Worked extractions

Load skill files when uncertain during extraction.
```

---

## PHASE 3: NICE TO HAVE (When Time Permits) - 1-2 hours

### Task 3.1: Verify Supporting References
- Check tier-assignment-guide.md
- Check consolidation-patterns.md
- Check expected-information.md

### Task 3.2: Add Implicit RDMAP Examples
- Create worked example in schema-guide.md
- Show complete object with all required fields

### Task 3.3: Formatting Consistency
- Standardize arrow usage (→)
- Standardize emoji usage (🚨)
- Standardize capitalization (READ FIRST vs Read first)

---

## TESTING AFTER REMEDIATION

1. **Schema validation:** Validate test extraction against updated schema
2. **End-to-end extraction:** Run Pass 1 → 2 → 3 on test paper
3. **Skill reference test:** Click through all skill references
4. **Source verification test:** Run Pass 3 on known good/bad extractions
5. **Cross-reference test:** Verify bidirectional references

---

## SUCCESS CRITERIA

**After Phase 1 complete:**
- ✅ Schema v2.5 complete with all RDMAP fields
- ✅ Verification-procedures.md has RDMAP section
- ✅ Schema-guide.md updated to v2.5
- ✅ Field names consistent (consolidated_from everywhere)

**After Phase 2 complete:**
- ✅ All skill references standardized
- ✅ All prompts have clear skill invocations
- ✅ Quality checklists consistent
- ✅ Workflow context clear in each prompt

**After Phase 3 complete:**
- ✅ Supporting references verified
- ✅ Examples comprehensive
- ✅ Formatting professional and consistent

---

**Start with Phase 1 - these are blocking issues for deployment.**
