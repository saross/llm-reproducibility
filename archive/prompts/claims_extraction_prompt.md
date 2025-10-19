Claims Extraction Prompt v2.2
Version: 2.2
Last Updated: 2025-10-17
Changes from v2.1: Added 4 empirical principles from Methods section rationalization (~125 words total)

Your Task
Extract evidence, claims, and implicit arguments from a research paper section using the provided JSON schema. The goal is to create a structured representation that enables systematic credibility assessment.

Core Extraction Principles
1. Evidence vs. Claims Distinction
EVIDENCE = Raw observations, measurements, or data that require minimal interpretation

Direct measurements (e.g., "125.8 person-hours")
Observations (e.g., "12 students owned smartphones")
Data points (e.g., "95.7% accuracy")
Captured verbatim from the paper
Someone could verify by checking the source
CLAIMS = Assertions that interpret, frame, or generalize from evidence

Require reasoning or expertise to assess
Make inferences beyond direct observation
Involve framing or definitional choices
Connect evidence to broader patterns
Professional Judgment Boundary: Statements requiring expertise to assess (e.g., "these maps are accurate") are CLAIMS supported by implicit professional judgment, not evidence. Extract as INTERPRETATION claims, not observations.

2. Evidence Must Support Claims
Extract observations only if they support specific claims. Context that doesn't support claims → project_metadata.

Test question: "Would removing this item cause a claim to lose evidential support?"

If YES → Evidence
If NO → Project metadata (timeline, location, resources, track record)
Track Record = Context, Not Evidence: "Method X worked before" justifies attempting the approach but doesn't support current project claims. Move to project_metadata, not evidence.

3. Uncertainty Tracking (Dual Layer)
Author Layer (Declared): What the paper explicitly states

Statistical ranges (±)
Confidence intervals
Hedging language ("approximately," "roughly," "around")
Stylistic ranges ("10-20 minutes")
Assessor Layer (Expected): What we expect to see but might be missing

For measurements: precision, error margins, sample size
For estimates: bounded ranges, confidence basis
For comparisons: what was held constant, fairness justification
Use expected_information_checklists to identify gaps
4. Hierarchical Organization (Four Levels)
Classify each claim by its role in the argument:

1. CORE (5-10 claims) - Main thesis arguments

The central conclusions the paper seeks to establish
Highest assessment priority
Example: "Crowdsourcing is suitable for datasets of 10,000-60,000 features"
2. INTERMEDIATE (10-15 claims) - Major supporting arguments

Build toward core claims
Substantial interpretations that support the thesis
Example: "The approach yields 190 features per staff-hour"
3. SUPPORTING (15-25 claims) - Specific findings and interpretations

Detailed results and analyses
Direct support for intermediate claims
Example: "In 2017, 54 seconds average per feature"
4. EVIDENCE (30-50 items) - Observations and measurements

Raw data points
Direct observations
Example: "125.8 person-hours of digitization work"
Additional roles:

BACKGROUND - Context from literature (assessed via citations, not paper's evidence)
METHODOLOGICAL - About methods (assessed for transparency and replicability)
TRANSITIONAL - Narrative scaffolding (low priority)
5. Implicit Arguments
Extract unstated reasoning for HIGH-PRIORITY claims only:

TYPE 1: Logical Implications (extract these)

Direct inferences the paper expects readers to make
Example: "X is 3x faster than Y" → [implicit: "X is more efficient"]
TYPE 2: Unstated Assumptions (extract these)

Essential assumptions never stated
Bridge claims that link evidence to conclusions
Specific causal links or predictions needed for THIS argument
Example: "Students prefer touch-screens" → [implicit: "Preference affects performance in this context"]
Example: "Ease of learning leads to sustained productivity" (specific prediction)
TYPE 3: Deep Disciplinary Assumptions (extract and label clearly)

Distinguishing criteria: Type 3 assumptions are:
Paradigmatic: Frame entire research programs, not just this paper's argument
Foundational: Taken as given within the discipline (rarely questioned or tested)
Values-based: Often express what the discipline values or prioritizes
Meta-level: About how research should be done, not specific predictions
When to use Type 3 vs Type 2:
Type 2: "This specific thing causes this specific outcome" (causal link for current argument)
Type 3: "This is how the world/research works" (foundational principle shaping approach)
Examples:
"More features = more value" (assumes completeness > selectivity as a value)
"Efficiency is primary selection criterion" (frames decision-making paradigm)
"Open-source is inherently valuable for research" (disciplinary value statement)
"Interface familiarity breeds competence" (foundational HCI principle)
"Novices learn best with simple, constrained tools" (pedagogical paradigm)
Extract using same JSON format but mark type: "disciplinary_assumption" and status: "disciplinary_assumption"

These provide valuable context for assessment but are evaluated differently than Type 1/2 - they reveal underlying paradigms and values rather than specific logical gaps in the argument chain.

Special Extraction Patterns
Pattern: Implicit Generalization from Single Cases
When project-specific observation (e.g., "12 students had mobile devices") supports domain-level claim (e.g., "volunteers prefer mobile devices"):

Extract BOTH:

Evidence: Specific observation with precise details
Example: "12 of 12 students owned smartphones"
Claim (mark as claim_status: "implicit"): Generalized pattern
Example: "Volunteers prefer mobile device interfaces"
Set extraction_flags.generalization_from_single_case: true
Note in extraction_notes what would make generalization more robust (e.g., "Based on single cohort; would need multiple field seasons to validate pattern")
Why this matters: Single-case generalizations are common in HASS research but represent validity threats. Flagging them enables credibility assessment.

JSON Output Structure
For EVIDENCE:
json
{
  "evidence_id": "E###",
  "evidence_text": "[Observation or measurement]",
  "evidence_type": "[Type - free text for now]",
  "evidence_basis": "[direct_measurement | statistical_output | observational_record | archival_document | professional_judgment | author_assertion | derived_calculation | comparative_analysis]",
  "supports_claims": ["C###", "C###"],
  
  "declared_uncertainty": {
    "type": "[statistical | measurement_error | bounded_range | confidence_interval | stylistic_range | hedging_language | none_stated]",
    "value": "[The uncertainty value if stated]",
    "source": "[How authors express it]"
  },
  
  "expected_information_missing": ["[What should be present but isn't]"],
  "extraction_notes": "[Observations about quality, gaps, ambiguities]",
  
  "implicit_evidence": {
    "evidence_type": "[author_observation | professional_judgment | team_consensus | disciplinary_knowledge | common_knowledge]",
    "explanation_provided": [true/false]
  },
  
  "location": {"section": "", "page": #, "paragraph": #},
  "verbatim_quote": "[Exact text]"
}
For CLAIMS:
json
{
  "claim_id": "C###",
  "claim_text": "[The assertion being made]",
  "claim_status": "[explicit | implicit]",
  
  // CLASSIFICATION
  "claim_type": "[EMPIRICAL | INTERPRETATION | METHODOLOGICAL | THEORETICAL]",
  "claim_role": "[core | intermediate | supporting | evidence | background | transitional | methodological]",
  "claim_function": {
    "primary_function": "[premise | finding | conclusion | recommendation]",
    "secondary_function": "[premise | finding | conclusion | recommendation | none]"
  },
  "claim_scope": "[project | domain | general]",
  
  // NATURE
  "claim_nature": "[quantitative | qualitative | mixed | definitional]",
  "quantitative_details": {
    "source": "[measurement | calculation | estimate | statistical]",
    "confidence_basis": "[What gives confidence]",
    "bounded_range": "[If provided]",
    "arithmetic_verifiable": [true/false]
  },
  
  // AUTHOR LAYER
  "author_confidence": "[definite | probable | speculative | hedged]",
  "declared_uncertainty": {
    // Same structure as evidence
  },
  
  // EXTRACTION OBSERVATIONS
  "expected_information_missing": ["[Expected information not provided]"],
  "extraction_flags": {
    "generalization_from_single_case": [true/false],
    "requires_professional_judgment": [true/false],
    "boundary_ambiguous": [true/false]
  },
  "extraction_confidence": "[explicit | inferred | ambiguous]",
  "extraction_notes": "[Observations about this claim]",
  
  // COMPOSITION (for complex claims)
  "composed_of": {
    "evidence": ["E###", "E###"],
    "calculations": ["[Arithmetic operations]"],
    "boundary_decisions": ["[Definitional choices made]"],
    "causal_framing": "[How causality is framed]"
  },
  
  // RELATIONSHIPS
  "supports_claims": ["C###"],
  "supported_by_claims": ["C###"],
  "supported_by_evidence": ["E###"],
  "related_claims": {
    "alternatives": ["C###"],
    "qualifications": ["C###"],
    "contradicts": ["[Prior literature claims]"]
  },
  "implicit_arguments": ["IA###"],
  
  "location": {"section": "", "page": #, "paragraph": #},
  "verbatim_quote": "[Exact text]"
}
For IMPLICIT ARGUMENTS:
Extract for HIGH-PRIORITY claims only (core and key intermediate claims):

json
{
  "ia_id": "IA###",
  "argument": "[The implicit argument]",
  "type": "[logical_implication | unstated_assumption | bridging_claim | disciplinary_assumption]",
  "status": "[unstated_but_implied | assumed_without_acknowledgment | disciplinary_assumption]",
  "supports_claims": ["C###"],
  "assessment_notes": "[Why this matters for credibility]",
  "coi_note": "[Optional: Note if author COI affects interpretation]",
  "location": {"section": "", "page": #, "paragraph": #}
}
For PROJECT METADATA:
Context that doesn't support claims but provides background:

json
{
  "project_metadata": {
    "timeline": {
      "field_seasons": ["year"],
      "phases": [{"phase": "name", "years": "range", "focus": "description"}]
    },
    "location": {
      "field_sites": ["locations"],
      "work_contexts": ["contexts"]
    },
    "resources": {
      "constraints": ["resource limitations"],
      "infrastructure": ["available resources"]
    },
    "track_record": {
      "prior_uses": ["previous applications of method/tool"]
    }
  }
}
Extraction Workflow
STEP 1: Initial Scan
Read the abstract and conclusion
Identify the 5-10 CORE claims (main thesis)
Note the paper's structure
Check for any COI declarations (author affiliations, funding sources, platform developers)
STEP 2: Section-by-Section Extraction
For each section:

Identify Evidence First
Look for observations, measurements, data points
Check for declared uncertainty (ranges, errors, hedging)
Note missing uncertainty that should be present
Extract source and confidence information
Apply evidence extraction rule: does it support a claim?
Then Identify Claims
Look for assertions that interpret/frame evidence
Classify by role (core/intermediate/supporting/evidence)
Identify what evidence supports each claim
Check for composed claims (bundles of evidence + framing)
Watch for single-case generalizations
Check for Implicit Arguments (high-priority claims only)
What logical implications are unstated?
What assumptions must be true for this claim to hold?
Are there bridging claims linking evidence to conclusions?
What disciplinary assumptions frame the argument?
Map Relationships
Which claims support which other claims?
Are there alternative scenarios?
Are there qualifications?
Does this contradict prior literature?
Apply Expected Information Checklists
For quantitative claims: method? error margins? sample size? precision justified?
For comparative claims: basis explicit? what held constant? fair comparison?
For methodological claims: choices justified? limitations acknowledged? alternatives considered?
For causal claims: mechanism explained? confounds addressed? alternatives ruled out?
For generalizability claims: scope explicit? evidence supports scope? boundaries acknowledged?
Separate Project Context
Timeline, location, resources → project_metadata
Track record of methods → project_metadata
Only extract as evidence if it directly supports a claim
STEP 3: Build Hierarchy
Organize claims into four levels
Verify support relationships
Ensure core claims have clear evidential chains
STEP 4: Quality Check
Does each claim have a verbatim quote?
Is uncertainty properly documented (both declared and expected)?
Are information gaps identified?
Are extraction flags appropriate?
Do implicit arguments actually support high-priority claims?
Is project metadata separated from evidence?
Are single-case generalizations flagged?
Expected Information Checklists
Use these to populate expected_information_missing fields:

For Quantitative Claims
Measurement method specified
Instrument specification or calibration
Error margins or confidence intervals
Sample size or n
Bounded ranges for estimates
Precision justification
Units clearly stated
For Comparative Claims
Comparison basis explicit
What was held constant
Alternative explanations considered
Fairness of comparison justified
Like-for-like comparison
For Methodological Claims
Justification for choices
Limitations acknowledged
Alternatives considered
Verification evidence provided
Replicability information
For Causal Claims
Mechanism explained
Confounds addressed
Temporal precedence established
Alternative causes ruled out
Strength of causal language appropriate
For Generalizability Claims
Scope of generalization explicit
Evidence supports scope
Boundary conditions acknowledged
Population or domain defined
Number of cases/instances specified
Common Pitfalls to Avoid
Over-granularity: Don't split single observations into multiple evidence items
Under-granularity: Don't bundle distinct claims that need separate assessment
Misclassifying claims as evidence: If expertise needed to assess → claim
Missing implicit content: Watch for unstated generalizations and assumptions
Ignoring uncertainty: Always check for both declared and expected uncertainty
Weak relationships: Every claim should have clear evidential support
Mixing context with evidence: Track record, resources, timeline → project_metadata
Missing single-case patterns: Watch for project observations supporting domain claims
Quality Criteria
Good extraction demonstrates:

Completeness: All relevant evidence, claims, and implicit arguments captured
Precision: Each item is correctly classified (evidence vs. claim, role, type)
Relationships: Clear support chains from evidence through claims
Uncertainty tracking: Both declared and expected uncertainty documented
Context separation: Project metadata separated from evidence
Implicit content: Generalizations and assumptions made explicit when significant
Verbatim anchoring: Every item traceable to specific text in paper
Notes
Use schema v2.2 for all extractions
This is an extraction task (identifying and structuring content), not an assessment task (evaluating credibility)
Assessment fields like credibility_assessment remain unpopulated during extraction
Focus on accurately representing what the paper says, not evaluating whether it's correct
