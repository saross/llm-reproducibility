# Extraction Outputs

This directory contains extraction results from the 7-pass workflow. Each paper gets its own subdirectory with structured JSON output and analysis files.

---

## Directory Structure

```
outputs/
├── paper-slug/              # One directory per paper
│   ├── extraction.json      # Primary extraction output (schema v2.6)
│   ├── paper-slug.txt       # Extracted paper text
│   ├── full_text.txt        # Alternative text format
│   ├── assessment/          # Assessment results (future)
│   ├── validation_results.json
│   └── extraction-summary.md
├── batch-analysis/          # Cross-paper analyses
│   └── README.md
└── batch-assessment-metrics.json
```

---

## Per-Paper Directory Contents

Each paper directory (`paper-slug/`) contains:

### Primary Files

**extraction.json** (Required)
- Complete structured extraction in JSON format
- Schema v2.6 with all object types
- Includes: evidence, claims, implicit_arguments, research_designs, methods, protocols, reproducibility_infrastructure
- Complete provenance tracking and relationships

**paper-slug.txt** (Required)
- Extracted paper text in markdown format
- Used as input for extraction workflow
- Preserves structure (sections, headings)

### Analysis Files

**extraction-summary.md** (Optional)
- Human-readable summary of extraction
- Item counts by type
- Key findings and patterns
- Validation results

**validation_results.json** (Optional)
- Output from validation pass
- Structural integrity checks
- Relationship verification
- Completeness assessment

**section_division.md** (Optional)
- Paper structure analysis
- Section boundaries for multi-section extraction
- Planning document

### Assessment Subdirectory

