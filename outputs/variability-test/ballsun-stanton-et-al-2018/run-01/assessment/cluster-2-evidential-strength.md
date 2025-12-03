# Cluster 2: Evidential Strength Assessment

**Paper:** ballsun-stanton-et-al-2018
**Assessment Date:** 2025-12-02
**Assessor Version:** v1.0

**Quality State:** HIGH
**Research Approach:** inductive (confidence: high)
**Paper Type:** methodological (software_tool)
**Context Flags:** 📦 (infrastructure), 🔧 (tool)

---

## Signal Scores Summary

| Signal | Score | Band | Approach Anchors |
|--------|-------|------|------------------|
| Plausibility | 78 | good | inductive/methodological |
| Validity | 68 | good | inductive/methodological |
| Robustness | 52 | moderate | 📦 software paper (adjusted expectations) |
| Generalisability | 72 | good | inductive/methodological |

**Cluster Rating:** Adequate

---

## Signal 3: Plausibility

**Score:** 78/100 (good)

**Approach anchors applied:** inductive/methodological

### Assessment

The paper's claims about software capabilities and design philosophy are well-grounded in established field research practices and prior work on digital data collection. The central claim that "field research disciplines, however, often lack transparency and reproducibility" (C045) is supported by citations to established literature [1,2-5,7], providing theoretical grounding for the software's motivation. The design decisions are consistent with domain knowledge about field research requirements, particularly the emphasis on offline capability ("designed for offline use, unlike most other generalised field data collection software"—E041, C038) and the need for customisation across disciplines.

The comparative positioning against existing tools (ODK, ARK, Heurist, Kora) demonstrates awareness of the software landscape and provides appropriate contextualisation. The paper acknowledges the different design lineages: "ODK was designed for social surveys... FAIMS originated in archaeology" (E007, E008, C005). This comparative grounding strengthens plausibility by showing how FAIMS addresses gaps in existing solutions.

The impact claims are generally plausible and consistent with comparable software adoption patterns. User-reported benefits (efficiency gains, data quality improvements, faster information exchange—E027-E031, C024-C028) align with documented advantages of digital recording systems in field research. The paper acknowledges anomalies, notably the challenge of time reallocation: "The greatest challenge posed by the transition from paper has been the reallocation of time from the end of a project (digitisation) to the beginning" (E034, C031).

### Evidence

**Strengths:**
- C045-C047: Problem statement grounded in cited literature [1,2-5,7] establishing field data collection challenges
- E007, E008, C005: Comparative positioning against ODK shows awareness of existing solutions and appropriate differentiation
- C031, E034: Explicit acknowledgement of challenges (time reallocation) prevents one-sided presentation
- RD001: Co-development design grounded in participatory design literature and established software development practices

**Weaknesses:**
- IA004: "Digital field recording is inherently superior to paper-based recording" — implicit assumption not fully defended; trade-offs (battery, device failure, tactile engagement) not addressed
- IA002: Economic sustainability assumptions (need for large user base) stated but not empirically validated
- Impact claims rely on self-reported user feedback without independent validation or comparison group

### Scoring Rationale

Score: 78 (Good for inductive/methodological). Patterns generally consistent with established field research frameworks (60-79 criterion); classifications reasonable against existing software tools; major challenges acknowledged (time reallocation, customisation complexity); interpretations grounded in comparative data. Does not reach excellent band (80-100) because some implicit assumptions (IA004) require stronger justification and impact validation lacks independent verification. Per inductive anchors: "Classifications reasonable; major anomalies addressed; interpretations have comparative basis."

---

## Signal 4: Validity

**Score:** 68/100 (good)

**Approach anchors applied:** inductive/methodological

### Assessment

The paper provides adequate evidence for its main claims about software capabilities and impact, though validation relies heavily on self-reported data. Technical capability claims are well-supported by explicit architectural documentation (E003, E012-E017, E038-E040) and feature specifications. The software's existence and functionality can be independently verified through the open-source repositories.

Impact claims draw on aggregate deployment statistics (40+ customisations, 29 field deployments, ~300 users, 20,000+ hours—E020-E022) and three published case studies (Sobotkova et al. 2016, referenced as E009). The case studies provide external validation, though they are authored by FAIMS team members. User feedback is presented with verbatim quotes (E029-E033), providing some traceability to source data.

