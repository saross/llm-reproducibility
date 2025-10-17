# Schema Crosswalk v1.0

**Version:** 1.0  
**Last Updated:** 2025-10-17  
**Purpose:** Map our schema elements to existing ontologies for future formalization  
**Schema Version:** v2.2

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
| **evidence.expected_information_missing** | Novel (empirical) | - | - | Assessment preparation, not in existing schemas |
| **evidence.implicit_evidence** | Novel (empirical) | Related | Professional judgment sources | Distinguishes unstated evidence |
| **evidence.provenance** | PROV-O | Exact | prov:wasGeneratedBy, prov:wasAttributedTo, prov:wasDerivedFrom | Low-hanging formalization |
| **claim.claim_type** | Novel (empirical) | Related | Multiple | EMPIRICAL/INTERPRETATION/METHODOLOGICAL/THEORETICAL |
| **claim.claim_role** | Novel (empirical) | Related | Hierarchy concepts | Four-level structure for assessment prioritization |
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
| **evidence.evidence_strength** | Multiple | Synthesized | legal:EvidenceWeight, cochrane:QualityOfEvidence | Hybrid from legal + systematic review frameworks |
| **implicit_argument.type** | Novel/Adapted | Related | walton:ArgumentationScheme | Type 1/2 = argument schemes; Type 3 = novel |
| **implicit_argument.type (disciplinary_assumption)** | Novel (empirical) | - | - | Type 3: meta-level, paradigmatic assumptions |
| **implicit_argument.argumentation_scheme** | Walton | Related | walton:ArgumentationScheme | Critical questions framework |
| **implicit_argument.coi_note** | Novel (empirical) | Related | Conflict of interest declarations | Author stake in findings |
| **supports_claims, supported_by_claims** | Multiple | Related | micropub:supports, aif:supports | Support relationships |
| **supported_by_evidence** | Multiple | Related | micropub:supportedBy | Evidence-claim links |

---

## Structural Elements

| Our Structure | Source Schema | Mapping Type | URI/Reference | Notes |
|---------------|---------------|--------------|---------------|-------|
| **Four-level hierarchy** (core → intermediate → supporting → evidence) | Novel (empirical) | - | - | Assessment prioritization structure |
| **Dual-layer uncertainty** (declared + expected) | Novel (empirical) | - | - | Author layer + assessor layer separation |
| **Extraction vs assessment separation** | repliCATS | Adapted | - | Phase 1 (identify) vs Phase 2 (evaluate) |
| **Project metadata separation** | Novel (empirical) | - | - | Context vs evidence distinction |
| **Two-pass workflow** (liberal → rationalization) | Novel (empirical) | - | - | Over-capture then consolidate strategy |

---

## Novel Elements (No Direct Mapping)

These elements emerged from empirical work and have no clear precedent in surveyed schemas:

| Element | Rationale | Future Formalization Path | Status |
|---------|-----------|---------------------------|--------|
| **project_metadata** | Separates context from evidence; emerged from Methods rationalization | Could map to dcterms:description or custom HASS vocab | Empirically validated |
| **claim_status (explicit/implicit)** | Tracks extraction artifact vs stated content | Consider prov:derivedByInference or custom property | Empirically validated |
| **generalization_from_single_case** | Abductive reasoning pattern in HASS research | Subtype of walton:ArgumentFromGeneralization | Empirically validated |
| **extraction_flags structure** | Quality tracking during extraction phase | May not need formalization (extraction metadata) | In use, refinement ongoing |
| **expected_information_missing** | Assessment preparation, not knowledge representation | May not need formalization (extraction metadata) | In use, refinement ongoing |
| **extraction_notes** | Extractor observations and concerns | May not need formalization (extraction metadata) | In use, refinement ongoing |
| **Dual-layer uncertainty** | Separates declared (author) from expected (assessor) | Novel contribution to research evaluation | Empirically validated |
| **Type 3 disciplinary assumptions** | Meta-level, paradigmatic, values-based foundations | Extension of implicit argument taxonomy | Newly formalized, testing in progress |
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