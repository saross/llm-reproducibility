# Schema Guide Update - v2.4 to v2.5

**Date:** 2025-10-22  
**Task:** Phase 1, Task 1.3 - Update schema-guide.md to v2.5  
**Status:** ✅ Complete

---

## What Was Missing

**Critical Problem:** Schema-guide.md was still at v2.4, outdated by one full version. Extractors consulting the guide would get incorrect information that contradicts v2.5 prompts and schema.

**Impact:**
- Extractors wouldn't know verbatim_quote is REQUIRED
- No documentation of trigger infrastructure (trigger_text, trigger_locations)
- No guidance on RDMAP explicit vs implicit distinction
- No worked examples of implicit RDMAP objects
- References pointed to outdated schema files

---

## What Was Updated

### 1. Header and Version References ✅

**Changed:**
- Title: "Schema v2.4" → "Schema v2.5"
- JSON example: `"schema_version": "2.4"` → `"2.5"`
- File references: Updated from v2.4 split files to unified v2.5 schema

---

### 2. New Section: Schema v2.5 Updates (~65 lines) ✅

**Location:** Inserted after Overview, before Complete JSON Structure

**Content:**
- Overview of hallucination prevention goals
- Mandatory sourcing requirements for all object types
- Explicit content (Evidence/Claims): verbatim_quote REQUIRED
- Implicit content (Implicit Arguments): trigger infrastructure REQUIRED
- RDMAP explicit vs implicit overview
- Source verification object explanation
- Why this matters (hallucination problem explained)

**Key points covered:**
- Cannot extract without source
- Location tracking mandatory
- Verification enabled
- Zero tolerance for fabrication

---

### 3. Evidence Object Updated ✅

**Added to Required fields:**
- `verbatim_quote`: **REQUIRED** - Exact text from paper

**Added to Key fields:**
- `location`: Where verbatim_quote appears (elevated importance)
- `source_verification`: Pass 3 validation fields

**Added:**
- v2.5 Sourcing Rule statement
- Updated example showing verbatim_quote and source_verification

**Example now includes:**
```json
"verbatim_quote": "We collected 8,343 features across 22 sites during the survey",
"source_verification": {
  "location_verified": true,
  "quote_verified": true,
  "content_aligned": true,
  "verified_by": "validator"
}
```

---

### 4. Claim Object Updated ✅

**Added to Required fields:**
- `verbatim_quote`: **REQUIRED** - Exact text from paper

**Added to Key fields:**
- `location`: Where verbatim_quote appears
- `source_verification`: Pass 3 validation fields

**Added:**
- v2.5 Sourcing Rule statement
- Updated example with verbatim_quote and source_verification

**Same pattern as Evidence Object**

---

### 5. Implicit Argument Object Completely Rewritten ✅

**Transformed from minimal to comprehensive:**

**Old version (7 lines):**
- Basic purpose
- Type list
- Minimal example with no sourcing

**New version (~40 lines):**
- Complete Required fields list with trigger infrastructure
- All 5 types explained
- Key fields including source_verification
- v2.5 Sourcing Rule
- Comprehensive example showing:
  - trigger_text array (3 passages)
  - trigger_locations array (parallel)
  - inference_reasoning (full explanation)
  - source_verification object

**Example demonstrates:**
- Multiple trigger passages from different sections
- How passages together imply argument
- Proper inference reasoning explanation
- Verification that checks trigger validity

---

### 6. NEW Section: RDMAP Explicit vs Implicit (~160 lines) ✅

**Location:** After Protocol Object, before Cross-Reference Architecture

**Major addition covering:**

#### Explicit RDMAP
- Status field values
- Sourcing requirements (verbatim_quote)
- Location requirements (Methods section)
- Verification approach (same as Evidence/Claims)
- Complete worked example of explicit Method

#### Implicit RDMAP - Two Types
**Type 1: mentioned_undocumented**
- Tool/approach named but details missing
- Example: GPS mentioned but no specs
- Worked example: Protocol P015 (standard consumer GPS)
- Shows complete implicit_metadata structure

**Type 2: inferred_from_results**
- Never mentioned, inferred from outputs
- Example: Precision implies high-end equipment
- Worked example: Protocol P018 (sub-meter accuracy)
- Demonstrates low reconstruction_confidence

#### Critical Distinction
- Explicit: "Here's what we did" (verbatim_quote)
- Implicit: "Here's what they must have done" (trigger_text + inference)

**Both examples show:**
- Complete trigger infrastructure
- Full implicit_metadata (all 4 required fields)
- Source_verification object
- Proper confidence levels (medium vs low)

---

### 7. Consolidation Metadata ✅

**No change needed:** Already uses `consolidated_from` (correct)

---

### 8. References Section Updated ✅

**Changed from:**
- `schema-v2.4-claims.json`
- `schema-v2.4-rdmap.json`

**Changed to:**
- `extraction_schema_v2.5.json` (unified schema)
- References to extraction-fundamentals.md
- References to verification-procedures.md

**Reflects current architecture:** Unified schema file, supporting skill documents

---

## Coverage Analysis

### What's Now Documented ✅

**For Evidence & Claims:**
- verbatim_quote REQUIRED ✓
- Source verification object ✓
- v2.5 sourcing rules ✓
- Complete examples ✓

