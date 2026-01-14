# Signal Cluster Assessment: Evidential Strength

## Plausibility + Validity + Robustness + Generalisability

## Paper: key-et-al-2024

**Assessment Date:** 2026-01-14
**Cluster:** 2 - Evidential Strength (Credibility Pillar)
**Research Approach:** Deductive (methodological validation)
**Quality State:** HIGH

---

## Cluster Overview

This cluster assesses the core credibility question: how much faith can we put in these results? Plausibility evaluates fit with established knowledge and theory; Validity evaluates whether evidence adequately supports claims; Robustness evaluates sensitivity to analytical choices; Generalisability evaluates appropriate scope constraints.

For a methodological paper, Evidential Strength centres on validation rigour. The key question: does the validation evidence convincingly demonstrate that OLE works for morphometric range estimation?

**Signal prioritisation for this paper:**
- **Secondary (but substantial):** Validity, Plausibility
- **Deemphasised:** Generalisability, Robustness (per classification.json)

Despite deemphasis, all signals are assessed—the methodological paper actually demonstrates strong Robustness through systematic parameter testing.

---

## Signal 3: Plausibility

**Score:** 85/100
**Confidence:** High

### Signal Definition

Does the claim align with established prior evidence and theory? Are interpretations consistent with domain knowledge?

### Assessment Summary

Key et al. (2024) demonstrates excellent plausibility. OLE is an established method from extinction dating studies with strong theoretical foundations. The application to morphometric range estimation is novel but well-justified through explicit analogy to temporal extinction estimation. Results align with theoretical expectations (accuracy improves with sample size, extreme values harder to estimate). No implausible auxiliary assumptions required.

### Key Strengths

- **Established method foundation:** OLE is grounded in peer-reviewed ecological/extinction research, not novel statistical invention
- **Explicit theoretical justification:** Paper explicitly justifies why extinction-based method should transfer to morphometrics (Section 2.1)
- **Results align with expectations:** Validation confirms intuitive predictions (C004: accuracy increases with sample; C008: minimum estimates more accurate than maximum)
- **Reasonable model assumptions:** Weibull distribution assumption explicitly justified for cultural artefacts (C022)
- **No implausible claims:** Authors appropriately qualify findings (C020: estimates are "theoretically robust predictions contingent on model assumptions")

### Key Weaknesses

- **Novel application domain:** While theoretically justified, application of extinction methods to morphometrics is novel—limited prior empirical validation
- **Assumption testability:** Model assumptions (Weibull, independence, equal discovery) are reasonable but not directly testable for archaeological data
- **Transfer uncertainty:** Some theoretical uncertainty about whether temporal extinction dynamics fully transfer to morphometric distributions

### Supporting Evidence from Extraction

**Theoretical grounding:**

- **RD001:** "Repurposing Optimal Linear Estimation (OLE) modelling from temporal extinction studies for archaeological morphometric range estimation" - Explicit theoretical lineage
- **RD004-006:** Model assumptions explicitly stated and justified
- **C022:** "Weibull-form distributions are a reasonable assumption for most cultural artefacts governed by cultural evolutionary pressures" - Theoretical justification

**Result plausibility:**

- **C004:** Accuracy increases with sample percentage - theoretically expected, empirically confirmed
- **C008:** Minimum range estimates more accurate than maximum - consistent with extinction estimation literature
- **C007:** k=5 optimal - consistent with prior OLE research recommendations (C021)
- **C024:** Accuracy correlates with distribution shape - theoretically coherent

**Appropriate qualification:**

- **C020:** "OLE estimates should be treated as theoretically robust predictions contingent on model assumptions being met, not as proof that extreme morphologies were definitively created in the past" - Appropriate epistemic caution

### Scoring Justification

Scored 85 (Excellent Plausibility for deductive research). This paper meets 80-100 anchor criteria:
- ✅ "Hypotheses grounded in established theory" - OLE method from extinction studies
- ✅ "Predictions consistent with domain knowledge" - Results align with theoretical expectations
- ✅ "Anomalous results acknowledged and explained" - Distribution shape effects noted (C024)
- ✅ "Theoretical framework coherent and well-established" - OLE framework robust
- ✅ "No implausible auxiliary assumptions required" - Model assumptions reasonable

Slight reduction from 90-100 because application domain is novel—while theoretically justified, this represents first comprehensive validation of OLE for morphometrics.

