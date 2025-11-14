# Research Assessor Skill

**Version:** 2.6
**Status:** Production Ready
**Last Updated:** 2025-11-13

A Claude AI skill for systematic extraction and assessment of research methodology, claims, evidence, and reproducibility infrastructure from fieldwork-based research papers. Enables evaluation of research transparency, replicability, and credibility through structured multi-pass extraction.

---

## Quick Links

- **[Quick Reference](quick-reference.md)** - Essential commands and workflows
- **[Usage Guide](usage-guide.md)** - Detailed usage instructions
- **[Architecture](architecture.md)** - System design and principles
- **[Installation Guide](installation-guide.md)** - Setup and configuration
- **[Version History](version.md)** - Changes and evolution
- **[Contributing](CONTRIBUTING.md)** - How to contribute

---

## Overview

### What This Does

The Research Assessor skill extracts seven types of research objects from academic papers:

**Claims & Evidence (Passes 1-2):**
- **Evidence** - Raw observations, measurements, data points
- **Claims** - Assertions that interpret or generalise
- **Implicit Arguments** - Unstated assumptions and logical implications

**RDMAP (Research Design, Methods, Protocols - Passes 3-5):**
- **Research Designs** - Strategic decisions (WHY framed this way)
- **Methods** - Tactical approaches (WHAT was done)
- **Protocols** - Operational procedures (HOW specifically implemented)

**Reproducibility Infrastructure (Pass 6):**
- **Persistent Identifiers (PIDs)** - DOIs, ORCIDs, dataset identifiers
- **FAIR Principles** - Findable, Accessible, Interoperable, Reusable data/software
- **Computational Reproducibility** - Code availability, dependencies, environments
- **Permits and Ethics** - IRB approvals, fieldwork permits, Indigenous data governance (CARE principles)
- **Funding and Research Context** - Grant acknowledgements, facility access

These extractions enable systematic assessment of research transparency, replicability, and credibility.

### Target Domains

Designed for **fieldwork-based disciplines** where research happens in uncontrolled settings:
- Archaeology
- Ecology
- Ethnography
- Biology (field studies)
- Geography (field research)
- Anthropology
- Heritage conservation

The framework respects fieldwork epistemology: opportunistic adaptation is legitimate when transparently documented.

### Key Features

- **Seven-pass iterative workflow** - Metadata → Claims/Evidence → RDMAP → Infrastructure → Validation
- **Skill + Runtime Prompts architecture** - Prompts provided at runtime, not embedded in skill
- **Single JSON document** - Accumulates content across passes, no merging needed
- **Cross-reference system** - Links between all object types for traceability
- **Expected information tracking** - Based on TIDieR, CONSORT-Outcomes frameworks
- **Consolidation metadata** - Complete traceability of rationalisation decisions
- **Infrastructure assessment** - Systematic PID, FAIR, and reproducibility evaluation

---

## Installation

### Prerequisites

- Access to Claude AI with Skills support
- Claude Sonnet 4.5 or later recommended

### Install the Skill

The skill is located in `.claude/skills/research-assessor/` within the project repository.

**Verify installation** by checking:
```bash
ls -la .claude/skills/research-assessor/
```

The skill package includes:
- Core guidance (SKILL.md)
- Schema definitions (complete object structures)
- Decision frameworks (tier assignment, consolidation patterns, expected information)
- Worked examples (from real extractions)
- Infrastructure assessment guidance (PIDs, FAIR principles, permits, funding)

### Get the Extraction Prompts

The seven extraction prompts (~6,000 lines total) are **provided at runtime**, not embedded in the skill:

1. **Pass 0: Metadata** - Paper-level metadata extraction (~400 lines)
2. **Pass 1: Claims/Evidence Liberal** - Comprehensive extraction (~800 lines)
3. **Pass 2: Claims/Evidence Rationalisation** - Consolidation (~900 lines)
4. **Pass 3: RDMAP Explicit** - Visible methodology extraction (~1,000 lines)
5. **Pass 4: RDMAP Implicit** - Implied decisions extraction (~800 lines)
6. **Pass 5: RDMAP Rationalisation** - Consolidation (~900 lines)
7. **Pass 6: Infrastructure** - Reproducibility infrastructure (~1,200 lines)
8. **Pass 7: Validation** - Integrity checks (~600 lines)

