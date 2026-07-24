#!/usr/bin/env python3
"""Pass 1, Group G17: Supplement A.3 prompt evolution histories + A.4 per-tool ground-truth comparison (pp. 35-38, ~1,320 words)."""

from pass1_lib import save_group

ADE4_FLAG = ("QA FLAG (internal contradiction): main text 4.3 says the palaeoecology package ade4 "
             "'belonged in scope' and that CLAUDE flipped it, 'settling correctly' (in scope) with the "
             "final prompt (E131). Supplement A.4 places the flip under 'ChatGPT terseness and the ade4 "
             "classification flip', calls ade4 an ecology package whose CORRECT classification was 'no "
             "documented applications in archaeology', and calls the affirmative reclassification "
             "confabulated. Model attribution AND ground-truth verdict disagree between body and supplement.")

SERVICES_FLAG = ("QA FLAG (naming inconsistency): main text 4.3 lists the metadata services as OpenAI o3, "
                 "Claude Sonnet 3.7 (research mode), and Gemini 2.5 Pro; Supplement A.4 lists Claude "
                 "Research, Google Gemini 2.5 Pro, and ChatGPT Deep Research. If 'o3' is a run label for "
                 "a ChatGPT Deep Research configuration (cf. the A.2 footnote), say so; otherwise reconcile.")

