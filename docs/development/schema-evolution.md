# Schema Crosswalk v1.1

**Version:** 1.1  
**Last Updated:** 2025-10-18  
**Purpose:** Map our schema elements to existing ontologies for future formalization  
**Schema Version:** v2.3

---

## Overview

This document tracks mappings between our pragmatic JSON schema and existing formal ontologies. As we develop the schema empirically, we document potential mappings to facilitate future formalization without blocking current progress.

**Mapping Types:**
- **Exact**: 1:1 correspondence with existing ontology concept
- **Broader**: Our concept is more specific than existing concept
- **Narrower**: Our concept is more general than existing concept
- **Related**: Similar but not identical; could inform future alignment
- **Novel**: No clear equivalent; emerged from empirical work

---

## Core Concepts

| Our Term | Definition | Exact Match | Broader | Narrower | Related | Notes |
|----------|------------|-------------|---------|----------|---------|-------|
| **evidence** | Raw observations/measurements requiring minimal interpretation | - | prov:Entity | micropub:Statement | doco:Result | Consider evidence_basis subtypes for refinement |
| **claim** | Assertions requiring evidence/interpretation | micropub:Claim | - | - | aif:I-node | Core assertion with support structure |
| **implicit_argument** | Unstated assumptions/implications/disciplinary foundations | - | aif:I-node | - | walton:ArgumentationScheme | Type 1/2/3 taxonomy is novel |
| **method** | Research procedure/process | - | prov:Activity | - | researchobject:Process | Need HASS qualitative extensions |
| **project_metadata** | Context not supporting claims | - | dcterms:description | - | - | Novel distinction from extraction work |

---

## Properties

