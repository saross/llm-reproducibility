# Exact Implementation Guide: Verbatim Quote Requirements

**Purpose:** Minimal, precise additions to enforce verbatim quote requirements  
**Strategy:** Heavy lifting in skill references, light reminders in prompts  
**Token Budget:** ~100 tokens per prompt, ~200 tokens in skill

---

## Files to Modify

### Summary Table

| File | Location | Addition | Tokens |
|------|----------|----------|--------|
| **Skill Files** | | | |
| SKILL.md | `/mnt/skills/user/research-assessor/SKILL.md` | Reference pointer | ~100 |
| extraction-fundamentals.md | `references/extraction-fundamentals.md` | Already updated ✅ | ~200 |
| verbatim-quote-requirements.md | `references/` | Already created ✅ | ~3500 |
| **Prompt Files** | | | |
| Claims Pass 1 | Your prompt location | Critical reminder | ~110 |
| Claims Pass 2 | Your prompt location | Verification step | ~130 |
| RDMAP Pass 1 | Your prompt location | Critical reminder | ~110 |
| RDMAP Pass 2 | Your prompt location | Verification step | ~130 |
| **Total Added to Prompts** | | | **~480** |

---

## PART 1: Skill Files

### File 1: SKILL.md (Main Skill File)

**Location:** `/mnt/skills/user/research-assessor/SKILL.md`

**Where to add:** In the "Key Capabilities" or "References" section (after general overview, before workflow details)

**Text to add:**

```markdown
### Source Verification Requirements

**Critical for preventing extraction failures:**

All extracted items must have verifiable sources. The skill enforces strict verbatim quote requirements to prevent 40-50% validation failure rates.

**Key principle:** `verbatim_quote` means EXACT text from paper (complete sentences, no paraphrasing).

**Detailed guidance:** See `references/verbatim-quote-requirements.md` for:
- What "verbatim" means (complete sentences only, no mid-sentence fragments)
- 5 common failure patterns with examples
- Character normalization rules
- Pre-extraction verification checklist

**When Claude should read this:** Any uncertainty about quote construction, source verification failures in Pass 3.
```

**Alternative (if your SKILL.md has a "References Overview" section):**

```markdown
### references/verbatim-quote-requirements.md

**Purpose:** Prevent source verification failures (40-50% failure rate without this guidance)

**Contains:**
- Strict definition of "verbatim" (complete sentences, exact copy, no paraphrasing)
- 5 failure patterns: partial quotes, paraphrasing, synthesis, character differences, PDF artifacts
- Good vs bad examples for each pattern
- Pre-extraction checklist

**When to read:** Before Pass 1 extraction if uncertain about quote construction; during Pass 2 if fixing non-verbatim quotes; after Pass 3 failures.

**Key rules:**
1. Extract complete sentences only (no mid-sentence fragments)
2. Copy-paste exact text (no reconstruction or paraphrasing)
3. Single source location per quote (no synthesis)
4. Verify quote exists before committing to JSON
```

---

### File 2: extraction-fundamentals.md

**Status:** ✅ Already updated (you can verify the section was added correctly)

**Verify this section exists around line 86-110:**

```markdown
---

## Verbatim Quote Requirements

**CRITICAL:** For detailed guidance on creating proper verbatim quotes, see:  
→ **`references/verbatim-quote-requirements.md`**

**Key rules (full details in reference file):**
1. Extract **complete sentences** only (whole grammatical units)
2. Copy-paste **exact text** from paper (no paraphrasing)
3. **Verify quote exists** in paper before extracting
4. Use **single source location** per quote (no synthesis)
5. Character normalization allowed: hyphens, line breaks, whitespace

**Common failures to avoid:**
- ❌ Mid-sentence fragments ("volunteers required extensive support")
- ❌ Paraphrased reconstruction ("In 2010, we attempted to...")
- ❌ Synthesized multi-source quotes (combining separate statements)

**When uncertain:** Read the detailed requirements file before extracting.

---
```

---

### File 3: verbatim-quote-requirements.md

**Status:** ✅ Already created (12 KB reference file in `references/`)

**No action needed** - this file contains all the detailed guidance.

---

## PART 2: Prompt Files

### Prompt 1: Claims Extraction - Pass 1

