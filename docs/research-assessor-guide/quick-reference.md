# Research Assessor v2.6 - Quick Reference

**Essential commands and workflows at a glance**

---

## Complete Workflow

```
📄 Blank Template (schema v2.6)
         ↓
📋 Pass 0 → Metadata extraction (paper-level information)
         ↓
📝 Pass 1 → Claims/Evidence liberal (over-capture expected)
         ↓
🔍 Pass 2 → Claims/Evidence rationalisation (15-20% consolidation)
         ↓
📝 Pass 3 → RDMAP explicit extraction (visible methodology)
         ↓
📝 Pass 4 → RDMAP implicit scanning (implied decisions)
         ↓
🔍 Pass 5 → RDMAP rationalisation (15-20% consolidation)
         ↓
🏗️ Pass 6 → Infrastructure assessment (PIDs, FAIR, reproducibility)
         ↓
✅ Pass 7 → Validation (integrity checks, bidirectional verification)
         ↓
🎯 Complete Extraction
```

**Key Principle:** Single JSON document flows through all passes. Each pass modifies only its designated sections.

---

## Pass Responsibilities

| Pass | Modifies | Leaves Alone | Expected Output |
|------|----------|--------------|-----------------|
| Pass 0 | Metadata only | All arrays | Paper title, authors, publication info |
| Pass 1 | evidence, claims, implicit_arguments | RDMAP, infrastructure | 40-60 evidence, 25-40 claims, 10-20 arguments |
| Pass 2 | evidence, claims, implicit_arguments | RDMAP, infrastructure | 15-20% consolidation |
| Pass 3 | research_designs, methods, protocols | Claims/evidence, infrastructure | Explicit methodology extraction |
| Pass 4 | research_designs, methods, protocols | Claims/evidence, infrastructure | Implicit decisions added |
| Pass 5 | research_designs, methods, protocols | Claims/evidence, infrastructure | 15-20% consolidation |
| Pass 6 | infrastructure object | All other sections | PIDs, FAIR scores, permits, funding |
| Pass 7 | Nothing (reads only) | All sections | Validation report (separate file) |

---

## Quick Commands

### Starting Extraction

```
"Using research-assessor skill, extract Pass 0 metadata from this paper"
"Extract Claims Pass 1 from this section using research-assessor skill"
"Rationalise this extraction using Pass 2 (research-assessor skill)"
"Extract explicit RDMAP (Pass 3) from Methods section"
"Scan for implicit RDMAP (Pass 4) across all sections"
```

### Checking Progress

```
"Count items in each array"
"Show me the first 3 evidence items"
"Verify cross-references are bidirectional"
"Check FAIR compliance score breakdown"
"Show PID connectivity score"
```

### Validation

```
"Run Pass 7 validation on this complete extraction"
"Check for orphaned cross-references"
"Verify bidirectional relationship consistency"
```

---

## Conversation Template

**For Each Pass:**

```
You: I'm using the research-assessor skill for [Pass Name].

Here's the [Pass Name] prompt:
[paste entire prompt from extraction-system/prompts/]

[For Pass 0:]
Extract metadata from this paper:
[paste front matter: title, authors, abstract, publication details]

[For Pass 1, 3, 4:]
Extract from this section:
[paste source text from outputs/{paper-slug}/{paper-slug}.txt]

Use this JSON:
[paste current extraction.json state]

[For Pass 2, 5:]
Here's the source text for verification:
[paste original section]

Here's the Pass [1/3-4] extraction to rationalise:
[paste current JSON]

[For Pass 6:]
Extract infrastructure from complete paper:
[paste full paper text or key sections]

Current extraction state:
[paste current JSON]

[For Pass 7:]
Validate this complete extraction:
[paste complete JSON]

Claude: [Executes extraction]
```

---

## Pass Details

### Pass 0: Metadata Extraction

**Input:** Paper front matter (title, authors, abstract, publication details)
**Output:** Populated metadata section
**Time:** 5-10 minutes

**Key Fields:**
- Title, authors, publication year, journal/venue
- DOI, paper type (empirical/methodological/review)
- Abstract, keywords
- Research domain/discipline

