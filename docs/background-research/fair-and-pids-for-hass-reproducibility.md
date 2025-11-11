# FAIR Principles and Persistent Identifiers for HASS Reproducibility Assessment

**Date**: 2025-11-03
**Purpose**: Background research to inform infrastructure extraction schema and assessment rubrics
**Focus**: Machine-actionability, PID graphs, and FAIR compliance evaluation for archaeology, history, and humanities

---

## Executive Summary

**FAIR Principles** (Findable, Accessible, Interoperable, Reusable) emphasise **machine-actionability** — the capacity of computational systems to find, access, interoperate with, and reuse data with minimal human intervention. This is distinct from simply making data "available" in human-readable formats.

**Persistent Identifiers (PIDs)** form the foundation of FAIR by providing globally unique, resolvable identifiers for diverse research objects: papers, datasets, software, physical samples, researchers, and projects. The emerging **"PID graph"** links these objects to create auditable research provenance.

**For HASS reproducibility assessment**, we must evaluate:
1. **Presence of PIDs** across research object types
2. **Machine-actionability** of linked resources (not just human-readable PDFs)
3. **PID graph completeness** (how well research objects are interconnected)
4. **Domain-appropriate standards** (acknowledging HASS lags natural sciences in adoption)

This report synthesises current FAIR frameworks, PID systems (DOI, ORCID, RAiD, IGSN), and assessment approaches to inform Pass 6 infrastructure extraction.

---

## 1. FAIR Principles: The Full Framework

### 1.1 Core Definition

The FAIR Guiding Principles (Wilkinson et al., 2016) establish guidelines for improving:
- **F**indability
- **A**ccessibility
- **I**nteroperability
- **R**eusability

**Critical innovation**: Emphasis on **"machine-actionability (i.e., the capacity of computational systems to find, access, interoperate, and reuse data with none or minimal human intervention)"** due to increasing data volume and complexity.

### 1.2 The 15 FAIR Principles

#### **F: Findable**

**F1. (Meta)data are assigned globally unique and persistent identifiers**
- Requires PIDs (DOIs, handles, IGSNs, etc.)
- Both data AND metadata must have identifiers

**F2. Data are described with rich metadata**
- Metadata richness defined by R1 (below)
- Must enable discovery by both humans and machines

**F3. Metadata clearly and explicitly include the identifier of the data they describe**
- Bi-directional linking: metadata points to data via PID

**F4. (Meta)data are registered or indexed in a searchable resource**
- Requires registration in discoverable repositories
- Machine-readable indexing essential

#### **A: Accessible**

**A1. (Meta)data are retrievable by their identifier using a standardised communication protocol**
- HTTP/HTTPS, FTP, etc.
- Protocol must be documented

**A1.1. The protocol is open, free, and universally implementable**
- Excludes proprietary protocols requiring licences
- HTTP/HTTPS preferred

**A1.2. The protocol allows for an authentication and authorisation procedure, where necessary**
- Restricted access is FAIR-compliant if properly governed
- Critical for Indigenous data (CARE principles)

**A2. Metadata are accessible, even when the data are no longer available**
- Metadata persistence requirements stricter than data
- "Tombstone" pages for removed datasets

#### **I: Interoperable**

**I1. (Meta)data use a formal, accessible, shared, and broadly applicable language for knowledge representation**
- Structured formats: JSON-LD, RDF, XML
- NOT unstructured PDFs or Word documents

**I2. (Meta)data use vocabularies that follow FAIR principles**
- Controlled vocabularies, ontologies, taxonomies
- Vocabularies themselves should be FAIR (have PIDs, be machine-readable)

**I3. (Meta)data include qualified references to other (meta)data**
- Links to related datasets, papers, software
- Relationships should be typed (e.g., "is derived from", "is supplement to")

#### **R: Reusable**

**R1. (Meta)data are richly described with a plurality of accurate and relevant attributes**
- Rich descriptive metadata enabling context understanding
- Domain-specific standards (e.g., Darwin Core for biodiversity)

**R1.1. (Meta)data are released with a clear and accessible data usage licence**
- Machine-readable licences (SPDX identifiers)
- CC-BY, CC0, MIT, Apache-2.0, etc.

**R1.2. (Meta)data are associated with detailed provenance**
- Who created, when, how, from what sources
- Processing pipelines, software versions, parameters

