# Cluster 3: Reproducibility Assessment

**Version:** v1.0
**Last Updated:** 2025-11-29
**Workflow Stage:** Pass 9 - Cluster 3 of 3
**Pillar:** Reproducibility
**Signals Assessed:** Reproducibility (single signal)

---

## Three Pillars Context

This cluster assesses the **Reproducibility pillar** — focused on re-executability:

| Pillar | Core Question | Signals | This Cluster |
|--------|---------------|---------|--------------|
| Transparency | Is the work documented and artefacts published? | Comprehensibility, Transparency | Cluster 1 |
| Credibility | How much faith can we put in the results? | Plausibility, Validity, Robustness, Generalisability | Cluster 2 |
| **Reproducibility** | Can computational aspects be re-executed? | Reproducibility | ✅ |

**See:** `references/credibility/assessment-pillars.md` for the full framework

---

## 🚨 CRITICAL: Understanding Reproducibility in HASS

**Reproducibility = Analytic or computational reproducibility, NOT beginning-to-end reproducibility or replication of fieldwork.**

| What We CAN Assess | What We CANNOT |
|--------------------|----------------|
| Statistical analyses | Re-excavating a site |
| Computational workflows | Re-conducting ethnographic fieldwork |
| Data transformations | Re-observing historical events |
| Machine learning model training | Re-collecting destroyed samples |
| GIS spatial analysis | Re-interviewing deceased informants |

**The question is:** Given the data and code, can someone else run the analysis and get the same results?

**NOT:** Can someone repeat the entire study from scratch?

---

## Your Task

Assess the Reproducibility signal — whether computational/analytical aspects of the research can be independently re-executed.

**Two pathways depending on paper content:**

| Paper Has | Pathway | Signal |
|-----------|---------|--------|
| Computational components | Standard Reproducibility | Full anchors |
| No computational components | Methodological Transparency variant | Experimental anchors |

**Inputs:**
- `extraction.json` from Pass 0-7 (complete extraction)
- `classification.json` from Pass 8 (research approach classification)
- `track-a-quality.md` from Track A (quality state)

**Your responsibility:** Determine pathway, score using appropriate anchors, complete Reproducibility Readiness Checklist

**Output:** NEW file `assessment/cluster-3-reproducibility.md`

---

## Assessment Workflow

### STEP 1: Determine Assessment Pathway

**Read from extraction.json:**
- `methods[]` — Look for computational/statistical methods
- `protocols[]` — Look for computational procedures
- `reproducibility_infrastructure.code_availability` — Is code mentioned?
- Paper type from `classification.json`

**Determine if paper has computational component:**

**YES - Has computational component if ANY of:**
- Statistical analyses (regression, ANOVA, PCA, clustering, etc.)
- Computational workflows (scripts, pipelines)
- Data transformations (ETL, cleaning, aggregation)
- Machine learning / AI models
- GIS / spatial analysis
- Quantitative modelling
- Code-based analysis (Python, R, SPSS syntax, Stata do-files)

**NO - Does NOT have computational component if:**
- Pure qualitative research (no quantitative analysis)
- Literature review / theoretical paper
- Software description without empirical validation
- Historiographic or archival research without quantitative component
- Ethnographic description without statistical analysis

**Record pathway:** `standard` or `methodological_transparency_variant`

---

### STEP 2A: Standard Reproducibility Assessment (Computational Papers)

**Core Question:** Can others reproduce the analytical outputs given the same inputs?

**Read from extraction.json:**

```
reproducibility_infrastructure:
├── code_availability
│   ├── statement_present: true|false
│   ├── repositories: [{name, url, access_conditions}]
│   └── machine_actionability: {rating, rationale}
├── data_availability
│   ├── statement_present: true|false
│   ├── repositories: [{name, url, access_conditions}]
│   └── machine_actionability: {rating, rationale}
├── persistent_identifiers
│   └── software_pids: [{software_name, repository, doi, url}]
├── preregistration
│   └── preregistered: true|false
└── fair_assessment (if populated)
    └── total_fair_score, fair_percentage
```

**Also read:**
- `methods[]` — Computational methods used
- `protocols[]` — Implementation details

**Assessment Dimensions:**

1. **Input availability:** Are data/inputs publicly accessible?
2. **Code availability:** Is analysis code shared and documented?
3. **Environment specification:** Are computational dependencies documented?
4. **Workflow documentation:** Can analytical steps be traced and rerun?
5. **Output documentation:** Are expected outputs documented for verification?

**Tool-Based Assessment:**