---

### Pass 1: Claims/Evidence Liberal

**Input:** Results, Discussion, or Methods sections
**Output:** Over-captured evidence, claims, implicit arguments
**Time:** 10-15 minutes per section

**Quality Checks:**
- Evidence items are observations/measurements
- Claims are interpretations/generalisations
- Implicit arguments capture unstated assumptions
- All items have location tracking
- Intentional over-extraction (40-50% expected)

---

### Pass 2: Claims/Evidence Rationalisation

**Input:** Pass 1 output + original source text
**Output:** Consolidated evidence/claims with metadata
**Time:** 10-15 minutes

**Quality Checks:**
- 15-20% reduction achieved
- Consolidation_metadata documents all merges
- Information preserved (no loss of meaning)
- Cross-references updated
- Boundaries refined (evidence vs claims clearer)

---

### Pass 3: RDMAP Explicit Extraction

**Input:** Methods section (explicit methodology statements)
**Output:** Research designs, methods, protocols
**Time:** 15-20 minutes

**Quality Checks:**
- Tier assignments appropriate:
  - Designs: Strategic WHY decisions
  - Methods: Tactical WHAT approaches
  - Protocols: Operational HOW procedures
- Hierarchy relationships captured
- Expected_information tracked
- Cross-references to claims/evidence

---

### Pass 4: RDMAP Implicit Scanning

**Input:** All sections (scan for unstated decisions)
**Output:** Additional RDMAP items (implicit methodology)
**Time:** 10-15 minutes

**Quality Checks:**
- Implicit decisions identified (unstated but evident)
- Integration with explicit RDMAP
- Cross-references established
- Extraction confidence tracked

---

### Pass 5: RDMAP Rationalisation

**Input:** Pass 3-4 combined output + source text
**Output:** Consolidated RDMAP with verified relationships
**Time:** 15-20 minutes

**Quality Checks:**
- 15-20% consolidation achieved
- Tier assignments verified/corrected
- Hierarchy coherent (Design → Method → Protocol)
- Cross-references bidirectional
- Expected information reviewed

---

### Pass 6: Infrastructure Assessment

**Input:** Complete paper (data availability statements, funding, permits)
**Output:** Infrastructure object with PIDs, FAIR scores, reproducibility
**Time:** 20-30 minutes

**Components Assessed:**
- **PIDs:** Data DOIs, ORCIDs, software identifiers (0-6 connectivity score)
- **FAIR:** 15-principle assessment (0-15 compliance score)
- **Code Availability:** GitHub, Zenodo, Software Heritage
- **Computational Reproducibility:** 0-4 spectrum (none → fully reproducible)
- **Permits:** IRB, fieldwork permits, CARE principles
- **Funding:** Grant numbers, acknowledgements

**Quality Checks:**
- PID connectivity accurately scored
- FAIR assessment uses examples
- Missing statements vs negative assessments distinguished
- Historical context considered (pre-2016 baseline)

---

### Pass 7: Validation

**Input:** Complete extraction (all passes 0-6)
**Output:** Validation report (separate file)
**Time:** 5-10 minutes

**Validation Checks:**
- Cross-reference integrity (no orphans)
- Bidirectional consistency
- Hierarchy validation (Design → Method → Protocol coherent)
- Schema compliance
- Expected information completeness
- Relationship mapping coverage

**Issue Severity:**
- CRITICAL: Blocking issues (orphaned references, schema violations)
- IMPORTANT: Quality issues (missing relationships, incomplete metadata)
- MINOR: Documentation suggestions (additional context helpful)

---

## Expected Item Counts

Based on diverse corpus testing (2016-2024):

**Claims/Evidence (Passes 1-2):**
- Evidence: 40-60 items (varies by paper length/complexity)
- Claims: 25-40 items
- Implicit Arguments: 10-20 items

**RDMAP (Passes 3-5):**
- Research Designs: 4-8 items (strategic decisions)
- Methods: 15-25 items (tactical approaches)
- Protocols: 8-15 items (operational procedures)

