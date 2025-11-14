# Documentation

Comprehensive documentation for the LLM-based Research Extraction and Assessment project.

**Version:** 2.6
**Last Updated:** 2025-11-13

---

## Quick Navigation

### 👤 For Users
Start here if you want to **use the extraction system**:

1. **[Getting Started](user-guide/getting-started.md)** - Installation and first extraction
2. **[Extraction Workflow](user-guide/extraction-workflow.md)** - Complete 7-pass workflow guide
3. **[PDF Extraction](user-guide/pdf-extraction.md)** - Preparing papers for analysis
4. **[Schema Reference](user-guide/schema-reference.md)** - Understanding extraction output (v2.6)

### 🛠️ For Developers
For understanding the system design and contributing:

1. **[Research Assessor Guide](research-assessor-guide/)** - Complete skill architecture and design
2. **[Schema Evolution](development/schema-evolution.md)** - Version history and mappings
3. **[Extraction System](../extraction-system/README.md)** - Technical overview and tools

### 📚 For Researchers
Background research and theoretical foundations:

1. **[Background Research](background-research/)** - Deep research reports on methodology, frameworks, and related work

---

## Documentation Structure

```
docs/
├── user-guide/                # For extraction system users
│   ├── getting-started.md     # Installation and first extraction
│   ├── extraction-workflow.md # 7-pass workflow guide
│   ├── pdf-extraction.md      # PDF processing
│   └── schema-reference.md    # Schema v2.6 reference
│
├── research-assessor-guide/   # Skill documentation
│   ├── overview.md            # Skill overview
│   ├── architecture.md        # Design principles
│   ├── usage-guide.md         # Detailed usage
│   ├── version-history.md     # Changelog v2.0 → v2.6
│   └── references/            # Reference materials
│       ├── infrastructure/    # FAIR, PID guides
│       └── methodology/       # Frameworks
│
├── development/               # For developers and contributors
│   ├── schema-evolution.md    # Schema version history
│   └── deployment-guide-v2.5.md  # Deployment procedures
│
└── background-research/       # Research reports and foundations
    └── [deep research reports]
```

---

## User Guide

### [Getting Started](user-guide/getting-started.md)
**For:** First-time users
**Contains:**
- Prerequisites and installation
- First extraction walkthrough (7 passes)
- Common workflows
- Troubleshooting basics

### [Extraction Workflow](user-guide/extraction-workflow.md)
**For:** Understanding the multi-pass extraction process
**Contains:**
- Seven-pass workflow explained (Passes 0-7)
- When to use each prompt
- Best practices
- Quality expectations
- Time estimates

### [PDF Extraction](user-guide/pdf-extraction.md)
**For:** Preparing source papers
**Contains:**
- PDF text extraction using PyMuPDF/pdfplumber
- Configuration options
- Batch processing
- Troubleshooting extraction issues

### [Schema Reference](user-guide/schema-reference.md)
**For:** Understanding extraction output
**Contains:**
- All seven object types explained (v2.6):
  - Evidence, claims, implicit arguments
  - Research designs, methods, protocols
  - Infrastructure (PIDs, FAIR, funding, permits)
- Field descriptions and examples
- Cross-reference system
- Schema versioning (v2.4 → v2.6)

---

## Research Assessor Skill Documentation

### [Skill Overview](research-assessor-guide/overview.md)
Complete overview of the Research Assessor skill

### [Architecture](research-assessor-guide/architecture.md)
Design principles and rationale:
- Skill + runtime prompts model
- Iterative accumulation workflow
- Seven-pass extraction philosophy
- Fieldwork epistemology

### [Usage Guide](research-assessor-guide/usage-guide.md)
Detailed usage instructions:
- Materials preparation
- Pass-by-pass extraction (0-6)
- Cross-reference management
- Quality assessment

### [Version History](research-assessor-guide/version-history.md)
Complete changelog from v2.0 → v2.6:
- Feature additions by version
- Schema changes (v2.4 → v2.5 → v2.6)
- Breaking changes
- Migration guides

