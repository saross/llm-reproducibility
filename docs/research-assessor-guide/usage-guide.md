# Usage Guide

**Version:** 2.6
**Last Updated:** 2025-11-13

Complete guide to using the Research Assessor skill for extracting research methodology, claims, evidence, and reproducibility infrastructure from academic papers.

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Complete Workflow](#complete-workflow)
4. [Pass-by-Pass Instructions](#pass-by-pass-instructions)
5. [Working with JSON](#working-with-json)
6. [Common Patterns](#common-patterns)
7. [Troubleshooting](#troubleshooting)
8. [Best Practices](#best-practices)

---

## Prerequisites

### Required

- **Claude AI access** with Skills support
- **Claude Sonnet 4.5** or later (recommended for best results)
- **Research paper** (PDF converted to text)
- **Extraction prompts** (8 prompts, ~6,000 lines total)
- **Blank JSON template** (schema v2.6)

### Recommended Skills

- Basic understanding of research methodology
- Familiarity with JSON format
- Domain expertise in the research field (helpful but not required)
- Understanding of FAIR principles and PIDs (for infrastructure assessment)

---

## Installation

### Step 1: Verify Skill Installation

The skill is located in `.claude/skills/research-assessor/` within the project repository.

**Verify installation:**
```bash
ls -la .claude/skills/research-assessor/
```

You should see:
- `SKILL.md` - Core skill definition
- `references/` - Decision frameworks and guides

### Step 2: Get the Extraction Prompts

The eight extraction prompts are in `extraction-system/prompts/`:

1. `00-metadata_pass0_prompt.md` (~400 lines)
2. `01-claims-evidence_pass1_prompt.md` (~800 lines)
3. `02-claims-evidence_pass2_prompt.md` (~900 lines)
4. `03-rdmap_pass1a_explicit_prompt.md` (~1,000 lines)
5. `04-rdmap_pass1b_implicit_prompt.md` (~800 lines)
6. `05-rdmap_pass2_consolidation_prompt.md` (~900 lines)
7. `06-infrastructure_pass6_prompt.md` (~1,200 lines)
8. `07-validation_pass3_prompt.md` (~600 lines)

### Step 3: Prepare Your Materials

**Extract PDF to text:**
Follow guidance in `input/WORKFLOW.md` for PDF extraction using `pdftotext`.

**Create working directory:**
```bash
mkdir -p outputs/{paper-slug}/
```

**Copy blank template:**
```bash
cp extraction-system/schema/blank-template-v2.6.json outputs/{paper-slug}/extraction.json
```

---

## Complete Workflow

### Overview

```
Research Paper PDF
       ↓
[Convert to text using pdftotext]
       ↓
outputs/{paper-slug}/{paper-slug}.txt
       ↓
┌──────────────────────┐
│  Pass 0: Metadata    │  ← Paper front matter
│  Extraction          │  → Paper-level info populated
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│  Pass 1: Claims      │  ← Results/Discussion sections
│  Liberal Extraction  │  → Evidence, claims, arguments
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│  Pass 2: Claims      │  ← Consolidation pass
│  Rationalisation     │  → Refined C&E (15-20% reduction)
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│  Pass 3: RDMAP       │  ← Methods section
│  Explicit Extraction │  → Visible methodology
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│  Pass 4: RDMAP       │  ← All sections scan
│  Implicit Scanning   │  → Implied decisions added
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│  Pass 5: RDMAP       │  ← Consolidation pass
│  Rationalisation     │  → Refined RDMAP (15-20% reduction)
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│  Pass 6:             │  ← Full paper context
│  Infrastructure      │  → PIDs, FAIR, reproducibility
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│  Pass 7: Validation  │  ← Complete extraction
│  Integrity Checks    │  → Validation report
└──────────────────────┘
```

### Time Estimates

**Per paper section (~5-10 pages):**
- Pass 0 Metadata: 5-10 minutes
- Pass 1 Claims: 10-15 minutes
- Pass 2 Claims: 10-15 minutes
- Pass 3 RDMAP Explicit: 15-20 minutes
- Pass 4 RDMAP Implicit: 10-15 minutes
- Pass 5 RDMAP Rationalisation: 15-20 minutes
- Pass 6 Infrastructure: 20-30 minutes
- Pass 7 Validation: 5-10 minutes
- **Total: 90-135 minutes per section**

**Full paper (30-50 pages):**
- Extract by section: 2-3 hours
- Infrastructure assessment: 30 minutes
- Review and refine: 30-60 minutes
- **Total: 3-4.5 hours**

---

## Pass-by-Pass Instructions

### Pass 0: Metadata Extraction

**Goal:** Extract paper-level metadata and publication information.

**Inputs:**
1. Metadata Pass 0 prompt
2. Paper front matter (title, authors, abstract, publication details)
3. Blank JSON template

**Conversation Template:**
```
You: I'm using the research-assessor skill for metadata extraction.

Here's the Pass 0 prompt:
[paste entire 00-metadata_pass0_prompt.md]

Extract metadata from this paper:
[paste title, authors, abstract, publication details, DOI]

Use this JSON:
[paste blank template]

Claude: [Extracts metadata into paper_metadata section]
```

**What to Expect:**
- Paper title, authors, publication year
- Journal/venue, DOI
- Paper type (empirical/methodological/review)
- Abstract, keywords
- Research domain/discipline

**Verification:**
- Title matches paper
- DOI correct and resolvable
- Publication year accurate
- Paper type appropriate

---

### Pass 1: Claims/Evidence Liberal Extraction

**Goal:** Comprehensive capture of evidence, claims, and implicit arguments.

**Inputs:**
1. Claims/Evidence Pass 1 prompt
2. Source section text (Results, Discussion, or Findings sections)
3. JSON document with metadata populated

**Conversation Template:**
```
You: Extracting claims and evidence using research-assessor skill.

Here's the Pass 1 prompt:
[paste entire 01-claims-evidence_pass1_prompt.md]

Extract from this section:
[paste source text from outputs/{paper-slug}/{paper-slug}.txt]

Use this JSON document:
[paste extraction.json with Pass 0 complete]

Claude: [Extracts evidence, claims, implicit_arguments]
```

**What to Expect:**
- 40-60 evidence items (observations, measurements, data points)
- 25-40 claims (interpretations, generalisations)
- 10-20 implicit arguments (unstated assumptions)
- Intentional over-extraction (40-50% above final expected)
- Some borderline cases included

**Verification:**
- Evidence items are minimally interpreted observations
- Claims are interpretations/generalisations
- Most claims reference evidence via `supported_by_evidence`
- All items have `location` field
- IDs unique and sequential (E001, E002..., C001, C002...)
- Extraction_notes documents any uncertainties

---

### Pass 2: Claims/Evidence Rationalisation

**Goal:** Consolidate, refine boundaries, and verify relationships.

**Inputs:**
1. Claims/Evidence Pass 2 prompt
2. Original source section text (for verification)
3. Pass 1 JSON output

**Conversation Template:**
```
You: Rationalising claims and evidence using research-assessor skill.

Here's the Pass 2 prompt:
[paste entire 02-claims-evidence_pass2_prompt.md]

Here's the source text for reference:
[paste original section]

Here's the Pass 1 extraction to rationalise:
[paste extraction.json with Pass 1 complete]

Claude: [Consolidates and refines C&E]
```

**What to Expect:**
- 15-20% reduction in item count
- Better-defined evidence/claim boundaries
- Consolidation_metadata added to merged items
- Improved cross-reference accuracy
- Preserved information (documented in metadata)

**Verification:**
- Check `consolidation_metadata` present on consolidated items
- Verify consolidated items make sense (acid test: "assess together or separately?")
- Confirm no information loss via `information_preserved` field
- Review boundary corrections (evidence vs claims clearer)
- Cross-references updated (if E042-E044 consolidated to E042, all references updated)

---

### Pass 3: RDMAP Explicit Extraction

**Goal:** Comprehensive capture of explicitly stated methodology.

**Inputs:**
1. RDMAP Pass 1a (Explicit) prompt
2. Methods section text
3. JSON document (with claims/evidence from Pass 2)

**Conversation Template:**
```
You: Extracting explicit RDMAP using research-assessor skill.

Here's the RDMAP Pass 3 prompt:
[paste entire 03-rdmap_pass1a_explicit_prompt.md]

Extract from this Methods section:
[paste Methods section from outputs/{paper-slug}/{paper-slug}.txt]

Use this JSON:
[paste extraction.json with Pass 2 complete]

Claude: [Extracts research_designs, methods, protocols from explicit statements]
```

**What to Expect:**
- 4-8 research designs (strategic WHY decisions)
- 15-25 methods (tactical WHAT approaches)
- 8-15 protocols (operational HOW procedures)
- Three-tier hierarchy clear
- Cross-references to claims/evidence (if present)
- Expected_information gaps flagged

**Verification:**
- Tier assignments appropriate:
  - Designs: Strategic decisions (research questions, frameworks, scope)
  - Methods: Tactical approaches (data collection, sampling, analysis)
  - Protocols: Operational procedures (specific tools, parameters, steps)
- Use tier tests: WHY? → Design, WHAT? → Method, HOW? → Protocol
- Hierarchy relationships present (`implements_designs`, `realized_through_protocols`)
- Cross-references point to valid IDs
- Intentional over-extraction for implicit pass

---

### Pass 4: RDMAP Implicit Scanning

**Goal:** Identify unstated methodological decisions evident from context.

**Inputs:**
1. RDMAP Pass 1b (Implicit) prompt
2. All sections (scan for implied decisions)
3. JSON document (with Pass 3 explicit RDMAP)

**Conversation Template:**
```
You: Scanning for implicit RDMAP using research-assessor skill.

Here's the RDMAP Pass 4 prompt:
[paste entire 04-rdmap_pass1b_implicit_prompt.md]

Scan these sections for implied decisions:
[paste relevant sections: Methods, Results, Discussion]

Current extraction state:
[paste extraction.json with Pass 3 complete]

Claude: [Adds implicit research_designs, methods, protocols]
```

**What to Expect:**
- Additional RDMAP items (unstated but evident)
- Integration with explicit RDMAP
- Cross-references established
- Extraction_confidence tracked (often "medium" or "low")

**Verification:**
- Implicit decisions genuinely implied (not speculative)
- Integration with explicit RDMAP coherent
- Cross-references to evidence/claims support inference
- Extraction_notes documents reasoning

---

### Pass 5: RDMAP Rationalisation

**Goal:** Consolidate RDMAP, verify hierarchy, formalise relationships.

**Inputs:**
1. RDMAP Pass 2 (Consolidation) prompt
2. Original Methods section text
3. Pass 3-4 combined JSON

**Conversation Template:**
```
You: Rationalising RDMAP using research-assessor skill.

Here's the RDMAP Pass 5 prompt:
[paste entire 05-rdmap_pass2_consolidation_prompt.md]

Here's the Methods section for reference:
[paste original Methods section]

Here's the Pass 3-4 extraction:
[paste extraction.json with Pass 4 complete]

Claude: [Consolidates and refines RDMAP]
```

**What to Expect:**
- 15-20% reduction in RDMAP item count
- Tier corrections if needed
- Consolidated procedures (maintaining granularity)
- Formalised and bidirectional cross-references

**Verification:**
- Hierarchy makes sense (Design → Method → Protocol flow logical)
- Cross-references bidirectional (if M008 implements RD001, then RD001 has M008 in `implemented_by_methods`)
- Consolidation_metadata present
- Tier assignments verified/corrected
- Expected_information reviewed and updated

---

### Pass 6: Infrastructure Assessment

**Goal:** Extract reproducibility infrastructure, PIDs, FAIR compliance, ethics/permits.

**Inputs:**
1. Infrastructure Pass 6 prompt
2. Full paper context (data availability statements, acknowledgements, ethics sections)
3. JSON document (with Passes 0-5 complete)

**Conversation Template:**
```
You: Assessing reproducibility infrastructure using research-assessor skill.

Here's the Pass 6 prompt:
[paste entire 06-infrastructure_pass6_prompt.md]

Extract infrastructure from this paper:
[paste full paper or key sections: data availability, acknowledgements, ethics, funding, supplementary materials]

Current extraction state:
[paste extraction.json with Pass 5 complete]

Claude: [Populates infrastructure object with PIDs, FAIR, permits, funding]
```

**What to Expect:**
- **PID Connectivity Score:** 0-6 (paper DOI, data DOI, code DOI, author ORCID, funder ID, vocab PID)
- **FAIR Compliance Score:** 0-15 (15-principle assessment)
- **Computational Reproducibility:** 0-4 levels (none → code_only → code_dependencies → containerised → fully_reproducible)
- **Permits/Ethics:** IRB numbers, fieldwork permits, CARE principles assessment
- **Funding:** Grant acknowledgements, facility access

**Verification:**
- PID connectivity accurately scored with examples
- FAIR assessment uses specific statements from paper
- Missing statements distinguished from negative assessments
- Historical context considered (pre-2016 baseline)
- GitHub-only vs archived code scored appropriately
- CARE principles assessed where relevant (Indigenous data, heritage sites)

---

### Pass 7: Validation

**Goal:** Verify structural integrity, cross-reference consistency, relationship coverage.

**Inputs:**
1. Validation Pass 7 prompt
2. Complete extraction JSON (after all Passes 0-6)

**Conversation Template:**
```
You: Validating complete extraction using research-assessor skill.

Here's the Validation Pass 7 prompt:
[paste entire 07-validation_pass3_prompt.md]

Here's the complete extraction to validate:
[paste extraction.json with Pass 6 complete]

Claude: [Produces validation report]
```

**What to Expect:**
- Validation report (can be separate file or embedded in extraction_notes)
- Overall status: PASS / PASS_WITH_ISSUES / FAIL
- Cross-reference integrity checks
- Bidirectional consistency verification
- Hierarchy validation (Design → Method → Protocol)
- Schema compliance verification
- Issues categorised by severity (CRITICAL / IMPORTANT / MINOR)

**Verification:**
- No CRITICAL issues (orphaned cross-references, schema violations)
- IMPORTANT issues noted and acceptable (missing relationships, incomplete metadata)
- MINOR issues documented (additional context helpful)
- Relationship mapping coverage >80%

---

## Working with JSON

### Managing Large JSONs

**Problem:** Complete extractions can be 100-180 objects, difficult to read.

**Solutions:**

**1. Use JSON viewer:**
```bash
# Pretty print with jq
cat extraction.json | jq '.' > extraction-pretty.json

# View specific arrays
cat extraction.json | jq '.evidence[]'

# Count items
jq '.evidence | length' extraction.json
jq '.claims | length' extraction.json

# Check FAIR score
jq '.infrastructure.fair_assessment.overall_score' extraction.json
```

**2. Extract by section:**
- Process one section at a time (recommended for large papers)
- Single JSON accumulates across sections
- Easier to manage context windows

**3. Use extraction_notes:**
```json
"extraction_notes": {
  "current_pass": 5,
  "section_extracted": "Methods (Pass 3-5), Results (Pass 1-2)",
  "item_counts": {
    "evidence": 48,
    "claims": 32,
    "implicit_arguments": 15,
    "research_designs": 6,
    "methods": 22,
    "protocols": 14
  }
}
```

### Backing Up Work

**Best Practice:** Save after each pass.

```
outputs/{paper-slug}/
├── extraction.json                        # Current state (accumulating)
├── backups/
│   ├── extraction-pass0-metadata.json
│   ├── extraction-pass1-claims.json
│   ├── extraction-pass2-claims.json
│   ├── extraction-pass3-rdmap-explicit.json
│   ├── extraction-pass4-rdmap-implicit.json
│   ├── extraction-pass5-rdmap-consolidated.json
│   └── extraction-pass6-infrastructure.json
├── {paper-slug}.txt                       # Extracted plain text
└── validation-report.json                 # Pass 7 output (optional separate file)
```

### Item Count Verification

**After each pass, verify counts:**
```bash
cd outputs/{paper-slug}/

# Count all arrays
jq '{
  evidence: (.evidence|length),
  claims: (.claims|length),
  implicit_arguments: (.implicit_arguments|length),
  research_designs: (.research_designs|length),
  methods: (.methods|length),
  protocols: (.protocols|length)
}' extraction.json
```

**Expected progression:**
- Pass 0: Metadata populated, all arrays empty
- Pass 1: Evidence/claims/arguments populated, RDMAP empty
- Pass 2: 15-20% C&E reduction, RDMAP still empty
- Pass 3: RDMAP explicit added (maintains C&E from Pass 2)
- Pass 4: RDMAP implicit added (no C&E changes)
- Pass 5: 15-20% RDMAP reduction (no C&E changes)
- Pass 6: Infrastructure populated (no other changes)
- Pass 7: No changes (validation only)

---

## Common Patterns

### Pattern 1: Full Paper Extraction

**Use case:** Complete extraction from empirical paper.

**Steps:**
1. Pass 0: Extract metadata from front matter
2. Pass 1-2: Extract claims/evidence from Results and Discussion
3. Pass 3: Extract explicit RDMAP from Methods
4. Pass 4: Scan all sections for implicit RDMAP
5. Pass 5: Consolidate RDMAP
6. Pass 6: Assess infrastructure from full paper
7. Pass 7: Validate complete extraction

**Time:** ~3-4 hours

**Output:** Complete extraction.json with 100-180 objects, infrastructure assessment, validation report

---

### Pattern 2: Methods-Only Extraction

**Use case:** Focus on methodology transparency assessment.

**Steps:**
1. Pass 0: Extract metadata
2. Skip Passes 1-2 (no claims/evidence)
3. Pass 3: Extract explicit RDMAP from Methods
4. Pass 4: Scan for implicit RDMAP
5. Pass 5: Consolidate RDMAP
6. Pass 6: Assess infrastructure (optional)
7. Pass 7: Validate RDMAP-only

**Time:** ~1.5 hours

**Note:** Pass 7 will note deferred validation for claims/evidence arrays.

---

### Pattern 3: Infrastructure-Only Assessment

**Use case:** Rapid reproducibility check for data/code availability.

**Steps:**
1. Pass 0: Extract metadata
2. Skip Passes 1-5 (no C&E or RDMAP)
3. Pass 6: Assess infrastructure only

**Time:** ~30-45 minutes

**Output:** Infrastructure object with PID connectivity (0-6), FAIR score (0-15), computational reproducibility (0-4)

**Use for:** Screening papers for reproducibility infrastructure, cross-paper PID adoption trends

---

### Pattern 4: Iterative Section Extraction (Large Papers)

**Use case:** Papers >50 pages with multiple results sections.

**Steps:**
1. Pass 0: Extract metadata once
2. Pass 1-2: Extract Results Section A
3. Pass 1-2: Extract Results Section B (same JSON, accumulating)
4. Pass 1-2: Extract Discussion (same JSON, accumulating)
5. Pass 3-5: Extract RDMAP from Methods
6. Pass 6: Assess infrastructure
7. Pass 7: Validate complete extraction

**Benefits:**
- Manageable section sizes
- Single final JSON (no merging)
- Progressive accumulation
- Better context window management

---

## Troubleshooting

### Issue: Claude doesn't follow prompt

**Symptoms:**
- Deviates from prompt instructions
- Doesn't use expected structure
- Ignores array boundaries (modifies wrong arrays)

**Solutions:**
✓ Verify you pasted the COMPLETE prompt (check line count matches)
✓ Mention "using research-assessor skill" explicitly
✓ Provide all required inputs (template, source text, current JSON state)
✓ Check skill is loaded (ask "Do you have research-assessor skill?")

---

### Issue: Array boundaries violated

**Symptoms:**
- Pass 3 modifies claims/evidence arrays
- Pass 1 populates RDMAP arrays

**Solutions:**
✓ Check prompt version (should be v2.6)
✓ Verify input JSON structure matches schema
✓ Re-run with explicit boundary reminder in prompt
✓ Check extraction_notes.current_pass field

---

### Issue: Reduction too high/low

**Symptoms:**
- Pass 2/5 reduces by <10% or >30%

**Solutions:**
✓ If <10%: May need more aggressive consolidation (acceptable if rationale documented)
✓ If >30%: Check for over-consolidation, verify no information loss
✓ Review consolidation_metadata.rationale for each merge
✓ Verify consolidation_metadata.information_preserved field

---

### Issue: Cross-references broken

**Symptoms:**
- Pass 7 validation reports orphaned references
- References point to non-existent IDs

**Solutions:**
✓ Check if IDs were renumbered without updating references
✓ Verify Pass 2/5 updated ALL references when consolidating
✓ Run Pass 7 validation to identify specific broken links
✓ Use validation output to locate and fix orphans

---

### Issue: FAIR scoring unclear

**Symptoms:**
- Uncertain whether GitHub-only code scores FAIR A2
- Unsure if missing data availability statement = score 0

**Solutions:**
✓ Check `.claude/skills/research-assessor/references/infrastructure/fair-principles-guide.md`
✓ GitHub-only: Scores A1 (basic access) but NOT A2 (long-term preservation)
✓ Missing statements: Document as "missing" not "negative" - pre-2016 papers expected to have none
✓ Use examples from paper to justify each FAIR principle score

---

### Issue: PID connectivity calculation

**Symptoms:**
- Uncertain which PIDs count toward connectivity score
- Unclear if grant numbers count as PIDs

**Solutions:**
✓ Check `.claude/skills/research-assessor/references/infrastructure/pid-systems-guide.md`
✓ 6 components: (1) paper DOI, (2) data DOI, (3) code DOI, (4) author ORCID, (5) funder ID, (6) vocabulary PID
✓ Each component: 0 (none) or 1 (present) → sum to 0-6 connectivity score
✓ Grant numbers: Record as alternative_identifiers but do NOT count toward core PID connectivity (weak PID)

---

### Issue: Extraction stops between passes

**Symptoms:**
- Claude asks "Should I continue to next pass?"
- Workflow pauses for permission

**Solutions:**
✓ Check CLAUDE.md - autonomous mode enabled for this project
✓ Workflow should continue automatically (don't ask permission)
✓ If using outside this project, explicitly request "continue through all passes"

---

### Issue: Item counts seem low

**Symptoms:**
- Pass 1 produces <30 evidence+claims
- Pass 3 produces <10 total RDMAP items

**Solutions:**
✓ Check section selection (Methods best for RDMAP, Results/Discussion for C&E)
✓ Verify liberal extraction mindset ("when uncertain → extract")
✓ Review extraction_notes.known_uncertainties for suppressed items
✓ Check if paper simply has minimal methodology reporting (legitimate)

---

### Issue: Uncertain during extraction

**Symptoms:**
- Many items marked extraction_confidence: low
- Unclear evidence/claim boundaries

**Solutions:**
✓ Check if right section selected (Methods for RDMAP, Results for C&E)
✓ Low confidence acceptable if text genuinely vague
✓ Skill will consult references (evidence-vs-claims-guide, tier-assignment-guide)
✓ Flag items with low confidence for manual review
✓ Pass 2/5 will refine boundaries during rationalisation

---

## Best Practices

### Planning Your Extraction

**Before starting:**
1. Review paper structure (identify Methods, Results, Discussion sections)
2. Estimate time (3-4 hours for full paper)
3. Create working directory (`outputs/{paper-slug}/`)
4. Extract PDF to text (`pdftotext -layout paper.pdf paper.txt`)
5. Copy blank template to `extraction.json`

**Document expectations:**
- What sections will you extract?
- What order? (metadata → C&E → RDMAP → infrastructure → validation)
- Any sections to skip? (e.g., methods-only extraction)

---

### During Extraction

**Save frequently:**
- After each pass (8 saves per full extraction)
- Use descriptive filenames (`extraction-pass2-claims.json`)
- Keep backups in `backups/` subdirectory

**Verify progress:**
- Check item counts after each pass
- Run quick validation checks (jq commands above)
- Review extraction_notes for uncertainties

**Document decisions:**
- Use extraction_notes.known_uncertainties for ambiguous items
- Record section boundaries (where did this section end?)
- Note any skipped content (why?)

---

### After Extraction

**Validation checklist:**
- [ ] Run Pass 7 validation
- [ ] No CRITICAL issues
- [ ] Review IMPORTANT issues (acceptable?)
- [ ] Item counts in expected ranges
- [ ] FAIR/PID scores justified with examples
- [ ] Cross-references bidirectional
- [ ] Consolidation metadata complete

**Quality checks:**
- [ ] Evidence items minimally interpreted?
- [ ] Claims supported by evidence?
- [ ] RDMAP tier assignments appropriate?
- [ ] Hierarchy logical (Design → Method → Protocol)?
- [ ] Infrastructure assessment complete?
- [ ] Historical context considered (pre-FAIR papers)?

**Archive completed extraction:**
- [ ] Save final `extraction.json`
- [ ] Save validation report
- [ ] Update `input/queue.yaml` (mark paper complete)
- [ ] Document any extraction challenges (for future reference)

---

### Tips for Success

**Liberal extraction (Passes 1, 3, 4):**
- When uncertain → extract (err on side of over-capture)
- Preserve granularity (split rather than lump)
- Document uncertainties explicitly
- Expected: 40-50% over-extraction vs final

**Rationalisation (Passes 2, 5):**
- Consolidate only when assessment impact identical
- Ask "would I assess these together or separately?"
- Document ALL consolidations with rationale
- Update ALL cross-references
- Verify information preservation

**Infrastructure assessment (Pass 6):**
- Distinguish missing statements from negative assessments
- Use specific examples to justify FAIR scores
- Consider historical context (pre-2016 = 0 FAIR expected)
- Check supplementary materials for hidden PIDs
- GitHub-only vs archived: different FAIR scoring

**Validation (Pass 7):**
- Address CRITICAL issues immediately (blocking)
- Review IMPORTANT issues (quality improvements)
- Note MINOR issues (helpful enhancements)
- Use validation output to guide refinements
- Target >80% relationship mapping coverage

---

## Next Steps

**After completing your first extraction:**
1. Review extraction quality against [quick-reference.md](quick-reference.md) success criteria
2. Compare to worked examples in `outputs/` directory
3. Refine approach based on lessons learned
4. Scale to additional papers
5. Consider batch processing for systematic review

**For advanced usage:**
- Consult [architecture.md](architecture.md) for design rationale
- Review skill references in `.claude/skills/research-assessor/references/`
- Check testing findings in `planning/pass6-phase1-testing-findings.md`

**Questions or issues?**
- Check [quick-reference.md](quick-reference.md) for common problems
- Review skill reference materials
- Consult worked examples
- Document edge cases for future guidance improvements
