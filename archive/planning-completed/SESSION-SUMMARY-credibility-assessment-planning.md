# Session Summary: Credibility Assessment Planning
## Ready for Implementation (2025-11-16)

**Context:** Recovered from VS Code crash, completed comprehensive planning for individual paper credibility assessment system.

---

## Planning Documents Created (3 documents, 43KB total)

### 1. `paper-credibility-analysis-framework.md` (v2.0, 24KB)
**Fundamental design decisions - ALL 20 QUESTIONS ANSWERED**

**Core decisions:**
- Individual papers as assessment target (not corpus aggregates)
- Maximum Claude automation (autonomous workflow)
- Research approach flexibility (inductive/deductive/abductive-specific criteria)
- 3-5 page summary reports initially
- RepliCATS alignment for external validation
- Two-track analysis: extraction quality (Track A) vs paper credibility (Track B)
- Approach-specific credibility definitions

**Key innovations:**
- **Expressed vs revealed approach** classification with HARKing detection
- **"No expressed method" as significant** indicator of weak research design
- **Continuous quality monitoring** (Track A runs alongside Track B with reducing overhead)
- **Explicit repliCATS divergences** documented for HASS adaptations

---

### 2. `research-approach-classification-framework.md` (16KB)
**Complete classification methodology - implementation-ready**

**Key features:**
- Classify after extraction (Pass 6.5 or early Pass 7)
- Dual classification: expressed (what paper says) vs revealed (what paper does)
- HARKing detection (mismatch between expressed/revealed)
- Qualitative mixed-method characterisation (no false precision)
- Structured YAML output schema

**Critical insight:** Absence of methodological statement = significant transparency weakness

---

### 3. `credibility-assessment-implementation-roadmap.md` (13KB)
**5-phase implementation plan (17-24 hours total effort)**

**Phases:**
1. Research approach classification (3-4 hours)
2. Universal signal rubrics (4-6 hours)
3. Pilot single-paper assessment (4-5 hours)
4. Iterative refinement (4-6 hours)
5. Documentation & integration (2-3 hours)

---

## All Design Questions Resolved (17/17 answered, 3 deferred to implementation)

### Classification (Q1-Q4): ✅
- After extraction (Pass 6.5/early Pass 7)
- Contextual inference with expressed vs revealed
- Qualitative mixed-method characterisation
- Iterative empirical validation

### Assessment Framework (Q5-Q7): ✅
- Narrative importance + experimental weights
- 7 universal rubrics, fork if needed empirically
- Assess all seven signals (repliCATS compatibility)

### Two-Track Workflow (Q8-Q10): ✅
- Metric-based quality + spot-checking, integrated self-assessment
- Parallel tracks with reducing overhead over time
- Already meet threshold, focus on continuous improvement

### RepliCATS Alignment (Q11-Q13): ✅
- Sufficient documentation available (`docs/background-research/`)
- Build complete tool first, validate on repliCATS corpus later
- Document divergences explicitly

### Implementation Strategy (Q17-Q20): ✅
- **Q17:** Build classifier first (foundational)
- **Q18:** Test on sobotkova-2024, ballsun-stanton-2018, penske-2023; expand to all 10 papers once working
- **Q19:** One prompt per signal (7 prompts) + classifier prompt + quality assessment prompt(s)
  - **Heuristic:** Discrete tasks = separate prompts; interacting tasks = same prompt
- **Q20:** Leverage research-assessor skill, extend as needed; use skill-creator to determine prompt/skill boundaries

### Deferred to Implementation (Q14-Q16): Report formatting details
- Report structure validation
- Visualisation approach
- Audience framing

---

## Prompt Architecture Design (CRITICAL)

**Total prompts needed:** ~9-10 prompts minimum

1. **Research approach classifier** (1 prompt)
2. **Seven signal assessors** (7 prompts):
   - Comprehensibility
   - Transparency
   - Plausibility
   - Validity
   - Robustness
   - Replicability
   - Generalisability
3. **Quality assessment** (1+ prompts) - Track A self-assessment

**Prompt design heuristic:**
- Discrete independent tasks → separate prompts
- Tasks that inform each other → same prompt
- Example: Seven signals are assessed independently → 7 separate prompts
- Example: Classification informs assessment → classifier runs first, output feeds to assessors

---

## Skills Strategy

**Current skill:** `research-assessor` (extraction-focused)

