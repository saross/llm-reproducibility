#!/usr/bin/env python3
"""Pass 1, Group G8: Results 4.3 Tool documentation (pp. 13-15, ~1,100 words). Tables 6-8."""

from pass1_lib import save_group

EVIDENCE = [
    {
        "evidence_id": "E123",
        "evidence_text": "The metadata prompt began as five prose fields rendered as CSV and grew over eight iterations into a thirty-four-field schema, each elaboration fixing a documented failure or absence in the previous run.",
        "evidence_type": "observation",
        "verbatim_quote": "The metadata prompt began as five prose fields rendered as commaseparated values and grew, over eight iterations, into a thirty-four-field schema, each elaboration fixing a documented failure or absence in the previous run.",
        "location": {"section": "4.3 Tool documentation", "page": 13},
        "supports_claims": ["C096", "C100"],
        "notes": "'commaseparated' preserves a line-break artefact of the processed md."
    },
    {
        "evidence_id": "E124",
        "evidence_text": "Asked for only a current snapshot, Claude persisted in supplying version histories, so a structured history field was added ('domesticating' the tendency).",
        "evidence_type": "observation",
        "verbatim_quote": "When Claude, for example, was asked to provide only a current snapshot of each tool but persisted in supplying version histories, we added a structured history field.",
        "location": {"section": "4.3 Tool documentation", "page": 13},
        "supports_claims": ["C097"],
        "notes": ""
    },
    {
        "evidence_id": "E125",
        "evidence_text": "When the model spontaneously noted in a 'weaknesses' field that a tool's closed proprietary design undermined reproducibility, instructions were added to capture 'transparency and reproducibility' consistently.",
        "evidence_type": "observation",
        "verbatim_quote": "When the model noted in a 'weaknesses' field that one tool's closed, proprietary design undermined reproducibility, we added instructions to capture 'transparency and reproducibility' consistently.",
        "location": {"section": "4.3 Tool documentation", "page": 13},
        "supports_claims": ["C097"],
        "notes": ""
    },
    {
        "evidence_id": "E126",
        "evidence_text": "Meta-prompting improved metadata outputs more consistently than it had for tool discovery.",
        "evidence_type": "observation",
        "verbatim_quote": "Meta-prompting improved metadata outputs more consistently than it had for tool discovery.",
        "location": {"section": "4.3 Tool documentation", "page": 13},
        "supports_claims": ["C096"],
        "notes": ""
    },
    {
        "evidence_id": "E127",
        "evidence_text": "Three services were assessed (OpenAI o3, Claude Sonnet 3.7 research mode, Gemini 2.5 Pro via Google AI Studio); model selection rested on comparing output across four prompt iterations against FAIMS, which the authors had built and maintained over a decade.",
        "evidence_type": "observation",
        "verbatim_quote": "We had built and maintained FAIMS over a decade, and model selection rested on comparison of output across four prompt iterations against it.",
        "location": {"section": "4.3 Tool documentation", "page": 13},
        "supports_claims": ["C103"],
        "notes": "Preceding sentence lists the three services assessed."
    },
    {
        "evidence_id": "E128",
        "evidence_text": "Despite prompt improvements, Gemini confused software versions, mixed features across releases, and partly confabulated personnel.",
        "evidence_type": "observation",
        "verbatim_quote": "Despite improvements to the prompt, Gemini confused software versions, mixing features across releases, and partly confabulating personnel.",
        "location": {"section": "4.3 Tool documentation", "page": 13},
        "supports_claims": ["C014"],
        "notes": ""
    },
    {
        "evidence_id": "E129",
        "evidence_text": "o3 produced more accurate outputs but some errors could not be overcome (e.g., never capturing FAIMS's GPL-to-Apache licensing move), and records remained terse to the point of omitting information.",
        "evidence_type": "observation",
        "verbatim_quote": "o3 produced more accurate outputs, but some errors (e.g., never capturing that FAIMS had moved from GPL to Apache licensing across versions) could not be overcome, and records remained terse to the point of omitting information.",
        "location": {"section": "4.3 Tool documentation", "page": 13},
        "supports_claims": ["C103"],
        "notes": ""
    },
    {
        "evidence_id": "E130",
        "evidence_text": "Claude was retained for production runs despite one intractable annoyance: narrative reports on first response, with CSV emitted only after a follow-up request.",
        "evidence_type": "observation",
        "verbatim_quote": "It was retained for production runs, despite one intractable annoyance: it produced narrative reports only on first response, emitting comma-separated output only after a follow-up \"please provide the requested CSV\" prompt.",
        "location": {"section": "4.3 Tool documentation", "page": 14},
        "supports_claims": ["C103"],
        "notes": "Preceding sentence ('Claude produced rich outputs free of errors, and was then tested against other tools with further prompt refinement.') spans the p13/p14 page break and is not quoted; verifiable against the PDF."
    },
    {
        "evidence_id": "E131",
        "evidence_text": "Model judgement was highly sensitive to minor prompt changes: the in-scope palaeoecology package ade4 flipped in and out of the tool definition across slight prompt revisions, settling correctly only with the final prompt version.",
        "evidence_type": "observation",
        "verbatim_quote": "Model judgement proved highly sensitive to minor prompt changes: during development, although the palaeoecology package ade4 belonged in scope, Claude flipped it in and out of the tool definition across slight prompt revisions, settling correctly only with the final version of the prompt.",
        "location": {"section": "4.3 Tool documentation", "page": 14},
        "supports_claims": ["C098"],
        "notes": ""
    },
    {
        "evidence_id": "E132",
        "evidence_text": "After settling, tool categorisation generalised well across the dataset.",
        "evidence_type": "observation",
        "verbatim_quote": "After settling, tool categorisation generalised well across the dataset.",
        "location": {"section": "4.3 Tool documentation", "page": 14},
        "supports_claims": ["C098"],
        "notes": ""
    },
    {
        "evidence_id": "E133",
        "evidence_text": "Metadata failure taxonomy (Table 6): 2 misattributed (FaceNet wrong domain; pnuts not a tool — Discovery phase), 6 retrieval failures (Fountain, Grid Machine, Microware name collisions; Wcvt2Pov, Bwigg, PyCoCu sparse documentation — Metadata phase), 8 total.",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "Misattributed 2 FaceNet (wrong domain), pnuts (not a tool) Discovery Retrieval failure 6 Fountain, Grid Machine, Microware (name collision); Wcvt2Pov, Bwigg, PyCoCu (sparse documentation) Metadata Total 8",
        "location": {"section": "4.3 Tool documentation", "page": 14},
        "supports_claims": ["C099", "C103"],
        "notes": "Flattened Table 6; layout verifiable against the PDF."
    },
    {
        "evidence_id": "E134",
        "evidence_text": "Metadata collection was attempted for 92 tools; eight failed, mostly from inadequate metadata availability (link rot, name collisions) rather than model error. Four lookups 'spawned' related tools, adding six records (MASA retired as consortium), completing 89 documented tools.",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "Metadata collection was attempted for 92 tools. Most produced complete records while eight failed, mostly due to inadequate metadata availability rather than model error, e.g., because of link rot (Klein, 2014) or name collisions. Four lookups 'spawned' related tools instead of, or in addition to, the one requested, adding six new records (while retiring MASA as a consortium rather than a tool), bringing the completed dataset to 89 documented tools (Tables 6 and 7).",
        "location": {"section": "4.3 Tool documentation", "page": 14},
        "supports_claims": ["C103"],
        "notes": "Table 7 (spawning events: Grid Machine→ArchaeoGRID failure; MASA Consortium→LogicistWriter/OpenArchaeo/OpenGuide success; Wcvt2Pov→POV-Ray failure; Rhino for AutoCAD→Rhinoceros 3D success) flattens with intercalated captions; verifiable against the PDF."
    },
    {
        "evidence_id": "E135",
        "evidence_text": "Failure had a consistent binary shape: on first-hand-known or manually verified tools, no subtle errors or partial completions were found — records were either complete and accurate or obvious failures (typically a category essay indicating insufficient information).",
        "evidence_type": "observation",
        "verbatim_quote": "Failure had a consistent shape: on tools we knew first-hand or verified manually, no subtle errors or partial completions were found; records were either complete and accurate, or obvious failures (typically resulting in an essay about the software category rather than data about the specific tool, often indicating that the model could not find enough information to build tool documentation).",
        "location": {"section": "4.3 Tool documentation", "page": 14},
        "supports_claims": ["C099", "C105"],
        "notes": ""
    },
    {
        "evidence_id": "E136",
        "evidence_text": "The orthogonal metadata check exposed a consortium (MASA), a non-domain library (FaceNet), and a non-tool website script (pnuts) — none confabulations (already caught), all misattributions or granularity errors.",
        "evidence_type": "observation",
        "verbatim_quote": "None were confabulations; discovery verification had already detected those. Instead, all were misattributions or granularity errors. Changing the question, and the questioner, exposed these errors.",
        "location": {"section": "4.3 Tool documentation", "page": 15},
        "supports_claims": ["C101", "C102", "C015"],
        "notes": "Lead-in sentence (fresh-context repository/licence/version query making subtle mistakes trivially visible) spans the p14/p15 page break; verifiable against the PDF."
    },
    {
        "evidence_id": "E137",
        "evidence_text": "Slop evaluation metrics (Table 8, n=88): anchored claims per 100 words mean 3.13 (range 1.4–8.3); generic phrases per entry mean 4.5 (range 2–10).",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "Anchored claims per 100 words 3.13 1.4–8.3 Generic phrases per entry 4.5 2–10",
        "location": {"section": "4.3 Tool documentation", "page": 15},
        "supports_claims": ["C103"],
        "notes": "Flattened Table 8 (upper panel); layout verifiable against the PDF."
    },
    {
        "evidence_id": "E138",
        "evidence_text": "Slop severity bands (Table 8, n=88): none 14 (15.9%), minimal 64 (72.7%), moderate 10 (11.4%), significant 0 (0.0%).",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "None 14 15.9 Minimal 64 72.7 Moderate 10 11.4 Significant 0 0.0",
        "location": {"section": "4.3 Tool documentation", "page": 15},
        "supports_claims": ["C103"],
        "notes": "Flattened Table 8 (lower panel); layout verifiable against the PDF."
    },
    {
        "evidence_id": "E139",
        "evidence_text": "In March 2026, Claude Opus 4.6 assessed 88 of 89 documented entries (one excluded by configuration error) using the Shaib et al. (2025) slop taxonomy, with severity summarised on a four-band scale of the authors' design.",
        "evidence_type": "observation",
        "verbatim_quote": "In March 2026, a newer Claude model (Opus 4.6) subsequently assessed 88 of the 89 documented entries (one was excluded by a configuration error) using the slop taxonomy proposed by Shaib et al. (2025), with overall severity summarised on a four-band scale of our own design (Shaib et al.'s protocol elicits a binary judgement).",
        "location": {"section": "4.3 Tool documentation", "page": 15},
        "supports_claims": ["C103"],
        "notes": ""
    },
    {
        "evidence_id": "E140",
        "evidence_text": "No entry reached the 'significant' slop band; moderate cases clustered where the model's domain knowledge thinned.",
        "evidence_type": "observation",
        "verbatim_quote": "No entry reached our \"significant\" band, and the moderate cases clustered where the model's domain knowledge thinned (Table 8).",
        "location": {"section": "4.3 Tool documentation", "page": 15},
        "supports_claims": ["C103"],
        "notes": ""
    },
    {
        "evidence_id": "E141",
        "evidence_text": "Accuracy was manually checked against first-hand knowledge of tools or sources like the open-archaeo catalogue and GitHub.",
        "evidence_type": "observation",
        "verbatim_quote": "We manually checked accuracy against first-hand knowledge of tools or against sources like the open-archaeo catalogue and GitHub.",
        "location": {"section": "4.3 Tool documentation", "page": 15},
        "supports_claims": ["C103"],
        "notes": ""
    },
]

