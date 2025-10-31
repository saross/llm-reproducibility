# ANTI-PATTERN: Failed Extraction Planning Prompt

**Date Created:** 2025-10-30
**Date Archived:** 2025-10-31
**Original Location:** extraction-system/staging/extraction-planning-prompt.md
**Reason for Failure:** Too prescriptive, acted as template rather than primer

---

## Why This Failed

1. **Too directive:** Told Claude WHAT to write instead of HOW to think
2. **Too long:** 148 lines - should be 10-20 lines core content
3. **Template approach:** Tried to prescribe format instead of priming thought process
4. **User feedback:** "Plans became much worse after using this - it failed, and your plans became much worse so I stopped using it"

---

## Lessons Learned

### What Didn't Work

- **Prescriptive templates**: Providing a fill-in-the-blank structure
- **Duplicating documentation**: Repeating content already in WORKFLOW.md
- **Example format sections**: Showing exact format to follow
- **Long-form prompts**: Too much instruction creates cognitive overload

### What Does Work

- **Brief primers**: 10-20 lines that point to documentation
- **Reference-based**: Point to WORKFLOW.md, don't duplicate it
- **Thinking prompts**: Prime thought process, don't prescribe outputs
- **Trust documentation**: Detailed guidance belongs in WORKFLOW.md, not launch prompts

---

## Replacement

See `input/EXTRACTION_LAUNCH.md` for the corrected approach:
- Brief (25 lines core content)
- Points to documentation
- Primes thinking without prescribing
- Trusts WORKFLOW.md for detailed guidance

---

## Historical Context

This prompt was created in response to recurring planning issues. The intent was good (ensure comprehensive plans), but the execution was flawed (too prescriptive). The issues it tried to address are now properly handled by:

1. **WORKFLOW.md** "Planning Mode Requirements" section at top
2. **EXTRACTION_PLAN_UNIFIED_MODEL.md** flexible planning model
3. **EXTRACTION_LAUNCH.md** brief primer that references these documents

---

# Original Content Below

---

# Extraction Planning Prompt

Use this prompt to initiate the extraction planning process for the next paper in the queue.

---

## Prompt

Please review the extraction queue and workflow documentation, then develop a comprehensive plan for extracting the next paper:

1. **Check queue:** Read `input/queue.yaml` to identify the next paper with `status: pending`
2. **Review workflow:** Read `input/WORKFLOW.md` to understand the 7-pass extraction process
3. **Develop plan:** Create a detailed extraction plan following the workflow structure

### Critical Requirements

**Skill Invocation:**
- **You MUST invoke the research-assessor skill at the start of pre-flight and keep it invoked throughout ALL 7 passes**
- This skill provides essential extraction guidance and is crucial for success
- Do not proceed without activating this skill

**Section-by-Section Approach (Pass 1 and Pass 3):**
- Define section groups for the paper (typically 4-8 groups based on paper structure and length)
- Apply chunking strategy: maximum 1500 words per section, natural boundaries preferred
- Use the SAME section groups for both Pass 1 (claims/evidence) and Pass 3 (RDMAP)
- Process each section group sequentially, creating one script per section

**Equal Attention to All Sections (Pass 3):**
- Pay EQUAL attention to the ENTIRE paper during Pass 3 RDMAP extraction
- DO NOT over-focus on the Methods section
- Research designs often appear in Introduction, Theory, Discussion, and Conclusions
- Methods, protocols, and implicit RDMAP can appear in any section
- Over-focusing on Methods leads to under-extraction of research designs and other RDMAP items

**Liberal Over-Extraction Philosophy:**

For **Pass 1 (Claims/Evidence):**
- **Approach:** Liberal extraction, cast wide net, aim for over-extraction (40-50% more than final target)
- Extract every potential claim, evidence item, and implicit argument
- Items will be consolidated in Pass 2 - better to over-extract than miss items
- Target: 60-100 claims, 30-60 evidence items initially

