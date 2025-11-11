# The Seven repliCATS Credibility Signals: HASS Adaptation Guide

## Overview

The repliCATS project (Collaborative Assessment for Trustworthy Science) developed a structured framework for assessing research credibility through seven distinct signals. Originally designed for social and behavioral sciences, these signals are being adapted for humanities and social sciences (HASS) research, particularly archaeology and interpretive scholarship.

**Key Innovation:** While repliCATS relied on human experts to mentally extract relevant features and provide assessments, the LLM-assisted approach automates the extraction of structured knowledge (Claims-Evidence-Methods graphs, RDMAP) and uses that structured data to assess credibility systematically.

---

## The Seven Signals: Detailed Breakdown

### 1. Comprehensibility (Clarity of Claims & Argument)

#### Original Definition (Social Science)
Are claims clear, explicit, and well-structured?

#### HASS Adaptation
- Are central claims **explicit** and **bounded** (not vague or unlimited)?
- Are key domain terms defined? (e.g., "site," "landscape unit," "phase")
- Is the logical structure of the argument traceable?
- Can readers understand what is being claimed and on what basis?

#### Automated Assessment Approach
- **Extraction:** LLM extracts main claims and checks for explicit scope, qualifiers, and cited support
- **Analysis:** Cross-check that claims have clear boundaries (temporal, spatial, conceptual)
- **Metrics:** 
  - % of claims with explicit scope statements
  - Argument completeness score
  - Presence of key term definitions

#### Assessment Questions
- Are claims stated explicitly or left implicit?
- Are scope boundaries clear (who/what/where/when)?
- Are technical terms defined in context?
- Can the logical structure be traced from evidence to claim?

#### Example Red Flags
- **Low score:** "The landscape was intensively used" (no temporal, spatial, or activity-type bounds)
- **High score:** "Between 1200-900 BCE, settlements in the Vardar valley concentrated within 2km of the river, suggesting intensive exploitation of riparian resources"

---

### 2. Transparency (Research Design & Documentation)

#### Original Definition
Are research methods and procedures well-documented and reproducible?

#### HASS Adaptation
- Is research clearly **exploratory** (hypothesis-generating) vs **confirmatory** (hypothesis-testing)?
- Are sampling strategies, survey coverage, excavation strategies documented?
- Are analytical choices **explained** (not just implemented)?
- Are field forms, context sheets, and raw data accessible via repositories?
- Are there links to repository artifacts?

#### Automated Assessment Approach
- **Extraction:** Detect presence/absence of design elements:
  - Sampling frames and rationale
  - Survey intensity and coverage maps
  - Trench placement rationale
  - Lab protocols and analytical workflows
- **Verification:** Check for repository links and verify they resolve
- **Mapping:** Align extracted methods to CRMarchaeo classes to grade documentation completeness
- **Infrastructure:** Link to Open Context, tDAR, ARIADNE repositories

#### Assessment Questions
- Is the research design explicitly stated (exploratory vs confirmatory)?
- Are sampling decisions explained and justified?
- Can field procedures be traced from documentation?
- Are analytical choices made explicit?
- Is sufficient detail provided for critical evaluation?

#### Example Red Flags
- **Low score:** Survey results presented without explaining area selection criteria or coverage intensity
- **Medium score:** Methods described but no access to raw data or field documentation
- **High score:** Explicit design statement, documented sampling rationale, publicly accessible datasets with clear metadata

---

### 3. Plausibility (Fit with Broader Knowledge)

#### Original Definition
Does the claim align with established prior evidence and theory?

#### HASS Adaptation
- Do interpretations respect chronology, geomorphology, and regional comparanda?
- Are claims consistent with established domain knowledge?
- Are anomalies acknowledged and explained (not ignored)?
- Do interpretations require implausible auxiliary assumptions?

#### Automated Assessment Approach
- **External Knowledge:** RAG over gazetteers, period ontologies (PeriodO), regional syntheses
- **Consistency Checks:** 
  - Claimed chronology vs accepted typology windows
  - Geographic claims vs established site distributions
  - Interpretations vs documented regional patterns