**Extensions needed:**
1. Classification guidance (expressed vs revealed approach detection)
2. Signal assessment rubrics (7 rubrics + approach-specific notes)
3. Quality assessment framework (Track A monitoring)

**Use skill-creator skill to:**
- Determine appropriate boundaries between prompts and skills
- Structure assessment guidance effectively
- Maintain coherent skill architecture

---

## Implementation Sequence (Next Session)

### Immediate Priority: Overall Implementation Plan

**Before building, create:**
- Detailed prompt architecture diagram (which prompts, execution order, data flow)
- Skill extension plan (what goes in research-assessor, what stays as prompts)
- File structure for outputs (classification.json, signal-assessments/, credibility-report.md)
- Validation checkpoints (how to verify each component works)

### Then Build (Phase 1):

**Step 1: Research Approach Classifier** (3-4 hours)
- Create classifier prompt (or extend research-assessor skill)
- Test on 3 papers (sobotkova-2024, ballsun-stanton-2018, penske-2023)
- Generate classification.json outputs
- Validate expressed vs revealed detection
- Document classification patterns

**Step 2: First Rubric (Transparency)** (1 hour)
- Create transparency-rubric.md in assessment-system/rubrics/
- 0-100 scoring scale with anchors
- Assessment questions
- Approach-specific interpretation notes

**Step 3: End-to-End Proof of Concept** (1-2 hours)
- Classify sobotkova-et-al-2024
- Assess transparency signal
- Generate mini-report (just transparency section)
- Validate workflow

**Success criteria:** Classification + one signal assessment working on one paper

---

## Context Recovery Notes

**Session started:** VS Code crashed mid-discussion, lost work

**Recovery actions:**
- Reviewed active-todo-list.md (Task 10.2)
- Reviewed extraction-to-analysis-transition.md (background context)
- User provided key decisions from memory
- Reconstructed and documented all decisions in planning documents

**Critical decisions captured from user memory:**
- Individual papers focus (not corpus)
- Maximum automation with bypass permissions
- Flexible approach-specific assessment
- Continuous quality monitoring (Track A/B parallel)
- No expressed method = significant finding
- Discrete tasks = separate prompts (key architectural principle)

---

## Files Modified This Session

**Created:**
- `planning/paper-credibility-analysis-framework.md` (24KB, comprehensive)
- `planning/research-approach-classification-framework.md` (16KB, detailed spec)
- `planning/credibility-assessment-implementation-roadmap.md` (13KB, 5-phase plan)
- `planning/SESSION-SUMMARY-credibility-assessment-planning.md` (this file)

**Updated:**
- `planning/active-todo-list.md` (Task 10.2 status)

---

## Ready for Next Session: Final Planning Before Implementation

**User request:** "Overall plan before we begin implementation"

**Next session tasks:**

1. **Create comprehensive implementation plan:**
   - Prompt architecture diagram
   - Skill extension design
   - File structure and data flow
   - Execution sequence with dependencies
   - Validation strategy per component

2. **Use skill-creator skill:**
   - Determine prompt vs skill boundaries
   - Design research-assessor extensions
   - Structure assessment guidance

3. **Validate plan with user, then begin Phase 1**

**Estimated next session:** 1-2 hours planning, then begin classifier implementation

---

## Key Architectural Principles Established

1. **Discrete tasks = separate prompts** (modularity, focus, debuggability)
2. **Expressed vs revealed methodology** (transparency, HARKing detection)
3. **No false precision** (qualitative over quantitative where appropriate)
4. **Empirical development** (iterate and refine based on evidence)
5. **Continuous quality monitoring** (Track A integrated, reducing overhead)
6. **RepliCATS compatibility** (assess all 7 signals, document divergences)
7. **Approach-specific assessment** (inductive ≠ deductive ≠ abductive)
8. **Maximum automation** (Claude-driven, not Python scripting)

---

## Documentation Quality Check ✅

- All planning well-documented in markdown
- Decisions traceable and justified
- Implementation-ready specifications
- Context preserved for session continuity
- Cross-referenced documents
- Version-controlled planning files

**Planning phase: COMPLETE**
**Implementation phase: READY TO BEGIN (after final planning session)**

---

**Document Status:** Session summary v1.0
**Date:** 2025-11-16
**Next Session:** Create overall implementation plan, then begin Phase 1 (classifier)
