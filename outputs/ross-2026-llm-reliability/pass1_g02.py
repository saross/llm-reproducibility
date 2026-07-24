#!/usr/bin/env python3
"""Pass 1, Group G2: Background 2.1-2.2 (pp. 3-4, ~1,230 words).

LLMs-in-research capabilities/debates + the limits of 'disclose and verify'.
Literature-heavy: cited findings extracted as evidence, author assertions as claims.
"""

from pass1_lib import save_group

EVIDENCE = [
    {
        "evidence_id": "E008",
        "evidence_text": "Long-tail research domains (humanities, social science, 'small science') tend to be less standardised, poorly funded, and use a wide range of idiosyncratic data and methods (Borgman 2015; Heidorn 2008).",
        "evidence_type": "literature_citation",
        "verbatim_quote": "Defining LLMs' position on that spectrum is especially important for 'long-tail' (humanities, social science, and 'small science') research, domains which tend to be less standardised, poorly funded, and that utilise a wide range of often idiosyncratic data and methods (Borgman, 2015; Heidorn, 2008).",
        "location": {"section": "2.1 LLMs in research: capabilities and debates", "page": 3},
        "supports_claims": ["C026", "C028"],
        "notes": ""
    },
    {
        "evidence_id": "E009",
        "evidence_text": "Long-tail domains rely on individual-investigator and small-team work where needed resourcing tends to exceed what a project can fund (Borgman 2015; Heidorn 2008).",
        "evidence_type": "literature_citation",
        "verbatim_quote": "On one hand, these domains rely on individual-investigator and small-team work, where the resourcing a project needs tends to exceed what it can fund (Borgman, 2015; Heidorn, 2008).",
        "location": {"section": "2.1 LLMs in research: capabilities and debates", "page": 3},
        "supports_claims": ["C027"],
        "notes": ""
    },
    {
        "evidence_id": "E010",
        "evidence_text": "The LLM debate is framed at poles (capable collaborator vs overhyped tool, Binz et al. 2025), and a genre of practical guidance has formed ('ten simple rules', 'how to embrace AI' advisories: Smith et al. 2024; Lin 2023).",
        "evidence_type": "literature_citation",
        "verbatim_quote": "The debate is often framed at the poles (the LLM as a capable collaborator versus an overhyped and misused tool (Binz et al., 2025)), and from it a genre of practical guidance has formed: the \"ten simple rules\" and \"how to embrace AI\" advisories that answer a real need (Smith et al., 2024; Lin, 2023).",
        "location": {"section": "2.1 LLMs in research: capabilities and debates", "page": 3},
        "supports_claims": ["C033"],
        "notes": ""
    },
    {
        "evidence_id": "E011",
        "evidence_text": "In a controlled comparison, neuroscience experts scored 63.4% at identifying a real abstract versus one altered to change its result while preserving coherence; general-purpose language models scored 81.4% (Luo et al. 2024).",
        "evidence_type": "literature_citation",
        "verbatim_quote": "In a controlled comparison, neuroscience experts scored 63.4 per cent at identifying the real abstract from one altered to change its result while preserving its coherence (for comparison, general-purpose language models scored 81.4 per cent (Luo et al., 2024)).",
        "location": {"section": "2.2 The limits of 'disclose and verify'", "page": 3},
        "supports_claims": ["C035", "C039"],
        "notes": "Quantitative anchor for the expert-verification-limits argument."
    },
    {
        "evidence_id": "E012",
        "evidence_text": "In a direct verification task, readers discriminating correct from incorrect generated text scored only slightly better than chance, even with explanations; higher self-rated expertise conferred no advantage (Steyvers et al. 2025).",
        "evidence_type": "literature_citation",
        "verbatim_quote": "In a direct verification task, readers asked to discriminate between correct and incorrect generated text scored only slightly better than chance, even when that text was accompanied by an explanation, and higher self-rated expertise conferred no advantage (Steyvers et al., 2025).",
        "location": {"section": "2.2 The limits of 'disclose and verify'", "page": 3},
        "supports_claims": ["C039", "C048"],
        "notes": ""
    },
    {
        "evidence_id": "E013",
        "evidence_text": "Readers may inappropriately defer to plausible fabrications (Wilson 1983); confident conversational delivery inflates credibility, fails to trigger suspicion, and discourages systematic review (Anderl et al. 2024; Smith et al. 2024).",
        "evidence_type": "literature_citation",
        "verbatim_quote": "Since LLMs produce confident and fluent prose, readers may inappropriately defer to their plausible fabrications (Wilson, 1983); their conversational, confident delivery inflates credibility and fails to trigger suspicion, thus discouraging systematic review (Anderl et al., 2024; Smith et al., 2024).",
        "location": {"section": "2.2 The limits of 'disclose and verify'", "page": 4},
        "supports_claims": ["C040"],
        "notes": ""
    },
    {
        "evidence_id": "E014",
        "evidence_text": "Readers substitute surface cues or heuristics for the work of real verification (Metzger, Flanagin, and Medders 2010).",
        "evidence_type": "literature_citation",
        "verbatim_quote": "Readers substitute surface cues or heuristics for the work of real verification (Metzger, Flanagin, and Medders, 2010).",
        "location": {"section": "2.2 The limits of 'disclose and verify'", "page": 4},
        "supports_claims": ["C040"],
        "notes": ""
    },
    {
        "evidence_id": "E015",
        "evidence_text": "Disclaimers and citations meant to instigate verification fail to do so in practice (Knor et al. 2026).",
        "evidence_type": "literature_citation",
        "verbatim_quote": "In practice, the disclaimers and citations meant to instigate verification fail to do so (Knor et al., 2026).",
        "location": {"section": "2.2 The limits of 'disclose and verify'", "page": 4},
        "supports_claims": ["C040", "C038"],
        "notes": ""
    },
    {
        "evidence_id": "E016",
        "evidence_text": "A model verifying its own output shares its memory, commitments, and confabulation propensities; self-correction improves only with feedback from outside the model (Huang et al. 2023; Kamoi et al. 2024; Pan et al. 2024).",
        "evidence_type": "literature_citation",
        "verbatim_quote": "A model verifying its own output, however, shares its memory, commitments, and confabulation propensities; any self-check reproduces the error, with self-correction improving only when subject to feedback from outside the model (Huang et al., 2023; Kamoi et al., 2024; Pan et al., 2024).",
        "location": {"section": "2.2 The limits of 'disclose and verify'", "page": 4},
        "supports_claims": ["C042"],
        "notes": "Quote shared with C042 (the sentence both reports literature and asserts the paper's position)."
    },
    {
        "evidence_id": "E017",
        "evidence_text": "Models have self-preference or self-enhancement bias ('narcissism'), preferring their own outputs (Zheng et al. 2023; Dietz et al. 2025).",
        "evidence_type": "literature_citation",
        "verbatim_quote": "Models also have self-preference or self-enhancement bias ('narcissism'), a preference for their own outputs (Zheng et al., 2023; Dietz et al., 2025).",
        "location": {"section": "2.2 The limits of 'disclose and verify'", "page": 4},
        "supports_claims": ["C044"],
        "notes": ""
    },
    {
        "evidence_id": "E018",
        "evidence_text": "If the same model builds or tunes a system and then evaluates it, the judge measures how well the system has met its own preferences ('circularity', Dietz et al. 2025).",
        "evidence_type": "literature_citation",
        "verbatim_quote": "If the same model is used to build or tune a system and then evaluate the system with the same model, the judge will measure how well the system has met its own preferences (Dietz et al., 2025).",
        "location": {"section": "2.2 The limits of 'disclose and verify'", "page": 4},
        "supports_claims": ["C045"],
        "notes": ""
    },
    {
        "evidence_id": "E019",
        "evidence_text": "Models instructed to summarise scientific findings overgeneralised whether or not prompted to work step by step, and overgeneralised more when told not to introduce inaccuracies (Peters and Chin-Yee 2025).",
        "evidence_type": "literature_citation",
        "verbatim_quote": "In one example, models instructed to summarise scientific findings overgeneralised whether or not they were prompted to work \"step by step\" (Peters and Chin-Yee, 2025, p. 3), and overgeneralised more when the prompt added \"do not introduce any inaccuracies\" (Peters and Chin-Yee, 2025, p. 13).",
        "location": {"section": "2.2 The limits of 'disclose and verify'", "page": 4},
        "supports_claims": ["C043"],
        "notes": ""
    },
    {
        "evidence_id": "E020",
        "evidence_text": "LLMs readily abandon correct answers when challenged, even with absurdly invalid arguments (Wang, Yue, and Sun 2023).",
        "evidence_type": "literature_citation",
        "verbatim_quote": "Push-back (confronting the model by declaring its answer to be wrong) is also unreliable; LLMs will readily abandon correct answers when challenged, even with \"absurdly invalid arguments\" (B. Wang, Yue, and Sun, 2023, p. 6).",
        "location": {"section": "2.2 The limits of 'disclose and verify'", "page": 4},
        "supports_claims": ["C043"],
        "notes": ""
    },
    {
        "evidence_id": "E021",
        "evidence_text": "Under unanimous group pressure, humans reverse a correct judgement about a physical referent in front of them (Asch 1956).",
        "evidence_type": "literature_citation",
        "verbatim_quote": "Humans share the propensity: under unanimous group pressure, they reverse a correct judgement about a physical referent in front of them (Asch, 1956).",
        "location": {"section": "2.2 The limits of 'disclose and verify'", "page": 4},
        "supports_claims": ["C043"],
        "notes": "Analogical evidence: push-back unreliability is not unique to models."
    },
    {
        "evidence_id": "E022",
        "evidence_text": "A second model may extend self-preference bias, systematically favouring outputs of particular models, especially those similar to itself (Panickssery, Bowman, and Feng 2024; Gu et al. 2024).",
        "evidence_type": "literature_citation",
        "verbatim_quote": "A second model may instead extend self-preference bias, systematically favouring the outputs of particular models, especially those similar to itself (Panickssery, Bowman, and Feng, 2024; Gu et al., 2024).",
        "location": {"section": "2.2 The limits of 'disclose and verify'", "page": 4},
        "supports_claims": ["C044"],
        "notes": ""
    },
    {
        "evidence_id": "E023",
        "evidence_text": "Models, like people, are swayed by surface cues including length, order of presentation, authoritative tone, and style (Zheng et al. 2023; Gu et al. 2024; Anghel et al. 2025).",
        "evidence_type": "literature_citation",
        "verbatim_quote": "Models, like people, are swayed by surface cues, including length, order of presentation, authoritative tone, and style (Zheng et al., 2023; Gu et al., 2024; Anghel et al., 2025).",
        "location": {"section": "2.2 The limits of 'disclose and verify'", "page": 4},
        "supports_claims": ["C044"],
        "notes": ""
    },
    {
        "evidence_id": "E024",
        "evidence_text": "The study behind this paper had stalled for the better part of a decade for lack of research assistance and was revived using LLMs.",
        "evidence_type": "observation",
        "verbatim_quote": "In our case the study behind this paper had stalled for the better part of a decade for lack of research assistance, and was revived using LLMs (Section 4).",
        "location": {"section": "2.1 LLMs in research: capabilities and debates", "page": 3},
        "supports_claims": ["C034"],
        "notes": "First-person project observation supporting the value-of-LLMs position."
    },
]

