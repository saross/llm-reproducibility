#!/usr/bin/env python3
"""Pass 1, Group G1: Abstract + Introduction (pp. 1-3, ~1,140 words).

Liberal extraction (40-50% over-extraction expected; Pass 2 consolidates).
Every quote verified against the page-anchored markdown by pass1_lib.save_group().
"""

from pass1_lib import save_group

EVIDENCE = [
    {
        "evidence_id": "E001",
        "evidence_text": "The paper's claims are grounded in two episodes: a 2025 campaign applying commercial LLMs to an archaeological study of research-software longevity (four stages, two thousand verified outcomes) and a 2026 re-application via a registry-grounded literature-search agent.",
        "evidence_type": "study_scope_summary",
        "verbatim_quote": "Two episodes ground these claims: a 2025 campaign applying commercial LLMs to an archaeological study of research-software longevity, across four stages and two thousand verified outcomes; a 2026 re-application through a literature-search agent grounded in bibliographic registries.",
        "location": {"section": "Abstract", "page": 1},
        "supports_claims": ["C014", "C015", "C019", "C020"],
        "notes": "Abstract-level summary of the evidential base; detailed results appear in Results sections. Borderline evidence vs project_metadata — retained liberally in Pass 1.",
        "extraction_confidence": "medium"
    },
    {
        "evidence_id": "E002",
        "evidence_text": "Two episodes a year apart: a 2025 evaluation of commercial LLMs (system customisation and prompts as the available levers) and a partial 2026 re-application using an agent built within a current framework.",
        "evidence_type": "study_scope_summary",
        "verbatim_quote": "We ground these claims in two episodes a year apart. The first is a 2025 evaluation of commercial LLMs applied to a study of archaeological research-software longevity involving system customisation and prompts, the levers available at the time. The second is a partial 2026 re-application: an agent built within a current framework.",
        "location": {"section": "1 Introduction", "page": 2},
        "supports_claims": ["C019", "C020", "C021"],
        "notes": "Case-study arc description; borderline evidence vs project_metadata — retained liberally in Pass 1.",
        "extraction_confidence": "medium"
    },
    {
        "evidence_id": "E003",
        "evidence_text": "The evaluation and safety literatures use 'scaffold' for capability-shaping structure built around a model; METR describes AI agents as consisting of an AI model and a scaffold (Kwa et al., 2025).",
        "evidence_type": "literature_citation",
        "verbatim_quote": "The evaluation and safety literatures use 'scaffold' for capability-shaping structure built around a model, as when METR describes AI agents \"consisting of an AI model and a scaffold\" (Kwa et al., 2025).",
        "location": {"section": "1 Introduction", "page": 1},
        "supports_claims": ["C022", "C024"],
        "notes": "Terminological grounding for the scaffolding/harness distinction."
    },
    {
        "evidence_id": "E004",
        "evidence_text": "Recent practitioner writing sometimes expands 'harness' to mean everything in an agent except the model (Böckeler, 2026), separating a built-in layer from an 'outer harness' users assemble.",
        "evidence_type": "literature_citation",
        "verbatim_quote": "Recent practitioner writing sometimes expands 'harness' to mean everything in an agent except the model (Böckeler, 2026).",
        "location": {"section": "1 Introduction", "page": 1},
        "supports_claims": ["C022", "C024"],
        "notes": "Second terminological anchor; the paper maps Böckeler's built-in layer to its 'harness' and outer harness to its 'scaffolding'."
    },
    {
        "evidence_id": "E005",
        "evidence_text": "A companion paper (Ballsun-Stanton and Ross, 2026) argues that these systems lack intrinsic judgement as an epistemic capability.",
        "evidence_type": "literature_citation",
        "verbatim_quote": "A companion paper argues that these systems lack intrinsic judgement as an epistemic capability Ballsun-Stanton and S. A. Ross, 2026.",
        "location": {"section": "1 Introduction", "page": 2},
        "supports_claims": ["C023"],
        "notes": "Establishes the companion-paper relationship: epistemic argument there, practitioner's complement here."
    },
    {
        "evidence_id": "E006",
        "evidence_text": "Between the two episodes, the same researcher-supplied judgement moved from prompts into skills, agent definitions, and verifier contracts while remaining the locus of reliability.",
        "evidence_type": "observation",
        "verbatim_quote": "Between our two episodes, the same researcher-supplied judgement moved from prompts into skills, agent definitions, and verifier contracts while remaining the locus of reliability (Section 5.1).",
        "location": {"section": "1 Introduction", "page": 2},
        "supports_claims": ["C019", "C022", "C024"],
        "notes": "Forward-referencing observation (detail in Section 5.1); grounds the functional rather than architectural boundary."
    },
    {
        "evidence_id": "E007",
        "evidence_text": "'Scaffolding' is used in its original pedagogic sense — support from a more capable partner enabling a learner to complete a task beyond unaided competence (Wood, Bruner, and Ross, 1976; van de Pol, Volman, and Beishuizen, 2010).",
        "evidence_type": "literature_citation",
        "verbatim_quote": "We use 'scaffolding' in its original, pedagogic sense, the support a more capable partner supplies so that a learner can complete a task beyond unaided competence (Wood, Bruner, and G. Ross, 1976; Pol, Volman, and Beishuizen, 2010).",
        "location": {"section": "1 Introduction", "page": 1},
        "supports_claims": ["C003"],
        "notes": "Definitional grounding for the central 'scaffolding' concept; candidate for project_metadata in Pass 2."
    },
]

