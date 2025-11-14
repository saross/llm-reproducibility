# Version History

**Current Version:** 2.5
**Release Date:** 2025-10-23
**Status:** Production Ready

---

## Version 2.5 (2025-10-23)

### Repository Rationalization Release

**Focus:** Repository organization and FAIR4RS preparation

**Repository Structure Changes:**
- Consolidated all extraction tools into `extraction-system/` (skill, prompts, schema, scripts)
- Organized documentation into `docs/` with user-guide/, skill-documentation/, development/, background-research/
- Curated `examples/` with best extraction and blank template
- Archived development history by version in `archive/extraction-development/`
- Streamlined `reports/` to key milestones only (extraction-testing/, quality-assurance/)
- Maintained active planning separate from archived development work

**FAIR4RS Preparation:**
- Added dual licensing (Apache 2.0 for code, CC-BY-4.0 International for documentation)
- Created CITATION.cff for machine-readable citation
- Added CHANGELOG.md from version history
- Enhanced README with comprehensive project overview
- Improved documentation navigation with README files at each level

**No Schema or Prompt Changes:**
- All extraction functionality remains unchanged from v2.4
- Schema stays at v2.5 (already updated)
- Prompts confirmed at v2.5 (already updated)
- This is purely an organizational and documentation release

---

## Version 2.4 (2025-10-19 to 2025-10-20)

### Major Features

**RDMAP Extraction Framework**
- Added research_designs, methods, protocols object types
- Three-tier hierarchy (Strategic → Tactical → Operational)
- Cross-references between RDMAP and claims/evidence
- Expected information tracking adapted from TIDieR and CONSORT-Outcomes

**Unified Validation (Pass 3)**
- Validates all six object types
- Cross-reference integrity checks
- Hierarchy validation
- Schema compliance verification
- Works with partial extractions (testing support)

**Architecture Evolution**
- **Skill + Runtime Prompts model** - Prompts provided at runtime, not embedded
- Iterative accumulation workflow - single JSON through all passes
- Separation of concerns - each pass handles specific arrays only

### Schema Changes

**New Object Types:**
- `research_designs` - Strategic framing and rationale (WHY)
- `methods` - Tactical approaches (WHAT)
- `protocols` - Operational procedures (HOW)

**Enhanced Existing Objects:**
- `claims` - Added `methodological_argument` type, `supports_method` field
- `implicit_arguments` - Added `design_assumption`, `methodological_assumption` types
- All objects - Added RDMAP cross-reference fields

**New Controlled Vocabularies:**
- Reasoning approaches: inductive/abductive/deductive/mixed/unclear
- Design types: research_framing, theoretical_framework, study_design, scope_definition, positionality
- Method types: data_collection, sampling, analysis, quality_control, validation, temporal_framework
- Protocol types: recording, measurement, analysis_procedure, quality_control_procedure, validation_check

### Prompt Changes

**All Five Prompts Updated for v2.4:**

1. **Claims/Evidence Pass 1** (~40 lines changed)
   - Input clarification: JSON may be blank or partially populated
   - Array boundaries: Only touch evidence, claims, implicit_arguments
   - Output: Same JSON with claims/evidence populated

2. **Claims/Evidence Pass 2** (~35 lines changed)
   - Input: JSON with claims/evidence from Pass 1
   - Preserves RDMAP arrays unchanged
   - Integrated v2.3 consolidation metadata

3. **RDMAP Pass 1** (~1,000 new lines)
   - Liberal extraction with three-tier hierarchy
   - Comprehensive examples (6 archaeology cases)
   - Expected information checklists
   - Preserves claims/evidence arrays unchanged

4. **RDMAP Pass 2** (~900 new lines)
   - Rationalization with tier verification
   - Consolidation patterns for each tier
   - Cross-reference formalization
   - Preserves claims/evidence arrays unchanged