CLAIMS = [
    {
        "claim_id": "C025",
        "claim_text": "LLMs lie along a spectrum of agency between an inert tool executing a fixed instruction and an autonomous agent that sets and pursues its own goals.",
        "claim_type": "theoretical",
        "claim_role": "supporting",
        "verbatim_quote": "LLMs lie along a spectrum of agency, somewhere between an inert tool executing a fixed instruction and an autonomous agent that sets and pursues its own goals.",
        "location": {"section": "2.1 LLMs in research: capabilities and debates", "page": 3},
        "supported_by": [],
        "supports_claims": ["C026"],
        "notes": ""
    },
    {
        "claim_id": "C026",
        "claim_text": "Defining LLMs' position on the agency spectrum is especially important for long-tail research.",
        "claim_type": "methodological_argument",
        "claim_role": "supporting",
        "verbatim_quote": "Defining LLMs' position on that spectrum is especially important for 'long-tail' (humanities, social science, and 'small science') research, domains which tend to be less standardised, poorly funded, and that utilise a wide range of often idiosyncratic data and methods (Borgman, 2015; Heidorn, 2008).",
        "location": {"section": "2.1 LLMs in research: capabilities and debates", "page": 3},
        "supported_by": ["E008"],
        "supports_claims": [],
        "notes": "Quote shared with E008 (assertion plus cited characterisation)."
    },
    {
        "claim_id": "C027",
        "claim_text": "In long-tail domains, a generative tool may be the only research assistant available for a project's information work (assembling a literature, compiling an inventory, gathering scattered evidence).",
        "claim_type": "interpretation",
        "claim_role": "supporting",
        "verbatim_quote": "There, a generative tool may be the only research assistant available for the information work a project requires: assembling a literature, compiling an inventory, gathering scattered evidence.",
        "location": {"section": "2.1 LLMs in research: capabilities and debates", "page": 3},
        "supported_by": ["E009"],
        "supports_claims": ["C034"],
        "notes": ""
    },
    {
        "claim_id": "C028",
        "claim_text": "Because long-tail disciplines are heterogeneous, outputs to be assessed vary widely and often require extrinsic rather than intrinsic evaluation.",
        "claim_type": "theoretical",
        "claim_role": "supporting",
        "verbatim_quote": "On the other hand, because these disciplines are heterogeneous, the outputs to be assessed vary widely and often require extrinsic rather than intrinsic evaluation.",
        "location": {"section": "2.1 LLMs in research: capabilities and debates", "page": 3},
        "supported_by": ["E008"],
        "supports_claims": ["C030"],
        "notes": ""
    },
    {
        "claim_id": "C029",
        "claim_text": "These challenges and opportunities, while most acute in long-tail disciplines, extend across domains.",
        "claim_type": "interpretation",
        "claim_role": "supporting",
        "verbatim_quote": "Such challenges and opportunities, while perhaps most acute or immediate in long-tail disciplines, extend across domains.",
        "location": {"section": "2.1 LLMs in research: capabilities and debates", "page": 3},
        "supported_by": [],
        "supports_claims": ["C021"],
        "notes": ""
    },
    {
        "claim_id": "C030",
        "claim_text": "The pivotal challenge is assessing the veracity of LLM outputs in the face of confabulations and other errors.",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "verbatim_quote": "Perhaps the pivotal challenge involves assessing the veracity of LLM outputs in the face of confabulations and other errors.",
        "location": {"section": "2.1 LLMs in research: capabilities and debates", "page": 3},
        "supported_by": [],
        "supports_claims": ["C004"],
        "notes": ""
    },
    {
        "claim_id": "C031",
        "claim_text": "Credibility criteria (accuracy, traceable provenance, verifiable references, internal consistency) apply as much to LLM-generated or joint outputs as to purely human-written ones.",
        "claim_type": "theoretical",
        "claim_role": "supporting",
        "verbatim_quote": "Credibility criteria such as accuracy, traceable provenance, verifiable references, and internal consistency apply as much to an LLM-generated or joint output as to a purely human-written one (Fritch and Cromwell, 2001; Marchionini, 2024).",
        "location": {"section": "2.1 LLMs in research: capabilities and debates", "page": 3},
        "supported_by": [],
        "supports_claims": ["C030"],
        "notes": "Citations (Fritch and Cromwell 2001; Marchionini 2024) embedded in quote."
    },
    {
        "claim_id": "C032",
        "claim_text": "LLMs cannot reliably appraise from within whether they have realised credibility criteria; that judgement, including the truth of the output, must come from outside the model.",
        "claim_type": "theoretical",
        "claim_role": "intermediate",
        "verbatim_quote": "LLMs, however, cannot reliably appraise from within whether they have successfully realised such criteria; that judgement, including the truth of the output, must come from outside the model.",
        "location": {"section": "2.1 LLMs in research: capabilities and debates", "page": 3},
        "supported_by": [],
        "supports_claims": ["C001"],
        "notes": "Background restatement of C002; Pass 2 consolidation candidate."
    },
    {
        "claim_id": "C033",
        "claim_text": "Practical guidance on assessment and credibility tends towards a triad: use the tools, disclose that you did, and expect human readers to judge the output.",
        "claim_type": "interpretation",
        "claim_role": "supporting",
        "verbatim_quote": "Regarding assessment and credibility, their advice tends towards a triad: use the tools, disclose that you did, and expect (human) readers to judge the output.",
        "location": {"section": "2.1 LLMs in research: capabilities and debates", "page": 3},
        "supported_by": ["E010"],
        "supports_claims": ["C004"],
        "notes": "Characterises the position the paper argues against."
    },
    {
        "claim_id": "C034",
        "claim_text": "LLMs are not unsuited to research: generative tools demonstrably do real, valuable information work.",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "verbatim_quote": "We reject the view that LLMs are unsuited to research. Generative tools demonstrably do real, valuable information work.",
        "location": {"section": "2.1 LLMs in research: capabilities and debates", "page": 3},
        "supported_by": ["E024"],
        "supports_claims": ["C036"],
        "notes": ""
    },
    {
        "claim_id": "C035",
        "claim_text": "On the right task with the right scaffolding, LLM capability is demonstrable, in one controlled comparison exceeding domain experts.",
        "claim_type": "interpretation",
        "claim_role": "supporting",
        "verbatim_quote": "On the right task, with the right scaffolding, their capability is demonstrable — in one controlled comparison, exceeding that of domain experts (Luo et al., 2024).",
        "location": {"section": "2.1 LLMs in research: capabilities and debates", "page": 3},
        "supported_by": ["E011"],
        "supports_claims": ["C034"],
        "notes": ""
    },
    {
        "claim_id": "C036",
        "claim_text": "The real question is not whether to use these systems but how to deploy them so research tasks can be completed and output trusted; verification is where practice needs development.",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "verbatim_quote": "The real question is not whether to use these systems but how to deploy them so that research tasks can be completed and their output can be trusted. Verification is where practice needs development.",
        "location": {"section": "2.1 LLMs in research: capabilities and debates", "page": 3},
        "supported_by": [],
        "supports_claims": ["C007"],
        "notes": ""
    },
    {
        "claim_id": "C037",
        "claim_text": "'Disclose and verify' tells a researcher to check but says nothing about how checking can be made to succeed.",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "verbatim_quote": "'Disclose and verify' tells a researcher to check, but says nothing about how checking can be made to succeed.",
        "location": {"section": "2.2 The limits of 'disclose and verify'", "page": 3},
        "supported_by": [],
        "supports_claims": ["C004"],
        "notes": ""
    },
    {
        "claim_id": "C038",
        "claim_text": "Disclosure is necessary but does not ensure reliability on its own: a disclosed confabulation is as fabricated as an undisclosed one, and disclosure alone shifts verification work to the human reader.",
        "claim_type": "methodological_argument",
        "claim_role": "supporting",
        "verbatim_quote": "Disclosure is necessary, but does not ensure reliability on its own: a disclosed confabulation is as fabricated as an undisclosed one. With disclosure alone, the work of verification shifts to the human reader.",
        "location": {"section": "2.2 The limits of 'disclose and verify'", "page": 3},
        "supported_by": ["E015"],
        "supports_claims": ["C037", "C005"],
        "notes": ""
    },
    {
        "claim_id": "C039",
        "claim_text": "Even experts struggle to distinguish a sound finding from a plausible-but-false one in dense prose.",
        "claim_type": "empirical",
        "claim_role": "intermediate",
        "verbatim_quote": "Even experts struggle to distinguish a sound finding from a plausible-but-false one in dense prose.",
        "location": {"section": "2.2 The limits of 'disclose and verify'", "page": 3},
        "supported_by": ["E011", "E012"],
        "supports_claims": ["C006"],
        "notes": "Summarising sentence 'In both of these cases, it proved challenging...' spans the p3/p4 page break in the processed md and was not separately extracted; content covered here."
    },
    {
        "claim_id": "C040",
        "claim_text": "Typical evaluation conditions appear to inhibit or confound readers verifying text.",
        "claim_type": "interpretation",
        "claim_role": "intermediate",
        "verbatim_quote": "Typical evaluation conditions appear to inhibit or confound readers verifying text.",
        "location": {"section": "2.2 The limits of 'disclose and verify'", "page": 4},
        "supported_by": ["E013", "E014", "E015"],
        "supports_claims": ["C006"],
        "notes": ""
    },
    {
        "claim_id": "C041",
        "claim_text": "Careful checking is costly; it may compete with doing the work oneself or be neglected as difficult and boring.",
        "claim_type": "interpretation",
        "claim_role": "supporting",
        "verbatim_quote": "Careful checking is costly; it may compete with simply doing the work oneself, or be neglected as a difficult and possibly boring task.",
        "location": {"section": "2.2 The limits of 'disclose and verify'", "page": 4},
        "supported_by": [],
        "supports_claims": ["C040"],
        "notes": ""
    },
    {
        "claim_id": "C042",
        "claim_text": "A model verifying its own output shares its memory, commitments, and confabulation propensities, so any self-check reproduces the error; self-correction improves only with outside feedback.",
        "claim_type": "theoretical",
        "claim_role": "intermediate",
        "verbatim_quote": "A model verifying its own output, however, shares its memory, commitments, and confabulation propensities; any self-check reproduces the error, with self-correction improving only when subject to feedback from outside the model (Huang et al., 2023; Kamoi et al., 2024; Pan et al., 2024).",
        "location": {"section": "2.2 The limits of 'disclose and verify'", "page": 4},
        "supported_by": ["E016"],
        "supports_claims": ["C047"],
        "notes": "Quote shared with E016."
    },
    {
        "claim_id": "C043",
        "claim_text": "The 'obvious' fixes fail: severity of instruction does not mitigate the problem, and push-back is unreliable.",
        "claim_type": "empirical",
        "claim_role": "intermediate",
        "verbatim_quote": "The 'obvious' fixes to these problems fail. Severity of instruction (asking the model to 'try harder') does not mitigate the problem.",
        "location": {"section": "2.2 The limits of 'disclose and verify'", "page": 4},
        "supported_by": ["E019", "E020", "E021"],
        "supports_claims": ["C047"],
        "notes": ""
    },
    {
        "claim_id": "C044",
        "claim_text": "Delegating the check to a second model does not automatically solve the verification problem.",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "verbatim_quote": "Delegating the check to a second model does not automatically solve this problem.",
        "location": {"section": "2.2 The limits of 'disclose and verify'", "page": 4},
        "supported_by": ["E017", "E022", "E023"],
        "supports_claims": ["C047"],
        "notes": ""
    },
    {
        "claim_id": "C045",
        "claim_text": "An evaluator that takes the producer's output as its premise cannot reliably escape that context to catch errors; it may judge the answer internally plausible given what it was shown rather than externally correct.",
        "claim_type": "theoretical",
        "claim_role": "intermediate",
        "verbatim_quote": "Finally, an evaluator that takes the producer's output as its premise cannot reliably escape that context to catch errors. In such a case, the model may evaluate the answer as internally plausible given what it was shown rather than as externally correct (Zheng et al., 2023; Dietz et al., 2025).",
        "location": {"section": "2.2 The limits of 'disclose and verify'", "page": 4},
        "supported_by": ["E018"],
        "supports_claims": ["C044", "C048"],
        "notes": "Premise-capture argument; grounds the independence-of-context mitigation."
    },
    {
        "claim_id": "C046",
        "claim_text": "The frequent alignment of LLM and human judges reported in the literature may reflect shared failure modes rather than the quality of the model's judgement.",
        "claim_type": "interpretation",
        "claim_role": "supporting",
        "verbatim_quote": "The frequent alignment of LLM and human judges reported in the literature may reflect shared failure modes rather than the quality of the model's judgement (Anghel et al., 2025; Alaofi et al., 2026).",
        "location": {"section": "2.2 The limits of 'disclose and verify'", "page": 4},
        "supported_by": [],
        "supports_claims": ["C044"],
        "notes": "Citations embedded in quote."
    },
    {
        "claim_id": "C047",
        "claim_text": "Neither unaided human review nor naive machine verification is a reliable backstop; both are captured by persuasive artefacts or compromised by shared context.",
        "claim_type": "interpretation",
        "claim_role": "intermediate",
        "verbatim_quote": "Neither unaided human review nor naive machine verification is a reliable backstop; both are captured by persuasive artefacts or compromised by shared context.",
        "location": {"section": "2.2 The limits of 'disclose and verify'", "page": 4},
        "supported_by": [],
        "supports_claims": ["C004", "C050"],
        "notes": "Synthesis of the Section 2.2 argument."
    },
    {
        "claim_id": "C048",
        "claim_text": "Independence of context is necessary but not sufficient: fully independent human readers still detect error at close to chance.",
        "claim_type": "interpretation",
        "claim_role": "intermediate",
        "verbatim_quote": "Independence of context is necessary, but not sufficient: the human readers described by Steyvers et al. (2025) are fully independent, but their detection of error still sits close to chance.",
        "location": {"section": "2.2 The limits of 'disclose and verify'", "page": 4},
        "supported_by": ["E012"],
        "supports_claims": ["C050"],
        "notes": ""
    },
    {
        "claim_id": "C049",
        "claim_text": "Independence must be operationalised as process and complemented by explicit reference to an external source of truth.",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "verbatim_quote": "Independence must be operationalised as process and complemented by explicit reference to an external source of truth.",
        "location": {"section": "2.2 The limits of 'disclose and verify'", "page": 4},
        "supported_by": [],
        "supports_claims": ["C050"],
        "notes": ""
    },
    {
        "claim_id": "C050",
        "claim_text": "Identifying error is a property of compound structures that ensure context independence and measure against an external source, not of disclosure plus expert judgement.",
        "claim_type": "methodological_argument",
        "claim_role": "core",
        "verbatim_quote": "The default approach to AI in research relies on disclosure and expert judgement to separate truth from error; we argue instead that identifying error is a property of compound structures that ensure context independence and measure against an external source.",
        "location": {"section": "2.2 The limits of 'disclose and verify'", "page": 4},
        "supported_by": [],
        "supports_claims": ["C007", "C016"],
        "notes": "Section 2.2's culminating thesis: the mechanism behind C007."
    },
]

