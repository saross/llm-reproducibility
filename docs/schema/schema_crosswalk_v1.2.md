# Schema Crosswalk v1.2

**Version:** 1.2  
**Last Updated:** 2025-10-27  
**Purpose:** Map our schema elements to existing ontologies for future formalization  
**Schema Version:** v2.5

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
| **implicit_argument** | Unstated assumptions/implications/disciplinary foundations | - | aif:I-node | - | walton:ArgumentationScheme | Type 1-5 taxonomy (3-5 are novel) |
| **method** | Research procedure/process (WHAT was done) | - | prov:Activity | - | researchobject:Process | Need HASS qualitative extensions |
| **research_design** | Strategic research framing (WHY framed this way) | - | - | - | CONSORT-SPI study design, SPIRIT protocol | Novel three-tier concept (v2.4) |
| **protocol** | Operational procedures (HOW specifically done) | protocols.io:Protocol | prov:Activity | - | researchobject:Workflow | Exact match for computational; need HASS extension |
| **project_metadata** | Context not supporting claims | - | dcterms:description | - | - | Novel distinction from extraction work |

---

## Properties

### v2.5 Hallucination Prevention (BREAKING CHANGES)

| Our Property | Source Schema | Mapping Type | URI/Reference | Notes |
|--------------|---------------|--------------|---------------|-------|
| **verbatim_quote** (REQUIRED for evidence/claims) | Novel (v2.5) | Related | doco:TextContent | Anti-hallucination measure; grounding in source text |
| **source_verification** | Novel (v2.5) | Related | prov:wasDerivedFrom | Pass 3 validation structure |
| **source_verification.location_verified** | Novel (v2.5) | Related | Validation frameworks | Confirms stated location exists |
| **source_verification.quote_verified** | Novel (v2.5) | Related | Validation frameworks | Confirms verbatim_quote or trigger_text found |
| **source_verification.content_aligned** | Novel (v2.5) | Related | Validation frameworks | Confirms content matches quote/inference reasonable |
| **source_verification.verification_notes** | Novel (v2.5) | - | - | Documentation of verification process |
| **source_verification.verified_by** | Novel (v2.5) | Related | prov:wasAttributedTo | Who performed verification (extractor/validator/manual) |
| **trigger_text** (REQUIRED for implicit) | Novel (v2.5) | Related | Annotation frameworks | Verbatim passages supporting inference |
| **trigger_locations** (REQUIRED for implicit) | Novel (v2.5) | Related | oa:Annotation | Parallel array to trigger_text |
| **inference_reasoning** (REQUIRED for implicit) | Novel (v2.5) | Related | Argumentation frameworks | Explains inference from triggers |

### v2.4 RDMAP Core Properties

| Our Property | Source Schema | Mapping Type | URI/Reference | Notes |
|--------------|---------------|--------------|---------------|-------|
| **research_design.design_id** | Novel (v2.4) | - | - | Strategic tier identifier pattern |
| **research_design.design_type** | Novel (v2.4) | Related | Multiple frameworks | Enum: research_question, hypothesis, theoretical_framework, study_design, scope_definition, positionality |
| **research_design.reasoning_approach** | Novel (v2.4) | Related | HPS epistemology | Inductive/abductive/deductive/mixed/unclear framework |
| **method.method_type** | Novel (v2.4) | Related | researchobject:Process | Enum: data_collection, sampling, analysis, quality_control, validation, temporal_framework |
| **protocol.protocol_type** | protocols.io | Exact | protocols.io:ProtocolType | Enum: recording, measurement, processing, sampling, validation, safety, ethics |
| **methodological_argument** (claim_type) | Novel (v2.4) | Related | micropub:Claim, CONSORT-SPI rationale | Claims that justify methodological choices |

### v2.4 Research Design Conditional Structures

