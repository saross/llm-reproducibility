# Implicit Arguments Skill Assessment & Improvement Recommendations

**Date**: 2025-10-27
**Context**: Apply lessons from implicit RDMAP improvements to strengthen implicit arguments extraction
**Fragility Issue**: Implicit arguments extraction "has been a bit fragile (although it worked fine in the last pass)"

---

## Executive Summary

The implicit RDMAP improvements revealed a pattern applicable to implicit arguments extraction:
- **Key insight**: Procedural knowledge needs to be in the skill, not just the prompts
- **Solution**: Create dedicated section in extraction-fundamentals.md with recognition patterns and common mistakes
- **Outcome**: More robust, consistent extraction across different papers

**Recommendation**: Apply same treatment to implicit arguments that was applied to implicit RDMAP.

---

## Current State Analysis

### What Works Well

**Pass 1 Prompt (01-claims-evidence_pass1_prompt.md:162-244):**
✅ Clear 4-type taxonomy:
  - Type 1: Logical Implications
  - Type 2: Unstated Assumptions
  - Type 3: Bridging Claims
  - Type 4: Disciplinary Assumptions

✅ Systematic search requirement for all core claims

✅ Proper sourcing requirements:
  - trigger_text array (verbatim passages)
  - trigger_locations
  - inference_reasoning

✅ Quality checklist enforcement

**Pass 2 Prompt (02-claims-evidence_pass2_prompt.md:283-341):**
✅ Completeness review in STEP 3
✅ Focus on cross-section synthesis
✅ Quality check for suspiciously low counts
✅ Guidance on adding missed implicit arguments

### Identified Gaps (Analogous to Pre-Fix Implicit RDMAP)

**Gap 1: No Dedicated Section in extraction-fundamentals.md**
- extraction-fundamentals.md mentions implicit arguments briefly (line 62)
- But has NO detailed section (unlike implicit RDMAP which now has lines 68-158)
- All detailed guidance lives in prompts, not in skill references

**Gap 2: No Recognition Patterns**
- Has type taxonomy (what they are)
- Missing: where to look, what triggers to scan for
- Analogous to RDMAP needing "VERBS without procedures" patterns

**Gap 3: No Common Mistakes Section**
- RDMAP has explicit "Common Mistakes to Avoid" (extraction-fundamentals.md:149-157)
- Implicit arguments has no equivalent
- User reports fragility → suggests common pitfalls exist

**Gap 4: No Template/Examples in Skill**
- Created consolidation_template.py and section_rdmap_template.py for RDMAP
- No equivalent template for implicit arguments
- Examples only in sobotkova-example.md, not as reusable template

---

## Fragility Root Causes

Based on RDMAP experience, fragility likely stems from:

### Cause 1: Inconsistent Scanning Patterns
**Problem**: Extractors may interpret "systematic search" differently
- Some may scan superficially
- Some may focus only on Type 1 (logical implications)
- Some may miss cross-section patterns

**Evidence from RDMAP**: Section-by-section extraction lost implicit items when extraction script changed, despite "scan for implicit" instruction

### Cause 2: Lack of Concrete Recognition Cues
**Problem**: "Look for unstated assumptions" is abstract
- What text patterns indicate an unstated assumption?
- Where in the paper should you look?
- What's the difference between "absent" and "implicit"?

**Evidence from RDMAP**: Needed concrete patterns like "VERBS without procedures", "EFFECTS implying causes"

### Cause 3: Type Taxonomy Without Application Guidance
**Problem**: Knowing 4 types doesn't tell you how to find them
- Types define categories after identification
- Don't provide identification methodology

**Evidence from RDMAP**: Had tier definitions (Design/Method/Protocol) but needed recognition patterns

---

## Recommended Improvements

### Improvement 1: Add Implicit Arguments Section to extraction-fundamentals.md

**Location**: After implicit RDMAP section (after line 158), before "Hallucination Prevention"

**Content Structure** (analogous to implicit RDMAP section):

