# Cluster 2: Evidential Strength Assessment

**Paper:** Sobotkova et al. (2016) - Measure Twice, Cut Once
**Run ID:** run-05
**Pillar:** Credibility

## Signal 3: Plausibility

### Definition
Are the claims scientifically plausible given domain knowledge?

### Assessment (Inductive Approach Anchors)

| Criterion | Score (0-100) | Evidence |
|-----------|---------------|----------|
| Theoretical grounding | 75 | Claims about software development trade-offs well grounded in software engineering literature |
| Domain appropriateness | 80 | Methods appropriate for evaluating digital archaeology tools |
| Mechanism plausibility | 70 | Time savings mechanisms (elimination of transcription, structured data) are plausible |
| Prior knowledge alignment | 75 | Findings align with known challenges of field data collection |
| Logical consistency | 70 | Internal consistency good; some tension between "upfront costs" and rapid deployment claims |

**Plausibility Score: 74/100**

### Justification
The core claims are scientifically plausible. The trade-offs between generalised and bespoke software are well-established in software engineering. The time savings from digital recording (elimination of transcription errors, immediate data availability) are mechanisms with clear plausibility. Minor tension exists between claims about significant upfront investment (Theme 1) and rapid deployment examples (PAZC in 3.5 weeks).

### Key Evidence
- C022: Time shift from backend to frontend is plausible and supported by software development literature
- E024: 95% labour saving (1-1.5 days vs 25-30 days) is substantial but plausible for digitisation tasks
- C016: Rapid deployment claim supported by E018-E019 evidence

---

## Signal 4: Validity

### Definition
Do the methods appropriately address the research questions?

### Assessment (Inductive Approach Anchors)

| Criterion | Score (0-100) | Evidence |
|-----------|---------------|----------|
| Design-question fit | 70 | Case study appropriate for exploratory evaluation; thematic analysis fits inductive goals |
| Internal validity | 55 | No comparison group; no control for confounds (project maturity, user enthusiasm) |
| Construct validity | 60 | "Success" operationalised through user reports, not independent measures |
| Measurement appropriateness | 65 | Time estimates subjective; cost data more objective |
| Alternative explanations | 45 | Hawthorne effect not addressed; self-selected enthusiastic early adopters |

**Validity Score: 59/100**

### Justification
The case study design is appropriate for exploratory methodological evaluation, but validity is limited by several factors: (1) no comparison with alternative platforms, (2) participants are self-selected FAIMS adopters, (3) outcome measures are largely self-reported, (4) potential Hawthorne effects (performance improvement from being studied) not addressed. The cost data is more objective than time savings estimates.

### Key Evidence
- RD001: Case study design explicit but lacks comparison condition
- IA005: Implicit assumption that three case studies generalise to broader community
- E022: "project members universally reported" - self-report data
- E024: Time estimates are researcher estimates, not systematic measurement

---

## Signal 5: Robustness

### Definition
Would findings hold under alternative analyses or conditions?

### Assessment (Inductive Approach Anchors)

| Criterion | Score (0-100) | Evidence |
|-----------|---------------|----------|
| Analytical robustness | 50 | Single thematic analysis; no alternative coding or member checking reported |
| Cross-case consistency | 70 | Three sites with different contexts show similar patterns; some divergence on server issues |
| Sensitivity analysis | 35 | No exploration of how different analytical choices would affect conclusions |
| Triangulation | 60 | Multiple data sources (interviews, emails, quantitative metrics) but single analytical approach |
| Negative cases | 55 | Performance problems acknowledged (E021-E022) but framed as resolvable |

**Robustness Score: 54/100**

### Justification
Robustness is moderate. The use of three diverse case studies (excavation/survey, different continents, different infrastructure) provides some confidence in pattern consistency. However, analytical robustness is limited by single-pass thematic analysis without reported validation procedures. Negative cases (performance problems, longer data entry times) are acknowledged but attributed to remediable causes rather than fundamental limitations.

### Key Evidence
- RD003: Three contrasting sites provide natural variation
- C019-C021: Performance problems acknowledged but explained away
- IA006: Implicit assumption that problems are design choices not platform limitations

---

## Signal 6: Generalisability

### Definition
To what population or contexts can findings be extended?

### Assessment (Inductive Approach Anchors)

| Criterion | Score (0-100) | Evidence |
|-----------|---------------|----------|
| Scope definition | 70 | Explicit focus on archaeological field recording; claims bounded to similar contexts |
| Sample diversity | 65 | Three continents, excavation and survey, but all established projects |
| Boundary conditions | 60 | Some conditions discussed (network availability, project maturity) |
| Transferability | 65 | Detailed thick description enables reader judgment |
| Limitations acknowledgment | 55 | Some limitations noted but systematic discussion absent |

**Generalisability Score: 63/100**

### Justification
The paper provides reasonable scope definition for an inductive study. The three case studies offer diversity in geography and project type, though all were established projects with experienced directors. The discussion of infrastructure trade-offs (local vs online servers) acknowledges context dependency. However, generalisability to novice users, small projects, or non-archaeology contexts is not systematically addressed.

### Key Evidence
- C014: Explicit acknowledgment that established projects have advantages
- E032-E035: Context-specific findings about server performance
- RD003: Comparative design provides variation but limited to three cases

---

## Cluster 2 Summary

| Signal | Score | Weight | Weighted Score |
|--------|-------|--------|----------------|
| Plausibility | 74 | 0.25 | 18.5 |
| Validity | 59 | 0.25 | 14.75 |
| Robustness | 54 | 0.25 | 13.5 |
| Generalisability | 63 | 0.25 | 15.75 |

**Cluster 2 Aggregate Score: 62.5/100**

### Interpretation
Evidential strength is moderate. The claims are plausible and grounded in domain knowledge, but the evidence base has limitations common to small-n case study designs: no comparison condition, self-selected participants, and self-reported outcomes. The three-site design provides some robustness through replication, but analytical robustness is limited.

### Recommendations for Improvement
1. Include comparison with alternative platforms (FileMaker, paper-based control)
2. Add systematic time-on-task measurement rather than estimates
3. Include independent user assessment (not just project directors)
4. Report thematic analysis validation procedures (member checking, inter-coder reliability)
5. Discuss boundary conditions and limitations systematically
