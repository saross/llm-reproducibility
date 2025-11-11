# Persistent Identifiers (PIDs) for Infrastructure Assessment

**Purpose**: Reference guide for identifying, extracting, and assessing Persistent Identifiers in research papers

**Context**: PIDs form the foundation of FAIR principle F1 by providing globally unique, resolvable identifiers for diverse research objects

**Audience**: Research assessor skill users performing infrastructure extraction (Pass 6) or validation (Pass 7)

---

## Overview

**Persistent Identifiers (PIDs)** are globally unique, persistent, and resolvable identifiers that prevent link rot and enable machine-actionable research discovery. They form the foundation of FAIR compliance and enable the creation of **PID graphs** — interconnected networks of research objects (papers → authors → data → software → samples → projects).

**Why PIDs matter for reproducibility assessment:**
- Enable reliable citation and retrieval of research outputs
- Support provenance tracking across research lifecycle
- Enable machine-actionable discovery and reuse
- Prevent link rot (URLs change; PIDs persist)
- Form foundation for FAIR Findability (F1 principle)

---

## PID Types for Research Objects

### 1. DOI (Digital Object Identifier)

**Scope**: Papers, datasets, software, preprints, vocabularies, supplementary materials

**Format**: `10.XXXXX/identifier` (always starts with "10.")

**Examples:**
- Paper DOI: `10.1016/j.quaint.2023.01.003`
- Dataset DOI: `10.5281/zenodo.1234567` (Zenodo repository)
- Software DOI: `10.5281/zenodo.7654321` (archived code release)
- Vocabulary DOI: `10.5281/zenodo.periodo` (PeriodO period gazetteer)

**Resolver URL**: `https://doi.org/10.XXXXX/identifier`

**Governance**: International DOI Foundation; registration agencies include DataCite (data), Crossref (publications), mEDRA (multilingual content)

**Adoption**:
- Papers: Universal in major journals
- Datasets: Growing rapidly via Zenodo, Figshare, Dryad, domain repositories (tDAR, Neotoma)
- Software: Emerging (Zenodo+GitHub integration, Software Heritage)
- Vocabularies: Rare but increasing

**Historical context**: 50 million DOI registrations (2011) → 391 million (2025)

**FAIR compliance**: ✅ Satisfies F1 (persistent), A1 (resolvable), I3 (qualified references)

---

### 2. ORCID (Open Researcher and Contributor ID)

**Scope**: Researchers, authors, contributors

**Format**: `0000-0000-0000-000X` (16 digits with hyphens, last digit may be X as checksum)

**Example**: `0000-0002-1694-233X`

**Resolver URL**: `https://orcid.org/0000-0002-1694-233X`

**Governance**: ORCID Inc. (non-profit)

**Purpose**: Disambiguate researchers (solves name ambiguity: J. Smith vs J. Smith vs Jane Smith)

**Adoption rates (2024-2025):**
- **Natural sciences**: 91-93% of authors have ORCIDs
- **Humanities**: 17-24% of authors have ORCIDs (significantly lower)
- **All authors in paper**: Only 14% of papers include ORCIDs for ALL authors
- **Corresponding authors**: ~90% include ORCID (more complete)
- **Profile maintenance**: 73% of ORCID holders maintain employment/publication records

**Policy drivers:**
- **US federal mandate (end 2025)**: All federal grant recipients must obtain and supply ORCID
- Many publishers now require/request ORCIDs (optional vs mandatory varies)
- Emerging funder requirements (NIH, NSF, Wellcome, ERC)

**HASS-specific context:**
- Growing but still low adoption in archaeology/history
- Often only corresponding author has ORCID
- Pre-2015 papers unlikely to have ORCIDs (ORCID launched 2012)
- 2020+ papers increasingly include ORCIDs due to publisher encouragement

**FAIR compliance**: ✅ Satisfies F1 (unique researcher identifier), I3 (links researchers to outputs)

