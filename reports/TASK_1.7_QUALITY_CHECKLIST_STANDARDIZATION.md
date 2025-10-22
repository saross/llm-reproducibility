# Task 1.7: Standardize Quality Checklists Across All Prompts

**Date:** 2025-10-22  
**Task:** Phase 1, Task 1.7 - Standardize quality checklists across all extraction prompts  
**Status:** ✅ Complete

---

## Problem

**Original issue:** Quality checklists varied across the 5 prompts in:
- Introductory text format ("Before finalizing" vs "Use this checklist as your roadmap")
- Level of detail for v2.5 sourcing requirements
- Emphasis/bolding inconsistency
- Granularity of sourcing checks

**Impact:**
- Inconsistent user experience across extraction passes
- Different levels of emphasis on critical v2.5 sourcing requirements
- Potential confusion about what's required at each pass

---

## Standardization Approach

### Principles Applied

1. **Pass-appropriate structure:** Pass 1 (extraction), Pass 2 (consolidation), Pass 3 (validation) have different focuses
2. **Consistent formatting within pass type:** All Pass 1s similar, all Pass 2s similar, Pass 3 unique
3. **V2.5 sourcing emphasis:** All checklists prominently feature sourcing requirements with bold formatting
4. **Domain-appropriate detail:** Claims/Evidence vs RDMAP checklists address domain-specific concerns

### What Changed vs What Stayed

**Changed:**
- claims-evidence Pass 1: Enhanced intro text and v2.5 sourcing granularity

**Already Good (No Changes):**
- RDMAP Pass 1: Already comprehensive
- Both Pass 2 prompts: Already consistent and comprehensive
- Pass 3 validation: Already well-structured with grouped format

---

## Changes Made

### Claims-Evidence Pass 1 Checklist

**Before:**
```markdown
## Quality Checklist for Pass 1

Before finalizing extraction:

- [ ] All potentially relevant evidence captured?
- [ ] All claims identified (core, intermediate, supporting)?
- [ ] Implicit arguments extracted for high-priority claims?
- [ ] **All items have verbatim_quote or trigger_text populated?**
- [ ] Evidence-claim support relationships mapped?
[... 5 more items]
```

**After:**
```markdown
## Quality Checklist for Pass 1

Use this checklist as your roadmap. Before finalizing:

- [ ] All potentially relevant evidence captured?
- [ ] All claims identified (core, intermediate, supporting)?
- [ ] Implicit arguments extracted for high-priority claims?
- [ ] **All evidence items have verbatim_quote populated**
- [ ] **All claims have verbatim_quote populated**
- [ ] **All implicit arguments have trigger_text, trigger_locations, inference_reasoning**
- [ ] Evidence-claim support relationships mapped?
- [ ] Expected information gaps flagged?
- [ ] Project metadata separated from evidence?
- [ ] All items have location tracking?
- [ ] Uncertain items marked in extraction_notes?
- [ ] **No hallucinations - only extract what's sourced**
- [ ] Other arrays (RDMAP) left unchanged?
```

**Key improvements:**
1. ✅ Added directive intro "Use this checklist as your roadmap" (matches RDMAP Pass 1)
2. ✅ Separated sourcing requirement into three specific items (evidence, claims, implicit args)
3. ✅ Added "No hallucinations" emphasis (matches RDMAP Pass 1)
4. ✅ More granular v2.5 sourcing checks

---

## Final Standardized Structure

### Pass 1 Checklists (Both)

