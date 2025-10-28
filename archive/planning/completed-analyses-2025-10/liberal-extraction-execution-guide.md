# Liberal Extraction Execution Guide

**Purpose:** Ensure comprehensive extraction across varied papers without relying on hard quantitative targets

**Problem:** Extraction can regress to conservative behaviour, missing 50-80% of extractable content by prioritising precision over comprehensiveness during liberal passes

**Solution:** Paper-agnostic indicators and process checks that trigger appropriate liberal extraction behaviour

---

## Core Principle

**Pass 1/3 Philosophy:** Comprehensiveness >> Precision
**Pass 2/4 Philosophy:** Precision >> Over-capture

During liberal passes, **when uncertain whether to extract an item: INCLUDE IT**. Pass 2/4 will consolidate and refine.

---

## 1. Process Indicators (Paper-Agnostic)

### Systematic Implicit Extraction Checklist

**For Pass 1 (Claims & Evidence):**

After extracting explicit claims from each section, run systematic implicit argument scan:

- [ ] For EACH core claim, applied all 4 implicit argument recognition patterns:
  - [ ] Type 1: Logical Implications ("If this is true, what must also be true?")
  - [ ] Type 2: Unstated Assumptions ("What must be true for this to hold?")
  - [ ] Type 3: Bridging Claims ("How do they get from evidence to claim?")
  - [ ] Type 4: Disciplinary Assumptions ("What field knowledge is taken for granted?")

- [ ] Documented scan methodology in extraction_notes if no implicit arguments found
- [ ] Applied 6 recognition patterns from extraction-fundamentals.md:212-248

**For Pass 3 (RDMAP):**

After extracting explicit RDMAP from each section:

- [ ] Scanned for implicit RDMAP using 4 recognition patterns (extraction-fundamentals.md:115-137):
  - [ ] Pattern 1: Mentioned Procedure (verbs without procedures: "cleaned", "validated", "checked")
  - [ ] Pattern 2: Inferred from Results (effects implying causes, thresholds implying monitoring)
  - [ ] Pattern 3: Undocumented Assignment ("assigned maps" without allocation method)
  - [ ] Pattern 4: Implied Strategic Decision (positioning without explicit design statement)

- [ ] Checked Results/Discussion sections specifically for undocumented procedures mentioned
- [ ] Documented implicit scan in extraction_notes

**Red Flag:** "No implicit items found" without documented systematic scan = incomplete extraction

---

## 2. Relative Indicators (Within-Paper Calibration)

### Evidence:Claims Ratio Check

**After completing Pass 1:**

```bash
jq '{evidence: (.evidence|length), claims: (.claims|length), ratio: ((.evidence|length) / (.claims|length))}' extraction.json
```

**Ratio interpretation (paper-agnostic):**
- **0.5-1.0:** Claims outweigh evidence → May indicate under-extraction of evidence OR evidence-lean theoretical paper
- **1.0-2.0:** Typical balanced range → Most papers fall here
- **2.0+:** Evidence-heavy → Typical for empirical papers with many measurements

**Action if ratio < 1.0:**
- Review Results section: Are quantitative outcomes extracted as separate evidence items?
- Check: Are you bundling multiple evidence items into single claims?
- Consider: Is this actually a theoretical/review paper with fewer direct observations?

### RDMAP Hierarchy Balance Check

**After completing Pass 3:**

```bash
jq '{designs: (.research_designs|length), methods: (.methods|length), protocols: (.protocols|length), m_per_d: ((.methods|length) / (.research_designs|length)), p_per_m: ((.protocols|length) / (.methods|length))}' extraction.json
```

**Typical ratios (paper-agnostic):**
- **Methods per Design:** 1.5-4.0 (each strategic decision enables multiple methods)
- **Protocols per Method:** 1.5-3.0 (each method realized through multiple protocols)

**Action if ratios are < 1.0:**
- Under-extraction at lower tiers → Protocols and Methods sections need more granular extraction
- Check: Are you bundling multiple protocols into single method descriptions?

