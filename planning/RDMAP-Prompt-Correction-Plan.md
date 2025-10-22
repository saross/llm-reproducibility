# RDMAP Prompts Correction Plan

**Date:** 2025-10-21  
**Scope:** Fix RDMAP Pass 1, Pass 2, and Pass 3 prompts  
**Goal:** v2.4 → v2.5 upgrade + fix sourcing section errors  
**Context remaining:** ~87,000 tokens (plenty)

---

## Overview

### Files to Correct
1. **rdmap_pass1_prompt.md** - v2.4 → v2.5 + fix sourcing
2. **rdmap_pass2_prompt.md** - v2.4 → v2.5 + fix sourcing  
3. **rdmap_pass3_prompt.md** - v2.5 but missing RDMAP source verification

### What Went Wrong
**Editing error in new versions:** The sourcing section (lines 32-67) was copied from Claims/Evidence prompts, resulting in:
- Discussion of Evidence, Claims, Implicit Arguments (wrong object types)
- No guidance for Research Designs, Methods, Protocols sourcing
- Missing explicit vs implicit RDMAP distinction

### What We Have
- ✅ Old v2.4 RDMAP prompts (uploaded) - correct sourcing but need v2.5 updates
- ✅ New v2.5 Claims/Evidence prompts - correct and working
- ✅ Schema v2.5 change tracking - complete specifications
- ✅ verification-procedures.md - comprehensive (896 lines)

---

## Schema v2.5 Changes Required (All RDMAP Prompts)

### Change 1: Version Number
- **Old:** v2.4
- **New:** v2.5
- **Where:** Header, schema_version field, output format section
- **Impact:** 3-4 locations per prompt

### Change 2: Status Fields (NEW in v2.5)
**Add to all RDMAP objects:**
```json
"design_status": "explicit" | "implicit"
"method_status": "explicit" | "implicit"  
"protocol_status": "explicit" | "implicit"
```

**Definitions:**
- **explicit**: Documented in Methods section with procedural detail
- **implicit**: Not documented in Methods (whether mentioned elsewhere or inferred)

**Prompt guidance needed:**
- When to classify as explicit vs implicit
- How to populate implicit_metadata when status=implicit
- Examples of each

### Change 3: Sourcing Requirements (NEW in v2.5)

**Explicit RDMAP items require:**
- `verbatim_quote` (string, required) - exact text describing the RDMAP item

**Implicit RDMAP items require:**
- `trigger_text` (array, required) - passages that imply the RDMAP item exists
- `trigger_locations` (array, required) - where trigger passages found
- `inference_reasoning` (string, required) - explanation of inference
- `implicit_metadata` object (required when status=implicit):
  - `basis`: "mentioned_undocumented" | "inferred_from_results"
  - `transparency_gap`: description
  - `assessability_impact`: description
  - `reconstruction_confidence`: "high" | "medium" | "low"

### Change 4: Source Verification Object (NEW in v2.5)

**For explicit RDMAP items:**
```json
"source_verification": {
  "location_verified": boolean,
  "quote_verified": boolean,
  "content_aligned": boolean,
  "verification_notes": string,
  "verified_by": "extractor" | "validator" | "manual_review"
}
```

**For implicit RDMAP items:**
```json
"source_verification": {
  "trigger_locations_verified": boolean,
  "trigger_quotes_verified": boolean,
  "inference_reasonable": boolean,
  "verification_notes": string,
  "verified_by": "extractor" | "validator" | "manual_review"
}
```

---

## Pass 1 Corrections

### Section 1: Header Updates
**Lines 1-6:**
- Change version: 2.4 → 2.5
- Change date: 2025-10-20 → 2025-10-21
- Add update note: "Added mandatory sourcing and status fields (hallucination prevention)"

### Section 2: Input/Output Updates  
**Line 14:**
- Change: `(schema v2.4)` → `(schema v2.5)`

**Lines 250-270 (Output Format):**
- Change: `"schema_version": "2.4"` → `"schema_version": "2.5"`

### Section 3: REPLACE Sourcing Section (CRITICAL)
**Lines ~32-67 in broken version (or insert after line 33 in old version):**

**Replace with:**

