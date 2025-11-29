# Documentation Index

Complete map of all documentation in the LLM Reproducibility project, organised by audience and purpose.

**Last Updated:** 2025-11-29
**Documentation Files:** 20+ files across 4 categories

---

## Quick Navigation

**New Users:** Start with [Getting Started](user-guide/getting-started.md) → [Extraction Workflow](user-guide/extraction-workflow.md)

**Installing the Skill:** See [Research Assessor Installation](research-assessor-guide/installation-guide.md)

**Reference During Extraction:** Use [Quick Reference](research-assessor-guide/quick-reference.md) and [Schema Reference](user-guide/schema-reference.md)

**Developers:** Read [Architecture](research-assessor-guide/architecture.md) and [FAIR4RS Compliance](fair4rs-compliance.md)

**Researchers:** Explore [Background Research](background-research/) papers

---

## Documentation by Audience

### For New Users (Getting Started)

Start here if you're new to the Research Assessor skill or paper extraction:

1. **[Getting Started](user-guide/getting-started.md)** (Primary entry point)
   - Installation requirements
   - First extraction walkthrough
   - Core concepts introduction
   - Common pitfalls and solutions
   - **Time:** 15-20 minutes reading

2. **[Extraction Workflow](user-guide/extraction-workflow.md)** (Complete workflow guide)
   - 8-pass workflow detailed (Passes 0-7)
   - Section-by-section extraction approach
   - JSON file management
   - Quality metrics and verification
   - **Time:** 30-40 minutes reading, reference during extraction

3. **[PDF Extraction](user-guide/pdf-extraction.md)** (Preparing papers)
   - Converting PDFs to processed markdown
   - Handling tables, figures, references
   - Troubleshooting OCR issues
   - **Time:** 10 minutes reading

4. **[Schema Reference](user-guide/schema-reference.md)** (Understanding extraction structure)
   - Complete schema v2.6 documentation
   - Field descriptions and examples
   - Object types (Evidence, Claims, RDMAP, Infrastructure)
   - Relationship types
   - **Time:** 20-30 minutes reading, reference during extraction

**Estimated Onboarding Time:** 1.5-2 hours to read core documentation, ready to start first extraction

---

### For Active Extractors (Reference Guides)

Quick-access guides for users actively extracting papers:

1. **[Quick Reference](research-assessor-guide/quick-reference.md)** (Essential commands and checklist)
   - 8-pass workflow checklist (Passes 0-7)
   - Common commands
   - Troubleshooting quick fixes
   - Validation checks
   - **Use:** Keep open during extractions

2. **[Schema Reference](user-guide/schema-reference.md)** (Field lookups)
   - Complete field descriptions
   - Required vs optional fields
   - Controlled vocabulary values
   - Cross-reference structure
   - **Use:** Reference when uncertain about field usage

3. **[Usage Guide](research-assessor-guide/usage-guide.md)** (Comprehensive pass-by-pass instructions)
   - Detailed instructions for each pass (0-7)
   - Conversation templates for Claude Code
   - Section extraction strategies
   - JSON validation procedures
   - **Use:** Detailed guidance when workflow unclear

---

### For Skill Users (Installation and Configuration)

Documentation for installing and configuring the Research Assessor skill:

1. **[Research Assessor Overview](research-assessor-guide/README.md)** (What the skill does)
   - Skill capabilities and features
   - 8-pass workflow overview (Passes 0-7)
   - Object types extracted
   - When to use this skill
   - **Time:** 10 minutes reading

2. **[Installation Guide](research-assessor-guide/installation-guide.md)** (Setup instructions)
   - Prerequisites (Claude Code 2.0.36+, Sonnet 4.5+)
   - Skill installation steps
   - Verification procedures
   - First extraction (Pass 0 walkthrough)
   - **Time:** 15-20 minutes installation + verification

3. **[Version History](research-assessor-guide/version.md)** (Release notes)
   - Complete changelog v2.0 → v2.6
   - Schema evolution
   - Feature additions
   - Breaking changes
   - **Time:** 5-10 minutes reading

---

### For Developers and Contributors

Technical documentation for understanding and extending the system:

1. **[Architecture](research-assessor-guide/architecture.md)** (Design rationale)
   - System architecture (skill + prompts model)
   - Liberal-consolidate philosophy
   - Two-pass extraction methodology
   - Infrastructure assessment framework
   - Design decisions and trade-offs
   - **Time:** 40-50 minutes reading

2. **[FAIR4RS Compliance](fair4rs-compliance.md)** (FAIR principles assessment)
   - Current FAIR score: 9/15 (Moderately FAIR)
   - Principle-by-principle assessment (15 principles)
   - Gap analysis and remediation plan
   - Timeline to 15/15 (Exemplary FAIR)
   - **Time:** 30-40 minutes reading

3. **[Contributing Guide](research-assessor-guide/CONTRIBUTING.md)** (How to contribute)
   - 9 contribution types (domain expansion, testing, examples, documentation, etc.)
   - Submission guidelines
   - Quality standards
   - Infrastructure enhancement opportunities
   - **Time:** 15-20 minutes reading

