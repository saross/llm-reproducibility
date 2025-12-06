# Cluster 3: Reproducibility

**Paper:** Sobotkova et al. (2016) - Measure Twice, Cut Once
**Run ID:** run-04
**Assessment Date:** 2025-12-04

---

## Signal Assessment

### Reproducibility

**Definition:** Can the analytical procedures be reproduced given the available materials?

**Note:** For HASS papers, reproducibility refers to *analytic reproducibility* (can others reproduce the analysis given the same inputs?) rather than beginning-to-end replication of fieldwork.

#### Inductive Anchors Applied (Methodological Paper)

| Score Range | Description | Paper Alignment |
|-------------|-------------|-----------------|
| 80-100 | Full workflow documentation, materials available, procedures replicable | — |
| 60-79 | Good documentation, most procedures reproducible with some gaps | **Best fit** |
| 40-59 | Partial documentation, significant barriers to reproduction | — |
| 20-39 | Limited documentation, reproduction difficult | — |
| 0-19 | No reproducibility infrastructure | — |

---

#### Assessment

**What would need to be reproduced:**
1. Thematic analysis of case study experiences
2. Cost-benefit calculations comparing paper vs digital workflows
3. Synthesis of observations into three themes

**Reproducibility Infrastructure Available:**

| Component | Available | Quality | Notes |
|-----------|-----------|---------|-------|
| Source data (communications) | Yes | High | Complete unedited communications in supplement |
| Software | Yes | High | GPLv.3 on GitHub |
| Questionnaire instrument | Unclear | Low | Not explicitly provided |
| Thematic coding scheme | No | N/A | Not documented |
| Cost calculation methods | Partial | Medium | Figures given but calculation procedure unclear |
| Module definition documents | Yes | High | Available in supplement and GitHub |

**Strengths:**
- Complete unedited communications with project directors available
- Software and modules available under open source licence
- Detailed supplementary materials for each case study
- Specific quantitative figures enable verification of calculations
- GitHub provides version-controlled access to modules

**Weaknesses:**
- Thematic analysis procedure not documented - themes cannot be independently derived
- Questionnaire instrument not provided
- Selection criteria for quotations not transparent
- Time-tracking methodology for savings calculations not specified
- Cost figures based on project director estimates without verification

**FAIR Assessment (from extraction):**
- Findable: 5/10 (GitHub, Google Play, but no DOI)
- Accessible: 6/10 (open source, but supplement access unclear)
- Interoperable: 5/10 (XML-based modules, but platform-specific)
- Reusable: 6/10 (GPLv.3 licence, good documentation)
- **Total: 22/40**

**Reproducibility Scenario Analysis:**

| Scenario | Feasibility | Barriers |
|----------|-------------|----------|
| Verify quantitative claims | High | Need to locate raw data in supplements |
| Reproduce thematic analysis | Low | No coding scheme or procedure documented |
| Reuse FAIMS modules | High | Well-documented, version-controlled |
| Replicate deployment experience | Medium | Technology has evolved since 2014 |
| Verify cost-benefit calculations | Medium | Figures available but methodology unclear |

---

#### Score: **62/100**

**Justification:** The paper provides substantial reproducibility infrastructure, particularly the complete unedited communications and open-source software. A researcher could verify the quotations and examine the source materials. However, the core analytical procedure (thematic analysis) is not documented, making it impossible to independently derive the same themes from the data. This is a significant gap for a methodological paper. The quantitative claims could be partially verified but the calculation methodology is not fully transparent.

---

## Cluster 3 Summary

| Signal | Score | Weight | Weighted Score |
|--------|-------|--------|----------------|
| Reproducibility | 62 | 1.0 | 62.0 |
| **Cluster 3 Total** | — | — | **62.0** |

**Cluster Assessment:** MODERATE

Reproducibility is moderate. The paper provides excellent access to source materials (communications, software, modules) but falls short on analytical procedure documentation. The thematic analysis that produces the paper's core findings is not replicable from the available materials. This is a common limitation of qualitative synthesis papers but nonetheless constrains reproducibility assessment.

---

## Reproducibility Enhancement Recommendations

1. **Document thematic analysis procedure:** Describe how themes emerged from data, including any coding scheme used
2. **Provide questionnaire instrument:** Share the post-project questionnaires administered to project directors
3. **Clarify cost calculation methodology:** Explain how time savings and cost comparisons were calculated
4. **Include quotation selection criteria:** Describe how representative quotations were selected from communications
5. **Add ORCID identifiers:** Enable researcher identification and attribution tracking
