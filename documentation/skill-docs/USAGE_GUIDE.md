# Usage Guide

**Version:** 2.4  
**Last Updated:** 2025-10-20

Complete guide to using the Research Assessor skill for extracting research methodology, claims, and evidence from academic papers.

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
- **Research paper** (PDF or text format)
- **Extraction prompts** (5 prompts, ~4,400 lines total)
- **Blank JSON template** (schema v2.4)

### Recommended Skills

- Basic understanding of research methodology
- Familiarity with JSON format
- Domain expertise in the research field (helpful but not required)

---

## Installation

### Step 1: Install the Skill

1. Download `research-assessor.zip` from this repository
2. Open Claude AI interface
3. Navigate to Skills settings
4. Upload the skill package
5. Verify installation: Ask Claude "Do you have the research-assessor skill?"

### Step 2: Get the Extraction Prompts

The five extraction prompts should be accessible in your project knowledge or saved locally:

1. `Claims/Evidence Pass 1 v2.4` (~800 lines)
2. `Claims/Evidence Pass 2 v2.4` (~900 lines)
3. `RDMAP Pass 1 v2.4` (~1,000 lines)
4. `RDMAP Pass 2 v2.4` (~900 lines)
5. `Pass 3 Validation v2.4` (~600 lines)

**Storage options:**
- Project Knowledge in Claude (recommended)
- Local text files
- GitHub repository

### Step 3: Prepare Your Template

Copy the blank JSON template for schema v2.4:

```json
{
  "schema_version": "2.4",
  "extraction_timestamp": "2025-10-20T10:30:00Z",
  "extractor": "Claude Sonnet 4.5",
  "evidence": [],
  "claims": [],
  "implicit_arguments": [],
  "research_designs": [],
  "methods": [],
  "protocols": [],
  "project_metadata": {},
  "extraction_notes": {
    "pass": 1,
    "section_extracted": "",
    "known_uncertainties": []
  }
}
```

Save this as `extraction-template-v2.4.json`

---

## Complete Workflow

### Overview

```
Research Paper
       ↓
[Section Selection]
       ↓
┌──────────────────────┐
│  Pass 1: Claims      │  ← Provide prompt + section
│  Liberal Extraction  │  → JSON with evidence/claims
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│  Pass 2: Claims      │  ← Provide prompt + Pass 1 JSON
│  Rationalization     │  → Refined evidence/claims
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│  Pass 1: RDMAP       │  ← Provide prompt + section
│  Liberal Extraction  │  → JSON with RDMAP added
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│  Pass 2: RDMAP       │  ← Provide prompt + Pass 1 JSON
│  Rationalization     │  → Refined RDMAP
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│  Pass 3: Validation  │  ← Provide prompt + complete JSON
│  Integrity Checks    │  → Validation report
└──────────────────────┘
```

### Time Estimates

**Per paper section (~5-10 pages):**
- Pass 1 Claims: 10-15 minutes
- Pass 2 Claims: 10-15 minutes
- Pass 1 RDMAP: 15-20 minutes
- Pass 2 RDMAP: 10-15 minutes
- Pass 3 Validation: 5-10 minutes
- **Total: 50-75 minutes per section**

**Full paper (30-50 pages):**
- Extract by section: 3-5 hours
- Review and refine: 1-2 hours
- **Total: 4-7 hours**

---

## Pass-by-Pass Instructions

### Pass 1: Claims/Evidence Liberal Extraction

**Goal:** Comprehensive capture of evidence, claims, and implicit arguments.

**Inputs:**
1. Claims/Evidence Pass 1 prompt
2. Source section text (Results or Discussion typically)
3. JSON document (blank or with RDMAP already extracted)

**Conversation Template:**
```
You: I'm using the research-assessor skill for claims extraction.

Here's the Pass 1 prompt:
[paste entire Claims/Evidence Pass 1 prompt]

Extract from this section:
[paste source text - typically 2-5 pages]

Use this JSON document:
[paste blank template or partially populated JSON]

Claude: [Follows prompt to extract evidence, claims, implicit_arguments]
```

**What to Expect:**
- 40-60 evidence items
- 30-50 claims
- 5-15 implicit arguments
- Intentional over-extraction
- Some borderline cases included

**Verification:**
- All claims have some evidence support
- Location tracking present
- Extraction notes document uncertainties

---

### Pass 2: Claims/Evidence Rationalization

**Goal:** Consolidate, refine, and verify the Pass 1 extraction.

**Inputs:**
1. Claims/Evidence Pass 2 prompt
2. Original source section text (for verification)
3. Pass 1 JSON output

**Conversation Template:**
```
You: Continuing with rationalization using research-assessor skill.

Here's the Pass 2 prompt:
[paste entire Claims/Evidence Pass 2 prompt]

Here's the source text for reference:
[paste original section]

Here's the Pass 1 extraction to rationalize:
[paste Pass 1 JSON]

Claude: [Follows prompt to consolidate and refine]
```

