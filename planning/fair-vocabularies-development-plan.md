# FAIR Vocabularies Development Plan

**Version:** 1.0
**Date:** 2025-11-13
**Status:** Planning complete, implementation deferred to v2.7
**FAIR Impact:** Achieves I2 compliance (9/15 → 10/15, final point when combined with DOI: 15/15)

---

## Executive Summary

Development of FAIR-compliant controlled vocabularies for research designs, methods, and protocols extracted by the Research Assessor skill. Addresses Interoperability principle I2 ("Software uses FAIR-compliant vocabularies where they exist") currently scored 0/1 in FAIR4RS assessment.

**Approach:** Evidence-based vocabulary development from 20+ paper corpus extraction, published as Simple Knowledge Organisation System (SKOS) vocabularies with Zenodo Digital Object Identifiers (DOIs), integrated via JSON-LD schema enhancement.

**Effort:** 38-58 hours across 3 phases
**Target Version:** v2.7 (post-documentation completion)
**Deliverables:** 3 SKOS vocabularies, JSON-LD schema integration, Zenodo deposits

---

## Problem Statement

### Current State: Ad Hoc Terminology (I2 = 0/1)

Extraction schema uses uncontrolled, free-text terminology for three object types:

```json
{
  "research_designs": [
    {"design_name": "survey methodology"}
  ],
  "methods": [
    {"method_name": "ceramic typological analysis"}
  ],
  "protocols": [
    {"protocol_name": "Harris Matrix recording"}
  ]
}
```

### Issues with Uncontrolled Terminology

1. **No semantic interoperability:**
   - "ceramic typological analysis" vs "pottery classification" vs "ceramic seriation" → same concept, different labels
   - Cannot aggregate across papers ("show all papers using radiocarbon dating")

2. **No machine-actionable identifiers:**
   - No Uniform Resource Identifiers (URIs) for concepts
   - Cannot link to external ontologies (Getty AAT, Darwin Core, CIDOC-CRM)

3. **No hierarchical relationships:**
   - "excavation" broader than "stratigraphic excavation"?
   - "radiocarbon dating" related to "AMS dating"?
   - Relationships implicit, not explicit

4. **No cross-system integration:**
   - Cannot map to archaeological data repositories (tDAR, Open Context)
   - Cannot enable semantic search in catalogue systems
   - Cannot support automated aggregation pipelines

### FAIR Compliance Impact

**FAIR4RS I2:** "Software uses FAIR-compliant vocabularies where they exist"

**Current score:** 0/1
- No controlled vocabularies with persistent identifiers
- No alignment to existing FAIR vocabularies
- Terminology not published or versioned

**Target score:** 1/1
- SKOS vocabularies with Zenodo DOIs (FAIR vocabularies are themselves FAIR)
- Alignment to existing ontologies (Getty AAT, Darwin Core, ENVO)
- JSON-LD integration for machine-actionable references

---

## Evidence-Based Development Approach

### Rationale: Bottom-Up vs Top-Down

**Top-down approach (NOT RECOMMENDED):**
- Start with comprehensive ontology design
- Define all possible research designs/methods/protocols
- Impose structure on extractions

**Issues:**
- Premature abstraction (no empirical evidence)
- Over-engineering (concepts never observed in corpus)
- Discipline bias (archaeological assumptions may not generalise)

**Bottom-up approach (RECOMMENDED):**
- Extract 20+ papers across fieldwork disciplines
- Aggregate observed terminology with frequency counts
- Identify clusters and hierarchies empirically
- Publish minimal viable vocabulary

**Advantages:**
- Evidence-based (real usage patterns)
- Pragmatic scope (common concepts prioritised)
- Iterative refinement (expand as corpus grows)
- Community validation (grounded in practice)

---

## Three-Phase Development Plan

### Phase 1: Corpus Extraction and Aggregation

**Duration:** 20-30 hours
**Deliverable:** 20+ extraction.json files, terminology frequency tables

#### 1.1 Corpus Selection (20-25 papers)

**Discipline diversity:**
- **Archaeology (10 papers):**
  - Excavation reports (3): stratigraphic methods, recording protocols
  - Survey papers (3): systematic survey, geophysical prospection
  - Experimental archaeology (2): lithic technology, ceramic production
  - Archaeological science (2): radiocarbon dating, zooarchaeology

- **Ecology (5 papers):**
  - Field surveys (2): transect sampling, plot-based surveys
  - Camera trap studies (2): wildlife monitoring protocols
  - Long-term monitoring (1): phenology, vegetation dynamics

- **Ethnography (3 papers):**
  - Participant observation (1)
  - Interview-based research (1)
  - Multi-sited ethnography (1)

- **Field Geology (2 papers):**
  - Stratigraphic sampling (1)
  - Geochemical analysis (1)

