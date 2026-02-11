# Completed Milestones Changelog

Detailed records of completed tasks, moved from `active-todo-list.md` to keep
the active list focused. Entries are preserved verbatim from the todo list.

**Extracted:** 2026-02-11

---

## Documentation Milestones Completed (2025-11-13 to 2025-11-14)

**All high-priority documentation tasks complete!**

### Phase 1-2: Repository Documentation ✅ (2025-11-13)
- Main README.md with licence badges and dual licensing section
- 6 subdirectory READMEs (extraction-system, outputs, archive, planning, reports, examples)
- Documentation index (docs/documentation-index.md)

### Phase 3: Research Assessor Skill Documentation ✅ (2025-11-13)
- 7 comprehensive guides in docs/research-assessor-guide/ (148KB)
- Updated from v2.4 (5-pass) to v2.6 (7-pass workflow)

### Phase 4: FAIR4RS Compliance ✅ (2025-11-13)
- Complete FAIR4RS assessment (docs/fair4rs-compliance.md, 41KB)
- Current FAIR score: 9/15 (Moderately FAIR), improved from 7/15
- Metadata infrastructure: codemeta.json, CITATION.cff v2.6, CODE_OF_CONDUCT.md, CONTRIBUTING.md

### Phase 5: Script Documentation ✅ (2025-11-14)
- Comprehensive script documentation (extraction-system/scripts/README.md, 24KB)
- All 9 production scripts documented with usage examples
- batch-assess.py header enhanced
- File naming compliance fixed (DOCUMENTATION_INDEX.md → documentation-index.md, FAIR4RS_COMPLIANCE.md → fair4rs-compliance.md)

### Phase 6: Credibility Metrics Assessment System ✅ (2025-11-15 to 2025-11-16)
- 8 credibility metrics implemented (ESD, TCI, SCS, RTI, RIS, PGCS, FCS, MDD)
- Corpus profile generation with metric statistics and interpretations
- Individual paper scorecards for all 10 papers
- Bug fixes in ESD and SCS calculations
- Location tracking simplified (sentence field removed, section/paragraph requirements clarified)
- Schema v2.5 and skill documentation updated with location requirements
- Comprehensive metrics reference guide (docs/assessment-guide/credibility-metrics-reference.md)

### Reproduction Pilot Programme ✅ (2026-02-09 to 2026-02-10)

**5/5 pilot papers reproduced.** Reproduction-assessor skill upgraded from v1.0 to v1.1.

- Crema et al. 2024: SUCCESSFUL — MCMC re-run on sapphire, all values within HPD intervals
- Marwick 2025: SUCCESSFUL — Docker build-as-render, all statistics matched
- Herskind & Riede 2024: SUCCESSFUL — 291/291 n-gram values exact match
- Dye et al. 2023: SUCCESSFUL — 54/54 Allen algebra values exact match
- Key et al. 2024: PARTIAL — 98.3% match (116/118), 2 discrepancies traced to paper errors, data availability bottleneck (3/13 datasets)

**v1.0 adversarial review** identified 12 issues (3 critical, 5 important, 4 minor). Review committed as `outputs/reproduction-system-review-v1.0.md`.

**v1.1 upgrade** implemented all 12 recommendations:
- 7-category discrepancy classification (CANNOT_COMPARE, PAPER_ERROR added)
- 5-level data access taxonomy and provenance protocol
- Artefact persistence checklists for all sessions
- Scope limitation taxonomy with FAIR implications
- Paper error handling with 5-step verification protocol
- Expanded wrapper script and Dockerfile pattern libraries
- Figure comparison checklist

Project bumped to v2.9, reproduction system to v1.1.

---

## 1. Repository Documentation ✅ **COMPLETE (2025-11-13)**

### 1.1 Main README Improvements
**File:** `/home/shawn/Code/llm-reproducibility/README.md`

**Completed:**
- [x] Clear project overview and purpose
- [x] Quick start guide (link to docs/user-guide/getting-started.md)
- [x] Repository structure explanation
- [x] Links to key documentation
- [x] Citation information (CITATION.cff created)
- [x] Licence information (dual licensing badges + section)
- [x] Contribution guidelines reference (CONTRIBUTING.md created)

### 1.2 Subdirectory README Files
**Completed:**

- [x] `extraction-system/README.md` - Overview of extraction workflow components (created 2025-11-13)
- [x] `outputs/README.md` - Explanation of extraction outputs structure (created 2025-11-13)
- [x] `archive/README.md` - Archive organisation and purpose (exists from 2025-10-23)
- [x] `planning/README.md` - Active planning documents (exists from 2025-10-23)
- [x] `reports/README.md` - Types of reports and their purposes (exists from 2025-10-23)
- [x] `examples/README.md` - Example extractions guide (created 2025-11-13)