| Our Property | Source Schema | Mapping Type | URI/Reference | Notes |
|--------------|---------------|--------------|---------------|-------|
| **evidence.evidence_basis** | Novel (empirical) | Related | prov:Entity subtypes | Observable classification of evidence source |
| **evidence.declared_uncertainty** | Novel (empirical) | Related | Multiple sources | Captures author-stated uncertainty |
| **evidence.declared_uncertainty.indicator** | Novel (v2.3) | Related | Hedging linguistics | Linguistic markers (ca., about, ~, ±) |
| **evidence.declared_uncertainty.applies_to** | Novel (v2.3) | - | - | Specifies scope of uncertainty |
| **evidence.declared_uncertainty.upper_bound** | Novel (v2.3) | Related | Statistical bounds | For bounded range uncertainties |
| **evidence.declared_uncertainty.range** | Novel (v2.3) | Related | Statistical bounds | For range-type uncertainties |
| **evidence.expected_information_missing** | Novel (empirical) | - | - | Assessment preparation, not in existing schemas |
| **evidence.expected_uncertainty_missing** | Novel (v2.3) | - | - | Extended from claims to evidence |
| **evidence.implicit_evidence** | Novel (empirical) | Related | Professional judgment sources | Distinguishes unstated evidence |
| **evidence.provenance** | PROV-O | Exact | prov:wasGeneratedBy, prov:wasAttributedTo, prov:wasDerivedFrom | Low-hanging formalization |
| **evidence.related_evidence** | Novel (v2.3) | Related | owl:seeAlso | Cross-references for analytical view pattern |
| **evidence.consolidation_metadata** | Novel (v2.3) | Related | prov:wasDerivedFrom, prov:qualifiedDerivation | Pass 2 rationalization provenance |
| **claim.claim_type** | Novel (empirical) | Related | Multiple | EMPIRICAL/INTERPRETATION/METHODOLOGICAL/THEORETICAL |
| **claim.claim_role** | Novel (empirical) | Related | Hierarchy concepts | Four-level structure for assessment prioritization |
| **claim.claim_role: "synthesis"** | Novel (v2.3) | Related | doco:Conclusion | Cross-subsection integration claims |
| **claim.primary_function** | Novel (v2.3) | Related | toulmin:Claim, aif:I-node | Argumentative role (premise/finding/conclusion/recommendation) |
| **claim.claim_nature** | Novel (v2.3) | - | - | Epistemic classification (quantitative/qualitative/mixed/definitional) |
| **claim.quantitative_details** | Novel (v2.3) | Related | Statistics ontologies | Nested structure for quantitative claims |
| **claim.quantitative_details.source** | Novel (v2.3) | Related | prov:wasGeneratedBy | Measurement/calculation/estimate/statistical |
| **claim.quantitative_details.arithmetic_verifiable** | Novel (v2.3) | - | - | Flags calculations vs measurements |
| **claim.claim_status** | Novel (empirical) | Related | prov:derivedByInference | explicit vs implicit distinction |
| **claim.author_confidence** | Novel (empirical) | Related | Hedging taxonomies | Captures authorial epistemic stance |
| **claim.extraction_flags** | Novel (empirical) | - | - | All three flags empirically identified |
| **claim.extraction_flags.generalization_from_single_case** | Novel (empirical) | Related | walton:ArgumentFromGeneralization | Abductive HASS research pattern |
| **claim.extraction_flags.requires_professional_judgment** | Novel (empirical) | Related | walton:ExpertOpinionScheme | Maps to expert opinion pattern |
| **claim.extraction_flags.boundary_ambiguous** | Novel (empirical) | - | - | Extraction quality tracking |
| **claim.credibility_assessment** | repliCATS | Adapted | replicats:CredibilitySignal | 7-signal framework adapted for HASS |
| **claim.credibility_assessment.transparency** | repliCATS | Adapted | replicats:Transparency | Methodological documentation quality |
| **claim.credibility_assessment.plausibility** | repliCATS | Adapted | replicats:Plausibility | Consistency with domain knowledge |
| **claim.credibility_assessment.validity** | repliCATS | Adapted | replicats:Validity | Methods appropriate to question |
| **claim.credibility_assessment.robustness** | repliCATS | Adapted | replicats:Robustness | Sensitivity to assumptions |
| **claim.credibility_assessment.comprehensibility** | repliCATS | Adapted | replicats:Comprehensibility | Clarity of methods/claims |
| **claim.credibility_assessment.replicability** | repliCATS | Adapted | replicats:Replicability | Sufficient detail to replicate |
| **claim.credibility_assessment.generalizability** | repliCATS | Adapted | replicats:Generalizability | Scope appropriately bounded |
| **claim.consolidation_metadata** | Novel (v2.3) | Related | prov:wasDerivedFrom | Pass 2 rationalization provenance |
| **evidence.evidence_strength** | Multiple | Synthesized | legal:EvidenceWeight, cochrane:QualityOfEvidence | Hybrid from legal + systematic review frameworks |
| **implicit_argument.type** | Novel/Adapted | Related | walton:ArgumentationScheme | Type 1/2 = argument schemes; Type 3 = novel |
| **implicit_argument.type (disciplinary_assumption)** | Novel (empirical) | - | - | Type 3: meta-level, paradigmatic assumptions |
| **implicit_argument.argumentation_scheme** | Walton | Related | walton:ArgumentationScheme | Critical questions framework |
| **implicit_argument.coi_note** | Novel (empirical) | Related | Conflict of interest declarations | Author stake in findings |
| **implicit_argument.consolidation_metadata** | Novel (v2.3) | Related | prov:wasDerivedFrom | Pass 2 rationalization provenance |
| **consolidation_metadata.consolidation_type** | Novel (v2.3) | Related | prov:qualifiedDerivation | Taxonomy of 9 consolidation operations |
| **consolidation_metadata.information_preserved** | Novel (v2.3) | Related | dcat:DataQuality | Tracks lossy vs lossless transformations |
| **consolidation_metadata.granularity_available** | Novel (v2.3) | - | - | Documents detail in source not extracted |
| **supports_claims, supported_by_claims** | Multiple | Related | micropub:supports, aif:supports | Support relationships |
| **supported_by_evidence** | Multiple | Related | micropub:supportedBy | Evidence-claim links |

---

## Structural Elements

| Our Structure | Source Schema | Mapping Type | URI/Reference | Notes |
|---------------|---------------|--------------|---------------|-------|
| **Four-level hierarchy** (core → intermediate → supporting → evidence) | Novel (empirical) | - | - | Assessment prioritization structure |
| **Dual-layer uncertainty** (declared + expected) | Novel (empirical) | - | - | Author layer + assessor layer separation; **v2.3:** Enhanced with indicator, applies_to, bounds fields |
| **Extraction vs assessment separation** | Novel (methodological) | Related | Annotation workflows | Clear phase distinction with field-level marking |
| **Two-pass extraction workflow** | Novel (methodological) | Related | PROV-O workflow patterns | Pass 1: liberal extraction; Pass 2: rationalization; **v2.3:** Now requires consolidation_metadata |
| **evidence_basis enumeration** | Observable source classification for extraction | Could inform prov:Entity subtypes | Empirically validated |
| **Four-level hierarchy** | Assessment prioritization (core > intermediate > supporting > evidence) | Could map to importance/priority ontologies | In use, may simplify to 3 levels |

