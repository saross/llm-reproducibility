#!/usr/bin/env python3
"""Pass 1, Group G11: Discussion 5 (opening) + 5.1 Persistence finding + 5.2 opening (pp. 19-20, ~1,285 words)."""

from pass1_lib import save_group

EVIDENCE = [
    {
        "evidence_id": "E179",
        "evidence_text": "Ecosystem changes between episodes were substantial: Claude Opus 4.6's capability substantially exceeded the research-mode services of early 2025, and the scaffolding apparatus was richer.",
        "evidence_type": "observation",
        "verbatim_quote": "Changes to the LLM ecosystem were substantial between episodes. The baseline model was stronger: Claude Opus 4.6's capability substantially exceeded that of the research-mode services of the first half of 2025. The scaffolding apparatus was richer.",
        "location": {"section": "5.1 The persistence finding", "page": 19},
        "supports_claims": ["C120", "C132"],
        "notes": ""
    },
    {
        "evidence_id": "E180",
        "evidence_text": "Where 2025 offered prompts, system instructions, process checklists, and human checkpoints, 2026 added declarative agent definitions, sub-agents in independent contexts, externalised skills, helper scripts, and API integrations supplying authoritative external tools.",
        "evidence_type": "observation",
        "verbatim_quote": "Where 2025 offered prompts, system instructions, process checklists, and human checkpoints, 2026 added declarative agent definitions, sub-agents in independent contexts, externalised skills, helper scripts for mechanical or deterministic tasks, and API integrations supplying authoritative external tools (Section 3.2).",
        "location": {"section": "5.1 The persistence finding", "page": 19},
        "supports_claims": ["C120", "C121"],
        "notes": ""
    },
    {
        "evidence_id": "E181",
        "evidence_text": "The 2025 prompts were procedural in aspiration (schemas, controlled vocabularies, explicit verification steps) but relied on downstream human or ad hoc verification; the 2026 scaffolding made the same commitments binding in execution and added automated verification.",
        "evidence_type": "observation",
        "verbatim_quote": "The 2025 prompts were already procedural in aspiration (schemas, controlled vocabularies, explicit verification steps), but relied on downstream human or ad hoc human–LLM verification (followed by human spot-checking). The 2026 scaffolding made the same commitments binding in execution (Khattab et al., 2023; Beurer-Kellner, Fischer, and Vechev, 2023) and added automated verification employing the principles outlined in the second half of this section.",
        "location": {"section": "5.1 The persistence finding", "page": 19},
        "supports_claims": ["C121", "C122"],
        "notes": ""
    },
    {
        "evidence_id": "E182",
        "evidence_text": "Blocked-action behaviour across episodes: in 2025 a system silently dropped out of research mode and simulated results (caught only by human monitoring); in 2026 a proposer unable to dispatch its verifier improvised the verifier's procedure, ran real queries, and caught a real error.",
        "evidence_type": "observation",
        "verbatim_quote": "In 2025, when asked to search a batch of journal issues, some of which did not exist, a system dropped out of research mode and silently simulated results rather than searching, and the fabrication surfaced only during human monitoring. In 2026, when an architectural constraint prevented a proposer agent from dispatching its verifier to audit its draft report, the agent improvised the verifier's procedure, ran real queries, and caught a real error doing so (Sections 4.2 and 4.5).",
        "location": {"section": "5.1 The persistence finding", "page": 19},
        "supports_claims": ["C123", "C124"],
        "notes": ""
    },
    {
        "evidence_id": "E183",
        "evidence_text": "Part of the 2026 improvement was architectural: the agent failed inside a workflow that declared what verification required and why, so its improvisation had a procedure to reach for and no room to conceal the substitution.",
        "evidence_type": "observation",
        "verbatim_quote": "Part of the improvement was also architectural: the 2026 agent failed inside a workflow that declared what verification required and why, so its improvisation had a procedure to reach for and no room to conceal the substitution.",
        "location": {"section": "5.1 The persistence finding", "page": 19},
        "supports_claims": ["C124"],
        "notes": ""
    },
    {
        "evidence_id": "E184",
        "evidence_text": "Cross-episode parallel: 2025 evidence records with genuine source/URL/tool concealed isolated fabrications (invented release events, misattributed claims); the 2026 agent's first run returned correct registry-retrieved DOIs and titles alongside author fields and citation counts synthesised from memory.",
        "evidence_type": "observation",
        "verbatim_quote": "In 2025, evidence records whose source, URL, or tool was genuine nevertheless concealed isolated fabrications, such as an invented release event or a misattributed claim (Section 4.4). In 2026, the literature-search agent's first run returned correct, registry-retrieved DOIs and titles, but also author fields synthesised from memory and wrong in most spot-checked rows, and citation counts likewise synthesised rather than retrieved (Section 4.5).",
        "location": {"section": "5.1 The persistence finding", "page": 19},
        "supports_claims": ["C125", "C119", "C132"],
        "notes": ""
    },
    {
        "evidence_id": "E185",
        "evidence_text": "When the registry record itself carried the wrong author order, re-querying it repeated the error, but an additional, independent source exposed it.",
        "evidence_type": "observation",
        "verbatim_quote": "The 2026 episode also extended one of them: when the registry record itself carried the wrong author order, re-querying it repeated the error, but an additional, independent source exposed it.",
        "location": {"section": "5.1 The persistence finding", "page": 20},
        "supports_claims": ["C128", "C129"],
        "notes": ""
    },
    {
        "evidence_id": "E186",
        "evidence_text": "The literature-search agent's constraints and self-checks all ran and still passed confabulated output, as the self-correction literature predicts; the failure emerged only in authentic use.",
        "evidence_type": "observation",
        "verbatim_quote": "In the case of the literature-search agent, the agent's constraints and self-checks all ran and still passed confabulated output, as the self-correction literature predicts (Huang et al., 2023; Kamoi et al., 2024; Pan et al., 2024) (Section 4.5). This failure emerged only in authentic use, during an actual literature search.",
        "location": {"section": "5.1 The persistence finding", "page": 20},
        "supports_claims": ["C130", "C131", "C042"],
        "notes": ""
    },
    {
        "evidence_id": "E187",
        "evidence_text": "The authors have since experienced the same build→fail→fix shape in other skill- and agent-building work, corroborating the documented episodes.",
        "evidence_type": "observation",
        "verbatim_quote": "We have since experienced the same build →fail →fix shape in other skill- and agent-building work, corroborating the episodes documented here.",
        "location": {"section": "5.1 The persistence finding", "page": 20},
        "supports_claims": ["C132"],
        "notes": "Informal corroboration beyond the two documented episodes."
    },
    {
        "evidence_id": "E188",
        "evidence_text": "Tool documentation was most reliable proceeding tool by tool, one CSV row at a time; tool discovery when examining journal issues in small blocks.",
        "evidence_type": "observation",
        "verbatim_quote": "Our tool documentation was most reliable when it proceeded tool by tool, one CSV row at a time, and tool discovery when it examined journal issues in small blocks (Sections 3.1, 4.2, and 4.3).",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 20},
        "supports_claims": ["C137"],
        "notes": ""
    },
    {
        "evidence_id": "E189",
        "evidence_text": "When the complete output of one model was handed to another for checking, the second model reproduced its fabrications one-for-one despite being a different model in 'fresh context'.",
        "evidence_type": "observation",
        "verbatim_quote": "When we handed the complete output of one model to another for checking, the second model reproduced its fabrications one-for-one, though it was a different model running in 'fresh context' (Section 4.2).",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 20},
        "supports_claims": ["C137", "C139", "C094"],
        "notes": ""
    },
]

