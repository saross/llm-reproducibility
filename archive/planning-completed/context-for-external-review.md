# Context for External Review of Credibility Assessment Implementation Plan

**Purpose:** Provide external LLM reviewer with essential background to critique `credibility-implementation-plan-detailed.md`

**Date:** 2025-11-16

---

## What We're Asking You to Review

We've created a detailed implementation plan for building an **individual research paper credibility assessment system** for Humanities, Arts, and Social Sciences (HASS) research. We need critical review focusing on:

1. **Architectural soundness** - Is the technical design robust?
2. **HASS research appropriateness** - Does it fit qualitative/mixed-method research norms?
3. **RepliCATS compatibility** - Can we validate against external benchmarks?
4. **Risks and gaps** - What could go wrong? What's missing?
5. **Complexity vs value** - Are we over-engineering or under-specifying?

**Your task:** Read the implementation plan and provide 5-10 critical observations with specific recommendations.

---

## Project Background

### What We've Built So Far (Phases 1-6 Complete)

**Phase 1-5: Extraction System**
- Seven-pass extraction workflow extracting claims, evidence, research designs, methods, and protocols from academic papers
- Structured JSON output (`extraction.json`) with cross-referenced elements
- Tested on 10 HASS papers (archaeology, ecology, palaeoecology, digital humanities)
- Uses `research-assessor` skill (custom Claude Code skill) for systematic extraction

**Phase 6: Credibility Metrics (Recently Complete)**
- 8 automated metrics calculated from extraction.json:
  1. **ESD** - Evidence Sufficiency Density (evidence per claim)
  2. **TCI** - Transparency & Completeness Index (RDMAP documentation)
  3. **SCS** - Scope Constraint Score (limitation statements)
  4. **RTI** - Research Traceability Index (cross-reference density)
  5. **RIS** - Reproducibility Infrastructure Score (data/code availability)
  6. **PGCS** - PID Graph Connectivity Score (persistent identifiers)
  7. **FCS** - FAIR Compliance Score (Findable, Accessible, Interoperable, Reusable)
  8. **MDD** - Methodological Documentation Density (RDMAP detail)
- Metrics provide quantitative baselines but need qualitative interpretation

### What We're Building Next (Current Plan Under Review)

**Phase 7-9: Individual Paper Credibility Assessment**
- Research approach classification (inductive/deductive/abductive)
- Seven-signal credibility assessment (adapted from repliCATS framework)
- 3-5 page credibility reports per paper
- Quality monitoring (Track A: assess our own assessment quality)

---

## Key Domain Context

### HASS Research Characteristics

**Why HASS is different from experimental sciences:**
- **Replication ≠ field replication** - Cannot re-excavate archaeological site, but CAN reproduce analysis
- **Evidence ≠ measurements** - Often interpretive observations, not quantitative data
- **Methods ≠ lab protocols** - Often adaptive, context-dependent, not standardized
- **Inductive research common** - Pattern discovery, not hypothesis testing
- **Qualitative/mixed methods** - Not purely statistical
- **CARE principles matter** - Indigenous data governance alongside FAIR principles

**Examples from our corpus:**
- Archaeological survey: "We documented 147 sites across 200km² survey area" (inductive, exploratory)
- Palaeoecology: "We tested hypothesis that climate change drove Bronze Age migration" (deductive)
- Digital humanities: "We developed software tool, then validated on 3 case studies" (abductive/methodological)

### RepliCATS Framework (External Validation Standard)

**What is repliCATS:**
- Collaborative Assessments for Trustworthy Science project
- Elicited expert judgments on research paper credibility using **Seven Signals**
- Achieved 73-84% accuracy predicting replication outcomes
- Used IDEA protocol (Investigate → Discuss → Estimate → Aggregate)

**Seven Signals:**
1. **Comprehensibility** - Clarity of claims and argument structure
2. **Transparency** - Research design and methods documentation
3. **Plausibility** - Theoretical coherence and contextual fit
4. **Validity** - Evidence adequacy for claims
5. **Robustness** - Sensitivity to analytical choices
6. **Replicability** - Analytic reproducibility (data/code/protocols)
7. **Generalisability** - Appropriate scope and limitation statements

**Why we reference repliCATS:**
- External benchmark for validation ("can we reproduce their panel judgments?")
- Established framework (not inventing from scratch)
- But: repliCATS focused on experimental psychology, we're adapting for HASS

