# Cluster 3: Reproducibility Assessment

**Paper:** ballsun-stanton-et-al-2018
**Assessment Date:** 2025-12-02
**Assessor Version:** v1.0

**Quality State:** HIGH
**Research Approach:** inductive (confidence: high)
**Paper Type:** methodological (software_tool)
**Assessment Pathway:** standard

---

## Signal Score Summary

| Signal | Score | Band | Pathway |
|--------|-------|------|---------|
| Reproducibility | 85 | excellent | standard |

**Cluster Rating:** Strong

---

## Signal 6: Reproducibility

**Score:** 85/100 (excellent)

**Pathway:** standard
**Approach anchors applied:** inductive/methodological (software publication)

### Assessment

This software publication achieves excellent reproducibility through comprehensive open-source code availability, extensive documentation, and clear licensing. The core question for this paper type is: **Can others install, use, and extend the software as described?** The answer is strongly affirmative.

**Code Availability:** The software is fully available under GPLv3 open-source licence through multiple distribution channels: GitHub (Elsevier SoftwareX archive), FAIMS Project GitHub organisation, Google Play Store, and direct APK download. The extraction identified 4 distinct repository/distribution channels with clear access conditions. Version information is explicit (code version 2.5, executable version 2.5.20—E001).

**Environment Specification:** Dependencies are thoroughly documented. The code metadata explicitly lists all technologies: "Java, Ruby, XML, SQLite, Spatialite, Javarosa, Antlr, Puppet, Apache, Imagemagick, God, Beanshell, gson, guice, Nutiteq, NativeCSS, Protobuf, Robotium" (E003). Installation requirements are specified: "Android 6+, Ubuntu 16.04" (E004). This level of dependency documentation enables reproduction.

**Documentation:** Extensive supplementary materials support reproducibility: Module Cookbook (developer tutorial), Beanshell API documentation, User-to-Developer guide, and getting started documentation. The extraction identified 5 supplementary material items with URLs. The documentation is comprehensive enough that independent projects have "customised FAIMS Mobile themselves using both the detailed approach of producing an entire definition packet and the simplified DSL-based method" (E011, C009).

**FAIR Assessment:** The extraction's FAIR assessment scored high across all dimensions: Findable (DOI present, multiple repositories), Accessible (open access, no barriers), Interoperable (standard formats—XML, SQL, GeoJSON, CSV), Reusable (GPLv3 licence, documentation available).

The paper does not contain computational analyses requiring reproduction in the traditional sense—there are no statistical models, regressions, or data transformations to verify. Reproducibility here means software usability, which is well-supported.

### Evidence

**From reproducibility_infrastructure:**
- Code availability: **YES** — Statement present with 4 repositories: GitHub/SoftwareX, GitHub/FAIMS, Google Play, direct APK; GPLv3 licence; machine_actionability rated "high"
- Data availability: **NOT APPLICABLE** — Software publication; no research data; software itself is the output
- Persistent identifiers: Paper DOI (10.1016/j.softx.2017.12.006); software repository URLs (no software DOI)
- FAIR score: High across all dimensions (Findable, Accessible, Interoperable, Reusable)

**From methods/protocols:**
- P001: Definition packet creation workflow documented with steps and timeframe ("one to two developer-days")
- P002: Field deployment workflow documented with 7 steps
- P003: QA testing protocol documented (Robotium framework)
- P004: Data export protocol documented with format options

**Strengths:**
- GPLv3 open-source licence permits modification, redistribution, and commercial use
- Multiple distribution channels ensure long-term availability
- Comprehensive documentation (Module Cookbook, API docs, User-to-Developer guide)
- Explicit dependency listing (18 technologies) enables environment reproduction
- Independent customisations documented (E011)—proof of reproducible usage

**Weaknesses:**
- No software DOI—relies on repository URLs which may change
- No containerised environment (Docker) documented—requires manual environment setup
- Nutiteq library noted as "non-free" (E003)—potential reproducibility barrier for that component
- No automated build/test pipeline documentation for contributors

### Tool Assessment

| Aspect | Status | Tool Type | Impact |
|--------|--------|-----------|--------|
| Core software | Java, Ruby | Open scriptable | No demerit |
| Customisation | XML, Beanshell, CSS | Open scriptable | No demerit |
| Database | SQLite3, Spatialite | Open scriptable | No demerit |
| GIS component | Nutiteq | Proprietary (non-free) | Minor demerit |
| Testing | Robotium | Open scriptable | No demerit |
| Deployment | Puppet, Apache | Open scriptable | No demerit |

**Overall tool assessment:** Primarily open scriptable (17 of 18 technologies open), with one proprietary component (Nutiteq for map rendering). Minor reproducibility impact.

### Scoring Rationale

Score: 85 (Excellent for inductive/methodological software publication). Per inductive anchors: "Data archived with comprehensive documentation" ✓ (code is the data, fully archived); "Analysis workflow documented" ✓ (customisation, deployment, QA workflows documented); "Classification schemes explicit" ✓ (definition packet structure documented); "Raw observations accessible" ✓ (source code available); "Metadata complete" ✓ (technology stack, versions, dependencies); "FAIR met" ✓ (high across all dimensions). Does not reach 90+ because: no software DOI, no containerised environment, one proprietary component (Nutiteq), no contributor pipeline documentation.

---

## Reproducibility Readiness Checklist