**File:** Your claims Pass 1 prompt (e.g., `claims_pass1_extraction.md` or similar)

**Where to add:** Immediately after the "Your Task" section, BEFORE detailed extraction instructions begin

**Text to add:**

```markdown
---

## 🚨 CRITICAL: Verbatim Quote Requirements

**Before extracting any item:**

Read if uncertain: `/mnt/skills/user/research-assessor/references/verbatim-quote-requirements.md`

**Non-negotiable rules for all `verbatim_quote` fields:**

1. **Complete sentences only** - Extract whole grammatical units, never mid-sentence fragments
2. **Exact text only** - Copy-paste from paper, never paraphrase or reconstruct from memory  
3. **Verify before committing** - Ensure exact quote exists in paper before adding to JSON
4. **Single source only** - Never synthesize quotes from multiple locations

**Self-check:** "Can I find this EXACT text string in the paper with simple search?"
- If YES → Extract it
- If NO → Quote is wrong; fix it or mark as implicit

⚠️ **Failure to follow these rules causes 40-50% validation failures in Pass 3.**

---
```

**Token cost:** ~110 tokens

---

### Prompt 2: Claims Rationalization - Pass 2

**File:** Your claims Pass 2 prompt (e.g., `claims_pass2_rationalization.md` or similar)

**Where to add:** In the consolidation workflow, add as a new step (Step 4 or final step before output)

**Text to add:**

```markdown
---

## Step [X]: Source Verification

**Before finalizing consolidated items, verify all verbatim quotes:**

For EACH explicit item being kept in final JSON:

1. **Check compliance:** Does `verbatim_quote` follow rules in `references/verbatim-quote-requirements.md`?
2. **Verify existence:** Search for exact quote in paper
3. **Fix if needed:**
   - Quote not found → Locate actual text in paper and update
   - Partial quote (missing beginning/end) → Add context to complete sentence
   - Paraphrased quote → Replace with true verbatim text from paper
   - Synthesized quote → Split into separate items with single sources

**Common patterns to fix:**
- Missing sentence beginnings (add prefix context)
- Mid-sentence fragments (expand to complete sentences)
- Paraphrased meanings (find and use actual text)

**If quote cannot be verified:** Mark as low confidence:
```json
{
  "extraction_confidence": "low",
  "extraction_notes": "Quote verification uncertain - needs Pass 3 review"
}
```

---
```

**Token cost:** ~130 tokens

---

### Prompt 3: RDMAP Extraction - Pass 1

**File:** Your RDMAP Pass 1 prompt (e.g., `rdmap_pass1_extraction.md` or similar)

**Where to add:** Immediately after the "Your Task" section, BEFORE detailed extraction instructions begin

**Text to add:** SAME TEXT as Claims Pass 1 (Prompt 1 above)

```markdown
---

## 🚨 CRITICAL: Verbatim Quote Requirements

**Before extracting any item:**

Read if uncertain: `/mnt/skills/user/research-assessor/references/verbatim-quote-requirements.md`

**Non-negotiable rules for all `verbatim_quote` fields:**

1. **Complete sentences only** - Extract whole grammatical units, never mid-sentence fragments
2. **Exact text only** - Copy-paste from paper, never paraphrase or reconstruct from memory  
3. **Verify before committing** - Ensure exact quote exists in paper before adding to JSON
4. **Single source only** - Never synthesize quotes from multiple locations

**Self-check:** "Can I find this EXACT text string in the paper with simple search?"
- If YES → Extract it
- If NO → Quote is wrong; fix it or mark as implicit

⚠️ **Failure to follow these rules causes 40-50% validation failures in Pass 3.**

---
```

**Token cost:** ~110 tokens

---

### Prompt 4: RDMAP Rationalization - Pass 2

**File:** Your RDMAP Pass 2 prompt (e.g., `rdmap_pass2_rationalization.md` or similar)

**Where to add:** In the consolidation workflow, add as a new step (Step 4 or final step before output)

**Text to add:** SAME TEXT as Claims Pass 2 (Prompt 2 above)

