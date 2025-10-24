# Source Verification Failure Pattern Analysis
## Sobotkova et al. (2023) - RDMAP Pass 2 Extraction

**Analysis Date:** October 23, 2025  
**Analyst:** Claude Sonnet 4.5

---

## Executive Summary

**Root Cause Identified:** ⚠️ **Quote Construction Issues, NOT PDF Quality**

After comparing the original markdown (892 lines) with a cleaner Gemini-generated markdown (329 lines) and manually verifying failed items, the source verification failures stem from **systematic quote construction problems** during extraction, not PDF conversion artifacts.

### Key Findings

1. ✅ **PDF quality is acceptable** - The cleaner markdown helped 1 item (E009) but the vast majority of failures persist
2. ❌ **Quotes are not truly verbatim** - Many "verbatim_quotes" are partial, paraphrased, or reconstructed
3. ❌ **Extraction methodology issue** - The Pass 1/Pass 2 extraction process didn't enforce strict verbatim requirements

---

## Pattern Categories Identified

### Pattern 1: Partial Quotes (Missing Beginning/End)
**Prevalence:** Very Common  
**Severity:** Critical - Prevents verification

**Description:** Extracted quotes take a middle portion of a sentence without including the beginning or end, making exact matching impossible.

**Example - E015:**
```
EXTRACTED QUOTE:
"project staff with desktop GIS experience could digitise at a sustained 
rate of 60 – 75 features per staff-hour"

ACTUAL TEXT IN PAPER:
"After brief workspace setup, project staff with desktop GIS experience 
could digitise at a sustained rate of 60-75 features per staff-hour."

ISSUES:
- Missing beginning: "After brief workspace setup, "
- Hyphen format: "60 – 75" vs "60-75" (en-dash with spaces vs hyphen)
- Missing end punctuation
```

**Impact:** Quote verification fails because the exact text string doesn't exist in the paper.

---

### Pattern 2: Paraphrased/Reconstructed Quotes
**Prevalence:** Common  
**Severity:** Critical - Violates verbatim requirement

**Description:** Extracted quotes reconstruct or paraphrase the paper's meaning rather than capturing exact wording. These appear to synthesize information from multiple sentences or rephrase content.

**Example - E020:**
```
EXTRACTED QUOTE:
"In 2010, we attempted to use desktop GIS to crowdsource digitisation 
but found volunteers required extensive and continuous staff support, 
resulting in a de facto production rate of 130 – 180 features per 
staff-hour (of desktop GIS support and troubleshooting)."

ACTUAL TEXT IN PAPER (from two locations):

Location 1 (Introduction, line 98):
"To overcome this problem, in 2010, project staff worked with student 
volunteers to digitise map features using ArcGIS. Our experience was 
much like that of other projects: novice volunteers found learning to 
configure and navigate desktop GIS challenging; many quit and those 
who continued required ongoing support."

Location 2 (Discussion, line 199):
"based on our 2010 digitisation rate of 130-180 features per staff-hour"

ISSUES:
- Synthesized from multiple non-contiguous passages
- Rephrased the original text
- Added interpretive language ("de facto production rate")
- The specific phrasing doesn't appear anywhere in the paper
```

**Impact:** These are not verbatim quotes and represent extraction hallucination or over-interpretation.

---

### Pattern 3: Composite Quotes (Multiple Sentences Merged)
**Prevalence:** Common  
**Severity:** Important - Makes location citation imprecise

**Description:** Extracted quotes combine multiple sentences or passages into a single "verbatim_quote" field, making it impossible to find the exact string.

**Example - E018:**
```
EXTRACTED QUOTE:
"Project staff can digitise mounds at a sustained rate of 60 – 75 
features per staff-hour. At this rate, the 57 h of staff time devoted 
to set-up, support, and quality assurance for our crowdsourcing system 
could have resulted in some 3,420 – 4,275 staff-digitised features"

ACTUAL TEXT IN PAPER (line 197-198):
"project staff with desktop GIS experience could digitise at a sustained 
rate of 60-75 features per staff-hour. At this rate, the 57 h of staff 
time devoted to set-up, support, and quality assurance for our 
crowdsourcing system could have resulted in some 3,420-4,275 
staff-digitised features"

ISSUES:
- First sentence modified: "Project staff can digitise mounds" vs 
  "project staff with desktop GIS experience could digitise"
- Changed verb tense and specificity
- Missing context clause
- Hyphen formatting
```

