# Extraction Examples

Curated examples showing complete extractions using the Research Assessor skill v2.5.

---

## Available Examples

### [sobotkova_complete.json](sobotkova_complete.json)

Complete extraction from:
**Sobotkova, A., Ross, S. A., Ballsun-Stanton, B., Fairbairn, A., Thompson, J., & VanValkenburgh, P. (2023)**. "Creating large, high-quality geospatial datasets from historical maps using novice volunteers" (*FAIMS Mobile Platform* paper).

**Domain:** Archaeological survey methodology
**Extraction Version:** v2.5 (Claims/Evidence Pass 1 complete)
**Quality:**
- 120+ objects extracted
- 200+ cross-references
- Comprehensive provenance tracking
- Complete validation passing

**What's Included:**
- Evidence objects (observations, measurements, data points)
- Claims (interpretations and assertions)
- Implicit arguments (assumptions and implications)
- Research designs (strategic framing)
- Methods (tactical approaches)
- Protocols (operational procedures)

**Use This Example To:**
- See what a complete extraction looks like
- Understand object type distinctions
- Learn cross-reference patterns
- Verify extraction quality for your own work

---

### [blank_template_v2.5.json](blank_template_v2.5.json)

Starting template for new extractions.

**Use This Template:**
1. Copy to your working directory
2. Fill in paper_metadata
3. Run through the five-pass extraction workflow
4. Template will accumulate content as you go

**Schema Version:** 2.5
**Compatible With:**
- Claims/Evidence Pass 1 & 2 prompts
- RDMAP Pass 1 & 2 prompts
- Pass 3 validation prompt

---

## Using These Examples

### To Learn the System

1. **Read sobotkova_complete.json** to see real extraction output
2. **Compare to the source paper** (if available) to understand how text maps to objects
3. **Study cross-references** to see how objects relate
4. **Check consolidation_metadata** to understand rationalization process

### To Start Your Own Extraction

1. **Copy blank_template_v2.5.json** to a new file
2. **Fill in paper metadata** (title, authors, year, DOI, etc.)
3. **Run Claims/Evidence Pass 1** with your paper's Results/Discussion
4. **Continue through workflow** (see [docs/user-guide/extraction-workflow.md](../docs/user-guide/extraction-workflow.md))

### To Validate Your Work

Compare your extraction to sobotkova_complete.json:
- **Object count**: Are you in the right ballpark? (40-60 evidence, 30-50 claims, 10-30 RDMAP objects for a typical methods paper)
- **Cross-references**: Are your objects well-connected?
- **Provenance**: Does every object have verbatim_quote and location?
- **Consolidation**: Did Pass 2 reduce items by 15-20%?

---

## Example Metrics

### Sobotkova Complete Extraction (v2.5)

**After Claims/Evidence Passes:**
- Evidence: 42 objects
- Claims: 38 objects
- Implicit Arguments: 12 objects
- Cross-references: ~150 relationships

**After RDMAP Passes:**
- Research Designs: 8 objects
- Methods: 18 objects
- Protocols: 14 objects
- Additional cross-references: ~80 relationships

**Total:**
- 132 objects
- 230+ cross-references
- 100% validation passing
- Extraction time: ~4-5 hours (full paper, all 5 passes)

**Quality Indicators:**
- Precision: ~85% (objects correctly classified)
- Recall: ~80% (vs. hand-coding benchmark)
- Boundary accuracy: ~75% (evidence/claim distinctions)
- Cross-reference integrity: 100% (bidirectional consistency)

---

## Additional Examples

More examples from diverse domains will be added as testing expands:

**Planned:**
- Ecological field study
- Ethnographic research
- Geological field mapping
- Archaeological excavation report

**Want to contribute your extraction?** See [docs/skill-documentation/CONTRIBUTING.md](../docs/skill-documentation/CONTRIBUTING.md)

---

## Test Outputs Archive

Earlier test outputs and iterations are archived in [archive/outputs/](../archive/outputs/):

- **before-skill/** - Early extraction attempts (pre-v2.0)
- **with-skill/** - Iterative development extractions (v2.0-v2.4)

These show the evolution of the extraction system but are superseded by the curated examples here.

---

## Example File Structure

All extraction files follow this structure:

```json
{
  "schema_version": "2.5",
  "extraction_timestamp": "ISO 8601",
  "extractor": "string",
  "paper_metadata": { ... },
  "evidence": [ ... ],
  "claims": [ ... ],
  "implicit_arguments": [ ... ],
  "research_designs": [ ... ],
  "methods": [ ... ],
  "protocols": [ ... ],
  "extraction_notes": { ... }
}
```

See [docs/user-guide/schema-reference.md](../docs/user-guide/schema-reference.md) for complete schema documentation.

---

## Troubleshooting

### "The example is very large, hard to navigate"

Use a JSON viewer/editor with collapsing:
- VS Code with JSON extension
- Online: jsonviewer.stack.hu
- Command line: `jq` for filtering

### "My extraction looks different from the example"

That's OK! Different papers will have different patterns:
- Methods-heavy papers: More RDMAP objects
- Results-heavy papers: More evidence and claims
- Theoretical papers: More implicit arguments

### "How do I know if my extraction is good enough?"

Run Pass 3 validation and check:
- Zero CRITICAL issues
- Few IMPORTANT issues (< 5)
- Cross-reference integrity passing
- Expected information reasonably complete

---

## Related Documentation

- [Getting Started](../docs/user-guide/getting-started.md) - First extraction guide
- [Extraction Workflow](../docs/user-guide/extraction-workflow.md) - 5-pass process
- [Schema Reference](../docs/user-guide/schema-reference.md) - Object type definitions
- [Skill Usage Guide](../docs/skill-documentation/USAGE_GUIDE.md) - Detailed usage

---

**Ready to extract!** Copy the blank template and start with [docs/user-guide/getting-started.md](../docs/user-guide/getting-started.md).
