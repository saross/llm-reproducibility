#!/usr/bin/env python3
"""Pass 1, Group G6: Results 4 intro + 4.1 Literature discovery and synthesis (pp. 9-11, ~1,190 words).

Tables 1-3 flatten to linear text in the processed md; row quotes are contiguous
normalised strings (column semantics from captions recorded in notes).
"""

from pass1_lib import save_group

T2 = ("Table 2 columns: Found (total sources returned), Errors (invalid sources), "
      "Valid (meeting inclusion criteria), Unique (valid sources found only by this method). "
      "Flattened table row; layout verifiable against the PDF.")
T3 = ("Table 3 columns: Non-academic, Not-relevant, Predatory, Confabulated, Total. "
      "Flattened table row; layout verifiable against the PDF.")

EVIDENCE = [
    {
        "evidence_id": "E066",
        "evidence_text": "The campaign exercised three model families (OpenAI, Anthropic, Google) plus Perplexity and Elicit for literature discovery.",
        "evidence_type": "observation",
        "verbatim_quote": "Across the campaign we exercised three model families (OpenAI, Anthropic, and Google), plus Perplexity and Elicit for literature discovery (see Table 1).",
        "location": {"section": "4 Results", "page": 9},
        "supports_claims": ["C080"],
        "notes": "Table 1 (tool-by-task coverage matrix) flattens to checkmark glyphs in the md; per-service task coverage verifiable against the PDF."
    },
    {
        "evidence_id": "E067",
        "evidence_text": "Coverage was shaped by lab releases: during literature discovery neither Claude Sonnet 3.7 nor Gemini 2.5 Pro yet offered a dedicated research mode; after Anthropic released one, the authors began using it.",
        "evidence_type": "observation",
        "verbatim_quote": "During the literature discovery stage, for example, neither Claude Sonnet 3.7 nor Gemini 2.5 Pro yet offered a dedicated research mode (the multi-step autonomous search-and-synthesis capability OpenAI had introduced as \"Deep Research\"). After Anthropic released such a mode, we began using it (see Supplement A for the release and availability timeline).",
        "location": {"section": "4 Results", "page": 9},
        "supports_claims": ["C079"],
        "notes": ""
    },
    {
        "evidence_id": "E068",
        "evidence_text": "Three tools were screened out: Hugging Face's Open Deep Research (~$200 per run on o1-pro credits, impractical at scale), Anthropic's Computer Use (technology demonstration), and OpenAI's Operator (trialled; only three discovery records).",
        "evidence_type": "observation",
        "verbatim_quote": "Three tools were screened out. Hugging Face's Open Deep Research was architecturally attractive, but at roughly $200 per run on o1-pro credits it was impractical at scale. Anthropic's Computer Use remained a technology demonstration rather than a production instrument during the testing window. OpenAI's Operator, though trialled, contributed only three discovery records (Table 4).",
        "location": {"section": "4 Results", "page": 9},
        "supports_claims": ["C080"],
        "notes": ""
    },
    {
        "evidence_id": "E069",
        "evidence_text": "Literature discovery, ChatGPT Deep Research: 58 sources found, 15 errors, 43 valid, 37 unique (Table 2).",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "ChatGPT Deep Research 58 15 43 37",
        "location": {"section": "4.1 Literature discovery and synthesis", "page": 10},
        "supports_claims": ["C082", "C083", "C080"],
        "notes": T2
    },
    {
        "evidence_id": "E070",
        "evidence_text": "Literature discovery, Perplexity Research: 34 found, 14 errors, 20 valid, 14 unique (Table 2).",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "Perplexity Research 34 14 20 14",
        "location": {"section": "4.1 Literature discovery and synthesis", "page": 10},
        "supports_claims": ["C082", "C080"],
        "notes": T2
    },
    {
        "evidence_id": "E071",
        "evidence_text": "Literature discovery, Elicit: 10 found, 0 errors, 10 valid, 8 unique (Table 2).",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "Elicit 10 0 10 8",
        "location": {"section": "4.1 Literature discovery and synthesis", "page": 10},
        "supports_claims": ["C082", "C080"],
        "notes": T2
    },
    {
        "evidence_id": "E072",
        "evidence_text": "Literature discovery, traditional manual-search baseline: 27 found, 0 errors, 27 valid, 27 unique (Table 2).",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "Traditional methods 27 0 27 27",
        "location": {"section": "4.1 Literature discovery and synthesis", "page": 10},
        "supports_claims": ["C083"],
        "notes": T2
    },
    {
        "evidence_id": "E073",
        "evidence_text": "Literature discovery totals: multi-service sources 7; overall 129 found, 29 errors, 100 valid, 93 unique (Table 2).",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "Multi-service — 0 7 7 Total 129 29 100 93",
        "location": {"section": "4.1 Literature discovery and synthesis", "page": 10},
        "supports_claims": ["C083", "C080"],
        "notes": T2
    },
    {
        "evidence_id": "E074",
        "evidence_text": "Error breakdown, ChatGPT Deep Research: 0 non-academic, 4 not-relevant, 0 predatory, 11 confabulated, 15 total (Table 3).",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "ChatGPT Deep Research 0 4 0 11 15",
        "location": {"section": "4.1 Literature discovery and synthesis", "page": 10},
        "supports_claims": ["C082", "C014"],
        "notes": T3
    },
    {
        "evidence_id": "E075",
        "evidence_text": "Error breakdown, Perplexity Research: 5 non-academic, 8 not-relevant, 1 predatory, 0 confabulated, 14 total (Table 3).",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "Perplexity Research 5 8 1 0 14",
        "location": {"section": "4.1 Literature discovery and synthesis", "page": 10},
        "supports_claims": ["C082"],
        "notes": T3
    },
    {
        "evidence_id": "E076",
        "evidence_text": "Error breakdown, Elicit: 0 errors in every category (Table 3); overall totals 5 non-academic, 12 not-relevant, 1 predatory, 11 confabulated, 29 errors.",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "Elicit 0 0 0 0 0 Total 5 12 1 11 29",
        "location": {"section": "4.1 Literature discovery and synthesis", "page": 10},
        "supports_claims": ["C082"],
        "notes": T3
    },
    {
        "evidence_id": "E077",
        "evidence_text": "ChatGPT Deep Research had the highest yield and most errors, and required a second prompt (the first generic attempt produced unusable output) before returning documented results.",
        "evidence_type": "observation",
        "verbatim_quote": "ChatGPT Deep Research had the highest yield but also the most errors, and required a second prompt (the first, generic, attempt produced unusable output) before it returned its documented results.",
        "location": {"section": "4.1 Literature discovery and synthesis", "page": 9},
        "supports_claims": ["C082"],
        "notes": ""
    },
    {
        "evidence_id": "E078",
        "evidence_text": "Most ChatGPT Deep Research errors were confabulated sources that could not be located manually.",
        "evidence_type": "observation",
        "verbatim_quote": "Most of its errors consisted of confabulated sources that could not be located manually (Table 3).",
        "location": {"section": "4.1 Literature discovery and synthesis", "page": 9},
        "supports_claims": ["C014"],
        "notes": ""
    },
    {
        "evidence_id": "E079",
        "evidence_text": "Some confabulations contained useful pointers, such as authors who had produced relevant works, discovered during manual verification.",
        "evidence_type": "observation",
        "verbatim_quote": "During manual verification, we learned that some of these confabulations did contain useful pointers, such as authors who had produced relevant works.",
        "location": {"section": "4.1 Literature discovery and synthesis", "page": 9},
        "supports_claims": ["C083"],
        "notes": "Serendipitous value of some confabulations."
    },
    {
        "evidence_id": "E080",
        "evidence_text": "Where ChatGPT Deep Research sources were real, citation accuracy was poor.",
        "evidence_type": "observation",
        "verbatim_quote": "Where sources were real, citation accuracy was poor.",
        "location": {"section": "4.1 Literature discovery and synthesis", "page": 9},
        "supports_claims": ["C084"],
        "notes": ""
    },
    {
        "evidence_id": "E081",
        "evidence_text": "ChatGPT Deep Research provided structured bibliographic export (BibTeX) for only part of the output despite repeated requests, though follow-up queries were often productive.",
        "evidence_type": "observation",
        "verbatim_quote": "The service only provided structured bibliographic export (BibTEX) for part of the output despite repeated requests, though follow-up queries were often productive.",
        "location": {"section": "4.1 Literature discovery and synthesis", "page": 9},
        "supports_claims": ["C084"],
        "notes": ""
    },
    {
        "evidence_id": "E082",
        "evidence_text": "Perplexity returned the highest proportion of non-academic and irrelevant material; follow-up queries lost the research thread, drifting to unrelated topics (oilfield decommissioning, end-of-life care).",
        "evidence_type": "observation",
        "verbatim_quote": "Perplexity returned the highest proportion of non-academic and irrelevant material, with follow-up queries losing the research thread entirely and drifting to unrelated topics such as oilfield decommissioning or end-of-life care.",
        "location": {"section": "4.1 Literature discovery and synthesis", "page": 9},
        "supports_claims": ["C082"],
        "notes": ""
    },
    {
        "evidence_id": "E083",
        "evidence_text": "Elicit, constrained by Semantic Scholar, returned the smallest yield but the cleanest, with no invalid references.",
        "evidence_type": "observation",
        "verbatim_quote": "Elicit, constrained by Semantic Scholar, returned the smallest yield but the cleanest, with no invalid references.",
        "location": {"section": "4.1 Literature discovery and synthesis", "page": 9},
        "supports_claims": ["C082"],
        "notes": "Registry constraint associated with zero invalid references — early signal for the external-grounding mitigation."
    },
    {
        "evidence_id": "E084",
        "evidence_text": "Gemini confabulated at high rates and, unlike the others, produced confabulations with no serendipitous value; in a representative episode it declared it had 'successfully analysed' a key chapter after downloading only a snippet.",
        "evidence_type": "observation",
        "verbatim_quote": "Gemini in particular confabulated at high rates and, unlike the others, produced confabulations with no serendipitous value. In a representative episode, it declared it had \"successfully analysed\" a key chapter after downloading only a snippet, collecting search results without evaluating them.",
        "location": {"section": "4.1 Literature discovery and synthesis", "page": 10},
        "supports_claims": ["C014"],
        "notes": "Preceding sentence (Claude Research and Gemini Deep Research surfaced no additional usable bibliography) spans the p9/p10 page break and is not separately quoted; verifiable against the PDF."
    },
    {
        "evidence_id": "E085",
        "evidence_text": "A Web of Science query across the same scope produced three relevant results from the first 50 returned (all already held); a parallel Scopus search contributed only one new source.",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "A Web of Science query across the same scope produced three relevant results from the first 50 returned, but the corpus already held all three. A parallel Scopus search fared similarly, contributing only one new source.",
        "location": {"section": "4.1 Literature discovery and synthesis", "page": 10},
        "supports_claims": ["C083"],
        "notes": "Conventional faceted-search baseline."
    },
    {
        "evidence_id": "E086",
        "evidence_text": "Every reference required human verification before import into a reference manager: BibTeX export was inconsistent and roughly two-thirds of valid AI-discovered sources needed manual correction of URLs, DOIs, or author information.",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "On the other hand, every reference required human verification before it could be imported into a reference manager: BibTEXexport was inconsistent, and roughly two-thirds of the valid AI-discovered sources needed manual correction of URLs, DOIs, or author information.",
        "location": {"section": "4.1 Literature discovery and synthesis", "page": 10},
        "supports_claims": ["C084", "C080"],
        "notes": "'BibTEXexport' preserves a spacing artefact of the processed md."
    },
    {
        "evidence_id": "E087",
        "evidence_text": "No service could be induced to perform citation chaining, and all defaulted to abstracts and open-access content, unable to engage paywalled full texts — in HASS, effectively abstract-only analysis of much of the corpus.",
        "evidence_type": "observation",
        "verbatim_quote": "None could be induced to perform citation chaining, mining the bibliography of a found source for further sources, and all defaulted to operating on abstracts and open-access content, unable to engage paywalled full texts; in humanities and social sciences, where open-access penetration is low, that amounts to abstractonly analysis of much of the relevant corpus (see also Tay, 2025; Li et al., 2025).",
        "location": {"section": "4.1 Literature discovery and synthesis", "page": 10},
        "supports_claims": ["C084", "C080"],
        "notes": "'abstractonly' preserves a line-break artefact of the processed md."
    },
    {
        "evidence_id": "E088",
        "evidence_text": "The services overlapped little: no source was returned by all, and only a handful by more than one.",
        "evidence_type": "observation",
        "verbatim_quote": "The services overlapped little; no source was returned by all of them and only a handful by more than one, perhaps a sign of divergent search strategies.",
        "location": {"section": "4.1 Literature discovery and synthesis", "page": 10},
        "supports_claims": ["C083"],
        "notes": "Includes the authors' hedged interpretation (divergent search strategies)."
    },
    {
        "evidence_id": "E089",
        "evidence_text": "The final literature output was built from AI-assisted search plus manual discoveries found by citation chaining or as a side-effect of searching for confabulated sources.",
        "evidence_type": "observation",
        "verbatim_quote": "The final output was built from AI-assisted search plus manual discoveries found either by citation chaining or as a side-effect of searching for (confabulated) sources.",
        "location": {"section": "4.1 Literature discovery and synthesis", "page": 10},
        "supports_claims": ["C084"],
        "notes": ""
    },
    {
        "evidence_id": "E090",
        "evidence_text": "Every model tested handled synthesis as accumulation rather than evaluation, laying sources side by side without registering tensions, contradictions, or temporal context.",
        "evidence_type": "observation",
        "verbatim_quote": "Every model tested handled synthesis as accumulation rather than evaluation: it laid one source beside another without registering the tensions, contradictions, or temporal context that turn a pile of references into an argument.",
        "location": {"section": "4.1 Literature discovery and synthesis", "page": 11},
        "supports_claims": ["C085"],
        "notes": ""
    },
    {
        "evidence_id": "E091",
        "evidence_text": "OpenAI models defaulted to sequential summary, retreating to meta-commentary or manufactured consensus when sources conflicted; successive models showed only marginal gains in instruction-following.",
        "evidence_type": "observation",
        "verbatim_quote": "OpenAI's models defaulted to sequential summary and retreated to meta-commentary or manufactured consensus when sources conflicted, with successive models in the family showing only marginal gains in instruction-following.",
        "location": {"section": "4.1 Literature discovery and synthesis", "page": 11},
        "supports_claims": ["C085"],
        "notes": ""
    },
    {
        "evidence_id": "E092",
        "evidence_text": "Claude wrote more fluent prose over the same epistemic gap, flattening a decade of sources into an eternal present and, pushed past its range, maintaining fluency while fabricating precise citations to non-existent articles.",
        "evidence_type": "observation",
        "verbatim_quote": "Claude wrote more fluent prose over the same epistemic gap, flattening a decade of sources into an eternal present and, when pushed past its range, maintaining fluency while fabricating precise citations to non-existent articles.",
        "location": {"section": "4.1 Literature discovery and synthesis", "page": 11},
        "supports_claims": ["C085", "C014"],
        "notes": ""
    },
    {
        "evidence_id": "E093",
        "evidence_text": "Gemini's lengthy, confident reports were the clearest case of the form of scholarship without its substance — an illusion of comprehensive inquiry dissolving on inspection.",
        "evidence_type": "observation",
        "verbatim_quote": "Gemini's lengthy, confident reports were the clearest case of the form of scholarship without its substance, an illusion of comprehensive inquiry that dissolved on inspection.",
        "location": {"section": "4.1 Literature discovery and synthesis", "page": 11},
        "supports_claims": ["C085"],
        "notes": ""
    },
    {
        "evidence_id": "E094",
        "evidence_text": "No system could detect that two sources contradicted one another, weigh competing authorities, or notice when accumulating evidence pointed somewhere other than the sources' stated conclusions.",
        "evidence_type": "observation",
        "verbatim_quote": "None of the systems could detect that two sources contradicted one another, weigh competing authorities, or notice when accumulating evidence pointed somewhere other than the sources' stated conclusions.",
        "location": {"section": "4.1 Literature discovery and synthesis", "page": 11},
        "supports_claims": ["C085"],
        "notes": ""
    },
]

