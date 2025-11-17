# Credibility Assessment Implementation Plan (Detailed)
## Complete Architecture, Prompts, Skills, and Data Flow

**Document Purpose:** Comprehensive implementation plan for individual paper credibility assessment system

**Date Created:** 2025-11-16
**Status:** Implementation-ready detailed plan
**Prerequisites:** Extraction complete (Pass 0-6), metrics calculated (Phase 6)

---

## Executive Summary

### What This Plan Delivers

A complete credibility assessment system consisting of:
- **Research approach classifier** (expressed vs revealed methodology with HARKing detection)
- **Seven signal assessors** (repliCATS Seven Signals adapted for HASS)
- **Track A quality monitor** (extraction/assessment quality tracking)
- **Report generator** (3-5 page credibility reports)

### Architecture Principles

Following the **research-assessor skill architecture**:
- **Skills provide:** Decision frameworks, schemas, reference materials
- **Runtime provides:** Extraction prompts (evolve through testing)
- **Why this separation:** Enables prompt tuning without skill versioning conflicts

**Critical design heuristic:** "Discrete tasks = separate prompts; interacting tasks = same prompt"

---

## Part 1: Prompt vs Skill Boundary Analysis

### Skill-Creator Guidance Applied

Based on skill-creator principles and research-assessor architecture analysis:

#### What Goes in Skills (Stable Knowledge)

**Skills are for:**
- Decision frameworks (how to apply rubrics)
- Schema definitions (output structures)
- Reference materials (signal definitions, approach characteristics)
- Domain expertise (HASS-specific adaptations)

**For credibility assessment, skills should contain:**
1. **Credibility frameworks** - How to interpret signals per research approach
2. **Signal definitions** - What each repliCATS signal means in HASS context
3. **Approach taxonomy** - Characteristics of inductive/deductive/abductive research
4. **Assessment schemas** - Output structure for classifications and assessments
5. **Quality monitoring frameworks** - Track A self-assessment criteria

#### What Goes in Runtime Prompts (Evolving Instructions)

**Prompts are for:**
- Specific extraction/assessment instructions
- Task-specific guidance that evolves through testing
- Context-specific examples
- Workflow orchestration

**For credibility assessment, prompts should contain:**
1. **Classification instructions** - How to classify this specific paper
2. **Signal assessment instructions** - How to assess this specific signal on this paper
3. **Quality check instructions** - How to evaluate extraction quality for this paper
4. **Report generation instructions** - How to structure the final report

### Recommendation: Extend research-assessor Skill

**Why extend rather than create new skill:**
- Credibility assessment builds directly on extraction
- Shares infrastructure (schemas, HASS domain knowledge)
- Maintains single coherent workflow
- Reduces skill proliferation

**What to add to research-assessor skill:**
```
.claude/skills/research-assessor/
├── SKILL.md (update description to include credibility assessment)
└── references/
    ├── credibility/
    │   ├── approach-taxonomy.md          # Inductive/deductive/abductive characteristics
    │   ├── signal-definitions-hass.md    # Seven signals adapted for HASS
    │   ├── assessment-frameworks.md      # How to apply signals per approach
    │   ├── harking-detection-guide.md    # Expressed vs revealed comparison
    │   └── track-a-quality-criteria.md   # Self-assessment framework
    └── schema/
        ├── classification-schema.md       # Research approach classification output
        └── assessment-schema.md           # Signal assessment output structure
```

**What stays as runtime prompts:**
```
assessment-system/prompts/
├── classify-research-approach.md    # Classification instructions
├── assess-comprehensibility.md      # Signal 1 assessment
├── assess-transparency.md           # Signal 2 assessment
├── assess-plausibility.md           # Signal 3 assessment
├── assess-validity.md               # Signal 4 assessment
├── assess-robustness.md             # Signal 5 assessment
├── assess-replicability.md          # Signal 6 assessment
├── assess-generalisability.md       # Signal 7 assessment
├── track-a-quality-check.md         # Quality monitoring
└── generate-credibility-report.md   # Report generation
```

---

## Part 2: Prompt Architecture Diagram

### Overview: 10 Prompts, Sequential + Parallel Execution

