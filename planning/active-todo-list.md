# Active To-Do List

**Last Updated:** 2025-11-02
**Status:** Post-RUN-08 milestone - Production-ready workflow

---

## Context

RUN-08 successfully achieved all extraction goals:
- ✅ Balanced extraction (159 items, ranked #3 of 7)
- ✅ Strong RDMAP coverage (29 items, ranked #2 of 7)
- ✅ Implicit RDMAP extraction working (5 items)
- ✅ Implicit arguments extraction working (16 items)
- ✅ High relationship mapping (81% evidence, 57% claims)

**Current Focus:** Documentation, code quality, and FAIR4RS compliance before expanding to new papers.

---

## High Priority

### 1. Repository Documentation

#### 1.1 Main README Improvements
**File:** `/home/shawn/Code/llm-reproducibility/README.md`

**Needs:**
- [ ] Clear project overview and purpose
- [ ] Quick start guide (link to docs/user-guide/getting-started.md)
- [ ] Repository structure explanation
- [ ] Links to key documentation
- [ ] Citation information
- [ ] License information
- [ ] Contribution guidelines reference

**Estimated effort:** 1-2 hours

#### 1.2 Subdirectory README Files
**Create README.md files for:**

- [ ] `extraction-system/README.md` - Overview of extraction workflow components
- [ ] `outputs/README.md` - Explanation of extraction outputs structure
- [ ] `archive/README.md` - Archive organization and purpose
- [ ] `planning/README.md` - Active planning documents (update existing if present)
- [ ] `reports/README.md` - Types of reports and their purposes
- [ ] `scripts/README.md` - Utility scripts documentation (if not covered elsewhere)

**Estimated effort:** 2-3 hours total

#### 1.3 Documentation Index
**File:** Create `docs/DOCUMENTATION_INDEX.md`

**Contents:**
- [ ] Map of all documentation
- [ ] When to use which document
- [ ] Documentation for users vs developers vs researchers
- [ ] Link to background research papers

**Estimated effort:** 1 hour

---

### 2. Code Quality - Script Documentation

#### 2.1 Python Script Comments
**Files to improve:**

```bash
outputs/sobotkova-et-al-2023/*.py
```

**For each script, ensure:**
- [ ] Comprehensive module docstring explaining purpose
- [ ] Function docstrings with parameters and return values
- [ ] Inline comments for non-obvious code sections
- [ ] Example usage in docstring
- [ ] Error handling documentation

**Scripts to document:**
- [ ] `execute_pass2.py` - Pass 2 conservative rationalization
- [ ] `execute_pass3.py` - Explicit RDMAP extraction
- [ ] `execute_pass4.py` - Implicit RDMAP scanning
- [ ] `execute_pass5.py` - RDMAP rationalization & relationship verification
- [ ] `execute_pass6.py` - Validation
- [ ] `fix_references.py` - Cross-reference repair
- [ ] `generate_summary.py` - Summary generation
- [ ] `compare_extractions.py` - Comparison to extraction-02
- [ ] `compare_all_runs.py` - Multi-run comparison
- [ ] `analyze_pass1.py` - Pass 1 analysis (if exists)

**Standard comment structure:**
```python
#!/usr/bin/env python3
"""
[Script Name] - [One-line purpose]

Detailed description of what this script does, when to use it,
and how it fits into the overall extraction workflow.

Usage:
    python3 script_name.py

Input:
    - extraction.json (current state)
    - [other inputs]

Output:
    - extraction.json (updated)
    - [other outputs]

Pass Context:
    This script implements Pass [N] of the 7-pass extraction workflow.
    [Brief explanation of this pass's role]

Author: [if applicable]
Date: [creation date]
"""
```

**Estimated effort:** 3-4 hours (30 min per script × 10 scripts)

---

### 3. FAIR4RS Principles Implementation

**Reference:** https://doi.org/10.1038/s41597-022-01710-x

#### 3.1 FAIR4RS Assessment Document
**File:** Create `docs/FAIR4RS_COMPLIANCE.md`

**Contents:**
- [ ] Assessment against each FAIR4RS principle
- [ ] Current compliance status
- [ ] Gaps identified
- [ ] Remediation plan
- [ ] Timeline for full compliance

**FAIR4RS Principles to assess:**
- **Findable:** F1 (unique identifier), F2 (metadata), F3 (indexed), F4 (registered)
- **Accessible:** A1 (retrievable), A2 (metadata persistence)
- **Interoperable:** I1 (data exchange), I2 (vocabularies), I3 (references)
- **Reusable:** R1 (metadata), R2 (provenance), R3 (standards), R4 (license)

**Estimated effort:** 2-3 hours

#### 3.2 Implement FAIR4RS Requirements
**Based on assessment, likely needs:**

- [ ] Add LICENSE file (if not present)
- [ ] Add CITATION.cff file
- [ ] Add CODE_OF_CONDUCT.md
- [ ] Add CONTRIBUTING.md (or improve existing)
- [ ] Add software metadata file (codemeta.json or similar)
- [ ] Improve provenance documentation in outputs
- [ ] Document dependencies clearly (requirements.txt, environment.yml)
- [ ] Add version information to outputs
- [ ] Document data formats and schemas

**Estimated effort:** 3-4 hours

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

**Priority:** DEFERRED (Phase 2 - after testing)
**Status:** Awaiting empirical grounding from Phase 1 testing on diverse papers
**Effort:** TBD based on testing outcomes and identified gaps

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

**Testing Phase (Immediate Next Step):**
Test Phase 1 implementation on 3-5 diverse papers:
- [ ] Recent (2023-2024) with PIDs/data availability statements
- [ ] Mid-period (2016-2019) transition era papers
- [ ] Pre-2016 minimal infrastructure papers
- [ ] Fieldwork-heavy paper (permits, CARE principles relevant)
- [ ] Computational paper (code/software PIDs, reproducibility relevant)

**Document extraction struggles and identify:**
- Which guidance is insufficient or unclear?
- Which examples are needed but missing?
- Which scoring criteria are ambiguous?
- Which assessment dimensions are too simplistic or too complex?

**Phase 2 Enhancements (Deferred Pending Testing Evidence):**

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

**When to Revisit:** After testing Phase 1 implementation on diverse papers and documenting empirical evidence of guidance gaps or assessment limitations.

**Dependencies:**
- Testing phase completion on 3-5 diverse papers
- Documentation of extraction struggles and ambiguities
- User decision on assessment scope and depth requirements

---

## Deferred / Future Projects

### 6. Secondary Source Attribution and Role Classification

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

### 7. Multi-Run Extraction Comparison Study

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

### 8. Additional Documentation

#### 8.1 Extraction Quality Metrics Documentation
**File:** Create `docs/QUALITY_METRICS.md`

**Contents:**
- [ ] Definition of quality metrics
- [ ] Interpretation guidelines
- [ ] Comparison methodology
- [ ] Benchmarks from RUN-08

**Estimated effort:** 1-2 hours

**Status:** DEFERRED - Focus on core documentation first

---

#### 8.2 Troubleshooting Guide
**File:** Create `docs/TROUBLESHOOTING.md`

**Contents:**
- [ ] Common extraction issues
- [ ] Validation failures and fixes
- [ ] Performance optimization
- [ ] FAQ

**Estimated effort:** 2 hours

**Status:** DEFERRED - Build from real issues as they arise

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

### Documentation Complete When:
- [ ] All README files created and helpful
- [ ] All scripts have comprehensive comments
- [ ] FAIR4RS compliance assessed and gaps addressed
- [ ] New users can onboard using documentation alone
- [ ] Developers understand codebase from comments alone

### Ready for Next Phase When:
- [ ] Documentation complete
- [ ] FAIR4RS compliant
- [ ] Code quality improved
- [ ] Repository professional and shareable
- [ ] Ready to expand to diverse papers

---

## Effort Summary

**High Priority Total:** 11-15 hours
- Repository documentation: 4-6 hours
- Script comments: 3-4 hours
- FAIR4RS implementation: 4-5 hours

**Medium Priority Total:** 1.75 hours (optional)
- Workflow improvements: 1.75 hours (optional enhancements)

**Low Priority Total:** 3-4 hours (deferred)

**Grand Total (High Priority):** 11-15 hours of focused work

---

## Recommended Schedule

**Week 1: Documentation Foundation**
- Main README improvements
- Subdirectory READMEs
- Documentation index

**Week 2: Code Quality**
- Script documentation
- Comment improvements
- Code cleanup

**Week 3: FAIR4RS Compliance**
- Assessment
- Gap remediation
- Metadata files

**Week 4: Review & Polish**
- Test documentation with fresh eyes
- Fix any gaps
- Prepare for broader sharing

---

*Last updated: 2025-10-28*

*Status: Active - Post-RUN-08 milestone*

*Next review: After documentation phase complete*
