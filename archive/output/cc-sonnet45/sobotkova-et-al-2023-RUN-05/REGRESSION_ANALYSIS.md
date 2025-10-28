# Regression Analysis: Current Run vs Prior Runs

**Analysis Date**: 2025-10-27
**Current Run**: outputs/sobotkova-et-al-2023/extraction.json
**Compared Against**: chatbot-02, cc-RUN-01 through cc-RUN-04

---

## Executive Summary

The current extraction achieved excellent **volume** (275 total items, best among all runs) but suffered **critical regressions** in:

1. **Zero implicit RDMAP extraction** (0 implicit RD/M/P vs 1-4 in prior runs)
2. **41 broken claim→evidence cross-references** (vs 0-5 in prior runs)
3. **26% unmapped claims** (21/78 vs 8% best prior)
4. **4 broken RDMAP cross-references** (vs 0 in all prior runs)

These regressions indicate **systematic process failures** rather than isolated issues.

---

## Root Cause Analysis

### 🔴 CRITICAL: Complete Loss of Implicit RDMAP Extraction

#### Evidence of Regression

**Prior Run Example** (cc-RUN-01, Oct 24):
```python
{
    "protocol_id": "P006",
    "protocol_text": "Map assignment protocol: volunteers assigned specific map tiles to digitise",
    "protocol_type": "task_allocation",
    "protocol_status": "implicit",  # ← IMPLICIT STATUS
    "trigger_text": [
        "participants failed to digitise some assigned maps",
        "Student C failing to digitise three contiguous sections of an assigned map"
    ],
    "trigger_locations": [
        {"section": "3.5.2. Digitisation errors", "page": 7}
    ],
    "inference_reasoning": "Multiple references to 'assigned maps' and 'assigned sections' indicate a formal assignment protocol existed, but the paper never describes how assignments were made...",
    "implicit_metadata": {
        "basis": "mentioned_undocumented",
        "assessment_implication": "Cannot determine if assignment strategy affected error patterns"
    }
}
```

**Current Run** (Oct 27):
- ✅ Extracted 84 RDMAP items (15 RD, 29 M, 40 P) - excellent volume
- ❌ ALL marked as `"design_status": "explicit"` / `"method_status": "explicit"` / `"protocol_status": "explicit"`
- ❌ ZERO implicit items
- ❌ No `trigger_text`, `trigger_locations`, or `inference_reasoning` fields present

#### Root Cause: Workflow Change Eliminated Implicit Extraction

**Timeline of Changes:**

1. **Oct 26 (Pass 3 RDMAP, original attempt)**: Whole-paper extraction in single script
   - File: `/tmp/pass3_rdmap_extraction.py`
   - **DID extract implicit items** (P006 example above)
   - User interrupted: "RDMAP extraction should proceed section by section"

2. **Oct 27 (Pass 3 RDMAP, corrected approach)**: Section-by-section extraction
   - Files: `pass3_abstract_intro_rdmap.py`, `pass3_methods_rdmap.py`, `pass3_results_rdmap.py`, `pass3_discussion_rdmap.py`
   - **All items marked explicit**
   - No implicit extraction logic included

**What Changed:**
- User correctly identified that section-by-section approach was needed (following Pass 1 Claims/Evidence pattern)
- BUT: The corrective scripts were generated WITHOUT implicit extraction guidance
- The autonomous agent created new scripts that only extracted explicit items
- No prompt reminded the agent to look for implicit RDMAP items

**Evidence from Schema & References:**

The skill references CLEARLY document implicit extraction:

From `/home/shawn/Code/llm-reproducibility/.claude/skills/research-assessor/references/extraction-fundamentals.md`:
```markdown
### IMPLICIT CONTENT
**Definition:** Not directly stated but can be reasonably inferred from available passages.

**Examples of implicit content:**
- Implicit Arguments: Unstated assumptions, logical implications
- Implicit Methods: Procedures mentioned but not described    # ← DOCUMENTED
- Implicit Protocols: Implementation details inferred from results  # ← DOCUMENTED
```