```markdown
## Implicit Arguments Extraction in Claims-Evidence Passes

### The Challenge

When extracting claims and evidence, implicit arguments are easily overlooked because they're definitionally unstated. Each core claim requires systematic search for 4 types of implicit arguments.

**Common failure mode**: Only extracting obvious logical implications (Type 1), missing deeper assumptions (Types 2-4).

### Where Implicit Arguments Hide

**Type 1: Logical Implications** - Unstated steps in reasoning chain:
- ✓ Discussion: "Method is accurate" → implies adequate calibration/validation
- ✓ Results: "Complete dataset" → implies no systematic exclusions occurred
- ✓ Claims about platform "efficiency" → implies comparison baseline exists

**Type 2: Unstated Assumptions** - Prerequisites assumed without acknowledgment:
- ✓ Introduction: Spatial analysis assumes GPS accuracy adequate for scale
- ✓ Methods: Sample representativeness assumes no systematic bias
- ✓ Claims: Quality judgments assume evaluator competence

**Type 3: Bridging Claims** - Missing links between evidence and conclusions:
- ✓ Evidence: "8,343 features collected" → Claim: "Comprehensive coverage"
  Missing bridge: What makes 8,343 "comprehensive"? (comparison to target/expectations)
- ✓ Evidence: "95% accuracy" → Claim: "High quality"
  Missing bridge: What threshold defines "high"? (disciplinary norms)

**Type 4: Disciplinary Assumptions** - Field-specific taken-for-granted knowledge:
- ✓ Archaeology: Surface visibility relates to artifact presence (not stated)
- ✓ GIS: Coordinate precision relates to data usability (assumed)
- ✓ Digital Humanities: Manual digitization quality assumptions

### Section-by-Section Extraction Workflow

**For EACH section (Abstract, Intro, Methods, Results, Discussion):**

1. **First**: Extract explicit claims and evidence
   - Direct statements requiring minimal interpretation
   - Use `*_status = "explicit"` with `verbatim_quote`

2. **Then**: For each CORE claim, run 4-type implicit argument scan
   - **Type 1 scan**: "If this claim is true, what MUST also be true?"
   - **Type 2 scan**: "What must be true for this claim to hold?"
   - **Type 3 scan**: "How do they get from evidence to this claim?"
   - **Type 4 scan**: "What field-specific knowledge is taken for granted?"

3. **For each implicit argument found**:
   - Extract `trigger_text` array (verbatim passages implying the argument)
   - Record `trigger_locations` (where each trigger found)
   - Write `inference_reasoning` (explain how triggers imply argument)
   - Add `implicit_metadata` with basis and assessment_implication

### Recognition Patterns

**Pattern 1: Undefended Quality Judgments**
- Trigger: Claims use evaluative terms without criteria
- Example: "Data quality was high" without defining "high"
- Extract: Implicit assumption about quality thresholds
- Reasoning: "Paper asserts 'high quality' but never specifies criteria or comparison baseline"

**Pattern 2: Comparison Without Baseline**
- Trigger: Efficiency/performance claims without stated comparison
- Example: "Platform was efficient" without stating "compared to what?"
- Extract: Implicit comparison assumption
- Reasoning: "Efficiency is relative—claim implies unstated baseline or expectations"

**Pattern 3: Capability Assumptions**
- Trigger: Methods rely on technical capabilities without verification
- Example: GPS-based analysis with no accuracy discussion
- Extract: Implicit adequacy assumption
- Reasoning: "Spatial analysis assumes GPS precision adequate for research scale, but never verified"

**Pattern 4: Inferential Leaps**
- Trigger: Large gap between evidence granularity and claim scope
- Example: Evidence: "3 volunteers had issues" → Claim: "Supervision challenges exist"
- Extract: Bridging argument about representativeness
- Reasoning: "Leap from 3 cases to general pattern needs bridging claim about sample representativeness"

### Quick Reference: Explicit vs Implicit Arguments

| Aspect | Explicit Claims | Implicit Arguments |
|--------|----------------|-------------------|
| **Location** | Directly stated in paper | Implied by reasoning structure |
| **Test** | "Does paper say this?" | "Does reasoning require this?" |
| **Status field** | `"explicit"` (claims) | `"implicit"` (arguments) |
| **Source field** | `verbatim_quote` | `trigger_text` array |
| **Reasoning** | Not required | `inference_reasoning` required |

### Common Mistakes to Avoid

❌ **Assuming implicit = unimportant**: Implicit arguments are often the most assessment-critical items. They reveal unacknowledged assumptions.

❌ **Only extracting Type 1 (logical implications)**: Type 1 is easiest to spot. Types 2-4 require deeper analysis but are often more significant.

❌ **Treating "domain knowledge" as implicit**: If paper never references concept, it's absent (don't extract). Implicit means reasoning requires it even if unstated.

❌ **Extracting from your own reasoning**: Only extract implicit arguments the AUTHORS' reasoning depends on, not what YOU think they should have considered.

✓ **Correct approach**: Systematic 4-type scan for EACH core claim, documenting trigger passages showing why authors' reasoning needs this implicit step.

### When NOT to Extract Implicit Arguments

**Don't extract when:**
- Paper explicitly states the assumption/implication (then it's an explicit claim)
- No textual triggers exist (your own inference, not theirs)
- Claim is so trivial no assessment implications exist
- It's about what they SHOULD have done (not what their reasoning depends on)

**Do extract when:**
- Authors' reasoning chain requires it even though unstated
- Multiple triggers imply the assumption
- Assessment implications exist (transparency, credibility)
- It's not obvious to readers outside the discipline
```

### Improvement 2: Add Common Pitfalls Checklist to Pass 1 Prompt

**Location**: After line 244 in 01-claims-evidence_pass1_prompt.md