| Our Property | Source Schema | Mapping Type | URI/Reference | Notes |
|--------------|---------------|--------------|---------------|-------|
| **research_question** | Qualitative preregistration | Exact | - | Emergent design acknowledgment |
| **hypothesis** | CONSORT, SPIRIT | Exact | - | Testable predictions with timing |
| **hypothesis.directionality** | Clinical trials | Exact | - | One-tailed/two-tailed/non-directional |
| **hypothesis.hypothesis_formulation_timing** | OSF existing data taxonomy | Related | - | Pre_data/during_data/post_data/unclear |
| **theoretical_framework** | Qualitative preregistration | Related | - | Framework name, paradigm, key concepts |
| **theoretical_framework.paradigm** | Qualitative research | Exact | - | Positivist/post-positivist/constructivist/interpretivist/critical/pragmatist |
| **study_design** | ClinicalTrials.gov | Adapted | ct.gov:StudyDesign | Extended for HASS with qualitative types |
| **scope** (spatial/temporal/thematic) | Novel (v2.4) | Related | dcterms:coverage | Research boundaries with justification |
| **positionality** | Qualitative preregistration | Exact | - | Researcher background, relationship, reflexivity |

### v2.4 Method Conditional Structures

| Our Property | Source Schema | Mapping Type | URI/Reference | Notes |
|--------------|---------------|--------------|---------------|-------|
| **data_collection_approach** | Novel/Multiple | Related | MDAR, CONSORT | Approach + domain-specific type |
| **sampling_strategy** | Multiple | Related | Clinical trials | Needs formalization as OWL ontology (critical gap) |
| **sampling_strategy.sampling_type** | Multiple | Related | - | Open vocab: random types, purposive types, convenience, theoretical, snowball, quota |
| **sampling_strategy.stopping_rule** | Clinical trials | Exact | SPIRIT | Predetermined_n, saturation, resource_constraint, access_constraint |
| **analysis_approach** | MDAR, CONSORT | Related | STATO (statistics) | Approach type, techniques, software, theoretical basis |
| **analysis_population** | SPIRIT, CONSORT | Exact | - | All_collected, quality_filtered, outliers_excluded, complete_cases_only |
| **analysis_population.exclusion_criteria** | CONSORT | Exact | - | Transparent exclusion documentation |
| **quality_control** | Novel (v2.4) | Related | Cochrane RoB | For HASS: triangulation, member checking, peer debriefing |
| **temporal_framework** | Novel (v2.4) | - | - | Field seasons, duration, frequency |
| **blinding** | CONSORT | Exact | - | None/single/double/triple/quadruple with who_blinded |
| **contingency_plans** | Preregistration | Related | protocols.io decision trees | IF-THEN structures with actually_triggered flag |
| **opportunistic_decisions** | Novel (v2.4) | - | - | Field condition adaptations (abductive research pattern) |

### v2.4 Protocol Conditional Structures

| Our Property | Source Schema | Mapping Type | URI/Reference | Notes |
|--------------|---------------|--------------|---------------|-------|
| **procedure.steps** | protocols.io | Exact | protocols.io:Step | Ordered steps with critical_for_replication flag |
| **procedure.decision_points** | protocols.io | Exact | - | Where choices made during execution |
| **tools** | protocols.io, MDAR | Exact | - | Equipment/software/platform with versions |
| **parameters** | protocols.io | Exact | - | Key-value pairs with units, ranges, criticality |
| **recording_standards** | MDAR | Exact | - | Format, precision, metadata captured, quality checks |
| **adaptation.adapted_from** | protocols.io | Related | prov:wasDerivedFrom | Protocol modifications documentation |
| **adaptation.opportunistic** | Novel (v2.4) | - | - | Field conditions forced change flag |
| **decision_rules** | Preregistration | Related | - | Conditional procedures (IF-THEN-rationale) |
| **ethics** | CONSORT-SPI Item 26 | Exact | - | Permissions, COI, community consultation, data sovereignty |
| **replicability_indicators** | Novel (v2.4) | Related | Cochrane RoB | Specificity/completeness/accessibility (flags, not scores) |

