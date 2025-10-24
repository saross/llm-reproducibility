# Verbatim Quote Requirements - Preventing Source Verification Failures

**Last Updated:** 2025-10-24  
**Schema Version:** 2.5+  
**Purpose:** Strict requirements for verbatim_quote and trigger_text fields  
**Problem Solved:** Source verification failures due to non-verbatim quotes

---

## The Problem

Analysis of extraction failures revealed that "verbatim_quote" fields often contained:
- **Partial quotes** (missing beginnings/ends)
- **Paraphrased text** (reconstructed from memory)
- **Synthesized content** (combined from multiple sources)
- **Character variations** (formatting inconsistencies)

These issues caused 40-50% source verification failure rates, preventing credibility assessment.

---

## 🚨 CRITICAL: What "Verbatim" Means

**Verbatim = EXACT copy-paste from paper, with minimal normalization**

### Non-Negotiable Rules

1. **Extract complete grammatical units**
   - ✅ Extract whole sentences or complete clauses
   - ❌ NEVER extract mid-sentence fragments
   - ❌ NEVER start/end quotes mid-phrase

2. **Copy-paste only, no paraphrasing**
   - ✅ Use exact words from the paper
   - ❌ NEVER reconstruct meaning in your own words
   - ❌ NEVER synthesize from multiple sources

3. **Verify before extracting**
   - ✅ Ensure quote exists in paper before committing to JSON
   - ✅ Check location contains the quote
   - ❌ NEVER guess or approximate quotes

4. **Character normalization is allowed**
   - ✅ Standardize hyphens: "60-75" (not "60 – 75" with en-dash)
   - ✅ Remove line-break artifacts: "experience" (not "experi-ence")
   - ✅ Normalize whitespace: single space between words
   - ❌ DO NOT change actual words or word order

---

## ✅ GOOD Examples vs ❌ BAD Examples

### Example 1: Complete Sentences

**Paper text:**
"After brief workspace setup, project staff with desktop GIS experience could digitise at a sustained rate of 60-75 features per staff-hour."
```json
// ✅ GOOD - Complete sentence
{
  "verbatim_quote": "After brief workspace setup, project staff with desktop GIS experience could digitise at a sustained rate of 60-75 features per staff-hour."
}

// ❌ BAD - Partial quote, missing beginning
{
  "verbatim_quote": "project staff with desktop GIS experience could digitise at a sustained rate of 60-75 features per staff-hour"
}

// ❌ BAD - Partial quote, missing end
{
  "verbatim_quote": "After brief workspace setup, project staff with desktop GIS experience could digitise"
}
```

**Why the bad examples fail:**
- Exact text strings don't exist in paper
- Source verification cannot locate them
- Appear to be fabricated

---

### Example 2: No Paraphrasing

**Paper text:**
"To overcome this problem, in 2010, project staff worked with student volunteers to digitise map features using ArcGIS."
```json
// ✅ GOOD - Exact text
{
  "verbatim_quote": "To overcome this problem, in 2010, project staff worked with student volunteers to digitise map features using ArcGIS."
}

// ❌ BAD - Paraphrased
{
  "verbatim_quote": "In 2010, we attempted to use desktop GIS to crowdsource digitisation"
}

// ❌ BAD - Reconstructed with added interpretation
{
  "verbatim_quote": "In 2010, the project attempted to use desktop GIS for volunteer-based digitization efforts"
}
```

**Why the bad examples fail:**
- Text doesn't exist in paper
- Appears to be hallucinated
- Cannot verify against source

---

### Example 3: Character Normalization (Allowed)

**Paper text (with line break):**
"The mobile platform supported offline oper-
ation during fieldwork periods."
```json
// ✅ GOOD - Line break artifact removed
{
  "verbatim_quote": "The mobile platform supported offline operation during fieldwork periods."
}

// ✅ ACCEPTABLE - Preserved exactly as written (but harder to verify)
{
  "verbatim_quote": "The mobile platform supported offline oper-ation during fieldwork periods."
}
```