**R1.3. (Meta)data meet domain-relevant community standards**
- TIDieR (intervention reporting), CONSORT (trials), Darwin Core (biodiversity)
- HASS: Increasingly developing standards (e.g., ARIADNEplus for archaeology)

### 1.3 Machine-Actionable vs Human-Readable: The Critical Distinction

**FAIR emphasises machine-actionability**, not just human accessibility.

#### Examples of NON-FAIR "available" data:

❌ **PDF supplementary materials** with tables as images
❌ **Word documents** with data in unstructured text
❌ **URLs without PIDs** (link rot)
❌ **Data repository with HTML-only interface** (no API, no structured export)
❌ **Zenodo upload with no metadata** beyond title

#### Examples of FAIR data:

✅ **Dataset with DOI** resolving to machine-readable metadata (JSON-LD)
✅ **Data in structured formats** (CSV, NetCDF, HDF5) with documented schemas
✅ **API access** for programmatic data retrieval
✅ **Linked via typed relationships** to related objects (papers, software, samples)
✅ **Rich metadata** using community standards (Dublin Core, DataCite Schema)

**Key insight from research**: "Comprehensive and machine-readable metadata descriptions empower both machines and human users to seamlessly discover, access, integrate, and reuse data" (JMIR 2024).

---

## 2. Persistent Identifiers (PIDs): The Foundation of FAIR

PIDs are **globally unique, persistent, and resolvable identifiers** that form the foundation of FAIR principle F1. Different PID systems target different research object types.

### 2.1 DOI (Digital Object Identifier)

**Scope**: Papers, datasets, software, pre-prints, vocabularies, supplementary materials

**Governance**: International DOI Foundation; registration agencies include DataCite, Crossref, mEDRA

**Resolution**: https://doi.org/10.xxxx/yyyyy → redirects to current location

**Growth**: 50 million registrations (2011) → 391 million (2025)

**FAIR compliance**:
- ✅ F1: Globally unique and persistent
- ✅ A1: Resolvable via HTTP
- ✅ I3: Can include qualified references to other DOIs
- ✅ Rich metadata via DataCite Schema (structured, machine-readable)

**Usage in HASS**:
- **Papers**: Universal in major journals
- **Datasets**: Growing adoption via Zenodo, Figshare, Dryad, domain repositories
- **Software**: Emerging (Zenodo+GitHub integration, Software Heritage)
- **Vocabularies/Ontologies**: Rare but increasing (e.g., PeriodO period gazetteer)

**Assessment criteria for infrastructure extraction**:
1. DOI present for paper itself?
2. DOI(s) for associated datasets?
3. DOI(s) for software/code repositories?
4. DOI(s) for vocabularies/gazetteers used?
5. DOIs resolve correctly?
6. DOI metadata includes structured relationships?

### 2.2 ORCID (Open Researcher and Contributor ID)

**Scope**: Researchers, authors, contributors

**Format**: https://orcid.org/0000-0002-1234-5678

**Governance**: ORCID Inc. (non-profit)

**Purpose**: Disambiguate researchers (solve name ambiguity problem)

**Adoption rates (2024-2025 research)**:
- **Natural sciences**: 91-93% uptake
- **Humanities**: 17-24% uptake (significantly lower)
- **All authors**: Only 14% of papers include ORCID for ALL authors (Spain study)
- **Corresponding authors**: ~90% include ORCID

**US Federal requirement (2025)**: All federal grant recipients must obtain and supply ORCID by end of 2025

**FAIR compliance**:
- ✅ F1: Unique, persistent identifier for researchers
- ✅ I3: Links researchers to outputs (papers, datasets, grants)
- ⚠️ Profile completeness varies: 73% maintain employment/publications (Spain study)

**Usage in HASS archaeology**:
- Growing but still low adoption
- Often only corresponding author has ORCID
- Pre-2015 papers unlikely to have ORCIDs

**Assessment criteria**:
1. ORCID present for corresponding author?
2. ORCID for ALL authors?
3. ORCIDs link to active profiles?

### 2.3 RAiD (Research Activity Identifier)

**Scope**: Research projects, activities, expeditions, campaigns

**Format**: DOI-based (minted by DataCite under ISO 23527 standard)

**Governance**: ARDC (Australia); expanding via national implementations

**Purpose**: Identify research activities to link outputs (papers, data), funding, participants, infrastructure

