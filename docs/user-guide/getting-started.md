# Getting Started

Quick start guide for your first extraction using the Research Assessor skill.

**Version:** 2.6
**Last Updated:** 2025-11-13

---

## Prerequisites

- **Claude Code** or **Claude AI** with Skills support
- **Claude Sonnet 4.5** or later (recommended)
- **Python 3.8+** for PDF extraction (optional, if using PDFs)
- **Research paper** to extract from (your own or open access)

---

## Installation

### 1. Install the Research Assessor Skill

The research-assessor skill is included with this project at `.claude/skills/research-assessor/`.

**In Claude Code:**
- The skill loads automatically from your project

**In Claude AI web interface:**
1. Package the skill from `.claude/skills/research-assessor/`
2. Install via Claude Skills interface
3. Verify by asking Claude: "Do you have the research-assessor skill?"

See [Research Assessor Guide](../research-assessor-guide/) for detailed skill documentation.

### 2. Install PDF Extraction Tools (Optional)

If working with PDFs:

```bash
cd llm-reproducibility
pip install -r requirements.txt
```

See [pdf-extraction.md](pdf-extraction.md) for full PDF processing guide.

---

## Your First Extraction

### Step 0: Prepare Your Paper

**Option A: PDF**
```bash
python extraction-system/scripts/pdf_processing/extract_pdf_text.py "your-paper.pdf"
# Output: input/sources/processed-md/your-paper.md
```

**Option B: Already have text**
Copy paper text to a convenient location for pasting into Claude.

### Step 1: Get the Blank Template

Copy the blank template from `extraction-system/templates/blank_template_v2.6.json` to your working directory.

The template has this structure:
```json
{
  "schema_version": "2.6",
  "extraction_timestamp": "2025-11-13T10:00:00Z",
  "extractor": "Your Name",
  "metadata": {
    "title": "Your Paper Title",
    "authors": ["Author One", "Author Two"],
    "publication_year": 2023,
    "doi": "10.xxxx/xxxxx",
    "journal": "Journal Name"
  },
  "evidence": [],
  "claims": [],
  "implicit_arguments": [],
  "research_designs": [],
  "methods": [],
  "protocols": [],
  "infrastructure": {}
}
```

### Step 2: Run Pass 0 (Metadata)

**In Claude:**

```
Here's the Pass 0 metadata prompt:
[paste: extraction-system/prompts/00-metadata_pass0_prompt.md]

Here's the paper:
[paste: full paper text or key sections]

Here's the blank JSON template:
[paste: blank_template_v2.6.json]

Please extract metadata and map the paper structure.
```

**Claude will:**
- Extract publication metadata
- Map paper structure (sections, subsections)
- Identify key methodological components
- Return updated JSON with metadata populated

**Save the output JSON** as `your-paper_pass0.json`

### Step 3: Run Pass 1 (Claims/Evidence - Liberal)

**In Claude:**

```
Here's the Claims/Evidence Pass 1 prompt:
[paste: extraction-system/prompts/01-claims-evidence_pass1_prompt.md]

Here's the paper's Results and Discussion sections:
[paste: Results and Discussion text]

Here's the JSON from Pass 0:
[paste: your-paper_pass0.json]

Please extract evidence, claims, and implicit arguments liberally.
```

**Claude will:**
- Extract evidence objects (observations, measurements)
- Extract claim objects (interpretations, assertions)
- Extract implicit argument objects (assumptions, implications)
- Return updated JSON with these arrays populated

**Save the output JSON** as `your-paper_pass1.json`

### Step 4: Run Pass 2 (Claims/Evidence - Rationalisation)

```
Here's the Claims/Evidence Pass 2 prompt:
[paste: extraction-system/prompts/02-claims-evidence_pass2_prompt.md]

Here's the JSON from Pass 1:
[paste: your-paper_pass1.json]

Please rationalise the extraction and consolidate redundant items.
```

**Claude will:**
- Consolidate redundant items (15-20% reduction)
- Refine boundaries
- Add consolidation_metadata to merged items
- Verify cross-references
- Return refined JSON

**Save as** `your-paper_pass2.json`

### Step 5: Run Pass 3 (RDMAP Explicit)

