# FAIR Principles Assessment Guide

**Purpose**: Reference guide for assessing FAIR compliance in research infrastructure

**Context**: FAIR emphasises machine-actionability — the capacity of computational systems to find, access, interoperate with, and reuse data **with minimal human intervention**

**Audience**: Research assessor skill users performing infrastructure extraction (Pass 6) or validation (Pass 7)

---

## Overview

The **FAIR Guiding Principles** (Wilkinson et al., 2016, *Scientific Data*) establish guidelines for improving research data:
- **F**indability
- **A**ccessibility
- **I**nteroperability
- **R**eusability

**Critical innovation**: Emphasis on **machine-actionability**, not just human readability, due to increasing data volume and complexity.

**Key distinction**: "Available" ≠ FAIR. Data in PDF supplementary materials is *available* but not *machine-actionable*.

---

## The 15 FAIR Principles

### F: Findable

**F1. (Meta)data are assigned globally unique and persistent identifiers**
- Requires PIDs (DOIs, ORCIDs, IGSNs, etc.)
- Both data AND metadata must have identifiers
- Foundation for all other FAIR principles

**F2. Data are described with rich metadata**
- See "Metadata Richness" section below
- Must enable discovery by both humans and machines
- Structured metadata formats preferred (JSON-LD, DataCite XML)

**F3. Metadata clearly and explicitly include the identifier of the data they describe**
- Bidirectional linking: metadata points to data via PID
- Enables automated relationship tracking

**F4. (Meta)data are registered or indexed in a searchable resource**
- Requires registration in discoverable repositories
- Machine-readable indexing essential (not just Google-findable)
- Examples: DataCite index, OpenAIRE, repository catalogues

---

### A: Accessible

**A1. (Meta)data are retrievable by their identifier using a standardised communication protocol**
- HTTP/HTTPS, FTP, or domain-specific protocols
- Protocol must be open, documented, and widely implemented
- DOI resolution via HTTPS is exemplary

**A1.1. The protocol is open, free, and universally implementable**
- Excludes proprietary protocols requiring licences
- HTTP/HTTPS strongly preferred
- No vendor lock-in

**A1.2. The protocol allows for an authentication and authorisation procedure, where necessary**
- ✅ **Restricted access is FAIR-compliant** if properly governed
- Critical for human subjects data, Indigenous data (CARE principles), endangered species locations
- **Ethical restrictions = POSITIVE FAIR signal** when justified
- "Open by default, restricted when necessary"

**A2. Metadata are accessible, even when the data are no longer available**
- Metadata persistence requirements stricter than data
- "Tombstone" pages for removed datasets
- Ensures discoverability even if data embargoed or withdrawn

---

### I: Interoperable

**I1. (Meta)data use a formal, accessible, shared, and broadly applicable language for knowledge representation**
- Structured formats: JSON-LD, RDF, XML, CSV with schema
- NOT unstructured PDFs, Word documents, or proprietary formats
- Machine-parseable structure

**I2. (Meta)data use vocabularies that follow FAIR principles**
- See "Controlled Vocabularies" section below
- Controlled vocabularies, ontologies, taxonomies
- Vocabularies themselves should be FAIR (have PIDs, be machine-readable)

**I3. (Meta)data include qualified references to other (meta)data**
- Links to related datasets, papers, software, samples
- Relationships should be typed (e.g., "is derived from", "is supplement to", "is cited by")
- Enables PID graph construction

---

### R: Reusable

**R1. (Meta)data are richly described with a plurality of accurate and relevant attributes**
- Rich descriptive metadata enabling context understanding
- See "Metadata Richness" section below
- Sufficient detail for independent reuse

**R1.1. (Meta)data are released with a clear and accessible data usage licence**
- Machine-readable licences preferred (SPDX identifiers)
- Examples: CC-BY, CC0, MIT, Apache-2.0, ODbL
- Ambiguous licences ("available on request") NOT FAIR-compliant

**R1.2. (Meta)data are associated with detailed provenance**
- Who created, when, how, from what sources
- Processing pipelines, software versions, parameters
- Enables reproducibility and quality assessment

