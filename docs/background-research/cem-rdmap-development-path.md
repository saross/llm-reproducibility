# From Diverse Frameworks to CEM + RDMAP: A Development Path Report

**Document Purpose:** Trace how the CEM + RDMAP architecture emerged from surveying 20+ existing frameworks  
**Date:** October 26, 2025  
**Project:** LLM-Assisted Reproducibility Assessment for HASS Research

---

## Executive Summary

The **CEM + RDMAP** framework represents a strategic synthesis of existing knowledge representation schemas and research methodology standards. This document explains how comprehensive literature review of 20+ frameworks led to a two-layer architecture that separates **argumentative structure** (Claims-Evidence-Methods) from **procedural structure** (Research Design-Methods-Protocols), enabling automated credibility assessment for humanities and social sciences research.

**Key Innovation:** While repliCATS proved that structured assessment of research credibility works (73-84% accuracy), they assumed humans would manually extract relevant features from papers. Our framework automates this extraction layer by building on proven patterns from multiple domains.

---

## Phase 1: Comprehensive Framework Survey

### Two Categories of Source Material

#### **1. Reporting Standards & Preregistration Frameworks**

These frameworks tell researchers *what to report* but don't provide extractable knowledge structures:

- **MDAR** (Materials Design Analysis Reporting) - Focused on *what* was done
- **Preregistration protocols** - OSF, ClinicalTrials.gov, SPIRIT, PRP-QUANT
- **Clinical trial standards** - CONSORT-SPI, TIDieR checklist (12 intervention elements)
- **Qualitative research templates** - Haven et al. Delphi consensus
- **Outcome specifications** - CONSORT-Outcomes 2022 framework
- **Study design taxonomies** - ClinicalTrials.gov controlled vocabularies

**Strengths:** Comprehensive checklists, domain validation, decades of refinement  
**Limitation:** Designed for *human reporting*, not *machine extraction*

#### **2. Knowledge Representation Schemas**

These frameworks model knowledge structures but often lack domain coverage:

- **Micropublications Ontology** - Explicit Claim class with support/attack graphs
- **Nanopublications** - Atomic assertions with immutable provenance
- **PROV-O** (W3C standard) - Data provenance tracking
- **Cochrane/GRADE** - Risk of bias assessment and evidence quality levels
- **repliCATS** - Seven credibility signals framework (validated predictor)
- **Research Objects** - Computational workflow provenance
- **Argumentation frameworks** - AIF, Carneades, Toulmin, Walton schemes
- **SPAR (SPARC/CiTO/FaBiO/DoCO)** - Document structure and citation typing
- **IBM Debater** - Claim extraction with neural quality scoring

**Strengths:** Formal structures, tool support, semantic interoperability  
**Limitation:** Often domain-specific (biomedicine, computational science)

---

## Phase 2: Gap Analysis - What's Missing?

### Critical Gap 1: No Integrated Framework

**Finding:** No single schema comprehensively models all three dimensions with quality assessment:

| Framework | Claims | Evidence | Methods | Quality Assessment |
|-----------|--------|----------|---------|-------------------|
| **Micropublications** | ✓✓ | ✓✓ | ✗ | Partial (argumentation only) |
| **Research Objects** | ✗ | ✓✓ | ✓✓ | Re-executability only |
| **Cochrane** | Partial | ✓ | ✓ | ✓✓ (RCTs only) |
| **repliCATS** | ✓ | ✓ | ✓ | ✓✓ (manual assessment) |
| **PROV-O** | ✗ | ✓ | ✓ | ✗ |

**Conclusion:** repliCATS came closest but required manual extraction. Micropublications strong on claims+evidence but weak on methods. Research Objects strong on methods+data but weak on claims.

### Critical Gap 2: HASS-Specific Needs Unmet

**Qualitative methods poorly represented:**
- No framework adequately captures interview protocols, ethnographic procedures, archival research methods, textual analysis approaches, or participant observation

**Single-case → generalization patterns not modeled:**
- Abductive reasoning from cases to theory
- How single case studies support theoretical claims
- Thick description as evidence type
- Exemplar-based reasoning