```
Here's the RDMAP Pass 3 explicit prompt:
[paste: extraction-system/prompts/03-rdmap_pass1a_explicit_prompt.md]

Here's the paper's Methods section:
[paste: Methods section text]

Here's the JSON from Pass 2:
[paste: your-paper_pass2.json]

Please extract explicitly stated research designs, methods, and protocols.
```

**Claude will:**
- Extract research designs (strategic framing)
- Extract methods (tactical approaches)
- Extract protocols (operational procedures)
- Mark all as `explicitly_stated: true`
- Return updated JSON

**Save as** `your-paper_pass3.json`

### Step 6: Run Pass 4 (RDMAP Implicit)

```
Here's the RDMAP Pass 4 implicit prompt:
[paste: extraction-system/prompts/04-rdmap_pass1b_implicit_prompt.md]

Here's the paper's Methods section:
[paste: Methods section text]

Here's the JSON from Pass 3:
[paste: your-paper_pass3.json]

Please extract implicit, assumed, or inadequately documented RDMAP.
```

**Claude will:**
- Identify methodological gaps
- Extract implicit standard practices
- Infer assumed procedures
- Mark all as `explicitly_stated: false`
- Return updated JSON

**Save as** `your-paper_pass4.json`

### Step 7: Run Pass 5 (RDMAP Rationalisation)

```
Here's the RDMAP Pass 5 rationalisation prompt:
[paste: extraction-system/prompts/05-rdmap_pass2_prompt.md]

Here's the JSON from Pass 4:
[paste: your-paper_pass4.json]

Please rationalise the RDMAP extraction.
```

**Claude will:**
- Consolidate redundant RDMAP items (15-20% reduction)
- Verify tier assignments (Design/Method/Protocol)
- Formalise cross-references to claims/evidence
- Validate explicit/implicit distinctions
- Return refined JSON

**Save as** `your-paper_pass5.json`

### Step 8: Run Pass 6 (Infrastructure)

```
Here's the Pass 6 infrastructure prompt:
[paste: extraction-system/prompts/06-infrastructure_pass6_prompt.md]

Here's the full paper text (focus on acknowledgements, methods, references):
[paste: full paper or relevant sections]

Here's the JSON from Pass 5:
[paste: your-paper_pass5.json]

Please extract infrastructure elements (PIDs, FAIR, funding, permits).
```

**Claude will:**
- Extract PIDs (DOI, ORCID, data/code DOIs)
- Assess FAIR compliance (data and code)
- Extract funding information
- Extract permits and authorisations
- Return updated JSON with infrastructure object populated

**Save as** `your-paper_pass6.json`

### Step 9: Run Pass 7 (Validation)

```
Here's the Pass 7 validation prompt:
[paste: extraction-system/prompts/07-validation_prompt.md]

Here's the complete extraction:
[paste: your-paper_pass6.json]

Please validate the extraction comprehensively.
```

**Claude will return a validation report** showing:
- Overall status (PASS / PASS_WITH_ISSUES / FAIL)
- Issues by severity (CRITICAL / IMPORTANT / MINOR)
- Cross-reference integrity checks
- Schema compliance verification
- Recommendations for fixes

**Address any CRITICAL issues** and re-run validation if needed.

**Save final extraction as** `your-paper_extraction.json`

---

## What You Should See

### After Pass 0 (Metadata)
- Complete publication metadata
- Paper structure map (sections, subsections)
- Key component identification
- Duration: 10-15 minutes

### After Pass 1 (Claims Liberal)
- 40-60 evidence items
- 30-50 claims
- 5-15 implicit arguments
- Intentional over-capture (40-50% more than final)
- Duration: 45-60 minutes

### After Pass 2 (Claims Rationalisation)
- 15-20% reduction from Pass 1
- Consolidation_metadata on merged items
- Refined boundaries
- Better cross-references
- Duration: 30-45 minutes

### After Pass 3 (RDMAP Explicit)
- 6-12 research designs (explicit only)
- 12-25 methods (explicit only)
- 8-20 protocols (explicit only)
- All marked `explicitly_stated: true`
- Duration: 60-90 minutes