**Status (2024-2025)**:
- **Pilot phase** in multiple jurisdictions
- **Europe**: EOSC RAiD via SURF (launch post-summer 2025); Finland pilot via Research.fi; Germany pilot
- **US**: NSF-funded US RAiD Pilot (SDSC + Lyrasis)
- **Czech Republic**: Recommended by R&D Council for national CRIS
- **Australia**: ARDC providing international leadership; heightened interest from research organisations

**HASS adoption**:
- Not yet widespread
- Research.fi (Finland) includes "research outputs (including in the arts)"
- ARIADNEplus (European archaeology infrastructure) promotes FAIR but RAiD not yet integrated
- Likely to see uptake 2026-2028 as pilots mature

**FAIR compliance**:
- ✅ F1: Unique, persistent identifier for projects
- ✅ I3: Links projects to outputs, funding, researchers
- ✅ Emerging component of "PID graph"

**Assessment criteria**:
1. RAiD present for research project?
2. RAiD links to paper outputs?
3. RAiD links to funding information?

**Infrastructure extraction strategy**:
- **2025-2026**: Rare; note if present
- **2027+**: Expect increasing adoption

### 2.4 IGSN (International Generic Sample Number)

**Scope**: Physical samples (geological, biological, archaeological artefacts, sediment cores, ice cores, museum specimens)

**Format**: Alphanumeric string (traditionally prefix + local ID); transitioning to DOI-based system via DataCite partnership (2021)

**Governance**: IGSN e.V. (registered association); DataCite partnership for registration services

**Original focus**: Geosciences (developed for rock/sediment samples)

**Expanded scope (rebranded from "Geo Sample Number" to "Generic Sample Number")**:
- ✅ Archaeological artefacts
- ✅ Biodiversity samples
- ✅ Ice/sediment cores
- ✅ Human tissue samples
- ✅ Material science specimens

**Recent developments (2024-2025)**:
- **FAIR AIMS project (2025-2027)**: Automated IGSN Management System (Helmholtz Centers)
- **DataCite partnership (2021)**: IGSN registration via DataCite infrastructure
- **Growing archaeology interest**: Explicitly mentioned in IGSN documentation

**FAIR compliance**:
- ✅ F1: Globally unique, persistent identifier for physical samples
- ✅ A1: Web-resolvable (via IGSN resolver or DOI system)
- ✅ I3: Can link samples to datasets, papers, projects
- ✅ Rich metadata schema (sample type, location, collector, collection date, current location)

**Usage in HASS archaeology**:
- **Very low** current adoption
- **Emerging interest** for:
  - Museum collections management
  - Sediment core repositories
  - Archaeological site sample tracking
  - Linking samples to publications

**Alternative**: DOIs for sample collections (less granular but more widely used)

**Assessment criteria**:
1. IGSN(s) for physical samples referenced?
2. DOI(s) for sample collections?
3. Sample identifiers resolvable?
4. Metadata includes current sample location (repository, museum)?

**Infrastructure extraction strategy**:
- **High priority** for palaeoecology, geoarchaeology (sediment cores)
- **Medium priority** for excavation-based archaeology
- **Note if present**; don't penalise absence (still emerging)

---

## 3. The PID Graph: Interconnected Research Objects

### 3.1 Concept

The **PID graph** connects research objects via PIDs and typed relationships:

```
Paper (DOI)
  ├─ cites → Dataset (DOI)
  ├─ describes → Samples (IGSN)
  ├─ uses → Software (DOI)
  ├─ uses → Vocabulary (DOI)
  ├─ authors → Researcher (ORCID)
  ├─ funded by → Project (RAiD)
  └─ related to → Other Papers (DOI)

Dataset (DOI)
  ├─ derived from → Samples (IGSN)
  ├─ generated using → Software (DOI)
  ├─ part of → Project (RAiD)
  └─ authors → Researcher (ORCID)

Project (RAiD)
  ├─ produces → Papers (DOI)
  ├─ produces → Datasets (DOI)
  ├─ uses → Infrastructure
  └─ participants → Researchers (ORCID)
```

### 3.2 FAIR Digital Objects (FDOs)

Recent 2025 research emphasises organising FAIR Digital Objects (FDOs), each identified by a **Globally Unique Persistent and Resolvable Identifier (GUPRI)** such as DOI, Handle, or resolvable IRI.

**FDO requirements**:
- Machine-actionable metadata
- Typed relationships to other FDOs
- Rich provenance
- Conformance to community standards

### 3.3 Assessment Implications

**PID graph completeness** is a key FAIR indicator:

| Completeness Level | Description | FAIR Score |
|-------------------|-------------|------------|
| **Minimal** | Paper DOI only; no linked PIDs | Low |
| **Basic** | Paper DOI + ORCID(s) | Low-Medium |
| **Intermediate** | Paper + ORCIDs + dataset DOI | Medium |
| **Strong** | Paper + ORCIDs + datasets + software + project | Medium-High |
| **Exemplary** | Full graph: paper + ORCIDs + datasets + software + samples + project + vocabularies | High |

**Relationships matter**: Not just presence of PIDs but whether they link together via structured metadata (DataCite relations, Crossref metadata)

---

## 4. FAIR Assessment Framework for Infrastructure Extraction

### 4.1 Evaluation Dimensions

#### **Dimension 1: PID Presence**

Binary checks (present/absent):

```yaml
paper_pid:
  doi: true/false
  doi_value: "10.xxxx/yyyyy"
  resolves: true/false

author_pids:
  corresponding_author_orcid: true/false
  all_authors_orcid: true/false/partial
  orcid_count: N
  total_authors: N
  coverage: N/N

dataset_pids:
  doi_present: true/false
  doi_count: N
  non_doi_identifiers: [accession numbers, URLs]

software_pids:
  doi_present: true/false
  doi_count: N
  non_doi_identifiers: [GitHub URLs, Zenodo links]

sample_pids:
  igsn_present: true/false
  igsn_count: N
  doi_present: true/false (for collections)

project_pid:
  raid_present: true/false
  raid_value: "10.xxxx/yyyyy"
```

#### **Dimension 2: Machine-Actionability**

Qualitative assessment (not just present, but FAIR):

```yaml
data_availability:
  statement_present: true/false
  doi_resolves: true/false
  machine_readable_format: true/false/unknown
    # true: API, structured export (JSON, CSV, NetCDF)
    # false: PDF only, HTML tables, images of data
    # unknown: requires manual checking
  structured_metadata: true/false
    # DataCite metadata, schema documentation
  license_machine_readable: true/false
    # SPDX identifier vs prose description

code_availability:
  statement_present: true/false
  doi_resolves: true/false
  executable: true/false/unknown
    # Dependencies documented, environment specified
  version_control: true/false
    # GitHub, GitLab, Bitbucket
  archived_snapshot: true/false
    # Zenodo/Software Heritage vs live GitHub only
```

#### **Dimension 3: PID Graph Connectivity**

How well are research objects interconnected?

```yaml
pid_graph_completeness:
  paper_has_pid: true/false
  authors_have_pids: none/partial/all
  datasets_have_pids: none/partial/all
  software_has_pids: none/partial/all
  samples_have_pids: none/partial/all
  project_has_pid: true/false

  # Connectivity score (0-6)
  connectivity_score: N
    # +1 for each category with PIDs
    # 0 = no PIDs beyond paper
    # 6 = full PID graph
```

#### **Dimension 4: FAIR Principle Coverage**

Map infrastructure to specific FAIR principles:

| Infrastructure Element | FAIR Principles Satisfied |
|------------------------|--------------------------|
| Paper DOI | F1, A1 |
| Dataset DOI with rich metadata | F1, F2, A1, R1 |
| Machine-readable data format | I1, R1 |
| API access | A1.1, I1 |
| Clear data licence | R1.1 |
| Provenance documentation | R1.2 |
| Community standard compliance | R1.3 |
| Vocabulary DOIs | F1, I2 |
| Typed relationships (DataCite) | I3 |
| ORCID for all authors | F1 (for researchers) |

### 4.2 Assessment Rubric

**Findable Score (0-4)**

- **0**: No PIDs beyond paper DOI
- **1**: Paper DOI + partial author ORCIDs
- **2**: Paper DOI + all author ORCIDs + dataset URL (not PID)
- **3**: Paper DOI + ORCIDs + dataset DOI(s)
- **4**: Full PID coverage (paper + ORCIDs + datasets + software + samples/project)

**Accessible Score (0-4)**

- **0**: Data not available
- **1**: Data "available upon request" (not FAIR)
- **2**: Data in repository but no PID / broken links
- **3**: Data with resolving PID, restricted access with justification
- **4**: Data with resolving PID, open access, clear licence

**Interoperable Score (0-4)**