**Professional judgment vs. observation boundaries unclear:**
- Distinction between direct observations (primary data), expert interpretations (secondary analysis), and theoretical inferences (tertiary claims)

**Interpretive reasoning not captured:**
- Field-based inference processes
- Context-dependent meaning making
- Non-repeatable phenomena requiring professional expertise

### Critical Gap 3: Reporting vs. Knowledge Structures

**The fundamental problem:**
- MDAR/CONSORT frameworks tell you *what to report in a paper*
- But they don't provide *extractable knowledge structures for machines*
- Preregistration schemas capture *prospective plans*, not *retrospective extraction from published papers*

**What was needed:**
- Schemas that can be populated from *published papers* (not just registrations)
- Structures that enable *automated extraction* (not just human checklists)
- Frameworks that support *credibility assessment* (not just completeness checking)

---

## Phase 3: Strategic Architectural Decision - The Two-Layer Split

### The Core Insight

During Methods section rationalization work, we discovered:

> **"Methods ≠ Evidence/Claims"**
> 
> - **Methods extraction**: What was done (procedures, tools, parameters)
> - **Evidence/Claims extraction**: What supports what (observations, measurements, interpretations)
> 
> These could be parallel extraction passes, not sequential. Both benefit from two-pass structure but serve different analytical purposes.

This led to separating:

1. **Argumentative structure** (what the paper argues)
2. **Procedural structure** (how the research was conducted)

### Why Two Separate Frameworks?

#### **CEM (Claims-Evidence-Methods) = "What does the paper argue?"**

**Borrowed from:**
- Micropublications Ontology (explicit Claim class)
- repliCATS framework (credibility signals)
- Toulmin (warrant-based reasoning)
- Carneades (proof standards)

**Purpose:** Extract the *argumentative structure* of the paper

**Focus:** 
- What claims are made?
- What evidence supports them?
- What's the logical structure connecting them?
- Which claims are explicit vs. implicit?

**Feeds into:** Credibility *assessment* (repliCATS seven signals)

#### **RDMAP (Research Design-Methods-Protocols) = "How was the research done?"**

**Borrowed from:**
- Preregistration frameworks (MDAR, CONSORT-SPI, SPIRIT)
- Clinical trial standards (TIDieR, CONSORT-Outcomes)
- Study design taxonomies (ClinicalTrials.gov)

**Purpose:** Extract the *procedural/methodological structure* of research

**Focus:**
- What was the research design? (WHY was it framed this way?)
- What methods were used? (WHAT approaches were employed?)
- What specific protocols? (HOW was it done step-by-step?)

**Feeds into:** Reproducibility *analysis* and methodological transparency assessment

### Different Extraction Philosophies

**CEM Decision Tree:**
```
Would a non-expert accept this at face value?
├─ YES → Evidence (observation, measurement, data)
└─ NO → Claim (interpretation requiring domain expertise)
```

**RDMAP Decision Tree:**
```
Does this explain WHY research was framed this way?
├─ YES → Research Design
└─ NO → Does this explain WHAT general approach was used?
    ├─ YES → Method
    └─ NO → Does this explain HOW specifically it was done?
        ├─ YES → Protocol
        └─ NO → Project context (metadata)
```

### Different Consolidation Needs

**CEM consolidation principle:**
- Consolidate when claims assess the *same phenomenon* at the *same level of specificity*
- Keep separate when different quality dimensions require independent assessment

**RDMAP consolidation principle:**
- Consolidate when procedural descriptions serve the *same assessment purpose*
- Keep separate when they enable distinct reproducibility evaluations

---

## Phase 4: Synthesis Process - Building the Unified Framework

### The Development Flow

