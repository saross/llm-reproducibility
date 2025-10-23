# LLM-Based Research Extraction and Assessment

Automated extraction of claims, evidence, and methodology from research papers using Large Language Models, enabling systematic assessment of research transparency, replicability, and credibility.

**Version:** 2.5
**Status:** Extraction system complete and tested, assessment framework in development
**Target Domains:** Fieldwork-based research (archaeology, ecology, ethnography, field geology, etc.)

---

## Overview

This repository contains tools and workflows for:

1. **Extraction** (Complete): Systematically extract claims, evidence, implicit arguments, research designs, methods, and protocols from research papers
2. **Assessment** (In Development): Evaluate research transparency, replicability, and credibility based on extracted information

The extraction system uses a multi-pass workflow with Claude Sonnet 4.5+ to create structured JSON representations of research papers, enabling downstream analysis and quality assessment.

---

## Quick Start

### 1. Install the Extraction Skill

```bash
# Install the research-assessor skill in Claude
# File: extraction-system/skill/research-assessor-v2.5.zip
```

See [docs/skill-documentation/](docs/skill-documentation/) for detailed installation instructions.

### 2. Prepare Your Paper

```bash
# Extract text from PDF
python extraction-system/scripts/extract_pdf_text.py "your-paper.pdf"

# Output will be in: sources/processed-md/your-paper.md
```

See [docs/user-guide/pdf-extraction.md](docs/user-guide/pdf-extraction.md) for more details.

### 3. Run Extraction

Use the five-pass workflow:

1. **Claims/Evidence Pass 1**: Liberal extraction of evidence, claims, implicit arguments
2. **Claims/Evidence Pass 2**: Rationalization and consolidation
3. **RDMAP Pass 1**: Liberal extraction of research designs, methods, protocols
4. **RDMAP Pass 2**: Rationalization and tier verification
5. **Pass 3 Validation**: Structural integrity checks

See [docs/user-guide/extraction-workflow.md](docs/user-guide/extraction-workflow.md) for complete workflow guide.

---

## Repository Structure

```
llm-reproducibility/
├── extraction-system/     # All extraction tools (skill, prompts, schema, scripts)
├── docs/                  # Documentation (user guides, skill docs, development)
├── examples/              # Curated extraction examples
├── planning/              # Active project planning (assessment phase upcoming)
├── reports/               # Key testing and QA reports
├── sources/               # Source papers (PDFs and processed markdown)
├── archive/               # Development history organized by version
├── LICENSE-CODE           # Apache 2.0 (code)
├── LICENSE-DOCS           # CC-BY-4.0 International (documentation)
└── CITATION.cff           # Machine-readable citation
```

### Key Directories

- **[extraction-system/](extraction-system/)** - Complete extraction toolkit
  - `skill/` - Research Assessor Claude skill (v2.5)
  - `prompts/` - Five extraction prompts (Claims Pass 1/2, RDMAP Pass 1/2/3, QA/QI)
  - `schema/` - JSON schema for extraction output
  - `scripts/` - PDF text extraction utilities

- **[docs/](docs/)** - All documentation
  - `user-guide/` - Getting started, workflow, schema reference
  - `skill-documentation/` - Comprehensive skill documentation
  - `development/` - Schema evolution, deployment guides
  - `background-research/` - Deep research reports

- **[planning/](planning/)** - Active planning documents
  - CWTS implementation plan (assessment phase)
  - Schema improvement roadmap
  - Strategic decisions

- **[examples/](examples/)** - Example extractions
  - Complete extraction from Sobotkova et al. (2023)
  - Blank template for new extractions

- **[archive/](archive/)** - Development history
  - Organized by version (v2.0-v2.1 → v2.5)
  - Planning, documentation, reports, test outputs

---

## Features

### Extraction System (v2.5)

**Six Object Types:**
- Evidence - Observations, measurements, data points
- Claims - Interpretations, assertions, generalizations
- Implicit Arguments - Unstated assumptions, logical implications
- Research Designs - Strategic framing and rationale (WHY)
- Methods - Tactical approaches (WHAT was done)
- Protocols - Operational procedures (HOW specifically)

**Multi-Pass Workflow:**
- Pass 1: Liberal extraction with over-capture (comprehensive coverage)
- Pass 2: Rationalization with consolidation (15-20% reduction)
- Pass 3: Validation ensuring structural integrity

**Provenance Tracking:**
- Every item linked to source text via verbatim quotes
- Location tracking (section, page, paragraph)
- Cross-references between all object types
- Complete consolidation metadata for traceability

**Fieldwork-Specific:**
- Respects abductive/inductive reasoning
- Tracks opportunistic decisions and adaptations
- Distinguishes planned vs. actual procedures
- Documents emergent discoveries

### Assessment Framework (In Development)

