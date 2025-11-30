# Pass 10: Final Credibility Assessment Report

**Version:** v1.0
**Last Updated:** 2025-11-30
**Workflow Stage:** Pass 10 - Final Report Generation
**Pillar:** Synthesis

---

## Purpose

Generate a unified credibility assessment report that consolidates all cluster outputs into a single document with:
1. Executive summary for quick assessment
2. Signal scores dashboard
3. Detailed findings from each cluster
4. Contextual interpretation explaining what scores mean for this paper type
5. Machine-readable JSON output for batch processing

---

## Your Task

Read all assessment outputs generated in Passes 8-9, synthesise into a unified report, add contextual interpretation, and generate the final credibility report.

**Inputs (read from assessment/ directory):**
- `classification.md` — Paper type, approach, framework
- `track-a-quality.md` — Quality gating result
- `cluster-1-foundational-clarity.md` — Signals 1-2
- `cluster-2-evidential-strength.md` — Signals 3-6
- `cluster-3-reproducibility.md` — Signal 7

**Also read:**
- `extraction.json` — For paper metadata (title, DOI, publication year)

**Output:** `assessment/credibility-report.md`

---

## Assessment Workflow

### STEP 1: Read All Inputs

**Read classification.md and extract:**
```yaml
paper_type: "[empirical|methodological|theoretical|meta_research]"
paper_subtype: "[specific subtype]"
approach: "[deductive|inductive|abductive]"
framework: "[framework used]"
classification_confidence: "[high|medium|low]"
```

**Read track-a-quality.md and extract:**
```yaml
quality_state: "[high|moderate|low]"
extraction_confidence: "[high|medium|low]"
```

**Read each cluster output and extract:**
- Signal scores (0-100)
- Signal bands (excellent/good/moderate/low/minimal)
- Cluster ratings
- Key strengths and weaknesses
- Structured YAML output

**Read extraction.json and extract:**
- Paper title
- Paper DOI
- Publication year

---

### STEP 2: Determine Era Context

Based on publication year, classify the era:

| Era | Year Range | Label |
|-----|------------|-------|
| **Pre-reproducibility** | Before 2015 | "Pre-reproducibility crisis awareness — transparency expectations lower" |
| **Early adopter** | 2015-2020 | "Early adopter era — reproducibility discussions emerging, data/code sharing becoming expected" |
| **Current** | 2020-present | "Current era — FAIR and open science expectations established" |

---

### STEP 3: Calculate Aggregate Score (EXPERIMENTAL)

Compute the aggregate credibility score:

```
aggregate = (comprehensibility + transparency + plausibility + validity
           + robustness + generalisability + reproducibility) / 7
```

Round to nearest integer.

**Determine verdict band from aggregate:**

| Band | Score Range |
|------|-------------|
| Excellent | 80-100 |
| Good | 60-79 |
| Moderate | 40-59 |
| Low | 20-39 |
| Minimal | 0-19 |

**Mark aggregate as EXPERIMENTAL** — include note that we are investigating what it means.

---

### STEP 4: Identify Context Flags

For each signal, determine if a context flag applies:

---

#### 📦 Descriptive/Artefact Papers (Robustness Context)

**These paper types describe artefacts rather than test hypotheses. A Moderate Robustness score reflects genre expectations, not a deficiency.**

| Paper Subtype | Signal | Flag | Note |
|---------------|--------|------|------|
| Software papers | Robustness | 📦 | "Describes software; comparative evaluation is a different paper type" |
| Data papers | Robustness | 📦 | "Documents dataset; focus on Transparency and Reproducibility" |
| Infrastructure papers | Robustness | 📦 | "Describes platform/system, not tests it against alternatives" |
| Protocol papers | Robustness | 📦 | "Describes method; validation ≠ systematic comparison" |
| Resource papers | Robustness | 📦 | "Documents database/ontology/vocabulary" |

**Interpretation template for 📦 papers:**
> **Why this score:** {Subtype} papers describe artefacts rather than testing hypotheses. They do not typically include systematic comparisons, sensitivity analyses, or robustness checks. A Moderate Robustness score reflects genre expectations — it is not a criticism.
>
> **What this means:** The paper describes {artefact} and its features. Comparative assessment is the reader's responsibility.
>
> **Generalisation:** Similar patterns expected for other software, data, infrastructure, protocol, and resource papers.

---

#### 📐 Synthesis/Framework Papers (Robustness Context)

**These paper types argue for positions rather than test hypotheses systematically.**

| Paper Subtype | Signal | Flag | Note |
|---------------|--------|------|------|
| Theoretical papers | Robustness | 📐 | "Proposes framework; exhaustive comparison not expected" |
| Position papers | Robustness | 📐 | "Argues viewpoint; limited comparison expected" |
| Commentary papers | Robustness | 📐 | "Responds to specific work; systematic comparison not expected" |
| Narrative reviews | Robustness | 📐 | "Synthesises literature; less rigorous than systematic reviews" |