CLAIMS = [
    {
        "claim_id": "C096",
        "claim_text": "In the tool-documentation stage the scaffolding became an explicit artefact.",
        "claim_type": "interpretation",
        "claim_role": "intermediate",
        "verbatim_quote": "The third stage collected structured metadata for each verified tool, and here the scaffolding became an explicit artefact.",
        "location": {"section": "4.3 Tool documentation", "page": 13},
        "supported_by": ["E123", "E126"],
        "supports_claims": ["C011", "C018"],
        "notes": ""
    },
    {
        "claim_id": "C097",
        "claim_text": "A recurring design principle: work with the model's grain, folding its spontaneous tendencies into the schema rather than fighting them.",
        "claim_type": "methodological_argument",
        "claim_role": "intermediate",
        "verbatim_quote": "One principle recurred across these revisions: work with the model's grain, folding its spontaneous tendencies into the schema rather than fighting them.",
        "location": {"section": "4.3 Tool documentation", "page": 13},
        "supported_by": ["E124", "E125"],
        "supports_claims": ["C016"],
        "notes": "Named design principle carried into the Discussion."
    },
    {
        "claim_id": "C098",
        "claim_text": "The reliable production classifications were a (somewhat fragile) property of tuned scaffolding.",
        "claim_type": "interpretation",
        "claim_role": "intermediate",
        "verbatim_quote": "The reliable production classifications were thus a (somewhat fragile) property of tuned scaffolding.",
        "location": {"section": "4.3 Tool documentation", "page": 14},
        "supported_by": ["E131", "E132"],
        "supports_claims": ["C003", "C016"],
        "notes": "Directly instantiates the thesis that reliability resides in scaffolding."
    },
    {
        "claim_id": "C099",
        "claim_text": "The binary failure mode made human verification tractable: erroneous records were easy to spot without auditing every field.",
        "claim_type": "interpretation",
        "claim_role": "intermediate",
        "verbatim_quote": "That binary failure mode made human verification tractable; erroneous records were easy to spot without the need for auditing every field.",
        "location": {"section": "4.3 Tool documentation", "page": 14},
        "supported_by": ["E133", "E135"],
        "supports_claims": ["C105"],
        "notes": ""
    },
    {
        "claim_id": "C100",
        "claim_text": "The eight-iteration prompt investment was a one-time cost that scaled across tools.",
        "claim_type": "interpretation",
        "claim_role": "supporting",
        "verbatim_quote": "The eight-iteration prompt investment was a one-time cost that scaled across tools.",
        "location": {"section": "4.3 Tool documentation", "page": 14},
        "supported_by": ["E123"],
        "supports_claims": ["C012"],
        "notes": ""
    },
    {
        "claim_id": "C101",
        "claim_text": "Metadata collection doubled as an orthogonal check on discovery outputs.",
        "claim_type": "empirical",
        "claim_role": "intermediate",
        "verbatim_quote": "Metadata collection doubled as an orthogonal check on discovery outputs.",
        "location": {"section": "4.3 Tool documentation", "page": 14},
        "supported_by": ["E136"],
        "supports_claims": ["C067", "C015"],
        "notes": "In-study demonstration of orthogonal framing."
    },
    {
        "claim_id": "C102",
        "claim_text": "Changing the question, and the questioner, exposed errors invisible to the original framing.",
        "claim_type": "interpretation",
        "claim_role": "supporting",
        "verbatim_quote": "Changing the question, and the questioner, exposed these errors.",
        "location": {"section": "4.3 Tool documentation", "page": 15},
        "supported_by": ["E136"],
        "supports_claims": ["C101", "C067"],
        "notes": ""
    },
    {
        "claim_id": "C103",
        "claim_text": "Overall, tool-documentation output quality was high.",
        "claim_type": "empirical",
        "claim_role": "intermediate",
        "verbatim_quote": "Overall, output quality was high.",
        "location": {"section": "4.3 Tool documentation", "page": 15},
        "supported_by": ["E127", "E129", "E130", "E133", "E134", "E137", "E138", "E139", "E140", "E141"],
        "supports_claims": ["C080", "C083"],
        "notes": ""
    },
    {
        "claim_id": "C104",
        "claim_text": "The slop assessment measured stylistic quality and information density rather than factual accuracy, and — one Claude model judging another — could have suffered from self-preference bias.",
        "claim_type": "methodological_argument",
        "claim_role": "supporting",
        "verbatim_quote": "That assessment measured stylistic quality and information density, not factual accuracy and, since one Claude model judged another, could have suffered from self-preference bias.",
        "location": {"section": "4.3 Tool documentation", "page": 15},
        "supported_by": [],
        "supports_claims": ["C103"],
        "notes": "Self-applied limitation echoing the narcissism/circularity literature (E017, E018)."
    },
    {
        "claim_id": "C105",
        "claim_text": "A mature prompt providing necessary scaffolding, combined with a binary failure mode, produced a reliable and verifiable outcome.",
        "claim_type": "interpretation",
        "claim_role": "intermediate",
        "verbatim_quote": "A mature prompt providing necessary scaffolding, combined with a binary failure mode, produced a reliable and verifiable outcome.",
        "location": {"section": "4.3 Tool documentation", "page": 15},
        "supported_by": ["E135", "E137", "E138"],
        "supports_claims": ["C080", "C016"],
        "notes": "Stage-level synthesis."
    },
]

