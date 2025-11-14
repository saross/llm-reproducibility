# Version History

**Current Version:** 2.6
**Last Updated:** 2025-11-13

Complete changelog documenting the evolution of the Research Assessor skill from initial claims/evidence extraction to comprehensive reproducibility infrastructure assessment.

---

## Version 2.6 (2025-11-11 to 2025-11-13)

**Status:** Current Release
**Focus:** Infrastructure assessment capability, 7-pass workflow

### New Features

**Infrastructure Assessment (Pass 6):**
- Persistent Identifiers (PIDs) assessment across 6 types
- FAIR principles evaluation (15-principle framework)
- Computational reproducibility spectrum (0-4 levels)
- Permits and ethics tracking (IRB, fieldwork, CARE principles)
- Funding acknowledgements and research context
- PID connectivity score (0-6)
- FAIR compliance score (0-15)

**Seven-Pass Workflow:**
- Pass 0: Metadata extraction (NEW)
- Pass 1: Claims/Evidence liberal
- Pass 2: Claims/Evidence consolidation
- Pass 3: RDMAP explicit extraction (was Pass 1 in v2.4)
- Pass 4: RDMAP implicit scanning (NEW - split from Pass 1)
- Pass 5: RDMAP consolidation (was Pass 2 in v2.4)
- Pass 6: Infrastructure assessment (NEW)
- Pass 7: Validation (was Pass 3 in v2.4)

### Infrastructure Guidance Added

**New Reference Files:**
- `pid-systems-guide.md` (~3,500 words): Data DOIs, ORCIDs, Software Heritage, grant identifiers, controlled vocabularies
- `fair-principles-guide.md` (~4,000 words): 15-principle assessment framework, historical context, scoring examples
- `fieldwork-permits-guide.md` (~2,000 words): IRB, archaeological permits, CARE principles, ancient DNA ethics
- `credit-taxonomy.md` (~1,500 words): Contributor roles (CRediT standard)

**Enhanced Infrastructure Content:**
- Software FAIR4RS principles (computational reproducibility)
- 5-level reproducibility spectrum (none → code_only → code_dependencies → containerised → fully_reproducible)
- Grant DOIs (Crossref/DataCite integration, ORCID linking)
- SPDX licence identifiers
- Ben Marwick's "built-in vs bolted-on" FAIR heuristic

### Testing and Validation

**Phase 1 Infrastructure Testing Complete:**
- 4 diverse papers tested (2016-2024, 0-15 FAIR range)
- Findings documented in `planning/pass6-phase1-testing-findings.md`
- 7 extraction challenges identified with solutions
- 5 guidance gaps documented with recommendations
- 5 schema gaps assessed with priority levels

**Testing Corpus:**
- Ballsun-Stanton et al. 2018 (SoftwareX): 13/15 FAIR, software publication baseline
- Sobotkova et al. 2024 (J Documentation): 4/15 FAIR, typical HASS computational paper
- Penske et al. 2023 (Nature): 14/15 FAIR, ancient DNA best practices
- Sobotkova et al. 2016 (Book chapter): 0/15 FAIR, pre-FAIR baseline

### Schema Changes

**Infrastructure Object Added:**
```json
"infrastructure": {
  "pid_graph": {...},
  "fair_assessment": {...},
  "computational_reproducibility": {...},
  "permits_ethics": {...},
  "funding": {...},
  "pid_connectivity_score": 0-6,
  "fair_compliance_score": 0-15
}
```

**No Breaking Changes:** v2.5 extractions fully compatible with v2.6 schema (infrastructure object optional).

### Documentation

**Major Updates:**
- Documentation reorganised to `docs/research-assessor-guide/` (from `docs/skill-documentation/`)
- All 8 core guides updated for 7-pass workflow (README, quick-reference, usage-guide, architecture, installation-guide, CONTRIBUTING, version)
- Infrastructure assessment workflow documented
- Pass 6 testing findings published
- User guides updated with Pass 0 and Pass 6 instructions

**New Content:**
- `extraction-system/README.md` - Extraction toolkit overview
- `outputs/README.md` - Outputs directory guide
- `planning/pass6-phase1-testing-findings.md` - Infrastructure testing results
- `planning/pass6-software-documentation-enhancement.md` - Phase 2 planning

### Prompt Updates