```markdown
## 🚨 CRITICAL SOURCING REQUIREMENT 🚨

**READ FIRST - BEFORE ANY EXTRACTION:**
`/mnt/skills/user/research-assessor/references/verification-procedures.md`

The verification procedures document contains:
- Complete verification protocols for RDMAP items (explicit and implicit)
- Decision trees for each verification step
- Worked examples (passes and fails)
- Red flags for hallucination detection
- Edge cases and troubleshooting

**MANDATORY for all RDMAP extractions:**

### Explicit RDMAP Items (Directly Described)

**Research Designs, Methods, and Protocols that are explicitly described require:**

1. **`verbatim_quote`** - Exact text from paper describing this RDMAP item
2. **Precise location** - Section, subsection, paragraph
3. **Faithful extraction** - Extract ONLY what quote explicitly states
4. **Set `status` field to "explicit"** - design_status, method_status, or protocol_status
5. **If quote doesn't exist** → Either it's implicit (see below) or DO NOT EXTRACT

**Examples of explicit RDMAP:**
- ✅ "We used stratified random sampling with 30% coverage" → Explicit method
- ✅ "GPS coordinates recorded using Garmin GPSMAP 64s with ±3cm accuracy" → Explicit protocol
- ✅ "The study aimed to compare efficiency of two data collection platforms" → Explicit design

---

### Implicit RDMAP Items (Inferred from Multiple Passages)

**Research Designs, Methods, or Protocols that are implied but not directly stated require:**

1. **`trigger_text` array** - Verbatim passages that together imply this RDMAP item
2. **`trigger_locations`** - Location of each trigger passage (array of location objects)
3. **`inference_reasoning`** - Explanation connecting triggers to RDMAP item
4. **`implicit_metadata` object** - Complete with:
   - `basis`: "mentioned_undocumented" (mentioned but procedures absent) OR "inferred_from_results" (never mentioned, inferred from outcomes)
   - `transparency_gap`: What documentation is missing?
   - `assessability_impact`: How does absence affect credibility assessment?
   - `reconstruction_confidence`: How confident in this reconstruction? (high/medium/low)
5. **Set `status` field to "implicit"**
6. **If no trigger passages exist** → DO NOT EXTRACT

**Examples of implicit RDMAP:**
- Protocol for data cleaning mentioned in Results but procedures not described → Implicit protocol (basis: mentioned_undocumented)
- Sampling decision rationale (conclusions imply comparative design but not stated) → Implicit design (basis: inferred_from_results)
- Quality control procedures (results show filtered data but filtering protocol absent) → Implicit method (basis: mentioned_undocumented)

**Distinguish implicit from missing:**
- **Implicit:** Multiple passages together imply the RDMAP item existed
- **Missing:** No passages suggest the RDMAP item, just absent from paper
- Only extract implicit RDMAP if there are trigger passages to support inference

---

### Quick Test Before Extracting

**For explicit RDMAP items:**
- ❓ "Can I point to the exact sentence that describes this research design/method/protocol?"
- If NO → Check for implicit (trigger passages) OR DO NOT EXTRACT

**For implicit RDMAP items:**
- ❓ "Can I point to multiple specific passages that together imply this RDMAP item?"
- ❓ "Does my inference_reasoning clearly explain how triggers support this inference?"
- ❓ "Can I classify the basis as mentioned_undocumented or inferred_from_results?"
- If NO → DO NOT EXTRACT

---

### Pass 1 Liberal Strategy + Sourcing Discipline

**Maintain both principles:**

✅ **Over-extract** when uncertain about tier assignment or boundaries
✅ **BUT require sourcing** for everything extracted

**This means:**
- When uncertain if something is Design vs Method → Extract as BOTH with sourcing for each
- When uncertain if explicit vs implicit → Extract with appropriate sourcing structure
- When uncertain if over-granular → Extract anyway with verbatim_quote
- **NEVER extract without sourcing** → This is the hallucination prevention discipline

---

### Unified Verification

All RDMAP items follow same verification procedures as Evidence/Claims:
- **Explicit items** → 3-part verification via verbatim_quote
- **Implicit items** → 3-part verification via trigger_text
- See verification-procedures.md for complete decision trees and examples

**Remember:** RDMAP extraction requires same sourcing discipline as Evidence/Claims. Every Research Design, Method, and Protocol must be traceable to specific passages in the paper.
```

**Insertion point:** After line 33 ("Output: Same JSON document...") in old v2.4 version

### Section 4: Update Quality Checklist
**Line 49 in old version (insert new items):**

Add to checklist:
```markdown
- [ ] Status fields set for all RDMAP items (explicit or implicit)
- [ ] All explicit items have verbatim_quote populated
- [ ] All implicit items have trigger_text, trigger_locations, inference_reasoning
- [ ] All implicit items have complete implicit_metadata
- [ ] No hallucinations - only extract what's sourced
```

### Section 5: Add Status Field Decision Guidance
**After line ~140 (three-tier framework section), add new section:**

