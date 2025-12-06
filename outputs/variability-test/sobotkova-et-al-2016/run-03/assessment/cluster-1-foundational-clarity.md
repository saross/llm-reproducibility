# Cluster 1: Foundational Clarity Assessment

**Paper:** sobotkova-et-al-2016
**Assessment Date:** 2025-12-04
**Assessor Version:** v1.0

**Quality State:** HIGH
**Research Approach:** inductive (confidence: high)
**Paper Type:** methodological (software_tool)

---

## Signal Scores Summary

| Signal | Score | Band | Approach Anchors |
|--------|-------|------|------------------|
| Comprehensibility | 72 | Good | methodological |
| Transparency | 68 | Good | methodological |

**Cluster Rating:** Adequate

---

## Signal 1: Comprehensibility

**Score:** 72/100 (Good)

**Approach anchors applied:** methodological (inductive variant with emphasis on technical specification clarity)

### Assessment

The paper presents clear, well-structured descriptions of the FAIMS Mobile platform and its deployment model. Technical specifications are explicit and bounded — the four-level customisation hierarchy (core, approach, module, instance) is precisely defined with specific examples. The co-development partnership model is articulated clearly with explicit rationale (time/expertise saving, bridging off-the-shelf and bespoke).

However, the paper's comprehensibility is limited by implicit qualitative methods. The thematic synthesis (Theme 1-3) organises case study observations, but the methodology for theme identification (M-IMP-001) and quote selection (M-IMP-002) is undocumented. Readers understand WHAT themes were identified but not HOW they were derived. Claims like "upfront costs of mobile recording are ultimately counterbalanced by back-end payoffs" (C001) are clear in their content but lack transparent derivation pathway.

The case studies themselves are comprehensible — each project (Boncuklu, MEMSAP, PAZC) is described with clear context, deployment experience, and outcomes. The logical progression from platform description → case studies → thematic observations → lessons learned is traceable.

### Evidence

**Strengths:**

- RD003: "The project has adopted a 'co-development' model, where existing relationships with researchers are leveraged for software development and deployment in a collaborative (rather than client) relationship" — Clear strategic positioning with explicit rationale
- P004: Four-level customisation hierarchy (core/approach/module/instance) — Precise technical specification with bounded definitions
- C006: "The approach that best bridges the gap between off-the-shelf and bespoke software is a generalised approach" — Clear bounded claim with explicit scope

**Weaknesses:**

- M-IMP-001: Theme identification methodology undocumented — Readers cannot evaluate how themes were derived from case study data
- M-IMP-002: Quote selection criteria unspecified — Exemplar quotes presented without selection rationale
- IM001: "Upfront costs are ultimately counterbalanced by back-end payoffs" — Implicit argument requiring reader acceptance without transparent derivation

### Scoring Rationale

Score of 72 (Good for methodological/inductive). Technical specifications clear and bounded (meets 60-79 criterion), logical progression traceable (60-79), key terms defined (60-79). Deducted from Excellent range because theme identification methodology undocumented (would need transparent derivation for 80-100) and some implicit arguments not explicitly derived (would need all claims explicitly grounded for 80-100).

---

## Signal 2: Transparency

**Score:** 68/100 (Good)

**Approach anchors applied:** methodological

### Assessment

The paper demonstrates good transparency for software architecture and deployment options. FAIMS platform architecture is documented with clear design rationale (Android-based, server-client model, SQLite local storage, module customisation). Design decisions are explained — why open source (sustainability), why generalised approach (bridging off-the-shelf/bespoke), why Android (field durability, cost).