---

## Controlled Vocabularies (Emerging)

These will be refined after 10+ paper extractions:

### evidence_type (currently free-text)

**Emerging categories:**
- archaeological_material
- archival_document
- statistical_output
- geospatial_data
- radiometric_date
- stratigraphic_sequence
- comparative_dataset
- expert_assessment
- observational_record

**Future mapping:** Domain-specific evidence taxonomies; could extend PROV-O Entity types

### method_type (currently free-text)

**Emerging categories:**
- radiocarbon_dating
- GIS_analysis
- bayesian_modeling
- survey
- excavation
- statistical_modeling
- crowdsourcing
- stylistic_analysis
- comparative_analysis

**Future mapping:** ResearchObject:Process + HASS qualitative extensions

---

## Novel Elements (No Direct Mapping)

| Element | Rationale | Future Formalization Path |
|---------|-----------|---------------------------|
| **project_metadata** | Empirically identified - separates context from evidence | Could map to dcterms:description or custom HASS vocab |
| **claim_status (explicit/implicit)** | Empirically identified - extraction artifact tracking | Consider prov:derivedByInference or custom property |
| **generalization_from_single_case** | Empirically identified - abductive reasoning pattern | Subtype of walton:ArgumentFromGeneralization |
| **requires_professional_judgment** | Empirically identified - flags claims needing domain expertise | Related to walton:ExpertOpinionScheme |
| **boundary_ambiguous** | Empirically identified - extraction quality tracking | Extraction metadata, may not need formalization |
| **consolidation_metadata** | Empirically identified (v2.3) - Pass 2 rationalization traceability needed | Map to PROV-O qualified derivation pattern |
| **consolidation_metadata.consolidation_type** | Empirically identified (v2.3) - taxonomy of 9 consolidation operations | Custom vocabulary; could extend PROV-O derivation types |
| **consolidation_metadata.information_preserved** | Empirically identified (v2.3) - lossy vs lossless tracking | Related to dcat:DataQuality; could formalize as quality metric |
| **consolidation_metadata.granularity_available** | Empirically identified (v2.3) - documents detail not extracted | Extraction metadata describing source richness |
| **related_evidence** | Empirically identified (v2.3) - analytical view pattern needs cross-referencing | Map to owl:seeAlso or custom relation property |
| **primary_function** | Empirically identified (v2.3) - argumentative role distinct from claim_role | Map to Toulmin model components (claim/data/warrant/backing) |
| **claim_nature** | Empirically identified (v2.3) - epistemic classification for assessment | Consider formal epistemology ontologies |
| **quantitative_details** | Empirically identified (v2.3) - structured quantitative claim metadata | Map to statistics/measurement ontologies (QUDT, OM) |
| **Multi-dimensional evidence pattern** | Empirically identified (v2.3) - Results test revealed need for multiple organizational views | Document as extraction pattern, not ontology concept; enables analytical views |
| **Anchor numbers principle** | Empirically identified (v2.3) - strategic duplication for interpretability | Methodological principle, not schema element |
| **Temporal progression separation** | Empirically identified (v2.3) - year-over-year comparisons require separate items | Extraction guideline, not schema element |

---

## Deferred Mappings (For Formalization Phase)

These will be addressed when moving to formal ontology:

- **Full PROV-O integration** - Complete provenance chains for all evidence
- **SPAR/DoCO document structure** - Section-level markup and citation typing
- **AIF formal argumentation** - Complete argument interchange format
- **Complete FAIR assessment** - Automated FAIR principle scoring
- **Nanopublication identifiers** - Immutable, versioned claim identifiers
- **Research Object workflows** - Complete computational provenance
- **OWL class definitions** - Formal logic and reasoning support
- **SHACL validation shapes** - RDF constraint validation

---

## Mapping Strategy

### Current Phase (Pragmatic Iteration)

**Approach:**
1. Build functional JSON schema based on empirical needs
2. Document obvious mappings as we encounter them (5 mins per addition)
3. Flag novel elements that emerged from extraction work
4. Don't block development waiting for perfect mappings

**Documentation trigger:** Every time we add a field, spend 5 minutes checking:
- Is this concept in the survey document?
- Does it map to existing ontology?
- Is it novel? If so, why does it exist?

### Future Phase (Formalization)

