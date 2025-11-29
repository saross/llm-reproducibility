# Development Archive

Complete development history of the LLM-based Research Extraction and Assessment project, organized chronologically by version.

**Active System:** v2.6 (see [main README](../README.md))
**Archive Purpose:** Preserve development transparency and enable understanding of design decisions

---

## Development Timeline

### Phase 1: Extraction System Development (Oct 16 - Nov 2025)

```text
v2.0-v2.1 → v2.2-v2.3 → v2.4 → v2.5 → v2.6
   ↓           ↓         ↓       ↓       ↓
 Claims/   Two-Pass   RDMAP   Repository  Infrastructure
Evidence  Workflow  Addition  Rationalisation + Assessment
```

---

## Version History

### [v2.0-v2.1](extraction-development/v2.0-v2.1/) (Oct 16, 2025)

**Focus:** Initial claims and evidence extraction

**Key Developments:**
- First extraction schema with evidence, claims, implicit arguments
- Single-pass extraction approach
- Simple cross-reference system
- Professional judgment boundary framework

**Archived Materials:**
- **Planning:**
  - `quick_start_extraction_guide.md` - Initial rapid prototyping guide
  - `claims_extraction_project_plan.md` - Early project planning

**Rationale:**
Quick proof-of-concept to validate that LLM-based extraction could work. Established basic object types and extraction patterns.

**What We Learned:**
- Single-pass extraction insufficient for quality
- Need for over-capture then rationalize approach
- Evidence/claim boundary challenging but manageable

---

### [v2.2-v2.3](extraction-development/v2.2-v2.3/) (Oct 17-18, 2025)

**Focus:** Two-pass workflow with consolidation

**Key Developments:**
- Pass 1: Liberal extraction (over-capture strategy)
- Pass 2: Rationalization (consolidation and refinement)
- Consolidation metadata for traceability (v2.3)
- Multi-dimensional evidence pattern (v2.3)
- 15-20% reduction target through Pass 2

**Archived Materials:**
- **Planning:**
  - `extraction_decisions_synopsis.md` - Core framework decisions
  - `decisions_doc_update.md` - v2.3 updates
- **Documentation:**
  - `claims-pass1-revision-explanation.md` - Pass 1 prompt design
  - `claims-pass2-revision-explanation.md` - Pass 2 prompt design
  - `prompt_revision_summary.md` - Overall prompt development
- **Reports:**
  - Various testing and refinement reports

**Rationale:**
Single-pass produced too many overlapping items. Two-pass workflow allows comprehensive capture without sacrificing quality. Consolidation metadata ensures traceability.

**What We Learned:**
- Over-capture then refine more reliable than single-pass precision
- Consolidation patterns repeatable across papers
- Metadata essential for transparency
- Multi-dimensional evidence needed for complex observations

---

### [v2.4](extraction-development/v2.4/) (Oct 19-20, 2025)

**Focus:** RDMAP extraction framework

**Key Developments:**
- Added research_designs, methods, protocols object types
- Three-tier hierarchy (Strategic WHY → Tactical WHAT → Operational HOW)
- Unified validation (Pass 3)
- Expected information checklists (TIDieR, CONSORT-Outcomes)
- Fieldwork-specific adaptations
- Skill + runtime prompts architecture

**Archived Materials:**
- **Planning:**
  - `rdmap_implementation_doc.md` - Complete RDMAP design decisions
  - `RDMAP-Prompt-Correction-Plan.md` - Correction task plan
- **Documentation:**
  - `rdmap-pass1-revision-explanation.md` - Pass 1 design
  - `rdmap-pass2-revision-explanation.md` - Pass 2 design
  - `rdmap_prompts_summary.md` - RDMAP overview
- **Reports:**
  - `RDMAP_Pass1_Extraction_Summary.md` - Pass 1 results
  - `RDMAP_Pass2_Rationalization_Summary.md` - Pass 2 results
  - Various correction and testing reports

**Rationale:**
Claims/evidence insufficient for assessing transparency. Need explicit extraction of methodology: designs (strategic rationale), methods (tactical approaches), protocols (operational details).

**What We Learned:**
- Three-tier hierarchy maps well to methodological reasoning
- Registration frameworks (TIDieR, CONSORT) adaptable for retrospective extraction
- Fieldwork epistemology distinct from lab/clinical research
- Skill + runtime prompts better than embedded prompts

---

### [v2.5](extraction-development/v2.5/) (Oct 23, 2025)

**Focus:** Repository rationalization and FAIR4RS preparation

**Key Developments:**
- Reorganized repository structure (extraction-system/, docs/, etc.)
- Dual licensing (Apache 2.0 code, CC-BY-4.0 docs)
- CITATION.cff and CHANGELOG.md
- Comprehensive documentation overhaul
- Navigation READMEs at all levels
- Archived development history by version