**Publication type diversity:**
- Journal articles: 15
- Edited volumes: 3
- Software publications: 2

**Temporal spread:**
- 2015-2019: 8 papers (baseline practices)
- 2020-2024: 12 papers (current practices)

#### 1.2 Extraction Process

For each paper, complete Passes 0-6:
1. Pass 0: Metadata extraction
2. Passes 1-2: Claims/Evidence extraction
3. Passes 3-5: Research Design and Methods Assessment Protocol (RDMAP) extraction
4. Pass 6: Infrastructure extraction

**Focus on RDMAP passes (3-5):** Research designs, methods, protocols

#### 1.3 Terminology Aggregation

**Aggregate across 20+ extractions:**

1. **Research designs frequency table:**
   ```
   Term                          | Count | Papers
   ------------------------------|-------|-------
   survey methodology            | 12    | 8
   excavation strategy           | 8     | 6
   experimental design           | 5     | 4
   stratigraphic excavation      | 7     | 5
   systematic survey             | 9     | 7
   ```

2. **Methods frequency table:**
   ```
   Term                          | Count | Papers
   ------------------------------|-------|-------
   radiocarbon dating            | 15    | 10
   ceramic typological analysis  | 6     | 5
   geophysical prospection       | 8     | 6
   zooarchaeological analysis    | 4     | 3
   photogrammetry               | 7     | 6
   ```

3. **Protocols frequency table:**
   ```
   Term                          | Count | Papers
   ------------------------------|-------|-------
   Harris Matrix recording       | 9     | 6
   single-context recording      | 7     | 5
   transect sampling             | 6     | 5
   stratigraphic soil sampling   | 5     | 4
   photogrammetric workflow      | 6     | 5
   ```

#### 1.4 Cluster Identification

**Identify synonyms and variants:**

Example clusters:
- "radiocarbon dating" + "C14 dating" + "AMS radiocarbon" → `rdmap:radiocarbon-dating`
- "survey methodology" + "archaeological survey" + "field survey design" → `rdmap:survey-methodology`
- "excavation" + "archaeological excavation" + "stratigraphic excavation" → hierarchy (broader/narrower)

**Document hierarchical relationships:**
- Broader/narrower: "excavation" (broader) ← "stratigraphic excavation" (narrower)
- Related: "survey methodology" related to "transect design"
- Exact match: "radiocarbon dating" exactMatch ENVO:01001359

---

### Phase 2: Vocabulary Creation and Publication

**Duration:** 10-20 hours
**Deliverable:** 3 SKOS vocabularies with Zenodo DOIs

#### 2.1 Create SKOS Vocabularies

**Three separate vocabularies (modular approach):**

**1. Fieldwork Research Designs Vocabulary**

File: `fieldwork-research-designs.ttl`

```turtle
@prefix rdmap: <https://w3id.org/rdmap/designs/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix dc: <http://purl.org/dc/elements/1.1/> .
@prefix dct: <http://purl.org/dc/terms/> .

<https://w3id.org/rdmap/designs/> a skos:ConceptScheme ;
    dct:title "Fieldwork Research Designs Vocabulary"@en ;
    dct:description "Controlled vocabulary for strategic research design types in fieldwork-based disciplines (archaeology, ecology, ethnography, field geology)"@en ;
    dct:creator "Shawn Graham, Claude Sonnet 4.5" ;
    dct:created "2025-11-13"^^xsd:date ;
    dct:license <https://creativecommons.org/licenses/by/4.0/> ;
    skos:hasTopConcept rdmap:survey-methodology,
                       rdmap:excavation-strategy,
                       rdmap:experimental-design .

# Top-level concepts
rdmap:survey-methodology a skos:Concept ;
    skos:inScheme <https://w3id.org/rdmap/designs/> ;
    skos:prefLabel "Survey Methodology"@en ;
    skos:altLabel "Archaeological Survey"@en ;
    skos:altLabel "Field Survey Design"@en ;
    skos:definition "Strategic framework for systematic investigation of landscape or region through non-invasive observation and recording"@en ;
    skos:broader rdmap:spatial-sampling-design ;
    skos:narrower rdmap:systematic-survey,
                  rdmap:opportunistic-survey ;
    skos:related rdmap:transect-design .

rdmap:excavation-strategy a skos:Concept ;
    skos:inScheme <https://w3id.org/rdmap/designs/> ;
    skos:prefLabel "Excavation Strategy"@en ;
    skos:definition "Strategic framework for invasive subsurface investigation through controlled removal of deposits"@en ;
    skos:narrower rdmap:stratigraphic-excavation,
                  rdmap:test-pit-excavation ;
    skos:related rdmap:sampling-strategy .

# Narrower concepts
rdmap:systematic-survey a skos:Concept ;
    skos:inScheme <https://w3id.org/rdmap/designs/> ;
    skos:prefLabel "Systematic Survey"@en ;
    skos:definition "Survey design using predetermined spatial intervals or grids"@en ;
    skos:broader rdmap:survey-methodology ;
    skos:closeMatch <http://vocab.getty.edu/aat/300054698> .

# Continue for all observed research design types...
```

