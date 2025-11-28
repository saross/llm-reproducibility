# Cluster 1: Foundational Clarity Assessment

**Version:** v1.0
**Last Updated:** 2025-11-28
**Workflow Stage:** Pass 9 - Cluster 1 of 3
**Signals Assessed:** Comprehensibility, Transparency

---

## Your Task

Assess the two foundational credibility signals: **Comprehensibility** (clarity of claims and argument) and **Transparency** (research design and documentation). These signals are "foundational" because they underpin assessment of all other signals — you cannot properly evaluate validity or robustness if you cannot understand what was done.

**Inputs:**
- `extraction.json` from Pass 0-7 (complete extraction)
- `classification.json` from Pass 8 (research approach classification)
- `track-a-quality.md` from Track A (quality state)

**Your responsibility:** Score both signals using approach-specific anchors, cite evidence from extraction, provide rationale

**Output:** NEW file `assessment/cluster-1-foundational-clarity.md`

---

## 🚨 CRITICAL: Approach-Specific Scoring

**Different research approaches require different credibility criteria.** A score of 75 on Transparency means different things for:

- **Deductive research:** Pre-registration, hypothesis specification, data + code sharing
- **Inductive research:** Workflow transparency, sampling documentation, data archiving
- **Abductive research:** Framework clarity, reasoning traceability, alternative explanations

**You MUST use approach-specific anchors from classification.json.** Using wrong anchors is a category error.

---

## Assessment Workflow

### STEP 1: Load Classification Context

**Read from classification.json:**

```json
{
  "primary_classification": {
    "approach": "[deductive|inductive|abductive]",
    "confidence": "[high|medium|low]"
  },
  "paper_type": "[empirical|methodological|theoretical|meta_research]",
  "transparency_assessment": {
    "expressed_methodology_present": true|false,
    "transparency_quality": "[high|moderate|low]"
  }
}
```

**Record:**
- Primary approach (determines which anchor set to use)
- Paper type (affects expectations)
- Classification confidence (affects scoring precision)
- Preliminary transparency assessment (baseline for Transparency signal)

**Read from track-a-quality.md:**
- Quality state (HIGH/MODERATE/LOW)
- If MODERATE: Note caveats that apply to this assessment

---

### STEP 2: Assess Comprehensibility (Signal 1)

**Core Question:** Are claims clear, explicit, and well-structured? Can readers understand what is being claimed and on what basis?

**Read from extraction.json:**
- `claims[]` - Sample claims for clarity assessment (review first 10, last 5, and any flagged as important)
- `research_designs[]` - Explicit design statements
- `implicit_arguments[]` - Unstated reasoning (indicator of comprehensibility gaps)

**Assessment Dimensions:**

1. **Claim clarity:** Are central claims explicit and bounded (not vague or unlimited)?
2. **Term definition:** Are key domain terms defined?
3. **Argument structure:** Is the logical structure of the argument traceable?
4. **Scope boundaries:** Are claims appropriately scoped (who/what/where/when)?
5. **Evaluability:** Can claims be evaluated independently?

**Apply Approach-Specific Anchors:**

#### For DEDUCTIVE Research (Hypothesis-Testing)

| Score | Band | Criteria |
|-------|------|----------|
| 80-100 | Excellent | Hypotheses explicitly stated and clearly bounded; all key terms operationally defined; logical structure of hypothesis testing transparent; claims unambiguous and testable; reasoning from test results to conclusions clear |
| 60-79 | Good | Hypotheses stated (some definitional clarity may be lacking); most key terms defined; logical structure mostly clear; claims understandable and evaluable; reasoning generally traceable |
| 40-59 | Moderate | Hypotheses present but may lack precision; some key terms defined, others implicit; logical structure partially obscured; claims understandable with effort; some reasoning gaps |
| 20-39 | Low | Vague or implicit hypotheses; key terms largely undefined; logical structure unclear; claims ambiguous; reasoning difficult to follow |
| 0-19 | Minimal | No clear hypotheses; terms undefined; logical structure absent; claims incomprehensible; reasoning not traceable |

#### For INDUCTIVE Research (Exploratory, Pattern-Finding)

| Score | Band | Criteria |
|-------|------|----------|
| 80-100 | Excellent | Research questions and goals explicit; pattern descriptions clear and well-bounded; key terms defined; logical progression from observations to patterns transparent; scope of pattern claims clear |
| 60-79 | Good | Research goals stated; pattern descriptions mostly clear; most key terms defined; logical progression traceable; scope generally clear |
| 40-59 | Moderate | Research goals present (may lack specificity); pattern descriptions understandable (some vagueness); some terms defined; logical progression partially clear; scope mentioned |
| 20-39 | Low | Vague research goals; pattern descriptions ambiguous; terms largely undefined; logical progression unclear; scope unclear |
| 0-19 | Minimal | No clear research goals; pattern descriptions incomprehensible; terms undefined; no logical structure; no scope boundaries |

