# Claims-Evidence Pass2 Prompt - Correction Summary

**Date:** 2025-10-22  
**Status:** ⚠️ INCONSISTENCIES FOUND & CORRECTED

---

## Issue Discovered

The claims-evidence Pass 2 prompt was **not fully updated** with v2.5 source verification requirements, making it inconsistent with:
1. The RDMAP Pass 2 prompt (which was properly updated)
2. The research-assessor skill (which has verification-procedures.md)
3. Schema v2.5 requirements (which mandate source verification)

---

## Critical Gaps Found

### 1. Quality Checklist Missing Source Verification Items
**Missing:**
- Source verification complete for consolidations
- Evidence/claims verbatim_quotes preserved
- Implicit argument trigger_text preserved

**Impact:** Extractors not reminded to verify source integrity during consolidation

### 2. Inadequate Source Verification Section
**Found:** 4-line note in STEP 2
**Missing:**
- Separate guidance for explicit items (verbatim_quote)
- Guidance for implicit arguments (trigger_text, trigger_locations)
- Reference to verification-procedures.md
- Guidance on adding implicit items in Pass 2

**Impact:** No guidance for implicit arguments, which use different sourcing mechanism

### 3. No Reference to Skill Documentation
**Missing:** `/mnt/skills/user/research-assessor/references/verification-procedures.md`

**Impact:** Extractors don't know where to find detailed verification procedures

### 4. Quality Checks Incomplete
**Missing:**
- Verification of verbatim_quotes
- Verification of trigger_text for implicit arguments
- Consolidated items preserve source integrity

**Impact:** Final quality checks don't ensure v2.5 compliance

---

## Corrections Applied

### ✅ Update 1: Quality Checklist (Lines 35-38)
Added three source verification items:
```markdown
- [ ] **Source verification complete for consolidations**
- [ ] **Evidence/claims verbatim_quotes preserved through consolidation**
- [ ] **Implicit argument trigger_text preserved through consolidation**
```

### ✅ Update 2: Expanded Source Verification Section (Lines 249-296)
Replaced 4-line note with full section matching RDMAP Pass2 structure:
- "🚨 Source Verification for Consolidations (v2.5)" heading
- Separate guidance for evidence/claims (explicit items)
- Separate guidance for implicit arguments
- Adding implicit arguments in Pass 2 requirements
- Reference to verification-procedures.md
- Pass 2 verification focus points

### ✅ Update 3: Enhanced Quality Checks (Lines 267-275)
Added explicit source verification checks:
```markdown
- **All evidence/claims have verified verbatim_quotes**
- **All implicit arguments have verified trigger_text and trigger_locations**
- **Consolidated items preserve source integrity**
```

---

## Comparison with RDMAP Pass2

### Before Correction:
| Feature | RDMAP Pass2 | Claims-Evidence Pass2 |
|---------|-------------|----------------------|
| Quality checklist source items | ✅ Yes (4 items) | ❌ No |
| Full source verification section | ✅ Yes (~40 lines) | ❌ No (4 lines) |
| Implicit item guidance | ✅ Yes | ❌ No |
| References verification-procedures.md | ✅ Yes | ❌ No |
| Enhanced quality checks | ✅ Yes | ⚠️ Partial |

### After Correction:
| Feature | RDMAP Pass2 | Claims-Evidence Pass2 |
|---------|-------------|----------------------|
| Quality checklist source items | ✅ Yes (4 items) | ✅ Yes (3 items) |
| Full source verification section | ✅ Yes (~40 lines) | ✅ Yes (~45 lines) |
| Implicit item guidance | ✅ Yes | ✅ Yes |
| References verification-procedures.md | ✅ Yes | ✅ Yes |
| Enhanced quality checks | ✅ Yes | ✅ Yes |

---

## Why This Matters

### 1. Schema v2.5 Compliance
All extracted items must have proper sourcing:
- **Evidence/Claims:** verbatim_quote required
- **Implicit Arguments:** trigger_text + trigger_locations required

Without explicit guidance, consolidations may lose this traceability.

### 2. Different Sourcing Mechanisms
Evidence/claims are always explicit (verbatim_quote), but implicit arguments use a different mechanism (trigger_text array). The brief note in the original didn't cover this distinction.

### 3. Skill Architecture Consistency
Both Pass 2 prompts should reference the same skill resources:
- verification-procedures.md for detailed procedures
- Same structure and emphasis on source verification

### 4. Hallucination Prevention
v2.5's entire sourcing discipline exists to prevent hallucinated content. Pass 2 consolidations are a critical point where source integrity can be lost if not carefully verified.

---

## Files Produced

1. **claims-evidence_pass2_analysis.md** - Detailed comparison and analysis
2. **claims-evidence_pass2_prompt_v2.5_corrected.md** - Corrected version with all updates applied

---

## Verification

**Changes verified against:**
- ✅ RDMAP Pass 2 prompt (used as model)
- ✅ Schema v2.5 requirements (verbatim_quote and trigger_text fields)
- ✅ Research-assessor skill (references verification-procedures.md correctly)
- ✅ Extraction-fundamentals.md (sourcing discipline principles)

**Quality assurance:**
- ✅ All three updates applied
- ✅ No changes to working content (consolidation patterns, etc.)
- ✅ Consistent structure with RDMAP Pass2
- ✅ Covers both explicit (evidence/claims) and implicit (implicit arguments)
- ✅ References skill documentation appropriately

---

## Recommended Next Steps

1. **Review the corrected version** against your requirements
2. **Test with real extraction** to verify guidance is clear
3. **Replace the current claims-evidence_pass2_prompt.md** in your repo
4. **Consider:** Both Pass 1 prompts (claims-evidence and RDMAP) should also reference extraction-fundamentals.md at the start for universal sourcing requirements

---

## Summary

**Original status:** Inconsistent with v2.5 requirements and RDMAP Pass2 structure  
**Corrected status:** Fully aligned with schema v2.5, RDMAP Pass2, and skill architecture  
**Priority:** HIGH - Source verification is critical for hallucination prevention  
**Recommendation:** Deploy corrected version