### HASS Adaptations Required

**RepliCATS → HASS adaptations:**
- **Replicability:** "Analytic reproducibility" not "experimental replication"
- **Plausibility:** Domain-specific (archaeological vs ecological vs computational)
- **Evidence:** Observational data, not just quantitative measurements
- **Robustness:** Triangulation and alternative interpretations, not just statistical sensitivity
- **CARE principles:** Indigenous data sovereignty considerations

---

## Our Design Decisions (From Previous Planning)

### Fundamental Choices Made

1. **Target:** Individual papers (not corpus-level aggregate analysis)
2. **Automation:** Maximum Claude autonomy (Claude-driven workflow, not Python scripting)
3. **Approach flexibility:** Credibility criteria vary by research approach (inductive ≠ deductive)
4. **Report format:** 3-5 page summaries initially (expand after validation)
5. **Two-track analysis:**
   - **Track A:** Assess quality of our own extraction/assessment (continuous improvement)
   - **Track B:** Assess credibility of research paper itself (primary output)
6. **Expressed vs revealed methodology:** Compare what paper says vs what paper does (detect HARKing)
7. **No expressed method = significant:** Absence of methodological statement indicates weak research design

### Key Architectural Principle

**"Discrete tasks = separate prompts; interacting tasks = same prompt"**

This heuristic guides our prompt architecture design:
- Classification (discrete) → own prompt
- Each signal assessment (discrete) → own prompt? (This is what plan proposes - 7 prompts)
- Or: Signals interact (validity informs robustness) → combined prompt? (Alternative not fully explored)

---

## Implementation Plan Overview (What You're Reviewing)

### Proposed Architecture

**10 prompts total:**
1. Research approach classifier (1 prompt)
2. Track A quality check (1 prompt)
3. Seven signal assessors (7 prompts) ← Can run in parallel
4. Report generator (1 prompt)

**Skill extension strategy:**
- Extend existing `research-assessor` skill (not create new skill)
- Add 7 reference files for credibility frameworks
- Add 2 schema files for output structures
- Skills = stable knowledge, Prompts = evolving instructions

**File structure:**
```
outputs/{paper-slug}/assessment/
├── classification.json
├── track-a-quality.md
├── signals/*.md (7 files)
└── credibility-report-v1.md
```

**Implementation phases:**
1. Extend skill + build classifier (3 hours)
2. Build all 7 signal rubrics (4-6 hours)
3. Build Track A + report generation (2-3 hours)
4. Test on full corpus (2-3 hours)
5. Documentation (2-3 hours)

**Total estimated effort:** 17-24 hours

---

## Critical Questions for Your Review

### 1. Prompt Architecture

**Is 10 prompts (7 for signals) optimal?**
- Pro: Modularity, focus, independent testing
- Con: Maintenance burden, coordination complexity, potential inconsistency
- Alternative: Consolidate signals into 2-3 prompts or even 1?

**Can signals run truly independently?**
- Plan assumes parallel execution
- But: Does Transparency assessment inform Replicability assessment?
- Should signals be sequential to allow cross-referencing?

### 2. Skill Extension Decision

**Should we extend research-assessor skill or create separate credibility-assessor skill?**
- Plan recommends extension (shared infrastructure, coherent workflow)
- But: Is this violating single responsibility principle?
- Will skill become too complex (Pass 0-7 extraction + Pass 8-9 assessment)?

### 3. Validation Strategy

**Is manual review sufficient?**
- Plan relies heavily on "makes sense" and "feels right" criteria
- Missing: Quantitative baselines (test-retest reliability, inter-rater agreement)
- Missing: Early repliCATS validation (plan defers to Phase 5+)

**Should we validate earlier?**
- Risk: Build full system, then discover repliCATS incompatibility
- Alternative: Phase 1.5 = test on 1-2 repliCATS papers with known expert scores?

### 4. Approach-Specific Assessment Mechanics

**How does "approach-specific emphasis" work mechanically?**
- Inductive: PRIMARY = Transparency, Comprehensibility
- Deductive: PRIMARY = Validity, Robustness
- But: Do we assess all 7 signals with same rigour, just emphasize differently in report?
- Or: Use different rubrics per approach?
- Or: Skip some signals based on approach?

