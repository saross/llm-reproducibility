# The Three Pillars of Research Credibility Assessment

**Purpose:** Conceptual framework organising the Seven Signals into three assessment pillars

**Date:** 2025-11-29

**Version:** 1.0

---

## Overview

The credibility assessment framework evaluates research through three complementary pillars, each addressing a distinct question about research quality. These pillars organise the Seven repliCATS Signals adapted for Humanities, Arts, and Social Sciences (HASS).

| Pillar | Core Question | Applies To |
|--------|---------------|------------|
| **Transparency** | Is the work documented and artefacts published? | All papers, all components |
| **Credibility** | How much faith can we put in the results? | All papers, all components |
| **Reproducibility** | Can computational aspects be re-executed? | Papers with computational components only |

---

## Pillar 1: Transparency

> "Show your work" / "The process is the product"

### Core Question

Is the work documented and artefacts published?

### Signals

- **Comprehensibility** — Are claims clear, explicit, and well-structured?
- **Transparency** — Are research methods and procedures well-documented?

### Applies To

All papers, all components. Every piece of research can be assessed for how well it documents what was done.

### Assessment Focus

- Clarity of claims and argument structure
- Documentation of methods and procedures
- Publication of data, code, and materials
- Accessibility of research artefacts

### Cluster

**Cluster 1: Foundational Clarity** — These two signals are "foundational" because they underpin assessment of all other signals. You cannot properly evaluate validity or robustness if you cannot understand what was done.

---

## Pillar 2: Credibility

> "How much faith can we put in the results?"

### Core Question

Given what was done, how sound is the evidence and how trustworthy are the conclusions?

### Signals

- **Plausibility** — Does the claim align with established prior evidence and theory?
- **Validity** — Are methods appropriate and claims adequately supported by evidence?
- **Robustness** — Would results hold under different reasonable analytical approaches?
- **Generalisability** — Can findings transfer to other contexts? Are claims carefully constrained?

### Applies To

All papers, all components. Every piece of research can be assessed for the quality and soundness of its evidence and conclusions.

### Assessment Focus

- Fit with domain knowledge and theory
- Evidence sufficiency and representativeness
- Sensitivity to analytical choices
- Appropriate scope and limitations

### Cluster

**Cluster 2: Evidential Strength** — These four signals assess the core credibility question: can we trust these results?

---

## Pillar 3: Reproducibility

> "Can we re-run the analysis?"

### Core Question

Can the computational or analytical aspects of the research be independently re-executed?

### Signals

- **Reproducibility** — Can others reproduce analytical outputs given the same inputs?

### Applies To

**Papers with computational components only.** Not all research has reproducible analytical components:

| Has Computational Component | Examples |
|----------------------------|----------|
| **Yes** | Statistical analyses, computational workflows, data transformations, machine learning, GIS analysis |
| **No** | Literature reviews, theoretical papers, pure qualitative research, software descriptions (without empirical validation) |

### Assessment Focus

- Availability of inputs (data)
- Availability of code/scripts
- Environment specification (dependencies, versions)
- Documentation of outputs
- Feasibility of re-execution

### Cluster

**Cluster 3: Reproducibility** — This single-signal cluster assesses whether computational aspects can be independently verified.

---

## The Reproducibility Distinction

### What Reproducibility Means in HASS

**Reproducibility = Analytic or computational reproducibility, NOT beginning-to-end reproducibility or replication of the overall research.**

| What We CAN Assess for Reproducibility | What We CANNOT |
|---------------------------------------|----------------|
| Statistical analyses | Re-excavating a site |
| Computational workflows | Re-conducting ethnographic fieldwork |
| Data transformations | Re-observing historical events |
| Machine learning model training | Re-collecting destroyed samples |
| GIS spatial analysis | Re-interviewing deceased informants |

The question is: **Given the data and code, can someone else run the analysis and get the same results?**

NOT: **Can someone repeat the entire study from scratch?**

### Tool-Based Assessment Guidance

When assessing reproducibility of computational components, consider the tools used:

| Tool Type | Examples | Reproducibility Impact |
|-----------|----------|----------------------|
| **Open scriptable** | Python, R, Julia, bash | Ideal — code is portable, inspectable, executable |
| **Proprietary scriptable** | SPSS syntax, Stata do-files, SAS | Reproducible if software available; demerit for closed tools |
| **GUI-based without documentation** | Excel, manual point-and-click | Significant demerit — requires step-by-step guidance for human/AI to reproduce |
| **GUI-based with documentation** | Excel with detailed procedures | Reduced demerit — reproducible but labour-intensive |

### Papers Without Computational Components

For papers without computational components, we use **experimental alternate anchors** focused on methodological transparency:

**Signal variant:** "Reproducibility (Methodological Transparency variant)"

**Core question:** Are methods described clearly enough that someone could apply the same approach to different data/contexts?

| Band | Methodological Transparency Criteria |
|------|--------------------------------------|
| 80-100 | Methods fully documented, all decision points explicit, could be operationalised |
| 60-79 | Most methods clear, some tacit knowledge required, generally reproducible approach |
| 40-59 | Partial documentation, significant gaps, experienced researcher could approximate |
| 20-39 | Sparse documentation, approach unclear, reproduction would require author consultation |
| 0-19 | Methods opaque, cannot determine how conclusions were reached |