**Action if Designs = 0-1:**
- Likely missing strategic-level framing (research questions, hypotheses, frameworks, study designs)
- Re-scan Abstract, Introduction, and Methods for WHY-level decisions
- See: research-design-operational-guide.md Section 6 (Sobotkova example: 4-6 designs expected for most papers)

---

## 3. Mid-Pass Reflection Checkpoints

### After Each Section Group

**Self-reflection questions:**

1. **Inclusion threshold check:**
   - "Did I extract items I was uncertain about, or only high-confidence items?"
   - If only high-confidence → Adjust to be MORE liberal in next section

2. **Granularity check:**
   - "Am I extracting compound items as single entities, or breaking them into components?"
   - Example: "10,827 features from Soviet maps in 2017-2018" → Should be 3-4 evidence items
   - If bundling → Increase granularity in next section

3. **Implicit extraction check:**
   - "Did I systematically scan for implicit arguments/RDMAP, or only extract obvious items?"
   - If skipped systematic scan → Apply patterns in next section

4. **Trajectory check:**
   - "Am I on pace for comprehensive extraction, or tracking conservatively?"
   - Simple test: Count items so far, estimate if trajectory will be comprehensive
   - Adjust liberalness in remaining sections if needed

**Document reflections:** Add notes to extraction_notes after each section group

---

## 4. Consolidation Rate as Retrospective Check

### Pass 2/4: Expected Rationalization

**Liberal extraction produces rationalization opportunities:**
- **Pass 2 (Claims/Evidence):** Expect to consolidate 15-20% of Pass 1 items
- **Pass 4 (RDMAP):** Expect to consolidate 15-20% of Pass 3 items

**Consolidation patterns that indicate healthy liberal extraction:**
- Redundant observations → Merge similar evidence items
- Overlapping claims → Consolidate claims covering same assertion
- Granular protocols → Merge sequential steps into unified procedures
- Duplicate attributions → Combine items from multiple mentions

**Red flag consolidation rates:**

- **0-5% consolidation:** Pass 1/3 was TOO CONSERVATIVE
  - Items already filtered and refined during extraction
  - Missed the "40-50% over-extraction" target
  - **Action:** Consider supplementary extraction pass to capture missing content

- **5-15% consolidation:** Mildly conservative (acceptable but not ideal)
  - Some over-extraction but less than intended
  - **Action:** Document in extraction_notes; be more liberal in future papers

- **15-25% consolidation:** IDEAL RANGE
  - Liberal extraction philosophy successfully applied
  - Pass 2/4 performing intended refinement function

- **25%+ consolidation:** Aggressive over-extraction (acceptable)
  - Strong liberal application, may be extracting marginal items
  - This is acceptable - better to over-extract than under-extract

**Self-check during Pass 2/4:**

If finding minimal consolidation opportunities:
```markdown
**extraction_notes warning:**
"Pass 2 identified only 3 consolidation opportunities (5% of items).
This indicates Pass 1 was too conservative, likely missing 30-50% of
extractable content. Recommend supplementary extraction pass before
proceeding to Pass 3."
```

---

## 5. Cross-Paper Benchmark Comparisons

### Compare Against Similar Papers

**When available, use prior extractions as calibration:**

For papers of similar:
- Length (page count)
- Type (empirical vs theoretical vs methods)
- Domain (archaeology, biology, ethnography)

Compare final extraction counts as sanity check:

```bash
# Current extraction
jq '{total: ((.evidence|length) + (.claims|length) + (.implicit_arguments|length) + (.research_designs|length) + (.methods|length) + (.protocols|length))}' outputs/current-paper/extraction.json

# Prior similar paper
jq '{total: ((.evidence|length) + (.claims|length) + (.implicit_arguments|length) + (.research_designs|length) + (.methods|length) + (.protocols|length))}' archive/output/cc-sonnet45/similar-paper-RUN-XX/extraction.json
```

**Interpretation:**
- **Within 20-30% of benchmark:** Reasonable variance (different content density)
- **< 50% of benchmark:** Likely under-extraction (investigate)
- **> 200% of benchmark:** Possible over-extraction OR genuinely denser content