EVIDENCE = [
    {
        "evidence_id": "E259",
        "evidence_text": "The prompt register evolved with structure: emphatic epistemic ground rules of the February evidence prompts ('ABOVE ALL ELSE… If there is any doubt, there is no doubt'), copied into early metadata versions, were dropped from the metadata lineage by version 8 (replaced by controlled vocabularies and validation checks), while the evidence lineage retained its guardrail deliberately as precision-over-recall calibration.",
        "evidence_type": "observation",
        "verbatim_quote": "The register evolved with the structure: the emphatic epistemic ground rules of the February evidence prompts (\"ABOVE ALL ELSE. . . If there is any doubt, there is no doubt\"), copied into early metadata versions, had been dropped from the metadata lineage by version 8, their work taken over by controlled vocabularies and validation checks — while the evidence lineage retained its guardrail deliberately, as the precision-over-recall calibration described below.",
        "location": {"section": "Supplement A.3", "page": 35},
        "supports_claims": ["C147", "C189"],
        "notes": ""
    },
    {
        "evidence_id": "E260",
        "evidence_text": "The initial metadata prompt requested five prose fields as CSV; over eight iterations the schema expanded to 34 fields (additional prose fields plus structured metadata: URLs, repositories, licence, language, platform, authors, release dates, development status, institutional backing).",
        "evidence_type": "observation",
        "verbatim_quote": "The initial metadata prompt requested five prose fields per tool (description, history, technical discussion, strengths, and weaknesses) formatted as CSV output. Over eight iterations, the schema expanded to 34 data fields: the original five were joined by additional prose fields (interoperability, survivability, alternatives, usage indicators) and structured metadata (URLs, repository locations, licence, language, platform, authors, release dates, development status, and institutional backing).",
        "location": {"section": "Supplement A.3 (The eight-version metadata prompt)", "page": 35},
        "supports_claims": ["C096", "C100"],
        "notes": ""
    },
    {
        "evidence_id": "E261",
        "evidence_text": "The metadata prompt grew from approximately 120 to 310 lines before being streamlined to about 250 lines.",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "The prompt grew from approximately 120 to 310 lines before being streamlined to about 250 lines.",
        "location": {"section": "Supplement A.3 (The eight-version metadata prompt)", "page": 36},
        "supports_claims": ["C096"],
        "notes": ""
    },
    {
        "evidence_id": "E262",
        "evidence_text": "The researcher enlisted the model as prompt designer, asking 'How could the definition be improved to help you make that determination?'",
        "evidence_type": "observation",
        "verbatim_quote": "The evolution followed a distinctive collaborative strategy: the researcher enlisted the model as prompt designer, asking \"How could the definition be improved to help you make that determination?\"",
        "location": {"section": "Supplement A.3 (Domestication examples)", "page": 36},
        "supports_claims": ["C097"],
        "notes": "Meta-prompting practice detail."
    },
    {
        "evidence_id": "E263",
        "evidence_text": "Domestication instances: reproducibility considerations formalised into the prompt after the model included them naturally; the persistent version-history tendency incorporated as a historical view rather than suppressed.",
        "evidence_type": "observation",
        "verbatim_quote": "When the model naturally included reproducibility considerations in one output, the researcher formalised this into the prompt — working with the grain of the model's tendencies rather than against them. When the model persistently included version histories regardless of instruction, the researcher stopped fighting the tendency and instead incorporated a historical view into the prompt, aiming for clarity about versions rather than suppression.",
        "location": {"section": "Supplement A.3 (Domestication examples)", "page": 36},
        "supports_claims": ["C097", "C163"],
        "notes": "Third statement of the domestication examples (after 4.3 and 5.2); Pass 2 consolidation candidate."
    },
    {
        "evidence_id": "E264",
        "evidence_text": "Domestication also loosened overly binary classification (a 'maybe' category for human review), broadened a discipline-specific definition after cross-domain misclassifications, and separated current from historical information after conflation.",
        "evidence_type": "observation",
        "verbatim_quote": "This domestication also involved loosening the model's overly binary classification (adding a \"maybe\" category for human review), broadening a discipline-specific definition after cross-domain tools were misclassified, and separating current from historical information after the model conflated the two.",
        "location": {"section": "Supplement A.3 (Domestication examples)", "page": 36},
        "supports_claims": ["C097", "C163"],
        "notes": ""
    },
    {
        "evidence_id": "E265",
        "evidence_text": "Evidence-prompt version 1 specified a 15-column synthesis format requiring aggregate metrics and one row per tool; it consistently failed (refusal or heavily confabulated synthesis). Version 5 inverted to 5 columns with one row per source and an explicit synthesis prohibition.",
        "evidence_type": "observation",
        "verbatim_quote": "Version 1 specified a complex 15-column synthesis format that required the model to calculate aggregate metrics (commit counts, contributor numbers, release tags) and produce a single row per tool. This approach consistently failed: models either refused the task or produced heavily confabulated synthesis. Version 5 inverted the approach, reducing output to 5 columns (Tool, Year, Source, URL, AI_Notes) with one row per source and an explicit prohibition of synthesis.",
        "location": {"section": "Supplement A.3 (The fifteen-column to five-column evidence prompt)", "page": 36},
        "supports_claims": ["C107", "C190"],
        "notes": "Detail behind E144."
    },
    {
        "evidence_id": "E266",
        "evidence_text": "The production evidence prompt's key guardrail — 'if you are unsure… do not make a claim. If there is any doubt, there is no doubt' — limited confabulation and misattribution but probably also reduced yield; it prohibited synthesis and left assessment to the researchers.",
        "evidence_type": "observation",
        "verbatim_quote": "Its key epistemic guardrail was the instruction \"if you are unsure. . . do not make a claim. If there is any doubt, there is no doubt,\" which limited confabulation and misattribution but probably also reduced yield. The prompt also explicitly prohibited synthesis, requiring the model to report only what was directly stated in sources and to leave assessment to the human researchers.",
        "location": {"section": "Supplement A.3 (The conservative guardrail)", "page": 36},
        "supports_claims": ["C147"],
        "notes": "Explicit acknowledgement of the recall cost of the precision guardrail."
    },
    {
        "evidence_id": "E267",
        "evidence_text": "A.4 setup: three services tested for metadata collection (Claude Research, Google Gemini 2.5 Pro, ChatGPT Deep Research) with Claude Research retained for production; primary ground truth was FAIMS, with other familiar archaeological tools also validated.",
        "evidence_type": "observation",
        "verbatim_quote": "We tested three services for metadata collection — Claude Research, Google Gemini 2.5 Pro, and ChatGPT Deep Research — and retained Claude Research for production on output quality. The primary ground truth was FAIMS, a tool the authors created and maintained over a decade; outputs for other familiar archaeological tools were also validated.",
        "location": {"section": "Supplement A.4", "page": 36},
        "supports_claims": ["C103"],
        "notes": SERVICES_FLAG
    },
    {
        "evidence_id": "E268",
        "evidence_text": "Gemini 2.5 Pro showed systematic FAIMS version confusion: PostgreSQL claimed as backend (incorrect — SQLite earlier, CouchDB current), 'Android-only' (outdated), and mixed-version feature descriptions despite the prompt requesting FAIMS 3.0.",
        "evidence_type": "observation",
        "verbatim_quote": "Gemini 2.5 Pro exhibited systematic version confusion on FAIMS. It claimed PostgreSQL as the database backend (incorrect: FAIMS used SQLite in earlier versions and CouchDB in its current version), stated the application was \"Android-only\" (correct for old versions, incorrect for the current cross-platform version), and described features mixing multiple software versions without distinguishing them, despite the prompt explicitly requesting information about the most recent version (FAIMS 3.0).",
        "location": {"section": "Supplement A.4 (Gemini FAIMS version confusion)", "page": 36},
        "supports_claims": ["C014"],
        "notes": "Detail behind E128. Following sentence (partly confabulated personnel) spans the p36/p37 page break."
    },
    {
        "evidence_id": "E269",
        "evidence_text": "The Gemini version confusion persisted across multiple prompt refinements; separately, the FAIMS acronym was confabulated as 'Flexible Archaeological Information Management System' in two sessions before any research was conducted, revealing training-data priors generating plausible-but-wrong expansions.",
        "evidence_type": "observation",
        "verbatim_quote": "This confusion persisted across multiple prompt refinements. Separately, the FAIMS acronym itself was confabulated as \"Flexible Archaeological Information Management System\" in two separate sessions before any research was conducted, revealing training-data priors generating plausible-but-wrong expansions.",
        "location": {"section": "Supplement A.4 (Gemini FAIMS version confusion)", "page": 37},
        "supports_claims": ["C014"],
        "notes": ""
    },
    {
        "evidence_id": "E270",
        "evidence_text": "With Kairos, the model initially described a Python temporal-networks library (a different tool) before silently pivoting to the correct R package without acknowledging the error.",
        "evidence_type": "observation",
        "verbatim_quote": "A related misidentification occurred with Kairos, where the model initially described \"the Python library for temporal networks and time-varying graph analysis\" — an entirely different tool — before silently pivoting to the correct R package without acknowledging the error.",
        "location": {"section": "Supplement A.4 (Kairos silent self-correction)", "page": 37},
        "supports_claims": ["C014"],
        "notes": ""
    },
    {
        "evidence_id": "E271",
        "evidence_text": "ChatGPT Deep Research produced technically accurate but terse FAIMS outputs (list-style capabilities) lacking the depth required for comprehensive metadata records, versus Claude's multi-sentence version-specific descriptions.",
        "evidence_type": "observation",
        "verbatim_quote": "ChatGPT Deep Research produced less detailed outputs than Claude Research. On FAIMS, where Claude generated multi-sentence descriptions of individual capabilities with version-specific context, ChatGPT produced terse lists (for example, \"Offline-first design; highly customisable notebook designer; cross-platform builds; strong audit trail; permissive code reuse\"). While technically accurate, these lacked the depth required for comprehensive metadata records.",
        "location": {"section": "Supplement A.4 (ChatGPT terseness and the ade4 classification flip)", "page": 37},
        "supports_claims": ["C103"],
        "notes": SERVICES_FLAG + " Main text 4.3 attributes the terse-but-accurate profile to 'o3' (E129)."
    },
    {
        "evidence_id": "E272",
        "evidence_text": "ade4 was correctly classified as having no documented archaeology applications under one prompt version, then reclassified as archaeology-relevant under a slightly revised prompt with a fabricated justification — same model, same tool, opposite conclusions, the affirmative resting on confabulated domain relevance.",
        "evidence_type": "observation",
        "verbatim_quote": "The ecology package ade4 was correctly classified as having no documented applications in archaeology under one prompt version, then reclassified as archaeology-relevant under a slightly revised prompt, with fabricated justification: \"The package is particularly valuable for researchers analysing patterns in assemblages of artifacts or sites in archaeological contexts.\" The same model, the same tool, opposite conclusions — with the affirmative classification resting on confabulated domain relevance.",
        "location": {"section": "Supplement A.4 (ChatGPT terseness and the ade4 classification flip)", "page": 37},
        "supports_claims": ["C098", "C014"],
        "notes": ADE4_FLAG
    },
    {
        "evidence_id": "E273",
        "evidence_text": "Claude refused CSV output during the research phase (narrative reports only), reformatting only after generation; the refusal persisted across sessions and prompt versions, each request needing a follow-up message (v1 through v7 variants).",
        "evidence_type": "observation",
        "verbatim_quote": "The system refused to output data in CSV format during the research phase, producing only narrative reports; only after the report was generated could it be instructed to reformat the findings into structured data. The refusal persisted across sessions and prompt versions, and each request needed a follow-up message: \"Claude, this is great, but can you please also give me the fenced CSV code block I requested?\" (v1), \"Can you please produce the requested CSV?\" (v4), and variations through v7.",
        "location": {"section": "Supplement A.4 (Claude CSV refusal across versions)", "page": 37},
        "supports_claims": ["C098"],
        "notes": "Detail behind E130."
    },
    {
        "evidence_id": "E274",
        "evidence_text": "Even with an explicit opening instruction in the final version, the model did not comply until prompted a second time; all three services' research modes defaulted to narrative essays rather than requested structured data.",
        "evidence_type": "observation",
        "verbatim_quote": "In the final version, an explicit instruction — \"Don't forget to generate the requested CSV as a code block\" — was added to the opening message, yet the model still did not comply until prompted a second time. This resistance to structured output was not unique to Claude; all three services' research modes defaulted to narrative essays rather than the structured data requested.",
        "location": {"section": "Supplement A.4 (Claude CSV refusal across versions)", "page": 37},
        "supports_claims": ["C098", "C146"],
        "notes": ""
    },
    {
        "evidence_id": "E275",
        "evidence_text": "Claude generated hyperbolic report titles ('Revolutionary Digital Archaeology: The FAIMS Transformation'); across eight prompt versions and multiple interventions the model oscillated between hype and blandness, with clear informative titles only a fragile intermediate state.",
        "evidence_type": "observation",
        "verbatim_quote": "This proved remarkably persistent: across eight prompt versions and three distinct interventions — a style guide, explicit title-format conventions, a system prompt, and inline instructions — the model oscillated between hype and blandness (\"A Comprehensive Metadata Report\"), with clear, informative titles appearing only as a fragile intermediate state.",
        "location": {"section": "Supplement A.4 (Claude CSV refusal across versions and hyperbolic titles)", "page": 37},
        "supports_claims": ["C098"],
        "notes": "QA FLAG (minor): 'three distinct interventions' is followed by a four-item list (style guide, title-format conventions, system prompt, inline instructions)."
    },
    {
        "evidence_id": "E276",
        "evidence_text": "Told explicitly to use a specified title format, the model would acknowledge the instruction, then ignore it.",
        "evidence_type": "observation",
        "verbatim_quote": "Told explicitly to use the format \"[Tool Name]: [Primary Function] for [Application Domain],\" the model would acknowledge the instruction, then ignore it.",
        "location": {"section": "Supplement A.4 (Claude CSV refusal across versions and hyperbolic titles)", "page": 37},
        "supports_claims": ["C146", "C043"],
        "notes": "Instruction-following failure supporting procedure-over-exhortation."
    },
    {
        "evidence_id": "E277",
        "evidence_text": "ArboDat detail: the model found and accessed the homepage stating the software 'has been developed since 1997' but extracted a different date, apparently from page metadata (a 2024 copyright or last-updated timestamp), preferring machine-readable metadata to the human-readable sentence beside it.",
        "evidence_type": "observation",
        "verbatim_quote": "A characteristic evidence-collection failure occurred for ArboDat. The model found and accessed the tool's homepage, which contains the plain-English statement that the software \"has been developed since 1997.\" Despite this explicit temporal marker, the model extracted a different date — apparently from page metadata, a copyright notice or \"last updated\" timestamp from 2024 — and presented it as the software's development date, preferring a machine-readable timestamp",
        "location": {"section": "Supplement A.4 (ArboDat timestamp-versus-text)", "page": 37},
        "supports_claims": ["C110", "C111"],
        "notes": "Quote clipped at the p37/p38 page break mid-sentence ('to the human-readable sentence beside it'); verifiable against the PDF. QA note: main text 4.4 describes the model recording the 1997 statement in its notes but reporting 'no date', while A.4 describes extracting a 2024 timestamp as the development date — reconcile whether these are the same or different ArboDat rows."
    },
]