### Approach-Specific Context

**Research Approach:** Deductive (methodological validation)

For deductive research, Plausibility emphasises theoretical grounding of hypotheses. This methodological paper excels by building on established extinction estimation methods rather than inventing novel statistics. The validation hypotheses are theoretically motivated, and results align with predictions derived from OLE theory.

---

## Signal 4: Validity

**Score:** 87/100
**Confidence:** High

### Signal Definition

Are methods appropriate for the research question and claims adequately supported by evidence?

### Assessment Summary

Key et al. (2024) demonstrates excellent validity through rigorous validation design. The core innovation—using replica assemblages with known complete distributions as ground truth—provides definitive test of OLE accuracy. Evidence directly addresses validation hypotheses: 64 parameter combinations tested across 1000 iterations each, with systematic exploration of k-values, sample percentages, and assemblage types.

### Key Strengths

- **Ground truth validation:** Replica assemblages (n=500 handaxes, n=45 archaic points) provide known complete distributions for accuracy testing (RD002)
- **Systematic parameter testing:** 64 combinations (4 k-values × 4 sample percentages × 2 bounds) systematically explored
- **Adequate iteration:** 1000 iterations per combination ensures statistical stability
- **Alternative hypotheses tested:** Effects of k-values (C007), sample size (C009), distribution shape (C024) explicitly investigated
- **Confound control:** Duplicate handling tested (C016: "little-to-no impact")
- **Sample size adequacy:** n=500 and n=45 assemblages bracket realistic archaeological sample sizes

### Key Weaknesses

- **Replica vs archaeological samples:** Validation uses controlled replica assemblages—transfer to archaeological assemblages with unknown true distributions not directly testable
- **Two assemblage types only:** Validation based on handaxes and archaic points; ceramics and other materials not included in validation (only case studies)
- **CI coverage threshold:** 0.8 coverage accepted as "broadly acceptable" (C009) though below theoretical 0.95—rationale could be stronger

### Supporting Evidence from Extraction

**Validation design:**

- **RD002:** "Blind test validation design using replica assemblages with known complete distributions as ground truth"
- **E001:** n=500 replica handaxes validation assemblage
- **E002:** n=45 archaic points validation assemblage

**Evidence-claim alignment:**

| Claim | Supporting Evidence | Adequacy |
|-------|---------------------|----------|
| C001 (OLE accuracy) | E017-E022 (validation results) | Strong - direct test |
| C004 (accuracy vs sample) | E017-E018 (accuracy matrices) | Strong - systematic test |
| C007 (k=5 optimal) | E019 (CI coverage by k) | Strong - systematic comparison |
| C010 (case study extensions) | E023-E034 (case study results) | Strong - 10 datasets |

**Evidence sufficiency:**

- Evidence-claim ratio: 1.125:1 (27 evidence items supporting 24 claims)
- Validation evidence: 6 items directly supporting validation claims
- Case study evidence: 12 items supporting demonstration claims

### Scoring Justification

Scored 87 (Excellent Validity for deductive research). This paper meets 80-100 anchor criteria:
- ✅ "Evidence directly addresses hypothesis" - Replica assemblage validation tests OLE accuracy directly
- ✅ "Sample size and power adequate" - n=500 and n=45 with 1000 iterations
- ✅ "Methods appropriate for testing predictions" - Blind test design appropriate
- ✅ "Alternative hypotheses explicitly tested" - k-values, sample sizes, distribution shapes tested
- ✅ "Confounds controlled or acknowledged" - Duplicate handling, distribution shape effects assessed
- ✅ "Limitations and threats to validity stated" - Model assumptions and interpretation limits explicit

Slight reduction because validation assemblages limited to two types (handaxes, archaic points) and transfer to non-replica archaeological assemblages not directly testable.

### Approach-Specific Context

**Research Approach:** Deductive (methodological validation)

For deductive research, Validity emphasises evidence-hypothesis alignment and alternative hypothesis testing. This paper exemplifies deductive validity by designing validation tests that directly measure OLE accuracy against known truth—the strongest possible test design for method validation.

---

## Signal 5: Robustness

**Score:** 82/100
**Confidence:** High

### Signal Definition

Would results hold under different reasonable analytical approaches? Are conclusions sensitive to specific methodological choices?

### Assessment Summary

