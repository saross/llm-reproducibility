Schema Improvement Plan: Pragmatic Iteration v1.0
Created: 2025-10-17
Status: Active Development
Current Schema Version: v2.1
Strategic Approach: Pragmatic iteration → formalization (with low-hanging formalization groundwork)

Strategic Context
Core Principles
Pragmatic iteration now - functional improvements based on empirical findings
Don't block formalization - avoid architectural decisions that complicate later semantic integration
Low-hanging formalization - capture obvious mappings/structure without extraordinary effort
Crosswalk documentation - map schema elements to existing ontologies as we go
Empirically-driven - let corpus analysis drive taxonomy development, not theory
Domain Scope (Initial Papers)
Digital archaeology
Palaeoenvironments
Archaeogenetics
Statistically modelled heritage management
Large-scale/long-term landscape archaeology outcomes
Common characteristics: Mixed methods but structured; quantitative + qualitative; computational approaches

Scheduled Reviews & Decision Points
These reviews are scheduled at specific triggers - check regularly:

☐ Evidence credibility extension (Phase 1.4) - After 1-2 test extractions
☐ Controlled vocabulary completeness review (Phase 5.4) - After 10 papers
☐ Implicit argument intensity review (Phase 5.5) - After 10 papers
☐ Schema stabilization assessment (Phase 5) - After minimal changes across 3 consecutive papers
Phase 1: Operationalize Credibility Assessment
Timeline: Immediate - Next 2 weeks
Goal: Make credibility assessment actionable with proven frameworks

☐ 1.1 Integrate adapted repliCATS credibility signals
Task: Add credibility_assessment object to claims schema

json
"credibility_assessment": {
  "transparency": {
    "score": "high|moderate|low|unclear",
    "rationale": "string - why this score",
    "missing_elements": ["array of specific gaps"]
  },
  "plausibility": {
    "score": "high|moderate|low|unclear", 
    "rationale": "string - domain knowledge consistency",
    "red_flags": ["array of concerns"]
  },
  "validity": {
    "score": "high|moderate|low|unclear",
    "rationale": "string - methods appropriate to question",
    "threats": ["array - e.g., generalization_from_single_case"]
  },
  "robustness": {
    "score": "high|moderate|low|unclear",
    "rationale": "string - sensitivity to assumptions",
    "vulnerabilities": ["array of weak points"]
  },
  "comprehensibility": {
    "score": "high|moderate|low|unclear",
    "rationale": "string - clarity of methods/claims"
  },
  "replicability": {
    "score": "high|moderate|low|unclear",
    "rationale": "string - sufficient detail to replicate",
    "missing_for_replication": ["array of gaps"]
  },
  "generalizability": {
    "score": "high|moderate|low|unclear",
    "rationale": "string - scope appropriately bounded",
    "boundary_issues": ["array of overgeneralization concerns"]
  }
}
Rationale: repliCATS framework proven at 61-84% accuracy. Existing flags (generalization_from_single_case, requires_professional_judgment) map directly to validity/robustness threats.

Crosswalk note: Maps to repliCATS:CredibilitySignal (adapted for HASS contexts)

☐ 1.2 Add evidence strength taxonomy
Task: Expand evidence object with strength assessment

json
"evidence_strength": {
  "assessment": "strong|moderate|weak|insufficient",
  "basis": "direct_measurement|statistical_significance|triangulation|professional_judgment|single_observation|author_assertion",
  "limitations": ["array of known weaknesses"],
  "triangulated_with": ["array of evidence IDs that corroborate"]
}
Sources:

Legal frameworks (direct/circumstantial evidence distinctions)
repliCATS strength markers
Your empirical findings on professional judgment vs observation
☐ 1.4 Extend credibility assessment to evidence (HIGH PRIORITY)
Trigger: After 1-2 more test extractions AND when beginning assessment phase

Task: Add parallel credibility assessment structure to evidence objects (assessment-time only, like claim assessments)