**Example:**
- Sobotkova RUN-05: 275 items (13-page empirical methods paper)
- Sobotkova current: 48 items (same paper) → 17% of benchmark → **Under-extraction confirmed**

---

## 6. Calibration Statements (Explicit Commitments)

### Pre-Pass 1 Calibration

Before starting Pass 1, explicitly state:

```markdown
**Pass 1 Liberal Extraction Commitment:**

I will follow liberal extraction philosophy for this pass:
- When uncertain whether to extract an item: INCLUDE IT
- When uncertain about item boundaries: SPLIT INTO MULTIPLE ITEMS
- Target: Over-extract rather than under-extract (Pass 2 will consolidate)
- Apply systematic implicit extraction patterns (not just obvious items)
- Check mid-pass indicators and adjust liberalness if tracking conservative
- Expect Pass 2 to consolidate 15-20% of items (if less, I was too conservative)
```

### Pre-Pass 3 Calibration

Before starting Pass 3, explicitly state:

```markdown
**Pass 3 Liberal RDMAP Extraction Commitment:**

I will follow liberal extraction for RDMAP:
- Extract strategic designs even if they seem "obvious" (framing decisions are designs)
- Scan systematically for implicit RDMAP in Results/Discussion (not just Methods section)
- When uncertain about Design vs Method vs Protocol: EXTRACT AT MULTIPLE TIERS
- Expect 4-6 Research Designs minimum (study design, frameworks, strategic decisions)
- Expect Pass 4 to consolidate 15-20% of items
```

---

## 7. Liberal Extraction Examples Reference

### Liberal vs Conservative Extraction Patterns

**Evidence Extraction:**

❌ **Too Conservative:**
- "10,827 features digitised from Soviet maps in 2017-2018" → Single evidence item

✅ **Appropriately Liberal:**
- E001: "10,827 mound features digitised" (quantitative outcome)
- E002: "Features digitised from Soviet military topographic maps" (data source)
- E003: "Digitisation conducted during 2017-2018 seasons" (temporal scope)
- E004: "FAIMS Mobile used for digitisation" (tool specification)
- → Pass 2 may consolidate E002+E001, E003+E001 if they're never cited independently

**RDMAP Extraction:**

❌ **Too Conservative:**
- Extract only 2 research designs (main research question + study design)

✅ **Appropriately Liberal:**
- RD001: Comparative evaluation design (vs GIS and ML)
- RD002: Efficiency hypothesis (crowdsourcing efficiency claim)
- RD003: Usability framework (HCI principles adaptation)
- RD004: Case study approach (demonstrate feasibility)
- RD005: Threshold analysis framework (quantitative boundaries)
- RD006: Scalability investigation (optimal range determination)
- → Pass 4 may consolidate RD004+RD001 if case study is subsumed by comparative design

**Implicit Argument Extraction:**

❌ **Too Conservative:**
- Extract only 1-2 obvious logical implications

✅ **Appropriately Liberal:**
- IA001: Efficiency measured by staff time (unstated assumption - Type 2)
- IA002: Generalisability beyond Bulgarian mounds (unstated assumption - Type 2)
- IA003: HCI principles transfer to deskbound work (disciplinary assumption - Type 4)
- IA004: Comparison baseline is failed 2010 attempt (bridging claim - Type 3)
- IA005: Adequate GPS accuracy for analysis scale (capability assumption - Type 2)
- IA006: Volunteer competence adequate for quality (logical implication - Type 1)
- IA007: Threshold calculations assume linear scaling (logical implication - Type 1)
- → Pass 2 may consolidate if some are redundant

---

## 8. Execution Checklist

### During Liberal Extraction Passes (Pass 1 & Pass 3)

**Before starting:**
- [ ] Read and commit to liberal extraction philosophy
- [ ] State explicit calibration commitment
- [ ] Prepare to apply systematic implicit extraction patterns