**For Implicit Arguments:**
- trigger_text REQUIRED ✓
- trigger_locations REQUIRED ✓
- inference_reasoning REQUIRED ✓
- Source verification object ✓
- Complete examples ✓

**For RDMAP Objects:**
- Explicit vs implicit distinction ✓
- Status fields ✓
- Sourcing requirements (both types) ✓
- Trigger infrastructure (implicit) ✓
- implicit_metadata structure ✓
- Two complete worked examples ✓

**General:**
- Hallucination prevention rationale ✓
- v2.5 breaking changes explained ✓
- References updated ✓

---

## File Statistics

**Original file:** 290 lines  
**Updated file:** 518 lines  
**Lines added:** 228 lines (79% increase)

**Major additions:**
- v2.5 Updates section: ~65 lines
- Evidence Object updates: ~15 lines
- Claim Object updates: ~15 lines
- Implicit Argument rewrite: ~25 lines (net)
- RDMAP Explicit vs Implicit: ~160 lines

---

## Integration Points

### With extraction_schema.json v2.5 ✅
- Documents all new required fields
- Explains status fields
- Shows trigger infrastructure
- Matches schema structure

### With extraction-fundamentals.md ✅
- References fundamental sourcing document
- Reinforces sourcing discipline
- Consistent terminology

### With verification-procedures.md ✅
- References verification procedures
- Source_verification objects explained
- Consistent with validation approach

### With All Prompts ✅
- Documents what prompts require
- Explains v2.5 sourcing rules
- Provides reference examples

---

## Quality Validation

### Consistency Checks ✅
- All examples use correct v2.5 structure
- Status fields shown correctly
- Trigger infrastructure complete
- implicit_metadata follows schema

### Completeness Checks ✅
- All six object types covered
- Both explicit and implicit documented
- Examples for all major patterns
- References comprehensive

### Accuracy Checks ✅
- Field names match schema exactly
- Required fields correctly identified
- Enum values accurate
- Structure consistent with schema

---

## Before vs After Comparison

### Evidence Object

**v2.4 (Old):**
```json
{
  "evidence_id": "E001",
  "evidence_text": "Survey collected 8,343 features",
  "supports_claims": ["C015"],
  "location": {"section": "Results"}
}
```

**v2.5 (New):**
```json
{
  "evidence_id": "E001",
  "evidence_text": "Survey collected 8,343 features across 22 sites",
  "verbatim_quote": "We collected 8,343 features across 22 sites during the survey",
  "location": {"section": "Results", "page": 8, "paragraph": 2},
  "supports_claims": ["C015"],
  "source_verification": {
    "location_verified": true,
    "quote_verified": true,
    "content_aligned": true,
    "verified_by": "validator"
  }
}
```

**Difference:** Now shows mandatory verbatim_quote and source_verification

---

### Implicit Argument Object

**v2.4 (Old):**
```json
{
  "implicit_argument_id": "IA001",
  "argument_text": "GPS accuracy is sufficient",
  "type": "methodological_assumption",
  "supports_claims": ["C008"]
}
```

**v2.5 (New):**
```json
{
  "implicit_argument_id": "IA001",
  "argument_text": "GPS accuracy is sufficient for archaeological survey purposes",
  "type": "methodological_assumption",
  "trigger_text": [
    "GPS units were used to record artifact locations",
    "spatial analysis conducted at site level",
    "precision adequate for landscape-scale interpretation"
  ],
  "trigger_locations": [
    {"section": "Methods", "paragraph": 2},
    {"section": "Methods", "paragraph": 5},
    {"section": "Discussion", "paragraph": 3}
  ],
  "inference_reasoning": "Methods mentions GPS use without stating accuracy. Analysis at 'site level' and 'landscape-scale' interpretation suggest moderate precision sufficient for archaeological purposes. Together these passages imply GPS accuracy adequate, though never explicitly stated.",
  "supports_claims": ["C008"],
  "source_verification": { ... }
}
```

**Difference:** Now shows complete trigger infrastructure and inference reasoning

---

### RDMAP Objects

**v2.4:** No explicit vs implicit distinction documented

**v2.5:** Complete section with:
- Status field explanation
- Explicit RDMAP example with verbatim_quote
- Implicit RDMAP example (mentioned_undocumented) with triggers
- Implicit RDMAP example (inferred_from_results) with low confidence
- implicit_metadata structure fully explained

---

## Next Steps

**Completed:**
- ✅ Task 1.1: Fix extraction_schema.json
- ✅ Task 1.2: Add RDMAP section to verification-procedures.md
- ✅ Task 1.3: Update schema-guide.md to v2.5

**Up next:**
- Task 1.4: Standardize skill references in all prompts
- Task 1.5: Add skill invocation to Pass 3 start
- Task 1.6: Add extraction-fundamentals to Pass 2 prompts
- Task 1.7: Standardize quality checklists

---

## Files Updated

**Location:** `/mnt/skills/user/research-assessor/references/schema/schema-guide.md`  
**Backup:** `/mnt/user-data/outputs/schema-guide_v2.5.md`

**The schema guide is now fully aligned with v2.5 requirements and can serve as authoritative reference for extractors.**

---

**Critical gap now closed:** Extractors consulting schema-guide.md will now get accurate v2.5 information that matches prompts, schema, and verification procedures.