CLAIMS = [
    {
        "claim_id": "C080",
        "claim_text": "The systems could augment work but not automate it: every stage that produced usable output did so because a human-built guard gated that output.",
        "claim_type": "empirical",
        "claim_role": "core",
        "verbatim_quote": "We found that the systems could augment work, but not automate it; every stage that produced usable output did so because a human-built guard gated that output.",
        "location": {"section": "4 Results", "page": 9},
        "supported_by": ["E066", "E068", "E069", "E070", "E071", "E073", "E086", "E087"],
        "supports_claims": ["C008", "C017"],
        "notes": "Headline empirical result for the 2025 campaign."
    },
    {
        "claim_id": "C081",
        "claim_text": "Each tool is reported on what it showed itself able to do in authentic research, measured against its intended use.",
        "claim_type": "methodological_argument",
        "claim_role": "supporting",
        "verbatim_quote": "We report what each tool showed itself able to do in authentic research, measured against its intended use.",
        "location": {"section": "4 Results", "page": 9},
        "supported_by": [],
        "supports_claims": ["C070"],
        "notes": "Reporting-standard claim."
    },
    {
        "claim_id": "C082",
        "claim_text": "The pattern across literature-discovery services indicates a trade between coverage and precision.",
        "claim_type": "empirical",
        "claim_role": "intermediate",
        "verbatim_quote": "The pattern across services indicates a trade between coverage and precision.",
        "location": {"section": "4.1 Literature discovery and synthesis", "page": 9},
        "supported_by": ["E069", "E070", "E071", "E074", "E075", "E076", "E077", "E082", "E083"],
        "supports_claims": ["C083"],
        "notes": ""
    },
    {
        "claim_id": "C083",
        "claim_text": "AI-assisted discovery was a genuine augmentation, contributing dozens of valid sources that conventional faceted search failed to surface.",
        "claim_type": "empirical",
        "claim_role": "intermediate",
        "verbatim_quote": "AI-assisted discovery was a genuine augmentation: it contributed dozens of valid sources that conventional faceted search failed to surface.",
        "location": {"section": "4.1 Literature discovery and synthesis", "page": 10},
        "supported_by": ["E069", "E072", "E073", "E085", "E088"],
        "supports_claims": ["C080", "C034"],
        "notes": ""
    },
    {
        "claim_id": "C084",
        "claim_text": "The resulting corpus was richer than traditional search alone would have produced, but required human verification, extension, or correction of the LLM's work at each step.",
        "claim_type": "empirical",
        "claim_role": "intermediate",
        "verbatim_quote": "The resulting corpus was richer than what would have been found through traditional search alone, but required human verification and extension or correction of the LLM's work at each step.",
        "location": {"section": "4.1 Literature discovery and synthesis", "page": 10},
        "supported_by": ["E080", "E081", "E086", "E087", "E089"],
        "supports_claims": ["C080"],
        "notes": ""
    },
    {
        "claim_id": "C085",
        "claim_text": "When the same systems were asked to synthesise rather than find sources, the augmentation evaporated.",
        "claim_type": "empirical",
        "claim_role": "intermediate",
        "verbatim_quote": "When the same systems were asked not to find sources but to synthesise them, the augmentation evaporated.",
        "location": {"section": "4.1 Literature discovery and synthesis", "page": 11},
        "supported_by": ["E090", "E091", "E092", "E093", "E094"],
        "supports_claims": ["C080", "C008"],
        "notes": ""
    },
    {
        "claim_id": "C086",
        "claim_text": "The authors do not anticipate using any of the AI synthesis reports when writing up the software-longevity study.",
        "claim_type": "empirical",
        "claim_role": "supporting",
        "verbatim_quote": "We do not anticipate using any of these synthesis reports when we write up the software-longevity study.",
        "location": {"section": "4.1 Literature discovery and synthesis", "page": 11},
        "supported_by": ["E090"],
        "supports_claims": ["C085"],
        "notes": ""
    },
]