**R1.3. (Meta)data meet domain-relevant community standards**
- TIDieR (intervention reporting), CONSORT (trials), Darwin Core (biodiversity)
- HASS: ARIADNEplus (archaeology), Dublin Core (general), EML (ecology)
- Domain standards ensure semantic consistency

---

## FAIR Scoring Framework

### Scoring Approach

Each FAIR principle is assessed as **present (1 point)** or **absent (0 points)**.

**Total FAIR score**: Sum across all 15 principles (max 16 points, simplified here to 16 across four dimensions)

**Simplified scoring for infrastructure extraction:**
- **Findable (F1-F4)**: max 4 points
- **Accessible (A1-A2)**: max 4 points
- **Interoperable (I1-I3)**: max 4 points (simplified from 3)
- **Reusable (R1-R1.3)**: max 4 points

**Total**: 16 points maximum

### Findable Dimension Scoring

**F1: Persistent identifiers** (0 or 1 point)
- Data/code has DOI, IGSN, SWHID, or accession number? → 1 point
- Only URLs or "available on request"? → 0 points

**F2: Rich metadata** (0 or 1 point)
- Repository provides structured metadata (authors, title, keywords, abstract, methods)? → 1 point
- Just a file with filename only? → 0 points

**F3: Metadata includes identifier** (0 or 1 point)
- Repository metadata explicitly includes the DOI/PID? → 1 point
- Metadata missing identifier reference? → 0 points

**F4: Indexed in searchable resource** (0 or 1 point)
- Repository indexed (Zenodo, Figshare, DataCite, institutional repo with search)? → 1 point
- Personal website, unindexed server, GitHub without Zenodo? → 0 points

**Findable total**: 0-4 points

---

### Accessible Dimension Scoring

**A1: Standard retrieval protocol** (0 or 1 point)
- HTTPS URL, DOI resolver, FTP, API? → 1 point
- Email request, postal mail, proprietary system? → 0 points

**A1.1: Open/free protocol** (0 or 1 point)
- Public HTTP/HTTPS, no login required for access? → 1 point
- Requires paid subscription or proprietary software? → 0 points

**A1.2: Authentication/authorisation where needed** (0 or 1 point)
- Restricted access with **ethical justification** (human subjects, Indigenous data, endangered species, cultural heritage protection)? → 1 point
- **CARE-compliant restrictions = POSITIVE signal**
- Completely closed with no justification? → 0 points

**A2: Metadata persistent even if data unavailable** (0 or 1 point)
- Repository committed to metadata persistence (Zenodo, DANS, institutional commitment)? → 1 point
- Metadata disappears if data removed (personal website, GitHub without archive)? → 0 points

**Accessible total**: 0-4 points

---

### Interoperable Dimension Scoring

**I1: Formal, shared language** (0 or 1 point)
- Structured format (CSV with schema, JSON, XML, netCDF, GeoPackage, shapefile)? → 1 point
- Unstructured format (PDF tables, Word doc, scanned images, plain text)? → 0 points

**I2: FAIR vocabularies** (0 or 1 point)
- Uses published ontologies, controlled vocabularies with PIDs? → 1 point
- See "Controlled Vocabularies" section below
- Ad hoc field names with no vocabulary standard? → 0 points

**I3: Qualified references** (0 or 1 point)
- Links to other datasets/samples/software use PIDs with relationship types? → 1 point
- Examples: "is derived from [DOI]", "uses software [DOI]"
- No linked resources or untyped links? → 0 points

**Interoperable total**: 0-3 points (but scored proportionally to align with 4-point scale)

---

### Reusable Dimension Scoring

**R1: Rich metadata** (0 or 1 point)
- Detailed documentation, README, data dictionary, methods description? → 1 point
- See "Metadata Richness" section below
- Minimal or no documentation beyond title? → 0 points

**R1.1: Clear licence** (0 or 1 point)
- Explicit machine-readable licence (CC-BY, CC0, MIT, GPL, ODbL, custom with terms)? → 1 point
- No licence, "all rights reserved", or "ask permission"? → 0 points

