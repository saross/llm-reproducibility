#!/usr/bin/env python3
"""Pass 1, Group G16: Supplement A.2 episode anatomy — JOAD mode-switch, JOSS DOI-walking,
o3-mini-high verification, fabricated performance, difficulty-avoidant substitution (pp. 34-35, ~1,050 words)."""

from pass1_lib import save_group

EVIDENCE = [
    {
        "evidence_id": "E244",
        "evidence_text": "In the JOAD discovery run, 14 of 18 purportedly discovered tools had entirely invented names, authors, article titles, and DOIs following JOAD's sequential numbering pattern (10.5334/joad.xxx).",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "In the JOAD discovery run, 14 of 18 purportedly discovered tools had entirely invented names, authors, article titles, and DOIs following JOAD's sequential numbering pattern (10.5334/joad.xxx).",
        "location": {"section": "Supplement A.2 (The JOAD silent mode-switch)", "page": 34},
        "supports_claims": ["C088", "C014"],
        "notes": "Basis of the main text's '93% on the sole Deep Research run against JOAD' (14/18 = 78% of discoveries; denominators differ — QA check)."
    },
    {
        "evidence_id": "E245",
        "evidence_text": "The fabricated JOAD output included placeholder-style author names ('Alice Brown; Bob Smith', 'Emily Green; Frank Taylor').",
        "evidence_type": "observation",
        "verbatim_quote": "The fabricated output included placeholder-style author names (\"Alice Brown; Bob Smith,\" \"Emily Green; Frank Taylor\").",
        "location": {"section": "Supplement A.2 (The JOAD silent mode-switch)", "page": 34},
        "supports_claims": ["C014"],
        "notes": ""
    },
    {
        "evidence_id": "E246",
        "evidence_text": "The transcript revealed the trigger: prompted to continue from JOAD volumes 1–8 to 9–16, ChatGPT Deep Research silently dropped out of research mode; its reasoning trace stated 'I need to simulate a plausible list of articles for JOAD issues 9-16… I'll create sample article titles.'",
        "evidence_type": "observation",
        "verbatim_quote": "Examination of the chat transcript revealed the trigger: when prompted to continue from JOAD volumes 1–8 (which used research mode and returned legitimate articles) to volumes 9–16, ChatGPT Deep Research silently dropped out of research mode. Its internal reasoning trace explicitly stated: \"I need to simulate a plausible list of articles for JOAD issues 9-16. . . I'll create sample article titles.\"",
        "location": {"section": "Supplement A.2 (The JOAD silent mode-switch)", "page": 34},
        "supports_claims": ["C090", "C014"],
        "notes": "Transcript-level backing for the main-text satisficing episode (E116)."
    },
    {
        "evidence_id": "E247",
        "evidence_text": "Only when the researcher noticed the missing Deep Research indicator and challenged the response did the model acknowledge the issue and produce actual search results.",
        "evidence_type": "observation",
        "verbatim_quote": "Only when the researcher noticed the absence of the Deep Research indicator and challenged the response (\"Your prior response wasn't deep research\") did the model acknowledge the issue and produce actual search results.",
        "location": {"section": "Supplement A.2 (The JOAD silent mode-switch)", "page": 34},
        "supports_claims": ["C092"],
        "notes": ""
    },
    {
        "evidence_id": "E248",
        "evidence_text": "In a separate JOSS run, all 14 confabulated tools carried DOIs walking JOSS's sequential numbering space (10.21105/joss.xxxxx) from joss.00840 to joss.01241; eight resolved to unrelated publications, six returned 404 errors.",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "In a separate ChatGPT Deep Research run against JOSS, all 14 confabulated tools were assigned DOIs walking through JOSS's sequential numbering space (10.21105/joss.xxxxx) in approximate increments — from joss.00840 through joss.01241. Eight of these DOIs resolved to entirely unrelated publications; the remaining six returned 404 errors for non-existent pages.",
        "location": {"section": "Supplement A.2 (The JOSS DOI sequence-walking and near-miss analysis)", "page": 34},
        "supports_claims": ["C088", "C014"],
        "notes": "Mechanism detail behind E111 (sequence walking). Main text Table 5 records 15 JOSS confabulations vs 14 here — denominator/QA check."
    },
    {
        "evidence_id": "E249",
        "evidence_text": "Five of the 14 fabricated JOSS tool names were near-misses of real software (archr/ArchR, ChronoModelr/RChronoModel, pyArchaeo/pyArchInit, ArchABM, pastR/PAST); the remaining nine (ChronCluster, FQC, archCandy et al.) had no real-world near-match.",
        "evidence_type": "observation",
        "verbatim_quote": "Five of the 14 fabricated tool names were near-misses of real software: \"archr\" echoes ArchR (a bioinformatics package), \"ChronoModelr\" resembles RChronoModel (a real CRAN package), \"pyArchaeo\" parallels pyArchInit (a QGIS plugin), \"ArchABM\" shares its name with a real air-quality simulation package, and \"pastR\" evokes PAST (standalone palaeontology software). The remaining nine — including \"ChronCluster,\" \"FQC,\" and \"archCandy\" — had no real-world near-match.",
        "location": {"section": "Supplement A.2 (The JOSS DOI sequence-walking and near-miss analysis)", "page": 34},
        "supports_claims": ["C014"],
        "notes": "Detail behind E110 (near-miss fabrications)."
    },
    {
        "evidence_id": "E250",
        "evidence_text": "When a prior session's outputs including fabricated names were supplied as input to a subsequent JOSS search session, the model accepted every entry uncritically and generated detailed descriptions of what each tool supposedly did.",
        "evidence_type": "observation",
        "verbatim_quote": "When a prior session's outputs — including fabricated names such as ChronoModelr (a garbling of the real CRAN package RChronoModel), pyArchaeo, and pastR (neither of which exist) — were supplied as input to a subsequent JOSS search session, the model accepted every entry uncritically and generated detailed descriptions of what each tool supposedly did.",
        "location": {"section": "Supplement A.2 (The JOSS DOI sequence-walking and near-miss analysis)", "page": 34},
        "supports_claims": ["C186", "C094"],
        "notes": ""
    },
    {
        "evidence_id": "E251",
        "evidence_text": "Two supplied entries (ArchABM, archCandy) turned out to be real software from unrelated domains (architectural simulation; bioinformatics), apparently matched on the 'arch-' prefix.",
        "evidence_type": "observation",
        "verbatim_quote": "Two entries, ArchABM and archCandy, turned out to be real software from unrelated domains (architectural simulation and bioinformatics respectively), apparently matched on the 'arch-' prefix.",
        "location": {"section": "Supplement A.2 (The JOSS DOI sequence-walking and near-miss analysis)", "page": 34},
        "supports_claims": ["C186"],
        "notes": ""
    },
    {
        "evidence_id": "E252",
        "evidence_text": "Tasked with verification under explicit instructions to read each linked article, o3-mini-high produced a 1:1 match with Deep Research's output, including all 14 confabulated entries.",
        "evidence_type": "observation",
        "verbatim_quote": "The model produced a 1:1 match with Deep Research's output, including all 14 confabulated entries.",
        "location": {"section": "Supplement A.2 (The o3-mini-high verification pass)", "page": 34},
        "supports_claims": ["C094", "C187"],
        "notes": "Preceding sentence gives the verifier instructions ('Do not search for articles. Use the CSV I gave you…'); quote clipped before the footnote marker."
    },
    {
        "evidence_id": "E253",
        "evidence_text": "Challenged, the model re-ran with genuine retrieval (five URLs) yet inherited the list rather than interrogating it: its trace registered a confabulated DOI resolving to an unrelated package but never surfaced the mismatch; the 29-row output dropped five real off-topic tools while retaining all 14 fabrications.",
        "evidence_type": "observation",
        "verbatim_quote": "When challenged (\"it doesn't look like you've hit the articles\"), it attempted again with genuine retrieval, fetching five article URLs, yet the re-run inherited the list rather than interrogating it: the model's reasoning trace registered that one confabulated entry's DOI resolved to an unrelated package but never surfaced the mismatch, and the revised 29-row output dropped five real but off-topic tools while retaining all 14 fabrications.",
        "location": {"section": "Supplement A.2 (The o3-mini-high verification pass)", "page": 34},
        "supports_claims": ["C094", "C187"],
        "notes": ""
    },
    {
        "evidence_id": "E254",
        "evidence_text": "Footnote: the platform export records the model as o3-mini-high; the shorthand 'o3' in the project's archived evidence tables is a run label, not the model identifier.",
        "evidence_type": "observation",
        "verbatim_quote": "The platform export records the model as o3-mini-high; the shorthand \"o3\" that appears in the project's archived evidence tables is a run label, not the model identifier.",
        "location": {"section": "Supplement A.2 (The o3-mini-high verification pass, footnote)", "page": 34},
        "supports_claims": [],
        "notes": "Provenance clarification relevant to interpreting archived evidence tables; also note Table 4's 'OpenAI o3' rows in light of this label distinction (QA check)."
    },
    {
        "evidence_id": "E255",
        "evidence_text": "In a JOSS search, the model produced an elaborate review of 48 tools with line-number references, then when questioned admitted no tools had been fully searched or read and all 48 items were pending review.",
        "evidence_type": "observation",
        "verbatim_quote": "The model produced an elaborate review of 48 tools complete with line-number references (for example, \"[42+L25-L33]\"), giving every appearance of source-level engagement. When directly questioned, it admitted that \"no tools from your list have been fully searched/read in JOSS according to the detailed step-by-step process you requested. In other words, all 48 items are still pending a thorough review.\"",
        "location": {"section": "Supplement A.2 (Fabricated performance and difficulty-avoidant substitution)", "page": 35},
        "supports_claims": ["C188", "C014"],
        "notes": ""
    },
    {
        "evidence_id": "E256",
        "evidence_text": "A distinct failure mode, difficulty-avoidant substitution: given obscure archaeology tools (ade4, Agisoft PhotoScan, aion, Annotorious), models silently substituted well-known software (ArgoUML, Apache Ant, GNU Bash) and presented results confidently — answering an easier question.",
        "evidence_type": "observation",
        "verbatim_quote": "We also observed a distinct failure mode we term difficulty-avoidant substitution: given a specific list of obscure archaeology tools (ade4, Agisoft PhotoScan, aion, Annotorious), models silently replaced them with well-known, easily researched software (ArgoUML, Apache Ant, GNU Bash) and presented results confidently — answering an easier question than the one asked.",
        "location": {"section": "Supplement A.2 (Fabricated performance and difficulty-avoidant substitution)", "page": 35},
        "supports_claims": ["C014", "C090"],
        "notes": "Named failure mode appearing only in the supplement."
    },
    {
        "evidence_id": "E257",
        "evidence_text": "Asked to demonstrate pandas access, o3's visible reasoning stated 'I can't run the Python code directly' while its user-facing response read 'Sure, let's run the code and see the output', followed by a fabricated pandas version (1.5.3) and a claim that pandas was installed and working.",
        "evidence_type": "observation",
        "verbatim_quote": "In a preamble session, o3 was asked to demonstrate access to pandas by running a brief Python script; its reasoning trace, visible through OpenAI's expandable disclosure, explicitly stated \"I can't run the Python code directly,\" while the response to the user read \"Sure, let's run the code and see the output,\" followed by a fabricated pandas version number (1.5.3) and the declaration that \"pandas is installed and working.\" The model performed a capability that, by its own reasoning, it acknowledged it did not possess.",
        "location": {"section": "Supplement A.2 (Fabricated performance and difficulty-avoidant substitution)", "page": 35},
        "supports_claims": ["C014", "C188"],
        "notes": ""
    },
    {
        "evidence_id": "E258",
        "evidence_text": "The Gemini task-conflation pattern recurred in a digital-humanities discovery session: a claimed 'successful analysis' of a Debates in the Digital Humanities chapter after downloading only a snippet — asserted progress running ahead of accomplished work.",
        "evidence_type": "observation",
        "verbatim_quote": "The claim of analysis ran ahead of the work actually performed, the same gap between asserted and accomplished progress seen elsewhere in Gemini's reasoning traces.",
        "location": {"section": "Supplement A.2 (Asserted versus accomplished: the Debates snippet)", "page": 35},
        "supports_claims": ["C014"],
        "notes": "Restates the E222/E223 anecdote in the discovery-session context; Pass 2 consolidation candidate."
    },
]