```
Starting Point: 20+ Disparate Frameworks
              ↓
        Gap Analysis
    "No schema does it all"
              ↓
    Strategic Split Decision
         ↙         ↘
    CEM Layer      RDMAP Layer
   (Arguments)     (Procedures)
         ↓              ↓
  Micropublications  Preregistration
  + repliCATS       + MDAR/CONSORT
  + Toulmin         + TIDieR
  + Carneades       + SPIRIT
  + Walton          + Study taxonomies
         ↘          ↙
      Unified Schema v2.4
    (with cross-references)
              ↓
        Assessment Phase
   (Seven Credibility Signals)
```

### Key Borrowings by Framework

| What We Took | From Where | Why This Framework? |
|--------------|------------|---------------------|
| **Explicit Claim class** | Micropublications Ontology | Only schema modeling claims as first-class objects |
| **Seven credibility signals** | repliCATS | Validated prediction framework (73-84% accuracy) |
| **Support/attack graphs** | Micropublications + AIF | Structured argumentation relationships |
| **Three-tier hierarchy** | Preregistration schemas | Natural organization: Design→Methods→Protocols |
| **TIDieR 12-element framework** | CONSORT-SPI | Comprehensive intervention documentation |
| **Risk of Bias taxonomy** | Cochrane | Adapted for HASS as `bias_concerns` |
| **Proof standards** | Carneades (legal reasoning) | Graduated credibility thresholds |
| **Argument patterns** | Walton | 60+ schemes with critical questions |
| **Provenance basics** | PROV-O (W3C) | Standard vocabulary (light touch) |
| **Study design taxonomies** | ClinicalTrials.gov | Controlled vocabularies (adapted for HASS) |

### Novel Contributions (Empirically Derived)

These elements emerged from **actual extraction work** on Methods sections:

1. **`generalization_from_single_case`** flag
   - Detected implicit generalizations from individual cases
   - Critical for HASS where single-case studies support theory

2. **`requires_professional_judgment`** flag
   - Marks claims needing domain expertise to assess
   - Distinguishes face-value observations from expert interpretations

3. **`claim_status`** (explicit/implicit)
   - Explicit: Stated directly in paper
   - Implicit: Logically necessary but unstated

4. **`project_metadata`** section
   - Separates contextual information from evidential claims
   - Prevents category errors (treating context as evidence)

5. **HPS epistemology categories**
   - Idiographic vs. nomothetic
   - Inductive/deductive/abductive reasoning modes
   - Single-case patterns flagged explicitly

6. **Two-pass extraction philosophy**
   - Pass 1: Liberal extraction (40-50% over-capture expected)
   - Pass 2: Systematic rationalization and consolidation
   - Rationale: Easier to consolidate than discover missed items

---

## Phase 5: Integration Architecture

### The Unified Schema v2.4 Structure

```
schema_v2.4/
├── shared_definitions/          # Prevent drift across objects
│   ├── location                 # Standardized source tracking
│   ├── uncertainty_structure    # Consistent uncertainty handling
│   ├── consolidation_metadata   # Two-pass workflow tracking
│   └── cross_reference_pattern  # Simple string ID arrays
│
├── CEM Layer (Argumentative)
│   ├── evidence_object          # What was observed/measured
│   ├── claim_object            # What was interpreted/argued
│   └── implicit_argument_object # Logical assumptions unstated
│
├── RDMAP Layer (Procedural)
│   ├── research_design_object   # WHY framed this way
│   ├── method_object           # WHAT approach used
│   └── protocol_object         # HOW specifically done
│
└── extraction_output            # Combined output structure
```

### Cross-Reference Architecture

**Design principle:** Simple string ID arrays (not complex structured objects)

**Why:** Match proven claims/evidence pattern; defer structured relationships to assessment phase

**Example:**
```json
{
  "method_id": "M003",
  "method_text": "Mobile platform (FAIMS) used for field data collection",
  "implements_designs": ["RD001"],
  "realized_through_protocols": ["P023", "P024"],
  "validated_by_evidence": ["E046"],
  "justification_claim": "C027"
}
```

### Methodological Arguments - Clean Separation

**Method description** (RDMAP object):
- "Used FAIMS mobile platform for data collection"

**Justification** (Claim object):
- "FAIMS was optimal choice because it enabled offline sync and custom modules"
- `claim_type: "methodological_argument"`
- `supports_method: "M003"`