```
┌─────────────────────────────────────────────────────────────────┐
│                    INPUT: extraction.json                        │
│          (Claims, Evidence, RDMAP, Infrastructure, Metrics)      │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ↓
┌─────────────────────────────────────────────────────────────────┐
│  PROMPT 1: classify-research-approach.md                         │
│  • Loads extraction (claims, RDMAP, methods structure)          │
│  • Detects expressed approach (stated methodology)              │
│  • Infers revealed approach (actual methodology)                │
│  • Compares expressed vs revealed (HARKing detection)           │
│  • Outputs: classification.json                                 │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ↓
                  classification.json
                         │
        ┌────────────────┴────────────────┐
        │                                  │
        ↓                                  ↓
┌──────────────────┐            ┌──────────────────────┐
│ TRACK A BRANCH   │            │ TRACK B BRANCH       │
│ (Quality)        │            │ (Credibility)        │
└──────────────────┘            └──────────────────────┘
        │                                  │
        ↓                                  ↓
┌─────────────────────────────────────────────────────────────────┐
│  PROMPT 2: track-a-quality-check.md                              │
│  • Evaluates extraction quality (completeness, accuracy)         │
│  • Validates metric scores against qualitative assessment        │
│  • Checks classification confidence                              │
│  • Identifies improvement opportunities                          │
│  • Outputs: track-a-quality.md                                  │
└─────────────────────────────────────────────────────────────────┘
        │
        │                       ┌─────────────────────────────────┐
        │                       │  PARALLEL EXECUTION (7 prompts) │
        │                       │  All use same inputs:           │
        │                       │  • extraction.json              │
        │                       │  • classification.json          │
        │                       │  Each outputs to own file       │
        │                       └─────────────────────────────────┘
        │                                  │
        │         ┌────────────────────────┼────────────────────────┐
        │         │            │           │           │            │
        │         ↓            ↓           ↓           ↓            ↓
        │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐
        │  │ PROMPT 3 │ │ PROMPT 4 │ │ PROMPT 5 │ │ PROMPT 6 │ │ PROMPT 7 │
        │  │Comprehen-│ │Transpare-│ │Plausibi- │ │ Validity │ │Robustness│
        │  │sibility  │ │ncy       │ │lity      │ │          │ │          │
        │  └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘
        │       │            │             │            │            │
        │       ↓            ↓             ↓            ↓            ↓
        │  signal-01.md  signal-02.md signal-03.md signal-04.md signal-05.md
        │
        │         ┌────────────────────────┐
        │         │                        │
        │         ↓                        ↓
        │  ┌──────────┐            ┌──────────┐
        │  │ PROMPT 8 │            │ PROMPT 9 │
        │  │Replicab- │            │Generaliz-│
        │  │ility     │            │ability   │
        │  └────┬─────┘            └────┬─────┘
        │       │                       │
        │       ↓                       ↓
        │  signal-06.md           signal-07.md
        │
        │
        └───────────────────┬───────────────────────┘
                            │
                            ↓
                    All 9 files ready:
                    • classification.json
                    • track-a-quality.md
                    • signal-01.md through signal-07.md
                            │
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│  PROMPT 10: generate-credibility-report.md                       │
│  • Loads all 9 input files                                       │
│  • Synthesises credibility assessment                            │
│  • Applies approach-specific emphasis                            │
│  • Generates 3-5 page summary report                             │
│  • Outputs: credibility-report.md                               │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ↓
┌─────────────────────────────────────────────────────────────────┐
│              OUTPUT: credibility-report.md                       │
│    (Complete credibility assessment with all signals)            │
└─────────────────────────────────────────────────────────────────┘
```

### Execution Dependencies

**Sequential dependencies:**
1. `classification.json` MUST exist before any other prompt runs
2. All 7 signal assessments + track-a quality check can run in parallel (independent)
3. `credibility-report.md` generation MUST wait for all 9 inputs to exist

**Parallel execution opportunities:**
- Prompts 3-9 (7 signals + track-a) can run concurrently once classification complete
- No dependencies between signal assessments

---

## Part 3: Skill Extension Design

### research-assessor Skill Updates

#### SKILL.md Description Update

**Current description:**
```yaml
description: Extracts and assesses research methodology, claims, evidence, and infrastructure from research papers in HASS disciplines. Evaluates transparency, replicability, and credibility through systematic extraction of research designs, methods, protocols, claims, evidence, and reproducibility infrastructure (PIDs, FAIR compliance, permits, funding) using a seven-pass iterative workflow.
```

**Proposed updated description:**
```yaml
description: Extracts and assesses research methodology, claims, evidence, and infrastructure from research papers in HASS disciplines. Evaluates transparency, replicability, and credibility through systematic extraction (seven-pass workflow) and credibility assessment (research approach classification and repliCATS Seven Signals evaluation adapted for HASS).
```

#### SKILL.md Workflow Section Addition

Add new section after existing Pass 7 (Validation):