```yaml
reproducibility_readiness:
  applies: true
  pathway: "standard"
  if_not_applicable_reason: ""

  inputs_available:
    status: "yes"
    details: "Software source code fully available via GitHub (2 repositories), Google Play, and direct APK. No input data required—software is the deliverable."

  code_available:
    status: "yes"
    tool_type: "open_scriptable"
    details: "Complete source code under GPLv3. Core: Java/Ruby. Customisation: XML/Beanshell/CSS. 17 of 18 dependencies open source. Version 2.5 (code) / 2.5.20 (executable) explicitly specified."

  environment_specified:
    status: "partial"
    details: "Dependencies fully enumerated (18 technologies listed). Platform requirements stated (Android 6+, Ubuntu 16.04). No containerised environment (Docker/Vagrant) documented. Manual environment setup required."

  outputs_documented:
    status: "yes"
    details: "Software functionality documented through feature descriptions, screenshots (implied), and extensive user/developer documentation. Expected outputs (data export formats—CSV, shapefile, GeoJSON, XML) explicitly specified."

  execution_feasibility: "ready"
  feasibility_rationale: "Software can be installed and run following documented procedures. Multiple distribution channels (GitHub, Google Play, APK) ensure availability. Documentation sufficient for independent deployment—evidence: external projects have successfully customised FAIMS (E011). Android app can be installed from Google Play immediately; server requires Ubuntu 16.04 setup."

  publication_year: 2018
  adoption_context: "early_adopter"
```

---

## Cluster Synthesis

**Overall Reproducibility:** Strong

The paper achieves strong reproducibility for a software publication from the early adopter era (2018). The comprehensive open-source availability, explicit licensing, and extensive documentation represent best practices for software reproducibility. The ability of external projects to independently customise FAIMS (E011) provides empirical validation that reproducibility infrastructure is sufficient.

### Chronological Context

Publication year 2018 places this paper in the **early adopter** era of reproducibility adoption. Code sharing was growing but not yet standard practice, particularly for complex multi-component software systems. In this context, the paper's reproducibility practices are **exemplary**:

- Open-source licensing (GPLv3) predates widespread funder mandates
- Multiple distribution channels exceed minimum requirements
- Documentation quality (Module Cookbook, API docs, User-to-Developer guide) exceeds typical 2018 practice
- Dependency enumeration is comprehensive

The high reproducibility score (85) reflects genuinely strong practices that would remain competitive by current (2025) standards, though modern expectations would additionally include containerisation and software DOIs.

### Gateway Assessment

**Execution Feasibility:** Ready

This paper could be queued for an actual reproduction attempt (software installation and customisation) with the following considerations:

**What would be needed to attempt reproduction:**
1. **Android device** (Android 6+) for mobile client installation—can use Google Play directly
2. **Ubuntu 16.04 server** for server component—requires manual setup following documentation
3. **Development environment** for customisation—follow Module Cookbook
4. **Optional:** Nutiteq licence for map rendering component (or substitute open alternative)

**Potential barriers:**
- Ubuntu 16.04 is now end-of-life (2021)—may need testing on newer Ubuntu versions
- Some repository URLs may have changed since 2018
- Nutiteq (now CARTO) licensing may have changed

**Recommended approach:** Contact FAIMS team for current deployment guidance; check for updated version (FAIMS 3.x exists as of 2025).

---

## Structured Output

```yaml
cluster_3_reproducibility:
  paper_slug: "ballsun-stanton-et-al-2018"
  assessment_date: "2025-12-02"
  quality_state: "high"
  research_approach: "inductive"
  paper_type: "methodological"
  pathway: "standard"
  experimental: false

  reproducibility:
    score: 85
    band: "excellent"
    strengths:
      - "Complete source code under GPLv3 via multiple distribution channels"
      - "Comprehensive documentation (Module Cookbook, API docs, User-to-Developer guide)"
      - "Explicit dependency enumeration (18 technologies)"
      - "Independent customisations documented—proof of reproducible usage"
      - "High FAIR scores across all dimensions"
    weaknesses:
      - "No software DOI—relies on repository URLs"
      - "No containerised environment documented"
      - "One proprietary component (Nutiteq)"
      - "Ubuntu 16.04 requirement now end-of-life"
    rationale: "Excellent reproducibility for software publication. Code fully available with GPLv3, comprehensive documentation, explicit dependencies, FAIR compliance. External customisations validate reproducibility infrastructure. Minor deductions for missing software DOI, no containerisation, one proprietary dependency."
    tool_assessment:
      primary_tool_type: "open_scriptable"
      tool_impact: "Minimal—17 of 18 technologies open source; one proprietary component (Nutiteq) creates minor barrier"

  reproducibility_readiness:
    applies: true
    pathway: "standard"
    inputs_available:
      status: "yes"
      details: "Software source code fully available via GitHub, Google Play, direct APK"
    code_available:
      status: "yes"
      tool_type: "open_scriptable"
      details: "Complete source under GPLv3; 17/18 dependencies open source"
    environment_specified:
      status: "partial"
      details: "Dependencies enumerated; platform requirements stated; no containerised environment"
    outputs_documented:
      status: "yes"
      details: "Feature documentation, export format specifications (CSV, shapefile, GeoJSON, XML)"
    execution_feasibility: "ready"
    feasibility_rationale: "Software installable following documented procedures; external customisations validate reproducibility; multiple distribution channels ensure availability"
    publication_year: 2018
    adoption_context: "early_adopter"

  cluster_synthesis:
    overall_rating: "strong"
    chronological_interpretation: "Exemplary reproducibility for 2018 early adopter era. Open-source licensing, multiple distribution channels, and comprehensive documentation exceed typical 2018 practice. Practices remain competitive by 2025 standards."
    gateway_recommendation: "Ready for reproduction attempt. Requires Android 6+ device and Ubuntu server. Check for updated FAIMS version (3.x) for current deployment. Contact FAIMS team for up-to-date guidance."
```
