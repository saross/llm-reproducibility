# Cluster 2: Evidential Strength Assessment

**Version:** v1.0
**Last Updated:** 2025-11-29
**Workflow Stage:** Pass 9 - Cluster 2 of 3
**Pillar:** Credibility
**Signals Assessed:** Plausibility, Validity, Robustness, Generalisability

---

## Three Pillars Context

This cluster assesses the **Credibility pillar** — the core assessment pillar:

| Pillar | Core Question | Signals | This Cluster |
|--------|---------------|---------|--------------|
| Transparency | Is the work documented and artefacts published? | Comprehensibility, Transparency | Cluster 1 |
| **Credibility** | How much faith can we put in the results? | Plausibility, Validity, Robustness, Generalisability | ✅ |
| Reproducibility | Can computational aspects be re-executed? | Reproducibility | Cluster 3 |

**See:** `references/credibility/assessment-pillars.md` for the full framework

---

## Your Task

Assess the four credibility signals that address the core question: **How much faith can we put in the results?**

- **Plausibility** — Fit with domain knowledge and theory
- **Validity** — Evidence sufficiency and appropriateness
- **Robustness** — Sensitivity to analytical choices
- **Generalisability** — Appropriate scope and limitations

**Inputs:**
- `extraction.json` from Pass 0-7 (complete extraction)
- `classification.json` from Pass 8 (research approach classification)
- `track-a-quality.md` from Track A (quality state)

**Your responsibility:** Score all four signals using approach-specific anchors, cite evidence from extraction, provide rationale

**Output:** NEW file `assessment/cluster-2-evidential-strength.md`

---

## 🚨 CRITICAL: Approach-Specific Scoring

**Different research approaches require different credibility criteria.** A score of 75 on Validity means different things for:

- **Deductive research:** Evidence directly addresses hypothesis; sample adequate; confounds controlled
- **Inductive research:** Data sufficient for pattern claims; sampling systematic; coverage adequate
- **Abductive research:** Evidence supports explanation; alternatives evaluated; gaps acknowledged

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
  "paper_type": "[empirical|methodological|theoretical|meta_research]"
}
```

**Record:**
- Primary approach (determines which anchor set to use)
- Paper type (affects expectations)
- Classification confidence (affects scoring precision)

**Read from track-a-quality.md:**
- Quality state (HIGH/MODERATE/LOW)
- If MODERATE: Note caveats that apply to this assessment

---

### STEP 2: Assess Plausibility (Signal 3)

**Core Question:** Does the claim align with established prior evidence and theory? Are interpretations consistent with domain knowledge?

**Read from extraction.json:**
- `claims[]` — Main claims to assess for theoretical grounding
- `evidence[]` — Evidence supporting or contradicting claims
- `implicit_arguments[]` — Unstated assumptions that affect plausibility

**Assessment Dimensions:**

1. **Theoretical grounding:** Are claims/hypotheses grounded in established theory?
2. **Domain consistency:** Are interpretations consistent with regional/chronological frameworks?
3. **Anomaly handling:** Are anomalies acknowledged and explained (not ignored)?
4. **Auxiliary assumptions:** Does the interpretation require implausible auxiliary assumptions?

**Apply Approach-Specific Anchors:**

#### For DEDUCTIVE Research (Hypothesis-Testing)

| Score | Band | Criteria |
|-------|------|----------|
| 80-100 | Excellent | Hypotheses grounded in established theory; predictions consistent with domain knowledge; anomalous results acknowledged and explained; theoretical framework coherent; no implausible auxiliary assumptions |
| 60-79 | Good | Hypotheses theoretically motivated; generally consistent with domain knowledge; major anomalies addressed; framework coherent; minimal implausible assumptions |
| 40-59 | Moderate | Hypotheses have theoretical basis (may be tenuous); partially consistent with domain knowledge; some anomalies acknowledged; framework present but may have gaps |
| 20-39 | Low | Weak theoretical grounding; inconsistencies with domain knowledge not addressed; anomalies ignored; framework unclear; multiple questionable assumptions |
| 0-19 | Minimal | No theoretical grounding; contradicts established knowledge; anomalies ignored; no coherent framework; implausible assumptions required |

#### For INDUCTIVE Research (Exploratory, Pattern-Finding)

| Score | Band | Criteria |
|-------|------|----------|
| 80-100 | Excellent | Observed patterns consistent with known regional/chronological frameworks; typologies follow established conventions; anomalies acknowledged and contextualised; interpretations grounded in comparative data |
| 60-79 | Good | Patterns generally consistent with frameworks; classifications reasonable; major anomalies addressed; interpretations have comparative basis |
| 40-59 | Moderate | Patterns partially consistent (some tensions); classifications defensible; some anomalies acknowledged; some comparative grounding |
| 20-39 | Low | Patterns inconsistent with frameworks; classifications questionable; anomalies not addressed; limited comparative grounding |
| 0-19 | Minimal | Patterns contradict established knowledge; classifications arbitrary; anomalies ignored; no comparative basis |

#### For ABDUCTIVE Research (Inference to Best Explanation)

| Score | Band | Criteria |
|-------|------|----------|
| 80-100 | Excellent | Proposed explanation coherent with domain knowledge; alternative explanations properly evaluated; inference grounded in established theory; framework robust; no ad hoc assumptions |
| 60-79 | Good | Explanation generally coherent; alternatives considered; theoretical grounding present; framework defensible; minimal ad hoc assumptions |
| 40-59 | Moderate | Explanation partially coherent; limited alternatives considered; some theoretical grounding; framework has gaps; some ad hoc assumptions |
| 20-39 | Low | Explanation weakly coherent; alternatives not considered; limited grounding; framework unclear; multiple ad hoc assumptions |
| 0-19 | Minimal | Explanation incoherent; no alternatives; no theoretical grounding; no framework; implausible assumptions required |

**Evidence to Cite:**
- Specific claims and their theoretical basis
- Evidence items supporting/contradicting established frameworks
- Implicit arguments revealing unstated assumptions
- Research designs articulating theoretical rationale

---

### STEP 3: Assess Validity (Signal 4)

**Core Question:** Are methods appropriate for the research question and claims adequately supported by evidence?

**Read from extraction.json:**
- `evidence[]` — Evidence base for claims
- `claims[]` — Claims requiring evidential support
- `methods[]` — Methods used to gather evidence
- `research_designs[]` — Design choices affecting validity

**Assessment Dimensions:**

1. **Evidence sufficiency:** Is evidence sufficient and representative for claims made?
2. **Method appropriateness:** Are methods appropriate for the research question?
3. **Alternative explanations:** Are alternative interpretations considered?
4. **Scope matching:** Is scope of claims matched to scope of evidence?
5. **Limitations acknowledgement:** Are gaps and limitations acknowledged?

**Apply Approach-Specific Anchors:**

#### For DEDUCTIVE Research (Hypothesis-Testing)

| Score | Band | Criteria |
|-------|------|----------|
| 80-100 | Excellent | Evidence directly addresses hypothesis; sample adequate; methods appropriate for testing; alternative hypotheses explicitly tested; confounds controlled; limitations stated |
| 60-79 | Good | Evidence addresses hypothesis; sample adequate; methods appropriate; some alternatives considered; major confounds addressed; limitations acknowledged |
| 40-59 | Moderate | Evidence partially addresses hypothesis; sample present but limited; methods defensible; limited alternatives; some confounds addressed; some limitations |
| 20-39 | Low | Evidence weakly supports hypothesis; sample insufficient; methods questionable; alternatives not considered; confounds not addressed; minimal limitations |
| 0-19 | Minimal | Evidence doesn't address hypothesis; sample inadequate; methods inappropriate; no alternatives; confounds ignored; no limitations |

#### For INDUCTIVE Research (Exploratory, Pattern-Finding)

| Score | Band | Criteria |
|-------|------|----------|
| 80-100 | Excellent | Data sufficient and representative for pattern claims; sampling systematic and appropriate; coverage adequate; alternative interpretations considered; sampling limitations acknowledged; claims scoped to evidence |
| 60-79 | Good | Data sufficient for main patterns; sampling systematic; coverage adequate; some alternatives considered; limitations acknowledged; claims generally scoped |
| 40-59 | Moderate | Data present but limited; sampling partially systematic; coverage partial; limited alternatives; some limitations; some claims may exceed evidence |
| 20-39 | Low | Data insufficient for patterns claimed; sampling unsystematic; coverage inadequate; no alternatives; minimal limitations; claims exceed evidence |
| 0-19 | Minimal | Data grossly insufficient; no systematic sampling; minimal coverage; no alternatives; no limitations; major evidence-claim mismatch |

#### For ABDUCTIVE Research (Inference to Best Explanation)

| Score | Band | Criteria |
|-------|------|----------|
| 80-100 | Excellent | Evidence supports proposed explanation; alternative explanations rigorously evaluated; inference well-grounded; rivals ruled out or ranked; gaps acknowledged; inference scope matched to evidence |
| 60-79 | Good | Evidence supports explanation; alternatives considered; inference grounded; some rivals addressed; gaps acknowledged; scope appropriate |
| 40-59 | Moderate | Evidence partially supports explanation; limited alternatives; inference has grounding; few rivals addressed; some gaps noted; scope may exceed evidence |
| 20-39 | Low | Evidence weakly supports explanation; alternatives not considered; inference poorly grounded; rivals ignored; gaps not acknowledged; inference exceeds evidence |
| 0-19 | Minimal | Evidence doesn't support explanation; no alternatives; inference ungrounded; rivals not addressed; gaps ignored; major inference-evidence mismatch |

**Evidence to Cite:**
- Evidence items and their relationship to claims
- Methods and their appropriateness
- Research design choices affecting validity
- Extraction notes on evidence gaps

---

### STEP 4: Assess Robustness (Signal 5)

**Core Question:** Would results hold under different reasonable analytical approaches? Are conclusions sensitive to specific methodological choices?

**Read from extraction.json:**
- `methods[]` — Analytical methods used
- `protocols[]` — Specific procedures applied
- `claims[]` — Claims to assess for sensitivity
- `extraction_notes` — Notes on analytical variations

**Assessment Dimensions:**

1. **Sensitivity analysis:** Are results tested under different analytical approaches?
2. **Choice dependency:** How dependent are results on specific choices?
3. **Triangulation:** Are multiple methods/indicators used for convergence?
4. **Documentation:** Are manual/subjective steps documented and justified?

**Apply Approach-Specific Anchors:**

#### For DEDUCTIVE Research (Hypothesis-Testing)

| Score | Band | Criteria |
|-------|------|----------|
| 80-100 | Excellent | Sensitivity analyses performed; results robust across analytical choices; alternative approaches tested; assumptions validated; dependencies documented; robustness checks reported |
| 60-79 | Good | Some sensitivity analysis; results appear robust; some alternatives tested; assumptions mostly tested; dependencies documented; some robustness evidence |
| 40-59 | Moderate | Limited sensitivity analysis; robustness unclear; few alternatives tested; assumptions stated not tested; some dependencies noted; minimal robustness evidence |
| 20-39 | Low | No sensitivity analysis; robustness unknown; single approach only; assumptions untested; dependencies not documented; no robustness evidence |
| 0-19 | Minimal | No sensitivity analysis; results likely fragile; arbitrary choices; assumptions violated; dependencies hidden; evidence of non-robustness |

#### For INDUCTIVE Research (Exploratory, Pattern-Finding)

| Score | Band | Criteria |
|-------|------|----------|
| 80-100 | Excellent | Pattern identification tested with multiple methods; results consistent across classification schemes; inter-observer reliability assessed; alternatives explored; sampling sensitivity documented; convergent evidence from multiple indicators |
| 60-79 | Good | Some methodological triangulation; main patterns robust to variations; some reliability assessment; some alternatives; sampling sensitivity considered; some convergent evidence |
| 40-59 | Moderate | Limited triangulation; pattern robustness unclear; minimal reliability assessment; few alternatives; sampling sensitivity mentioned; limited convergent evidence |
| 20-39 | Low | No triangulation; single method only; no reliability assessment; no alternatives; sampling sensitivity ignored; no convergent evidence |
| 0-19 | Minimal | Arbitrary methods; results likely artefactual; no reliability consideration; method-dependent conclusions; sampling biases ignored; contradictory evidence ignored |

#### For ABDUCTIVE Research (Inference to Best Explanation)

| Score | Band | Criteria |
|-------|------|----------|
| 80-100 | Excellent | Alternative explanations rigorously tested; inference robust across frameworks; evidence triangulation; theoretical assumptions tested; inference stability assessed; framework sensitivity documented |
| 60-79 | Good | Alternatives considered; inference appears robust; some triangulation; assumptions considered; some stability evidence; framework sensitivity noted |
| 40-59 | Moderate | Limited alternatives; robustness unclear; minimal triangulation; assumptions stated; stability unclear; framework sensitivity minimal |
| 20-39 | Low | No alternatives; single framework only; no triangulation; assumptions untested; stability unknown; framework dependency hidden |
| 0-19 | Minimal | No alternative explanations; framework-dependent conclusions; evidence cherry-picking; assumptions violated; inference unstable; critical dependencies ignored |

**Evidence to Cite:**
- Methods showing analytical variation
- Protocols with sensitivity checks
- Evidence of triangulation
- Notes on robustness testing

---

### STEP 5: Assess Generalisability (Signal 7)

**Core Question:** Can findings transfer to other contexts? Are claims carefully constrained by place, time, and context?

**Read from extraction.json:**
- `claims[]` — Claims to assess for scope
- `research_designs[]` — Design statements on scope
- `extraction_notes` — Notes on limitations and scope

**Assessment Dimensions:**

1. **Scope boundaries:** Are claims bounded by geography, chronology, context?
2. **Limitation acknowledgement:** Are limitations explicitly stated?
3. **Evidence matching:** Is scope of generalisation matched to evidence?
4. **Transfer conditions:** Are conditions for transfer to other contexts specified?

**Apply Approach-Specific Anchors:**

#### For DEDUCTIVE Research (Hypothesis-Testing)

| Score | Band | Criteria |
|-------|------|----------|
| 80-100 | Excellent | Scope of hypothesis clearly bounded; limitations to external validity stated; population, context, temporal bounds clear; extrapolations qualified; threats to generalisation discussed; transfer conditions specified |
| 60-79 | Good | Hypothesis scope stated; main limitations acknowledged; bounds mostly clear; extrapolations qualified; some generalisability discussion; transfer considerations present |
| 40-59 | Moderate | Scope present but vague; some limitations stated; bounds partially clear; some qualification; limited generalisability discussion; minimal transfer consideration |
| 20-39 | Low | Vague scope; minimal limitations; bounds unclear; unqualified claims; no generalisability discussion; no transfer consideration |
| 0-19 | Minimal | No scope boundaries; no limitations; unbounded claims; universal claims from limited context; no generalisability consideration |

#### For INDUCTIVE Research (Exploratory, Pattern-Finding)

| Score | Band | Criteria |
|-------|------|----------|
| 80-100 | Excellent | Pattern claims explicitly bounded (geographic, temporal, cultural); sampling limitations thoroughly discussed; scope matched to coverage; extrapolations carefully qualified; regional/contextual constraints clear; limitation statements prominent |
| 60-79 | Good | Pattern claims bounded; sampling limitations acknowledged; scope generally matched; extrapolations qualified; constraints stated; limitations present |
| 40-59 | Moderate | Claims partially bounded; some sampling limitations noted; scope partially matched; some qualification; some constraints; some limitations |
| 20-39 | Low | Claims weakly bounded; sampling limitations minimal; scope exceeds coverage; limited qualification; vague constraints; minimal limitations |
| 0-19 | Minimal | Claims unbounded; no sampling limitations; scope greatly exceeds coverage; no qualification; no constraints; no limitations |

#### For ABDUCTIVE Research (Inference to Best Explanation)

| Score | Band | Criteria |
|-------|------|----------|
| 80-100 | Excellent | Explanatory scope clearly bounded; contextual constraints explicit; transfer conditions specified; limitations of inference acknowledged; domain of applicability clear; alternative contexts discussed |
| 60-79 | Good | Explanation scope stated; constraints present; transfer considerations mentioned; inference limitations acknowledged; applicability domain stated; some context discussion |
| 40-59 | Moderate | Scope partially bounded; some constraints; limited transfer discussion; some inference limitations; domain partially clear; minimal context discussion |
| 20-39 | Low | Vague scope; minimal constraints; no transfer discussion; inference limitations minimal; domain unclear; no context discussion |
| 0-19 | Minimal | Unbounded explanatory claims; no constraints; universal claims from single context; no inference limitations; no domain specification |

**Evidence to Cite:**
- Claims with scope statements
- Research design limitations
- Evidence items with geographic/temporal context
- Extraction notes on boundaries

---

### STEP 6: Synthesise Cluster Assessment

After scoring all four signals:

1. **Calculate overall pattern:**
   - Are scores consistent across signals?
   - Do any signals diverge significantly?
   - What's the overall credibility profile?

2. **Identify key patterns:**
   - Strongest credibility aspects
   - Weakest credibility aspects
   - Approach-specific considerations

3. **Note implications for Cluster 3:**
   - How do these findings affect reproducibility assessment?
   - Does evidence quality affect reproducibility expectations?

---

### STEP 7: Generate Output

**File location:** `assessment/cluster-2-evidential-strength.md`

**Output format:**

```markdown
# Cluster 2: Evidential Strength Assessment

