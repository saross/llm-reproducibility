# Active To-Do List

**Last Updated:** 2025-11-14
**Status:** All high-priority documentation complete (Phases 1-4) - Medium-priority tasks deferred

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

### Deferred Documentation Work
See "Low Priority / Nice to Have" section (Section 9) for:
- Quality metrics documentation
- Troubleshooting guide
- Additional how-to guides

**Current FAIR Score:** 9/15 (Moderately FAIR)
**Path to 15/15:** DOI minting (→14/15) + FAIR vocabularies (→15/15)

---

## Context

RUN-08 successfully achieved all extraction goals:
- ✅ Balanced extraction (159 items, ranked #3 of 7)
- ✅ Strong RDMAP coverage (29 items, ranked #2 of 7)
- ✅ Implicit RDMAP extraction working (5 items)
- ✅ Implicit arguments extraction working (16 items)
- ✅ High relationship mapping (81% evidence, 57% claims)

**Current Focus:** Documentation complete - ready for next major milestone (DOI release, FAIR vocabularies, or corpus expansion)

---

## High Priority

### 1. Repository Documentation

#### 1.1 Main README Improvements ✅ **COMPLETE (2025-11-13)**
**File:** `/home/shawn/Code/llm-reproducibility/README.md`

**Completed:**
- [x] Clear project overview and purpose
- [x] Quick start guide (link to docs/user-guide/getting-started.md)
- [x] Repository structure explanation
- [x] Links to key documentation
- [x] Citation information (CITATION.cff created)
- [x] Licence information (dual licensing badges + section)
- [x] Contribution guidelines reference (CONTRIBUTING.md created)

#### 1.2 Subdirectory README Files ✅ **COMPLETE (2025-11-13)**
**Completed:**

- [x] `extraction-system/README.md` - Overview of extraction workflow components (created 2025-11-13)
- [x] `outputs/README.md` - Explanation of extraction outputs structure (created 2025-11-13)
- [x] `archive/README.md` - Archive organisation and purpose (exists from 2025-10-23)
- [x] `planning/README.md` - Active planning documents (exists from 2025-10-23)
- [x] `reports/README.md` - Types of reports and their purposes (exists from 2025-10-23)
- [x] `examples/README.md` - Example extractions guide (created 2025-11-13)

#### 1.3 Documentation Index ✅ **COMPLETE (2025-11-13)**
**File:** `docs/documentation-index.md`

**Completed:**
- [x] Map of all documentation (18 files across 4 categories)
- [x] Quick navigation guide (by audience)
- [x] Documentation by topic, format, and audience
- [x] Four reading paths (quick start, comprehensive, developer, research)
- [x] Documentation gaps identified
- [x] Link to background research papers

---

### 2. Code Quality - Script Documentation ✅ **COMPLETE (2025-11-14)**

#### 2.1 Production Script Documentation ✅ **COMPLETE**
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

### 3. FAIR4RS Principles Implementation

**Reference:** https://doi.org/10.1038/s41597-022-01710-x

#### 3.1 FAIR4RS Assessment Document ✅ **COMPLETE (2025-11-13)**
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

#### 3.2 Implement FAIR4RS Requirements ✅ **COMPLETE (2025-11-13)**

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

## Medium Priority

### 4. Low-Priority Workflow Improvements

These are optional enhancements to prompts. Implement only if updating prompts for other reasons.

#### 4.1 Fix 4: Reframe Transparency → Content
**File:** `extraction-system/prompts/04-rdmap_pass1b_implicit_prompt.md`
**Location:** "Why This Pass Matters" section (lines 35-45)

**Change:**
Reframe implicit RDMAP from "transparency gap documentation" to "primary content extraction"

**Rationale:** Positions implicit RDMAP as equally important content, improving executor mindset.

**Estimated effort:** 30 minutes

**Status:** OPTIONAL - RUN-08 succeeded with current framing

---

#### 4.2 Improvement 2: Liberal Extraction Mental Model
**Files:** `extraction-system/prompts/01-claims-evidence_pass1_prompt.md` and `03-rdmap_pass1a_explicit_prompt.md`

**Change:**
Add early framing section emphasizing liberal extraction philosophy:
- Pass 1/3 job: CAPTURE (comprehensively)
- Pass 2/5 job: CONSOLIDATE (rationally)
- Rules: When uncertain → extract, when granular → keep separate

**Rationale:** Sets correct mental model for comprehensive extraction.

**Estimated effort:** 30 minutes (both prompts)

**Status:** OPTIONAL - RUN-08 achieved good liberal extraction (62→53 items)

---

#### 4.3 Improvement 3: Relationship Mapping Emphasis
**Files:** `extraction-system/prompts/01-claims-evidence_pass1_prompt.md` and `03-rdmap_pass1a_explicit_prompt.md`

**Change:**
Add relationship mapping discipline section:
- For each item, immediately populate relationship fields
- Map relationships during extraction (not after)
- Understand argumentative structure

**Rationale:** May push relationship mapping from 81% to 90%+

**Estimated effort:** 45 minutes (both prompts)

**Status:** OPTIONAL - RUN-08 achieved 81% evidence mapping, 57% claim coverage

---

### 5. Remove Sobotkova-Specific Metrics from Prompts/Skill

**Priority:** MEDIUM
**Status:** DEFERRED until multi-paper testing phase - awaiting empirical analysis of 10 completed extractions
**Effort:** 3-4 hours audit + 2-3 hours refinement

**Related Analysis:** See `planning/extraction-metrics-guidance-analysis.md` for comprehensive discussion of whether numeric targets help or harm extraction quality (premature stopping vs forced extraction).

**Issue:**
Extraction prompts and skill may contain metrics, targets, or patterns calibrated to Sobotkova et al. 2023 rather than generalisable across diverse fieldwork-based research. Additionally, providing specific numeric targets (e.g., "expect 40-50 claims") may create perverse incentives: premature stopping when targets are reached, or forced extraction of marginal items to hit targets.

**Audit Locations (High Priority):**
- [ ] Prompt 03 (RDMAP Pass 1) - Research Design count guidance
- [ ] Prompt 04 (RDMAP Pass 2) - Consolidation targets
- [ ] Prompt 02 (Claims/Evidence Pass 2) - Consolidation targets
- [ ] references/checklists/expected-information.md - Completeness patterns
- [ ] .claude/skills/research-assessor/SKILL.md - Any metrics/targets

**Audit Locations (Medium Priority):**
- [ ] Prompt 01 - Evidence/claims extraction targets
- [ ] Prompt 05 - Validation thresholds
- [ ] All reference files - Examples and patterns

**Actions Needed:**

**Phase 1: Empirical Analysis (4-6 hours) - NEXT STEP**
- [ ] Extract count distributions from 10 completed papers
- [ ] Quality assessment using rubric: identify goldilocks vs under/over-extracted papers
- [ ] Granularity consistency check using rubric
- [ ] Identify evidence of target-seeking behaviour
- [ ] Decision: Keep ranges with better framing, or remove numeric guidance entirely?

**Assessment Tool:** Use `planning/extraction-assessment-rubric-v1.md` for systematic quality evaluation (Accuracy + Granularity dimensions)

**Phase 2: Implementation (3-4 hours audit + 2-3 hours refinement)**
1. Replace specific numbers with principles (e.g., "Expect 4-6 designs" → "Quality over count - if <3 review for under-extraction, if >10 review for over-extraction")
2. Use multiple paper examples where possible, label sources
3. Base standards on domain knowledge (TIDieR, CONSORT) not single paper
4. Test revised approach on 2-3 new papers to validate

**When:** Phase 1 NOW (10-paper extraction phase complete); Phase 2 after empirical analysis

**Original documentation:** Archived in `archive/planning-completed/future-task-remove-sobotkova-specific-metrics.md`

---

### 5a. Cross-Paper Error Analysis Follow-Up (Phase 2)

**Priority:** MEDIUM
**Status:** ✅ COMPLETE (as of 2025-11-02)
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

---

#### 5a.1 Compound Claim Handling Guidance ✅
**Completed:** 2025-11-02
**Time:** 2 hours

**Files Modified:**
- `.claude/skills/research-assessor/references/checklists/evidence-vs-claims-guide.md` (+440 lines)
  - Added Case 6: Compound Claims with full decision framework
  - Four types: Conjunctive, Comparative, Conditional, Sequential
  - Worked example from sobotkova-et-al-2023 C004
  - Pass 1 vs Pass 2 extraction rules
  - Validation checklist
- `extraction-system/prompts/01-claims-evidence_pass1_prompt.md` (brief reference to Case 6)
- `extraction-system/prompts/02-claims-evidence_pass2_prompt.md` (compound claims review guidance)

**Outcome:** Universal guidance now available in research-assessor skill for handling complex claims with multiple assertions. Prevents context loss errors identified in cross-paper analysis (4 instances).

---

#### 5a.2 Secondary Source Findings Documentation ✅
**Completed:** 2025-11-02
**Time:** 2 hours

**Files Modified:**
- `planning/secondary-source-attribution-analysis.md` (+207 lines empirical findings section)
  - Documented 6 instances of literature review vs empirical misclassification across 4 papers
  - Simple decision tree would prevent 100% of observed errors
  - Evidence does NOT support complex provenance tracking
  - Recommendation: Simple `claim_origin` field (novel/tested/supported/synthesised)

**Outcome:** Empirical findings from 10-paper corpus now documented. Informs future secondary source implementation decisions (Section 6).

---

#### 5a.3 Schema Field Name Standardisation ✅
**Completed:** 2025-11-02
**Time:** 5.5 hours

**Files Created:**
- `extraction-system/scripts/migrate_field_names.py` (434 lines, full migration tool)
- `planning/migration-log.md` (comprehensive documentation)

**Files Modified:**
- `.claude/skills/research-assessor/references/schema/schema-guide.md` (+98 lines)
  - Added "Canonical Field Names (Schema v2.5)" section
  - Documents correct vs deprecated field names
  - Bidirectional consistency requirements
- All 10 `outputs/*/extraction.json` files (376 field name changes across 7 papers)

**Migration Results:**
- Papers migrated: 7/10 (3 already using canonical names)
- Total changes: 376 field name updates
- Post-migration validation: 243 auto-corrections applied, 59 conflicts flagged for human review
- Backup created: `outputs.backup-pre-migration/`

**Canonical field names now enforced:**
- `implemented_by_methods` (not child_methods, enables_methods)
- `implements_designs` (reverse reference)
- `realized_through_protocols` (not child_protocols)
- `implements_methods` plural (not implements_method singular)
- `supported_by` (not supported_by_evidence)

**Outcome:** Schema consistency restored across all 10 extractions. Migration script available for future schema updates. Breaking changes documented in migration-log.md.

---

## Section 5b: Infrastructure Assessment Enhancement (Phase 2)

**Priority:** MEDIUM (Phase 1 complete, Phase 2 planning)
**Status:** ✅ Phase 1 testing COMPLETE (2025-11-11)
**Effort:** Phase 1: 12 hours (complete) | Phase 2: TBD based on findings

**Context:**
Phase 1 infrastructure assessment capability deployed (2025-11-11):
- Created 4 reference files: pid-systems-guide.md, fair-principles-guide.md, fieldwork-permits-guide.md, credit-taxonomy.md
- Integrated FAIR4RS (software-specific FAIR principles) with 5-level computational reproducibility spectrum
- Extended schema with computational_reproducibility object
- Updated Pass 6 and Pass 7 prompts to reference skill files
- Updated research-assessor SKILL.md to document infrastructure capability

**Phase 1 Implementation Included:**
- ✅ Software PIDs (Software Heritage, Zenodo, CodeMeta, swMath, ASCL)
- ✅ Computational reproducibility spectrum (none → code_only → code_dependencies → containerised → fully_reproducible)
- ✅ Environment specification assessment (requirements file, lock file, container, binder)
- ✅ Analysis transparency tracking (random seeds, parameters, workflow, alternatives)
- ✅ Metadata richness framework (DataCite schema, mandatory vs recommended fields)
- ✅ Controlled vocabularies guidance (6 HASS examples: PeriodO, Pleiades, Getty AAT, Darwin Core, CIDOC-CRM, ChronOntology)
- ✅ CARE principles expansion (Collective benefit, Authority to control, Responsibility, Ethics)
- ✅ Machine-actionability definitions and examples
- ✅ Ben Marwick's "built-in vs bolted-on" FAIR heuristic (documented with observable indicators)

**Phase 1 Testing Complete (2025-11-11):**
✅ Tested on 4 diverse papers:
- ✅ Ballsun-Stanton et al. 2018 (SoftwareX) - Software publication, 13/15 FAIR
- ✅ Sobotkova et al. 2024 (J Documentation) - Recent computational paper, 4/15 FAIR
- ✅ Penske et al. 2023 (Nature) - High-profile genomics, 14/15 FAIR
- ✅ Sobotkova et al. 2016 (Book chapter) - Pre-FAIR baseline, 0/15 FAIR

**Findings Documented:** `planning/pass6-phase1-testing-findings.md`
- Extraction challenges: Missing statements, book chapters, ancient DNA ethics, GitHub-only sharing, missing ORCIDs, supplementary materials access
- Guidance gaps: Pre-FAIR era papers, code vs data FAIR divergence, licence taxonomy, multi-component systems
- Schema gaps: Software documentation structure, supplementary materials structure, computational environment specification
- Recommendations: Immediate guidance updates (HIGH), Phase 2 schema enhancements (MEDIUM), deferred enhancements (LOW)

**Phase 2 Actions:**

**Immediate (HIGH Priority) - Guidance Updates:**
1. Update infrastructure prompt (Pass 6): Add decision trees for missing statements, ancient DNA ethics, ORCIDs, supplementary materials
2. Update PID systems guide: Add book chapters/ISBNs, grant identifier formats, SPDX licence identifiers
3. Update FAIR principles guide: Add historical context, code vs data divergence interpretation, GitHub-only vs Zenodo scoring

**Deferred (MEDIUM-LOW Priority) - Schema Enhancements:**
1. Software documentation structure (MEDIUM - requires 10+ paper evidence)
2. Supplementary materials structure (MEDIUM - straightforward, low effort)
3. Computational environment specification (HIGH - critical for reproducibility but design-intensive)
4. Author contributions (LOW - not core to FAIR)
5. Multi-version tracking (DEFERRED indefinitely - out of scope)

**Phase 2 Enhancements Detailed:**

### Potential Additions Based on Testing Outcomes:

**5b.1 Worked Examples from Real Extractions**
- Add concrete extraction examples to each infrastructure reference file based on actual challenges encountered
- Document edge cases and ambiguous scenarios discovered during testing
- Create before/after examples showing common mistakes and corrections

**5b.2 Full FAIR4RS Research Report (If Needed)**
- **Condition:** Deploy only if software assessment shows insufficient depth
- **Scope:** Comprehensive research report on FAIR principles for Research Software (Chue Hong et al. 2022, Barker et al. 2022)
- **Content:** Extended guidance on software citation, version control, testing, documentation, software registries, software management plans
- **Effort:** ~6-8 hours research + documentation
- **Alternative:** Current (~600 word) software FAIR section may be sufficient for HASS papers with modest computational components

**5b.3 "Built-in vs Bolted-on" FAIR Operationalization**
- **Current state:** Heuristic documented in pid-systems-guide.md with observable indicators
- **Challenge:** Temporal integration difficult to assess from published papers alone
- **Future opportunity:** RAiD (Research Activity Identifier) adoption could enable timeline tracking
- **Potential approach:** Develop rubric for assessing integration depth from available signals (acknowledgements, methods narrative, data management plan references)

**5b.4 Software-Specific Replicability Scoring Refinements**
- **Condition:** Deploy if testing shows need for more granular assessment
- **Current:** 5-level computational reproducibility spectrum (0-4)
- **Potential enhancement:** Subscales for environment completeness, workflow documentation, dependency specification quality
- **Risk:** Over-engineering assessment complexity for typical HASS papers
- **Decision point:** Defer until testing corpus reveals genuine need

**5b.5 Cross-Paper PID Adoption Trend Analysis**
- **Requires:** Full corpus extraction complete (all 10+ papers)
- **Analysis:** ORCID coverage over time, DOI adoption curves, software PID emergence, vocabulary PID usage patterns
- **Output:** Empirical baseline for HASS archaeological research (2005-2024)
- **Use case:** Contextualise individual paper scores against discipline norms
- **Effort:** 4-6 hours after full corpus available

**5b.6 Repository-Specific Assessment Guidelines**
- **Condition:** Deploy only if testing corpus shows heavy reliance on specific platforms
- **Candidates:** Zenodo, Figshare, Dryad, GitHub, Software Heritage, tDAR, ADS, Open Context
- **Content:** Platform-specific PID formats, metadata standards, preservation policies, FAIR compliance levels
- **Decision point:** Assess after testing whether general guidance is sufficient or platform-specific knowledge needed

**5b.7 Indigenous Data Governance Case Studies**
- **Condition:** Deploy if CARE principles extraction shows insufficient guidance
- **Current:** General CARE framework in fieldwork-permits-guide.md
- **Enhancement:** Worked examples of CARE-compliant vs non-compliant disclosure
- **Sources:** AIATSIS Code of Ethics cases, OCAP principles examples, Tribal Historical Preservation Offices (THPOs) case studies
- **Effort:** 3-4 hours research + documentation

**5b.8 Software Documentation Assessment Enhancement**
- **Priority:** DEFERRED (Phase 2 - after testing)
- **Status:** Recommendation documented, awaiting testing evidence
- **Documentation:** `planning/pass6-software-documentation-enhancement.md`
- **Context:** Gap identified during Ballsun-Stanton et al. 2018 extraction - documentation is critical for FAIR R1 (Reusability) but lacks systematic assessment structure
- **Proposed enhancement:** Add `documentation` sub-object within `code_availability`:
  - Documentation types taxonomy (readme, api_reference, user_manual, installation_guide, tutorial, etc.)
  - Completeness assessment scale (none → minimal → basic → good → comprehensive)
  - Quality indicators (versioned, includes_examples, machine_readable, citation_cff_present)
  - Accessibility tracking (publicly_accessible, archive_preserved)
- **Questions for testing:** Software creator vs user perspectives, citation patterns, proprietary vs open-source documentation, domain-specific tools
- **Testing phase:** Test on sobotkova-et-al-2024, penske-et-al-2023, sobotkova-et-al-2016 to gather evidence from software user perspective
- **Decision point:** After 4-paper test corpus complete, refine schema based on empirical evidence

**When to Revisit:** After testing Phase 1 implementation on diverse papers and documenting empirical evidence of guidance gaps or assessment limitations.

**Dependencies:**
- Testing phase completion on 3-5 diverse papers
- Documentation of extraction struggles and ambiguities
- User decision on assessment scope and depth requirements

---

## Deferred / Future Projects

### 6. FAIR Vocabularies Development (I2 Compliance)

**Priority:** DEFERRED (post-documentation v2.7)
**Status:** Complete planning document created
**Effort:** 38-58 hours total (3 phases)
**FAIR Impact:** I2: 0/1 → 1/1 | Combined with DOI: 9/15 → 15/15 (Exemplary FAIR)

**Planning Document:** `planning/fair-vocabularies-development-plan.md`

**Overview:**
Development of FAIR-compliant controlled vocabularies for research designs, methods, and protocols using evidence-based approach from 20+ paper corpus extraction. Vocabularies published as SKOS with Zenodo DOIs, integrated via JSON-LD schema enhancement.

**Three-Phase Approach:**
- **Phase 1:** Corpus extraction (20-25 papers across archaeology, ecology, ethnography, field geology) → terminology aggregation → cluster identification (28-38 hours)
- **Phase 2:** SKOS vocabulary creation → Zenodo publication → w3id.org URIs (9-15 hours)
- **Phase 3:** JSON-LD schema integration → prompt updates → validation testing (6-9 hours)

**Deliverables:**
1. Fieldwork Research Designs Vocabulary v1.0 (SKOS + Zenodo DOI)
2. Fieldwork Methods Vocabulary v1.0 (SKOS + Zenodo DOI)
3. Fieldwork Protocols Vocabulary v1.0 (SKOS + Zenodo DOI)
4. Extraction Schema v2.7 with JSON-LD context
5. 20+ paper corpus extractions

**Key Design Decisions:**
- Evidence-based development (bottom-up, not top-down ontology design)
- Empirical scope (terms observed ≥3 times prioritised)
- External alignment (Getty AAT, Darwin Core, ENVO, CIDOC-CRM)
- FAIR vocabularies themselves must be FAIR (15/15 target)

**Timeline:** 5-7 weeks calendar time (Q1 2025 target)

**Current FAIR4RS Score:** 9/15 (Moderately FAIR)
- Vocabularies add I2: +1 point → 10/15
- Combined with DOI minting (F1, F3, F4, A1, A2): +5 points → **15/15 (Exemplary FAIR)**

**When:** After documentation Phases 3-7 complete

---

### 7. Secondary Source Attribution and Role Classification

**Priority:** DEFERRED (long-term project)
**Status:** Awaiting specific assessment goals to drive requirements
**Effort:** TBD (requires methodological design)

**Detailed Analysis:** See `planning/secondary-source-attribution-analysis.md` for comprehensive brainstorming on taxonomy, assessment dimensions, implementation phases, and extraction challenges.

**Issue Summary:**
Current extraction does not systematically distinguish the role of secondary sources (citations to previous work). A cited source can function as:

1. **Evidence supporting a claim in current paper** - "Previous results show X [citation], which supports our interpretation that Y"
2. **Claim being tested/evaluated** - "Smith (2020) claims X, but our new evidence suggests Y"
3. **Background/context** - General citation for established knowledge

**Current State:**
- Citations captured in verbatim_quote fields when they appear in extracted items
- No systematic tracking of citation role or source attribution
- No distinction between primary evidence (generated by current paper) vs secondary evidence (cited from other papers)

**Proposed Approach (from analysis document):**
- Phase 1: Simple optional fields (`source_type`, `claim_origin`) - 6-7 hours
- Phase 2: Structured citation metadata with relationships - 15-18 hours
- Phase 3: Full provenance tracking - 34-44 hours

**Decision point:** Run pilot study (4-6 hours) on 2-3 papers only after assessment framework defines specific needs.

**When:** After Phase 2 (assessment framework development) defines concrete requirements

**Dependencies:**
- Assessment framework design (Phase 2)
- Multi-paper corpus analysis
- Citation context analysis methodology

---

### 8. Multi-Run Extraction Comparison Study

**Priority:** DEFERRED (medium-term project)
**Status:** Awaiting Phase 1 empirical analysis completion and rubric validation
**Effort:** 15-20 hours for 10-run study on single paper + analysis

**Purpose:**
Quantify extraction variability and assess completeness through repeated extractions rather than attempting direct completeness assessment (which requires re-extraction anyway).

**Proposed Approach:**

**Phase 1: Single-Paper Multi-Run Study (8-10 hours)**
- [ ] Select representative paper (medium length, empirical)
- [ ] Run extraction 10 times on same paper (fresh sessions, no memory)
- [ ] Compare outputs using consistency metrics:
  - Items appearing in all runs (high-confidence items)
  - Items appearing in some runs (borderline/inconsistent)
  - Items appearing in one run only (potential over-extraction or missed opportunities)
- [ ] Calculate consistency rate: (Run1 ∩ Run2 ∩ ... ∩ Run10) / (Run1 ∪ Run2 ∪ ... ∪ Run10)
- [ ] Identify high-variance sections/item types

**Phase 2: Cross-Model Comparison (7-10 hours)**
- [ ] Adapt workflow for another model (GPT-4.5, Gemini 2.5 Pro, or different Claude version)
- [ ] Run 3-5 extractions with alternative model
- [ ] Compare inter-model vs intra-model variability
- [ ] Assess if core items are consistent across models

**Metrics to Calculate:**
- **Consistency rate:** How often do runs agree?
- **Coverage variation:** Which sections show high variance?
- **Item stability:** Which item types are most/least consistent?
- **Granularity variation:** Do runs split/merge items differently?

**Expected Insights:**
- Quantify inherent variability in probabilistic extraction
- Identify borderline items (appear in 3-5 runs but not all)
- Validate liberal over-extraction principle (is 40-50% variation normal?)
- Inform completeness expectations (what % agreement is "good enough"?)

**When:** After:
1. Phase 1 empirical analysis (Section 5) validates rubric
2. Rubric pilot test on 1-2 papers confirms assessment methodology
3. Metrics guidance decision (Section 5) informs what to measure

**Dependencies:**
- Validated assessment rubric (planning/extraction-assessment-rubric-v1.md)
- Empirical analysis of 10-paper corpus
- Potential workflow adaptation for cross-model testing

**Subtask:** Adapt extraction workflow for alternative model (skill transfer challenge)

---

## Low Priority / Nice to Have

### 9. Additional Documentation (DEFERRED)

**Status:** All optional documentation deferred until needed
**When:** After broader user testing, corpus expansion, or specific requests

#### 9.1 Extraction Quality Metrics Documentation
**File:** Create `docs/quality-metrics.md`

**Contents:**
- [ ] Definition of quality metrics (items/page, claims:evidence ratio, relationship density)
- [ ] Interpretation guidelines (what constitutes "good" extraction)
- [ ] Comparison methodology (cross-paper benchmarking)
- [ ] Benchmarks from completed extractions (target ranges)
- [ ] Quality assessment rubric integration

**Estimated effort:** 2-3 hours

**Rationale for deferral:** Need broader corpus (20+ papers) to establish meaningful benchmarks. Current metrics in batch-assess.py sufficient for now.

**When to implement:** After FAIR vocabularies corpus extraction (20-25 papers)

---

#### 9.2 Troubleshooting Guide
**File:** Create `docs/troubleshooting.md`

**Contents:**
- [ ] Common extraction issues (PDF conversion, session compaction, JSON errors)
- [ ] Validation failures and fixes (reference errors, duplicate IDs, schema violations)
- [ ] Performance optimization (long papers, complex arguments, RDMAP-heavy papers)
- [ ] Frequently asked questions (FAQ)
- [ ] Error message reference

**Estimated effort:** 2-3 hours

**Rationale for deferral:** Should be built organically from real user issues. extraction-system/scripts/README.md already includes troubleshooting sections for validation scripts.

**When to implement:** After community use begins or when pattern of recurring issues emerges

---

#### 9.3 Additional How-To Guides (DEFERRED)

**Potential guides identified but not yet prioritized:**
- [ ] How to adapt extraction for non-archaeology disciplines (ecology, ethnography)
- [ ] How to extract from methodological papers (no empirical data)
- [ ] How to extract from short papers (<10 pages)
- [ ] How to extract from book chapters (complex structure)
- [ ] How to handle multi-proxy studies (multiple RDMAP hierarchies)

**Estimated effort:** 1-2 hours each (5-10 hours total)

**Rationale for deferral:** Extraction plan unified model (extraction-system/extraction-plan-unified-model.md) provides flexible guidance. Specific how-tos should emerge from actual use cases.

**When to implement:** On-demand when users request specific guidance or when patterns emerge from corpus expansion

---

## Archive Candidates

The following planning documents should be moved to `archive/planning-completed/`:

- `planning/remaining-tasks-summary.md` - Phase 1 complete, superseded by this list
- `planning/future-workflow-improvements.md` - Items extracted to this list, monitoring deferred
- `planning/QA_REMEDIATION_PLAN.md` - Completed per user confirmation
- `planning/schema_improvement_plan.md` - v2.5 complete
- `planning/prompt-to-skill-optimization.md` - Historical, workflow finalized
- `planning/skill-content-assessment.md` - Historical assessment
- `planning/skill-structure-assessment.md` - Historical assessment
- `planning/implicit-arguments-skill-assessment.md` - Assessment complete, workflow working

The following docs should be archived to `archive/docs-obsolete/`:

- `docs/development/repository-reorganization-v2.5.md` - Reorganization complete
- `docs/development/schema-evolution.md` - Historical, could archive
- `docs/schema/schema_crosswalk_v1.1.md` - Old version
- `docs/schema/schema_crosswalk_v1.2.md` - Old version (keep if still referenced)

**KEEP all files in:**
- `docs/background-research/` - Research documentation
- `docs/user-guide/` - Current user documentation
- `docs/skill-documentation/` - Skill documentation

---

## Testing & Validation Queue

After documentation improvements, next steps:

1. **Test on diverse papers:**
   - Different research fields
   - Different transparency levels
   - Different paper lengths

2. **Monitor quality metrics:**
   - Implicit RDMAP extraction consistency
   - Relationship mapping completeness
   - Validation pass rates

3. **Reassess workflow enhancements:**
   - Implement only if real issues emerge
   - Base on evidence, not theory

---

## Success Criteria

### Documentation Complete When: ✅ **ACHIEVED (2025-11-14)**
- [x] All README files created and helpful (7 READMEs created/updated)
- [x] All scripts have comprehensive comments (9 production scripts documented + verified headers)
- [x] FAIR4RS compliance assessed and gaps addressed (9/15 score, roadmap to 15/15)
- [x] New users can onboard using documentation alone (getting-started.md + quick-reference.md)
- [x] Developers understand codebase from comments alone (architecture.md + scripts/README.md)

### Ready for Next Phase When: ✅ **ACHIEVED (2025-11-14)**
- [x] Documentation complete (Phases 1-5 complete)
- [x] FAIR4RS assessment complete (9/15 Moderately FAIR, clear path to 15/15)
- [x] Code quality improved (all production scripts documented)
- [x] Repository professional and shareable (CODE_OF_CONDUCT.md, CONTRIBUTING.md, codemeta.json)
- [x] Ready to expand to diverse papers (workflow documented, validation tools ready)

---

## Effort Summary (FINAL)

**High Priority Total:** 15-18 hours **COMPLETE** ✅
- Repository documentation: 4-6 hours ✅
- Script documentation: 3-4 hours ✅
- FAIR4RS implementation: 4-5 hours ✅
- File naming compliance: 1 hour ✅
- Research Assessor Skill docs: 3-4 hours ✅ (from previous session)

**Medium Priority Total:** 1.75 hours (optional, deferred)
- Workflow improvements: 1.75 hours (optional enhancements)

**Low Priority Total:** 8-14 hours (deferred)
- Quality metrics documentation: 2-3 hours
- Troubleshooting guide: 2-3 hours
- Additional how-to guides: 5-10 hours

**Total Effort Invested:** ~18 hours across 2 sessions (2025-11-13 to 2025-11-14)

---

## Next Major Milestones (Choose One)

**Option A: DOI Release (v3.0 or v0.5)**
- Effort: 2-4 hours
- Mint Zenodo DOI
- Update codemeta.json and CITATION.cff (2 lines each)
- FAIR score impact: 9/15 → 14/15 (Exemplary FAIR)

**Option B: FAIR Vocabularies Development (v2.7)**
- Effort: 38-58 hours over 5-7 weeks
- Extract 20-25 paper corpus
- Build evidence-based SKOS vocabularies
- Publish to Zenodo with DOIs
- FAIR score impact: 9/15 → 10/15 (alone), 9/15 → 15/15 (with DOI)
- Planning: `planning/fair-vocabularies-development-plan.md`

**Option C: Corpus Expansion**
- Effort: 15-20 hours
- Extract 5-10 diverse papers (ecology, ethnography, geology)
- Build evidence base for vocabularies
- Test workflow across disciplines

---

*Last updated: 2025-11-14*

*Status: Active - Post-RUN-08 milestone*

*Next review: After documentation phase complete*