**Paper text (with en-dash):**
"Error rates ranged from 1.3% – 10.6%"
```json
// ✅ GOOD - En-dash normalized to hyphen
{
  "verbatim_quote": "Error rates ranged from 1.3%-10.6%"
}

// ✅ ACCEPTABLE - Preserved as-is
{
  "verbatim_quote": "Error rates ranged from 1.3% – 10.6%"
}
```

**Normalization guidelines:**
- Prefer normalized form for consistency
- Document normalization if extensive: `"normalization_notes": "hyphens standardized, line breaks removed"`

---

### Example 4: Single-Source Quotes Only

**Paper has two separate statements:**
- Location 1: "Project staff digitised features at 60-75 per hour"
- Location 2: "The crowdsourcing system required 57 hours of staff time"
```json
// ❌ BAD - Synthesized from multiple sources
{
  "verbatim_quote": "Project staff digitised features at 60-75 per hour. The crowdsourcing system required 57 hours of staff time."
}

// ✅ GOOD - Separate evidence items
{
  "evidence_id": "E001",
  "verbatim_quote": "Project staff digitised features at 60-75 per hour",
  "location": {"section": "Discussion", "paragraph": 12}
},
{
  "evidence_id": "E002", 
  "verbatim_quote": "The crowdsourcing system required 57 hours of staff time",
  "location": {"section": "Results", "paragraph": 5}
}
```

---

## Extraction Workflow

### Before Extracting Any Item
```
1. Locate the source text in paper
   ↓
2. Ask: "Is this explicitly stated?"
   ↓ YES                    ↓ NO
   Extract verbatim quote   Check if implicit (trigger_text)
   ↓
3. Copy exact text (whole sentences)
   ↓
4. Verify quote exists at stated location
   ↓
5. Normalize characters if needed
   ↓
6. Commit to JSON
```

### Quick Pre-Extraction Checklist

Before adding any `verbatim_quote` to JSON, verify:

- [ ] Quote is **complete grammatical unit** (whole sentence/clause)
- [ ] Text is **exact copy** from paper (not paraphrased)
- [ ] Quote is from **single source location** (not synthesized)
- [ ] **Location verified** to contain the quote
- [ ] Character normalization **documented** if applied

**If ANY checkbox fails → DO NOT EXTRACT or use implicit_metadata instead**

---

## Special Cases

### Case 1: Quote Spans Multiple Sentences

**When to do this:** When evidence/claim naturally encompasses multiple sentences

**How to do it:**
```json
{
  "verbatim_quote": "First complete sentence from paper. Second complete sentence from paper.",
  "location": {"section": "Results", "paragraph": 3, "sentence_start": 2, "sentence_end": 3}
}
```

**Requirements:**
- Both sentences must be contiguous (no text omitted)
- Both must be from same paragraph
- Use sentence_start and sentence_end to specify range

---

### Case 2: Quote Contains Typos/Errors in Original

**When to do this:** Source document has typos but you need exact text

**How to do it:**
```json
{
  "verbatim_quote": "The platfrom was highly efective [sic]",
  "extraction_notes": "Verbatim includes original typos: 'platfrom', 'efective'"
}
```

**Requirements:**
- Use `[sic]` to indicate original errors
- Note typos in extraction_notes
- Do NOT correct typos in verbatim_quote

---

### Case 3: Quote Contains Ellipsis (Omitted Text)

**When to avoid:** Generally AVOID omitting text with ellipsis - extract complete sentences instead

**When acceptable:** When sentence has long parenthetical that's not relevant

**How to do it:**
```json
{
  "verbatim_quote": "Error rates ranged from 1.3% [...] to 10.6%",
  "extraction_notes": "Ellipsis omits non-essential parenthetical about Student C"
}
```

**Requirements:**
- Use sparingly - prefer complete sentences
- Use `[...]` for omissions (not `...`)
- Document what was omitted in extraction_notes

---

## Verification Test

### Self-Check Before Pass 3 Validation

Every extractor should mentally verify their quotes:

**Question:** "If I search this exact text in the paper, will I find it?"
```
If YES → Good verbatim quote
If NO, but very close → Fix character differences
If NO, meaning is right but words differ → BAD - Need to re-extract
If NO, can't find anything similar → HALLUCINATION - Delete
```

