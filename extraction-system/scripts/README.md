# Extraction System Scripts

Production utilities for PDF processing, validation, and extraction workflow management.

**Version:** 2.6
**Last Updated:** 2025-11-14

---

## Overview

This directory contains reusable production scripts for the extraction workflow. These tools support PDF preprocessing, schema validation, reference integrity checking, and extraction quality assessment.

**Key principle:** These scripts are **workflow infrastructure**, not per-paper code. For transparency, paper-specific working scripts generated during extraction sessions are preserved in `outputs/{paper-name}/` directories.

---

## Quick Reference

| Script | Purpose | When to Use |
|--------|---------|-------------|
| `validate_extraction.py` | Schema compliance + reference integrity | After any pass, before commits |
| `validate_bidirectional.py` | Bidirectional relationship verification | After Pass 1, 2, 3, 5 (mapping-heavy) |
| `check_rdmap_completeness.py` | RDMAP tier coverage validation | After Pass 3, 4, 5 (RDMAP extraction) |
| `migrate_field_names.py` | Schema migration across versions | During schema updates (v2.5→v2.6) |
| `pdf_processing/extract_pdf_text.py` | PDF → markdown conversion | Before starting extraction (Pass 0) |
| `pdf_processing/pdf_cleaner.py` | PDF text cleaning utilities | Imported by extract_pdf_text.py |
| `extraction/section_rdmap_template.py` | RDMAP extraction template generator | Planning section-level RDMAP extraction |
| `extraction/consolidation_template.py` | Consolidation script template | Planning Pass 2 or Pass 5 consolidation |
| `extraction/section_implicit_arguments_template.py` | Implicit argument extraction template | Planning Pass 1 implicit argument extraction |

---

## Validation Scripts

### validate_extraction.py

**Purpose:** Comprehensive JSON schema validation and reference integrity checking

**Usage:**
```bash
python3 extraction-system/scripts/validate_extraction.py <extraction.json>

# Example
python3 extraction-system/scripts/validate_extraction.py outputs/paper-name/extraction.json
```

**Validation Checks:**
1. **JSON Schema compliance** - Validates against `extraction-system/schema/extraction_schema.json`
   - Required fields present
   - Correct data types
   - `uniqueItems` constraints
   - Minimum value constraints (e.g., page ≥ 1)

2. **Unique ID verification** - Checks for duplicate IDs within arrays
   - Evidence IDs (E001, E002, etc.)
   - Claim IDs (C001, C002, etc.)
   - Method IDs (M001, M002, etc.)
   - Protocol IDs (P001, P002, etc.)
   - Research Design IDs (RD001, RD002, etc.)

3. **Reference integrity** - Validates all cross-references exist
   - Claim→Evidence: `claims.supported_by` references exist in `evidence` array
   - Evidence→Claim: `evidence.supports_claims` references exist in `claims` array
   - Method→Design: `methods.implements_designs` references exist in `research_designs`
   - Protocol→Method: `protocols.implements_methods` references exist in `methods`

4. **Page number validity** - Ensures page numbers are ≥1 or null (not -1 placeholders)

**Exit Codes:**
- `0` - All validation passed
- `1` - Validation errors found

**Output:**
```text
Validating extraction against schema: outputs/paper-name/extraction.json
================================================================================
Checking JSON Schema compliance...
Checking for duplicate IDs...
Checking page number validity...
Checking reference integrity...

================================================================================
VALIDATION RESULTS
================================================================================

Item counts:
  Evidence: 52
  Claims: 34
  Methods: 15
  Protocols: 8
  Research Designs: 6

Total errors found: 0
  Schema violations: 0
  Reference errors: 0
  Duplicate IDs: 0
  Invalid pages: 0

✅ All validation checks passed!
```

**Dependencies:**
- `jsonschema` - Install with `pip install jsonschema`