For **Pass 3 (RDMAP):**
- **Approach:** Liberal extraction, cast wide net, aim for over-extraction (40-50% more than final target)
- MIRROR the liberal approach used in Pass 1
- Be ESPECIALLY liberal with research designs (commonly under-extracted)
- Extract every potential research design, method, and protocol
- Items will be consolidated in Pass 5 - better to over-extract than miss items
- Target: 4-8 research designs, 12-20 methods, 20-35 protocols initially

**Rationalization Philosophy:**
- Pass 2 (claims/evidence) and Pass 5 (RDMAP) perform CONSERVATIVE consolidation
- Target 15-20% reduction, but accept 10-15% for well-differentiated technical papers
- Preserve distinct claims/RDMAP items, only merge true redundancies

### Plan Structure

Your extraction plan should include:

1. **Pre-Flight:** Paper identification, directory setup, schema initialisation
2. **Pass 0:** Metadata extraction from title page (8 fields)
3. **Pass 1:** Liberal claims/evidence extraction
   - Define section groups (list all with page ranges)
   - State liberal over-extraction approach explicitly
   - Create pass1_section{N}_{description}.py for each section
4. **Pass 2:** Rationalize claims/evidence (conservative consolidation)
5. **Pass 3:** Liberal RDMAP extraction
   - Use SAME section groups as Pass 1
   - State liberal over-extraction approach explicitly (especially for research designs)
   - Equal attention to all sections
   - Create pass3_rdmap_extraction.py
6. **Pass 4:** Extract implicit RDMAP (mentioned-but-undocumented procedures)
7. **Pass 5:** Rationalize RDMAP (conservative consolidation)
8. **Pass 6:** Validate extraction (cross-references, hierarchy, metadata, sourcing)
9. **Post-extraction:** Generate summary.md, update queue.yaml

### Example Opening for Your Plan

```markdown
# Extraction Plan: [Paper Title]

## Paper Details
- Path: [from queue.yaml]
- Slug: [from queue.yaml]
- Pages: [check PDF]
- Type: [methods paper / research article / etc.]

## Pre-Flight
1. Invoke research-assessor skill
2. Load paper from path
3. Create outputs/{slug}/ directory
4. Initialize extraction.json with schema v2.5

## Pass 0: Metadata Extraction
Extract 8 metadata fields from title page...

## Pass 1: Liberal Claims/Evidence Extraction

**Section Groups:** (SAME groups will be used for Pass 3)
1. Section 1: Abstract + Introduction (pp. X-Y, ~Z words)
2. Section 2: [description] (pp. A-B, ~C words)
...

**Approach:** Liberal extraction, cast wide net, aim for over-extraction. Extract every potential claim, evidence item, and implicit argument. Items will be consolidated in Pass 2.

**Target:** 60-100 claims, 30-60 evidence items

**Scripts:**
- pass1_section1_abstract_intro.py
- pass1_section2_[description].py
...

## Pass 3: Liberal RDMAP Extraction

**Section Groups:** SAME as Pass 1 above

**Approach:** Liberal extraction, cast wide net, aim for over-extraction. MIRROR Pass 1 liberal approach. Be ESPECIALLY liberal with research designs. Pay EQUAL attention to all sections (not just Methods). Items will be consolidated in Pass 5.

**Target:** 4-8 research designs, 12-20 methods, 20-35 protocols

**Script:** pass3_rdmap_extraction.py

[Continue with remaining passes...]
```

---

## Usage Notes

- Use this prompt at the start of each new extraction
- Review the plan with the user if ambiguities exist (e.g., unclear section structure)
- Proceed autonomously once plan is confirmed
- Do not stop between passes - work through all 7 passes continuously
- Update queue.yaml checkpoints after each major pass

## Common Pitfalls to Avoid

1. ❌ Forgetting to invoke research-assessor skill
2. ❌ Using different section groups for Pass 1 vs Pass 3
3. ❌ Over-focusing on Methods section during Pass 3
4. ❌ Not being liberal enough with research design extraction
5. ❌ Not explicitly stating liberal over-extraction approach for Pass 1 and Pass 3
6. ❌ Stopping to ask user "Should I continue?" between passes

## Version History

- v1.0.0 (2025-10-30): Initial version combining lessons learned from ross-et-al-2009 and previous extractions