### After Pass 4 (RDMAP Implicit)
- 2-4 additional research designs (implicit)
- 3-8 additional methods (implicit)
- 2-8 additional protocols (implicit)
- All marked `explicitly_stated: false`
- Duration: 30-45 minutes

### After Pass 5 (RDMAP Rationalisation)
- 15-20% reduction from Passes 3+4
- Tier assignments verified (Design/Method/Protocol)
- Cross-references to claims/evidence formalised
- Duration: 45-60 minutes

### After Pass 6 (Infrastructure)
- PIDs extracted (DOI, ORCID, repository DOIs)
- FAIR assessments for data and code
- Funding information captured
- Permits and authorisations documented
- Duration: 30-45 minutes

### After Pass 7 (Validation)
- Zero CRITICAL issues
- Few IMPORTANT issues (<5)
- Cross-reference integrity: 100%
- Ready for assessment
- Duration: 15-30 minutes

---

## Common First-Time Issues

### "I extracted too few items in Pass 1, 3, or 4"
**Fix:** Re-run liberal extraction passes with explicit instruction to over-capture. Aim for 40-50% more items than you think you need.

### "I can't tell if something is evidence or a claim"
**Guidance:**
- Evidence = minimal inference (observation, measurement, count)
- Claim = requires interpretation, categorisation, or inference
- See [schema-reference.md](schema-reference.md) for detailed distinctions

### "I can't tell if something is a Design, Method, or Protocol"
**Guidance:**
- Design = strategic framing and rationale (WHY)
- Method = tactical approach (WHAT was done)
- Protocol = operational procedure (HOW specifically, step-by-step)
- See [extraction-workflow.md](extraction-workflow.md) for three-tier framework

### "The JSON is getting too large for Claude"
**Fix:**
- Extract one section at a time (Results, then Discussion)
- Use the same JSON document, it accumulates across sections
- For very large papers, consider splitting extraction across multiple sessions

### "Validation shows many broken cross-references"
**Check:**
- Did you complete all passes (0-6)?
- Partial extractions will show deferred validation (expected)
- Re-run Passes 2 or 5 if consolidation broke references

### "Infrastructure extraction returned empty fields"
**Check:**
- Does the paper actually contain this information?
- Many papers lack data/code repositories (FAIR scores will be low)
- Some papers lack explicit funding statements
- Check acknowledgements, methods, references, and supplementary materials

---

## Next Steps

### Learn More
- **[Extraction Workflow](extraction-workflow.md)** - Complete 7-pass guide with detailed explanations
- **[Schema Reference](schema-reference.md)** - Understanding object types and field definitions
- **[Examples Directory](../../examples/)** - See complete extractions (coming soon)
- **[Extraction System Overview](../../extraction-system/README.md)** - Technical documentation
- **[Research Assessor Guide](../research-assessor-guide/)** - Skill documentation

### Improve Your Extractions
- Study completed examples in `outputs/` directory
- Review [extraction-workflow.md](extraction-workflow.md) for best practices
- Check [schema-reference.md](schema-reference.md) for detailed field guidance
- Test validation with `extraction-system/scripts/validate_extraction.py`

### Test on More Papers
- Start with papers you know well (can validate extraction easily)
- Try varied domains (archaeology, ecology, ethnography, etc.)
- Compare extractions across methodological paradigms
- Share feedback and improvements

---

## Troubleshooting

**"Skill not loading"**
→ Verify skill location (`.claude/skills/research-assessor/`), check Claude Code version

**"Prompts not working"**
→ Ensure you're using v2.6 prompts from `extraction-system/prompts/`

**"JSON validation failing"**
→ Check `schema_version` is "2.6", verify all required fields present

**"Wrong pass modified my arrays"**
→ Verify prompt version (v2.6 has strict separation of concerns)

**"Need help"**
→ See [Research Assessor Guide](../research-assessor-guide/) or review [extraction-system/README.md](../../extraction-system/README.md)

---

**Questions?** See the [extraction workflow guide](extraction-workflow.md) or [Research Assessor documentation](../research-assessor-guide/) for comprehensive details.

**Ready to go!** Start with Pass 0 to map your paper structure, then proceed through the 7-pass workflow.