The evidence-claim scope matching is generally appropriate. The paper explicitly notes that "most uptake has been at large, multi-year projects that are still early in their lifecycle" (C021) and that "the first research publications based on data generated using FAIMS will appear in 2018" (E024). These statements appropriately constrain the impact claims to current state rather than long-term demonstrated outcomes.

Limitations are partially acknowledged but focus mainly on comparison to alternatives ("In short, FAIMS is more customisable and has more fieldwork-specific features than ODK, but as a result customisation is more entailed"—C039) rather than on the evidence base for impact claims.

### Evidence

**Strengths:**
- E012-E017, E038-E040: Technical capability claims fully supported by explicit architecture documentation
- E020-E022: Deployment statistics quantify adoption scope (40+ customisations, 29 deployments, 300 users, 20,000 hours)
- E009, C007: External validation via published case studies (Sobotkova et al. 2016)
- C021, E024: Explicit acknowledgement that projects are early in lifecycle constrains claim scope appropriately

**Weaknesses:**
- E027-E034: User feedback is self-reported without independent validation; no comparison group
- All case studies authored by FAIMS team members; no independent third-party evaluation
- Aggregate statistics (E020-E022) lack demographic breakdown, error margins, or methodological detail on data collection
- M007: Requirements gathering methodology implicit—unclear how user needs were systematically captured and validated

### Scoring Rationale

Score: 68 (Good for inductive/methodological). Data sufficient for main pattern claims (adoption, technical capabilities); sampling systematic at deployment level but user feedback unsystematic; coverage adequate for software publication scope; some alternatives considered (comparison to ODK, ARK); limitations partially acknowledged; claims generally scoped to evidence. Does not reach 80-100 because validation relies on self-reported feedback and team-authored case studies; no independent evaluation or comparative baseline. Per inductive anchors: "Data sufficient for main patterns; sampling systematic; coverage adequate; some alternatives considered; limitations acknowledged; claims generally scoped."

---

## Signal 5: Robustness

**Score:** 52/100 (moderate)

**Approach anchors applied:** 📦 software paper (adjusted expectations)

### Assessment

> **📦 Context Note:** This is a software/infrastructure paper describing an artefact rather than testing hypotheses. Per cluster-2 prompt guidelines, software papers have moderate Robustness expectations (40-60 range). A moderate score reflects genre expectations, not a deficiency. The paper's job is to describe what the software does, not systematically compare it against alternatives.

The paper demonstrates moderate robustness appropriate for its genre. Software capabilities are documented through technical specification (architecture, technology stack, features) rather than systematic testing against alternatives. The paper acknowledges trade-offs between FAIMS and alternative approaches: "FAIMS is more customisable and has more fieldwork-specific features than ODK, but as a result customisation is more entailed" (C039). This represents honest documentation of limitations rather than systematic robustness testing.

Multiple deployment contexts (archaeology, ecology, geoscience, history) provide some convergent evidence that the software functions across disciplines (E023, C020), though these are presented descriptively rather than as sensitivity analyses. User feedback consistency across multiple case studies (E027-E034) suggests pattern stability, but no formal inter-observer reliability or methodological triangulation is reported.

The paper explicitly documents that "each customisation and deployment is, indeed, a miniature software development project" (C016, E018) requiring quality assurance, suggesting awareness of implementation sensitivity. QA protocols are documented (P003, E019—Robotium testing framework), providing some robustness infrastructure.

### Evidence

**Strengths:**
- C039: Explicit acknowledgement of trade-offs ("more customisable... but customisation is more entailed")
- E023, C020: Cross-disciplinary deployment (archaeology, ecology, geoscience, history) demonstrates broad applicability
- P003, E019: Documented QA testing protocol (Robotium) provides robustness infrastructure
- RD003: Case study evaluation design provides multiple observation points

**Weaknesses:**
- No systematic comparison against alternatives (ODK, ARK, Heurist) using benchmark metrics
- No formal sensitivity analysis of user adoption factors
- User feedback not triangulated with independent metrics (e.g., task completion time, error rates)
- Single software implementation—no alternative architectures tested

### Scoring Rationale