**Common format:**
- Intro: "Use this checklist as your roadmap. Before finalizing:"
- 10-13 items covering:
  - Comprehensive capture items (domain-specific)
  - **Bolded v2.5 sourcing requirements** (3-5 items)
  - Relationship mapping
  - Location tracking
  - **Hallucination prevention emphasis**
  - Separation of concerns (don't touch other arrays)

**Claims-Evidence Pass 1 Sourcing Emphasis:**
- **All evidence items have verbatim_quote populated**
- **All claims have verbatim_quote populated**
- **All implicit arguments have trigger_text, trigger_locations, inference_reasoning**
- **No hallucinations - only extract what's sourced**

**RDMAP Pass 1 Sourcing Emphasis:**
- **Status fields set for all RDMAP items (explicit or implicit)**
- **All explicit items have verbatim_quote populated**
- **All implicit items have trigger_text, trigger_locations, inference_reasoning**
- **All implicit items have complete implicit_metadata**
- **No hallucinations - only extract what's sourced**

---

### Pass 2 Checklists (Both)

**Common format:**
- Intro: "Use this checklist as your roadmap. Before finalizing:"
- 15-16 items covering:
  - Reduction targets (15-20%)
  - Consolidation metadata
  - **Bolded source verification items** (3-4 items)
  - No information loss
  - Domain-specific quality checks
  - Cross-reference validation
  - Separation of concerns

**Claims-Evidence Pass 2 Sourcing Emphasis:**
- **Source verification complete for consolidations**
- **Evidence/claims verbatim_quotes preserved through consolidation**
- **Implicit argument trigger_text preserved through consolidation**

**RDMAP Pass 2 Sourcing Emphasis:**
- **Source verification complete for consolidations**
- **Status fields preserved/corrected after consolidation**
- **Explicit items maintain verbatim_quote integrity**
- **Implicit items maintain trigger_text integrity**

---

### Pass 3 Validation Checklist

**Unique grouped format** (appropriate for validation task):

```markdown
## Validation Checklist

Use this checklist as your roadmap. Execute all applicable checks:

**Cross-Reference Integrity:**
- [ ] All referenced IDs exist
- [ ] Bidirectional references consistent
- [ ] No orphaned objects (or appropriately flagged)

**Hierarchy Validation:**
- [ ] RDMAP chains valid (Design → Method → Protocol)
- [ ] Claims hierarchy valid (if claims present)
- [ ] Evidence chains valid (if evidence present)

**Schema Compliance:**
- [ ] Required fields present
- [ ] Enum values valid
- [ ] ID formats correct
- [ ] Location objects structured properly

**Source Verification:**
- [ ] All evidence/claims have verbatim_quote
- [ ] All implicit arguments have trigger_text and trigger_locations
- [ ] All RDMAP items properly sourced (explicit or implicit)
- [ ] Source verification fields populated
- [ ] Verification pass rates acceptable (>95%)

[... 3 more categories]
```

**Why different format:**
- Validation is checking multiple dimensions, not extracting
- Grouped categories make complex validation clearer
- Cross-functional checks (applies to both claims/evidence and RDMAP)
- Different cognitive task requires different structure

---

## Consistency Analysis

### What's Now Consistent ✅

**Across all Pass 1 prompts:**
- ✅ Same intro format
- ✅ Comprehensive v2.5 sourcing emphasis (3-5 bolded items)
- ✅ "No hallucinations" emphasis
- ✅ Similar structure and length
- ✅ Separation of concerns (don't touch other arrays)

**Across both Pass 2 prompts:**
- ✅ Same intro format
- ✅ Source verification emphasis for consolidations
- ✅ Similar structure and length
- ✅ Domain-appropriate items

**Pass 3 validation:**
- ✅ Appropriate grouped format for validation task
- ✅ Comprehensive sourcing checks across all object types

### What's Appropriately Different ✅

**Domain-specific items:**
- Claims-evidence: "Multi-dimensional evidence", "Anchor numbers", "Calculation claims"
- RDMAP: "Tier assignments", "Status fields", "Reasoning approaches"

**Pass-specific focus:**
- Pass 1: Comprehensive capture
- Pass 2: Consolidation quality
- Pass 3: Validation completeness

---

## Validation Metrics

### V2.5 Sourcing Coverage

**All checklists now explicitly check:**
- ✅ verbatim_quote presence (explicit content)
- ✅ trigger_text + trigger_locations presence (implicit content)
- ✅ Hallucination prevention
- ✅ Source verification (Pass 2 consolidations, Pass 3 validation)

**RDMAP-specific additions:**
- ✅ Status field accuracy (explicit vs implicit)
- ✅ implicit_metadata completeness
- ✅ Trigger_text preservation through consolidation

### Formatting Consistency

**All checklists use:**
- ✅ Markdown checkbox format `- [ ]`
- ✅ Bold formatting for critical v2.5 items
- ✅ Question marks for open-ended checks
- ✅ Specific requirements without question marks

---

## Before vs After Summary

### Claims-Evidence Pass 1

| Aspect | Before | After |
|--------|--------|-------|
| Intro | "Before finalizing extraction:" | "Use this checklist as your roadmap. Before finalizing:" |
| Sourcing items | 1 combined item | 3 separated items + hallucination emphasis |
| Granularity | Generic "verbatim_quote or trigger_text" | Specific: evidence, claims, implicit args |
| Emphasis | Moderate | Strong (matches RDMAP Pass 1) |

### All Other Checklists

| Checklist | Status |
|-----------|--------|
| RDMAP Pass 1 | Already excellent - no changes |
| Claims-Evidence Pass 2 | Already good - no changes |
| RDMAP Pass 2 | Already good - no changes |
| Pass 3 Validation | Already excellent - no changes |

---

## Integration Points

**Works with:**
- ✅ Task 1.1: Schema has source_verification fields
- ✅ Task 1.2: verification-procedures.md has validation guidance
- ✅ Task 1.3: schema-guide.md documents v2.5 requirements
- ✅ Task 1.4: References use standard format
- ✅ Task 1.5: Pass 3 has prominent skill invocation
- ✅ Task 1.6: Pass 2 prompts have sourcing reminders

**Enables:**
- Consistent user experience across all extraction passes
- Clear emphasis on v2.5 sourcing requirements throughout workflow
- Appropriate level of detail for each pass type
- Quality checks aligned with v2.5 hallucination prevention goals

---

## Files Updated

### Primary Changes

**Input:** `/mnt/user-data/uploads/claims-evidence_pass1_prompt.md`  
**Output:** `/mnt/user-data/outputs/claims-evidence_pass1_prompt_v2.5_final.md`  
**Changes:** Enhanced checklist with separated sourcing items and directive intro

### Already Standardized (Verified, No Changes)

**Files confirmed as already meeting standards:**
- `/mnt/user-data/outputs/rdmap_pass1_prompt_v2.5_final.md` (copied as-is)
- `/mnt/user-data/outputs/claims-evidence_pass2_prompt_v2.5_final.md` (from Task 1.6)
- `/mnt/user-data/outputs/rdmap_pass2_prompt_v2.5_final.md` (from Task 1.6)
- `/mnt/user-data/outputs/rdmap_pass3_prompt_v2.5_final.md` (from Task 1.5)

---

## Checklist Coverage Matrix

### Pass 1: Extraction Quality

| Check Type | C/E Pass 1 | RDMAP Pass 1 |
|------------|------------|--------------|
| Comprehensive capture | ✓ | ✓ |
| verbatim_quote emphasis | ✓ (3 items) | ✓ (2 items) |
| trigger_text emphasis | ✓ (1 item) | ✓ (2 items) |
| Status fields | N/A | ✓ |
| implicit_metadata | N/A | ✓ |
| Hallucination prevention | ✓ | ✓ |
| Relationship mapping | ✓ | ✓ |
| Location tracking | ✓ | ✓ |
| Separation of concerns | ✓ | ✓ |

### Pass 2: Consolidation Quality

| Check Type | C/E Pass 2 | RDMAP Pass 2 |
|------------|------------|--------------|
| Reduction target | ✓ | ✓ |
| Consolidation metadata | ✓ | ✓ |
| Source verification | ✓ | ✓ |
| verbatim_quote preservation | ✓ | ✓ |
| trigger_text preservation | ✓ | ✓ |
| Status field accuracy | N/A | ✓ |
| No information loss | ✓ | ✓ |
| Relationship validation | ✓ | ✓ |
| Domain-specific checks | ✓ | ✓ |
| Separation of concerns | ✓ | ✓ |

### Pass 3: Validation Completeness

| Check Category | Coverage |
|----------------|----------|
| Cross-Reference Integrity | ✓ |
| Hierarchy Validation | ✓ |
| Schema Compliance | ✓ |
| Source Verification | ✓ (all object types) |
| Expected Information | ✓ |
| Consolidation Metadata | ✓ |
| Type Consistency | ✓ |

---

## Expected Impact

**For extractors:**
- Clear, consistent guidance across all passes
- Strong emphasis on v2.5 sourcing requirements
- No confusion about what's required at each stage

**For quality:**
- Higher compliance with sourcing requirements
- Fewer hallucinations
- Better Pass 3 validation pass rates (>95% target)

**For maintenance:**
- Consistent patterns make updates easier
- Clear structure for future enhancements

---

## Lessons for Future Checklist Design

1. **Pass-appropriate structure:** Extraction, consolidation, and validation need different formats
2. **Progressive emphasis:** Pass 1 emphasizes capture, Pass 2 emphasizes preservation, Pass 3 emphasizes validation
3. **Domain-specific items:** Generic checklists don't work - tailor to claims/evidence vs RDMAP
4. **Bold critical items:** v2.5 sourcing requirements must stand out visually
5. **Granular checks:** "All items have quotes" too vague - separate by object type
6. **Grouped categories:** Complex validation benefits from categorization (Pass 3)

---

**Task 1.7 Complete** - Quality checklists are now standardized across all 5 prompts with consistent formatting, comprehensive v2.5 sourcing emphasis, and pass-appropriate structure.