| Tool Type | Examples | Impact on Score |
|-----------|----------|-----------------|
| **Open scriptable** | Python, R, Julia, bash | Ideal — no demerit |
| **Proprietary scriptable** | SPSS syntax, Stata do-files, SAS | Minor demerit — reproducible if software available |
| **GUI-based without documentation** | Excel point-and-click, manual processes | Significant demerit — hard to reproduce |
| **GUI-based with documentation** | Excel with step-by-step guide | Moderate demerit — reproducible but labour-intensive |

**Apply Approach-Specific Anchors:**

#### For DEDUCTIVE Research (Hypothesis-Testing)

| Score | Band | Criteria |
|-------|------|----------|
| 80-100 | Excellent | Complete data publicly available with PIDs; all code shared with documentation; environment specified; workflow fully documented and executable; outputs reproducible; FAIR principles met |
| 60-79 | Good | Data available (minor gaps); code shared with basic documentation; workflow documented; most outputs reproducible; FAIR mostly met |
| 40-59 | Moderate | Data partially available; some code shared (may be incomplete); workflow partially documented; some outputs reproducible; partial FAIR |
| 20-39 | Low | Minimal data sharing; fragmentary or no code; workflow poorly documented; outputs difficult to reproduce; limited FAIR |
| 0-19 | Minimal | No data sharing; no code; no workflow documentation; outputs not reproducible; no FAIR compliance |

#### For INDUCTIVE Research (Exploratory, Pattern-Finding)

| Score | Band | Criteria |
|-------|------|----------|
| 80-100 | Excellent | Data archived with comprehensive documentation; analysis workflow documented (even if not automated); classification schemes explicit; raw observations accessible; metadata complete; FAIR/CARE met |
| 60-79 | Good | Data archived with documentation; workflow documented; procedures explicit; observations accessible; metadata adequate; FAIR/CARE mostly met |
| 40-59 | Moderate | Data partially archived; workflow partially documented; procedures stated; some observations accessible; metadata present; partial FAIR/CARE |
| 20-39 | Low | Minimal archiving; workflow poorly documented; procedures vague; limited access; minimal metadata; limited FAIR/CARE |
| 0-19 | Minimal | No archiving; no workflow documentation; procedures opaque; no access; no metadata; no FAIR/CARE |

#### For ABDUCTIVE Research (Inference to Best Explanation)

| Score | Band | Criteria |
|-------|------|----------|
| 80-100 | Excellent | Evidence sources fully documented and accessible; reasoning process traceable; framework specified; interpretive decisions explained; source materials archived |
| 60-79 | Good | Sources documented and mostly accessible; reasoning traceable; framework specified; decisions explained; materials mostly archived |
| 40-59 | Moderate | Sources partially documented; reasoning partially traceable; framework present; some decisions explained; partial archiving |
| 20-39 | Low | Minimal documentation; reasoning difficult to trace; framework vague; decisions unexplained; minimal archiving |
| 0-19 | Minimal | No documentation; reasoning not traceable; no framework; decisions hidden; no archiving |

**Proceed to STEP 3.**

---

### STEP 2B: Methodological Transparency Variant (Non-Computational Papers)

**⚠️ EXPERIMENTAL:** This variant uses alternate anchors. Flag output as `experimental: true`.

**Core Question:** Are methods described clearly enough that someone could apply the same approach to different data/contexts?

**Focus Areas:**
- Procedure documentation completeness
- Decision criteria explicitness
- Sampling/selection transparency
- Analytical reasoning traceability

**Apply Experimental Anchors:**

| Score | Band | Methodological Transparency Criteria |
|-------|------|--------------------------------------|
| 80-100 | Excellent | Methods fully documented; all decision points explicit; procedures could be operationalised by another researcher |
| 60-79 | Good | Most methods clear; some tacit knowledge required; generally reproducible approach |
| 40-59 | Moderate | Partial documentation; significant gaps; experienced researcher could approximate |
| 20-39 | Low | Sparse documentation; approach unclear; reproduction would require author consultation |
| 0-19 | Minimal | Methods opaque; cannot determine how conclusions were reached |

**Evidence to Cite:**
- Methods documentation quality
- Protocol specificity
- Decision criteria explicitness
- Gaps in procedural documentation

**Proceed to STEP 3.**

---

### STEP 3: Complete Reproducibility Readiness Checklist

**For ALL papers (both pathways), complete this checklist:**