### 1.3 Documentation Index
**File:** `docs/documentation-index.md`

**Completed:**
- [x] Map of all documentation (18 files across 4 categories)
- [x] Quick navigation guide (by audience)
- [x] Documentation by topic, format, and audience
- [x] Four reading paths (quick start, comprehensive, developer, research)
- [x] Documentation gaps identified
- [x] Link to background research papers

---

## 2. Code Quality - Script Documentation ✅ **COMPLETE (2025-11-14)**

### 2.1 Production Script Documentation
**File:** `extraction-system/scripts/README.md` (24KB, 728 lines)

**Completed:**
- [x] Comprehensive documentation for all 9 production scripts
- [x] Validation scripts (3): validate_extraction.py, validate_bidirectional.py, check_rdmap_completeness.py
- [x] PDF processing scripts (2): extract_pdf_text.py, pdf_cleaner.py
- [x] Migration scripts (1): migrate_field_names.py
- [x] Template generators (3): section_rdmap_template.py, consolidation_template.py, section_implicit_arguments_template.py
- [x] Batch tools (1): batch-assess.py (header enhanced)
- [x] All scripts verified to have comprehensive header blocks and comments per style guide
- [x] Quick reference table created
- [x] Usage examples with real paths
- [x] Troubleshooting section
- [x] Development guidelines
- [x] Fixed broken link in extraction-system/README.md:136

**Per-Paper Script Policy (DEFERRED - transparency preservation):**
Scripts in `outputs/*/` directories (~101 scripts) are ephemeral working scripts generated during extraction sessions. These are preserved for transparency and reproducibility but not documented as they are paper-specific, non-reusable session artifacts. Long-term archival strategy to be determined later.

---

## 3. FAIR4RS Principles Implementation ✅ **COMPLETE (2025-11-13)**

**Reference:** https://doi.org/10.1038/s41597-022-01710-x

### 3.1 FAIR4RS Assessment Document
**File:** `docs/fair4rs-compliance.md` (41KB, 1240 lines)

**Contents:**
- [x] Assessment against each FAIR4RS principle (all 15 principles)
- [x] Current compliance status (6/15 - Minimally FAIR)
- [x] Gaps identified (5 critical gaps documented)
- [x] Remediation plan (3 priority levels with detailed actions)
- [x] Timeline for full compliance (3-phase roadmap)

**FAIR4RS Principles assessed:**
- **Findable:** F1 (0/1), F2 (0/1), F3 (0/1), F4 (0/1) = 0/4 points
- **Accessible:** A1 (0/1), A1.1 (1/1), A1.2 (1/1), A2 (0/1) = 2/4 points
- **Interoperable:** I1 (1/1), I2 (0/1), I3 (0/1) = 1/3 points
- **Reusable:** R1 (1/1), R1.1 (0/1), R1.2 (1/1), R1.3 (1/1) = 3/4 points

**Key Findings:**
- Current score: 6/15 (Minimally FAIR)
- Target Phase 1: 14/15 (4-6 hours effort - DOI, licence, metadata)
- Target Phase 2: 15/15 (20-40 hours effort - FAIR vocabularies)

### 3.2 Implement FAIR4RS Requirements

**Completed:**
- [x] LICENSE files present (LICENSE-CODE: Apache-2.0, LICENSE-DOCS: CC-BY-4.0 - dual licensing)
- [x] CITATION.cff file created (updated to v2.6, Shawn Graham authorship, placeholder DOI)
- [x] CODE_OF_CONDUCT.md created (Contributor Covenant v2.1 with research ethics additions)
- [x] CONTRIBUTING.md created (comprehensive contribution guidelines, 9 contribution types)
- [x] Software metadata file created (codemeta.json with complete CodeMeta 2.0 metadata)
- [x] README.md updated (licence badges, licence section, citation information)

**Current FAIR Score:** 9/15 (Moderately FAIR)
- F2: Rich metadata (codemeta.json) = +1
- I3: Qualified references (codemeta.json referencePublication) = +1
- R1.1: Clear licence (dual licensing already present, discovered in session) = already 1/1

**Remaining FAIR gaps:**
- F1, F3, F4, A1, A2: Blocked until DOI minted (v3.0/v0.5 release)
- I2: FAIR vocabularies (deferred to v2.7, see planning/fair-vocabularies-development-plan.md)

---

## 5a. Cross-Paper Error Analysis Follow-Up (Phase 2) ✅ **COMPLETE (2025-11-02)**

**Effort:** 9.5 hours total
**Context:** Systematic quality improvements based on cross-paper error analysis of 10 completed extractions