- **Flagging:** Semantic consistency flags + human review queue for significant disagreements
- **Metrics:** Domain coherence score; anomaly acknowledgment index

#### Assessment Questions
- Do chronological claims align with established typologies?
- Are interpretations consistent with regional patterns?
- Are anomalies explicitly addressed?
- Does the interpretation require accepting claims that contradict established knowledge?

#### Example Red Flags
- **Low score:** Dating pottery assemblage to period inconsistent with established typology without acknowledging discrepancy
- **Medium score:** Novel interpretation that challenges conventional wisdom but acknowledges the departure
- **High score:** Interpretations fully integrated with chronological frameworks and regional patterns; anomalies explicitly discussed

---

### 4. Validity (Evidential Adequacy)

#### Original Definition
Are methods appropriate for the research question and claims adequately supported?

#### HASS Adaptation
- Are data **sufficient** and **representative** for the claims made?
- Are **alternative interpretations** explicitly considered?
- Is there over-generalization from limited data?
- Do authors acknowledge sampling limitations?
- Are rival hypotheses addressed?

#### Automated Assessment Approach
- **Evidence Assessment:** 
  - Score whether explicit alternative explanations are raised
  - Quantify sample completeness (N contexts, coverage maps if present)
  - Detect over-generalization language patterns
- **Claim-Evidence Matching:** Verify evidential support is adequate for scope of claims
- **Metrics:** 
  - Coverage index (data sufficiency)
  - Rival-hypotheses index (alternative interpretations considered)
  - Generalization-boundary alignment

#### Assessment Questions
- Is evidence sufficient for the claims being made?
- Are sampling limitations acknowledged?
- Are alternative explanations considered?
- Is the scope of claims appropriately matched to the scope of evidence?
- Are there acknowledged gaps in the evidence base?

#### Example Red Flags
- **Low score:** Landscape-scale claims based on 3 test pits without acknowledging sampling limitations
- **Medium score:** Adequate data but alternative interpretations not discussed
- **High score:** Sufficient, representative data; alternative interpretations explicitly considered; limitations clearly stated

---

### 5. Robustness (Sensitivity to Analytical Choices)

#### Original Definition
Would results hold under different reasonable analytical approaches?

#### HASS Adaptation
- Would main inferences survive reasonable alternative analytical processing?
- Are there sensitivity analyses showing results aren't artifacts of specific choices?
- How dependent are results on hand-curated or subjective steps?
- Are key analytical decisions justified?
- Would different reasonable choices lead to different conclusions?

#### Automated Assessment Approach
- **Detection:** 
  - Presence of sensitivity analyses
  - Re-analysis notebooks or alternative processing
  - Degree of dependency on undocumented manual steps
- **Code Analysis:** Reproducible code/pipelines vs manual workflows
- **Metrics:** 
  - Robustness checklist score
  - Analytical transparency index
  - Sensitivity testing coverage

#### Assessment Questions
- Are sensitivity analyses performed?
- How dependent are results on specific analytical choices?
- Are alternative analytical approaches explored?
- Could different reasonable choices lead to different conclusions?
- Are manual curation steps documented and justified?

#### Example Red Flags
- **Low score:** Chronological model entirely dependent on subjective phasing decisions without exploring alternatives
- **Medium score:** Some analytical choices justified but no sensitivity testing
- **High score:** Multiple analytical approaches tested; results robust across reasonable variations; dependencies clearly documented

---

### 6. Replicability (Analytic Reproducibility)

#### Original Definition
Can the study be replicated by independent researchers?

#### HASS Adaptation (Critical Shift for Archaeology)
**For HASS: Replicability = Analytic Reproducibility, NOT field replication**

- Can others reproduce the **analytical outputs** given the same inputs?
- Are data and code available and complete?
- Are computational workflows documented?
- Can analytical steps be traced and rerun?

**Important:** This does NOT mean "can you re-excavate the site" — that's impossible. It means "given the excavation data, can you reproduce the analysis?"