Score: 52 (Moderate for 📦 software paper). This score is **appropriate for genre**—software papers describe artefacts rather than test alternatives. Per prompt guidance: "A Moderate Robustness score (40-60) reflects genre expectations, not a deficiency." The paper meets moderate band criteria: limited but present triangulation (cross-disciplinary deployment); pattern robustness unclear but consistent across case studies; minimal formal reliability assessment; trade-offs documented. Does not reach Good band because no systematic comparison testing; reaches moderate rather than low because QA infrastructure exists and trade-offs are documented honestly.

---

## Signal 7: Generalisability

**Score:** 72/100 (good)

**Approach anchors applied:** inductive/methodological

### Assessment

The paper demonstrates good awareness of generalisability boundaries while making appropriately scoped claims. The software is explicitly positioned as "generalised software which combines features required for field research with sufficient customisability to allow its use across disciplines" (C051). Cross-disciplinary deployment evidence (archaeology, ecology, geoscience, history—E023, C020) supports this generalisation claim within the documented scope.

Scope boundaries are partially explicit. The paper notes key constraints: offline capability designed for "network-degraded environments" (E041), Android platform requirement (E004), and customisation investment requirements ("one to two developer-days"—E026, C023). The target domain is clearly field research, not laboratory or other data collection contexts.

Limitations are acknowledged for validation scope: "Most uptake has been at large, multi-year projects that are still early in their lifecycle" (C021); "FAIMS-related publications to date have focused on the software itself or the transition from paper-based to digital workflows" (C021). These statements appropriately constrain generalisation of impact claims.

Transfer conditions are partially specified through the customisation framework (definition packets, DSL approach) and documentation (Module Cookbook, User-to-Developer guide). The paper provides infrastructure for applying FAIMS to new contexts while acknowledging customisation requirements.

### Evidence

**Strengths:**
- C051: Explicit generalisation scope ("generalised software... across disciplines")
- E023, C020: Cross-disciplinary evidence (4 disciplines) supports generalisation claims
- C021: Explicit acknowledgement of early lifecycle stage constrains impact generalisation
- P001: Definition packet workflow provides explicit transfer mechanism to new contexts
- C039: Trade-off acknowledgement ("customisation is more entailed") sets appropriate expectations

**Weaknesses:**
- Geographic scope primarily Australia-focused (all 11 funders Australian); international applicability assumed but not validated
- Temporal bounds not specified—sustainability model not addressed for long-term generalisation
- IA008: Implicit assumption that field research across disciplines shares sufficient common requirements not fully defended
- No explicit discussion of contexts where FAIMS would NOT be appropriate

### Scoring Rationale

Score: 72 (Good for inductive/methodological). Pattern claims bounded by discipline (4 documented) and context (field research); sampling limitations acknowledged (early lifecycle, large projects); scope generally matched to evidence; extrapolations qualified ("can support" rather than "will transform"); constraints stated (customisation requirements, platform dependencies). Does not reach excellent band because geographic scope narrow and transfer limits not fully explored. Per inductive anchors: "Pattern claims bounded; sampling limitations acknowledged; scope generally matched; extrapolations qualified; constraints stated; limitations present."

---

## Cluster Synthesis

**Overall Evidential Strength:** Adequate

The paper demonstrates adequate evidential strength across the four credibility signals, with scores ranging from moderate (Robustness: 52) to good (Plausibility: 78, Generalisability: 72, Validity: 68). This profile is appropriate for a methodological software publication.

The strongest aspect is **Plausibility** (78)—the software design is well-grounded in field research requirements, appropriately differentiated from alternatives, and challenges are honestly acknowledged. **Generalisability** (72) is also strong, with appropriate scope boundaries and explicit acknowledgement of early-stage validation. **Validity** (68) is adequate but limited by reliance on self-reported user feedback without independent validation.

The **Robustness** score (52) reflects genre expectations for software papers, not a deficiency. The 📦 context flag correctly indicates that software papers describe artefacts rather than test hypotheses—systematic comparison against alternatives would constitute a different paper type (comparative evaluation). The moderate score is appropriate.

### Pattern Summary

The pattern across signals reflects a well-documented software publication with appropriate transparency about limitations. Plausibility and Generalisability benefit from clear scope boundaries and honest acknowledgement of constraints. Validity is limited by the validation approach (team-authored case studies, self-reported feedback) rather than evidence gaps. Robustness is genre-appropriate moderate.