**Impact:** The modified text prevents exact matching even though the content is approximately correct.

---

### Pattern 4: Character-Level Formatting Differences
**Prevalence:** Very Common  
**Severity:** Minor - Could be resolved with normalization

**Description:** Systematic differences in punctuation, whitespace, or special characters between extracted quotes and paper text.

**Common Issues:**
- **En-dash vs hyphen:** "60 – 75" (extracted) vs "60-75" (paper)
- **Hyphenation at line breaks:** "experi-ence" in paper vs "experience" in extraction
- **Whitespace normalization:** Multiple spaces vs single space
- **Case sensitivity:** "Project" vs "project"

**Example:**
```
EXTRACTED: "60 – 75 features"
PAPER:     "60-75 features"

Difference: En-dash with spaces vs hyphen without spaces
```

**Impact:** These differences could be resolved with text normalization, but they still prevent exact string matching on raw text.

---

### Pattern 5: PDF Quality Issues (Rare)
**Prevalence:** Rare  
**Severity:** Minor - Only 1 confirmed case

**Description:** The original PDF-to-markdown conversion introduced artifacts that were corrected in the cleaner Gemini version.

**Example - E009:**
```
EXTRACTED QUOTE:
"Students' individual error rates ranged from 1.3% to 10.6%"

RESULT:
- NOT found in original markdown (892 lines)
- FOUND in Gemini markdown (329 lines)
```

**Impact:** Only 1 of 32 failed items was resolved by using cleaner markdown, indicating PDF quality is NOT the primary issue.

---

## Detailed Analysis by Failed Item

### Evidence Items Analysis

| ID | Quote Type | Primary Issue | In New MD? | Fixable? |
|----|-----------|---------------|------------|----------|
| E009 | Partial | PDF quality | ✅ YES | Auto-fixed |
| E015 | Partial | Missing beginning | ❌ NO | Yes - add prefix |
| E018 | Composite + Modified | Sentence reconstruction | ❌ NO | Yes - use actual text |
| E020 | Paraphrased | Synthesized from multiple sources | ❌ NO | Delete/Replace |
| E023 | Partial | Missing beginning | ❌ NO | Yes - add prefix |

### RDMAP Items Analysis

**Research Designs:** 6 of 8 failed (75% failure rate)  
**Methods:** 10 of 11 failed (91% failure rate)  
**Protocols:** 15 of 20 failed (75% failure rate)

**Common RDMAP Issues:**
1. Quotes cite "Methods" section but text is in Introduction or Discussion
2. Implicit RDMAP items have incomplete or missing trigger_text
3. Location mismatches between citation and actual text location
4. Paraphrased procedural descriptions rather than verbatim quotes

---

## Root Cause Analysis

### Primary Issue: Extraction Methodology

The Pass 1/Pass 2 extraction process appears to have:

1. **Interpreted "verbatim_quote" too loosely**
   - Allowed paraphrasing
   - Permitted partial quotes
   - Accepted reconstructed composite quotes

2. **Lacked strict verification during extraction**
   - No real-time quote verification against source
   - No requirement for exact string matching
   - No normalization or formatting consistency checks

3. **Conflated content extraction with quote extraction**
   - Extracted the *meaning* of the paper (good)
   - But called it "verbatim" when it wasn't (bad)

### Secondary Issue: Location Citation Inconsistency

Many items cite incorrect sections:
- Quote says "Discussion" but text is in "Results"
- Quote says "Methods" but text is in "Introduction"
- Location citations appear to reference where concept is discussed, not where quote actually appears

---

## Impact Assessment

### What This Means for the Extraction

**Structural Integrity:** ✅ Excellent (100% pass)
- Cross-references valid
- Hierarchies intact
- Schema compliant

**Content Quality:** ⚠️ Good but unverifiable
- Evidence/claims capture meaningful content
- RDMAP captures actual methodology
- BUT cannot verify quotes are truly from the paper