**After each section group:**
- [ ] Document mid-pass reflection in extraction_notes
- [ ] Check relative indicators (ratios, trajectory)
- [ ] Adjust liberalness for next section if needed
- [ ] Save progress to extraction.json

**After completing pass:**
- [ ] Check RDMAP hierarchy balance (if Pass 3)
- [ ] Check evidence:claims ratio (if Pass 1)
- [ ] Document extraction approach in extraction_notes

### During Rationalization Passes (Pass 2 & Pass 4)

**During consolidation:**
- [ ] Track consolidation rate (% of items merged)
- [ ] Document consolidation patterns

**After completing pass:**
- [ ] Calculate consolidation rate: (items_removed / items_before) * 100
- [ ] Interpret consolidation rate:
  - 0-5%: Too conservative in prior pass (document warning)
  - 5-15%: Mildly conservative (acceptable)
  - 15-25%: Ideal range
  - 25%+: Aggressive liberal extraction (acceptable)
- [ ] If < 15% consolidation: Consider supplementary extraction pass

---

## 9. Warning Signs of Conservative Extraction

### During Extraction

- Hesitating to extract items due to uncertainty about classification
- Bundling multiple observations into single evidence items
- Only extracting "important" or "core" items
- Skipping systematic implicit scans because "nothing obvious found"
- Thinking "Pass 2 will catch this if important" (backwards - Pass 2 filters, not discovers)

### After Extraction

- Pass 2/4 finds < 15% consolidation opportunities
- Evidence:claims ratio < 1.0 (for empirical papers)
- Research Designs = 0-2 (most papers have 4-6 strategic decisions)
- Protocols:methods ratio < 1.5 (under-extraction at operational tier)
- Total extraction < 50% of comparable benchmark paper
- No implicit arguments despite core claims present
- No implicit RDMAP despite Results/Discussion mentioning procedures

### Response to Warning Signs

1. **During extraction:** Immediately increase liberalness in remaining sections
2. **After extraction:** Document in extraction_notes with consolidation rate analysis
3. **Before proceeding:** Consider supplementary extraction pass if severely under-extracted
4. **For future papers:** Review this guide and re-commit to liberal philosophy

---

## 10. User Invocation Pattern

### Recommended User Instruction

When initiating extraction workflow, include:

```markdown
Execute the extraction workflow with liberal extraction approach:

1. Follow liberal extraction philosophy aggressively
   - Apply "when uncertain, include it" principle consistently
   - Over-extract rather than under-extract (Pass 2/4 will consolidate)
   - Trust the rationalization passes to refine

2. Apply systematic implicit extraction patterns
   - 4-type implicit argument scan for EACH core claim
   - 4-pattern implicit RDMAP scan for EACH section
   - Document scan methodology if no implicit items found

3. Use mid-pass reflection checkpoints
   - After each section group, check relative indicators
   - Adjust liberalness if tracking conservative
   - Document reflections in extraction_notes

4. Monitor consolidation rate in Pass 2/4
   - Target: 15-20% consolidation rate
   - If < 15%: Document as conservative extraction warning
   - If < 5%: Consider supplementary extraction pass

Reference: planning/liberal-extraction-execution-guide.md
```

---

## Appendix: Why This Matters

**Conservative extraction impact:**
- Assessment-critical content missed (implicit assumptions, methodological gaps)
- Transparency evaluation compromised (incomplete RDMAP extraction)
- Reproducibility assessment limited (missing protocols and decision points)
- Cross-paper comparisons invalid (inconsistent extraction depth)

**Liberal extraction with rationalization:**
- Comprehensive capture in Pass 1/3 ensures nothing important missed
- Refinement in Pass 2/4 improves precision and eliminates redundancy
- Final extraction is both comprehensive AND high-quality
- Process is systematic and consistent across papers

**The goal:** Extract everything assessment-relevant, then refine. Not: extract only what seems most important.

---

**Version:** 1.0
**Last Updated:** 2025-10-28
**Status:** Active execution guide
**Related:** WORKFLOW.md, extraction-fundamentals.md, prompts 01/02/03/04