**2. Fieldwork Methods Vocabulary**

File: `fieldwork-methods.ttl`

```turtle
@prefix rdmap: <https://w3id.org/rdmap/methods/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix dc: <http://purl.org/dc/elements/1.1/> .
@prefix dct: <http://purl.org/dc/terms/> .
@prefix aat: <http://vocab.getty.edu/aat/> .
@prefix envo: <http://purl.obolibrary.org/obo/> .

<https://w3id.org/rdmap/methods/> a skos:ConceptScheme ;
    dct:title "Fieldwork Methods Vocabulary"@en ;
    dct:description "Controlled vocabulary for research methods in fieldwork-based disciplines"@en ;
    dct:creator "Shawn Graham, Claude Sonnet 4.5" ;
    dct:created "2025-11-13"^^xsd:date ;
    dct:license <https://creativecommons.org/licenses/by/4.0/> ;
    skos:hasTopConcept rdmap:chronometric-methods,
                       rdmap:analytical-methods,
                       rdmap:recording-methods .

# Chronometric methods
rdmap:radiocarbon-dating a skos:Concept ;
    skos:inScheme <https://w3id.org/rdmap/methods/> ;
    skos:prefLabel "Radiocarbon Dating"@en ;
    skos:altLabel "C14 Dating"@en ;
    skos:altLabel "14C Dating"@en ;
    skos:definition "Chronometric method using radioactive decay of carbon-14 isotope to determine age of organic materials"@en ;
    skos:broader rdmap:chronometric-methods ;
    skos:related rdmap:ams-radiocarbon ;
    skos:exactMatch envo:ENVO_01001359 ;
    skos:closeMatch aat:300054307 .

rdmap:ceramic-analysis a skos:Concept ;
    skos:inScheme <https://w3id.org/rdmap/methods/> ;
    skos:prefLabel "Ceramic Analysis"@en ;
    skos:altLabel "Pottery Analysis"@en ;
    skos:altLabel "Ceramic Typological Analysis"@en ;
    skos:definition "Analytical method for classification and characterisation of ceramic artefacts"@en ;
    skos:broader rdmap:artefact-analysis ;
    skos:narrower rdmap:ceramic-seriation,
                  rdmap:ceramic-petrography ;
    skos:closeMatch aat:300054277 .

# Continue for all observed methods...
```

**3. Fieldwork Protocols Vocabulary**

File: `fieldwork-protocols.ttl`

```turtle
@prefix rdmap: <https://w3id.org/rdmap/protocols/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix dc: <http://purl.org/dc/elements/1.1/> .
@prefix dct: <http://purl.org/dc/terms/> .

<https://w3id.org/rdmap/protocols/> a skos:ConceptScheme ;
    dct:title "Fieldwork Protocols Vocabulary"@en ;
    dct:description "Controlled vocabulary for operational protocols in fieldwork-based disciplines"@en ;
    dct:creator "Shawn Graham, Claude Sonnet 4.5" ;
    dct:created "2025-11-13"^^xsd:date ;
    dct:license <https://creativecommons.org/licenses/by/4.0/> ;
    skos:hasTopConcept rdmap:recording-protocols,
                       rdmap:sampling-protocols,
                       rdmap:processing-protocols .

# Recording protocols
rdmap:harris-matrix-recording a skos:Concept ;
    skos:inScheme <https://w3id.org/rdmap/protocols/> ;
    skos:prefLabel "Harris Matrix Recording"@en ;
    skos:definition "Stratigraphic recording protocol using matrix diagram to represent temporal relationships between contexts"@en ;
    skos:broader rdmap:stratigraphic-recording ;
    skos:related rdmap:single-context-recording ;
    skos:note "Standard protocol: record each stratigraphic unit, document physical relationships, create matrix diagram"@en .

rdmap:single-context-recording a skos:Concept ;
    skos:inScheme <https://w3id.org/rdmap/protocols/> ;
    skos:prefLabel "Single Context Recording"@en ;
    skos:definition "Archaeological recording protocol treating each stratigraphic context as independent unit with dedicated recording sheet"@en ;
    skos:broader rdmap:stratigraphic-recording ;
    skos:related rdmap:harris-matrix-recording .

# Continue for all observed protocols...
```

#### 2.2 Vocabulary Metadata

**Each vocabulary includes:**
- ConceptScheme metadata (title, description, creator, date, licence)
- CC-BY-4.0 licence (FAIR vocabularies must have open licence)
- Top concepts (high-level categories)
- Hierarchical relationships (broader/narrower)
- Associative relationships (related)
- External alignments (exactMatch, closeMatch to Getty AAT, ENVO, Darwin Core)
- Usage notes (procedural details where needed)