**Output flag:** Scores using alternate anchors are marked `experimental: true` in assessment output.

---

## Chronological Context: Diffusion of Innovation

Reproducibility practices have evolved significantly. When interpreting Reproducibility scores, consider the publication era:

| Era | Adoption Stage | Expectations |
|-----|----------------|--------------|
| **Pre-2015** | Innovators | Reproducibility practices rare; high scores exceptional |
| **2015-2020** | Early Adopters | Growing awareness; code sharing emerging |
| **2020-2025** | Late Early Adopters | Data/code sharing increasingly expected; not yet mainstream |
| **Post-2025** | Early Majority (projected) | Reproducibility practices becoming standard |

### Implementation

Chronological context is recorded as **metadata only** — scores are not adjusted for era.

- Consistent scoring enables cross-era comparison
- Metadata provides interpretive context
- Example interpretation: "For a 2012 paper, this reproducibility score of 35 reflects practices that were ahead of their time for the era"

---

## Reproducibility Readiness Checklist

For papers with computational components, Cluster 3 outputs a structured readiness assessment for future automation:

```yaml
reproducibility_readiness:
  applies: true|false  # Does paper have computational component?
  if_not_applicable_reason: "string"  # e.g., "Literature review", "Theoretical paper"

  # If applies = true:
  inputs_available:
    status: "yes|partial|no"
    details: "string"
  code_available:
    status: "yes|partial|no"
    tool_type: "open_scriptable|proprietary_scriptable|gui_based|mixed"
    details: "string"
  environment_specified:
    status: "yes|partial|no"
    details: "string"
  outputs_documented:
    status: "yes|partial|no"
    details: "string"

  execution_feasibility: "ready|needs_work|not_feasible"
  feasibility_rationale: "string"

  # Chronological context
  publication_year: 2024
  adoption_context: "innovator|early_adopter|early_majority|mainstream"
```

### Future Use

This checklist serves as a **gateway for actual reproduction attempts**:

1. **Value in its own right** — Understanding the reproducibility landscape across papers
2. **Gateway to child process** — Papers marked `execution_feasibility: "ready"` can be queued for automated reproduction attempts (get inputs → run code → verify outputs)

---

## Mapping Signals to Pillars and Clusters

| Signal | Pillar | Cluster | Assessment Focus |
|--------|--------|---------|-----------------|
| Comprehensibility | Transparency | Cluster 1 | Clarity of claims and argument |
| Transparency | Transparency | Cluster 1 | Documentation of methods and procedures |
| Plausibility | Credibility | Cluster 2 | Fit with domain knowledge |
| Validity | Credibility | Cluster 2 | Evidence sufficiency |
| Robustness | Credibility | Cluster 2 | Sensitivity to analytical choices |
| Generalisability | Credibility | Cluster 2 | Appropriate scope and limitations |
| Reproducibility | Reproducibility | Cluster 3 | Re-executability of computational aspects |

---

## Assessment Workflow

```text
extraction.json (from Passes 0-7)
        ↓
classification.json (Pass 8)
        ↓
Track A Quality Gating
        ↓
┌───────────────────────────────────────────────────────────┐
│                    Cluster 1                              │
│            Transparency Pillar                            │
│     Comprehensibility + Transparency signals              │
│          (applies to all papers)                          │
└───────────────────────────────────────────────────────────┘
        ↓
┌───────────────────────────────────────────────────────────┐
│                    Cluster 2                              │
│            Credibility Pillar                             │
│  Plausibility + Validity + Robustness + Generalisability  │
│          (applies to all papers)                          │
└───────────────────────────────────────────────────────────┘
        ↓
┌───────────────────────────────────────────────────────────┐
│                    Cluster 3                              │
│          Reproducibility Pillar                           │
│           Reproducibility signal                          │
│    (computational components only; or alternate anchors)  │
└───────────────────────────────────────────────────────────┘
        ↓
Credibility Report + assessment.json
```

---

## Key Principles

### 1. Different Questions, Different Scope

Each pillar asks a different question and applies differently:

- **Transparency** and **Credibility** apply to **all papers**
- **Reproducibility** applies only to **computational components** (or uses alternate anchors)

### 2. Transparency ≠ Reproducibility

A paper can be highly transparent (well-documented) but not reproducible (no code shared). These are related but distinct concepts:

| Transparent | Reproducible | Description |
|-------------|--------------|-------------|
| Yes | Yes | Ideal: documented AND artefacts available |
| Yes | No | Good documentation but no code/data sharing |
| No | Yes | Code available but poorly documented |
| No | No | Neither documented nor shareable |

### 3. Realistic HASS Expectations

The framework acknowledges what can and cannot be reproduced in HASS:

- **Fieldwork, excavations, ethnographic encounters** → Assess on transparency and credibility
- **Computational analyses of collected data** → Assess on reproducibility

### 4. Era-Aware Interpretation

Reproducibility scores are consistent across eras, but interpretation should be contextualised. A 2010 paper with a reproducibility score of 50 represents different field practices than a 2024 paper with the same score.

---

## Related References

- `signal-definitions-hass.md` — Detailed signal definitions with approach-specific anchors
- `assessment-frameworks.md` — Signal emphasis by research approach
- `track-a-quality-criteria.md` — Quality gating for credibility assessment

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-11-29 | Initial framework; Generalisability moved to Cluster 2; Reproducibility terminology standardised |