**Source Verification:** ❌ Failed (53% pass rate overall)
- Cannot trust quotes are verbatim
- Cannot verify location citations
- Cannot distinguish real content from hallucination

### Assessment Implications

**Can this extraction be used for credibility assessment?** ⚠️ **Limited use**

- **✅ Can assess:** Completeness of what was documented (expected_information)
- **❌ Cannot assess:** Accuracy of specific claims without re-verification
- **❌ Cannot assess:** Replicability from protocols without checking against paper

**Risk:** Without verified quotes, any assessment conclusions could be challenged as based on potentially inaccurate extractions.

---

## Recommendations

### Immediate Actions

#### Option 1: Manual Correction (Recommended)
**Effort:** High (3-5 hours)  
**Outcome:** Verified, assessment-ready extraction

**Process:**
1. For each failed item, locate actual text in paper
2. Replace extracted quote with true verbatim text
3. Update location to match actual location
4. Delete items that cannot be verified (hallucinations)
5. Re-run Pass 3 validation to confirm >95% pass rate

**Priority items:**
- All 32 failed evidence/claims (highest priority - these are data)
- All 7 implicit RDMAP items (0% pass rate)
- Failed protocols (critical for replicability assessment)

#### Option 2: Re-extraction with Strict Rules (Alternative)
**Effort:** Very High (6-10 hours)  
**Outcome:** Clean extraction from scratch

**Process:**
1. Define strict verbatim requirements for Pass 1
2. Re-run Pass 1 extraction with verification enabled
3. Verify each quote against paper during extraction
4. Complete Pass 2 consolidation with source integrity checks
5. Run Pass 3 validation

**Benefit:** Systematic fix prevents similar issues in future papers

#### Option 3: Selective Assessment (Workaround)
**Effort:** Low  
**Outcome:** Limited assessment with caveats

**Process:**
1. Use only the 63 verified evidence/claims items
2. Focus assessment on completeness gaps (expected_information)
3. Manually verify any quoted values used in conclusions
4. Clearly document extraction limitations in assessment report

**Limitation:** Cannot make strong claims about specific values or protocols

---

### Systematic Improvements for Future Extractions

#### 1. Enforce Strict Verbatim Requirements

**Rule:** verbatim_quote MUST be copy-pasted exact text from paper, not paraphrased

**Implementation:**
- During Pass 1, require exact quote extraction
- Use quote verification as part of extraction process
- Flag any quote that cannot be exactly located
- Document any character normalization performed

#### 2. Implement Real-Time Verification

**Tool:** Quote verification script run during extraction, not just in Pass 3

**Process:**
- Each quote verified against paper before committing to JSON
- Location citations verified to contain the quote
- Character normalization applied consistently
- Failed verifications flagged for manual review

#### 3. Distinguish Quote Types

**Categories:**
- **verbatim_quote:** Exact text string from paper (strict requirement)
- **paraphrase:** Researcher's interpretation (separate field)
- **synthesis:** Combined information from multiple sources (separate field)

**Benefit:** Maintains both accuracy and interpretive value

#### 4. Document Quote Modifications

If normalization or minor editing is needed:
```json
{
  "verbatim_quote_original": "text-as-it-appears-in-paper",
  "verbatim_quote_normalized": "text after normalization",
  "normalization_applied": ["hyphen_standardization", "whitespace_normalization"]
}
```

---

## Conclusion

### Is this a PDF problem?
**❌ NO** - Only 1 of 32 failures resolved with cleaner markdown

### Is this a formatting problem?
**Partially** - Character differences contribute but are minor compared to quote construction issues

### Is this something else systematic?
**✅ YES** - Extraction methodology issue

**The real issue:** The extraction process interpreted "verbatim" too loosely, creating paraphrases, partial quotes, and reconstructions instead of true verbatim captures.

---

## Next Steps

1. **Decide on correction strategy** (Option 1, 2, or 3 above)
2. **Prioritize critical items** (evidence/claims first, then RDMAP)
3. **Implement quote verification** for this and future extractions
4. **Document methodology** changes to prevent recurrence

---

**Analysis Complete**  
**Analyst:** Claude Sonnet 4.5 (research-assessor skill v2.5)  
**Validation Report:** `sobotkova_validation_pass3_report.json`  
**Pattern Analysis:** This document