#### 2.3 Zenodo Publication

**Deposit each vocabulary on Zenodo:**

1. Create Zenodo deposit for each vocabulary
2. Upload .ttl files with README documentation
3. Add metadata:
   - Title: "Fieldwork Research Designs Vocabulary v1.0"
   - Creators: Shawn Graham, Claude Sonnet 4.5
   - Description: Purpose, scope, development methodology
   - Keywords: FAIR, SKOS, controlled vocabulary, fieldwork, archaeology
   - Licence: CC-BY-4.0
   - Related identifiers: Link to extraction schema, GitHub repository
4. Publish and obtain DOI

**Expected DOIs:**
- Research Designs: `10.5281/zenodo.XXXXXXX`
- Methods: `10.5281/zenodo.YYYYYYY`
- Protocols: `10.5281/zenodo.ZZZZZZZ`

#### 2.4 Persistent URI Registration

**Register w3id.org redirects:**

Request permanent URIs redirecting to Zenodo:
- `https://w3id.org/rdmap/designs/` → Zenodo DOI landing page
- `https://w3id.org/rdmap/methods/` → Zenodo DOI landing page
- `https://w3id.org/rdmap/protocols/` → Zenodo DOI landing page

**Fallback:** Use Zenodo DOIs directly if w3id.org registration delayed.

---

### Phase 3: Schema Integration and Validation

**Duration:** 4-8 hours
**Deliverable:** Schema v2.7 with JSON-LD context

#### 3.1 JSON-LD Context Creation

**Add @context to extraction schema:**

File: `extraction-system/schema/extraction-schema-v2.7.json`

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "@context": {
    "@vocab": "https://w3id.org/rdmap/schema/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "dc": "http://purl.org/dc/elements/1.1/",
    "rdmap-designs": "https://w3id.org/rdmap/designs/",
    "rdmap-methods": "https://w3id.org/rdmap/methods/",
    "rdmap-protocols": "https://w3id.org/rdmap/protocols/"
  },
  "title": "Research Assessor Extraction Schema v2.7",
  "description": "Schema for systematic extraction of claims, evidence, RDMAP, and infrastructure with FAIR vocabularies",
  "type": "object",
  "properties": {
    "research_designs": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "design_id": {"type": "string"},
          "design_name": {"type": "string"},
          "design_uri": {
            "type": "string",
            "format": "uri",
            "description": "URI from RDMAP Research Designs vocabulary"
          },
          "@type": {
            "type": "string",
            "description": "Vocabulary concept URI (e.g., rdmap-designs:survey-methodology)"
          },
          "tier": {"type": "string", "enum": ["strategic", "tactical", "operational"]},
          "verbatim_quote": {"type": "string"}
        },
        "required": ["design_id", "design_name", "tier"]
      }
    },
    "methods": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "method_id": {"type": "string"},
          "method_name": {"type": "string"},
          "method_uri": {
            "type": "string",
            "format": "uri",
            "description": "URI from RDMAP Methods vocabulary"
          },
          "@type": {
            "type": "string",
            "description": "Vocabulary concept URI (e.g., rdmap-methods:radiocarbon-dating)"
          },
          "tier": {"type": "string", "enum": ["strategic", "tactical", "operational"]},
          "verbatim_quote": {"type": "string"}
        },
        "required": ["method_id", "method_name", "tier"]
      }
    },
    "protocols": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "protocol_id": {"type": "string"},
          "protocol_name": {"type": "string"},
          "protocol_uri": {
            "type": "string",
            "format": "uri",
            "description": "URI from RDMAP Protocols vocabulary"
          },
          "@type": {
            "type": "string",
            "description": "Vocabulary concept URI (e.g., rdmap-protocols:harris-matrix-recording)"
          },
          "tier": {"type": "string", "enum": ["strategic", "tactical", "operational"]},
          "verbatim_quote": {"type": "string"}
        },
        "required": ["protocol_id", "protocol_name", "tier"]
      }
    }
  }
}
```

#### 3.2 Update RDMAP Prompts (Passes 3-5)

**Add vocabulary guidance to prompts:**

**Pass 3 (Explicit RDMAP) enhancement:**

```markdown
### Vocabulary Usage

When extracting research designs, methods, and protocols, align terminology with RDMAP vocabularies:

**Research Designs:**
- Check RDMAP Research Designs vocabulary: https://w3id.org/rdmap/designs/
- Use preferred labels (skos:prefLabel) when available
- Record URI in `design_uri` field
- Add `@type` with full vocabulary URI

**Methods:**
- Check RDMAP Methods vocabulary: https://w3id.org/rdmap/methods/
- Use preferred labels for consistency
- Record URI in `method_uri` field

