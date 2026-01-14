# Signal Cluster Assessment: Foundational Clarity

## Comprehensibility + Transparency

## Paper: key-et-al-2024

**Assessment Date:** 2026-01-14
**Cluster:** 1 - Foundational Clarity (Transparency Pillar)
**Research Approach:** Deductive (methodological validation)
**Quality State:** HIGH

---

## Cluster Overview

This cluster assesses how clearly the research is communicated. Comprehensibility evaluates clarity of claims and argument structure; Transparency evaluates completeness of research design and methods documentation. These signals are foundational because poor comprehensibility undermines ability to evaluate transparency, and together they underpin assessment of all other credibility signals.

For a methodological paper like Key et al. (2024), Foundational Clarity is especially important—the paper's primary contribution is a method, so clear communication and thorough documentation are essential for adoption and replication.

---

## Signal 1: Comprehensibility

**Score:** 88/100
**Confidence:** High

### Signal Definition

Are claims clear, explicit, and well-structured? Can readers understand what is being claimed and on what basis?

### Assessment Summary

Key et al. (2024) demonstrates excellent comprehensibility for a methodological paper. Core claims are explicitly stated with clear boundaries, technical terminology is defined, and the logical structure from validation to case studies is transparent. The paper's argument flow—presenting OLE, justifying its application to morphometrics, validating against ground truth, and demonstrating through case studies—is exemplary.

### Key Strengths

- **Explicit core claims:** C001 ("OLE modelling provides broadly accurate estimates") and C002 ("OLE can be applied across lithic, ceramic, and metal artefacts") are stated clearly with explicit scope
- **Defined terminology:** Key terms (OLE, confidence interval coverage, k-values, Weibull distribution) are operationally defined in Methods section
- **Clear hypothesis specification:** Validation component has explicit testable predictions (C004: "accuracy increases with sample percentage"; C007: "k=5 less likely to underestimate")
- **Transparent argument structure:** Logical progression from theoretical justification → validation → case studies → discussion is traceable
- **Bounded scope:** Paper explicitly states limitations (C020: "estimates should be treated as theoretically robust predictions contingent on model assumptions")

### Key Weaknesses

- **Domain-specific terminology:** Some archaeological terms (handaxe, cleaver, bipolar core) assumed familiar—appropriate for target audience but may limit accessibility to non-specialists
- **Statistical terminology density:** High density of statistical concepts may challenge readers without quantitative background
- **Implicit theoretical framework:** While OLE is well-explained, the theoretical rationale for why extinction-based methods should transfer to morphometrics could be more explicit

### Supporting Evidence from Extraction

**Claim structure analysis:**

- **Core claims (5):** C001, C002, C004, C010, C013 - All explicitly stated with clear scope
- **Intermediate claims (8):** C006-C009, C012, C014, C018, C020-C021, C024 - Support core claims with specific findings
- **Supporting claims (8):** C003, C005, C011, C015-C017, C019, C022-C023 - Provide methodological context

**Argument flow:**

1. Introduction establishes problem (fragmentary archaeological record)
2. Section 2.1-2.2 presents OLE and model assumptions (RD004-RD006)
3. Section 2.3 describes validation design (RD002) with explicit hypothesis
4. Section 2.4 describes case study design (RD003)
5. Results report validation findings (E017-E022) then case study findings (E023-E034)
6. Discussion synthesises and bounds interpretations (C020)

### Scoring Justification

Scored 88 (Excellent Comprehensibility for deductive research). This paper meets all 80-100 anchor criteria:
- ✅ "Hypotheses explicitly stated and clearly bounded" - Validation hypotheses explicit (C004-C009)
- ✅ "All key terms operationally defined" - OLE, CI coverage, k-values defined in Section 2
- ✅ "Logical structure of hypothesis testing transparent" - Clear progression through validation
- ✅ "Claims unambiguous and testable" - Core claims are specific and assessable
- ✅ "Reasoning from test results to conclusions clear" - Discussion carefully bounds conclusions

Minor reduction from 90-100 range due to dense statistical terminology and some domain-specific assumptions about audience familiarity.

### Approach-Specific Context

**Research Approach:** Deductive (methodological validation)

For deductive research, Comprehensibility emphasises hypothesis clarity and logical structure. This paper exemplifies deductive clarity by explicitly stating what the validation tests will measure (OLE accuracy, CI coverage), how success is defined (C005: "perfect CI coverage equals 0.95"), and what the results mean for the method's validity.

The mixed inductive component (case studies) is appropriately framed as demonstration rather than hypothesis testing, avoiding category confusion.

### Relevant Metrics

Formal metrics not computed. Proxy indicators:

- **Claims with explicit scope:** 24/24 (100%)
- **Core claims with clear boundaries:** 5/5 (100%)
- **Defined terminology density:** High (OLE, CI, k, Weibull defined explicitly)

---

## Signal 2: Transparency

**Score:** 78/100
**Confidence:** High

### Signal Definition

Are research methods and procedures well-documented and reproducible? Can others understand and critically evaluate the research design?

### Assessment Summary

Key et al. (2024) demonstrates good-to-excellent transparency in research design and methods documentation. The paper provides exceptionally detailed protocols (12 documented), explicit model assumptions (RD004-RD006), and complete specification of validation procedures. However, code and data are available only through publisher supplementary materials rather than dedicated repositories, limiting machine-actionability and long-term preservation.

### Key Strengths