#### Automated Assessment Approach
- **Availability Checks:**
  - Detect code availability (GitHub, Zenodo, etc.)
  - Detect data DOIs
  - Repository verification (Open Context, tDAR, institutional repositories)
  - Verify links resolve and files are complete
- **Standards Assessment:**
  - **FAIR** principles (Findable, Accessible, Interoperable, Reusable)
  - **CARE** principles (Collective benefit, Authority to control, Responsibility, Ethics) — especially for Indigenous data
- **Metrics:**
  - Data availability score
  - Code availability score  
  - Workflow documentation completeness
  - FAIR/CARE compliance rating

#### Assessment Questions
- Are raw data publicly accessible (or appropriately restricted with justification)?
- Is analysis code available and documented?
- Can analytical workflows be traced step-by-step?
- Are data and code complete (not just fragments)?
- If access is restricted, is governance framework explained?

#### Example Red Flags
- **Low score:** Statistical analysis claims with no code or raw data provided
- **Medium score:** Data available but analysis code missing; or code provided but undocumented
- **High score:** Complete data + documented code in stable repository; or appropriate restrictions with CARE-compliant governance framework

#### Special Considerations
- **Indigenous/Community Data:** System does NOT penalize appropriate restrictions if aligned with CARE principles
- **Sensitive Archaeological Data:** Legitimate restrictions (site protection) should be explained, not hidden

---

### 7. Generalisability (Scope & Limitations)

#### Original Definition
Can findings transfer to other contexts, populations, or settings?

#### HASS Adaptation
- Are claims carefully **constrained** by place, time, and context?
- Do authors **explicitly articulate limits** to generalization?
- Are scope boundaries appropriate for the evidence?
- Are limitations acknowledged rather than ignored?
- Is over-generalization avoided?

#### Automated Assessment Approach
- **Extraction:**
  - Detect explicit limitation statements
  - Map spatial/temporal extents using gazetteers
  - Identify scope qualifiers in claims
- **Flagging:** Unbounded extrapolations or missing limitation statements
- **Metrics:**
  - Limitation statement density
  - Scope-evidence alignment
  - Geographic/temporal constraint explicitness

#### Assessment Questions
- Are claims appropriately bounded by context (geographic, temporal, cultural)?
- Are limitations explicitly stated?
- Is the scope of generalization matched to the scope of evidence?
- Are extrapolations appropriately qualified?
- Are there unjustified leaps from local to regional/universal claims?

#### Example Red Flags
- **Low score:** Study of Bronze Age settlement in one valley making unqualified claims about "Bronze Age settlement patterns"
- **Medium score:** Regional patterns described but temporal/cultural boundaries unclear
- **High score:** Claims carefully bounded by geography, chronology, and context; explicit limitation statements; appropriate constraint on generalizations

---

## Key HASS-Specific Adaptations

### Adaptation 1: Non-Repeatable Phenomena

**Challenge:** Archaeological sites are destroyed by excavation; historical events can't be rerun.

**Solution:**
- **Replicability** signal shifts to **analytic reproducibility** (same inputs → same outputs)
- **Robustness** emphasizes **convergent evidence** (multiple independent indicators supporting same conclusion)
- System does NOT penalize inability to "rerun the excavation"
- Focus is on transparency of analytical processes, not repeatability of field events

**Example:** An excavation with excellent documentation, publicly available data, and reproducible analysis code scores HIGH on replicability — even though the site is now destroyed.

---

### Adaptation 2: Interpretive/Narrative Papers

**Challenge:** Some HASS work is primarily interpretive with limited empirical data.

**Solution:**
- Validate primarily on *transparency, plausibility, generalisability, reflexivity*
- Mark *replicability* as "not applicable to empirical pipeline" rather than scoring low
- Prevent inappropriate penalization of valid interpretive scholarship
- Different credibility profiles for different research types

**Example:** A theoretical synthesis paper with no new data collection would not be scored on "data availability" — that's category error. Instead, focus on logical coherence, engagement with prior literature, and explicit scope limitations.

---

### Adaptation 3: Indigenous & Community Data

**Challenge:** FAIR principles (open access) can conflict with Indigenous data sovereignty and community rights.

