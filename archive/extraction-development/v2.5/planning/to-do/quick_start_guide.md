# Quick Start: Fixing Source Verification Failures

**Updated:** October 24, 2025  
**Status:** Phase 1 COMPLETE - Ready for Phase 2  
**Time to implement:** 15 minutes

---

## ✅ What's Already Done (Phase 1)

Your `research-assessor` skill has been enhanced with:

1. **Detailed verbatim requirements** (12 KB)
   - `/mnt/skills/user/research-assessor/references/verbatim-quote-requirements.md`
   - Complete guidance on what "verbatim" means
   - 5 failure patterns explained with examples
   - Good vs bad examples for each case

2. **Updated extraction fundamentals**
   - `/mnt/skills/user/research-assessor/references/extraction-fundamentals.md`
   - Pointer to verbatim requirements
   - Brief summary of key rules

3. **Quote verification script** (12 KB)
   - `/mnt/skills/user/research-assessor/scripts/verify_quotes.py`
   - Detects common failure patterns
   - Provides fix suggestions
   - Run between Pass 1 and Pass 2

**These files are ready to use immediately.**

---

## 📋 What You Need to Do (Phase 2) - 15 Minutes

Update your 4 extraction prompts with minimal additions.

### Step 1: Update Claims Pass 1 Prompt

**Location:** Your claims extraction Pass 1 prompt file

**Action:** Add this section after task description, before extraction instructions:

```markdown
## 🚨 CRITICAL: Verbatim Quote Requirements

**Before extracting any item, read:**  
`/mnt/skills/user/research-assessor/references/verbatim-quote-requirements.md`

**Non-negotiable rules:**
1. **Extract complete sentences only** - No mid-sentence fragments
2. **Copy-paste exact text** - No paraphrasing or reconstruction  
3. **Verify quote exists** - Search paper before committing to JSON
4. **Single source location** - No synthesizing from multiple passages

**Quick test:** "Can I find this exact text with simple search?"
- If NO → Fix quote or mark as implicit
- If YES → Proceed with extraction

**Failure to follow these rules causes 40-50% validation failures and blocks assessment.**
```

---

### Step 2: Update RDMAP Pass 1 Prompt

**Location:** Your RDMAP extraction Pass 1 prompt file

**Action:** Add the same section as Step 1

---

### Step 3: Update Claims Pass 2 Prompt

**Location:** Your claims rationalization Pass 2 prompt file

**Action:** Add this in the consolidation workflow section:

```markdown
### Step 4: Source Verification

**Before finalizing consolidations, verify all quotes:**

For each item being kept:
1. Check verbatim_quote follows requirements in `references/verbatim-quote-requirements.md`
2. Search for exact quote in paper
3. If quote not found → Locate actual text and update
4. If quote is paraphrased → Replace with true verbatim text
5. If quote is synthesized → Split into separate items

**Common fixes needed:**
- Add missing sentence beginnings/endings
- Replace paraphrases with exact text
- Split multi-source quotes into separate items

**Mark suspicious items:**
```json
{
  "extraction_confidence": "low",
  "extraction_notes": "Quote verification uncertain - needs Pass 3 review"
}
```
```

---

### Step 4: Update RDMAP Pass 2 Prompt

**Location:** Your RDMAP rationalization Pass 2 prompt file

**Action:** Add the same section as Step 3

---

## Expected Results

### Current State (Sobotkova)
```
Pass Rate: 53%
Status:    FAIL - blocks assessment
Issues:    67 items failed source verification
```

### After Phase 2 (Skill + Prompt Updates)
```
Expected:  85-90% pass rate
Status:    PASS WITH ISSUES
Issues:    ~5-10 items may still fail
```

### If Needed: Phase 3 (+ Verification Script)
```
Expected:  95-98% pass rate
Status:    PASS - assessment ready
Issues:    0-2 items per paper
```

---

## Testing Your Changes

### Quick Test (Recommended)

1. Pick a short paper for testing
2. Run Pass 1 extraction with updated prompts
3. Check a few quotes manually:
   - Can you find exact text in paper?
   - Are sentences complete?
   - Any paraphrasing?
