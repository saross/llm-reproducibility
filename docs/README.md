# Documentation

Comprehensive documentation for the LLM-based Research Extraction and Assessment project.

---

## Quick Navigation

### 👤 For Users
Start here if you want to **use the extraction system**:

1. **[Getting Started](user-guide/getting-started.md)** - Installation and first extraction
2. **[Extraction Workflow](user-guide/extraction-workflow.md)** - Complete 5-pass workflow guide
3. **[PDF Extraction](user-guide/pdf-extraction.md)** - Preparing papers for analysis
4. **[Schema Reference](user-guide/schema-reference.md)** - Understanding extraction output

### 🛠️ For Developers
For understanding the system design and contributing:

1. **[Skill Documentation](skill-documentation/)** - Complete skill architecture and design
2. **[Schema Evolution](development/schema-evolution.md)** - Version history and mappings
3. **[Deployment Guide](development/deployment-guide-v2.5.md)** - Skill packaging and deployment

### 📚 For Researchers
Background research and theoretical foundations:

1. **[Background Research](background-research/)** - Deep research reports on methodology, frameworks, and related work

---

## Documentation Structure

```
docs/
├── user-guide/              # For extraction system users
│   ├── getting-started.md
│   ├── extraction-workflow.md
│   ├── pdf-extraction.md
│   └── schema-reference.md
│
├── skill-documentation/     # Comprehensive skill docs
│   ├── README.md
│   ├── ARCHITECTURE.md
│   ├── USAGE_GUIDE.md
│   ├── VERSION.md
│   ├── QUICK_REFERENCE.md
│   └── [other skill docs]
│
├── development/             # For developers and contributors
│   ├── schema-evolution.md
│   └── deployment-guide-v2.5.md
│
└── background-research/     # Research reports and foundations
    └── [deep research reports]
```

---

## User Guide

### [Getting Started](user-guide/getting-started.md)
**For:** First-time users
**Contains:**
- Prerequisites and installation
- First extraction walkthrough
- Common workflows
- Troubleshooting basics

### [Extraction Workflow](user-guide/extraction-workflow.md)
**For:** Understanding the multi-pass extraction process
**Contains:**
- Five-pass workflow explained
- When to use each prompt
- Best practices
- Quality expectations

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
- All six object types explained
- Field descriptions and examples
- Cross-reference system
- Expected information checklists

---

## Skill Documentation

### [Skill README](skill-documentation/README.md)
Complete overview of the Research Assessor skill

### [Architecture](skill-documentation/ARCHITECTURE.md)
Design principles and rationale:
- Skill + runtime prompts model
- Iterative accumulation workflow
- Two-pass extraction philosophy
- Fieldwork epistemology

### [Usage Guide](skill-documentation/USAGE_GUIDE.md)
Detailed usage instructions:
- Materials preparation
- Pass-by-pass extraction
- Cross-reference management
- Quality assessment

### [Version History](skill-documentation/VERSION.md)
Complete changelog from v2.0 → v2.5:
- Feature additions by version
- Schema changes
- Breaking changes
- Migration guides

### Other Skill Documentation
- **QUICK_REFERENCE.md** - Cheat sheet for common patterns
- **TESTING.md** - Testing procedures and results
- **CONTRIBUTING.md** - Contribution guidelines
- **INSTALLATION_GUIDE.md** - Detailed installation steps
- **DELIVERY_SUMMARY.md** - Packaging and delivery information

---

## Development Documentation

### [Schema Evolution](development/schema-evolution.md)
**For:** Understanding schema versioning
**Contains:**
- Version-to-version changes
- Ontology mappings (CRMarchaeo, CIDOC-CRM)
- Backward compatibility notes
- Future formalization plans

### [Deployment Guide](development/deployment-guide-v2.5.md)
**For:** Skill deployment and packaging
**Contains:**
- v2.5 packaging details
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

**"How does the extraction workflow work?"**
→ [user-guide/extraction-workflow.md](user-guide/extraction-workflow.md)

**"What does this field in the schema mean?"**
→ [user-guide/schema-reference.md](user-guide/schema-reference.md)

**"Why was the system designed this way?"**
→ [skill-documentation/ARCHITECTURE.md](skill-documentation/ARCHITECTURE.md)

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

See [skill-documentation/CONTRIBUTING.md](skill-documentation/CONTRIBUTING.md) for guidelines.

---

## Related Resources

- [Main README](../README.md) - Project overview
- [Extraction System](../extraction-system/) - All extraction tools
- [Examples](../examples/) - Worked extraction examples
- [Planning](../planning/) - Project roadmap
- [Archive](../archive/) - Development history

---

**Need help?** Start with [user-guide/getting-started.md](user-guide/getting-started.md) or check the skill documentation for comprehensive technical details.