```markdown
### 2. Explicit vs Implicit Status

**Every RDMAP item must be classified as explicit or implicit.**

**EXPLICIT = Documented in Methods section**
- Procedural details provided
- Replication possible from description
- Extractable via verbatim_quote

**IMPLICIT = Not documented in Methods**
- May be mentioned elsewhere without procedures
- May be inferred from results/discussion
- Requires trigger_text and inference_reasoning

**Decision tree:**
```
Is this RDMAP item described in Methods section?
├─ YES → Status = explicit, extract with verbatim_quote
└─ NO → Are there passages that imply it existed?
    ├─ YES → Status = implicit, extract with trigger_text
    └─ NO → DO NOT EXTRACT (absent, not implicit)
```

**Basis classification for implicit items:**
- **mentioned_undocumented**: Paper mentions item but doesn't describe procedures
  - Example: "Data were cleaned" (mentioned) but no cleaning procedure described
- **inferred_from_results**: Never mentioned but implied by outcomes
  - Example: Results show "outliers removed" but removal never mentioned in Methods

**Examples:**

**Explicit Method:**
```json
{
  "method_id": "M003",
  "method_text": "Stratified random sampling with 30% coverage of survey area",
  "method_status": "explicit",
  "verbatim_quote": "We used stratified random sampling with 30% coverage",
  "location": {"section": "Methods", "subsection": "2.3 Sampling", "paragraph": 1}
}
```

**Implicit Protocol (mentioned_undocumented):**
```json
{
  "protocol_id": "P002",
  "protocol_text": "Desktop GIS supervised data integration in 2010 season",
  "protocol_status": "implicit",
  "trigger_text": [
    "volunteers completed supervised desktop GIS work in 2010",
    "2010 season used desktop workstation setup"
  ],
  "trigger_locations": [
    {"section": "Discussion", "subsection": "4.1.1", "paragraph": 2},
    {"section": "Discussion", "subsection": "4.1.1", "paragraph": 3}
  ],
  "inference_reasoning": "Discussion mentions supervised desktop GIS in 2010, but Methods section doesn't describe this protocol. Inferred that procedure existed but wasn't documented.",
  "implicit_metadata": {
    "basis": "mentioned_undocumented",
    "transparency_gap": "Supervision procedures, GIS software, quality control steps not described",
    "assessability_impact": "Cannot assess quality control or replication without protocol details",
    "reconstruction_confidence": "medium"
  },
  "location": {"section": "Discussion", "subsection": "4.1.1"}
}
```

**Implicit Method (inferred_from_results):**
```json
{
  "method_id": "M015",
  "method_text": "Outlier removal applied before statistical analysis",
  "method_status": "implicit",
  "trigger_text": [
    "Analysis performed on cleaned dataset",
    "Three outliers excluded from final analysis"
  ],
  "trigger_locations": [
    {"section": "Results", "subsection": "3.2", "paragraph": 1},
    {"section": "Results", "subsection": "3.4", "paragraph": 2}
  ],
  "inference_reasoning": "Results mention outliers were excluded and data cleaned, but Methods never describes outlier detection or removal procedures. Inferred that method was used but not documented.",
  "implicit_metadata": {
    "basis": "inferred_from_results",
    "transparency_gap": "Outlier detection criteria, removal justification, effect on results not described",
    "assessability_impact": "Cannot assess appropriateness of exclusions or reproduce analysis",
    "reconstruction_confidence": "low"
  },
  "location": {"section": "Results", "subsection": "3.2"}
}
```

**→ For detailed guidance on implicit RDMAP, see `references/checklists/tier-assignment-guide.md`**
```

### Section 6: Update Expected Information Section
**Around line 200-250 (expected information checklists):**

Add note at beginning:
```markdown
**Note:** Expected information gaps don't indicate implicit status. A method can be explicit (documented) but still missing expected information (e.g., sample size justified but quality control procedures absent). Implicit status means the method/protocol ISN'T documented at all.
```

### Section 7: Update Output Format
**Lines 250-270:**

Update example object to include v2.5 fields:
```json
{
  "method_id": "M001",
  "method_text": "Pedestrian archaeological survey",
  "method_type": "data_collection",
  "method_status": "explicit",
  "verbatim_quote": "We conducted systematic pedestrian survey...",
  "source_verification": {
    "location_verified": true,
    "quote_verified": true,
    "content_aligned": true,
    "verified_by": "extractor"
  },
  "location": {...},
  "extraction_confidence": "high"
}
```

---

## Pass 2 Corrections

### Section 1: Header Updates
**Lines 1-6:**
- Change version: 2.4 → 2.5
- Change date: 2025-10-20 → 2025-10-21
- Add update note: "Added source verification for consolidations"

### Section 2: Input/Output Updates
**Line ~70 (Output Format):**
- Change: `"schema_version": "2.4"` → `"schema_version": "2.5"`

### Section 3: ADD Sourcing Verification Section
**After line ~118 (Consolidation Workflow, STEP 2), add:**