Key pattern: **Claims are appropriately scoped to available evidence, but evidence base for impact claims relies on self-reported data without independent verification.** Technical capability claims are fully supported; impact claims require additional independent validation to strengthen.

### Implications for Cluster 3

- **For Reproducibility:** The excellent code availability (GPLv3, multiple repositories) enables strong reproducibility assessment. However, this is a software description paper—"reproducibility" here means whether the software can be installed and used, not whether analyses can be re-run. The standard pathway applies with focus on code/environment availability rather than analytical workflow reproduction.

---

## Structured Output

```yaml
cluster_2_evidential_strength:
  paper_slug: "ballsun-stanton-et-al-2018"
  assessment_date: "2025-12-02"
  quality_state: "high"
  research_approach: "inductive"
  paper_type: "methodological"
  context_flags: ["📦", "🔧"]

  plausibility:
    score: 78
    band: "good"
    approach_anchors_used: "inductive/methodological"
    strengths:
      - "Problem statement grounded in cited literature establishing field data collection challenges"
      - "Comparative positioning against existing tools (ODK, ARK) shows domain awareness"
      - "Challenges explicitly acknowledged (time reallocation, customisation complexity)"
      - "Design decisions consistent with established field research requirements"
    weaknesses:
      - "Implicit assumption that digital recording is inherently superior to paper (IA004)"
      - "Impact claims rely on self-reported feedback without independent validation"
    rationale: "Patterns generally consistent with frameworks; classifications reasonable; major anomalies addressed; comparative grounding present. Does not reach excellent due to implicit assumptions and self-reported validation."

  validity:
    score: 68
    band: "good"
    approach_anchors_used: "inductive/methodological"
    strengths:
      - "Technical capabilities fully documented with explicit architecture"
      - "Deployment statistics quantify adoption (40+ customisations, 29 deployments, 300 users)"
      - "External validation via published case studies"
      - "Claim scope explicitly constrained to early lifecycle stage"
    weaknesses:
      - "User feedback self-reported without independent validation or comparison group"
      - "Case studies authored by FAIMS team—no independent third-party evaluation"
      - "Aggregate statistics lack demographic breakdown or methodological detail"
    rationale: "Data sufficient for main patterns; coverage adequate; claims generally scoped to evidence. Does not reach excellent due to self-reported validation and team-authored case studies."

  robustness:
    score: 52
    band: "moderate"
    approach_anchors_used: "📦 software paper"
    context_flag: "📦"
    genre_appropriate: true
    strengths:
      - "Trade-offs explicitly acknowledged (customisation complexity)"
      - "Cross-disciplinary deployment demonstrates broad applicability"
      - "QA testing protocol documented (Robotium)"
    weaknesses:
      - "No systematic comparison against alternatives using benchmarks"
      - "User feedback not triangulated with independent metrics"
      - "Single software implementation tested"
    rationale: "Score reflects genre expectations for 📦 software papers (40-60 expected). Software papers describe artefacts, not test alternatives. Moderate score appropriate—trade-offs documented, QA exists, but no systematic comparison."

  generalisability:
    score: 72
    band: "good"
    approach_anchors_used: "inductive/methodological"
    strengths:
      - "Explicit generalisation scope stated (generalised software across disciplines)"
      - "Cross-disciplinary evidence (4 disciplines) supports scope claims"
      - "Early lifecycle stage explicitly acknowledged"
      - "Transfer mechanism documented (definition packets, DSL)"
    weaknesses:
      - "Geographic scope primarily Australian; international applicability not validated"
      - "No explicit discussion of unsuitable contexts"
      - "Long-term sustainability model not addressed"
    rationale: "Pattern claims appropriately bounded; sampling limitations acknowledged; scope matched to coverage; extrapolations qualified. Does not reach excellent due to narrow geographic validation and incomplete transfer discussion."

  cluster_synthesis:
    overall_rating: "adequate"
    pattern_summary: "Well-documented software publication with appropriate scope boundaries. Plausibility and Generalisability strong due to honest limitation acknowledgement. Validity limited by self-reported evidence base. Robustness genre-appropriate moderate."
    consistency_check: "consistent"
    implications:
      cluster_3: "Excellent code availability enables strong reproducibility assessment via standard pathway. Focus on installability and usability rather than analytical workflow reproduction."
```