**assessment/** (Future)
- Will contain credibility assessment results
- Signal scores (comprehensibility, transparency, etc.)
- Comparative metrics
- Not yet implemented

### Backup Files

**extraction.backup-YYYYMMDD-HHMMSS.json**
- Automatic backups created during migrations
- Preserved for safety during schema updates
- Can be deleted once migration verified

### Workflow Scripts

**pass N_*.py** (Optional)
- Python scripts used during extraction
- Documented workflow for reproducibility
- Can be archived after extraction complete

---

## Understanding extraction.json

### Top-Level Structure

```json
{
  "paper_metadata": {},
  "evidence": [],
  "claims": [],
  "implicit_arguments": [],
  "research_designs": [],
  "methods": [],
  "protocols": [],
  "reproducibility_infrastructure": {},
  "extraction_notes": {},
  "extraction_timestamp": ""
}
```

### Object Counts (Typical)

After rationalization, expect:

| Object Type | Typical Range | Purpose |
|-------------|--------------|---------|
| Evidence | 40-60 items | Raw observations, data points, measurements |
| Claims | 25-40 items | Interpretations, assertions, conclusions |
| Implicit arguments | 10-20 items | Unstated assumptions, logical implications |
| Research designs | 4-8 items | Strategic framing (WHY) |
| Methods | 10-20 items | Tactical approaches (WHAT) |
| Protocols | 5-15 items | Operational procedures (HOW) |
| Infrastructure | 1 object | PIDs, FAIR, funding, permits |

Counts vary by paper length, domain, and complexity.

### Relationships

extraction.json includes bidirectional relationships:

- Claims → Evidence (supports_claims / supported_by_evidence)
- Methods → Designs (implements_designs / implemented_by_methods)
- Protocols → Methods (implements_methods / realized_through_protocols)
- Evidence ↔ Claims (supports_claims / supported_by_evidence)

Typical extraction includes 150-250 relationship mappings.

---

## Using Extraction Outputs

### Viewing Results

**Quick overview:**
```bash
jq '{
  evidence: (.evidence | length),
  claims: (.claims | length),
  methods: (.methods | length),
  designs: (.research_designs | length)
}' outputs/paper-name/extraction.json
```

**List all claims:**
```bash
jq '.claims[] | {id, brief_description}' outputs/paper-name/extraction.json
```

**Check FAIR scores:**
```bash
jq '.reproducibility_infrastructure.fair_assessment' outputs/paper-name/extraction.json
```

### Validation

**Run all checks:**
```bash
./extraction-system/qa-checks.sh outputs/paper-name/extraction.json
```

**Individual validators:**
```bash
# Schema compliance
python extraction-system/scripts/validate_extraction.py outputs/paper-name/extraction.json

# Relationship integrity
python extraction-system/scripts/validate_bidirectional.py outputs/paper-name/extraction.json

# RDMAP completeness
python extraction-system/scripts/check_rdmap_completeness.py outputs/paper-name/extraction.json
```

### Analysis

See [batch-analysis/README.md](batch-analysis/README.md) for cross-paper analysis tools.

---

## Schema Version

All extraction outputs use **schema v2.6** (Nov 2025).

**Key features:**
- 7-pass workflow support (Pass 0-6 plus validation)
- Infrastructure assessment
- FAIR scoring framework
- Bidirectional relationships
- Complete provenance tracking

See [extraction-system/schema/README.md](../extraction-system/schema/README.md) for detailed schema documentation.

---

## Quality Metrics

### Structural Integrity

Validated extractions should achieve:

- ✅ 100% schema compliance
- ✅ 100% bidirectional relationship consistency
- ✅ 100% RDMAP tier verification (designs → methods → protocols)
- ✅ 80%+ evidence-claim relationship coverage
- ✅ All required fields populated

### Content Quality

Assessed extractions typically achieve:

- **Precision**: 85-95% (items correctly classified)
- **Recall**: 75-90% (items captured vs. hand-coding)
- **Granularity**: Consistent within paper, variable across papers
- **Provenance**: 100% (all items have verbatim quotes)

---

## Batch Analysis

The `batch-analysis/` directory contains cross-paper analyses:

- Extraction metrics comparison
- Schema field usage statistics
- RDMAP pattern analysis
- FAIR score distributions
- Quality assessment summaries

See [batch-analysis/README.md](batch-analysis/README.md) for details.

---

## Paper Naming Convention

Paper directories use lowercase slugs with hyphens:

**Format:** `author-et-al-YYYY`

**Examples:**
- `sobotkova-et-al-2024`
- `penske-et-al-2023`
- `ross-ballsun-stanton-2022` (multiple surnames, all included)

**Single author:** `lastname-YYYY`

---

## Adding New Extractions

To extract a new paper:

1. Convert PDF to markdown (if needed):
   ```bash
   python extraction-system/scripts/pdf_processing/extract_pdf_text.py "paper.pdf"
   ```

2. Add to queue:
   ```bash
   # Edit input/queue.yaml
   ```

3. Run extraction workflow:
   - Follow [input/workflow.md](../input/workflow.md)
   - Or see [docs/user-guide/extraction-workflow.md](../docs/user-guide/extraction-workflow.md)

4. Validate output:
   ```bash
   ./extraction-system/qa-checks.sh outputs/paper-name/extraction.json
   ```

---

## Troubleshooting

**Common issues:**

1. **Missing extraction.json**: Extraction incomplete or failed
   - Check queue.yaml status
   - Review extraction logs
   - Restart from last successful pass

2. **Validation errors**: Run individual validators to identify specific issues
   - Schema errors: `validate_extraction.py`
   - Relationship errors: `validate_bidirectional.py`
   - RDMAP gaps: `check_rdmap_completeness.py`

3. **Large file sizes**: extraction.json > 1MB unusual
   - Check for over-extraction (too many items)
   - Verify granularity (items too detailed?)
   - Consider rationalization pass

4. **Missing relationships**: Low relationship coverage
   - Re-run Pass 2 (claims rationalization)
   - Re-run Pass 5 (RDMAP rationalization)
   - Check for relationship mapping errors

---

## Related Documentation

- **Extraction Workflow**: [docs/user-guide/extraction-workflow.md](../docs/user-guide/extraction-workflow.md)
- **Schema Reference**: [docs/user-guide/schema-reference.md](../docs/user-guide/schema-reference.md)
- **Validation Guide**: [extraction-system/scripts/README.md](../extraction-system/scripts/README.md)
- **Queue Management**: [input/README.md](../input/README.md)

---

**Version:** 2.6
**Schema:** v2.6 (Nov 2025)
**Last Updated:** November 2025