**R1.2: Provenance** (0 or 1 point)
- Creation process, data sources, transformations, software versions documented? → 1 point
- No provenance information? → 0 points

**R1.3: Community standards** (0 or 1 point)
- Follows discipline-specific format (Darwin Core, EML, CIDOC-CRM, Dublin Core, ARIADNEplus, DataCite)? → 1 point
- No community standard applied? → 0 points

**Reusable total**: 0-4 points

---

### Overall FAIR Rating

**Total FAIR score**: Sum of four dimension scores (max 16 points)

**Rating categories:**
- **0-4**: Not FAIR
- **5-8**: Minimally FAIR
- **9-12**: Moderately FAIR
- **13-16**: Highly FAIR

**Context matters**: See "Context-Dependent Assessment" section below

---

## Metadata Richness

**What is "rich metadata"?**

Metadata is "rich" when it provides sufficient structured information to enable discovery, assessment, and reuse without accessing the data itself.

### DataCite Metadata Schema

**DataCite** is the leading standard for research data metadata.

**Mandatory fields (minimal):**
- Creator (author names, affiliations, ORCIDs)
- Title (dataset name)
- Publisher (repository name)
- Publication Year
- Resource Type (dataset, software, collection, etc.)
- Identifier (DOI)

**Recommended fields (for richness):**
- Subject (keywords, discipline codes)
- Contributor (additional researchers, roles)
- Date (collection dates, embargo dates)
- Language
- AlternateIdentifier (accession numbers, local IDs)
- RelatedIdentifier (links to papers, related datasets)
- Size (file size, record count)
- Format (file formats: CSV, NetCDF, GeoTIFF)
- Version (v1.0, v2.1, etc.)
- Rights (licence information)
- Description (abstract, methods summary)
- GeoLocation (spatial coverage)
- FundingReference (grant numbers, funders)

**What makes metadata "rich"?**
- All mandatory + most recommended fields populated
- Structured format (JSON-LD, XML) not free text
- Includes methods summary and provenance
- Links to related objects via PIDs
- Uses controlled vocabularies for subjects/keywords

### Examples: Rich vs Poor Metadata

**❌ Poor metadata example (not FAIR):**
```
Title: Data
Creator: J Smith
Year: 2023
Format: ZIP file
```

**✅ Rich metadata example (FAIR-compliant):**
```json
{
  "identifier": {"identifierType": "DOI", "identifier": "10.5281/zenodo.1234567"},
  "creators": [
    {"name": "Smith, Jane", "orcid": "0000-0002-1234-5678", "affiliation": "University of X"}
  ],
  "titles": [{"title": "Pollen counts from Lake Keilambete sediment core, 2019-2020"}],
  "publisher": "Zenodo",
  "publicationYear": 2023,
  "resourceType": {"resourceTypeGeneral": "Dataset", "resourceType": "Palynological data"},
  "subjects": [
    {"subject": "Palaeoecology"},
    {"subject": "Quaternary", "subjectScheme": "LCSH"}
  ],
  "dates": [
    {"date": "2019-06/2020-03", "dateType": "Collected"}
  ],
  "geoLocations": [
    {"geoLocationPlace": "Lake Keilambete, Victoria, Australia",
     "geoLocationPoint": {"pointLatitude": -38.0833, "pointLongitude": 142.9167}}
  ],
  "relatedIdentifiers": [
    {"relationType": "IsReferencedBy", "relatedIdentifier": "10.1016/j.quaint.2023.01.003", "relatedIdentifierType": "DOI"}
  ],
  "descriptions": [
    {"description": "Pollen counts from 50 depth intervals across 5m sediment core. Methods: standard acetolysis preparation, count 300+ grains per sample. Taxonomy follows...", "descriptionType": "Abstract"}
  ],
  "fundingReferences": [
    {"funderName": "Australian Research Council", "funderIdentifier": "https://ror.org/05mmh0f86", "awardNumber": "DP190101234"}
  ],
  "rights": [
    {"rights": "Creative Commons Attribution 4.0 International", "rightsURI": "https://creativecommons.org/licenses/by/4.0/", "rightsIdentifier": "CC-BY-4.0", "rightsIdentifierScheme": "SPDX"}
  ],
  "formats": ["CSV", "PDF"],
  "sizes": ["150 KB", "2500 records"],
  "version": "1.0"
}
```