- **0**: No structured data; PDF/Word only
- **1**: Data in repository but unstructured format (HTML tables)
- **2**: Structured format (CSV, JSON) but no schema documentation
- **3**: Structured format + schema + API or programmatic access
- **4**: Full interoperability (structured, typed relationships, FAIR vocabularies)

**Reusable Score (0-4)**

- **0**: No licence, no provenance
- **1**: Licence present but ambiguous (e.g., "for research purposes")
- **2**: Clear licence + minimal metadata
- **3**: Machine-readable licence (SPDX) + rich metadata + provenance
- **4**: Exemplary reusability (licence + provenance + community standards + complete documentation)

**Overall FAIR Score: Sum / 16** (max 16 points)

- **0-4**: Not FAIR
- **5-8**: Minimally FAIR
- **9-12**: Moderately FAIR
- **13-16**: Highly FAIR

---

## 5. HASS-Specific Considerations

### 5.1 Discipline Gaps

**Evidence from research**:
- ORCID uptake: 91-93% (natural sciences) vs 17-24% (humanities)
- RAiD: Pilots mention "arts" but archaeology-specific adoption unclear
- IGSN: Emerging interest in archaeology but very low actual use
- Software DOIs: Higher in computational fields; rare in traditional HASS

**Implication**: Must assess **relative to discipline baseline**, not penalise HASS for broader systemic gaps

### 5.2 Pre-2015 Papers

**Timeline**:
- FAIR Principles published: 2016
- ORCID launched: 2012 (widespread adoption post-2015)
- DataCite growth: Exponential post-2015
- RAiD: Pilots starting 2023-2025

**Assessment philosophy**:
- Papers pre-2016: FAIR not yet a standard → descriptive assessment, not normative
- Papers 2016-2020: FAIR emerging → moderate expectations
- Papers 2020+: FAIR mainstream → full assessment appropriate

### 5.3 Ethical Access Restrictions (CARE Principles)

**Critical**: FAIR A1.2 explicitly allows authentication/authorisation where necessary

**CARE Principles for Indigenous Data Governance**:
- **C**ollective Benefit
- **A**uthority to Control
- **R**esponsibility
- **E**thics

**Assessment approach**:
- Restricted access **with ethical justification** = **POSITIVE** FAIR signal (A1.2 compliance)
- Restricted access **without justification** = **NEGATIVE** signal
- Indigenous data protocols (CARE) = **EXEMPLARY** practice

**Examples**:
- ✅ "Site coordinates restricted; available with permission from Traditional Owners"
- ✅ "Human remains data embargoed per community agreement"
- ❌ "Data available upon request" (no justification, often link rot)

### 5.4 Domain Repositories

**HASS-specific repositories** (assess for PID support):

| Repository | PIDs Supported | FAIR Quality | Domain |
|-----------|----------------|--------------|--------|
| **Open Context** | DOIs for projects/datasets | High | Archaeology |
| **tDAR** | DOIs for datasets | High | Archaeology (North America) |
| **ADS** (Archaeology Data Service) | DOIs for archives | High | UK archaeology |
| **ARIADNEplus** | Aggregator; links to DOI repositories | High | European archaeology |
| **Zenodo** | DOIs for all deposits | High | General |
| **Figshare** | DOIs for all deposits | Medium-High | General |
| **Dryad** | DOIs for datasets | High | General (biology focus) |
| **OSF** | DOIs for projects/components | Medium-High | General |
| **Academia.edu / ResearchGate** | No PIDs; not FAIR-compliant | Low | General (social) |
| **Personal/Institutional websites** | No PIDs; link rot risk | Low | N/A |

**Assessment priority**:
1. Deposits in recognised repositories with DOIs = **HIGH** FAIR score
2. Domain repositories (Open Context, tDAR, ADS) = **EXEMPLARY** (field-specific standards)
3. General repositories (Zenodo, Figshare) = **GOOD** (PIDs but less domain-specific)
4. Institutional repositories with DOIs = **MODERATE**
5. URLs without PIDs = **LOW**
6. "Available upon request" = **VERY LOW**

---

## 6. Connection to repliCATS Seven Signals

### 6.1 Direct Mapping

