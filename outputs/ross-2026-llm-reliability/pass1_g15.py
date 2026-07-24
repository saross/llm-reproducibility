#!/usr/bin/env python3
"""Pass 1, Group G15: Supplement A.1 source synthesis per-model detail + other tools screened + A.2 per-journal detail (pp. 32-34, ~1,170 words)."""

from pass1_lib import save_group

DISCREPANCY = ("NOTE FOR PRE-SUBMISSION QA: supplement aggregate figures (243 unique tools; 155/63.8% "
               "verified; 137 of 144 unique-verified; JOSS 22%, JOAD 82% confabulation) differ from "
               "main-text Tables 4-5 (242 unique; 154 verified; 136 of 143 unique-verified/95.1%; "
               "JOSS first-run 44%, JOAD sole-run 93%). Some differences reflect different denominators "
               "(overall vs per-run rates), but the 243-vs-242 / 155-vs-154 / 137-vs-136 unit offsets "
               "look like an internal inconsistency to reconcile before submission.")

EVIDENCE = [
    {
        "evidence_id": "E224",
        "evidence_text": "All tested models exhibited significant synthesis limitations; differences between OpenAI's models were marginal despite marketing claims of progressive sophistication.",
        "evidence_type": "observation",
        "verbatim_quote": "When tasked with synthesising discovered literature into coherent analysis, all tested models exhibited significant limitations, and the differences between OpenAI's models were marginal despite marketing claims of progressive sophistication.",
        "location": {"section": "Supplement A.1 (Source synthesis: per-model detail)", "page": 32},
        "supports_claims": ["C085"],
        "notes": ""
    },
    {
        "evidence_id": "E225",
        "evidence_text": "GPT-4.5 performed adequately at structured outputs but defaulted to sequential summarisation (Source A then Source B) without identifying tensions, contradictions, or synthetic insights.",
        "evidence_type": "observation",
        "verbatim_quote": "GPT-4.5 performed adequately at generating structured outputs such as section headings or reformatting existing content, but when asked to synthesise multiple sources into coherent arguments it defaulted to sequential summarisation rather than analytical integration: it would present Source A's claims, then Source B's claims, without identifying the tensions, contradictions, or synthetic insights that emerge from their juxtaposition.",
        "location": {"section": "Supplement A.1 (Source synthesis: per-model detail)", "page": 32},
        "supports_claims": ["C085"],
        "notes": ""
    },
    {
        "evidence_id": "E226",
        "evidence_text": "o1 Pro showed incremental gains in instruction adherence and focus, but these remained within textual manipulation rather than genuine analytical capability.",
        "evidence_type": "observation",
        "verbatim_quote": "o1 Pro demonstrated incremental improvements in instruction adherence and a reduced tendency toward tangential elaboration — it more reliably maintained focus on the specified research questions and was marginally better at distinguishing primary claims from supporting evidence — but these gains remained within textual manipulation rather than genuine analytical capability.",
        "location": {"section": "Supplement A.1 (Source synthesis: per-model detail)", "page": 32},
        "supports_claims": ["C085"],
        "notes": ""
    },
    {
        "evidence_id": "E227",
        "evidence_text": "Neither OpenAI model could identify contradictory claims about the same phenomenon, assess relative credibility of competing authorities, or recognise when accumulating evidence pointed away from sources' stated conclusions.",
        "evidence_type": "observation",
        "verbatim_quote": "Neither model could identify when sources made contradictory claims about the same phenomenon, assess the relative credibility of competing authorities, or recognise when accumulating evidence pointed toward conclusions different from those the sources explicitly stated.",
        "location": {"section": "Supplement A.1 (Source synthesis: per-model detail)", "page": 32},
        "supports_claims": ["C085"],
        "notes": ""
    },
    {
        "evidence_id": "E228",
        "evidence_text": "Both OpenAI models exhibited 'confidence collapse' at synthesis boundaries: retreating to meta-commentary or manufacturing false consensus when confronted with conflicting evidence.",
        "evidence_type": "observation",
        "verbatim_quote": "Both exhibited what we termed 'confidence collapse' at synthesis boundaries: retreating to meta-commentary (\"scholars debate this point\") or manufacturing false consensus when confronted with conflicting evidence.",
        "location": {"section": "Supplement A.1 (Source synthesis: per-model detail)", "page": 32},
        "supports_claims": ["C085", "C014"],
        "notes": "Named phenomenon at the synthesis boundary."
    },
    {
        "evidence_id": "E229",
        "evidence_text": "Claude Sonnet 3.7 showed superior linguistic sophistication undermined by identical evaluation limitations.",
        "evidence_type": "observation",
        "verbatim_quote": "Claude Sonnet 3.7 exhibited a characteristic pattern: superior linguistic sophistication undermined by identical limitations of evaluation.",
        "location": {"section": "Supplement A.1 (Source synthesis: per-model detail)", "page": 32},
        "supports_claims": ["C085"],
        "notes": ""
    },
    {
        "evidence_id": "E230",
        "evidence_text": "Claude wove together sources from different decades without acknowledging temporal context (a 2010 prediction beside 2024 assessments without recognising one could evaluate the other), extending to citation practice mixing historical and contemporary references.",
        "evidence_type": "observation",
        "verbatim_quote": "Synthesising literature on software sustainability, Claude would weave together sources from different decades without acknowledging temporal context — a 2010 prediction about future technological needs presented alongside 2024 assessments without recognition that one could evaluate the other.",
        "location": {"section": "Supplement A.1 (Source synthesis: per-model detail)", "page": 32},
        "supports_claims": ["C085"],
        "notes": ""
    },
    {
        "evidence_id": "E231",
        "evidence_text": "When synthesis exceeded Claude's operational scope its confabulation rate rose sharply: unlike Deep Research (whose output became less coherent), Claude maintained fluency while fabricating citations and non-existent studies, repeatedly citing specific page numbers from fictional journal articles in perfect academic format.",
        "evidence_type": "observation",
        "verbatim_quote": "The confabulation rate rose sharply when synthesis tasks exceeded Claude's operational scope: unlike Deep Research, whose output simply became less coherent, Claude maintained linguistic fluency while introducing fabricated citations and non-existent studies, repeatedly citing specific page numbers from completely fictional journal articles with perfect academic formatting.",
        "location": {"section": "Supplement A.1 (Source synthesis: per-model detail)", "page": 32},
        "supports_claims": ["C085", "C014", "C006"],
        "notes": ""
    },
    {
        "evidence_id": "E232",
        "evidence_text": "Only about 60% of Claude Research's citations corresponded to real publications, but fabricated references often contained accurate author names or plausible titles that led to relevant literature when searched independently.",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "Despite these confabulations, Claude Research proved unexpectedly useful as a serendipitous discovery mechanism: while only about 60% of its citations corresponded to real publications, the fabricated references often contained accurate author names or plausible titles that, when searched independently, led to relevant literature.",
        "location": {"section": "Supplement A.1 (Source synthesis: per-model detail)", "page": 32},
        "supports_claims": ["C083", "C085"],
        "notes": ""
    },
    {
        "evidence_id": "E233",
        "evidence_text": "The gains remained within 'mundane utility': the tools excel as sophisticated search-and-format assistants, and Anthropic's marketing description ('operates agentically', 'easy-to-check citations') sat awkwardly against practice in which citations had to be checked.",
        "evidence_type": "observation",
        "verbatim_quote": "These gains, however, remained firmly within Mowshowitz's \"mundane utility\" (Mowshowitz, 2023): the tools excel when treated as sophisticated searchand-format assistants rather than autonomous researchers, and Anthropic's own description of Research as a system that \"operates agentically\" and returns \"thorough answers, complete with easy-to-check citations\" (Anthropic, 2025) sat awkwardly against a practice in which the prose often obscured factual claims and the \"easy-to-check\" citations had to be checked.",
        "location": {"section": "Supplement A.1 (Source synthesis: per-model detail)", "page": 32},
        "supports_claims": ["C008", "C085"],
        "notes": "'searchand-format' preserves a line-break artefact of the processed md."
    },
    {
        "evidence_id": "E234",
        "evidence_text": "Gemini Deep Research combined vast search access with near-complete absence of critical evaluation; its single-threaded architecture, compulsive report generation, and self-deceptive progress claims created an illusion of comprehensive investigation.",
        "evidence_type": "observation",
        "verbatim_quote": "Gemini Deep Research was the clearest case among tested systems of the form of scholarship without its substance: vast search access combined with near-complete absence of critical evaluation, producing outputs that superficially resembled research while lacking essential scholarly judgement. Its single-threaded architecture, compulsive report generation, and self-deceptive progress claims created an illusion of comprehensive investigation that dissolved upon examination.",
        "location": {"section": "Supplement A.1 (Source synthesis: per-model detail)", "page": 32},
        "supports_claims": ["C085"],
        "notes": "Following sentence (underperformance despite Google's search advantages) spans the p32/p33 page break."
    },
    {
        "evidence_id": "E235",
        "evidence_text": "Ultimately the models were used to discover sources but did not contribute significantly to the analytical synthesis in the literature review.",
        "evidence_type": "observation",
        "verbatim_quote": "Ultimately, the models were used to discover sources but did not contribute significantly to the analytical synthesis of those sources in our literature review.",
        "location": {"section": "Supplement A.1 (Source synthesis: per-model detail)", "page": 33},
        "supports_claims": ["C085", "C086"],
        "notes": ""
    },
    {
        "evidence_id": "E236",
        "evidence_text": "OpenAI's Operator could not decompose tasks, maintain notes, or work to a plan, and lost track of its objective on simple data-collection sequences.",
        "evidence_type": "observation",
        "verbatim_quote": "OpenAI's Operator functioned as a technology demonstration: it could not decompose tasks, maintain notes, or work to a plan, and lost track of its objective on even simple datacollection sequences, becoming distracted by tangentially related content.",
        "location": {"section": "Supplement A.1 (Other tools screened out)", "page": 33},
        "supports_claims": ["C080"],
        "notes": "'datacollection' preserves a line-break artefact of the processed md."
    },
    {
        "evidence_id": "E237",
        "evidence_text": "Anthropic's Computer Use (local Docker container) showed costs exceeding Open Deep Research, rapid API-credit consumption for minimal progress, and failed basic tasks like locating and loading academic papers.",
        "evidence_type": "observation",
        "verbatim_quote": "Anthropic's Computer Use ran in a local Docker container, in principle reaching desktop applications, but practical testing revealed costs exceeding even Open Deep Research, with API credits consumed rapidly for minimal progress, and it failed basic tasks such as locating and loading academic papers.",
        "location": {"section": "Supplement A.1 (Other tools screened out)", "page": 33},
        "supports_claims": ["C080"],
        "notes": ""
    },
    {
        "evidence_id": "E238",
        "evidence_text": "Claude Code showed more promise for qualitative research via local filesystem access, iterating over files with Markdown to-do lists for state management, though its confabulation rate required line-by-line verification of all quoted material.",
        "evidence_type": "observation",
        "verbatim_quote": "By contrast, Anthropic's Claude Code showed more promise for qualitative research through its local filesystem access: using a systematised prompting approach, it iterated over files while maintaining Markdown to-do lists for state management across larger tasks, though its confabulation rate remained high enough to require line-by-line verification of all quoted material. Its ability to write state files to disk offers a practical model for tools seeking genuinely systematic research workflows.",
        "location": {"section": "Supplement A.1 (Other tools screened out)", "page": 33},
        "supports_claims": ["C148"],
        "notes": "Prefigures the persistent-external-state principle."
    },
    {
        "evidence_id": "E239",
        "evidence_text": "A.2 aggregate: 243 unique tools identified, 155 (63.8%) verified as legitimate research software, 53 (21.8%) misattributions, 33 (13.6%) confabulations, 2 (0.8%) granularity errors.",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "Across multiple discovery runs against the target journals, the systems identified 243 unique tools, of which 155 (63.8%) verified as legitimate research software; 53 (21.8%) were misattributions (real software that did not meet the definition of 'tool' provided to the model), 33 (13.6%) were confabulations (fabricated tools with no real-world counterpart), and 2 (0.8%) were granularity errors (a non-tool entity, such as a project or consortium, reported as a specific tool).",
        "location": {"section": "Supplement A.2", "page": 33},
        "supports_claims": ["C087"],
        "notes": DISCREPANCY
    },
    {
        "evidence_id": "E240",
        "evidence_text": "Per-model: ChatGPT DR contributed 137 of 144 single-model unique verified tools (95.1%); o3 5 (3.5%, all one JCAA run); Operator 2 (1.4%); Perplexity DR none unique; twelve tools found by more than one model.",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "ChatGPT Deep Research was the primary discovery engine, contributing 137 of the 144 verified tools unique to a single model (95.1%); OpenAI o3 contributed 5 (3.5%), all from a single run against JCAA; OpenAI Operator contributed 2 (1.4%); Perplexity Deep Research confirmed existing discoveries but contributed none unique. Twelve tools were discovered by more than one model.",
        "location": {"section": "Supplement A.2", "page": 33},
        "supports_claims": ["C087"],
        "notes": DISCREPANCY
    },
    {
        "evidence_id": "E241",
        "evidence_text": "Per-journal: Internet Archaeology 77 unique verified, confabulation <1%; JOSS 49 unique verified at 22% confabulation; JOAD 3 unique verified at 82% confabulation; JCAA 5 unique verified, zero confabulations; SoftwareX 9 verified, 3 confabulations (25%).",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "Internet Archaeology, with its 30-year open-access publication history, yielded the most verified tools (77 unique) with a confabulation rate below 1%. JOSS contributed the second-largest yield (49 unique verified tools) but at a 22% confabulation rate. JOAD yielded only 3 unique verified tools against an 82% confabulation rate. JCAA contributed 5 unique verified tools with no confabulations; SoftwareX yielded 9 verified tools but 3 confabulations (a 25% rate).",
        "location": {"section": "Supplement A.2", "page": 33},
        "supports_claims": ["C087", "C088"],
        "notes": "Overall per-journal rates; main text quotes per-run rates (JOSS first run 44%, JOAD sole DR run 93%) — denominators differ, worth clarifying in the text."
    },
    {
        "evidence_id": "E242",
        "evidence_text": "General software journals (JOSS ~2,700 and SoftwareX ~1,950 publications, all domains) forced needle-in-haystack search, producing DOI sequence walking; archaeology-specific journals constrained the search space — JCAA, the smallest corpus (~100 articles, 9 volumes since 2018), produced zero confabulations.",
        "evidence_type": "observation",
        "verbatim_quote": "The general software journals (JOSS and SoftwareX, with approximately 2,700 and 1,950 total publications respectively, spanning all domains) required the models to locate archaeologyrelevant papers among thousands of unrelated entries, producing the 'DOI sequence walking' pattern described below. The archaeology-specific journals (Internet Archaeology, JCAA, JOAD) constrained the search space to relevant content — and JCAA, despite being the smallest corpus (approximately 100 articles across 9 volumes since 2018), produced zero confabulations.",
        "location": {"section": "Supplement A.2", "page": 33},
        "supports_claims": ["C088"],
        "notes": "'archaeologyrelevant' preserves a line-break artefact of the processed md."
    },
    {
        "evidence_id": "E243",
        "evidence_text": "JOAD's 82% rate resulted not from corpus characteristics but from a documented scaffolding failure: JOAD shares publisher (Ubiquity Press) and metadata infrastructure with JCAA, which produced no confabulations.",
        "evidence_type": "observation",
        "verbatim_quote": "Critically, JOAD's 82% rate resulted not from corpus characteristics but from a documented scaffolding failure (detailed below): JOAD shares both its publisher (Ubiquity Press) and its metadata infrastructure with JCAA, which produced no confabulations at all.",
        "location": {"section": "Supplement A.2", "page": 33},
        "supports_claims": ["C088", "C089"],
        "notes": "Closing sentence ('Corpus size and metadata quality alone do not predict confabulation risk; the interaction ... does.') spans the p33/p34 page break and is not separately extracted; verifiable against the PDF."
    },
]

save_group(
    {
        "group": "G15",
        "section_title": "Supplement A.1 source synthesis per-model detail + other tools screened out + A.2 per-journal confabulation detail",
        "page_range": "32-34",
        "estimated_words": 1170,
        "natural_boundary": "Before 'The JOAD silent mode-switch' heading (p. 34)",
        "split_rationale": "Supplement subsection boundaries; flags supplement-vs-main-text numeric discrepancies for pre-submission QA (see E239/E240 notes)."
    },
    evidence=EVIDENCE,
    claims=[],
    implicit_arguments=[],
)
