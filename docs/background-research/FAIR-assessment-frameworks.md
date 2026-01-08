# FAIR Assessment Frameworks: Operational Tools and Open Science Best Practices for LLM-Assisted Research Credibility

**The FAIR assessment landscape has matured significantly since 2016, with operational tools now enabling semi-automated evaluation of research outputs.** The RDA FAIR Data Maturity Model provides the foundational framework adopted across most implementations, while F-UJI offers the most deployable automated assessment tool. However, a critical gap persists: machine-actionability implementation substantially lags behind human-readable FAIR compliance, and archaeology/HASS disciplines remain underserved by existing assessment corpora. For an LLM-assisted system assessing archaeology papers, a hybrid approach combining automated metadata/PID verification (Stage 1-2) with LLM-enhanced interpretation of narrative elements offers the most promising path forward.

---

## Part 1: Core FAIR Assessment Frameworks and Operational Tools

### The foundational FAIR principles establish machine-actionability as central

The original FAIR Guiding Principles (Wilkinson et al., 2016, *Scientific Data* 3:160018, DOI: 10.1038/sdata.2016.18) comprise **15 principles** across four categories designed to enhance machine-actionable data discovery and reuse. The principles explicitly emphasize computational systems finding, accessing, and reusing data "with none or minimal human intervention."

The 15 principles structure as follows:
- **Findable (F1-F4)**: Persistent identifiers, rich metadata, explicit identifier-metadata linkage, searchable indexing
- **Accessible (A1-A2)**: Standardized retrieval protocols (with authentication options), metadata persistence beyond data lifespan
- **Interoperable (I1-I3)**: Formal knowledge representation languages, FAIR vocabularies, qualified cross-references
- **Reusable (R1.1-R1.3)**: Clear licensing, detailed provenance, domain-relevant community standards

Critically, the original publication described FAIR as a **continuum toward machine-actionability** rather than binary compliance—an aspiration that most assessment frameworks have adopted through graduated scoring.

### RDA FAIR Data Maturity Model provides the assessment lingua franca

The **RDA FAIR Data Maturity Model** (June 2020, DOI: 10.15497/rda00050) has become the de facto standard for FAIR assessment, developed by **200+ experts from 20+ countries** through consensus. It translates principles into **41 assessable indicators** organized by priority:

| Priority Level | Count | Examples |
|---------------|-------|----------|
| Essential (●●●) | Core indicators | Persistent identifiers, basic metadata |
| Important (●●) | High-value indicators | License information, provenance |
| Useful (●) | Enhancement indicators | Rich vocabularies, qualified references |

The model uses **graduated maturity levels (0-3)** rather than binary pass/fail, enabling nuanced assessment:
- Level 0: Not implemented
- Level 1: Initial/minimal compliance
- Level 2: Managed/moderate compliance  
- Level 3: Defined/full compliance

**URL**: https://zenodo.org/records/3909563 | **Publication**: https://datascience.codata.org/articles/10.5334/dsj-2020-041

### F-UJI delivers the most operationally mature automated assessment