From extraction schema v2.5:
```json
"method_status": {
  "type": "string",
  "enum": ["explicit", "implicit"],
  "description": "Whether documented in Methods (explicit) or inferred (implicit)"
}
```

**Conclusion:** The schema and skill references support implicit RDMAP extraction, but the section-by-section extraction scripts generated on Oct 27 did not implement this capability.

---

### 🔴 CRITICAL: Pass 2 Consolidation Broke Cross-References

#### Evidence of Regression

**Broken References Count:**
- Current: 41 broken claim→evidence refs
- cc-RUN-03: 5 broken refs
- All other prior runs: 0 broken refs

**Example Broken Reference:**
```json
Claim C029 references: ["E012", "E013", "E014"]
But E012, E013, E014 no longer exist (consolidated into E011 during Pass 2)
```

#### Root Cause: One-Directional Update During Consolidation

From `/tmp/pass2_rationalization.py` (inferred from validation results):

**What Happened:**
1. Pass 2 rationalization consolidated evidence items (E012+E013+E014 → E011)
2. Consolidation preserved source IDs in `consolidation_metadata`:
   ```json
   {
     "evidence_id": "E011",
     "consolidation_metadata": {
       "consolidated_from": ["E012", "E013", "E014"],
       "consolidation_type": "identical_support_pattern"
     }
   }
   ```
3. **BUT**: Claims that referenced E012, E013, E014 were NOT updated to reference E011
4. Result: Claims point to non-existent evidence IDs

**Why This Happened:**
- Pass 2 rationalization modified the `evidence` array
- But did NOT iterate through `claims` array to update `supported_by_evidence` fields
- Cross-reference repair was not part of consolidation logic

**Expected Behavior:**
When consolidating E012+E013+E014 → E011, should also:
```python
for claim in data['claims']:
    for old_id in ['E012', 'E013', 'E014']:
        if old_id in claim['supported_by_evidence']:
            claim['supported_by_evidence'].remove(old_id)
            if 'E011' not in claim['supported_by_evidence']:
                claim['supported_by_evidence'].append('E011')
```

---

### ⚠️ MODERATE: Claims Without Evidence (26%)

#### Evidence of Regression

- Current: 21/78 claims unmapped (26%)
- cc-RUN-03: 2/26 claims unmapped (8% - best prior)
- cc-RUN-04: 89/89 claims unmapped (100% - but that run had other issues)

#### Contributing Factors

1. **Broken cross-references** (see above) - Some "unmapped" claims may actually have broken refs
2. **Framework/definitional claims** - Claims C008-C027 cluster (background/gap statements)
   - These may legitimately not require direct evidence
   - Example: C010 "Existing research provides little guidance on when investments in different digitisation approaches become worthwhile" is a gap statement

3. **Liberal extraction philosophy** - Pass 1 over-extracted claims (intentionally)
   - Some may have been extracted without evidence links
   - Pass 2 should have rationalized these but didn't fully address mapping

#### Analysis

Not all "unmapped" claims are problematic:
- **Background claims** (C013-C025): Contextual framing, may not need evidence
- **Gap statements** (C010): Identify research gaps, inherently claim-only
- **Methodological arguments** without empirical support: Some are framework claims

**But**: 26% is higher than cc-RUN-03's 8%, suggesting mapping degradation.

---

### ⚠️ MODERATE: Broken RDMAP Cross-References (4)

#### Evidence

- Current: 4 broken RDMAP refs
- All prior runs: 0 broken

#### Root Cause

Likely similar to evidence consolidation issue:
- Pass 4 RDMAP rationalization consolidated items (8 consolidations performed)
- Example: RD004+RD005 → RD004, M015+M025 → M015, etc.
- Cross-reference updates may have been incomplete

**Specific Consolidations in Pass 4:**
1. RD004+RD005 → RD004 (case study positioning)
2. M015+M025 → M015 (downtime leveraging)
3. P028+P029 → P028 (workflow stages 1-2)
4. P031+P032 → P031 (volunteer stages)
5. P033+P034 → P033 (staff post-processing)
6. P038+P039 → P038 (execution results)
7. P043+P044+P046 → P043 (threshold framework)