```markdown
### Pass 8: Research Approach Classification (Optional - For Credibility Assessment)

**Purpose:** Classify research approach (inductive/deductive/abductive) with expressed vs revealed comparison

**Inputs:**
- extraction.json (complete extraction from Passes 1-6)

**Process:**
1. Detect expressed approach (what paper states)
2. Infer revealed approach (what paper does)
3. Compare expressed vs revealed (HARKing detection)
4. Generate classification with confidence and justification

**Outputs:**
- classification.json

**References:**
- `references/credibility/approach-taxonomy.md`
- `references/credibility/harking-detection-guide.md`
- `references/schema/classification-schema.md`

### Pass 9: Credibility Assessment (Optional - After Classification)

**Purpose:** Assess paper credibility using repliCATS Seven Signals adapted for HASS

**Inputs:**
- extraction.json
- classification.json
- Metrics (from Phase 6)

**Process:**
1. Track A quality check (extraction quality monitoring)
2. Assess seven signals in parallel:
   - Comprehensibility
   - Transparency
   - Plausibility
   - Validity
   - Robustness
   - Replicability
   - Generalisability
3. Apply approach-specific emphasis
4. Generate credibility report

**Outputs:**
- track-a-quality.md
- signal-01.md through signal-07.md
- credibility-report.md

**References:**
- `references/credibility/signal-definitions-hass.md`
- `references/credibility/assessment-frameworks.md`
- `references/credibility/track-a-quality-criteria.md`
- `references/schema/assessment-schema.md`
```

#### New Reference Files to Add

**1. `references/credibility/approach-taxonomy.md`**

Content structure:
```markdown
# Research Approach Taxonomy
## Inductive, Deductive, Abductive Characteristics for HASS

### Three Primary Approaches

#### Deductive (Hypothesis-Testing, Confirmatory)
[Content from research-approach-classification-framework.md]

#### Inductive (Pattern-Finding, Exploratory)
[Content from research-approach-classification-framework.md]

#### Abductive (Inference to Best Explanation)
[Content from research-approach-classification-framework.md]

### Mixed-Method Characterisation
[Qualitative description guidance]

### Absence of Expressed Methodology
[Significance and interpretation]
```

**2. `references/credibility/signal-definitions-hass.md`**

Content structure:
```markdown
# RepliCATS Seven Signals - HASS Adaptations
## Signal Definitions with Approach-Specific Guidance

### Signal 1: Comprehensibility
- Definition
- Assessment questions (5-7 questions)
- Approach-specific interpretation
- Red flags / green flags
- Scoring guidance (0-100 scale)

[Repeat for all 7 signals]
```

**3. `references/credibility/assessment-frameworks.md`**

Content structure:
```markdown
# Credibility Assessment Frameworks by Research Approach

### Framework Selection Logic
- Deductive → Emphasise Validity, Robustness, Replicability
- Inductive → Emphasise Transparency, Comprehensibility, Generalisability
- Abductive → Emphasise Plausibility, Validity, Robustness

### Approach-Specific Signal Weighting
[Narrative importance + experimental percentages]

### HARKing-Flagged Papers
[Additional scrutiny requirements]
```

**4. `references/credibility/harking-detection-guide.md`**

Content structure:
```markdown
# HARKing Detection Guide
## Expressed vs Revealed Methodology Comparison

### Detection Process
1. Extract expressed approach
2. Determine revealed approach
3. Compare and flag mismatches

### Mismatch Types
- HARKing_potential
- methodological_confusion
- disciplinary_convention
- legitimately_mixed

### Examples and Patterns
[From research-approach-classification-framework.md]
```

**5. `references/credibility/track-a-quality-criteria.md`**

Content structure:
```markdown
# Track A Quality Monitoring Criteria
## Self-Assessment Framework for Extraction and Assessment Quality

### Quality Dimensions
1. Extraction accuracy
2. Metric validity
3. Classification quality
4. Assessment consistency

### Assessment Questions
[From credibility-assessment-implementation-roadmap.md Track A section]

### Output Format
[Track A notes template]
```

**6. `references/schema/classification-schema.md`**

Content structure:
```yaml
# Research Approach Classification Schema

[Complete YAML schema from research-approach-classification-framework.md]
```

**7. `references/schema/assessment-schema.md`**

Content structure:
```yaml
# Credibility Assessment Output Schema

signal_assessment:
  signal_name: "transparency"
  signal_number: 2
  score: 75
  confidence: "high"

  # Assessment content
  assessment_summary: "2-3 sentence summary"
  key_strengths: ["strength 1", "strength 2"]
  key_weaknesses: ["weakness 1", "weakness 2"]

  # Evidence from extraction
  supporting_evidence:
    - extraction_element: "RD001"
      relevance: "Explicit research design statement"
    - extraction_element: "M023"
      relevance: "Detailed protocol documentation"

  # Justification
  scoring_justification: "Detailed rationale for score"

  # Approach context
  approach_context: "How this signal applies to this research approach"

  # Metadata
  assessment_date: "2025-11-16"
  assessor: "Claude (research-assessor skill)"
```

---

## Part 4: File Structure Specification

### Complete Directory Structure