**When to Use:**
- After completing any extraction pass
- Before committing changes to git
- After manual edits to extraction.json
- As part of QA workflow (see `extraction-system/qa-checks.sh`)

---

### validate_bidirectional.py

**Purpose:** Validate and auto-correct bidirectional relationship consistency

**Usage:**
```bash
python3 extraction-system/scripts/validate_bidirectional.py <extraction.json>

# Example
python3 extraction-system/scripts/validate_bidirectional.py outputs/paper-name/extraction.json
```

**Validation Checks:**

1. **Claim↔Evidence bidirectionality**
   - If `C001` in `E005.supports_claims`, verify `E005` in `C001.supported_by`
   - Auto-corrects missing reverse mappings

2. **Method↔Design bidirectionality**
   - If `M001` in `RD001.implemented_by_methods`, verify `RD001` in `M001.implements_designs`
   - Auto-corrects missing reverse mappings

3. **Protocol↔Method bidirectionality**
   - If `P001` in `M001.realized_through_protocols`, verify `M001` in `P001.implements_methods`
   - Auto-corrects missing reverse mappings

**Auto-Correction Behaviour:**
- Builds missing reverse mappings from forward direction
- Preserves existing correct mappings
- Flags conflicts (forward contradicts reverse) for human review
- Creates backup before modifying file

**Output:**
```text
Validating bidirectional consistency: outputs/paper-name/extraction.json
================================================================================
Checking claim↔evidence mappings...
Checking method↔design mappings...
Checking protocol↔method mappings...

Corrections made:
  ✓ Added E012 to C005.supported_by (was in E012.supports_claims)
  ✓ Added RD002 to M003.implements_designs (was in RD002.implemented_by_methods)

Total corrections: 2
Conflicts requiring review: 0

✅ Bidirectional consistency validated (2 corrections applied)
```

**Exit Codes:**
- `0` - No conflicts found (corrections applied if needed)
- `1` - Conflicts detected requiring human review

**When to Use:**
- After Pass 1 (Claims/Evidence extraction - high mapping volume)
- After Pass 2 (Claims/Evidence consolidation - IDs change)
- After Pass 3 (RDMAP extraction - design/method linkages)
- After Pass 5 (RDMAP consolidation - RDMAP IDs change)
- Whenever you manually edit cross-reference arrays

**Why This Matters:**
RUN-07 identified 88+ bidirectional inconsistencies. This validator prevents assessment errors caused by incomplete relationship mappings.

---

### check_rdmap_completeness.py

**Purpose:** Validate RDMAP extraction completeness and hierarchy integrity

**Usage:**
```bash
python3 extraction-system/scripts/check_rdmap_completeness.py <extraction.json>

# Example
python3 extraction-system/scripts/check_rdmap_completeness.py outputs/paper-name/extraction.json
```

**Validation Checks:**

1. **Tier coverage** - All three RDMAP tiers present
   - Research Designs (strategic tier) - Expected: ≥1
   - Methods (tactical tier) - Expected: ≥1
   - Protocols (operational tier) - Expected: ≥0 (methodological papers may lack protocols)

2. **Orphaned items** - Items disconnected from hierarchy
   - Methods without linked Designs
   - Protocols without linked Methods

3. **Hierarchy completeness** - Chain integrity
   - Design → Method → Protocol chains complete
   - No broken references

4. **Protocol linkage rate** - Operational detail coverage
   - Expected: ≥80% of Protocols linked to Methods
   - Low linkage suggests missed relationships

**Output:**
```text
Checking RDMAP completeness: outputs/paper-name/extraction.json
================================================================================
Tier coverage:
  Research Designs: 6
  Methods: 15
  Protocols: 8

Orphaned items:
  Methods without designs: 0
  Protocols without methods: 1 (P008)

Protocol linkage rate: 87.5% (7/8 linked)

⚠️  1 warning found:
  Protocol P008 not linked to any method

Recommendations:
  - Review P008 context - should it link to an existing method?
  - Check if P008 is actually a method-level item (tier misclassification)
```