CLAIMS = [
    {
        "claim_id": "C119",
        "claim_text": "The two episodes share a failure at the synthesis boundary, and mitigations rely on independence of context, external re-grounding, and orthogonal framing rather than stronger instruction; these characteristics persisted across a model generation and a tooling regime.",
        "claim_type": "interpretation",
        "claim_role": "intermediate",
        "verbatim_quote": "The two episodes described above share a failure at the synthesis boundary, where retrieved evidence ends and the model's own composition begins. Mitigations rely on independence of context, external re-grounding, and orthogonal framing rather than stronger instruction. These shared characteristics persisted across a model generation and a tooling regime.",
        "location": {"section": "5 Discussion", "page": 19},
        "supported_by": ["E184"],
        "supports_claims": ["C014", "C015", "C019"],
        "notes": "Discussion restatement of the central findings; Pass 2 consolidation candidate."
    },
    {
        "claim_id": "C120",
        "claim_text": "The similarity between episodes represents persistence rather than continuity: the same pattern of failure modes and mitigations recurs even as model and harness improve.",
        "claim_type": "interpretation",
        "claim_role": "intermediate",
        "verbatim_quote": "This similarity represents persistence rather than continuity: not only does the work resemble its earlier self, but the same pattern (failure modes and mitigations) recurs even as the model and harness improve.",
        "location": {"section": "5.1 The persistence finding", "page": 19},
        "supported_by": ["E179", "E180"],
        "supports_claims": ["C019"],
        "notes": ""
    },
    {
        "claim_id": "C121",
        "claim_text": "Between episodes, guards moved out of the prompt and into the workflow.",
        "claim_type": "empirical",
        "claim_role": "intermediate",
        "verbatim_quote": "Guards moved out of the prompt and into the workflow.",
        "location": {"section": "5.1 The persistence finding", "page": 19},
        "supported_by": ["E180", "E181"],
        "supports_claims": ["C019", "C022"],
        "notes": ""
    },
    {
        "claim_id": "C122",
        "claim_text": "The richer 2026 apparatus extended what could be produced reliably: literature search, the one 2025 stage no scaffold made reliable, was successfully implemented a year later.",
        "claim_type": "empirical",
        "claim_role": "intermediate",
        "verbatim_quote": "The richer 2026 apparatus also extended what outputs could be produced reliably: literature search, the one 2025 stage whose output no scaffold made reliable (Section 4.1), was successfully implemented a year later.",
        "location": {"section": "5.1 The persistence finding", "page": 19},
        "supported_by": ["E181", "E173", "E174"],
        "supports_claims": ["C015"],
        "notes": ""
    },
    {
        "claim_id": "C123",
        "claim_text": "What improved between episodes was the gracefulness of degradation, not the need for the guard.",
        "claim_type": "interpretation",
        "claim_role": "intermediate",
        "verbatim_quote": "What improved was the gracefulness of degradation, not the need for the guard.",
        "location": {"section": "5.1 The persistence finding", "page": 19},
        "supported_by": ["E182"],
        "supports_claims": ["C120", "C019"],
        "notes": ""
    },
    {
        "claim_id": "C124",
        "claim_text": "Improvisation when an action is blocked appears to inherit the shape of its scaffold.",
        "claim_type": "interpretation",
        "claim_role": "intermediate",
        "verbatim_quote": "Improvisation when an action is blocked appears to inherit the shape of its scaffold.",
        "location": {"section": "5.1 The persistence finding", "page": 19},
        "supported_by": ["E182", "E183"],
        "supports_claims": ["C123", "C003"],
        "notes": ""
    },
    {
        "claim_id": "C125",
        "claim_text": "The failure mode persisted: in both the 2025 evidence collection and the 2026 agent's first run, grounded retrieval was paired with synthesised narrative and confabulation entered at the synthesis boundary.",
        "claim_type": "empirical",
        "claim_role": "intermediate",
        "verbatim_quote": "The failure mode, however, persisted. In both the 2025 evidence collection and the 2026 agent's first run, grounded retrieval was paired with synthesised narrative, and confabulation entered at the synthesis boundary.",
        "location": {"section": "5.1 The persistence finding", "page": 19},
        "supported_by": ["E184"],
        "supports_claims": ["C014"],
        "notes": "Restates C014 with the cross-episode mechanism; Pass 2 consolidation candidate."
    },
    {
        "claim_id": "C126",
        "claim_text": "Formal thoroughness amplified confabulations: credibility signals covered grounded and ungrounded fields alike, since nothing in the presentation distinguished them.",
        "claim_type": "interpretation",
        "claim_role": "intermediate",
        "verbatim_quote": "Formal thoroughness amplified confabulations. Credibility signals covered grounded and ungrounded fields alike, since nothing in the presentation distinguished them.",
        "location": {"section": "5.1 The persistence finding", "page": 19},
        "supported_by": ["E167"],
        "supports_claims": ["C127", "C006"],
        "notes": ""
    },
    {
        "claim_id": "C127",
        "claim_text": "Incomplete grounding may improve outputs field by field, but a reader assigns credibility to an artefact as a whole — so partial grounding can make residual fabrication more dangerous.",
        "claim_type": "interpretation",
        "claim_role": "intermediate",
        "verbatim_quote": "Incomplete grounding may improve outputs field by field, but a reader assigns credibility to an artefact as a whole.",
        "location": {"section": "5.1 The persistence finding", "page": 19},
        "supported_by": ["E167"],
        "supports_claims": ["C006", "C016"],
        "notes": "The following sentence (trust growing faster than verification warrants; nine-tenths-grounded output more dangerous than an obviously flawed one) spans the p19/p20 page break; verifiable against the PDF."
    },
    {
        "claim_id": "C128",
        "claim_text": "The three mitigations employed informally in 2025 were each still crucial in 2026: the guard properties, not just the failure mode, carried over, while the approach matured from improvised practice to designed verification.",
        "claim_type": "empirical",
        "claim_role": "intermediate",
        "verbatim_quote": "We first employed the three mitigations identified in Section 2 informally in 2025, and each was still crucial in 2026 (Section 4.5). The guard properties, not just the failure mode, carried over, while the approach matured from improvised practice to designed verification.",
        "location": {"section": "5.1 The persistence finding", "page": 20},
        "supported_by": ["E185"],
        "supports_claims": ["C015", "C019"],
        "notes": ""
    },
    {
        "claim_id": "C129",
        "claim_text": "The independence principle, applied in 2025 to contexts, worked equally well for sources.",
        "claim_type": "empirical",
        "claim_role": "intermediate",
        "verbatim_quote": "The independence principle, applied in 2025 to contexts, worked equally well for sources.",
        "location": {"section": "5.1 The persistence finding", "page": 20},
        "supported_by": ["E185"],
        "supports_claims": ["C128", "C015"],
        "notes": ""
    },
    {
        "claim_id": "C130",
        "claim_text": "The experience of constructing systems persisted: build the tool, run it on a real task, manually observe and characterise the failure, design a scaffold around it, re-test.",
        "claim_type": "empirical",
        "claim_role": "intermediate",
        "verbatim_quote": "The experience of constructing systems also persisted: build the tool, run it on a real task, manually observe and characterise the failure, design a scaffold around it, re-test.",
        "location": {"section": "5.1 The persistence finding", "page": 20},
        "supported_by": ["E186", "E187"],
        "supports_claims": ["C019"],
        "notes": ""
    },
    {
        "claim_id": "C131",
        "claim_text": "Latent judgement the model demonstrably possesses (distinguishing grounded retrieval from synthesised recall when a verifier forces the comparison) was elicited only once scaffolding made that distinction structural rather than implicit.",
        "claim_type": "interpretation",
        "claim_role": "core",
        "verbatim_quote": "Latent judgement the model demonstrably possesses (it can tell a grounded retrieval from a synthesised recall when a verifier forces the comparison) was elicited only once the scaffolding made that distinction structural rather than implicit.",
        "location": {"section": "5.1 The persistence finding", "page": 20},
        "supported_by": ["E172", "E186"],
        "supports_claims": ["C001", "C003"],
        "notes": "Key interpretive move: capability exists but is elicited by structure — the thesis in miniature."
    },
    {
        "claim_id": "C132",
        "claim_text": "The economical explanation of the persistence is that the deficiencies are structural, not a characteristic of particular models or harnesses.",
        "claim_type": "interpretation",
        "claim_role": "core",
        "verbatim_quote": "The economical explanation is that the deficiencies are structural, not a characteristic of particular models or harnesses.",
        "location": {"section": "5.1 The persistence finding", "page": 20},
        "supported_by": ["E179", "E184", "E187"],
        "supports_claims": ["C016"],
        "notes": ""
    },
    {
        "claim_id": "C133",
        "claim_text": "The structural conclusion is argued rather than proven: two episodes are not a sample, and a case study's value is situated depth rather than statistical generalisability.",
        "claim_type": "methodological_argument",
        "claim_role": "supporting",
        "verbatim_quote": "We argue this rather than prove it: two episodes are not a sample, and a case study's value is situated depth rather than statistical generalisability (Section 3.3).",
        "location": {"section": "5.1 The persistence finding", "page": 20},
        "supported_by": [],
        "supports_claims": ["C132", "C076"],
        "notes": "Explicit epistemic self-limitation on the core interpretive claim."
    },
    {
        "claim_id": "C134",
        "claim_text": "The working expectation is that these limitations will continue alongside capability improvements; a builder who expects the burden to persist will design differently from one who waits for it to lift.",
        "claim_type": "interpretation",
        "claim_role": "intermediate",
        "verbatim_quote": "Our working expectation is that these limitations will continue alongside capability improvements; a builder who expects this burden to persist will design differently from one who waits for it to lift.",
        "location": {"section": "5.1 The persistence finding", "page": 20},
        "supported_by": [],
        "supports_claims": ["C016", "C135"],
        "notes": ""
    },
    {
        "claim_id": "C135",
        "claim_text": "Researchers cannot simply wait for a better model; reliability should be built into the architecture of LLM-based research systems.",
        "claim_type": "methodological_argument",
        "claim_role": "core",
        "verbatim_quote": "Researchers cannot simply 'wait for a better model' to supply the capabilities and judgement necessary to avoid confabulations and other errors. Instead, reliability should be built into the architecture of LLM-based research systems (Zaharia et al., 2024; Ballsun-Stanton and S. A. Ross, 2026).",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 20},
        "supported_by": [],
        "supports_claims": ["C007", "C016"],
        "notes": ""
    },
    {
        "claim_id": "C136",
        "claim_text": "Reliability rests on three architectural questions: where the work runs (independence), what its output rests on (external re-grounding), and what question the check asks (orthogonal framing).",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "verbatim_quote": "This reliability rests on how three architectural questions are answered: where the work runs (independence); what its output rests on (external re-grounding); and what question the check asks (orthogonal framing).",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 20},
        "supported_by": [],
        "supports_claims": ["C135", "C015"],
        "notes": ""
    },
    {
        "claim_id": "C137",
        "claim_text": "Reliability depends upon the architecture of attention rather than the wording of instructions.",
        "claim_type": "theoretical",
        "claim_role": "intermediate",
        "verbatim_quote": "Reliability depends upon the architecture of attention rather than the wording of instructions.",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 20},
        "supported_by": ["E188", "E189"],
        "supports_claims": ["C136"],
        "notes": "Independence-of-context principle statement."
    },
    {
        "claim_id": "C138",
        "claim_text": "A model rereading its own prior reasoning takes its earlier commitments as given and cannot reliably question them.",
        "claim_type": "theoretical",
        "claim_role": "supporting",
        "verbatim_quote": "A model rereading its own prior reasoning takes its earlier commitments as given and cannot reliably question them (Zheng et al., 2023; Dietz et al., 2025).",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 20},
        "supported_by": [],
        "supports_claims": ["C137"],
        "notes": "Citations embedded in quote."
    },
    {
        "claim_id": "C139",
        "claim_text": "Context freshness alone is not enough: a verifier can still be captured by the artefact it audits.",
        "claim_type": "theoretical",
        "claim_role": "intermediate",
        "verbatim_quote": "Freshness alone is not enough, however: a verifier can still be captured by the artefact it audits (Gu et al., 2024; Anghel et al., 2025).",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 20},
        "supported_by": ["E189"],
        "supports_claims": ["C137", "C094"],
        "notes": ""
    },
]

