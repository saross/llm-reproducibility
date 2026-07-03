# LLM-Based Research Extraction and Assessment

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

Automated extraction of claims, evidence, and methodology from research papers using Large Language Models, enabling systematic assessment of research transparency, reproducibility, and credibility.

**Version:** 3.0.1 | **Schema:** v2.6 | **Workflow:** v5.0.0 (8-pass, session-per-pass)
**Status:** Extraction system complete, assessment framework pilot-tested, reproduction system v1.1
**Target Domains:** Fieldwork-based research (archaeology, ecology, ethnography, field geology, etc.)
**Manifest:** See [manifest.yaml](manifest.yaml) for component versions

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
# Install the research-assessor skill in Claude Code
# The skill is located at: .claude/skills/research-assessor/
```

See [docs/research-assessor-guide/installation.md](docs/research-assessor-guide/installation.md) for detailed installation instructions.

### 2. Prepare Your Paper

```bash
# Extract text from PDF
python extraction-system/scripts/extract_pdf_text.py "your-paper.pdf"

# Output will be in: sources/processed-md/your-paper.md
```

See [docs/user-guide/pdf-extraction.md](docs/user-guide/pdf-extraction.md) for more details.

### 3. Run Extraction

Use the eight-pass workflow (Pass 0-7):

0. **Metadata Pass**: Extract publication metadata and paper structure
1. **Claims/Evidence Pass 1**: Liberal extraction of evidence, claims, implicit arguments
2. **Claims/Evidence Pass 2**: Rationalisation and consolidation
3. **RDMAP Pass 1a**: Liberal extraction of research designs, methods, protocols
4. **RDMAP Pass 1b**: Implicit RDMAP extraction
5. **RDMAP Pass 2**: Rationalisation and tier verification
6. **Infrastructure Pass**: Extract PIDs, FAIR assessment, funding, permits
7. **Validation Pass**: Structural integrity checks

See [docs/user-guide/extraction-workflow.md](docs/user-guide/extraction-workflow.md) for complete workflow guide.

---

## Repository Structure

```text
llm-reproducibility/
├── input/                 # Workflow entry points (queue, launch prompt, workflow)
├── extraction-system/     # All extraction tools (skill, prompts, schema, scripts)
├── assessment-system/     # Assessment tools (pilot-tested)
├── reproduction-system/   # Docker-based reproduction workflow (prompts, templates)
├── docs/                  # User-facing documentation (guides, skill docs, background)
├── wiki/                  # Research process record (continuity, lab notebook, planning)
├── studies/               # Research studies using the pipeline (open-science-compliance)
├── examples/              # Curated extraction examples
├── outputs/               # Extraction outputs organised by paper
├── reports/               # Key testing and QA reports
├── archive/               # Development history organised by version
├── manifest.yaml          # Component version manifest (source of truth)
├── LICENSE-CODE           # Apache 2.0 (code)
├── LICENSE-DOCS           # CC-BY-4.0 International (documentation)
└── CITATION.cff           # Machine-readable citation
```

### Key Directories

- **[input/](input/)** - Workflow entry points
  - `workflow.md` - Authoritative 8-pass extraction workflow
  - `extraction-launch.md` - Quick-start primer for new extractions
  - `queue.yaml` - Paper processing queue with status tracking

- **[extraction-system/](extraction-system/)** - Complete extraction toolkit
  - `prompts/` - Eight extraction prompts (Pass 0-7)
  - `schema/` - JSON schema for extraction output (v2.6)
  - `scripts/` - PDF text extraction and validation utilities
  - `extraction-plan-unified-model.md` - Flexible planning guidance

- **[docs/](docs/)** - User-facing documentation: how to install and use the systems
  - `user-guide/` - Getting started, workflow, schema reference
  - `research-assessor-guide/` - Comprehensive skill documentation
  - `schema/` - Schema versioning and crosswalks
  - `background-research/` - Deep research reports

- **[wiki/](wiki/)** - Versioned research process record: how the research is being done
  - `continuity.md` - Cross-session state and session log
  - `working-notes.md` - Empirical lab notebook
  - `reflections/` - Meta-research observations
  - `planning/` - Implementation plans and roadmaps
  - Kept in-repo (not a GitHub Wiki) so the process record is versioned and
    archived with the code — see `wiki/index.md`

> **docs/ vs wiki/:** `docs/` documents the *product* (for users of the
> extraction/assessment/reproduction systems); `wiki/` documents the *process*
> (for provenance and project continuity). If you want to use the tools, start
> in `docs/`; if you want to see how this project works day to day, start in
> `wiki/`.

- **[examples/](examples/)** - Example extractions
  - Complete extraction samples with annotations
  - Blank templates for new extractions
  - Quick reference guides

- **[archive/](archive/)** - Development history
  - Organized by version (v2.0-v2.1 → v2.5)
  - Planning, documentation, reports, test outputs

---

## Features

### Extraction System (v2.6)

**Six Object Types:**
- Evidence - Observations, measurements, data points
- Claims - Interpretations, assertions, generalizations
- Implicit Arguments - Unstated assumptions, logical implications
- Research Designs - Strategic framing and rationale (WHY)
- Methods - Tactical approaches (WHAT was done)
- Protocols - Operational procedures (HOW specifically)

**Multi-Pass Workflow (8 passes, 0-7):**
- Pass 0: Metadata extraction
- Passes 1-2: Claims/Evidence (liberal extraction → rationalisation)
- Passes 3-5: RDMAP (liberal → implicit → rationalisation)
- Pass 6: Infrastructure (PIDs, FAIR, funding, permits)
- Pass 7: Validation ensuring structural integrity

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
- Reproducibility
- Generalisability

See [wiki/planning/credibility-implementation-plan-v2.0.md](wiki/planning/credibility-implementation-plan-v2.0.md) for roadmap.

---

## Documentation

### User Guides
- [Getting Started](docs/user-guide/getting-started.md) - Installation and first extraction
- [Extraction Workflow](docs/user-guide/extraction-workflow.md) - Complete 8-pass workflow (Pass 0-7)
- [PDF Extraction](docs/user-guide/pdf-extraction.md) - Preparing papers for analysis
- [Schema Reference](docs/user-guide/schema-reference.md) - Understanding the extraction schema

### Research Assessor Skill Guide
- [Overview](docs/research-assessor-guide/README.md) - What the skill does and when to use it
- [Installation](docs/research-assessor-guide/installation-guide.md) - Installing and verifying the skill
- [Usage Guide](docs/research-assessor-guide/usage-guide.md) - Complete usage reference
- [Architecture](docs/research-assessor-guide/architecture.md) - How the skill works
- [Quick Reference](docs/research-assessor-guide/quick-reference.md) - Cheat sheet for common tasks

### Schema and Development
- [Schema Reference](docs/user-guide/schema-reference.md) - Current schema documentation
- [Version History](docs/research-assessor-guide/version.md) - Skill version information

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

### ✅ Completed (v2.6)
- Extraction system complete and validated (8-pass workflow, Pass 0-7)
- Infrastructure extraction (PIDs, FAIR assessment, funding, permits)
- Schema v2.6 with complete object types
- PDF processing pipeline working
- Comprehensive documentation
- Repository organisation and FAIR4RS preparation

### 🚧 In Progress
- Assessment framework development (Three Pillars: Transparency → Credibility → Reproducibility)
- repliCATS Seven Signals adaptation for HASS disciplines
- Testing on additional papers from varied domains

### 📋 Planned (Next Phase)
- Complete assessment framework (cluster prompts, quality gating)
- Multi-paper batch processing
- Integration with archaeological data repositories
- Zenodo deposition and DOI assignment

---

## Contributing

We welcome contributions in several areas:

- **Domain expansion**: Adapt extraction to new fieldwork disciplines
- **Vocabulary development**: Refine controlled vocabularies empirically
- **Testing**: Run extractions on new papers, report issues
- **Examples**: Contribute worked extractions from other domains
- **Assessment**: Help develop credibility assessment rubrics
- **Documentation**: Improve guides and fix errors

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## Citation

If you use this work in research, please cite:

```bibtex
@software{llm-reproducibility-v2.6,
  title = {LLM-Based Research Extraction and Assessment},
  author = {[Author information in CITATION.cff]},
  version = {2.6},
  year = {2025},
  url = {[Repository URL in CITATION.cff]}
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
- Inspired by research transparency and reproducibility initiatives

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
- **v2.5** (Oct 23, 2025): Repository rationalisation and FAIR4RS preparation
- **v2.6** (Nov 2025): Infrastructure extraction (Pass 6), 8-pass workflow complete (Pass 0-7), assessment framework development

See [archive/README.md](archive/README.md) for complete development history.

---

## Licence

This project uses dual licensing:

- **Code** (scripts, validation tools): [Apache-2.0](LICENSE-CODE)
- **Documentation** (guides, prompts, examples): [CC-BY-4.0](LICENSE-DOCS)

See [LICENSE-CODE](LICENSE-CODE) and [LICENSE-DOCS](LICENSE-DOCS) for full licence texts.

---

**Ready to extract!** See [docs/user-guide/getting-started.md](docs/user-guide/getting-started.md) to begin.