```markdown
### Source Verification for Consolidations

When consolidating RDMAP items in Pass 2, verify sourcing integrity:

**For consolidating explicit RDMAP items:**
1. **Verify all source quotes from same general location** - If consolidating M003 + M004, both verbatim_quotes should be from same Methods section/subsection
2. **Consolidated text must not claim anything beyond source quotes** - New combined text faithful to what sources actually state
3. **If sources conflict** → Flag for manual review, do NOT consolidate

**For consolidating implicit RDMAP items:**
1. **All trigger_text passages should relate to same RDMAP concept** - Don't consolidate unrelated implicit items
2. **Combined inference_reasoning should explain unified concept** - Not just list two separate inferences
3. **If trigger passages contradict** → Keep as separate implicit items

**For mixed consolidations (explicit + implicit):**
- Generally avoid mixing explicit and implicit items
- If necessary, mark the consolidated item's status appropriately
- Document the mix in consolidation_metadata

---

### New Implicit RDMAP in Pass 2?

Pass 2 may identify implicit RDMAP items missed in Pass 1, particularly:
- **Cross-subsection synthesis** - Method implied across multiple sections
- **Overlooked implicit content** - Protocol mentioned but not described
- **Comparative designs** - Design rationale implied but not stated

**If adding implicit RDMAP in Pass 2:**
1. Must have `trigger_text` array with verbatim passages
2. Must have `trigger_locations` for each passage
3. Must have `inference_reasoning` explaining the inference
4. Must have complete `implicit_metadata` object
5. Must explain in extraction_notes why missed in Pass 1

---

### Verification Reference

**For detailed verification procedures, see:**
`/mnt/skills/user/research-assessor/references/verification-procedures.md`

**Pass 2 verification focuses:**
- Consolidated items preserve source integrity
- No information invented during consolidation
- Status fields (explicit/implicit) remain accurate after consolidation
- Trigger_text and verbatim_quotes updated appropriately

**Remember:** Pass 2 consolidates and refines, but maintains same sourcing discipline established in Pass 1.
```

### Section 4: Update Quality Checklist
**Line 30 (checklist section), add items:**

```markdown
- [ ] Source verification complete for consolidations
- [ ] Status fields preserved/corrected after consolidation
- [ ] Explicit items maintain verbatim_quote integrity
- [ ] Implicit items maintain trigger_text integrity
```

---

## Pass 3 Corrections

### Section 1: Header Update
**Line 6:**
Change: "Added source verification checks (hallucination prevention)"
To: "Added source verification checks for ALL object types including RDMAP (hallucination prevention)"

### Section 2: ADD RDMAP Source Verification
**After line 397 (end of Check 4.4), insert new section:**

```markdown
---

#### Check 4.5: RDMAP Source Verification (NEW in v2.5)

**🚨 CRITICAL: RDMAP items require same sourcing discipline as Evidence/Claims**

Schema v2.5 requires all Research Designs, Methods, and Protocols to be properly sourced. Verify:

**For explicit RDMAP items (status = "explicit"):**
1. **`verbatim_quote` populated** (required field, non-empty string)
2. **`source_verification` object complete** with fields:
   - `location_verified`: boolean
   - `quote_verified`: boolean
   - `content_aligned`: boolean
   - `verification_notes`: string
   - `verified_by`: enum value

**For implicit RDMAP items (status = "implicit"):**
1. **`trigger_text` array populated** (required, minimum 1 passage)
2. **`trigger_locations` array populated** (required, parallel to trigger_text)
3. **`inference_reasoning` populated** (required, non-empty string)
4. **`implicit_metadata` object complete** with required fields:
   - `basis`: "mentioned_undocumented" | "inferred_from_results"
   - `transparency_gap`: string
   - `assessability_impact`: string
   - `reconstruction_confidence`: "high" | "medium" | "low"
5. **`source_verification` object complete** with fields:
   - `trigger_locations_verified`: boolean
   - `trigger_quotes_verified`: boolean
   - `inference_reasonable`: boolean
   - `verification_notes`: string
   - `verified_by`: enum value

**Report critical issues:**
```json
"rdmap_source_issues": [
  {
    "id": "M008",
    "type": "method",
    "status": "explicit",
    "issue": "Missing verbatim_quote - cannot verify sourcing",
    "severity": "critical"
  },
  {
    "id": "P002",
    "type": "protocol",
    "status": "implicit",
    "issue": "trigger_text array empty - implicit item requires trigger passages",
    "severity": "critical"
  }
]
```

**Statistical quality metrics for RDMAP:**
- Calculate pass rates separately for Research Designs, Methods, Protocols
- Overall RDMAP sourcing quality (explicit + implicit combined)
- Flag if <95% pass rate (systematic issue)

**Common RDMAP sourcing failures:**
- Explicit item missing verbatim_quote (extract without source)
- Implicit item missing trigger_text (inferred without evidence)
- Implicit item missing implicit_metadata (incomplete reconstruction info)
- Status field not set (default without decision)
- Mixed status (verbatim_quote AND trigger_text both present)

**Cross-consistency checks:**
- If status="explicit" → MUST have verbatim_quote, MUST NOT have trigger_text
- If status="implicit" → MUST have trigger_text, verbatim_quote should be null or empty
- If trigger_text present → status MUST be "implicit"
- If verbatim_quote present → status MUST be "explicit"

**See verification-procedures.md for:**
- Complete verification decision trees for RDMAP
- Pass/fail examples for RDMAP sourcing
- Edge cases (e.g., method mentioned but not described)
- Guidance on implicit vs missing distinction
```

