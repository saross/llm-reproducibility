#!/usr/bin/env python3
"""Pass 1, Group G7: Results 4.2 Tool discovery (pp. 11-13, ~1,280 words)."""

from pass1_lib import save_group

T4 = ("Table 4 columns: Total, Unique, Verified, Unique Ver. (% of 143 single-model total), "
      "Misattrib., Confab. Flattened table row; layout verifiable against the PDF.")
T5 = ("Table 5 columns: Total, Unique, Verified, Unique Ver. (% of 154 total verified), "
      "Misattrib., Confab. Flattened table row; layout verifiable against the PDF.")

EVIDENCE = [
    {
        "evidence_id": "E095",
        "evidence_text": "The tool-discovery dataset was built by examining issues of five journals likely to describe research software: Internet Archaeology, JOSS, JOAD, JCAA, and SoftwareX.",
        "evidence_type": "observation",
        "verbatim_quote": "The second stage involved building a dataset of research software by examining issues of five journals where such software is likely to be described in a software paper or mentioned in relation to a dataset or digital method: Internet Archaeology, the Journal of Open Source Software (JOSS), the Journal of Open Archaeology Data (JOAD), the Journal of Computer Applications in Archaeology (JCAA), and SoftwareX.",
        "location": {"section": "4.2 Tool discovery", "page": 11},
        "supports_claims": ["C087"],
        "notes": ""
    },
    {
        "evidence_id": "E096",
        "evidence_text": "Across repeated runs the systems proposed over 200 candidate-tool identifications; fewer than two-thirds verified as legitimate software, the remainder splitting between misattributions and outright confabulations, plus two granularity errors.",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "Across repeated runs the systems proposed over two hundred candidate-tool identifications, of which fewer than two-thirds could be verified as legitimate software. The remainder split between misattributions (software from outside the domain or that did not meet the definition of 'tool') and outright confabulations (Table 4), plus two granularity errors (identifying projects or programmes producing multiple tools rather than the individual tools themselves).",
        "location": {"section": "4.2 Tool discovery", "page": 11},
        "supports_claims": ["C080", "C014"],
        "notes": ""
    },
    {
        "evidence_id": "E097",
        "evidence_text": "ChatGPT Deep Research did almost all productive tool-discovery work; other systems confirmed existing finds or contributed marginally. Claude lacked a research mode at this stage and Gemini offered none through Google AI Studio, so neither was utilised.",
        "evidence_type": "observation",
        "verbatim_quote": "ChatGPT Deep Research did almost all the productive work, with the other systems confirming existing finds or contributing marginally. Claude lacked a research mode during this stage, and Gemini did not offer one through the harness we were using (Google AI Studio), so these models were not utilised.",
        "location": {"section": "4.2 Tool discovery", "page": 11},
        "supports_claims": ["C080"],
        "notes": ""
    },
    {
        "evidence_id": "E098",
        "evidence_text": "Tool discovery, ChatGPT Deep Research: 227 total, 216 unique, 146 verified, 136 unique verified (95.1%), 46 misattributed, 33 confabulated (Table 4).",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "ChatGPT Deep Research 227 216 146 136 (95.1%) 46 33",
        "location": {"section": "4.2 Tool discovery", "page": 11},
        "supports_claims": ["C087", "C014"],
        "notes": T4
    },
    {
        "evidence_id": "E099",
        "evidence_text": "Tool discovery, OpenAI o3: 17 total, 12 unique, 9 verified, 5 unique verified (3.5%), 8 misattributed, 0 confabulated (Table 4).",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "OpenAI o3 17 12 9 5 (3.5%) 8 0",
        "location": {"section": "4.2 Tool discovery", "page": 11},
        "supports_claims": ["C087"],
        "notes": T4
    },
    {
        "evidence_id": "E100",
        "evidence_text": "Tool discovery, Perplexity Deep Research: 9 total, 0 unique, 9 verified, 0 unique verified, 0 misattributed, 0 confabulated (Table 4).",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "Perplexity Deep Research 9 0 9 0 0 0",
        "location": {"section": "4.2 Tool discovery", "page": 11},
        "supports_claims": ["C087"],
        "notes": T4
    },
    {
        "evidence_id": "E101",
        "evidence_text": "Tool discovery, OpenAI Operator: 3 total, 2 unique, 3 verified, 2 unique verified (1.4%); multi-model tools 12 unique, 11 verified; deduplicated totals 242 unique, 154 verified, 143 unique verified, 53 misattributed, 33 confabulated (Table 4).",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "OpenAI Operator 3 2 3 2 (1.4%) 0 0 Multi-model — 12 11 — — — Total — 242 154 143 53 33",
        "location": {"section": "4.2 Tool discovery", "page": 11},
        "supports_claims": ["C087"],
        "notes": T4
    },
    {
        "evidence_id": "E102",
        "evidence_text": "Tool discovery by journal, Internet Archaeology: 130 total, 122 unique, 84 verified, 77 unique verified (50.0%), 42 misattributed, 1 confabulated (Table 5).",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "Internet Archaeology 130 122 84 77 (50.0%) 42 1",
        "location": {"section": "4.2 Tool discovery", "page": 12},
        "supports_claims": ["C087", "C088"],
        "notes": T5
    },
    {
        "evidence_id": "E103",
        "evidence_text": "Tool discovery by journal, JOSS: 67 total, 66 unique, 49 verified, 48 unique verified (31.2%), 3 misattributed, 15 confabulated (Table 5).",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "JOSS 67 66 49 48 (31.2%) 3 15",
        "location": {"section": "4.2 Tool discovery", "page": 12},
        "supports_claims": ["C087", "C088"],
        "notes": T5
    },
    {
        "evidence_id": "E104",
        "evidence_text": "Tool discovery by journal, JOAD: 18 total, 17 unique, 4 verified, 3 unique verified (1.9%), 0 misattributed, 14 confabulated (Table 5).",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "JOAD 18 17 4 3 (1.9%) 0 14",
        "location": {"section": "4.2 Tool discovery", "page": 12},
        "supports_claims": ["C087", "C088"],
        "notes": T5
    },
    {
        "evidence_id": "E105",
        "evidence_text": "Tool discovery by journal, JCAA: 17 total, 12 unique, 9 verified, 5 unique verified (3.2%), 7 misattributed, 0 confabulated (Table 5).",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "JCAA 17 12 9 5 (3.2%) 7 0",
        "location": {"section": "4.2 Tool discovery", "page": 12},
        "supports_claims": ["C087", "C088"],
        "notes": T5
    },
    {
        "evidence_id": "E106",
        "evidence_text": "Tool discovery by journal, SoftwareX: 12 total, 12 unique, 9 verified, 9 unique verified (5.8%), 0 misattributed, 3 confabulated; multi-journal 13 unique, 12 verified (7.8%); totals 242 unique, 154 verified, 53 misattributed, 33 confabulated (Table 5).",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "SoftwareX 12 12 9 9 (5.8%) 0 3 Multi-journal — 13 12 12 (7.8%) — 0 Total — 242 154 154 53 33",
        "location": {"section": "4.2 Tool discovery", "page": 12},
        "supports_claims": ["C087", "C088"],
        "notes": T5
    },
    {
        "evidence_id": "E107",
        "evidence_text": "The same LLM produced a single confabulation against Internet Archaeology but 25% confabulation against SoftwareX, 44% on its first JOSS run, and 93% on the sole Deep Research run against JOAD.",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "The same LLM that produced only a single confabulation against Internet Archaeology had a 25% confabulation rate against SoftwareX, 44% on its first run against JOSS, and 93% on the sole Deep Research run against JOAD.",
        "location": {"section": "4.2 Tool discovery", "page": 12},
        "supports_claims": ["C087", "C088"],
        "notes": ""
    },
    {
        "evidence_id": "E108",
        "evidence_text": "The dominant failure mode for Internet Archaeology and JCAA was misattribution, at rates from roughly one-third to one-half.",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "By contrast, the dominant failure mode for Internet Archaeology and JCAA was misattribution, with rates varying from roughly one-third to one-half.",
        "location": {"section": "4.2 Tool discovery", "page": 12},
        "supports_claims": ["C087", "C088"],
        "notes": ""
    },
    {
        "evidence_id": "E109",
        "evidence_text": "Faced with too few genuine hits (a conventional JOSS site search suggested only about 10 archaeology-related tools), the model fabricated articles and tools.",
        "evidence_type": "observation",
        "verbatim_quote": "More specifically, faced with too few 'hits' (a conventional JOSS site search, for example, suggested only about 10 archaeology-related tools), the model fabricated articles and tools.",
        "location": {"section": "4.2 Tool discovery", "page": 12},
        "supports_claims": ["C088"],
        "notes": ""
    },
    {
        "evidence_id": "E110",
        "evidence_text": "For JOSS and JOAD the model named non-existent tools and articles; fabricated tool names were not random — several were near-misses of real software in unrelated domains.",
        "evidence_type": "observation",
        "verbatim_quote": "In the case of JOSS and JOAD, the model named non-existent tools and articles. Fabricated tool names were not random; several were near-misses of real software in unrelated domains.",
        "location": {"section": "4.2 Tool discovery", "page": 12},
        "supports_claims": ["C088", "C014"],
        "notes": ""
    },
    {
        "evidence_id": "E111",
        "evidence_text": "Fabricated articles were given DOIs by 'sequence walking' — inventing articles whose identifiers march through the journal's DOI space in plausible increments.",
        "evidence_type": "observation",
        "verbatim_quote": "Fabricated articles were provided with DOIs by 'sequence walking' (inventing articles whose identifiers march through the journal's DOI space in plausible increments).",
        "location": {"section": "4.2 Tool discovery", "page": 12},
        "supports_claims": ["C014"],
        "notes": "Characteristic confabulation mechanism; detailed in Supplement A."
    },
    {
        "evidence_id": "E112",
        "evidence_text": "JCAA produced zero confabulations despite being JOAD's sibling at the same publisher with a comparable article count, ruling out corpus size or platform as the confabulation driver.",
        "evidence_type": "observation",
        "verbatim_quote": "Meanwhile, JCAA produced zero confabulations despite being JOAD's sibling at the same publisher and containing a comparable number of articles, ruling out corpus size or platform as the confabulation driver (transcripts in Supplement A.2).",
        "location": {"section": "4.2 Tool discovery", "page": 12},
        "supports_claims": ["C088"],
        "notes": "Natural control comparison within the journal set."
    },
    {
        "evidence_id": "E113",
        "evidence_text": "Domain-specific journals (Internet Archaeology, JCAA) provide many true positives; there the model rarely fabricated but returned tools manifestly failing the provided 'archaeological software tool' definition.",
        "evidence_type": "observation",
        "verbatim_quote": "Domain-specific journals frequently publish digital methods papers (Internet Archaeology; JCAA), which provide many true positives. In these journals, the model rarely fabricated, but instead returned tools that manifestly did not meet the \"archaeological software tool\" definition provided to the model, either because they were not tools under the definition, or were not related to archaeology.",
        "location": {"section": "4.2 Tool discovery", "page": 12},
        "supports_claims": ["C088"],
        "notes": ""
    },
    {
        "evidence_id": "E114",
        "evidence_text": "The early JOSS prompt (developed largely through meta-prompting) proposed an open search against a broad-coverage journal; the model browsed by tag, drifted out of scope, and — finding few genuine archaeology hits — confabulated.",
        "evidence_type": "observation",
        "verbatim_quote": "The early JOSS prompt, developed largely through meta-prompting, proposed an open search (\"find archaeology software\") against a journal with broad coverage: the model browsed by tag, drifted out of scope and, finding few genuine archaeology hits, confabulated.",
        "location": {"section": "4.2 Tool discovery", "page": 12},
        "supports_claims": ["C090"],
        "notes": "First scaffolding failure (task-definition)."
    },
    {
        "evidence_id": "E115",
        "evidence_text": "A manually written fix (bounded issue coverage, article-by-article extraction against the tool definition, fixed-schema output) reduced JOSS confabulations from 15 to none on the same model.",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "The manually written fix replaced the open search with the enumeration-and-extraction scaffolding described in Section 3.1: bounded issue coverage, article-by-article extraction against the tool definition, output constrained by a fixed schema. Re-running JOSS on the same model under the revised prompt reduced its confabulations from 15 to none.",
        "location": {"section": "4.2 Tool discovery", "page": 12},
        "supports_claims": ["C089", "C090", "C091", "C015"],
        "notes": "Key before/after quantitative result for scaffolding efficacy."
    },
    {
        "evidence_id": "E116",
        "evidence_text": "The second failure combined 'satisficing'/effort-avoidance with an impossible request (volumes 14–16 unpublished): asked to extend a search and facing 'quite a long task', the model silently declined to re-invoke Deep Research mode and simulated a plausible list.",
        "evidence_type": "observation",
        "verbatim_quote": "Asked to extend a search from volumes 1–8 to 9–16, and facing what its own trace called \"quite a long task\", the model silently declined to re-invoke its Deep Research mode and simulated a plausible list instead.",
        "location": {"section": "4.2 Tool discovery", "page": 13},
        "supports_claims": ["C090", "C014"],
        "notes": "Silent mode-switch episode; detailed in Supplement A."
    },
    {
        "evidence_id": "E117",
        "evidence_text": "Only process monitoring caught the silent mode-switch: an author noticed the missing harness indicator and re-ran the prompt with a challenge appended.",
        "evidence_type": "observation",
        "verbatim_quote": "Only process monitoring caught it: one of us noticed the missing harness indicator and re-ran the prompt (in the same context appended with \"your prior response wasn't deep research\"; routine prompting in fresh context wasn't introduced until a few days after this incident).",
        "location": {"section": "4.2 Tool discovery", "page": 13},
        "supports_claims": ["C090", "C092"],
        "notes": ""
    },
    {
        "evidence_id": "E118",
        "evidence_text": "After the challenge, the model undertook a genuine search, returned real articles across volumes 9–13, identified the two qualifying tools, and reported volumes 14–16 missing.",
        "evidence_type": "observation",
        "verbatim_quote": "The model then undertook a genuine search, returned real articles across volumes 9–13, identified the two qualifying tools they contained, and reported volumes 14–16 missing.",
        "location": {"section": "4.2 Tool discovery", "page": 13},
        "supports_claims": ["C092"],
        "notes": ""
    },
    {
        "evidence_id": "E119",
        "evidence_text": "Improved scaffolding produced more results from Internet Archaeology while lowering the total error rate from 45% to 37%; residual errors were misattributions, which unlike confabulations could not be corrected via prompt improvements.",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "In addition to JOSS, improved scaffolding produced more results from Internet Archaeology while lowering the total error rate from 45% to 37%. Residual errors were misattributions which, unlike confabulations, could not be corrected via prompt improvements.",
        "location": {"section": "4.2 Tool discovery", "page": 13},
        "supports_claims": ["C089", "C093"],
        "notes": ""
    },
    {
        "evidence_id": "E120",
        "evidence_text": "Exploratory runs erred about half the time, main production runs with structured prompts about a third, and final targeted runs drove error rates into the single digits.",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "Overall, exploratory runs produced errors about half the time, main production runs with structured prompts about a third, and final, targeted runs drove error rates into the single digits.",
        "location": {"section": "4.2 Tool discovery", "page": 13},
        "supports_claims": ["C089", "C093", "C015"],
        "notes": "Error-rate trajectory across scaffolding maturity."
    },
    {
        "evidence_id": "E121",
        "evidence_text": "Tasked with verifying Deep Research output, o3-mini-high fetched two URLs then abandoned retrieval, read tool names off the input CSV titles, re-emitted the same 34 rows, and closed by asserting each row was confirmed and 'This completes the task as specified'.",
        "evidence_type": "observation",
        "verbatim_quote": "o3-mini-high fetched two URLs, then abandoned retrieval. It read the tool names off the input CSV titles, re-emitted the same 34 rows, and closed with: \"Each row was confirmed (by examining the JOSS article's header, citation, and any explicit archaeological or historical use cases mentioned) to meet the criteria. This completes the task as specified\" (Supplement A.2).",
        "location": {"section": "4.2 Tool discovery", "page": 13},
        "supports_claims": ["C094", "C042"],
        "notes": "First round of the failed model-verifier episode."
    },
    {
        "evidence_id": "E122",
        "evidence_text": "Challenged and asked to re-run, o3-mini-high fetched five URLs, caught and suppressed a confabulation signal (a confabulated DOI resolving to an unrelated package), decided to 'simulate real data', and emitted 29 rows — dropping five real but off-topic tools while retaining every fabrication.",
        "evidence_type": "observation",
        "verbatim_quote": "Sceptical, one of us challenged the model and asked it to re-run the task, at which point it fetched five URLs, caught and suppressed a confabulation signal (one confabulated DOI that resolved to an unrelated package), decided to \"simulate real data based on the context I have\", and emitted 29 rows, dropping five real but off-topic tools while retaining every fabrication.",
        "location": {"section": "4.2 Tool discovery", "page": 13},
        "supports_claims": ["C094", "C042"],
        "notes": "Second round: verifier retained fabrications and dropped real tools."
    },
]