The 4 broken references are likely from methods/protocols that referenced the now-deleted M025, P029, P032, P034, P039, P044, or P046 IDs.

---

## Positive Achievements

### ✅ Overall Extraction Volume: Best Performance

- **Total items: 275** (vs 221 best prior, 64 worst prior)
- Claims: 78 (comprehensive)
- Evidence: 107 (comprehensive)
- RDMAP: 84 (15 RD, 29 M, 40 P - excellent coverage)

**This is significant**: The section-by-section approach DID result in more comprehensive extraction overall.

### ✅ Perfect RDMAP Internal Connectivity

- 100% Research Designs → Methods
- 100% Methods connected bidirectionally
- 100% Protocols → Methods

**No orphans within RDMAP hierarchy** - excellent structural quality.

### ✅ Complete Sourcing (100%)

All 275 items have proper source attribution:
- Explicit items: `verbatim_quote` + `location`
- (Would have been for implicit items: `trigger_text` + `trigger_locations` + `inference_reasoning`)

---

## Likely Culprits Summary

### 1. Missing Implicit RDMAP Extraction Prompt/Logic

**Problem:** Section-by-section extraction scripts generated on Oct 27 only extracted explicit RDMAP items.

**Why:**
- User correction prompted re-generation of extraction scripts
- New scripts followed section-by-section pattern (correct)
- But lost implicit extraction capability present in Oct 26 version
- No explicit guidance in user's correction to preserve implicit extraction

**Solution Needed:**
- Extraction prompts must explicitly instruct: "Extract BOTH explicit and implicit RDMAP items"
- Reference `extraction-fundamentals.md` for implicit extraction requirements
- Include examples of implicit methods/protocols in extraction prompt

### 2. Incomplete Cross-Reference Repair During Consolidation

**Problem:** Pass 2 and Pass 4 rationalization consolidated items but didn't update referring items.

**Why:**
- Consolidation logic modifies target arrays (evidence, methods, protocols)
- But doesn't search through referencing arrays (claims referencing evidence, methods referencing protocols, etc.)
- No automated repair step

**Solution Needed:**
- Add cross-reference repair function to consolidation scripts
- After consolidating E012+E013→E011, update all claims' `supported_by_evidence` arrays
- After consolidating M025→M015, update all protocols' `implements_method` fields
- Validate cross-references before writing final JSON

### 3. Inadequate Mapping Guidance in Pass 1

**Problem:** 26% of claims extracted without evidence links.

**Why:**
- Liberal extraction phase intentionally over-captures
- But may have captured claims without identifying supporting evidence
- Pass 2 rationalization didn't fully address mapping completeness

**Solution Needed:**
- Pass 1 extraction prompt should emphasize: "For each claim, identify supporting evidence immediately"
- Pass 2 rationalization should include mapping audit: "Are there claims without evidence? Should they have evidence?"
- Distinguish intentionally unmapped (framework) claims from incomplete extraction

---

## Recommendations

### Immediate Fixes

1. **Fix broken cross-references** in current extraction:
   - Map consolidated IDs (E012+E013+E014→E011, etc.)
   - Update all claim references
   - Update all RDMAP references
   - Validate with pass5_validation.py

2. **Extract implicit RDMAP items** as remediation pass:
   - Use Oct 26 script logic as template
   - Focus on Results/Discussion sections (implicit methods often inferred from execution)
   - Add trigger_text, inference_reasoning fields
   - Expect 1-5 implicit designs, 1-3 implicit methods, 4-8 implicit protocols

### Process Improvements

1. **Update section-by-section extraction template** to include implicit extraction:
   ```python
   # For each section:
   # 1. Extract explicit RDMAP (documented in Methods)
   # 2. Extract implicit RDMAP (mentioned but not described)
   #    - Look for procedures mentioned in Results/Discussion
   #    - Check for undocumented protocols implied by execution details
   ```

