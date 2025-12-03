# Credibility Assessment Report

**Paper:** Ballsun-Stanton et al. (2018) - FAIMS Mobile: Flexible, open-source software for field research
**Run:** run-04
**Date:** 2025-12-03
**Assessor:** Claude (research-assessor skill v2.6)

---

## Executive Summary

This software publication describing FAIMS Mobile demonstrates **STRONG** transparency and reproducibility practices with **ADEQUATE** evidential strength. The paper excels at making software available, documented, and reproducible, while impact claims rest on less rigorous evidence.

### Overall Verdict: **GOOD**

### Aggregate Score: **78/100**

---

## Paper Classification

| Attribute | Value | Confidence |
|-----------|-------|------------|
| Paper Type | Methodological (Software Publication) | High |
| Research Approach | Inductive | Medium |
| Context Flags | 📦 Software/Tool, 🔧 Methodological | High |

**Classification Notes:** This is an original software publication from SoftwareX journal describing FAIMS Mobile field data collection platform. The paper documents software architecture, features, and deployment impact without presenting empirical research findings. Assessment adapted for software publication genre.

---

## Signal Summary

| Cluster | Signal | Rating | Score |
|---------|--------|--------|-------|
| 1: Foundational Clarity | Comprehensibility | Strong | 85 |
| 1: Foundational Clarity | Transparency | Strong | 90 |
| 2: Evidential Strength | Validity | Adequate | 70 |
| 2: Evidential Strength | Robustness | Adequate | 65 |
| 2: Evidential Strength | Generalisability | Adequate | 72 |
| 3: Reproducibility | Reproducibility | Strong | 88 |

### Cluster Averages

| Cluster | Rating | Average Score |
|---------|--------|---------------|
| Foundational Clarity | Strong | 87.5 |
| Evidential Strength | Adequate | 69 |
| Reproducibility | Strong | 88 |

---

## Key Strengths

### 1. Exemplary Software Transparency

The paper sets a high standard for software publication transparency:
- Full source code under GPLv3 license
- Multiple repositories (FAIMS organisation, SoftwareX archive)
- Clear version numbering (code v2.5, software v2.5.20)
- Perma.cc archival links for long-term accessibility

### 2. Comprehensive Documentation Ecosystem

Documentation serves multiple audiences:
- User documentation (Atlassian wiki)
- Developer documentation (Module Cookbook, Beanshell API)
- Transition guides for users becoming developers
- 24 public module definitions as templates

### 3. Clear Technical Communication

Architecture and features well-explained:
- Effective browser-website analogy clarifies core/module separation
- Technology stack fully enumerated
- Comparison with alternatives (ODK) helps positioning
- Visual aids illustrate interface and functionality

### 4. Strong Reproducibility Infrastructure

Multiple pathways to obtain and deploy:
- Google Play Store and direct APK download
- Server installer script
- Complete dependency documentation
- Module library for rapid customisation

---

## Key Weaknesses

### 1. Impact Evidence Methodology Gap

Deployment statistics lack transparency:
- "40+ customisations, 300 users, 20,000+ hours" cited without methodology
- How were these metrics collected and verified?
- Selection criteria for case studies not documented

### 2. Self-Report Reliance

Impact claims rest on project team's own assessment:
- User feedback quoted but selection not documented
- No independent verification of effectiveness
- Potential selection bias toward successful deployments

### 3. Testing Documentation Absent

No systematic testing reported:
- Stress testing, edge cases, failure modes not documented
- Performance benchmarks not provided
- Comparative testing with alternatives not conducted

### 4. Archaeology-Dominant Evidence

Cross-disciplinary claims exceed evidence breadth:
- Seven disciplines mentioned but archaeology dominates examples
- Barriers to adoption in other disciplines not discussed
- Resource requirements for deployment unclear

---

## FAIR Assessment (FAIR4RS)

| Principle | Score | Notes |
|-----------|-------|-------|
| Findable | 9/10 | GitHub indexed, DOI, clear versioning |
| Accessible | 9/10 | Open repos, multiple download options |
| Interoperable | 8/10 | Standard platform, documented APIs |
| Reusable | 9/10 | GPLv3, modular, well-documented |
| **Total** | **35/40** | **87.5%** |

---

## Recommendations

### For Authors

1. **Document impact methodology:** Future publications should explain how deployment statistics are collected.

2. **Include failure cases:** Discussing deployments that encountered challenges would strengthen validity.

3. **Provide containerised deployment:** Docker images would reduce server setup complexity.

### For Readers

1. **Technical claims reliable:** Architecture and feature descriptions verifiable through code.

2. **Impact claims require caution:** Deployment statistics are self-reported without methodology.

3. **Cross-disciplinary evidence limited:** Most evidence from archaeology; other disciplines less documented.

### For Replicators

1. **Start with module library:** 24 public definitions provide templates for new deployments.

2. **Server setup requires expertise:** Ubuntu server administration skills needed for deployment.

3. **Expect customisation effort:** DSL and Beanshell scripting required for non-trivial adaptations.

---

## Assessment Metadata

| Field | Value |
|-------|-------|
| Assessment Framework | repliCATS Seven Signals (HASS-adapted) |
| Paper Type Adaptations | Software publication criteria applied |
| Extraction Counts | 43 evidence, 58 claims, 8 implicit arguments |
| Research Infrastructure | 4 designs, 4 methods, 9 protocols |
| Known Uncertainties | 4 documented |

---

## Conclusion

Ballsun-Stanton et al. (2018) represents strong practice in software publication transparency and reproducibility. The paper makes FAIMS Mobile fully accessible, well-documented, and practically deployable. Impact claims would benefit from more rigorous evidence methodology, but this limitation is common in software publications and does not undermine the paper's core contribution: describing a mature, open-source tool for field research data collection.

**Final Verdict: GOOD (78/100)**

The paper earns a "Good" rating for:
- Excellent transparency and reproducibility (Clusters 1 & 3)
- Adequate but limited evidential strength (Cluster 2)
- Appropriate adaptation of claims to available evidence
- Strong open-source and documentation practices