**Exit Codes:**
- `0` - No critical issues (warnings allowed)
- `1` - Critical issues found (missing tiers, high orphan rate)

**When to Use:**
- After Pass 3 (explicit RDMAP extraction)
- After Pass 4 (implicit RDMAP extraction)
- After Pass 5 (RDMAP rationalization and tier verification)
- Before declaring RDMAP extraction complete

**Thresholds:**
- **Critical:** Missing tier entirely (0 Designs or 0 Methods)
- **Warning:** >20% orphaned Methods or Protocols
- **Warning:** <60% Protocol linkage rate

---

## PDF Processing Scripts

### pdf_processing/extract_pdf_text.py

**Purpose:** Convert academic PDFs to processed markdown optimised for LLM analysis

**Usage:**
```bash
python3 extraction-system/scripts/pdf_processing/extract_pdf_text.py input.pdf -o output.md

# With custom config
python3 extraction-system/scripts/pdf_processing/extract_pdf_text.py input.pdf --config config.yaml
```

**Features:**
1. **Text extraction** - Uses PyMuPDF and pdfplumber for robust text extraction
2. **Header/footer removal** - Filters text blocks in top 8% and bottom 8% of pages
3. **Section detection** - Identifies section headings and formats as markdown
4. **Table extraction** - Attempts to preserve table structure
5. **Abstract extraction** - Identifies and separates abstract section
6. **Reference cleaning** - Special handling for reference sections
7. **Hyphenation fixing** - Repairs word breaks across lines

**Input:**
- PDF files (academic papers)

