# Extraction System

Complete toolkit for extracting structured knowledge representations from research papers using the research-assessor skill and Claude Code.

**Version:** 2.6 | **Workflow:** 8-pass (0-7) | **Schema:** v2.6
**Manifest:** See [../manifest.yaml](../manifest.yaml) for component versions

---

## Overview

The extraction system transforms unstructured research papers into structured JSON representations capturing:

- Claims, evidence, and implicit arguments
- Research designs, methods, and protocols
- Infrastructure elements (PIDs, FAIR assessment, funding, permits)
- Complete provenance and relationships

This enables systematic assessment of research transparency, replicability, and credibility.

---

## Directory Structure

```
extraction-system/
├── prompts/               # Eight extraction prompts (Pass 0-7)
│   ├── 00-metadata_pass0_prompt.md
│   ├── 01-claims-evidence_pass1_prompt.md
│   ├── 02-claims-evidence_pass2_prompt.md
│   ├── 03-rdmap_pass1a_explicit_prompt.md
│   ├── 04-rdmap_pass1b_implicit_prompt.md
│   ├── 05-rdmap_pass2_prompt.md
│   ├── 06-infrastructure_pass6_prompt.md
│   ├── 07-validation_prompt.md
│   └── readme.md
├── schema/                # JSON schema definitions
│   ├── extraction-schema-v2.5.json
│   ├── README.md
│   └── schema-validation.json
├── scripts/               # Utility scripts
│   ├── extraction/        # Extraction workflow scripts
│   ├── pdf_processing/    # PDF text extraction
│   ├── check_rdmap_completeness.py
│   ├── migrate_field_names.py
│   ├── validate_bidirectional.py
│   └── validate_extraction.py
├── staging/               # Temporary working files
├── templates/             # Extraction templates
├── extraction-plan-unified-model.md
└── qa-checks.sh
```

---

## How It Works

### 1. Input Preparation

Papers are converted to markdown format:

```bash
python scripts/pdf_processing/extract_pdf_text.py "paper.pdf"
# Output: input/sources/processed-md/paper.md
```

### 2. Eight-Pass Extraction

The extraction workflow processes each paper through eight sequential passes (0-7):

#### Pass 0: Metadata Extraction
- Extract publication metadata
- Map paper structure (sections, subsections)
- Identify key components

#### Passes 1-2: Claims and Evidence
- **Pass 1**: Liberal extraction of evidence, claims, implicit arguments
- **Pass 2**: Rationalization and consolidation (15-20% reduction)

#### Passes 3-5: Research Design, Methods, and Protocols (RDMAP)
- **Pass 3**: Liberal extraction of explicit RDMAP
- **Pass 4**: Implicit RDMAP extraction
- **Pass 5**: Rationalization and tier verification

#### Pass 6: Infrastructure
- Extract PIDs (DOI, ORCID, data/code DOIs)
- FAIR assessment (data and code)
- Funding information
- Permits and authorisations
- Ethics approvals

#### Pass 7: Validation
- Structural integrity checks
- Bidirectional relationship verification
- Schema compliance
- Completeness assessment

### 3. Quality Assurance

After extraction, run validation:

```bash
./extraction-system/qa-checks.sh "outputs/paper-name/extraction.json"
```

Or individual validators:

```bash
python extraction-system/scripts/validate_extraction.py extraction.json
python extraction-system/scripts/validate_bidirectional.py extraction.json
python extraction-system/scripts/check_rdmap_completeness.py extraction.json
```

---

## Key Files

### Prompts Directory

Contains prompts for each extraction pass. Each prompt is optimised for Claude Code and the research-assessor skill.

See [prompts/readme.md](prompts/readme.md) for detailed prompt documentation.

### Schema Directory

Contains JSON schema definitions (v2.6) and validation tools.

See [schema/README.md](schema/README.md) for schema documentation and versioning.

### Scripts Directory

Utility scripts for PDF processing, validation, and extraction management.

See [scripts/README.md](scripts/README.md) for script documentation.

### Extraction Plan

`extraction-plan-unified-model.md` provides flexible planning guidance for diverse paper types (empirical/methodological/short/long/multi-proxy).

---

## Usage

### Quick Start

1. Install research-assessor skill in Claude Code
2. Convert paper to markdown
3. Follow workflow in [input/workflow.md](../input/workflow.md)
4. Run validation after extraction

### Complete Guide

See [docs/user-guide/extraction-workflow.md](../docs/user-guide/extraction-workflow.md) for the complete extraction workflow guide.

---

## Schema Version

**Current:** v2.6 (Nov 2025)

Major features:
- Complete 8-pass workflow support (Pass 0-7)
- Infrastructure assessment capability (13 sections)
- FAIR assessment scoring (0-40)
- Bidirectional relationship tracking
- Canonical field names

See schema/README.md for version history and migration guides.

---

## Dependencies

**Required:**
- Claude Code with research-assessor skill
- Claude Sonnet 4.5+ (recommended)

**Optional:**
- Python 3.8+ (for scripts)
- PyMuPDF, pdfplumber (for PDF processing)
- PyYAML (for configuration)

```bash
pip install -r ../requirements.txt
```

---

## Quality Metrics

Typical extraction outputs (after rationalization):

- **Evidence**: 40-60 items
- **Claims**: 25-40 items
- **Implicit arguments**: 10-20 items
- **RDMAP**: 20-35 items
- **Infrastructure**: 1 comprehensive object
- **Relationships**: 150-250 mappings
- **Validation**: 100% structural integrity

Metrics vary by paper length, complexity, and domain.

---

## Troubleshooting

**Common issues:**

1. **Validation errors**: Run `./qa-checks.sh` to identify issues
2. **Missing relationships**: Use `validate_bidirectional.py` to fix
3. **Incomplete RDMAP**: Use `check_rdmap_completeness.py` to identify gaps
4. **PDF extraction issues**: See [docs/user-guide/pdf-extraction.md](../docs/user-guide/pdf-extraction.md)

---

## Contributing

Contributions welcome! Areas of focus:

- **Prompt refinement**: Improve extraction accuracy
- **Schema enhancements**: Propose new object types or fields
- **Validation tools**: Add new checks
- **Documentation**: Improve guides

See [../CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.

---

## Related Documentation

- **Workflow Entry Points** (in `input/`):
  - [input/workflow.md](../input/workflow.md) - Authoritative 8-pass workflow
  - [input/extraction-launch.md](../input/extraction-launch.md) - Quick-start primer
  - [input/queue.yaml](../input/queue.yaml) - Paper processing queue

- **Planning Guidance**:
  - [extraction-plan-unified-model.md](extraction-plan-unified-model.md) - Flexible planning for diverse paper types

- **User Guides**: [docs/user-guide/](../docs/user-guide/)
- **Skill Documentation**: [docs/research-assessor-guide/](../docs/research-assessor-guide/)
- **Schema Reference**: [docs/user-guide/schema-reference.md](../docs/user-guide/schema-reference.md)

---

**Version:** 2.6
**Last Updated:** November 2025
**Maintained by:** LLM Reproducibility Project