**Archived Materials:**
- **Documentation:**
  - `verification-procedures_with_RDMAP.md` - Validation procedures
  - `Pass3_Consolidation_Report.md` - Pass 3 testing
  - `Consolidation_Summary.md` - Consolidation results
  - Various schema and update summaries
- **Reports:**
  - `PHASE_1_COMPLETE_SUMMARY.md` - Extraction phase completion
  - `TASK_1.4_SKILL_REFERENCE_STANDARDIZATION.md` - Task report
  - `TASK_1.5_PASS3_SKILL_INVOCATION.md` - Task report
  - `TASK_1.7_QUALITY_CHECKLIST_STANDARDIZATION.md` - Task report
  - `PACKAGING_COMPLETE.md` - Skill packaging
  - Various correction, schema, and investigation reports

**Rationale:**
Extraction system complete and tested. Prepare for sharing with collaborators and broader community. FAIR4RS compliance preparation for near-term publication/archiving.

**What We Learned:**
- Clear organisation essential for collaboration
- Development transparency valuable but needs structure
- Active planning vs. completed work separation important
- Documentation at every level aids navigation

---

### v2.6 (Nov 2025)

**Focus:** Infrastructure extraction and assessment framework development

**Key Developments:**
- Pass 6: Infrastructure extraction (PIDs, FAIR assessment, funding, permits)
- 8-pass workflow complete (Pass 0-7)
- Assessment framework development (Three Pillars, Seven Signals)
- Research approach classification (inductive, deductive, abductive)
- Cluster-based assessment prompts (Clusters 1-3)
- Terminology standardisation ("replicability" → "reproducibility")

**Archived Materials:**
- **Planning (planning-completed/):**
  - `assessment-implementation-plan.md` - Initial assessment planning
  - `credibility-implementation-plan-detailed.md` - Detailed credibility plan
  - `research-approach-classification-framework.md` - Classification framework
  - `synthesis-external-feedback.md` - GPT-4 and other model feedback
  - `gpt51-feedback/` - GPT-5.1 feedback documents
  - Plus 9 additional superseded planning documents

- **Corpus Profiles (corpus-profiles/):**
  - 6 timestamped corpus profile versions (keeping latest in outputs/)

- **Outputs Backup (outputs-backup-pre-migration/):**
  - Pre-migration backup of extraction outputs

**Rationale:**
Complete extraction pipeline with infrastructure assessment. Begin transition to assessment phase with Three Pillars framework (Transparency → Credibility → Reproducibility).

**What We Learned:**
- Infrastructure extraction critical for reproducibility assessment
- Methodological papers need alternate assessment pathways
- repliCATS Seven Signals adaptable to HASS disciplines
- Quality gating prevents misleading assessments on low-quality extractions

---

## Archive Organisation

```text
archive/
├── extraction-development/    # Version-organised development
│   ├── v2.0-v2.1/
│   │   └── planning/
│   ├── v2.2-v2.3/
│   │   ├── planning/
│   │   ├── documentation/
│   │   └── reports/
│   ├── v2.4/
│   │   ├── planning/
│   │   ├── documentation/
│   │   └── reports/
│   └── v2.5/
│       ├── documentation/
│       └── reports/
├── planning-completed/        # Superseded planning documents (v2.6)
│   ├── assessment-implementation-plan.md
│   ├── credibility-*.md files
│   ├── gpt51-feedback/
│   └── [13+ planning docs]
├── corpus-profiles/           # Archived corpus profile versions
├── outputs-backup-pre-migration/  # Pre-migration outputs backup
├── outputs/                   # Test extractions
│   ├── before-skill/
│   └── with-skill/
├── superseded-prompts/        # Old prompt versions
└── superseded-docs/           # Obsolete documentation
```

---

## Archive Contents

### Planning Documents
**Purpose:** Capture design decisions and strategic direction for each development phase

**Contains:**
- Conceptual frameworks
- Schema improvement plans
- Implementation strategies
- Correction plans

### Documentation
**Purpose:** Explain revisions, updates, and technical changes

**Contains:**
- Revision explanations for prompts
- Update summaries
- Verification procedures
- Consolidation reports

### Reports
**Purpose:** Document development progress, testing, and task completion

**Contains:**
- Pass testing summaries
- Task completion reports
- Correction summaries
- Investigation findings
- Phase milestone reports

### Outputs
**Purpose:** Preserve test extractions showing system evolution