CLAIMS = [
    {
        "claim_id": "C001",
        "claim_text": "Reliability in the research use of LLMs is a property of the human–AI system built around the model, not the model alone.",
        "claim_type": "theoretical",
        "claim_role": "core",
        "verbatim_quote": "Reliability in the research use of large language models (LLMs) is a property of the human–AI system built around the model, not the model alone.",
        "location": {"section": "1 Introduction", "page": 1},
        "supported_by": [],
        "supports_claims": [],
        "notes": "Central thesis of the paper (also stated in Abstract)."
    },
    {
        "claim_id": "C002",
        "claim_text": "An LLM cannot appraise from within whether it has succeeded at a task, so any appraisal must come from outside.",
        "claim_type": "theoretical",
        "claim_role": "supporting",
        "verbatim_quote": "Because an LLM cannot appraise from within whether it has succeeded at a task, any appraisal must come from outside; the locus of reliability is the scaffolding the researcher constructs (the prompts, skills, workflows, and verification structures), not the raw capability of the model and harness.",
        "location": {"section": "1 Introduction", "page": 1},
        "supported_by": [],
        "supports_claims": ["C003"],
        "notes": "Premise half of a compound sentence shared with C003."
    },
    {
        "claim_id": "C003",
        "claim_text": "The locus of reliability is the scaffolding the researcher constructs (prompts, skills, workflows, verification structures), not the raw capability of the model and harness.",
        "claim_type": "theoretical",
        "claim_role": "intermediate",
        "verbatim_quote": "Because an LLM cannot appraise from within whether it has succeeded at a task, any appraisal must come from outside; the locus of reliability is the scaffolding the researcher constructs (the prompts, skills, workflows, and verification structures), not the raw capability of the model and harness.",
        "location": {"section": "1 Introduction", "page": 1},
        "supported_by": ["E007"],
        "supports_claims": ["C001"],
        "notes": "Conclusion half of the compound sentence shared with C002."
    },
    {
        "claim_id": "C004",
        "claim_text": "The common advice for responsible LLM use — disclosure plus reliance on expert judgement to verify output — is insufficient.",
        "claim_type": "methodological_argument",
        "claim_role": "core",
        "verbatim_quote": "The common recommendations for using LLMs responsibly include disclosure and reliance on expert judgement to verify the output. We argue that this advice is insufficient.",
        "location": {"section": "1 Introduction", "page": 2},
        "supported_by": [],
        "supports_claims": ["C007"],
        "notes": ""
    },
    {
        "claim_id": "C005",
        "claim_text": "Disclosure tells a reader what to suspect rather than what to trust.",
        "claim_type": "methodological_argument",
        "claim_role": "supporting",
        "verbatim_quote": "Disclosure tells a reader what to suspect rather than what to trust, and unaided expert verification does not reliably catch fluent, plausibly framed error, especially at scale.",
        "location": {"section": "1 Introduction", "page": 2},
        "supported_by": [],
        "supports_claims": ["C004"],
        "notes": "Compound sentence shared with C006."
    },
    {
        "claim_id": "C006",
        "claim_text": "Unaided expert verification does not reliably catch fluent, plausibly framed error, especially at scale.",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "verbatim_quote": "Disclosure tells a reader what to suspect rather than what to trust, and unaided expert verification does not reliably catch fluent, plausibly framed error, especially at scale.",
        "location": {"section": "1 Introduction", "page": 2},
        "supported_by": [],
        "supports_claims": ["C004"],
        "notes": "Compound sentence shared with C005; developed empirically in Sections 4-5."
    },
    {
        "claim_id": "C007",
        "claim_text": "Reliability must be engineered into the structure of human–AI collaboration.",
        "claim_type": "methodological_argument",
        "claim_role": "core",
        "verbatim_quote": "Reliability must instead be engineered into the structure of human–AI collaboration — that structure is the focus of this paper.",
        "location": {"section": "1 Introduction", "page": 2},
        "supported_by": [],
        "supports_claims": [],
        "notes": ""
    },
    {
        "claim_id": "C008",
        "claim_text": "LLMs can augment a researcher but not yet automate research.",
        "claim_type": "methodological_argument",
        "claim_role": "core",
        "verbatim_quote": "Our answer turns on a distinction: LLMs can augment a researcher but not yet automate research.",
        "location": {"section": "1 Introduction", "page": 2},
        "supported_by": [],
        "supports_claims": [],
        "notes": ""
    },
    {
        "claim_id": "C009",
        "claim_text": "Augmentation requires a human to supply judgement the system cannot — primarily through scaffolding construction, secondarily through targeted verification.",
        "claim_type": "methodological_argument",
        "claim_role": "supporting",
        "verbatim_quote": "Augmentation in this case requires a human to supply judgement the system cannot, primarily through construction of scaffolding to guide the model, secondarily through targeted verification.",
        "location": {"section": "1 Introduction", "page": 2},
        "supported_by": [],
        "supports_claims": ["C008"],
        "notes": ""
    },
    {
        "claim_id": "C010",
        "claim_text": "Conflating augmentation with automation can undermine research reliability, whether by naively expecting an LLM to verify work or by relying on poorly constrained human verification.",
        "claim_type": "methodological_argument",
        "claim_role": "supporting",
        "verbatim_quote": "These systems can expand research, but conflating augmentation with automation can undermine research reliability, whether the conflation lies in naively expecting an LLM to verify work or in relying on poorly constrained human verification.",
        "location": {"section": "1 Introduction", "page": 2},
        "supported_by": [],
        "supports_claims": ["C008"],
        "notes": ""
    },
    {
        "claim_id": "C011",
        "claim_text": "Treating scaffolding as the locus of reliability turns prompt and workflow design from a knack into a method.",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "verbatim_quote": "Treating scaffolding as the locus of reliability turns prompt and workflow design from a knack into a method.",
        "location": {"section": "1 Introduction", "page": 2},
        "supported_by": [],
        "supports_claims": [],
        "notes": ""
    },
    {
        "claim_id": "C012",
        "claim_text": "Iterative scaffolding construction is an upfront investment, like scripting a reproducible analysis, yielding a procedure others can inspect, rerun, and improve.",
        "claim_type": "methodological_argument",
        "claim_role": "supporting",
        "verbatim_quote": "Iterative construction of effective scaffolding represents an upfront investment, like scripting a reproducible analysis, yielding a procedure others can inspect, rerun, and improve.",
        "location": {"section": "1 Introduction", "page": 2},
        "supported_by": [],
        "supports_claims": ["C011", "C018"],
        "notes": ""
    },
    {
        "claim_id": "C013",
        "claim_text": "Scaffolding has two parts: building judgement into the workflow (decomposition to within-competence components; externalising judgements the model cannot make) and confirming success through producer-independent, externally anchored verification.",
        "claim_type": "methodological_argument",
        "claim_role": "supporting",
        "verbatim_quote": "This scaffolding has two parts. The first builds judgement into the workflow: decomposing a task until each component falls within the model's competence, and externalising the judgements the model cannot reliably make. The second confirms that the work succeeded, through verification independent of the producer and anchored to an external source.",
        "location": {"section": "1 Introduction", "page": 2},
        "supported_by": [],
        "supports_claims": ["C011"],
        "notes": "Structural definition of the scaffolding framework developed in Sections 2.3 and 5.2."
    },
    {
        "claim_id": "C014",
        "claim_text": "A model generation apart, both episodes failed the same way: retrieval succeeded while confabulation entered at the synthesis boundary, where retrieved evidence ends and the model's composition begins.",
        "claim_type": "empirical",
        "claim_role": "core",
        "verbatim_quote": "A model generation apart, both failed in the same way. Retrieval succeeded, while confabulation entered at the synthesis boundary, where retrieved evidence ends and the model's composition begins.",
        "location": {"section": "Abstract", "page": 1},
        "supported_by": ["E001"],
        "supports_claims": ["C016"],
        "notes": "Central empirical finding; substantiated in Results."
    },
    {
        "claim_id": "C015",
        "claim_text": "Independence of context, external re-grounding, and orthogonal framing mitigated the failure mode in both episodes.",
        "claim_type": "empirical",
        "claim_role": "core",
        "verbatim_quote": "Independence of context, external re-grounding, and orthogonal framing mitigated both.",
        "location": {"section": "Abstract", "page": 1},
        "supported_by": ["E001"],
        "supports_claims": ["C016"],
        "notes": "The mitigation triad; substantiated in Results and Discussion."
    },
    {
        "claim_id": "C016",
        "claim_text": "The persistence of the failure mode is structural rather than transitional, and translates into design principles for researcher-builders (encoding requirements as procedure rather than exhortation; stage-gating workflows with human checkpoints).",
        "claim_type": "interpretation",
        "claim_role": "core",
        "verbatim_quote": "We argue this persistence is structural rather than transitional and translate it into design principles for researcher-builders, from encoding requirements as procedure rather than exhortation to stage-gating workflows with human checkpoints.",
        "location": {"section": "Abstract", "page": 1},
        "supported_by": [],
        "supports_claims": [],
        "notes": ""
    },
    {
        "claim_id": "C017",
        "claim_text": "Because LLMs currently augment rather than automate research, reliability must be engineered into scaffolding that supplies from outside the judgement the model cannot supply from within.",
        "claim_type": "methodological_argument",
        "claim_role": "supporting",
        "verbatim_quote": "LLMs currently augment rather than automate research, so reliability must be engineered into scaffolding that provides from outside the judgement the model cannot supply from within.",
        "location": {"section": "Abstract", "page": 1},
        "supported_by": [],
        "supports_claims": ["C007", "C008"],
        "notes": "Abstract restatement bridging the augment/automate distinction and the engineering prescription; Pass 2 consolidation candidate."
    },
    {
        "claim_id": "C018",
        "claim_text": "Scaffolding is worth publishing, both as method and as evidence of what these tools can and cannot do.",
        "claim_type": "methodological_argument",
        "claim_role": "core",
        "verbatim_quote": "Such scaffolding is worth publishing as method and as evidence of what these tools can and cannot do.",
        "location": {"section": "Abstract", "page": 1},
        "supported_by": [],
        "supports_claims": [],
        "notes": "Prescriptive core claim; elaborated in Discussion and Conclusion."
    },
    {
        "claim_id": "C019",
        "claim_text": "The locus of reliability remained invariant across the model generation separating the two episodes, evidencing that reliability is structural rather than a property of any one model.",
        "claim_type": "empirical",
        "claim_role": "intermediate",
        "verbatim_quote": "The locus of reliability remains invariant across the model generation that separates them, providing evidence that reliability is structural rather than a property of any one model.",
        "location": {"section": "1 Introduction", "page": 2},
        "supported_by": ["E001", "E002", "E006"],
        "supports_claims": ["C016"],
        "notes": ""
    },
    {
        "claim_id": "C020",
        "claim_text": "Despite a year of model and harness development, both cases exhibited the same failure mode in similar instances and yielded to the same classes of mitigation.",
        "claim_type": "empirical",
        "claim_role": "intermediate",
        "verbatim_quote": "Despite a year of development in models and in the software harnesses that operate them, both cases exhibited the same failure mode, in similar instances, and both yielded to the same classes of mitigation.",
        "location": {"section": "1 Introduction", "page": 2},
        "supported_by": ["E001", "E002"],
        "supports_claims": ["C014", "C015"],
        "notes": ""
    },
    {
        "claim_id": "C021",
        "claim_text": "Although based in a particular discipline, the findings concern what LLMs can accomplish as research tools in general.",
        "claim_type": "interpretation",
        "claim_role": "supporting",
        "verbatim_quote": "Although based in a particular discipline, our findings concern what LLMs can accomplish as research tools in general.",
        "location": {"section": "1 Introduction", "page": 2},
        "supported_by": ["E002"],
        "supports_claims": ["C001"],
        "notes": "Generalisability claim; see IA002 for the bridging argument it requires."
    },
    {
        "claim_id": "C022",
        "claim_text": "The scaffolding/harness boundary is drawn functionally rather than architecturally because the argument concerns the source of judgement, not its location in the stack.",
        "claim_type": "methodological_argument",
        "claim_role": "supporting",
        "verbatim_quote": "We draw the boundary functionally rather than architecturally because our argument concerns the source of judgement rather than its location in the stack.",
        "location": {"section": "1 Introduction", "page": 2},
        "supported_by": ["E003", "E004", "E006"],
        "supports_claims": ["C003"],
        "notes": "Definitional-choice justification."
    },
    {
        "claim_id": "C023",
        "claim_text": "The companion paper's epistemic claim and this paper's practitioner claim are two views of one phenomenon: the system does not exercise judgement, but well-designed structure around it can stand in for what judgement would provide.",
        "claim_type": "theoretical",
        "claim_role": "supporting",
        "verbatim_quote": "These claims represent two views of one phenomenon: the system does not exercise judgement, but a well-designed structure around it can stand in for what judgement would provide.",
        "location": {"section": "1 Introduction", "page": 2},
        "supported_by": ["E005"],
        "supports_claims": ["C001"],
        "notes": ""
    },
    {
        "claim_id": "C024",
        "claim_text": "A vocabulary tied to stack position would rename the judgement-bearing structure each time it moved.",
        "claim_type": "methodological_argument",
        "claim_role": "supporting",
        "verbatim_quote": "A vocabulary tied to stack position would rename this structure each time it moved.",
        "location": {"section": "1 Introduction", "page": 2},
        "supported_by": ["E003", "E004", "E006"],
        "supports_claims": ["C022"],
        "notes": ""
    },
]

