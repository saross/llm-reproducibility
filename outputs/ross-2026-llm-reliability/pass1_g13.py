#!/usr/bin/env python3
"""Pass 1, Group G13: Discussion 5.2 (end) + 5.3 Limitations + 6 Conclusion (pp. 23-24, ~1,000 words)."""

from pass1_lib import save_group

EVIDENCE = [
    {
        "evidence_id": "E201",
        "evidence_text": "METR measures time horizons (task lengths a model completes at a given success rate); its 80%-success horizons run roughly one-fifth the length of its headline 50% figures (Kwa et al. 2025).",
        "evidence_type": "literature_citation",
        "verbatim_quote": "METR measures time horizons, the task lengths a model completes at a given success rate, and its 80%-success horizons run roughly one-fifth the length of its headline 50% figures (Kwa et al., 2025).",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 23},
        "supports_claims": ["C161"],
        "notes": ""
    },
    {
        "evidence_id": "E202",
        "evidence_text": "During tool documentation the authors ran trials against software known first-hand until sure the task completed reliably and failures were all-or-nothing and readily identifiable.",
        "evidence_type": "observation",
        "verbatim_quote": "In our case, during tool documentation, we ran trials against software we knew first-hand, until we were sure that the task was completing reliably and had come to understand that failures were all-or-nothing and thus readily identifiable (Section 4.3).",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 23},
        "supports_claims": ["C162"],
        "notes": ""
    },
    {
        "evidence_id": "E203",
        "evidence_text": "When the model would not stop reporting tool histories during documentation, the authors gave up requiring only a current snapshot and provided a historical field in the schema.",
        "evidence_type": "observation",
        "verbatim_quote": "When, for example, the model would not stop reporting each tool's history during documentation, we gave up on requiring only a current snapshot and instead provided a historical field in the schema.",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 23},
        "supports_claims": ["C163"],
        "notes": "Discussion restatement of the E124 domestication example; Pass 2 consolidation candidate."
    },
    {
        "evidence_id": "E204",
        "evidence_text": "An unprompted model appraisal of reproducibility became a standing schema requirement for tool documentation (codifying a spontaneous contribution).",
        "evidence_type": "observation",
        "verbatim_quote": "Where the model spontaneously offers something of value, codify it so that it is captured in all future runs, as when an unprompted appraisal of reproducibility became a standing schema requirement for tool documentation (Section 4.3).",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 23},
        "supports_claims": ["C163"],
        "notes": "Discussion restatement of the E125 codification example; Pass 2 consolidation candidate."
    },
    {
        "evidence_id": "E205",
        "evidence_text": "Each documented error made by the 2026 verifier instigated a structural fix.",
        "evidence_type": "observation",
        "verbatim_quote": "This approach helps improve the scaffolding, as was the case when each documented error made by our 2026 verifier instigated a structural fix (Section 4.5).",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 23},
        "supports_claims": ["C164", "C165"],
        "notes": ""
    },
    {
        "evidence_id": "E206",
        "evidence_text": "Shojaee et al. (2025) find reasoning models collapse to zero accuracy beyond a model-specific threshold of compositional complexity, implying scope discipline and external scaffolding are ongoing requirements, not transitional workarounds.",
        "evidence_type": "literature_citation",
        "verbatim_quote": "Shojaee et al. (2025) find that reasoning models collapse to zero accuracy beyond a model-specific threshold of compositional complexity, implying that scope discipline and external scaffolding are not transitional workarounds but ongoing requirements.",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 23},
        "supports_claims": ["C166", "C016"],
        "notes": ""
    },
    {
        "evidence_id": "E207",
        "evidence_text": "The laboratories releasing the most capable models are simultaneously building the most elaborate scaffolding (sub-agents, independent context windows, structured workflows, verifier patterns).",
        "evidence_type": "observation",
        "verbatim_quote": "The fact that the laboratories releasing the most capable models are simultaneously building the most elaborate scaffolding (sub-agents, independent context windows, structured workflows, verifier patterns) is evidence that such an apparatus is necessary for the models to be reliable in non-trivial work.",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 24},
        "supports_claims": ["C173"],
        "notes": "Quote shared with C173 (observation plus the inference drawn from it)."
    },
    {
        "evidence_id": "E208",
        "evidence_text": "The literature scout enlisted for this paper confabulated, was diagnosed, and was repaired by precisely the guards set out in the design principles, with the build-and-fix artefacts becoming part of the paper's evidence.",
        "evidence_type": "observation",
        "verbatim_quote": "The literature scout enlisted to retrieve relevant information-science literature (Section 4.5) confabulated, was diagnosed, and was repaired by precisely the guards set out above, while the artefacts documenting the effort of building and fixing the instrument became part of the paper's evidence.",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 24},
        "supports_claims": ["C167", "C168"],
        "notes": "Self-instantiation of the tooling-as-evidence principle."
    },
    {
        "evidence_id": "E209",
        "evidence_text": "Verifier testing is limited: across fifteen runs (April–June 2026) it made thirteen confirmed corrections and missed two errors, both caught manually; undetected misses cannot be excluded.",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "Likewise, testing of the 2026 verifier agent's performance is limited: across fifteen runs between April and June 2026, it made thirteen confirmed corrections and missed two errors, both caught manually (undetected misses cannot be excluded).",
        "location": {"section": "5.3 Limitations", "page": 24},
        "supports_claims": ["C174", "C175"],
        "notes": ""
    },
    {
        "evidence_id": "E210",
        "evidence_text": "The samples are small (a four-row spot-check, a single agent build), so the authors report the direction of each failure and treat its magnitude as uncertain.",
        "evidence_type": "observation",
        "verbatim_quote": "The samples mentioned are small (a four-row spotcheck, a single agent build), so we report the direction of each failure and treat its magnitude as uncertain.",
        "location": {"section": "5.3 Limitations", "page": 24},
        "supports_claims": ["C174"],
        "notes": "'spotcheck' preserves a line-break artefact of the processed md."
    },
]

