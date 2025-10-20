# Research Assessor v2.4 - Quick Reference & Testing Checklist

**Keep this open during testing!**

---

## Complete Workflow

```
📄 Blank Template (schema v2.4)
         ↓
📝 Claims Pass 1 → Liberal extraction of evidence, claims, implicit_arguments
         ↓
🔍 Claims Pass 2 → Rationalize (15-20% reduction expected)
         ↓
📝 RDMAP Pass 1 → Liberal extraction of research_designs, methods, protocols
         ↓
🔍 RDMAP Pass 2 → Rationalize (15-20% reduction expected)
         ↓
✅ Validation Pass 3 → Integrity checks (produces separate report)
         ↓
🎯 Complete Extraction
```

**Key Principle:** Single JSON document flows through all passes. Each pass modifies only its designated arrays.

---

## Pass Responsibilities

| Pass | Modifies | Leaves Alone | Expected Output |
|------|----------|--------------|-----------------|
| Claims P1 | evidence, claims, implicit_arguments | RDMAP arrays | 40-60 evidence, 30-50 claims |
| Claims P2 | evidence, claims, implicit_arguments | RDMAP arrays | 15-20% reduction |
| RDMAP P1 | research_designs, methods, protocols | Claims/evidence arrays | 10-15 designs, 20-30 methods, 15-25 protocols |
| RDMAP P2 | research_designs, methods, protocols | Claims/evidence arrays | 15-20% reduction |
| Validation P3 | Nothing (reads only) | All arrays | Validation report (separate JSON) |

---

## Conversation Template

**For Each Pass:**

```
You: I'm using the research-assessor skill for [Pass Name].

Here's the [Pass Name] prompt:
[paste entire prompt from project knowledge]

[If Pass 1:]
Extract from this section:
[paste source text]

Use this JSON:
[paste blank template or previous pass output]

[If Pass 2:]
Here's the source text for verification:
[paste original section]

Here's the Pass 1 extraction to rationalize:
[paste Pass 1 JSON]

[If Pass 3:]
Here's the complete extraction to validate:
[paste complete JSON]

Claude: [Executes extraction]
```

---

## Quick Commands

**Getting Prompts from Project Knowledge:**
- "Show me the Claims Pass 1 v2.4 prompt from project knowledge"
- "Use the RDMAP Pass 1 v2.4 prompt from project knowledge"

**Starting Extraction:**
- "Using research-assessor skill, extract Claims Pass 1 from this section"
- "Rationalize this extraction using Claims Pass 2 (research-assessor skill)"

**Checking Progress:**
- "Count the items in each array"
- "Show me the first 3 evidence items"
- "Verify cross-references are bidirectional"

---

## Testing Checklist

### Pre-Test Setup

- [ ] Skill installed and recognized by Claude
- [ ] Can access all 5 prompts in project knowledge
- [ ] Have Sobotkova paper ready
- [ ] Have blank template v2.4 ready
- [ ] Selected test section (recommend Methods section, ~3 pages)

---

### Test 1: Claims Pass 1 (Liberal Extraction)

**Input:** Blank template + source section  
**Prompt:** Claims/Evidence Pass 1 v2.4  
**Expected Time:** 10-15 minutes

**Verification Checklist:**
- [ ] Evidence array populated (target: 40-60 items from Results/Discussion section)
- [ ] Claims array populated (target: 30-50 items from Results/Discussion section)
- [ ] Implicit_arguments populated if applicable (target: 5-15 items)
- [ ] RDMAP arrays remain empty (`research_designs: []`, `methods: []`, `protocols: []`)
- [ ] All items have `location` field
- [ ] All items have unique IDs (E001, E002... C001, C002...)
- [ ] Extraction_notes documents any uncertainties
- [ ] Intentional over-extraction present (this is correct!)

**Quality Checks:**
- [ ] Evidence items are observations/measurements (minimal interpretation)
- [ ] Claims are interpretations/generalizations
- [ ] Most claims reference some evidence via `supported_by_evidence`
- [ ] Location tracking points to actual sections

**Save output as:** `test-claims-pass1.json`

---

### Test 2: Claims Pass 2 (Rationalization)

**Input:** Pass 1 JSON + original source section  
**Prompt:** Claims/Evidence Pass 2 v2.4  
**Expected Time:** 10-15 minutes

**Verification Checklist:**
- [ ] Evidence count reduced (target: 15-20% reduction)
- [ ] Claims count reduced (target: 15-20% reduction)
- [ ] RDMAP arrays still empty
- [ ] All consolidated items have `consolidation_metadata` field
- [ ] Consolidation metadata includes: `consolidated_from`, `consolidation_type`, `rationale`
- [ ] Cross-references updated (if E042-E044 consolidated to E042, all references updated)
- [ ] No information loss (verify via consolidation_metadata.information_preserved)