**New Prompts:**
- `00-metadata_pass0_prompt.md` (~400 lines) - Paper-level metadata
- `04-rdmap_pass1b_implicit_prompt.md` (~800 lines) - Implicit methodology scanning
- `06-infrastructure_pass6_prompt.md` (~1,200 lines) - Infrastructure assessment

**Updated Prompts:**
- `03-rdmap_pass1a_explicit_prompt.md` - Renamed from `01-rdmap_pass1_prompt.md`
- `05-rdmap_pass2_consolidation_prompt.md` - Renamed from `02-rdmap_pass2_prompt.md`
- `07-validation_pass3_prompt.md` - Renamed from `03-validation_pass3_prompt.md`
- All prompts updated to reference skill infrastructure guides

### Known Limitations

**Phase 2 Enhancements Deferred:**
- Software documentation structure assessment (requires 10+ paper evidence)
- Supplementary materials tracking (straightforward, low priority)
- Computational environment specification (design-intensive)
- Historical trends analysis (requires full corpus)

**Guidance Gaps Identified:**
- Pre-FAIR era paper interpretation (partial solution in fair-principles-guide)
- Ancient DNA ethics regional variation (guidance added but needs examples)
- Book chapter PID handling (ISBNs documented)
- Multi-component software systems (deferred to Phase 2)

---

## Version 2.5 (2025-10-28 to 2025-11-02)

**Status:** Superseded by v2.6
**Focus:** Schema field name standardisation, bidirectional validation, cross-paper quality improvements

### Major Changes

**Schema Field Name Standardisation:**
- Canonical field names enforced across all objects
- `implemented_by_methods` (not child_methods, enables_methods)
- `implements_designs` (reverse reference)
- `realized_through_protocols` (not child_protocols)
- `implements_methods` plural (not singular)
- `supported_by` (not supported_by_evidence)

**Migration:**
- 376 field name changes across 7 papers
- Migration script created: `extraction-system/scripts/migrate_field_names.py`
- Backups created before migration
- Post-migration validation: 243 auto-corrections, 59 conflicts flagged

**Bidirectional Validation:**
- Validator script with auto-correction: `scripts/validate_bidirectional.py`
- JSON Schema validation rules added
- Pass 7 validation prompt updated with bidirectional checks
- Reminders added to Pass 2/5 prompts

### Quality Improvements

**Compound Claim Handling:**
- Case 6 added to `evidence-vs-claims-guide.md` (~440 lines)
- Four types: Conjunctive, Comparative, Conditional, Sequential
- Worked example from sobotkova-et-al-2023
- Pass 1 vs Pass 2 extraction rules
- Prevents context loss errors (4 instances identified in cross-paper analysis)

**Secondary Source Attribution:**
- Analysis documented in `planning/secondary-source-attribution-analysis.md`
- 6 instances of literature review vs empirical misclassification across 4 papers
- Simple decision tree would prevent 100% of observed errors
- Recommendation: Simple `claim_origin` field (novel/tested/supported/synthesised)
- Implementation deferred to future phase

**Cross-Paper Error Analysis:**
- 10-paper corpus systematic review
- Bidirectional mapping errors, consolidation inconsistencies, compound claims identified
- Quote completeness requirements clarified
- RDMAP completeness checker script created

### Documentation

**Updated:**
- Schema guide with canonical field names section
- Migration log documenting breaking changes
- Evidence-vs-claims guide (Case 6 added)
- Active todo list (Section 5a completed)

---

## Version 2.4 (2025-10-19 to 2025-10-20)

**Status:** Superseded by v2.5
**Focus:** RDMAP integration, five-pass workflow, skill + runtime prompts architecture

### Major Changes

**RDMAP Extraction Added:**
- Research Designs (strategic WHY decisions)
- Methods (tactical WHAT approaches)
- Protocols (operational HOW procedures)
- Three-tier hierarchy with bidirectional relationships

**Five-Pass Workflow:**
- Pass 1: Claims/Evidence liberal
- Pass 2: Claims/Evidence consolidation
- Pass 3: RDMAP liberal (NEW - was Pass 1)
- Pass 4: RDMAP consolidation (NEW - was Pass 2)
- Pass 5: Validation (was Pass 3)