2. **Add automated cross-reference repair** to consolidation scripts:
   ```python
   def repair_cross_references(data, old_id, new_id, ref_field):
       """Update all references after consolidation"""
       for item in all_referencing_items:
           if old_id in item[ref_field]:
               item[ref_field].remove(old_id)
               if new_id not in item[ref_field]:
                   item[ref_field].append(new_id)
   ```

3. **Enhance Pass 2 rationalization** to include mapping audit:
   - After consolidation, check for unmapped claims
   - Identify which are intentionally unmapped (framework) vs incomplete
   - Flag incomplete mapping for correction

4. **Add cross-reference validation** BEFORE Pass 5:
   - Run validation checks after Pass 2 and Pass 4
   - Block progression if broken references detected
   - Force repair before continuing

---

## Comparison with Prior Best Run (cc-RUN-03)

| Metric | Current | cc-RUN-03 | Assessment |
|--------|---------|-----------|------------|
| Total Items | 275 | 109 | ✓ BETTER (+152%) |
| Implicit RD | 0 | 0 | = SAME |
| Implicit M | 0 | 0 | = SAME |
| Implicit P | 0 | 0 | = SAME |
| Claims w/o Evidence | 21 (26%) | 2 (8%) | ⚠️ WORSE |
| Broken C→E Refs | 41 | 5 | ⚠️ WORSE |
| Broken RDMAP Refs | 4 | 0 | ⚠️ WORSE |
| RDMAP Connectivity | 100% | 83% | ✓ BETTER |

**Note:** cc-RUN-03 also had 0 implicit RDMAP items, so this isn't a regression from that specific run - but earlier runs (chatbot-02, cc-RUN-01, cc-RUN-02) DID extract some implicit items.

---

## Files Examined

### Skill & Schema
- `/home/shawn/Code/llm-reproducibility/.claude/skills/research-assessor/SKILL.md`
- `/home/shawn/Code/llm-reproducibility/.claude/skills/research-assessor/references/extraction-fundamentals.md`
- `/home/shawn/Code/llm-reproducibility/extraction-system/schema/extraction_schema.json`

### Extraction Scripts
- `/tmp/pass3_rdmap_extraction.py` (Oct 26, had implicit extraction)
- `/tmp/pass3_abstract_intro_rdmap.py` (Oct 27, no implicit extraction)
- `/tmp/pass3_methods_rdmap.py` (Oct 27, no implicit extraction)
- `/tmp/pass3_results_rdmap.py` (Oct 27, no implicit extraction)
- `/tmp/pass3_discussion_rdmap.py` (Oct 27, no implicit extraction)
- `/tmp/pass4_rdmap_rationalization.py` (Oct 27, consolidation without cross-ref repair)

### Validation
- `/tmp/pass5_validation.py` (identified 45 cross-ref issues, 21 unmapped claims)

### Transcript
- `/home/shawn/Code/llm-reproducibility/archive/cc-interactions/2025-10-27-a.txt` (heavily compacted, only shows Pass 5)

---

## Conclusion

The current extraction represents a **mixed result**:

**Strengths:**
- Highest item count (275) among all runs
- Excellent RDMAP structural quality (100% connectivity)
- Complete sourcing for all items
- Section-by-section approach yielded comprehensive coverage

**Critical Weaknesses:**
- Zero implicit RDMAP extraction (loss of capability present in Oct 26 run)
- 41 broken claim→evidence cross-references from incomplete consolidation
- 26% unmapped claims (higher than best prior run)
- 4 broken RDMAP cross-references

**Root Causes:**
1. Section-by-section extraction scripts lost implicit extraction logic during workflow correction
2. Consolidation operations didn't include cross-reference repair
3. No automated validation blocking progression when broken references detected

**Recommendation:** The extraction quality is high enough to use with remediation:
1. Fix the 45 broken cross-references (map consolidated IDs)
2. Optionally add implicit RDMAP extraction pass (4-10 items expected)
3. Audit the 21 unmapped claims (identify framework claims vs incomplete extraction)

The **volume achievement is real and valuable** - don't discard this extraction. But the **systematic process failures must be addressed** in future runs through better prompting, automated repair, and validation gates.
