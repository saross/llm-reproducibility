#!/usr/bin/env python3
"""Pass 1, Group G3: Background 2.3 'Reliability as a property of structure' (pp. 4-6, ~1,160 words)."""

from pass1_lib import save_group

EVIDENCE = [
    {
        "evidence_id": "E025",
        "evidence_text": "Compound-AI-systems literature contends that quality and reliability arise not from the model itself but as a property of interacting components — multiple model calls plus retrievers and other external tools (Zaharia et al. 2024).",
        "evidence_type": "literature_citation",
        "verbatim_quote": "A growing body of work on compound AI systems contends that quality and reliability arise not from the model itself, but as a property of interacting components, including multiple calls to one or more models, alongside invocation of retrievers or other external tools (Zaharia et al., 2024).",
        "location": {"section": "2.3 Reliability as a property of structure", "page": 4},
        "supports_claims": ["C051"],
        "notes": ""
    },
    {
        "evidence_id": "E026",
        "evidence_text": "The design of the system governs the outcome (Chen et al. 2024); Wang et al. (2025) argue system outputs do not decompose neatly, so the whole must be aligned jointly.",
        "evidence_type": "literature_citation",
        "verbatim_quote": "The design of the system governs the outcome (Chen et al., 2024);",
        "location": {"section": "2.3 Reliability as a property of structure", "page": 4},
        "supports_claims": ["C051"],
        "notes": "The continuation reporting X. Wang et al. (2025) — 'system outputs do not decompose neatly, so the whole must be aligned jointly, not component by component' — spans the p4/p5 page break in the processed md, so only the pre-break clause is quoted; the Wang content is verifiable against the PDF."
    },
    {
        "evidence_id": "E027",
        "evidence_text": "Pairing a human with a model does not by itself make the result more reliable — on average such pairings underperform the better of the two alone; what governs the outcome is how the collaboration is structured (Vaccaro, Almaatouq, and Malone 2024).",
        "evidence_type": "literature_citation",
        "verbatim_quote": "The principle holds when one of those components is a person: pairing a human with a model does not by itself make the result more reliable (on average such pairings underperform the better of the two alone). What governs the outcome is how the collaboration is structured (Vaccaro, Almaatouq, and Malone, 2024).",
        "location": {"section": "2.3 Reliability as a property of structure", "page": 5},
        "supports_claims": ["C051"],
        "notes": ""
    },
    {
        "evidence_id": "E028",
        "evidence_text": "After initial failures of an integrated approach, the authors split their software-tool research into three steps: tool discovery, tool documentation, and cataloguing tool use evidence.",
        "evidence_type": "observation",
        "verbatim_quote": "After initial failures of an integrated approach, for example, we split our own software tool research into three steps: tool discovery, tool documentation, and cataloguing tool use evidence (Section 4).",
        "location": {"section": "2.3 Reliability as a property of structure", "page": 5},
        "supports_claims": ["C053"],
        "notes": "First-person project observation illustrating decomposition."
    },
    {
        "evidence_id": "E029",
        "evidence_text": "Decomposed prompting breaks a problem into a sequence of smaller model calls (Khot et al. 2022), as do least-to-most (Zhou et al. 2022) and plan-and-solve prompting (Wang et al. 2023).",
        "evidence_type": "literature_citation",
        "verbatim_quote": "Decomposed prompting breaks a problem into a sequence of smaller model calls (Khot et al., 2022), as do least-to-most (Zhou et al., 2022) and plan-and-solve prompting (L. Wang et al., 2023).",
        "location": {"section": "2.3 Reliability as a property of structure", "page": 5},
        "supports_claims": ["C053"],
        "notes": ""
    },
    {
        "evidence_id": "E030",
        "evidence_text": "These techniques extend chain-of-thought and reason-and-act patterns (Bosma et al. 2022; Yao et al. 2022), now built into base models or their harnesses.",
        "evidence_type": "literature_citation",
        "verbatim_quote": "Such techniques extend the chain-of-thought and reason-and-act patterns that preceded them (Bosma et al., 2022; Yao et al., 2022) but are now built into base models or their harnesses.",
        "location": {"section": "2.3 Reliability as a property of structure", "page": 5},
        "supports_claims": ["C053"],
        "notes": ""
    },
    {
        "evidence_id": "E031",
        "evidence_text": "Decomposition's complement is delegation — which sub-tasks the model performs and which the researcher keeps — the division of labour studied in human–AI collaboration literature (Fügener et al. 2022; Dellermann et al. 2019; Hemmer et al. 2025).",
        "evidence_type": "literature_citation",
        "verbatim_quote": "Decomposition's complement is delegation (which sub-tasks the model performs and which the researcher keeps), representing the division of labour studied in the human–AI collaboration literature (Fügener et al., 2022; Dellermann et al., 2019; Hemmer et al., 2025).",
        "location": {"section": "2.3 Reliability as a property of structure", "page": 5},
        "supports_claims": ["C053"],
        "notes": ""
    },
    {
        "evidence_id": "E032",
        "evidence_text": "Prompts assembled as long strings discovered by trial and error are brittle and do not scale (Khattab et al. 2023) — a fair description of the authors' early practice.",
        "evidence_type": "literature_citation",
        "verbatim_quote": "Prompts assembled as long strings discovered by trial and error (a fair description of our early practice) are brittle and do not scale (Khattab et al., 2023).",
        "location": {"section": "2.3 Reliability as a property of structure", "page": 5},
        "supports_claims": ["C055"],
        "notes": "Includes reflexive self-observation."
    },
    {
        "evidence_id": "E033",
        "evidence_text": "Especially on pre-2026 models, prompts were sensitive to apparently trivial choices of wording and format (Schulhoff et al. 2024; Sclar et al. 2023).",
        "evidence_type": "literature_citation",
        "verbatim_quote": "Especially on pre-2026 models, prompts were sensitive to apparently trivial choices of wording and format (Schulhoff et al., 2024; Sclar et al., 2023).",
        "location": {"section": "2.3 Reliability as a property of structure", "page": 5},
        "supports_claims": ["C055"],
        "notes": ""
    },
    {
        "evidence_id": "E034",
        "evidence_text": "A declarative-programming tradition treats the prompt as a program composed of parameterised, reusable modules with explicit output constraints (Khattab et al. 2023; Beurer-Kellner, Fischer, and Vechev 2023).",
        "evidence_type": "literature_citation",
        "verbatim_quote": "In response, a declarative-programming tradition has emerged that treats the prompt as a program, composed of parameterised, reusable modules with explicit output constraints (Khattab et al., 2023; Beurer-Kellner, Fischer, and Vechev, 2023).",
        "location": {"section": "2.3 Reliability as a property of structure", "page": 5},
        "supports_claims": ["C055"],
        "notes": ""
    },
    {
        "evidence_id": "E035",
        "evidence_text": "The authors constrained model output to a declared structure (quoted CSV) for each phased prompt in their research, resting on the structured-output principle (Liu et al. 2024; Geng et al. 2023).",
        "evidence_type": "observation",
        "verbatim_quote": "Constraining a model's output to a declared structure, as we did for the comma-separated values (CSV) output required of each phased prompt in our research, rests on the same principle (Liu et al., 2024; Geng et al., 2023).",
        "location": {"section": "2.3 Reliability as a property of structure", "page": 5},
        "supports_claims": ["C055"],
        "notes": "Mixed first-person practice plus literature grounding."
    },
    {
        "evidence_id": "E036",
        "evidence_text": "Cognition can be offloaded onto the environment (Risko and Gilbert 2016); the cockpit, not the pilots, remembers the speeds at which a descending airliner reconfigures its wings (Hutchins 1995).",
        "evidence_type": "literature_citation",
        "verbatim_quote": "Cognition can be offloaded onto the environment (Risko and Gilbert, 2016): the cockpit, not the pilots, remembers the speeds at which a descending airliner reconfigures its wings (Hutchins, 1995).",
        "location": {"section": "2.3 Reliability as a property of structure", "page": 5},
        "supports_claims": ["C056", "C057"],
        "notes": ""
    },
    {
        "evidence_id": "E037",
        "evidence_text": "The LLM factuality literature emphasises decomposing text outputs into atomic, independently verifiable claims (Min et al. 2023; Wei et al. 2024).",
        "evidence_type": "literature_citation",
        "verbatim_quote": "The LLM factuality literature makes this explicit, emphasising the need to decompose text outputs into atomic, independently verifiable claims (Min et al., 2023; Wei et al., 2024).",
        "location": {"section": "2.3 Reliability as a property of structure", "page": 5},
        "supports_claims": ["C059"],
        "notes": ""
    },
    {
        "evidence_id": "E038",
        "evidence_text": "Recent work treats the granularity of decomposition as the variable governing whether verification succeeds (Lu et al. 2025).",
        "evidence_type": "literature_citation",
        "verbatim_quote": "Recent work treats the granularity of that decomposition as the variable that governs whether verification succeeds (Lu et al., 2025).",
        "location": {"section": "2.3 Reliability as a property of structure", "page": 5},
        "supports_claims": ["C059"],
        "notes": ""
    },
    {
        "evidence_id": "E039",
        "evidence_text": "For human verification, decomposition lowers verification cost, improving human verifier performance (Vasconcelos et al. 2023).",
        "evidence_type": "literature_citation",
        "verbatim_quote": "For human verification, decomposition lowers verification cost, which improves human verifier performance (Vasconcelos et al., 2023).",
        "location": {"section": "2.3 Reliability as a property of structure", "page": 5},
        "supports_claims": ["C059"],
        "notes": ""
    },
    {
        "evidence_id": "E040",
        "evidence_text": "Once work is broken into checkable units, a researcher can audit a sample rather than the whole, as in human review of automated remote sensing (Olofsson et al. 2014).",
        "evidence_type": "literature_citation",
        "verbatim_quote": "Once the work is broken into checkable units a researcher can, for example, audit a sample rather than the whole, as is common practice in human review of automated remote sensing",
        "location": {"section": "2.3 Reliability as a property of structure", "page": 5},
        "supports_claims": ["C059"],
        "notes": "Closing citation '(Olofsson et al., 2014)' spans the p5/p6 page break in the processed md and is omitted from the quote; verifiable against the PDF."
    },
    {
        "evidence_id": "E041",
        "evidence_text": "Each decomposed claim must carry enough context to be checked on its own (Wanner, Van Durme, and Dredze 2025; Hu, Long, and Wang 2025).",
        "evidence_type": "literature_citation",
        "verbatim_quote": "Each claim must therefore carry enough context to be checked on its own (Wanner, Van Durme, and Dredze, 2025; Hu, Long, and W. Wang, 2025).",
        "location": {"section": "2.3 Reliability as a property of structure", "page": 6},
        "supports_claims": ["C061"],
        "notes": ""
    },
    {
        "evidence_id": "E042",
        "evidence_text": "Resampling a single model measures within-model variation but cannot catch consistent errors (Farquhar et al. 2024; Manakul, Liusie, and Gales 2023); a separate examiner in a separate context working from the artefact is needed (Cohen et al. 2023; Dhuliawala et al. 2024).",
        "evidence_type": "literature_citation",
        "verbatim_quote": "Since resampling a single model measures within-model variation but cannot catch errors the model makes consistently (Farquhar et al., 2024; Manakul, Liusie, and Gales, 2023), architectural independence is necessary to catch systematic error: a separate examiner, in a separate context, working from the artefact rather than from the producer's reasoning (Cohen et al., 2023; Dhuliawala et al., 2024).",
        "location": {"section": "2.3 Reliability as a property of structure", "page": 6},
        "supports_claims": ["C064"],
        "notes": "Quote shared with C064 (sentence both cites literature and asserts the paper's requirement)."
    },
    {
        "evidence_id": "E043",
        "evidence_text": "Agreement among sources of common origin is a cue, not a check (Metzger, Flanagin, and Medders 2010).",
        "evidence_type": "literature_citation",
        "verbatim_quote": "Since agreement among sources of common origin is a cue, not a check (Metzger, Flanagin, and Medders, 2010), a verifier must re-ground each claim against independent evidence rather than re-deriving it from the producer's context.",
        "location": {"section": "2.3 Reliability as a property of structure", "page": 6},
        "supports_claims": ["C065"],
        "notes": "Quote shared with C065."
    },
    {
        "evidence_id": "E044",
        "evidence_text": "People evaluate claims by corroborating them across concurring, independent sources (Hilligoss and Rieh 2008).",
        "evidence_type": "literature_citation",
        "verbatim_quote": "People similarly evaluate claims by corroborating them across concurring, independent sources (Hilligoss and Rieh, 2008).",
        "location": {"section": "2.3 Reliability as a property of structure", "page": 6},
        "supports_claims": ["C066"],
        "notes": ""
    },
    {
        "evidence_id": "E045",
        "evidence_text": "Given a fluent claim whose citations are correctly formatted but do not support it (Wu et al. 2025), a producer-parallel check may not detect the error.",
        "evidence_type": "literature_citation",
        "verbatim_quote": "Given a fluent claim whose citations are correctly formatted but do not in fact support it (Wu et al., 2025), a check parallel to the producer (read the claim, confirm the references look apposite) may not detect the error.",
        "location": {"section": "2.3 Reliability as a property of structure", "page": 6},
        "supports_claims": ["C067", "C068"],
        "notes": ""
    },
]