```yaml
reproducibility_readiness:
  # Pathway determination
  applies: true|false
  pathway: "standard|methodological_transparency_variant"
  if_not_applicable_reason: ""  # Only if applies=false

  # Input availability
  inputs_available:
    status: "yes|partial|no"
    details: "{description of data/input availability}"

  # Code availability
  code_available:
    status: "yes|partial|no|not_applicable"
    tool_type: "open_scriptable|proprietary_scriptable|gui_based|mixed|none"
    details: "{description of code/workflow availability}"

  # Environment specification
  environment_specified:
    status: "yes|partial|no|not_applicable"
    details: "{description of computational environment documentation}"

  # Output documentation
  outputs_documented:
    status: "yes|partial|no"
    details: "{description of expected outputs for verification}"

  # Overall feasibility
  execution_feasibility: "ready|needs_work|not_feasible"
  feasibility_rationale: "{explanation of feasibility assessment}"

  # Chronological context (metadata only - does not affect score)
  publication_year: {year}
  adoption_context: "innovator|early_adopter|early_majority|mainstream"
```

**Adoption Context Guidelines:**

| Era | Stage | Description |
|-----|-------|-------------|
| Pre-2015 | innovator | Reproducibility practices rare; high scores exceptional |
| 2015-2020 | early_adopter | Growing awareness; code sharing emerging |
| 2020-2025 | early_majority | Data/code sharing increasingly expected; not yet mainstream |
| Post-2025 | mainstream | Reproducibility practices becoming standard |

**Note:** Adoption context is **metadata only** — scores are not adjusted for era. This enables cross-era comparison while providing interpretive context.

---

### STEP 4: Synthesise Assessment

1. **Record pathway used:** Standard or Methodological Transparency variant
2. **Calculate score using appropriate anchors**
3. **Complete Reproducibility Readiness Checklist**
4. **Note implications for future reproduction attempts**
5. **If experimental variant:** Flag output accordingly

---

### STEP 5: Generate Output

**File location:** `assessment/cluster-3-reproducibility.md`

**Output format:**

```markdown
# Cluster 3: Reproducibility Assessment

**Paper:** {paper-slug}
**Assessment Date:** {date}
**Assessor Version:** v1.0

**Quality State:** {HIGH|MODERATE}
**Research Approach:** {approach} (confidence: {confidence})
**Paper Type:** {type}
**Assessment Pathway:** {standard|methodological_transparency_variant}
{If variant: **⚠️ EXPERIMENTAL: Using Methodological Transparency alternate anchors**}

---

## Signal Score Summary

| Signal | Score | Band | Pathway |
|--------|-------|------|---------|
| Reproducibility | {score} | {band} | {pathway} |

**Cluster Rating:** {Strong|Adequate|Weak}

---

## Signal 6: Reproducibility

**Score:** {score}/100 ({band})

**Pathway:** {standard|methodological_transparency_variant}
**Approach anchors applied:** {approach}

### Assessment

{Detailed assessment of reproducibility...}

### Evidence

**From reproducibility_infrastructure:**
- Code availability: {status} — {details}
- Data availability: {status} — {details}
- Persistent identifiers: {details}
- FAIR score: {score if available}

**From methods/protocols:**
- {citation}: {relevant detail}

**Strengths:**
- {strength}

**Weaknesses:**
- {weakness}

### Tool Assessment

| Aspect | Status | Tool Type | Impact |
|--------|--------|-----------|--------|
| Primary analysis | {description} | {type} | {impact} |
| {Other tools} | ... | ... | ... |

### Scoring Rationale

{Why this score, referencing specific anchor criteria for this approach/pathway}

---

## Reproducibility Readiness Checklist

```yaml
reproducibility_readiness:
  applies: {true|false}
  pathway: "{standard|methodological_transparency_variant}"
  if_not_applicable_reason: "{reason if applies=false}"

  inputs_available:
    status: "{yes|partial|no}"
    details: "{details}"

  code_available:
    status: "{yes|partial|no|not_applicable}"
    tool_type: "{type}"
    details: "{details}"

  environment_specified:
    status: "{yes|partial|no|not_applicable}"
    details: "{details}"

  outputs_documented:
    status: "{yes|partial|no}"
    details: "{details}"

  execution_feasibility: "{ready|needs_work|not_feasible}"
  feasibility_rationale: "{rationale}"

  publication_year: {year}
  adoption_context: "{stage}"
