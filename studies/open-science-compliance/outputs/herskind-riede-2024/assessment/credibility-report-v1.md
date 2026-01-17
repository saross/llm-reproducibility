# Credibility Assessment Report

## Herskind & Riede (2024)

**Paper:** "A computational linguistic methodology for assessing semiotic structure in prehistoric art and the meaning of southern Scandinavian Mesolithic ornamentation"

**Journal:** Journal of Archaeological Science (2024)

**Assessment Date:** 2026-01-17

**Quality State:** HIGH (full assessment with approach-specific anchors)

---

## Executive Summary

This paper presents a novel computational linguistic methodology for investigating semiotic structure in prehistoric art, demonstrated through a case study of South Scandinavian Mesolithic portable art (483 objects). The primary finding is that this corpus shows no evident semiotic structure — the art was likely not a form of proto-writing — though tentative patterns emerge in the Late Mesolithic Ertebølle period.

**Overall Credibility Assessment: GOOD**

The paper achieves good-to-excellent scores across credibility signals, with particular strengths in methodological transparency, comprehensibility, and computational reproducibility. For a methodological paper, these are the primary assessment criteria — and the paper meets them well. Minor weaknesses in robustness (no sensitivity testing) and validity (classification reliability not tested) are appropriate for an initial method demonstration.

### Signal Profile

| Signal | Score | Band | Confidence |
|--------|-------|------|------------|
| Comprehensibility | 83 | Excellent | High |
| Transparency | 82 | Excellent | High |
| Plausibility | 78 | Good | High |
| Validity | 72 | Good | High |
| Robustness | 55 | Moderate | Medium |
| Generalisability | 70 | Good | High |
| Reproducibility | 80 | Excellent | High |

**Mean score:** 74.3/100

**Cluster breakdown:**

- **Foundational Clarity** (Comprehensibility + Transparency): 82.5 average — Excellent
- **Evidential Strength** (Plausibility + Validity + Robustness + Generalisability): 68.8 average — Good
- **Reproducibility** (Reproducibility): 80 — Excellent

---

## Research Approach and Framework

**Research Approach:** Inductive (methodological paper with case study demonstration)

**Classification Confidence:** High

The paper is a methodological contribution presenting a novel approach (skipgram + PMI) for analysing prehistoric art. The case study serves a demonstrative function — validating the method through descriptive findings rather than hypothesis testing. This inductive validation approach is appropriate for novel methodology papers.

**Assessment Framework Applied:** Methodological paper with inductive emphasis

**Signal Prioritisation:**

- **Primary signals:** Transparency, Reproducibility, Comprehensibility
- **Secondary signals:** Validity, Plausibility
- **Deemphasised signals:** Generalisability, Robustness

This prioritisation reflects that for methodological papers, the core credibility question is: "Can others understand, evaluate, and apply the method?"

---

## Pillar 1: Transparency (Foundational Clarity)

### Comprehensibility (83/100)

**Assessment:** Excellent clarity for a computational methodology paper.

The paper achieves excellent comprehensibility through:

- Explicit dual research goals (presenting method + demonstrating capability)
- Well-defined technical terminology (skipgram, PMI, n-gram)
- Carefully bounded pattern claims ("no evident semiotic structure" in this specific corpus)
- Traceable argument structure from evidence through intermediate claims to core conclusions
- Clear distinction between methodological claims and empirical findings

Minor limitations include assumed archaeological domain knowledge and an implicit justification for interpretive transitions from rejecting semiotic structure to proposing socio-political explanations.

### Transparency (82/100)

**Assessment:** Excellent methodological documentation.

Strong transparency is demonstrated through:

- Explicit framing as exploratory/demonstrative research
- Comprehensive documentation of data source (Płonka 2003 catalogue) and transformation procedures
- Clear analysis workflow with documented parameters (R v4.2.2, Quanteda, k=13)
- Open data and code availability in Zenodo with DOIs
- Thorough acknowledgement of limitations (6 implicit assumptions documented)

Gaps include missing computational environment containerisation, no explicit licence for deposited materials, and classification scheme not independently validated.

### Pillar 1 Summary

**Average Score:** 82.5/100 (Excellent)