**Skill + Runtime Prompts Architecture:**
- Skill contains stable frameworks
- Prompts provided at runtime (not embedded)
- Progressive disclosure (load only when needed)
- Enables rapid prompt iteration

### Schema Changes

**Added:**
- `research_designs[]` array
- `methods[]` array
- `protocols[]` array
- Hierarchy relationships (implements_designs, realized_through_protocols)
- Expected_information tracking per RDMAP object
- TIDieR-based completeness checklists

### Reference Materials Added

**New Guides:**
- `tier-assignment-guide.md` - Design/Method/Protocol tier tests
- `consolidation-patterns.md` - Lumping vs splitting guidance
- `expected-information.md` - TIDieR/CONSORT completeness checklists
- `research-design-patterns.md` - Design pattern library

### Testing

**Sobotkova et al. (2023) extraction complete:**
- 159 total objects (balanced extraction)
- 29 RDMAP items (ranked #2 of 7 test runs)
- 81% evidence relationship mapping
- 57% claim relationship coverage

---

## Version 2.3 (2025-10-18)

**Status:** Superseded by v2.4
**Focus:** Consolidation metadata, multi-dimensional evidence pattern

### Major Changes

**Consolidation Metadata:**
- Full traceability of all merges
- `consolidated_from` field (array of original IDs)
- `consolidation_type` taxonomy
- `rationale` for consolidation decision
- `information_preserved` verification

**Multi-Dimensional Evidence:**
- Single evidence item can support multiple claims
- `evidence.supports_claims[]` array (not single reference)
- Bidirectional consistency (evidence ↔ claims)

### Schema Changes

**Added:**
- `consolidation_metadata` object (required for consolidated items)
- Multi-valued cross-reference arrays

**Improved:**
- Verbatim quote requirements
- Location tracking precision
- Extraction confidence vocabulary

---

## Version 2.2 (2025-10-17)

**Status:** Superseded by v2.3
**Focus:** Two-pass workflow, liberal-consolidate philosophy

### Major Changes

**Two-Pass Workflow:**
- Pass 1: Liberal extraction (over-capture by 40-50%)
- Pass 2: Rationalisation (15-20% reduction)
- Pass 3: Validation (new)

**Liberal-Consolidate Philosophy:**
- "When uncertain → extract" (Pass 1 mindset)
- "Consolidate only when assessment impact identical" (Pass 2 acid test)
- Systematic review ensures nothing missed
- Complete traceability via metadata

### Rationale

**Evidence for two-pass approach:**
- RepliCATS project: ~80% accuracy with multi-pass
- Missing items harder to find than consolidating extras
- LLMs better at critique than generation
- Preliminary testing: single-pass showed ~30% lower recall

---

## Version 2.1 (2025-10-17)

**Status:** Superseded by v2.2
**Focus:** Boundary refinements, implicit arguments

### Major Changes

**Implicit Arguments Added:**
- Unstated assumptions
- Logical implications
- Inferential leaps
- Reasoning bridges

**Boundary Refinements:**
- Evidence vs claims distinction clearer
- Tier tests: "Could this be wrong without interpretation being invalid?"
- Case studies added to evidence-vs-claims guide

---

## Version 2.0 (2025-10-16)

**Status:** Superseded by v2.1
**Focus:** Initial claims/evidence extraction

### Major Changes

**Initial Release:**
- Evidence extraction (observations, measurements)
- Claims extraction (interpretations, generalisations)
- Single-pass workflow
- Basic schema (evidence, claims)
- Simple cross-references

---

## Schema Version History

| Version | Date       | Changes |
|---------|------------|---------|
| 2.6     | 2025-11-13 | Infrastructure object, metadata, 7-pass workflow |
| 2.5     | 2025-11-02 | Canonical field names, bidirectional validation |
| 2.4     | 2025-10-20 | RDMAP arrays, 5-pass workflow |
| 2.3     | 2025-10-18 | Consolidation metadata, multi-dimensional evidence |
| 2.2     | 2025-10-17 | Two-pass workflow annotations |
| 2.1     | 2025-10-17 | Implicit arguments array |
| 2.0     | 2025-10-16 | Initial schema (evidence, claims) |

---

## Breaking Changes

### v2.6 → (no breaking changes)

**Additions only:**
- Infrastructure object (optional, backward compatible)
- Pass numbering updated (renumbered but workflow logic unchanged)

### v2.5 → v2.6 (no breaking changes)

**Additions only:**
- Infrastructure object (optional)
- Prompts renumbered (backward compatible)

### v2.4 → v2.5 (field name standardisation)

**Breaking changes:**
- `child_methods` → `implemented_by_methods`
- `child_protocols` → `realized_through_protocols`
- `enables_methods` → `implemented_by_methods`
- `implements_method` → `implements_methods` (plural)
- `supported_by_evidence` → `supported_by` (context clear from field location)

**Migration:** Use `extraction-system/scripts/migrate_field_names.py`

### v2.3 → v2.4 (RDMAP integration)

**Breaking changes:**
- Workflow changed from 3-pass to 5-pass
- Pass numbering updated (Pass 3 Validation → Pass 5 Validation)

**Non-breaking:**
- RDMAP arrays added (empty in v2.3 extractions, compatible)

### v2.2 → v2.3 (consolidation metadata)

**Non-breaking:**
- Consolidation_metadata added (optional field)

### v2.1 → v2.2 (workflow change)

**Non-breaking:**
- Two-pass workflow (procedural change, no schema change)

### v2.0 → v2.1 (implicit arguments)

**Non-breaking:**
- Implicit_arguments array added (empty in v2.0 extractions, compatible)

---

## Future Roadmap

### Planned for v2.7

**Infrastructure Phase 2 Enhancements:**
- Software documentation structure assessment
- Supplementary materials tracking
- Computational environment specification
- Historical trends analysis (PID adoption 2005-2024)

**Prompt Refinements:**
- Decision trees for missing statements (Pass 6)
- Ancient DNA ethics examples (regional variation)
- Book chapter PID handling (ISBNs)
- Multi-component systems guidance

### Under Consideration

**Multi-Run Comparison Study:**
- Quantify extraction variability
- 10 runs on single paper
- Consistency metrics (item overlap, boundary agreement)
- Inform consolidation targets

**Assessment Framework:**
- Transparency scoring rubric
- Replicability evaluation
- Automated scoring algorithms
- Benchmark datasets

**Domain Expansions:**
- Ecology-specific vocabulary
- Ethnography adaptations
- Biology field study patterns
- Geographic research frameworks

**Secondary Source Attribution:**
- `claim_origin` field (novel/tested/supported/synthesised)
- Citation role classification
- Provenance tracking (Phase 2)

---

## Deprecation Policy

**Prompt versions:**
- Previous prompt versions remain available in `archive/prompts-archive/`
- Maintain backward compatibility for 2 versions (current + 1 previous major)
- Breaking changes documented in this file

**Schema versions:**
- Migration scripts provided for breaking changes
- Old extractions remain valid (JSON structure compatible)
- Field renames/additions backward compatible where possible

**Skill versions:**
- Skill located in `.claude/skills/research-assessor/` (version controlled)
- Major changes require user awareness (documented here)
- No forced upgrades (user controls version)

---

## Version Numbering

**Format:** MAJOR.MINOR

**MAJOR version increment:**
- Incompatible schema changes (breaking)
- Workflow changes (pass count/order)
- Prompt architecture changes

**MINOR version increment:**
- Backward-compatible additions (new fields, new passes)
- Prompt refinements (non-breaking)
- Documentation updates (substantial)

**Current:** v2.6 (MAJOR=2, MINOR=6)

---

## Acknowledgements

**Contributors:**
- Primary development: Claude Sonnet 4.5 + human collaboration
- Testing corpus: Sobotkova et al. papers (2016, 2023, 2024), Ballsun-Stanton et al. (2018), Penske et al. (2023)
- Framework influences: TIDieR, CONSORT-Outcomes, SPIRIT, RepliCATS, FAIR4RS

**Informed by:**
- Research transparency initiatives (FAIR, CARE, FAIR4RS)
- Reporting standards (TIDieR, CONSORT, ARRIVE)
- Archaeological field research practices
- Computational reproducibility frameworks

---

**For complete development narrative, see:**
- [architecture.md](architecture.md) - Design rationale
- `archive/documentation-archive/skill-documentation/prompt-revision-summary.md` - Historical prompt evolution
- `planning/active-todo-list.md` - Current development priorities
- `planning/pass6-phase1-testing-findings.md` - Infrastructure testing results
