#!/usr/bin/env python3
"""Pass 1, Group G12: Discussion 5.2 design principles (pp. 21-22, ~1,340 words)."""

from pass1_lib import save_group

EVIDENCE = [
    {
        "evidence_id": "E190",
        "evidence_text": "Guard B received the whole drafted report but was bound to re-derive every claim from a live registry query and emit an auditable comparison — a fact-checker who never talks to the writer, for whom the report is an agenda but not evidence.",
        "evidence_type": "observation",
        "verbatim_quote": "The 2026 verifier, Guard B, received the whole drafted report but was bound to re-derive every claim from a live registry query and emit an auditable comparison: a fact-checker who never talks to the writer, for whom the report is an agenda but not evidence (Section 4.5).",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 21},
        "supports_claims": ["C140"],
        "notes": ""
    },
    {
        "evidence_id": "E191",
        "evidence_text": "Both verification examples combined independence with re-grounding: each verdict terminated outside the model, in a live registry response or retrieved source rather than in an LLM's recall.",
        "evidence_type": "observation",
        "verbatim_quote": "Both verification examples above combined independence with re-grounding. Each verdict terminated outside the model, in a live registry response or a retrieved source rather than in an LLM's recall.",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 21},
        "supports_claims": ["C142"],
        "notes": ""
    },
    {
        "evidence_id": "E192",
        "evidence_text": "Guard A grounded the proposer itself: drafting could begin only from freshly retrieved metadata, never from recall; single-field errors still occurred but wholesale fabrication was eliminated.",
        "evidence_type": "observation",
        "verbatim_quote": "Guard A of the 2026 workflow grounded the proposer itself: drafting could begin only from freshly retrieved metadata, never from recall. Although single-field errors still occurred, this mitigation eliminated wholesale fabrication (Section 4.5).",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 21},
        "supports_claims": ["C142"],
        "notes": ""
    },
    {
        "evidence_id": "E193",
        "evidence_text": "Tool documentation doubled as an orthogonal check on discovery accuracy: asking for repository, licence, version, and other metadata made misattributions and granularity errors trivially visible in outputs that had already survived discovery verification.",
        "evidence_type": "observation",
        "verbatim_quote": "Tool documentation doubled as such a check on the accuracy of discovery: asking for a tool's repository, licence, version, and other metadata made misattributions and granularity errors trivially visible in outputs that had already survived discovery verification (Section 4.3).",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 21},
        "supports_claims": ["C144", "C145", "C101"],
        "notes": ""
    },
    {
        "evidence_id": "E194",
        "evidence_text": "The 2026 improvised check isolates the orthogonal-framing effect: a changed question in the same context caught a registry-seeded error.",
        "evidence_type": "observation",
        "verbatim_quote": "The improvised check implemented by the model when its verifier could not be dispatched in 2026 isolates this effect: a changed question in the same context caught a registryseeded error (Section 4.5).",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 21},
        "supports_claims": ["C144", "C145"],
        "notes": "'registryseeded' preserves a line-break artefact of the processed md."
    },
    {
        "evidence_id": "E195",
        "evidence_text": "A 'never fabricate' instruction failed to prevent fabricated results in the 2026 proposer while a required grounded-retrieval step succeeded; in 2025, structured prompts with explicit constraints (output schemas) rather than stronger appeals lowered error rates.",
        "evidence_type": "observation",
        "verbatim_quote": "Where a \"never fabricate\" instruction failed to prevent fabricated results in the 2026 proposer agent (Section 4.5), a requirement to use output from a grounded-retrieval step succeeded. Likewise, in 2025, structured prompts with explicit constraints such as output schemas (Liu et al., 2024; Geng et al., 2023), rather than stronger appeals, lowered error rates (Sections 4.2 and 4.4).",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 22},
        "supports_claims": ["C146"],
        "notes": ""
    },
    {
        "evidence_id": "E196",
        "evidence_text": "The 2025 prompt lineages reflect the procedure/calibration distinction: procedure replaced pleading where possible, while exhortation survived iteration where it served as calibration.",
        "evidence_type": "observation",
        "verbatim_quote": "The 2025 prompt lineages reflect this distinction: procedure replaced pleading where possible, while exhortation survived iteration where it served as calibration (Supplement A.3).",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 22},
        "supports_claims": ["C147"],
        "notes": ""
    },
    {
        "evidence_id": "E197",
        "evidence_text": "Both episodes kept durable memory outside the context window: disposition tags in a shared Zotero library recorded origin and quality of AI-supplied references; templated CSV outputs came from the discovery, documentation, and evidence runs; the 2026 agent pair generated machine-readable claims blocks and an audit trail.",
        "evidence_type": "observation",
        "verbatim_quote": "Both episodes already kept their memory this way: disposition tags in a shared Zotero library recorded the origin and quality of AI-supplied references (Section 3.1); templated CSV outputs were produced from the tool discovery, documentation, and evidence runs;",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 21},
        "supports_claims": ["C148"],
        "notes": "Final list element (2026 machine-readable claims blocks and audit trail) spans the p21/p22 page break and is clipped from the quote; verifiable against the PDF."
    },
    {
        "evidence_id": "E198",
        "evidence_text": "Considerable human judgement was spent on early tool-documentation outputs (model choice, prompt refinement) before stepping back to spot-checks as quality improved, whereas a human reviewed every literature-search result since errors persisted.",
        "evidence_type": "observation",
        "verbatim_quote": "In our work, for example, considerable human judgement was spent on early tool documentation outputs (choosing a model and refining the prompt) before we stepped back to spot-checks as quality improved (Olofsson et al., 2014), whereas a human reviewed every literature search result since errors persisted (Sections 4.3 and 4.1).",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 22},
        "supports_claims": ["C153"],
        "notes": ""
    },
    {
        "evidence_id": "E199",
        "evidence_text": "Recap: source material determined the failure mode while scaffolding maturity influenced its rate; fabrication yielded to a better prompt (bounded article-by-article extraction), misattribution survived every prompt improvement and fell to an orthogonal metadata check.",
        "evidence_type": "observation",
        "verbatim_quote": "In our case, the source material determined the failure mode, while the maturity of the scaffolding influenced its rate. During tool discovery, journals with few genuine targets provoked fabrication, whereas target-rich journals provoked misattribution. Fabrication yielded to a better prompt, which replaced a broad search with bounded, article-by-article extraction against an explicit definition and schema (Sections 3.1 and 4.2). Misattribution survived every prompt improvement and fell instead to an orthogonal metadata check (Section 4.3).",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 22},
        "supports_claims": ["C155", "C157", "C089"],
        "notes": ""
    },
    {
        "evidence_id": "E200",
        "evidence_text": "Jones (2025) gives the mandate criterion: narrow until the agent finishes without rescue at least 90% of the time, remaining failures are bounded, auditable, and reversible, and every error surfaces quickly enough for a human to decide roll back or roll forward.",
        "evidence_type": "literature_citation",
        "verbatim_quote": "Jones (2025) gives the criterion: the researcher should narrow the mandate until they can demonstrate that the agent finishes the task without rescue at least 90% of the time, that any remaining failures are bounded, auditable, and reversible, and that every error surfaces quickly enough for a human, rather than automation, to decide whether to roll back or roll forward.",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 22},
        "supports_claims": ["C158"],
        "notes": ""
    },
]

