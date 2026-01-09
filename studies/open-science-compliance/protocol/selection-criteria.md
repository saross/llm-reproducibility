# Corpus Selection Criteria

**Study:** Open Science Compliance Study
**Phase:** 1 (Exploratory Pilot)
**Date:** 2025-01-09

---

## Inclusion Criteria

Papers must meet ALL of the following:

### 1. Journal

- **Required:** Journal of Archaeological Science (JAS) — main journal
- **Excluded:** JAS: Reports (sister journal) — may be included in Phase 2

### 2. Publication Window

- **Required:** Published 2023-2025
- **Rationale:** Post-JAS reproducibility policy (January 2024) and recent enough for current practices

### 3. Access

- **Required:** Open Access (gold OA, green OA, or accessible preprint)
- **Acceptable:** Author-deposited versions in institutional repositories
- **Excluded:** Paywalled articles without accessible version

### 4. Computational Component

- **Required:** Paper mentions code, software, statistical analysis, or computational methods in abstract or methods section
- **Indicators:**
  - Programming languages mentioned (R, Python, MATLAB, etc.)
  - Statistical software mentioned (SPSS, JASP, etc.)
  - "Code available" or "Data available" statements
  - GitHub, Zenodo, OSF repository mentioned
  - Computational methods (Bayesian inference, machine learning, simulation, GIS analysis)

### 5. Language

- **Required:** English

### 6. Article Type

- **Required:** Original research article
- **Excluded:** Reviews, editorials, commentaries, erratum, correspondence

---

## Exclusion Criteria

Papers are excluded if ANY of the following apply:

1. **Not JAS main journal** — JAS: Reports excluded for Phase 1
2. **Published before 2023** — Pre-policy baseline not assessed in pilot
3. **Not open access** — Cannot assess without full text
4. **No computational component** — Purely descriptive or qualitative without code
5. **Not in English** — Assessment methodology designed for English
6. **Not original research** — Reviews, editorials, etc.

---

## Sampling Strategy

### Phase 1 (Pilot)

**Target:** 5 papers

**Strategy:** Purposive sampling for methodological diversity

| Criterion | Target |
|-----------|--------|
| Confirmed code repository | ≥3 papers |
| Different method types | ≥3 types |
| Post-2024 reproducibility policy | ≥2 papers |
| Award-recognised or exemplary | ≥1 paper |

### Phase 2 (Confirmatory)

**Target:** 15-25 papers

**Strategy:** TBD based on Phase 1 findings — may include:
- Random sampling from eligible pool
- Stratified sampling by year/method type
- Exhaustive sampling of reproducibility-badged papers

---

## Search Strategy

### Sources Consulted

1. **[benmarwick/ctv-archaeology](https://github.com/benmarwick/ctv-archaeology)** — CRAN Task View for Archaeological Science
   - Curated list of papers with code repositories
   - Updated regularly by Ben Marwick (JAS Reproducibility Specialist)

2. **[apalmisano82/Open_Science](https://github.com/apalmisano82/Open_Science)** — Open science practices dataset
   - CSV of JAS papers with reproducible research
   - From Palmisano & Titolo (2024)

3. **JAS website** — Direct journal searches
   - Reproducibility Prize winners
   - JAS-SAS Emerging Investigator Award

4. **Zenodo/GitHub/OSF** — Repository searches
   - "Journal of Archaeological Science" + year

### Search Terms

- "Journal of Archaeological Science" + 2024 + code
- "Journal of Archaeological Science" + GitHub
- "Journal of Archaeological Science" + reproducibility
- JAS reproducibility prize
- JAS-SAS award

---

## Selection Documentation

### Phase 1 Selection Record

| Slug | How Identified | Selection Rationale |
|------|----------------|---------------------|
| crema-et-al-2024 | ctv-archaeology | Exemplary compendium, Bayesian methods |
| marwick-2025 | Web search | Meta-analysis by Reproducibility Specialist |
| key-et-al-2024 | ctv-archaeology | Code in title, morphometrics |
| herskind-riede-2024 | JAS-SAS Award search | Award winner, novel NLP methods |
| dye-et-al-2023 | ctv-archaeology | CRAN package, Bayesian chronology |

### Rejected Candidates

| Paper | Reason for Exclusion |
|-------|---------------------|
| (None rejected in Phase 1 — all candidates met criteria) | |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-01-09 | Initial criteria |