5. **Validation Pass 3** (~600 new lines)
   - Unified validation across all object types
   - Flexible validation (adapts to partial extractions)
   - Deferred validation for missing arrays
   - Produces validation report (doesn't modify extraction)

**Total Prompt Content:** ~4,400 lines (up from ~1,700 in v2.3)

### Design Decisions

**Vocabulary Choices:**
- ✅ Reasoning: inductive/abductive/deductive (NOT exploratory/confirmatory)
- ✅ Separate research questions vs hypotheses tracking
- ✅ Open lists for study designs and sampling strategies
- ✅ Domain-specific terms evolve empirically

**Expected Information Frameworks:**
- ✅ TIDieR adapted for methods (10 elements)
- ✅ CONSORT-Outcomes adapted for protocols (8 elements)
- ✅ Sampling strategy checklist (7 elements)
- ✅ Analysis methods checklist (7 elements)

**Fieldwork-Specific Adaptations:**
- ✅ Opportunistic decisions tracking
- ✅ Contingency plans (planned vs actual)
- ✅ Adaptive procedures with justification
- ✅ Emergent discoveries
- ✅ Distinction: legitimate adaptation vs opacity

### Documentation

**New Files:**
- ARCHITECTURE.md - Design principles and rationale
- USAGE_GUIDE.md - Detailed usage instructions
- PROMPT_REVISION_SUMMARY.md - Development narrative
- TESTING.md - Testing procedures and results
- CONTRIBUTING.md - Contribution guidelines

**Updated Files:**
- README.md - Architecture explanation, quick start
- Skill SKILL.md - Runtime prompts model
- references/schema/schema-guide.md - Complete v2.4 schema

### Performance

**Tested on Sobotkova et al. (2023):**
- Pass 1: ~150 items extracted (comprehensive capture)
- Pass 2: ~120 items after consolidation (15-20% reduction)
- Pass 3: Validation successful
- Cross-references: ~200+ relationships mapped

---

## Version 2.3 (2025-10-18)

### Features

**Consolidation Metadata**
- Added `consolidation_metadata` object to all types
- Tracks `consolidated_from`, `consolidation_type`, `information_preserved`, `rationale`
- Complete traceability of rationalization decisions

**Multi-Dimensional Evidence Pattern**
- Enhanced evidence object with dimensional tracking
- Support for complex multi-faceted observations
- Improved claim-evidence granularity matching

### Prompt Changes

**Claims/Evidence Pass 2 Updated (~100 lines changed):**
- Consolidation metadata requirements added
- Multi-dimensional evidence guidance
- Enhanced consolidation patterns
- Improved quality checklist

### Testing

- Validated consolidation metadata on Sobotkova Results section
- Confirmed information preservation through rationalization
- Tested multi-dimensional evidence extraction

---

## Version 2.2 (2025-10-17)

### Features

**Two-Pass Extraction Workflow**
- Pass 1: Liberal extraction (over-capture strategy)
- Pass 2: Rationalization (consolidation and refinement)
- Target: 15-20% reduction through Pass 2

**Consolidation Framework**
- Decision framework: "Assess together or separately?"
- Lumping patterns (12 patterns identified)
- Splitting patterns (6 patterns identified)
- Granularity matching to assessment needs

### Prompt Changes

**Claims/Evidence Pass 1 Created (~800 lines):**
- Liberal extraction philosophy
- Comprehensive examples
- Expected information checklists
- Quality criteria

**Claims/Evidence Pass 2 Created (~850 lines):**
- Consolidation guidance
- Boundary refinement
- Relationship verification
- Change tracking

### Schema Changes

- Enhanced location object (section, page, paragraph, note)
- Added extraction_confidence field
- Added verbatim_quote field for traceability

### Testing

- Initial testing on Sobotkova Methods section
- Pass 1: 46 evidence items, 32 claims (comprehensive)
- Pass 2: 37 evidence items, 26 claims (15-20% reduction achieved)

---

## Version 2.1 (2025-10-16)

### Features

**Enhanced Evidence/Claim Distinction**
- Professional judgment boundary clarified
- Evidence basis taxonomy expanded
- Claim type refinements

**Project Metadata Structure**
- Timeline tracking
- Location information
- Resources documentation
- Track record

### Schema Changes

- Added `evidence_basis` field with controlled vocabulary
- Enhanced `claim_type` enumeration
- Added `project_metadata` object

---

## Version 2.0 (2025-10-16)

### Features

**Initial Claims/Evidence Extraction**
- Evidence objects (observations, measurements)
- Claim objects (interpretations, generalizations)
- Implicit argument objects (assumptions, implications)
- Simple cross-references (string ID arrays)

**Single-Pass Extraction**
- One extraction prompt (~400 lines)
- Direct extraction without rationalization

### Schema

**Core Objects:**
- evidence (evidence_id, evidence_text, evidence_type)
- claims (claim_id, claim_text, claim_type)
- implicit_arguments (implicit_id, implicit_text, type)

**Cross-References:**
- supported_by_evidence
- enables_claim
- support_relationships

### Testing

- Proof of concept on Sobotkova paper
- Established baseline extraction approach

---

## Version Numbering Scheme

**Major.Minor Format:**

**Major version (X.0):**
- Schema-breaking changes
- Major architectural shifts
- Significant prompt rewrites

**Minor version (X.Y):**
- Schema additions (backward compatible)
- Prompt enhancements
- New features

---

## Future Roadmap

### Version 2.5 (Planned)

**Assessment Framework:**
- Transparency scoring rubric
- Replicability indicators
- Quality metrics

**Domain Extensions:**
- Ecology-specific adaptations
- Ethnography-specific adaptations
- Biology field study adaptations

### Version 3.0 (Planned)

**Schema Evolution:**
- Formalized controlled vocabularies (empirically derived)
- Enhanced temporal tracking
- Causality modeling

**Automation:**
- Batch processing support
- API integration
- Automated validation

---

## Migration Guide

### From v2.3 to v2.4

**Schema Changes:**
- Add `research_designs`, `methods`, `protocols` arrays to JSON template
- Add RDMAP cross-reference fields to existing objects
- Update `claim_type` enum to include `methodological_argument`
- Update `implicit_arguments` type enum for RDMAP assumptions

**Workflow Changes:**
- Split extraction into five passes (was two)
- Use RDMAP prompts for methodology extraction
- Run Pass 3 validation after all extractions

**Backward Compatibility:**
- v2.3 extractions valid as input to v2.4 RDMAP passes
- Can add RDMAP to existing v2.3 extractions
- No need to re-extract claims/evidence

### From v2.2 to v2.3

**Schema Changes:**
- Add `consolidation_metadata` object to consolidated items
- Add dimensional tracking to evidence objects

**Workflow Changes:**
- Update Pass 2 prompt to generate consolidation metadata
- No changes to Pass 1

**Backward Compatibility:**
- v2.2 extractions valid, can add metadata retroactively

---

## Breaking Changes Log

### v2.4

**Non-Breaking:**
- All v2.3 extractions remain valid
- RDMAP arrays can be added to existing extractions

**Minor Breaking:**
- Validation Pass 3 replaces informal validation
- Prompt structure changes require re-reading prompts

### v2.3

**Non-Breaking:**
- All v2.2 extractions remain valid
- Consolidation metadata optional (recommended)

### v2.2

**Major Breaking:**
- Two-pass workflow required (was single-pass)
- Pass 1 prompts incompatible with v2.0/2.1 prompts

---

## Known Issues

### Version 2.4

**Minor Issues:**
- Cross-reference validation can be slow for large extractions (>200 objects)
- Some domain-specific vocabularies still evolving
- Expected information checklists archaeology-focused (other domains need development)

**Workarounds:**
- Validate in sections rather than entire paper
- Accept free-text terms, standardize later
- Adapt checklists manually for other domains

**Planned Fixes:**
- Optimize validation algorithms (v2.5)
- Build domain-specific vocabulary lists through usage (v2.5)
- Develop domain-specific checklists (v2.5)

---

## Release Notes

### v2.4 Release Notes

**Installation:**
1. Download `research-assessor.zip` (v2.4)
2. Install via Claude Skills interface
3. Obtain v2.4 extraction prompts from project knowledge

**Testing Before Use:**
- Test on Sobotkova paper (example provided)
- Verify Pass 1 liberal extraction quality
- Verify Pass 2 consolidation appropriateness
- Verify Pass 3 validation reports

**Known Limitations:**
- Optimized for fieldwork-based research
- Best results with Claude Sonnet 4.5+
- Large papers (>50 pages) may need sectioning

**Support:**
- Documentation in repository
- Example extractions provided
- GitHub Issues for bug reports

---

**For detailed development narrative, see [PROMPT_REVISION_SUMMARY.md](PROMPT_REVISION_SUMMARY.md)**