**Protocols:**
- Check RDMAP Protocols vocabulary: https://w3id.org/rdmap/protocols/
- Use preferred labels
- Record URI in `protocol_uri` field

**If concept not in vocabulary:**
- Record free-text label in `design_name`/`method_name`/`protocol_name`
- Leave `design_uri`/`method_uri`/`protocol_uri` as null
- Note in extraction_notes for vocabulary enhancement
```

#### 3.3 Validation Testing

**Test schema integration on 4 existing extractions:**

1. Sobotkova et al. 2024
2. Ballsun-Stanton et al. 2018
3. Penske et al. 2023
4. Sobotkova et al. 2016

**For each extraction:**
- Map observed terminology to vocabulary URIs
- Add `@type` fields with vocabulary concepts
- Validate JSON-LD syntax
- Check URI resolution (vocabularies accessible)

**Expected outcome:**
- 80%+ of research designs map to vocabulary concepts
- 70%+ of methods map to vocabulary concepts
- 60%+ of protocols map to vocabulary concepts
- Remaining 20-40% documented for vocabulary v1.1 enhancement

---

## Alignment with External Ontologies

### Target Ontologies for Mapping

**1. Getty Art & Architecture Thesaurus (AAT)**
- **Coverage:** Material culture, archaeological methods, building techniques
- **URL pattern:** `http://vocab.getty.edu/aat/XXXXXXX`
- **Relationship:** `skos:exactMatch` or `skos:closeMatch`

**Examples:**
- Archaeological excavation: `aat:300053682`
- Survey methods: `aat:300054698`
- Radiocarbon dating: `aat:300054307`
- Ceramic analysis: `aat:300054277`

**2. CIDOC Conceptual Reference Model (CRM)**
- **Coverage:** Cultural heritage documentation, fieldwork activities
- **URL pattern:** `http://www.cidoc-crm.org/cidoc-crm/E##_ClassName`
- **Relationship:** `skos:related` (different semantic framework)

**Examples:**
- Fieldwork activity: `crm:E7_Activity`
- Observation: `crm:E13_Attribute_Assignment`
- Excavation: `crm:E7_Activity` subtype

**3. Darwin Core (biodiversity/ecology)**
- **Coverage:** Sampling protocols, occurrence recording
- **URL pattern:** `http://rs.tdwg.org/dwc/terms/TermName`
- **Relationship:** `skos:exactMatch` for ecological fieldwork

**Examples:**
- Sampling protocol: `dwc:samplingProtocol`
- Event (field survey): `dwc:Event`
- Location recording: `dwc:Location`

**4. Environment Ontology (ENVO)**
- **Coverage:** Environmental sampling, chronometric methods
- **URL pattern:** `http://purl.obolibrary.org/obo/ENVO_XXXXXXX`
- **Relationship:** `skos:exactMatch` for scientific methods

**Examples:**
- Radiocarbon dating: `ENVO:01001359`
- Soil sampling: `ENVO:02000061`
- Field survey: `ENVO:01000831`

### Mapping Strategy

**Prioritise:**
1. **exactMatch:** Identical semantic meaning (rare)
2. **closeMatch:** Very similar meaning, minor scope differences (common)
3. **related:** Associated concepts, different semantic domains (fallback)

**Document in SKOS:**
```turtle
rdmap:radiocarbon-dating a skos:Concept ;
    skos:exactMatch envo:ENVO_01001359 ;  # Exact semantic match
    skos:closeMatch aat:300054307 ;        # Close but scope differs slightly
    skos:related crm:E16_Measurement .     # Related activity
```

---

## Scope Decisions and Exclusions

### Include in Vocabularies

**✅ Common fieldwork concepts (empirically observed ≥3 times):**
- Survey methodology, excavation strategy, experimental design
- Radiocarbon dating, ceramic analysis, geophysical prospection
- Harris Matrix recording, single-context recording, transect sampling

**✅ Discipline-standard terminology:**
- Terms from published methodological frameworks (TIDieR, CONSORT-Outcomes)
- Concepts from archaeological/ecological textbooks
- Methods with established best practices

**✅ Hierarchical clusters:**
- Broader concepts with multiple narrower variants
- Example: "excavation" (broader) ← "stratigraphic excavation" (narrower)

### Exclude from Vocabularies

**❌ Ultra-specific techniques mentioned once:**
- "Sobotkova's tablet workflow" → Too specific, not generalizable
- Proprietary software workflows → Tools, not methods
- One-off experimental protocols → Document in free text

**❌ Proprietary software as methods:**
- "ArcGIS analysis" → Tool, not method (use "spatial analysis" instead)
- "Photoshop editing" → Tool, not protocol