**Location:** `extraction-system/prompts/` directory

**Why separate?** Prompts evolve frequently through testing. This architecture allows refinement without repackaging the skill, minimising versioning conflicts.

---

## Quick Start

### 1. Prepare Your Materials

- Research paper (PDF converted to text via `input/WORKFLOW.md` guidance)
- Blank JSON template (schema v2.6)
- Extraction prompt for desired pass

### 2. Run Extraction

**Example conversation:**
```
You: Here's the Claims/Evidence Pass 1 prompt:
     [paste full prompt from extraction-system/prompts/01-claims-evidence_pass1_prompt.md]

     Extract from this Methods section:
     [paste section text from outputs/{paper-slug}/{paper-slug}.txt]

     Use this template:
     [paste JSON from outputs/{paper-slug}/extraction.json]

Claude: [Follows prompt to extract evidence, claims, implicit_arguments]
```

### 3. Continue Through Passes

Each pass builds on the previous:
```
Blank Template
    ↓
Pass 0 → Metadata extraction
    ↓
Pass 1 → Claims/Evidence liberal
    ↓
Pass 2 → Claims/Evidence rationalisation
    ↓
Pass 3 → RDMAP explicit extraction
    ↓
Pass 4 → RDMAP implicit scanning
    ↓
Pass 5 → RDMAP rationalisation
    ↓
Pass 6 → Infrastructure assessment
    ↓
Pass 7 → Validation and integrity checks
```

**See [usage-guide.md](usage-guide.md) for detailed instructions.**

---

## Architecture Highlights

### Skill + Runtime Prompts Design

**The Skill Provides:**
- Core decision frameworks (evidence vs claims, tier assignment, consolidation)
- Schema definitions (object structures, field requirements)
- Reference materials (checklists, examples, infrastructure guides)

**You Provide at Runtime:**
- Extraction prompts (detailed instructions for each pass)
- Source material (paper sections to extract from)
- JSON document (template or partially populated)

**Benefits:**
- ✅ Prompts can be refined independently without skill repackaging
- ✅ Minimises versioning conflicts
- ✅ Efficient context window usage
- ✅ Supports prompt experimentation and tuning

### Iterative Accumulation Workflow

Single JSON document flows through all passes:
- Each pass populates or refines specific arrays
- Other arrays remain untouched
- No merging step required
- Flexible pass ordering within stages

### Liberal-Consolidate Extraction Philosophy

**Liberal Passes (1, 3, 4): Over-Capture**
- 40-50% over-extraction expected
- Preserve granularity
- Mark uncertainties
- Comprehensive coverage

**Rationalisation Passes (2, 5): Consolidate**
- 15-20% reduction through consolidation
- Refine boundaries
- Verify relationships
- Document all changes via consolidation metadata

**See [architecture.md](architecture.md) for complete design rationale.**

---

## Expected Performance

Based on testing across diverse papers (2016-2024):

**Pass 1-2 (Claims/Evidence):**
- ~40-60 evidence items (varies by paper complexity)
- ~25-40 claims
- ~10-20 implicit arguments
- Comprehensive coverage with intentional over-extraction in Pass 1
- 15-20% consolidation in Pass 2

**Pass 3-5 (RDMAP):**
- ~4-8 research designs (strategic decisions)
- ~15-25 methods (tactical approaches)
- ~8-15 protocols (operational procedures)
- Explicit + implicit methodology captured
- Consolidation maintains granularity whilst eliminating redundancy

**Pass 6 (Infrastructure):**
- PID connectivity: 0-6 score (pre-FAIR baseline to exemplary)
- FAIR compliance: 0-15 score across 15 principles
- Computational reproducibility: 0-4 levels
- Permits/ethics documentation completeness
- Funding acknowledgements and research context