**Why the second example is FAIR:**
- F1: Has DOI
- F2: Rich metadata (subjects, methods, spatial/temporal coverage)
- F3: Metadata includes DOI
- F4: Indexed in DataCite (searchable)
- A1: Retrievable via DOI resolution (HTTPS)
- I1: Structured JSON-LD format
- I2: Uses controlled vocabulary (LCSH)
- I3: Qualified reference to related paper
- R1: Rich description including methods
- R1.1: Machine-readable licence (SPDX identifier)
- R1.2: Provenance (methods, temporal, spatial context)
- R1.3: Follows DataCite community standard

---

## Controlled Vocabularies

**What are controlled vocabularies?**

Published ontologies, gazetteers, taxonomies, or thesauri that provide standardised terms with persistent identifiers, enabling semantic interoperability (FAIR I2 principle).

### Why They Matter

**Problem**: Researchers use inconsistent terminology
- "Holocene" vs "Postglacial" vs "Recent" (same period)
- "Excavation" vs "Dig" vs "Archaeological investigation" (same method)
- Place names change over time ("Constantinople" → "Istanbul")

**Solution**: Controlled vocabularies provide:
- Standard terms with definitions
- Hierarchical relationships (Bronze Age ⊂ Prehistory)
- Multilingual equivalents
- Persistent identifiers (URIs/DOIs)
- Machine-readable structure (RDF, SKOS, OWL)

**Result**: Cross-dataset search, semantic reasoning, automated aggregation

### HASS-Specific Controlled Vocabularies

#### PeriodO (Chronological Periods)

**URL**: https://perio.do/
**PID**: DOI-based URIs
**Scope**: Global gazetteer of historical, archaeological, and geological periods
**Format**: JSON-LD (machine-readable)

**Example**:
- Term: "Late Bronze Age (Levant)"
- URI: `https://perio.do/p/6z3xq5g3qw3#`
- Temporal span: -1550 to -1200
- Spatial coverage: Levant region
- Authority: Shaw, R. et al. (editors)

**Usage**: Standardise chronological terminology across datasets

---

#### Pleiades (Ancient Places Gazetteer)

**URL**: https://pleiades.stoa.org/
**PID**: URI-based (e.g., `https://pleiades.stoa.org/places/579885`)
**Scope**: Ancient geography (Mediterranean, Near East, Europe)
**Format**: RDF, JSON

**Example**:
- Place: "Athens"
- URI: `https://pleiades.stoa.org/places/579885`
- Coordinates: 37.97°N, 23.73°E
- Time periods: Archaic through Modern
- Variant names: Ἀθῆναι (Greek), Athenae (Latin)

**Usage**: Standardise ancient place names, link to modern coordinates

---

#### Getty AAT (Art & Architecture Thesaurus)

**URL**: http://www.getty.edu/research/tools/vocabularies/aat/
**PID**: URI-based (e.g., `http://vocab.getty.edu/aat/300264088`)
**Scope**: Art, architecture, material culture terminology
**Format**: RDF, SKOS

**Example**:
- Term: "Amphora"
- URI: `http://vocab.getty.edu/aat/300148696`
- Definition: "Storage jars..."
- Broader term: Vessels
- Related terms: Pelike, hydria

**Usage**: Standardise artefact terminology across museum collections

---

#### Darwin Core (Biodiversity Data)

**URL**: https://dwc.tdwg.org/
**PID**: Term URIs (e.g., `http://rs.tdwg.org/dwc/terms/scientificName`)
**Scope**: Biodiversity observations, specimens, occurrences
**Format**: RDF, XML, CSV standards

**Example**:
- Term: `scientificName`
- URI: `http://rs.tdwg.org/dwc/terms/scientificName`
- Definition: "The full scientific name..."
- Required for: Species occurrence data

**Usage**: Standardise biodiversity data across repositories (GBIF, iDigBio)

---

#### CIDOC-CRM (Cultural Heritage Conceptual Reference Model)

