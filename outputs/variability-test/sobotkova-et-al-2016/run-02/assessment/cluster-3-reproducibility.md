# Cluster 3: Reproducibility

**Paper:** Sobotkova et al. (2016) - Measure Twice, Cut Once
**Run ID:** run-02
**Assessment Date:** 2025-12-04

## Signal 3.1: Reproducibility

### Score: 72/100

### Assessment Framework

**Methodological Paper Anchors Applied**

For software/methods papers, reproducibility focuses on:
- Can others deploy the software?
- Can others follow the customisation process?
- Are workflows sufficiently documented for replication?

*Note: Beginning-to-end archaeological site reproduction is impossible and not the relevant standard.*

---

## Reproducibility Components

### Component A: Software Reproducibility

**Score: 85/100**

#### Strengths

1. **Open source availability:** All FAIMS software is GPLv3 licensed on GitHub
2. **Active distribution:** Available via Google Play for end-user deployment
3. **Documentation:** Extensive support documentation at fedarch.org
4. **Version control:** GitHub provides full version history
5. **Module sharing:** XML-based modules can be shared and adapted

#### Weaknesses

1. **No DOI for software:** GitHub URL provided but no software citation
2. **Version pinning:** Specific version used in 2014 deployments not archived
3. **Dependency documentation:** External dependencies not fully specified

#### Evidence

- E007: 19 workflows created for 17 projects (demonstrating reusability)
- E013: Doctoral students successfully self-deployed (demonstrating reproducibility)
- reproducibility_infrastructure.code_availability: GitHub + GPLv3

---

### Component B: Process Reproducibility

**Score: 70/100**

#### Strengths

1. **Customisation workflow documented:** XML editing process described in P005
2. **Communication logs preserved:** Full correspondence available in supplements
3. **Cost benchmarks provided:** Other projects can estimate effort requirements
4. **Iterative process described:** P006 documents requirements-development-testing cycles

#### Weaknesses

1. **Tacit knowledge gaps:** Some customisation expertise not fully documented
2. **Support dependency:** Papers acknowledge need for "exceptional support" (C043)
3. **Hardware specifications incomplete:** FAIMS-in-a-box components not fully listed

#### Evidence

- P001-P010: Ten protocols documented at varying specificity
- E018-E019: Timeline examples for module development

---

### Component C: Analytical Reproducibility

**Score: 62/100**

#### Strengths

1. **Data export documented:** CSV export process to desktop software described (P008)
2. **Database structure available:** Module definitions exportable
3. **Quantitative claims traceable:** Specific figures provided (though methodology informal)

#### Weaknesses

1. **Analysis code not shared:** No scripts for cost-benefit calculations
2. **Thematic analysis not detailed:** How themes were derived from case studies not specified
3. **Communication log analysis:** Process for extracting quotes not documented
4. **No supplementary data tables:** Raw metrics not provided in machine-readable format

#### Evidence

- E020: CSV export example
- E023-E025: Time savings calculations (methodology unstated)

---

## FAIR Principles Assessment

### Findability: 6/10

- **Present:** Clear citation, known repository (GitHub)
- **Missing:** No DOI for paper, no software DOI, no ORCID for authors

### Accessibility: 8/10

- **Present:** Open access book, open source software, Google Play distribution
- **Missing:** Some institutional barriers to supplementary materials

### Interoperability: 7/10

- **Present:** CSV export, XML configuration files, standard formats
- **Missing:** No formal ontology alignment, limited metadata standards

### Reusability: 8/10

- **Present:** GPLv3 licence clear, documentation extensive, modular design
- **Missing:** Version-specific archiving, dependency specification

### Total FAIR Score: 29/40 (72.5%)

---

## Reproducibility Spectrum Assessment

For methodological papers, assess where on the reproducibility spectrum the work falls:

| Level | Description | This Paper |
|-------|-------------|------------|
| **1. Same Software** | Others can use FAIMS | ✅ Fully achieved |
| **2. Same Process** | Others can customise modules | ✅ Largely achieved |
| **3. Same Workflow** | Others can replicate deployment approach | ⚠️ Partially achieved |
| **4. Same Results** | Others achieve similar outcomes | ❓ Not tested |
| **5. Same Conclusions** | Independent evaluation confirms findings | ❓ Not available |

### Reproducibility Level: 2.5/5 (Process reproducibility with some workflow gaps)

---

## Reproducibility Barriers

### Low Barriers

- Software access (open source, free)
- Basic documentation (extensive)
- Licence clarity (GPLv3)

### Moderate Barriers

- Technical expertise required
- Infrastructure costs (AUD $1,700-$15,000)
- Support availability

### High Barriers

- Tacit knowledge in FAIMS team
- Specific hardware configurations
- Android ecosystem fragmentation

---

## Cluster 3 Summary

### Aggregate Score: 72/100

### Interpretation (Methodological Paper Framework)

Strong software reproducibility is the paper's key strength—FAIMS is genuinely open and accessible. Process reproducibility is good but assumes technical competence. Analytical reproducibility is weakest due to informal quantitative methodology.

### Key Findings

1. **Software Reproducibility (85):** Excellent open-source availability and documentation
2. **Process Reproducibility (70):** Good workflow documentation with some tacit knowledge gaps
3. **Analytical Reproducibility (62):** Quantitative claims lack methodological transparency

### Caveats Applied

- Reproducibility assessment based on 2016 documentation; current FAIMS versions may differ
- Support dependency means full reproducibility requires FAIMS team engagement or significant technical expertise
- Cost/time reproducibility claims are indicative rather than guaranteed

---

*Cluster 3 assessment complete. All clusters assessed. Proceeding to final credibility report.*