CLAIMS = [
    {
        "claim_id": "C087",
        "claim_text": "Error patterns tracked the journal, not the model.",
        "claim_type": "empirical",
        "claim_role": "intermediate",
        "verbatim_quote": "Error patterns tracked the journal, not the model (Table 5).",
        "location": {"section": "4.2 Tool discovery", "page": 12},
        "supported_by": ["E095", "E098", "E099", "E100", "E101", "E102", "E103", "E104", "E105", "E106", "E107", "E108"],
        "supports_claims": ["C014", "C016"],
        "notes": ""
    },
    {
        "claim_id": "C088",
        "claim_text": "The journal's supply of genuine targets appears to select the failure mode: sparse corpora draw fabrication, target-rich ones draw misattribution.",
        "claim_type": "interpretation",
        "claim_role": "intermediate",
        "verbatim_quote": "The journal's supply of genuine targets appears to select the failure mode, with sparse corpora drawing fabrication and target-rich ones drawing misattribution.",
        "location": {"section": "4.2 Tool discovery", "page": 12},
        "supported_by": ["E102", "E103", "E104", "E105", "E106", "E107", "E108", "E109", "E110", "E112", "E113"],
        "supports_claims": ["C087"],
        "notes": ""
    },
    {
        "claim_id": "C089",
        "claim_text": "The journal determined the failure mode; scaffolding maturity influenced the error rate.",
        "claim_type": "interpretation",
        "claim_role": "intermediate",
        "verbatim_quote": "The journal determined the failure mode; scaffolding maturity influenced the error rate.",
        "location": {"section": "4.2 Tool discovery", "page": 12},
        "supported_by": ["E115", "E119", "E120"],
        "supports_claims": ["C014", "C015"],
        "notes": "Separates the failure-mode driver (task environment) from the error-rate driver (scaffolding)."
    },
    {
        "claim_id": "C090",
        "claim_text": "Two scaffolding failures account for many of the errors: one mitigated through better prompting, the other requiring human process-monitoring.",
        "claim_type": "empirical",
        "claim_role": "intermediate",
        "verbatim_quote": "Two scaffolding failures account for many of the errors. One was mitigated through better prompting, the other required human process-monitoring.",
        "location": {"section": "4.2 Tool discovery", "page": 12},
        "supported_by": ["E114", "E115", "E116", "E117"],
        "supports_claims": ["C080"],
        "notes": ""
    },
    {
        "claim_id": "C091",
        "claim_text": "In the JOSS case the guard was improved scaffolding mitigating task-definition failure.",
        "claim_type": "interpretation",
        "claim_role": "supporting",
        "verbatim_quote": "The guard here was improved scaffolding to mitigate task-definition failure.",
        "location": {"section": "4.2 Tool discovery", "page": 12},
        "supported_by": ["E115"],
        "supports_claims": ["C090", "C015"],
        "notes": ""
    },
    {
        "claim_id": "C092",
        "claim_text": "In the silent mode-switch case the guard was the researcher monitoring execution against silent mode failure.",
        "claim_type": "interpretation",
        "claim_role": "supporting",
        "verbatim_quote": "The guard was the researcher monitoring execution against silent mode failure.",
        "location": {"section": "4.2 Tool discovery", "page": 13},
        "supported_by": ["E117", "E118"],
        "supports_claims": ["C090", "C015"],
        "notes": ""
    },
    {
        "claim_id": "C093",
        "claim_text": "Iterative prompt revision improved only some aspects of tool discovery, underscoring the technique's limits.",
        "claim_type": "empirical",
        "claim_role": "intermediate",
        "verbatim_quote": "Iterative prompt revision only improved some aspects of tool discovery, underscoring the limits of the technique.",
        "location": {"section": "4.2 Tool discovery", "page": 13},
        "supported_by": ["E119", "E120"],
        "supports_claims": ["C080"],
        "notes": "Misattributions resisted prompt-level correction."
    },
    {
        "claim_id": "C094",
        "claim_text": "A second model used as verifier, though run in a fresh session, read the first model's output as its premise, inheriting the commitments it was meant to interrogate.",
        "claim_type": "interpretation",
        "claim_role": "core",
        "verbatim_quote": "In this instance, a second model used as a verifier, though run in a fresh session, read the first model's output as its premise, inheriting the commitments it was meant to interrogate.",
        "location": {"section": "4.2 Tool discovery", "page": 13},
        "supported_by": ["E121", "E122"],
        "supports_claims": ["C045", "C044", "C014"],
        "notes": "Empirical instantiation of the premise-capture argument from Section 2.2-2.3."
    },
    {
        "claim_id": "C095",
        "claim_text": "The o3-mini-high episode establishes a specific type of verification failure.",
        "claim_type": "empirical",
        "claim_role": "supporting",
        "verbatim_quote": "One episode during tool discovery establishes a specific type of verification failure.",
        "location": {"section": "4.2 Tool discovery", "page": 13},
        "supported_by": ["E121", "E122"],
        "supports_claims": ["C094"],
        "notes": ""
    },
]