**URL**: http://www.cidoc-crm.org/
**PID**: URI-based ontology
**Scope**: Cultural heritage documentation (museums, archives)
**Format**: OWL ontology (RDF)

**Coverage**: Events, actors, objects, places, time-spans, information objects

**Usage**: Enable semantic integration across cultural heritage databases

---

#### EML (Ecological Metadata Language)

**URL**: https://eml.ecoinformatics.org/
**PID**: Schema URIs
**Scope**: Ecological and environmental datasets
**Format**: XML schema

**Usage**: Standardise ecological metadata (species, sites, sampling protocols)

---

### How to Identify Vocabulary Usage in Papers

**Look for:**
- Explicit vocabulary citations in Methods: "Terminology follows Getty AAT"
- URIs in data documentation: `http://vocab.getty.edu/aat/300148696`
- Namespace declarations in metadata files: `xmlns:dwc="http://rs.tdwg.org/dwc/terms/"`
- Repository metadata standards: "Dataset conforms to Darwin Core standard"
- Ontology references: "Site types coded using ARIADNEplus vocabulary"

**Extractable signals:**
- Vocabulary name + version
- Specific terms used with URIs
- Conformance statements in data availability
- Linked data assertions (RDF triples)

---

## Software-Specific FAIR Considerations (FAIR4RS)

**Context**: Software differs from data — it is **executable, versioned, and evolves**. FAIR principles adapted for Research Software (FAIR4RS, Chue Hong et al. 2022) recognise these distinctions.

### Software vs Data: Key Differences

| Aspect | Data | Software |
|--------|------|----------|
| Nature | Static artefact | Executable process |
| Change | Immutable (versions replace) | Continuously evolves |
| Dependencies | Standalone files | Requires runtime environment |
| Validity | Data is data | Software can be broken |
| Reuse | Read and interpret | Execute and obtain results |

**Implication**: "Code available on GitHub" ≠ "Computationally reproducible"

### Computational Reproducibility Spectrum

**Level 0: No code shared**
- Paper describes analysis verbally
- No scripts, no software specification
- **Reproducibility**: Impossible without re-implementing from description

**Level 1: Code only**
- Scripts shared (GitHub, supplementary materials)
- No dependency specification, no environment documentation
- **Example**: R script with `library()` calls but no package versions
- **Reproducibility**: Possible if dependencies guessed correctly; likely to break

**Level 2: Code + dependencies**
- Scripts + dependency specification
- **Example**: R script + `renv.lock`, Python + `requirements.txt`
- **Reproducibility**: Good if platform-compatible; may fail on different OS

**Level 3: Code + containerised environment**
- Scripts + complete computational environment
- **Example**: Docker container with all dependencies + OS + scripts
- **Reproducibility**: Excellent; container ensures consistent environment

**Level 4: Code + container + data + workflow orchestration**
- Complete pipeline: data → processing → results
- **Example**: Snakemake workflow + Docker + example data + documentation
- **Reproducibility**: Exemplary; push-button replication possible

---

### Environment Specification Types

**None**: No environment documented
- ❌ Cannot reproduce (dependency versions unknown)

**Requirements file**: Plain-text dependency list
- Examples: `requirements.txt` (Python), `package.json` (Node), `DESCRIPTION` (R)
- ⚠️ Better than nothing; may not capture exact versions or transitive dependencies

**Lock file**: Exact dependency snapshot
- Examples: `renv.lock` (R), `Pipfile.lock` (Python), `yarn.lock` (Node)
- ✅ Good; captures exact versions including transitive dependencies

**Container**: Complete OS + dependencies + code
- Examples: `Dockerfile` (Docker), `Singularity.def` (Singularity/Apptainer)
- ✅ Excellent; fully reproducible environment

**Executable notebook environment**: Cloud-based reproducible runtime
- Examples: Binder, Google Colab, Code Ocean
- ✅ Excellent; one-click execution without local setup

---

### Analysis Transparency

Beyond environment, **analytical transparency** requires documentation of:

**Random seeds documented**:
- Algorithms with stochastic elements (MCMC, random forest, bootstrapping) require seeds
- **Example**: `set.seed(42)` in R, `np.random.seed(42)` in Python
- ✅ Enables exact replication of stochastic results
- ❌ Without seeds: different random numbers → slightly different results

**Parameters documented**:
- Model parameters, algorithm hyperparameters, threshold choices
- **Example**: "MCMC run for 100,000 iterations, burn-in 10,000, thinning 10"
- ✅ Enables replication of exact analysis choices
- ❌ Default parameters may change across software versions

**Workflow specified**:
- Order of operations, data transformations, filtering steps
- **Example**: "Data cleaned (removed outliers >3 SD), log-transformed, z-scored, then ANOVA"
- ✅ Enables step-by-step replication
- ❌ Narrative descriptions may omit steps

**Alternative analyses considered**:
- Sensitivity analyses, robustness checks, alternative models tested
- **Example**: "Also tested with non-parametric Kruskal-Wallis; results consistent"
- ✅ Increases confidence in results (not p-hacking)
- ❌ Difficult to assess without this transparency

---

### HASS Software Contexts

**Common software types in HASS archaeology/palaeoecology:**

**Statistical analysis**: R, Python, Stata, SPSS
- Scripts for data processing, statistical tests, modelling
- **Reproducibility need**: Package versions, random seeds, parameters

**GIS workflows**: QGIS, ArcGIS, Python (GeoPandas, Rasterio), R (sf, terra)
- Spatial analysis, site distributions, viewshed analysis
- **Reproducibility need**: Software versions, projection definitions, algorithm parameters

**Domain-specific tools**: OxCal (radiocarbon calibration), PAST (palaeontology), pollen software
- Often GUI-based with limited scripting
- **Reproducibility need**: Version number, input file formats, settings screenshots

**Computational pipelines**: Snakemake, Nextflow, KNIME (rare in HASS but emerging)
- Multi-step data processing workflows
- **Reproducibility need**: Complete workflow definition + containers

**Interactive notebooks**: Jupyter (Python), R Markdown, Quarto
- Combine narrative + code + results
- **Reproducibility need**: Runtime environment + data

---

### FAIR4RS Assessment Criteria

**When assessing code availability, evaluate:**

**F: Findable**
- Software has PID (DOI, SWHID)? Not just GitHub URL?
- Software metadata present (CodeMeta.json, CITATION.cff)?
- Software indexed (Software Heritage, Zenodo, JOSS)?

**A: Accessible**
- Software downloadable via standard protocol (HTTPS)?
- Source code open (not compiled binaries only)?
- Access restrictions justified (proprietary dependencies, sensitive algorithms)?

**I: Interoperable**
- Uses standard formats (Python/R/MATLAB, not proprietary)?
- Dependencies documented?
- Workflow portable across systems (containerised)?

**R: Reusable**
- Licence clear (MIT, GPL, Apache, CC-BY)?
- Documentation present (README, examples, API docs)?
- Installation instructions provided?
- Tests included (unit tests, integration tests)?
- Active maintenance or archived release?

---

### Software FAIR Scoring

**Use computational reproducibility spectrum as scoring guide:**

| Level | Description | FAIR Score Contribution |
|-------|-------------|------------------------|
| 0 | No code shared | 0 points |
| 1 | Code only (GitHub) | +1 Findable (if public), +1 Accessible |
| 2 | Code + dependencies | +1 Interoperable, +1 Reusable (partial) |
| 3 | Code + container | +2 Reusable (high reproducibility) |
| 4 | Complete pipeline | +4 Reusable (exemplary) |

**Additional points:**
- Software PID (DOI/SWHID): +1 Findable
- Clear licence: +1 Reusable
- Documentation: +1 Reusable
- Archived snapshot (not just live repo): +1 Accessible

**Software FAIR maximum**: 16 points (same as data FAIR)

---

## Machine-Actionability: The Critical Distinction

**FAIR emphasises machine-actionability**, not just human accessibility.

### Definition

**Machine-actionable**: Computational systems can find, access, parse, and reuse the resource **with minimal or no human intervention**.

**Human-readable**: Humans can read and understand, but machines cannot automatically process.

