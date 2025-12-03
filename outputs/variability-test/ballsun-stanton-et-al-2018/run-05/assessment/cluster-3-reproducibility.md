# Cluster 3: Reproducibility Assessment

**Paper:** ballsun-stanton-et-al-2018
**Assessment Date:** 2025-12-03
**Assessor Version:** v1.0

**Quality State:** HIGH
**Research Approach:** inductive (confidence: high)
**Paper Type:** methodological (subtype: software_tool)
**Assessment Pathway:** methodological_transparency_variant

---

## Signal Score Summary

| Signal | Score | Band | Pathway |
|--------|-------|------|---------|
| Reproducibility | 90 | Excellent | methodological_transparency_variant |

**Cluster Rating:** Strong

---

## Signal 6: Reproducibility

**Score:** 90/100 (Excellent)

**Pathway:** methodological_transparency_variant
**Approach anchors applied:** methodological

### Assessment

This software publication achieves exceptional reproducibility for its genre. The paper describes software infrastructure — the reproducible artefact IS the software itself, and it is exceptionally well-documented and accessible.

**Code Availability:** The software is fully open source (GPLv3) with multiple distribution channels:
- GitHub repository: https://github.com/ElsevierSoftwareX/SOFTX-D-17-00021 (version archived)
- FAIMS Project GitHub: https://github.com/FAIMS (active development)
- Google Play Store: direct installation for Android devices
- Direct APK download: https://www.fedarch.org/apk
- Server installation: Puppet-based wget/bash installer

**Documentation:** Comprehensive documentation exceeds typical standards:
- Module Cookbook: step-by-step module creation tutorial
- Beanshell API: complete API reference
- Developer documentation home: technical reference
- User to Developer documentation: end-user pathway to customisation
- All with permanent archived links (perma.cc)

**Environment Specification:** Clear requirements documented:
- Android 6+ for mobile client
- Ubuntu 16.04 for server
- Complete dependency list in code metadata table

**Validation Approach:** While this is a software description (not empirical validation study), the paper documents validation through case studies and adoption metrics. The software itself can be downloaded, installed, and tested by any reader.

### Evidence

**From reproducibility_infrastructure:**

- Code availability: YES — GPLv3, GitHub (Elsevier archive + FAIMS Project), Google Play, direct APK, server installer
- Data availability: Not applicable — software publication, not data paper
- Persistent identifiers: DOI (10.1016/j.softx.2017.12.006), perma.cc archived documentation links
- FAIR score: 93.75% — Excellent compliance

**From methods/protocols:**

- P001: FAIMS-led deployment workflow comprehensively documented
- P002: Module creation using definition packets with explicit steps
- P003: DSL-based module generation as simplified alternative
- P004: Server installation protocol with explicit commands

**Strengths:**

- Multiple redundant distribution channels ensure long-term availability
- Open source licence (GPLv3) ensures perpetual reusability
- Comprehensive documentation enables independent customisation
- Permanent archived links (perma.cc) protect against link rot
- Version archived at SoftwareX GitHub for paper-specific reproducibility

**Weaknesses:**

- Some proprietary dependencies noted (Nutiteq for non-watermarked GIS) — documented as optional
- No containerisation (Docker) for fully reproducible environment — not standard practice in 2017

### Tool Assessment

| Aspect | Status | Tool Type | Impact |
|--------|--------|-----------|--------|
| Mobile client | Android/Java | open_scriptable | No demerit |
| Server | Ruby on Rails | open_scriptable | No demerit |
| Customisation | XML/Beanshell/CSS | open_scriptable | No demerit |
| GIS rendering | Nutiteq (optional) | proprietary | Minor demerit (optional) |
| Installation | Puppet | open_scriptable | No demerit |

### Scoring Rationale

Score of 90 reflects Excellent band (80-100) for methodological papers. All criteria exceeded: software architecture documented with design rationale; code publicly available via multiple channels (GPLv3, GitHub, Google Play); environment specified (Android 6+, Ubuntu 16.04); dependencies documented. The software itself is the reproducible artefact, and it is exceptionally accessible. Minor deduction for optional proprietary dependency (Nutiteq) and absence of containerisation (not standard practice in 2017 publication).

---

## Reproducibility Readiness Checklist