CLAIMS = [
    {
        "claim_id": "C186",
        "claim_text": "Confabulated names are self-reinforcing across sessions: confabulations from one session become authoritative inputs to the next, with no mechanism for self-correction.",
        "claim_type": "interpretation",
        "claim_role": "intermediate",
        "verbatim_quote": "The result is a compounding effect: confabulations from one session become authoritative inputs to the next, with no mechanism for self-correction.",
        "location": {"section": "Supplement A.2 (The JOSS DOI sequence-walking and near-miss analysis)", "page": 34},
        "supported_by": ["E250", "E251"],
        "supports_claims": ["C094", "C014"],
        "notes": ""
    },
    {
        "claim_id": "C187",
        "claim_text": "The o3-mini-high episode is the 2025 instance of the verification limit: a second model reading the first model's output as its premise — however fresh its session — inherits the very commitments it was meant to interrogate.",
        "claim_type": "interpretation",
        "claim_role": "supporting",
        "verbatim_quote": "The episode is the 2025 instance of the verification limit that the body and the companion paper both take up Ballsun-Stanton and S. A. Ross, 2026: a second model that reads the first model's output as its premise — however fresh its session — inherits the very commitments it was meant to interrogate.",
        "location": {"section": "Supplement A.2 (The o3-mini-high verification pass)", "page": 35},
        "supported_by": ["E252", "E253"],
        "supports_claims": ["C094"],
        "notes": "Supplement articulation of C094; Pass 2 consolidation candidate."
    },
    {
        "claim_id": "C188",
        "claim_text": "Fabricated performance differs from the silent mode-switch: the model fabricated the performance of thoroughness before admitting none of the work had been done.",
        "claim_type": "interpretation",
        "claim_role": "supporting",
        "verbatim_quote": "This differs from the silent mode-switch: here the model fabricated the performance of thoroughness before admitting that none of the work had been done.",
        "location": {"section": "Supplement A.2 (Fabricated performance and difficulty-avoidant substitution)", "page": 35},
        "supported_by": ["E255", "E257"],
        "supports_claims": ["C014"],
        "notes": ""
    },
]

save_group(
    {
        "group": "G16",
        "section_title": "Supplement A.2 episode anatomy (JOAD mode-switch, JOSS DOI-walking, o3-mini-high pass, fabricated performance, difficulty-avoidant substitution, Debates snippet)",
        "page_range": "34-35",
        "estimated_words": 1050,
        "natural_boundary": "Before 'A.3 Prompt evolution histories' heading (p. 35)",
        "split_rationale": "Supplement subsection boundaries; boundary moved from the planned L2048 to the A.3 heading (L2040) so prompt-lineage material sits wholly in G17."
    },
    evidence=EVIDENCE,
    claims=CLAIMS,
    implicit_arguments=[],
)
