# Assessment Phase Implementation Plan

**Version:** 1.0
**Date:** 2025-11-14
**Status:** Phase 1 in progress

---

## Overview

This document outlines the phased implementation plan for transitioning from extraction to credibility assessment in the LLM reproducibility project. The plan follows an iterative approach: build minimal viable assessment first, then progressively add depth and automation.

---

## Validation Strategy

### Phase 1-3: Internal Validation (Weeks 1-5)
**Expert:** Shawn Graham (domain expert, project lead)
**Corpus:** 11 papers (archaeology, ancient history, palaeoenvironmental, archaeogenetics, GIS)
**Goal:** Build prototype that passes "smell test" - metrics and assessments align with expert intuition

### Phase 4-5: External Validation (Weeks 6-7+)
**Expert:** Aaron Willcox (repliCATS data scientist)
**Corpus:** Expanded corpus (20-30 papers across broader HASS disciplines)
**Goal:** Validate scalability, inter-rater reliability, calibration to repliCATS methodology

---

## Disciplinary Scope

**Current corpus:** 11 papers spanning:
- Archaeology (predictive modelling, landscape analysis, remote sensing)
- Ancient history and philology
- Palaeoenvironmental reconstruction (multi-proxy analysis)
- Archaeogenetics (ancient DNA)
- GIS and mobile data collection systems
- Digital archaeology and preregistration methodology

**Broader than repliCATS:** Lab-based experimental sciences → HASS fieldwork research
**Design principle:** Metrics and rubrics must work across diverse HASS methodologies

---

## Architecture Decisions

### Prompts vs Skills Division

**Skills (orchestration, workflow, infrastructure):**
- `assessment-coordinator`: Multi-signal workflow orchestration (Phase 3+)
- `research-assessor`: Extraction workflow (existing)

**Prompts (domain logic, scoring, judgement):**
- `credibility-assessment/signal-{1-7}.md`: Per-signal scoring (Phase 2+)
- `credibility-assessment/synthesis.md`: Scorecard generation (Phase 2+)

**Rationale:**
- Skills for cross-cutting concerns (easier to maintain complex workflows)
- Prompts for domain-specific judgement (easier to refine, version control visible)
- Separation enables independent iteration and sharing

### Key Design Principles

1. **Modularity:** Each signal assessed independently, synthesised later
2. **Provenance:** Every score traceable to CEM graph elements
3. **Uncertainty:** Explicit confidence bounds and ambiguity flags
4. **Incrementality:** Each phase produces standalone value
5. **Validation:** Continuous calibration via expert review

---

## Phase 1: Foundation (Week 1, 12-15 hours)

### Goal
Operational quantitative metrics on all 11 papers in corpus

### Deliverables

#### Code
- `assessment-system/scripts/analysis_toolkit.py` - Graph query and metrics library
- `assessment-system/scripts/batch_metrics.py` - Automated batch runner

#### Data
- `outputs/credibility-metrics-dashboard.json` - Metrics for all 11 papers
- `outputs/credibility-metrics-summary.md` - Human-readable summary
- `outputs/{paper-id}/metrics-scorecard.md` - Per-paper scorecards (11 files)

#### Documentation
- `docs/assessment-guide/credibility-metrics.md` - Metrics documentation
- `assessment-system/templates/metrics-scorecard.md` - Scorecard template

### Components

#### 1.1 Analysis Toolkit (6-8 hours)
**File:** `assessment-system/scripts/analysis_toolkit.py`

**Graph Query Library:**
- Load and parse extraction.json files
- Extract claims, evidence, RDMAP items
- Filter by section, type, tier
- Query relationships (claims→evidence mappings, method→design links)
- Extract infrastructure elements (PIDs, FAIR scores, permits)

**8 Quantitative Metrics:**

1. **Evidential Support Density (ESD)**
   - **Measures:** Claims:Evidence ratio by section
   - **Purpose:** Detect under-supported claims
   - **Calculation:** Claims / Evidence per section, corpus-wide average
   - **Interpretation:** Lower is better (more evidence per claim)

2. **Transparency Completeness Index (TCI)**
   - **Measures:** RDMAP coverage and detail level
   - **Purpose:** Assess methods documentation completeness
   - **Calculation:** (Research Designs + Methods + Protocols) / Expected count, weighted by tier
   - **Interpretation:** Higher is better (more complete documentation)

3. **Scope Constraint Score (SCS)**
   - **Measures:** Explicit scope/limitation statements
   - **Purpose:** Detect overclaiming or insufficient qualification
   - **Calculation:** Count of scope constraints, limitations, caveats in claims and discussion
   - **Interpretation:** Higher is better (more explicit about boundaries)

4. **Robustness Triangulation Index (RTI)**
   - **Measures:** Evidence type diversity
   - **Purpose:** Assess whether claims rest on single vs multiple evidence types
   - **Calculation:** Shannon diversity index of evidence types supporting claims
   - **Interpretation:** Higher is better (more diverse evidence base)