Planned assessment dimensions adapted from repliCATS:
- Comprehensibility
- Transparency
- Plausibility
- Evidential Adequacy
- Robustness
- Replicability
- Generalizability

See [planning/cwts_implementation_plan.md](planning/cwts_implementation_plan.md) for roadmap.

---

## Documentation

### User Guides
- [Getting Started](docs/user-guide/getting-started.md) - Installation and first extraction
- [Extraction Workflow](docs/user-guide/extraction-workflow.md) - Complete 5-pass workflow
- [PDF Extraction](docs/user-guide/pdf-extraction.md) - Preparing papers for analysis
- [Schema Reference](docs/user-guide/schema-reference.md) - Understanding the extraction schema

### Skill Documentation
- [README](docs/skill-documentation/README.md) - Skill overview
- [Architecture](docs/skill-documentation/ARCHITECTURE.md) - Design principles
- [Usage Guide](docs/skill-documentation/USAGE_GUIDE.md) - Detailed usage
- [Version History](docs/skill-documentation/VERSION.md) - Complete changelog

### Development
- [Schema Evolution](docs/development/schema-evolution.md) - Schema versioning and mappings
- [Deployment Guide](docs/development/deployment-guide-v2.5.md) - Skill deployment details

---

## Testing

Tested extensively on:
- Sobotkova et al. (2023) "Arbitrary Offline Data Capture on All of Your Androids: The FAIMS Mobile Platform" (archaeological survey methodology)

Quality metrics (v2.5):
- ~120 objects extracted after rationalization
- ~200+ cross-references mapped
- 85%+ precision in object classification
- 80%+ recall vs. hand-coding
- Complete validation passing

See [reports/extraction-testing/](reports/extraction-testing/) for detailed results.

---

## Dependencies

**Extraction System:**
- Claude AI with Skills support (Claude Sonnet 4.5+ recommended)
- Python 3.8+ for PDF extraction scripts

**PDF Processing:**
- PyMuPDF (fitz) - Text extraction
- pdfplumber - Table extraction
- PyYAML - Configuration
- python-slugify - Filename handling

```bash
pip install -r requirements.txt
```

---

## Project Status

### ✅ Completed (v2.5)
- Extraction system complete and validated
- Five-pass workflow tested and refined
- Schema v2.5 with complete object types
- PDF processing pipeline working
- Comprehensive documentation
- Repository organization and FAIR4RS preparation

### 🚧 In Progress
- Testing on additional papers from varied domains
- Expanding domain-specific vocabulary

### 📋 Planned (Next Phase)
- Assessment framework development (credibility scoring)
- Multi-paper batch processing
- Integration with archaeological data repositories
- FAIR4RS full compliance (DOI, Zenodo deposition)

---

## Contributing

We welcome contributions in several areas:

- **Domain expansion**: Adapt extraction to new fieldwork disciplines
- **Vocabulary development**: Refine controlled vocabularies empirically
- **Testing**: Run extractions on new papers, report issues
- **Examples**: Contribute worked extractions from other domains
- **Assessment**: Help develop credibility assessment rubrics

See [docs/skill-documentation/CONTRIBUTING.md](docs/skill-documentation/CONTRIBUTING.md) for guidelines.

---

## Citation

If you use this work in research, please cite:

```bibtex
@software{llm-reproducibility-v2.5,
  title = {LLM-Based Research Extraction and Assessment},
  author = {[Your Name]},
  version = {2.5},
  year = {2025},
  url = {https://github.com/[your-username]/llm-reproducibility}
}
```

See [CITATION.cff](CITATION.cff) for machine-readable citation.

---

## License

- **Code** (extraction system, scripts): [Apache License 2.0](LICENSE-CODE)
- **Documentation** (guides, prompts, schema): [CC-BY-4.0 International](LICENSE-DOCS)

---

## Acknowledgments

- Developed with Claude Sonnet 4.5 (Anthropic)
- Tested on archaeological research papers
- Informed by TIDieR, CONSORT-Outcomes, and SPIRIT frameworks
- Assessment framework adapted from repliCATS methodology
- Inspired by research transparency and replication initiatives

---

## Support

- **Documentation**: See [docs/](docs/) for comprehensive guides
- **Issues**: Report issues via GitHub Issues
- **Questions**: See [docs/user-guide/getting-started.md](docs/user-guide/getting-started.md)

---

## Development History

This project has evolved through multiple versions:

- **v2.0-2.1** (Oct 16, 2025): Initial claims/evidence extraction
- **v2.2-2.3** (Oct 17-18, 2025): Two-pass workflow with consolidation
- **v2.4** (Oct 19-20, 2025): RDMAP extraction framework added
- **v2.5** (Oct 23, 2025): Repository rationalization and FAIR4RS preparation

See [archive/README.md](archive/README.md) for complete development history.

---

**Ready to extract!** See [docs/user-guide/getting-started.md](docs/user-guide/getting-started.md) to begin.
