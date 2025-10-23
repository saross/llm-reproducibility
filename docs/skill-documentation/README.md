# Research Assessor Skill

**Version:** 2.4  
**Status:** Production Ready  
**Last Updated:** 2025-10-20

A Claude AI skill for systematic extraction and assessment of research methodology, claims, and evidence from fieldwork-based research papers. Enables evaluation of research transparency, replicability, and credibility through structured multi-pass extraction.

---

## Quick Links

- **[Installation](#installation)** - Get started quickly
- **[Usage Guide](USAGE_GUIDE.md)** - Detailed usage instructions
- **[Architecture](ARCHITECTURE.md)** - System design and principles
- **[Version History](VERSION.md)** - Changes and evolution
- **[Prompt Development](PROMPT_REVISION_SUMMARY.md)** - How prompts were refined

---

## Overview

### What This Does

The Research Assessor skill extracts six types of research objects from academic papers:

**Claims & Evidence:**
- **Evidence** - Raw observations, measurements, data points
- **Claims** - Assertions that interpret or generalize
- **Implicit Arguments** - Unstated assumptions and logical implications

**RDMAP (Research Design, Methods, Protocols):**
- **Research Designs** - Strategic decisions (WHY framed this way)
- **Methods** - Tactical approaches (WHAT was done)
- **Protocols** - Operational procedures (HOW specifically implemented)

These extractions enable systematic assessment of research transparency and replicability.

### Target Domains

Designed for **fieldwork-based disciplines** where research happens in uncontrolled settings:
- Archaeology
- Ecology
- Ethnography
- Biology (field studies)
- Geography (field research)
- Anthropology

The framework respects fieldwork epistemology: opportunistic adaptation is legitimate when transparently documented.

### Key Features

- **Five-pass iterative workflow** - Liberal extraction → Rationalization → Validation
- **Skill + Runtime Prompts architecture** - Prompts provided at runtime, not embedded in skill
- **Single JSON document** - Accumulates content across passes, no merging needed
- **Cross-reference system** - Links between all object types for traceability
- **Expected information tracking** - Based on TIDieR, CONSORT-Outcomes frameworks
- **Consolidation metadata** - Complete traceability of rationalization decisions

---

## Installation

### Prerequisites

- Access to Claude AI with Skills support
- Claude Sonnet 4.5 or later recommended

### Install the Skill

1. **Download** the skill package: `research-assessor.zip`
2. **Install** via Claude Skills interface
3. **Verify** by asking Claude: "Do you have the research-assessor skill?"

The skill package includes:
- Core guidance (SKILL.md)
- Schema definitions (complete object structures)
- Decision frameworks (tier assignment, consolidation patterns, expected information)
- Worked examples (from real extractions)

### Get the Extraction Prompts

The five extraction prompts (~4,000 lines total) are **provided at runtime**, not embedded in the skill:

1. **Claims/Evidence Pass 1** - Liberal extraction (~800 lines)
2. **Claims/Evidence Pass 2** - Rationalization (~900 lines)
3. **RDMAP Pass 1** - Liberal extraction (~1,000 lines)
4. **RDMAP Pass 2** - Rationalization (~900 lines)
5. **Pass 3 Validation** - Integrity checks (~600 lines)

**Location:** These prompts are in your project knowledge or can be provided directly in chat.

**Why separate?** Prompts evolve frequently through testing. This architecture allows refinement without repackaging the skill, minimizing versioning conflicts.

---

## Quick Start

### 1. Prepare Your Materials

- Research paper (PDF or text)
- Blank JSON template (schema v2.4)
- Extraction prompt for desired pass

### 2. Run Extraction

**Example conversation:**
```
You: Here's the Claims/Evidence Pass 1 prompt:
     [paste full prompt]
     
     Extract from this Methods section:
     [paste section text]
     
     Use this blank template:
     [paste JSON template]

Claude: [Follows prompt to extract evidence, claims, implicit_arguments]
```

### 3. Continue Through Passes

Each pass builds on the previous:
```
Blank Template
    ↓
Claims Pass 1 → Liberal extraction
    ↓
Claims Pass 2 → Rationalization
    ↓
RDMAP Pass 1 → Liberal extraction
    ↓
RDMAP Pass 2 → Rationalization
    ↓
Validation Pass 3 → Integrity checks
```

**See [USAGE_GUIDE.md](USAGE_GUIDE.md) for detailed instructions.**

---

## Architecture Highlights

### Skill + Runtime Prompts Design

**The Skill Provides:**
- Core decision frameworks (evidence vs claims, tier assignment, consolidation)
- Schema definitions (object structures, field requirements)
- Reference materials (checklists, examples)

**You Provide at Runtime:**
- Extraction prompts (detailed instructions for each pass)
- Source material (paper sections to extract from)
- JSON document (template or partially populated)

**Benefits:**
- ✅ Prompts can be refined independently without skill repackaging
- ✅ Minimizes versioning conflicts
- ✅ Efficient context window usage
- ✅ Supports prompt experimentation and tuning

### Iterative Accumulation Workflow

Single JSON document flows through all passes:
- Each pass populates or refines specific arrays
- Other arrays remain untouched
- No merging step required
- Flexible ordering (claims first OR RDMAP first)

### Two-Pass Extraction Philosophy

**Pass 1: Liberal Extraction**
- Over-capture (40-50% more items expected)
- Preserve granularity
- Mark uncertainties
- Comprehensive coverage

**Pass 2: Rationalization**
- Consolidate redundant items (15-20% reduction target)
- Refine boundaries
- Verify relationships
- Document all changes via consolidation metadata

**See [ARCHITECTURE.md](ARCHITECTURE.md) for complete design rationale.**

---

## Expected Performance

Based on testing with Sobotkova et al. (2023):

**Pass 1 Extraction:**
- Comprehensive capture with intentional over-extraction
- Preserves granularity for later assessment
- Flags uncertainties explicitly

**Pass 2 Rationalization:**
- 15-20% reduction through consolidation
- Improved structural coherence
- Complete traceability via metadata

**Complete Extraction:**
- ~100-150 objects per paper (varies by complexity)
- ~200+ cross-references
- Assessment-ready for transparency/replicability evaluation

**Quality Targets:**
- Precision: >85% (items correctly classified)
- Recall: >80% (items captured vs hand-coding)
- Boundary Accuracy: >75% (evidence/claim distinctions)

---

## Use Cases

### Research Transparency Assessment

Evaluate how completely research methods are documented:
- What information is provided?
- What information is missing?
- Could this study be replicated?

### Systematic Literature Review

Extract methodology from multiple papers for comparison:
- Standardized extraction across studies
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

---

## Repository Structure

```
research-assessor-skill/
├── research-assessor.zip          # Skill package
├── README.md                       # This file
├── ARCHITECTURE.md                 # Design principles and rationale
├── USAGE_GUIDE.md                  # Detailed usage instructions
├── VERSION.md                      # Version history
├── PROMPT_REVISION_SUMMARY.md      # Prompt development documentation
├── TESTING.md                      # Testing procedures and results
├── CONTRIBUTING.md                 # Contribution guidelines
├── LICENSE                         # License information
└── examples/
    ├── sobotkova-extraction.json   # Complete worked example
    └── blank-template-v2.4.json    # Starting template
```

---

## Development History

### Evolution

**v1.0-2.1** (2025-10-16 to 2025-10-17)
- Initial claims/evidence extraction
- Single-pass workflow
- Basic schema (evidence, claims)

**v2.2-2.3** (2025-10-17 to 2025-10-18)
- Two-pass workflow (liberal → rationalize)
- Consolidation metadata
- Multi-dimensional evidence pattern

**v2.4** (2025-10-19 to 2025-10-20)
- RDMAP extraction (research designs, methods, protocols)
- Three-tier hierarchy
- Unified validation framework
- Iterative accumulation workflow
- Skill + runtime prompts architecture

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

**See [PROMPT_REVISION_SUMMARY.md](PROMPT_REVISION_SUMMARY.md) for complete development narrative.**

---

## Testing

### Test Dataset

Primary testing on:
**Sobotkova et al. (2023)** "Arbitrary Offline Data Capture on All of Your Androids: The FAIMS Mobile Platform"

Archaeological survey paper chosen because:
- Representative of fieldwork complexity
- Well-documented methodology
- Multi-method approach
- Opportunistic adaptations documented

### Testing Procedures

1. **Pass-by-pass testing** - Each extraction pass tested independently
2. **Boundary testing** - Evidence/claim distinctions validated
3. **Tier testing** - Design/Method/Protocol assignments verified
4. **Cross-reference testing** - Relationship integrity checked
5. **Consolidation testing** - Rationalization quality assessed

**See [TESTING.md](TESTING.md) for detailed procedures and results.**

---

## Contributing

We welcome contributions! Areas for enhancement:

- **Domain expansion** - Adapt to new fieldwork disciplines
- **Vocabulary development** - Refine controlled vocabularies empirically
- **Validation rules** - Add domain-specific checks
- **Examples** - Contribute worked extractions from other papers
- **Prompt refinement** - Improve extraction quality through testing

**See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.**

---

## Citation

If you use this skill in research, please cite:

```
Research Assessor Skill v2.4 (2025)
https://github.com/[your-username]/research-assessor-skill
Developed through iterative empirical testing on fieldwork-based research
```

---

## License

[To be determined - recommend MIT or Apache 2.0 for FAIR4RS compliance]

---

## Support and Contact

- **Issues:** [GitHub Issues](link-to-issues)
- **Documentation:** This repository
- **Updates:** Watch this repository for new releases

---

## Acknowledgments

Developed through iterative testing with:
- Claude Sonnet 4.5 (Anthropic)
- Tested on archaeological research papers
- Informed by TIDieR, CONSORT-Outcomes, and SPIRIT frameworks
- Inspired by RepliCATS and research transparency initiatives

---

## Future Directions

### Planned Enhancements

- **FAIR4RS compliance** - Complete metadata and documentation
- **Automated testing suite** - Regression testing for prompt changes
- **Domain-specific extensions** - Ecology, ethnography, biology variants
- **Assessment framework** - Scoring transparency and replicability
- **Scale testing** - Multi-paper batch processing

### Research Questions

- How does extraction quality vary across domains?
- What are minimum reporting standards by field?
- Can we predict replicability from extraction patterns?
- How do implicit assumptions correlate with research quality?

**Contributions welcome on any of these directions.**