**❌ Theoretical frameworks:**
- "Post-processual archaeology" → Theory, not operational method
- "Actor-Network Theory" → Interpretive framework

**❌ Author-specific jargon:**
- Neologisms without community adoption
- Undefined abbreviations

### Edge Cases: Decision Tree

**When uncertain if concept belongs in vocabulary:**

1. **Frequency test:** Observed in ≥3 papers from different research groups?
   - Yes → Include
   - No → Free text, consider for v1.1

2. **Generalisability test:** Can other researchers use this term?
   - Yes → Include
   - No (too specific) → Free text

3. **Operationalisation test:** Describes HOW research was done?
   - Yes → Include
   - No (describes WHY or WHAT was found) → May be claim/evidence, not RDMAP

4. **Community recognition test:** Term appears in textbooks or methods standards?
   - Yes → Include with high priority
   - No → Include with lower priority if frequent

---

## FAIR Principles for Vocabularies

**Meta-requirement:** FAIR vocabularies must themselves be FAIR.

### Findable

- **F1:** Zenodo DOIs for each vocabulary
- **F2:** Rich metadata (title, description, creator, keywords)
- **F3:** Vocabularies reference DOIs of related resources (extraction schema)
- **F4:** Indexed in Zenodo search, w3id.org registry

### Accessible

- **A1:** Vocabularies retrievable via Zenodo DOI (persistent, free)
- **A1.1:** HTTPS protocol (standard web access)
- **A1.2:** No authentication required (public access)
- **A2:** Metadata persists even if vocabularies updated (Zenodo versioning)

### Interoperable

- **I1:** SKOS (formal, widely-used knowledge representation language)
- **I2:** SKOS uses FAIR vocabularies (references Getty AAT, ENVO with URIs)
- **I3:** Qualified references (skos:exactMatch, skos:broader with relationship types)

### Reusable

- **R1:** CC-BY-4.0 licence (clear, open)
- **R1.1:** Provenance documented (empirical development from 20-paper corpus)
- **R1.2:** SKOS standard aligns with community standards (Linked Open Data)
- **R1.3:** Detailed usage notes in SKOS definitions

**Expected FAIR score for vocabularies:** 15/15 (Exemplary FAIR)

---

## Implementation Timeline

### Pre-Phase: Prerequisites

**Before starting Phase 1:**
- ✅ Extraction system complete (Passes 0-6 validated)
- ✅ Schema v2.6 stable
- ✅ Documentation complete (Phases 3-7)
- ⏳ Identify 20-25 candidate papers for corpus

**Estimated pre-phase effort:** 4-6 hours (paper identification and acquisition)

### Phase 1: Corpus Extraction (3-4 weeks)

| Week | Papers | Discipline Focus | Effort |
|------|--------|------------------|--------|
| 1 | 5 papers | Archaeology (excavation) | 6-8 hours |
| 2 | 5 papers | Archaeology (survey) | 6-8 hours |
| 3 | 5 papers | Ecology + Ethnography | 6-8 hours |
| 4 | 5 papers | Archaeological science + Geology | 6-8 hours |

**Total Phase 1:** 24-32 hours (extraction) + 4-6 hours (aggregation) = **28-38 hours**

### Phase 2: Vocabulary Creation (1-2 weeks)

| Task | Duration | Deliverable |
|------|----------|-------------|
| SKOS file creation | 4-6 hours | 3 .ttl files |
| External alignment (Getty, ENVO) | 2-4 hours | skos:exactMatch mappings |
| Zenodo deposits | 2-3 hours | 3 DOIs |
| w3id.org registration | 1-2 hours | Persistent URIs |

**Total Phase 2:** **9-15 hours**

### Phase 3: Schema Integration (1 week)

| Task | Duration | Deliverable |
|------|----------|-------------|
| JSON-LD context creation | 2-3 hours | Schema v2.7 |
| Prompt updates (Passes 3-5) | 2-3 hours | Updated prompts |
| Validation testing | 2-3 hours | 4 test extractions |

**Total Phase 3:** **6-9 hours**

### Overall Timeline

**Total effort:** 43-62 hours
**Calendar time:** 5-7 weeks (allowing for corpus paper acquisition)
**Target completion:** v2.7 release (Q1 2025)

---

## Deliverables

### Primary Deliverables

1. **Fieldwork Research Designs Vocabulary v1.0**
   - SKOS .ttl file (50-100 concepts)
   - Zenodo deposit with DOI
   - w3id.org persistent URI
   - CC-BY-4.0 licence

2. **Fieldwork Methods Vocabulary v1.0**
   - SKOS .ttl file (80-120 concepts)
   - Zenodo deposit with DOI
   - w3id.org persistent URI
   - CC-BY-4.0 licence

3. **Fieldwork Protocols Vocabulary v1.0**
   - SKOS .ttl file (60-100 concepts)
   - Zenodo deposit with DOI
   - w3id.org persistent URI
   - CC-BY-4.0 licence

