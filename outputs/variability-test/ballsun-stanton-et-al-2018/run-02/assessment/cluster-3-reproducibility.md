# Cluster 3: Reproducibility Assessment

**Paper:** Ballsun-Stanton et al. (2018) - FAIMS Mobile
**Run:** run-02
**Assessment Date:** 2025-12-02
**Paper Type:** Methodological (Software Publication)

## Overview

This cluster assesses the reproducibility and replicability of the research. For software publications, this translates to software reproducibility, deployment replicability, and documentation quality.

## Signal 3.1: Software Reproducibility

### Assessment

| Criterion | Rating | Evidence |
|-----------|--------|----------|
| Source code availability | **Strong** | GitHub repository, GPLv3 licence |
| Build instructions | **Strong** | Docker-based deployment documented |
| Dependency documentation | **Moderate** | Docker handles dependencies; manual install less documented |
| Version control | **Strong** | Git-based development |

### Reproducibility Infrastructure

| Component | Status | Location |
|-----------|--------|----------|
| Source code | ✅ Available | GitHub (fedarch organisation) |
| Licence | ✅ Open | GPLv3 |
| Container | ✅ Available | Docker deployment |
| Documentation | ✅ Available | GitHub wiki |
| Sample modules | ✅ Available | 24 public definitions |

**Score: 4.5/5**

## Signal 3.2: Deployment Replicability

### Assessment

| Criterion | Rating | Evidence |
|-----------|--------|----------|
| Installation documentation | **Strong** | Docker-based process documented |
| Configuration guidance | **Strong** | Module Definition Language documented |
| Example deployments | **Strong** | 24 public module definitions as templates |
| Troubleshooting resources | **Moderate** | Wiki available; depth unclear |

### Deployment Path Analysis

**Standard deployment:**
1. Docker container deployment (documented)
2. Server configuration (documented)
3. Module definition creation (templates available)
4. Android app installation (standard APK process)

**Replication barriers:**
- Requires Linux server (explicit dependency)
- Technical expertise needed for customisation
- Training recommended for complex deployments

**Score: 4/5**

## Signal 3.3: Documentation Quality

### Assessment

| Criterion | Rating | Evidence |
|-----------|--------|----------|
| Completeness | **Strong** | Wiki with module definitions, user guides |
| Accuracy | **Assumed** | Active maintenance suggested by update frequency |
| Accessibility | **Moderate** | Technical audience; non-specialist access limited |
| Maintenance | **Strong** | Active development and community support |

### Documentation Inventory

| Type | Present | Quality |
|------|---------|---------|
| Installation guide | ✅ | Strong |
| User manual | ✅ | Strong |
| API documentation | ⚠️ | Limited mention |
| Module Definition Language spec | ✅ | Strong (XML-based) |
| Training materials | ✅ | Workshops referenced |

**Score: 4/5**

## Signal 3.4: FAIR Compliance (Software-Adapted)

### Assessment

Based on extraction.json FAIR assessment:

| Principle | Score | Notes |
|-----------|-------|-------|
| **Findable** | 10/10 | GitHub repository, DOI via SoftwareX |
| **Accessible** | 10/10 | Open-source, no access barriers |
| **Interoperable** | 9/10 | Standard formats (GeoTIFF, Shapefile, SQLite, CSV export) |
| **Reusable** | 8/10 | GPLv3 licence, documentation present; some expertise needed |
| **Total** | 37/40 | 92.5% |

### FAIR Strengths

- **Persistent identifiers:** DOI via publication, GitHub URLs
- **Open access:** GPLv3 licence, no registration requirements
- **Standard formats:** XML-based module definitions, standard export formats
- **Rich metadata:** Comprehensive documentation in repository

### FAIR Limitations

- **Expertise requirement:** Customisation requires technical skills
- **Server dependency:** Requires infrastructure setup
- **Training need:** Complex deployments benefit from workshops

**Score: 4.5/5**

## Signal 3.5: Long-Term Sustainability

### Assessment

| Criterion | Rating | Evidence |
|-----------|--------|----------|
| Institutional backing | **Strong** | University-based development (Macquarie) |
| Community engagement | **Strong** | Active user community, workshops |
| Funding model | **Uncertain** | Grant-funded; sustainability explicitly flagged |
| Maintenance commitment | **Moderate** | 5 years of development; future uncertain |

### Sustainability Risk Assessment

**Strengths:**
- Open-source model allows community continuation
- Existing user base provides adoption momentum
- Documentation enables independent maintenance

**Risks:**
- Grant funding model creates uncertainty
- Single institutional dependency
- Technical debt not assessed

**Score: 3.5/5**

## Cluster 3 Summary

| Signal | Score | Weight | Weighted |
|--------|-------|--------|----------|
| 3.1 Software Reproducibility | 4.5/5 | 0.25 | 1.125 |
| 3.2 Deployment Replicability | 4.0/5 | 0.25 | 1.00 |
| 3.3 Documentation Quality | 4.0/5 | 0.20 | 0.80 |
| 3.4 FAIR Compliance | 4.5/5 | 0.20 | 0.90 |
| 3.5 Long-Term Sustainability | 3.5/5 | 0.10 | 0.35 |
| **Cluster Total** | | | **4.175/5** |

## Qualitative Assessment

### Strengths

1. **Exemplary open-source practice:** Full source availability with permissive licence
2. **Strong documentation ecosystem:** Wiki, module definitions, training resources
3. **High FAIR compliance:** 92.5% alignment with FAIR principles
4. **Practical replication support:** Docker deployment and template modules

### Limitations

1. **Sustainability uncertainty:** Grant funding model explicitly flagged as concern
2. **Technical barriers:** Non-trivial expertise required for deployment
3. **Infrastructure requirements:** Linux server dependency

### Reproducibility Classification

**Category:** Highly Reproducible (for software publication)

The software meets high standards for reproducibility:
- Source code fully available
- Deployment process documented
- Examples and templates provided
- Active community support

---

*Cluster 3 Assessment completed: 2025-12-02*
*Overall Score: 4.175/5 (Strong)*