```
outputs/{paper-slug}/
├── extraction.json                           # From Passes 1-6 (existing)
├── {paper-slug}.txt                          # Plain text (existing)
├── metrics/                                  # From Phase 6 (existing)
│   └── metrics.json                          # 8 credibility metrics
├── assessment/                               # NEW: Credibility assessment outputs
│   ├── classification.json                   # Research approach classification
│   ├── track-a-quality.md                   # Quality monitoring (Track A)
│   ├── signals/                             # Individual signal assessments
│   │   ├── 01-comprehensibility.md
│   │   ├── 02-transparency.md
│   │   ├── 03-plausibility.md
│   │   ├── 04-validity.md
│   │   ├── 05-robustness.md
│   │   ├── 06-replicability.md
│   │   └── 07-generalisability.md
│   ├── credibility-report-v1.md             # 3-5 page summary report
│   └── scorecard-credibility.md             # Optional: Scorecard format
└── logs/                                     # Optional: Workflow logs
    └── assessment-log.md
```

### File Descriptions

**`classification.json`** (YAML format in JSON file)
```yaml
research_approach_classification:
  classified_after_pass: 6
  classification_date: "2025-11-16"

  expressed_approach: "inductive|deductive|abductive|mixed|none_stated"
  expressed_evidence: ["quote 1", "quote 2"]
  expressed_source_sections: ["introduction", "methods"]

  revealed_approach: "inductive|deductive|abductive|mixed"
  revealed_evidence:
    claims_structure: "..."
    methods_application: "..."
    analytical_workflow: "..."
  revealed_confidence: "high|medium|low"

  expressed_vs_revealed: "matched|partial|mismatched"
  harking_flag: false

  classification_justification: |
    Detailed narrative...

  credibility_framework_to_use: "inductive_emphasis"
  signal_prioritisation:
    primary_signals: ["transparency", "comprehensibility", "generalisability"]
    secondary_signals: ["validity", "robustness"]
    deemphasised_signals: []
```

**`track-a-quality.md`** (Markdown report)
```markdown
# Track A: Extraction & Assessment Quality Notes
## Paper: {paper-slug}

### Extraction Confidence
- **Overall:** High|Medium|Low
- **Claims extraction:** [notes]
- **Evidence extraction:** [notes]
- **RDMAP extraction:** [notes]
- **Infrastructure extraction:** [notes]

### Metric Validity
- **Metrics align with qualitative assessment:** Yes|Partial|No
- **Discrepancies noted:** [specific mismatches]
- **Most useful metrics:** [list]
- **Least useful metrics:** [list]

### Classification Quality
- **Approach classification confidence:** High|Medium|Low
- **Classification notes:** [uncertainties]

### Assessment Quality
- **Rubric application consistency:** [notes]
- **Score confidence:** [notes]
- **Areas of uncertainty:** [list]

### Improvement Opportunities
- [Specific suggestions for extraction]
- [Specific suggestions for metrics]
- [Specific suggestions for rubrics]
```

**`signals/02-transparency.md`** (Example signal assessment)
```markdown
# Signal Assessment: Transparency
## Paper: {paper-slug}

**Score:** 75/100
**Confidence:** High

### Summary
Research design and methods are well-documented with explicit methodological statements. Data availability clearly stated. Some gaps in protocol detail for field sampling procedures.

### Key Strengths
- Explicit research design statement in Introduction (RD001)
- Detailed methods documentation with protocols (M005, M007, M023)
- Data repository link provided (DOI: 10.5281/zenodo.123456)
- ORCID identifiers for all authors

### Key Weaknesses
- No code repository despite computational analysis (GIS procedures)
- Sampling protocol lacks detail on selection criteria
- No pre-registration or analysis plan documented

### Supporting Evidence from Extraction
- **RD001:** "This study employs an inductive exploratory approach..."
- **M023:** Detailed survey protocol with spatial sampling framework
- **Infrastructure:** Data DOI present, code DOI absent

### Scoring Justification
Score of 75 reflects strong transparency in research design documentation and data sharing (80-100 range = "High transparency"), with minor deductions for missing code repository (-10) and incomplete protocol detail (-15).

### Approach-Specific Context
For inductive exploratory research, transparency is a PRIMARY signal. This paper meets high standards for stated approach documentation and data availability. Code sharing would move score to 85-90 range.

---

**Assessment Date:** 2025-11-16
**Assessor:** Claude (research-assessor skill)
```