json
"evidence_credibility": {
  "_assessment_status": "not_yet_assessed",
  "data_quality": {
    "score": "high|moderate|low|unclear|not_assessed",
    "rationale": "measurement precision, calibration, error handling",
    "concerns": []
  },
  "source_reliability": {
    "score": "high|moderate|low|unclear|not_assessed",
    "rationale": "source documentation, chain of custody, potential bias",
    "concerns": []
  },
  "transparency": {
    "score": "high|moderate|low|unclear|not_assessed",
    "rationale": "sufficient documentation of collection/processing",
    "missing_elements": []
  }
}
Decision point:

During extraction: Monitor whether evidence quality issues are being surfaced through claim assessment
When starting assessment phase: If evidence-level issues systematic, implement this extension
Keep extraction workflow focused on identification, not evaluation
Note: Like claim credibility assessment, this is ASSESSMENT-TIME work, not populated during extraction pass.

Task: Create consolidation_rules.md documenting Methods rationalization findings

Structure:

markdown
# Consolidation Rules v1.0

## When to LUMP (Consolidate)
1. Multiple observations specify the same entity
2. Multiple interpretations form single compound claim
3. Technical features jointly support one capability
4. Process steps form single workflow

## When to SPLIT (Keep Separate)  
1. Different observations support different claims
2. Claims have different assessment requirements
3. Evidence from different sources/methods
4. Alternative limitations address different concerns

## Acid Test
"Would I assess credibility of these statements TOGETHER or SEPARATELY?"
Crosswalk note: Maps to SKOS broader/narrower relationships when formalized

Phase 2: Evidence & Methods Taxonomy
Timeline: Weeks 3-4
Goal: Develop controlled vocabularies from corpus analysis

☐ 2.1 Evidence type taxonomy for archaeology/HASS
Task: Add refined evidence categorization (start controlled, expand iteratively)

IMPORTANT: Use controlled vocabularies SPARINGLY - only where confident. Expect incompleteness until more testing. Review after 10 papers (see Phase 5.4).

json
"evidence_type_refined": {
  "category": "primary_source|secondary_source|derived|synthetic",
  "subtype": "archaeological_material|archival_document|statistical_output|geospatial_data|radiometric_date|stratigraphic_sequence|comparative_dataset|expert_assessment|observational_record",
  "provenance_chain": ["E001", "E005"],
  "transformation_applied": "string - how raw data became this evidence"
}
Approach:

Start with high-level categories from your test papers
Let subtypes emerge from next 5-10 extractions
Add new subtypes as encountered, don't force premature taxonomy
Accept that vocabulary will be incomplete initially
Crosswalk note:

category → prov:Entity (broader)
provenance_chain → prov:wasDerivedFrom (exact)
transformation_applied → prov:Activity (related)
☐ 2.2 Methods taxonomy for mixed-methods archaeology
Task: Expand from free-text to emerging structured taxonomy

IMPORTANT: Sparse controlled vocabulary - expect expansion. Review after 10 papers (see Phase 5.4).

json
"method_detail": {
  "category": "quantitative|qualitative|computational|mixed",
  "specific_method": "radiocarbon_dating|GIS_analysis|bayesian_modeling|survey|excavation|statistical_modeling|crowdsourcing|stylistic_analysis|comparative_analysis",
  "quality_indicators": {
    "sample_adequacy": "adequate|limited|insufficient|unclear",
    "systematic_bias_concerns": ["array of identified biases"],
    "reproducibility_level": "fully_specified|partially_specified|underspecified",
    "validation_performed": "yes|partial|no",
    "calibration_documented": "yes|partial|no"
  }
}
Approach: Let archaeology-specific methods emerge naturally from corpus

Crosswalk note:

Maps to ResearchObject:Process + HASS qualitative extensions
quality_indicators → cochrane:RiskOfBias (adapted for non-RCT contexts)
Phase 3: Low-Hanging Formalization Groundwork
Timeline: Weeks 3-4 (concurrent with Phase 2)
Goal: Capture obvious semantic structure without extra extraction work

☐ 3.1 Add basic PROV-O structure to evidence/methods
Task: Make existing implicit relationships explicit