IMPLICIT_ARGUMENTS = [
    {
        "implicit_argument_id": "IA001",
        "argument_text": "Human judgement, once externalised into scaffolding, is itself reliable enough to confer system-level reliability — the researcher can supply what the model cannot.",
        "type": "unstated_assumption",
        "trigger_text": [
            "Because an LLM cannot appraise from within whether it has succeeded at a task, any appraisal must come from outside; the locus of reliability is the scaffolding the researcher constructs (the prompts, skills, workflows, and verification structures), not the raw capability of the model and harness.",
            "Augmentation in this case requires a human to supply judgement the system cannot, primarily through construction of scaffolding to guide the model, secondarily through targeted verification."
        ],
        "trigger_locations": [
            {"section": "1 Introduction", "page": 1},
            {"section": "1 Introduction", "page": 2}
        ],
        "inference_reasoning": "The argument moves from 'the model cannot self-appraise' to 'scaffolding confers reliability' only if the judgement the researcher encodes is itself adequate and reliably encoded. That adequacy is assumed rather than argued in the Introduction; later sections partially address it through verification structures, but the assumption underpins the thesis (C001, C003).",
        "supports_claims": ["C001", "C003"],
        "assessment_implications": "If researcher-encoded judgement is itself error-prone (as the paper's own Reflexivity section concedes for verification), system reliability inherits that limit; the thesis depends on scaffolding quality being achievable and auditable."
    },
    {
        "implicit_argument_id": "IA002",
        "argument_text": "Two episodes from the same research programme, one model generation apart, are sufficiently representative to support the generalisation that the failure mode and the locus of reliability are structural to LLM-assisted research.",
        "type": "bridging_claim",
        "trigger_text": [
            "Despite a year of development in models and in the software harnesses that operate them, both cases exhibited the same failure mode, in similar instances, and both yielded to the same classes of mitigation.",
            "The locus of reliability remains invariant across the model generation that separates them, providing evidence that reliability is structural rather than a property of any one model.",
            "Although based in a particular discipline, our findings concern what LLMs can accomplish as research tools in general."
        ],
        "trigger_locations": [
            {"section": "1 Introduction", "page": 2},
            {"section": "1 Introduction", "page": 2},
            {"section": "1 Introduction", "page": 2}
        ],
        "inference_reasoning": "The inference from two same-team, same-domain cases to 'structural' invariance and discipline-general findings requires an unstated bridge about representativeness (that these cases are typical of LLM research use, not artefacts of one team's practice or one task family). The Limitations section later concedes situated depth, but the Introduction's generalisation depends on this bridge.",
        "supports_claims": ["C019", "C021"],
        "assessment_implications": "Central to external validity: readers must judge whether n=2 episodes from one research programme licence claims about LLM research tools in general."
    },
    {
        "implicit_argument_id": "IA003",
        "argument_text": "Existing research quality-control practices (expert reading, self-checking) are calibrated to human error patterns, so LLM errors — characteristically fluent and plausibly framed — systematically evade them.",
        "type": "logical_implication",
        "trigger_text": [
            "That advice is insufficient because readers do not reliably catch fluent error and self-checking reproduces the errors it should catch.",
            "Disclosure tells a reader what to suspect rather than what to trust, and unaided expert verification does not reliably catch fluent, plausibly framed error, especially at scale."
        ],
        "trigger_locations": [
            {"section": "Abstract", "page": 1},
            {"section": "1 Introduction", "page": 2}
        ],
        "inference_reasoning": "For 'disclose and verify' to fail specifically for LLM output, LLM errors must differ in kind from the errors expert review evolved to catch — fluency and plausible framing defeating the surface cues reviewers rely on. This difference in error distribution is implied but not stated as a premise in the Introduction (the Background later develops it via the information-science literature).",
        "supports_claims": ["C004", "C006"],
        "assessment_implications": "If expert review catches LLM errors as well as human errors, the insufficiency argument weakens; the claim's force depends on this implied distributional difference."
    },
    {
        "implicit_argument_id": "IA004",
        "argument_text": "Scaffolding is stable and transferable enough across models, harnesses, and tasks to repay upfront investment and to be worth publishing for reuse, analogous to reproducible analysis code.",
        "type": "unstated_assumption",
        "trigger_text": [
            "Iterative construction of effective scaffolding represents an upfront investment, like scripting a reproducible analysis, yielding a procedure others can inspect, rerun, and improve.",
            "Such scaffolding is worth publishing as method and as evidence of what these tools can and cannot do."
        ],
        "trigger_locations": [
            {"section": "1 Introduction", "page": 2},
            {"section": "Abstract", "page": 1}
        ],
        "inference_reasoning": "The reproducible-analysis analogy and the publish-as-method prescription assume scaffolding retains value beyond its original model/harness context. The paper's own evidence of judgement migrating across forms (prompts to skills to agent definitions) supports partial stability, but transferability to other teams and tasks is assumed rather than demonstrated.",
        "supports_claims": ["C012", "C018"],
        "assessment_implications": "Affects the practical payoff of the paper's prescriptions: if scaffolding is brittle across contexts, publishing it documents rather than transfers reliability."
    },
]

save_group(
    {
        "group": "G1",
        "section_title": "Abstract + Introduction",
        "page_range": "1-3",
        "estimated_words": 1140,
        "natural_boundary": "Before 'Background' heading (Section 2, p. 3)",
        "split_rationale": "Abstract (p. 1) combined with Introduction (pp. 1-3) per default grouping; total under 1,500-word cap."
    },
    evidence=EVIDENCE,
    claims=CLAIMS,
    implicit_arguments=IMPLICIT_ARGUMENTS,
)