**Plan is ambiguous on this implementation detail.**

### 5. Track A Integration

**Is Track A (quality monitoring) properly integrated?**
- Plan shows Track A parallel to Track B
- But: Should Track A be a pre-assessment gate? (Don't assess credibility if extraction quality too low)
- What happens if Track A identifies major issues? Abort? Caveat? Proceed anyway?

### 6. Complexity vs Value

**Are we over-engineering?**
- 10 prompts + skill extensions + 7 reference files + 2 schemas = substantial complexity
- Is this warranted for 10-paper corpus?
- Could we start simpler, add complexity based on need?

**Are we under-specifying?**
- Error handling missing (what if classification fails? Low confidence? Missing evidence?)
- File format choices not justified (JSON vs YAML vs Markdown - why?)
- Prompt versioning strategy absent (how to handle prompt evolution mid-corpus?)

---

## What Good Critique Looks Like

**Please provide:**

1. **3-5 major concerns** - Architectural issues, risks, gaps
2. **3-5 medium concerns** - Implementation details that need refinement
3. **2-3 opportunities** - Things we haven't considered that could improve the plan
4. **Top 5 recommendations** - Prioritized list of changes to make

**Focus areas:**
- HASS appropriateness (we're not experimental psychologists - does plan fit HASS norms?)
- Technical soundness (data flow, dependencies, error handling)
- RepliCATS compatibility (will we be able to validate against their corpus?)
- Complexity management (10 prompts - too many? Skill extension - right choice?)
- Validation strategy (manual review sufficient? Need quantitative baselines?)

**Be specific:**
- Instead of: "Validation is weak"
- Say: "Validation lacks quantitative baselines. Recommend: run each assessment 3x, measure score variance, expect SD < 10 for reliable scoring."

**Challenge assumptions:**
- "Plan assumes 7 separate prompts based on 'discrete tasks = separate prompts' heuristic, but signals may interact (transparency → replicability). Consider consolidated assessment prompt."

---

## Documents to Review (In Priority Order)

**PRIMARY (MUST READ):**
1. `credibility-implementation-plan-detailed.md` (25KB, 1221 lines) - The plan under review

**SECONDARY (Optional, for deeper context):**
2. `paper-credibility-analysis-framework.md` - Design decisions (17 questions answered)
3. `research-approach-classification-framework.md` - Classification methodology
4. `credibility-assessment-implementation-roadmap.md` - 5-phase overview

**BACKGROUND (If time permits):**
5. `docs/background-research/replicats-seven-signals-hass-adaptation.md` - RepliCATS signal definitions
6. `docs/assessment-guide/credibility-metrics-reference.md` - Our 8 existing metrics

---

## Output Format Requested

```markdown
# External Review: Credibility Assessment Implementation Plan

## Reviewer
[Your model name/version]

## Summary Assessment
[2-3 paragraph overview: strengths, weaknesses, overall grade]

## Major Concerns (3-5 issues)

### 1. [Concern title]
**Issue:** [What's wrong]
**Impact:** [Why it matters]
**Recommendation:** [Specific fix]

[Repeat for each concern]

## Medium Concerns (3-5 issues)
[Same format, less critical issues]

## Opportunities (2-3 suggestions)
[Things we haven't considered that could improve plan]

## Top 5 Recommendations (Prioritized)
1. [Highest priority change]
2. [Second priority]
...

## Overall Grade
[A/B/C/D with justification]
```

---

## Key Terminology

- **HASS:** Humanities, Arts, and Social Sciences
- **RepliCATS:** Collaborative Assessments for Trustworthy Science (external validation benchmark)
- **RDMAP:** Research Design, Methods, and Protocols
- **FAIR:** Findable, Accessible, Interoperable, Reusable (data principles)
- **CARE:** Collective benefit, Authority to control, Responsibility, Ethics (Indigenous data principles)
- **HARKing:** Hypothesising After Results are Known (methodological issue)
- **Track A/B:** Two-track analysis (A = assess our assessment quality, B = assess paper credibility)
- **Inductive/Deductive/Abductive:** Three research approaches with different credibility criteria
- **Expressed vs Revealed:** What paper says it's doing vs what it actually does

---

**Thank you for your critical review! Your external perspective is valuable for strengthening this plan before implementation.**