CLAIMS = [
    {
        "claim_id": "C160",
        "claim_text": "The paper adopts Jones's 90% threshold as the floor for research use rather than a target to approach; that floor determines how far tasks must be decomposed.",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "verbatim_quote": "We therefore adopt Jones's 90% threshold as the floor for research use rather than a target to approach. That floor determines how far tasks must be decomposed.",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 23},
        "supported_by": ["E200"],
        "supports_claims": ["C155", "C158"],
        "notes": ""
    },
    {
        "claim_id": "C161",
        "claim_text": "At a 90% success bar the METR horizon would contract further, so most research must still be aggressively decomposed even with mid-2026 models.",
        "claim_type": "interpretation",
        "claim_role": "intermediate",
        "verbatim_quote": "At a 90% bar the horizon would contract further, so most research must still be aggressively decomposed, even with mid-2026 models.",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 23},
        "supported_by": ["E201"],
        "supports_claims": ["C160", "C053"],
        "notes": ""
    },
    {
        "claim_id": "C162",
        "claim_text": "Limiting error requires examining the material and running trials to determine failure modes, shrinking task scope and model remit until success is provable, then deploying verifiers that catch remaining failures.",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "verbatim_quote": "Limiting error requires that the researcher examine the material and run trials to determine the failure modes, then shrink both the scope of the task and the remit of the model until success is provable, and finally deploy human or machine verifiers that catch any remaining failures.",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 23},
        "supported_by": ["E202"],
        "supports_claims": ["C155"],
        "notes": ""
    },
    {
        "claim_id": "C163",
        "claim_text": "Where a model persists in an unwanted tendency, domesticate it — absorb it into the architecture and route it to its own container; where it spontaneously offers value, codify it.",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "verbatim_quote": "Where a model persists in an unwanted tendency, 'domesticate' it: instead of trying to forbid it, absorb the tendency into the architecture.",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 23},
        "supported_by": ["E203", "E204"],
        "supports_claims": ["C097", "C016"],
        "notes": "Discussion articulation of the working-with-the-grain principle (C097)."
    },
    {
        "claim_id": "C164",
        "claim_text": "Scaffold development should be an iterative articulate→build→test→improve loop in which productive failures and chance contributions are systematised.",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "verbatim_quote": "Approach scaffold development as an iterative articulate →build →test →improve loop in which productive failures and chance contributions are systematised.",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 23},
        "supported_by": ["E205"],
        "supports_claims": ["C016"],
        "notes": ""
    },
    {
        "claim_id": "C165",
        "claim_text": "A workflow that logs and reviews failures turns some into findings; one that only suppresses them discards the serendipitous wins with the errors.",
        "claim_type": "methodological_argument",
        "claim_role": "supporting",
        "verbatim_quote": "A workflow that logs and reviews failures turns some into findings; one that only suppresses them discards the serendipitous wins with the errors.",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 23},
        "supported_by": ["E205", "E079"],
        "supports_claims": ["C164"],
        "notes": ""
    },
    {
        "claim_id": "C166",
        "claim_text": "The design principles gain urgency from the complexity ceiling: the harder the task, the more of the structure must come from outside the model.",
        "claim_type": "interpretation",
        "claim_role": "intermediate",
        "verbatim_quote": "The harder the task, the more of the structure must come from outside the model, as the evidence stage's narrowed mandate showed (Section 4.4).",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 23},
        "supported_by": ["E206", "E144"],
        "supports_claims": ["C016", "C135"],
        "notes": ""
    },
    {
        "claim_id": "C167",
        "claim_text": "The scaffolding a researcher-builder constructs is not overhead but itself a reproducible-research contribution — an upfront cost yielding a procedure others can inspect, rerun, and improve.",
        "claim_type": "methodological_argument",
        "claim_role": "core",
        "verbatim_quote": "The scaffolding a researcher-builder constructs (the prompts, the helper scripts, the staged workflow, the verification architecture) is not overhead incurred on the way to a result; it is itself a reproducible-research contribution. Like a script that encodes an analysis, it is an upfront cost that yields a procedure the researcher or others can inspect, rerun, and improve.",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 23},
        "supported_by": ["E208"],
        "supports_claims": ["C018", "C012"],
        "notes": "Tooling-investment-as-evidence principle."
    },
    {
        "claim_id": "C168",
        "claim_text": "A frank account of the scaffolding investment provides evidence about what scaffolded LLM systems can and cannot do.",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "verbatim_quote": "A frank account of the investment provides evidence about what scaffolded LLM systems can and cannot do. Such knowledge matters as researchers come to terms with AI capabilities and learn how to apply them.",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 23},
        "supported_by": ["E208"],
        "supports_claims": ["C018"],
        "notes": ""
    },
    {
        "claim_id": "C169",
        "claim_text": "Bare results give readers values without 'handles' (a defined unit to check, a source to check against, a procedure to check by); disclosure only adds a warning label, but publishing the workflow provides the missing handles.",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "verbatim_quote": "Bare results give that reader values without 'handles': points of purchase on a claim, including a defined unit to check, a source to check it against, and a procedure to check it by. Disclosure only adds a warning label (Smith et al., 2024; Lin, 2023), but publishing the workflow provides the missing handles.",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 23},
        "supported_by": [],
        "supports_claims": ["C018", "C005"],
        "notes": ""
    },
    {
        "claim_id": "C170",
        "claim_text": "Workflow specifications show what every field was required to contain; execution records show where every value came from and what verification it survived.",
        "claim_type": "methodological_argument",
        "claim_role": "supporting",
        "verbatim_quote": "The workflow's specifications (prompts, skills, agent definitions) show what every field was required to contain, while its execution records (session transcripts, the verifier's audit trails) show where every value actually came from and what verification it survived.",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 23},
        "supported_by": [],
        "supports_claims": ["C169"],
        "notes": ""
    },
    {
        "claim_id": "C171",
        "claim_text": "Checking can succeed because the reader starts from handles rather than prose: a bare output can only be believed or doubted, but a record of specifications and execution can be examined.",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "verbatim_quote": "Checking can then succeed because the reader starts from handles rather than prose: a bare output can only be believed or doubted, but a record of specifications and execution can be examined.",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 23},
        "supported_by": [],
        "supports_claims": ["C169", "C018"],
        "notes": ""
    },
    {
        "claim_id": "C172",
        "claim_text": "The same record opens the verification implementation itself to scrutiny: a reader can evaluate not only the findings but how far the verification behind them deserves trust.",
        "claim_type": "methodological_argument",
        "claim_role": "supporting",
        "verbatim_quote": "The same record opens the verification implementation itself to scrutiny: a human or machine reader can evaluate not only the findings but how far the verification behind them deserves trust.",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 23},
        "supported_by": [],
        "supports_claims": ["C169"],
        "notes": ""
    },
    {
        "claim_id": "C173",
        "claim_text": "That the labs releasing the most capable models simultaneously build the most elaborate scaffolding is evidence that such an apparatus is necessary for reliability in non-trivial work.",
        "claim_type": "interpretation",
        "claim_role": "intermediate",
        "verbatim_quote": "The fact that the laboratories releasing the most capable models are simultaneously building the most elaborate scaffolding (sub-agents, independent context windows, structured workflows, verifier patterns) is evidence that such an apparatus is necessary for the models to be reliable in non-trivial work.",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 24},
        "supported_by": ["E207"],
        "supports_claims": ["C016", "C132"],
        "notes": "Quote shared with E207."
    },
    {
        "claim_id": "C174",
        "claim_text": "The paper is a case study whose second episode arose incidentally; it offers situated depth, and the wider applicability of the persistence finding and design principles remains to be seen.",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "verbatim_quote": "This paper constitutes a case study whose second episode arose incidentally, during manuscript preparation. It offers situated depth, and the wider applicability of persistence and design principles remains to be seen (Section 3.3).",
        "location": {"section": "5.3 Limitations", "page": 24},
        "supported_by": ["E209", "E210"],
        "supports_claims": ["C133", "C076"],
        "notes": "Limitations statement."
    },
    {
        "claim_id": "C175",
        "claim_text": "The verifier is presented as a worked design pattern rather than a benchmarked result.",
        "claim_type": "methodological_argument",
        "claim_role": "supporting",
        "verbatim_quote": "As such, we present the verifier as a worked design pattern rather than a benchmarked result (Section 4.5).",
        "location": {"section": "5.3 Limitations", "page": 24},
        "supported_by": ["E209"],
        "supports_claims": ["C174"],
        "notes": ""
    },
    {
        "claim_id": "C176",
        "claim_text": "Provision of all outputs, specifications, and session transcripts (Supplement A) allows readers to assess the claims.",
        "claim_type": "methodological_argument",
        "claim_role": "supporting",
        "verbatim_quote": "Provision of all outputs, specifications, and session transcripts (Supplement A) allows readers to assess our claims.",
        "location": {"section": "5.3 Limitations", "page": 24},
        "supported_by": [],
        "supports_claims": ["C169"],
        "notes": ""
    },
    {
        "claim_id": "C177",
        "claim_text": "The nearest future step is migrating the remaining 2025 stages into the agentic scaffolding the literature search uses, run at intervals so the software-longevity dataset becomes a continuously extended, versioned resource.",
        "claim_type": "methodological_argument",
        "claim_role": "supporting",
        "verbatim_quote": "The nearest step is migrating the remaining 2025 stages — tool discovery, documentation, and evidence collection — into the agentic scaffolding the literature search now uses, and running the pipeline at intervals, so that the software-longevity dataset becomes a continuously extended, versioned resource rather than a snapshot.",
        "location": {"section": "6 Conclusion", "page": 24},
        "supported_by": [],
        "supports_claims": [],
        "notes": "Future-work commitment."
    },
    {
        "claim_id": "C178",
        "claim_text": "Because models and harnesses change faster than publication, a maintained public evaluation protocol (stable, with versioned result releases) is more valuable than any fixed comparison of services.",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "verbatim_quote": "Because models and harnesses change faster than publication, we see more value in a maintained, public evaluation protocol than in any fixed comparison of services. Such a protocol remains stable while its results are re-issued as versioned releases.",
        "location": {"section": "6 Conclusion", "page": 24},
        "supported_by": ["E067"],
        "supports_claims": ["C018"],
        "notes": ""
    },
    {
        "claim_id": "C179",
        "claim_text": "The same logic argues for sharing the scaffolding itself (skills, agent definitions, verifier contracts) through open repositories.",
        "claim_type": "methodological_argument",
        "claim_role": "supporting",
        "verbatim_quote": "The same logic argues for sharing the scaffolding itself (skills, agent definitions, verifier contracts) through open repositories.",
        "location": {"section": "6 Conclusion", "page": 24},
        "supported_by": [],
        "supports_claims": ["C018"],
        "notes": ""
    },
    {
        "claim_id": "C180",
        "claim_text": "The verifier invites benchmarking: seeding known errors into its inputs would measure the catching power the record only exercises.",
        "claim_type": "methodological_argument",
        "claim_role": "supporting",
        "verbatim_quote": "The verifier this paper offers as a worked pattern invites benchmarking: seeding known errors into its inputs would measure the catching power our record only exercises (Section 5.3).",
        "location": {"section": "6 Conclusion", "page": 24},
        "supported_by": ["E209"],
        "supports_claims": ["C175"],
        "notes": ""
    },
    {
        "claim_id": "C181",
        "claim_text": "Documentation of LLM use in research needs community standards, pursued through a proposed Research Data Alliance working group.",
        "claim_type": "methodological_argument",
        "claim_role": "supporting",
        "verbatim_quote": "Finally, the documentation of LLM use in research needs community standards, which we are pursuing through a proposed Research Data Alliance working group.",
        "location": {"section": "6 Conclusion", "page": 24},
        "supported_by": [],
        "supports_claims": ["C018"],
        "notes": ""
    },
    {
        "claim_id": "C182",
        "claim_text": "Conclusion restatement: reliability is a property of the human–AI system with its locus in researcher-built scaffolding, and the builder's epistemic and design burden persisted across a model generation and significant harness evolution.",
        "claim_type": "theoretical",
        "claim_role": "supporting",
        "verbatim_quote": "Reliability is a property of the human–AI system, not just of the model; its locus is the scaffolding the researcher builds around the model, not the model's raw capability. The builder's epistemic and design burden persisted across a model generation and significant harness evolution (Section 5.1).",
        "location": {"section": "6 Conclusion", "page": 24},
        "supported_by": [],
        "supports_claims": ["C001", "C003", "C019"],
        "notes": "Concluding restatement; Pass 2 consolidation candidate."
    },
    {
        "claim_id": "C183",
        "claim_text": "The persistence changes the practical question from when a model will overcome these constraints to how to design research scaffolding and workflows that respect them and leverage what models do well.",
        "claim_type": "interpretation",
        "claim_role": "core",
        "verbatim_quote": "This persistence changes the practical question from when a model will overcome these constraints to how we design research scaffolding and workflows that respect them and leverage what models do well (Section 5.2) Ballsun-Stanton and S. A. Ross, 2026.",
        "location": {"section": "6 Conclusion", "page": 24},
        "supported_by": [],
        "supports_claims": ["C016", "C135"],
        "notes": ""
    },
    {
        "claim_id": "C184",
        "claim_text": "Now and for the foreseeable future these systems augment scholarship rather than automate it; accommodating model limitations through scaffolded human–LLM systems is necessary to unlock their dependable utility.",
        "claim_type": "interpretation",
        "claim_role": "supporting",
        "verbatim_quote": "Now and for the foreseeable future, these systems augment scholarship rather than automate it; accommodating model limitations through the construction of scaffolded human–LLM systems is necessary to unlock the dependable utility they offer (Section 1).",
        "location": {"section": "6 Conclusion", "page": 24},
        "supported_by": [],
        "supports_claims": ["C008", "C007"],
        "notes": "Concluding restatement; Pass 2 consolidation candidate."
    },
]