IMPLICIT_ARGUMENTS = [
    {
        "implicit_argument_id": "IA014",
        "argument_text": "Model performance on FAIMS — a tool the authors built and know intimately — generalises to the other ~90 tools, so a FAIMS-benchmarked model selection yields reliable performance dataset-wide.",
        "type": "methodological_assumption",
        "trigger_text": [
            "We had built and maintained FAIMS over a decade, and model selection rested on comparison of output across four prompt iterations against it.",
            "After settling, tool categorisation generalised well across the dataset."
        ],
        "trigger_locations": [
            {"section": "4.3 Tool documentation", "page": 13},
            {"section": "4.3 Tool documentation", "page": 14}
        ],
        "inference_reasoning": "Selecting the production model by benchmarking against a single deeply-known tool assumes FAIMS is representative of the dataset (in documentation availability, domain specificity, and complexity). The generalisation observation partially validates this, but the selection logic itself rests on the unstated representativeness premise.",
        "supports_claims": ["C103"],
        "assessment_implications": "A tool with unusually rich documentation (built by the evaluators) may overstate expected model performance on sparsely documented tools — exactly where Table 6's retrieval failures clustered."
    },
    {
        "implicit_argument_id": "IA015",
        "argument_text": "The binary failure shape observed on first-hand-known or manually verified tools holds for the records not so verified — no subtle errors lurk in the unchecked remainder.",
        "type": "bridging_claim",
        "trigger_text": [
            "Failure had a consistent shape: on tools we knew first-hand or verified manually, no subtle errors or partial completions were found; records were either complete and accurate, or obvious failures (typically resulting in an essay about the software category rather than data about the specific tool, often indicating that the model could not find enough information to build tool documentation).",
            "That binary failure mode made human verification tractable; erroneous records were easy to spot without the need for auditing every field."
        ],
        "trigger_locations": [
            {"section": "4.3 Tool documentation", "page": 14},
            {"section": "4.3 Tool documentation", "page": 14}
        ],
        "inference_reasoning": "The tractability claim licenses spot-level rather than field-level auditing on the strength of the binary pattern observed in the checked subset. Extending that pattern to unchecked records is an inductive bridge; a subtle-error mode that only appears on unfamiliar tools would evade it by construction.",
        "supports_claims": ["C099", "C105"],
        "assessment_implications": "The verification economy of the stage depends on this bridge; the March 2026 slop re-assessment partially tests style but explicitly not factual accuracy (C104)."
    },
]

save_group(
    {
        "group": "G8",
        "section_title": "Results 4.3 Tool documentation",
        "page_range": "13-15",
        "estimated_words": 1100,
        "natural_boundary": "Before '4.4 Tool evidence collection' heading (p. 15)",
        "split_rationale": "Single Results subsection; under 1,500-word cap. Tables 6-8 extracted as flattened quotes; two page-break-spanning sentences noted on E130 and E136."
    },
    evidence=EVIDENCE,
    claims=CLAIMS,
    implicit_arguments=IMPLICIT_ARGUMENTS,
)
