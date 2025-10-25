# Research Design Extraction - Gap Analysis

**Date:** 2025-10-25
**Issue:** v2.6.1 aimed to increase RD granularity but achieved opposite effect
**Baseline:** Chatbot extracted 5 RDs (without v2.6.1 guidance)
**Current:** CC v2.6.1 extracts 2 RDs (with granularity principle)
**Status:** ⚠️ CRITICAL - Target was increase, achieved 60% decrease

---

## Chatbot's Self-Assessment (What Worked)

### 1. Read Fundamentals Document First ✓
**Chatbot:** "I actually read extraction-fundamentals.md before starting. This grounded me in sourcing requirements."

**Current guidance:** Pass 1 prompt says "READ FIRST" but may not be enforced
- Line 60: `**READ FIRST:** /mnt/skills/user/research-assessor/references/extraction-fundamentals.md`

**Gap:** No verification that fundamentals were read; instruction may be skipped

---

### 2. Internalized the "WHY" Test ✓
**Chatbot:** "I consistently asked: Does this explain WHY research was framed this way?"

**Current guidance:** Present in both prompt and tier-assignment-guide
- Prompt line 29: "Strategic decisions about WHY research was framed this way"
- Prompt line 150: "Does this explain WHY research was framed/designed this way?"
- Tier guide line 15: "Is this about WHY the research was framed this way?"

**Gap:** None - guidance is clear

---

### 3. Recognized Multiple Design Types ✓
**Chatbot:** "I didn't just hunt for research questions. I extracted:
- Research questions (RD001, RD003, RD004, RD010)
- Study design decisions with rationale (RD002, RD007, RD008, RD009)
- Theoretical frameworks (RD005, RD006)"

**Current guidance:** Lists multiple types
- Prompt line 103: "questions, hypotheses, study designs, frameworks"
- Prompt lines 159-164: All five design_type categories listed

**Chatbot's types:**
- research_goal
- study_design_choice

**Current schema types:**
- research_framing
- theoretical_framework
- study_design
- scope_definition
- positionality

**Gap:** Schema complexity may be overwhelming; chatbot's simpler taxonomy (2 types) may have encouraged more granular extraction

---

### 4. Paid Close Attention to Introduction/Background ✓✓
**Chatbot:** "Most Research Designs live in Abstract/Introduction, not in Methods section. I invested time carefully reading these sections."

**Current guidance:**
- Prompt line 327: "Scan Abstract, Introduction, Background carefully"
- Tier guide line 72: "Most Research Designs appear in Abstract/Introduction/Background, NOT only in Methods"

**Emphasis difference:**
- Chatbot: "MOST RDs live in Introduction" (strong emphasis)
- Current: "Scan carefully" (weaker emphasis)

**Gap:** Not enough emphasis on WHERE to find RDs; no workflow step requiring Introduction analysis FIRST

---

### 5. Looked for "Design Language" Keywords ✓
**Chatbot:** Listed specific phrases:
- "The decision to..."
- "Our approach sought to..."
- "The aim of..."
- "We chose... because..."
- "rationale", "framework"

**Current guidance:**
- Prompt line 328: "Scan for design language keywords (see tier-assignment-guide.md)"
- Tier guide lines 51-56: Keywords listed

**Gap:** Keywords exist but are EXTERNAL REFERENCE; chatbot may have internalized them more effectively

---

### 6. Distinguished Description from Rationale ✓
**Chatbot:** "Critical distinction:
- ✅ 'Three activities were undertaken' → Research Design (study structure/framing)
- ❌ Each activity's procedure → Method/Protocol"

**Current guidance:**
- Tier guide lines 66-68: Counter-example provided

**Gap:** Only ONE counter-example; chatbot emphasizes this needs MULTIPLE examples

---

### 7. Captured Design Philosophy as Design ✓
**Chatbot:** "RD009 (workflow design philosophy) felt very high-level/abstract, but I included it because it explains WHY they structured the workflow."

**Current guidance:**
- Prompt line 334: "Liberal extraction: Include 'high-level' design elements"

**Emphasis difference:**
- Chatbot: Explicitly overcame hesitation about "too high-level"
- Current: Mentions it but may not emphasize enough

**Gap:** May need stronger language: "If it feels 'too obvious' or 'too high-level,' that's usually a sign it's a Research Design - extract it anyway"

---