The paper establishes an excellent foundation for credibility assessment. Methodological documentation is comprehensive, the argument is clearly structured, and materials are openly available for verification.

---

## Pillar 2: Credibility (Evidential Strength)

### Plausibility (78/100)

**Assessment:** Good theoretical grounding and appropriate interpretations.

The method is grounded in established computational linguistics (skipgram, PMI) with theoretical basis in Bouissac's semiotic framework. The null finding (no evident semiotic structure) is consistent with archaeological domain expectations for Mesolithic art. Interpretations are appropriately hedged with modal language.

Limitations include untested methodological assumptions (binary encoding sufficiency, statistical independence) and speculative socio-political interpretations for the Ertebølle cluster.

### Validity (72/100)

**Assessment:** Good case study validation with acknowledged limitations.

The substantial corpus (483 objects, nearly half of European Mesolithic portable art) provides adequate statistical power. The method's technical capability is demonstrated through successful generation of n-gram frequencies and PMI values. Limitations are explicitly acknowledged.

Gaps include reliance on typological dating rather than direct radiocarbon dates, unvalidated classification scheme (inter-coder reliability not tested), and a single case study limiting validation scope.

### Robustness (55/100)

**Assessment:** Moderate, appropriate for initial method demonstration.

The analysis uses a single analytical pipeline without sensitivity testing or alternative method comparison. This is acknowledged as a limitation — the goal is demonstrating capability, not exhausting variations. Parameters (k=13, binary encoding, Płonka classification) are documented but not varied.

**Contextual note:** For novel method papers, robustness is appropriately deemphasised. Future work could address this through sensitivity analysis and cross-corpus validation.

### Generalisability (70/100)

**Assessment:** Good scope constraints with appropriately bounded claims.

Case study findings are carefully constrained to the South Scandinavian Mesolithic corpus. Temporal and spatial scope is explicit. The methodological claim about transferability (C004) is framed as potential rather than demonstrated. The paper appropriately distinguishes case study findings from method capabilities.

Limitations include method transferability being claimed but not demonstrated and sample representativeness being assumed rather than examined.

### Pillar 2 Summary

**Average Score:** 68.8/100 (Good)

The evidential strength is appropriate for a methodological demonstration paper. The method is plausibly grounded, the case study is adequate for initial validation, and claims are appropriately bounded. Lower robustness reflects appropriate deemphasis for novel methods.

---

## Pillar 3: Reproducibility

### Reproducibility (80/100)

**Assessment:** Excellent computational reproducibility for a 2024 methodology paper.

Strong reproducibility infrastructure includes:

- Data openly archived in Zenodo with DOIs
- Code openly archived in Zenodo
- R version (4.2.2) and primary package (Quanteda) documented
- Clear workflow description enabling independent verification
- Expected outputs documented for comparison (Tables 1-2, Figures 3-5)

Gaps include no computational environment containerisation, incomplete dependency specification, missing licence for deposited materials, and no author ORCIDs.

**Reproducibility Readiness:** Ready

A researcher with R programming experience could plausibly reproduce the analysis with moderate effort. The main risk is package version incompatibility over time.

**FAIR Assessment:** 10/16 (62.5%, "moderately_fair")

### Pillar 3 Summary

**Score:** 80/100 (Excellent)

Excellent reproducibility strongly supports the paper's credibility as a methodological contribution. The open availability of data and code enables verification, reproduction, and extension.

---

## Methodological Considerations

### Strengths of the Research Design

1. **Clear method-case study separation:** The paper distinguishes what the method can do from what this specific case study shows
2. **Appropriate null finding:** Absence of semiotic structure is a legitimate finding, not a failure
3. **Computational grounding:** Adaptation of established techniques (skipgram, PMI) to archaeological data
4. **Transparent limitations:** Six implicit assumptions explicitly documented and discussed

### Areas for Future Development

1. **Positive validation:** Apply method to corpora with known semiotic structure to validate detection capability
2. **Sensitivity analysis:** Vary analytical parameters (k value, n-gram lengths, classification granularity)
3. **Inter-coder reliability:** Test classification scheme consistency
4. **Direct dating:** Obtain radiocarbon dates for chronological pattern claims
5. **Cross-corpus validation:** Apply to other regional or temporal corpora

### Implicit Assumptions