| repliCATS Signal | PID/FAIR Infrastructure Support |
|------------------|-------------------------------|
| **Transparency** | **PRIMARY**: Data/code availability with PIDs; ORCID transparency; funding disclosure; permits documented |
| **Replicability (Analytic)** | **PRIMARY**: Code availability (DOI); executable environment; data with PID; software version PIDs |
| **Validity** | **MODERATE**: Sample PIDs (traceability); vocabulary PIDs (construct validity); ethics/permits (procedural validity) |
| **Robustness** | **MODERATE**: Supplementary materials DOIs; sensitivity analyses archived; multi-method triangulation documented |
| **Generalisability** | **MINIMAL**: Infrastructure doesn't directly assess generalisability, but data availability enables reanalysis in new contexts |
| **Comprehensibility** | **MINIMAL**: Metadata richness (R1) supports comprehensibility |
| **Plausibility** | **MINIMAL**: Vocabulary DOIs aid plausibility checks (standardised terminology) |

### 6.2 Transparency Signal Enhancement

**Current extraction** (Passes 0-6): Intrinsic transparency (methods documented, rationales explicit)

**Infrastructure extraction** (Pass 6): Extrinsic transparency (PIDs, repositories, FAIR compliance)

**Combined assessment**:
- High intrinsic + high FAIR infrastructure = **EXEMPLARY** transparency
- High intrinsic + low FAIR infrastructure = **GOOD** transparency (well-documented but not FAIR)
- Low intrinsic + high FAIR infrastructure = **FAIR-compliant but opaque** (data available but poorly explained)
- Low intrinsic + low FAIR infrastructure = **POOR** transparency

---

## 7. Practical Extraction and Assessment Workflow

### 7.1 Pass 6 Infrastructure Extraction

**Target sections**:
1. Paper metadata (DOI, authors, ORCIDs)
2. Data Availability Statement
3. Code Availability Statement
4. Acknowledgements (funding, project PIDs, permits)
5. Author Contributions (CReDIT)
6. Supplementary Information

**PID extraction checklist**:
```markdown
## PID Extraction

**Paper**:
- [ ] Extract DOI from header/metadata
- [ ] Verify DOI resolves

**Authors**:
- [ ] Extract ORCIDs for all listed authors
- [ ] Note coverage (N/M authors have ORCID)

**Datasets**:
- [ ] Extract DOIs from Data Availability Statement
- [ ] Extract non-DOI identifiers (GenBank accessions, repository URLs)
- [ ] Note access conditions (open/restricted/embargoed)

**Software/Code**:
- [ ] Extract DOIs (Zenodo, Software Heritage)
- [ ] Extract version control URLs (GitHub, GitLab)
- [ ] Note if archived snapshot vs live repository only

**Physical Samples**:
- [ ] Extract IGSNs if present
- [ ] Extract collection DOIs
- [ ] Note current repository/museum location

**Project**:
- [ ] Extract RAiD if present
- [ ] Extract funding grant numbers
- [ ] Extract project website/infrastructure links

**Vocabularies/Ontologies**:
- [ ] Extract DOIs for controlled vocabularies
- [ ] Extract PeriodO/Pleiades identifiers
- [ ] Note community standards used
```

### 7.2 FAIR Assessment (Integrated into Pass 6 or Separate)

For each identified PID:

```markdown
## FAIR Compliance Assessment

**Data Availability**:
- PID resolves: Yes/No
- Metadata structured: Yes/No/Unknown
- Format machine-readable: Yes/No/Unknown
- Licence present: Yes/No
- Licence machine-readable (SPDX): Yes/No

**Code Availability**:
- PID resolves: Yes/No
- Executable: Yes/No/Unknown (dependencies documented)
- Version control: Yes/No
- Archived snapshot: Yes/No

**Overall FAIR Score**:
- Findable: 0-4
- Accessible: 0-4
- Interoperable: 0-4
- Reusable: 0-4
- **Total: X/16**
```

### 7.3 Lightweight Self-Validation

Built into Pass 6 prompt:

```markdown
## Self-Validation Checklist

After extraction, verify:

**Format validity**:
- [ ] DOIs start with "10." (if present)
- [ ] ORCIDs follow format "0000-0000-0000-000X" (if present)
- [ ] URLs use https:// (if present)
- [ ] IGSNs follow expected format (if present)

**Completeness**:
- [ ] All infrastructure sections examined (even if "not present")
- [ ] extraction_metadata.sections_examined lists all checked sections
- [ ] All identified PIDs have resolver URLs recorded

**Cross-checks**:
- [ ] Author count matches between paper metadata and author_contributions
- [ ] Funding acknowledgements consistent with funding array
- [ ] Data Availability Statement matches repositories array

Report any issues in extraction_metadata.notes.
```

---

