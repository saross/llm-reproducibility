# Cluster 1: Foundational Clarity (Transparency Pillar)

**Paper:** Ballsun-Stanton et al. (2018) - FAIMS Mobile
**Run:** run-04
**Date:** 2025-12-03
**Paper Type:** Methodological (Software Publication)

---

## Signals Assessed

- **Comprehensibility:** Can qualified readers understand what was done?
- **Transparency:** Is the research process sufficiently documented for scrutiny?

---

## Signal 1: Comprehensibility

### Rating: **STRONG** (85/100)

### Assessment

The paper provides clear, accessible descriptions of FAIMS Mobile's architecture, functionality, and deployment model.

**Strengths:**

1. **Clear problem statement** (Section 1): Field research data collection challenges are articulated with references to prior literature.

2. **Systematic architecture description** (Section 2.1): Technology stack enumerated component-by-component with roles explained.
   > "FAIMS uses the following technologies: Javarosa to render native Android UI elements at runtime; Sqlite3 to store an attribute-key-value datastore..."

3. **Effective analogy:** Browser-website metaphor clarifies core/definition packet separation.
   > "This distinction between the 'core' client and the definition packet resembles the one between a web browser and a website."

4. **Comprehensive feature documentation** (Section 2.2): Bulleted list format enables quick comprehension.

5. **Visual aids:** Figures 1-4 illustrate interface, metadata capture, and GIS functionality.

6. **Comparison with alternatives:** ODK comparison helps readers position FAIMS in the landscape.

**Weaknesses:**

1. **Technical jargon:** Terms like "definition packets", "DSL", "Beanshell" assume developer familiarity.

2. **Limited workflow narrative:** No end-to-end deployment scenario walks through typical use.

3. **Impact evidence summary:** Deployment statistics presented without methodology.

### Scoring Rationale (Methodological/Software Paper)

For software publications, Comprehensibility emphasises whether readers can understand:
- What the software does (clear ✅)
- How it works architecturally (clear ✅)
- How to use/customise it (adequate with documentation pointers ✅)
- What outcomes it produces (moderately clear ⚠️)

**Score: 85/100**

---

## Signal 2: Transparency

### Rating: **STRONG** (90/100)

### Assessment

The paper achieves excellent transparency for software publications through comprehensive code and documentation availability.

**Strengths:**

1. **Full source code availability:**
   - GitHub repository: https://github.com/ElsevierSoftwareX/SOFTX-D-17-00021
   - FAIMS organisation: https://github.com/FAIMS
   - GPLv3 licensing ensures open access

2. **Version specificity:**
   - Code version: 2.5
   - Software version: 2.5.20
   - Clear version numbering enables reproducibility

3. **Multiple documentation channels:**
   - User documentation: Atlassian wiki
   - Developer documentation: Module Cookbook, Beanshell API
   - User-to-Developer guide: GitHub repository

4. **Installation procedures:**
   - Server installer script provided
   - Android app on Google Play and direct APK download
   - Dependencies explicitly listed

5. **Permanent archival links:**
   - Perma.cc links alongside primary URLs
   - Addresses link rot concerns

6. **Technology stack disclosure:**
   - All languages, libraries, and services enumerated
   - Non-free component (Nutiteq) explicitly noted

**Weaknesses:**

1. **Deployment statistics methodology:** How 40+ customisations, 300 users, 20,000+ hours were tracked is not documented.

2. **Case study data:** User feedback from Sobotkova et al. (2016) referenced but not reproduced; readers must access external publication.

3. **Module library completeness:** GitHub library mentioned but specific module count/coverage not documented.

### Scoring Rationale (Software Publication)

For software papers, Transparency emphasises:
- Code availability (excellent ✅)
- Documentation accessibility (excellent ✅)
- Installation/deployment procedures (excellent ✅)
- Usage evidence transparency (moderate ⚠️)

**Score: 90/100**

---

## Cluster 1 Summary

| Signal | Rating | Score |
|--------|--------|-------|
| Comprehensibility | Strong | 85 |
| Transparency | Strong | 90 |
| **Cluster Average** | **Strong** | **87.5** |

### Key Findings

1. **Outstanding software transparency:** Code, documentation, and deployment procedures fully accessible under open license.

2. **Clear technical communication:** Architecture and features well-explained with effective analogies and visual aids.

3. **Gap in impact transparency:** Methods for collecting deployment statistics and user feedback not documented.

### Cluster Rating: **STRONG**
