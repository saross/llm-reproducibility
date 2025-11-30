# Cluster 3: Reproducibility Assessment

**Paper:** ballsun-stanton-et-al-2018
**Assessment Date:** 2025-11-30
**Assessor Version:** v1.0

**Quality State:** HIGH
**Research Approach:** Methodological (confidence: high)
**Paper Type:** Methodological (software paper)
**Assessment Pathway:** Standard (software is the computational component)

---

## Signal Score Summary

| Signal | Score | Band | Pathway |
|--------|-------|------|---------|
| Reproducibility | 82 | Excellent | Standard 🔧 |

**Cluster Rating:** Strong

> 🔧 **Context:** For software papers, Reproducibility assesses whether others can install, use, and extend the software. The software itself is the "computational component" being reproduced.

---

## Signal 6: Reproducibility

**Score:** 82/100 (Excellent)

**Pathway:** Standard
**Approach anchors applied:** Methodological

### Assessment

This software paper demonstrates excellent reproducibility. The FAIMS Mobile platform is fully available for reproduction: source code on GitHub under GPLv3, archival snapshot at ElsevierSoftwareX, compiled application on Google Play. This represents best practice for research software papers.

**Code availability** is exemplary. The source code is available in multiple locations: active development at https://github.com/FAIMS, archival snapshot at ElsevierSoftwareX/SOFTX-D-17-00021. The GPLv3 licence ensures full open source rights. User-to-Developer documentation at https://github.com/FAIMS/UserToDev supports extension and customisation.

**Environment specification** is good. The paper specifies Android platform (native application), Ubuntu server, and key dependencies (BeanShell, SQLite). Version 2.5+ is documented. However, exact build dependencies and development environment setup are in external documentation rather than the paper itself.

**Installation accessibility** is excellent. The compiled application is available on Google Play for direct installation. Users can deploy FAIMS without building from source. Server installation procedures exist in documentation.

**Workflow documentation** for customisation is comprehensive. The paper describes the module definition system, BeanShell scripting, and data schema configuration. Library of customisation modules available at GitHub.

### Evidence

**From reproducibility_infrastructure:**
- Code availability: **Yes** — GitHub (active + archival), GPLv3
- Data availability: **N/A** — Software paper, no research data
- Persistent identifiers: ElsevierSoftwareX archival link
- FAIR: N/A (software paper)

**From methods/protocols:**
- Module customisation workflow documented
- BeanShell scripting approach described
- Server architecture explained

**Strengths:**
- Full source code available (GitHub, GPLv3)
- Archival snapshot provides permanent link
- Compiled app on Google Play
- User-to-Developer documentation
- Customisation module library

**Weaknesses:**
- Build environment details in external docs not paper
- Server installation may require technical expertise

### Tool Assessment

| Aspect | Status | Tool Type | Impact |
|--------|--------|-----------|--------|
| Mobile application | Android native | open_source | Ideal |
| Server | Ubuntu/Linux | open_source | Ideal |
| Scripting | BeanShell | open_scriptable | Ideal |
| Build system | Not detailed | N/A | Minor gap |

### Scoring Rationale

Score of 82 (Excellent) reflects: complete source code publicly available with PIDs (80-100); open source GPLv3 licence (80-100); environment specified at platform level (60-79 for details); workflow documented (60-79); software executable via Google Play (80-100). Strong overall software reproducibility.

---

## Reproducibility Readiness Checklist

```yaml
reproducibility_readiness:
  applies: true
  pathway: "standard"
  if_not_applicable_reason: ""

  inputs_available:
    status: "not_applicable"
    details: "Software paper - no research data inputs. The software itself IS the reproducible artefact."

  code_available:
    status: "yes"
    tool_type: "open_source"
    details: "GitHub (active + archival snapshot), GPLv3 licence, Google Play for compiled app."

  environment_specified:
    status: "partial"
    details: "Platform specified (Android, Ubuntu). Build dependencies in external documentation. Google Play install bypasses build requirements."

  outputs_documented:
    status: "yes"
    details: "Software capabilities documented. Screenshots and feature descriptions in paper. Module library demonstrates outputs."

  execution_feasibility: "ready"
  feasibility_rationale: "Software is fully available for use via Google Play. Source code available for extension. Customisation documented. No barriers to reproduction."

  publication_year: 2018
  adoption_context: "early_adopter"
```

---

## Cluster Synthesis

**Overall Reproducibility:** Strong

This software paper demonstrates strong reproducibility — the software described is fully available for installation, use, and extension. The combination of Google Play availability (easy installation), GitHub source (full code access), GPLv3 licence (open source rights), and archival snapshot (permanent link) represents best practice for research software papers.

### Chronological Context

Publication year 2018 places this paper in the **early adopter** era. For 2018, having full open source code, Google Play distribution, and archival snapshot exceeds typical expectations. This reflects the authors' commitment to software sustainability and reproducibility.

### Gateway Assessment

**Execution Feasibility:** Ready

This software is ready for immediate use:

**Available now:**
- Compiled application on Google Play
- Full source code on GitHub
- User-to-Developer documentation
- Customisation module library

**No gaps blocking use:**
- Installation: Google Play (trivial)
- Customisation: Documentation available
- Extension: Source code under GPLv3

**Recommendation:** Fully ready for deployment. Users can install via Google Play and customise using documented procedures. Developers can fork and extend under GPLv3.

---

## Structured Output

```yaml
cluster_3_reproducibility:
  paper_slug: "ballsun-stanton-et-al-2018"
  assessment_date: "2025-11-30"
  quality_state: "high"
  research_approach: "methodological"
  pathway: "standard"
  experimental: false

  reproducibility:
    score: 82
    band: "excellent"
    strengths:
      - "Full source code on GitHub (GPLv3)"
      - "Archival snapshot at ElsevierSoftwareX"
      - "Compiled app on Google Play"
      - "User-to-Developer documentation"
    weaknesses:
      - "Build environment in external docs"
    rationale: "Excellent software reproducibility. Full code access, open source licence, easy installation via Google Play."
    tool_assessment:
      primary_tool_type: "open_source"
      tool_impact: "Ideal - full source code available"

  reproducibility_readiness:
    applies: true
    pathway: "standard"
    inputs_available:
      status: "not_applicable"
      details: "Software paper - no research data"
    code_available:
      status: "yes"
      tool_type: "open_source"
      details: "GitHub, GPLv3, Google Play"
    environment_specified:
      status: "partial"
      details: "Platform specified; build deps in external docs"
    outputs_documented:
      status: "yes"
      details: "Software capabilities documented"
    execution_feasibility: "ready"
    feasibility_rationale: "Software fully available via Google Play"
    publication_year: 2018
    adoption_context: "early_adopter"

  cluster_synthesis:
    overall_rating: "strong"
    chronological_interpretation: "2018 paper exceeds era expectations with full open source, archival snapshot"
    gateway_recommendation: "Ready for immediate deployment; no barriers to use"
```
