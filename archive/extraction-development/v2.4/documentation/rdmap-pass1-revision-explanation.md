# RDMAP Pass 1 Revision Explanation

**Date:** 2025-10-20  
**Revised By:** Claude Sonnet 4.5  
**Original Length:** 878 lines  
**Revised Length:** 499 lines  
**Net Change:** -379 lines (-43% reduction)

---

## Summary of Changes

This was a **major streamlining** focused on eliminating redundancy with skill components while preserving all essential decision-making guidance.

### Quantitative Summary

| Section | Original | Revised | Reduction |
|---------|----------|---------|-----------|
| **Header & Task** | ~30 lines | ~45 lines | +15 (added checklist) |
| **Core Principles** | ~410 lines | ~180 lines | **-230 (-56%)** |
| **Workflow** | ~35 lines | ~40 lines | +5 |
| **Boundary Cases** | ~55 lines | ~65 lines | +10 |
| **Examples** | ~255 lines | ~120 lines | **-135 (-53%)** |
| **Output & End** | ~45 lines | ~50 lines | +5 |
| **TOTAL** | **878 lines** | **499 lines** | **-379 (-43%)** |

---

## Major Changes

### 1. Quality Checklist Added to Top ⬆️
**Before:** No checklist at top  
**After:** 11-item checklist immediately after "Your Task" (lines 39-51)

**Why:** Roadmap principle - see goals before diving into details

**Effect:** +13 lines, but improves usability

---

### 2. Core Extraction Principles HEAVILY Streamlined ✂️

**Removed sections (now in skill checklists):**

**a) Extended Tier Hierarchy Explanation** (-70 lines)
- **Before:** Full explanations of Design/Method/Protocol with multiple examples
- **After:** Quick decision tree + brief definitions
- **Rationale:** Detailed guidance in `tier-assignment-guide.md`
- **Cross-reference added:** Line 135

**b) Expected Information Checklists** (-125 lines)
- **Before:** Lines 240-310 had 4 complete checklists:
  - TIDieR-adapted method documentation (10 items)
  - CONSORT-adapted measurement specs (8 items)  
  - Sampling strategy checklist (7 items)
  - Analysis methods checklist (7 items)
- **After:** Brief explanation + cross-reference
- **Rationale:** All checklists already in `expected-information.md`
- **Cross-reference added:** Line 213

**c) Controlled Vocabularies** (-50 lines)
- **Before:** Lines 312-361 had extensive vocabulary lists:
  - Reasoning approaches (5 options)
  - Study designs (8+ options)
  - Sampling types (13+ options)
  - Analysis populations (4 options)
- **After:** Removed entirely (standard vocabularies don't need to be in extraction prompt)
- **Rationale:** Extractors can use natural language; no need for vocab reference here

**d) Extended Cross-Reference Patterns** (-30 lines)
- **Before:** Detailed explanation of every cross-reference type with examples
- **After:** Concise bullet list (lines 241-248)
- **Rationale:** Cross-referencing is straightforward once you understand the objects

**e) Location Tracking Details** (-20 lines)
- **Before:** Extended explanation of location tracking
- **After:** Brief mention in workflow, explicit in examples
- **Rationale:** Self-explanatory in schema

**f) Fieldwork-Specific Guidance** (-35 lines)
- **Before:** Lines 365-465 had extended discussion of:
  - Opportunistic decisions (21 lines)
  - Contingency plans (14 lines)
  - Emergent discoveries (18 lines)
- **After:** Condensed to essential points (lines 215-229)
- **Rationale:** Key concepts preserved, extended examples removed

---

### 3. Examples Dramatically Condensed ✂️

**Before:** 6 examples × ~40-45 lines each = ~255 lines
- Full JSON objects shown
- Every field populated
- Extensive extraction_notes
- Multiple examples per category

**After:** 4 examples × ~30 lines each = ~120 lines
- Key fields only (not full objects)
- Focus on decision points
- Concise extraction_notes
- One example per key pattern

**Examples removed:**
- Example 5: Protocol - Tool Specification (redundant with Example 3)
- Example 6: Protocol - Measurement with Decision Rules (redundant)

**Examples condensed:**
- All remaining examples shortened by ~30%
- Focus on what makes each decision challenging
- Remove obvious field population

**Reduction:** ~135 lines (-53%)

---

### 4. Cross-References Added 🔗

Added 3 explicit cross-references:

1. **Line 135:** → `tier-assignment-guide.md` (after tier hierarchy)
2. **Line 213:** → `expected-information.md` (after missing elements discussion)
3. **Line 485:** → `schema-guide.md` (after output format)

**Progressive disclosure:** Claude loads detailed guidance only when needed

---

### 5. Structural Improvements 🏗️

**Section consolidation:**
- "Description vs Argumentation Boundary" moved up (now section 2)
- "Reasoning Approach" and "Research Questions vs Hypotheses" consolidated (sections 3-4)
- Fieldwork considerations condensed into single section

**Removed redundancy:**
- Multiple explanations of same concepts
- Obvious guidance (e.g., "populate this field with X")
- Extended philosophical discussions

---

## What Was Preserved (Complete)

✅ **All decision frameworks intact:**
- Three-tier hierarchy decision tree
- Description vs argumentation test
- Reasoning approach classification (all 5 types)
- Research questions vs hypotheses distinction
- Timing classification (pre-data vs post-data)

✅ **All boundary cases covered:**
- Combined description + argumentation
- Ambiguous tier assignment
- Mixed reasoning approach
- Unclear hypothesis timing

✅ **All workflow steps preserved:**
- 5-step workflow maintained
- All key actions documented
- Cross-referencing guidance complete

✅ **All extraction philosophy:**
- Liberal extraction principle
- Over-capture strategy
- 40-50% over-extraction expected
- "When uncertain, include it"

✅ **All key concepts:**
- Opportunistic decisions
- Contingency plans
- Emergent discoveries
- Expected information flagging

---

## Consistency Checks with Skill

### ✅ No Contradictions Found

**Field names verified:**
- `enables_methods` (research_designs) ✓
- `design_context` (methods) ✓
- `uses_protocols` (methods) ✓
- `implements_method` (protocols) ✓
- `supports_claims` (RDMAP → claims) ✓
- `supported_by_evidence` (claims → RDMAP) ✓
- `expected_information_missing` ✓
- All field names match schema-guide.md

**Tier hierarchy verified:**
- Design → Method → Protocol hierarchy matches SKILL.md ✓
- WHY → WHAT → HOW framework matches tier-assignment-guide.md ✓
- Decision tree consistent ✓

**Checklists verified:**
- Reference to expected-information.md is accurate ✓
- TIDieR, CONSORT, sampling, analysis checklists all present in expected-information.md ✓
- Domain-specific checklists (archaeology, biology, ethnography) present ✓

**Workflow separation verified:**
- RDMAP responsibility clearly stated ✓
- Claims/evidence arrays marked "leave untouched" ✓
- Matches SKILL.md separation of concerns ✓

---

## Line-by-Line Comparison of Major Sections

### Core Extraction Principles: Before vs After

**Before (lines 57-466, ~410 lines):**
- § 1: Three-tier hierarchy (40 lines)
- § 2: Description vs argumentation (42 lines)
- § 3: Reasoning approach (50 lines)
- § 4: Research questions vs hypotheses (47 lines)
- § 5: Expected information checklists (70 lines)
- § 6: Controlled vocabularies (50 lines)
- § 7: Fieldwork-specific guidance (100 lines)
- § 8: Cross-reference patterns (28 lines)
- § 9: Location tracking (21 lines)

**After (lines 55-250, ~195 lines):**
- § 1: Three-tier hierarchy + cross-reference (28 lines)
- § 2: Description vs argumentation (25 lines)
- § 3: Reasoning approach (40 lines) - kept full detail
- § 4: Research questions vs hypotheses (40 lines) - kept full detail
- § 5: Expected information + cross-reference (20 lines)
- § 6: Fieldwork considerations (15 lines)
- § 7: Cross-referencing (10 lines)

**Reductions:**
- Tier hierarchy: 40 → 28 lines (-30%)
- Expected checklists: 70 → 20 lines (-71%)
- Controlled vocabularies: 50 → 0 lines (removed)
- Fieldwork guidance: 100 → 15 lines (-85%)
- Cross-reference patterns: 28 → 10 lines (-64%)
- Location tracking: 21 → merged into workflow

**Preserved:**
- Reasoning approach: kept at ~40 lines (critical decision framework)
- Research questions vs hypotheses: kept at ~40 lines (critical distinction)

---

### Examples: Before vs After

