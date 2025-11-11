# CReDIT (Contributor Roles Taxonomy)

**Purpose**: Reference guide for extracting and interpreting CReDIT contributor roles from author contribution statements

**Context**: CReDIT provides standardised taxonomy for describing author contributions, improving transparency and enabling proper credit attribution

**Audience**: Research assessor skill users performing infrastructure extraction (Pass 6) or validation (Pass 7)

---

## Overview

**CReDIT** (Contributor Roles Taxonomy) is a standardised framework developed by CASRAI (Consortia Advancing Standards in Research Administration Information) for describing individual author contributions to scholarly research outputs.

**Purpose**:
- Improve transparency about who did what in research
- Enable proper credit attribution (especially for early-career researchers, technicians, data scientists)
- Support assessment and evaluation (distinguish intellectual vs technical contributions)
- Address "gift authorship" and contribution inflation

**Adoption**: Increasingly requested or required by publishers (PLOS, eLife, Elsevier, Nature Portfolio journals, PNAS, etc.)

**Format in papers**: Usually appears in "Author Contributions" section with structured or narrative format

---

## The 14 CReDIT Roles

### 1. Conceptualisation

**Definition**: Ideas; formulation or evolution of overarching research goals and aims

**Typical contributors**: Principal investigators, project leaders, senior researchers

**Examples**:
- Developed research questions
- Formulated hypotheses
- Designed overall study framework

---

### 2. Data Curation

**Definition**: Management activities to annotate (produce metadata), scrub data, and maintain research data (including software code) for initial use and later re-use

**Typical contributors**: Data managers, curators, lab technicians, database administrators

**Examples**:
- Organised and maintained datasets
- Created metadata and data dictionaries
- Quality control and validation
- Database development

---

### 3. Formal Analysis

**Definition**: Application of statistical, mathematical, computational, or other formal techniques to analyse or synthesise study data

**Typical contributors**: Statisticians, computational specialists, analysts

**Examples**:
- Performed statistical analyses
- Ran computational models
- Conducted GIS analyses
- Applied Bayesian calibration

---

### 4. Funding Acquisition

**Definition**: Acquisition of the financial support for the project leading to this publication

**Typical contributors**: Principal investigators, co-investigators

**Examples**:
- Wrote grant proposals
- Secured funding
- Obtained research contracts

---

### 5. Investigation

**Definition**: Conducting a research and investigation process, specifically performing the experiments, or data/evidence collection

**Typical contributors**: Fieldwork directors, laboratory researchers, data collectors, excavation staff

**Examples**:
- Conducted excavations
- Collected field samples
- Ran laboratory analyses
- Gathered archival data
- Administered surveys

---

### 6. Methodology

**Definition**: Development or design of methodology; creation of models

**Typical contributors**: Methodological specialists, statisticians, modellers

**Examples**:
- Designed sampling strategy
- Developed analytical protocols
- Created computational models
- Designed experimental setup

---

### 7. Project Administration

**Definition**: Management and coordination responsibility for the research activity planning and execution

**Typical contributors**: Project managers, coordinators, principal investigators

**Examples**:
- Managed project logistics
- Coordinated team activities
- Administered contracts and agreements
- Scheduled fieldwork campaigns

---

### 8. Resources

**Definition**: Provision of study materials, reagents, materials, patients, laboratory samples, animals, instrumentation, computing resources, or other analysis tools

**Typical contributors**: Lab directors, collection managers, equipment providers

**Examples**:
- Provided access to museum collections
- Supplied laboratory equipment
- Contributed unpublished data
- Provided fieldwork infrastructure

---

### 9. Software

**Definition**: Programming, software development; designing computer programs; implementation of the computer code and supporting algorithms; testing of existing code components

**Typical contributors**: Software developers, programmers, bioinformaticians

**Examples**:
- Wrote analysis scripts
- Developed software tools
- Implemented algorithms
- Maintained code repositories

---

### 10. Supervision

**Definition**: Oversight and leadership responsibility for the research activity planning and execution, including mentorship external to the core team

**Typical contributors**: PhD supervisors, project leaders, senior researchers

**Examples**:
- Supervised research students
- Provided mentorship
- Led research team
- Oversaw project direction

---

### 11. Validation

**Definition**: Verification, whether as a part of the activity or separate, of the overall replication/reproducibility of results/experiments and other research outputs

**Typical contributors**: Independent validators, reproducibility checkers, quality assurance specialists

**Examples**:
- Verified computational reproducibility
- Replicated analyses
- Quality control checks
- Validated identifications (taxonomy, artefact types)

---

### 12. Visualisation

**Definition**: Preparation, creation and/or presentation of the published work, specifically visualisation/data presentation

**Typical contributors**: Graphic designers, illustrators, data visualisation specialists

**Examples**:
- Created figures and charts
- Designed maps
- Produced illustrations
- Developed data dashboards

---

### 13. Writing – Original Draft

**Definition**: Preparation, creation and/or presentation of the published work, specifically writing the initial draft (including substantive translation)

**Typical contributors**: First authors, writing leads

**Examples**:
- Wrote first draft of manuscript
- Created initial outline
- Translated text from another language

---

### 14. Writing – Review & Editing

**Definition**: Preparation, creation and/or presentation of the published work by those from the original research group, specifically critical review, commentary or revision – including pre- or post-publication stages

**Typical contributors**: All authors typically contribute to this role

**Examples**:
- Revised manuscript drafts
- Provided critical feedback
- Edited for clarity and accuracy
- Responded to reviewer comments

---

## CReDIT Format Variations