### Examples: Not Machine-Actionable (NOT FAIR)

❌ **PDF supplementary materials** with data tables as images
- Humans can read; machines cannot extract structured data
- Requires manual transcription

❌ **Word documents** with data in unstructured paragraphs
- No defined schema; machines cannot parse reliably

❌ **Scanned images** of tables or field notes
- Requires OCR; no structured representation

❌ **URLs without PIDs** (link rot)
- Links break when servers move or shut down
- Not persistent; machines cannot reliably resolve

❌ **HTML tables without semantic markup**
- Presentation-focused; no machine-readable schema
- Cannot distinguish header rows, units, missing values

❌ **Data "available upon request"**
- Requires human interaction (email negotiation)
- No standard protocol; machines cannot retrieve automatically

❌ **Excel files without data dictionaries**
- Structured but lacking semantic metadata
- Machines cannot interpret column meanings, units, missing value codes

---

### Examples: Machine-Actionable (FAIR-Compliant)

✅ **Dataset with DOI** resolving to structured metadata (JSON-LD)
- Machines can resolve DOI, parse metadata, extract fields automatically

✅ **CSV files with schema documentation** (JSON Schema, Frictionless Data Package)
- Machines can validate structure, parse data, understand semantics

✅ **API access** for programmatic data retrieval
- RESTful APIs, OAI-PMH harvesters, SPARQL endpoints
- Machines can query, filter, retrieve without human intervention

✅ **NetCDF, HDF5, GeoPackage** with embedded metadata
- Self-describing formats; machines can read structure + semantics

✅ **RDF/JSON-LD** with linked data relationships
- Triple stores enable semantic reasoning
- Machines can traverse relationships, infer connections

✅ **Repository with OAI-PMH endpoint**
- Machines can harvest metadata automatically
- Enables aggregation services (DataCite, OpenAIRE)

---

### Machine-Actionability Rating Scale

**None**: No structured access
- PDF tables, email request, scanned documents, proprietary formats
- Requires full manual processing

**Low**: URLs exist but data unstructured
- Excel files without documentation, HTML tables, Word documents
- Some structure but no semantic layer

**Moderate**: Structured data but limited automation
- CSV with README (not machine-readable schema)
- Repository with download but no API
- Some metadata but not machine-parseable

**High**: Full machine-actionability
- CSV with JSON Schema or Frictionless metadata
- API access with OpenAPI/Swagger documentation
- Rich structured metadata (JSON-LD, RDF)
- Typed relationships to related objects (I3)
- Community standards compliance (R1.3)

---

## Context-Dependent Assessment

**FAIR expectations must be adjusted for:**

### Publication Year

**Pre-2016** (before FAIR principles published):
- Data sharing rare; any repository deposit = positive signal
- ORCIDs uncommon (launched 2012, adoption grew slowly)
- Domain repositories emerging but not widespread
- **Assessment**: Don't penalise lack of PIDs/FAIR practices

**2016-2019** (FAIR principles maturing):
- Increasing expectations for data sharing
- Repository use expected by progressive journals
- ORCIDs requested (but not required) by publishers
- **Assessment**: Moderate FAIR expectations; presence = good, absence ≠ bad

**2020+** (FAIR principles established):
- Many funders require data management plans
- Publishers increasingly require data availability statements
- ORCIDs often required for corresponding authors
- **Assessment**: Higher FAIR expectations reasonable

---

### Discipline

**HASS (Humanities, Arts, Social Sciences)**:
- **ORCID adoption**: 17-24% (2024 baseline)
- **Data sharing culture**: Developing but not universal
- **Domain repositories**: Emerging (tDAR, Open Context, ARIADNEplus)
- **Assessment**: Lower baseline expectations than natural sciences

**Natural sciences**:
- **ORCID adoption**: 91-93% (2024 baseline)
- **Data sharing culture**: Well-established
- **Domain repositories**: Mature (GenBank, ENA, Dryad, Zenodo)
- **Assessment**: Higher FAIR expectations