### v2.4 Cross-References (RDMAP)

| Our Property | Source Schema | Mapping Type | URI/Reference | Notes |
|--------------|---------------|--------------|---------------|-------|
| **research_design.enables_methods** | Novel (v2.4) | Related | prov:influenced | Simple string ID array pattern |
| **research_design.constrains_protocols** | Novel (v2.4) | Related | prov:influenced | Design-level constraints |
| **research_design.informs_claims** | Novel (v2.4) | Related | micropub:supports | Methodological argument claims |
| **method.implements_designs** | Novel (v2.4) | Related | prov:wasInfluencedBy | Bidirectional to enables_methods |
| **method.realized_through_protocols** | Novel (v2.4) | Related | prov:wasGeneratedBy | Method-protocol linkage |
| **method.validated_by_evidence** | Novel (v2.4) | Related | micropub:supportedBy | Evidence validating method choice |
| **method.justification_claim** | Novel (v2.4) | Related | micropub:supports | Link to methodological_argument claim |
| **protocol.implements_methods** | Novel (v2.4) | Related | prov:wasGeneratedBy | Bidirectional to realized_through_protocols |
| **protocol.produces_evidence** | Novel (v2.4) | Related | prov:wasGeneratedBy | Protocol outputs |
| **protocol.sub_protocols** | protocols.io | Exact | - | Hierarchical protocol nesting |
| **protocol.parent_protocol** | protocols.io | Exact | - | Inverse of sub_protocols |

### v2.3 & Earlier Properties (Carried Forward)

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
| **claim.claim_type** | Novel (empirical) | Related | Multiple | EMPIRICAL/INTERPRETATION/METHODOLOGICAL/THEORETICAL + methodological_argument (v2.4) |
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
| **implicit_argument.type** | Novel/Adapted | Related | walton:ArgumentationScheme | Type 1/2 = argument schemes; Type 3-5 = novel (v2.4 added 4-5) |
| **implicit_argument.type: design_assumption** | Novel (v2.4) | - | - | Type 4: Unstated assumptions underlying research design |
| **implicit_argument.type: methodological_assumption** | Novel (v2.4) | - | - | Type 5: Unstated assumptions underlying methods |
| **implicit_argument.type (disciplinary_assumption)** | Novel (empirical) | - | - | Type 3: Meta-level, paradigmatic assumptions |
| **implicit_argument.argumentation_scheme** | Walton | Related | walton:ArgumentationScheme | Critical questions framework |
| **implicit_argument.coi_note** | Novel (empirical) | Related | Conflict of interest declarations | Author stake in findings |
| **implicit_argument.consolidation_metadata** | Novel (v2.3) | Related | prov:wasDerivedFrom | Pass 2 rationalization provenance |
| **consolidation_metadata.consolidation_type** | Novel (v2.3, extended v2.4) | Related | prov:qualifiedDerivation | Taxonomy of consolidation operations (added design_rationale_synthesis, workflow_aggregation, protocol_specification in v2.4) |
| **consolidation_metadata.information_preserved** | Novel (v2.3) | Related | dcat:DataQuality | Tracks lossy vs lossless transformations |
| **consolidation_metadata.granularity_available** | Novel (v2.3) | - | - | Documents detail in source not extracted |
| **supports_claims, supported_by_claims** | Multiple | Related | micropub:supports, aif:supports | Support relationships |
| **supported_by_evidence** | Multiple | Related | micropub:supportedBy | Evidence-claim links |

---

## Structural Elements