---

### For Researchers (Background and Theory)

Deep research reports informing the extraction framework:

1. **[CEM-RDMAP Development Path](background-research/cem-rdmap-development-path.md)**
   - Evolution from Claims-Evidence-Methods to RDMAP framework
   - Rationale for three-tier RDMAP structure
   - Fieldwork-specific adaptations
   - **Time:** 25-30 minutes reading

2. **[FAIR and PIDs for HASS Reproducibility](background-research/fair-and-pids-for-hass-reproducibility.md)**
   - FAIR principles adaptation to HASS disciplines
   - Persistent Identifiers (PIDs) in archaeological research
   - Infrastructure assessment methodology
   - **Time:** 30-35 minutes reading

3. **[repliCATS Report](background-research/replicats-report.md)**
   - Collaborative Assessments for Trustworthy Science methodology
   - Seven credibility signals
   - Adaptation to computational methods
   - **Time:** 20-25 minutes reading

4. **[repliCATS Seven Signals HASS Adaptation](background-research/replicats-seven-signals-hass-adaptation.md)**
   - Applying repliCATS framework to HASS fieldwork
   - Signal adaptation for archaeology, ecology, ethnography
   - Assessment rubric development
   - **Time:** 25-30 minutes reading

5. **[Schemas Research Report](background-research/schemas_research_report.md)**
   - Survey of existing extraction schemas
   - TIDieR, CONSORT-Outcomes, SPIRIT frameworks
   - Schema design decisions
   - **Time:** 30-40 minutes reading

**Total Background Reading:** 2.5-3 hours for complete theoretical foundation

---

## Documentation by Topic

### Extraction Process

- [Getting Started](user-guide/getting-started.md) - First extraction
- [Extraction Workflow](user-guide/extraction-workflow.md) - Complete 8-pass workflow (Passes 0-7)
- [Quick Reference](research-assessor-guide/quick-reference.md) - Workflow checklist
- [Usage Guide](research-assessor-guide/usage-guide.md) - Pass-by-pass detailed instructions

### Schema and Data Structures

- [Schema Reference](user-guide/schema-reference.md) - Complete schema v2.6 documentation
- [Schemas Research Report](background-research/schemas_research_report.md) - Schema design rationale
- [CEM-RDMAP Development Path](background-research/cem-rdmap-development-path.md) - Framework evolution

### Infrastructure Assessment

- [FAIR4RS Compliance](fair4rs-compliance.md) - Software FAIR principles
- [FAIR and PIDs for HASS Reproducibility](background-research/fair-and-pids-for-hass-reproducibility.md) - FAIR adaptation to HASS

### Credibility Assessment (Future)

- [repliCATS Report](background-research/replicats-report.md) - Assessment methodology
- [repliCATS Seven Signals HASS Adaptation](background-research/replicats-seven-signals-hass-adaptation.md) - HASS-specific signals

### System Design

- [Architecture](research-assessor-guide/architecture.md) - Technical architecture
- [Version History](research-assessor-guide/version.md) - System evolution

### Contributing

- [Contributing Guide](research-assessor-guide/CONTRIBUTING.md) - How to contribute
- [FAIR4RS Compliance](fair4rs-compliance.md) - FAIR compliance roadmap

---

## Documentation by Format

### User Guides (Practical How-To)

- [Getting Started](user-guide/getting-started.md)
- [Extraction Workflow](user-guide/extraction-workflow.md)
- [PDF Extraction](user-guide/pdf-extraction.md)
- [Quick Reference](research-assessor-guide/quick-reference.md)
- [Usage Guide](research-assessor-guide/usage-guide.md)
- [Installation Guide](research-assessor-guide/installation-guide.md)

### Reference Documentation (Look-Up)

- [Schema Reference](user-guide/schema-reference.md)
- [Quick Reference](research-assessor-guide/quick-reference.md)
- [Version History](research-assessor-guide/version.md)

### Technical Documentation (System Understanding)

- [Architecture](research-assessor-guide/architecture.md)
- [FAIR4RS Compliance](fair4rs-compliance.md)
- [Contributing Guide](research-assessor-guide/CONTRIBUTING.md)

### Research Reports (Theoretical Background)

- [CEM-RDMAP Development Path](background-research/cem-rdmap-development-path.md)
- [FAIR and PIDs for HASS Reproducibility](background-research/fair-and-pids-for-hass-reproducibility.md)
- [repliCATS Report](background-research/replicats-report.md)
- [repliCATS Seven Signals HASS Adaptation](background-research/replicats-seven-signals-hass-adaptation.md)
- [Schemas Research Report](background-research/schemas_research_report.md)

---

## Documentation Not Included in This Index

The following documentation is embedded in the codebase rather than docs/:

### Extraction System Documentation

Located in `extraction-system/`:
- `extraction-system/README.md` - Extraction system overview
- `extraction-system/prompts/*.md` - Eight extraction prompts (Passes 0-7)
- `extraction-system/schema/reproducibility-infrastructure-schema-v2.6.json` - JSON schema

### Skill Reference Files

