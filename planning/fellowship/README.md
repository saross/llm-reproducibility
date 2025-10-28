# CWTS Fellowship Planning

**Purpose:** This directory contains strategic planning documents for the broader research fellowship context that informed the development of this extraction workflow.

**Relationship to extraction workflow:** The extraction system developed in this repository is a foundational component of the larger fellowship research project described in these documents.

---

## Contents

### 1. cwts_implementation_plan.md (34K)

**Created:** 2025-10-16

**Purpose:** Comprehensive implementation plan for CWTS Fellowship (September 2025 - February 2026)

**Scope:**
- Strategic assets and implementation architecture
- Multi-model consensus development
- Validation strategy (CWTS expert feedback, domain expertise, formal panel)
- Development environment and documentation approach
- Critical path: extraction-first strategy

**Key Insight:** Six-month timeline depends on achieving reliable Claim-Evidence-Method graph extraction by Month 2. All subsequent assessment work builds upon this foundation.

**Relevance:** Provides research context for why this extraction workflow exists and what it enables.

---

### 2. implementation_plan_supplement.md (5.6K)

**Created:** 2025-10-16

**Purpose:** Strategic decisions and context for extraction prototype development

**Contents:**
- Copyright and access strategy (co-authored papers, open access)
- Multilingual development pathway (English first, then expand)
- Community engagement plan (CAA-Australasia)
- Publication strategy for marginal/negative results
- CLIO investigation decision (deferred pending empirical validation)

**Relevance:** Captures strategic clarifications that informed extraction workflow design decisions.

---

## Relationship to Active Planning

**Active workflow planning:** See `planning/active-todo-list.md`

**Fellowship planning (this folder):** Provides broader research context but doesn't contain immediate actionable workflow tasks.

**Archive:** Completed workflow planning is in `archive/planning-completed/`

---

## Current Status

### Extraction Workflow Status
✅ **Production-ready** (as of RUN-08, 2025-10-28)

The extraction system has achieved all foundational goals:
- Balanced coverage across all categories (159 items, ranked #3 of 7)
- Strong RDMAP extraction (29 items, ranked #2 of 7)
- Implicit RDMAP extraction working (5 items)
- Implicit arguments extraction working (16 items)
- High relationship mapping (81% evidence, 57% claims)
- Complete RDMAP hierarchy (100%)

### Fellowship Timeline Context

The fellowship implementation plan anticipated "reliable Claim-Evidence-Method graph extraction by Month 2" as the critical milestone.

**Actual progress:** Achieved ahead of schedule. The extraction workflow is production-ready and can now support the broader assessment work described in the fellowship plan.

**Next steps (per fellowship plan):**
- Expand to diverse papers (different fields, transparency levels)
- Validate generalizability across HASS domains
- Begin assessment layer development (repliCATS Seven Signals adaptation)

---

## Using These Documents

**When to reference:**
- Understanding broader research goals
- Contextualizing extraction workflow design decisions
- Planning next phases of fellowship work
- Explaining project scope to collaborators

**When NOT to reference:**
- Immediate workflow to-do items (use `planning/active-todo-list.md`)
- Day-to-day extraction work (use `docs/user-guide/`)
- Skill development (use `extraction-system/skill/`)

---

*This directory separates strategic fellowship planning from operational workflow planning, making it easier to focus on immediate tasks while preserving broader research context.*