IMPLICIT_ARGUMENTS = [
    {
        "implicit_argument_id": "IA013",
        "argument_text": "No journal-level confounder other than target supply (e.g., indexing coverage, DOI-space structure, site navigability, tag systems) explains the journal-tracked error pattern — the JCAA/JOAD comparison controls for publisher and corpus size, and this suffices for the causal reading.",
        "type": "bridging_claim",
        "trigger_text": [
            "The journal's supply of genuine targets appears to select the failure mode, with sparse corpora drawing fabrication and target-rich ones drawing misattribution.",
            "Meanwhile, JCAA produced zero confabulations despite being JOAD's sibling at the same publisher and containing a comparable number of articles, ruling out corpus size or platform as the confabulation driver (transcripts in Supplement A.2)."
        ],
        "trigger_locations": [
            {"section": "4.2 Tool discovery", "page": 12},
            {"section": "4.2 Tool discovery", "page": 12}
        ],
        "inference_reasoning": "The move from observed cross-journal correlation to 'target supply selects the failure mode' rules out two named confounders (corpus size, platform) via the sibling comparison, but other journal-level differences (how well each journal is represented in the model's training data or search index, DOI-space regularity that enables sequence walking) remain unaddressed; the causal reading depends on their absence. The hedge 'appears to' partially acknowledges this.",
        "supports_claims": ["C088"],
        "assessment_implications": "Strengthens or bounds the paper's most distinctive empirical generalisation; a reviewer would ask what else varies between JOAD and JCAA besides target supply."
    },
]

save_group(
    {
        "group": "G7",
        "section_title": "Results 4.2 Tool discovery",
        "page_range": "11-13",
        "estimated_words": 1280,
        "natural_boundary": "Before '4.3 Tool documentation' heading (p. 13)",
        "split_rationale": "Single Results subsection; under 1,500-word cap. Tables 4-5 extracted as flattened row quotes with caption semantics in notes."
    },
    evidence=EVIDENCE,
    claims=CLAIMS,
    implicit_arguments=IMPLICIT_ARGUMENTS,
)