Located in `.claude/skills/research-assessor/references/`:
- Infrastructure assessment guides (PIDs, FAIR, permits, CReDIT)
- Evidence vs claims classification guides
- RDMAP tier classification guides
- Expected information checklists

### Planning Documents

Located in `planning/`:
- Active to-do list
- FAIR vocabularies development plan
- Pass 6 testing findings
- Schema improvement plans
- Archive of completed planning documents

### Output Documentation

Located in `outputs/`:
- `outputs/README.md` - Outputs directory structure

### Archive Documentation

Located in `archive/`:
- `archive/README.md` - Archive organisation
- Historical planning documents
- Obsolete documentation versions

---

## Reading Paths

### Path 1: Quick Start (Minimal Reading, Start Extracting)

**Time:** 30-45 minutes
**Goal:** Start first extraction today

1. [Getting Started](user-guide/getting-started.md) (20 min)
2. [Quick Reference](research-assessor-guide/quick-reference.md) (10 min)
3. Start extracting with [Usage Guide](research-assessor-guide/usage-guide.md) open for reference

**Best For:** Users who learn by doing, comfortable with trial and error

---

### Path 2: Comprehensive Onboarding (Complete Understanding)

**Time:** 3-4 hours
**Goal:** Understand system thoroughly before extracting

1. [Research Assessor Overview](research-assessor-guide/README.md) (10 min)
2. [Installation Guide](research-assessor-guide/installation-guide.md) (20 min)
3. [Getting Started](user-guide/getting-started.md) (20 min)
4. [Extraction Workflow](user-guide/extraction-workflow.md) (40 min)
5. [Schema Reference](user-guide/schema-reference.md) (30 min)
6. [Architecture](research-assessor-guide/architecture.md) (50 min)
7. [CEM-RDMAP Development Path](background-research/cem-rdmap-development-path.md) (30 min)
8. Start extracting with all guides available for reference

**Best For:** Researchers planning systematic multi-paper extraction, contributors

---

### Path 3: Developer Onboarding (System Extension)

**Time:** 2-3 hours
**Goal:** Understand architecture to extend or modify system

1. [Architecture](research-assessor-guide/architecture.md) (50 min)
2. [Schema Reference](user-guide/schema-reference.md) (30 min)
3. [FAIR4RS Compliance](fair4rs-compliance.md) (40 min)
4. [CEM-RDMAP Development Path](background-research/cem-rdmap-development-path.md) (30 min)
5. [Contributing Guide](research-assessor-guide/CONTRIBUTING.md) (20 min)
6. Review `extraction-system/prompts/` and `.claude/skills/research-assessor/`

**Best For:** Developers extending the skill, adapting to new domains

---

### Path 4: Research Background (Theoretical Foundation)

**Time:** 2.5-3 hours
**Goal:** Understand theoretical basis for extraction framework

1. [Schemas Research Report](background-research/schemas_research_report.md) (40 min)
2. [CEM-RDMAP Development Path](background-research/cem-rdmap-development-path.md) (30 min)
3. [FAIR and PIDs for HASS Reproducibility](background-research/fair-and-pids-for-hass-reproducibility.md) (35 min)
4. [repliCATS Report](background-research/replicats-report.md) (25 min)
5. [repliCATS Seven Signals HASS Adaptation](background-research/replicats-seven-signals-hass-adaptation.md) (30 min)

**Best For:** Researchers planning assessments, methodology papers, citations

---

## Documentation Gaps

The following documentation is planned but not yet created:

### User Guides

- **Troubleshooting Guide** - Common issues and solutions
- **Quality Metrics Guide** - Interpreting extraction quality metrics
- **Multi-Paper Batch Processing** - Queue management and automation

### Technical Documentation

- **API Reference** - Programmatic access to extractions (if developed)
- **Testing Guide** - Validation testing procedures
- **Deployment Guide** - Skill deployment and updates

### Examples

- **Worked Extraction Examples** - Annotated example extractions
- **Edge Case Catalogue** - Borderline item decisions documented

**See:** [Planning documents](../planning/) for roadmaps addressing these gaps

---

## Updating This Index

When adding new documentation:

1. Add file to appropriate section (by audience, topic, format)
2. Estimate reading time (10 min per 2000 words)
3. Update counts at top of document
4. Consider adding to reading paths if essential
5. Update "Last Updated" date

---

## Feedback

Documentation feedback and improvement suggestions:
- Open GitHub issue with label `documentation`
- Describe which document and what was unclear
- Suggest improvements

See [Contributing Guide](research-assessor-guide/CONTRIBUTING.md) for contribution process.

---

## Licence

All documentation is licensed under [CC-BY-4.0 International](../LICENSE-DOCS).

You are free to:
- **Share** - Copy and redistribute in any format
- **Adapt** - Remix, transform, and build upon the material

Under the following terms:
- **Attribution** - Give appropriate credit, link to licence, indicate changes
- **No additional restrictions** - Cannot apply legal/technical measures restricting others

---

**Navigation:** [Main README](../README.md) | [User Guide](user-guide/) | [Research Assessor Guide](research-assessor-guide/) | [Background Research](background-research/)

**Last Updated:** 2025-11-29