**`credibility-report-v1.md`** (3-5 page summary)
```markdown
# Credibility Assessment Report
## {Paper Title}

**Authors:** {authors}
**Publication:** {journal} ({year})
**Assessment Date:** 2025-11-16
**Assessor:** Claude (research-assessor skill)

---

## Executive Summary

[2-3 paragraph overview of credibility profile, key strengths/weaknesses, overall assessment]

---

## Paper Metadata & Research Approach

### Classification
- **Expressed Approach:** Inductive
- **Revealed Approach:** Primarily inductive
- **Alignment:** Matched
- **Confidence:** High

[Brief justification of classification]

---

## Metric Scorecard

[Table of 8 metrics with scores and interpretations]

---

## Seven-Signal Assessment

### Signal 1: Comprehensibility (Score: 80/100)
[~150-200 words: summary, strengths, weaknesses, justification]

### Signal 2: Transparency (Score: 75/100)
[~150-200 words]

[Repeat for all 7 signals]

---

## Key Strengths & Weaknesses

### Major Strengths
1. [Strength with specific evidence]
2. [Strength with specific evidence]
3. [Strength with specific evidence]

### Major Weaknesses
1. [Weakness with specific evidence]
2. [Weakness with specific evidence]
3. [Weakness with specific evidence]

---

## Actionable Recommendations

### For This Paper (Retrospective)
1. [Specific improvement with feasibility assessment]
2. [Specific improvement]
3. [Specific improvement]

### For Future Research (Prospective)
1. [Best practice to adopt]
2. [Best practice to adopt]
3. [Best practice to adopt]

---

## Overall Credibility Profile

[Final 2-3 paragraph synthesis: what is this paper's credibility signature? How does it compare to corpus norms? What are implications for trustworthiness and replicability?]

---

## Track A Quality Notes

[Condensed version of track-a-quality.md - extraction confidence, metric validity, assessment quality]

---

**Report Version:** 1.0
**Generation Date:** 2025-11-16
**Based On:**
- extraction.json (Pass 6 complete)
- metrics.json (8 credibility metrics)
- classification.json (Research approach)
- 7 signal assessments
```

---

## Part 5: Data Flow & Dependencies

### Input Requirements per Prompt

**PROMPT 1: classify-research-approach.md**
- **Inputs:**
  - extraction.json (claims, RDMAP, methods structure)
  - Paper full text (if needed for methodological statements)
- **Skill references:**
  - `references/credibility/approach-taxonomy.md`
  - `references/credibility/harking-detection-guide.md`
  - `references/schema/classification-schema.md`
- **Outputs:**
  - classification.json

**PROMPT 2: track-a-quality-check.md**
- **Inputs:**
  - extraction.json
  - metrics.json
  - classification.json
- **Skill references:**
  - `references/credibility/track-a-quality-criteria.md`
- **Outputs:**
  - track-a-quality.md

**PROMPTS 3-9: assess-{signal}.md** (7 prompts)
- **Inputs (all signals):**
  - extraction.json
  - classification.json
  - metrics.json (relevant metrics for signal)
- **Skill references (all signals):**
  - `references/credibility/signal-definitions-hass.md`
  - `references/credibility/assessment-frameworks.md`
  - `references/schema/assessment-schema.md`
- **Outputs:**
  - signals/0{N}-{signal-name}.md

**PROMPT 10: generate-credibility-report.md**
- **Inputs:**
  - classification.json
  - track-a-quality.md
  - signals/01-comprehensibility.md through signals/07-generalisability.md
  - metrics.json (for scorecard table)
- **Skill references:**
  - Assessment frameworks (for synthesis)
- **Outputs:**
  - credibility-report-v1.md