json
"provenance": {
  "entity_id": "E001",
  "generated_by": "M003",
  "attributed_to": "staff_geospatial_team|author_observation|instrument_X",
  "derived_from": ["source_maps_1920", "E005"],
  "generation_time": "2018-06-15",
  "generation_context": "field_season_2018"
}
Why low-hanging: You already track these relationships informally. Making them explicit = zero extra extraction work, enables clean PROV-O export later.

Crosswalk note: Direct PROV-O mappings:

entity_id → prov:Entity
generated_by → prov:wasGeneratedBy → prov:Activity
attributed_to → prov:wasAttributedTo → prov:Agent
derived_from → prov:wasDerivedFrom → prov:Entity
☐ 3.2 Add argument scheme references to implicit_arguments
Task: Link to Walton argumentation schemes where applicable

json
"argumentation_scheme": {
  "walton_scheme": "expert_opinion|sign|cause_to_effect|analogy|generalization|consequence|precedent|none",
  "scheme_premises": ["array of required premises for this scheme"],
  "critical_questions": ["Is expert qualified?", "Is domain relevant?", "Are experts consistent?"],
  "critical_question_answers": {
    "Is expert qualified?": "yes|no|unclear - with rationale"
  }
}
Why pragmatic: Your requires_professional_judgment flags are already implicit expert opinion schemes. Making this explicit enables critical question framework at zero additional cost.

Crosswalk note:

Maps to walton:ArgumentationScheme (related)
Enables integration with AIF (Argument Interchange Format) later
Phase 4: Crosswalk Documentation
Timeline: Ongoing (5 mins per schema addition)
Goal: Map elements to existing ontologies as we develop

☐ 4.1 Create schema_crosswalk.md
Task: Living document tracking all mappings

Template structure:

markdown
# Schema Crosswalk v1.0
Last updated: YYYY-MM-DD

## Core Concepts

| Our Term | Definition | Exact Match | Broader | Narrower | Related | Notes |
|----------|------------|-------------|---------|----------|---------|-------|
| evidence | Raw observations/measurements | - | prov:Entity | micropub:Statement | doco:Result | Consider evidence types |
| claim | Interpretation requiring support | micropub:Claim | - | - | aif:I-node | Core assertion |
| implicit_argument | Unstated assumption/implication | - | aif:I-node | - | walton:ArgumentationScheme | Type 1/2/3 taxonomy |
| method | Research procedure/process | - | prov:Activity | - | researchobject:Process | Need HASS extension |

## Properties

| Our Property | Source Schema | Mapping Type | URI/Reference | Notes |
|--------------|---------------|--------------|---------------|-------|
| generalization_from_single_case | Novel (empirical) | - | - | Consider walton:ArgumentFromGeneralization |
| requires_professional_judgment | Novel (empirical) | Related | walton:ExpertOpinionScheme | Maps to expert opinion pattern |
| evidence.provenance.generated_by | PROV-O | Exact | prov:wasGeneratedBy | Direct mapping |
| claim.credibility_assessment | repliCATS | Adapted | replicats:CredibilitySignal | 7-signal framework |
| evidence.strength | Multiple | Synthesized | legal:EvidenceWeight, cochrane:QualityOfEvidence | Hybrid from legal + systematic review |

## Novel Elements (No Direct Mapping)

| Element | Rationale | Future Formalization Path |
|---------|-----------|---------------------------|
| project_metadata | Empirically identified - separates context from evidence | Could map to dcterms:description or custom HASS vocab |
| claim_status (explicit/implicit) | Empirically identified - extraction artifact tracking | Consider prov:derivedByInference or custom property |
| generalization_from_single_case | Empirically identified - abductive reasoning pattern | Subtype of walton:ArgumentFromGeneralization |
☐ 4.2 Update crosswalk with each schema change
Process: When adding any new field/object:

Check survey document for similar concepts (5 mins)
Add row to crosswalk with mapping type (exact/broader/narrower/related/novel)
Flag "needs investigation" if uncertain
Move on (don't get stuck researching obscure ontologies)
Phase 5: Empirically-Driven Refinement
Timeline: After 5-10 more paper extractions
Goal: Replace theoretical structures with corpus-validated ones

☐ 5.1 Refine expected_information_checklists
Current state: Generic theoretical checklists
Target state: Domain-specific empirical checklists

Process:

Track what's ACTUALLY missing across 5-10 archaeology papers
Pattern analysis:
What's consistently missing in radiocarbon claims? (calibration curves? lab protocols? sample context?)
What's missing in GIS-based claims? (projections? resolution? accuracy assessment?)
What's missing in statistical models? (priors? sensitivity? validation?)
What's missing in survey-based claims? (sampling strategy? coverage? bias assessment?)
Deliverable: Domain-specific checklists replacing generic ones

json
"expected_information_checklists": {
  "radiocarbon_date_claims": [
    "calibration_curve_specified",
    "lab_and_sample_id",
    "material_dated",
    "stratigraphic_context",
    "pretreatment_protocol",
    "error_margins_justified"
  ],
  "gis_based_spatial_claims": [
    "projection_system",
    "spatial_resolution_or_scale",
    "accuracy_assessment_performed",
    "data_sources_documented",
    "processing_steps_reproducible"
  ]
  // etc - let corpus drive these
}
☐ 5.2 Develop credibility signal thresholds
Current state: Score labels (high/moderate/low) without clear thresholds
Target state: Empirical rubrics for scoring

Process after 50+ scored claims:

When does "moderate" transparency → "low"? (missing 1 key element? 2? 3?)
What combination of red flags drops validity from high → moderate?
Which missing checklist elements matter most for replicability?
Do certain evidence strength assessments cluster with certain credibility scores?
Deliverable: Scoring rubrics

markdown
## Transparency Scoring Rubric (Empirical - after 50+ claims)

**High**: All key methodological elements present; minor details may be missing
**Moderate**: Core methodology clear but missing 1-2 elements needed for full replication
**Low**: Missing 3+ key elements; significant gaps in methodological reporting
**Unclear**: Insufficient information to assess transparency level

### Key elements by claim type:
- Radiocarbon claims: [list derived from corpus analysis]
- GIS claims: [list derived from corpus analysis]
- Statistical model claims: [list derived from corpus analysis]
☐ 5.3 Validate consolidation heuristics
Process: After 5 more sections extracted

Track all consolidation decisions
Identify patterns: which heuristic applied most often?
Find edge cases: where did heuristics fail or conflict?
Refine rules based on actual ambiguities encountered
☐ 5.4 Review controlled vocabulary completeness
Trigger: After 10 paper extractions

Process:

What percentage of evidence types fit existing categories?
What percentage of methods fit existing categories?
Are new subtypes stabilizing or still proliferating?
Which free-text fields should become controlled vocabularies?
Deliverable: Updated controlled vocabularies + documented gaps

☐ 5.5 Review implicit argument extraction intensity
Trigger: After 10 paper extractions

Process:

Are we missing important Type 2 arguments consistently?
Is Type 3 formalization working as expected?
False positive rate acceptable?
Should extraction become more liberal or stay conservative?
Deliverable: Updated extraction guidelines + prompt refinements

Scope Management: What NOT to Do
Avoid these temptations (wait for later phases):

❌ Cross-document claim tracking
Why not yet: Need 20+ papers before patterns emerge
When: After corpus reaches 20+ papers, then design tracking infrastructure
❌ Peer review/validation workflow modeling
Why not yet: Not in scope for extraction; separate research question
When: If/when you pivot to studying peer review process itself
❌ Full FAIR assessment automation
Why not yet: Requires formal ontology infrastructure + reasoning tools
When: Formalization phase; can be automated once semantic layer exists
❌ Complete methods ontology
Why not yet: Can't predict full taxonomy needs from 1 test paper
When: Let it emerge organically from corpus analysis (Phase 5)
❌ Formal OWL class definitions
Why not yet: Premature; wait for stable schema + crosswalk completion
When: Formalization phase, after pragmatic iteration stabilizes
❌ Nanopublication infrastructure
Why not yet: Requires formal identifiers, versioning, immutability infrastructure
When: Future interoperability phase; not needed for initial extraction
❌ Cross-system API integrations
Why not yet: Schema still evolving; APIs would require constant updates
When: After schema stabilization + broader adoption
Key Decisions Needed
Decision 1: Credibility assessment location ✅ DECIDED
Decision: Start with claims only, extend to evidence after 1-2 more test extractions
Rationale: Evidence quality issues will surface through claim assessment. Priority is proving the credibility framework works before expanding scope.
Action: ☐ Add evidence credibility extension to Phase 1 checklist (high priority after initial test)
Decision 2: Controlled vocabulary timing ✅ DECIDED
Decision: Hybrid approach with sparse controlled vocabularies
Implementation:
Use controlled lists ONLY where confident (high-level categories)
Expect incompleteness until more testing done
Free-text for subtypes until patterns clear
Let domain terms emerge naturally
Action: ☐ Add controlled vocabulary review to Phase 5 checklist
Decision 3: Implicit argument extraction intensity ✅ DECIDED
Decision: Conservative on Type 2, formalize Type 3, review after more testing
Rationale: Calibration showed 93% Type 2 accuracy with conservative approach. Can loosen later if missing important patterns.
Actions:
☐ Formalize Type 3 (disciplinary assumptions) extraction rules in prompt
☐ Add implicit argument intensity review to Phase 5 checklist
Immediate Action Items (This Week)
✅ Priority 1: Schema v2.2 with assessment structure (COMPLETED 2025-10-17)
✅ Added credibility_assessment object to claim definition (unpopulated during extraction)
✅ Added evidence_strength placeholder to evidence definition (assessment-time)
✅ Enhanced extraction-time fields: evidence_basis, extraction_flags, expected_information_missing
✅ Clear separation: extraction-time vs assessment-time fields
✅ Updated schema version + changelog to v2.2
✅ Added workflow_notes to track extraction/assessment completion
✅ Priority 2: Update extraction prompt with empirical improvements (COMPLETED 2025-10-17)
✅ Added 4 principles from Methods rationalization (~125 words)
✅ Professional judgment boundary (claims vs evidence)
✅ Evidence must support claims rule
✅ Single-case generalization pattern
✅ Track record = context guidance
✅ Formalized Type 3 extraction with distinguishing criteria
✅ Created extraction_prompt_v2.2 (unified version - committed to git)
✅ Priority 3: Split prompt into multi-stage workflow (COMPLETED 2025-10-17)
✅ Created extraction_prompt_pass1_v2.2.md (Liberal extraction with over-capture strategy)
✅ Created extraction_prompt_pass2_v2.2.md (Rationalization with consolidation rules)
✅ Pass 1: Focus on comprehensive capture, accept over-extraction
✅ Pass 2: Consolidate, correct boundaries, verify relationships
✅ Included lumping/splitting heuristics and change log format
Status: Ready for next extraction test using two-pass workflow

☐ Priority 4: Document extraction vs assessment workflow
Create extraction_assessment_workflow_v1.md
Clarify what gets populated when
Prevent scope creep during extraction phase
Target: Complete before assessment phase begins
☐ Priority 5: Create consolidation rules reference
Optional standalone consolidation_rules_v1.md for quick reference
Already integrated into Pass 2 prompt, but standalone doc may be useful
Target: If needed after testing Pass 2 prompt
☐ Priority 6: Start crosswalk document
Create schema_crosswalk.md with template structure
Document all v2.2 elements with known mappings
Flag novel elements from empirical work
Target: Start this week, ongoing maintenance
Success Criteria
Phase 1 Complete When:
✅ Credibility assessment structure added to schema (unpopulated during extraction)
✅ Extraction-time vs assessment-time fields clearly separated
✅ Two-pass workflow prompts created (Pass 1: Liberal extraction, Pass 2: Rationalization)
☐ Two-pass workflow tested on one section
☐ Extraction/assessment workflow documented
☐ Consolidation effectiveness measured
☐ Decision made: Extend credibility assessment to evidence or wait (after 1-2 tests)
Status: Implementation complete, ready for testing

Phase 2 Complete When:
☐ Evidence type taxonomy covers 90%+ of encountered evidence
☐ Methods taxonomy covers 90%+ of encountered methods
☐ Quality indicators identify gaps in 5+ papers
Phase 3 Complete When:
☐ Provenance structure applied throughout one full paper
☐ Argument schemes assigned to 80%+ of implicit arguments where applicable
☐ No additional extraction burden vs current approach
Phase 4 Complete When:
☐ Crosswalk document covers all schema elements
☐ 80%+ of properties mapped to existing ontologies (exact/broader/related)
☐ Novel elements justified with empirical rationale
Phase 5 Complete When:
☐ Domain-specific checklists replace generic ones
☐ Credibility scoring rubrics based on 50+ claim sample
☐ Consolidation heuristics validated across 5+ papers
☐ Controlled vocabulary review completed (after 10 papers)
☐ Implicit argument intensity review completed (after 10 papers)
☐ Schema stabilized (minimal changes across 3 consecutive papers)
Notes & Observations
Add empirical observations here as you work:

2025-10-17: Schema v2.2 - Assessment Structure Added
Decision: Separated extraction-time vs assessment-time workflow after questioning whether credibility assessment should be populated during extraction.

Rationale:

Extraction = identifying and structuring content (what's there)
Assessment = evaluating credibility/quality (how good is it)
repliCATS model explicitly separates these phases
Prevents scope creep during extraction
Assessment requires domain expertise and scoring rubrics (not yet developed)
Implementation:

Added credibility_assessment structure to claims (defaults to "not_yet_assessed")
Added evidence_strength placeholder to evidence (assessment-time)
Enhanced extraction-time observability: evidence_basis, extraction_flags, expected_information_missing
Clear comment markers in schema distinguish phases
Impact:

Extraction workflow stays focused on identification
Schema is assessment-ready when we get there
Prevents confusion about current task scope
Enables iterative assessment protocol development separate from extraction refinement
Next actions: Document workflow, create consolidation rules, start crosswalk.

2025-10-17: Prompt v2.2 - Empirical Improvements + Type 3 Formalization
What was added:

Four empirical principles from Methods rationalization (~125 words total):
Professional judgment boundary (claims vs evidence)
Evidence must support claims rule
Single-case generalization pattern detection
Track record = context (not evidence)
Type 3 distinguishing criteria:
Paradigmatic vs specific assumptions
Foundational vs testable links
Values-based vs causal predictions
Meta-level vs argument-level
Clear decision framework: "Type 2 = specific causal link; Type 3 = foundational principle"
Rationale:

Four principles emerged from manual Methods section rationalization
Solved real extraction problems (over-extraction, boundary ambiguity, missing implicit content)
Type 3 criteria needed because examples alone insufficient for reliable classification
Conservative approach: purely additive, can't degrade existing performance
Impact:

Extraction should better separate context from evidence
Single-case generalizations will be flagged systematically
Professional judgment properly classified as claims
Type 3 extraction should be more consistent and reliable
2025-10-17: Prompt Split into Two-Pass Workflow
What was created:

extraction_prompt_pass1_v2.2.md - Liberal extraction with over-capture strategy
extraction_prompt_pass2_v2.2.md - Rationalization with consolidation rules
Architecture:

Pass 1: Comprehensive capture, accept 40-50% over-extraction
Philosophy: "When uncertain, INCLUDE IT"
Preserve granularity for Pass 2
Focus on not missing anything
Pass 2: Consolidate and refine
Operations: REMOVE, CONSOLIDATE, SPLIT, RECLASSIFY, ADD, VERIFY
Lumping/splitting heuristics from Methods rationalization
Change log for transparency
Target 15-20% reduction from Pass 1
Rationale:

Liberal extraction (Pass 1) + systematic consolidation (Pass 2) more reliable than perfect extraction in single pass
Easier to consolidate than to discover missed items
Enables empirical measurement of extraction vs rationalization effectiveness
Separates comprehensive capture from quality refinement
Key features:

Acid test: "Assess together or separately?"
Category-specific consolidation patterns (maps, platform features, participant data, validation)
When to lump vs split decision framework
Change log format for documenting operations
Quality criteria for each pass
Status: Ready for testing on next section extraction (Results or Discussion)

Next: Run two-pass workflow test, measure metrics (precision, recall, boundary accuracy, consolidation quality)

Next Review Date: [Set after two-pass test complete]
Document Status: Living - update as you progress