The extraction identified six implicit assumptions that affect interpretation:

| ID | Assumption | Implication |
|----|------------|-------------|
| IA001 | Classification adequacy | Pattern detection depends on Płonka scheme reliability |
| IA002 | Typological dating accuracy | Chronological patterns may reflect dating artefacts |
| IA003 | Sample representativeness | Corpus assumed to represent broader practices |
| IA004 | PMI interpretation | Positive PMI assumed to indicate meaningful combination |
| IA005 | Statistical independence | Independence assumed despite cultural transmission |
| IA006 | Binary encoding sufficiency | Repetition and arrangement information discarded |

These assumptions are acknowledged in the paper but limit confidence in archaeological conclusions.

---

## Infrastructure Quality

### Open Science Practices

| Practice | Status | Notes |
|----------|--------|-------|
| Data availability | ✓ Excellent | Zenodo with DOI |
| Code availability | ✓ Excellent | Zenodo with DOI |
| Pre-registration | ✗ N/A | Appropriate for exploratory methods paper |
| ORCIDs | ✗ Missing | Not present in paper text |
| Licence | ✗ Unclear | Not stated for deposited materials |
| CReDIT statement | ✓ Present | Full author contributions |
| Funding statement | ✓ Present | "No funding sources involved" |

### FAIR Score Breakdown

| Principle | Score | Notes |
|-----------|-------|-------|
| Findable | 3/4 | Zenodo DOI; missing domain-specific indexing |
| Accessible | 3/4 | Open access; Zenodo persistence unclear |
| Interoperable | 2/4 | Custom classification; no controlled vocabulary |
| Reusable | 2/4 | Missing licence; no community standards |
| **Total** | **10/16** | **62.5% (moderately FAIR)** |

---

## Assessment Confidence

**Overall Confidence:** High

Factors supporting high confidence:

- Comprehensive extraction (29 evidence, 33 claims, 6 implicit arguments, 6 designs, 8 methods, 9 protocols)
- All extraction passes completed with validation
- Clear research approach classification (inductive methodological paper)
- No major extraction gaps or classification ambiguities
- Strong metric-signal alignment

**No quality caveats required.**

---

## Conclusions

### Principal Finding

Herskind & Riede (2024) presents a credible methodological contribution to archaeological research. The skipgram + PMI approach offers a novel, computationally reproducible method for investigating semiotic structure in prehistoric art. The case study demonstrates the method's technical capability while producing a plausible archaeological finding (no evident semiotic structure in South Scandinavian Mesolithic portable art).

### Credibility Profile

**Primary strengths (supporting credibility):**

- Excellent methodological transparency and comprehensibility
- Strong computational reproducibility with openly available data and code
- Appropriate theoretical grounding in computational linguistics
- Carefully bounded claims with explicit limitations

**Primary limitations (qualifying credibility):**

- Single case study without sensitivity testing or positive validation
- Data quality limitations (typological dating, unvalidated classification)
- Methodological assumptions not empirically examined
- Method transferability claimed but not demonstrated

### Appropriate Use of This Research

**For method application:**

- The skipgram + PMI approach is well-documented and reproducible
- Researchers can apply the method to other corpora
- Caution warranted regarding classification scheme reliability

**For archaeological interpretation:**

- The null finding (no semiotic structure) is specific to this corpus
- Chronological patterns (Ertebølle cluster) are tentative given dating limitations
- Socio-political interpretations are speculative

**For citation:**

- Appropriate to cite for methodological innovation
- Archaeological conclusions should be cited with noted limitations

### Final Assessment

**Credibility rating:** GOOD

This paper successfully achieves its primary goal — demonstrating a novel computational methodology for investigating prehistoric art. The transparent documentation, open materials, and appropriate scoping of claims support credibility. Minor limitations in robustness and validity are appropriate for an initial method demonstration and represent opportunities for future development rather than fundamental flaws.

---

## Assessment Metadata

**Assessor:** research-assessor skill v0.2-alpha
**Assessment Date:** 2026-01-17
**Assessment Type:** Standard (HIGH quality state)
**Extraction Source:** extraction.json (Pass 7 validated)
**Classification Source:** classification.json (Pass 8 complete)
**Report Version:** v1