**Complete Extraction:**
- ~100-180 objects per paper (varies by complexity and length)
- ~200-400 cross-references
- Assessment-ready for transparency/replicability evaluation

**Quality Targets:**
- Precision: >85% (items correctly classified)
- Recall: >80% (items captured vs expert coding)
- Boundary Accuracy: >75% (evidence/claim distinctions)
- Relationship Mapping: >80% (evidence linked to claims/methods)

---

## Use Cases

### Research Transparency Assessment

Evaluate how completely research methods are documented:
- What information is provided?
- What information is missing?
- Could this study be replicated?

### Reproducibility Infrastructure Evaluation

Assess data/code availability and preservation:
- Are datasets findable and accessible?
- Is code archived with dependencies?
- Are permit numbers and ethical approvals documented?
- Does the research follow FAIR principles?

### Systematic Literature Review

Extract methodology from multiple papers for comparison:
- Standardised extraction across studies
- Consistent granularity
- Cross-study analysis support

### Research Quality Evaluation

Assess evidential support for claims:
- Which claims have strong evidence?
- Which claims rest on implicit assumptions?
- Where are the inferential leaps?

### Research Training

Teach systematic methodology documentation:
- What constitutes complete reporting?
- How to distinguish observation from interpretation?
- How to document decision-making processes?
- How to ensure computational reproducibility?

---

## Repository Structure

```
llm-reproducibility/
├── .claude/skills/research-assessor/    # Skill package
│   ├── SKILL.md                         # Core skill definition
│   └── references/                      # Decision frameworks and guides
│       ├── checklists/                  # Evidence-vs-claims, expected info
│       ├── consolidation/               # Rationalisation patterns
│       ├── infrastructure/              # PID, FAIR, permits, funding guides
│       ├── rdmap/                       # Design-method-protocol tier guidance
│       └── schema/                      # JSON schema definitions
├── extraction-system/                   # Extraction workflow components
│   ├── prompts/                         # Pass-specific extraction prompts
│   └── schema/                          # JSON schema files
├── outputs/                             # Extraction outputs by paper
│   └── {paper-slug}/
│       ├── extraction.json              # Primary extraction output
│       └── {paper-slug}.txt             # Extracted plain text
├── docs/                                # Documentation
│   ├── research-assessor-guide/         # This guide
│   ├── user-guide/                      # User documentation
│   └── background-research/             # Research context
└── input/
    ├── WORKFLOW.md                      # Complete extraction workflow
    └── queue.yaml                       # Paper processing queue
```

---

## Development History

### Evolution

**v1.0-2.1** (2025-10-16 to 2025-10-17)
- Initial claims/evidence extraction
- Single-pass workflow
- Basic schema (evidence, claims)

**v2.2-2.3** (2025-10-17 to 2025-10-18)
- Two-pass workflow (liberal → rationalise)
- Consolidation metadata
- Multi-dimensional evidence pattern

**v2.4** (2025-10-19 to 2025-10-20)
- RDMAP extraction (research designs, methods, protocols)
- Three-tier hierarchy
- Unified validation framework
- Iterative accumulation workflow
- Skill + runtime prompts architecture

**v2.5** (2025-10-28 to 2025-11-02)
- Schema field name standardisation
- Bidirectional relationship validation
- Cross-paper error analysis and improvements
- Compound claim handling guidance
- Seven-pass workflow (split RDMAP into explicit/implicit/rationalisation)

**v2.6** (2025-11-11 to 2025-11-13)
- Infrastructure assessment capability (Pass 6)
- PID systems guide (data, publications, software, grants)
- FAIR principles guide (15-principle assessment framework)
- Fieldwork permits and CARE principles
- Computational reproducibility spectrum
- Documentation reorganisation and updates

### Key Decisions

**Vocabulary Choices:**
- Reasoning: inductive/abductive/deductive (NOT exploratory/confirmatory)
- Separate tracking for research questions vs hypotheses
- Open vocabularies (domain-specific terms evolve empirically)