**Assessment note**: ORCID presence indicates FAIR-aware authorship practices but absence does NOT indicate poor practice for older papers or HASS fields with lower adoption baselines

---

### 3. RAiD (Research Activity Identifier)

**Scope**: Research projects, activities, expeditions, field campaigns, grants

**Format**: DOI-based (e.g., `10.RAID/12345678-abcd-1234-abcd-123456789abc`)

**Resolver URL**: `https://raid.org/10.RAID/identifier` or standard DOI resolver

**Governance**: RAiD consortium (Australia, Europe, US, Finland)

**Purpose**: Provide persistent identifier for entire research projects (not just outputs), enabling linkage across datasets, publications, funding, and contributors over time

**Adoption status (2025):**
- ⚠️ **Pilot phase**: Launching 2025-2028
- Currently used in specific projects (e.g., Australian National Data Service pilots)
- **Not yet widespread**: Unlikely to be present in most papers until 2026+

**FAIR compliance**: ✅ Designed for F1, I3 (once widely adopted)

**Assessment note**: Absence of RAiD is expected for papers published before 2025; presence indicates cutting-edge data management practice

---

### 4. IGSN (International Generic Sample Number)

**Scope**: Physical samples including geological, biological, archaeological, and environmental samples

**Format**: Alphanumeric codes (e.g., `IEAU12345`, `IGSN: IEWF0001`)

**Resolver URL**: `http://igsn.org/IEAU12345` or `https://app.geosamples.org/sample/igsn/IEAU12345`

**Governance**: IGSN e.V. (international non-profit); rebranded to "International Generic Sample Number" to broaden beyond geology

**Purpose**: Enable persistent identification, citation, and tracking of physical samples across their lifecycle

**Relevance to HASS:**
- **Archaeology**: Artefacts, ecofacts, sediment samples, faunal/botanical remains
- **Palaeoecology**: Sediment cores, pollen samples, macrofossils
- **Geoarchaeology**: Soil samples, geological specimens
- **Heritage science**: Material samples for analysis

**Adoption status (2024-2025):**
- Well-established in geology and geosciences
- **Emerging in archaeology**: Explicitly included in IGSN scope (2024 rebrand)
- Low current adoption in HASS but increasing awareness
- Repositories exist: SESAR (System for Earth Sample Registration)

**FAIR compliance**: ✅ Satisfies F1 (persistent), A1 (resolvable), supports R1.2 (provenance)

**Assessment note**: Absence of IGSNs is common for archaeology/palaeoecology papers but presence indicates exemplary sample stewardship practice; expect increasing adoption 2025+

---

### 5. Accession Numbers (Repository-Specific PIDs)

**Scope**: Datasets in domain-specific or general repositories

**Format**: Varies by repository (e.g., `PRJEB12345`, `GSE123456`, `tDAR-ID-123456`)

**Examples:**
- **European Nucleotide Archive (ENA)**: `PRJEB12345` (project), `ERR123456` (run)
- **NCBI GenBank**: `GSE123456` (GEO series), `SRA123456` (sequence read archive)
- **tDAR (Digital Archaeological Record)**: `tDAR-ID-123456` (dataset identifier)
- **Neotoma Paleoecology Database**: `Dataset ID: 12345`

**Resolver URLs**: Repository-specific (e.g., `https://www.ebi.ac.uk/ena/browser/view/PRJEB12345`)

**Governance**: Individual repository systems

**Persistence**: ⚠️ Variable — domain repositories generally persistent (ENA, GenBank commit to perpetuity), but not guaranteed like DOIs

**FAIR compliance**: ✅ Satisfies F1 (unique identifier), F4 (indexed), A1 (resolvable), often R1.3 (community standards)

**Assessment note**: Domain-specific accessions often superior to general DOIs for FAIR compliance because they include discipline-specific structured metadata and adhere to community standards (e.g., Darwin Core for biodiversity)