#### For ABDUCTIVE Research (Inference to Best Explanation)

| Score | Band | Criteria |
|-------|------|----------|
| 80-100 | Excellent | Explanatory claims explicitly stated and bounded; theoretical framework clear; alternative explanations articulated; inference logic transparent; key concepts well-defined; scope and limitations clear |
| 60-79 | Good | Explanatory claims stated; framework mostly clear; some alternatives mentioned; inference logic traceable; key concepts defined |
| 40-59 | Moderate | Explanatory claims present (may lack precision); framework partially clear; alternatives implicit or limited; inference logic partially obscured; some concepts defined |
| 20-39 | Low | Vague explanatory claims; framework unclear; no alternatives; inference logic opaque; concepts undefined |
| 0-19 | Minimal | No clear explanatory claims; no framework; single interpretation with no justification; inference logic absent; concepts undefined |

#### For METHODOLOGICAL Papers

Use inductive anchors with additional emphasis on:
- Technical specification clarity
- Feature descriptions bounded and precise
- Design rationale explicit

**Evidence Collection:**

Document specific evidence from extraction.json:
- Quote 2-3 exemplary claims (clear/unclear)
- Note any implicit_arguments flagged (comprehensibility gaps)
- Reference research_designs that state or fail to state research goals
- Note any undefined terms or scope ambiguities

**Score Assignment:**

```yaml
comprehensibility:
  score: [0-100]
  band: "[minimal|low|moderate|good|excellent]"
  approach_anchors_used: "[deductive|inductive|abductive|methodological]"
  evidence_citations:
    - "C001: '[quote]' - [assessment]"
    - "RD001: '[quote]' - [assessment]"
    - "IM001: '[quote]' - [assessment - indicates gap]"
  strengths:
    - "[Specific strength 1]"
    - "[Specific strength 2]"
  weaknesses:
    - "[Specific weakness 1]"
  rationale: "[2-3 sentence justification referencing anchor criteria]"
```

---

### STEP 3: Assess Transparency (Signal 2)

**Core Question:** Are research methods and procedures well-documented? Can others understand and critically evaluate the research design?

**Read from extraction.json:**
- `research_designs[]` - Explicit design statements
- `methods[]` - Method descriptions
- `protocols[]` - Documented procedures
- `evidence[]` - Check for repository links, data access statements
- `implicit_methods[]` - Undocumented procedures (transparency gaps)

**Assessment Dimensions:**

1. **Design statement:** Is the research design explicitly stated?
2. **Methods documentation:** Are methods sufficiently detailed for evaluation?
3. **Sampling/coverage:** Are sampling decisions explained and justified?
4. **Analytical decisions:** Are analytical choices made explicit?
5. **Data accessibility:** Are data and materials accessible (or restrictions justified)?
6. **Limitations:** Are limitations acknowledged?

**Apply Approach-Specific Anchors:**

#### For DEDUCTIVE Research (Hypothesis-Testing)

| Score | Band | Criteria |
|-------|------|----------|
| 80-100 | Excellent | Pre-registered study design (or convincing explanation for absence); comprehensive methods with protocols; data and code publicly available with persistent identifiers; all materials accessible; explicit limitations |
| 60-79 | Good | Clear research design and hypothesis specification; detailed methods; data availability stated (even if embargoed); code/workflow documented; major limitations acknowledged |
| 40-59 | Moderate | Research design stated (may lack detail); methods described (gaps present); data availability mentioned (may be vague); some protocol documentation; limitations present |
| 20-39 | Low | Implicit research design; incomplete methods; data availability unclear; minimal protocol documentation; limitations absent or superficial |
| 0-19 | Minimal | No clear research design; vague or absent methods; no data/code sharing; no protocols; no limitations |

#### For INDUCTIVE Research (Exploratory, Pattern-Finding)

| Score | Band | Criteria |
|-------|------|----------|
| 80-100 | Excellent | Clear documentation of exploratory goals; comprehensive data collection and sampling procedures; analysis workflow documented; data archived with documentation; explicit scope constraints. *Note: Pre-registration not expected* |
| 60-79 | Good | Research goals clearly stated; data collection documented; analysis approach described; data accessible; limitations acknowledged |
| 40-59 | Moderate | Research goals present; data collection described (gaps); analysis approach mentioned; data availability partially addressed; some limitations |
| 20-39 | Low | Vague research goals; incomplete data collection documentation; analysis approach unclear; data availability not addressed; minimal limitations |
| 0-19 | Minimal | No clear research goals; data collection not documented; analysis opaque; no data sharing; no limitations |