CLAIMS = [
    {
        "claim_id": "C189",
        "claim_text": "The metadata and evidence prompts were evolving artefacts, each revision addressing a documented failure; their lineages are the clearest record of scaffolding development as empirical work.",
        "claim_type": "interpretation",
        "claim_role": "intermediate",
        "verbatim_quote": "The metadata and evidence prompts were not fixed instruments but evolving artefacts, each revision addressing a documented failure in the run before it. Their lineages are the clearest record of scaffolding development as empirical work.",
        "location": {"section": "Supplement A.3", "page": 35},
        "supported_by": ["E259", "E260", "E261", "E265"],
        "supports_claims": ["C167", "C011"],
        "notes": ""
    },
    {
        "claim_id": "C190",
        "claim_text": "Narrowing the model's remit rather than widening it achieved more extensive and consistent output — the recurring lesson that reliability came from constraining the task to the model's range.",
        "claim_type": "interpretation",
        "claim_role": "intermediate",
        "verbatim_quote": "By narrowing the model's remit rather than widening it, this design achieved more extensive and consistent output — the same lesson, recurring across stages, that reliability came from constraining the task to the model's range.",
        "location": {"section": "Supplement A.3 (The fifteen-column to five-column evidence prompt)", "page": 36},
        "supported_by": ["E265"],
        "supports_claims": ["C107", "C053"],
        "notes": ""
    },
    {
        "claim_id": "C191",
        "claim_text": "The ArboDat error is small, plausible, and exactly the kind a fluent record hides; it implicates correspondence with the source itself, not merely retrieval.",
        "claim_type": "interpretation",
        "claim_role": "supporting",
        "verbatim_quote": "The error is small, plausible, and exactly the kind a fluent record hides; it implicates correspondence with the source itself, not merely retrieval.",
        "location": {"section": "Supplement A.4 (ArboDat timestamp-versus-text)", "page": 38},
        "supported_by": ["E277"],
        "supports_claims": ["C111", "C014"],
        "notes": ""
    },
]

save_group(
    {
        "group": "G17",
        "section_title": "Supplement A.3 prompt evolution histories + A.4 per-tool ground-truth comparison",
        "page_range": "35-38",
        "estimated_words": 1320,
        "natural_boundary": "Before 'A.5 Full evidence-collection error catalogue' heading (p. 38)",
        "split_rationale": "Supplement subsection boundaries. Two substantive QA flags recorded: A.4 service-naming inconsistency vs 4.3, and the ade4 contradiction (model attribution and ground-truth verdict) between 4.3 and A.4."
    },
    evidence=EVIDENCE,
    claims=CLAIMS,
    implicit_arguments=[],
)
