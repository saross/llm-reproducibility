# Skill Reference Standardization - All Prompts

**Date:** 2025-10-22  
**Task:** Phase 1, Task 1.4 - Standardize skill references across all prompts  
**Status:** ✅ Complete

---

## Standardization Pattern

**Established pattern:**
1. **First mention (prominent section):** `**READ FIRST:** /mnt/skills/user/research-assessor/references/file.md`
2. **Subsequent mentions:** `→ See references/file.md` (with backticks around path)

---

## Files Already Correct ✅

**No changes needed:**
- claims-evidence_pass1_prompt.md - Already using standard format
- rdmap_pass1_prompt.md - Already using standard format

---

## Files Updated

### 1. claims-evidence_pass2_prompt.md ✅

**Change:** Line 292  
**Before:** `/mnt/skills/user/research-assessor/references/verification-procedures.md` (bare full path)  
**After:** `→ See references/verification-procedures.md` (standardized subsequent-mention format)

**Result:** All references now use short form with arrow

---

### 2. rdmap_pass2_prompt.md ✅

**Change:** Line 425  
**Before:** `/mnt/skills/user/research-assessor/references/verification-procedures.md` (bare full path)  
**After:** `→ See references/verification-procedures.md` (standardized subsequent-mention format)

**Result:** All references now use short form with arrow

---

### 3. rdmap_pass3_prompt.md ✅

**Multiple changes to achieve consistency:**

**Line 122:**  
**Before:** `→ See /mnt/skills/user/research-assessor/references/verification-procedures.md`  
**After:** `→ See references/verification-procedures.md`

**Line 149:**  
**Before:** `→ See verification-procedures.md` (no backticks)  
**After:** `→ See references/verification-procedures.md` (with backticks and full relative path)

**Line 218 (Main invocation):**  
**Before:** `**Read first:** /mnt/skills/user/research-assessor/references/verification-procedures.md` (lowercase)  
**After:** `**READ FIRST:** /mnt/skills/user/research-assessor/references/verification-procedures.md` (uppercase)

**Line 279:**  
**Before:** `→ See verification-procedures.md section on RDMAP` (no backticks)  
**After:** `→ See references/verification-procedures.md section on RDMAP` (with backticks)

**Line 321:**  
**Before:** `**See verification-procedures.md for complete...` (bolded, no arrow, no backticks)  
**After:** `→ See references/verification-procedures.md for complete...` (arrow, backticks)

**Result:** All references now standardized with consistent formatting

---

## Verification

**All 5 prompts now follow consistent pattern:**
- ✅ claims-evidence_pass1_prompt.md - Consistent
- ✅ claims-evidence_pass2_prompt.md - Standardized
- ✅ rdmap_pass1_prompt.md - Consistent  
- ✅ rdmap_pass2_prompt.md - Standardized
- ✅ rdmap_pass3_prompt.md - Standardized

---

## Reference Format Summary

### First Mention (Prominent)
```markdown
**READ FIRST:** `/mnt/skills/user/research-assessor/references/extraction-fundamentals.md`
```

### Subsequent Mentions
```markdown
→ See `references/extraction-fundamentals.md`
```

### With Section Reference
```markdown
→ See `references/verification-procedures.md` section on RDMAP validation
```

---

## Impact

**Benefits of standardization:**
- Consistent visual cues across all prompts
- Clear distinction between first-mention and subsequent references
- Easier maintenance (pattern is obvious)
- Professional appearance
- Reduced cognitive load for readers

**Files updated:**
- `/mnt/user-data/outputs/claims-evidence_pass2_prompt_standardized.md`
- `/mnt/user-data/outputs/rdmap_pass2_prompt_standardized.md`
- `/mnt/user-data/outputs/rdmap_pass3_prompt_standardized.md`

---

**Task 1.4 Complete** - All skill references now follow consistent, professional formatting across all 5 extraction prompts.