### 8. Recognized Theoretical Frameworks as Designs ✓
**Chatbot:** "RD005 (Utility-Usability framework) and RD006 (HCI principles) are theoretical frameworks that ground design choices."

**Current guidance:**
- Tier guide line 71: "Theoretical frameworks ARE Research Designs"

**Gap:** Mentioned once; chatbot extracted TWO framework items, suggesting it really internalized this

---

### 9. Was Liberal in Pass 1 ✓
**Chatbot:** "The prompt says 'when in doubt, include it' - I took this seriously for Research Designs."

**Current guidance:**
- Prompt line 123: "When uncertain: INCLUDE IT"
- Prompt line 334: "Liberal extraction"

**Gap:** General liberalism stated, but may need RD-SPECIFIC liberalism emphasis

---

### 10. Read for Meta-Level Framing ✓
**Chatbot:** "RD002 required recognizing that the paper isn't just describing what they did - it's testing a design hypothesis about when crowdsourcing becomes worthwhile."

**Current guidance:** Not explicitly addressed

**Gap:** ⚠️ MAJOR - No guidance on recognizing "meta-level" research designs (e.g., comparative evaluation as a strategic design choice)

---

## What the Chatbot Identified as Missing from Current Guidance

### Missing Element 1: Explicit Workflow Step - "Scan for Design Language FIRST"
**Chatbot recommendation:** "Before extracting anything, do a quick scan marking sections with decision points, theoretical frameworks, study structure explanations."

**Current workflow:** Goes straight to "Step 1: Identify Research Designs"

**Gap:** No pre-extraction scan step

---

### Missing Element 2: Design Language Keyword List (Inline)
**Chatbot recommendation:** Provide keywords IN THE PROMPT, not just reference

**Current:** External reference to tier-assignment-guide.md

**Gap:** May be skipped or not internalized

---

### Missing Element 3: Multiple Counter-Examples
**Chatbot recommendation:** Provide multiple NOT/IS pairs

**Current:** One counter-example in tier guide (line 66-68)

**Gap:** Insufficient examples

---

### Missing Element 4: Design Types Checklist
**Chatbot recommendation:**
```
For each paper section, ask:
□ Research questions stated?
□ Hypotheses stated?
□ Theoretical frameworks referenced?
□ Study design decisions explained?
□ Design philosophy/rationale discussed?
```

**Current:** No checklist format

**Gap:** ⚠️ MAJOR - Checklist would operationalize "multiple types" recognition

---

### Missing Element 5: Strong Emphasis on Introduction/Background
**Chatbot recommendation:**
```
CRITICAL: Most Research Designs appear in:
- Abstract (study framing)
- Introduction (research questions, aims)
- Background (theoretical frameworks)

Methods section primarily contains Methods and Protocols, not Designs.
```

**Current:** "Scan carefully" (line 327)

**Gap:** Not strong enough; needs CRITICAL emphasis

---

### Missing Element 6: Rubric for design_type Classification
**Chatbot recommendation:** Clear if-then rules for each type

**Current:** Types listed but no classification rubric

**Gap:** May lead to wrong type assignment or skipping items

---

### Missing Element 7: "Design Rationale Pattern" Recognition
**Chatbot recommendation:**
```
Pattern: [Decision] + [Because/Rationale] = Research Design

Examples:
- "We chose X because Y" → Design
- "Our approach sought to..." → Design
```

**Current:** Implicit in "WHY" test but not operationalized as pattern

**Gap:** Pattern recognition not explicit

---

### Missing Element 8: RD-Specific Liberal Extraction Emphasis
**Chatbot recommendation:** "Research Designs often feel 'obvious' or 'too high-level' - include them anyway."

**Current:** General liberalism, not RD-specific

**Gap:** May lead to conservative RD extraction despite liberal philosophy

---

### Missing Element 9: Worked Examples from Real Extraction
**Chatbot recommendation:** Include RD005, RD006, RD009 as examples

**Current:** Generic hypothetical examples only

**Gap:** ⚠️ MAJOR - No real-world examples showing theoretical frameworks, design philosophy

---

### Missing Element 10: Meta-Level Framing Recognition
**Chatbot recommendation:** Guidance on recognizing when paper has design-level hypothesis (e.g., "comparative evaluation to test efficiency thresholds")

**Current:** Not addressed

**Gap:** ⚠️ CRITICAL - This is likely why current extraction misses higher-level designs

---

## Schema Complexity Hypothesis