| Our Structure | Source Schema | Mapping Type | URI/Reference | Notes |
|---------------|---------------|--------------|---------------|-------|
| **Four-level hierarchy** (core → intermediate → supporting → evidence) | Novel (empirical) | - | - | Assessment prioritization structure |
| **Three-tier RDMAP hierarchy** (Design → Methods → Protocols) | Preregistration schemas | Adapted | CONSORT-SPI, SPIRIT, TIDieR | Strategic → Tactical → Operational mapping |
| **Dual-layer uncertainty** (declared + expected) | Novel (empirical) | - | - | Author layer + assessor layer separation; **v2.3:** Enhanced with indicator, applies_to, bounds fields |
| **Extraction vs assessment separation** | Novel (methodological) | Related | Annotation workflows | Clear phase distinction with field-level marking |
| **Three-pass extraction workflow** | Novel (methodological, extended v2.4) | Related | PROV-O workflow patterns | Pass 1: liberal extraction; Pass 2: rationalization; **Pass 3 (v2.5):** source verification |
| **evidence_basis enumeration** | Observable source classification for extraction | Could inform prov:Entity subtypes | Empirically validated |
| **Reasoning approach framework** | HPS epistemology | Related | - | Inductive/abductive/deductive/mixed/unclear with self-documenting definitions |
| **Explicit/implicit status tracking** | Novel (empirical) | Related | prov:derivedByInference | All RDMAP objects have _status field (explicit/implicit) |
| **Implicit metadata structure** | Novel (v2.4) | - | - | Basis/transparency_gap/assessability_impact/reconstruction_confidence for RDMAP |

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

### method_type (v2.4 - controlled enum)

**Fixed categories:**
- data_collection
- sampling
- analysis
- quality_control
- validation
- temporal_framework

**Future mapping:** ResearchObject:Process + HASS qualitative extensions

### sampling_type (currently open vocabulary)

**Emerging categories:**
- **Probability:** simple_random, stratified_random, systematic_random, cluster
- **Non-probability:** purposive (various subtypes), convenience, theoretical, snowball, quota, judgmental
- **Complete:** total_collection, total_coverage, census

**Critical gap:** No formal ontology exists. **Formalization opportunity** for RDMAP.

### study_design_type (open vocabulary)

**Emerging categories:**
- **Fieldwork:** survey, excavation, ethnographic
- **Analytical:** comparative, longitudinal, case_study
- **Experimental:** experimental, quasi_experimental
- **Integration:** mixed_methods

**Future mapping:** Extend ClinicalTrials.gov taxonomy + qualitative research frameworks

---

## Novel Elements (No Direct Mapping)

### v2.5 Additions

| Element | Rationale | Future Formalization Path |
|---------|-----------|---------------------------|
| **verbatim_quote (REQUIRED)** | Hallucination prevention - ground extractions in source text | Map to doco:TextContent with provenance linking |
| **source_verification** | Pass 3 validation workflow - ensure extraction integrity | Map to PROV-O validation patterns |
| **trigger_text/locations/reasoning (REQUIRED for implicit)** | Make implicit inference traceable and verifiable | Extend annotation frameworks (Open Annotation) |

### v2.4 Additions (RDMAP)

| Element | Rationale | Future Formalization Path |
|---------|-----------|---------------------------|
| **Three-tier RDMAP hierarchy** | Separate strategic (WHY), tactical (WHAT), operational (HOW) | Extend preregistration frameworks; document as HASS pattern |
| **reasoning_approach framework** | HPS epistemology classification critical for HASS | Formalize as epistemology ontology extension |
| **methodological_argument** | Claims justifying method choices - distinct from empirical claims | Extend Micropublications:Claim with subtype |
| **Type 4: design_assumption** | Unstated assumptions underlying research design | Extend implicit_argument taxonomy |
| **Type 5: methodological_assumption** | Unstated assumptions underlying methods | Extend implicit_argument taxonomy |
| **opportunistic_decisions** | Field condition adaptations - abductive research pattern | Novel concept; document as HASS fieldwork pattern |
| **contingency_plans** | IF-THEN decision rules with actually_triggered tracking | Extend preregistration conditional procedures |
| **positionality** | Qualitative research reflexivity | Exact match to qualitative preregistration consensus |
| **temporal_framework** | Field seasons/duration - distinct from study design | Novel method type for longitudinal fieldwork |
| **analysis_population** | What data analyzed vs collected - exclusion transparency | Exact match to SPIRIT/CONSORT |
| **replicability_indicators** | Extraction-time flags (not assessment scores) | Novel separation of extraction vs assessment |