---

### 6. Software PIDs

**Context**: Software differs from data — it is executable, versioned, and evolves. Software PIDs must capture specific versions to enable reproducibility.

#### 6a. Software Heritage Identifiers (SWHID)

**Scope**: Software source code (universal archive)

**Format**: Cryptographic hash (e.g., `swh:1:cnt:94a9ed024d3859793618152ea559a168bbcbb5e2`)

**Example**: `swh:1:dir:d198bc9d7a6bcf6db04f476d29314f157507d505`

**Resolver URL**: `https://archive.softwareheritage.org/swh:1:dir:...`

**Governance**: Software Heritage Foundation (UNESCO-supported)

**Purpose**: Universal software archive capturing all public source code (GitHub, GitLab, Bitbucket, etc.) with cryptographic identifiers

**Adoption status (2025):**
- Software Heritage archives 15+ billion source files
- Integration with GitHub, HAL (French archive), Inria
- **Increasing adoption** as awareness grows
- Recommended by FAIR4RS principles

**FAIR compliance**: ✅ Exemplary F1 (cryptographic persistence), A2 (metadata persistent), R1.2 (provenance)

**Assessment note**: Presence indicates cutting-edge software preservation; absence is common but Zenodo DOI is acceptable alternative

---

#### 6b. Zenodo Software DOIs

**Scope**: Archived snapshots of software releases

**Format**: Standard DOI (e.g., `10.5281/zenodo.7654321`)

**Example**: `10.5281/zenodo.1234567` (specific version), `10.5281/zenodo.1234566` (all versions concept DOI)

**How it works**: GitHub+Zenodo integration archives each release with DOI

**Governance**: Zenodo (CERN-operated, EU-funded)

**Persistence**: ✅ Strong — CERN commits to 20+ year preservation

**FAIR compliance**: ✅ Satisfies F1 (DOI), F4 (indexed), A1 (resolvable), A2 (metadata persistent)

**Assessment preference**: Zenodo DOI > GitHub URL alone (live repos change; archives persist)

---

#### 6c. Software Metadata Standards

**CodeMeta.json**: Software metadata schema (JSON-LD format)
- Describes software: name, version, authors, dependencies, licence
- Machine-readable by repositories and indexers
- Analogous to DataCite XML for data

**CITATION.cff**: Citation File Format
- Plain-text format specifying how to cite software
- Supported by GitHub, Zenodo
- Example: `cff-version: 1.2.0`

**Why these matter**: Enable machine-actionable software citation and dependency tracking

**FAIR compliance**: Support F2 (rich metadata), I1 (structured format), R1 (reusability through documentation)

---

### 7. Vocabulary PIDs

**Scope**: Published controlled vocabularies, ontologies, gazetteers, taxonomies

**Purpose**: Enable semantic interoperability (FAIR I2 principle)

**Examples in HASS:**
- **PeriodO** (chronological periods): `https://perio.do/en/` (DOI-based)
- **Pleiades** (ancient places): `https://pleiades.stoa.org/places/579885` (URI-based)
- **Getty AAT** (Art & Architecture Thesaurus): `http://vocab.getty.edu/aat/300264088`
- **CIDOC-CRM** (cultural heritage ontology): `http://www.cidoc-crm.org/`

**Why they matter**: Papers using standardised vocabularies enable cross-dataset search and semantic reasoning

**FAIR compliance**: ✅ Satisfies I2 (FAIR vocabularies), I3 (qualified references)

**Assessment note**: Rare in HASS papers but presence indicates exemplary interoperability practice

---

## PID Format Specifications and Validation

### Format Validation Rules

**DOI:**
- Must start with `10.`
- Format: `10.XXXXX/identifier` (prefix/suffix)
- Allowed characters: alphanumeric, hyphens, periods, underscores
- Case-insensitive but conventionally lowercase

