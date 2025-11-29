# Credibility Assessment Implementation Plan v2.0
## Revised Architecture with Quality Gating, Reliability Checks, and 6-Prompt Design

**Document Purpose:** Implementation-ready plan incorporating external review feedback and design refinements

**Date Created:** 2025-11-17
**Version:** 2.0 (revised from v1.0 based on synthesis of Claude + GPT-5.1 feedback + Shawn decisions)
**Status:** Implementation-ready
**Prerequisites:** Extraction complete (Pass 0-6), metrics calculated (Phase 6)

---

## Document Changelog

### Changes from v1.0 to v2.0

**Major architectural changes:**
1. **6-prompt architecture** (down from 10) - Signals clustered by conceptual coherence
2. **Track A quality gating** - Three-state system with behavioral rules
3. **Approach-specific scoring anchors** - Concrete 0-100 scales per research approach
4. **Test-retest reliability checks** - Quantitative validation at multiple checkpoints
5. **Canonical assessment.json** - Post-processing consolidation for corpus analysis
6. **Early repliCATS pilot** - Phase 1.5 added for structural alignment validation

**Medium improvements:**
7. Low-confidence classification handling integrated with Track A
8. File format standardization (JSON for data, Markdown for narrative)
9. Defeasible "no expressed method" interpretation
10. Metric-signal soft guidance with divergence monitoring
11. Experimental system disclaimer in all reports
12. Cross-signal coherence checking added to validation

**Design decisions finalized:**
- Extend research-assessor skill (not separate credibility-assessor)
- 500-line prompt threshold = monitoring point, not hard ceiling
- RepliCATS access confirmed via colleague (early pilot enabled)
- Manual assessment of 3 papers by Shawn in Phase 4 (gold standard)

---

## Executive Summary

### What This Plan Delivers

A credible, robust credibility assessment system consisting of:
- **Research approach classifier** (expressed vs revealed methodology with HARKing detection)
- **Quality gating system** (Track A monitors extraction quality, gates assessment)
- **Six signal assessment clusters** (repliCATS Seven Signals, grouped for coherence)
- **Comprehensive reports** (3-5 pages with experimental disclaimer)
- **Validation framework** (test-retest reliability, metric correlation, repliCATS pilot)

### Architecture Principles

**Skills = Stable Knowledge, Prompts = Evolving Instructions**
- **Skills provide:** Frameworks, schemas, approach taxonomies, signal definitions
- **Prompts provide:** Task-specific instructions that evolve through empirical testing
- **Why:** Enables prompt iteration without skill versioning conflicts

**Prompt Consolidation by Conceptual Coherence**
- Signals grouped where they interact (foundational clarity, evidential strength, scope)
- Reduces maintenance burden (6 vs 10 prompts)
- Enables cross-signal reasoning within clusters
- All prompts ≤ 550 lines (close to 500-line monitoring threshold)

**Quality-First Assessment**
- Track A quality check determines assessment pathway
- Three states: High (full report), Moderate (caveated), Low (abort)
- Reports reflect assessment confidence prominently

---

## Part 1: Prompt vs Skill Boundary Analysis

### Skill-Creator Guidance Applied

*[Unchanged from v1.0 - this section remains valid]*

#### What Goes in Skills (Stable Knowledge)

**Skills are for:**
- Decision frameworks (how to apply rubrics)
- Schema definitions (output structures)
- Reference materials (signal definitions, approach characteristics)
- Domain expertise (HASS-specific adaptations)

**For credibility assessment, skills contain:**
1. **Credibility frameworks** - How to interpret signals per research approach
2. **Signal definitions** - What each repliCATS signal means in HASS context
3. **Approach taxonomy** - Characteristics of inductive/deductive/abductive research
4. **Assessment schemas** - Output structure for classifications and assessments
5. **Quality monitoring frameworks** - Track A self-assessment criteria

#### What Goes in Runtime Prompts (Evolving Instructions)

**Prompts are for:**
- Specific assessment instructions
- Task-specific guidance that evolves through testing
- Context-specific examples
- Workflow orchestration

**For credibility assessment, prompts contain:**
1. **Classification instructions** - How to classify this specific paper
2. **Signal cluster assessment instructions** - How to assess related signals together
3. **Quality gating instructions** - How to determine assessment viability
4. **Report generation instructions** - How to structure the final report

### Recommendation: Extend research-assessor Skill