IMPLICIT_ARGUMENTS = [
    {
        "implicit_argument_id": "IA005",
        "argument_text": "Findings from constrained laboratory verification tasks (abstract discrimination, generated-text judgement) generalise to real-world expert verification of LLM-assisted research outputs.",
        "type": "bridging_claim",
        "trigger_text": [
            "In a controlled comparison, neuroscience experts scored 63.4 per cent at identifying the real abstract from one altered to change its result while preserving its coherence (for comparison, general-purpose language models scored 81.4 per cent (Luo et al., 2024)).",
            "In a direct verification task, readers asked to discriminate between correct and incorrect generated text scored only slightly better than chance, even when that text was accompanied by an explanation, and higher self-rated expertise conferred no advantage (Steyvers et al., 2025).",
            "Even experts struggle to distinguish a sound finding from a plausible-but-false one in dense prose."
        ],
        "trigger_locations": [
            {"section": "2.2 The limits of 'disclose and verify'", "page": 3},
            {"section": "2.2 The limits of 'disclose and verify'", "page": 3},
            {"section": "2.2 The limits of 'disclose and verify'", "page": 3}
        ],
        "inference_reasoning": "The argument that unaided expert verification fails for research use rests on two cited experiments in artificial discrimination settings. Extending those results to working researchers verifying LLM-assisted outputs in their own domain (with more context, stakes, and time) requires an unstated bridge about task representativeness.",
        "supports_claims": ["C039", "C006"],
        "assessment_implications": "If real verification contexts differ materially from the lab tasks (motivation, domain familiarity, access to sources), the insufficiency claim may overstate; the paper's own episodes provide partial ecological support."
    },
    {
        "implicit_argument_id": "IA006",
        "argument_text": "A reliable external source of truth exists, is identifiable, and is itself trustworthy for the research tasks in question — verification can be anchored to it.",
        "type": "unstated_assumption",
        "trigger_text": [
            "Independence must be operationalised as process and complemented by explicit reference to an external source of truth.",
            "The default approach to AI in research relies on disclosure and expert judgement to separate truth from error; we argue instead that identifying error is a property of compound structures that ensure context independence and measure against an external source."
        ],
        "trigger_locations": [
            {"section": "2.2 The limits of 'disclose and verify'", "page": 4},
            {"section": "2.2 The limits of 'disclose and verify'", "page": 4}
        ],
        "inference_reasoning": "The prescription to measure against an external source assumes such sources (registries, bibliographic databases, catalogues) exist for the task, can be queried reliably, and are themselves accurate. The 2026 episode later shows partial grounding failing, which the paper addresses, but the availability and adequacy of external anchors is assumed rather than argued in Section 2.2.",
        "supports_claims": ["C049", "C050"],
        "assessment_implications": "For tasks lacking authoritative registries (much interpretive HASS work), the compound-structure prescription may not transfer; scope of the thesis depends on this assumption."
    },
]

save_group(
    {
        "group": "G2",
        "section_title": "Background 2.1 (LLMs in research) + 2.2 (The limits of 'disclose and verify')",
        "page_range": "3-4",
        "estimated_words": 1230,
        "natural_boundary": "Before '2.3 Reliability as a property of structure' heading (p. 4)",
        "split_rationale": "Two Background subsections combined; total under 1,500-word cap. One summarising sentence spanning the p3/p4 page break left unextracted (content covered by C039), noted on C039."
    },
    evidence=EVIDENCE,
    claims=CLAIMS,
    implicit_arguments=IMPLICIT_ARGUMENTS,
)