**Rationale:** Leverages existing claims assessment framework; maintains clean separation between description and argumentation

---

## Phase 6: Assessment Enablement

### How CEM + RDMAP Enable repliCATS Signals

The extracted structures map to credibility assessment:

| repliCATS Signal | Extracted from CEM | Extracted from RDMAP |
|------------------|-------------------|---------------------|
| **Comprehensibility** | Explicit claims with scope qualifiers, logical claim-evidence links | Research design clarity, method documentation |
| **Transparency** | Evidence-claim provenance chains | Design rationale, protocol specifications |
| **Plausibility** | Domain context for consistency checking | Methodological appropriateness |
| **Validity** | Evidence-claim support strength, alternative interpretations | Measurement validity, sampling adequacy |
| **Robustness** | Evidence triangulation patterns | Sensitivity analyses, analytical robustness |
| **Replicability** | Data/code availability flags | Protocol detail sufficiency, tool specifications |
| **Generalisability** | Claim scope declarations, limitation statements | Sampling strategy, geographic/temporal bounds |

### The Complete Workflow

```
1. EXTRACTION PHASE (Automated)
   ├─ Pass 1: Liberal extraction → CEM graph + RDMAP structure
   └─ Pass 2: Rationalization → Consolidated, cross-referenced

2. ASSESSMENT PHASE (Semi-automated)
   ├─ Map CEM structures → Argument strength, evidence adequacy
   ├─ Map RDMAP structures → Methodological transparency, reproducibility
   └─ Combine both → Seven credibility signals scores

3. OUTPUT
   └─ Credibility scorecard with transparent provenance
```

---

## The Critical Innovation

### What repliCATS Proved

> **"Structured assessment of research credibility works"**
> 
> - 73-84% accuracy predicting replication outcomes
> - Seven credibility signals framework effective
> - Human deliberation produces good judgments

**But:** They assumed humans would manually:
1. Read papers
2. Extract relevant features (in their heads)
3. Write justifications
4. Code those justifications post-hoc

### What CEM + RDMAP Provides

> **"Automated extraction of the knowledge structures needed for assessment"**

**Your system workflow:**
1. **LLM extracts** structured knowledge directly (CEM graphs + RDMAP)
2. **LLM maps** that knowledge to credibility signals
3. **System outputs** assessments with transparent provenance

**repliCATS workflow:**
1. **Humans read** papers (manual, implicit)
2. **Humans write** justifications (unstructured)
3. **Humans code** justifications (post-hoc)
4. **System aggregates** coded markers

### The Value Proposition

**CEM + RDMAP is the missing layer** that repliCATS assumed would be done manually:

- **repliCATS proved:** *IF* you can identify what's going on in a paper, you can reliably assess credibility
- **Your innovation:** Building the system that *does the identification automatically*

---

## Conclusion

The journey from **20+ disparate frameworks** to **CEM + RDMAP** involved:

1. **Comprehensive survey** of existing standards and schemas
2. **Gap analysis** revealing no integrated solution
3. **Strategic split** between argumentative and procedural structures
4. **Selective borrowing** of proven patterns from each domain
5. **Empirical refinement** through actual extraction work
6. **Novel additions** addressing HASS-specific needs
7. **Integration architecture** enabling assessment

**Result:** A two-layer framework that:
- ✓ Builds on proven methodologies (not reinventing wheels)
- ✓ Adapts terminology for HASS/fieldwork context
- ✓ Maintains clean separation while enabling cross-references
- ✓ Supports automated extraction from published papers
- ✓ Enables systematic credibility assessment
- ✓ Provides transparent, auditable outputs

**The Bottom Line:** CEM + RDMAP automates the extraction layer that makes repliCATS-style assessment scalable, enabling content-based quality evaluation for HASS research beyond citation metrics.

---

**Document Status:** Complete synthesis report  
**Version:** 1.0  
**Date:** October 26, 2025  
**Next Steps:** Use this narrative for CWTS presentation, grant applications, and publication framing