IMPLICIT_ARGUMENTS = [
    {
        "implicit_argument_id": "IA020",
        "argument_text": "The labs' investment in elaborate scaffolding is best explained by reliability necessity — rather than by product differentiation, capability extension, or market positioning — so it can serve as corroborating evidence for the structural thesis.",
        "type": "bridging_claim",
        "trigger_text": [
            "The fact that the laboratories releasing the most capable models are simultaneously building the most elaborate scaffolding (sub-agents, independent context windows, structured workflows, verifier patterns) is evidence that such an apparatus is necessary for the models to be reliable in non-trivial work."
        ],
        "trigger_locations": [
            {"section": "5.2 Design principles for researcher-builders", "page": 24}
        ],
        "inference_reasoning": "The inference from 'labs build scaffolding' to 'scaffolding is necessary for reliability' requires excluding alternative motives for that investment (feature competition, agentic capability expansion, enterprise workflow demands). The convergence is suggestive corroboration but the necessity reading depends on this unstated premise.",
        "supports_claims": ["C173"],
        "assessment_implications": "A secondary supporting argument for the thesis; its weight depends on how uniquely reliability explains lab behaviour."
    },
]

save_group(
    {
        "group": "G13",
        "section_title": "Discussion 5.2 (end: mandate floor, working with the grain, tooling as evidence) + 5.3 Limitations + 6 Conclusion",
        "page_range": "23-24",
        "estimated_words": 1000,
        "natural_boundary": "Before 'References' (p. 24)",
        "split_rationale": "Final third of the Discussion plus Limitations and Conclusion; under 1,500-word cap."
    },
    evidence=EVIDENCE,
    claims=CLAIMS,
    implicit_arguments=IMPLICIT_ARGUMENTS,
)