**Approach:**
1. Complete crosswalk for all elements
2. Create formal mapping ontology (OWL/SKOS)
3. Add JSON-LD @context with proper URIs
4. Implement RDF serialization option
5. Enable semantic interoperability

**Timeline:** After schema stabilizes (minimal changes across 3 consecutive papers)

---

## Integration Examples

### Example 1: Basic Evidence with PROV-O

**Our JSON:**
```json
{
  "evidence_id": "E001",
  "evidence_text": "125.8 person-hours of digitization",
  "evidence_basis": "direct_measurement"
}
```

**Potential JSON-LD with @context:**
```json
{
  "@context": {
    "evidence": "https://hass-credibility.org/vocab#Evidence",
    "prov": "http://www.w3.org/ns/prov#"
  },
  "@type": "evidence",
  "@id": "E001",
  "evidence_text": "125.8 person-hours of digitization",
  "prov:wasGeneratedBy": "digitization_activity",
  "evidence_basis": "direct_measurement"
}
```

### Example 2: Claim with Support Relationships

**Our JSON:**
```json
{
  "claim_id": "C001",
  "claim_text": "Crowdsourcing is efficient for large datasets",
  "supported_by_evidence": ["E001", "E002"]
}
```

**Potential mapping:**
```json
{
  "@context": {
    "claim": "https://micropublications.org/vocab#Claim",
    "supports": "https://micropublications.org/vocab#supports"
  },
  "@type": "claim",
  "@id": "C001",
  "claim_text": "Crowdsourcing is efficient for large datasets",
  "supports:supportedBy": ["E001", "E002"]
}
```

### Example 3: Consolidation Metadata with PROV-O (v2.3)

**Our JSON:**
```json
{
  "evidence_id": "E001",
  "consolidation_metadata": {
    "consolidation_performed": true,
    "source_items": ["P1_E001", "P1_E002", "P1_E003"],
    "consolidation_type": "phase_aggregation",
    "information_preserved": "lossy_granularity"
  }
}
```

**Potential PROV-O mapping:**
```json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#"
  },
  "@id": "E001",
  "prov:wasDerivedFrom": ["P1_E001", "P1_E002", "P1_E003"],
  "prov:qualifiedDerivation": {
    "@type": "prov:Derivation",
    "prov:hadActivity": "phase_aggregation",
    "custom:informationPreserved": "lossy_granularity"
  }
}
```

---

## Usage Notes

### During Schema Development

**When adding new fields:**
1. Add to schema
2. Document here with "Novel (empirical)" if no mapping found
3. Briefly explain why field exists
4. Continue development (don't block)

**When borrowing concepts:**
1. Note source schema
2. Document any adaptations
3. Map property if possible (exact/broader/narrower/related)
4. Continue development

### During Formalization

**Priority mappings:**
1. Core concepts (evidence, claim, method)
2. Structural relationships (supports, generated_by)
3. Provenance (PROV-O properties)
4. Novel contributions (document for publication)

**Lower priority:**
1. Extraction metadata (may not need formalization)
2. Quality flags (extraction-specific)
3. Controlled vocabularies (will emerge)

---

## Update History

**v1.1 (2025-10-18):**
- Updated to reflect schema v2.3 changes
- Added consolidation_metadata mappings (15 new property entries)
- Added related_evidence for analytical view pattern
- Added primary_function, claim_nature, quantitative_details mappings
- Enhanced declared_uncertainty structure documentation (4 new subfields)
- Added expected_uncertainty_missing to evidence
- Added "synthesis" to claim_role enum mapping
- Documented 6 new novel elements with formalization paths
- Updated structural elements section for v2.3 enhancements
- Added Example 3 showing consolidation_metadata PROV-O mapping

**v1.0 (2025-10-17):**
- Initial crosswalk based on schema v2.2
- Documented all core concepts and properties
- Flagged novel elements from empirical work
- Identified deferred mappings for formalization phase
- Established update process for ongoing development

---

## Next Steps

**Immediate:**
- Update this document as schema evolves (5 mins per change)
- Flag any new novel elements that emerge
- Document rationale for novel elements

**After 10 papers:**
- Refine controlled vocabularies
- Validate novel element utility
- Assess which elements need formalization

**Before formalization:**
- Complete all mappings
- Create formal alignment ontology
- Add JSON-LD @context
- Implement validation

---

**Document Status:** Living - update with each schema change  
**Maintenance:** 5 minutes per schema addition/modification  
**Review Trigger:** Before formalization phase begins