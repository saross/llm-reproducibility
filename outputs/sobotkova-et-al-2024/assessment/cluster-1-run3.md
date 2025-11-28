# Cluster 1: Foundational Clarity Assessment - Run 3

**Paper:** sobotkova-et-al-2024
**Assessment Date:** 2025-11-28
**Assessor Version:** v1.0
**Reliability Run:** 3

**Quality State:** HIGH
**Research Approach:** deductive (confidence: high)
**Paper Type:** empirical

---

## Signal Scores Summary

| Signal | Score | Band | Approach Anchors |
|--------|-------|------|------------------|
| Comprehensibility | 77 | Good | deductive |
| Transparency | 79 | Good | deductive |

**Cluster Rating:** Strong

---

## Signal 1: Comprehensibility

**Score:** 77/100 (Good)

**Approach anchors applied:** deductive

### Assessment

This deductive validation study demonstrates good comprehensibility. The paper tests ML model predictions against comprehensive ground truth data with clear quantified outcomes. The logical structure follows prediction → test → result: CNN predictions function as implicit hypotheses tested against field-verified mound locations, yielding specific performance metrics.

Claims are bounded and evaluable. The paper reports precise outcomes — "high false positive (87.1%) and false negative (95.3%) rates" — rather than vague generalisations. Scope is explicitly constrained to Kazanlak Valley context. Technical terminology (CNN, transfer learning, precision/recall, F1 score) is used consistently within established ML conventions.

Research designs RD001-RD004 provide explicit framework: external validation (RD001), two-run comparative design (RD002), negative results documentation (RD003), and cost-benefit analysis (RD004). Each includes stated rationale.

The paper falls short of excellent comprehensibility because hypotheses are not formally stated. The extraction notes "Hypothesis stated explicitly" as expected information missing from RD002. The validation logic is transparent, but explicit hypothesis statements would strengthen deductive clarity.

### Evidence

**Strengths:**
- C001: "Pre-trained CNNs have significant limitations when detecting varied features" — Clear, bounded finding
- RD001-RD004: Four explicit research designs with stated rationale
- Claims quantified: 87.1% FP, 95.3% FN, 135 hours vs 42 hours comparison
- Logical structure transparent throughout

**Weaknesses:**
- RD002: Hypothesis not stated explicitly (expected information missing)
- Implicit arguments (IA001-IA005) reveal unstated premises

### Scoring Rationale

Score of 77 falls in Good band (60-79) for deductive research. Paper meets Good criteria: predictions/hypotheses stated (implicitly via validation design), most key terms defined, logical structure mostly clear, claims understandable and evaluable. Does not reach Excellent (80-100) due to absence of explicit hypothesis statements. Strong validation logic and specific quantified claims support upper Good band.

---

## Signal 2: Transparency

**Score:** 79/100 (Good)

**Approach anchors applied:** deductive

### Assessment

The paper demonstrates strong transparency for a deductive ML validation study. Methodological documentation is comprehensive: 7 methods and 12 protocols extracted, covering the full ML workflow from model selection through validation. Four explicit research designs (RD001-RD004) articulate validation framework with stated rationale.

Code availability is excellent. The extraction documents an explicit code availability statement with three GitHub repositories clearly described: cnn-testing (training data preparation), burial-mounds (2021 classifier), MoundDetection (2022 classifier). Code machine actionability rated "high" in FAIR assessment. This significantly supports analytical reproducibility.

Limitations are extensively documented. RD003 explicitly frames the paper as documenting "failure" to "counterbalance publication bias." The paper acknowledges what went wrong and why, demonstrating commitment to methodological transparency.

The paper falls short of excellent transparency due to: (1) code repositories lack DOIs — no persistent identifiers despite excellent code sharing; (2) historical field survey data not deposited — data availability statement absent; (3) no pre-registration (acceptable for retrospective validation but prevents highest rating); (4) some computational environment details under-documented (specific hardware, framework versions, training time).