**Completed Tasks (Week 1-2):**
- ✅ Bidirectional validator with auto-correction script
- ✅ JSON Schema validation rules
- ✅ Pass 6 validation prompt integration
- ✅ Bidirectional mapping reminders in prompts
- ✅ Phase 2b/5b consolidation reconciliation workflow
- ✅ Quote completeness requirements in prompts
- ✅ RDMAP completeness checker script

**Completed Tasks (Week 3):**
- ✅ Compound claim handling guidance (5a.1)
- ✅ Secondary source findings documentation (5a.2)
- ✅ Schema field name standardisation (5a.3)

### 5a.1 Compound Claim Handling Guidance ✅
**Completed:** 2025-11-02, **Time:** 2 hours

**Files Modified:**
- `.claude/skills/research-assessor/references/checklists/evidence-vs-claims-guide.md` (+440 lines)
  - Added Case 6: Compound Claims with full decision framework
  - Four types: Conjunctive, Comparative, Conditional, Sequential
  - Worked example from sobotkova-et-al-2023 C004
  - Pass 1 vs Pass 2 extraction rules
  - Validation checklist
- `extraction-system/prompts/01-claims-evidence_pass1_prompt.md` (brief reference to Case 6)
- `extraction-system/prompts/02-claims-evidence_pass2_prompt.md` (compound claims review guidance)

### 5a.2 Secondary Source Findings Documentation ✅
**Completed:** 2025-11-02, **Time:** 2 hours

**Files Modified:**
- `planning/secondary-source-attribution-analysis.md` (+207 lines empirical findings section)

### 5a.3 Schema Field Name Standardisation ✅
**Completed:** 2025-11-02, **Time:** 5.5 hours

**Files Created:**
- `extraction-system/scripts/migrate_field_names.py` (434 lines, full migration tool)
- `planning/migration-log.md` (comprehensive documentation)

**Migration Results:**
- Papers migrated: 7/10 (3 already using canonical names)
- Total changes: 376 field name updates

---

## 8a. Variability Test Findings ✅ **COMPLETE (2025-12-06)**

25/25 runs complete across 5 papers. Classification stability: 100% paper_type consistency, aggregate score CV 1.9-3.4%. Results: `outputs/variability-test/variability-analysis-report.md`.

**Action items remaining (moved to active todo):**
- Mark pipeline "experimental" for literature-based/interpretive studies
- Revisit ross-2005 variability findings
- Document "experimental" flag in assessment outputs

---

## Documentation Success Criteria ✅ **ACHIEVED (2025-11-14)**

- [x] All README files created and helpful (7 READMEs created/updated)
- [x] All scripts have comprehensive comments (9 production scripts documented + verified headers)
- [x] FAIR4RS compliance assessed and gaps addressed (9/15 score, roadmap to 15/15)
- [x] New users can onboard using documentation alone (getting-started.md + quick-reference.md)
- [x] Developers understand codebase from comments alone (architecture.md + scripts/README.md)

## Ready for Next Phase ✅ **ACHIEVED (2025-11-14)**

- [x] Documentation complete (Phases 1-5 complete)
- [x] FAIR4RS assessment complete (9/15 Moderately FAIR, clear path to 15/15)
- [x] Code quality improved (all production scripts documented)
- [x] Repository professional and shareable (CODE_OF_CONDUCT.md, CONTRIBUTING.md, codemeta.json)
- [x] Ready to expand to diverse papers (workflow documented, validation tools ready)

## Effort Summary

**High Priority Total:** 15-18 hours **COMPLETE** ✅
- Repository documentation: 4-6 hours ✅
- Script documentation: 3-4 hours ✅
- FAIR4RS implementation: 4-5 hours ✅
- File naming compliance: 1 hour ✅
- Research Assessor Skill docs: 3-4 hours ✅ (from previous session)

**Total Effort Invested:** ~18 hours across 2 sessions (2025-11-13 to 2025-11-14)

---

## Archive Candidates ✅ **COMPLETE** (verified 2026-02-11)

All 12 archive candidates were moved in prior sessions:

- 8 planning docs → `archive/planning-completed/`
- 3 docs files → `archive/docs-obsolete/`
- 1 file (`docs/development/schema-evolution.md`) — not found anywhere; presumed deleted or never created

---

## Known Gaps — Resolved

- ~~**reproduction-implementation-notes.md**~~ ✅ **RESOLVED** (2026-02-11): Key et al. 2024 gotchas integrated.
- ~~**Output location inconsistency**~~ ✅ **RESOLVED** (2026-02-11): All 5 study papers consolidated under `studies/open-science-compliance/outputs/{slug}/reproduction/`. Added `output_dir` field to queue.yaml entries to prevent recurrence.

---

*Changelog created: 2026-02-11*