**ORCID:**
- Format: `0000-0000-0000-000X` (exactly 16 characters with hyphens)
- Last character may be X (checksum digit)
- No spaces, all numeric except possible final X
- Regex: `^\d{4}-\d{4}-\d{4}-\d{3}[\dX]$`

**RAiD:**
- DOI-based format: `10.RAID/...` prefix
- Full format varies (DOI structure)

**IGSN:**
- Alphanumeric codes
- Often prefixed with `IGSN:` or collection code
- Examples: `IEAU12345`, `IEWF0001`

**URLs:**
- Must use `https://` (preferred) or `http://`
- Avoid FTP, proprietary protocols

### Resolver URL Construction

**DOI**: `https://doi.org/` + identifier
- Example: `10.5281/zenodo.1234567` → `https://doi.org/10.5281/zenodo.1234567`

**ORCID**: `https://orcid.org/` + identifier
- Example: `0000-0002-1694-233X` → `https://orcid.org/0000-0002-1694-233X`

**RAiD**: `https://raid.org/` + identifier or standard DOI resolver

**IGSN**: `http://igsn.org/` + identifier or `https://app.geosamples.org/sample/igsn/` + identifier

---

## ORCID Coverage Calculation

**Purpose**: Assess author PID coverage completeness

**Formula:**
```
ORCID Coverage (%) = (Authors with ORCID / Total Authors) × 100
```

**Coverage categories:**
- **none**: 0% (no ORCIDs present)
- **minimal**: 1-25% (e.g., only corresponding author)
- **partial**: 26-75% (some authors)
- **high**: 76-99% (most authors)
- **complete**: 100% (all authors have ORCIDs)

**Assessment context:**
- Pre-2016 papers: ORCID presence rare
- 2016-2020: Corresponding author common, full coverage rare
- 2020+: Increasing full coverage due to publisher requirements
- HASS baseline: 17-24% adoption (lower than natural sciences 91-93%)

---

## PID Graph Connectivity Scoring

**Concept**: The PID graph represents interconnections between research objects. Greater connectivity enables better provenance, discovery, and reuse.

**Connectivity Score**: Count distinct PID types present (0-6 scale)

**Scoring:**
- **Paper DOI present**: +1 point
- **Any author ORCID present**: +1 point (even if not all authors)
- **Dataset PID present**: +1 point (DOI, accession, or repository-specific)
- **Software PID present**: +1 point (DOI, SWHID, or archived repository)
- **Sample PID present**: +1 point (IGSN or DOI for physical samples)
- **Project RAiD OR vocabulary PID present**: +1 point (either counts)

**Maximum score**: 6 points (all PID types present)

**Connectivity ratings:**
- **0-1 points**: Minimal connectivity (paper DOI only, or no PIDs)
- **2-3 points**: Moderate connectivity (paper + authors + one output type)
- **4-5 points**: Strong connectivity (paper + authors + multiple output types)
- **6 points**: Complete connectivity (exemplary PID graph)

**Assessment context:**
- Natural sciences baseline (2024): Often 4-5 points
- HASS baseline (2024): Often 2-3 points
- Pre-2016 papers: Often 1-2 points (paper DOI only)
- Target trajectory: Increasing connectivity over time

**Why it matters**: PID graph completeness directly supports FAIR F1 (findability), I3 (qualified references), R1.2 (provenance)

---

## Field-Specific PID Systems (HASS)

### Archaeology-Specific Repositories

**tDAR (The Digital Archaeological Record)**
- Domain-specific repository for archaeological data
- Issues `tDAR-ID` identifiers
- Community standards compliance (Dublin Core metadata)
- URL: `https://core.tdar.org/dataset/ID`

**Open Context**
- Archaeological data publication platform
- Issues DOIs for datasets
- Semantic web integration (linked open data)
- URL: `https://opencontext.org/`