### Data Flow Summary

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
        ↓                                  ↓                 │
  track-a-quality ←─── metrics.json  assess-signals ←───────┘
        │                                  │
        ↓                                  ↓
  track-a-quality.md              signals/*.md (7 files)
        │                                  │
        └────────────────┬─────────────────┘
                         │
                         ↓
              generate-credibility-report
                         │
                         ↓
               credibility-report-v1.md
```

---

## Part 6: Validation Checkpoints

### Checkpoint 1: Classifier Working

**After implementing classify-research-approach.md prompt:**

**Test papers:** sobotkova-et-al-2024, ballsun-stanton-et-al-2018, penske-et-al-2023

**Validation criteria:**
- [ ] classification.json generated for all 3 papers
- [ ] All required fields populated (expressed, revealed, comparison, justification)
- [ ] Expressed vs revealed comparison makes sense
- [ ] HARKing detection working (flags mismatches appropriately)
- [ ] "none_stated" handled correctly (doesn't strain to find absent methodology)
- [ ] Mixed-method papers characterised qualitatively (no false precision)
- [ ] Justifications cite specific extraction elements (claim IDs, RDMAP IDs)

**Validation commands:**
```bash
# Check required fields present
jq '.research_approach_classification | keys' classification.json

# Verify approach values
jq '.research_approach_classification.expressed_approach' classification.json
jq '.research_approach_classification.revealed_approach' classification.json

# Check HARKing detection
jq '.research_approach_classification.harking_flag' classification.json

# Validate justification length (should be substantial)
jq '.research_approach_classification.classification_justification | length' classification.json
```

**Manual review:**
- Do classifications align with paper reading?
- Are justifications well-grounded in extraction?
- Is confidence appropriately calibrated?

### Checkpoint 2: First Rubric Working (Transparency)

**After implementing assess-transparency.md prompt:**

**Test paper:** sobotkova-et-al-2024

**Validation criteria:**
- [ ] signals/02-transparency.md generated
- [ ] Score in 0-100 range with confidence
- [ ] Summary present (2-3 sentences)
- [ ] Key strengths (3-5 items) with specific evidence
- [ ] Key weaknesses (3-5 items) with specific evidence
- [ ] Supporting evidence cites extraction elements
- [ ] Scoring justification explains score
- [ ] Approach-specific context applied

**Validation commands:**
```bash
# Check file exists and has content
test -f assessment/signals/02-transparency.md && echo "File exists"
wc -w assessment/signals/02-transparency.md  # Should be ~400-600 words

# Extract score (manual inspection)
grep "Score:" assessment/signals/02-transparency.md
```

**Manual review:**
- Does score feel right given paper characteristics?
- Are strengths/weaknesses specific (not generic)?
- Does assessment reference extraction elements correctly?
- Is approach context appropriate (inductive emphasis)?

### Checkpoint 3: End-to-End Proof of Concept

**After implementing classifier + transparency assessment:**

**Test paper:** sobotkova-et-al-2024

**Full workflow test:**
1. Run classifier → classification.json
2. Run transparency assessor → signals/02-transparency.md
3. Generate mini-report (just classification + transparency section)

**Validation criteria:**
- [ ] Workflow completes without errors
- [ ] classification.json valid and sensible
- [ ] signals/02-transparency.md complete and grounded
- [ ] Data flows correctly between prompts
- [ ] Mini-report coherent and actionable

**Success criteria:**
- All files generated
- Manual review confirms quality
- Ready to expand to remaining 6 signals

### Checkpoint 4: All Seven Signals Working

**After implementing all 7 signal assessment prompts:**

**Test papers:** sobotkova-et-al-2024, ballsun-stanton-et-al-2018, penske-et-al-2023

**Validation criteria:**
- [ ] All 7 signal files generated for each paper
- [ ] Scores discriminate appropriately (not all 70-80)
- [ ] Approach-specific emphasis visible in assessments
- [ ] Parallel execution successful (no dependency issues)
- [ ] Cross-signal consistency (no contradictions)

**Validation commands:**
```bash
# Check all 7 signals present
ls -1 assessment/signals/ | wc -l  # Should be 7

# Extract all scores
for f in assessment/signals/*.md; do
  echo "$f:"
  grep "Score:" "$f"
done

# Check score distribution (should vary)
grep -h "Score:" assessment/signals/*.md | sort
```

**Manual review:**
- Do signal scores make sense together?
- Are approach-specific emphases applied (inductive vs deductive)?
- Do assessments reference different extraction elements appropriately?

### Checkpoint 5: Complete Report Generated

**After implementing generate-credibility-report.md:**

**Test paper:** sobotkova-et-al-2024

**Validation criteria:**
- [ ] credibility-report-v1.md generated
- [ ] Report is 3-5 pages (~1500-2500 words)
- [ ] All sections present (metadata, scorecard, signals, recommendations)
- [ ] Synthesis coherent and actionable
- [ ] Track A notes integrated
- [ ] Report references specific evidence

**Validation commands:**
```bash
# Check report length
wc -w assessment/credibility-report-v1.md  # Target: 1500-2500 words

# Check section headers present
grep "^##" assessment/credibility-report-v1.md
```

**Manual review:**
- Is report readable and well-structured?
- Does synthesis add value beyond individual signal assessments?
- Are recommendations specific and implementable?
- Is overall credibility profile convincing?

### Checkpoint 6: Corpus Testing (Expand to All 10 Papers)

**After validating on 3 papers:**

**Test all papers in corpus**

**Validation criteria:**
- [ ] All 10 papers classified successfully
- [ ] All 10 papers have 7 signal assessments
- [ ] All 10 papers have credibility reports
- [ ] Cross-paper patterns emerge
- [ ] Rubrics applied consistently
- [ ] No systematic failures

**Validation commands:**
```bash
# Count successful classifications
find outputs -name "classification.json" | wc -l  # Should be 10

# Count complete assessments (7 signals each)
for paper in outputs/*/; do
  count=$(find "$paper/assessment/signals" -name "*.md" 2>/dev/null | wc -l)
  echo "$paper: $count signals"
done  # All should show 7