- **Explicit design statement:** Clear separation between validation (RD002) and case studies (RD003)
- **Comprehensive protocol documentation:** 12 protocols covering software (P001), sampling (P002), parameters (P003, P005), iterations (P004), CI calculation (P006), replica production (P007-P008), measurement (P009), data filtering (P010), and resampling (P012)
- **Documented model assumptions:** Three statistical assumptions explicitly stated (RD004: Weibull; RD005: independence; RD006: equal discovery probability)
- **Documented software environment:** "All analyses were undertaken in R version 4.3.0" (P001)
- **Code availability:** R scripts for validation and case study analyses provided in supplementary
- **Explicit limitations:** Paper states conditions under which estimates may be less accurate (C020, C024)

### Key Weaknesses

- **Supplementary-only code/data:** Code and data in publisher supplementary materials rather than dedicated repositories (GitHub, Zenodo)
- **No separate DOIs:** No persistent identifiers for code or data beyond paper DOI
- **Limited machine-actionability:** FAIR assessment shows low machine-actionability rating for code and data
- **Missing kernel density parameters:** One implicit protocol (P-IMP-001) identified—kernel density visualisation parameters not specified
- **No author ORCIDs:** Author identifiers not included in PDF

### Supporting Evidence from Extraction

**Research design documentation:**

- **RD001:** Methodological framework explicitly stated ("repurposing OLE modelling")
- **RD002:** Validation design documented ("blind test validation using replica assemblages")
- **RD003:** Case study design documented ("multi-material... across humans, extinct hominins, and non-human primates")

**Methods documentation:**

- **M001-M004:** Validation methods with clear specifications
- **M005:** Data quality control (duplicate handling)
- **M006:** Measurement approach

**Protocol specificity:**

- **P002:** Subsampling procedure (5%, 10%, 20%, 50%)
- **P003:** k-value specification (5, 10, 20, 30)
- **P004:** Iteration specification (1000 iterations)
- **P006:** CI coverage calculation procedure

**FAIR assessment summary (from Pass 6):**

- Total FAIR score: 9/15 (60%)
- Findable: 2/4 (paper DOI only, no dataset/code DOIs)
- Accessible: 4/4 (open access CC BY)
- Interoperable: 0/3 (no formal schemas or qualified links)
- Reusable: 3/4 (provenance documented, no CodeMeta)

### Scoring Justification

Scored 78 (Good Transparency for deductive research). This paper meets 60-79 anchor criteria:
- ✅ "Clear research design and hypothesis specification" - RD001-RD003 explicitly documented
- ✅ "Detailed methods documentation" - 12 protocols, 6 methods with complete specifications
- ✅ "Data availability clearly stated" - Supplementary data referenced with CC BY licence
- ✅ "Code or analysis workflow documented" - R scripts provided, R version specified
- ✅ "Major limitations acknowledged" - Model assumptions and interpretation constraints stated

Does not reach 80-100 because:
- ❌ "Data and code publicly available with persistent identifiers" - No separate DOIs for code/data
- ❌ "Pre-registered study design" - No pre-registration (not unusual for methods paper, but noted)

For a 2024 methods paper, dedicated repository archiving with DOIs would be expected for top-tier transparency.

### Approach-Specific Context

**Research Approach:** Deductive (methodological validation)

For deductive research, Transparency emphasises pre-specification, methods documentation, and data/code sharing. While this paper lacks formal pre-registration (not expected for methods papers), it compensates with exceptionally detailed methods documentation. The 12 protocols documented allow reconstruction of all analytical procedures.

The emphasis for methodological papers shifts slightly from pre-registration to method specification completeness—this paper excels in the latter.

### Relevant Metrics

From FAIR assessment:

- **FAIR score:** 60% (moderately FAIR)
- **Machine-actionability:** Low
- **Protocol documentation:** 12 explicit protocols (96% explicit RDMAP)
- **Code availability:** Yes (supplementary)
- **Data availability:** Yes (supplementary)
- **Environment specification:** Partial (R version stated, packages not listed)

---

## Cross-Signal Coherence Check

**Do the signals in this cluster cohere?**

Yes. Comprehensibility (88) and Transparency (78) are both strong and directionally consistent. The 10-point gap is explained by a coherent pattern:

- **Communication clarity:** Excellent (explains high Comprehensibility)
- **Methods documentation:** Excellent (contributes to both signals)
- **Infrastructure quality:** Good but not optimal (explains Transparency score ceiling)

The paper communicates clearly and documents methods thoroughly, but falls short of optimal transparency standards for 2024 due to supplementary-only code/data sharing. This is not a coherence issue—it reflects the distinct aspects each signal measures.

**Unexplained tensions:** None identified.

---

## Cluster Summary

**Overall Assessment:** Foundational Clarity is strong

**Primary Strengths:**

1. Exceptionally clear argument structure from validation to case studies
2. Comprehensive methods documentation enabling critical evaluation
3. Explicit model assumptions and limitations
4. All core claims bounded and testable

**Primary Weaknesses:**

1. Code and data not archived in dedicated repositories with DOIs
2. Limited machine-actionability for reuse
3. Dense statistical terminology may limit accessibility

**Implications for Overall Credibility:**

Strong Foundational Clarity supports credible assessment of other signals. The paper's clear communication allows confident evaluation of Validity and Robustness; the thorough documentation enables assessment of Reproducibility. No concerns that poor comprehensibility or transparency might be masking methodological issues.

---

## Assessment Metadata

**Assessor:** research-assessor skill v2.1
**Assessment Date:** 2026-01-14
**Approach-Specific Anchors Applied:** Yes (deductive research anchors)
**Quality State:** HIGH
