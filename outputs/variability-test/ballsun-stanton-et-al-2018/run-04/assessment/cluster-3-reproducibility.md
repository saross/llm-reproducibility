# Cluster 3: Reproducibility (Reproducibility Pillar)

**Paper:** Ballsun-Stanton et al. (2018) - FAIMS Mobile
**Run:** run-04
**Date:** 2025-12-03
**Paper Type:** Methodological (Software Publication)

---

## Signals Assessed

- **Reproducibility:** Can the software be obtained, installed, and used to achieve similar results?

---

## Signal 6: Reproducibility

### Rating: **STRONG** (88/100)

### Assessment

For software publications, reproducibility concerns whether others can obtain, install, configure, and use the software to achieve comparable functionality.

**Strengths:**

1. **Complete source code availability:**
   - Primary repository: https://github.com/FAIMS
   - SoftwareX archive: https://github.com/ElsevierSoftwareX/SOFTX-D-17-00021
   - Full codebase accessible under GPLv3
   > "All source code available at GitHub under GPLv3"

2. **Explicit version identification:**
   - Code version: 2.5
   - Software version: 2.5.20
   - Enables precise reproduction of paper's described state

3. **Multiple installation pathways:**
   - Google Play Store distribution
   - Direct APK download
   - Server installer script
   > "Client available on Google Play Store, can also download .apk directly"

4. **Comprehensive documentation:**
   - User documentation on Atlassian wiki
   - Developer documentation via Module Cookbook
   - Beanshell API reference
   - User-to-Developer transition guide
   > "FAIMS provides documentation through several mechanisms..."

5. **Dependency transparency:**
   - Technology stack fully enumerated
   - Languages, libraries, and external services listed
   - Non-free component (Nutiteq) explicitly noted with alternatives

6. **Archival provisions:**
   - Perma.cc links for critical URLs
   - Addresses link rot concerns
   > "All perma.cc links effective as of 1st October 2017"

7. **Module library for templates:**
   - 24 public module definitions available
   - Reduces barrier to creating new deployments
   > "a 'library' of 24 public module definitions for FAIMS Mobile is being established on GitHub"

**Weaknesses:**

1. **Server infrastructure complexity:**
   - Requires Ubuntu server setup
   - Multiple service dependencies (CouchDB, etc.)
   - May challenge users without system administration experience

2. **Hardware requirements not specified:**
   - Android device specifications not documented
   - Server resource requirements unclear

3. **No containerised deployment:**
   - Docker or similar not mentioned
   - Would simplify reproducible deployment

4. **Documentation currency:**
   - Wiki links may become outdated
   - No versioned documentation snapshots

### FAIR Assessment (FAIR4RS Principles)

| Dimension | Score | Evidence |
|-----------|-------|----------|
| **Findable** | 9/10 | GitHub repositories indexed, DOI via SoftwareX publication, clear version numbering |
| **Accessible** | 9/10 | Open repositories, multiple download options, no authentication barriers |
| **Interoperable** | 8/10 | Standard Android platform, documented APIs, export formats specified |
| **Reusable** | 9/10 | GPLv3 license, modular architecture, extensive documentation, community engagement |
| **Total** | **35/40** | **87.5%** |

### Scoring Rationale (Software Publication)

For software papers, Reproducibility assesses:
- Code availability (excellent ✅)
- Documentation completeness (excellent ✅)
- Installation feasibility (good ✅)
- Version control and archival (excellent ✅)
- Deployment complexity (moderate ⚠️)

**Score: 88/100**

---

## Cluster 3 Summary

| Signal | Rating | Score |
|--------|--------|-------|
| Reproducibility | Strong | 88 |
| **Cluster Average** | **Strong** | **88** |

### Key Findings

1. **Exemplary open-source practice:** Full code availability under permissive license with multiple access pathways.

2. **Strong documentation ecosystem:** Layered documentation serves users, developers, and deployers.

3. **Version control excellence:** Clear version numbering enables precise reproduction.

4. **Archival awareness:** Perma.cc links demonstrate commitment to long-term accessibility.

5. **Deployment complexity:** Server requirements may limit accessibility for some users; containerisation would help.

### Cluster Rating: **STRONG**