5. **Replicability Infrastructure Score (RIS)**
   - **Measures:** Data/code sharing, PIDs, reproducibility artefacts
   - **Purpose:** Assess analytical reproducibility potential
   - **Calculation:** Binary flags (data shared, code shared, persistent IDs) + completeness
   - **Interpretation:** Higher is better (more reproducible)

6. **PID Graph Connectivity Score (PGCS)**
   - **Measures:** Linked persistent identifiers network density
   - **Purpose:** Assess machine-actionability and citation graph completeness
   - **Calculation:** (PIDs with resolvable links) / (Total PIDs mentioned)
   - **Interpretation:** Higher is better (more connected infrastructure)

7. **FAIR Compliance Score (FCS)**
   - **Measures:** FAIR principles adherence (from Pass 6 assessments)
   - **Purpose:** Assess data/code FAIRness
   - **Calculation:** FAIR score (0-15) from infrastructure extraction
   - **Interpretation:** Higher is better (15/15 is exemplary)

8. **Methods Documentation Density (MDD)**
   - **Measures:** RDMAP item detail and completeness
   - **Purpose:** Assess procedural transparency depth
   - **Calculation:** Average character count + field completeness for RDMAP items
   - **Interpretation:** Higher is better (more detailed procedures)

#### 1.2 Batch Metrics Runner (2-3 hours)
**File:** `assessment-system/scripts/batch_metrics.py`

**Functionality:**
- Iterate through all papers in `outputs/` directory
- Load each `extraction.json`
- Calculate all 8 metrics using `analysis_toolkit.py`
- Generate corpus-wide statistics (mean, median, std dev, outliers)
- Output structured results: `outputs/credibility-metrics-dashboard.json`
- Create human-readable summary: `outputs/credibility-metrics-summary.md`

**Dashboard JSON Structure:**
```json
{
  "corpus_summary": {
    "paper_count": 11,
    "metrics": {
      "ESD": {"mean": 0.65, "min": 0.42, "max": 1.12, "std": 0.18},
      "TCI": {"mean": 0.78, "min": 0.45, "max": 0.95, "std": 0.14},
      ...
    }
  },
  "papers": [
    {
      "paper_id": "sobotkova-et-al-2023",
      "metrics": {
        "ESD": 0.58,
        "TCI": 0.85,
        ...
      },
      "flags": ["high-evidence-support", "excellent-transparency"],
      "needs_review": false
    },
    ...
  ]
}
```

#### 1.3 Metrics Documentation (2-3 hours)
**File:** `docs/assessment-guide/credibility-metrics.md`