4. Run Pass 3 validation
5. Check pass rate

**Success:** >85% pass rate → Deploy!  
**Needs work:** <85% → Add Phase 3 (verification script)

---

### Full Test (Optional)

1. Re-extract Sobotkova paper with new prompts
2. Compare to original extraction
3. Run Pass 3 validation
4. Compare pass rates:
   - Old: 53%
   - New: Should be >85%
5. Review any remaining failures

---

## Using the Verification Script (Phase 3 - Optional)

If your pass rate is still <95% after Phase 2, use the verification script:

### Basic Usage

```bash
python /mnt/skills/user/research-assessor/scripts/verify_quotes.py \
    your_extraction_pass1.json \
    paper.md
```

### Integration in Workflow

```
1. Run Pass 1 extraction with new prompts
   ↓
2. Run verification script
   ↓
3. Review failures and fix common patterns
   ↓
4. Run Pass 2 rationalization
   ↓
5. Run Pass 3 validation
   ↓
6. Should achieve >95% pass rate
```

---

## Troubleshooting

### If pass rate is still <85%:

**Check:**
1. Did Claude read the verbatim requirements file?
   - Look for references in extraction reasoning
2. Are the rules clear enough?
   - Review examples in requirements file
3. Are quotes being verified before extraction?
   - Check extraction_notes for verification mentions

**Actions:**
1. Make prompt reminders more emphatic (bold, caps)
2. Add specific examples in prompts
3. Use verification script to catch issues early

---

### If verification script reports false positives:

**Common causes:**
- PDF conversion differences
- Line break handling
- Hyphen/dash variations

**Solutions:**
- Adjust normalization in script
- Document acceptable variations
- Update requirements file with examples

---

## Quick Reference: File Locations

### Files You've Created (Phase 1) ✅
```
/mnt/skills/user/research-assessor/
├── references/
│   ├── verbatim-quote-requirements.md  ← NEW (12 KB)
│   └── extraction-fundamentals.md      ← UPDATED
└── scripts/
    └── verify_quotes.py                ← NEW (12 KB)
```

### Files for You to Update (Phase 2) 📋
```
Your extraction prompts folder/
├── claims_pass1_prompt.md              ← ADD REMINDER
├── claims_pass2_prompt.md              ← ADD VERIFICATION STEP
├── rdmap_pass1_prompt.md               ← ADD REMINDER
└── rdmap_pass2_prompt.md               ← ADD VERIFICATION STEP
```

### Documentation Created
```
/mnt/user-data/outputs/
├── implementation_summary.md           ← Complete guide
├── prompt_modification_guide.md        ← Detailed instructions
├── source_verification_pattern_analysis.md  ← Problem diagnosis
└── pattern_analysis_executive_summary.md    ← Quick overview
```

---

## Questions?

**About verbatim requirements:**
- Read: `/mnt/skills/user/research-assessor/references/verbatim-quote-requirements.md`
- 5 failure patterns explained
- Good vs bad examples
- Character normalization rules

**About implementation:**
- Read: `/mnt/user-data/outputs/implementation_summary.md`
- Phased rollout strategy
- Expected outcomes
- Testing approach

**About the problem:**
- Read: `/mnt/user-data/outputs/pattern_analysis_executive_summary.md`
- Root cause analysis
- Not a PDF problem
- Quote construction methodology issue

---

## Next Steps

1. **Today:** Update your 4 prompts (15 minutes)
2. **Tomorrow:** Test on a paper
3. **This week:** Validate improvement across 2-3 papers
4. **If needed:** Add verification script for >95% pass rate

---

## Success Metrics

**Target:** >95% source verification pass rate

**Milestones:**
- ✅ Phase 1 complete: Skill files created
- 📋 Phase 2: Update prompts → expect >85%
- 🔧 Phase 3 (if needed): Add script → expect >95%

---

**You're ready to deploy! Start with Phase 2 prompt updates, test, and iterate as needed.**