## 8. Schema Implications

### 8.1 New Top-Level Fields

Add to infrastructure schema (from `REPRODUCIBILITY_INFRASTRUCTURE_SCHEMA.md`):

```json
"persistent_identifiers": {
  "paper_doi": "10.1234/example",
  "paper_doi_resolves": true,

  "author_orcids": [
    {
      "author_name": "Smith, J.",
      "orcid": "0000-0002-1234-5678",
      "profile_active": true
    }
  ],
  "orcid_coverage": "3/5 authors",

  "dataset_pids": [
    {
      "pid_type": "doi",
      "pid_value": "10.5281/zenodo.1234567",
      "resolves": true,
      "repository": "Zenodo",
      "description": "Raw survey data"
    }
  ],

  "software_pids": [
    {
      "pid_type": "doi",
      "pid_value": "10.5281/zenodo.7654321",
      "resolves": true,
      "repository": "Zenodo",
      "github_url": "https://github.com/lab/project",
      "archived_snapshot": true
    }
  ],

  "sample_pids": [
    {
      "pid_type": "igsn",
      "pid_value": "IGSN12345",
      "resolves": true,
      "sample_type": "sediment_core",
      "repository": "National Lacustrine Core Facility"
    }
  ],

  "project_pid": {
    "pid_type": "raid",
    "pid_value": "10.1234/raid.5678",
    "resolves": true
  },

  "vocabulary_pids": [
    {
      "pid_type": "doi",
      "pid_value": "10.1234/periodo.abc",
      "vocabulary_name": "PeriodO period definitions",
      "purpose": "chronological_framework"
    }
  ]
}
```

### 8.2 FAIR Assessment Object

Add to infrastructure schema:

```json
"fair_assessment": {
  "assessed": true,
  "assessment_date": "2025-11-03",
  "assessor": "claude-sonnet-4-5",

  "findable_score": 3,
  "findable_notes": "Paper DOI + all author ORCIDs + dataset DOIs present. No sample or project PIDs.",

  "accessible_score": 4,
  "accessible_notes": "All PIDs resolve. Data in Zenodo with open CC-BY licence. Code in GitHub + archived snapshot.",

  "interoperable_score": 3,
  "interoperable_notes": "Data in CSV format with schema documentation. No API access. Vocabulary used (PeriodO) has DOI.",

  "reusable_score": 4,
  "reusable_notes": "Machine-readable licence (CC-BY-4.0). Rich metadata in DataCite schema. Provenance documented. Follows ARIADNEplus standards.",

  "total_fair_score": 14,
  "fair_rating": "highly_fair",

  "pid_graph_completeness": 4,
  "pid_graph_notes": "Paper + authors + datasets + software have PIDs. Missing: sample PIDs, project RAiD.",

  "machine_actionability": "high",
  "machine_actionability_notes": "Data downloadable via API, metadata structured (JSON-LD), licence SPDX-compliant."
}
```

---

## 9. Implementation Priorities

### 9.1 Phase 1: Core PID Extraction (Immediate)

**Must-have** for all papers:
1. Paper DOI
2. Author ORCIDs (all authors)
3. Dataset DOIs/URLs
4. Code repository DOIs/URLs
5. Funding information (for Transparency signal)

**Estimated time**: 5-10 minutes per paper

### 9.2 Phase 2: FAIR Assessment (Near-term)

**After PID extraction**:
1. Check DOI resolution (automated)
2. Basic machine-actionability assessment (requires manual checking or heuristics)
3. FAIR score calculation
4. PID graph completeness

**Estimated time**: Additional 5 minutes per paper (if manual); <1 minute (if automated checks)

### 9.3 Phase 3: Emerging PIDs (Future)

**Monitor for adoption**:
1. RAiD (research projects) — expect uptake 2026-2028
2. IGSN (physical samples) — relevant for palaeoecology/geoarchaeology
3. Vocabulary DOIs (PeriodO, AAT, Pleiades) — increasingly common
4. Software PIDs (Software Heritage, Zenodo-GitHub) — growing adoption

**Strategy**: Note if present; don't penalise absence until critical mass adoption

---

## 10. Key Takeaways for Prompt Development

### 10.1 Extraction Focus

**Pass 6 prompt must target**:
1. **PIDs first**: Structured extraction of DOIs, ORCIDs, RAiD, IGSN
2. **Resolver check**: Note if PIDs resolve (can be automated post-extraction)
3. **Machine-actionability**: Assess whether linked resources are machine-readable (high value)
4. **Context**: Note access conditions (open/restricted/embargoed + justification)
5. **FAIR scoring**: Integrated lightweight assessment or deferred to Pass 7