**Contents:**
- Introduction: What quantitative metrics measure and why
- Detailed metric descriptions (8 sections)
- Calculation methodology (formulas, code references)
- Interpretation guidelines (thresholds, what's "good" vs "concerning")
- Disciplinary context (fieldwork vs lab science differences)
- Relationship to repliCATS seven signals (mapping table)
- Known limitations and edge cases
- Future enhancements

#### 1.4 Traffic Light Scorecard (2 hours)
**File:** `assessment-system/templates/metrics-scorecard.md`

**Features:**
- Red/yellow/green flags per paper based on metric thresholds
- Thresholds calibrated to 11-paper corpus distribution (bottom 25%, middle 50%, top 25%)
- Identifies papers needing deeper qualitative review
- Highlights specific areas of concern (e.g., "low evidence diversity", "missing PIDs")
- Comparative ranking within corpus

**Example Scorecard:**
```markdown
# Credibility Metrics Scorecard: sobotkova-et-al-2023

## Overall Assessment: 🟢 STRONG

## Metrics Summary

| Metric | Score | Flag | Corpus Rank |
|--------|-------|------|-------------|
| Evidential Support Density | 0.58 | 🟢 | 3/11 |
| Transparency Completeness | 0.85 | 🟢 | 2/11 |
| Scope Constraint | 12 | 🟡 | 6/11 |
| Robustness Triangulation | 2.4 | 🟢 | 4/11 |
| Replicability Infrastructure | 8/15 | 🟡 | 5/11 |
| PID Graph Connectivity | 0.75 | 🟢 | 3/11 |
| FAIR Compliance | 9/15 | 🟡 | 4/11 |
| Methods Documentation Density | 1250 | 🟢 | 2/11 |

## Key Strengths
- Excellent methods documentation (high TCI, MDD)
- Strong evidence base (low ESD, high RTI)
- Good PID infrastructure (high PGCS)

## Areas for Improvement
- Moderate FAIR compliance (could improve to 12-15/15 with DOI release)
- Scope constraints could be more explicit in claims sections

## Recommendation
✅ Does not require deep qualitative review (strong across most metrics)
```

### Workflow

**Session 1 (4-5 hours):**
1. Create `assessment-system/scripts/analysis_toolkit.py` with skeleton
2. Implement graph query functions
3. Implement first 4 metrics (ESD, TCI, SCS, RTI)
4. Test on 2-3 papers manually, verify calculations

**Session 2 (4-5 hours):**
5. Implement remaining 4 metrics (RIS, PGCS, FCS, MDD)
6. Create `batch_metrics.py` runner
7. Run on all 11 papers
8. Generate `credibility-metrics-dashboard.json` and summary

**Session 3 (4-5 hours):**
9. Create `docs/assessment-guide/credibility-metrics.md`
10. Create `assessment-system/templates/metrics-scorecard.md`
11. Generate per-paper scorecards (11 files)
12. **Expert review:** Shawn validates metrics make sense for corpus

### Success Criteria

**Technical:**
- ✅ All 8 metrics calculate without errors on all 11 papers
- ✅ Results are reproducible (same metrics each run)
- ✅ Code is documented and reusable

**Validation (Expert Review):**
- ✅ Metrics align with Shawn's intuitive sense of paper quality
- ✅ High/low scores correspond to papers flagged as strong/weak
- ✅ Metrics discriminate between papers (not all similar scores)
- ✅ Traffic light flags prioritise papers needing deeper review

**Output Quality:**
- ✅ Dashboard provides useful comparative view
- ✅ Scorecards highlight meaningful patterns
- ✅ Documentation is clear enough for Aaron to understand later

---

## Phase 2: Qualitative Depth (Weeks 2-3, 18-24 hours)

### Goal
Deep rubric-based assessment on 3 papers with LLM assistance

### Deliverables

#### Rubrics
- `assessment-system/credibility-rubrics-v1.md` - Detailed scoring criteria for 7 signals

#### Prompts
- `assessment-system/prompts/signal-1-comprehensibility.md`
- `assessment-system/prompts/signal-2-transparency.md`
- `assessment-system/prompts/signal-3-plausibility.md`
- `assessment-system/prompts/signal-4-validity.md`
- `assessment-system/prompts/signal-5-robustness.md`
- `assessment-system/prompts/signal-6-replicability.md`
- `assessment-system/prompts/signal-7-generalisability.md`
- `assessment-system/prompts/synthesis-scorecard.md`

#### Assessments
- `outputs/{paper-id}/credibility-scorecard-v1.md` - Full qualitative scorecards (3 papers)

### Components

#### 2.1 Credibility Rubrics (8-10 hours)
**File:** `assessment-system/credibility-rubrics-v1.md`

Detailed scoring criteria (0-100) for seven repliCATS signals adapted to HASS fieldwork:

**1. Comprehensibility**
- **Definition:** Are claims clear, explicit, and well-bounded?
- **Assessment questions:**
  1. Are claims stated explicitly or only implied?
  2. Are claim scopes clearly defined (spatial, temporal, conceptual)?
  3. Are technical terms defined or contextualised?
  4. Are causal claims distinguished from correlational claims?
  5. Are quantitative claims precise (with uncertainty bounds)?
- **Scoring rubric:**
  - 0-25: Claims vague, ambiguous, or missing scope
  - 26-50: Claims mostly clear but some ambiguity or scope issues
  - 51-75: Claims clear and scoped, minor ambiguities
  - 76-100: Claims explicit, precise, well-bounded, unambiguous
- **Red flags:** Implied claims, undefined jargon, unclear scope
- **Green flags:** Explicit statements, defined terms, bounded scope
- **Evidence from CEM:** Claim texts, scope_constraint fields, qualification statements

**2. Transparency**
- **Definition:** Is research design documented? Are methods explained?
- **Assessment questions:**
  1. Is the overall research design explicit and justified?
  2. Are data collection procedures documented?
  3. Are analytical methods described in sufficient detail?
  4. Are deviations from protocols noted?
  5. Are analytical choices justified?
- **Scoring rubric:**
  - 0-25: Research design unclear, methods minimally documented
  - 26-50: Research design stated, methods described but gaps
  - 51-75: Research design justified, methods mostly complete
  - 76-100: Research design explicit and justified, methods reproducible
- **Red flags:** Missing procedures, unjustified choices, protocol deviations not noted
- **Green flags:** Detailed protocols, justified decisions, complete documentation
- **Evidence from CEM:** RDMAP items (research designs, methods, protocols), methodology sections

**3. Plausibility**
- **Definition:** Do claims fit with established knowledge?
- **Assessment questions:**
  1. Are claims consistent with domain knowledge?
  2. Are surprising claims acknowledged as such?
  3. Are alternative explanations considered?
  4. Are contradictions with prior work addressed?
  5. Is background literature appropriately cited?
- **Scoring rubric:**
  - 0-25: Claims contradict established knowledge without justification
  - 26-50: Claims mostly plausible, some tensions unaddressed
  - 51-75: Claims plausible, surprising findings acknowledged
  - 76-100: Claims well-grounded, alternatives considered, tensions addressed
- **Red flags:** Unsupported novel claims, ignored contradictions, sparse citations
- **Green flags:** Grounded in literature, alternatives discussed, tensions addressed
- **Evidence from CEM:** Literature evidence items, alternative_explanations fields

**4. Validity**
- **Definition:** Is evidence adequate for claims? Are alternatives considered?
- **Assessment questions:**
  1. Is the evidence type appropriate for the claim type?
  2. Is the evidence quantity sufficient?
  3. Are confounding factors controlled or acknowledged?
  4. Are alternative explanations ruled out?
  5. Are inference steps justified?
- **Scoring rubric:**
  - 0-25: Evidence insufficient or inappropriate for claims
  - 26-50: Evidence adequate for some claims, gaps for others
  - 51-75: Evidence mostly sufficient, minor gaps or confounds
  - 76-100: Evidence robust, confounds addressed, alternatives ruled out
- **Red flags:** Unsupported claims, missing confound control, weak inferences
- **Green flags:** Multiple evidence types, confounds controlled, strong inference chain
- **Evidence from CEM:** Claim-evidence mappings, evidence types, inference chains

**5. Robustness**
- **Definition:** Do results survive analytical choices?
- **Assessment questions:**
  1. Are analytical choices documented?
  2. Are sensitivity analyses performed?
  3. Are results triangulated across methods?
  4. Are negative results reported?
  5. Are limitations acknowledged?
- **Scoring rubric:**
  - 0-25: Single analysis path, no sensitivity testing
  - 26-50: Analytical choices documented, limited testing
  - 51-75: Sensitivity analysis on key decisions, some triangulation
  - 76-100: Comprehensive sensitivity testing, multiple methods, limitations explicit
- **Red flags:** Single method, no sensitivity analysis, selective reporting
- **Green flags:** Multiple methods, sensitivity tests, negative results reported
- **Evidence from CEM:** Multiple methods for same question, sensitivity analyses, limitations

**6. Replicability**
- **Definition:** Can analytical procedures be reproduced?
- **Assessment questions:**
  1. Are data publicly available?
  2. Is analysis code shared?
  3. Are software versions specified?
  4. Are random seeds or parameters documented?
  5. Are intermediate outputs available?
- **Scoring rubric:**
  - 0-25: No data/code sharing, minimal procedural detail
  - 26-50: Data available, code not shared or incomplete
  - 51-75: Data and code shared, minor gaps in documentation
  - 76-100: Complete reproducibility package (data, code, environment, docs)
- **Red flags:** No data sharing, missing code, unspecified versions
- **Green flags:** Full data/code availability, versioned software, complete documentation
- **Evidence from CEM:** Infrastructure items (PIDs, repositories, licences), FAIR scores

**7. Generalisability**
- **Definition:** Are scope limits explicit?
- **Assessment questions:**
  1. Are study contexts (time, place, conditions) specified?
  2. Are population characteristics described?
  3. Are generalisability claims bounded?
  4. Are context dependencies acknowledged?
  5. Are transferability limits discussed?
- **Scoring rubric:**
  - 0-25: Context unspecified, overgeneralised claims
  - 26-50: Context stated, some generalisation issues
  - 51-75: Context well-described, generalisability mostly bounded
  - 76-100: Context explicit, generalisability carefully constrained, transferability discussed
- **Red flags:** Universal claims from specific contexts, unspecified conditions
- **Green flags:** Explicit boundaries, context-dependence noted, careful generalisation
- **Evidence from CEM:** Study context descriptions, scope constraints, limitation statements

**Rubric Structure per Signal:**
- Definition (HASS-adapted from repliCATS)
- Assessment questions (5-7 per signal)
- Scoring rubric (0-25-50-75-100 with descriptors)
- Red flags (warning signs of low credibility)
- Green flags (indicators of high credibility)
- Evidence requirements from CEM graph (what to query)
- Relationship to quantitative metrics (which metrics inform this signal)

#### 2.2 LLM Assessment Prompts (4-6 hours)

**Architecture:** Multi-prompt workflow (7 signal prompts + 1 synthesis prompt)

**Per-Signal Prompt Structure:**
- Load rubric for this signal
- Query CEM graph via analysis_toolkit.py for relevant evidence
- Apply scoring criteria
- Output: Score (0-100) + justification + evidence citations + uncertainty flags

**Example: `signal-1-comprehensibility.md`**
```markdown
# Credibility Assessment: Signal 1 - Comprehensibility

## Objective
Assess whether claims in this paper are clear, explicit, and well-bounded.

## Rubric
[Load rubric section for Comprehensibility]

## Data Sources
Use `analysis_toolkit.py` to query:
- All claim items from extraction.json
- Scope constraint fields
- Qualification statements
- Technical term definitions

## Assessment Process

1. **Load claims:** Extract all claim items, grouped by section
2. **Check clarity:** For each claim, assess:
   - Is it explicitly stated or only implied?
   - Are technical terms defined?
   - Is scope specified (time, place, conditions)?
3. **Check precision:** For quantitative claims:
   - Are measurements precise?
   - Are uncertainty bounds provided?
4. **Check boundaries:** For generalising claims:
   - Are scope constraints explicit?
   - Are limitations acknowledged?

## Scoring

Calculate score (0-100) based on rubric:
- Count: Explicit vs implied claims
- Count: Defined vs undefined technical terms
- Count: Scoped vs unscoped claims
- Aggregate to overall score

## Output Format

```json
{
  "signal": "comprehensibility",
  "score": 75,
  "confidence": "high",
  "justification": "Claims are mostly explicit and well-scoped. 89% of claims have explicit scope constraints. Technical terms are defined on first use. Minor ambiguity in claims about causality vs correlation in section 4.",
  "evidence_citations": [
    "claim_C042: Explicit scope constraint (spatial: Kazanlak Valley, temporal: 1960-2010)",
    "claim_C015: Technical term 'ordered logit' defined in methods section"
  ],
  "red_flags": [
    "claim_C037: Causal claim without explicit causal language"
  ],
  "green_flags": [
    "89% of claims include explicit scope constraints",
    "All technical terms defined on first use"
  ],
  "quantitative_support": {
    "explicit_claims_pct": 0.95,
    "scoped_claims_pct": 0.89,
    "defined_terms_pct": 1.0
  }
}
```
```

**Synthesis Prompt:** `synthesis-scorecard.md`
- Loads all 7 signal assessments
- Generates overall credibility profile
- Identifies patterns (strengths, weaknesses, trade-offs)
- Creates human-readable scorecard
- Flags papers needing expert review

#### 2.3 Pilot Deep Assessments (6-8 hours)

**Paper Selection Strategy:**
- **High metrics paper:** Baseline validation (do rubrics agree with quantitative flags?)
- **Medium metrics paper:** Discrimination test (can rubrics add nuance?)
- **Low metrics paper:** Sensitivity test (do rubrics surface specific issues?)

**Suggested Papers:**
- High: `sobotkova-et-al-2023` (citizen science GIS, strong metrics)
- Medium: `eftimoski-et-al-2017` (landscape archaeology, mixed metrics)
- Low: `ross-2005` (philology, sparse evidence base)

**Process per Paper (2-3 hours):**
1. Run quantitative metrics (baseline)
2. Run 7 signal assessment prompts sequentially
3. Run synthesis prompt
4. Generate `outputs/{paper-id}/credibility-scorecard-v1.md`
5. **Expert review:** Shawn validates rubric scores and justifications
6. Document discrepancies, edge cases, rubric ambiguities

**Output:** 3 complete qualitative scorecards with Shawn's validation notes

### Success Criteria

**Rubric Quality:**
- ✅ Rubrics are clear and unambiguous
- ✅ Scoring criteria are applicable to all 3 pilot papers
- ✅ Rubrics discriminate between high/medium/low quality
- ✅ Red/green flags surface meaningful patterns

**LLM Assessment Quality:**
- ✅ LLM scores align with Shawn's expert judgement (±10 points)
- ✅ Justifications cite appropriate CEM evidence
- ✅ Uncertainty flags are appropriate
- ✅ Assessments are reproducible

**Workflow Validation:**
- ✅ 7-prompt workflow is manageable (not too time-consuming)
- ✅ Synthesis produces coherent overall profile
- ✅ Scorecards are human-readable and actionable

---

## Phase 3: Architecture for Scale (Weeks 4-5, 15-20 hours)

### Goal
Multi-agent LLM workflow with uncertainty quantification, ready to scale to full corpus

### Deliverables

#### Skill
- `.claude/skills/assessment-coordinator/SKILL.md` - Assessment orchestration skill
- `.claude/skills/assessment-coordinator/references/` - Rubrics and guidance

#### Infrastructure
- `assessment-system/scripts/uncertainty_quantification.py` - Multi-run variance analysis
- `assessment-system/validation/benchmark-comparisons.md` - Validation methodology

#### Assessments
- Pilot multi-agent assessments on same 3 papers (compare to Phase 2 manual)

### Components

#### 3.1 Assessment Coordinator Skill (8-12 hours)
**File:** `.claude/skills/assessment-coordinator/SKILL.md`

**Capabilities:**
- Load extraction.json for target paper
- Run quantitative metrics (call analysis_toolkit.py)
- Orchestrate 7 signal assessments sequentially
- Aggregate scores with uncertainty bounds
- Generate credibility scorecard
- Manage assessment provenance (track which prompt version, when run)
- Support multi-run variance analysis

**Workflow:**
1. User invokes skill with paper ID
2. Skill loads extraction and runs metrics
3. Skill launches 7 signal assessment sub-tasks
4. Each sub-task uses corresponding prompt + rubric
5. Skill aggregates results
6. Skill generates scorecard
7. Skill outputs JSON + markdown report

**Configuration:**
- Multi-run mode (default: 3 runs for variance)
- Signal selection (can run subset of 7 signals)
- Output verbosity (summary vs detailed)

#### 3.2 Uncertainty Quantification (4-5 hours)
**File:** `assessment-system/scripts/uncertainty_quantification.py`

**Methods:**
- **Multi-run variance:** Run each signal assessment 3 times, calculate score variance
- **Confidence intervals:** 95% CI on scores based on variance
- **Uncertainty flags:** Explicit tags for ambiguous cases
  - "insufficient_evidence": Not enough CEM data to score confidently
  - "ambiguous_rubric": Multiple rubric interpretations possible
  - "domain_dependent": Score varies by disciplinary norms
- **Sensitivity analysis:** How much do scores change with rubric threshold adjustments?

**Output:**
```json
{
  "signal": "validity",
  "score_mean": 68,
  "score_std": 5.2,
  "confidence_interval": [63, 73],
  "confidence_level": "medium",
  "uncertainty_flags": ["ambiguous_rubric"],
  "uncertainty_note": "Confound control assessment varies between runs due to ambiguous rubric criteria for 'acknowledged' vs 'controlled'",
  "runs": [
    {"run": 1, "score": 65, "timestamp": "2025-11-14T10:23:45"},
    {"run": 2, "score": 70, "timestamp": "2025-11-14T10:25:12"},
    {"run": 3, "score": 69, "timestamp": "2025-11-14T10:26:38"}
  ]
}
```

#### 3.3 Validation Framework (3-4 hours)
**File:** `assessment-system/validation/benchmark-comparisons.md`

**Validation Approach:**

1. **Internal consistency:**
   - Do quantitative metrics correlate with expected qualitative signals?
   - ESD → Validity signal
   - TCI → Transparency signal
   - RIS → Replicability signal
   - SCS → Generalisability signal

2. **Expert agreement:**
   - Compare LLM scores to Shawn's independent assessments
   - Calculate mean absolute error, correlation coefficient
   - Identify systematic biases (e.g., LLM consistently harsher/easier than expert)

3. **Multi-run consistency:**
   - Are scores stable across runs (low variance)?
   - Which signals have high variance (need rubric refinement)?

4. **RepliCATS calibration (future with Aaron):**
   - Map our 7 signals to repliCATS 7 signals
   - Compare score distributions
   - Document where HASS fieldwork differs from lab science
   - Refine rubrics based on repliCATS benchmarks

**Documentation:**
- Validation results table
- Identified biases and corrections
- Rubric refinement recommendations
- Known edge cases

### Success Criteria

**Technical:**
- ✅ Assessment coordinator skill operational
- ✅ Can assess any paper with single invocation
- ✅ Multi-run variance calculated for all signals

**Validation:**
- ✅ Internal consistency: Metrics correlate with signals (r > 0.6)
- ✅ Expert agreement: LLM scores within ±15 points of Shawn's (80%+ of cases)
- ✅ Multi-run consistency: Score std dev < 10 points per signal

**Scalability:**
- ✅ Skill ready to run on remaining 8 papers
- ✅ Workflow documented for Aaron's future validation

---

## Phase 4: Full Corpus Assessment (Week 6, 10-15 hours)

### Goal
Complete credibility assessment of all 11 papers with comparative analysis

### Deliverables

#### Assessments
- `outputs/{paper-id}/credibility-scorecard-v1.md` - Full scorecards for all 11 papers

#### Analysis
- `outputs/corpus-credibility-analysis.md` - Cross-paper patterns and insights
- `outputs/credibility-dashboard.html` - Interactive visualisation

#### Data
- `outputs/corpus-credibility-scores.json` - Structured scores for all papers

### Components

#### 4.1 Batch Assessment (6-8 hours)
**Process:**
- Run assessment-coordinator skill on remaining 8 papers
- Generate standardised scorecards
- Collect uncertainty metrics
- Document edge cases, ambiguities, and rubric interpretation questions

**Quality Control:**
- Spot-check 2-3 scorecards for plausibility
- Verify all papers have complete assessments (7 signals + synthesis)
- Check for technical errors (missing citations, broken references)

#### 4.2 Cross-Paper Analysis (3-5 hours)
**File:** `outputs/corpus-credibility-analysis.md`

**Analyses:**

1. **Comparative Score Distributions:**
   - Which signals show most variation across corpus?
   - Which papers are outliers (high/low)?
   - Are there signal clusters (papers strong on multiple signals)?

2. **Pattern Identification:**
   - Signal correlations: Do high transparency papers also have high validity?
   - Paper type differences: Do quantitative vs qualitative papers score differently?
   - Temporal patterns: Do newer papers score higher (methods improving over time)?
   - Disciplinary patterns: Does archaeology vs ancient history vs palaeoenvironmental differ?

3. **Outlier Analysis:**
   - Which papers are unexpectedly strong/weak?
   - Why? (Methodology, domain norms, author practices)

4. **Improvement Themes:**
   - What are common weaknesses across corpus?
   - What interventions would help most? (e.g., preregistration, data sharing, sensitivity analysis)

**Tables:**
- Signal scores matrix (11 papers × 7 signals)
- Ranking by overall credibility
- Strengths and weaknesses summary per paper

#### 4.3 Visualisation Dashboard (2-3 hours)
**File:** `outputs/credibility-dashboard.html`

**Interactive Features:**
- **Radar charts:** 7-signal profile per paper (hoverable)
- **Heatmap:** 11 papers × 7 signals colour-coded by score
- **Scatter plots:** Pairwise signal correlations
- **Distributions:** Histograms per signal across corpus
- **Filters:** By paper type, domain, year, author

**Technology:** Simple HTML + JavaScript (D3.js or Chart.js, no backend required)

**Purpose:**
- Quick visual assessment of corpus credibility landscape
- Identify patterns at a glance
- Shareable with Aaron for validation planning

### Success Criteria

**Completeness:**
- ✅ All 11 papers have full credibility scorecards
- ✅ All scorecards use same rubric version (consistency)
- ✅ All uncertainty metrics collected

**Analysis Quality:**
- ✅ Cross-paper patterns are interpretable
- ✅ Outliers have plausible explanations
- ✅ Improvement themes are actionable

**Presentation:**
- ✅ Dashboard is functional and informative
- ✅ Analysis document is clear and comprehensive
- ✅ Ready to share with Aaron for validation feedback

---

## Phase 5: Refinement and Documentation (Week 7, 8-12 hours)

### Goal
Production-ready assessment system, validated and documented, ready for Aaron and broader use

### Deliverables

#### Validation
- `assessment-system/validation/expert-review-protocol.md` - Protocol for Aaron's validation
- Package of 2-3 papers for Aaron's independent assessment

#### Documentation
- `docs/assessment-guide/README.md` - Complete assessment guide
- `docs/assessment-guide/credibility-rubrics.md` - User-facing rubric documentation
- `docs/assessment-guide/interpretation-guide.md` - How to read scorecards

#### Publication
- `planning/assessment-methodology-paper-outline.md` - Academic paper outline

### Components

#### 5.1 Expert Validation Preparation (3-4 hours)

**Select Papers for Aaron's Review:**
- 2-3 papers spanning disciplines and score ranges
- Ideally include one lab-based science paper if available (for repliCATS comparison)

**Package Materials:**
- Extraction.json files
- Our credibility scorecards
- Quantitative metrics
- Rubrics and assessment prompts
- Blank scorecard template for Aaron's independent assessment

**Design Expert Elicitation Protocol:**
- Instructions for Aaron
- Which signals to focus on
- How to score (using our rubrics)
- Time estimate (2-3 hours per paper)
- Feedback questions:
  - Do rubrics make sense?
  - Are scores plausible?
  - Systematic biases detected?
  - Suggested refinements?

**Comparison Framework:**
- Calculate inter-rater agreement (Aaron vs LLM)
- Identify discrepancies
- Categorise disagreements (rubric ambiguity, evidence interpretation, domain norms)
- Plan rubric refinements

#### 5.2 Assessment Guide Documentation (3-4 hours)

**File:** `docs/assessment-guide/README.md`

**Contents:**
- **Overview:** What credibility assessment is, why it matters
- **Quick start:** How to run assessment on a new paper
- **Assessment workflow:** Step-by-step (quantitative → qualitative → synthesis)
- **Interpreting results:** How to read scorecards, what scores mean
- **Validation:** How system was validated, known accuracy
- **Troubleshooting:** Common issues and solutions
- **Advanced usage:** Customising rubrics, adding signals, batch processing

**File:** `docs/assessment-guide/credibility-rubrics.md` (user-facing version)

**Contents:**
- Simplified rubric descriptions (less technical than internal version)
- Examples of high/medium/low scoring papers per signal
- FAQs about scoring edge cases
- Domain-specific guidance (archaeology vs ethnography vs philology)

**File:** `docs/assessment-guide/interpretation-guide.md`

**Contents:**
- What credibility scores do and don't mean
- How to use scores for improvement (not judgement)
- Uncertainty interpretation
- Comparative vs absolute assessment
- Avoiding misuse (scores as gatekeeping, ranking pressure)

#### 5.3 Methodology Paper Outline (2-4 hours)

**File:** `planning/assessment-methodology-paper-outline.md`

**Proposed Title:** "LLM-Assisted Credibility Assessment for HASS Fieldwork Research: Adapting the repliCATS Framework"

**Outline:**

1. **Introduction**
   - Reproducibility crisis in HASS
   - Existing frameworks (repliCATS) limited to lab sciences
   - Need for HASS-adapted credibility assessment
   - LLMs as scalable assessment tools

2. **Background**
   - RepliCATS seven signals framework
   - HASS fieldwork methodologies (archaeology, ethnography, palaeoenvironmental)
   - LLM capabilities for research assessment

3. **Methods**
   - Extraction phase (CEM/RDMAP graphs)
   - Quantitative metrics (8 metrics described)
   - Qualitative rubrics (7 signals adapted to HASS)
   - Multi-agent LLM workflow
   - Validation approach (expert agreement, internal consistency)

4. **Results**
   - 11-paper corpus description
   - Quantitative metrics distributions
   - Qualitative assessment results
   - Inter-rater reliability (LLM vs expert)
   - Cross-paper patterns
   - Signal correlations

5. **Discussion**
   - HASS vs lab science differences in credibility assessment
   - Strengths and limitations of LLM assessment
   - Scalability potential
   - Implications for open research practices

6. **Conclusion**
   - Framework is viable for HASS credibility assessment
   - LLMs can augment (not replace) expert judgement
   - Path to broader adoption

**Next Steps:**
- Share outline with Aaron
- Get feedback on framing
- Identify journal targets (e.g., *Meta-Psychology*, *Royal Society Open Science*)

### Success Criteria

**Validation Preparation:**
- ✅ Aaron has clear protocol and materials
- ✅ Papers selected strategically

**Documentation:**
- ✅ Guides are comprehensive and accessible
- ✅ Users can run assessments without assistance
- ✅ Interpretation guidance prevents misuse

**Methodology Paper:**
- ✅ Outline is coherent and publication-ready
- ✅ Aaron provides feedback on framing
- ✅ Target journals identified

---

## Timeline Summary

| Phase | Duration | Effort | Key Deliverable |
|-------|----------|--------|-----------------|
| 1. Foundation | Week 1 | 12-15h | Quantitative metrics on 11 papers |
| 2. Qualitative Depth | Weeks 2-3 | 18-24h | Rubrics + deep assessment on 3 papers |
| 3. Architecture for Scale | Weeks 4-5 | 15-20h | Multi-agent LLM workflow |
| 4. Full Corpus | Week 6 | 10-15h | All 11 papers assessed + analysis |
| 5. Refinement | Week 7 | 8-12h | Validation prep + documentation |
| **Total** | **7 weeks** | **63-86 hours** | **Production assessment framework** |

---

## Risk Mitigation

### Risk 1: Metrics Don't Discriminate
**Symptom:** All papers score similarly on quantitative metrics
**Mitigation:** Refine metric calculations, add new metrics, focus on qualitative rubrics
**Contingency:** Use qualitative assessment as primary, metrics as supplementary

### Risk 2: Rubrics Are Ambiguous
**Symptom:** High variance in multi-run scores, Shawn disagrees with LLM frequently
**Mitigation:** Iterative rubric refinement based on pilot assessments
**Contingency:** Simplify rubrics to fewer score levels (e.g., Low/Medium/High instead of 0-100)

### Risk 3: LLM Assessment Unreliable
**Symptom:** LLM scores don't correlate with expert judgement or quantitative metrics
**Mitigation:** Prompt engineering, ensemble methods (multiple LLMs), chain-of-thought reasoning
**Contingency:** Fall back to manual expert assessment, use LLM for evidence retrieval only

### Risk 4: Scale Issues
**Symptom:** Assessment takes too long per paper (>3 hours)
**Mitigation:** Streamline prompts, parallelise signal assessments, automate more
**Contingency:** Assess subset of signals per paper, triage based on quantitative flags

### Risk 5: Aaron Validation Reveals Systematic Bias
**Symptom:** LLM consistently scores higher/lower than expert, or misses key issues
**Mitigation:** Document biases, recalibrate rubrics, re-run assessments
**Contingency:** Hybrid approach (LLM first pass, expert review for flagged papers)

---

## Success Metrics (End of Phase 5)

**Technical Metrics:**
- ✅ All 11 papers have complete credibility assessments (quantitative + qualitative)
- ✅ Assessment workflow is documented and repeatable
- ✅ Code is modular, tested, and version-controlled

**Validation Metrics:**
- ✅ Quantitative metrics correlate with qualitative signals (r > 0.6)
- ✅ LLM-expert agreement >70% (scores within ±15 points)
- ✅ Multi-run score variance <10 points per signal

**Output Quality Metrics:**
- ✅ Scorecards are clear, actionable, and evidence-based
- ✅ Cross-paper analysis reveals interpretable patterns
- ✅ Dashboard is functional and informative

**Validation Readiness:**
- ✅ Aaron has clear protocol and materials for external validation
- ✅ Methodology is documented for academic publication
- ✅ Framework is ready to scale to larger corpus (20-30 papers)

---

## Next Steps After Phase 5

### Short-term (Months 2-3):
1. Aaron conducts external validation on 3-5 papers
2. Refine rubrics based on Aaron's feedback
3. Expand corpus to 20-30 papers across broader HASS disciplines
4. Re-run assessments on expanded corpus
5. Analyse validation results and inter-rater reliability

### Medium-term (Months 4-6):
6. Draft methodology paper
7. Create public-facing dashboard for corpus
8. Develop training materials for other researchers
9. Pilot with external users (2-3 research groups)
10. Gather feedback and iterate

### Long-term (Months 7-12):
11. Submit methodology paper for publication
12. Release assessment framework as open-source tool
13. Build community of practice around credibility assessment
14. Integrate with existing infrastructure (OSF, Zenodo, journals)

---

## References

### Internal Documents
- `planning/extraction-to-analysis-transition.md` - Original transition roadmap
- `docs/background-research/replicats-seven-signals-hass-adaptation.md` - Signal definitions
- `docs/background-research/replicats-report.md` - RepliCATS IDEA protocol
- `assessment-system/prompts/assessment-medium.md` - Extraction quality assessment (existing)

### External References
- Hanea et al. (2021). "The Epistemic Uncertainty of Experts: Elicitation and Aggregation." *MetaArXiv*
- Fraser et al. (2021). "Predicting reliability through structured expert elicitation with repliCATS." *MetaArXiv*
- Wilkinson et al. (2016). "The FAIR Guiding Principles for scientific data management and stewardship." *Scientific Data*

---

## Document History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | 2025-11-14 | Initial plan created | Claude Sonnet 4.5 |

---

**Status:** Phase 1 in progress
**Next Review:** After Phase 1 completion (Week 1)
**Contact:** Shawn Graham (expert validation), Aaron Willcox (external validation - Phase 5+)