### v2.3 & Earlier Novel Elements (Carried Forward)

| Element | Rationale | Future Formalization Path |
|---------|-----------|---------------------------|
| **project_metadata** | Empirically identified - separates context from evidence | Could map to dcterms:description or custom HASS vocab |
| **claim_status (explicit/implicit)** | Empirically identified - extraction artifact tracking | Consider prov:derivedByInference or custom property |
| **generalization_from_single_case** | Empirically identified - abductive reasoning pattern | Subtype of walton:ArgumentFromGeneralization |
| **requires_professional_judgment** | Empirically identified - flags claims needing domain expertise | Related to walton:ExpertOpinionScheme |
| **boundary_ambiguous** | Empirically identified - extraction quality tracking | Extraction metadata, may not need formalization |
| **consolidation_metadata** | Empirically identified (v2.3) - Pass 2 rationalization traceability needed | Map to PROV-O qualified derivation pattern |
| **consolidation_metadata.consolidation_type** | Empirically identified (v2.3, extended v2.4) - taxonomy of consolidation operations | Custom vocabulary; could extend PROV-O derivation types |
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

## Framework Source Documentation

### v2.4 RDMAP Sources

**Primary frameworks borrowed from:**

1. **TIDieR Checklist (Hoffmann et al. 2014)** - 12-element intervention documentation
   - Brief Name, Why (rationale), What (Materials), What (Procedures), Who Provided, How (delivery), Where (setting), When/How Much, Tailoring, Modifications, How Well Planned (fidelity), How Well Actual
   - **Used for:** Expected information checklists in methods extraction

2. **CONSORT-SPI 2018 (Grant et al.)** - Social and Psychological Interventions extension
   - Item 26: Stakeholder involvement
   - Item 2b: Theory of change and mechanisms
   - Item 5: Implementation and fidelity
   - **Used for:** Ethics framework, community consultation, adaptation tracking

3. **SPIRIT 2025 (Chan et al.)** - Standard Protocol Items: Recommendations for Interventional Trials
   - Analysis population specifications (ITT, per-protocol, as-treated, modified ITT, complete case)
   - Schedule of assessments template
   - **Used for:** Analysis_population structure, temporal framework

4. **CONSORT-Outcomes 2022 (Butcher et al.)** - Outcome specification framework
   - Domain, Instrument, Metric, Aggregation, Time points, Reporter, Primary/Secondary designation
   - **Used for:** Expected information about measurement approaches

5. **Qualitative Preregistration Template (Haven & Van Grootel 2019)**
   - Research questions (not hypotheses), theoretical paradigm, purposive sampling, credibility strategies, positionality
   - **Used for:** Paradigm taxonomy, positionality structure, quality_control for qualitative work

6. **ClinicalTrials.gov controlled vocabularies**
   - Study design taxonomy, allocation methods, masking levels
   - **Used for:** Study design controlled vocabularies (adapted for HASS)

7. **OSF Preregistration existing data taxonomy**
   - Five-level timeline: prior to data creation, observation, accessing, analysis, post-preliminary analysis
   - **Used for:** Hypothesis formulation timing structure

8. **protocols.io schema patterns**
   - Step-by-step procedures, tool specifications, parameters, decision points
   - **Used for:** Protocol_object structure, tools array, parameters object

---

## Deferred Mappings (For Formalization Phase)

These will be addressed when moving to formal ontology:

- **Full PROV-O integration** - Complete provenance chains for all RDMAP objects
- **SPAR/DoCO document structure** - Section-level markup and citation typing
- **AIF formal argumentation** - Complete argument interchange format
- **Complete FAIR assessment** - Automated FAIR principle scoring
- **Nanopublication identifiers** - Immutable, versioned claim identifiers
- **Research Object workflows** - Complete computational provenance for RDMAP
- **OWL class definitions** - Formal logic and reasoning support
- **SHACL validation shapes** - RDF constraint validation
- **Sampling strategy ontology** - Critical gap identified; formalize probability/nonprobability taxonomy
- **HPS epistemology ontology** - Formalize reasoning approach framework
- **Fieldwork patterns ontology** - Opportunistic decisions, field adaptations

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
5. Develop SHACL validation shapes
6. Submit sampling strategy ontology to OBO Foundry (if pursuing formal semantic web)

**Timeline:** After schema stabilizes (minimal changes across 10 consecutive papers)

---

## Integration Examples

### Example 1: Evidence with Hallucination Prevention (v2.5)

**Our JSON:**
```json
{
  "evidence_id": "E001",
  "evidence_text": "125.8 person-hours of digitization",
  "evidence_basis": "direct_measurement",
  "verbatim_quote": "The digitization process required 125.8 person-hours",
  "location": {"section": "Results", "page": 5, "paragraph": 2},
  "source_verification": {
    "location_verified": true,
    "quote_verified": true,
    "content_aligned": true,
    "verified_by": "validator"
  }
}
```

**Potential JSON-LD with @context:**
```json
{
  "@context": {
    "evidence": "https://hass-credibility.org/vocab#Evidence",
    "prov": "http://www.w3.org/ns/prov#",
    "doco": "http://purl.org/spar/doco/"
  },
  "@type": "evidence",
  "@id": "E001",
  "evidence_text": "125.8 person-hours of digitization",
  "prov:wasGeneratedBy": "digitization_activity",
  "doco:TextContent": "The digitization process required 125.8 person-hours",
  "prov:wasValidatedBy": "validator_agent"
}
```

### Example 2: RDMAP Three-Tier Structure (v2.4)

**Our JSON:**
```json
{
  "research_design_id": "RD001",
  "design_text": "Comparative study of mobile data collection methods",
  "design_type": "study_design",
  "study_design": {
    "design_type": "comparative",
    "design_rationale": "Test mobile platform effectiveness"
  },
  "enables_methods": ["M003"]
},
{
  "method_id": "M003",
  "method_text": "Mobile platform (FAIMS) used for field data collection",
  "method_type": "data_collection",
  "implements_designs": ["RD001"],
  "realized_through_protocols": ["P023"]
},
{
  "protocol_id": "P023",
  "protocol_text": "FAIMS Mobile v2.6 configured for survey recording",
  "protocol_type": "recording",
  "implements_methods": ["M003"],
  "tools": [{
    "tool_name": "FAIMS Mobile",
    "version": "2.6",
    "tool_type": "software"
  }]
}
```

**Potential PROV-O mapping:**
```json
{
  "@context": {
    "prov": "http://www.w3.org/ns/prov#",
    "rdmap": "https://hass-credibility.org/rdmap#"
  },
  "research_design": {
    "@id": "RD001",
    "@type": "rdmap:ResearchDesign",
    "prov:influenced": ["M003"]
  },
  "method": {
    "@id": "M003",
    "@type": ["prov:Activity", "rdmap:Method"],
    "prov:wasInfluencedBy": "RD001",
    "prov:wasGeneratedBy": ["P023"]
  },
  "protocol": {
    "@id": "P023",
    "@type": ["prov:Activity", "rdmap:Protocol", "protocols.io:Protocol"],
    "prov:generated": "M003",
    "prov:used": {
      "@type": "rdmap:Tool",
      "tool_name": "FAIMS Mobile",
      "version": "2.6"
    }
  }
}
```

### Example 3: Implicit Argument with Triggers (v2.5)