### Chatbot Schema (simpler)
```json
{
  "design_id": "RD001",
  "design_type": "research_goal",  // Only 2 types: research_goal, study_design_choice
  "design_text": null,             // Simple structure
  ...
}
```

### Current Schema v2.5 (complex)
```json
{
  "design_id": "RD001",
  "design_type": "research_framing",  // 5 types: research_framing, theoretical_framework, study_design, scope_definition, positionality
  "design_text": "...",
  "research_framing": {               // Conditional complex object
    "research_questions": [...],
    "hypotheses": [...],
    "emergent_findings": [...]
  },
  "confirmatory_stance": {...},
  "theoretical_framework": {...},
  "study_design": {...},
  "scope": {...},
  "positionality": {...}
}
```

**Hypothesis:** Complex conditional schema may lead to:
1. Cognitive overload - too many decisions per item
2. Tendency to consolidate to avoid complexity
3. Uncertainty about which conditional fields to populate

**Evidence:** Chatbot with simple schema → 5 items; Current with complex schema → 2 items

---

## Root Cause Analysis

### Why did v2.6.1 changes have OPPOSITE effect?

**v2.6.1 changes (from commit d48336f):**
1. Added "Research Design Granularity Principle" to tier-assignment-guide
2. Added design language keywords
3. Added consolidation rules: "RDs preserve granularity (unlike Evidence)"
4. Emphasized Abstract/Introduction/Background sections for RD extraction

**Paradox:** All changes SHOULD increase granularity, but decreased it instead

**Possible explanations:**

1. **Schema Complexity Override:** Despite prompt improvements, complex schema discourages granular extraction

2. **Consolidation Guidance Misinterpreted:** Pass 2/Pass 4 prompts may emphasize consolidation too much, overriding Pass 1 liberal extraction

3. **Examples Insufficient:** Generic examples don't show actual granularity level needed

4. **Checklist Absence:** Without operational checklist, guidance remains abstract

5. **Reading Pattern:** CC may not be reading Introduction as carefully as chatbot did

6. **Field Population Burden:** Complex conditional fields may create pressure to minimize items

---

## Diagnostic Questions for Current Extraction

**For the 2 RDs extracted by current CC:**

1. RD001: Case study research design
   - Is this ONE design or could it be split?
   - Chatbot might have extracted: RD001 (research goal) + RD002 (case study choice) separately

2. RD002: Comparative evaluation design
   - Is this ONE design or could it be split?
   - Chatbot might have extracted: RD003 (comparative framework) + RD004 (efficiency threshold hypothesis) + RD005 (theoretical framework)

**Key question:** Are current RDs APPROPRIATELY HOLISTIC or OVER-CONSOLIDATED?

---

## Recommendations

### Immediate (P0) - Prompt Changes

1. **Add Pre-Extraction Scan Step** (before Step 1)
```markdown
### Step 0: Pre-Scan for Research Designs (REQUIRED)

Before extracting any RDMAP items, scan the ENTIRE paper for design elements:

Read in this order:
1. Abstract - Study framing, aims
2. Introduction - Research questions, hypotheses, context
3. Background/Literature Review - Theoretical frameworks
4. Methods Introduction - Study design rationale

Mark passages with:
□ Decision language ("chose," "selected," "decision to")
□ Rationale language ("because," "rationale," "reasoning")
□ Purpose language ("aimed to," "sought to," "designed to")
□ Framework language ("framework," "guided by," "informed by")
□ Study structure descriptions

This scan informs Step 1 extraction.
```

2. **Add Design Types Checklist to Step 1**
```markdown
For EACH major paper section (Abstract, Intro, Methods), systematically check:
□ Research questions explicitly stated?
□ Hypotheses explicitly stated?
□ Theoretical frameworks referenced?
□ Study design decisions explained with rationale?
□ Design philosophy or workflow rationale discussed?
□ Scope boundaries justified?

Extract ALL that apply as separate RDs.
```

3. **Add RD-Specific Liberal Extraction Warning**
```markdown
⚠️ **Research Designs often feel "too obvious" or "too high-level"**

If you're thinking "this seems too basic" or "everyone knows this" → EXTRACT IT ANYWAY.

Design-level decisions that feel obvious are usually the most critical for transparency assessment.

Examples that should be extracted:
✓ "We chose mobile over desktop" (even if seems obvious from context)
✓ "Comparative evaluation to test efficiency" (even if entire paper is comparative)
✓ "Case study design" (even if paper is obviously a case study)
```

