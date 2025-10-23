# Changelog

All notable changes to the LLM-Based Research Extraction and Assessment project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.5.0] - 2025-10-23

### Repository Rationalization Release

#### Changed
- Reorganized entire repository structure for clarity and usability
- Consolidated extraction tools into `extraction-system/` folder
- Organized all documentation into `docs/` with user-guide/, skill-documentation/, development/
- Curated `examples/` with only best extraction + blank template
- Archived development history by version in `archive/extraction-development/`
- Streamlined `reports/` to key milestones only
- Separated active `planning/` from archived development work

#### Added
- Dual licensing: Apache 2.0 (code), CC-BY-4.0 International (documentation)
- CITATION.cff for machine-readable citation
- CHANGELOG.md (this file)
- Comprehensive main README.md
- Navigation README.md files at every level (planning/, docs/, examples/, reports/, archive/)
- User guide documentation (getting-started.md, extraction-workflow.md, pdf-extraction.md, schema-reference.md)
- extraction-system/schema/README.md explaining versioning

#### Fixed
- Updated all version references to v2.5
- Corrected file paths in documentation
- Improved cross-referencing throughout documentation

---

## [2.4.0] - 2025-10-20

### RDMAP Extraction Framework

#### Added
- Research Designs, Methods, and Protocols (RDMAP) object types
- Three-tier hierarchy: Strategic (WHY) → Tactical (WHAT) → Operational (HOW)
- Unified validation (Pass 3) across all object types
- Expected information checklists adapted from TIDieR and CONSORT-Outcomes frameworks
- Fieldwork-specific adaptations (opportunistic decisions, contingency tracking)
- Skill + runtime prompts architecture

#### Changed
- Extended claims with `methodological_argument` type
- Extended implicit_arguments with `design_assumption` and `methodological_assumption` types
- Added RDMAP cross-reference fields to all existing objects
- Increased total prompt content to ~4,400 lines (from ~1,700)

---

## [2.3.0] - 2025-10-18

### Consolidation Metadata and Multi-Dimensional Evidence

#### Added
- `consolidation_metadata` object to evidence, claims, and implicit arguments
- Complete traceability for all rationalization decisions
- Multi-dimensional evidence pattern for complex observations
- `related_evidence` field for granularity tracking

#### Changed
- Enhanced claim structure with primary_function, claim_nature, quantitative_details
- Improved declared_uncertainty structure
- Added 'synthesis' to claim_role enum

---

## [2.2.0] - 2025-10-17

### Two-Pass Extraction Workflow

#### Added
- Pass 1: Liberal extraction with intentional over-capture strategy
- Pass 2: Rationalization with consolidation and refinement
- Consolidation framework with 12 lumping patterns, 6 splitting patterns
- Target: 15-20% reduction through Pass 2

#### Changed
- Enhanced location object (section, page, paragraph, note)
- Added extraction_confidence field
- Added verbatim_quote field for traceability
- Separated extraction-time vs assessment-time fields

---

## [2.1.0] - 2025-10-16

### Evidence/Claim Enhancement

#### Added
- Enhanced evidence/claim boundary framework
- Evidence basis taxonomy
- Project metadata structure (timeline, location, resources, track record)
- Optional conflict-of-interest field for implicit arguments

#### Changed
- Refined claim_type enumeration
- Formalized Type 3 (disciplinary_assumption) extraction

---

## [2.0.0] - 2025-10-16

### Initial Release

#### Added
- Core extraction schema with three object types: evidence, claims, implicit_arguments
- Single-pass extraction workflow
- Simple cross-reference system (string ID arrays)
- Dual-layer uncertainty tracking (declared vs expected)
- Professional judgment boundary framework
- Four-level hierarchy support
- Initial extraction prompts (~400 lines)

---

## Version Numbering

**Major.Minor.Patch Format:**

- **Major (X.0.0):** Schema-breaking changes, major architectural shifts
- **Minor (X.Y.0):** Schema additions (backward compatible), new features, significant enhancements
- **Patch (X.Y.Z):** Bug fixes, documentation updates, non-functional changes

---

## Future Releases

### Planned for v2.6+
- Assessment framework development (credibility scoring)
- Multi-paper batch processing
- Archaeological repository integration
- Additional domain-specific adaptations

See [planning/cwts_implementation_plan.md](planning/cwts_implementation_plan.md) for detailed roadmap.

---

## Links

- **Repository:** https://github.com/[your-username]/llm-reproducibility
- **Documentation:** [docs/](docs/)
- **Issues:** https://github.com/[your-username]/llm-reproducibility/issues
- **Releases:** https://github.com/[your-username]/llm-reproducibility/releases

---

For detailed version information including prompt changes, schema specifics, and migration guides, see [docs/skill-documentation/VERSION.md](docs/skill-documentation/VERSION.md).