CLAIMS = [
    {
        "claim_id": "C051",
        "claim_text": "Reliability must be engineered into the scaffolding of the human–AI system (endorsing the compound-systems principle for the human-in-the-loop case).",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "verbatim_quote": "Reliability, therefore, must be engineered into the scaffolding of the human–AI system (Ballsun-Stanton and S. A. Ross, 2026).",
        "location": {"section": "2.3 Reliability as a property of structure", "page": 5},
        "supported_by": ["E025", "E026", "E027"],
        "supports_claims": ["C001", "C007"],
        "notes": ""
    },
    {
        "claim_id": "C052",
        "claim_text": "The scaffold has two complementary halves: building judgement into the workflow so the model can do the task, and verifying whether it worked from a position the producer cannot influence.",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "verbatim_quote": "That scaffold has two complementary halves: building judgement into the workflow, so the model can do the task, and verifying whether it worked, from a position the producer cannot influence.",
        "location": {"section": "2.3 Reliability as a property of structure", "page": 5},
        "supported_by": [],
        "supports_claims": ["C051"],
        "notes": "Near-duplicate of C013 (Introduction two-part structure); Pass 2 consolidation candidate."
    },
    {
        "claim_id": "C053",
        "claim_text": "Workflow scaffolding begins with decomposition: the researcher decomposes a task beyond the model's reach until each part falls within model competence.",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "verbatim_quote": "Workflow scaffolding begins with decomposition. Faced with a task beyond the model's reach, the researcher decomposes it until each part falls within model competence.",
        "location": {"section": "2.3 Reliability as a property of structure", "page": 5},
        "supported_by": ["E028", "E029", "E030", "E031"],
        "supports_claims": ["C052"],
        "notes": ""
    },
    {
        "claim_id": "C054",
        "claim_text": "Where a model can manage a task's scope but cannot supply the necessary judgement, the researcher must externalise that judgement.",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "verbatim_quote": "Decomposition, however, is only the first step. Where a model can manage the scope of a task but still cannot supply the necessary judgement, the researcher must externalise it.",
        "location": {"section": "2.3 Reliability as a property of structure", "page": 5},
        "supported_by": [],
        "supports_claims": ["C052"],
        "notes": ""
    },
    {
        "claim_id": "C055",
        "claim_text": "Externalisation makes implicit judgement explicit through custom instructions, prompts, schemas, and constraints — now also durable skill, agent, and workflow definitions — carrying discriminations the model will not make on its own.",
        "claim_type": "methodological_argument",
        "claim_role": "supporting",
        "verbatim_quote": "Externalisation makes implicit judgement explicit by articulating it through custom instructions, prompts, schemas, and constraints (and now into durable skill, agent, and workflow definitions) that carry discriminations the model will not make on its own.",
        "location": {"section": "2.3 Reliability as a property of structure", "page": 5},
        "supported_by": ["E032", "E033", "E034", "E035"],
        "supports_claims": ["C054"],
        "notes": ""
    },
    {
        "claim_id": "C056",
        "claim_text": "Externalising judgement into durable structure is not merely an expedient but an instance of a deeper principle (cognitive offloading / distributed cognition).",
        "claim_type": "theoretical",
        "claim_role": "supporting",
        "verbatim_quote": "Externalising judgement into durable structure is not merely an expedient, but rather an instance of a deeper principle.",
        "location": {"section": "2.3 Reliability as a property of structure", "page": 5},
        "supported_by": ["E036"],
        "supports_claims": ["C054"],
        "notes": ""
    },
    {
        "claim_id": "C057",
        "claim_text": "Scaffolding provided to an LLM can create a cognitive system analogous to environment-offloaded human cognition.",
        "claim_type": "theoretical",
        "claim_role": "supporting",
        "verbatim_quote": "Scaffolding provided to an LLM can create an analogous cognitive system (Clark and Chalmers, 1998).",
        "location": {"section": "2.3 Reliability as a property of structure", "page": 5},
        "supported_by": ["E036"],
        "supports_claims": ["C056"],
        "notes": ""
    },
    {
        "claim_id": "C058",
        "claim_text": "Decomposition and externalisation together form the first half of the structure: judgement built into the workflow before the model runs.",
        "claim_type": "methodological_argument",
        "claim_role": "supporting",
        "verbatim_quote": "Together, decomposition and externalisation are the first half of the structure: judgement built into the workflow before the model runs.",
        "location": {"section": "2.3 Reliability as a property of structure", "page": 5},
        "supported_by": [],
        "supports_claims": ["C052"],
        "notes": ""
    },
    {
        "claim_id": "C059",
        "claim_text": "Verification again requires decomposition: a narrowly scoped output becomes verifiable (does a tool exist, is a metadata field accurate, does a citation evidence a tool's existence).",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "verbatim_quote": "Outputs must then be verified, which again requires decomposition. A narrowly scoped output becomes verifiable: whether a tool exists, whether a metadata field is accurate, whether a citation represents evidence of a tool's existence.",
        "location": {"section": "2.3 Reliability as a property of structure", "page": 5},
        "supported_by": ["E037", "E038", "E039", "E040"],
        "supports_claims": ["C052"],
        "notes": ""
    },
    {
        "claim_id": "C060",
        "claim_text": "A comprehensive report fusing discovery, documentation, and evidence is difficult to verify — by person or machine — until broken into more checkable units.",
        "claim_type": "methodological_argument",
        "claim_role": "supporting",
        "verbatim_quote": "A comprehensive report that fuses discovery, documentation, and evidence is difficult to verify, by a person or a machine, until it is broken into units more amenable to checking.",
        "location": {"section": "2.3 Reliability as a property of structure", "page": 5},
        "supported_by": [],
        "supports_claims": ["C059"],
        "notes": ""
    },
    {
        "claim_id": "C061",
        "claim_text": "Decomposition can go too far: a unit stripped of its context can become unverifiable, so each claim must carry enough context to be checked on its own.",
        "claim_type": "methodological_argument",
        "claim_role": "supporting",
        "verbatim_quote": "This decomposition can go too far, since a unit stripped of its context can become unverifiable.",
        "location": {"section": "2.3 Reliability as a property of structure", "page": 6},
        "supported_by": ["E041"],
        "supports_claims": ["C059"],
        "notes": ""
    },
    {
        "claim_id": "C062",
        "claim_text": "The decomposition that keeps tasks within model competence is also the precondition for verification.",
        "claim_type": "theoretical",
        "claim_role": "supporting",
        "verbatim_quote": "The decomposition that keeps tasks within model competence turns out to be the precondition for verification as well.",
        "location": {"section": "2.3 Reliability as a property of structure", "page": 6},
        "supported_by": [],
        "supports_claims": ["C059", "C053"],
        "notes": ""
    },
    {
        "claim_id": "C063",
        "claim_text": "Decomposition is necessary but not sufficient: because unaided LLM and human review both fail, verification power must come from the compound system, especially independence and external reference.",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "verbatim_quote": "Again, decomposition is necessary but not sufficient; the mechanics of the verification are also important. Unaided LLM (self or second) and human review both fail, so verification power has to come from the compound system, especially independence and external reference.",
        "location": {"section": "2.3 Reliability as a property of structure", "page": 6},
        "supported_by": [],
        "supports_claims": ["C050"],
        "notes": ""
    },
    {
        "claim_id": "C064",
        "claim_text": "Architectural independence is necessary to catch systematic error: a separate examiner, in a separate context, working from the artefact rather than the producer's reasoning.",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "verbatim_quote": "Since resampling a single model measures within-model variation but cannot catch errors the model makes consistently (Farquhar et al., 2024; Manakul, Liusie, and Gales, 2023), architectural independence is necessary to catch systematic error: a separate examiner, in a separate context, working from the artefact rather than from the producer's reasoning (Cohen et al., 2023; Dhuliawala et al., 2024).",
        "location": {"section": "2.3 Reliability as a property of structure", "page": 6},
        "supported_by": ["E042"],
        "supports_claims": ["C063", "C015"],
        "notes": "Quote shared with E042."
    },
    {
        "claim_id": "C065",
        "claim_text": "A verifier must re-ground each claim against independent evidence rather than re-deriving it from the producer's context.",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "verbatim_quote": "Since agreement among sources of common origin is a cue, not a check (Metzger, Flanagin, and Medders, 2010), a verifier must re-ground each claim against independent evidence rather than re-deriving it from the producer's context.",
        "location": {"section": "2.3 Reliability as a property of structure", "page": 6},
        "supported_by": ["E043", "E044"],
        "supports_claims": ["C063", "C015"],
        "notes": "Quote shared with E043."
    },
    {
        "claim_id": "C066",
        "claim_text": "Even an independent verifier must be anchored to an external source.",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "verbatim_quote": "Even an independent verifier must be anchored to an external source.",
        "location": {"section": "2.3 Reliability as a property of structure", "page": 6},
        "supported_by": ["E044"],
        "supports_claims": ["C063"],
        "notes": ""
    },
    {
        "claim_id": "C067",
        "claim_text": "Re-grounding should change the question, not just the questioner: orthogonal framing has the examiner approach the artefact from a different direction.",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "verbatim_quote": "This re-grounding should also change the question, not just the questioner. Orthogonal framing has an examiner approach the artefact from a different direction.",
        "location": {"section": "2.3 Reliability as a property of structure", "page": 6},
        "supported_by": ["E045"],
        "supports_claims": ["C063", "C015"],
        "notes": ""
    },
    {
        "claim_id": "C068",
        "claim_text": "If each cited source is first retrieved and then evaluated for what claims it can actually support, citation errors invisible to producer-parallel checks can be revealed — verification undertaken anew from the evidence.",
        "claim_type": "methodological_argument",
        "claim_role": "supporting",
        "verbatim_quote": "But if each cited source is first retrieved and then evaluated for what claims it can actually support, the error can be revealed. In the latter case, the verification is undertaken anew from the evidence, rather than being captured by a fluent-but-incorrect claim (Gao et al., 2023; Wu et al., 2025).",
        "location": {"section": "2.3 Reliability as a property of structure", "page": 6},
        "supported_by": ["E045"],
        "supports_claims": ["C067"],
        "notes": ""
    },
]