Key et al. (2024) demonstrates good-to-excellent robustness through systematic sensitivity analysis. The validation systematically varies k-values (5, 10, 20, 30), sample percentages (5%, 10%, 20%, 50%), and tests across two different assemblage types. Core findings (OLE provides accurate estimates, accuracy improves with sample size) are robust across these variations. The 10 case studies provide additional triangulation across diverse materials and contexts.

### Key Strengths

- **Systematic k-value testing:** Four k-values tested (5, 10, 20, 30) with consistent results (P003)
- **Systematic sample percentage testing:** Four percentages tested (5%, 10%, 20%, 50%) (P002)
- **Multi-assemblage validation:** Two distinct replica assemblages (handaxes n=500, archaic points n=45)
- **Results robust across variations:** Core findings consistent across parameter space
- **Case study triangulation:** 10 diverse case studies across lithic, ceramic, metal, human/hominin/primate contexts

### Key Weaknesses

- **Single statistical method:** OLE only—no comparison to alternative range estimation methods
- **Bootstrap or cross-validation not employed:** Validation relies on repeated sampling rather than formal bootstrap
- **Single implementation:** R implementation only—no comparison to alternative software implementations
- **Distribution sensitivity:** Paper notes accuracy varies with distribution shape (C024) but doesn't systematically test across distribution types

### Supporting Evidence from Extraction

**Sensitivity analyses:**

- **P002:** Subsampling at 5%, 10%, 20%, 50%
- **P003:** k-values of 5, 10, 20, 30
- **P004:** 1000 iterations per combination
- **E017-E019:** Results reported across parameter combinations

**Robustness indicators:**

- **C004:** Accuracy increases with sample percentage - consistent pattern across k-values
- **C007:** k=5 optimal across both assemblages
- **C008:** Minimum more accurate than maximum - consistent across conditions
- **C016:** Results robust to duplicate handling

**Triangulation:**

- **E007:** 10 case studies across diverse contexts (lithic, ceramic, metal)
- **C010:** Range extension pattern consistent across all case studies

### Scoring Justification

Scored 82 (Excellent Robustness for deductive research). This paper meets 80-100 anchor criteria:
- ✅ "Sensitivity analyses performed (varying parameters, methods)" - Systematic k and percentage variation
- ✅ "Results robust across reasonable analytical choices" - Core findings consistent
- ✅ "Assumptions validated or tested" - Distribution effects explored (C024)
- ✅ "Dependencies on choices clearly documented" - Parameter recommendations explicit (C021)
- ✅ "Robustness checks reported" - Full results across parameter space

Reduction from 90-100 because:
- ❌ "Alternative statistical approaches tested" - OLE only, no comparison methods
- No formal bootstrap validation

Note: Robustness is deemphasised for methodological papers per classification framework, but this paper actually performs well on this signal through systematic parameter testing.

### Approach-Specific Context

**Research Approach:** Deductive (methodological validation)

For deductive research, Robustness emphasises sensitivity analysis and assumption testing. While typically deemphasised for methods papers (where the focus is "does the method work?" not "is it robust to alternatives?"), Key et al. actually provides strong robustness evidence through systematic parameter space exploration.

---

## Signal 6: Generalisability

**Score:** 76/100
**Confidence:** High

### Signal Definition

Can findings transfer to other contexts? Are claims carefully constrained by place, time, and context? Are limitations explicitly acknowledged?

### Assessment Summary

Key et al. (2024) demonstrates good generalisability through appropriate scope constraint. The paper explicitly bounds claims to artefacts meeting model assumptions, provides diverse case study demonstration (10 contexts spanning 1.8 million years), but appropriately does not overclaim universal applicability. For a methodological paper, the emphasis is on demonstrating breadth while acknowledging constraints—this paper achieves that balance.

### Key Strengths

- **Explicit scope limitations:** C020 clearly states OLE estimates are "contingent on model assumptions being met"
- **Model assumption constraints:** Three assumptions (Weibull, independence, equal discovery) define applicability domain
- **Diverse demonstration:** 10 case studies across lithic, ceramic, metal; human, hominin, primate; 1.8 Ma timespan
- **No overclaiming:** Paper demonstrates applicability without claiming OLE works universally
- **Transfer conditions specified:** Paper specifies when OLE more/less appropriate (C24: distribution shape effects)

### Key Weaknesses

