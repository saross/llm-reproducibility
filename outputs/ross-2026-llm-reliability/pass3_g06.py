#!/usr/bin/env python3
"""Pass 3 (explicit RDMAP) — G6: Results 4 (intro/coverage) + 4.1 Literature discovery (pp. 9-11).

Results-section RDMAP: four-stage scope, authentic-use measurement stance, tool
screening, stage-1 evaluation question, and comparison/baseline methods
described in the Results narrative.
"""

from rdmap_lib import save_group

designs = [
    {
        "design_id": "RD021",
        "design_text": (
            "Four-stage bounded project scope: the 2025 work comprised a bounded, verifiable "
            "project covering literature discovery, tool discovery, tool documentation, and "
            "evidence collection."
        ),
        "design_type": "scope_definition",
        "design_status": "explicit",
        "verbatim_quote": (
            "Work in 2025 involved a bounded, verifiable project covering four stages of "
            "research: literature discovery, tool discovery, tool documentation, and evidence "
            "collection."
        ),
        "location": {"section": "Results", "page": 9},
        "expected_information_missing": [],
    },
    {
        "design_id": "RD022",
        "design_text": (
            "Authentic-use measurement stance: each tool is reported on what it showed itself "
            "able to do in authentic research, measured against its intended use (rather than "
            "on benchmark performance)."
        ),
        "design_type": "study_design",
        "design_status": "explicit",
        "verbatim_quote": (
            "We report what each tool showed itself able to do in authentic research, measured "
            "against its intended use."
        ),
        "location": {"section": "Results", "page": 9},
        "expected_information_missing": [],
    },
    {
        "design_id": "RD023",
        "design_text": (
            "Tool-screening decisions: three tools excluded from the campaign — Open Deep "
            "Research (cost at scale), Computer Use (technology demonstration status), and "
            "Operator (minimal contribution after trial)."
        ),
        "design_type": "scope_definition",
        "design_status": "explicit",
        "verbatim_quote": (
            "Three tools were screened out. Hugging Face's Open Deep Research was "
            "architecturally attractive, but at roughly $200 per run on o1-pro credits it was "
            "impractical at scale. Anthropic's Computer Use remained a technology "
            "demonstration rather than a production instrument during the testing window. "
            "OpenAI's Operator, though trialled, contributed only three discovery records "
            "(Table 4)."
        ),
        "location": {"section": "Results", "page": 9},
        "expected_information_missing": [],
    },
    {
        "design_id": "RD024",
        "design_text": (
            "Stage-1 evaluation question: can a service discover relevant literature, and can "
            "its output be ingested into a reference manager without human intervention?"
        ),
        "design_type": "research_question",
        "design_status": "explicit",
        "verbatim_quote": (
            "The first stage focused on a ubiquitous research task: can a service discover "
            "relevant literature, and can its output be ingested into a reference manager "
            "without human intervention?"
        ),
        "location": {"section": "Results", "subsection": "4.1 Literature discovery and synthesis", "page": 9},
        "expected_information_missing": [],
    },
]

methods = [
    {
        "method_id": "M018",
        "method_text": (
            "Comparative multi-service deployment: three model families exercised across the "
            "campaign (OpenAI, Anthropic, Google) plus Perplexity and Elicit for literature "
            "discovery, with per-task coverage recorded (Table 1)."
        ),
        "method_type": "data_collection",
        "method_status": "explicit",
        "verbatim_quote": (
            "Across the campaign we exercised three model families (OpenAI, Anthropic, and "
            "Google), plus Perplexity and Elicit for literature discovery (see Table 1)."
        ),
        "location": {"section": "Results", "page": 9},
        "implements_designs": ["RD015", "RD021"],
        "expected_information_missing": [
            "Run counts per service per stage are not summarised in the main text",
        ],
    },
    {
        "method_id": "M019",
        "method_text": (
            "Traditional-search baseline comparison: Web of Science and Scopus queries across "
            "the same scope, compared against the AI-assisted yield."
        ),
        "method_type": "validation",
        "method_status": "explicit",
        "verbatim_quote": (
            "A Web of Science query across the same scope produced three relevant results from "
            "the first 50 returned, but the corpus already held all three. A parallel Scopus "
            "search fared similarly, contributing only one new source."
        ),
        "location": {"section": "Results", "subsection": "4.1 Literature discovery and synthesis", "page": 10},
        "implements_designs": ["RD024"],
        "expected_information_missing": [
            "Query strings and evaluation depth beyond the first 50 results are not documented",
        ],
    },
    {
        "method_id": "M020",
        "method_text": (
            "Corpus assembly method: final literature corpus built from AI-assisted search plus "
            "manual discoveries via citation chaining or as side-effects of searching for "
            "confabulated sources."
        ),
        "method_type": "data_collection",
        "method_status": "explicit",
        "verbatim_quote": (
            "The final output was built from AI-assisted search plus manual discoveries found "
            "either by citation chaining or as a side-effect of searching for (confabulated) "
            "sources."
        ),
        "location": {"section": "Results", "subsection": "4.1 Literature discovery and synthesis", "page": 10},
        "implements_designs": ["RD024"],
        "expected_information_missing": [],
    },
    {
        "method_id": "M021",
        "method_text": (
            "Synthesis evaluation task: the same systems asked to synthesise discovered "
            "sources (rather than find them), assessed for analytical integration."
        ),
        "method_type": "data_collection",
        "method_status": "explicit",
        "verbatim_quote": (
            "When the same systems were asked not to find sources but to synthesise them, the "
            "augmentation evaporated."
        ),
        "location": {"section": "Results", "subsection": "4.1 Literature discovery and synthesis", "page": 11},
        "implements_designs": ["RD014"],
        "expected_information_missing": [
            "Synthesis task prompts and assessment criteria are not documented in the main text",
        ],
    },
]

save_group(
    {
        "group": "G6",
        "section_title": "Results 4 (intro/coverage) + 4.1 Literature discovery and synthesis",
        "page_range": "9-11",
        "scan_note": (
            "Results-opening group: four-stage scope, authentic-use stance, screening "
            "decisions, and stage-1 question extracted as designs; baseline comparison, corpus "
            "assembly, and synthesis-evaluation methods extracted. Tables 1-3 are evidence "
            "(Session B); per-service error narratives are claims/evidence, not RDMAP."
        ),
    },
    research_designs=designs,
    methods=methods,
)