```

---

## Cluster Synthesis

**Overall Reproducibility:** {Strong|Adequate|Weak}

{1-2 paragraph synthesis}

### Chronological Context

Publication year {year} places this paper in the **{stage}** era of reproducibility adoption. {Interpretation of score in context of era expectations.}

### Gateway Assessment

**Execution Feasibility:** {ready|needs_work|not_feasible}

{Assessment of whether this paper could be queued for actual reproduction attempt}

{If ready: What would be needed to attempt reproduction?}
{If needs_work: What gaps need to be addressed?}
{If not_feasible: Why is reproduction not possible?}

---

## Structured Output

```yaml
cluster_3_reproducibility:
  paper_slug: "{slug}"
  assessment_date: "{date}"
  quality_state: "{state}"
  research_approach: "{approach}"
  pathway: "{standard|methodological_transparency_variant}"
  experimental: {true|false}  # true if using variant anchors

  reproducibility:
    score: {0-100}
    band: "{band}"
    strengths:
      - "{strength}"
    weaknesses:
      - "{weakness}"
    rationale: "{rationale}"
    tool_assessment:
      primary_tool_type: "{type}"
      tool_impact: "{impact}"

  reproducibility_readiness:
    applies: {true|false}
    pathway: "{pathway}"
    inputs_available:
      status: "{status}"
      details: "{details}"
    code_available:
      status: "{status}"
      tool_type: "{type}"
      details: "{details}"
    environment_specified:
      status: "{status}"
      details: "{details}"
    outputs_documented:
      status: "{status}"
      details: "{details}"
    execution_feasibility: "{feasibility}"
    feasibility_rationale: "{rationale}"
    publication_year: {year}
    adoption_context: "{context}"

  cluster_synthesis:
    overall_rating: "{strong|adequate|weak}"
    chronological_interpretation: "{interpretation}"
    gateway_recommendation: "{recommendation}"
```
```

---

## Quality State Adjustments

### If Quality State = HIGH

- Use precise scores (±5 point precision)
- Apply full anchor criteria
- Complete full readiness checklist

### If Quality State = MODERATE

- Use 20-point score bands
- Note caveats prominently
- Add caveat header:

```markdown
> ⚠️ **CAVEATED ASSESSMENT:** This assessment has reduced precision due to [extraction gaps | classification uncertainty]. Scores are reported as 20-point bands.
```

### If Quality State = LOW

- DO NOT proceed with cluster assessment
- If you reach this prompt with LOW quality, STOP and report error

---

## Self-Validation Checklist

Before finalising cluster-3-reproducibility.md, verify:

- [ ] Classification.json read and approach identified
- [ ] Track-a-quality.md read and quality state confirmed
- [ ] Pathway determined (standard or variant)
- [ ] If variant: Output flagged as experimental
- [ ] Correct anchors applied for pathway and approach
- [ ] Reproducibility score assigned with evidence citations
- [ ] Score justified with reference to anchor criteria
- [ ] **Reproducibility Readiness Checklist completed** (all fields)
- [ ] Tool assessment completed
- [ ] Adoption context determined and recorded
- [ ] Chronological interpretation provided
- [ ] Gateway assessment completed
- [ ] Structured YAML output included
- [ ] Quality state adjustments applied if MODERATE
- [ ] File written to assessment/cluster-3-reproducibility.md

---

## Common Errors to Avoid

**❌ Assessing field reproducibility**
- "Cannot re-excavate the site" is NOT relevant
- Focus on analytical/computational reproducibility only

**✅ Focus on: Can someone re-run the analysis given the data?**

---

**❌ Missing reproducibility_infrastructure check**
- Looking only at methods[] for code/data availability

**✅ Always check extraction.json → reproducibility_infrastructure:**
- `code_availability.statement_present` and `.repositories[]`
- `data_availability.statement_present` and `.repositories[]`
- `persistent_identifiers.software_pids[]`

---

**❌ Penalising non-computational papers on standard anchors**
- Literature reviews shouldn't score 0 on Reproducibility

**✅ Use Methodological Transparency variant for non-computational papers**

---

**❌ Adjusting scores for publication era**
- "This is from 2010 so we'll add 20 points"

**✅ Scores are consistent across eras; era is metadata for interpretation**

---

**❌ Forgetting to complete Readiness Checklist**
- Checklist is required for ALL papers

**✅ Complete full checklist regardless of pathway**

---

## References

**Signal definitions with anchors:**
→ `.claude/skills/research-assessor/references/credibility/signal-definitions-hass.md`

**Framework selection by approach:**
→ `.claude/skills/research-assessor/references/credibility/assessment-frameworks.md`

**Three pillars framework:**
→ `.claude/skills/research-assessor/references/credibility/assessment-pillars.md`

**Quality gating criteria:**
→ `.claude/skills/research-assessor/references/credibility/track-a-quality-criteria.md`