- **Validation scope narrower than application:** Validation based on lithic replicas; case studies include ceramics and metals not directly validated
- **Cultural-evolutionary assumption:** C022 assumes Weibull applies to "cultural artefacts governed by cultural evolutionary pressures"—may not hold for all artefact types
- **Geographic scope of case studies:** All case studies from published Western/African datasets; global applicability assumed but not demonstrated

### Supporting Evidence from Extraction

**Scope constraints:**

- **C020:** "OLE estimates should be treated as theoretically robust predictions contingent on model assumptions being met, not as proof that extreme morphologies were definitively created"
- **RD004-006:** Model assumptions define applicability boundaries

**Breadth demonstration:**

- **RD003:** "Multi-material case study design covering lithic, ceramic, and metal artefacts across humans, extinct hominins, and non-human primates"
- **E007 (consolidated):** 10 case studies with diverse samples (n=18 to n=1047)

**Temporal scope:**

- Case studies span: Gona (~2.6-1.5 Ma) to historical copper points
- Demonstrates applicability across archaeological time periods

### Scoring Justification

Scored 76 (Good Generalisability for deductive research). This paper meets 60-79 anchor criteria:
- ✅ "Hypothesis scope stated" - Model assumptions define scope
- ✅ "Main limitations acknowledged" - C020 explicit about interpretation limits
- ✅ "Bounds mostly clear" - Weibull, independence, equal discovery constraints
- ✅ "Extrapolations qualified" - Case studies framed as demonstration, not proof

Does not reach 80-100 because:
- Validation scope (lithic replicas) narrower than application scope (lithic + ceramic + metal)
- Transfer conditions for ceramics/metals not formally tested

Note: Generalisability is deemphasised for methodological papers—the priority is demonstrating method validity, not claiming universal applicability. Score reflects appropriate constraint rather than limitation.

### Approach-Specific Context

**Research Approach:** Deductive (methodological validation)

For methodological papers, Generalisability assessment focuses on whether scope is appropriately bounded rather than whether findings transfer broadly. The goal is method adoption, which requires demonstrating breadth while acknowledging constraints. This paper appropriately constrains claims to artefacts meeting model assumptions while demonstrating breadth through diverse case studies.

---

## Cross-Signal Coherence Check

**Do the signals in this cluster cohere?**

Yes. The signal scores form a coherent pattern:

| Signal | Score | Coherence Analysis |
|--------|-------|-------------------|
| Plausibility | 85 | Strong theoretical grounding supports high validity |
| Validity | 87 | Rigorous validation enables confidence in robustness claims |
| Robustness | 82 | Systematic testing confirms validity findings stable |
| Generalisability | 76 | Appropriate constraint acknowledges validation scope limits |

**Pattern:** High core credibility (Plausibility, Validity) with good robustness testing and appropriate scope constraint. The slight Generalisability gap reflects deliberate scope limitation rather than methodological weakness.

**Expected relationships confirmed:**
- High Validity + High Plausibility: Theoretically grounded method performs as expected
- High Robustness (despite deemphasis): Systematic testing confirms findings not fragile
- Moderate Generalisability (deemphasised): Appropriate for methods paper—scope constraint is a feature

**Unexplained tensions:** None. All signals cohere with methodological paper expectations.

---

## Cluster Summary

**Overall Assessment:** Evidential Strength is strong

**Primary Strengths:**

1. Ground truth validation design provides definitive accuracy testing
2. Strong theoretical foundation in established extinction estimation methods
3. Systematic sensitivity analysis across parameter space
4. Appropriate scope constraint with explicit model assumptions
5. Diverse case study demonstration without overclaiming

**Primary Weaknesses:**

1. Validation scope limited to lithic replicas (ceramics/metals in case studies only)
2. No comparison to alternative range estimation methods
3. Transfer from replica to archaeological assemblages not directly testable

**Implications for Overall Credibility:**

Strong Evidential Strength supports confidence in the paper's core claim that OLE provides accurate morphometric range estimates. The validation design (ground truth testing) is as rigorous as possible for method validation. Appropriate scope constraints acknowledge that validation evidence, while strong, has boundaries.

---

## Assessment Metadata

**Assessor:** research-assessor skill v2.1
**Assessment Date:** 2026-01-14
**Approach-Specific Anchors Applied:** Yes (deductive research anchors)
**Quality State:** HIGH
