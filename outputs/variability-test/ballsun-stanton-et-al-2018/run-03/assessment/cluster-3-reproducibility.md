# Cluster 3: Reproducibility Assessment

**Paper:** ballsun-stanton-et-al-2018
**Assessment Date:** 2025-12-02
**Assessor Version:** v1.0

**Quality State:** HIGH
**Research Approach:** inductive (confidence: high)
**Paper Type:** methodological (software_tool)
**Assessment Pathway:** standard (software with computational components)

---

## Signal Score Summary

| Signal | Score | Band | Pathway |
|--------|-------|------|---------|
| Reproducibility | 85 | Excellent | standard |

**Cluster Rating:** Strong

---

## Signal 6: Reproducibility

**Score:** 85/100 (Excellent)

**Pathway:** standard (software publication with computational components)
**Approach anchors applied:** inductive (methodological paper)

### Assessment

FAIMS Mobile demonstrates excellent reproducibility for a software publication. The paper provides comprehensive infrastructure for software installation, customisation, and deployment. Code is publicly available under GPLv3 license via permanent GitHub repository. All dependencies are explicitly documented in the Code metadata table.

For software publications, "reproducibility" means: can users install, customise, and deploy the software? FAIMS provides strong support for this:

1. **Code availability:** Complete source code on GitHub (https://github.com/ElsevierSoftwareX/SOFTX-D-17-00021) under GPLv3
2. **Environment specification:** Android 6+ client, Ubuntu 16.04 server, all dependencies listed including versions
3. **Documentation:** Multiple resources - Module Cookbook, Beanshell API, User to Developer documentation
4. **Customisation instructions:** Definition packet structure, DSL syntax documented
5. **Community support:** Documentation links to FAIMS community resources

The paper uses open scriptable tools throughout - Android (Java), Beanshell scripting, XML configuration. The only proprietary dependency is Nutiteq mapping library, which is documented honestly.

Minor gaps: exact versions of some dependencies not specified, and some aspects of server configuration may require additional documentation beyond what's in the paper.

### Evidence

**From reproducibility_infrastructure:**

- Code availability: **Complete** - GPLv3, GitHub repository with permanent link
- Data availability: **Not applicable** - software paper, no research data
- Persistent identifiers: DOI 10.1016/j.softx.2017.12.006, GitHub URL
- FAIR score: Not formally calculated (software paper)

**From methods/protocols:**

- P001: "Definition packet implementation: Standardized XML structure with Beanshell scripts, CSS, annotation files, and properties files"
- P002: "DSL-based module generation: Scripted configuration generation from simplified definition language"
- M001: "Definition packet customisation: Deep customisation through XML documents, Beanshell scripts, and CSS styling"

**Strengths:**

- Complete source code availability under permissive open source license
- Comprehensive dependency documentation in Code metadata table
- Multiple documentation resources for different user types
- Open scriptable tool chain (Java, Beanshell, XML)

**Weaknesses:**

- One proprietary dependency (Nutiteq) - documented but limits full open reproducibility
- Some dependency versions not specified
- Server configuration may need supplementary documentation

### Tool Assessment

| Aspect | Status | Tool Type | Impact |
|--------|--------|-----------|--------|
| Core application | Android (Java) | open_scriptable | No demerit |
| Customisation scripts | Beanshell | open_scriptable | No demerit |
| Configuration | XML, CSS | open_scriptable | No demerit |
| Mapping | Nutiteq | proprietary | Minor demerit |
| Database | SQLite | open_scriptable | No demerit |
| Server | Ubuntu Linux | open_scriptable | No demerit |

### Scoring Rationale

Score of 85 (Excellent for inductive/methodological). Data archived with comprehensive documentation (80-100 criterion): code on GitHub, dependencies listed, multiple documentation resources. Analysis workflow documented (80-100): definition packets, DSL, customisation process all specified. FAIR partially met (60-79): open source but one proprietary dependency. Near-excellent reproducibility for software publication.

---

## Reproducibility Readiness Checklist

```yaml
reproducibility_readiness:
  applies: true
  pathway: "standard"
  if_not_applicable_reason: ""

  inputs_available:
    status: "yes"
    details: "Source code fully available on GitHub under GPLv3. All configuration components (XML, Beanshell, CSS) included in repository structure."

  code_available:
    status: "yes"
    tool_type: "open_scriptable"
    details: "Complete Android application code and server components on GitHub. Build system documented. One proprietary dependency (Nutiteq) honestly noted."

  environment_specified:
    status: "yes"
    details: "Code metadata table specifies: Android 6+, Ubuntu 16.04, Java with Beanshell, SQLite3. Full dependency list provided including Spring Framework, Hibernate, Spatialite. Some versions not specified."

  outputs_documented:
    status: "partial"
    details: "Expected software behaviour documented through feature descriptions. No formal test suite outputs documented in paper, though Robotium automated testing is mentioned."

  execution_feasibility: "ready"
  feasibility_rationale: "Software installation and customisation feasible with documented resources. GitHub repository is permanent link. Multiple documentation resources available. One would need Android development environment and Ubuntu server to fully reproduce."

  publication_year: 2018
  adoption_context: "early_adopter"
```

---

## Cluster Synthesis

**Overall Reproducibility:** Strong

FAIMS Mobile demonstrates strong reproducibility infrastructure appropriate for software publication. Code availability is complete, dependencies documented, and documentation resources comprehensive. The paper represents excellent practice for software reproducibility in the early_adopter era (2018).

### Chronological Context

Publication year 2018 places this paper in the **early_adopter** era of reproducibility adoption. At this time, software reproducibility practices were emerging but not yet standard. FAIMS demonstrates exemplary practice for its era: open source licensing, GitHub repository, comprehensive dependency documentation, and multiple documentation resources. This would score well even against mainstream (post-2025) expectations.

### Gateway Assessment

**Execution Feasibility:** ready

This paper could be queued for software reproduction attempt. Required resources:

1. **Hardware:** Android device (6+), Ubuntu 16.04 server
2. **Development environment:** Android SDK, Java with Beanshell
3. **Time estimate:** 2-4 hours for basic installation, additional time for customisation
4. **Documentation:** All available via paper links and GitHub repository

**Potential barriers:**
- Nutiteq library availability (proprietary, may have licensing requirements)
- Server configuration may need additional setup beyond paper documentation
- Five-year-old software may need dependency updates for modern systems

**Recommendation:** Feasible reproduction attempt. Clear pathway from paper to running software.

---

## Structured Output

```yaml
cluster_3_reproducibility:
  paper_slug: "ballsun-stanton-et-al-2018"
  assessment_date: "2025-12-02"
  quality_state: "high"
  research_approach: "inductive"
  pathway: "standard"
  experimental: false

  reproducibility:
    score: 85
    band: "excellent"
    strengths:
      - "Complete source code under GPLv3 on permanent GitHub repository"
      - "Comprehensive dependency documentation in Code metadata table"
      - "Multiple documentation resources for different user types"
      - "Open scriptable tool chain throughout"
    weaknesses:
      - "One proprietary dependency (Nutiteq mapping library)"
      - "Some dependency versions not specified"
      - "Server configuration may need supplementary documentation"
    rationale: "Excellent for inductive/methodological. Code available, dependencies documented, workflow specified. Minor deduction for proprietary dependency and some version gaps."
    tool_assessment:
      primary_tool_type: "open_scriptable"
      tool_impact: "Minimal - predominantly open tools with one proprietary component honestly documented"

  reproducibility_readiness:
    applies: true
    pathway: "standard"
    inputs_available:
      status: "yes"
      details: "Complete source code on GitHub under GPLv3"
    code_available:
      status: "yes"
      tool_type: "open_scriptable"
      details: "Android app and server code available, one proprietary dependency noted"
    environment_specified:
      status: "yes"
      details: "Android 6+, Ubuntu 16.04, full dependency list in Code metadata"
    outputs_documented:
      status: "partial"
      details: "Feature behaviour documented, no formal test outputs in paper"
    execution_feasibility: "ready"
    feasibility_rationale: "Clear pathway to software reproduction with documented resources"
    publication_year: 2018
    adoption_context: "early_adopter"

  cluster_synthesis:
    overall_rating: "strong"
    chronological_interpretation: "Exemplary reproducibility practice for early_adopter era (2018). Would score well against mainstream expectations."
    gateway_recommendation: "Ready for reproduction attempt. Clear pathway, documented resources, accessible repository."
```