#### For ABDUCTIVE Research (Inference to Best Explanation)

| Score | Band | Criteria |
|-------|------|----------|
| 80-100 | Excellent | Theoretical framework explicitly stated; alternative explanations documented; evidence selection criteria transparent; reasoning traceable; data/sources accessible; inference scope clearly bounded |
| 60-79 | Good | Framework stated; some alternatives considered; evidence criteria mentioned; reasoning documented; sources accessible |
| 40-59 | Moderate | Framework implicit or partial; limited alternatives; evidence criteria unclear; reasoning partially documented; some source access |
| 20-39 | Low | Vague framework; no alternatives; evidence selection opaque; reasoning not documented; source access unclear |
| 0-19 | Minimal | No framework; no alternatives; arbitrary evidence; reasoning not traceable; no source access |

#### For METHODOLOGICAL Papers

| Score | Band | Criteria |
|-------|------|----------|
| 80-100 | Excellent | Software/method architecture documented; design decisions explained with rationale; code publicly available (open source); validation approach explicit; dependencies documented |
| 60-79 | Good | Architecture documented; design decisions stated; code available; validation described; major dependencies noted |
| 40-59 | Moderate | Architecture partially documented; some design rationale; code availability unclear; validation mentioned; dependencies partially listed |
| 20-39 | Low | Architecture vague; minimal design rationale; code not shared; validation unclear; dependencies unclear |
| 0-19 | Minimal | No architecture documentation; no design rationale; no code; no validation; no dependencies |

**Evidence Collection:**

Document specific evidence from extraction.json:
- Quote 2-3 exemplary methods/protocols (well/poorly documented)
- Note any implicit_methods flagged (transparency gaps)
- Reference any data access statements in evidence[]
- Note any limitations or scope statements

**Score Assignment:**

```yaml
transparency:
  score: [0-100]
  band: "[minimal|low|moderate|good|excellent]"
  approach_anchors_used: "[deductive|inductive|abductive|methodological]"
  evidence_citations:
    - "M001: '[quote]' - [assessment]"
    - "P001: '[quote]' - [assessment]"
    - "IM_M001: '[quote]' - [assessment - indicates gap]"
    - "E001: '[data access statement]' - [assessment]"
  strengths:
    - "[Specific strength 1]"
    - "[Specific strength 2]"
  weaknesses:
    - "[Specific weakness 1]"
  rationale: "[2-3 sentence justification referencing anchor criteria]"
```

---

### STEP 4: Cluster Synthesis

**Synthesise findings across both signals:**

1. **Pattern identification:** What do both signals tell us about foundational clarity?
2. **Consistency check:** Are Comprehensibility and Transparency scores consistent? (Both high, both low, or divergent?)
3. **Implications for other signals:** What do these scores suggest for subsequent cluster assessments?

**Cluster-Level Assessment:**

```yaml
cluster_synthesis:
  overall_foundational_clarity: "[strong|adequate|weak]"
  pattern_summary: "[1-2 sentences describing overall clarity pattern]"
  consistency: "[scores consistent|scores divergent - explain]"
  implications_for_assessment:
    - "[Implication 1 for subsequent signals]"
    - "[Implication 2]"
```

**Cluster Rating Logic:**

- **Strong:** Both signals ≥70, no major gaps identified
- **Adequate:** Both signals ≥50, or one signal ≥70 with other ≥40
- **Weak:** Either signal <40, or both signals <50

---

### STEP 5: Generate cluster-1-foundational-clarity.md

**Output file:** `assessment/cluster-1-foundational-clarity.md`

**Use this template:**