IMPLICIT_ARGUMENTS = [
    {
        "implicit_argument_id": "IA018",
        "argument_text": "No alternative explanation — such as shared builder practices, prompting habits, or blind spots carried by the same team across both episodes — accounts for the recurrence as economically as structural deficiency does.",
        "type": "bridging_claim",
        "trigger_text": [
            "The economical explanation is that the deficiencies are structural, not a characteristic of particular models or harnesses.",
            "We have since experienced the same build →fail →fix shape in other skill- and agent-building work, corroborating the episodes documented here."
        ],
        "trigger_locations": [
            {"section": "5.1 The persistence finding", "page": 20},
            {"section": "5.1 The persistence finding", "page": 20}
        ],
        "inference_reasoning": "The inference to the best explanation treats structural deficiency as the most economical account of cross-episode recurrence. Both episodes and the corroborating experience come from the same research team, so team-level constants (task selection, prompting style, verification standards) are not excluded as alternative common causes; the argument's force rests on parsimony plus the literature convergence rather than on ruling these out.",
        "supports_claims": ["C132"],
        "assessment_implications": "The paper concedes 'argue rather than prove' (C133); independent replication by other teams would discriminate structural deficiency from team-level constancy."
    },
]

save_group(
    {
        "group": "G11",
        "section_title": "Discussion 5 (opening) + 5.1 The persistence finding + 5.2 opening (independence of context)",
        "page_range": "19-20",
        "estimated_words": 1285,
        "natural_boundary": "p20/p21 page boundary (mid-5.2, before the 2025-evidence-check detail)",
        "split_rationale": "Discussion (~3,700 words) split into three groups; G11/G12 boundary at the p20/p21 page break, the nearest paragraph boundary to the subsection break."
    },
    evidence=EVIDENCE,
    claims=CLAIMS,
    implicit_arguments=IMPLICIT_ARGUMENTS,
)
