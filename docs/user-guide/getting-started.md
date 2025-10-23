# Getting Started

Quick start guide for your first extraction using the Research Assessor skill.

---

## Prerequisites

- **Claude AI** with Skills support
- **Claude Sonnet 4.5** or later (recommended)
- **Python 3.8+** for PDF extraction (optional, if using PDFs)
- **Research paper** to extract from (your own or open access)

---

## Installation

### 1. Install the Research Assessor Skill

1. Download: [../../extraction-system/skill/research-assessor-v2.5.zip](../../extraction-system/skill/research-assessor-v2.5.zip)
2. Install via Claude Skills interface
3. Verify by asking Claude: "Do you have the research-assessor skill?"

See [../skill-documentation/INSTALLATION_GUIDE.md](../skill-documentation/INSTALLATION_GUIDE.md) for detailed instructions.

### 2. Install PDF Extraction Tools (Optional)

If working with PDFs:

```bash
cd llm-reproducibility
pip install -r requirements.txt
```

See [pdf-extraction.md](pdf-extraction.md) for full PDF processing guide.

---

## Your First Extraction

### Step 1: Prepare Your Paper

**Option A: PDF**
```bash
python extraction-system/scripts/extract_pdf_text.py "your-paper.pdf"
# Output: sources/processed-md/your-paper.md
```

**Option B: Already have text**
Copy paper text to a convenient location for pasting into Claude.

### Step 2: Get the Blank Template

Copy [../../examples/blank_template_v2.5.json](../../examples/blank_template_v2.5.json) to your working directory.

Fill in paper metadata:
```json
{
  "schema_version": "2.5",
  "extraction_timestamp": "2025-10-23T10:00:00Z",
  "extractor": "Your Name",
  "paper_metadata": {
    "title": "Your Paper Title",
    "authors": ["Author One", "Author Two"],
    "year": 2023,
    "doi": "10.xxxx/xxxxx",
    "journal": "Journal Name"
  },
  ...
}
```

### Step 3: Run Claims/Evidence Pass 1

**In Claude:**

```
Here's the Claims/Evidence Pass 1 prompt:
[paste: extraction-system/prompts/claims-evidence_pass1_prompt.md]

Here's the paper's Results section:
[paste: Results section text]

Here's the blank JSON template:
[paste: blank_template_v2.5.json]

Please extract evidence, claims, and implicit arguments.
```

**Claude will:**
- Extract evidence objects (observations, measurements)
- Extract claim objects (interpretations, assertions)
- Extract implicit argument objects (assumptions, implications)
- Return updated JSON with these arrays populated

**Save the output JSON** as `your-paper_pass1.json`

### Step 4: Run Claims/Evidence Pass 2

```
Here's the Claims/Evidence Pass 2 prompt:
[paste: extraction-system/prompts/claims-evidence_pass2_prompt.md]

Here's the JSON from Pass 1:
[paste: your-paper_pass1.json]

Please rationalize the extraction.
```

**Claude will:**
- Consolidate redundant items
- Refine boundaries
- Add consolidation_metadata
- Return refined JSON

**Save as** `your-paper_pass2.json`

### Step 5: Run RDMAP Pass 1

```
Here's the RDMAP Pass 1 prompt:
[paste: extraction-system/prompts/rdmap_pass1_prompt.md]

Here's the paper's Methods section:
[paste: Methods section text]

Here's the JSON from Pass 2:
[paste: your-paper_pass2.json]

Please extract research designs, methods, and protocols.
```

**Save as** `your-paper_rdmap_pass1.json`

### Step 6: Run RDMAP Pass 2

```
Here's the RDMAP Pass 2 prompt:
[paste: extraction-system/prompts/rdmap_pass2_prompt.md]

Here's the JSON from RDMAP Pass 1:
[paste: your-paper_rdmap_pass1.json]

Please rationalize the RDMAP extraction.
```

**Save as** `your-paper_rdmap_pass2.json`

### Step 7: Run Validation (Pass 3)

```
Here's the Pass 3 validation prompt:
[paste: extraction-system/prompts/rdmap_pass3_prompt.md]

Here's the complete extraction:
[paste: your-paper_rdmap_pass2.json]

Please validate the extraction.
```

**Claude will return a validation report** showing:
- Overall status (PASS / PASS_WITH_ISSUES / FAIL)
- Issues by severity
- Recommendations

**Address any CRITICAL issues** and re-run validation if needed.

---

## What You Should See

### After Claims Pass 1
- 40-60 evidence items
- 30-50 claims
- 5-15 implicit arguments
- Intentional over-capture (40-50% more than final)

### After Claims Pass 2
- 15-20% reduction from Pass 1
- Consolidation_metadata on merged items
- Refined boundaries
- Better cross-references

### After RDMAP Pass 1
- 8-15 research designs
- 15-30 methods
- 10-25 protocols
- Three-tier hierarchy clear

### After RDMAP Pass 2
- 15-20% reduction from Pass 1
- Tier assignments verified
- Cross-references to claims/evidence formalized

### After Validation
- Zero CRITICAL issues
- Few IMPORTANT issues (<5)
- Cross-reference integrity: 100%
- Ready for assessment

---

## Common First-Time Issues

### "I extracted too few items in Pass 1"
**Fix:** Re-run Pass 1 with explicit instruction to over-capture. Aim for 40-50% more items than you think you need.

### "I can't tell if something is evidence or a claim"
**Guidance:**
- Evidence = minimal inference (observation, measurement, count)
- Claim = requires interpretation, categorization, or inference
- See [schema-reference.md](schema-reference.md) for detailed distinctions

### "The JSON is getting too large for Claude"
**Fix:**
- Extract one section at a time
- Use the same JSON document, it accumulates across sections
- For very large papers, consider splitting by Results vs Discussion

### "Validation shows many broken cross-references"
**Check:**
- Did you run both Claims/Evidence AND RDMAP passes?
- Partial extractions will show deferred validation (expected)

---

## Next Steps

### Learn More
- **[Extraction Workflow](extraction-workflow.md)** - Complete 5-pass guide
- **[Schema Reference](schema-reference.md)** - Understanding object types
- **[Examples](../../examples/)** - See complete extraction (Sobotkova paper)
- **[Skill Documentation](../skill-documentation/)** - Technical details

### Improve Your Extractions
- Study the [Sobotkova complete example](../../examples/sobotkova_complete.json)
- Review [QUICK_REFERENCE.md](../skill-documentation/QUICK_REFERENCE.md) for common patterns
- Check [extraction-workflow.md](extraction-workflow.md) for best practices

### Test on More Papers
- Start with papers you know well (can validate extraction easily)
- Try varied domains (archaeology, ecology, ethnography, etc.)
- Share results via [CONTRIBUTING.md](../skill-documentation/CONTRIBUTING.md)

---

## Troubleshooting

**"Skill not loading"**
→ Verify skill installation, check Claude version (need 4.5+)

**"Prompts not working"**
→ Ensure you're using v2.5 prompts from extraction-system/prompts/

**"JSON validation failing"**
→ Check schema_version is "2.5", verify all required fields present

**"Need help"**
→ See [skill documentation](../skill-documentation/) or review [examples](../../examples/)

---

**Questions?** See the [extraction workflow guide](extraction-workflow.md) or [skill documentation](../skill-documentation/) for comprehensive details.

**Ready to go!** Start with Claims/Evidence Pass 1 on your paper's Results section.