```yaml
reproducibility_readiness:
  applies: true
  pathway: "methodological_transparency_variant"
  if_not_applicable_reason: ""

  inputs_available:
    status: "yes"
    details: "Software is the input/output. Fully available: GitHub repository (archived version + active development), Google Play, direct APK, server installer. Multiple redundant channels ensure availability."

  code_available:
    status: "yes"
    tool_type: "open_scriptable"
    details: "GPLv3 licensed. Complete source code available on GitHub. Server and mobile components fully accessible. Java (Android), Ruby (server), XML/Beanshell/CSS (customisation). Documentation comprehensive."

  environment_specified:
    status: "yes"
    details: "Android 6+ for mobile, Ubuntu 16.04 for server. Complete dependency list in paper metadata table. Puppet-based installation automates server setup. No containerisation (Docker) but clear manual requirements."

  outputs_documented:
    status: "yes"
    details: "Expected outputs are functioning software installations. Paper includes screenshots (Figs. 1-4) demonstrating expected UI. Adoption metrics document expected scale of operation (40+ customisations, 29 deployments, 300 users, 20,000+ hours)."

  execution_feasibility: "ready"
  feasibility_rationale: "Software can be downloaded and installed immediately. Android app available on Google Play for immediate testing. Server installation requires Ubuntu 16.04 (may need updating for current systems). Module customisation documented with tutorials. Active project with support email (support@fedarch.org)."

  publication_year: 2018
  adoption_context: "early_adopter"
```

---

## Cluster Synthesis

**Overall Reproducibility:** Strong

This paper achieves exceptional reproducibility for a software publication. The software is fully open source (GPLv3), available through multiple redundant channels (GitHub archive, active development repository, Google Play, direct download, server installer), and comprehensively documented (Module Cookbook, API reference, developer documentation, user-to-developer pathway).

The reproducibility infrastructure directly embodies best practices for software publication: permanent archiving at SoftwareX GitHub for version-specific reproducibility, active development repository for ongoing use, multiple distribution channels for accessibility, and permanent archived links (perma.cc) protecting against link rot.

### Chronological Context

Publication year 2018 places this paper in the **early_adopter** era of reproducibility adoption. In this context, the reproducibility infrastructure is exceptional — code/data sharing was emerging but not yet standard, and this paper exceeds what would be expected for its era. The comprehensive documentation and multiple distribution channels represent leading-edge practice for 2017/2018.

### Gateway Assessment

**Execution Feasibility:** Ready

This paper is immediately reproducible:

1. **What's needed:** Android device or emulator for mobile testing; Ubuntu 16.04 (or updated equivalent) for server installation
2. **How to proceed:**
   - Download FAIMS Mobile from Google Play or https://www.fedarch.org/apk
   - Install server using documented Puppet script (may need adaptation for current Ubuntu versions)
   - Access existing modules from GitHub library or follow Module Cookbook to create custom module
   - Contact support@fedarch.org for assistance

3. **Potential challenges:**
   - Ubuntu 16.04 is now EOL; server installation may need updating for current LTS
   - Nutiteq licence required for non-watermarked GIS (optional)
   - Robotium testing framework may need updates for current Android versions

The software is a living project with active maintenance — reproduction is not just possible but actively supported.

---

## Structured Output

```yaml
cluster_3_reproducibility:
  paper_slug: "ballsun-stanton-et-al-2018"
  assessment_date: "2025-12-03"
  quality_state: "high"
  research_approach: "inductive"
  paper_type: "methodological"
  paper_subtype: "software_tool"
  pathway: "methodological_transparency_variant"
  experimental: false

  reproducibility:
    score: 90
    band: "excellent"
    strengths:
      - "Multiple redundant distribution channels (GitHub, Google Play, direct APK, server installer)"
      - "Open source licence (GPLv3) ensures perpetual reusability"
      - "Comprehensive documentation (Cookbook, API, developer docs, user-to-developer)"
      - "Permanent archived links (perma.cc) protect against link rot"
      - "Version archived at SoftwareX GitHub for paper-specific reproducibility"
    weaknesses:
      - "Optional proprietary dependency (Nutiteq for GIS)"
      - "No containerisation (not standard practice in 2017)"
    rationale: "Excellent band achieved. All criteria exceeded: code publicly available (GPLv3, multiple channels), environment specified, dependencies documented. Software is the reproducible artefact and is exceptionally accessible. Minor deductions for optional proprietary dependency and absence of containerisation."
    tool_assessment:
      primary_tool_type: "open_scriptable"
      tool_impact: "No demerit - fully open source stack (Java, Ruby, XML/Beanshell/CSS)"

  reproducibility_readiness:
    applies: true
    pathway: "methodological_transparency_variant"
    inputs_available:
      status: "yes"
      details: "Software fully available via multiple channels"
    code_available:
      status: "yes"
      tool_type: "open_scriptable"
      details: "GPLv3 licensed, GitHub repository, comprehensive documentation"
    environment_specified:
      status: "yes"
      details: "Android 6+, Ubuntu 16.04, full dependency list in paper"
    outputs_documented:
      status: "yes"
      details: "Expected outputs documented with screenshots and adoption metrics"
    execution_feasibility: "ready"
    feasibility_rationale: "Software can be downloaded and installed immediately. Active project with support available."
    publication_year: 2018
    adoption_context: "early_adopter"

  cluster_synthesis:
    overall_rating: "strong"
    chronological_interpretation: "Exceptional reproducibility for 2018 early_adopter era. Exceeds contemporary standards for software publication."
    gateway_recommendation: "Ready for immediate reproduction. Download from Google Play or GitHub, install server following documented procedure, access existing modules or create custom following Cookbook."
```