### 10.2 Assessment Philosophy

**Descriptive + context-dependent normative**:
- **Describe** PID/FAIR infrastructure present
- **Context**: Adjust expectations by publication date, discipline, research type
- **CARE-aware**: Restricted access with ethical justification = POSITIVE
- **Graph completeness**: Assess how well research objects interconnect
- **Machine-actionability over human-readability**: PDFs ≠ FAIR

### 10.3 Alignment with repliCATS

**Transparency signal** is primary beneficiary:
- Transparency = Intrinsic (method documentation) + Extrinsic (PID/FAIR infrastructure)
- High FAIR score → High Transparency score contribution
- PID graph completeness → Enhanced trust and traceability

**Replicability (Analytic)** secondary beneficiary:
- Code availability + PID + executable = Strong Replicability signal
- Data availability + PID + machine-readable = Enables reanalysis

---

## 11. References and Further Reading

### Core FAIR Documents

- Wilkinson, M. D., et al. (2016). The FAIR Guiding Principles for scientific data management and stewardship. *Scientific Data*, 3, 160018. https://doi.org/10.1038/sdata.2016.18

- GO FAIR Initiative: https://www.go-fair.org/fair-principles/

### Recent FAIR Research (2024-2025)

- Harmonizing quality measures of FAIRness assessment towards machine-actionable quality information. *International Journal of Digital Earth*, 2024. https://doi.org/10.1080/17538947.2024.2390431

- Suggestions for extending the FAIR Principles based on a linguistic perspective on semantic interoperability. *Scientific Data*, 2025. https://doi.org/10.1038/s41597-025-05011-x

- Making Metadata Machine-Readable as the First Step to Providing Findable, Accessible, Interoperable, and Reusable Population Health Data. *Online Journal of Public Health Informatics*, 2024. https://doi.org/10.5210/ojphi.v16i1.13766

### PID Systems

- **DOI**: International DOI Foundation: https://www.doi.org/
  DataCite: https://datacite.org/

- **ORCID**: ORCID Inc.: https://orcid.org/
  - Bordons, M., et al. (2024). ORCID identifier adoption in Spanish scholarly communication. *Learned Publishing*. https://doi.org/10.1002/leap.1606

- **RAiD**: RAiD website: https://www.raid.org/
  ARDC RAiD Service: https://ardc.edu.au/services/ardc-identifier-services/raid-research-activity-identifier-service/

- **IGSN**: IGSN e.V.: https://ev.igsn.org/
  - Lehnert, K., et al. (2021). Towards Globally Unique Identification of Physical Samples. *Data Science Journal*. https://doi.org/10.5334/dsj-2021-033

### HASS Domain Infrastructure

- **ARIADNEplus** (European archaeology infrastructure): https://ariadne-infrastructure.eu/

- **Open Context**: https://opencontext.org/

- **tDAR** (The Digital Archaeological Record): https://www.tdar.org/

- **ADS** (Archaeology Data Service): https://archaeologydataservice.ac.uk/

### CARE Principles

- CARE Principles for Indigenous Data Governance: https://www.gida-global.org/care

- Carroll, S. R., et al. (2020). The CARE Principles for Indigenous Data Governance. *Data Science Journal*. https://doi.org/10.5334/dsj-2020-043

---

## 12. Conclusion

**FAIR is not binary** — it exists on a continuum. For HASS reproducibility assessment:

1. **PID extraction** forms the foundation — capture DOIs, ORCIDs, RAiD, IGSN systematically
2. **Machine-actionability** is the critical distinction — assess whether resources are truly FAIR vs merely "available"
3. **PID graph completeness** indicates research provenance quality
4. **Context matters** — adjust expectations by discipline, publication date, research type
5. **CARE principles** — restricted access with ethical justification is FAIR-compliant

**Next step**: Integrate these principles into Pass 6 infrastructure extraction prompt, with lightweight FAIR assessment built in or deferred to Pass 7 comprehensive validation.

The **PID graph vision** is emerging now (2024-2025) — our extraction should position papers along this continuum, recognising that most HASS papers will be partially compliant, with exemplary cases providing benchmarks for the field.

---

**Document Status**: Background research complete; ready for schema integration and prompt development.
