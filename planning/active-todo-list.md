# Active To-Do List

**Last Updated:** 2025-10-28
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
**Status:** DEFERRED until multi-paper testing phase
**Effort:** 3-4 hours audit + 2-3 hours refinement

**Issue:**
Extraction prompts and skill may contain metrics, targets, or patterns calibrated to Sobotkova et al. 2023 rather than generalizable across diverse fieldwork-based research.

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
1. Replace specific numbers with principles (e.g., "Expect 4-6 designs" → "Quality over count - if <3 review for under-extraction, if >10 review for over-extraction")
2. Use multiple paper examples where possible, label sources
3. Base standards on domain knowledge (TIDieR, CONSORT) not single paper
4. Test on 5-10 diverse papers to validate generalizability

**When:** After current 10-paper extraction phase, during multi-paper analysis

**Original documentation:** Archived in `archive/planning-completed/future-task-remove-sobotkova-specific-metrics.md`

---

## Deferred / Future Projects

### 6. Secondary Source Attribution and Role Classification

**Priority:** DEFERRED (long-term project)
**Status:** Awaiting specific assessment goals to drive requirements
**Effort:** TBD (requires methodological design)

**Issue:**
Current extraction does not systematically distinguish the role of secondary sources (citations to previous work). A cited source can function as:

1. **Evidence supporting a claim in current paper** - "Previous results show X [citation], which supports our interpretation that Y"
2. **Claim being tested/evaluated** - "Smith (2020) claims X, but our new evidence suggests Y"
3. **Background/context** - General citation for established knowledge

**Current State:**
- Citations are captured in verbatim_quote fields when they appear in extracted items
- No systematic tracking of citation role or source attribution
- No distinction between primary evidence (generated by current paper) vs secondary evidence (cited from other papers)

**Future Requirements (to be determined by assessment goals):**
- [ ] Define citation role taxonomy (evidence/claim/background/other)
- [ ] Determine if secondary source metadata should be structured (author, year, DOI)
- [ ] Decide if cited claims need separate extraction from paper's own claims
- [ ] Consider provenance tracking (chain of evidence across papers)
- [ ] Assess impact on credibility/transparency assessment framework

**Implementation Approach:**
- Assessment-driven: Specific assessment needs will define schema requirements
- May require schema extension (e.g., `citation_role`, `source_type`, `cited_work` fields)
- Could leverage existing citation extraction tools/APIs
- Test on pilot papers with heavy citation use

**When:** After Phase 2 (assessment framework development) defines concrete requirements

**Dependencies:**
- Assessment framework design (Phase 2)
- Multi-paper corpus analysis
- Citation context analysis methodology

---

## Low Priority / Nice to Have

### 7. Additional Documentation

#### 7.1 Extraction Quality Metrics Documentation
**File:** Create `docs/QUALITY_METRICS.md`

**Contents:**
- [ ] Definition of quality metrics
- [ ] Interpretation guidelines
- [ ] Comparison methodology
- [ ] Benchmarks from RUN-08

**Estimated effort:** 1-2 hours

**Status:** DEFERRED - Focus on core documentation first

---

#### 7.2 Troubleshooting Guide
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