**Infrastructure (Pass 6):**
- PID Connectivity: 0-6 score (0 = pre-FAIR baseline, 6 = exemplary)
- FAIR Compliance: 0-15 score (0 = minimal, 15 = fully compliant)
- Computational Reproducibility: 0-4 levels

**Total Extraction:**
- 100-180 objects per paper
- 200-400 cross-references
- 80%+ relationship mapping coverage

---

## Success Criteria

### Liberal Passes (1, 3, 4)

✅ Comprehensive capture (over-extraction expected)
✅ All items have location tracking
✅ IDs unique and sequential
✅ Array boundaries respected
✅ Uncertainties flagged

### Rationalisation Passes (2, 5)

✅ 15-20% reduction achieved
✅ Consolidation metadata present
✅ Information preserved (no loss)
✅ Cross-references updated
✅ Boundaries refined

### Infrastructure Pass (6)

✅ PID connectivity scored accurately
✅ FAIR assessment with examples
✅ Missing vs negative statements distinguished
✅ Historical context considered
✅ Permit/ethics documentation captured

### Validation Pass (7)

✅ No CRITICAL issues
✅ Validation report clear
✅ Issues categorised by severity
✅ Recommendations actionable

---

## Common Issues & Quick Fixes

### Issue: Extraction stops between passes

**Symptom:** Asks "Should I continue to next pass?"
**Fix:**
✓ Check CLAUDE.md - autonomous mode enabled
✓ Workflow continues automatically
✓ Don't ask permission between passes

### Issue: Item counts too low

**Symptom:** Pass 1 produces <30 items total
**Fix:**
✓ Check section selection (Methods best for RDMAP)
✓ Verify liberal extraction mindset ("when uncertain → extract")
✓ Review extraction_notes for suppressed items

### Issue: Consolidation too aggressive

**Symptom:** Pass 2/5 reduces by >30%
**Fix:**
✓ Check consolidation_metadata rationale
✓ Verify information_preserved field
✓ Review for over-consolidation

### Issue: Cross-references broken

**Symptom:** Pass 7 validation reports orphans
**Fix:**
✓ Check if IDs renumbered without updating references
✓ Verify Pass 2/5 updated all references
✓ Use validation output to identify broken links

### Issue: FAIR scoring unclear

**Symptom:** Uncertain about GitHub-only vs Zenodo scoring
**Fix:**
✓ Check infrastructure/fair-principles-guide.md
✓ GitHub-only: Scores A1 (basic access) but NOT A2 (preservation)
✓ Zenodo/archive: Scores both A1 and A2

### Issue: PID connectivity calculation

**Symptom:** Uncertain which PIDs count
**Fix:**
✓ Check infrastructure/pid-systems-guide.md
✓ 6 components: Paper DOI, data DOI, code DOI, author ORCID, funder ID, vocab PID
✓ Each component: 0 (none) or 1 (present) → sum to 0-6

---

## Reference Materials

### In Skill Package (.claude/skills/research-assessor/references/)

**Schema:**
- `schema/schema-guide.md` - Complete object definitions

**Checklists:**
- `checklists/evidence-vs-claims-guide.md` - Boundary decision framework
- `checklists/expected-information.md` - Completeness checklists
- `checklists/tier-assignment-guide.md` - Design/Method/Protocol tests

**Consolidation:**
- `consolidation/consolidation-patterns.md` - Lumping vs splitting guidance

**RDMAP:**
- `rdmap/research-design-patterns.md` - Design pattern library

**Infrastructure:**
- `infrastructure/pid-systems-guide.md` - PID types and scoring
- `infrastructure/fair-principles-guide.md` - 15-principle assessment
- `infrastructure/fieldwork-permits-guide.md` - Permits, ethics, CARE
- `infrastructure/credit-taxonomy.md` - Contributor roles

### In Repository

**Extraction System:**
- `extraction-system/prompts/` - All 8 pass prompts
- `extraction-system/schema/` - JSON schema files

**Documentation:**
- `docs/research-assessor-guide/` - This guide
- `docs/user-guide/` - User documentation
- `input/WORKFLOW.md` - Complete extraction workflow