### [Reference Materials](research-assessor-guide/references/)
Specialised reference guides:
- **Infrastructure/**
  - `fair-principles-guide.md` - FAIR assessment framework
  - `pid-systems-guide.md` - Persistent identifier extraction
- **Methodology/** - Methodological frameworks and standards

---

## Development Documentation

### [Schema Evolution](development/schema-evolution.md)
**For:** Understanding schema versioning
**Contains:**
- Version-to-version changes (v2.4 → v2.5 → v2.6)
- Ontology mappings (CRMarchaeo, CIDOC-CRM)
- Backward compatibility notes
- Future formalisation plans

### [Deployment Guide](development/deployment-guide-v2.5.md)
**For:** Skill deployment and packaging
**Contains:**
- Packaging details
- Deployment procedures
- Version management
- Testing before deployment

---

## Background Research

Deep research reports on:
- Methodology frameworks (TIDieR, CONSORT-Outcomes, SPIRIT)
- Research transparency initiatives
- Credibility assessment approaches (repliCATS)
- Domain-specific considerations
- LLM capabilities for research extraction

See [background-research/](background-research/) for all reports.

---

## Current Version: v2.6

### Key Features
- **7-pass extraction workflow** (Passes 0-6 plus validation)
- **Infrastructure extraction** (Pass 6): PIDs, FAIR assessment, funding, permits
- **Explicit/implicit distinction** for RDMAP objects
- **Metadata extraction** (Pass 0) for paper structure mapping
- **Comprehensive validation** (Pass 7) with integrity checks

### Workflow Summary
```
Pass 0: Metadata extraction (publication info, paper structure)
Pass 1: Claims/Evidence liberal extraction
Pass 2: Claims/Evidence rationalisation
Pass 3: RDMAP explicit extraction
Pass 4: RDMAP implicit extraction
Pass 5: RDMAP rationalisation
Pass 6: Infrastructure extraction (PIDs, FAIR, funding, permits)
Pass 7: Validation (structural integrity checks)
```

---

## Documentation Standards

### For User-Facing Docs
- Clear, step-by-step instructions
- Examples from real extractions
- Troubleshooting sections
- Links to related documentation

### For Developer Docs
- Rationale for design decisions
- Technical specifications
- Version compatibility information
- Migration guides

### For Research Docs
- Literature review and synthesis
- Methodological foundations
- Empirical findings
- Future research directions

---

## Finding What You Need

**"How do I install the system?"**
→ [user-guide/getting-started.md](user-guide/getting-started.md)

**"How does the 7-pass extraction workflow work?"**
→ [user-guide/extraction-workflow.md](user-guide/extraction-workflow.md)

**"What does this field in the schema mean?"**
→ [user-guide/schema-reference.md](user-guide/schema-reference.md)

**"How do I extract infrastructure (PIDs, FAIR)?"**
→ [user-guide/extraction-workflow.md#phase-3-infrastructure-pass-6](user-guide/extraction-workflow.md) and [research-assessor-guide/references/infrastructure/](research-assessor-guide/references/infrastructure/)

**"Why was the system designed this way?"**
→ [research-assessor-guide/architecture.md](research-assessor-guide/architecture.md)

**"How has the schema changed over time?"**
→ [development/schema-evolution.md](development/schema-evolution.md)

**"What research informed this project?"**
→ [background-research/](background-research/)

---

## Contributing to Documentation

Documentation contributions are welcome! Areas for improvement:

- **User guides**: Clearer explanations, more examples
- **Domain-specific guides**: Adaptation to different research fields
- **Troubleshooting**: Common issues and solutions
- **Examples**: Worked extractions with annotations
- **Infrastructure guides**: FAIR assessment examples, PID extraction patterns

For contribution guidelines, see the Research Assessor skill documentation.

---

## Related Resources

- **[Main README](../README.md)** - Project overview
- **[Extraction System](../extraction-system/README.md)** - All extraction tools, prompts, and scripts
- **[Outputs Directory](../outputs/README.md)** - Extraction outputs and usage guide
- **[Examples](../examples/)** - Worked extraction examples (coming soon)
- **[Planning](../planning/)** - Project roadmap and active tasks
- **[Archive](../archive/)** - Development history and completed work

---

**Need help?** Start with [user-guide/getting-started.md](user-guide/getting-started.md) or check the [Research Assessor Guide](research-assessor-guide/) for comprehensive technical details.