### Supporting Deliverables

4. **Extraction Schema v2.7**
   - JSON schema with JSON-LD @context
   - Integration with vocabulary URIs
   - Backwards-compatible with v2.6

5. **Updated RDMAP Prompts**
   - Pass 3, 4, 5 prompts with vocabulary guidance
   - Lookup instructions for vocabulary alignment

6. **Vocabulary Development Report**
   - Aggregation methodology
   - Frequency tables
   - Mapping decisions documented
   - Future enhancement recommendations

7. **20+ Paper Corpus Extractions**
   - Complete extraction.json files
   - Test cases for validation
   - Evidence base for future vocabulary expansion

---

## Success Metrics

### Quantitative Metrics

1. **Vocabulary coverage:** 70%+ of RDMAP concepts from 20-paper corpus map to vocabulary URIs
2. **External alignment:** 50%+ of concepts have skos:exactMatch or skos:closeMatch to external ontologies
3. **Hierarchy depth:** 2-3 levels (top concepts → narrower concepts → specific variants)
4. **Reuse validation:** 3+ external projects adopt vocabularies within 6 months

### FAIR Compliance Metrics

1. **Vocabulary FAIR score:** 15/15 (Exemplary FAIR)
2. **Extraction schema I2 compliance:** 0/1 → 1/1
3. **Overall extraction schema FAIR score:** 9/15 → 10/15 (with DOI: 15/15)

### Qualitative Metrics

1. **Community feedback:** 5+ domain experts review vocabularies (archaeology, ecology)
2. **Usability:** Extraction workflow maintains <5 minutes per RDMAP object (no efficiency loss)
3. **Interoperability demonstration:** Cross-paper aggregation queries work (e.g., "all papers using radiocarbon dating")

---

## Risks and Mitigation

### Risk 1: Insufficient Corpus Diversity

**Risk:** 20 papers dominated by single discipline (e.g., 18 archaeology, 2 ecology)

**Impact:** Vocabularies biased towards archaeological terminology, poor coverage for ecology/ethnography

**Mitigation:**
- Enforce corpus selection quotas (minimum 3 papers per discipline)
- Prioritise multi-disciplinary papers (archaeology + geology, ecology + ethnography)
- Document discipline coverage in vocabulary metadata
- Plan v1.1 enhancement for under-represented disciplines

**Likelihood:** Medium | **Impact:** Medium | **Mitigation Cost:** Low

---

### Risk 2: External Ontology Mapping Complexity

**Risk:** Getty AAT, ENVO, Darwin Core use incompatible semantic frameworks

**Impact:** Difficult to create accurate exactMatch/closeMatch alignments

**Mitigation:**
- Prioritise closeMatch over exactMatch (acknowledge semantic differences)
- Use related for loose associations
- Document mapping decisions in vocabulary notes
- Consult ontology documentation for canonical definitions

**Likelihood:** Medium | **Impact:** Low | **Mitigation Cost:** Medium (2-4 extra hours)

---

### Risk 3: Vocabulary Versioning Challenges

**Risk:** v1.0 vocabularies need revision after 6 months (new concepts, refined hierarchies)

**Impact:** Existing extractions reference outdated URIs, backwards compatibility issues

**Mitigation:**
- Use Zenodo versioning (v1.0, v1.1, v1.2 with separate DOIs)
- Never delete concepts (deprecate with skos:deprecated, redirect to replacement)
- Document versioning policy in vocabulary README
- Schema supports multiple vocabulary versions (optional version parameter)

**Likelihood:** High (expected) | **Impact:** Low (manageable) | **Mitigation Cost:** Low

---

### Risk 4: Low Community Adoption

**Risk:** External projects don't use vocabularies (effort wasted)

**Impact:** Limited reuse, vocabularies become project-specific rather than community standard

**Mitigation:**
- Publicise vocabularies via blog post, conference presentation
- Deposit vocabularies in domain registries (Research Data Alliance, FAIRsharing.org)
- Create usage examples (Jupyter notebook demonstrating queries)
- Solicit feedback from 5+ domain experts before v1.0 publication

**Likelihood:** Medium | **Impact:** Medium | **Mitigation Cost:** Medium (8-12 extra hours)

---

### Risk 5: w3id.org Registration Delay

**Risk:** w3id.org permanent URI registration takes >4 weeks

**Impact:** Cannot use persistent URIs in schema, blocks Phase 3

**Mitigation:**
- Use Zenodo DOIs directly as URIs (fallback, less elegant but functional)
- w3id.org registration can happen post-publication (update schema later)
- Example: `https://doi.org/10.5281/zenodo.XXXXXXX#survey-methodology`

**Likelihood:** Low | **Impact:** Low | **Mitigation Cost:** None (fallback plan)