# Count credibility reports
find outputs -name "credibility-report-v1.md" | wc -l  # Should be 10
```

**Manual review:**
- Do classifications make sense across corpus?
- Are scores discriminating (high vs medium vs low credibility papers)?
- Do patterns emerge (temporal trends, disciplinary differences)?
- Are any papers outliers requiring special handling?

---

## Part 7: Implementation Sequence (Phase 1 Detailed)

### Step 1: Extend research-assessor Skill (2 hours)

**Actions:**
1. Update SKILL.md description and add Passes 8-9
2. Create 7 new reference files in `references/credibility/`
3. Create 2 new schema files in `references/schema/`
4. Document skill changes

**Files to create:**
- `references/credibility/approach-taxonomy.md` (adapt from research-approach-classification-framework.md)
- `references/credibility/signal-definitions-hass.md` (adapt from background-research/replicats-seven-signals-hass-adaptation.md)
- `references/credibility/assessment-frameworks.md` (new, from paper-credibility-analysis-framework.md)
- `references/credibility/harking-detection-guide.md` (from research-approach-classification-framework.md)
- `references/credibility/track-a-quality-criteria.md` (from credibility-assessment-implementation-roadmap.md)
- `references/schema/classification-schema.md` (from research-approach-classification-framework.md)
- `references/schema/assessment-schema.md` (new, define signal assessment structure)

**Validation:**
- [ ] All files created
- [ ] SKILL.md updated
- [ ] Skill loads correctly (test with research-assessor skill invocation)

### Step 2: Create Classification Prompt (1 hour)

**Actions:**
1. Create `assessment-system/prompts/classify-research-approach.md`
2. Include clear instructions for:
   - Detecting expressed approach
   - Inferring revealed approach
   - Comparing expressed vs revealed
   - Handling "none_stated" cases
   - Mixed-method characterisation
3. Include examples from skill references
4. Specify output format (classification.json)

**Prompt structure:**
```markdown
# Research Approach Classification Prompt

## Task
Classify this paper's research approach...

## Instructions
1. Detect expressed approach
   - Search for methodological statements in intro/methods
   - Document exact quotes or paraphrases
   - If none stated, mark as "none_stated" (significant finding)

2. Infer revealed approach
   - Analyse claims structure (descriptive or hypothesis-testing?)
   - Analyse methods application (exploratory or confirmatory?)
   - Analyse analytical workflow (pattern discovery or prediction testing?)

3. Compare expressed vs revealed
   - Matched: Alignment between stated and actual
   - Partial: Mixed-method or legitimate variation
   - Mismatched: HARKing potential (flag for scrutiny)

4. Generate classification
   - Use schema from references/schema/classification-schema.md
   - Include detailed justification citing extraction elements
   - Assign confidence level

## Output
classification.json (YAML format)

## References
- references/credibility/approach-taxonomy.md
- references/credibility/harking-detection-guide.md
```

**Validation:**
- [ ] Prompt complete and clear
- [ ] References to skill files correct
- [ ] Output format specified

### Step 3: Test Classifier on 3 Papers (1 hour)

**Actions:**
1. Run classification on sobotkova-et-al-2024
2. Run classification on ballsun-stanton-et-al-2018
3. Run classification on penske-et-al-2023
4. Validate outputs (Checkpoint 1)
5. Refine prompt based on results

**Testing command pattern:**
```bash
# Manual invocation pattern (will be automated later)
# User provides paper path and classification prompt
# Claude executes classification following prompt
```

**Expected outcomes:**
- sobotkova-et-al-2024: Primarily inductive, matched
- ballsun-stanton-et-al-2018: Mixed methodological (software development), partial match
- penske-et-al-2023: Deductive, matched

**Refinement based on results:**
- Adjust prompt clarity if misunderstandings occur
- Update skill references if decision frameworks insufficient
- Document classification patterns in planning/classification-testing-log.md

### Step 4: Create First Rubric (Transparency) (1 hour)

**Actions:**
1. Create `assessment-system/prompts/assess-transparency.md`
2. Include:
   - Signal definition (what is transparency in HASS?)
   - 5-7 assessment questions
   - Scoring scale (0-100 with anchors)
   - Approach-specific interpretation notes
   - Examples of low/high transparency
3. Specify output format (signals/02-transparency.md)

**Prompt structure:**
```markdown
# Transparency Signal Assessment Prompt

## Signal Definition
Transparency: Clarity and completeness of research design, methods, and data documentation.

## Assessment Questions
1. Is research design explicitly stated?
2. Are methods documented with sufficient detail for assessment?
3. Are protocols available (if applicable)?
4. Is data availability clearly stated?
5. Is code/analysis workflow documented (if computational)?
6. Are research materials accessible?
7. Are limitations and assumptions stated?

## Scoring Scale (0-100)
- 0-19: Minimal transparency (no research design, vague methods)
- 20-39: Low transparency (implicit design, incomplete methods)
- 40-59: Moderate transparency (stated design, adequate methods, some gaps)
- 60-79: Good transparency (clear design, detailed methods, minor gaps)
- 80-100: Excellent transparency (comprehensive documentation, all materials accessible)