**Solution:**
- Incorporate **CARE** principles (Collective benefit, Authority to control, Responsibility, Ethics) alongside FAIR
- System **does NOT** auto-penalize restricted access if justification aligns with CARE
- "Good stewardship" respects authority to control and ethical obligations
- Distinguish between "hidden data" (bad) and "appropriately governed data" (good)

**Example:** A study using Indigenous oral histories with access restrictions governed by community protocols scores HIGH on data stewardship — restricted access is appropriate, not a failure.

---

## Mapping to Extraction Schema

Your **CEM graphs + RDMAP extraction** provides the raw material for assessing these signals:

| Credibility Signal | What Your Extraction Provides |
|-------------------|-------------------------------|
| **Comprehensibility** | Explicit claims with scope qualifiers, logical links between claims, term definitions |
| **Transparency** | Research design declarations (exploratory/confirmatory), method documentation, repository links, RDMAP structure |
| **Plausibility** | Domain context for consistency checking, chronological/geographic references, regional comparanda |
| **Validity** | Evidence-claim links showing support relationships, alternative interpretations (when stated), sampling limitations |
| **Robustness** | Analytical workflows, sensitivity analyses (when present), dependencies between analytical steps |
| **Replicability** | Data/code availability flags, repository metadata, DOI links, FAIR/CARE compliance markers |
| **Generalisability** | Claim scope declarations, explicit limitation statements, geographic/temporal bounds |

---

## The Key Innovation: From Human Mental Extraction to Automated Structured Extraction