**Contains:**
- **before-skill/**: Early extraction attempts (pre-v2.0)
- **with-skill/**: Iterative development extractions (v2.0-v2.4)

### Superseded Materials
**Purpose:** Preserve obsolete but historically significant items

**Contains:**
- Old prompt versions
- Replaced documentation
- Deprecated schemas

---

## Using the Archive

### For Understanding Design Decisions

**"Why does the system work this way?"**
1. Start with the relevant version in `extraction-development/`
2. Read planning documents for strategic rationale
3. Review documentation for technical details
4. Check reports for empirical validation

**Example:** Understanding two-pass workflow
→ See `v2.2-v2.3/planning/extraction_decisions_synopsis.md`

### For Tracking Feature Evolution

**"How did RDMAP extraction develop?"**
→ See `v2.4/planning/rdmap_implementation_doc.md` + documentation + reports

**"How has the schema changed?"**
→ Compare across versions, see [docs/development/schema-evolution.md](../docs/development/schema-evolution.md)

### For Learning from Iterations

**"What didn't work and why?"**
- Correction reports show issues found and fixed
- Investigation reports trace problem resolution
- Testing reports compare approaches

---

## Key Design Decisions (Cross-Version)

### Evidence vs. Claims Distinction
**Established:** v2.0
**Refined:** v2.1, v2.2
**Archive:** `v2.2-v2.3/planning/extraction_decisions_synopsis.md`

### Two-Pass Workflow
**Established:** v2.2
**Archive:** `v2.2-v2.3/planning/`
**Rationale:** Over-capture then rationalize > single-pass precision

### Consolidation Metadata
**Added:** v2.3
**Archive:** `v2.2-v2.3/documentation/`
**Rationale:** Traceability essential for transparency assessment

### RDMAP Framework
**Added:** v2.4
**Archive:** `v2.4/planning/rdmap_implementation_doc.md`
**Rationale:** Methodology extraction needed for transparency assessment

### Three-Tier Hierarchy
**Established:** v2.4
**Archive:** `v2.4/`
**Rationale:** Design (WHY) → Methods (WHAT) → Protocols (HOW) maps to methodological reasoning

### Fieldwork Adaptations
**Established:** v2.4
**Archive:** `v2.4/planning/rdmap_implementation_doc.md`
**Rationale:** Fieldwork epistemology differs from lab/clinical research

---

## Development Metrics

### Iteration Speed
- **v2.0 → v2.1**: 1 day (refinement)
- **v2.1 → v2.2**: 1 day (major architecture change)
- **v2.2 → v2.3**: 1 day (enhancement)
- **v2.3 → v2.4**: 2 days (major expansion)
- **v2.4 → v2.5**: 3 days (reorganization)

### Schema Growth
- **v2.0**: 3 object types (evidence, claims, implicit_arguments)
- **v2.4**: 6 object types (+research_designs, +methods, +protocols)
- **v2.5**: No new object types (organizational release)

### Prompt Evolution
- **v2.0**: 1 extraction prompt (~400 lines)
- **v2.2**: 2 prompts (~1,700 lines total)
- **v2.4**: 5 prompts (~4,400 lines total)
- **v2.5**: 5 prompts (same content, reorganized repository)

### Testing Progression
- **v2.0-v2.1**: Proof of concept on Methods section
- **v2.2-v2.3**: Full paper extraction with validation
- **v2.4**: Complete RDMAP extraction with Pass 3 validation
- **v2.5**: Comprehensive QA and skill validation

---

## Lessons Learned

### Process
- **Iterate rapidly**: 1-3 day cycles enabled quick learning
- **Test on real papers**: Sobotkova paper provided realistic complexity
- **Document decisions**: Planning docs essential for consistency
- **Preserve history**: Archive enables learning from iterations

### Technical
- **Over-capture then refine** works better than single-pass precision
- **Metadata essential** for traceability
- **Three-tier hierarchy** maps well to methodological reasoning
- **Fieldwork-specific** adaptations necessary
- **Skill + runtime prompts** more flexible than embedded

### Organizational
- **Active vs. archived** distinction crucial
- **Version-based organization** clearer than chronological
- **Navigation READMEs** at every level aid usability
- **Development transparency** valuable but needs structure

---

## Related Documentation

- [Main README](../README.md) - Current system overview
- [Version History](../docs/research-assessor-guide/version.md) - Complete changelog
- [CHANGELOG](../CHANGELOG.md) - Project changelog
- [Planning](../planning/) - Active planning for future work

---

## Contributing to the Archive

The archive is complete for extraction development (v2.0-v2.6). Future assessment framework development will be documented in new version folders.

**Assessment Phase (in progress):**
- v2.6: Infrastructure extraction and assessment framework development
- v2.7+: Complete assessment system, batch processing
- New archive structure as assessment phase completes

---

**Exploring development history?** Start with a version folder matching your interest, then read planning → documentation → reports for complete context.