**F-UJI** (https://www.f-uji.net | GitHub: https://github.com/pangaea-data-publisher/fuji) is the flagship automated FAIR assessment tool, developed by PANGAEA under the FAIRsFAIR project. It provides REST API-based programmatic assessment against **16-17 metrics** derived from the RDA model.

**Technical specifications for integration:**
- **Input**: Persistent identifier (DOI) or landing page URL
- **Output formats**: JSON (default), RDF/XML, Turtle, JSON-LD, N3 following W3C Data Quality Vocabulary
- **License**: MIT open source
- **Language**: Python 3.11
- **Authentication**: Basic auth for API access

**How F-UJI works technically:**
1. Accepts DOI/PID as input
2. Harvests metadata from multiple sources: landing page (schema.org, Dublin Core, DCAT), PID provider (DataCite content negotiation), repository registry (re3data API), Signposting typed links
3. Runs automated tests against each metric
4. Outputs individual metric scores, grouped F/A/I/R scores, and visualizations

**Metrics assessed:**

| Category | Metric IDs | What's Tested |
|----------|-----------|---------------|
| Findable | FsF-F1-01D/02D, F2-01M, F4-01M | PID scheme recognition, resolution, core metadata, schema.org/DC |
| Accessible | FsF-A1-02M/03D | HTTP/HTTPS protocol validation |
| Interoperable | FsF-I1-01M/02M | JSON-LD, RDFa, RDF detection; LOV namespace validation |
| Reusable | FsF-R1.1-01M, R1.2-01M, R1.3-01M | SPDX license matching, PROV-O provenance, community standards |

**Scoring output structure:**
- Per-metric numerical scores with maximum possible points
- **FAIR levels**: 3-tier maturity (incomplete/initial/moderate/advanced)
- **Maximum scores**: Findable=7, Accessible=3, Interoperable=4, Reusable=10

**External services F-UJI queries:**
- re3data (repository registry)
- DataCite API
- SPDX License List (https://spdx.org/licenses/)
- RDA Metadata Standards Catalog
- Linked Open Vocabularies (https://lov.linkeddata.es)

**Key limitation for paper assessment**: F-UJI assesses datasets at repository/DOI level, not research papers directly. Paper assessment requires a hybrid approach combining automated DOI/data assessment with manual or LLM-assisted evaluation of paper-level practices.

### Additional operational assessment tools

**FAIR-Checker** (https://fair-checker.france-bioinformatique.fr | GitHub: https://github.com/IFB-ElixirFr/FAIR-checker) offers complementary capabilities:
- Extracts embedded semantic annotations (JSON-LD, RDFa, HTML microdata)
- SPARQL queries for FAIR assessment against knowledge graphs
- **SHACL constraint validation** against Bioschemas profiles
- Enriches metadata via WikiData, OpenAIRE, OpenCitations
- Particularly strong for life science resources with Bioschemas markup

**ARDC FAIR Self-Assessment Tool** (https://ardc.edu.au/resource/fair-data-self-assessment-tool/) provides researcher-friendly manual assessment:
- Interactive web questionnaire with explanatory popups
- Outputs percentage scores per principle plus overall alignment
- Provides actionable improvement recommendations
- Educational component explaining FAIR concepts during assessment

**FAIR Evaluator** (https://w3id.org/AmIFAIR | GitHub: https://github.com/FAIRMetrics/Metrics) uses community-authored Maturity Indicators with pass/fail testing, producing detailed reports of what "a machine sees" when visiting a resource.

---

## Part 2: FAIR Variants for Different Research Output Types

### FAIR for Research Software (FAIR4RS) is now established

**FAIR4RS Principles** (May 2022, DOI: 10.15497/RDA00068, *Scientific Data* 9:622) adapt FAIR for software with key modifications:
- **F1.1/F1.2**: Components at different granularity and versions get distinct identifiers
- **Interoperability rewritten**: "Software interoperates with other software by exchanging data/metadata through standards"
- **Reusability expanded**: Addresses both executability and understanding/modification

**Maturity level: ESTABLISHED** — Community-endorsed after ~2 years development by 500+ contributors. Jointly convened by RDA, ReSA, and FORCE11.

**Assessment tools:**
- F-UJI extension for FAIR4RS metrics (FAIR-IMPACT project): https://github.com/FAIR-IMPACT/fuji
- ARDC FAIR Research Software Self-Assessment Tool (in development)
- ELIXIR Software Management Plan aligned with FAIR4RS

### FAIR for Computational Workflows has mature infrastructure

**Key publication**: Wilkinson et al. (2025), "Applying the FAIR Principles to computational workflows," *Scientific Data* 12:328 (DOI: 10.1038/s41597-025-04451-9)

Workflows are treated as **composite digital objects** requiring both FAIR data AND FAIR4RS principles. Key infrastructure:
- **WorkflowHub** (https://workflowhub.eu): FAIR workflow registry with 817+ workflows
- **RO-Crate**: Workflow packaging specification using schema.org + JSON-LD
- **LifeMonitor**: Workflow testing and monitoring service

**Maturity level: ESTABLISHED** — Strong ecosystem with automatic RO-Crate building, pytest-workflow testing framework.

### FAIR Digital Objects remain emerging

**FDO Forum** (https://fairdo.org) provides an **implementation framework** combining Digital Object Architecture with Semantic Web approaches. Every FDO requires: persistent identifier, type, metadata, provenance, and operations.

**Maturity level: EMERGING** — Specifications under active development (FDO Memos finalized May 2025), proof-of-concept implementations underway, but broad adoption still developing. RO-Crate serves as practical web-native FDO implementation.

### FAIR for Machine Learning (FAIR4ML) is nascent

The RDA FAIR4ML Interest Group (accepted September 2022) has published **FAIR4ML metrics** (September 2024, DOI: 10.5281/zenodo.13835105) and is developing a schema.org-based metadata schema. Complementary frameworks include Model Cards, Datasheets for Datasets, and Hugging Face's model documentation tools.

**Maturity level: EMERGING** — Monthly meetings, growing community, but assessment tools still developing.

---

## Part 3: Key Initiatives and Their Operational Outputs

### GO-FAIR provides FAIRification methodology

**GO-FAIR** (https://www.go-fair.org) operates through three pillars (GO CHANGE, GO TRAIN, GO BUILD) and Implementation Networks. Key operational outputs:
- **FAIR Data Point specification** (https://specs.fairdatapoint.org): Metadata provisioning infrastructure
- **FAIR Implementation Profiles (FIPs)**: Methodology for communities to declare FAIR practices
- **Metadata for Machines Workshops**: FAIRification training

**Current status**: Active through GO FAIR Foundation, though many Implementation Networks now archived.

### WorldFAIR produced the Cross-Domain Interoperability Framework

**WorldFAIR** (https://worldfair-project.eu, EC Horizon Europe 2022-2024) developed the **Cross-Domain Interoperability Framework (CDIF)** through 11 domain case studies including geochemistry, biodiversity, social sciences, and cultural heritage.

CDIF modules cover: Discovery, Access, Integration, Controlled Vocabularies, Mappings, Provenance, Temporal/Spatial description. **Continuing as WorldFAIR+** with CODATA coordination.

### EOSC drives European FAIR infrastructure

The **European Open Science Cloud** coordinates FAIR assessment through multiple projects:

**FAIRsFAIR (2019-2022)** produced:
- F-UJI automated assessment tool
- FAIR-Aware self-assessment tool
- 17 minimum viable metrics for data object assessment
- ACME-FAIR capability maturity guides

**FAIR-IMPACT (2022-2025, https://fair-impact.eu)** is extending:
- F-UJI for research software (17 metrics for FAIR4RS)
- O'FAIRe: Ontology FAIRness Evaluator for semantic artefacts
- Cascading grants for FAIR implementation

### RDA working groups provide authoritative recommendations

Beyond the FAIR Data Maturity Model, key RDA outputs include:
- **FAIRsharing Registry** (https://fairsharing.org): 1,293+ standards, 1,209+ databases, 118+ policies
- **FAIR Mappings WG**: Guidelines for crosswalks between schemas
- **I-ADOPT WG**: Framework for representing observable properties
- **Machine-Actionable DMP WG**: Standardized API for DMPs

---

## Part 4: Machine-Actionability Assessment—The Persistent Gap

### Evidence confirms machine-actionability substantially lags

The 2016 FAIR publication envisioned machine-actionability as central, yet **evidence strongly supports the hypothesis that implementation has lagged behind human-readable compliance**:

**From automated assessment limitations (CODATA 2024)**:
- "Automated tools are unable to capture any FAIR metrics in scenarios where a dataset doesn't at least have a URL and a machine-readable metadata record"
- "Generic FAIR assessment tools lack domain specificity"

**From F-UJI findings**:
- "Some aspects (rich, plurality, accurate, relevant) specified in FAIR principles still require human mediation"
- A2 principle (metadata persistence) is "virtually impossible to test" automatically—"no machine-interpretable indicator of tombstone status exists"

**From AgReFed Study (2024)**: Datasets improved from **47% to 74% FAIRness** after implementing machine-readable metadata, demonstrating the gap in initial implementations.

### What can be automatically tested for machine-actionability

**PID Infrastructure Verification:**

| Service | API Endpoint | What's Tested |
|---------|-------------|---------------|
| DOI/DataCite | https://api.datacite.org/dois/{doi} | Resolution, metadata retrieval |
| ORCID | https://pub.orcid.org/v3.0/{orcid} | Author identifier validation |
| ROR | https://api.ror.org/organizations/{ror_id} | Organization identifier lookup |

**Structured Metadata Assessment:**
- Schema.org JSON-LD embedded in landing pages
- Dublin Core meta tags
- DataCite content negotiation (6 mandatory properties: identifier, creator, title, publisher, publicationYear, resourceType)

**Signposting Protocol** (https://signposting.org/FAIR/) provides typed web links making landing pages machine-navigable:
- Level 1: `cite-as`, `describedby`, `item`, `author`, `license`, `type` links
- Level 2: Complete Link Sets (RFC9264)
- **Adopters**: Digital Repository of Ireland, Zenodo, Dataverse, RADAR

**License Machine-Readability:**
- SPDX identifier validation against https://spdx.org/licenses/
- Schema.org `license` property, Dublin Core `dc:rights`, Signposting `license` typed link

### Main barriers to machine-actionability

**Technical barriers:**
- No complete, authoritative cross-domain semantic resources registry
- No registry of scientific file formats with community mappings
- Limited machine-interpretable indicators for policies (tombstoning, access conditions)

**Implementation barriers:**
- Landing pages optimized for humans, not machines
- Content resources often on different platforms (can't modify HTTP headers)
- OAI-PMH can't use same PID as published object

---

## Part 5: Published FAIR Assessment Studies and Potential Validation Corpora

### Large-scale FAIR assessments provide methodological models

**Dental Research Data FAIR Assessment** (Sofi-Mahmudi et al., 2022, *J Dent Res*, PMID: 35656591):
- **Sample**: 7,509 articles from PubMed-indexed journals (2016-2021)
- **Finding**: Only 112 articles (1.5%) shared data
- **Methodology**: Programmatic assessment of sharing + FAIR compliance
- **Relevance**: Large-scale discipline-specific benchmark

**Data Sharing Across Disciplines** (Tedersoo et al., 2021, *Scientific Data* 8:192):
- **Sample**: Articles from 9 disciplines in Nature and Science (2000-2019)
- **Disciplines included**: Ecology, forestry, humanities, psychology, social sciences
- **Methodology**: Manual review of data availability statements + author contact
- **Finding**: Data sharing improved over decades but highly variable by discipline

**Cognition Journal Policy Assessment** (Hardwicke et al., 2018, *Royal Society Open Science* 5:180448):
- Pre/post open data policy assessment
- **Study 2**: In-depth analytic reproducibility for subset
- **Assessment criteria**: Accessibility, completeness, understandability

### Archaeology-specific FAIR resources

**"Will It Ever Be FAIR?"** (Nicholson, Kansa & Fernandez, 2023, *Advances in Archaeological Practice* 11(1):67-81, DOI: 10.1017/aap.2022.40):
- Comprehensive review for North American archaeology
- Lists 9+ types of archaeological data needing FAIR treatment
- **Key repositories assessed**: tDAR (CoreTrustSeal certified), Open Context, ADS (UK), ARIADNEplus
- Discusses FAIR+CARE principles for Indigenous data governance

**Archaeology repositories with documented FAIR compliance:**
- **tDAR (Digital Archaeological Record)**: CoreTrustSeal certified, detailed FAIR mapping
- **Open Context**: Publishes FAIR-compliant datasets with structured metadata
- **Archaeology Data Service (ADS)**: Self-declared FAIR-compliant, qualified Dublin Core
- **ARIADNEplus** (https://training.ariadne-infrastructure.eu): 20 guidelines for HASS data FAIR alignment

**Dutch Archaeological e-Depot (DANS)**:
- Legally mandated data deposit within 2 years of fieldwork
- SIKB0102 national metadata standard (XML)
- Model for national-scale FAIR implementation with legal backing

### Critical gap: no comprehensive manually-assessed archaeology corpus exists

Despite extensive guidance, **no published study has manually assessed a corpus of archaeology publications for FAIR compliance**. This represents a significant opportunity for the planned assessment of 50-100 archaeology papers to contribute a valuable benchmark to the field.

### Ecology and biodiversity offer relevant models

**WorldFAIR Agricultural Biodiversity FAIR Assessment Rubrics** (Drucker et al., 2024, DOI: 10.5281/zenodo.10719265):
- Rubric for Plant-Pollinator Interactions Data
- 6 pilot study assessments
- FAIR Implementation Profile + manual rubric methodology
- **Raw data available on Zenodo**

**BEXIS2 FAIR Conformity Assessment** (Over et al., 2021, PMC8589773):
- Self-assessment using RDA FAIR Data Maturity Model
- 1,767+ datasets in iDiv biodiversity repository
- Strong Findability/Accessibility, moderate Interoperability, partial Reusability

---

## Part 6: Adjacent Open Science Frameworks

### TOP Guidelines provide comprehensive transparency assessment

The **Transparency and Openness Promotion (TOP) Guidelines** (Nosek et al., 2015, *Science*, DOI: 10.1126/science.aab2374 | COS: https://www.cos.io/initiatives/top-guidelines) offer a structured framework complementary to FAIR.

**Original TOP 2015: 8 standards with 4 levels (0-3):**

| Standard | Level 1 (Disclosure) | Level 2 (Requirement) | Level 3 (Verification) |
|----------|---------------------|----------------------|------------------------|
| Data Citation | Should cite with DOIs | Must cite with DOIs | Citations verified |
| Data Transparency | State if available | Must post to repository | Independent verification |
| Code Transparency | State if available | Must post to repository | Code verified |
| Materials Transparency | State if available | Must post to repository | Materials verified |
| Design/Analysis Transparency | Encourage guidelines | Require guidelines | Independent verification |
| Study Preregistration | State if registered | Registration certified | Only preregistered published |
| Analysis Plan Preregistration | State if registered | Plan certified | Only certified plans published |
| Replication | Encouraged | Results-blind review | Registered Reports required |

**TOP 2025 revision** (preprint: https://osf.io/preprints/metaarxiv/nmfs6_v2) restructures into:
- **7 Research Practices** (each with Disclosed/Shared/Certified levels)
- **2 Verification Practices** (Results Transparency, Computational Reproducibility)
- **4 Verification Study types** (Replication, Registered Reports, Multiverse, Many Analysts)

**TOP Factor Database** (https://www.topfactor.org): 3,000+ journals scored, data downloadable at https://osf.io/qatkz

**Automation feasibility for TOP assessment:**

| Element | Automation Level | Method |
|---------|-----------------|--------|
| Data availability statements | HIGH | NLP/text mining |
| Repository DOI links | HIGH | DOI resolution + registry checks |
| Preregistration links | HIGH | Link detection + timestamp verification |
| Citation format compliance | MEDIUM | Reference parsing |
| Reporting guideline compliance | MEDIUM | Checklist detection |
| Preregistration completeness | LOW | Semantic analysis required |
| Computational reproducibility | LOW | Actual code execution required |

### TRUST Principles and CoreTrustSeal assess repository trustworthiness

**TRUST Principles** (Lin et al., 2020, *Scientific Data* 7:144, DOI: 10.1038/s41597-020-0486-7):
- **T**ransparency, **R**esponsibility, **U**ser focus, **S**ustainability, **T**echnology
- Complementary to FAIR: FAIR focuses on data characteristics; TRUST on repository trustworthiness
- Repositories demonstrate TRUST through **CoreTrustSeal certification**

**CoreTrustSeal** (https://www.coretrustseal.org) certifies repositories against 16 requirements covering organizational infrastructure, digital object management, and IT security. **160+ certified repositories** including ICPSR, Dryad, Zenodo, Figshare.

**For Stage 2 assessment**: CoreTrustSeal certification status (queryable via https://amt.coretrustseal.org/certificates) provides strong signal that deposited data will remain FAIR over time.

### Open Science Badges signal transparent practices

**COS Open Science Badges** (https://www.cos.io/initiatives/badges):
- **Open Data**: Digitally-shareable data publicly available
- **Open Materials**: Methodology components publicly available
- **Preregistered**: Study design registered prior to research

Badges appear in journal articles (Psychological Science pioneered since 2014) and can be detected during paper assessment.

---

## Part 7: Recommendations for LLM-Assisted Assessment Implementation

### Proposed three-stage assessment architecture

Based on this research, the planned three-stage approach aligns well with available tools and frameworks:

**Stage 1 (Immediate priority): Paper self-presentation assessment**
- Parse data/code availability statements using NLP
- Detect repository links (DOIs to Zenodo, Figshare, Dryad, discipline-specific repositories)
- Identify preregistration links (OSF Registries, ClinicalTrials.gov, AsPredicted)
- Extract license information from text
- Check for Open Science Badges
- Assess against TOP Guidelines Level 1 (disclosure) criteria
- Map claims to RDA FAIR Data Maturity Model indicators

**Stage 2: Verification**
- Verify DOI resolution via DataCite API
- Run F-UJI on deposited datasets (if DOIs available)
- Check CoreTrustSeal certification of deposit repositories
- Verify ORCID, ROR identifiers where claimed
- Test Signposting protocol implementation on landing pages
- Assess metadata completeness against DataCite schema

**Stage 3: Computational reproduction**
- Retrieve deposited data and code
- Attempt execution in documented environment
- Compare outputs to published results

### LLM enhancement opportunities

LLMs can address gaps that automated tools cannot:

**Metadata extraction from unstructured sources:**
- Parse README files, documentation, supplementary materials
- Extract provenance from narrative methodology sections
- Identify domain-specific terminology and map to ontologies

**Semantic understanding:**
- Assess whether metadata is "rich" qualitatively (not just checkbox completeness)
- Evaluate description adequacy for reuse
- Map free-text descriptions to controlled vocabulary terms

**License interpretation:**
- Parse non-standard license text
- Map to SPDX equivalents
- Identify access restrictions buried in prose

**Provenance assessment:**
- Extract workflow descriptions from Methods sections
- Identify data sources and transformations
- Assess reproducibility from narrative descriptions

### Recommended assessment rubric structure

Based on established frameworks, structure assessment output as:

```
FAIR Assessment Report
├── Overall Score (percentage or maturity level)
├── Findable
│   ├── F1: Persistent identifier (binary + identifier type)
│   ├── F2: Metadata richness (maturity level 0-3)
│   ├── F3: Metadata-data linkage (binary)
│   └── F4: Searchable indexing (repository + indexed sources)
├── Accessible
│   ├── A1: Retrieval protocol (protocol type + authentication)
│   └── A2: Metadata persistence (repository policy assessment)
├── Interoperable
│   ├── I1: Knowledge representation (formats detected)
│   ├── I2: FAIR vocabularies (namespaces used)
│   └── I3: Qualified references (linked resources)
├── Reusable
│   ├── R1.1: License (SPDX identifier or assessment)
│   ├── R1.2: Provenance (detail level)
│   └── R1.3: Community standards (standards detected)
├── TOP Guidelines Alignment
│   ├── Data transparency level (0-3)
│   ├── Code transparency level (0-3)
│   └── Preregistration status
└── Verification Results (Stage 2)
    ├── DOI resolution status
    ├── Repository certification status
    └── F-UJI scores (if applicable)
```

### Key URLs for implementation

**Assessment Tools:**
- F-UJI API: https://www.f-uji.net | https://github.com/pangaea-data-publisher/fuji
- FAIR-Checker: https://fair-checker.france-bioinformatique.fr

**Registries and Validation:**
- SPDX Licenses: https://spdx.org/licenses/
- FAIRsharing: https://fairsharing.org
- Linked Open Vocabularies: https://lov.linkeddata.es
- CoreTrustSeal certificates: https://amt.coretrustseal.org/certificates

**PID APIs:**
- DataCite: https://api.datacite.org/dois/{doi}
- ORCID: https://pub.orcid.org/v3.0/{orcid}
- ROR: https://api.ror.org/organizations/{ror_id}

**Frameworks:**
- RDA FAIR Data Maturity Model: https://zenodo.org/records/3909563
- TOP Guidelines: https://osf.io/9f6gx/wiki/Guidelines/
- TOP Factor data: https://osf.io/qatkz

---

## Conclusion: Gaps and Opportunities

This research reveals **five key gaps** relevant to the planned archaeology paper assessment:

1. **No archaeology-specific FAIR assessment corpus exists** — The planned assessment of 50-100 papers could establish a valuable benchmark for the discipline

2. **Machine-actionability implementation substantially lags** — Most FAIR compliance remains human-readable only; automated assessment tools can only capture surface-level machine-actionable elements

3. **Paper-level vs. dataset-level assessment gap** — Existing tools (F-UJI, FAIR-Checker) assess datasets at repository level, not research papers; LLM-assisted extraction can bridge this gap

4. **HASS disciplines remain underserved** — While guidelines exist (ALLEA, ARIADNEplus), operational assessment tools and validation corpora are sparse for humanities and social sciences

5. **Stage 1 assessment is tractable** — Assessing how papers present themselves (availability statements, repository links, claimed practices) is highly automatable and aligns with established frameworks; Stages 2-3 require progressively more verification infrastructure

The **consensus best practice** for FAIR assessment uses **graduated maturity levels** (not binary) based on the RDA FAIR Data Maturity Model, with visualization through radar charts or traffic-light indicators. For an LLM-assisted system, combining F-UJI's automated metrics with LLM-enhanced interpretation of narrative elements offers the most promising approach to comprehensive FAIR assessment of archaeology papers.