CLAIMS = [
    {
        "claim_id": "C140",
        "claim_text": "Independence of context, not severity of instruction, allows a verifier to break free from a producer's commitments and do its job.",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "verbatim_quote": "Independence of context, not severity of instruction, allows a verifier to break free from a producer's commitments and do its job.",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 21},
        "supported_by": ["E190", "E146"],
        "supports_claims": ["C136", "C015"],
        "notes": "Principle 1 conclusion."
    },
    {
        "claim_id": "C141",
        "claim_text": "Re-grounding applies to producers as well as verifiers: Guard A grounded drafting itself in mandatory retrieval.",
        "claim_type": "methodological_argument",
        "claim_role": "supporting",
        "verbatim_quote": "Re-grounding does not, however, just apply to verifiers. Guard A of the 2026 workflow grounded the proposer itself: drafting could begin only from freshly retrieved metadata, never from recall.",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 21},
        "supported_by": ["E192"],
        "supports_claims": ["C142"],
        "notes": ""
    },
    {
        "claim_id": "C142",
        "claim_text": "Grounding in one external source is necessary; grounding in additional sources of independent provenance turns it into a robust check, since a single source's errors become visible through comparison.",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "verbatim_quote": "Grounding in one external source is necessary; grounding in additional sources of independent provenance turns it into a robust check, since a single source's errors become visible through comparison (Metzger, Flanagin, and Medders, 2010; Hilligoss and Rieh, 2008).",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 21},
        "supported_by": ["E191", "E185"],
        "supports_claims": ["C136", "C129"],
        "notes": "Principle 2 (external re-grounding)."
    },
    {
        "claim_id": "C143",
        "claim_text": "Once model errors are mitigated, the remaining errors are the sources' own; the pipeline now consults more than one authority where possible and has caught source errors.",
        "claim_type": "empirical",
        "claim_role": "intermediate",
        "verbatim_quote": "Once model errors are mitigated, the errors that remain are the sources' own: our pipeline now consults more than one authority wherever such sources exist, and has caught source errors (Section 4.5).",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 21},
        "supported_by": ["E177", "E185"],
        "supports_claims": ["C142"],
        "notes": ""
    },
    {
        "claim_id": "C144",
        "claim_text": "A check run parallel to the producer inherits its framing and blind spots; only a check approaching the artefact from another direction escapes them.",
        "claim_type": "theoretical",
        "claim_role": "intermediate",
        "verbatim_quote": "Because a check run parallel to the producer only reads the claim and confirms it looks right, it inherits the producer's framing and perhaps its blind spots. Only a check that approaches the artefact from another direction escapes them.",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 21},
        "supported_by": ["E193", "E194"],
        "supports_claims": ["C136", "C067"],
        "notes": "Principle 3 (orthogonal framing)."
    },
    {
        "claim_id": "C145",
        "claim_text": "Any verifier's contract should be written orthogonally: start from the evidence and re-derive each claim, rather than start from the claim and seek confirmation.",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "verbatim_quote": "The design lesson is to write any verifier's contract orthogonally: start from the evidence and re-derive each claim, rather than start from the claim and seek its confirmation (Gao et al., 2023; Wu et al., 2025).",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 21},
        "supported_by": ["E193", "E194"],
        "supports_claims": ["C144"],
        "notes": ""
    },
    {
        "claim_id": "C146",
        "claim_text": "Requirements that matter should be encoded as workflow steps, not exhortations (procedure over pleading).",
        "claim_type": "methodological_argument",
        "claim_role": "core",
        "verbatim_quote": "Encode requirements that matter as workflow steps, not as exhortations (Peters and Chin-Yee, 2025).",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 22},
        "supported_by": ["E195", "E169"],
        "supports_claims": ["C016"],
        "notes": "Design principle named in the Abstract."
    },
    {
        "claim_id": "C147",
        "claim_text": "Each load-bearing output should be the product of an enforced procedure, with prompt language reserved for what procedure cannot reach (calibrations such as the precision-over-recall guardrail).",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "verbatim_quote": "Treat each load-bearing output as the product of an enforced procedure, and reserve prompt language for what procedure cannot reach: calibrations such as the 2025 evidence stage's precision-over-recall guardrail, an evidentiary threshold not easily encoded into the workflow (Section 4.4).",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 22},
        "supported_by": ["E196", "E143"],
        "supports_claims": ["C146"],
        "notes": ""
    },
    {
        "claim_id": "C148",
        "claim_text": "The context window is a poor system of record (volatile, opaque, session-bound); durable state belongs outside it in version-controlled, inspectable stores.",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "verbatim_quote": "The context window is a poor system of record: volatile, opaque, and lost when a session ends. Durable state belongs outside it, in versioncontrolled stores that can be inspected and recovered, offloading cognition onto durable structure (Risko and Gilbert, 2016; Hutchins, 1995).",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 21},
        "supported_by": ["E197"],
        "supports_claims": ["C136", "C056"],
        "notes": "Principle 4 (persistent external state). 'versioncontrolled' preserves a line-break artefact of the processed md."
    },
    {
        "claim_id": "C149",
        "claim_text": "Externalised artefacts should record not only what was kept but what was rejected and why: tombstones let the workflow accumulate a memory of its own failures rather than re-explore them.",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "verbatim_quote": "This principle generalises the practice: externalised artefacts should record not only what was kept but what was rejected and why. Tombstones for the sources discarded, the interpretations abandoned, and the paths that failed let the workflow accumulate a memory of its own failures rather than re-explore them.",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 22},
        "supported_by": [],
        "supports_claims": ["C148"],
        "notes": "Prescriptive extension beyond the episodes' documented practice."
    },
    {
        "claim_id": "C150",
        "claim_text": "Gate the workflow and put a human at the gates that matter.",
        "claim_type": "methodological_argument",
        "claim_role": "core",
        "verbatim_quote": "Gate the workflow, and put a human at the gates that matter.",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 22},
        "supported_by": ["E198"],
        "supports_claims": ["C016"],
        "notes": "Design principle named in the Abstract (stage-gating with human checkpoints)."
    },
    {
        "claim_id": "C151",
        "claim_text": "Humans should neither review everything at the end (failure-prone) nor monitor every step (forfeits partial automation); total review or constant watchfulness burdens without structuring and is likely unreliable.",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "verbatim_quote": "Humans should not have to review everything at the end (a practice prone to failure (Luo et al., 2024; Steyvers et al., 2025)), nor should they have to monitor every step, which would forfeit the value of partial automation. Total review or constant watchfulness burdens the human without structuring the collaboration, and either is likely to be unreliable (Vaccaro, Almaatouq, and Malone, 2024).",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 22},
        "supported_by": [],
        "supports_claims": ["C150"],
        "notes": "Citations embedded in quote."
    },
    {
        "claim_id": "C152",
        "claim_text": "Stages provide gates and reversibility makes a 'no' at a gate actionable; continuous workflows offer no junctures and rigid one-way pipelines allow inspection but no send-back.",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "verbatim_quote": "If the workflow is continuous, no junctures present themselves for human review. If the workflow is a rigid one-way pipeline, humans are forced to inspect results but cannot send work back. Stages provide gates, while reversibility makes a 'no' at a gate actionable.",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 22},
        "supported_by": [],
        "supports_claims": ["C150"],
        "notes": ""
    },
    {
        "claim_id": "C153",
        "claim_text": "Human judgement is the workflow's scarcest input: position it where work commits and proportion it towards calibration and the stages where the error rate refuses to fall, not across every output.",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "verbatim_quote": "Human judgement is the workflow's scarcest input: position it where work commits (qualifying an instrument for production, validating what enters the corpus), and proportion it towards calibration and towards the stages where the error rate refuses to fall rather than across every output.",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 22},
        "supported_by": ["E198"],
        "supports_claims": ["C150"],
        "notes": ""
    },
    {
        "claim_id": "C154",
        "claim_text": "Gates only work if the system can stop at one: systems must be corrigible, admitting failure rather than manufacturing confident fabrication — 'this stage failed' must be a producible output.",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "verbatim_quote": "Gates only work if the system can stop at one, so systems must be corrigible, admitting failure rather than manufacturing a confident fabrication; 'this stage failed' is an output the tool must be able to produce.",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 22},
        "supported_by": ["E116"],
        "supports_claims": ["C150"],
        "notes": "The 2025 silent mode-switch is the negative case."
    },
    {
        "claim_id": "C155",
        "claim_text": "A mandate is safe only where model, harness, and scaffolding — backed by independent checks — can catch the failures the material produces; where a failure arises that nothing can see, the mandate must shrink until something can.",
        "claim_type": "methodological_argument",
        "claim_role": "core",
        "verbatim_quote": "A mandate is safe only where the model, the harness, and the scaffolding, backed by those independent checks, can catch the failures the material produces. Where a failure arises that nothing available can see, the mandate over that aspect must shrink until something can.",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 22},
        "supported_by": ["E199"],
        "supports_claims": ["C016"],
        "notes": "Principle: match the mandate to what the system can repeatedly achieve and verify."
    },
    {
        "claim_id": "C156",
        "claim_text": "A verifier can only be as good as what it can see.",
        "claim_type": "theoretical",
        "claim_role": "supporting",
        "verbatim_quote": "A verifier, however, can only be as good as what it can see.",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 22},
        "supported_by": ["E176"],
        "supports_claims": ["C155"],
        "notes": ""
    },
    {
        "claim_id": "C157",
        "claim_text": "The shape of the failure tells the builder which check can see it, and so how much can safely be asked between checkpoints.",
        "claim_type": "interpretation",
        "claim_role": "intermediate",
        "verbatim_quote": "The shape of the failure tells the builder which check can see it, and so how much can safely be asked between checkpoints.",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 22},
        "supported_by": ["E199"],
        "supports_claims": ["C155"],
        "notes": ""
    },
    {
        "claim_id": "C158",
        "claim_text": "Mandate and scope pull against each other: the only way to widen what runs between checkpoints is to narrow what each task attempts until the checks reliably catch what fails.",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "verbatim_quote": "Mandate and scope therefore pull against each other, since the only way to widen what runs between checkpoints is to narrow what each task attempts until the checks reliably catch what fails.",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 22},
        "supported_by": ["E200"],
        "supports_claims": ["C155"],
        "notes": ""
    },
    {
        "claim_id": "C159",
        "claim_text": "Benchmark tasks can be scored automatically, but research output cannot — correctness in research is established by correspondence with orthogonal evidence.",
        "claim_type": "theoretical",
        "claim_role": "intermediate",
        "verbatim_quote": "Benchmark tasks can be scored automatically, but research output cannot.",
        "location": {"section": "5.2 Design principles for researcher-builders", "page": 22},
        "supported_by": [],
        "supports_claims": ["C155", "C136"],
        "notes": "The continuation (correctness established by correspondence with orthogonal evidence) spans the p22/p23 page break; verifiable against the PDF."
    },
]