**What to Expect:**
- 15-20% reduction in item count
- Better-defined boundaries
- Consolidation metadata added
- Improved relationships

**Verification:**
- Check consolidation metadata is present
- Verify consolidated items make sense
- Confirm no information loss
- Review boundary corrections

---

### Pass 1: RDMAP Liberal Extraction

**Goal:** Comprehensive capture of research designs, methods, and protocols.

**Inputs:**
1. RDMAP Pass 1 prompt
2. Methods section text
3. JSON document (blank or with claims/evidence already extracted)

**Conversation Template:**
```
You: Extracting RDMAP using research-assessor skill.

Here's the RDMAP Pass 1 prompt:
[paste entire RDMAP Pass 1 prompt]

Extract from this Methods section:
[paste Methods section text]

Use this JSON:
[paste template or JSON with claims/evidence]

Claude: [Follows prompt to extract research_designs, methods, protocols]
```

**What to Expect:**
- 10-15 research designs
- 20-30 methods
- 15-25 protocols
- Three-tier hierarchy clear
- Cross-references to claims/evidence (if present)

**Verification:**
- Tier assignments appropriate (Design/Method/Protocol)
- Cross-references point to valid IDs
- Expected information gaps flagged

---

### Pass 2: RDMAP Rationalization

**Goal:** Consolidate, verify hierarchy, and formalize cross-references.

**Inputs:**
1. RDMAP Pass 2 prompt
2. Original Methods section text
3. Pass 1 RDMAP JSON

**Conversation Template:**
```
You: Rationalizing RDMAP using research-assessor skill.

Here's the RDMAP Pass 2 prompt:
[paste entire RDMAP Pass 2 prompt]

Here's the Methods section for reference:
[paste original section]

Here's the Pass 1 extraction:
[paste Pass 1 JSON]

Claude: [Follows prompt to rationalize RDMAP]
```

**What to Expect:**
- 15-20% reduction in RDMAP items
- Tier corrections if needed
- Consolidated procedures
- Formalized cross-references

**Verification:**
- Hierarchy makes sense (Design → Method → Protocol)
- Cross-references bidirectional
- Consolidation metadata present

---

### Pass 3: Validation

**Goal:** Verify structural integrity and cross-reference consistency.

**Inputs:**
1. Validation Pass 3 prompt
2. Complete extraction JSON (after all Pass 2s)

**Conversation Template:**
```
You: Validating complete extraction using research-assessor skill.

Here's the Validation Pass 3 prompt:
[paste entire Validation prompt]

Here's the complete extraction to validate:
[paste complete JSON with all arrays populated]

Claude: [Produces validation report]
```

**What to Expect:**
- Validation report (separate JSON)
- Cross-reference integrity checks
- Hierarchy validation
- Schema compliance verification
- List of issues by severity

**Verification:**
- Address CRITICAL issues immediately
- Review IMPORTANT issues
- Note MINOR issues for future refinement

---

## Working with JSON

### Managing Large JSONs

**Problem:** Complete extractions can be 100-150 objects, difficult to read.

**Solutions:**

**1. Use JSON viewer:**
```bash
# Pretty print with jq
cat extraction.json | jq '.' > extraction-pretty.json

# View specific arrays
cat extraction.json | jq '.evidence[]'
```

**2. Extract by section:**
- Process one section at a time
- Merge at the end
- Easier to manage

**3. Use extraction_notes:**
```json
"extraction_notes": {
  "section": "Methods",
  "pass": 2,
  "item_counts": {
    "evidence": 45,
    "claims": 32,
    "research_designs": 12,
    "methods": 25,
    "protocols": 18
  }
}
```

### Merging Extractions

**If you extract sections separately:**

1. Keep `schema_version`, `extraction_timestamp`, `extractor`
2. Concatenate arrays:
   - `evidence`: all evidence from all sections
   - `claims`: all claims from all sections
   - etc.
3. **Renumber IDs** to avoid collisions:
   - Section 1: E001-E050, C001-C040
   - Section 2: E051-E100, C041-C080
4. **Update cross-references** accordingly

**Python example:**
```python
import json

# Load extractions
with open('section1.json') as f:
    s1 = json.load(f)
with open('section2.json') as f:
    s2 = json.load(f)

# Merge arrays
merged = {
    "schema_version": "2.4",
    "evidence": s1['evidence'] + s2['evidence'],
    "claims": s1['claims'] + s2['claims'],
    # ... etc
}

# Renumber and update references (implement renumbering logic)

with open('merged.json', 'w') as f:
    json.dump(merged, f, indent=2)
```

### Backing Up Work

**Best Practice:** Save after each pass.