### Section 3: Update Check 5.1 (Expected Information)
**Line ~404:**

Add note:
```markdown
**Note:** Expected information completeness is separate from explicit/implicit status. An explicit (documented) method can still be missing expected information. Implicit methods automatically have higher expected information gaps (since they're not documented).
```

### Section 4: Update Statistical Quality Section
**After Check 4.3 (line ~388), expand to:**

```markdown
#### Check 4.3: Statistical Quality Metrics (EXPANDED for v2.5)

**Calculate and report pass rates for ALL object types:**

**Evidence & Claims:**
- Overall pass rate (all three verification checks pass)
- Per-check pass rates (location, quote, content alignment)
- Total items verified

**Implicit Arguments:**
- Overall pass rate (all three verification checks pass)
- Per-check pass rates (trigger locations, trigger quotes, inference reasonableness)
- Total items verified

**RDMAP (NEW in v2.5):**
- **Research Designs:** explicit pass rate, implicit pass rate, overall
- **Methods:** explicit pass rate, implicit pass rate, overall
- **Protocols:** explicit pass rate, implicit pass rate, overall
- **Combined RDMAP:** overall sourcing quality across all three tiers

**Quality thresholds:**
- Target: >95% overall pass rate (per object type)
- Warning: 90-95% pass rate
- Critical: <90% pass rate (systematic quality issue)

**Include in report:** 
```json
"source_verification_metrics": {
  "evidence_claims": {
    "total": 45,
    "passed": 43,
    "pass_rate": 95.6,
    "status": "target"
  },
  "implicit_arguments": {
    "total": 3,
    "passed": 3,
    "pass_rate": 100,
    "status": "target"
  },
  "rdmap": {
    "research_designs": {
      "explicit": {"total": 5, "passed": 5, "pass_rate": 100},
      "implicit": {"total": 1, "passed": 1, "pass_rate": 100},
      "overall": {"total": 6, "passed": 6, "pass_rate": 100}
    },
    "methods": {
      "explicit": {"total": 18, "passed": 17, "pass_rate": 94.4},
      "implicit": {"total": 2, "passed": 2, "pass_rate": 100},
      "overall": {"total": 20, "passed": 19, "pass_rate": 95.0}
    },
    "protocols": {
      "explicit": {"total": 25, "passed": 24, "pass_rate": 96.0},
      "implicit": {"total": 1, "passed": 0, "pass_rate": 0},
      "overall": {"total": 26, "passed": 24, "pass_rate": 92.3}
    },
    "rdmap_overall": {
      "total": 52,
      "passed": 49,
      "pass_rate": 94.2,
      "status": "warning"
    }
  }
}
```
```

---

## Correction Workflow

### Step 1: RDMAP Pass 1 (Estimated 20 minutes)
1. Update header (version, date, note)
2. Update schema version references (2 locations)
3. REPLACE sourcing section (lines after line 33)
4. ADD status field guidance section (after three-tier framework)
5. UPDATE quality checklist (add sourcing items)
6. UPDATE expected information note
7. UPDATE output format examples
8. Save as `rdmap_pass1_prompt_v2.5.md`

### Step 2: RDMAP Pass 2 (Estimated 15 minutes)
1. Update header (version, date, note)
2. Update schema version reference (1 location)
3. ADD source verification section (after STEP 2 in workflow)
4. UPDATE quality checklist (add sourcing items)
5. Save as `rdmap_pass2_prompt_v2.5.md`

### Step 3: Pass 3 Validation (Estimated 15 minutes)
1. Update header note (clarify includes RDMAP)
2. ADD Check 4.5 (RDMAP source verification)
3. EXPAND Check 4.3 (statistical metrics for RDMAP)
4. UPDATE Check 5.1 note (expected info vs implicit status)
5. Save as `rdmap_pass3_prompt_v2.5.md`