IMPLICIT_ARGUMENTS = [
    {
        "implicit_argument_id": "IA007",
        "argument_text": "Findings from the compound-AI-systems and human–AI teaming literatures (largely engineering and experimental contexts) transfer to individual researcher workflows in long-tail HASS research.",
        "type": "bridging_claim",
        "trigger_text": [
            "A growing body of work on compound AI systems contends that quality and reliability arise not from the model itself, but as a property of interacting components, including multiple calls to one or more models, alongside invocation of retrievers or other external tools (Zaharia et al., 2024).",
            "Reliability, therefore, must be engineered into the scaffolding of the human–AI system (Ballsun-Stanton and S. A. Ross, 2026)."
        ],
        "trigger_locations": [
            {"section": "2.3 Reliability as a property of structure", "page": 4},
            {"section": "2.3 Reliability as a property of structure", "page": 5}
        ],
        "inference_reasoning": "The 'therefore' moves from literature about engineered compound systems and controlled human–AI pairings to a prescription for individual research practice. The step requires an unstated bridge that these system-level findings hold for solo researcher-built scaffolding in idiosyncratic research domains; the paper's episodes then serve as partial demonstration.",
        "supports_claims": ["C051"],
        "assessment_implications": "The strength of the theoretical grounding depends on this transfer; the two episodes provide within-programme support but not independent confirmation across research settings."
    },
    {
        "implicit_argument_id": "IA008",
        "argument_text": "The distributed-cognition analogy carries normative weight: judgement offloaded into scaffolding functions as dependably as instrument-embedded memory does in the cockpit case.",
        "type": "unstated_assumption",
        "trigger_text": [
            "Cognition can be offloaded onto the environment (Risko and Gilbert, 2016): the cockpit, not the pilots, remembers the speeds at which a descending airliner reconfigures its wings (Hutchins, 1995).",
            "Scaffolding provided to an LLM can create an analogous cognitive system (Clark and Chalmers, 1998)."
        ],
        "trigger_locations": [
            {"section": "2.3 Reliability as a property of structure", "page": 5},
            {"section": "2.3 Reliability as a property of structure", "page": 5}
        ],
        "inference_reasoning": "The cockpit analogy is offered as grounding for externalisation, but engineered avionics embed validated, deterministic parameters, whereas researcher-written prompts and schemas encode contestable judgements without equivalent validation regimes. Treating the two as analogous assumes the offloading principle survives this difference.",
        "supports_claims": ["C056", "C057"],
        "assessment_implications": "If the analogy is weaker than presented, externalisation is an empirical design choice to be validated (as the paper's episodes attempt) rather than a principle inherited from distributed-cognition theory."
    },
]

save_group(
    {
        "group": "G3",
        "section_title": "Background 2.3 Reliability as a property of structure",
        "page_range": "4-6",
        "estimated_words": 1160,
        "natural_boundary": "Before 'Methods' heading (Section 3, p. 6)",
        "split_rationale": "Single conceptual subsection; under 1,500-word cap. Two quotes clipped at page-break-spanning citations (E026, E040), noted on the items."
    },
    evidence=EVIDENCE,
    claims=CLAIMS,
    implicit_arguments=IMPLICIT_ARGUMENTS,
)