**Note:** Systematic reviews are different — they DO require robustness checks and should not receive 📐 flag.

---

#### 🔧 Methodological Transparency (Reproducibility Context)

**For papers without computational workflows to reproduce:**

| Paper Subtype | Signal | Flag | Note |
|---------------|--------|------|------|
| Software papers | Reproducibility | 🔧 | "Can users install, use, and extend the software?" |
| Interpretive papers | Reproducibility | 🔧 | "Can readers access sources and follow reasoning?" |
| Theoretical papers | Reproducibility | 🔧 | "Can readers trace the argument?" |
| Methodological papers | Reproducibility | 🔧 | "Can readers implement the method?" |

---

#### Approach-Specific Flags

| Approach | Signal | Flag | Note |
|----------|--------|------|------|
| Abductive | Robustness | — | "Inference to best explanation — alternatives considered but not exhaustively tested" |
| Inductive | Transparency | — | "Pre-registration not expected for exploratory research" |

---

**Apply flags** to signals that warrant contextual interpretation.

---

### STEP 5: Generate Executive Summary

Write a concise executive summary (< 200 words) containing:

1. **Paper identification** (title, type, approach)
2. **Verdict** (band + confidence)
3. **Era context** (one line)
4. **Key strengths** (2-3 bullet points from cluster outputs)
5. **Key concerns** (1-2 bullet points if any)
6. **Bottom line** (one sentence summary)

**Template:**

> **Verdict:** {band} | **Confidence:** {confidence}
>
> This {paper_type} paper using {approach} reasoning demonstrates {overall_pattern}. {era_context_sentence}.
>
> **Key Strengths:**
> - {strength_1}
> - {strength_2}
>
> **Key Concerns:**
> - {concern_1}
>
> **Bottom Line:** {summary_statement}

---

### STEP 6: Compile Detailed Findings

For each cluster, summarise:

1. **Cluster 1: Foundational Clarity**
   - Rating (strong/adequate/weak)
   - Summary (2-3 sentences)
   - Key strengths (from cluster output)
   - Key weaknesses (from cluster output)

2. **Cluster 2: Evidential Strength**
   - Rating
   - Summary
   - Key strengths
   - Key weaknesses

3. **Cluster 3: Reproducibility**
   - Rating
   - Pathway (computational or methodological_transparency)
   - Summary
   - Key strengths
   - Key weaknesses

---

### STEP 7: Generate Contextual Interpretation

**This is the key value-add of the unified report.**

For each signal with a context flag, write an interpretation:

```markdown
### {Signal Name} ({score}, {band}) {flag}

**Why this score:** {Explain why this score is expected for this paper type/approach}

**What this means:** {How readers should interpret this — not a weakness, just different expectations}

**What readers should consider:** {Any independent evaluation readers should do}
```

**Example for Methodological Paper with Moderate Robustness:**

> ### Robustness (58, Moderate) ⚠️
>
> **Why this score:** Methodological advocacy papers argue for a position rather than testing multiple alternatives. A Moderate Robustness score is typical — and not a severe criticism — for this paper type.
>
> **What this means:** The paper builds a coherent case for preregistration but does not exhaustively compare alternative approaches to research transparency.
>
> **What readers should consider:** Evaluate alternative transparency mechanisms (e.g., registered reports, data sharing mandates, statistical reforms) independently when assessing the argument.

---

### STEP 8: Compile Infrastructure & FAIR Summary

From extraction.json `reproducibility_infrastructure` section, summarise:

- **FAIR score** (0-40) and rating
- **Code availability** (available/not_available/not_applicable/embargoed/upon_request)
- **Data availability** (same options + partially_available)
- **Preregistration** (preregistered/not_preregistered/not_applicable)
- **PID coverage** (DOIs, ORCIDs present/absent)
- **Infrastructure gaps** (what's missing)

---

### STEP 9: Generate JSON Output

Generate the structured JSON output block following the schema in `assessment-system/schema/credibility-report-schema.json`.

**JSON structure:**

```json
{
  "credibility_report": {
    "version": "1.0",
    "paper": {
      "slug": "{paper_slug}",
      "title": "{paper_title}",
      "doi": "{paper_doi}",
      "publication_year": {year}
    },
    "classification": {
      "paper_type": "{paper_type}",
      "paper_subtype": "{paper_subtype}",
      "approach": "{approach}",
      "framework": "{framework}",
      "quality_state": "{quality_state}",
      "classification_confidence": "{confidence}"
    },
    "verdict": {
      "band": "{band}",
      "confidence": "{confidence}",
      "aggregate_score": {aggregate},
      "aggregate_experimental": true
    },
    "signals": {
      "comprehensibility": { "score": {n}, "band": "{band}" },
      "transparency": { "score": {n}, "band": "{band}" },
      "plausibility": { "score": {n}, "band": "{band}" },
      "validity": { "score": {n}, "band": "{band}" },
      "robustness": { "score": {n}, "band": "{band}", "context_flag": "{flag}" },
      "generalisability": { "score": {n}, "band": "{band}" },
      "reproducibility": { "score": {n}, "band": "{band}", "variant": "{variant}" }
    },
    "aggregates": {
      "cluster_1_rating": "{rating}",
      "cluster_2_rating": "{rating}",
      "cluster_3_rating": "{rating}"
    },
    "infrastructure": {
      "fair_score": {score},
      "fair_rating": "{rating}",
      "fair_maximum": 40,
      "code_availability": "{status}",
      "data_availability": "{status}",
      "preregistration": "{status}"
    },
    "era_context": {
      "publication_year": {year},
      "era": "{era}",
      "era_label": "{label}",
      "expectations_note": "{note}"
    },
    "assessment_metadata": {
      "assessment_date": "{YYYY-MM-DD}",
      "assessor_version": "v1.0",
      "schema_version": "1.0"
    }
  }
}
```

---

### STEP 10: Assemble Final Report

Use the template in `assessment-system/templates/credibility-assessment-report-template.md`.

Fill in all placeholders with data collected in Steps 1-9.

**Output file:** `assessment/credibility-report.md`

---

## Quality State Adjustments

### If Quality State = HIGH

- Report precise scores (0-100)
- Full contextual interpretation
- Standard report format

### If Quality State = MODERATE

- Add caveat banner at top:

```markdown
> ⚠️ **CAVEATED ASSESSMENT:** This assessment has reduced precision due to {caveat_reason}. Scores are reported as 20-point bands.
```

- Report scores as bands (e.g., "60-80" instead of "72")
- Include caveat notes in interpretation

### If Quality State = LOW

- **DO NOT generate final report**
- Track A should have prevented assessment
- If you reach this prompt with LOW quality, STOP and report error

---

## Verdict Determination Logic

**5-Tier Verdict (from aggregate score):**

| Band | Score Range | Criteria |
|------|-------------|----------|
| **Excellent** | 80-100 | All signals ≥ 60; aggregate ≥ 80; no signal < 50 |
| **Good** | 60-79 | Most signals ≥ 60; aggregate ≥ 60; at most one signal < 50 |
| **Moderate** | 40-59 | Most signals ≥ 40; aggregate ≥ 40 |
| **Low** | 20-39 | Aggregate 20-39; multiple signals < 40 |
| **Minimal** | 0-19 | Aggregate < 20; majority of signals < 40 |

**Confidence Level:**

| Level | Criteria |
|-------|----------|
| HIGH | Quality State = HIGH AND Classification Confidence = HIGH |
| MEDIUM | Either Quality State or Classification = MODERATE |
| LOW | Either Quality State or Classification = LOW |

---

## Self-Validation Checklist

Before finalising credibility-report.md, verify:

- [ ] All cluster outputs read and scores extracted
- [ ] Paper metadata from extraction.json included
- [ ] Era context determined from publication year
- [ ] Aggregate score calculated correctly
- [ ] Context flags applied where appropriate
- [ ] Executive summary < 200 words
- [ ] All 7 signals included in dashboard
- [ ] Detailed findings for all 3 clusters
- [ ] Infrastructure & FAIR summary complete
- [ ] Contextual interpretation for flagged signals
- [ ] JSON output valid and parseable
- [ ] Quality state adjustments applied if MODERATE
- [ ] Report written to assessment/credibility-report.md

---

## Common Errors to Avoid

**❌ Missing context interpretation**
- Don't just report scores — explain what they mean for this paper

**✅ Include interpretation for every flagged signal**

---

**❌ Wrong era classification**
- Check publication year carefully

**✅ Use correct era boundaries: pre-2015, 2015-2020, 2020+**

---

**❌ Inconsistent JSON structure**
- JSON must match schema exactly

**✅ Validate JSON against credibility-report-schema.json**

---

**❌ Executive summary too long**
- Busy readers need quick assessment

**✅ Keep executive summary under 200 words**

---

**❌ Missing experimental flag on aggregate**
- Aggregate score is experimental

**✅ Always include `"aggregate_experimental": true`**

---

## References

**Template:**
→ `assessment-system/templates/credibility-assessment-report-template.md`

**JSON Schema:**
→ `assessment-system/schema/credibility-report-schema.json`

**Cluster Prompts:**
→ `assessment-system/prompts/cluster-*.md`

**Signal Definitions:**
→ `.claude/skills/research-assessor/references/credibility/signal-definitions-hass.md`

---

**End of Pass 10 Prompt**