**Total estimated time: 50 minutes**

---

## Verification Checklist

After corrections complete, verify each prompt:

### RDMAP Pass 1 v2.5 ✓
- [ ] Version 2.5 in header and schema references
- [ ] Sourcing section discusses Research Designs, Methods, Protocols (NOT Evidence/Claims)
- [ ] Explicit vs implicit distinction explained
- [ ] Status field decision guidance included
- [ ] Examples show both explicit and implicit RDMAP
- [ ] References verification-procedures.md
- [ ] Quality checklist includes sourcing items
- [ ] Output format shows v2.5 fields

### RDMAP Pass 2 v2.5 ✓
- [ ] Version 2.5 in header and schema reference
- [ ] Source verification section for consolidations
- [ ] Guidance on consolidating explicit vs implicit items
- [ ] Quality checklist includes sourcing verification
- [ ] References verification-procedures.md

### Pass 3 v2.5 (RDMAP enhanced) ✓
- [ ] Check 4.5 added for RDMAP source verification
- [ ] Check 4.3 expanded with RDMAP metrics
- [ ] Both explicit and implicit RDMAP verification covered
- [ ] Cross-consistency checks for status fields
- [ ] References verification-procedures.md for RDMAP

---

## Files to Produce

1. **rdmap_pass1_prompt_v2.5.md** - Complete corrected Pass 1
2. **rdmap_pass2_prompt_v2.5.md** - Complete corrected Pass 2
3. **rdmap_pass3_prompt_v2.5.md** - Enhanced Pass 3 with RDMAP verification

---

## Context Budget

**Current:** ~87,000 tokens  
**Estimated usage:**
- Plan review: 3,000 tokens
- Pass 1 correction: 15,000 tokens
- Pass 2 correction: 10,000 tokens
- Pass 3 correction: 8,000 tokens
- **Total: ~36,000 tokens**

**Remaining after corrections:** ~51,000 tokens (plenty for review and adjustments)

---

---

## Phase 4: Optimization & Streamlining (AFTER Critical Fixes)

**Note:** These optimizations should be done AFTER completing Phases 1-3 and testing the corrected prompts. Based on the earlier systematic review, these improvements will reduce duplication, improve consistency, and enhance maintainability.

### Why Wait for Phase 4?
- Test schema v2.5 with working prompts first
- Identify which sections actually cause confusion in practice
- Optimize based on empirical extraction experience (2-3 test papers)
- Avoid premature optimization before validation

---

### Optimization 1: Create extraction-fundamentals.md Reference (3-4 hours)

**Goal:** Consolidate duplicated core concepts into single reference file

**Create:** `/mnt/skills/user/research-assessor/references/extraction-fundamentals.md`

**Content to consolidate:**
- Evidence vs Claims distinction (detailed with examples)
- RDMAP three-tier hierarchy (WHY/WHAT/HOW with examples)
- Four-level claims hierarchy (Core/Intermediate/Supporting/Evidence)
- Explicit vs Implicit distinction (unified across all object types)
- Implicit arguments types (4 types with examples)
- Professional judgment boundary guidance

**Current duplication:**
- Evidence/Claims definition appears in Claims Pass 1 prompt (~18 lines)
- RDMAP tiers appear in both RDMAP Pass 1 (~60 lines) and Pass 2 prompts
- Similar examples repeated across prompts

**After consolidation:**
- Each prompt: Brief inline definition (2-3 lines) + pointer to fundamentals
- **Token savings:** 40-60 lines across all prompts (~5-7% reduction)
- **Maintainability:** Single source of truth for core concepts

**Example transformation:**

**Before (in prompt - 18 lines):**
```markdown
### 1. Evidence vs. Claims Distinction

**EVIDENCE** = Raw observations, measurements, or data that require minimal interpretation
- Direct measurements (e.g., "125.8 person-hours")
- Observations (e.g., "12 students owned smartphones")
- Data points (e.g., "95.7% accuracy")
[... continues for 18 lines ...]
```

**After (in prompt - 6 lines):**
```markdown
### 1. Evidence vs. Claims Distinction

**EVIDENCE** = Direct observations verifiable by checking sources (measurements, data points)  
**CLAIMS** = Assertions requiring interpretation or expertise to assess

**Quick test:** "Could someone verify this just by checking the source, or does it require judgment?"

→ For detailed framework with examples, see `references/extraction-fundamentals.md`
```

**Prompts to update:**
- claims-evidence_pass1_prompt.md
- rdmap_pass1_prompt.md (after Phase 1 corrections)
- rdmap_pass2_prompt.md (after Phase 2 corrections)

---

### Optimization 2: Create pass2-patterns.md Reference (2-3 hours)