**Output:**
- Markdown file with:
  - Document metadata (title, authors, pages, word count)
  - Section structure (## headings)
  - Clean paragraph breaks
  - Preserved tables (where possible)

**Configuration Options:**
```yaml
remove_headers_footers: true
header_threshold: 0.08  # Top 8% of page
footer_threshold: 0.92  # Bottom 8% of page
detect_sections: true
extract_tables: true
extract_abstract: true
aggressive_cleaning: false
include_metadata: true
```

**Dependencies:**
- `PyMuPDF` (fitz) - PDF text extraction
- `pdfplumber` - Table extraction
- `python-slugify` - Filename generation

Install with:
```bash
pip install PyMuPDF pdfplumber python-slugify
```

**When to Use:**
- Before starting Pass 0 (metadata extraction)
- When adding new papers to extraction queue
- Converting papers from PDF-only sources

**Quality Notes:**
- Works best with text-based PDFs (not scanned images)
- May struggle with complex multi-column layouts
- Tables may require manual post-processing
- Check output before starting extraction

---

### pdf_processing/pdf_cleaner.py

**Purpose:** Text cleaning utility functions for PDF extraction

**Type:** Utility library (not standalone script)

**Usage:**
```python
from pdf_cleaner import (
    clean_extracted_text,
    detect_section_heading,
    format_as_markdown_heading,
    extract_abstract,
    remove_headers_footers,
    clean_reference_section
)
```

**Functions:**
- `remove_hyphenation(text)` - Fix line-break hyphenation ("archaeo-\nlogy" → "archaeology")
- `remove_page_numbers(text)` - Strip standalone page numbers
- `clean_whitespace(text)` - Normalise spacing while preserving paragraph breaks
- `remove_headers_footers(blocks, page_height)` - Filter header/footer text blocks
- `detect_section_heading(text)` - Identify section headings by pattern
- `format_as_markdown_heading(text, level)` - Convert to markdown heading
- `extract_abstract(text)` - Locate and extract abstract section
- `clean_reference_section(text)` - Special handling for bibliographies

**Design:**
- Modular functions for pipeline composition
- Conservative cleaning (preserve > delete)
- Optimised for academic paper patterns
- Type hints and comprehensive docstrings

**Imported By:**
- `extract_pdf_text.py` (main PDF extractor)

---

## Migration and Maintenance Scripts

### migrate_field_names.py

**Purpose:** Standardise field names across extractions to canonical schema v2.6 names

**Usage:**
```bash
# Audit mode (read-only, report variants)
python3 extraction-system/scripts/migrate_field_names.py --audit

# Test single extraction (show diff, no write)
python3 extraction-system/scripts/migrate_field_names.py --dry-run paper-name

# Migrate single extraction
python3 extraction-system/scripts/migrate_field_names.py --migrate paper-name

# Batch migrate all extractions
python3 extraction-system/scripts/migrate_field_names.py --migrate-all
```

**Field Migrations (v2.5 → v2.6):**

| Object Type | Old Field | Canonical Field |
|-------------|-----------|-----------------|
| research_designs | `child_methods` | `implemented_by_methods` |
| research_designs | `enables_methods` | `implemented_by_methods` |
| research_designs | `supported_by_methods` | `implemented_by_methods` |
| methods | `linked_designs` | `implements_designs` |
| methods | `design_context` | `implements_designs` |
| methods | `child_protocols` | `realized_through_protocols` |
| methods | `implemented_by_protocols` | `realized_through_protocols` |
| protocols | `implements_method` | `implements_methods` |
| protocols | `linked_methods` | `implements_methods` |
| claims | `supported_by_evidence` | `supported_by` |
| claims | `supporting_evidence` | `supported_by` |

**Safety Features:**
- Creates timestamped backup before migration
- Dry-run mode shows changes without writing
- Audit mode reports variants without modifying files
- Preserves all other fields unchanged

**Output (Audit Mode):**
```text
Auditing field name variants across all extractions...
================================================================================

research_designs field variants:
  Paper: sobotkova-et-al-2023
    - RD001 uses 'child_methods' → should be 'implemented_by_methods'
    - RD002 uses 'enables_methods' → should be 'implemented_by_methods'

methods field variants:
  Paper: sobotkova-et-al-2024
    - M003 uses 'linked_designs' → should be 'implements_designs'

Total variants found: 3 across 2 papers
```

**When to Use:**
- After schema version updates (e.g., v2.5 → v2.6)
- Before batch validation runs
- When standardising legacy extractions
- After discovering field name inconsistencies

---

## Template Generators

These scripts provide **code templates** demonstrating best practices for extraction workflows. They are **not executable utilities** but **pedagogical examples** for creating paper-specific extraction scripts.

### extraction/section_rdmap_template.py

**Purpose:** Template demonstrating section-by-section RDMAP extraction

**Type:** Code template (copy and adapt for specific papers)

**Demonstrates:**
1. **Explicit RDMAP extraction** - Documented procedures with verbatim quotes
2. **Implicit RDMAP extraction** - Mentioned procedures without detail
3. **Recognition patterns** for implicit RDMAP:
   - Verbs without procedures ("cleaned", "validated", "checked")
   - Effects implying causes ("performance degraded" → monitoring protocol)
   - Mentions without descriptions ("assigned maps" → assignment protocol)

**Key Principle:**
Each section extraction must capture BOTH explicit and implicit RDMAP. Common failure mode: only extracting explicit items, missing implicit ones.

**Usage:**
1. Copy template to `outputs/paper-name/passN_rdmap_extraction.py`
2. Adapt examples to paper-specific content
3. Run to populate extraction.json

**When to Use:**
- Planning Pass 3 (explicit RDMAP extraction)
- Planning Pass 4 (implicit RDMAP scanning)
- Learning RDMAP recognition patterns

---

### extraction/consolidation_template.py

**Purpose:** Template for consolidation workflows with cross-reference repair

**Type:** Code template (copy and adapt for specific papers)

**Demonstrates:**
1. **Consolidation metadata tracking** - Recording consolidated_from IDs
2. **Cross-reference repair** - Building ID maps and updating references
3. **Safe consolidation workflow**:
   - Perform all consolidations first
   - Build consolidation map (old_id → new_id)
   - Repair all cross-references
   - Validate no broken references remain
   - Write updated JSON

**Key Principle:**
Consolidation creates broken cross-references unless you repair them. This template prevents the common failure mode where consolidation leaves orphaned ID references.

**Usage:**
1. Copy template to `outputs/paper-name/passN_consolidation.py`
2. Adapt consolidation logic to paper-specific patterns
3. Run to consolidate and repair references

**When to Use:**
- Planning Pass 2 (Claims/Evidence consolidation)
- Planning Pass 5 (RDMAP rationalization)
- Learning safe consolidation patterns

---

### extraction/section_implicit_arguments_template.py

**Purpose:** Template for systematic implicit argument extraction

**Type:** Code template (copy and adapt for specific papers)

**Demonstrates:**
1. **4-type systematic scan** for each core claim:
   - Type 1: Logical Implications
   - Type 2: Unstated Assumptions
   - Type 3: Bridging Claims
   - Type 4: Disciplinary Assumptions

2. **Recognition patterns**:
   - Pattern 1: Undefended quality judgments ("data quality was high")
   - Pattern 2: Comparison without baseline ("faster than traditional methods")
   - Pattern 3: Capability assumptions ("volunteers can identify features")
   - Pattern 4: Inferential leaps ("therefore reproducible")
   - Pattern 5: Definitional assumptions ("high accuracy" threshold undefined)
   - Pattern 6: Causal assumptions (correlation implied as causation)

3. **Required fields** for implicit arguments:
   - `trigger_text` - Verbatim passages from paper
   - `trigger_locations` - Where each trigger found
   - `inference_reasoning` - How triggers imply the implicit argument
   - `implicit_metadata` - Basis, confidence, assessment implications

**Key Principle:**
Each core claim requires systematic 4-type scan. Common failure mode: only extracting Type 1 (logical implications), missing Types 2-4 which are often more assessment-critical.

**Usage:**
1. Copy template to `outputs/paper-name/pass1_implicit_arguments.py`
2. Identify core claims requiring implicit argument scan
3. Adapt examples to paper-specific arguments
4. Run to populate extraction.json

**When to Use:**
- Planning Pass 1 (Claims/Evidence liberal extraction)
- Learning implicit argument recognition
- Understanding assessment implications

---

## Batch Analysis Tools

### Top-level: batch-assess.py

**Location:** `/home/shawn/Code/llm-reproducibility/batch-assess.py`

**Purpose:** Rapid quality assessment across multiple extractions

**Usage:**
```bash
python3 batch-assess.py
```

**Metrics Analysed:**
1. **Item counts** - Evidence, Claims, Methods, Protocols, Research Designs
2. **Claims-to-evidence ratio** - Expected: 0.4-0.8 (sparse to dense)
3. **Total RDMAP items** - Expected: 15-35 (depending on paper complexity)
4. **Relationship mappings** - Claim-evidence, method-design, protocol-method

**Output:**
```text
================================================================================================================
Paper                          Total    Ev     Cl     Me     Pr     RD     C:E      Maps
================================================================================================================
sobotkova-et-al-2023          159      52     34     15     8      6      0.65     234
sobotkova-et-al-2024          183      61     38     17     9      7      0.62     267
ross-ballsun-stanton-2022     142      48     31     12     6      5      0.65     198
================================================================================================================

Detailed metrics saved to: outputs/batch-assessment-metrics.json
```

**JSON Output:**
```json
[
  {
    "paper_id": "sobotkova-et-al-2023",
    "total_items": 159,
    "counts": {
      "evidence": 52,
      "claims": 34,
      "methods": 15,
      "protocols": 8,
      "research_designs": 6
    },
    "claims_to_evidence_ratio": 0.65,
    "rdmap_items": 29,
    "total_mappings": 234,
    "mappings": {
      "claim_evidence": 187,
      "method_design": 32,
      "protocol_method": 15
    }
  }
]
```

**Use Cases:**
- Quality comparison across extractions
- Identifying outlier extractions (too sparse/dense)
- Schema migration verification (field name changes)
- Batch validation before releases
- Tracking extraction quality trends over time

**When to Use:**
- After completing a batch of extractions
- Before major releases or milestones
- When assessing corpus-level quality
- Preparing for FAIR vocabularies development (needs 20+ papers)

---

## QA Workflow Integration

Scripts integrate with `extraction-system/qa-checks.sh` for comprehensive validation:

```bash
./extraction-system/qa-checks.sh outputs/paper-name/extraction.json
```

QA script runs:
1. `validate_extraction.py` - Schema compliance
2. `validate_bidirectional.py` - Relationship consistency
3. `check_rdmap_completeness.py` - RDMAP coverage

Exit code `0` only if all three pass.

---

## Dependencies

### Required (for validation)
```bash
pip install jsonschema
```

### Optional (for PDF processing)
```bash
pip install PyMuPDF pdfplumber python-slugify pyyaml
```

### Complete installation
```bash
pip install -r requirements.txt
```

---

## Troubleshooting

### Common Issues

**Issue:** `ModuleNotFoundError: No module named 'jsonschema'`
**Solution:** Install validation dependencies: `pip install jsonschema`

**Issue:** Validation fails with "Reference error: claim C001 references non-existent evidence 'E005'"
**Solution:** Run `validate_bidirectional.py` to auto-repair or manually check consolidation metadata

**Issue:** RDMAP completeness shows 0 Protocols
**Solution:** Methodological papers may legitimately have no protocols. Check if paper describes operational procedures.

**Issue:** PDF extraction produces garbled text
**Solution:** PDF may be scanned image. Use OCR preprocessing or manual transcription.

**Issue:** Migration script shows "Backup already exists"
**Solution:** Previous migration created backup. Safe to proceed (or delete old backups if confident).

---

## Development Guidelines

### Adding New Scripts

1. **Header block required** (per style guide):
   ```python
   #!/usr/bin/env python3
   """
   Script Name - One-line purpose

   Detailed description of what this script does, when to use it,
   and how it fits into the overall extraction workflow.

   Usage:
       python3 script_name.py <arguments>

   Input:
       - extraction.json (current state)
       - [other inputs]

   Output:
       - extraction.json (updated)
       - [other outputs]

   Author: [name]
   Date: [YYYY-MM-DD]
   """
   ```

2. **Function docstrings required** (with parameters and return values)
3. **Type hints encouraged** (for function signatures)
4. **Inline comments** for non-obvious logic
5. **Error handling** with informative messages

### Script Categories

**Validation scripts:** Read-only, report errors, exit codes for CI/CD
**Migration scripts:** Backup-first, dry-run mode, batch support
**Template scripts:** Pedagogical examples, copy-and-adapt pattern
**Batch tools:** Multi-paper analysis, comparative metrics

---

## Contributing

See [CONTRIBUTING.md](../../CONTRIBUTING.md) for contribution guidelines.

**Priority areas:**
- Additional validation checks (e.g., implicit argument quality)
- PDF extraction improvements (table handling, multi-column)
- Batch migration tools (schema v2.6 → v2.7)
- Quality metric expansions (relationship density, provenance coverage)

---

## Related Documentation

- **Extraction System Overview:** [extraction-system/README.md](../README.md)
- **Schema Reference:** [docs/user-guide/schema-reference.md](../../docs/user-guide/schema-reference.md)
- **Validation Workflow:** [docs/user-guide/extraction-workflow.md](../../docs/user-guide/extraction-workflow.md)
- **Research Assessor Guide:** [docs/research-assessor-guide/](../../docs/research-assessor-guide/)

---

**Version:** 2.6
**Last Updated:** 2025-11-14
**Maintained by:** LLM Reproducibility Project