```markdown
# Cluster 1: Foundational Clarity Assessment

**Paper:** {paper-slug}
**Assessment Date:** {date}
**Assessor Version:** v1.0

**Quality State:** {from track-a-quality.md}
**Research Approach:** {from classification.json}
**Paper Type:** {from classification.json}

---

## Signal Scores Summary

| Signal | Score | Band | Approach Anchors |
|--------|-------|------|------------------|
| Comprehensibility | {score} | {band} | {approach} |
| Transparency | {score} | {band} | {approach} |

**Cluster Rating:** {strong|adequate|weak}

---

## Signal 1: Comprehensibility

**Score:** {score}/100 ({band})

**Approach anchors applied:** {deductive|inductive|abductive|methodological}

### Assessment

{2-3 paragraphs assessing comprehensibility against approach-specific criteria}

### Evidence

**Strengths:**
- {strength 1 with citation}
- {strength 2 with citation}

**Weaknesses:**
- {weakness 1 with citation}

### Scoring Rationale

{2-3 sentences explaining why this score was assigned, referencing specific anchor criteria}

---

## Signal 2: Transparency

**Score:** {score}/100 ({band})

**Approach anchors applied:** {deductive|inductive|abductive|methodological}

### Assessment

{2-3 paragraphs assessing transparency against approach-specific criteria}

### Evidence

**Strengths:**
- {strength 1 with citation}
- {strength 2 with citation}

**Weaknesses:**
- {weakness 1 with citation}

### Scoring Rationale

{2-3 sentences explaining why this score was assigned, referencing specific anchor criteria}

---

## Cluster Synthesis

**Overall Foundational Clarity:** {strong|adequate|weak}

{1-2 paragraphs synthesising findings across both signals}

### Pattern Summary

{What do both signals tell us about the paper's foundational clarity?}

### Implications for Subsequent Assessment

{How do these findings affect assessment of other clusters?}

- **For Cluster 2 (Evidential Strength):** {implication}
- **For Cluster 3 (Reproducibility & Scope):** {implication}

---

## Structured Output

```yaml
cluster_1_foundational_clarity:
  paper_slug: "{slug}"
  assessment_date: "{date}"
  quality_state: "{state}"
  research_approach: "{approach}"

  comprehensibility:
    score: {0-100}
    band: "{band}"
    strengths:
      - "{strength}"
    weaknesses:
      - "{weakness}"
    rationale: "{rationale}"

  transparency:
    score: {0-100}
    band: "{band}"
    strengths:
      - "{strength}"
    weaknesses:
      - "{weakness}"
    rationale: "{rationale}"

  cluster_synthesis:
    overall_rating: "{strong|adequate|weak}"
    pattern_summary: "{summary}"
    consistency_check: "{consistent|divergent}"
    implications:
      cluster_2: "{implication}"
      cluster_3: "{implication}"
```
```

---

## Quality State Adjustments

### If Quality State = HIGH

- Use precise scores (±5 point precision)
- Apply full anchor criteria
- Standard report format

### If Quality State = MODERATE

- Use 20-point score bands (e.g., 60-80 instead of 72)
- Note caveats prominently
- Add caveat header to report:

```markdown
> ⚠️ **CAVEATED ASSESSMENT:** This assessment has reduced precision due to [extraction gaps | classification uncertainty | other caveat from Track A]. Scores are reported as 20-point bands.
```

### If Quality State = LOW

- DO NOT proceed with cluster assessment
- Track A should have aborted assessment
- If you reach this prompt with LOW quality, STOP and report error

---

## Self-Validation Checklist

Before finalising cluster-1-foundational-clarity.md, verify:

- [ ] Classification.json read and approach identified
- [ ] Track-a-quality.md read and quality state confirmed
- [ ] Correct approach-specific anchors selected for BOTH signals
- [ ] Comprehensibility score assigned with evidence citations
- [ ] Transparency score assigned with evidence citations
- [ ] Both scores justified with reference to anchor criteria
- [ ] Evidence from extraction.json cited (claims, methods, protocols, implicit items)
- [ ] Cluster synthesis completed with rating
- [ ] Implications for subsequent clusters noted
- [ ] Structured YAML output included
- [ ] Quality state adjustments applied if MODERATE
- [ ] File written to assessment/cluster-1-foundational-clarity.md

---

## Common Errors to Avoid

**❌ Using wrong anchors for approach**
- Deductive papers need hypothesis clarity, not pattern descriptions
- Inductive papers need workflow transparency, not pre-registration

**✅ Always check classification.json for approach before selecting anchors**

---

**❌ Scoring based on absolute criteria**
- "No pre-registration" is not a transparency failure for inductive research
- "No hypothesis specification" is not a comprehensibility failure for inductive research

**✅ Apply approach-appropriate expectations**

---

**❌ Vague evidence citations**
- "Methods were well documented" (no citation)

**✅ Specific citations from extraction.json**
- "M003: 'Systematic field walking at 20m transect intervals' - clear, bounded method description"

---

**❌ Scores without anchor justification**
- "Score: 75" (no explanation)

**✅ Justify by referencing specific anchor band criteria**
- "Score: 75 (Good for inductive). Research goals clearly stated (60-79 criterion), data collection documented (60-79), but analysis workflow lacks detail (would need for 80-100)."

---

## References

**Signal definitions with anchors:**
→ `.claude/skills/research-assessor/references/credibility/signal-definitions-hass.md`

**Framework selection by approach:**
→ `.claude/skills/research-assessor/references/credibility/assessment-frameworks.md`

**Quality gating criteria:**
→ `.claude/skills/research-assessor/references/credibility/track-a-quality-criteria.md`