### Structured CReDIT Statement

**Format**: Explicit role labels with author initials

**Example**:
```
S.C.: Conceptualisation, Methodology, Investigation, Writing – Original Draft, Funding Acquisition
I.T.: Resources, Writing – Review & Editing, Supervision
A.B.: Formal Analysis, Data Curation, Visualisation, Software
```

**Extraction approach**: Parse roles by author, map to CReDIT taxonomy

---

### Narrative Format

**Format**: Free-text description without explicit CReDIT labels

**Example**:
```
S.C. designed the study, conducted fieldwork, and drafted the manuscript. I.T. provided access to laboratory facilities and supervised the research. A.B. performed the statistical analyses and created the figures. All authors contributed to manuscript revision and approved the final version.
```

**Extraction approach**: Map narrative descriptions to approximate CReDIT roles, note when ambiguous

---

### Mixed Format

**Format**: Combination of structured and narrative

**Example**:
```
S.C. and I.T. conceived the study (Conceptualisation). S.C. conducted fieldwork (Investigation) and wrote the first draft (Writing – Original Draft). Formal Analysis and Visualisation were performed by A.B. All authors contributed to writing and revision (Writing – Review & Editing).
```

**Extraction approach**: Parse both structured roles and narrative descriptions

---

## Extraction Guidance

### When Extracting Author Contributions (Pass 6):

1. **Locate Author Contributions section** - Usually near end of paper (before or after Acknowledgements)

2. **Identify format** - Structured CReDIT, narrative, or mixed?

3. **Extract contribution for each author**:
   - Author name
   - CReDIT roles (if structured format)
   - Free-text description (if narrative format)

4. **Cross-reference with ORCIDs** - Link contributions to author ORCID identifiers if available

5. **Validate author count** - Ensure contribution statement covers all authors from paper metadata

6. **Note format** in extraction metadata:
   - Format: "credit" (structured), "narrative" (free text), "mixed", "equal_contribution" (if stated), "not_stated"

---

## Common Patterns in HASS Research

### Multi-author archaeology papers often show:

- **Conceptualisation**: 1-2 senior researchers (PIs)
- **Methodology**: 1-3 specialists (dating, sampling, GIS, statistics)
- **Investigation**: 2-8 researchers (excavation team, lab analysts)
- **Formal Analysis**: 1-4 specialists (stats, aDNA, isotopes, GIS)
- **Resources**: 1-2 (lab facilities, collections access)
- **Data Curation**: 1-2 (often underrecognised role)
- **Software**: 0-2 (emerging; computational archaeology)
- **Visualisation**: 1-3 (maps, figures, reconstructions)
- **Writing – Original Draft**: 1-2 (usually first author)
- **Writing – Review & Editing**: All authors
- **Funding Acquisition**: 1-3 (grant holders)
- **Supervision**: 1-2 (PhD supervisors, project leads)

---

## Assessment Implications

### Transparency Signal

**CReDIT statements improve transparency** by:
- Making division of labour explicit
- Recognising all contributions (not just writing)
- Enabling identification of responsible parties for specific claims/methods

**Assessment indicators**:
- ✅ **Exemplary**: Structured CReDIT with all authors, roles clearly assigned
- ✅ **Good**: Narrative contribution statement covering major roles
- ⚠️ **Minimal**: "All authors contributed equally" (lacks specificity)
- ❌ **Absent**: No author contribution statement

---

### Credibility Implications

**Who performed which analyses matters for assessment**:
- **Formal Analysis** role indicates who to contact about statistical methods
- **Data Curation** role indicates who can provide data access
- **Investigation** role indicates who conducted fieldwork (primary data collection)
- **Validation** role indicates independent quality checks performed

**Cross-validation opportunities**:
- Do stated contributions match methods description?
- Do ORCIDs link to expertise profiles consistent with contributions?
- Are data/code repositories attributed to correct Software/Data Curation contributors?

---

### Evolution from Authorship Order

**Traditional approach**: Authorship order signals contribution
- First author: primary contributor
- Last author: senior author/PI
- Middle authors: unclear contribution

**CReDIT improvement**: Explicit roles, reducing ambiguity and enabling proper credit

---

## Linking to ORCIDs

When both CReDIT and ORCIDs present:

**Enhanced transparency through linkage**:
- ORCID profiles can verify expertise claims (past work in same roles)
- Funders can track Funding Acquisition roles
- Institutions can verify supervisory relationships (Supervision role)
- Career progression tracking (early-career researchers moving from Investigation → Methodology → Conceptualisation)

**Extraction approach**: Create combined data structure linking author name → ORCID → CReDIT roles

---

## Validation Checks (Pass 7)

When validating author contributions:

1. **Completeness**: Do contributions cover all authors listed in paper metadata?
2. **Consistency**: Do contributions align with methods descriptions?
3. **Plausibility**: Are roles reasonable for author positions (e.g., students unlikely to have Funding Acquisition)
4. **ORCID alignment**: Do ORCID profiles show expertise consistent with stated roles?

---

## References

- Brand et al. (2015). Beyond authorship: Attribution, contribution, collaboration, and credit. *Learned Publishing* 28:151-155. https://doi.org/10.1087/20150211
- CReDIT Taxonomy: https://credit.niso.org/
- Allen et al. (2019). Publishing: Credit where credit is due. *Nature* 508:312-313. https://doi.org/10.1038/508312a
- CASRAI: https://casrai.org/credit/

---

**Document Version**: 1.0
**Last Updated**: 2025-11-11
**Part of**: research-assessor skill infrastructure assessment capability