**Paper:** {paper-slug}
**Assessment Date:** {date}
**Assessor Version:** v1.0

**Quality State:** {HIGH|MODERATE}
**Research Approach:** {approach} (confidence: {confidence})
**Paper Type:** {type}

---

## Signal Scores Summary

| Signal | Score | Band | Approach Anchors |
|--------|-------|------|------------------|
| Plausibility | {score} | {band} | {approach} |
| Validity | {score} | {band} | {approach} |
| Robustness | {score} | {band} | {approach} |
| Generalisability | {score} | {band} | {approach} |

**Cluster Rating:** {Strong|Adequate|Weak}

---

## Signal 3: Plausibility

**Score:** {score}/100 ({band})

**Approach anchors applied:** {approach}

### Assessment

{Detailed assessment of plausibility...}

### Evidence

**Strengths:**
- {citation}: {quote or reference}

**Weaknesses:**
- {citation}: {issue}

### Scoring Rationale

{Why this score, referencing specific anchor criteria for this approach}

---

## Signal 4: Validity

**Score:** {score}/100 ({band})

**Approach anchors applied:** {approach}

### Assessment

{Detailed assessment of validity...}

### Evidence

**Strengths:**
- {citation}: {quote or reference}

**Weaknesses:**
- {citation}: {issue}

