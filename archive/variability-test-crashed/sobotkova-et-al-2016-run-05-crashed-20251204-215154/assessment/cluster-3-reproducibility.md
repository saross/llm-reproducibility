# Cluster 3: Reproducibility Assessment

**Paper:** Sobotkova et al. (2016) - Measure Twice, Cut Once
**Run ID:** run-05
**Pillar:** Reproducibility

## Signal 7: Reproducibility

### Definition
Can the analytical workflow be reproduced given available materials?

**Note:** For HASS papers, reproducibility refers to analytic/computational reproducibility (can others reproduce analytical outputs given same inputs?), not beginning-to-end replication of fieldwork.

### Assessment (Inductive/Methodological Approach Anchors)

| Criterion | Score (0-100) | Evidence |
|-----------|---------------|----------|
| Software availability | 75 | FAIMS software openly available on GitHub (GPLv3); URL provided |
| Software versioning | 40 | No specific version tags or DOIs for software used in case studies |
| Data availability | 20 | Interview/correspondence data not deposited; no access path provided |
| Protocol documentation | 45 | Co-development process described at high level; interview protocol implicit |
| Analytical workflow | 35 | Thematic analysis process not documented in reproducible detail |
| Computational environment | 50 | Android platform mentioned; server requirements partially specified |

**Reproducibility Score: 44/100**

### Detailed Assessment

#### Software Reproducibility
The FAIMS software is openly available under GPLv3 licence, which is commendable. However:
- No DOI for software versions used in case studies
- FAIMS 2.0 mentioned but specific commits/releases not identified
- Module customisations for each project not archived

**Software Reproducibility Sub-score: 55/100**

#### Data Reproducibility
Case study data is not available for independent analysis:
- Interview transcripts not deposited
- Email correspondence not archived
- Quantitative data (time estimates, costs) presented only as aggregates
- No raw data underlying the 95% labour saving claim

**Data Reproducibility Sub-score: 20/100**

#### Analytical Reproducibility
The thematic analysis cannot be reproduced:
- No codebook or coding scheme provided
- Theme identification process not documented
- No inter-rater reliability reported
- Member checking or validation not described

**Analytical Reproducibility Sub-score: 30/100**

#### Methodological Reproducibility
Could another team replicate the co-development evaluation approach?
- Case study selection criteria implicit
- Interview questions not provided
- Data collection timeline not specified
- Analysis procedures described at high level only

**Methodological Reproducibility Sub-score: 45/100**

### Key Evidence from Extraction

**Supporting Reproducibility:**
- E014: "All FAIMS project software is free and open source (GPLv.3 licence)"
- E015: "FAIMS project uses GitHub... to publish and manage individual modules"
- reproducibility_infrastructure.code_availability.statement_present: true

**Limiting Reproducibility:**
- reproducibility_infrastructure.data_availability.statement_present: false
- P001: Interview protocol is implicit
- P004: Theme identification protocol is implicit
- extraction_notes.known_limitations: "Interview protocols not explicitly described"

### CARE Principles Consideration
Not applicable - this paper does not involve Indigenous or community data requiring CARE-based restrictions.

### Computational Reproducibility Spectrum Placement

| Level | Description | Paper Status |
|-------|-------------|--------------|
| Level 0 | No materials available | ❌ |
| Level 1 | Code/software available | ✓ (partial) |
| Level 2 | Code + data available | ❌ |
| Level 3 | Code + data + environment | ❌ |
| Level 4 | Fully automated reproduction | ❌ |

**Placement: Level 1 (partial)** - Software available but not versioned; data not available.

---

## Cluster 3 Summary

**Reproducibility Score: 44/100**

### Interpretation
Reproducibility is limited despite the paper's focus on open-source software for research data collection. The irony is notable: a paper advocating for better data management practices does not itself meet high standards for research reproducibility. The software availability is a strength, but the lack of deposited case study data, undocumented analytical procedures, and implicit interview protocols significantly limit reproducibility.

### Context-Appropriate Assessment
For a 2016 book chapter in digital archaeology, the reproducibility limitations are understandable given then-current disciplinary norms. However, the paper advocates for practices (structured data, version control, reusable workflows) that it does not fully apply to its own research process.

### Recommendations for Improvement
1. **Software:** Archive specific software versions used with DOIs (e.g., Zenodo)
2. **Data:** Deposit de-identified interview transcripts or summaries
3. **Analysis:** Provide thematic coding scheme and example coded passages
4. **Protocol:** Publish interview guide as supplementary material
5. **Workflow:** Document step-by-step analytical process

### Alignment with Paper's Own Values
The paper states: "More continuous recordkeeping, including of 'messy' work-in-progress, not only helps researchers at a later time better understand what they have excavated, but may contribute toward both making workflows more transparent" (C047). This principle could be applied to the research process of the paper itself.