**Content**:
```markdown
**Common Pitfalls When Extracting Implicit Arguments:**

- ❌ Only scanning for Type 1 (logical implications), missing Types 2-4
- ❌ Superficial scan instead of systematic 4-type review per core claim
- ❌ Missing cross-section assumptions (visible only when seeing full argument arc)
- ❌ Extracting your own critique (what they should have considered) vs what their reasoning depends on
- ❌ No trigger_text (your inference without textual basis)

**Quality Check:** For each core claim, can you demonstrate you ran all 4 type scans? Document in extraction_notes.
```

### Improvement 3: Create Template Script

**File**: `extraction-system/scripts/extraction/section_implicit_arguments_template.py`

**Purpose**: Show concrete examples of each implicit argument type with proper trigger_text sourcing

**Key Examples**:
- Type 1: Logical implication from capability claim
- Type 2: Unstated assumption in spatial analysis
- Type 3: Bridging claim for quality judgment
- Type 4: Disciplinary assumption about methods

### Improvement 4: Update SKILL.md References

**Location**: SKILL.md line 100 (Core Extraction Principles section)

**Current**:
```markdown
- `references/extraction-fundamentals.md` - Universal sourcing requirements, explicit vs implicit extraction, section-by-section implicit RDMAP patterns (ALWAYS read first for Pass 1 & 2)
```

**Update to**:
```markdown
- `references/extraction-fundamentals.md` - Universal sourcing requirements, explicit vs implicit extraction, systematic implicit RDMAP patterns, systematic implicit arguments patterns (ALWAYS read first for Pass 1 & 2)
```

---

## Implementation Priority

**Priority 1 (HIGH)**: Improvement 1 - extraction-fundamentals.md section
- Addresses root cause (lack of recognition patterns)
- Provides reusable procedural knowledge
- Benefits all future extractions

**Priority 2 (MEDIUM)**: Improvement 2 - Common pitfalls in prompt
- Quick addition with immediate impact
- Prevents most common failure modes

**Priority 3 (MEDIUM)**: Improvement 4 - SKILL.md update
- Ensures discovery of new content
- Quick edit

**Priority 4 (LOW)**: Improvement 3 - Template script
- Nice-to-have reference
- Can be added later if Pattern proves useful

---

## Expected Outcomes

After implementing these improvements:

1. **More consistent implicit argument extraction** across different papers
   - Recognition patterns provide concrete scanning methodology
   - Common mistakes section prevents known failure modes

2. **Less fragility** in implicit argument detection
   - Procedural knowledge moves from prompts (ephemeral) to skill (permanent)
   - Multiple extractors will use same recognition patterns

3. **Better coverage of Type 2-4** implicit arguments
   - Current fragility likely from Type 1 bias
   - Recognition patterns emphasize all 4 types equally

4. **Analogous to implicit RDMAP fix**
   - Same root cause (procedural knowledge missing)
   - Same solution structure (dedicated skill section + patterns)
   - Should achieve similar robustness gains

---

## Comparison: Before and After RDMAP Improvements

### RDMAP Before Fix
- Had tier taxonomy (Design/Method/Protocol)
- Had implicit status field definition
- **But**: No recognition patterns, no "where to look" guidance
- **Result**: 0 implicit RDMAP items in latest run (vs 1-4 expected)

### RDMAP After Fix
- Added dedicated section in extraction-fundamentals.md
- Added 4 recognition patterns with concrete examples
- Added common mistakes to avoid
- Added template script
- **Expected Result**: Implicit RDMAP restored in future extractions

### Implicit Arguments Current State (Analogous to "Before Fix")
- Has 4-type taxonomy
- Has implicit status field definition
- **But**: No recognition patterns, no "where to look" guidance beyond abstract types
- **Result**: "Fragile" extraction (sometimes works, sometimes doesn't)

### Implicit Arguments After Proposed Fix
- Add dedicated section in extraction-fundamentals.md
- Add 4 recognition patterns with concrete examples
- Add common mistakes to avoid
- Add template script
- **Expected Result**: Robust, consistent implicit argument extraction

---

## Implementation Plan

**Status: ✅ COMPLETED (2025-10-27)**

Implementation order:

1. ✅ Create this assessment document (DONE)
2. ✅ Add implicit arguments section to extraction-fundamentals.md (lines 161-315)
3. ✅ Add common pitfalls to Pass 1 prompt (lines 246-258)
4. ✅ Update SKILL.md extraction-fundamentals.md description (line 100)
5. ✅ Create section_implicit_arguments_template.py (extraction-system/scripts/extraction/)

**Note**: All changes paper-agnostic, work for any research paper extraction.

---

## Validation Strategy

After implementation, validate on next paper extraction:

1. Check implicit arguments count (expect >3 for complex arguments)
2. Verify 4-type distribution (not just Type 1 bias)
3. Review trigger_text quality (specific passages, not vague)
4. Assess inference_reasoning (clear connection to triggers)
5. Compare fragility (expect more consistent results)

---

## Questions for User

1. Does this assessment align with your experience of "fragility"?
2. Are there specific implicit argument failures you've observed that we should address?
3. Should I proceed with implementation (Improvements 1-4)?
4. Priority order correct, or adjust?