**Quality Checks:**
- [ ] Consolidations make sense (acid test: "assess together or separately?")
- [ ] Boundaries cleaner (evidence/claim distinctions refined)
- [ ] Relationships verified (all claims have evidential support)
- [ ] Verbatim quotes meaningful

**Calculate Reduction:**
- Pass 1 evidence count: ____
- Pass 2 evidence count: ____
- Reduction: ____% (target 15-20%)

**Save output as:** `test-claims-pass2.json`

---

### Test 3: RDMAP Pass 1 (Liberal Extraction)

**Input:** Claims Pass 2 JSON (or blank template) + Methods section  
**Prompt:** RDMAP Pass 1 v2.4  
**Expected Time:** 15-20 minutes

**Verification Checklist:**
- [ ] Research_designs array populated (target: 10-15 items)
- [ ] Methods array populated (target: 20-30 items)
- [ ] Protocols array populated (target: 15-25 items)
- [ ] Claims/evidence arrays unchanged from Pass 2
- [ ] Three-tier hierarchy clear (Design → Method → Protocol)
- [ ] Cross-references to claims/evidence present (if Claims already extracted)
- [ ] Expected_information_missing fields populated

**Quality Checks:**
- [ ] Tier assignments appropriate:
  - Designs: Strategic decisions (research questions, frameworks, scope)
  - Methods: Tactical approaches (data collection, sampling, analysis)
  - Protocols: Operational procedures (specific tools, parameters, steps)
- [ ] Use tier tests: WHY? → Design, WHAT? → Method, HOW? → Protocol
- [ ] Hierarchy relationships present (`implements_designs`, `realized_through_protocols`)
- [ ] Intentional over-extraction (this is correct!)

**Save output as:** `test-rdmap-pass1.json`

---

### Test 4: RDMAP Pass 2 (Rationalization)

**Input:** RDMAP Pass 1 JSON + original Methods section  
**Prompt:** RDMAP Pass 2 v2.4  
**Expected Time:** 10-15 minutes

**Verification Checklist:**
- [ ] Research_designs count reduced (target: 15-20% reduction)
- [ ] Methods count reduced (target: 15-20% reduction)
- [ ] Protocols count reduced (target: 15-20% reduction)
- [ ] Claims/evidence arrays still unchanged
- [ ] Consolidation_metadata on consolidated RDMAP items
- [ ] Cross-references formalized and bidirectional
- [ ] Tier assignments verified/corrected

**Quality Checks:**
- [ ] Hierarchy makes sense (Design → Method → Protocol flow logical)
- [ ] Cross-references bidirectional (if M008 implements RD001, then RD001 enabled by M008)
- [ ] Consolidations appropriate per tier
- [ ] Expected information review complete

**Calculate Reduction:**
- Pass 1 RDMAP total: ____
- Pass 2 RDMAP total: ____
- Reduction: ____% (target 15-20%)

**Save output as:** `test-rdmap-pass2.json`

---

### Test 5: Validation Pass 3

**Input:** Complete extraction (Claims + RDMAP after both Pass 2s)  
**Prompt:** Validation Pass 3 v2.4  
**Expected Time:** 5-10 minutes

**Verification Checklist:**
- [ ] Validation report produced (separate JSON, not modifying extraction)
- [ ] Overall status reported (PASS/PASS_WITH_ISSUES/FAIL)
- [ ] Cross-reference integrity checked
- [ ] Bidirectional consistency verified
- [ ] Hierarchy validation performed
- [ ] Schema compliance checked
- [ ] Issues categorized by severity (CRITICAL/IMPORTANT/MINOR)

**Review Issues:**
- [ ] No CRITICAL issues (blocking)
- [ ] IMPORTANT issues noted and acceptable
- [ ] MINOR issues documented

**Quality Checks:**
- [ ] Cross-reference orphans = 0 (all referenced IDs exist)
- [ ] Bidirectional pairs complete
- [ ] Tier hierarchy logical
- [ ] Expected information gaps reasonable

**Save output as:** `test-validation-report.json`

---

## Success Criteria

### Extraction Quality

**Pass 1 (Both):**
- ✅ Comprehensive capture (over-extraction expected)
- ✅ All items have location tracking
- ✅ IDs unique and sequential
- ✅ Array boundaries respected

**Pass 2 (Both):**
- ✅ 15-20% reduction achieved
- ✅ Consolidation metadata present
- ✅ Information preserved
- ✅ Cross-references updated