## Approach-Specific Interpretation
- **Inductive research:** PRIMARY SIGNAL - transparency crucial for assessing pattern validity
- **Deductive research:** HIGH IMPORTANCE - need clear hypothesis specification and testing procedures
- **Abductive research:** HIGH IMPORTANCE - need explicit theoretical frameworks and inference logic

## Assessment Process
1. Review extraction (RDMAP, infrastructure, methods)
2. Assess each question above
3. Identify key strengths (3-5 specific items with evidence)
4. Identify key weaknesses (3-5 specific items with evidence)
5. Assign score with justification
6. Apply approach-specific context

## Output Format
signals/02-transparency.md (see references/schema/assessment-schema.md)

## References
- references/credibility/signal-definitions-hass.md
- references/credibility/assessment-frameworks.md
```

**Validation:**
- [ ] Prompt complete
- [ ] Assessment questions clear
- [ ] Scoring anchors defined
- [ ] Approach context specified

### Step 5: End-to-End Proof of Concept (1-2 hours)

**Actions:**
1. On sobotkova-et-al-2024:
   - Run classifier
   - Run transparency assessor
   - Generate mini-report (classification + transparency only)
2. Validate workflow (Checkpoint 3)
3. Refine prompts based on output quality

**Mini-report structure:**
```markdown
# Credibility Assessment Mini-Report (Transparency Only)
## {Paper Title}

## Research Approach
[Classification summary]

## Transparency Assessment
[Signal assessment summary]

## Key Findings
- Strengths: [list]
- Weaknesses: [list]
- Recommendations: [list]
```

**Validation:**
- [ ] Workflow completes successfully
- [ ] classification.json valid
- [ ] signals/02-transparency.md complete
- [ ] Mini-report coherent
- [ ] Ready to expand to remaining signals

**Success criteria for Phase 1:**
- Classifier working on 3 papers
- First signal (transparency) assessment working
- End-to-end proof of concept validated
- Prompt architecture validated
- Skill extensions functional

---

## Part 8: Next Steps After Phase 1

### Phase 2: Complete All Seven Signal Rubrics (4-6 hours)

1. Create 6 remaining assessment prompts (comprehensibility, plausibility, validity, robustness, replicability, generalisability)
2. Each prompt follows transparency template structure
3. Test each signal on sobotkova-et-al-2024
4. Validate cross-signal consistency (Checkpoint 4)

### Phase 3: Create Track A and Report Generation (2-3 hours)

1. Create track-a-quality-check.md prompt
2. Create generate-credibility-report.md prompt
3. Test full workflow on sobotkova-et-al-2024
4. Validate complete report (Checkpoint 5)

### Phase 4: Expand to Corpus (2-3 hours)

1. Run full workflow on remaining 7 papers
2. Validate consistency across corpus (Checkpoint 6)
3. Document patterns in planning/cross-paper-assessment-patterns.md
4. Refine rubrics based on empirical application

### Phase 5: Documentation and Integration (2-3 hours)

1. Update WORKFLOW.md to include credibility assessment phase
2. Create user guide: docs/assessment-guide/how-to-assess-credibility.md
3. Create interpretation guide: docs/assessment-guide/interpreting-credibility-reports.md
4. Update assessment-system/README.md

---

## Summary: Implementation Readiness

### What We Have

✅ **Design decisions:** 17/17 questions answered, documented in planning/
✅ **Prompt architecture:** 10 prompts defined with execution dependencies
✅ **Skill extension plan:** 7 reference files + 2 schema files to add to research-assessor
✅ **File structure:** Complete directory structure specified
✅ **Data flow:** Inputs, outputs, dependencies mapped
✅ **Validation strategy:** 6 checkpoints with clear success criteria
✅ **Phase 1 implementation:** Step-by-step build sequence (6-7 hours)

### Ready to Build

**Immediate next actions:**
1. Extend research-assessor skill (Step 1)
2. Create classification prompt (Step 2)
3. Test on 3 papers (Step 3)
4. Create transparency rubric (Step 4)
5. End-to-end proof of concept (Step 5)

**Estimated Phase 1 time:** 6-7 hours
**Estimated total time (Phases 1-5):** 17-24 hours

---

**Document Status:** Implementation-ready detailed plan v1.0
**Date:** 2025-11-16
**Next Action:** Begin Step 1 (Extend research-assessor skill)

**Related Documents:**
- planning/paper-credibility-analysis-framework.md (design decisions)
- planning/research-approach-classification-framework.md (classification spec)
- planning/credibility-assessment-implementation-roadmap.md (5-phase overview)
- planning/SESSION-SUMMARY-credibility-assessment-planning.md (session recovery)