---

## Common Failure Patterns to Avoid

### Pattern: Mid-Sentence Fragments

❌ **WRONG:**
```json
{
  "verbatim_quote": "volunteers required extensive and continuous staff support"
}
```

✅ **RIGHT:**
```json
{
  "verbatim_quote": "Novice volunteers found learning to configure and navigate desktop GIS challenging; many quit and those who continued required ongoing support."
}
```

---

### Pattern: Interpretive Paraphrasing

❌ **WRONG:**
```json
{
  "verbatim_quote": "The mobile application was more efficient than desktop GIS for volunteer digitization"
}
```

✅ **RIGHT:**
```json
{
  "verbatim_quote": "At the highest rate, desktop GIS digitisation using novice volunteers is almost competitive with the mobile application approach we used."
}
```

---

### Pattern: Value Synthesis

❌ **WRONG:**
```json
{
  "verbatim_quote": "Staff digitisation produced 3,420-4,275 features in 57 hours at 60-75 features per hour"
}
```

✅ **RIGHT:** Create separate evidence items
```json
{
  "evidence_id": "E001",
  "verbatim_quote": "project staff with desktop GIS experience could digitise at a sustained rate of 60-75 features per staff-hour"
},
{
  "evidence_id": "E002",
  "verbatim_quote": "the 57 h of staff time devoted to set-up, support, and quality assurance for our crowdsourcing system could have resulted in some 3,420-4,275 staff-digitised features"
}
```

---

## Trigger Text Requirements (Implicit Items)

For implicit RDMAP items and implicit arguments, `trigger_text` follows same verbatim rules:
```json
{
  "method_id": "M008",
  "method_status": "implicit",
  "trigger_text": [
    "Exact sentence 1 that implies the method",
    "Exact sentence 2 that implies the method"
  ],
  "trigger_locations": [
    {"section": "Introduction", "paragraph": 5},
    {"section": "Discussion", "paragraph": 12}
  ],
  "inference_reasoning": "These passages together imply X method was used because..."
}
```

**Same rules apply:**
- Each trigger must be verbatim text
- Each trigger must be complete grammatical unit
- Each trigger must be locatable at stated location

---

## Implementation Notes

### During Pass 1 (Liberal Extraction)

Even during over-extraction phase:
- Follow verbatim rules strictly
- If unsure, extract multiple versions rather than paraphrase
- Flag uncertain quotes: `"extraction_confidence": "medium"`

### During Pass 2 (Rationalization)

Key consolidation task: **Fix non-verbatim quotes**
- Review all quotes for verbatim compliance
- Locate actual text in paper for suspicious quotes
- Update quotes to match paper exactly
- Delete items that cannot be verified

---

## Quality Metrics

**Target:** >95% of items pass source verification in Pass 3

**Indicators of good verbatim quotes:**
- Minimal character normalization needed
- Easily locatable with simple text search
- No "almost but not quite" matches

**Red flags indicating problems:**
- Cannot find quote in paper with text search
- Multiple similar but not identical phrasings exist
- Quote "sounds right" but words are different

---

## When in Doubt

**If uncertain whether quote is verbatim:**
1. Re-locate the text in the paper
2. Copy-paste exactly
3. Verify with text search
4. If still uncertain, flag: `"extraction_confidence": "low"`

**Better to:**
- Extract conservatively with perfect verbatim quotes
- Use implicit status when text not explicit
- Skip item if cannot source properly

**Than to:**
- Paraphrase and hope it's close enough
- Approximate quote from memory
- Synthesize meaning across passages

---

## Summary: The Golden Rules

1. **Copy-paste whole sentences only**
2. **Never paraphrase - exact words only**
3. **Verify quote exists before extracting**
4. **Single source location per quote**
5. **Normalize characters consistently**

**Remember:** Source verification failure blocks credibility assessment. Taking extra 10 seconds per quote to ensure verbatim accuracy prevents hours of rework in Pass 3.

---

**End of Verbatim Quote Requirements**

*See also: `extraction-fundamentals.md` for general sourcing requirements, `verification-procedures.md` for Pass 3 validation.*