**Testing:**
- `planning/pass6-phase1-testing-findings.md` - Infrastructure testing results

---

## Prompt Locations

All prompts in `extraction-system/prompts/`:

- `00-metadata_pass0_prompt.md` - Metadata extraction
- `01-claims-evidence_pass1_prompt.md` - Liberal C&E extraction
- `02-claims-evidence_pass2_prompt.md` - C&E rationalisation
- `03-rdmap_pass1a_explicit_prompt.md` - Explicit RDMAP
- `04-rdmap_pass1b_implicit_prompt.md` - Implicit RDMAP
- `05-rdmap_pass2_consolidation_prompt.md` - RDMAP rationalisation
- `06-infrastructure_pass6_prompt.md` - Infrastructure assessment
- `07-validation_pass3_prompt.md` - Final validation

---

## Testing Checklist

### Pre-Test Setup

- [ ] Skill installed (.claude/skills/research-assessor/)
- [ ] Can access all 8 prompts (extraction-system/prompts/)
- [ ] Have paper text extracted (outputs/{paper-slug}/{paper-slug}.txt)
- [ ] Have blank template (extraction.json schema v2.6)

### During Testing

- [ ] Pass 0 completes (metadata populated)
- [ ] Pass 1 completes (C&E liberal extraction)
- [ ] Pass 2 completes (15-20% C&E consolidation)
- [ ] Pass 3 completes (explicit RDMAP)
- [ ] Pass 4 completes (implicit RDMAP addition)
- [ ] Pass 5 completes (15-20% RDMAP consolidation)
- [ ] Pass 6 completes (infrastructure assessment)
- [ ] Pass 7 completes (no CRITICAL issues)

### Post-Test Validation

- [ ] Item counts in expected ranges
- [ ] Cross-references bidirectional
- [ ] Consolidation metadata present
- [ ] FAIR/PID scores justified with examples
- [ ] Validation report clear
- [ ] Total time reasonable (2-3 hours for complete paper)

---

## File Organisation

```
outputs/{paper-slug}/
├── extraction.json              # Primary extraction (all passes accumulate here)
├── {paper-slug}.txt            # Extracted plain text from PDF
└── validation-report.json      # Pass 7 output (optional separate file)
```

**Key Files:**
- `extraction.json` - Single accumulating document (Passes 0-6 modify)
- `validation-report.json` - Separate output from Pass 7 (read-only validation)

---

## Version Information

**Current Version:** 2.6
**Schema Version:** 2.6
**Compatible Prompts:** Pass 0-7 (v2.6)
**Last Updated:** 2025-11-13

**Breaking Changes from v2.4:**
- Added Pass 0 (metadata extraction)
- Split RDMAP into 3 passes (explicit, implicit, rationalisation)
- Added Pass 6 (infrastructure assessment)
- Infrastructure object with PIDs, FAIR, reproducibility
- Updated to 7-pass workflow (was 5-pass in v2.4)

---

## Tips for Success

**Liberal Extraction (Passes 1, 3, 4):**
- When uncertain → extract (err on side of over-capture)
- Preserve granularity (split rather than lump)
- Document uncertainties in extraction_notes
- Expected: 40-50% over-extraction vs final

**Rationalisation (Passes 2, 5):**
- Consolidate only when assessment impact identical
- Document ALL consolidations in metadata
- Update ALL cross-references
- Verify information preservation

**Infrastructure Assessment (Pass 6):**
- Distinguish missing statements from negative assessments
- Use examples to justify FAIR scores
- Consider historical context (pre-2016 baseline)
- Check supplementary materials for hidden PIDs

**Validation (Pass 7):**
- Address CRITICAL issues immediately
- Document IMPORTANT issues for review
- Use validation output to guide refinements

---

**Remember:**

✓ Over-extraction in liberal passes is EXPECTED
✓ Consolidation in rationalisation passes is the refinement
✓ Infrastructure assessment requires full paper context
✓ Validation catches structural issues
✓ The skill provides frameworks, YOU provide prompts
✓ Iteration and refinement are part of the process