**Pass 3:**
- ✅ No CRITICAL issues
- ✅ Validation report clear
- ✅ Issues documented

### Overall System

**Completeness:**
- [ ] All six object types extracted
- [ ] ~100-150 total items
- [ ] ~200+ cross-references

**Quality:**
- [ ] Boundaries clear (evidence vs claims, Design vs Method vs Protocol)
- [ ] Relationships logical
- [ ] Traceability complete
- [ ] Expected information tracked

---

## Common Issues & Quick Fixes

### Issue: Claude doesn't follow prompt
**Symptom:** Extraction deviates from instructions  
**Fix:** 
- ✓ Verify you pasted the COMPLETE prompt (full 800-1000 lines)
- ✓ Mention "using research-assessor skill"
- ✓ Provide all required inputs (template, source text)

### Issue: Array boundaries violated
**Symptom:** RDMAP Pass modifies claims/evidence  
**Fix:**
- ✓ Check you used correct prompt version (v2.4)
- ✓ Verify input JSON structure
- ✓ Re-run with explicit boundary reminder

### Issue: Reduction too high/low
**Symptom:** Pass 2 reduces by <10% or >30%  
**Fix:**
- ✓ If <10%: May need more aggressive consolidation (acceptable, document)
- ✓ If >30%: Check for over-consolidation, information loss
- ✓ Review consolidation_metadata for rationale

### Issue: Cross-references broken
**Symptom:** Validation reports orphans  
**Fix:**
- ✓ Check if IDs were renumbered without updating references
- ✓ Verify Pass 2 updated references when consolidating
- ✓ Run validation to identify all broken links

### Issue: Uncertain during extraction
**Symptom:** Many items marked extraction_confidence: low  
**Fix:**
- ✓ Check if right section (Methods best for RDMAP)
- ✓ This may be appropriate if text is vague
- ✓ Skill will consult references (tier-assignment-guide, consolidation-patterns)
- ✓ Flag for manual review later

---

## Reference Materials

**In Skill Package (Claude can read):**
- `references/schema/schema-guide.md` - Complete object definitions
- `references/checklists/tier-assignment-guide.md` - Design/Method/Protocol tests
- `references/checklists/consolidation-patterns.md` - Lumping vs splitting
- `references/checklists/expected-information.md` - Completeness checklists
- `references/examples/sobotkova-example.md` - Worked extraction

**In Repository:**
- USAGE_GUIDE.md - Detailed instructions
- ARCHITECTURE.md - Design rationale
- TESTING.md - Testing procedures
- TROUBLESHOOTING section in USAGE_GUIDE.md

---

## Post-Test Review

### Questions to Answer

**Quality:**
- [ ] Did extraction capture key methodology elements?
- [ ] Are boundaries (evidence/claims, Design/Method/Protocol) clear?
- [ ] Is consolidation appropriate (not losing information)?
- [ ] Are cross-references meaningful?

**Process:**
- [ ] Was workflow clear?
- [ ] Were prompts effective?
- [ ] Did skill references help when needed?
- [ ] What would improve the process?

**Time:**
- [ ] How long did each pass take?
- [ ] Within expected range (30-40 min per section)?
- [ ] Where were the slowdowns?

**Issues:**
- [ ] What errors occurred?
- [ ] Were they systematic or one-off?
- [ ] Could prompts be improved?
- [ ] Should skill references be enhanced?

### Document Findings

**Keep notes on:**
- Quality issues found
- Prompt improvements needed
- Reference material gaps
- Time actuals vs estimates
- Surprises (good or bad)

**This will inform:**
- Prompt refinement
- Skill enhancements
- Documentation improvements
- Domain adaptation needs

---

## Next Steps After Testing

**If Successful:**
1. ✅ Document test results
2. ✅ Note any prompt refinements needed
3. ✅ Plan additional paper tests
4. ✅ Consider domain adaptations
5. ⏭️ Scale to production

**If Issues Found:**
1. ✅ Document specific problems
2. ✅ Identify root causes
3. ✅ Refine prompts or skill references
4. ✅ Re-test with improvements
5. ✅ Iterate until quality acceptable

---

**Good luck with testing! 🚀**

**Remember:**
- Over-extraction in Pass 1 is EXPECTED
- Consolidation in Pass 2 is the refinement
- Validation in Pass 3 catches structural issues
- The skill provides frameworks, YOU provide prompts
- Iteration is part of the process

**Questions during testing?**
- Check skill references (Claude can read them)
- Consult USAGE_GUIDE.md
- Review worked example (sobotkova-example.md)