### Evidence

**Strengths:**
- Explicit code availability statement with 3 GitHub repositories
- Code machine actionability: "high" rating in extraction
- FAIR score: 12/16 (75%) — "highly_fair" rating
- Comprehensive methods (7) and protocols (12) documentation
- RD003: Explicit negative results framing
- 95% DOI coverage in references

**Weaknesses:**
- software_pids: All three repos have doi: null (no persistent identifiers)
- data_availability: statement_present = false
- P001: Missing hardware specifications, training time
- Code licences not stated (R1.1 partial)

### Scoring Rationale

Score of 79 falls at upper boundary of Good band (60-79) for deductive research. Paper meets Good criteria exceptionally well: clear research design, detailed methods documentation, code publicly available, major limitations acknowledged. Score does not quite reach Excellent (80-100) because: (1) code lacks persistent identifiers (DOIs), (2) data not publicly available. However, the combination of three code repositories, comprehensive methods documentation, explicit limitations acknowledgement, and high FAIR compliance (75%) justifies upper Good band.

---

## Cluster Synthesis

**Overall Foundational Clarity:** Strong

Both signals score in upper Good band (77-79), with Transparency at the threshold of Excellent. The paper demonstrates strong foundational clarity: clear validation framework, specific bounded claims, comprehensive methods documentation, excellent code availability, and explicit limitations discussion.

### Pattern Summary

Excellent code transparency (3 GitHub repos) with strong methods documentation. Main gaps: formal hypothesis specification (Comprehensibility) and persistent identifiers for code/data (Transparency). Pattern typical for high-quality computational archaeology: code sharing practices outpace formal hypothesis statements and PID infrastructure.

### Implications for Subsequent Assessment

- **For Cluster 2 (Evidential Strength):** Strong foundational clarity enables confident Validity/Robustness assessment. Two-run design and quantified metrics provide clear evidential basis.
- **For Cluster 3 (Reproducibility & Scope):** Three code repositories support analytical replicability. Data sharing gap constrains full reproducibility. Scope explicitly bounded to Kazanlak Valley.

---

## Structured Output

```yaml
cluster_1_foundational_clarity:
  paper_slug: "sobotkova-et-al-2024"
  assessment_date: "2025-11-28"
  reliability_run: 3
  quality_state: "high"
  research_approach: "deductive"

  comprehensibility:
    score: 77
    band: "good"
    strengths:
      - "Clear validation framework with prediction → test → result structure"
      - "Claims quantified and bounded (87.1% FP, 95.3% FN)"
      - "Four explicit research designs with rationale"
      - "Technical terms used consistently"
    weaknesses:
      - "Hypotheses not formally stated"
      - "Some implicit arguments (IA001-IA005)"
    rationale: "Good band for deductive. Clear validation logic, evaluable claims, transparent structure. Falls short of Excellent due to implicit hypothesis structure."

  transparency:
    score: 79
    band: "good"
    strengths:
      - "Explicit code availability with 3 GitHub repositories"
      - "Code machine actionability: high"
      - "FAIR score: 75% (highly_fair)"
      - "Comprehensive methods (7) and protocols (12)"
      - "Explicit negative results framing"
    weaknesses:
      - "Code repositories lack DOIs"
      - "Data not deposited"
      - "Some computational details missing"
    rationale: "Upper Good band for deductive. Excellent code sharing, comprehensive documentation. Falls short of Excellent due to lack of persistent identifiers and no data sharing."

  cluster_synthesis:
    overall_rating: "strong"
    pattern_summary: "Upper Good scores (77-79). Excellent code availability, comprehensive methods. Gaps in formal hypotheses and persistent identifiers."
    consistency_check: "consistent"
    implications:
      cluster_2: "Strong clarity enables confident evidential assessment."
      cluster_3: "Code supports replicability; data gaps constrain full reproducibility."
```
