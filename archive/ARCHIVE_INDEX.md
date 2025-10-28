# Archive Index

**Last Updated:** 2025-10-28

**Purpose:** This archive preserves completed work, historical assessments, and superseded documentation. Items are archived when they are no longer actively used but may have historical or reference value.

---

## Archive Structure

```text
archive/
├── cc-interactions/          # Claude Code conversation logs
├── output/                   # Historical extraction runs (RUN-00 through RUN-07)
│   ├── cc-sonnet45/         # CC autonomous extractions
│   └── chatbot-sonnet45/    # Chatbot-assisted extractions
├── planning-completed/       # Completed planning documents
└── docs-obsolete/           # Superseded documentation
```

---

## Planning Documents - Completed (planning-completed/)

**Archived:** 2025-10-28
**Reason:** Phase 1 implementation complete, RUN-08 milestone achieved

### Workflow Development & Assessment (8 files)

1. **remaining-tasks-summary.md** (15K)
   - Tracked implicit RDMAP & comprehensive extraction tasks
   - Phase 1 (split architecture) complete
   - Phase 2/3 improvements deferred
   - **Status:** Superseded by `planning/active-todo-list.md`

2. **future-workflow-improvements.md** (13K)
   - Deferred improvements from chatbot extraction analysis
   - Identified best practices for quality
   - **Status:** Relevant items moved to active-todo-list.md

3. **QA_REMEDIATION_PLAN.md** (from reports/quality-assurance/)
   - Schema v2.5 updates
   - Verification procedures
   - Documentation standardization
   - **Status:** All tasks confirmed complete by user (2025-10-28)

4. **schema_improvement_plan.md** (26K)
   - Schema v2.5 development plan
   - RDMAP implicit fields
   - Sourcing requirements
   - **Status:** v2.5 implementation complete

5. **prompt-to-skill-optimization.md** (19K)
   - Prompt size reduction strategy
   - Skill vs prompt division analysis
   - **Status:** Architecture finalized, workflow stable

6. **skill-content-assessment.md** (22K)
   - Skill file organization assessment
   - Content placement decisions
   - **Status:** Skill structure finalized

7. **skill-structure-assessment.md** (11K)
   - Skill architecture evaluation
   - Reference file organization
   - **Status:** Structure complete and working

8. **implicit-arguments-skill-assessment.md** (15K)
   - Implicit argument extraction assessment
   - Prompt structure evaluation
   - **Status:** Workflow complete, RUN-08 validated (16 implicit arguments)

---

## Documentation - Obsolete (docs-obsolete/)

**Archived:** 2025-10-28
**Reason:** Superseded by current versions or reorganization complete

### Development Documentation (1 file)

1. **repository-reorganization-v2.5.md** (17K)
   - Repository reorganization completed 2025-10-23
   - FAIR4RS preparation
   - Directory structure rationalization
   - **Status:** Reorganization complete, report archived

### Schema Versions - Old (2 files)

2. **schema_crosswalk_v1.1.md** (18K)
   - Schema v2.3 ontology mappings
   - Last updated: 2025-10-18
   - **Status:** Superseded by `docs/schema/schema_crosswalk_v1.2.md` (schema v2.5)

3. **schema_crosswalk_v1.1_duplicate.md** (formerly schema-evolution.md)
   - Duplicate of v1.1 crosswalk
   - Last updated: 2025-10-18
   - **Status:** Duplicate file, archived to reduce confusion

---

## Historical Extraction Runs (output/)

**Date Range:** 2025-10-23 to 2025-10-28

**Paper:** Sobotkova et al. (2023) - Creating large, high-quality geospatial datasets from historical maps using novice volunteers

### cc-sonnet45/ (Claude Code autonomous extractions)

#### Complete Runs (6 runs)

- **RUN-01** (85 items, 18 RDMAP) - 2025-10-25
- **RUN-02** (112 items, 26 RDMAP) - 2025-10-25
- **RUN-03** (109 items, 20 RDMAP) - 2025-10-26
- **RUN-04** (221 items, 18 RDMAP) - 2025-10-26
- **RUN-05** (275 items, 84 RDMAP) - 2025-10-27
- **RUN-07** (62 items, 26 RDMAP, 14 implicit) - 2025-10-28

#### Incomplete/Failed Runs

- **RUN-00-fail** - Initial attempt with structural issues
- **RUN-06-partial** - Interrupted run

### chatbot-sonnet45/ (Chatbot-assisted extractions)

#### with-skill/ (2 runs)

- **extraction-01** - Earlier test run
- **extraction-02** - Previous best run (64 items, 25 RDMAP)
  - Comparison baseline for RUN-08 evaluation

#### before-skill/

- Early extractions before skill implementation

---

## Current Production Run

**Location:** `outputs/sobotkova-et-al-2023/` (RUN-08)

**Status:** ✅ PRODUCTION-READY

**Results:**
- Total: 159 items (ranked #3 of 7 complete runs)
- RDMAP: 29 items (ranked #2 of 7 runs)
- Implicit RDMAP: 5 items
- Implicit arguments: 16 items
- Evidence mapping: 81%
- Claims with evidence: 57%
- RDMAP hierarchy: 100% complete

**Significance:** First extraction to achieve balanced coverage across all quality metrics.

---

## Archive Maintenance

### When to Archive

**Planning Documents:**
- Tasks completed and verified
- Assessments that informed final decisions
- Plans superseded by implementation

**Documentation:**
- Superseded by newer versions
- Historical reorganization reports
- Old schema versions (keep current + 1 previous)

**Extraction Runs:**
- Completed runs replaced by superior runs
- Failed runs after lessons learned
- Test runs after production runs established

### What NOT to Archive

**Keep Active:**
- Current planning documents
- Active monitoring checklists
- User guides and documentation
- Background research papers
- Most recent schema version + 1 previous
- Production extraction runs
- Comparison reports

---

## Retrieval Information

### To Find Archived Items

**Planning history:**
```bash
ls -lh archive/planning-completed/
```

**Old documentation:**
```bash
ls -lh archive/docs-obsolete/
```

**Historical extractions:**
```bash
ls -lh archive/output/cc-sonnet45/
ls -lh archive/output/chatbot-sonnet45/
```

### To Compare Current vs Historical

**Current extraction:**
```bash
outputs/sobotkova-et-al-2023/extraction.json
```

**Historical comparisons:**
```bash
# vs extraction-02 (chatbot best)
archive/output/chatbot-sonnet45/with-skill/extraction-02/sobotkova_rdmap_pass3_corrected.json

# vs RUN-01 through RUN-07
archive/output/cc-sonnet45/sobotkova-et-al-2023-RUN-*/extraction.json
```

**Comparison reports available:**
```bash
outputs/sobotkova-et-al-2023/comparison-report.md
outputs/sobotkova-et-al-2023/multi-run-comparison.md
```

---

## Version Control Note

All archived items remain in git history. This archive structure provides:
- Clear separation of active vs historical work
- Easy retrieval of past decisions and analyses
- Clean repository structure for new collaborators
- Preservation of development process

---

*Archive maintained by: Shawn & Claude Code*

*Last major update: 2025-10-28 (Post-RUN-08 milestone)*