**Goal:** Consolidate Pass 2-specific guidance appearing in multiple prompts

**Create:** `/mnt/skills/user/research-assessor/references/pass2-patterns.md`

**Content to consolidate:**
- Strategic verbosity in claims/RDMAP
- Anchor numbers in claims (acceptable duplication)
- Multi-dimensional evidence pattern
- Calculation claims removal logic
- Addition patterns (comparisons, recommendations, synthesis)
- Consolidation decision trees

**Current duplication:**
- Similar consolidation patterns in Claims Pass 2 (~30 lines) and RDMAP Pass 2 (~40 lines)
- Strategic verbosity guidance repeated

**After consolidation:**
- **Token savings:** 30-40 lines across Pass 2 prompts
- **Consistency:** Same consolidation philosophy across object types
- **Discoverability:** Centralized Pass 2 guidance

**Prompts to update:**
- claims-evidence_pass2_prompt.md
- rdmap_pass2_prompt.md (after Phase 2 corrections)

---

### Optimization 3: Standardize Prompt Structure (2-3 hours)

**Goal:** Consistent section ordering across all 5 prompts for predictability

**Current inconsistencies:**
- Quality checklist placement varies (start vs end)
- Section ordering differs across prompts
- Some have Philosophy before Principles, others reverse

**Recommended standard structure:**

```markdown
# [Pass Type] - PASS [N]: [Phase Name] v2.5

**Version:** 2.5 Pass N
**Last Updated:** YYYY-MM-DD
**Workflow Stage:** [Description]
**Update:** [Latest changes]

---

## Your Task
[What you're doing, inputs, outputs]

---

## Quality Checklist
[EXCEPT Pass 1 where it goes at end as final review]

---

## [Pass Type] Philosophy
[Pass-specific approach and mindset]

---

## Core Principles
[Essential concepts with pointers to references]

---

## [Pass Type] Workflow
[Step-by-step instructions]

---

## Output Format
[Expected JSON structure]

---

## Remember
[Key takeaways]
```

**Specific decisions:**
- **Pass 1 prompts:** Checklist at END (final review before submission)
- **Pass 2+ prompts:** Checklist at START (roadmap for work)
- **Philosophy before Principles:** Consistent ordering
- **Core Principles before Workflow:** Understand then execute

**Benefits:**
- Predictable navigation across prompts
- Easier to find sections
- Clear distinction between Pass 1 (review) vs Pass 2+ (roadmap) checklist usage

**Prompts to update:** All 5

---

### Optimization 4: Standardize Terminology (30 minutes)

**Goal:** Consistent terms across all prompts

**Decisions:**

**"Rationalization" vs "Consolidation":**
- **Choose:** "rationalization" (already in Pass 2 titles)
- **Update:** Change "consolidation" to "rationalization" where referring to the overall Pass 2 process
- **Keep:** "consolidation" when referring to specific act of combining items
- **Usage:** "Pass 2 rationalization includes consolidation, boundary correction, and verification"

**"Liberal extraction" vs "Over-extraction":**
- **Choose:** "liberal extraction" (less negative connotation)
- **Update:** Change "over-extraction" to "liberal extraction strategy"
- **Usage:** "Pass 1 uses liberal extraction with intentional over-capture"

**"RDMAP" usage:**
- **Acceptable:** Both "RDMAP" and "Research Designs, Methods, and Protocols"
- **Pattern:** First mention full, then RDMAP abbreviation
- **Consistency:** Use same pattern across all prompts

**Find/replace across all 5 prompts**

---

### Optimization 5: Standardize Reference Pointers (30 minutes)

**Goal:** Consistent format for pointing to reference files

**Current variations:**
- `→ See references/checklists/...`
- `For detailed X, see references/checklists/...`
- Inline pointers vs separate lines

**Recommended standard:**

**For inline pointers (brief reference):**
```markdown
→ See `references/checklists/tier-assignment-guide.md`
```

**For major references (detailed guidance):**
```markdown
**For complete [topic], see:**
`references/checklists/[file].md`
```

**At section start (overview):**
```markdown
**Supporting references:**
- `references/checklists/tier-assignment-guide.md` - Design/Method/Protocol decisions
- `references/checklists/consolidation-patterns.md` - Lumping vs splitting guidance
```

**Benefits:**
- Scannable (arrow symbol draws eye)
- Consistent format aids recognition
- Clear when brief vs major reference

**Prompts to update:** All 5

---

### Optimization 6: Verify Consolidation-Patterns Consistency (1-2 hours)

**Goal:** Ensure reference file matches what prompts say