**Decision rationale (Shawn's input):**
- Activities organically linked (credibility depends on extraction schemas)
- Progressive disclosure manages complexity effectively
- Track A monitors extraction quality (direct linkage)
- Compartmentalized references maintain clarity (`references/credibility/` separate from `references/extraction/`)

**What to add to research-assessor skill:**
```
.claude/skills/research-assessor/
├── SKILL.md (update: add Passes 8-9, credibility assessment)
└── references/
    ├── credibility/
    │   ├── approach-taxonomy.md              # Inductive/deductive/abductive
    │   ├── signal-definitions-hass.md        # Seven signals for HASS
    │   ├── assessment-frameworks.md          # Approach-specific frameworks
    │   ├── harking-detection-guide.md        # Expressed vs revealed
    │   └── track-a-quality-criteria.md       # Quality gating framework
    └── schema/
        ├── classification-schema.md           # Research approach output
        └── assessment-schema.md               # Signal assessment output
```

**What stays as runtime prompts:**
```
assessment-system/prompts/
├── classify-research-approach.md              # Classification (~400 lines)
├── track-a-quality-gate.md                    # Quality gating (~300 lines)
├── assess-foundational-clarity.md             # Comprehensibility + Transparency (~500 lines)
├── assess-evidential-strength.md              # Plausibility + Validity + Robustness (~550 lines)
├── assess-reproducibility-scope.md            # Reproducibility + Generalisability (~400 lines)
└── generate-credibility-report.md             # Report synthesis (~400 lines)
```

---

## Part 2: Prompt Architecture Diagram (REVISED)

### Overview: 6 Prompts with Quality Gating

**Key change from v1.0:** Consolidation from 10 prompts to 6, based on:
- Conceptual coherence (signals that interact grouped together)
- Size constraints (all prompts 300-550 lines, monitoring threshold ~500)
- Maintainability (fewer prompts = easier refinement)

```
┌─────────────────────────────────────────────────────────────────┐
│                    INPUT: extraction.json                        │
│          (Claims, Evidence, RDMAP, Infrastructure, Metrics)      │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ↓
┌─────────────────────────────────────────────────────────────────┐
│  PROMPT 1: classify-research-approach.md (~400 lines)            │
│  • Detects expressed approach (what paper states)               │
│  • Infers revealed approach (what paper does)                   │
│  • Compares expressed vs revealed (HARKing detection)           │
│  • Handles "none_stated" with context sensitivity              │
│  • Outputs: classification.json                                 │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ↓
                  classification.json
                         │
                         ↓
┌─────────────────────────────────────────────────────────────────┐
│  PROMPT 2: track-a-quality-gate.md (~300 lines)                  │
│  • Evaluates extraction quality (completeness, accuracy)         │
│  • Validates metric-assessment alignment                         │
│  • Checks classification confidence                              │
│  • OUTPUTS QUALITY STATE: "high|moderate|low"                   │
│  • Determines assessment pathway                                 │
│  • Outputs: track-a-quality.md + quality state                  │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ↓
                  ┌──────┴──────┐
                  │ Quality State│
                  └──────┬──────┘
        ┌────────────────┼────────────────┐
        │                │                 │
   [HIGH QUALITY]   [MODERATE]         [LOW]
        │                │                 │
        ↓                ↓                 ↓
  Full assessment  Caveated assessment  Abort
   (3 clusters)    (3 clusters)       (Track A only)
        │                │
        │                │
        └────────┬───────┘
                 │
                 ↓
        ┌────────────────────────────────┐
        │  PARALLEL EXECUTION (3 prompts)│
        │  All use same inputs:          │
        │  • extraction.json             │
        │  • classification.json         │
        │  • metrics.json                │
        │  • quality_state               │
        └────────────────────────────────┘
                 │
        ┌────────┼────────┐
        │        │        │
        ↓        ↓        ↓
┌──────────┐ ┌──────────┐ ┌──────────┐
│ PROMPT 3 │ │ PROMPT 4 │ │ PROMPT 5 │
│Foundatio-│ │Evidential│ │Reproduc- │
│nal       │ │Strength  │ │ibility & │
│Clarity   │ │          │ │Scope     │
│          │ │          │ │          │
│Comprehen-│ │Plausibi- │ │Replicab- │
│sibility  │ │lity      │ │ility     │
│+         │ │+         │ │+         │
│Transpare-│ │Validity  │ │Generaliz-│
│ncy       │ │+         │ │ability   │
│          │ │Robustness│ │          │
│(~500)    │ │(~550)    │ │(~400)    │
└────┬─────┘ └────┬─────┘ └────┬─────┘
     │            │            │
     ↓            ↓            ↓
cluster-1.md  cluster-2.md cluster-3.md
(2 signals)   (3 signals)  (2 signals)
                 │
        ┌────────┴────────┐
        │                 │
        ↓                 ↓
  All 3 clusters    track-a-quality.md
  + classification.json
        │
        ↓
┌─────────────────────────────────────────────────────────────────┐
│  PROMPT 6: generate-credibility-report.md (~400 lines)           │
│  • Loads all inputs (classification, 3 clusters, Track A)        │
│  • Synthesises seven-signal assessment                           │
│  • Applies approach-specific emphasis                            │
│  • Applies quality-state caveats (if moderate)                   │
│  • Generates 3-5 page report with disclaimer                     │
│  • Outputs: credibility-report-v1.md                            │
│  • Outputs: assessment.json (canonical consolidation)           │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ↓
┌─────────────────────────────────────────────────────────────────┐
│              OUTPUTS: credibility-report-v1.md                   │
│                      + assessment.json                           │
│    (Complete credibility assessment with quality caveats)        │
└─────────────────────────────────────────────────────────────────┘
```

### Signal Clustering Rationale

**Cluster 1: Foundational Clarity (Comprehensibility + Transparency)**
- **Conceptual link:** Both assess how clearly research is communicated
- **Interaction:** Poor comprehensibility undermines transparency interpretation
- **Size:** ~500 lines (at monitoring threshold)

**Cluster 2: Evidential Strength (Plausibility + Validity + Robustness)**
- **Conceptual link:** All assess strength of evidence-claim relationships
- **Interaction:** Plausibility → Validity → Robustness is reasoning chain
- **Size:** ~550 lines (slightly over threshold, but tightly related content)

**Cluster 3: Reproducibility & Scope (Reproducibility + Generalisability)**
- **Conceptual link:** Both assess appropriate boundaries and reproduction
- **Interaction:** Reproducibility infrastructure enables generalisability assessment
- **Size:** ~400 lines (well under threshold)

### Execution Dependencies

**Sequential dependencies:**
1. `classification.json` MUST exist before Track A runs
2. Track A quality state MUST exist before signal clusters run
3. All signal clusters + Track A MUST exist before report generation

**Parallel execution opportunities:**
- Prompts 3-5 (3 signal clusters) can run concurrently once quality gating complete
- No dependencies between clusters

**Quality-conditional execution:**
- If quality_state = "low" → Skip Prompts 3-5, generate Track A report only

---

## Part 3: Skill Extension Design

### research-assessor Skill Updates

*[Most content unchanged from v1.0, key additions noted]*

#### SKILL.md Description Update

**Updated description:**
```yaml
description: Extracts and assesses research methodology, claims, evidence, and infrastructure from research papers in HASS disciplines. Evaluates transparency, reproducibility, and credibility through systematic extraction (seven-pass workflow) and credibility assessment (research approach classification, quality gating, and repliCATS Seven Signals evaluation adapted for HASS).
```

#### SKILL.md Workflow Section Addition

*[Passes 8-9 from v1.0 retained, with addition of quality gating note]*

```markdown
### Pass 8: Research Approach Classification

[Content from v1.0 unchanged]

### Pass 9: Credibility Assessment (Quality-Gated)

**Purpose:** Assess paper credibility using repliCATS Seven Signals adapted for HASS

**Inputs:**
- extraction.json
- classification.json
- metrics.json

**Process:**
1. **Track A quality gating** (determines pathway):
   - Evaluate extraction quality
   - Output quality_state: "high|moderate|low"
   - Route to appropriate assessment pathway

2. **Signal cluster assessment** (if quality ≥ moderate):
   - Assess foundational clarity (Comprehensibility + Transparency)
   - Assess evidential strength (Plausibility + Validity + Robustness)
   - Assess reproducibility & scope (Reproducibility + Generalisability)
   - Apply approach-specific scoring anchors

3. **Report generation:**
   - Synthesise seven signals
   - Apply quality caveats (if moderate)
   - Generate canonical assessment.json

**Outputs:**
- track-a-quality.md
- cluster-1-foundational-clarity.md (if quality ≥ moderate)
- cluster-2-evidential-strength.md (if quality ≥ moderate)
- cluster-3-reproducibility-scope.md (if quality ≥ moderate)
- credibility-report-v1.md (or track-a-only.md if quality = low)
- assessment.json (canonical consolidation)
```

#### New Reference File: track-a-quality-criteria.md (ENHANCED)

**NEW SECTION: Quality Gating Framework**

```markdown
# Track A Quality Monitoring and Gating Criteria
## Self-Assessment Framework with Behavioral Rules

### Quality Dimensions

[Existing content from v1.0 retained]

### Quality Gating Decision Logic (NEW)

**Quality assessment produces three possible states:**

#### STATE 1: HIGH QUALITY → Full Assessment

**Triggers:**
- Extraction confidence: High
- Metric-assessment alignment: Yes
- Classification confidence: High OR Medium
- No major extraction errors identified

**Behaviour:**
- Run all 7 signal assessments (3 cluster prompts)
- Generate full 3-5 page report
- Apply approach-specific anchors with confidence
- Standard file naming: `credibility-report-v1.md`

#### STATE 2: MODERATE QUALITY → Caveated Assessment

**Triggers (any of):**
- Extraction confidence: Medium
- Metric-assessment alignment: Partial
- Classification confidence: Low
- Classification expressed vs revealed: Mismatched (unclear type)
- Research approach: "Mixed" with high ambiguity

**Behaviour:**
- Run all 7 signal assessments (3 cluster prompts)
- Generate report with prominent "Assessment Limitations" section at top
- Constrain scoring to 20-point bands (e.g., 60-80, not precise 72)
- All signal cluster files include bold caveat header
- Use approach-generic rubrics (no approach-specific anchors if classification ambiguous)
- File naming: `credibility-report-v1-CAVEATED.md`

**Caveat header for cluster files:**
```markdown
> **ASSESSMENT QUALITY CAVEAT**
>
> This assessment is based on medium-confidence extraction. [Specific limitation: e.g., "Classification
> is ambiguous (low confidence)" OR "Metric-signal alignment is partial"]. Scores should be interpreted
> as approximate ranges rather than precise values.
```

#### STATE 3: LOW QUALITY → Abort Assessment

**Triggers (any of):**
- Extraction confidence: Low
- Major extraction errors identified (e.g., claims/evidence severely incomplete)
- Classification completely ambiguous (cannot determine approach)
- Structural problems with paper (e.g., paywall, corrupted PDF, non-research content)

**Behaviour:**
- **Do not run** signal cluster assessments (Prompts 3-5)
- Generate Track A quality report only
- Create brief `assessment-not-viable.md` explaining why assessment aborted
- Flag paper for re-extraction or manual review
- File naming: `track-a-only.md` + `assessment-not-viable.md`

**Example assessment-not-viable.md:**
```markdown
# Credibility Assessment Not Viable
## Paper: {paper-slug}

**Quality State:** Low

**Assessment Date:** {date}

## Reason for Abortion

Extraction confidence is low due to [specific issue: e.g., "incomplete methods extraction - only 2 of estimated 8-10 methods captured"]. Credibility assessment requires higher extraction quality to produce meaningful signal scores.

## Recommended Actions

1. **Re-extract** paper with revised prompt guidance for [specific sections]
2. **Manual review** of extraction to identify systematic errors
3. **Alternative:** Manually assess if urgent; LLM assessment not viable at this quality level

## Track A Quality Notes

[Full Track A analysis explaining quality issues]
```

### Output Format

**Track A prompt must output quality state explicitly:**

```yaml
track_a_quality:
  quality_state: "high|moderate|low"  # REQUIRED: Determines assessment pathway
  extraction_confidence: "high|medium|low"
  extraction_notes: "..."
  metric_signal_alignment: "yes|partial|no"
  classification_confidence: "high|medium|low"
  assessment_viability_summary: "..."
  improvement_opportunities: [...]
```

### Implementation in Prompts

**track-a-quality-gate.md prompt must:**
1. Evaluate quality dimensions
2. Apply gating decision logic
3. Output quality_state prominently
4. Generate track-a-quality.md with decision justification

**Signal cluster prompts (3-5) must:**
1. Read quality_state from track-a-quality.md
2. If moderate: Apply caveats, use 20-point bands, add warning headers
3. If low: Should not execute (workflow skips)

**generate-credibility-report.md prompt must:**
1. Read quality_state
2. Apply state-appropriate formatting
3. Name file according to state (standard vs `-CAVEATED`)
```

*[Other reference files from v1.0 retained with additions noted below]*

#### Enhanced Reference File: signal-definitions-hass.md

**NEW SECTION: Approach-Specific Scoring Anchors**

Add to each signal definition:

```markdown
## Signal N: {Signal Name}

[Existing definition content from v1.0]

### Approach-Specific Scoring Anchors (0-100 Scale)

#### For Deductive Research (Hypothesis-Testing)

**Example: Transparency Signal**

**80-100: Excellent Transparency**
- Pre-registered study design and analysis plan (or convincing explanation for absence)
- Comprehensive methods documentation with protocols
- Data and code publicly available with persistent identifiers
- All research materials accessible
- Explicit limitations and assumptions stated

**60-79: Good Transparency**
- Clear research design and hypothesis specification
- Detailed methods documentation
- Data availability clearly stated (even if embargoed)
- Code or analysis workflow documented
- Major limitations acknowledged

**40-59: Moderate Transparency**
- Research design stated (may lack detail)
- Methods described (gaps present)
- Data availability mentioned (may be vague)
- Some protocol documentation
- Limitations present (may be minimal)

**20-39: Low Transparency**
- Implicit research design
- Incomplete methods (hard to assess procedures)
- Data availability unclear or unstated
- Minimal protocol documentation
- Limitations absent or superficial

**0-19: Minimal Transparency**
- No clear research design
- Vague or absent methods
- No data/code sharing information
- No protocol documentation
- No acknowledgment of limitations

#### For Inductive Research (Exploratory, Pattern-Finding)

**80-100: Excellent Transparency**
- Clear documentation of exploratory goals and research questions
- Comprehensive data collection and sampling procedures
- Analysis workflow documented (how patterns identified)
- Data archived with documentation
- Explicit scope constraints and interpretation limitations
- *Note: Pre-registration not expected; emphasis on workflow transparency*

**60-79: Good Transparency**
- Research goals clearly stated
- Data collection procedures documented
- Analysis approach described
- Data accessible (or access path clear)
- Limitations acknowledged

**40-59: Moderate Transparency**
- Research goals present (may lack specificity)
- Data collection described (gaps present)
- Analysis approach mentioned (may be vague)
- Data availability partially addressed
- Some limitations noted

**20-39: Low Transparency**
- Vague research goals
- Incomplete data collection documentation
- Analysis approach unclear
- Data availability not addressed
- Minimal limitations

**0-19: Minimal Transparency**
- No clear research goals
- Data collection not documented
- Analysis process opaque
- No data sharing
- No limitations

#### For Abductive Research (Inference to Best Explanation)

**80-100: Excellent Transparency**
- Theoretical framework explicitly stated
- Alternative explanations considered and documented
- Evidence selection criteria transparent
- Reasoning process traceable
- Data/sources accessible
- Scope and limitations of inference clearly bounded

**60-79: Good Transparency**
- Framework stated
- Some alternative explanations considered
- Evidence criteria mentioned
- Reasoning documented
- Sources accessible

**40-59: Moderate Transparency**
- Framework implicit or partial
- Limited consideration of alternatives
- Evidence criteria unclear
- Reasoning partially documented
- Some source access

**20-39: Low Transparency**
- Vague framework
- No alternative explanations
- Evidence selection opaque
- Reasoning not documented
- Source access unclear

**0-19: Minimal Transparency**
- No theoretical framework
- Single interpretation, no alternatives
- Evidence selection arbitrary
- Reasoning not traceable
- No source access

### Scoring Guidance

**How to use approach-specific anchors:**

1. **Identify research approach** from classification.json
2. **Select appropriate anchor set** (deductive/inductive/abductive)
3. **Assess paper against anchor descriptions** (not universal criteria)
4. **Assign score within appropriate band**
5. **Justify score by referencing specific anchor criteria met or missed**

**Example justification:**
> "Transparency scored 75 (Good Transparency band for inductive research). This paper clearly documents exploratory goals and data collection procedures (required for 60-79), has archived data (60-79), but lacks detailed analysis workflow documentation (would move to 80-100). Pre-registration not expected for inductive work, so absence does not lower score."

**Cross-approach note:**
> A score of 75 means different things for different approaches. 75 for deductive research implies data + code sharing; 75 for inductive research implies workflow transparency. Do not compare scores across approaches numerically; compare against anchor descriptions.
```

*[Repeat approach-specific anchors for all 7 signals]*

---

## Part 4: File Structure Specification

### Complete Directory Structure (REVISED)

```
outputs/{paper-slug}/
├── extraction.json                           # From Passes 1-6 (existing)
├── {paper-slug}.txt                          # Plain text (existing)
├── metrics/                                  # From Phase 6 (existing)
│   └── metrics.json                          # 8 credibility metrics
├── assessment/                               # NEW: Credibility assessment outputs
│   ├── classification.json                   # Research approach classification
│   ├── track-a-quality.md                   # Quality monitoring + state
│   ├── clusters/                            # NEW: Signal cluster assessments
│   │   ├── cluster-1-foundational-clarity.md    # Comprehensibility + Transparency
│   │   ├── cluster-2-evidential-strength.md     # Plausibility + Validity + Robustness
│   │   └── cluster-3-reproducibility-scope.md   # Reproducibility + Generalisability
│   ├── credibility-report-v1.md             # 3-5 page report (or -CAVEATED.md)
│   ├── assessment.json                      # NEW: Canonical consolidation
│   └── assessment-not-viable.md             # Only if quality_state = "low"
└── logs/                                     # Optional: Workflow logs
    └── assessment-log.md
```

### File Descriptions (UPDATED)

**`classification.json`** (JSON format)

*[Content from v1.0 retained, no changes needed]*

**`track-a-quality.md`** (Markdown report with quality state)

```markdown
# Track A: Extraction & Assessment Quality Report
## Paper: {paper-slug}

**Quality State:** HIGH|MODERATE|LOW
**Assessment Date:** 2025-11-17

---

## Quality State Decision

**Rationale:** [Why this quality state assigned - which triggers met]

---

## Extraction Confidence

**Overall:** High|Medium|Low

### Claims Extraction
- **Completeness:** [Estimate: captured X of estimated Y claims]
- **Accuracy:** [Evidence of correct claim identification]
- **Notes:** [Specific issues or strengths]

### Evidence Extraction
- **Completeness:** [Estimate]
- **Accuracy:** [Assessment]
- **Notes:** [...]

### RDMAP Extraction
- **Completeness:** [...]
- **Accuracy:** [...]
- **Notes:** [...]

### Infrastructure Extraction
- **Completeness:** [...]
- **Accuracy:** [...]
- **Notes:** [...]

---

## Metric-Signal Alignment

**Overall Alignment:** Yes|Partial|No

### Metric-Signal Divergences Identified

- **ESD vs Validity signal:** [Expected relationship, observed relationship, divergence if any]
- **TCI vs Transparency signal:** [...]
- **RTI vs Robustness signal:** [...]

[For each divergence, note whether explained or problematic]

---

## Classification Quality

**Classification Confidence:** High|Medium|Low
**Classification Notes:** [Certainties and uncertainties in approach classification]

---

## Assessment Implications

**If HIGH quality:**
- Proceed with full signal assessment
- Apply approach-specific anchors with confidence
- Generate standard report

**If MODERATE quality:**
- Proceed with caveated assessment
- Use 20-point score bands
- Apply approach-generic rubrics if classification is ambiguous
- Generate report with prominent limitations section

**If LOW quality:**
- Abort signal assessment
- Generate Track A report and assessment-not-viable notice
- Recommend re-extraction or manual review

---

## Improvement Opportunities

1. [Specific improvement for extraction]
2. [Specific improvement for metrics]
3. [Specific improvement for classification]
4. [...]

---

**Report Version:** 2.0
**Track A Framework:** references/credibility/track-a-quality-criteria.md
```

**`clusters/cluster-1-foundational-clarity.md`** (Example signal cluster assessment)

```markdown
# Signal Cluster Assessment: Foundational Clarity
## Comprehensibility + Transparency
## Paper: {paper-slug}

[IF QUALITY_STATE = "MODERATE", ADD:]
> **ASSESSMENT QUALITY CAVEAT**
>
> This assessment is based on [specific limitation]. Scores should be interpreted as
> approximate 20-point ranges rather than precise values.

---

## Cluster Overview

This cluster assesses how clearly the research is communicated. Comprehensibility evaluates clarity of claims and argument structure; Transparency evaluates completeness of research design and methods documentation. These signals are assessed together because poor comprehensibility undermines ability to evaluate transparency.

---

## Signal 1: Comprehensibility

**Score:** 75/100 [or 60-80 if moderate quality]
**Confidence:** High|Medium|Low

### Signal Definition

Comprehensibility: Clarity of research claims, argument structure, and overall communication.

### Assessment Summary

[2-3 sentence summary of comprehensibility evaluation]

### Key Strengths

- [Specific strength with evidence from extraction]
- [Specific strength]
- [Specific strength]

### Key Weaknesses

- [Specific weakness with evidence]
- [Specific weakness]
- [Specific weakness]

### Supporting Evidence from Extraction

- **Claim structure:** [How claims are formulated - clear vs vague]
- **Argument flow:** [Logical progression assessment]
- **Terminology:** [Specialized terms defined vs assumed]

### Scoring Justification

[Detailed rationale citing approach-specific anchors from signal-definitions-hass.md]

Example:
> "Scored 75 (Good Comprehensibility for inductive research). Claims are clearly formulated with explicit scope (60-79 anchor), argument structure is logical and traceable (60-79), but some domain-specific terminology lacks definition for non-specialist readers (prevents 80-100)."

### Approach-Specific Context

**Research Approach:** [Inductive|Deductive|Abductive from classification]

[How comprehensibility criteria apply to this approach]

Example for inductive:
> "For inductive research, comprehensibility emphasizes clear pattern descriptions and transparent reasoning from observations to interpretations. This paper meets standards for observational clarity but has minor gaps in reasoning documentation."

---

## Signal 2: Transparency

**Score:** 70/100 [or 60-80 if moderate quality]
**Confidence:** High|Medium|Low

### Signal Definition

Transparency: Clarity and completeness of research design, methods, and data documentation.

### Assessment Summary

[2-3 sentence summary]

### Key Strengths

- [With evidence]
- [...]

### Key Weaknesses

- [With evidence]
- [...]

### Supporting Evidence from Extraction

- **RDMAP documentation:** [Extent and quality]
- **Methods detail:** [Protocols present vs absent]
- **Data availability:** [Sharing statements, PIDs]
- **Infrastructure:** [Code, permits, registrations]

### Scoring Justification

[Detailed rationale citing approach-specific anchors]

Example:
> "Scored 70 (Good Transparency for inductive research, approaching 60-79 anchor). Data collection procedures clearly documented (meets 60-79), data archived with DOI (meets 60-79), but analysis workflow lacks detail (prevents 80-100) and no code repository despite computational analysis (minor deduction)."

### Approach-Specific Context

[How transparency applies to this approach]

---

## Cross-Signal Coherence Check

**Do Comprehensibility and Transparency assessments cohere?**

[Check for contradictions - e.g., high comprehensibility but low transparency would be unusual and require explanation]

Example coherence note:
> "Comprehensibility (75) and Transparency (70) scores are coherent. Paper communicates clearly AND documents methods well, with similar minor gaps in both (terminology definitions for comprehensibility, workflow detail for transparency)."

---

## Relevant Metrics

### TCI (Transparency & Completeness Index): [Score from metrics.json]

**Metric-Signal Correlation:** [Does TCI align with Transparency signal?]

Example:
> "TCI = 68, Transparency signal = 70. Strong alignment (correlation expected ~0.7). TCI captures RDMAP completeness; signal additionally considers data/code sharing, which is good for this paper."

### Other Relevant Metrics

- **MDD (Methodological Documentation Density):** [Score and interpretation]

---

**Assessment Date:** 2025-11-17
**Assessor:** Claude (research-assessor skill)
**Framework:** references/credibility/signal-definitions-hass.md, assessment-frameworks.md
**Approach-Specific Anchors Applied:** Yes [or "No - generic HASS criteria used" if moderate quality + classification ambiguous]
```

*[Repeat cluster structure for cluster-2 (evidential strength) and cluster-3 (reproducibility & scope)]*

**`assessment.json`** (NEW: Canonical consolidation)

```json
{
  "paper_id": "sobotkova-et-al-2024",
  "assessment_date": "2025-11-17",
  "system_version": "v0.2-alpha",

  "classification": {
    "expressed_approach": "inductive",
    "revealed_approach": "inductive",
    "expressed_vs_revealed": "matched",
    "revealed_confidence": "high",
    "harking_flag": false,
    "credibility_framework_to_use": "inductive_emphasis",
    "signal_prioritisation": {
      "primary_signals": ["transparency", "comprehensibility", "generalisability"],
      "secondary_signals": ["validity", "robustness"],
      "deemphasised_signals": []
    }
  },

  "track_a": {
    "quality_state": "high",
    "extraction_confidence": "high",
    "metric_signal_alignment": "yes",
    "classification_confidence": "high",
    "assessment_viability_summary": "Extraction quality is high; full assessment viable with standard approach-specific anchors.",
    "improvement_opportunities": [
      "Consider enhancing code documentation extraction for computational methods",
      "..."
    ]
  },

  "signals": [
    {
      "signal_name": "comprehensibility",
      "signal_number": 1,
      "cluster": "foundational_clarity",
      "score": 75,
      "score_band": "60-79",
      "confidence": "high",
      "summary": "Claims clearly formulated; argument structure logical; minor terminology gaps.",
      "strengths": ["Clear claim formulation", "Logical progression", "Accessible writing"],
      "weaknesses": ["Some undefined domain terms", "..."],
      "justification": "Scored 75 (Good Comprehensibility for inductive research)...",
      "approach_context": "For inductive research, comprehensibility emphasizes...",
      "approach_anchors_applied": true
    },
    {
      "signal_name": "transparency",
      "signal_number": 2,
      "cluster": "foundational_clarity",
      "score": 70,
      "score_band": "60-79",
      "confidence": "high",
      "summary": "Good methods documentation and data sharing; workflow detail could improve.",
      "strengths": ["Data archived with DOI", "Methods documented", "..."],
      "weaknesses": ["Workflow lacks detail", "No code repository", "..."],
      "justification": "Scored 70 (Good Transparency for inductive research)...",
      "approach_context": "...",
      "approach_anchors_applied": true
    },
    {
      "signal_name": "plausibility",
      "signal_number": 3,
      "cluster": "evidential_strength",
      "score": 80,
      "score_band": "80-100",
      "confidence": "high",
      "summary": "...",
      "strengths": [...],
      "weaknesses": [...],
      "justification": "...",
      "approach_context": "...",
      "approach_anchors_applied": true
    },
    ... (signals 4-7)
  ],

  "metrics": {
    "ESD": 2.3,
    "TCI": 68,
    "SCS": 55,
    "RTI": 0.42,
    "RIS": 72,
    "PGCS": 45,
    "FCS": 60,
    "MDD": 71
  },

  "report_metadata": {
    "report_path": "assessment/credibility-report-v1.md",
    "report_type": "standard",
    "word_count": 2150,
    "quality_caveats": false
  }
}
```

**Benefits of canonical assessment.json:**
- Enables corpus-level statistics (mean scores per signal, approach-specific profiles)
- Cross-paper comparisons straightforward (`jq` queries)
- Downstream tooling (dashboards, visualizations) simplified
- Preserves all assessment data in machine-readable format

**`credibility-report-v1.md`** (3-5 page report with disclaimer)

```markdown
# Credibility Assessment Report
## {Paper Title}

**Authors:** {authors}
**Publication:** {journal} ({year})
**Assessment Date:** 2025-11-17
**Assessor:** Claude (research-assessor skill)
**System Version:** v0.2-alpha

---

> **EXPERIMENTAL SYSTEM - DEVELOPMENT PHASE**
>
> This assessment was generated by an experimental LLM-based credibility evaluation system
> currently under development. Scores and interpretations should be treated as provisional
> and subject to revision as the system is refined. Do not use for high-stakes decisions.
>
> Assessment quality: HIGH [or MODERATE with specific caveats]
> Report version: 2.0

---

## Executive Summary

[2-3 paragraph overview: credibility profile, key strengths/weaknesses, overall assessment]

**Overall Credibility Profile:** [1-2 sentence characterization]

**Key Strengths:** [Brief list - 3 items]

**Key Weaknesses:** [Brief list - 3 items]

---

## Paper Metadata & Research Approach

### Classification

- **Expressed Approach:** Inductive
- **Revealed Approach:** Primarily inductive
- **Alignment:** Matched
- **Confidence:** High
- **HARKing Flag:** No

### Classification Justification

[Brief summary - 2-3 sentences from classification.json]

### Credibility Framework Applied

**Framework:** Inductive emphasis (transparency, comprehensibility, generalisability as primary signals)

[1 sentence explaining what this means for assessment]

---

[IF QUALITY_STATE = "MODERATE", ADD PROMINENT SECTION HERE:]

## Assessment Limitations

**Quality State:** MODERATE

This assessment is subject to the following limitations:

- [Specific limitation from Track A, e.g., "Classification confidence is low - mixed-method paper resists clean categorization"]
- [Impact on assessment, e.g., "Generic HASS criteria used instead of approach-specific anchors"]
- [Interpretation guidance, e.g., "Scores represent 20-point bands (e.g., 60-80) rather than precise values"]

**Implication:** Treat this report as indicative rather than definitive. Scores should be interpreted as approximate ranges.

---

---

## Credibility Scorecard

### Seven Signals Overview

| Signal              | Score | Band  | Confidence | Cluster              |
|---------------------|-------|-------|------------|----------------------|
| Comprehensibility   | 75    | 60-79 | High       | Foundational Clarity |
| Transparency        | 70    | 60-79 | High       | Foundational Clarity |
| Plausibility        | 80    | 80-100| High       | Evidential Strength  |
| Validity            | 72    | 60-79 | High       | Evidential Strength  |
| Robustness          | 68    | 60-79 | Medium     | Evidential Strength  |
| Reproducibility       | 65    | 60-79 | High       | Reproducibility/Scope|
| Generalisability    | 75    | 60-79 | High       | Reproducibility/Scope|

**Mean Score:** 72 (Good credibility - approaching excellent in some signals)

### Credibility Metrics

| Metric | Score | Interpretation                          |
|--------|-------|-----------------------------------------|
| ESD    | 2.3   | Good evidence density (>2.0)            |
| TCI    | 68    | Good transparency & completeness        |
| SCS    | 55    | Moderate scope constraint documentation |
| RTI    | 0.42  | Moderate research traceability          |
| RIS    | 72    | Good reproducibility infrastructure     |
| PGCS   | 45    | Moderate PID connectivity               |
| FCS    | 60    | Moderate FAIR compliance                |
| MDD    | 71    | Good methodological documentation       |

---

## Seven-Signal Assessment (Detailed)

### Cluster 1: Foundational Clarity

**Cluster Score:** 72.5 average (Comprehensibility 75, Transparency 70)

#### Signal 1: Comprehensibility (75/100 - Good)

[~150-200 words: summary, key strengths/weaknesses, justification]

**Approach Context:** [How comprehensibility applies to inductive research]

#### Signal 2: Transparency (70/100 - Good)

[~150-200 words]

**Approach Context:** [...]

---

### Cluster 2: Evidential Strength

**Cluster Score:** 73.3 average (Plausibility 80, Validity 72, Robustness 68)

#### Signal 3: Plausibility (80/100 - Excellent)

[~150-200 words]

#### Signal 4: Validity (72/100 - Good)

[~150-200 words]

#### Signal 5: Robustness (68/100 - Good)

[~150-200 words]

---

### Cluster 3: Reproducibility & Scope

**Cluster Score:** 70 average (Reproducibility 65, Generalisability 75)

#### Signal 6: Reproducibility (65/100 - Good)

[~150-200 words]

**Approach Context:** [Reproducibility for inductive research = analytic reproducibility, not field replication]

#### Signal 7: Generalisability (75/100 - Good)

[~150-200 words]

---

## Cross-Signal Coherence

**Are the seven signal assessments coherent and mutually reinforcing?**

[2-3 paragraph analysis: Do scores make sense together? Any apparent contradictions? How do clusters relate?]

Example:
> "Signal assessments are highly coherent. Foundational Clarity (72.5 avg) establishes good communication baseline, which supports Evidential Strength assessment (73.3 avg) - we can evaluate evidence because it's clearly documented. Reproducibility & Scope (70 avg) aligns with Transparency (70), reflecting documented data sharing but workflow gaps. The pattern is consistent: strong communication and evidence, moderate reproducibility infrastructure."

---

## Key Strengths & Weaknesses

### Major Strengths

1. **[Strength title]** - [2-3 sentences with specific evidence from extraction]
2. **[...]**
3. **[...]**

### Major Weaknesses

1. **[Weakness title]** - [2-3 sentences with specific evidence]
2. **[...]**
3. **[...]**

---

## Actionable Recommendations

### For This Paper (Retrospective)

**If authors were to revise or publish supplementary materials:**

1. **[Recommendation]** - [Specific action, effort estimate, credibility impact]
   - *Action:* [What to do]
   - *Effort:* [Low/Medium/High]
   - *Impact:* [Would improve Signal X from Y to Z]

2. **[...]**

3. **[...]**

### For Future Research (Prospective)

**Best practices for future work in this domain:**

1. **[Best practice]** - [Why this matters, how to implement]

2. **[...]**

3. **[...]**

---

## Overall Credibility Profile

[Final 2-3 paragraph synthesis]

**Research Approach:** [Inductive|Deductive|Abductive]

**Credibility Signature:** [Descriptive characterization - e.g., "Strong on communication and plausibility, good on validity, moderate on reproducibility"]

**Comparison to Corpus:** [If available - e.g., "Above corpus mean (68) in comprehensibility and plausibility; at corpus mean for reproducibility"]

**Trustworthiness Assessment:** [Overall judgment with caveats]

**Reproducibility Outlook:** [What aspects could be replicated analytically? What could not?]

---

## Track A Quality Notes (Summary)

**Quality State:** HIGH [or MODERATE with explanation]

**Extraction Confidence:** High - Claims (complete), Evidence (complete), RDMAP (complete), Infrastructure (complete)

**Metric-Signal Alignment:** Yes - TCI correlates with Transparency (r~0.7), ESD correlates with Validity, minor divergences explained

**Classification Quality:** High confidence in inductive classification; expressed and revealed approaches matched

**Assessment Limitations:** [None for high quality; specific limitations for moderate; N/A for low quality as report not generated]

**Full Track A report:** `assessment/track-a-quality.md`

---

## Appendices

### Assessment Methodology

**Framework:** RepliCATS Seven Signals adapted for HASS research

**Approach-Specific Anchors:** Yes (inductive research scoring criteria applied)

**Quality Gating:** Track A pre-assessment determined high quality → full assessment viable

**Cluster Assessment:** Signals assessed in conceptually coherent clusters for cross-signal reasoning

### Signal Cluster Files

- `assessment/clusters/cluster-1-foundational-clarity.md` (Comprehensibility + Transparency)
- `assessment/clusters/cluster-2-evidential-strength.md` (Plausibility + Validity + Robustness)
- `assessment/clusters/cluster-3-reproducibility-scope.md` (Reproducibility + Generalisability)

### Canonical Assessment Data

- `assessment/assessment.json` (Machine-readable consolidation of all assessment data)

---

**Report Version:** 2.0
**Generation Date:** 2025-11-17
**Based On:**
- extraction.json (Pass 6 complete)
- metrics.json (8 credibility metrics)
- classification.json (Research approach classification)
- 3 signal cluster assessments (7 signals total)
- track-a-quality.md (Quality gating and monitoring)

**System Documentation:** planning/credibility-implementation-plan-v2.0.md
```

---

## Part 5: Data Flow & Dependencies (UPDATED)

### Input Requirements per Prompt

**PROMPT 1: classify-research-approach.md (~400 lines)**
- **Inputs:**
  - extraction.json (claims, RDMAP, methods structure)
  - Paper full text (if needed for methodological statements)
- **Skill references:**
  - `references/credibility/approach-taxonomy.md`
  - `references/credibility/harking-detection-guide.md`
  - `references/schema/classification-schema.md`
- **Outputs:**
  - classification.json

**PROMPT 2: track-a-quality-gate.md (~300 lines)**
- **Inputs:**
  - extraction.json
  - metrics.json
  - classification.json
- **Skill references:**
  - `references/credibility/track-a-quality-criteria.md` (includes gating decision logic)
- **Outputs:**
  - track-a-quality.md (includes `quality_state: "high|moderate|low"`)
- **Critical output:** `quality_state` determines whether Prompts 3-5 run

**PROMPTS 3-5: assess-{cluster}.md (3 prompts, ~400-550 lines each)**

*Only execute if quality_state ∈ {"high", "moderate"}. Skip if quality_state = "low".*

- **Inputs (all clusters):**
  - extraction.json
  - classification.json
  - metrics.json
  - track-a-quality.md (read quality_state)
- **Skill references (all clusters):**
  - `references/credibility/signal-definitions-hass.md` (with approach-specific anchors)
  - `references/credibility/assessment-frameworks.md`
  - `references/schema/assessment-schema.md`
- **Behavioural rules based on quality_state:**
  - If "high": Apply approach-specific anchors, precise scores, standard format
  - If "moderate": Add caveat headers, use 20-point bands, apply generic rubrics if classification ambiguous
- **Outputs:**
  - clusters/cluster-1-foundational-clarity.md (Comprehensibility + Transparency)
  - clusters/cluster-2-evidential-strength.md (Plausibility + Validity + Robustness)
  - clusters/cluster-3-reproducibility-scope.md (Reproducibility + Generalisability)

**PROMPT 6: generate-credibility-report.md (~400 lines)**
- **Inputs:**
  - classification.json
  - track-a-quality.md (including quality_state)
  - clusters/cluster-1-foundational-clarity.md (if exists)
  - clusters/cluster-2-evidential-strength.md (if exists)
  - clusters/cluster-3-reproducibility-scope.md (if exists)
  - metrics.json (for scorecard table)
- **Skill references:**
  - Assessment frameworks (for synthesis)
- **Behavioural rules based on quality_state:**
  - If "high": Generate credibility-report-v1.md (standard 3-5 pages)
  - If "moderate": Generate credibility-report-v1-CAVEATED.md (with limitations section)
  - If "low": Generate track-a-only.md + assessment-not-viable.md (no signal synthesis)
- **Outputs:**
  - credibility-report-v1.md (or -CAVEATED.md or track-a-only.md)
  - assessment.json (canonical consolidation - always generated)

### Data Flow Summary (UPDATED)

```
extraction.json ─────────┬──────────────────────────────────┐
                         │                                   │
                         ↓                                   │
                  classify-research-approach                 │
                         │                                   │
                         ↓                                   │
                  classification.json                        │
                         │                                   │
        ┌────────────────┴────────────────┐                 │
        │                                  │                 │
        ↓                                  │                 │
  track-a-quality-gate ←─── metrics.json  │                 │
        │                                  │                 │
        ↓                                  │                 │
  track-a-quality.md                       │                 │
  (includes quality_state)                 │                 │
        │                                  │                 │
        ↓                                  │                 │
   [Quality Gate]                          │                 │
        │                                  │                 │
        ├─── "high" ──────────┐            │                 │
        ├─── "moderate" ──────┤            │                 │
        └─── "low" ───> SKIP   │            │                 │
                               │            │                 │
                               ↓            ↓                 │
                       assess-clusters ←────┴─────────────────┘
                       (3 prompts parallel)
                               │
                               ↓
                    cluster-1.md, cluster-2.md, cluster-3.md
                               │
                ┌──────────────┴──────────────┐
                │                             │
                ↓                             ↓
          track-a-quality.md         All cluster files
          + classification.json      (if quality ≥ moderate)
                │                             │
                └──────────────┬──────────────┘
                               │
                               ↓
                    generate-credibility-report
                    (applies quality caveats)
                               │
                               ↓
                ┌──────────────┴──────────────┐
                │                             │
                ↓                             ↓
        credibility-report-v1.md      assessment.json
        (or -CAVEATED.md)             (canonical)
        (or track-a-only.md if low)
```

---

## Part 6: Validation Checkpoints (ENHANCED)

*[All checkpoints from v1.0 retained with significant enhancements for reliability and quality gating]*

### Checkpoint 1: Classifier Working

**After implementing classify-research-approach.md prompt:**

**Test papers:** sobotkova-et-al-2024, ballsun-stanton-et-al-2018, penske-et-al-2023

**Validation criteria:**
- [ ] classification.json generated for all 3 papers
- [ ] All required fields populated (expressed, revealed, comparison, justification)
- [ ] Expressed vs revealed comparison makes sense
- [ ] HARKing detection working (flags mismatches appropriately)
- [ ] "none_stated" handled with context sensitivity (not automatic penalty)
- [ ] Mixed-method papers characterised qualitatively (no false precision)
- [ ] Justifications cite specific extraction elements (claim IDs, RDMAP IDs)

**NEW: Test-Retest Reliability Check (v2.0)**

**Purpose:** Measure classification consistency across multiple runs

**Process:**
1. Run classification 3x on sobotkova-et-al-2024 (identical inputs, different invocations)
2. Run classification 3x on ballsun-stanton-et-al-2018
3. Run classification 3x on penske-et-al-2023

**Measurements:**
- **Expressed approach consistency:** Should be identical across all 3 runs (deterministic from paper text)
- **Revealed approach consistency:**
  - Acceptable: All 3 runs agree OR 2/3 runs agree and 3rd is "mixed"
  - Threshold: <2 classification changes across 3 runs
- **HARKing flag consistency:** Should be identical if confidence is high

**Analysis:**
```bash
# Run classification 3x (manual invocations)
# Compare outputs:
for run in run1 run2 run3; do
  jq '.research_approach_classification.revealed_approach' classification-$run.json
done

# Count unique values - should be ≤ 2
jq '.research_approach_classification.revealed_approach' classification-*.json | sort | uniq -c

# Check variance
# If >2 different revealed approaches across 3 runs → Classification insufficiently constrained
```

**Interpretation:**
- **If all 3 runs identical:** Excellent reliability → Proceed
- **If 2/3 agree, 1 differs:** Acceptable reliability if difference is "mixed" vs "inductive/deductive" → Monitor
- **If all 3 runs differ:** Poor reliability → Revise classification prompt (insufficient anchoring) → Re-test

**Validation commands:**
```bash
# Check required fields present
jq '.research_approach_classification | keys' classification.json

# Verify approach values
jq '.research_approach_classification.expressed_approach' classification.json
jq '.research_approach_classification.revealed_approach' classification.json

# Check HARKing detection
jq '.research_approach_classification.harking_flag' classification.json

# Validate justification length (should be substantial - >200 chars)
jq '.research_approach_classification.classification_justification | length' classification.json
```

**Manual review:**
- Do classifications align with paper reading?
- Are justifications well-grounded in extraction?
- Is confidence appropriately calibrated?

**Decision gate:**
- If test-retest reliability acceptable (≤2 changes across 9 runs) → Proceed to Checkpoint 2
- If poor reliability → Revise prompt, re-test

---

### Checkpoint 2: First Cluster Working (Foundational Clarity)

**After implementing assess-foundational-clarity.md prompt:**

**Test paper:** sobotkova-et-al-2024

**Validation criteria:**
- [ ] clusters/cluster-1-foundational-clarity.md generated
- [ ] Both signals assessed (Comprehensibility + Transparency)
- [ ] Scores in 0-100 range with confidence
- [ ] Summary present for each signal (2-3 sentences)
- [ ] Key strengths/weaknesses (3-5 items each) with specific evidence
- [ ] Supporting evidence cites extraction elements
- [ ] Scoring justifications reference approach-specific anchors
- [ ] Approach-specific context applied
- [ ] Cross-signal coherence check present

**NEW: Score Variance Check (Test-Retest Reliability) (v2.0)**

**Purpose:** Measure signal scoring consistency

**Process:**
1. Run foundational clarity assessment 3x on sobotkova-et-al-2024 (identical inputs)
2. Extract Comprehensibility scores and Transparency scores from each run
3. Calculate mean and standard deviation for each signal

**Measurements:**
- **Comprehensibility:** Mean score ± SD
- **Transparency:** Mean score ± SD
- **Threshold:** SD < 10 points = acceptable reliability

**Analysis:**
```bash
# Extract scores from 3 runs
grep "Signal 1: Comprehensibility" cluster-1-run*.md -A 1 | grep "Score:"
grep "Signal 2: Transparency" cluster-1-run*.md -A 1 | grep "Score:"

# Calculate SD manually or with script
# Example: Run 1: 75, Run 2: 78, Run 3: 73 → Mean = 75.3, SD = 2.5 ✓ (< 10)
# Example: Run 1: 75, Run 2: 62, Run 3: 81 → Mean = 72.7, SD = 9.6 ⚠ (close to threshold)
# Example: Run 1: 75, Run 2: 55, Run 3: 85 → Mean = 71.7, SD = 15.3 ✗ (> 10, too variable)
```

**Interpretation:**
- **SD < 5:** Excellent reliability → High confidence in scoring
- **SD 5-10:** Acceptable reliability → Moderate confidence, monitor
- **SD > 10:** Poor reliability → Investigate causes:
  - Rubric insufficiently anchored (revise approach-specific anchors)
  - Evidence ambiguous (document in Track A)
  - LLM temperature too high (check settings)

**NEW: Metric-Signal Correlation Check (v2.0)**

**Purpose:** Validate that metrics and signals measure related constructs

**Process:**
1. Extract TCI (Transparency & Completeness Index) from metrics.json
2. Extract Transparency signal score from cluster-1
3. Compare relationship

**Expected correlation:** TCI and Transparency signal should correlate positively (r > 0.6 if tested across multiple papers)

**For single-paper check:**
- If TCI = 68 and Transparency = 70 → Alignment ✓
- If TCI = 68 and Transparency = 30 → Divergence → Investigate
- If TCI = 30 and Transparency = 70 → Divergence → Investigate

**Analysis:**
```bash
# Extract both values
TCI=$(jq '.TCI' metrics/metrics.json)
TRANS=$(grep "Signal 2: Transparency" cluster-1.md -A 1 | grep "Score:" | awk '{print $2}' | cut -d'/' -f1)

echo "TCI: $TCI, Transparency: $TRANS"

# Manual assessment: Are they within ~20 points of each other?
# If divergence > 20 points → Check cluster-1.md for explanation in scoring justification
```

**Interpretation:**
- **Alignment (within 20 points):** Metric and signal measure similar constructs ✓
- **Divergence (>20 points, explained in justification):** Acceptable if LLM explains why (e.g., "TCI is low because RDMAP incomplete, but Transparency scored higher because excellent data/code sharing compensates") ✓
- **Divergence (>20 points, unexplained):** Problem → Either metric or signal assessment flawed → Investigate

**Validation commands:**
```bash
# Check file exists and has content
test -f assessment/clusters/cluster-1-foundational-clarity.md && echo "File exists"
wc -w assessment/clusters/cluster-1-foundational-clarity.md  # Should be ~800-1200 words

# Extract scores (manual inspection)
grep "**Score:**" assessment/clusters/cluster-1-foundational-clarity.md
```

**Manual review:**
- Do scores feel right given paper characteristics?
- Are strengths/weaknesses specific (not generic)?
- Does assessment reference extraction elements correctly?
- Is approach context appropriate (inductive emphasis)?
- Do Comprehensibility and Transparency assessments cohere?

**Decision gate:**
- If test-retest SD < 10 AND metric-signal alignment acceptable → Proceed to Checkpoint 3
- If SD > 10 OR unexplained divergence → Revise rubric, re-test

---

### Checkpoint 3: End-to-End Proof of Concept

**After implementing classifier + foundational clarity cluster + Track A gating:**

**Test paper:** sobotkova-et-al-2024

**Full workflow test:**
1. Run classifier → classification.json
2. Run Track A quality gate → track-a-quality.md (with quality_state)
3. Run foundational clarity assessment → cluster-1.md
4. Generate mini-report (classification + Track A + cluster 1 only)

**Validation criteria:**
- [ ] Workflow completes without errors
- [ ] classification.json valid and sensible
- [ ] track-a-quality.md includes quality_state (should be "high" for sobotkova-et-al-2024)
- [ ] cluster-1-foundational-clarity.md complete and grounded
- [ ] Quality gating logic works (quality_state correctly determines assessment pathway)
- [ ] Data flows correctly between prompts
- [ ] Mini-report coherent and actionable

**NEW: Quality Gating Logic Test (v2.0)**

**Purpose:** Verify that Track A correctly gates assessment

**Process:**
1. For sobotkova-et-al-2024 (expected high quality):
   - Verify quality_state = "high"
   - Verify cluster-1 uses approach-specific anchors
   - Verify cluster-1 has no caveat headers
   - Verify mini-report is standard format (not caveated)

2. **Simulated moderate quality test:**
   - Manually edit track-a-quality.md to set quality_state = "moderate"
   - Re-run cluster-1 assessment
   - Verify cluster-1 includes caveat header
   - Verify cluster-1 uses 20-point score bands (e.g., "60-80" not "72")
   - Verify mini-report includes "Assessment Limitations" section

3. **Simulated low quality test:**
   - Manually set quality_state = "low"
   - Verify cluster-1 assessment is SKIPPED
   - Verify mini-report is track-a-only.md + assessment-not-viable.md

**Analysis:**
```bash
# Check quality state
grep "quality_state:" track-a-quality.md

# For moderate quality simulation:
# Check for caveat header in cluster-1
grep "ASSESSMENT QUALITY CAVEAT" cluster-1.md

# Check for 20-point bands vs precise scores
grep "Score:" cluster-1.md  # Should show "60-80" not "72"

# For low quality simulation:
# Cluster-1 should not exist
test ! -f cluster-1.md && echo "Correctly skipped"
# assessment-not-viable.md should exist
test -f assessment-not-viable.md && echo "Correctly aborted"
```

**Success criteria:**
- All files generated correctly based on quality state
- Quality gating logic enforces correct behaviours (caveats, score bands, abortion)
- Manual review confirms quality and coherence
- Ready to expand to remaining 2 clusters (evidential strength, reproducibility & scope)

---

### Checkpoint 4: All Three Clusters Working

**After implementing all 3 signal cluster prompts:**

**Test papers:** sobotkova-et-al-2024, ballsun-stanton-et-al-2018, penske-et-al-2023

**Validation criteria:**
- [ ] All 3 cluster files generated for each paper
- [ ] All 7 signals assessed (cluster-1: 2 signals, cluster-2: 3 signals, cluster-3: 2 signals)
- [ ] Scores discriminate appropriately (not all 70-80)
- [ ] Approach-specific emphasis visible in assessments
- [ ] Parallel execution successful (no dependency issues between clusters)
- [ ] Cross-signal consistency (no contradictions)

**NEW: Approach-Specific Scoring Validation (v2.0)**

**Purpose:** Verify that approach-specific anchors are actually applied

**Test design:**
- sobotkova-et-al-2024: Inductive
- penske-et-al-2023: Deductive
- Compare signal profiles

**Hypothesis:**
- Transparency should be PRIMARY for inductive (sobotkova) → expect higher emphasis, detailed justification
- Validity/Robustness should be PRIMARY for deductive (penske) → expect higher emphasis
- Reproducibility interpretation should differ:
  - Inductive: Analytic reproducibility (workflow documentation)
  - Deductive: Pre-registration + data/code sharing

**Analysis:**
```bash
# Extract Reproducibility scores and justifications from both papers
grep -A 20 "Signal 6: Reproducibility" sobotkova-2024/cluster-3.md | grep "Scoring Justification"
grep -A 20 "Signal 6: Reproducibility" penske-2023/cluster-3.md | grep "Scoring Justification"

# Compare:
# sobotkova justification should reference "workflow documentation" (inductive anchor)
# penske justification should reference "pre-registration" or "hypothesis testing" (deductive anchor)
```

**Interpretation:**
- **If justifications reference different anchor criteria:** Approach-specific anchors working ✓
- **If justifications identical/generic:** Approach anchors not applied → Revise prompts

**NEW: Test-Retest Reliability for All Signals (v2.0)**

**Process:**
1. Run all 3 cluster assessments 3x on sobotkova-et-al-2024
2. Extract all 7 signal scores from each run
3. Calculate SD for each signal

**Threshold:** SD < 10 for each signal

**Analysis:**
```bash
# Extract all scores from 3 runs
for signal in comprehensibility transparency plausibility validity robustness reproducibility generalisability; do
  echo "Signal: $signal"
  grep -i "$signal" cluster-*-run*.md | grep "Score:" | awk '{print $2}' | cut -d'/' -f1
  # Calculate SD manually or with script
done
```

**Decision gate:**
- If all signals SD < 10 → Acceptable reliability → Proceed
- If any signal SD > 10 → Revise that signal's rubric → Re-test

**Validation commands:**
```bash
# Check all 3 clusters present for each paper
for paper in sobotkova-2024 ballsun-stanton-2018 penske-2023; do
  count=$(ls -1 $paper/assessment/clusters/*.md 2>/dev/null | wc -l)
  echo "$paper: $count clusters"
done  # All should show 3

# Extract all scores from one paper (check discrimination)
grep -h "**Score:**" sobotkova-2024/assessment/clusters/*.md

# Check score distribution (should vary - not all in same band)
grep -h "**Score:**" */assessment/clusters/*.md | awk '{print $2}' | cut -d'/' -f1 | sort -n
```

**Manual review:**
- Do signal scores make sense together?
- Are approach-specific emphases applied (inductive vs deductive)?
- Do clusters show internal coherence?
- Do assessments reference different extraction elements appropriately?

**Cross-Signal Coherence Analysis:**

**Purpose:** Detect contradictions between signals

**Process:**
1. For each paper, identify pairs of signals that should correlate:
   - Comprehensibility ↔ Transparency (communication quality)
   - Transparency ↔ Reproducibility (documentation quality)
   - Plausibility ↔ Validity (evidence quality)
   - Validity ↔ Robustness (evidence strength)

2. Check for unexplained divergences (>20 points difference)

**Example checks:**
- High Transparency (80) but Low Reproducibility (40) → Suspicious (methods documented but not reproducible? Needs explanation)
- Low Comprehensibility (40) but High Plausibility (80) → Suspicious (poorly communicated but plausible? Unlikely, needs explanation)

**Analysis:**
```bash
# Extract score pairs for manual comparison
echo "Comprehensibility vs Transparency:"
grep "comprehensibility" -A 1 cluster-1.md | grep "Score:"
grep "transparency" -A 1 cluster-1.md | grep "Score:"

echo "Transparency vs Reproducibility:"
grep "transparency" -A 1 cluster-1.md | grep "Score:"
grep "reproducibility" -A 1 cluster-3.md | grep "Score:"

# If divergence > 20 points, check cluster files for explanation in justifications or cross-signal coherence sections
```

**Decision gate:**
- If coherence checks pass AND test-retest reliable AND approach anchors applied → Proceed to Checkpoint 5
- If incoherence detected OR poor reliability → Revise prompts, consider consolidating clusters further

---

### Checkpoint 5: Complete Report Generated

**After implementing generate-credibility-report.md:**

**Test paper:** sobotkova-et-al-2024

**Validation criteria:**
- [ ] credibility-report-v1.md generated
- [ ] Report is 3-5 pages (~1500-2500 words)
- [ ] All sections present (metadata, disclaimer, scorecard, signal details, recommendations)
- [ ] Synthesis coherent and actionable
- [ ] Track A quality state reflected in report (standard vs caveated vs track-a-only)
- [ ] Experimental system disclaimer present
- [ ] Report references specific evidence (not generic)
- [ ] assessment.json (canonical) generated and valid

**NEW: Canonical assessment.json Validation (v2.0)**

**Purpose:** Verify machine-readable consolidation is complete and accurate

**Validation commands:**
```bash
# Check JSON is valid
jq '.' assessment/assessment.json > /dev/null && echo "Valid JSON"

# Check required top-level keys present
jq 'keys' assessment/assessment.json
# Should include: paper_id, assessment_date, system_version, classification, track_a, signals, metrics, report_metadata

# Check all 7 signals present in signals array
jq '.signals | length' assessment/assessment.json
# Should be 7

# Check signal names correct
jq '.signals[].signal_name' assessment/assessment.json
# Should list all 7: comprehensibility, transparency, plausibility, validity, robustness, reproducibility, generalisability

# Verify scores match cluster files
# Example: Extract Comprehensibility score from assessment.json
jq '.signals[] | select(.signal_name=="comprehensibility") | .score' assessment/assessment.json
# Compare to cluster-1.md (should match)
grep "Signal 1: Comprehensibility" clusters/cluster-1.md -A 1 | grep "Score:"

# Check quality state propagated
jq '.track_a.quality_state' assessment/assessment.json
# Should match track-a-quality.md
```

**Manual review:**
- Is report readable and well-structured?
- Does synthesis add value beyond individual cluster assessments (not just copying)?
- Are recommendations specific and implementable?
- Is overall credibility profile convincing?
- Does assessment.json accurately consolidate all assessment data?

**NEW: Quality State Conditional Formatting Check (v2.0)**

**Test:** Verify report format varies correctly based on quality state

**For high quality (sobotkova-et-al-2024):**
- [ ] File named `credibility-report-v1.md` (not -CAVEATED)
- [ ] No "Assessment Limitations" section in report
- [ ] Disclaimer says "Assessment quality: HIGH"
- [ ] assessment.json has `report_metadata.quality_caveats: false`

**For moderate quality (simulate):**
- [ ] File named `credibility-report-v1-CAVEATED.md`
- [ ] "Assessment Limitations" section present prominently
- [ ] Disclaimer says "Assessment quality: MODERATE"
- [ ] Scores shown as bands (e.g., "60-80") if appropriate
- [ ] assessment.json has `report_metadata.quality_caveats: true`

**Validation commands:**
```bash
# Check report length
wc -w assessment/credibility-report-v1.md  # Target: 1500-2500 words

# Check section headers present
grep "^##" assessment/credibility-report-v1.md

# Check experimental disclaimer present
grep "EXPERIMENTAL SYSTEM" assessment/credibility-report-v1.md

# Check quality state mentioned
grep -i "assessment quality:" assessment/credibility-report-v1.md
```

**Decision gate:**
- If report complete AND assessment.json valid AND quality gating formats correct → Proceed to Checkpoint 6
- If issues → Revise report generation prompt

---

### Checkpoint 6: Corpus Testing (Expand to All 10 Papers)

**After validating on 3 papers:**

**Test all papers in corpus**

**Validation criteria:**
- [ ] All 10 papers classified successfully
- [ ] All 10 papers have Track A quality assessments
- [ ] 10 papers have complete credibility assessments (or track-a-only if quality = low)
- [ ] All 3 cluster files present for each complete assessment
- [ ] All 10 papers have credibility reports (standard, caveated, or track-a-only)
- [ ] All 10 papers have assessment.json
- [ ] Cross-paper patterns emerge (approach types, signal profiles, quality states)
- [ ] Rubrics applied consistently
- [ ] No systematic failures

**Validation commands:**
```bash
# Count successful classifications
find outputs -name "classification.json" | wc -l  # Should be 10

# Count Track A quality assessments
find outputs -name "track-a-quality.md" | wc -l  # Should be 10

# Count complete assessments (3 clusters each)
for paper in outputs/*/; do
  count=$(find "$paper/assessment/clusters" -name "*.md" 2>/dev/null | wc -l)
  echo "$(basename $paper): $count clusters"
done  # Should show 3 for each (or 0 if quality = low)

# Count credibility reports (any type)
find outputs -name "credibility-report*.md" -o -name "track-a-only.md" | wc -l  # Should be 10

# Count assessment.json files
find outputs -name "assessment.json" | wc -l  # Should be 10

# Extract quality states across corpus
for paper in outputs/*/; do
  echo -n "$(basename $paper): "
  grep "quality_state:" "$paper/assessment/track-a-quality.md" 2>/dev/null || echo "missing"
done

# Distribution of quality states
grep -h "quality_state:" outputs/*/assessment/track-a-quality.md | sort | uniq -c
# Example output: "8 high, 2 moderate, 0 low" would be good
```

**NEW: Corpus-Level Analysis via assessment.json (v2.0)**

**Purpose:** Use canonical JSON files for cross-paper statistics

**Analysis commands:**
```bash
# Create consolidated corpus file (all assessment.json merged)
jq -s '.' outputs/*/assessment/assessment.json > corpus-assessments.json

# Calculate mean scores per signal across corpus
for signal in comprehensibility transparency plausibility validity robustness reproducibility generalisability; do
  echo -n "$signal: "
  jq -r --arg sig "$signal" '.[] | .signals[] | select(.signal_name==$sig) | .score' corpus-assessments.json | \
    awk '{sum+=$1; n++} END {print sum/n}'
done

# Distribution of research approaches
jq -r '.[].classification.revealed_approach' corpus-assessments.json | sort | uniq -c

# Approach-specific signal profiles
# Example: Compare mean Reproducibility scores for inductive vs deductive papers
echo "Inductive Reproducibility mean:"
jq -r '.[] | select(.classification.revealed_approach=="inductive") | .signals[] | select(.signal_name=="reproducibility") | .score' corpus-assessments.json | awk '{sum+=$1; n++} END {print sum/n}'

echo "Deductive Reproducibility mean:"
jq -r '.[] | select(.classification.revealed_approach=="deductive") | .signals[] | select(.signal_name=="reproducibility") | .score' corpus-assessments.json | awk '{sum+=$1; n++} END {print sum/n}'

# Expected: Deductive should score higher (stricter standards as per anchors)
# If no difference → approach anchors not being applied properly
```

**Manual review across corpus:**
- Do classifications make sense across corpus?
- Are scores discriminating (high vs medium vs low credibility papers identified)?
- Do approach-specific patterns emerge (e.g., inductive papers prioritize transparency)?
- Are there temporal trends (older vs newer papers)?
- Are there disciplinary patterns (archaeology vs palaeoecology vs digital humanities)?
- Are any papers outliers requiring special handling?
- Is quality gating functioning appropriately (identifying genuinely low-quality extractions)?

**NEW: Cross-Paper Coherence Check (v2.0)**

**Purpose:** Verify rubrics applied consistently across diverse papers

**Process:**
1. Identify 2-3 pairs of papers with similar characteristics (e.g., both inductive, both from same journal)
2. Compare signal profiles - should be similar if characteristics similar
3. Identify pairs with very different characteristics - signal profiles should differ

**Example analysis:**
```bash
# Extract signal scores for two similar papers
echo "Paper A (inductive archaeology):"
jq '.signals[] | "\(.signal_name): \(.score)"' paper-a/assessment/assessment.json

echo "Paper B (inductive archaeology, same era):"
jq '.signals[] | "\(.signal_name): \(.score)"' paper-b/assessment/assessment.json

# If very similar papers have wildly different profiles (e.g., A: transparency=80, B: transparency=40)
# → Investigate: Is difference justified by actual quality difference?
# → Or: Inconsistent rubric application?
```

**Documentation of patterns:**

Create `planning/cross-paper-assessment-patterns.md`:
```markdown
# Cross-Paper Assessment Patterns
## Corpus: 10 HASS papers

### Approach Distribution
- Inductive: 6 papers
- Deductive: 3 papers
- Abductive: 1 paper

### Quality State Distribution
- High: 8 papers
- Moderate: 2 papers (reasons: [list])
- Low: 0 papers

### Signal Score Profiles by Approach

**Inductive papers (n=6):**
- Mean Transparency: 72 (PRIMARY signal, as expected)
- Mean Comprehensibility: 68 (PRIMARY signal)
- Mean Reproducibility: 58 (lower, as expected - workflow docs vary)

**Deductive papers (n=3):**
- Mean Validity: 75 (PRIMARY signal, as expected)
- Mean Robustness: 70 (PRIMARY signal)
- Mean Reproducibility: 68 (higher than inductive, as expected - better code sharing)

**Pattern confirmation:** Approach-specific anchors ARE being applied (profiles differ as expected) ✓

### Temporal Patterns
- Papers 2018-2024: Transparency scores increasing over time (r=0.6)
- Likely reflects improving data sharing norms

### Disciplinary Patterns
- Archaeology papers: Lower Reproducibility (field constraints)
- Digital humanities papers: Higher Transparency (computational methods)

### Outliers
- [Paper X]: Unusually low Plausibility (42) despite high Validity (78)
  - Investigation: Plausibility low because theoretical framework weak, but evidence still strong
  - Coherent, not error

### Rubric Refinements Identified
1. Reproducibility anchors for inductive research need refinement (scores clustering 55-65, not discriminating)
2. Robustness assessment may be conflating sensitivity analysis with triangulation (clarify in prompt)
3. [...]
```

**Decision gate:**
- If all 10 papers assessed AND patterns coherent AND no systematic failures → Phase 1 COMPLETE ✅
- If inconsistencies detected → Refine rubrics, re-assess affected papers

---

### NEW Checkpoint 1.5: Early RepliCATS Pilot (CONDITIONAL)

*Inserted between Checkpoint 1 and Checkpoint 2*

**Condition:** Only if repliCATS corpus access confirmed (Shawn confirmed: YES)

**Timing:** After classifier working + before building all cluster rubrics

**Purpose:** Validate that our approach produces structurally similar assessments to repliCATS expert panels BEFORE investing effort in all 7 signals

**Test papers:** 1-2 papers from repliCATS corpus with expert assessment scores available

**Process:**
1. Select 1-2 repliCATS papers (ideally from HASS-adjacent fields if available)
2. Run classification on repliCATS paper(s)
3. Build transparency assessment (cluster-1, just transparency signal initially)
4. Compare our Transparency score to repliCATS expert panel Transparency rating
5. **NOT calibrating** - just checking for structural sanity

**Validation criteria:**
- [ ] Classification runs successfully on repliCATS paper
- [ ] Transparency assessment generates sensible score
- [ ] Our score does not invert repliCATS ranking (if assessing 2 papers)
- [ ] Our score is in same ballpark as expert panel (within ±30 points acceptable)

**Analysis:**
```bash
# Extract our Transparency score
OUR_SCORE=$(grep "Signal 2: Transparency" replicats-paper-1/cluster-1.md -A 1 | grep "Score:" | awk '{print $2}' | cut -d'/' -f1)

# Expert panel score (from repliCATS data)
EXPERT_SCORE=65  # Example from repliCATS dataset

# Calculate divergence
echo "Our score: $OUR_SCORE, Expert score: $EXPERT_SCORE, Divergence: $(($OUR_SCORE - $EXPERT_SCORE))"

# Acceptable: Divergence ≤ 30 points
# If divergence > 30 → Investigate: Different interpretation? Different evidence? Systematic bias?
```

**Interpretation:**
- **Divergence ≤ 20 points:** Excellent alignment ✓ → Proceed with confidence
- **Divergence 20-30 points:** Acceptable alignment ✓ → Proceed, monitor
- **Divergence > 30 points AND same direction (both high or both low):** Moderate concern → Discuss with Shawn, consider rubric adjustment, proceed cautiously
- **Divergence > 30 points AND opposite direction (we say high, experts say low):** Serious misalignment ✗ → Do not proceed to all 7 signals → Investigate root cause

**Root cause investigation if misalignment:**
1. Read repliCATS expert justifications (if available) - what did they emphasize?
2. Read our justification - what did we emphasize?
3. Compare:
   - Are we using different evidence? (extraction may have missed key elements)
   - Are we using different standards? (anchors may be miscalibrated)
   - Are we interpreting signal differently? (definition may need refinement)

**Decision gate:**
- If alignment acceptable (divergence ≤ 30 AND same direction) → Proceed to build all cluster rubrics (Checkpoint 2+)
- If serious misalignment (divergence > 30 OR opposite direction) → STOP, discuss with Shawn:
  - Option A: Refine rubrics based on repliCATS feedback, re-test
  - Option B: Accept that HASS adaptation diverges from psychology corpus, proceed with documentation of differences
  - Option C: Abandon repliCATS validation, focus on internal consistency

**Estimated effort:** 1-2 hours (if corpus accessible as confirmed)

**Value:** Catches structural misalignments BEFORE building all 7 signal rubrics (saves 10-15 hours of wasted effort if fundamental approach flawed)

---

## Part 7: Implementation Sequence (Phase 1 Detailed - REVISED)

*[All steps from v1.0 retained with enhancements for quality gating, reliability testing, and clustering]*

### Step 1: Extend research-assessor Skill (2 hours)

*[Unchanged from v1.0]*

**Actions:**
1. Update SKILL.md description and add Passes 8-9
2. Create 7 new reference files in `references/credibility/`
3. Create 2 new schema files in `references/schema/`
4. Document skill changes

**Files to create:**
- `references/credibility/approach-taxonomy.md`
- `references/credibility/signal-definitions-hass.md` **(ENHANCED with approach-specific anchors)**
- `references/credibility/assessment-frameworks.md`
- `references/credibility/harking-detection-guide.md`
- `references/credibility/track-a-quality-criteria.md` **(ENHANCED with gating decision logic)**
- `references/schema/classification-schema.md`
- `references/schema/assessment-schema.md`

**Validation:**
- [ ] All files created
- [ ] SKILL.md updated with Passes 8-9
- [ ] Skill loads correctly (test invocation)

---

### Step 2: Create Classification Prompt (1 hour)

*[Unchanged from v1.0 conceptually, enhanced with context-sensitive "none_stated" handling]*

**Actions:**
1. Create `assessment-system/prompts/classify-research-approach.md`
2. Include clear instructions for:
   - Detecting expressed approach
   - Inferring revealed approach
   - Comparing expressed vs revealed
   - **Handling "none_stated" with context sensitivity (NEW)**
   - Mixed-method characterisation
3. Include examples from skill references
4. Specify output format (classification.json)

**Prompt enhancements (v2.0):**

Add context-sensitive "none_stated" handling:
```markdown
### Handling "No Expressed Methodology"

When no explicit methodological framework is stated:

**Do not automatically penalize.** Absence of methodology section may indicate:
1. Methodological naivete or weak research design (common for contemporary papers)
2. Disciplinary genre conventions (some fields/eras don't use methodology sections)
3. Methodological commitments expressed through narrative rather than explicit section

**Classification:**
- expressed_approach: "none_stated"
- revealed_approach: [Infer from claims and methods]
- expressed_vs_revealed: "partial" (cannot compare what's not stated)

**Justification must include:**
- Contextual interpretation (publication year, discipline, journal norms)
- Whether absence appears to be oversight (problematic) or convention (acceptable)
- Impact on credibility assessment (will trigger Track A monitoring)
```

**Validation:**
- [ ] Prompt complete and clear
- [ ] "none_stated" handling context-sensitive
- [ ] References to skill files correct
- [ ] Output format specified

---

### Step 3: Test Classifier on 3 Papers with Test-Retest (1.5 hours)

*[Enhanced from v1.0 with reliability testing]*

**Actions:**
1. Run classification 3x on sobotkova-et-al-2024
2. Run classification 3x on ballsun-stanton-et-al-2018
3. Run classification 3x on penske-et-al-2023
4. Validate outputs (Checkpoint 1 - including test-retest reliability)
5. Refine prompt based on results

**NEW: Test-retest reliability procedure:**
- Run each classification 3 times (9 total runs)
- Measure consistency (see Checkpoint 1)
- If SD acceptable → Proceed
- If SD high → Revise prompt, re-test

**Expected time:**
- 3 papers × 3 runs × 5 min = 45 min (classification runs)
- 15 min (test-retest analysis)
- 30 min (refinement if needed)

**Expected outcomes:**
- sobotkova-et-al-2024: Primarily inductive, matched, high confidence
- ballsun-stanton-et-al-2018: Mixed methodological (software), partial match, medium confidence
- penske-et-al-2023: Deductive, matched, high confidence

---

### NEW Step 3.5: Early RepliCATS Pilot (1-2 hours) - CONDITIONAL

**Condition:** If repliCATS corpus accessible (CONFIRMED)

**Actions:**
1. Identify 1-2 repliCATS papers with expert Transparency scores
2. Run classification on repliCATS paper(s)
3. Build foundational clarity assessment (next step, but only transparency signal initially)
4. Compare our Transparency score to expert panel
5. Validate alignment (see Checkpoint 1.5)

**Decision gate:**
- If aligned → Proceed to build all 3 clusters
- If misaligned → Investigate, refine, discuss with Shawn

**Effort:** 1-2 hours

---

### Step 4: Create Track A Quality Gating Prompt (1 hour) - NEW

**Actions:**
1. Create `assessment-system/prompts/track-a-quality-gate.md`
2. Include:
   - Quality dimension evaluation (extraction, metrics, classification)
   - Gating decision logic (high/moderate/low state assignment)
   - Output format (track-a-quality.md with explicit quality_state)

**Prompt structure:**
```markdown
# Track A Quality Gating Prompt

## Task
Evaluate extraction and assessment quality, assign quality state, determine assessment pathway.

## Quality Dimensions to Evaluate

### 1. Extraction Confidence
[Assessment questions for claims, evidence, RDMAP, infrastructure]

### 2. Metric-Signal Alignment
[How to check if metrics and qualitative assessment cohere]

### 3. Classification Quality
[Classification confidence, ambiguity handling]

## Gating Decision Logic

Apply the following rules to determine quality_state:

**HIGH QUALITY** (triggers: ...)
**MODERATE QUALITY** (triggers: ...)
**LOW QUALITY** (triggers: ...)

[See references/credibility/track-a-quality-criteria.md for detailed rules]

## Output Format

track-a-quality.md with:
- Explicit quality_state declaration (first line after header)
- Justification for state assignment
- Detailed quality assessment
- Improvement opportunities

## References
- references/credibility/track-a-quality-criteria.md (gating framework)
```

**Validation:**
- [ ] Prompt complete
- [ ] Decision logic clear
- [ ] quality_state output specified

---

### Step 5: Create First Cluster Rubric (Foundational Clarity) (1.5 hours)

*[Enhanced from v1.0 "transparency rubric" to "cluster rubric"]*

**Actions:**
1. Create `assessment-system/prompts/assess-foundational-clarity.md`
2. Include:
   - Cluster overview (why Comprehensibility + Transparency together)
   - Signal 1 (Comprehensibility): definition, assessment questions, approach-specific anchors, scoring guidance
   - Signal 2 (Transparency): definition, assessment questions, approach-specific anchors, scoring guidance
   - Cross-signal coherence check
   - Metric integration (TCI for Transparency)
   - Output format (cluster-1-foundational-clarity.md)

**Prompt structure:**
```markdown
# Foundational Clarity Cluster Assessment Prompt
## Comprehensibility + Transparency

## Cluster Rationale
These signals are assessed together because poor comprehensibility undermines ability to evaluate
transparency. If we cannot understand claims, we cannot assess whether methods are transparent.

## Quality State Handling

**Read quality_state from track-a-quality.md:**

- If "high": Apply approach-specific anchors, precise scores, standard format
- If "moderate": Add caveat header, use 20-point bands, apply generic rubrics if classification ambiguous
- If "low": This prompt should not execute (workflow aborted)

## Signal 1: Comprehensibility

### Signal Definition
[From signal-definitions-hass.md]

### Assessment Questions
1. Are research claims clearly formulated?
2. Is argument structure logical and traceable?
3. [5-7 questions total]

### Approach-Specific Scoring Anchors (0-100)

#### For Deductive Research
**80-100:** [Concrete description]
**60-79:** [Concrete description]
[Full anchor set from signal-definitions-hass.md]

#### For Inductive Research
[Full anchor set]

#### For Abductive Research
[Full anchor set]

### Scoring Process
1. Identify research approach from classification.json
2. Select appropriate anchor set
3. Assess against anchor descriptions
4. Assign score within band
5. Justify by referencing anchors

### Relevant Metrics
[If applicable for Comprehensibility]

---

## Signal 2: Transparency

[Same structure: definition, questions, approach anchors, scoring process]

### Relevant Metrics

**TCI (Transparency & Completeness Index):** [Expected correlation, how to interpret divergence]

---

## Cross-Signal Coherence Check

**Do Comprehensibility and Transparency scores cohere?**

Example checks:
- High Comprehensibility + Low Transparency: Unusual (clear writing but poor documentation?)
- Low Comprehensibility + High Transparency: Contradictory (cannot be transparent if incomprehensible)

If divergence >20 points, explain in cluster file.

---

## Output Format

clusters/cluster-1-foundational-clarity.md (see references/schema/assessment-schema.md)

Include:
- Cluster overview
- Signal 1 assessment (summary, strengths, weaknesses, justification, approach context)
- Signal 2 assessment (same structure)
- Cross-signal coherence analysis
- Relevant metrics section

**If quality_state = "moderate":**
- Add caveat header at top
- Use 20-point score bands (e.g., "60-80")
- Note if generic rubrics used

## References
- references/credibility/signal-definitions-hass.md (with anchors)
- references/credibility/assessment-frameworks.md
- references/schema/assessment-schema.md
```

**Validation:**
- [ ] Prompt complete (~500 lines)
- [ ] Both signals included
- [ ] Approach anchors integrated
- [ ] Quality state handling specified
- [ ] Cross-signal coherence included

---

### Step 6: Test Track A + Foundational Clarity with Reliability Checks (2 hours)

*[Enhanced from v1.0 with quality gating and reliability testing]*

**Actions:**
1. On sobotkova-et-al-2024:
   - Run Track A quality gate → should output quality_state = "high"
   - Run foundational clarity 3x → test-retest reliability
   - Check metric-signal correlation (TCI vs Transparency)
2. Validate workflow (Checkpoint 2 - enhanced)
3. Refine prompts based on output quality

**Reliability testing:**
- 3x foundational clarity runs = 3 runs × 10 min = 30 min
- Test-retest analysis = 15 min
- Metric correlation check = 10 min
- Refinement if needed = 30 min

**NEW: Quality gating simulation test:**
- Manually edit track-a-quality.md to set quality_state = "moderate"
- Re-run foundational clarity
- Verify caveat headers appear, 20-point bands used
- Revert to "high" for continued testing

**Decision gate:**
- If test-retest SD < 10 AND TCI alignment acceptable AND quality gating works → Proceed
- If issues → Revise, re-test

---

### Step 7: Create Remaining Cluster Rubrics (2-3 hours)

*[NEW in v2.0 - consolidates 6 signal prompts from v1.0 into 2 cluster prompts]*

**Actions:**
1. Create `assess-evidential-strength.md` (~550 lines)
   - Plausibility + Validity + Robustness
   - Rationale: Evidence-claim reasoning chain
   - Approach-specific anchors for all 3 signals
   - Cross-signal coherence (especially Validity → Robustness)
   - Relevant metrics: ESD (for Validity), RTI (for Robustness)

2. Create `assess-reproducibility-scope.md` (~400 lines)
   - Reproducibility + Generalisability
   - Rationale: Boundaries and reproduction
   - Approach-specific anchors (especially Reproducibility: analytic reproducibility for inductive vs pre-registration for deductive)
   - Cross-signal coherence
   - Relevant metrics: RIS, FCS (for Reproducibility), SCS (for Generalisability)

**Effort estimate:**
- Evidential strength prompt: 1.5 hours (3 signals, tight interactions)
- Reproducibility & scope prompt: 1 hour (2 signals, clear structure from foundational clarity template)

**Validation:**
- [ ] Both prompts complete
- [ ] All signals covered (7 total: 2 in cluster-1, 3 in cluster-2, 2 in cluster-3)
- [ ] Approach anchors for all signals
- [ ] Quality state handling in both
- [ ] Cross-signal coherence for both

---

### Step 8: Test All Three Clusters with Reliability (2-3 hours)

*[Enhanced from v1.0 with comprehensive reliability and coherence testing]*

**Actions:**
1. On sobotkova-et-al-2024:
   - Run all 3 cluster assessments 3x (test-retest for all 7 signals)
   - Check cross-cluster coherence
   - Check metric-signal correlations for all relevant metrics
2. On ballsun-stanton-et-al-2018 and penske-et-al-2023:
   - Run all 3 cluster assessments 1x each
   - Compare approach-specific profiles (inductive vs deductive)
3. Validate (Checkpoint 4 - enhanced)
4. Refine based on results

**Test-retest for 7 signals:**
- 3 runs × 3 clusters × 15 min = 135 min (2.25 hours)
- Analysis: 30 min
- Refinement if needed: 45 min

**Decision gate:**
- If all signals SD < 10 AND cross-signal coherence AND approach profiles differ appropriately → Proceed
- If issues → Revise cluster prompts

---

### Step 9: Create Report Generation Prompt (1 hour)

*[Enhanced from v1.0 with quality-conditional formatting and assessment.json generation]*

**Actions:**
1. Create `generate-credibility-report.md`
2. Include:
   - Report structure (all sections)
   - Synthesis instructions (not just copying clusters)
   - Quality state conditional formatting:
     - High → standard report
     - Moderate → caveated report with limitations section
     - Low → track-a-only + assessment-not-viable
   - Experimental disclaimer
   - Canonical assessment.json generation
3. Word count constraints (1500-2500 words)

**Prompt enhancements (v2.0):**
```markdown
# Credibility Report Generation Prompt

## Task
Synthesise credibility assessment from all inputs into 3-5 page report.

## Inputs Required
- classification.json
- track-a-quality.md (READ quality_state FIRST)
- clusters/cluster-1-foundational-clarity.md (if exists)
- clusters/cluster-2-evidential-strength.md (if exists)
- clusters/cluster-3-reproducibility-scope.md (if exists)
- metrics.json

## Quality State Conditional Formatting

**Read quality_state from track-a-quality.md BEFORE generating report.**

### If quality_state = "high":
- File name: credibility-report-v1.md
- Format: Standard 3-5 pages
- Disclaimer: "Assessment quality: HIGH"
- No limitations section

### If quality_state = "moderate":
- File name: credibility-report-v1-CAVEATED.md
- Format: 3-5 pages with prominent "Assessment Limitations" section
- Disclaimer: "Assessment quality: MODERATE - [specific limitation]"
- Scores shown as bands where appropriate

### If quality_state = "low":
- File name: track-a-only.md
- Content: Track A summary only, no signal synthesis
- Generate additional file: assessment-not-viable.md (explanation)
- Canonical assessment.json still generated (with quality_state = "low")

## Report Structure

[All sections from file structure specification]

## Synthesis Requirements

**Do not copy-paste cluster files.** Synthesise:
- Extract key themes across signals
- Identify overall credibility signature
- Distill recommendations (not list all from clusters)
- Add value through integration

## Canonical assessment.json Generation

**Always generate** assessment.json consolidating:
- classification
- track_a (including quality_state)
- signals (array of 7 signal objects - if assessed)
- metrics
- report_metadata

[See file structure specification for schema]

## Word Count Targets
- Executive summary: 150-200 words
- Each signal (detailed section): 150-200 words
- Overall credibility profile: 200-300 words
- **Total report: 1500-2500 words**

## References
- All cluster files
- classification.json
- track-a-quality.md
```

**Validation:**
- [ ] Prompt complete
- [ ] Quality-conditional formatting specified
- [ ] assessment.json generation included
- [ ] Synthesis requirements clear (not copying)

---

### Step 10: End-to-End Validation with Quality Gating (1-2 hours)

*[Enhanced from v1.0 "proof of concept" to full validation with quality gating tests]*

**Actions:**
1. On sobotkova-et-al-2024 (high quality expected):
   - Run full workflow: classify → Track A → 3 clusters → report
   - Validate Checkpoint 5 (enhanced)
   - Check assessment.json
2. Quality gating simulations:
   - Simulate moderate quality → verify caveated report
   - Simulate low quality → verify abortion + track-a-only
3. Validate Checkpoint 3 (enhanced)

**Simulation procedure:**
```bash
# Test 1: High quality (natural)
# [Run full workflow]
# Verify: credibility-report-v1.md, assessment.json complete

# Test 2: Moderate quality (simulated)
# Manually edit track-a-quality.md: quality_state = "moderate"
# Re-run clusters + report
# Verify: credibility-report-v1-CAVEATED.md, caveat headers in clusters

# Test 3: Low quality (simulated)
# Manually edit track-a-quality.md: quality_state = "low"
# Re-run workflow (should skip clusters)
# Verify: track-a-only.md, assessment-not-viable.md, no cluster files
```

**Decision gate:**
- If all quality states produce correct outputs AND assessment.json valid → **Phase 1 COMPLETE** ✅
- If issues → Revise prompts

---

## Part 8: Next Steps After Phase 1 (UPDATED)

### Phase 2: Corpus Expansion with Approach Diversity (2-3 hours)

*[Updated from v1.0 to emphasize approach diversity testing]*

**Actions:**
1. Run full workflow on remaining 7 papers
2. Focus on approach diversity:
   - Ensure inductive, deductive, and abductive papers all represented
   - Verify approach-specific anchors produce different profiles
3. Monitor for quality state distribution:
   - Expect mostly "high", some "moderate" acceptable, "low" triggers re-extraction
4. Validate Checkpoint 6 (corpus testing - enhanced)
5. Document patterns in `planning/cross-paper-assessment-patterns.md`

**Key validations:**
- Approach-specific scoring working (deductive ≠ inductive profiles)
- Quality gating identifying genuine extraction issues
- Rubrics applied consistently
- No systematic failures

---

### Phase 3: RepliCATS Validation (Full Corpus) (3-4 hours)

*[NEW in v2.0 - leverages early pilot from Phase 1.5]*

**Prerequisite:** Early pilot (Phase 1.5) showed acceptable alignment

**Actions:**
1. Identify 5-10 repliCATS papers with full expert Seven Signals scores
2. Run full credibility assessment on repliCATS corpus
3. Compare our scores to expert panel scores for all 7 signals
4. Calculate correlations (per signal)
5. Investigate systematic divergences

**Analysis:**
```bash
# For each signal, calculate correlation between our scores and expert scores
# Expected: r > 0.5 for most signals (moderate correlation)
# Psychology corpus may not align perfectly with HASS adaptations

# Focus on:
# - Are rankings preserved? (high papers scored high, low papers scored low)
# - Are approach adaptations appropriate? (inductive papers assessed differently)
```

**Outcomes:**
- If r > 0.6 for most signals → Excellent validation ✓
- If r 0.4-0.6 → Acceptable (HASS adaptation expected) ✓
- If r < 0.4 → Investigate divergence sources

**Decision:**
- Validation successful → Proceed to Phase 4
- Systematic issues identified → Refine rubrics, re-assess HASS corpus

---

### Phase 4: Manual Assessment & Gold Standard (4-6 hours)

*[Enhanced from v1.0 with Shawn's confirmed participation]*

**Confirmed:** Shawn will manually assess 3 papers

**Actions:**
1. Shawn selects 3 papers from corpus (diverse approaches)
2. Shawn manually assesses using same rubrics (approach-specific anchors)
3. Compare Shawn's scores to LLM scores for all 7 signals
4. Calculate mean absolute error per signal
5. Investigate divergences (where Shawn disagrees with LLM significantly)

**Expected divergence:**
- MAE < 15 points per signal = Excellent agreement
- MAE 15-25 points = Acceptable agreement
- MAE > 25 points = Investigate systematic bias

**Regression testing:**
- Save Shawn's assessments as gold standard
- Every time rubrics revised, re-run LLM assessment on these 3 papers
- Check for drift from gold standard

**Effort estimate:**
- Shawn: 2-3 hours per paper × 3 papers = 6-9 hours
- Analysis and comparison: 1-2 hours
- **Total: 7-11 hours** (mostly Shawn's time)

---

### Phase 5: Documentation and Integration (2-3 hours)

*[Unchanged from v1.0]*

**Actions:**
1. Update WORKFLOW.md to include credibility assessment (Passes 8-9)
2. Create user guide: `docs/assessment-guide/how-to-assess-credibility.md`
3. Create interpretation guide: `docs/assessment-guide/interpreting-credibility-reports.md`
4. Update `assessment-system/README.md`
5. Document validation results and rubric refinements

---

## Summary: Implementation Readiness (v2.0)

### What We Have ✅

✅ **Design decisions finalized:** 17/17 questions answered + all synthesis decisions
✅ **Prompt architecture:** 6 prompts with conceptual coherence and size constraints
✅ **Quality gating system:** Three-state Track A with behavioral rules
✅ **Approach-specific anchors:** Concrete 0-100 scales for all 7 signals × 3 approaches
✅ **Reliability framework:** Test-retest checks, metric correlations, cross-signal coherence
✅ **Skill extension plan:** 7 reference files (enhanced) + 2 schema files
✅ **File structure:** Complete with canonical assessment.json
✅ **Data flow:** Inputs, outputs, quality-conditional execution
✅ **Validation strategy:** 6 checkpoints (enhanced) + Phase 1.5 repliCATS pilot
✅ **Phase 1 implementation:** 10 steps, 12-15 hours (up from 6-7 due to enhancements)

### Major Improvements from v1.0

1. **Track A quality gating** - Not just monitoring, but gating with behavioral rules
2. **6-prompt architecture** - Reduced complexity, increased coherence
3. **Approach-specific scoring anchors** - Concrete, operational, approach-differentiated
4. **Test-retest reliability** - Quantitative validation throughout
5. **Early repliCATS pilot** - Structural validation before full build
6. **Canonical assessment.json** - Enables corpus-level analysis
7. **Defeasible interpretations** - Context-sensitive "no method" handling
8. **Metric-signal integration** - Soft guidance with divergence monitoring
9. **Experimental disclaimers** - Appropriate caveats for development phase
10. **Cross-signal coherence** - Explicit checks for contradictions

### Ready to Build ✅

**Immediate next actions:**
1. **Step 1:** Extend research-assessor skill (2h)
2. **Step 2:** Create classification prompt (1h)
3. **Step 3:** Test classifier with reliability (1.5h)
4. **Step 3.5:** Early repliCATS pilot (1-2h) *CONDITIONAL*
5. **Step 4:** Create Track A gating prompt (1h)
6. **Step 5:** Create foundational clarity cluster (1.5h)
7. **Step 6:** Test Track A + cluster 1 with reliability (2h)
8. **Steps 7-10:** Remaining clusters + report + validation (5-7h)

**Estimated Phase 1 time:** 12-15 hours (up from 6-7h in v1.0, due to reliability testing and quality enhancements)
**Estimated total time (Phases 1-5):** 25-35 hours (accounting for repliCATS validation and Shawn's manual assessment)

---

## Appendix: Key Design Decisions Log

*[For reference - decisions made during plan revision]*

### Decision 1: Skill Architecture
- **Question:** Extend research-assessor vs create separate credibility-assessor?
- **Decision:** Extend research-assessor
- **Rationale:** Organic linkage, progressive disclosure, compartmentalized references
- **Source:** Shawn input (2025-11-16)

### Decision 2: Prompt Consolidation
- **Question:** 10 separate prompts vs consolidated?
- **Decision:** 6-prompt architecture (clusters by conceptual coherence)
- **Rationale:** Reduces maintenance, enables cross-signal reasoning, respects size constraints
- **Source:** Synthesis of Claude + GPT-5.1 + Shawn feedback

### Decision 3: 500-Line Threshold
- **Question:** Hard ceiling or monitoring point?
- **Decision:** Monitoring threshold, not hard ceiling
- **Clarification:** 500 lines triggers careful attention, but 550-650 acceptable if conceptually coherent
- **Source:** Shawn clarification (2025-11-16)

### Decision 4: Track A Integration
- **Question:** Parallel monitoring vs quality gating?
- **Decision:** Quality gating with three states
- **Rationale:** GPT-5.1 correctly identified "operationally toothless" flaw; gating adds control logic
- **Source:** GPT-5.1 Major Concern #2, fully adopted

### Decision 5: Approach-Specific Operationalization
- **Question:** How to mechanically implement approach emphasis?
- **Decision:** Concrete 0-100 anchors per approach per signal
- **Rationale:** Addresses "mechanically vague" critique, enables validation of actual application
- **Source:** GPT-5.1 Major Concern #3, fully adopted

### Decision 6: Validation Quantification
- **Question:** Manual "makes sense" checks sufficient?
- **Decision:** Add test-retest reliability (SD < 10), metric correlations, cross-signal coherence
- **Rationale:** Quantitative baselines catch issues manual review might miss
- **Source:** GPT-5.1 Major Concern #4 + Claude self-critique, fully adopted

### Decision 7: RepliCATS Timing
- **Question:** Validate after full build (Phase 5) or earlier?
- **Decision:** Add Phase 1.5 early pilot + Phase 3 full validation
- **Rationale:** Early pilot catches structural misalignment before investing in all rubrics
- **Source:** GPT-5.1 Major Concern #4, conditionally adopted (access confirmed)

### Decision 8: Report Length
- **Question:** 3-5 pages or reduce to 1-2 pages?
- **Decision:** Keep 3-5 pages
- **Rationale:** Development use case requires detail; add disclaimer instead
- **Source:** Respectfully declined GPT-5.1 Medium Concern #4

### Decision 9: Metric-Signal Rules
- **Question:** Hard rules (e.g., "If ESD < X, Validity < Y") or soft guidance?
- **Decision:** Soft guidance with divergence monitoring
- **Rationale:** Hard rules too rigid, defeats LLM flexibility; monitoring catches issues without constraining
- **Source:** Respectfully declined GPT-5.1 Medium Concern #5, adopted alternative

### Decision 10: Canonical Assessment Object
- **Question:** Keep individual files or consolidate?
- **Decision:** Both - individual files + canonical assessment.json post-processing
- **Rationale:** Files for human reading, JSON for corpus analysis
- **Source:** GPT-5.1 Opportunity #1, fully adopted

---

**Plan Status:** Implementation-ready v2.0
**Next Action:** Begin Step 1 (Extend research-assessor skill)

**Related Documents:**
- planning/credibility-implementation-plan-detailed.md (v1.0)
- planning/synthesis-external-feedback.md (critical analysis)
- planning/paper-credibility-analysis-framework.md (design decisions)
- planning/research-approach-classification-framework.md (classification spec)
- planning/gpt51-feedback/credibility-implementation-plan-detailed-feedback.md (external review)