IMPLICIT_ARGUMENTS = [
    {
        "implicit_argument_id": "IA019",
        "argument_text": "Error-rate signals are observable enough, early enough, to allocate scarce human judgement to the stages 'where the error rate refuses to fall' — the allocation rule assumes the very visibility of error that verification is being designed to create.",
        "type": "methodological_assumption",
        "trigger_text": [
            "Human judgement is the workflow's scarcest input: position it where work commits (qualifying an instrument for production, validating what enters the corpus), and proportion it towards calibration and towards the stages where the error rate refuses to fall rather than across every output.",
            "In our work, for example, considerable human judgement was spent on early tool documentation outputs (choosing a model and refining the prompt) before we stepped back to spot-checks as quality improved (Olofsson et al., 2014), whereas a human reviewed every literature search result since errors persisted (Sections 4.3 and 4.1)."
        ],
        "trigger_locations": [
            {"section": "5.2 Design principles for researcher-builders", "page": 22},
            {"section": "5.2 Design principles for researcher-builders", "page": 22}
        ],
        "inference_reasoning": "Proportioning human review to observed error rates presupposes a phase in which error rates are measured accurately enough to steer allocation — which itself requires the comprehensive checking the rule is designed to economise. The episodes resolved this by front-loading comprehensive verification and relaxing later, but the principle as stated leaves this bootstrap requirement implicit.",
        "supports_claims": ["C153"],
        "assessment_implications": "Adopters who skip the front-loaded calibration phase could under-allocate review exactly where errors hide; the principle's safety depends on the unstated calibration step."
    },
]

save_group(
    {
        "group": "G12",
        "section_title": "Discussion 5.2 design principles (re-grounding through mandate-matching)",
        "page_range": "21-22",
        "estimated_words": 1340,
        "natural_boundary": "p22/p23 page boundary (before the scaffolding-reflection paragraphs)",
        "split_rationale": "Middle third of the Discussion; boundary at the p22/p23 page break, nearest paragraph boundary."
    },
    evidence=EVIDENCE,
    claims=CLAIMS,
    implicit_arguments=IMPLICIT_ARGUMENTS,
)