**Our JSON:**
```json
{
  "implicit_argument_id": "IA004",
  "type": "methodological_assumption",
  "assumption_text": "Platform familiarity improves data quality",
  "verbatim_quote": null,
  "trigger_text": [
    "Team members had extensive FAIMS training",
    "Platform was familiar from previous seasons"
  ],
  "trigger_locations": [
    {"section": "Methods", "page": 4, "paragraph": 2},
    {"section": "Methods", "page": 4, "paragraph": 5}
  ],
  "inference_reasoning": "Authors emphasize training and familiarity without explicitly stating the assumption that this improves data quality, but this is the implicit rationale for the methodological choice",
  "implicit_metadata": {
    "basis": "mentioned_undocumented",
    "transparency_gap": "Assumption about familiarity-quality link not stated",
    "assessability_impact": "Prevents assessment of whether assumption is warranted",
    "reconstruction_confidence": "high"
  },
  "source_verification": {
    "location_verified": true,
    "quote_verified": true,
    "content_aligned": true,
    "verification_notes": "Both trigger passages found; inference reasonable",
    "verified_by": "validator"
  }
}
```

---

## Usage Notes

### During Schema Development

**When adding new fields:**
1. Add to schema
2. Document here with "Novel (empirical)" or "Novel (vX.X)" if no mapping found
3. Briefly explain why field exists
4. Note which framework version introduced it
5. Continue development (don't block)

**When borrowing concepts:**
1. Note source schema
2. Document any adaptations
3. Map property if possible (exact/broader/narrower/related)
4. Reference specific framework documents (e.g., "TIDieR 2014", "CONSORT-SPI Item 26")
5. Continue development

### During Formalization

**Priority mappings:**
1. Core concepts (evidence, claim, method, research_design, protocol)
2. Structural relationships (supports, generated_by, enables, implements)
3. Provenance (PROV-O properties)
4. Novel contributions (document for publication)

**Lower priority:**
1. Extraction metadata (may not need formalization)
2. Quality flags (extraction-specific)
3. Controlled vocabularies (will emerge)

---

## Update History

**v1.2 (2025-10-27):**
- **MAJOR UPDATE:** Documented schema v2.5 (hallucination prevention) and v2.4 (RDMAP)
- Added RDMAP core objects: research_design, method, protocol with all conditional structures
- Added v2.5 hallucination prevention: verbatim_quote (REQUIRED), source_verification, trigger_text/locations/reasoning
- Documented reasoning_approach framework (inductive/abductive/deductive/mixed)
- Added methodological_argument claim type
- Added Type 4 (design_assumption) and Type 5 (methodological_assumption) to implicit arguments
- Extended consolidation_type taxonomy with RDMAP operations (design_rationale_synthesis, workflow_aggregation, protocol_specification)
- Added comprehensive RDMAP conditional structures (25+ new properties)
- Added cross-reference mappings for three-tier hierarchy
- Added Framework Source Documentation section with specific citations
- Updated Novel Elements section with v2.4 and v2.5 additions
- Added three new integration examples
- Documented explicit/implicit status tracking for RDMAP objects
- Added implicit_metadata structure for RDMAP
- Updated Structural Elements with three-tier hierarchy and three-pass workflow

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
- Track RDMAP extraction patterns as they emerge

**After 10 papers:**
- Refine controlled vocabularies (sampling_type, study_design_type)
- Validate novel element utility (opportunistic_decisions, reasoning_approach)
- Assess which RDMAP elements need formalization priority
- Consider formalization of sampling strategy ontology (critical gap)

**Before formalization:**
- Complete all mappings
- Create formal alignment ontology
- Add JSON-LD @context with RDMAP namespace
- Implement validation for three-tier hierarchy
- Submit sampling strategy ontology (if pursuing OBO Foundry)
- Publish RDMAP pattern documentation for HASS community

---

**Document Status:** Living - update with each schema change  
**Maintenance:** 5 minutes per schema addition/modification  
**Review Trigger:** Before formalization phase begins  
**Critical for:** Publication documenting novel contributions and framework sources