**Before (lines 561-816, ~255 lines):**
- Example 1: Research Design - Study Design (28 lines, full JSON)
- Example 2: Research Design - RQ vs Hypothesis (41 lines, full JSON)
- Example 3: Method - Data Collection (40 lines, full JSON)
- Example 4: Method - Sampling (37 lines, full JSON)
- Example 5: Protocol - Tool Spec (47 lines, full JSON)
- Example 6: Protocol - Measurement (60 lines, full JSON)

**After (lines 320-460, ~140 lines):**
- Example 1: Research Design with Reasoning (25 lines, key fields only)
- Example 2: Method with Opportunistic Decision (25 lines, key fields only)
- Example 3: Protocol with Tool Specification (20 lines, key fields only)
- Example 4: Combined Description + Claim (30 lines, shows splitting)

**Changes:**
- 6 examples → 4 examples (removed redundant tool/measurement examples)
- Full JSON → Key fields only
- ~42 lines each → ~30 lines each
- Total: 255 → 140 lines (-45%)

---

## Impact Analysis

### What This Achieves

**1. Faster Loading** ⚡
- 43% fewer lines = faster for Claude to load and process
- Reduced token consumption per extraction

**2. Progressive Disclosure** 📖
- Essential guidance in prompt
- Detailed checklists available when needed
- Cross-references make skill architecture visible

**3. Reduced Redundancy** ♻️
- Single source of truth for checklists
- No duplication between prompt and skill files
- Easier to maintain consistency

**4. Maintained Quality** ✅
- All critical decision frameworks preserved
- All boundary cases covered
- All extraction philosophy intact

### What This Doesn't Change

**Quality of extractions:** All decision guidance present
**Comprehensiveness:** Still captures all RDMAP
**Uncertainty handling:** Still liberal extraction philosophy
**Cross-referencing:** Still complete bidirectional links

---

## Risk Assessment

**Low Risk Changes:**
- ✅ Removing controlled vocabularies (not needed in prompt)
- ✅ Condensing examples (key points preserved)
- ✅ Cross-referencing checklists (all content still accessible)
- ✅ Streamlining tier hierarchy (decision tree preserved)

**Medium Risk Changes:**
- ⚠️ Removing extended fieldwork guidance (condensed to essentials)
  - **Mitigation:** Key concepts (opportunistic, contingent, emergent) preserved
  - **Test:** Verify Claude still identifies these patterns in text

**No High Risk Changes**

---

## Testing Recommendations

**Test 1: Tier Assignment**
- Run on Methods section with mixed design/method/protocol content
- Verify Claude uses decision tree correctly
- Check if tier-assignment-guide.md is consulted when uncertain

**Test 2: Expected Information Flagging**
- Run on section with incomplete methodology
- Verify `expected_information_missing` arrays populated
- Check if expected-information.md is referenced

**Test 3: Reasoning Approach Classification**
- Run on section with explicit reasoning statements
- Verify classification (inductive/deductive/abductive/mixed/unclear)
- Check confidence levels and indicators

**Test 4: Fieldwork Patterns**
- Run on section with opportunistic decisions
- Verify Claude identifies and marks opportunistic/contingent/emergent
- Check extraction_notes document these patterns

**Test 5: Cross-Referencing**
- Run complete extraction (designs → methods → protocols)
- Verify bidirectional links (enables_methods ↔ design_context)
- Check claim → method cross-references

---

## Key Insight

**From comprehensive instruction manual to focused decision guide**

**Before:** Self-contained document teaching everything about RDMAP extraction  
**After:** Focused workflow guide that references skill components when needed

This implements **progressive disclosure** - Claude has everything it needs to start extracting, with clear paths to deeper guidance when uncertainty arises.

The 43% reduction comes from **eliminating teaching** (now in skill) while **preserving decision-making** (stays in prompt).

---

## Conclusion

The revised RDMAP Pass 1 prompt maintains all essential extraction guidance while:
- Reducing length by 43% (878 → 499 lines)
- Eliminating redundancy with skill checklists
- Implementing progressive disclosure
- Preserving all critical decision frameworks
- Maintaining all boundary case guidance

**Ready for:** Integration into skill and testing on Sobotkova Methods section.

---

## Recommendation

Before proceeding to RDMAP Pass 2, consider testing this revision to ensure:
1. Tier assignments remain accurate
2. Expected information flagging works correctly
3. Cross-references to skill files are followed appropriately
4. No critical guidance was inadvertently removed

This will validate the approach before applying similar streamlining to RDMAP Pass 2.