### What repliCATS Did (Human Process)
1. **Humans read papers** → mental extraction of relevant features (happens in expert's head)
2. **Humans write justifications** → unstructured text explaining reasoning
3. **Humans code justifications** → structured markers extracted from text post-hoc
4. **Humans score signals** → final credibility ratings based on coded markers

**Result:** 73-84% accuracy, but requires expert time at every step

### What LLM-Assisted System Does (Automated Process)
1. **LLM reads papers** → automated extraction of structured knowledge (CEM graphs, RDMAP)
2. **LLM generates assessments** → structured credibility scores + textual justifications
3. **Structure is immediate** → no post-hoc coding needed; signals scored directly from extracted structures

**Result:** Aims to match repliCATS accuracy while scaling beyond human capacity

---

## Assessment Workflow: Multi-Agent Ensemble Approach

Following repliCATS's multi-expert deliberation model:

### Stage 1: Independent Assessment (IDEA: Investigate)
- Run 3-5 **independently seeded** LLM agents per paper
- Each agent reviews CEM graph + text excerpts
- Each drafts **structured assessments** for each signal with:
  - Lower bound / best estimate / upper bound scores (0-100)
  - 3-sentence justification with citations to extracted elements
  - Specific evidence for rating

### Stage 2: Aggregation (IDEA: Discuss & Estimate)
- Collate agent assessments
- Expose reasoning to "synthesizer" agent (or human moderator for flagged cases)
- Mathematical aggregation (trimmed means, quantile aggregation)
- Compute **internal uncertainty** (between-agent variance) to drive escalation

### Stage 3: Calibration (IDEA: Aggregate)
- Compare against expert panel ratings on same papers
- Calculate inter-rater reliability (Gwet's AC1, Kendall's W)
- Calibrate scores using proper scoring rules (Brier scores)
- Adjust thresholds based on empirical validation

---

## Success Metrics (Target Performance)

Based on repliCATS benchmarks and ChatExtract extraction results:

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Extraction Precision** | >85% | % extracted claims/evidence/methods correct |
| **Extraction Recall** | >80% | % of actual content successfully extracted |
| **Signal Correlation** | >0.6 | LLM scores vs expert panel scores |
| **Calibration** | Brier < 0.25 | Probability calibration on held-out papers |
| **Classification Accuracy** | 70-84% | Binary credibility classification (if applicable) |

---

## Practical Example: Assessing a Hypothetical Paper

### Paper: "Bronze Age Settlement Patterns in the Vardar Valley"

**Comprehensibility Assessment:**
- ✅ Main claims explicit: "concentrated riparian settlement 1200-900 BCE"
- ✅ Key terms defined: "settlement" = permanent habitation sites >0.5ha
- ✅ Scope bounded: geographic (Vardar valley), temporal (1200-900 BCE), activity type
- **Score: 85/100** — High comprehensibility

**Transparency Assessment:**
- ✅ Research design stated: "exploratory survey documenting previously unknown sites"
- ✅ Survey strategy explained: "systematic field walking at 20m transect intervals"
- ❌ No repository links for site data
- ⚠️ Sampling rationale unclear (why these survey areas?)
- **Score: 60/100** — Moderate transparency; documentation incomplete

**Plausibility Assessment:**
- ✅ Chronology aligns with established typologies
- ✅ Settlement patterns consistent with known Bronze Age economies
- ✅ Anomaly acknowledged: "unusual lack of upland sites requires further investigation"
- **Score: 80/100** — High plausibility

**Validity Assessment:**
- ⚠️ Claims based on 23 sites from 100 sq km survey
- ❌ No discussion of survey coverage bias (valleys easier to survey than hills?)
- ❌ Alternative interpretation not considered: "were upland sites present but not detected?"
- **Score: 55/100** — Moderate-low validity; sampling limitations not addressed

**Robustness Assessment:**
- ❌ Single dating approach (ceramic typology only)
- ❌ No sensitivity analysis of chronological assignments
- ❌ Dependence on subjective ceramic classification not acknowledged
- **Score: 40/100** — Low robustness

**Replicability Assessment:**
- ❌ No site coordinates provided (not even approximate)
- ❌ No ceramic data published
- ❌ No code for spatial analysis
- **Score: 20/100** — Very low replicability

**Generalisability Assessment:**
- ✅ Claims explicitly bounded: "Vardar valley, 1200-900 BCE"
- ✅ Limitations acknowledged: "survey coverage incomplete; upland areas underrepresented"
- ❌ But text includes unqualified statements: "Bronze Age people preferred valley locations" (over-generalization)
- **Score: 65/100** — Moderate generalisability; mostly bounded but some leakage

### Overall Credibility Profile
**Strengths:** Clear claims, plausible interpretations, appropriate geographic/temporal scope
**Weaknesses:** Limited data access, no robustness checks, sampling limitations not fully addressed
**Priority for Improvement:** Make data publicly available; consider alternative dating methods; explicitly discuss survey bias

---

## References & Further Reading

### repliCATS Project
- Website: https://replicats.research.unimelb.edu.au/
- Primary Publication: Wintle et al. (2021), "Predicting reliability through structured expert elicitation with the repliCATS process," PLOS ONE
- Validation Study: 84% accuracy on known-outcome claims (AUC 0.94)
- Phase 1 Performance: 73-84% classification accuracy (AUC > 0.75)

### Follow-On Work
- **SMART Program** (Center for Open Science): Scaling Machine Assessments of Research Trustworthiness
- Combines machine learning with human deliberation for automated credibility assessment

### Extraction Foundations
- **ChatExtract** (Polak & Morgan, 2024): Multi-turn conversational prompting for scientific extraction
- **CLIO** (Anthropic, 2024): Semantic extraction at scale across 1M+ conversations

### Archaeological Data Infrastructure
- **CRMarchaeo**: CIDOC-CRM extension for archaeological excavation and survey documentation
- **Open Context**: Open access archaeological data repository
- **tDAR**: The Digital Archaeological Record (CoreTrustSeal certified)
- **ARIADNE**: Research infrastructure for archaeological datasets

### Data Principles
- **FAIR Principles**: Findable, Accessible, Interoperable, Reusable (Wilkinson et al., 2016)
- **CARE Principles**: Collective benefit, Authority to control, Responsibility, Ethics (Global Indigenous Data Alliance)

---

## Document Version
- **Version:** 1.0
- **Date:** October 26, 2025
- **Status:** Reference document for RDMAP credibility assessment development
- **Next Steps:** Operationalize as LLM assessment prompts; validate against expert panel ratings