---

## Post-v1.0 Roadmap

### Version 1.1 Enhancements (6 months post-v1.0)

**Triggers for v1.1:**
- 50+ papers extracted (2.5× corpus expansion)
- New disciplines added (field geology, marine ecology)
- User feedback identifies missing concepts

**Planned additions:**
- 20-30 new concepts from expanded corpus
- Refinement of hierarchies based on usage patterns
- Additional external alignments (PeriodO chronology, SESAR sample IDs)

### Version 2.0 Major Revision (12-18 months post-v1.0)

**Triggers for v2.0:**
- 100+ papers extracted (5× corpus expansion)
- Community consensus on hierarchical restructuring
- Integration with archaeological data repositories (tDAR, Open Context)

**Planned changes:**
- Top-level restructuring (evidence-based from 100-paper corpus)
- Cross-disciplinary alignment (archaeology + ecology + ethnography unified framework)
- Multi-lingual labels (Spanish, French for international adoption)

---

## References and Resources

### Vocabulary Standards

- **SKOS Primer:** https://www.w3.org/TR/skos-primer/
- **SKOS Reference:** https://www.w3.org/TR/skos-reference/
- **Linked Open Vocabularies (LOV):** https://lov.linkeddata.es/dataset/lov/

### External Ontologies

- **Getty AAT:** http://vocab.getty.edu/aat/
- **CIDOC-CRM:** http://www.cidoc-crm.org/
- **Darwin Core:** http://rs.tdwg.org/dwc/
- **ENVO:** http://environmentontology.org/
- **PeriodO:** https://perio.do/

### Publishing Platforms

- **Zenodo:** https://zenodo.org/
- **w3id.org:** https://w3id.org/
- **FAIRsharing.org:** https://fairsharing.org/

### Methodology References

- Chue Hong et al. (2022). FAIR Principles for Research Software. *Scientific Data* 9:622. https://doi.org/10.1038/s41597-022-01710-x
- Wilkinson et al. (2016). The FAIR Guiding Principles for scientific data management and stewardship. *Scientific Data* 3:160018. https://doi.org/10.1038/sdata.2016.18

---

## Appendix A: Example Corpus Papers (Provisional)

### Archaeology (10 papers)

**Excavation:**
1. Hodder, I. (2021). Çatalhöyük excavations: stratigraphic methods
2. Lucas, G. (2019). Single-context recording in practice
3. Harris, E. (2018). Principles of archaeological stratigraphy

**Survey:**
4. Banning, E. B. (2020). Archaeological survey methods
5. Parcak, S. (2017). Remote sensing and ground survey integration
6. Fish & Kowalewski (2019). Regional survey methodologies

**Experimental:**
7. Outram, A. (2018). Experimental archaeology of bone working
8. Eren et al. (2020). Lithic technology replication experiments

**Archaeological Science:**
9. Colonese et al. (2022). Radiocarbon dating best practices
10. Reitz & Wing (2019). Zooarchaeological analysis protocols

### Ecology (5 papers)

11. Ralph et al. (2020). Camera trap survey design
12. Jones et al. (2021). Vegetation transect sampling
13. Lindenmayer et al. (2018). Long-term ecological monitoring
14. McKinney & Lockwood (2019). Plot-based biodiversity assessment
15. Krebs (2019). Ecological methodology

### Ethnography (3 papers)

16. Marcus (2019). Multi-sited ethnography: methods
17. Bernard (2018). Research methods in anthropology (interviews)
18. Schensul et al. (2020). Participant observation protocols

### Field Geology (2 papers)

19. Tucker et al. (2020). Stratigraphic sampling for geochronology
20. Walker & Lowe (2019). Quaternary dating methods

---

## Appendix B: SKOS Quick Reference

### Concept Properties

```turtle
# Basic properties
skos:prefLabel      # Preferred label (one per language)
skos:altLabel       # Alternative labels (synonyms, abbreviations)
skos:definition     # Formal definition
skos:note           # Usage notes, procedural details

# Hierarchical relationships
skos:broader        # Parent concept (one level up)
skos:narrower       # Child concept (one level down)
skos:topConceptOf   # Top-level concept in scheme

# Associative relationships
skos:related        # Semantically related (not hierarchical)

# External alignment
skos:exactMatch     # Identical semantic meaning
skos:closeMatch     # Very similar meaning
skos:broadMatch     # External broader concept
skos:narrowMatch    # External narrower concept
```

### ConceptScheme Properties

```turtle
# Metadata
dct:title           # Vocabulary title
dct:description     # Purpose and scope
dct:creator         # Author(s)
dct:created         # Publication date
dct:license         # CC-BY-4.0 recommended

# Structure
skos:hasTopConcept  # Top-level concepts in this scheme
```

---

**End of Planning Document**