```
project/
├── extraction-pass1-claims.json
├── extraction-pass2-claims.json
├── extraction-pass1-rdmap.json
├── extraction-pass2-rdmap.json
└── extraction-validated.json
```

---

## Common Patterns

### Pattern 1: Extract Results and Methods

**Use case:** Full extraction from a paper.

**Steps:**
1. Extract claims from Results section (Pass 1 + 2)
2. Extract RDMAP from Methods section (Pass 1 + 2)
3. Validate complete extraction (Pass 3)

**Time:** ~2 hours

---

### Pattern 2: Methods-Only Extraction

**Use case:** Focus on methodology transparency.

**Steps:**
1. Start with blank template
2. Extract RDMAP from Methods (Pass 1 + 2)
3. Validate RDMAP-only (Pass 3 with deferred validation)

**Time:** ~45 minutes

**Note:** Pass 3 will note deferred validation for claims/evidence.

---

### Pattern 3: Iterative Section Extraction

**Use case:** Large paper (50+ pages).

**Steps:**
1. Start with blank template
2. Extract Results Section A (Pass 1 + 2)
3. Extract Results Section B on same JSON (Pass 1 + 2)
4. Extract Discussion on same JSON (Pass 1 + 2)
5. Extract Methods on same JSON (Pass 1 + 2)
6. Validate complete extraction (Pass 3)

**Benefits:**
- Manageable sections
- Single final JSON
- Progressive accumulation

---

### Pattern 4: Quick Assessment

**Use case:** Rapid transparency check.

**Steps:**
1. Extract Methods only (Pass 1 RDMAP)
2. Check expected_information_missing fields
3. Skip Pass 2 and validation

**Time:** ~20 minutes

**Note:** Lower quality, but fast for screening.

---

## Troubleshooting

### Issue: Claude doesn't follow prompt

**Symptoms:**
- Deviates from prompt instructions
- Doesn't use expected structure
- Ignores boundaries

**Solutions:**
1. ✓ Verify you provided the COMPLETE prompt (all ~800-1000 lines)
2. ✓ Check you mentioned "using research-assessor skill"
3. ✓ Ensure source text is provided
4. ✓ Start fresh conversation if context cluttered

---

### Issue: Cross-references broken

**Symptoms:**
- IDs in cross-references don't exist
- Bidirectional inconsistency

**Solutions:**
1. ✓ Run Pass 3 validation to identify issues
2. ✓ Check if IDs were renumbered without updating references
3. ✓ Verify Pass 2 updated references when consolidating

---

### Issue: Over-extraction seems excessive

**Symptoms:**
- 80+ evidence items from short section
- Many borderline cases

**Diagnosis:** This may be **correct** for Pass 1.

**Solutions:**
1. ✓ Confirm it's Pass 1 (liberal extraction expected)
2. ✓ Run Pass 2 to consolidate (should reduce 15-20%)
3. ✓ Check if truly all evidence or project metadata mixed in

---

### Issue: Consolidation loses information

**Symptoms:**
- Pass 2 combines items inappropriately
- Critical details missing after consolidation

**Solutions:**
1. ✓ Review consolidation_metadata for rationale
2. ✓ Check consolidation-patterns.md for guidance
3. ✓ Manually split if needed
4. ✓ Provide clearer instruction about what to preserve

---

### Issue: Tier assignments unclear

**Symptoms:**
- Unsure if Design, Method, or Protocol
- Extraction mixes tiers

**Solutions:**
1. ✓ Have Claude read tier-assignment-guide.md
2. ✓ Use the decision tests:
   - "Is this about WHY (framing/rationale)?" → Design
   - "Is this about WHAT (general approach)?" → Method
   - "Is this about HOW (specific procedure)?" → Protocol
3. ✓ When uncertain, extract at multiple levels and rationalize in Pass 2

---

### Issue: Extraction confidence low

**Symptoms:**
- Many items marked `extraction_confidence: low`
- Lots of uncertainties in extraction_notes

**Solutions:**
1. ✓ This may be **appropriate** if text is vague
2. ✓ Flag these for manual review
3. ✓ Consider if domain expertise needed
4. ✓ Check if right section (Methods section best for RDMAP)

---

## Best Practices

### 1. Start with Methods Section

**Why:** Best-documented, most structured.

**Approach:**
- Extract RDMAP first (Pass 1 + 2)
- Then extract claims if needed
- Build confidence with clear content

---

### 2. Keep Source Text Accessible

**Why:** Pass 2 needs source for verification.

**Approach:**
- Copy section text to separate document
- Reference line/paragraph numbers
- Maintain context for review

---

### 3. Document as You Go

**Why:** Context loss over long extractions.

**Approach:**
```json
"extraction_notes": {
  "section": "Methods subsection 3.2",
  "challenges": "Sampling strategy not explicitly stated",
  "decisions": "Inferred stratified from context",
  "review_needed": ["Protocol P015 boundaries unclear"]
}
```