### Scoring Rationale

{Why this score, referencing specific anchor criteria for this approach}

---

## Signal 5: Robustness

**Score:** {score}/100 ({band})

**Approach anchors applied:** {approach}

### Assessment

{Detailed assessment of robustness...}

### Evidence

**Strengths:**
- {citation}: {quote or reference}

**Weaknesses:**
- {citation}: {issue}

### Scoring Rationale

{Why this score, referencing specific anchor criteria for this approach}

---

## Signal 7: Generalisability

**Score:** {score}/100 ({band})

**Approach anchors applied:** {approach}

### Assessment

{Detailed assessment of generalisability...}

### Evidence

**Strengths:**
- {citation}: {quote or reference}

**Weaknesses:**
- {citation}: {issue}

### Scoring Rationale

{Why this score, referencing specific anchor criteria for this approach}

---

## Cluster Synthesis

**Overall Evidential Strength:** {Strong|Adequate|Weak}

{2-3 paragraph synthesis of credibility findings}

### Pattern Summary

{What patterns emerge across the four signals?}

### Implications for Cluster 3

- **For Reproducibility:** {How do these findings affect reproducibility assessment?}

---

## Structured Output

```yaml
cluster_2_evidential_strength:
  paper_slug: "{slug}"
  assessment_date: "{date}"
  quality_state: "{state}"
  research_approach: "{approach}"

  plausibility:
    score: {0-100}
    band: "{band}"
    strengths:
      - "{strength}"
    weaknesses:
      - "{weakness}"
    rationale: "{rationale}"

  validity:
    score: {0-100}
    band: "{band}"
    strengths:
      - "{strength}"
    weaknesses:
      - "{weakness}"
    rationale: "{rationale}"

  robustness:
    score: {0-100}
    band: "{band}"
    strengths:
      - "{strength}"
    weaknesses:
      - "{weakness}"
    rationale: "{rationale}"

  generalisability:
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

Before finalising cluster-2-evidential-strength.md, verify:

- [ ] Classification.json read and approach identified
- [ ] Track-a-quality.md read and quality state confirmed
- [ ] Correct approach-specific anchors selected for ALL FOUR signals
- [ ] Plausibility score assigned with evidence citations
- [ ] Validity score assigned with evidence citations
- [ ] Robustness score assigned with evidence citations
- [ ] Generalisability score assigned with evidence citations
- [ ] All scores justified with reference to anchor criteria
- [ ] Evidence from extraction.json cited (claims, evidence, methods, designs)
- [ ] Cluster synthesis completed with rating
- [ ] Implications for Cluster 3 noted
- [ ] Structured YAML output included
- [ ] Quality state adjustments applied if MODERATE
- [ ] File written to assessment/cluster-2-evidential-strength.md

---

## Common Errors to Avoid

**❌ Using wrong anchors for approach**
- Deductive papers need hypothesis testing criteria
- Inductive papers need pattern-finding criteria
- Abductive papers need inference-to-explanation criteria

**✅ Always check classification.json for approach before selecting anchors**

---

**❌ Conflating signals**
- Validity is about evidence sufficiency, not robustness
- Robustness is about analytical sensitivity, not validity
- Generalisability is about scope, not plausibility

**✅ Keep each signal focused on its specific question**

---

**❌ Vague evidence citations**
- "Methods were appropriate" (no citation)

**✅ Specific citations from extraction.json**
- "M003: 'Systematic field walking at 20m transect intervals' provides appropriate coverage for pattern claims"

---

**❌ Scores without anchor justification**
- "Score: 68" (no explanation)

**✅ Justify by referencing specific anchor band criteria**
- "Score: 68 (Good for inductive). Data sufficient for main patterns (60-79), sampling systematic (60-79), but coverage only partial for regional claims."

---

## References

**Signal definitions with anchors:**
→ `.claude/skills/research-assessor/references/credibility/signal-definitions-hass.md`

**Framework selection by approach:**
→ `.claude/skills/research-assessor/references/credibility/assessment-frameworks.md`

**Quality gating criteria:**
→ `.claude/skills/research-assessor/references/credibility/track-a-quality-criteria.md`

**Three pillars framework:**
→ `.claude/skills/research-assessor/references/credibility/assessment-pillars.md`