```markdown
---

## Step [X]: Source Verification

**Before finalizing consolidated items, verify all verbatim quotes:**

For EACH explicit item being kept in final JSON:

1. **Check compliance:** Does `verbatim_quote` follow rules in `references/verbatim-quote-requirements.md`?
2. **Verify existence:** Search for exact quote in paper
3. **Fix if needed:**
   - Quote not found → Locate actual text in paper and update
   - Partial quote (missing beginning/end) → Add context to complete sentence
   - Paraphrased quote → Replace with true verbatim text from paper
   - Synthesized quote → Split into separate items with single sources

**Common patterns to fix:**
- Missing sentence beginnings (add prefix context)
- Mid-sentence fragments (expand to complete sentences)
- Paraphrased meanings (find and use actual text)

**If quote cannot be verified:** Mark as low confidence:
```json
{
  "extraction_confidence": "low",
  "extraction_notes": "Quote verification uncertain - needs Pass 3 review"
}
```

---
```

**Token cost:** ~130 tokens

---

## Implementation Checklist

### Phase 1: Skill Files

- [ ] Verify `references/extraction-fundamentals.md` has verbatim section (should already be there)
- [ ] Verify `references/verbatim-quote-requirements.md` exists (should already be there - 12KB file)
- [ ] Add reference pointer to main `SKILL.md` (use one of the two options above)

**Time:** 5 minutes  
**Test:** Ask Claude to summarize verbatim requirements - should reference the files

---

### Phase 2: Prompt Files

- [ ] Add critical reminder to **Claims Pass 1** prompt (after task description)
- [ ] Add critical reminder to **RDMAP Pass 1** prompt (after task description)
- [ ] Add verification step to **Claims Pass 2** prompt (in consolidation workflow)
- [ ] Add verification step to **RDMAP Pass 2** prompt (in consolidation workflow)

**Time:** 10 minutes  
**Test:** Run extraction, check if Claude mentions verbatim rules

---

### Phase 3: Validation

- [ ] Run test extraction on short paper
- [ ] Check Pass 3 validation report
- [ ] Measure source verification pass rate
- [ ] Target: >90% (from current 53%)

**Time:** 30-60 minutes  
**Success criteria:** >85% pass rate (>90% ideal)

---

## Quick Copy-Paste Reference

### For Pass 1 Prompts (Both Claims and RDMAP)

Copy this block:

```
---

## 🚨 CRITICAL: Verbatim Quote Requirements

**Before extracting any item:**

Read if uncertain: `/mnt/skills/user/research-assessor/references/verbatim-quote-requirements.md`

**Non-negotiable rules for all `verbatim_quote` fields:**

1. **Complete sentences only** - Extract whole grammatical units, never mid-sentence fragments
2. **Exact text only** - Copy-paste from paper, never paraphrase or reconstruct from memory  
3. **Verify before committing** - Ensure exact quote exists in paper before adding to JSON
4. **Single source only** - Never synthesize quotes from multiple locations

**Self-check:** "Can I find this EXACT text string in the paper with simple search?"
- If YES → Extract it
- If NO → Quote is wrong; fix it or mark as implicit

⚠️ **Failure to follow these rules causes 40-50% validation failures in Pass 3.**

---
```

---

### For Pass 2 Prompts (Both Claims and RDMAP)

Copy this block:

```
---

## Step [X]: Source Verification

**Before finalizing consolidated items, verify all verbatim quotes:**

For EACH explicit item being kept in final JSON:

1. **Check compliance:** Does `verbatim_quote` follow rules in `references/verbatim-quote-requirements.md`?
2. **Verify existence:** Search for exact quote in paper
3. **Fix if needed:**
   - Quote not found → Locate actual text in paper and update
   - Partial quote (missing beginning/end) → Add context to complete sentence
   - Paraphrased quote → Replace with true verbatim text from paper
   - Synthesized quote → Split into separate items with single sources

**Common patterns to fix:**
- Missing sentence beginnings (add prefix context)
- Mid-sentence fragments (expand to complete sentences)
- Paraphrased meanings (find and use actual text)

**If quote cannot be verified:** Mark as low confidence:
```json
{
  "extraction_confidence": "low",
  "extraction_notes": "Quote verification uncertain - needs Pass 3 review"
}
```

---
```

---

## Token Budget Summary

### Added to Always-Loaded Context