Code is publicly available on GitHub (https://github.com/FAIMS) under GPLv3 licence, providing excellent code transparency. However, there is no DOI for archived software versions, and module definition documents lack comprehensive metadata.

The validation approach (case study demonstration) is implicit rather than explicitly stated as methodology. The paper does not frame case studies as formal validation — they are presented as illustrative experiences rather than systematic evaluation. This represents a transparency gap: readers understand WHAT the case studies show, but the paper doesn't explicitly state that this is the validation strategy.

Data collection instruments are partially documented — the post-project questionnaire (P001) is mentioned but full instrument not provided. Communication logs (M002) are referenced but analysis procedure undocumented.

### Evidence

**From reproducibility_infrastructure:**

- Code availability: **present** — GitHub repository (https://github.com/FAIMS), GPLv3 licence, machine_actionability: moderate
- Data availability: **implicit_reference** — Supplementary materials referenced but access mechanism unclear
- Persistent identifiers: Software URL only (no DOI), no author ORCIDs
- FAIR score: 9/16 (56.25%) — moderately_fair

**Strengths:**

- Code openly available on GitHub with explicit GPLv3 licence
- Software architecture clearly documented with design rationale
- Deployment options (own server, FAIMS server, partner/funder server) explicitly enumerated with costs
- Funding sources documented with grant numbers (NeCTAR RT043, ARC LE140100151)

**Weaknesses:**

- P001: "The questionnaire was circulated by the FAIMS Project through email to the three directors" — Questionnaire mentioned but full instrument not provided
- M-IMP-001, M-IMP-002: Qualitative analysis methodology undocumented
- No formal data availability statement
- No archived software DOI (GitHub URL only)
- Supplementary materials access unclear

### Scoring Rationale

Score of 68 (Good for methodological). Software architecture documented with design rationale (60-79 criterion), code publicly available (60-79), major dependencies noted (GPLv3, Android). Deducted from Excellent because no archived software DOI (would need persistent identifier for 80-100), validation approach implicit rather than explicit (would need validation approach explicit for 80-100), and data collection instruments not fully provided (would need comprehensive documentation for 80-100). The 2016 publication year contextualises these gaps — FAIR and DOI practices were not yet standard for HASS software papers.

---

## Cluster Synthesis

**Overall Foundational Clarity:** Adequate

The paper demonstrates adequate foundational clarity overall. Both signals score in the Good range (72 and 68), indicating that the core technical content is comprehensible and transparently documented. The FAIMS platform itself is well-documented — architecture, design decisions, customisation options, and deployment models are clear. The code availability on GitHub with explicit licensing is a significant transparency strength.

The pattern across both signals reveals a consistent gap: while the technical/software content is transparent and comprehensible, the qualitative research methodology (theme identification, quote selection, case study analysis) is implicit. This creates an asymmetry where readers can understand and evaluate the FAIMS software claims but cannot fully evaluate the thematic synthesis claims.

### Pattern Summary

Strong technical transparency (software architecture, design rationale, code availability) combined with weak methodological transparency (qualitative analysis procedures). This pattern is common in methodological/software papers where the software itself is the contribution and case studies serve demonstrative rather than evidential roles.

### Implications for Subsequent Assessment

- **For Cluster 2 (Evidential Strength):** The implicit qualitative methodology will affect Validity assessment. Case study evidence supports platform capability claims but methodology for synthesising thematic lessons is undocumented. Robustness assessment should use 📦 software paper context flag — limited comparison to alternatives is genre-appropriate.

- **For Cluster 3 (Reproducibility):** High code availability (GitHub, GPLv3) supports reproducibility of software. However, the case study analysis methodology cannot be reproduced due to documentation gaps. Assessment pathway should be standard (has computational component in FAIMS software) but the validation case studies are non-computational.

---

## Structured Output

```yaml
cluster_1_foundational_clarity:
  paper_slug: "sobotkova-et-al-2016"
  assessment_date: "2025-12-04"
  quality_state: "high"
  research_approach: "inductive"

  comprehensibility:
    score: 72
    band: "good"
    strengths:
      - "Technical specifications clear and bounded (four-level customisation hierarchy)"
      - "Logical progression from platform description to case studies to themes traceable"
      - "Co-development model articulated with explicit rationale"
    weaknesses:
      - "Theme identification methodology undocumented (M-IMP-001)"
      - "Quote selection criteria unspecified (M-IMP-002)"
    rationale: "Good for methodological/inductive. Technical content comprehensible, logical structure traceable. Deducted from Excellent due to undocumented qualitative methods for thematic synthesis."

  transparency:
    score: 68
    band: "good"
    strengths:
      - "Software architecture documented with design rationale"
      - "Code publicly available on GitHub (GPLv3)"
      - "Funding sources documented with grant numbers"
    weaknesses:
      - "No archived software DOI (GitHub URL only)"
      - "Validation approach implicit rather than explicit"
      - "Data collection instruments not fully provided"
    rationale: "Good for methodological. Strong code transparency (GitHub, open source). Deducted from Excellent due to missing persistent identifiers, implicit validation approach, incomplete instrument documentation."

  cluster_synthesis:
    overall_rating: "adequate"
    pattern_summary: "Strong technical transparency (software, architecture, code) with weak methodological transparency (qualitative analysis). Asymmetry between software documentation and case study methodology."
    consistency_check: "consistent"
    implications:
      cluster_2: "Validity affected by undocumented qualitative methodology. Apply software paper context flag for Robustness."
      cluster_3: "High code availability supports software reproducibility. Case study methodology not reproducible."
```