**Architectural Principles:**
- Simple cross-references (string ID arrays only)
- Extraction vs assessment separation
- Expected information ≠ Required information
- Respect for fieldwork epistemology

**See [version.md](version.md) for complete changelog.**

---

## Testing

### Test Datasets

Primary testing across diverse corpus (2016-2024):

**Sobotkova et al. (2023)** - "Arbitrary Offline Data Capture on All of Your Androids: The FAIMS Mobile Platform"
- Representative of fieldwork complexity
- Well-documented methodology
- Multi-method approach

**Ballsun-Stanton et al. (2018)** - "FAIMS Mobile: Flexible, open-source software for field research" (SoftwareX)
- Software publication with exceptional documentation
- Infrastructure testing baseline (13/15 FAIR)

**Penske et al. (2023)** - Ancient DNA genomics paper (Nature)
- High-profile publication with exemplary data sharing
- Infrastructure testing (14/15 FAIR)

**Sobotkova et al. (2024)** - "Four years of FAIMS in the field" (Journal of Documentation)
- Recent computational paper
- Typical HASS infrastructure patterns

**Sobotkova et al. (2016)** - Book chapter on FAIMS development
- Pre-FAIR baseline (0/15)
- Historical context for infrastructure evolution

### Testing Procedures

1. **Pass-by-pass testing** - Each extraction pass tested independently
2. **Boundary testing** - Evidence/claim distinctions validated
3. **Tier testing** - Design/Method/Protocol assignments verified
4. **Cross-reference testing** - Relationship integrity checked
5. **Consolidation testing** - Rationalisation quality assessed
6. **Infrastructure testing** - PID, FAIR, reproducibility assessment validated

**See `planning/pass6-phase1-testing-findings.md` for detailed Phase 1 infrastructure testing results.**

---

## Contributing

We welcome contributions! Areas for enhancement:

- **Domain expansion** - Adapt to new fieldwork disciplines
- **Vocabulary development** - Refine controlled vocabularies empirically
- **Validation rules** - Add domain-specific checks
- **Examples** - Contribute worked extractions from other papers
- **Prompt refinement** - Improve extraction quality through testing
- **Infrastructure guidance** - Expand PID/FAIR/reproducibility coverage

**See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.**

---

## Citation

If you use this skill in research, please cite:

```
Research Assessor Skill v2.6 (2025)
https://github.com/[repository-location]/llm-reproducibility
Developed through iterative empirical testing on fieldwork-based research
```

---

## Licence

[To be determined - recommend MIT or Apache 2.0 for FAIR4RS compliance]

---

## Support and Contact

- **Issues:** GitHub Issues (repository-specific)
- **Documentation:** This repository
- **Updates:** Watch repository for new releases

---

## Acknowledgements

Developed through iterative testing with:
- Claude Sonnet 4.5 (Anthropic)
- Tested on archaeological and fieldwork-based research papers
- Informed by TIDieR, CONSORT-Outcomes, and SPIRIT frameworks
- Inspired by RepliCATS and research transparency initiatives
- Infrastructure guidance informed by FAIR4RS, DataCite, Crossref, and community standards

---

## Future Directions

### Planned Enhancements

- **FAIR4RS compliance** - Complete metadata and documentation
- **Automated testing suite** - Regression testing for prompt changes
- **Domain-specific extensions** - Ecology, ethnography, biology variants
- **Assessment framework** - Scoring transparency and replicability
- **Scale testing** - Multi-paper batch processing
- **Infrastructure enhancements** - Software documentation structure, supplementary materials tracking

### Research Questions

- How does extraction quality vary across domains?
- What are minimum reporting standards by field?
- Can we predict replicability from extraction patterns?
- How do implicit assumptions correlate with research quality?
- How has reproducibility infrastructure adoption evolved in HASS fields?
- What are typical PID connectivity and FAIR compliance baselines by discipline?

**Contributions welcome on any of these directions.**