4. **Add Inline Design Language Keywords** (don't just reference external doc)
```markdown
**Design Language Signals - Extract when you see:**
- Decision: "chose," "selected," "opted for," "decision to"
- Rationale: "because," "rationale," "reasoning," "given that"
- Purpose: "aimed to," "sought to," "designed to," "intended to"
- Framework: "framework," "approach," "paradigm," "guided by"
- Comparison: "compared," "evaluated," "tested whether"
```

5. **Add Multiple Counter-Examples**
```markdown
**NOT a Research Design → IS a Research Design:**

❌ "We used FAIMS Mobile"
✅ "We chose FAIMS Mobile for offline capability and usability"

❌ "Data were collected via survey"
✅ "We selected survey methodology to cover large spatial area efficiently"

❌ "We analyzed patterns"
✅ "We adopted an exploratory analytical framework to identify emergent patterns"

❌ "Students participated"
✅ "We recruited field school students as novice volunteers to test generalizability"
```

### High Priority (P1) - Schema Simplification

6. **Consider Reverting to Simpler design_type Taxonomy**

Chatbot's approach:
- `research_goal` - What the research aims to accomplish
- `study_design_choice` - Strategic decisions about how to structure research

Current v2.5:
- `research_framing`, `theoretical_framework`, `study_design`, `scope_definition`, `positionality`

**Hypothesis:** Simpler taxonomy = more granular extraction (less anxiety about "getting type right")

7. **Make Conditional Fields Optional**

Current schema requires choosing which conditional object to populate (research_framing vs theoretical_framework vs study_design).

Recommendation: Make ALL conditional fields optional; allow extraction with just design_text + design_type

### Medium Priority (P2) - Examples and Documentation

8. **Add Real-World Worked Example**

Include chatbot's actual Sobotkova extraction as appendix showing:
- RD001-RD010 actual items
- Why each is separate
- How granularity looks in practice

9. **Add Pass 4 Quality Check**
```markdown
**Research Design Count Check:**
- Typical range: 3-6 research designs for fieldwork papers
- If count < 3: Review for under-extraction
  - Check if design decisions consolidated into single item
  - Check if theoretical frameworks extracted
  - Check if comparative/evaluative framing recognized as design
- If count > 8: Review for over-extraction
  - Check if methods misclassified as designs
```

10. **Add Meta-Level Framing Guidance**
```markdown
**Recognizing Meta-Level Research Designs:**

Papers often have strategic-level design choices that frame entire research:

Examples:
- "Comparative evaluation of platform efficiency" (comparison AS design choice)
- "Case study to demonstrate approach transferability" (case study AS strategic choice)
- "Exploratory analysis to identify patterns" (exploratory stance AS design)

These feel "obvious" because they frame the whole paper - extract them anyway.
```

---

## Testing Plan

After implementing changes, test with Sobotkova et al. 2023:

**Expected outcome:** 4-6 research designs including:
1. Research goal/aim (what paper seeks to accomplish)
2. Case study design choice
3. Comparative evaluation framework
4. Efficiency threshold hypothesis/question
5. Theoretical framework (if applicable - e.g., crowdsourcing theory)
6. Platform selection rationale (FAIMS vs alternatives)

**Current outcome:** 2 research designs (case study + comparative evaluation consolidated)

**Success criteria:** Achieve 4+ research designs with clear rationales for separate extraction

---

## Summary

**Core Problem:** Despite adding granularity guidance in v2.6.1, extraction became LESS granular

**Root Causes:**
1. Schema complexity creates consolidation pressure
2. Guidance not operationalized (checklists, inline examples)
3. Introduction reading not emphasized enough
4. No pre-scan workflow step
5. RD-specific liberal extraction not emphasized
6. Meta-level framing recognition not addressed

**Solution Direction:**
- Immediate: Add operational checklists, inline examples, pre-scan step
- Long-term: Consider schema simplification

**Key Insight from Chatbot:**
> "Research Designs answer 'WHY frame it this way?' not 'WHAT did we do?' Keeping that distinction sharp, combined with careful reading of Introduction sections and attention to 'design language,' seems to be the recipe for success."

The chatbot succeeded because it INTERNALIZED and OPERATIONALIZED the guidance through:
- Systematic section-by-section review
- Active pattern recognition (design language)
- Overcoming "too obvious" hesitation
- Recognizing theoretical frameworks as designs

Current guidance has the CONTENT but lacks OPERATIONALIZATION.