IMPLICIT_ARGUMENTS = [
    {
        "implicit_argument_id": "IA011",
        "argument_text": "The traditional-search baseline used (one Web of Science query round, a parallel Scopus search, and the pre-existing corpus) adequately represents what skilled conventional search would surface, so the 'genuine augmentation' comparison is fair.",
        "type": "bridging_claim",
        "trigger_text": [
            "AI-assisted discovery was a genuine augmentation: it contributed dozens of valid sources that conventional faceted search failed to surface.",
            "A Web of Science query across the same scope produced three relevant results from the first 50 returned, but the corpus already held all three. A parallel Scopus search fared similarly, contributing only one new source."
        ],
        "trigger_locations": [
            {"section": "4.1 Literature discovery and synthesis", "page": 10},
            {"section": "4.1 Literature discovery and synthesis", "page": 10}
        ],
        "inference_reasoning": "The augmentation claim is comparative, and its baseline is a bounded conventional-search effort (first 50 WoS results; one Scopus pass; the existing corpus). Concluding genuine augmentation requires the unstated bridge that a more exhaustive conventional effort would not have closed the gap.",
        "supports_claims": ["C083"],
        "assessment_implications": "Baseline construction governs the size of the claimed augmentation; the direction (dozens of unique valid sources) is robust but the magnitude depends on baseline effort."
    },
    {
        "implicit_argument_id": "IA012",
        "argument_text": "Scholarly synthesis is defined by evaluation — registering tensions and contradictions, weighing authorities, following evidence against stated conclusions — so accumulation without these operations fails as synthesis regardless of fluency.",
        "type": "unstated_assumption",
        "trigger_text": [
            "Every model tested handled synthesis as accumulation rather than evaluation: it laid one source beside another without registering the tensions, contradictions, or temporal context that turn a pile of references into an argument.",
            "None of the systems could detect that two sources contradicted one another, weigh competing authorities, or notice when accumulating evidence pointed somewhere other than the sources' stated conclusions."
        ],
        "trigger_locations": [
            {"section": "4.1 Literature discovery and synthesis", "page": 11},
            {"section": "4.1 Literature discovery and synthesis", "page": 11}
        ],
        "inference_reasoning": "The synthesis-failure verdict rests on an implicit normative definition of synthesis quality (evaluative operations over accumulation). The definition is plausible and disciplinarily grounded but is not operationalised or measured; the verdict is qualitative expert judgement against that unstated standard.",
        "supports_claims": ["C085", "C086"],
        "assessment_implications": "The synthesis findings are qualitative judgements rather than counted outcomes; their force depends on accepting the implied definition of synthesis."
    },
]

save_group(
    {
        "group": "G6",
        "section_title": "Results 4 (intro/coverage) + 4.1 Literature discovery and synthesis",
        "page_range": "9-11",
        "estimated_words": 1190,
        "natural_boundary": "Before '4.2 Tool discovery' heading (p. 11)",
        "split_rationale": "Results opening and the first stage; Tables 1-3 extracted as flattened row quotes with caption semantics in notes."
    },
    evidence=EVIDENCE,
    claims=CLAIMS,
    implicit_arguments=IMPLICIT_ARGUMENTS,
)