**ARIADNEplus**
- European archaeological data infrastructure
- Aggregates multiple repositories
- Does not issue PIDs but indexes existing ones

### Palaeoecology-Specific Repositories

**Neotoma Paleoecology Database**
- Issues `Dataset ID` identifiers
- Well-structured metadata (chronological, spatial, taxonomic)
- API access for programmatic retrieval
- URL: `https://www.neotomadb.org/`

**PANGAEA**
- Earth system science data repository
- Issues DOIs for datasets
- Strong in palaeoclimate, palaeoecology
- URL: `https://www.pangaea.de/`

### Heritage Science Repositories

**Heritage Science repository landscape emerging:**
- ARIADNE (archaeology)
- IPERION (heritage science infrastructure)
- CulturalHeritage.science (aggregator)

**Adoption status (2025)**: Growing but not yet universal; presence indicates engagement with domain best practices

---

## Assessment Criteria Summary

### When extracting PIDs (Pass 6):
1. **Extract identifier exactly as stated** in paper
2. **Construct resolver URL** using standard format
3. **Record location** where PID was found (title page, data availability statement, etc.)
4. **Do NOT verify resolution** in Pass 6 (verification is Pass 7 task)
5. **Calculate ORCID coverage** and PID graph connectivity score
6. **Note absence explicitly** (e.g., "No dataset PIDs found" rather than leaving field empty)

### When validating PIDs (Pass 7):
1. **Verify format** matches expected pattern (DOI starts with 10., ORCID has correct structure)
2. **Attempt resolution** (do PIDs resolve to active resources?)
3. **Check metadata presence** (do resolved resources have structured metadata?)
4. **Flag broken PIDs** as critical validation issue
5. **Note link rot** if URLs present instead of PIDs

### When assessing FAIR compliance:
1. **PID presence enables F1** (findable) — core FAIR foundation
2. **PID resolution enables A1** (accessible via standard protocol)
3. **PID metadata richness affects F2, R1** (descriptive quality)
4. **PID relationships enable I3** (qualified references to related objects)
5. **Context matters**: Adjust expectations by publication year, discipline, research type

---

## Marwick's "Built-In vs Bolted-On" Heuristic

**Concept** (Marwick 2017, 2020): FAIR practices can be either:
- **Built-in**: Integrated throughout research process (data management plan, continuous sharing, preregistration)
- **Bolted-on**: Added retroactively at publication (data uploaded to repository only when manuscript accepted)

**Observable indicators in papers:**
- **Built-in signals**: Preregistration present, data management plan mentioned, continuous deposition (multiple DOIs during project), project PID (RAiD)
- **Bolted-on signals**: Single data deposit at publication, no DMP mentioned, data availability statement added in revision

**Assessment challenge**: Papers rarely document temporal process, so distinguishing built-in from bolted-on is difficult without external evidence

**Current approach**: Note presence/absence of PIDs and FAIR infrastructure; temporal integration cannot be reliably assessed from paper text alone

**Future potential**: If project PIDs (RAiD) become common, could enable assessment of when outputs were registered relative to research timeline

---

## References

- Chue Hong et al. (2022). FAIR Principles for Research Software (FAIR4RS). Scientific Data 9:622. https://doi.org/10.1038/s41597-022-01710-x
- Marwick, B. (2017). Computational reproducibility in archaeological research. Journal of Archaeological Method and Theory 24:424-450.
- Wilkinson et al. (2016). The FAIR Guiding Principles. Scientific Data 3:160018. https://doi.org/10.1038/sdata.2016.18
- ORCID adoption statistics: Martín-Martín et al. (2024). Scientific Reports 14:23340.
- Software Heritage: https://www.softwareheritage.org/
- RAiD: https://www.raid.org/
- IGSN: https://www.igsn.org/

---

**Document Version**: 1.0
**Last Updated**: 2025-11-11
**Part of**: research-assessor skill infrastructure assessment capability