| Location | Tokens | Frequency |
|----------|--------|-----------|
| SKILL.md pointer | ~100 | Always (but only pointer) |
| Claims Pass 1 reminder | ~110 | Every claims extraction |
| Claims Pass 2 verification | ~130 | Every claims rationalization |
| RDMAP Pass 1 reminder | ~110 | Every RDMAP extraction |
| RDMAP Pass 2 verification | ~130 | Every RDMAP rationalization |
| **Total per full extraction** | **~580** | **Per paper** |

### Loaded On-Demand (Not Always in Context)

| File | Tokens | When Loaded |
|------|--------|-------------|
| verbatim-quote-requirements.md | ~3,500 | Only when Claude uncertain |
| extraction-fundamentals.md | ~2,000 | Only when reviewing sourcing rules |
| **On-demand total** | **~5,500** | **Occasional** |

**Key insight:** Only ~580 tokens added to regular extraction context. Large reference files loaded only when needed.

---

## Expected Outcomes

### Before (Sobotkova Baseline)

```
Pass 1: No verbatim enforcement
  ↓
Pass 2: No verification step
  ↓
Pass 3: 53% pass rate (67 failures)
  ↓
Status: FAIL - blocks assessment
```

### After (With These Changes)

```
Pass 1: Critical reminder (extract complete sentences, no paraphrasing)
  ↓
Pass 2: Verification step (check and fix quotes)
  ↓
Pass 3: Expected 85-90% pass rate (~5-10 failures)
  ↓
Status: PASS WITH ISSUES - assessment possible
```

### If Needed: Manual Review

```
Pass 3: If still <90%
  ↓
Manual review of failures (use pattern analysis)
  ↓
Targeted fixes to prompts or remaining items
  ↓
Target: >95% pass rate
```

---

## Troubleshooting

### If pass rate is still <80% after implementation:

**Check these things:**

1. **Did Claude read the verbatim requirements?**
   - Look for mentions in extraction reasoning
   - Check extraction_notes for quote verification
   - If not mentioned: Make prompt reminder more emphatic

2. **Are quotes being verified in Pass 2?**
   - Check if consolidation notes mention verification
   - Look for "fixed quote" or "updated quote" mentions
   - If not happening: Strengthen Pass 2 verification step

3. **Are there domain-specific issues?**
   - Archaeology/fieldwork jargon causing problems?
   - Technical terminology hard to quote exactly?
   - If yes: Add domain examples to verbatim-quote-requirements.md

---

### If specific patterns persist:

**Partial quotes still common:**
- Add examples specific to your papers in verbatim-quote-requirements.md
- Make "complete sentences only" more emphatic in Pass 1 reminder
- Add automated check in Pass 2: "Does quote start mid-sentence?"

**Paraphrasing still occurring:**
- Add paper-specific "bad examples" showing actual paraphrases found
- Emphasize "copy-paste only" in Pass 1 reminder
- Consider adding verification script as safety net

**Character differences causing failures:**
- Document acceptable normalizations in verbatim-quote-requirements.md
- Add normalization note to Pass 2 verification step
- Less critical (only 5-10% of failures)

---

## Summary

### What You're Adding

**To Skill:**
- Small pointer in SKILL.md (~100 tokens)
- Already have detailed requirements file (loaded on-demand)

**To Prompts:**
- Pass 1: Brief critical reminder (~110 tokens × 2 prompts)
- Pass 2: Verification step (~130 tokens × 2 prompts)
- Total: ~580 tokens across all prompts

### What You're Getting

**Problem solved:**
- 47% failure rate → Expected 85-90% (>95% with manual review)
- Paraphrasing prevented by explicit "exact text only" rule
- Partial quotes prevented by "complete sentences only" rule
- Systematic approach to quote construction

**Workflow impact:**
- Pass 1: Claude aware of verbatim requirements from start
- Pass 2: Claude checks and fixes quotes before finalization
- Pass 3: Validation passes, assessment can proceed

---

## Ready to Implement

All text is provided above in copy-paste ready format:
- ✅ SKILL.md addition
- ✅ Pass 1 reminder (use for both prompts)
- ✅ Pass 2 verification (use for both prompts)

**Next step:** Copy the text into your files, test on a paper, measure improvement.

---

**Questions to resolve before implementing:**

1. Where is your SKILL.md located? Should I confirm the exact section to add the pointer?
2. What are your prompt files called? (So I can give you exact file paths)
3. Do you want to test on Sobotkova again to measure improvement, or use a new paper?