---

### 4. Validate Early and Often

**Why:** Catch issues before they compound.

**Approach:**
- Run Pass 3 after each section
- Fix issues immediately
- Don't wait until full paper extracted

---

### 5. Build Domain-Specific Examples

**Why:** Improves future extractions.

**Approach:**
- Save good examples from your extractions
- Note domain-specific patterns
- Build your own vocabulary lists
- Contribute back to project

---

### 6. Use Project Knowledge Effectively

**Why:** Efficient context management.

**Approach:**
- Store prompts in Project Knowledge
- Reference by name: "Use the Claims Pass 1 prompt from Project Knowledge"
- Keep frequently-used templates there
- Reduces copy-paste errors

---

### 7. Manage Context Window

**Why:** Long papers can exceed context limits.

**Approach:**
- Extract by section
- Use fresh conversations for each pass
- Don't keep entire paper in context
- Load only current section text

---

### 8. Review Consolidation Metadata

**Why:** Understand rationalization decisions.

**Approach:**
```json
"consolidation_metadata": {
  "consolidated_from": ["E042", "E043", "E044"],
  "consolidation_type": "procedure_chain",
  "rationale": "Sequential GPS procedure steps assessed as unit"
}
```

Check this explains the consolidation clearly.

---

### 9. Track Expected Information Gaps

**Why:** Identify transparency issues systematically.

**Approach:**
```json
"expected_information_missing": [
  "TIDieR element 7: Procedure modification criteria not specified",
  "CONSORT-Outcomes element 3: Measurement timing unclear"
]
```

Aggregate these for assessment.

---

### 10. Test on Known Papers First

**Why:** Calibrate understanding.

**Approach:**
- Start with Sobotkova et al. (2023) example
- Compare your extraction to example
- Understand decision patterns
- Then extract your target papers

---

## Advanced Usage

### Custom Prompt Variations

**For specialized domains:**
1. Copy base prompt
2. Add domain-specific examples
3. Adjust expected information checklists
4. Test and refine
5. Document changes

**Example:** Ecology adaptation
- Add ecology-specific study designs
- Modify sampling strategies for field ecology
- Adjust expected information for ecological methods
- Add ecology examples

---

### Batch Processing

**For multiple papers:**
1. Set up extraction pipeline
2. Process papers sequentially
3. Maintain consistent prompt versions
4. Aggregate results for analysis

**Python pseudo-code:**
```python
for paper in papers:
    # Pass 1 Claims
    claims_p1 = extract(paper, claims_p1_prompt)
    
    # Pass 2 Claims
    claims_p2 = rationalize(claims_p1, claims_p2_prompt)
    
    # Pass 1 RDMAP
    rdmap_p1 = extract(paper, rdmap_p1_prompt)
    
    # Pass 2 RDMAP
    rdmap_p2 = rationalize(rdmap_p1, rdmap_p2_prompt)
    
    # Validate
    validation = validate(claims_p2 + rdmap_p2, validation_prompt)
    
    # Save
    save(paper.id, claims_p2, rdmap_p2, validation)
```

---

### Quality Control

**For critical extractions:**
1. **Double extraction:** Two extractors independently
2. **Compare:** Identify differences
3. **Reconcile:** Discuss disagreements
4. **Document:** Final decisions and rationale

**Inter-rater reliability:**
- Calculate agreement rates
- Identify systematic differences
- Refine prompts based on patterns

---

## Additional Resources

**In This Repository:**
- [README.md](README.md) - Overview and quick start
- [ARCHITECTURE.md](ARCHITECTURE.md) - Design principles
- [TESTING.md](TESTING.md) - Testing procedures
- [PROMPT_REVISION_SUMMARY.md](PROMPT_REVISION_SUMMARY.md) - Development history

**In Skill Package:**
- references/schema/schema-guide.md - Complete schema
- references/checklists/tier-assignment-guide.md - Tier decisions
- references/checklists/consolidation-patterns.md - Consolidation logic
- references/checklists/expected-information.md - Completeness checklists
- references/examples/sobotkova-example.md - Worked example

---

## Getting Help

**If stuck:**
1. Check [Troubleshooting](#troubleshooting) section above
2. Review relevant checklist in skill package
3. Consult worked example (sobotkova-example.md)
4. Check [ARCHITECTURE.md](ARCHITECTURE.md) for design rationale
5. Open issue on GitHub repository

---

## Next Steps

After mastering basic extraction:
1. **Adapt to your domain** - Add domain-specific examples
2. **Build vocabulary** - Contribute controlled vocabularies
3. **Develop assessment** - Create transparency scoring
4. **Scale up** - Process multiple papers
5. **Contribute back** - Share improvements with community

**See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.**