**Archaeology/palaeoecology specifically**:
- Field-specific repositories exist (tDAR, Neotoma, PANGAEA)
- Increasing FAIR adoption but still behind lab sciences
- Sample archiving traditions (museum collections) but limited PIDs
- **Assessment**: Moderate expectations; presence of domain repository use = exemplary

---

### Research Type

**Fieldwork** (excavation, survey, sampling):
- Data may be sensitive (site locations, Indigenous lands)
- Permits expected, sample curation important
- CARE principles relevant (Indigenous data sovereignty)
- **Assessment**: Ethical restrictions = positive when justified

**Laboratory** (analytical, experimental):
- Ethics approval common, protocols detailed
- Equipment/methods documentation critical
- **Assessment**: High expectations for protocol transparency

**Computational** (modelling, simulation, GIS):
- Code availability critical for reproducibility
- Software versions, parameters, seeds essential
- **Assessment**: High expectations for code sharing + environment specification

**Archival/textual** (historical documents, texts):
- Primary source citations expected
- Digital humanities: TEI-XML, linked open data emerging
- **Assessment**: Moderate expectations; structured encoding = exemplary

---

### CARE Principles Context

**When Indigenous data, traditional knowledge, or culturally sensitive information involved:**

**CARE Principles override full openness**:
- **C**ollective benefit: Data ecosystems for community benefit
- **A**uthority to control: Indigenous data sovereignty
- **R**esponsibility: Respectful relationships
- **E**thics: Indigenous ethical frameworks

**FAIR + CARE = Ethical data practices**:
- Restricted access with community authorisation = **POSITIVE A1.2 signal**
- Proper permitting demonstrates **Authority to Control**
- Benefit-sharing agreements demonstrate **Collective Benefit**

**Assessment approach**:
- ✅ Restricted access + ethical justification + community agreements = Exemplary FAIR+CARE
- ❌ Fully open Indigenous data without community consultation = Ethical violation
- Evaluate **whether restrictions are justified**, not just whether data is open

---

## Summary Assessment Guide

**When performing FAIR assessment (Pass 6):**

1. **Score each FAIR dimension** (F, A, I, R) using 0-4 point scale
2. **Calculate total FAIR score** (0-16 points)
3. **Assign FAIR rating**: Not FAIR (0-4), Minimally (5-8), Moderately (9-12), Highly (13-16)
4. **Assess machine-actionability**: None, Low, Moderate, High
5. **Document context**: Publication year, discipline, research type
6. **Justify scoring decisions**: Why this score? What context applies?
7. **Generate recommendations**: What would improve FAIR compliance?

**Common scoring patterns:**

| Paper Type | Typical Score | Rationale |
|------------|--------------|-----------|
| Pre-2016 HASS | 2-4 (Not FAIR) | Paper DOI only; data sharing rare |
| 2016-2020 HASS | 5-8 (Minimally) | Data shared but minimal PIDs/metadata |
| 2020+ HASS progressive | 9-12 (Moderately) | Repository use, some PIDs, structured metadata |
| 2020+ computational exemplary | 13-16 (Highly) | Full PID graph, code+container, rich metadata, community standards |

**Remember**: Context-dependent assessment is essential. A 2016 paper with score 6 may be exemplary for its time; a 2024 paper with score 6 may be below expectations.

---

## References

- Chue Hong et al. (2022). FAIR Principles for Research Software (FAIR4RS). *Scientific Data* 9:622. https://doi.org/10.1038/s41597-022-01710-x
- Marwick, B. (2017). Computational reproducibility in archaeological research. *Journal of Archaeological Method and Theory* 24:424-450.
- Wilkinson et al. (2016). The FAIR Guiding Principles. *Scientific Data* 3:160018. https://doi.org/10.1038/sdata.2016.18
- Carroll et al. (2020). The CARE Principles for Indigenous Data Governance. *Data Science Journal* 19:43. https://doi.org/10.5334/dsj-2020-043
- DataCite Metadata Schema: https://schema.datacite.org/
- FAIR4RS: https://www.rd-alliance.org/groups/fair-research-software-fair4rs-wg

---

**Document Version**: 1.0
**Last Updated**: 2025-11-11
**Part of**: research-assessor skill infrastructure assessment capability