**Tasks:**
1. Read `references/checklists/consolidation-patterns.md`
2. Compare patterns listed in Pass 2 prompts
3. Check examples consistency
4. Verify terminology alignment
5. Resolve any mismatches (update reference OR prompts)

**If inconsistencies found:**
- Reference is source of truth
- Update prompts to match reference
- Or update reference if prompts are better

**Prompts to check:**
- claims-evidence_pass2_prompt.md
- rdmap_pass2_prompt.md (after Phase 2 corrections)

---

### Optimization 7: Output Format Consolidation (20-30 minutes)

**Goal:** Don't repeat full JSON structure in every prompt

**Current:** Each prompt shows complete JSON output format (~20-30 lines)

**Proposed:**
- **Create:** `references/schema/output-format-examples.md` with complete examples
- **In prompts:** Show only relevant arrays + pointer to complete reference

**Example in RDMAP Pass 1 (after change):**
```markdown
## Output Format

**Return the same JSON document with RDMAP arrays populated:**

```json
{
  "schema_version": "2.5",
  "research_designs": [design_object],  // You populate these
  "methods": [method_object],            // You populate these
  "protocols": [protocol_object],        // You populate these
  
  // Leave untouched:
  "evidence": [...],
  "claims": [...],
  "implicit_arguments": [...]
}
```

**For complete object structure and field definitions:**
`references/schema/schema-guide.md`

**For complete output examples:**
`references/schema/output-format-examples.md`
```

**Token savings:** 20-30 lines per prompt × 5 prompts = 100-150 lines

---

## Phase 4 Summary

### Estimated Effort
| Optimization | Time | Tokens Saved | Benefit |
|--------------|------|--------------|---------|
| extraction-fundamentals.md | 3-4 hrs | 40-60 lines | Single source for core concepts |
| pass2-patterns.md | 2-3 hrs | 30-40 lines | Consistent Pass 2 guidance |
| Standardize structure | 2-3 hrs | 0 lines | Predictability, easier navigation |
| Standardize terminology | 30 min | 0 lines | Consistency, clarity |
| Standardize pointers | 30 min | 0 lines | Scannable, recognizable |
| Verify consolidation-patterns | 1-2 hrs | 0 lines | Accuracy, consistency |
| Output format consolidation | 30 min | 100-150 lines | Major token reduction |

**Total Phase 4 effort:** 10-14 hours  
**Total token reduction:** 170-250 lines (~8-10% across all prompts)  
**Primary benefits:** Maintainability, consistency, single source of truth

---

### Phase 4 Execution Order

**After completing Phases 1-3 and testing with 2-3 papers:**

1. **Quick wins first** (2 hours):
   - Standardize terminology
   - Standardize reference pointers
   - Verify consolidation-patterns consistency

2. **Structural changes** (3-4 hours):
   - Standardize prompt structure across all 5

3. **Reference creation** (6-8 hours):
   - Create extraction-fundamentals.md
   - Create pass2-patterns.md
   - Create output-format-examples.md
   - Update prompts to use new references

4. **Validation** (1-2 hours):
   - Test extraction with optimized prompts
   - Verify no quality loss
   - Confirm token reduction achieved

---

### When to Do Phase 4

**Recommended timing:**
1. ✅ Complete Phases 1-3 (critical fixes)
2. ✅ Run 2-3 full test extractions with corrected prompts
3. ✅ Identify which prompt sections actually cause confusion
4. ✅ Note which examples are helpful vs unhelpful
5. ✅ THEN do Phase 4 optimizations based on empirical data

**Why wait:**
- Real extraction experience reveals what matters most
- Avoid optimizing sections that work fine
- Focus optimization where highest ROI
- Premature optimization wastes effort on wrong problems

**Red flags to watch for during testing:**
- "This section is confusing" → Priority for Phase 4
- "Where do I find X guidance?" → Needs better pointer
- "This example didn't help" → Replace in Phase 4
- "I had to read this multiple times" → Streamline in Phase 4

---

## Complete Implementation Sequence

**Phase 1: RDMAP Pass 1 corrections** (20 min) → v2.5 functional  
**Phase 2: RDMAP Pass 2 corrections** (15 min) → v2.5 functional  
**Phase 3: Pass 3 enhancements** (15 min) → Complete validation  
**Phase 4: Testing** (4-9 hours) → 2-3 full paper extractions  
**Phase 5: Optimization** (10-14 hours) → Based on Phase 4 learnings  

**Total: 12-19 hours from broken prompts to optimized system**

---

## Ready to Execute?

**Updated plan now includes:**
✅ Critical fixes (Phases 1-3)  
✅ Optimization roadmap (Phase 4)  
✅ Timing guidance (test first, optimize second)  
✅ Complete effort estimates  

**Confirm plan before proceeding, or identify any adjustments needed.**

