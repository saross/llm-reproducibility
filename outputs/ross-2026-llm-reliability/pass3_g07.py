#!/usr/bin/env python3
"""Pass 3 (explicit RDMAP) — G7: Results 4.2 Tool discovery (pp. 11-13).

Journal sampling frame, discovery method, process monitoring, the JOSS prompt
lineage (open search -> enumeration-and-extraction), and the o3-mini-high
second-model verification trial.
"""

from rdmap_lib import save_group

designs = [
    {
        "design_id": "RD025",
        "design_text": (
            "Journal sampling frame for tool discovery: five journals selected where research "
            "software is likely to be described in a software paper or mentioned in relation "
            "to a dataset or digital method — Internet Archaeology, JOSS, JOAD, JCAA, and "
            "SoftwareX."
        ),
        "design_type": "scope_definition",
        "design_status": "explicit",
        "verbatim_quote": (
            "The second stage involved building a dataset of research software by examining "
            "issues of five journals where such software is likely to be described in a "
            "software paper or mentioned in relation to a dataset or digital method: Internet "
            "Archaeology, the Journal of Open Source Software (JOSS), the Journal of Open "
            "Archaeology Data (JOAD), the Journal of Computer Applications in Archaeology "
            "(JCAA), and SoftwareX."
        ),
        "location": {"section": "Results", "subsection": "4.2 Tool discovery", "page": 11},
        "expected_information_missing": [
            "Issue/volume coverage per journal is not systematically enumerated in the main text",
        ],
    },
]

methods = [
    {
        "method_id": "M022",
        "method_text": (
            "Journal-issue examination method for tool discovery: building the research- "
            "software dataset by examining issues of the five selected journals via LLM "
            "discovery runs."
        ),
        "method_type": "data_collection",
        "method_status": "explicit",
        "verbatim_quote": (
            "The second stage involved building a dataset of research software by examining "
            "issues of five journals where such software is likely to be described in a "
            "software paper or mentioned in relation to a dataset or digital method: Internet "
            "Archaeology, the Journal of Open Source Software (JOSS), the Journal of Open "
            "Archaeology Data (JOAD), the Journal of Computer Applications in Archaeology "
            "(JCAA), and SoftwareX."
        ),
        "location": {"section": "Results", "subsection": "4.2 Tool discovery", "page": 11},
        "implements_designs": ["RD025", "RD021"],
        "expected_information_missing": [],
    },
    {
        "method_id": "M023",
        "method_text": (
            "Human process-monitoring during runs: one of two scaffolding-failure classes "
            "required human monitoring of execution (rather than prompt improvement) to catch."
        ),
        "method_type": "quality_control",
        "method_status": "explicit",
        "verbatim_quote": (
            "Two scaffolding failures account for many of the errors. One was mitigated "
            "through better prompting, the other required human process-monitoring."
        ),
        "location": {"section": "Results", "subsection": "4.2 Tool discovery", "page": 12},
        "implements_designs": ["RD016"],
        "expected_information_missing": [
            "Monitoring cadence and coverage (which runs were watched) are not documented",
        ],
    },
    {
        "method_id": "M024",
        "method_text": (
            "Second-model verification trial: a different model (o3-mini-high) tasked with "
            "verifying a Deep Research run's output, supplied with the complete results file "
            "and instructed to read each linked article."
        ),
        "method_type": "validation",
        "method_status": "explicit",
        "verbatim_quote": (
            "Suspicious that a Deep Research run might have confabulations, we tasked a "
            "different model (o3-mini-high) with verifying output. We supplied the complete "
            "results as a file and instructed the verifier to read each linked article."
        ),
        "location": {"section": "Results", "subsection": "4.2 Tool discovery", "page": 13},
        "implements_designs": ["RD016"],
        "expected_information_missing": [],
    },
]

protocols = [
    {
        "protocol_id": "P012",
        "protocol_text": (
            "Early JOSS open-search prompt (superseded): a meta-prompting-developed prompt "
            "proposing an open search ('find archaeology software') against a broad-coverage "
            "journal; the model browsed by tag, drifted out of scope, and confabulated."
        ),
        "protocol_type": "prompt_specification",
        "protocol_status": "explicit",
        "verbatim_quote": (
            "The early JOSS prompt, developed largely through meta-prompting, proposed an open "
            "search (\"find archaeology software\") against a journal with broad coverage: the "
            "model browsed by tag, drifted out of scope and, finding few genuine archaeology "
            "hits, confabulated."
        ),
        "location": {"section": "Results", "subsection": "4.2 Tool discovery", "page": 12},
        "implements_methods": ["M022"],
        "expected_information_missing": [
            "Full prompt text is not reproduced in the main body (lineage in Supplement A)",
        ],
    },
    {
        "protocol_id": "P013",
        "protocol_text": (
            "Revised JOSS enumeration-and-extraction prompt: bounded issue coverage, "
            "article-by-article extraction against the tool definition, output constrained by "
            "a fixed schema — replacing the open search and reducing confabulations from 15 "
            "to none on re-run."
        ),
        "protocol_type": "prompt_specification",
        "protocol_status": "explicit",
        "verbatim_quote": (
            "The manually written fix replaced the open search with the "
            "enumeration-and-extraction scaffolding described in Section 3.1: bounded issue "
            "coverage, article-by-article extraction against the tool definition, output "
            "constrained by a fixed schema."
        ),
        "location": {"section": "Results", "subsection": "4.2 Tool discovery", "page": 12},
        "implements_methods": ["M022", "M009"],
        "expected_information_missing": [],
    },
    {
        "protocol_id": "P014",
        "protocol_text": (
            "Process-monitoring challenge and re-run protocol: on noticing the missing harness "
            "(Deep Research) indicator, the researcher re-ran the prompt in the same context "
            "appended with a challenge ('your prior response wasn't deep research'); routine "
            "fresh-context prompting was introduced a few days after this incident."
        ),
        "protocol_type": "verification",
        "protocol_status": "explicit",
        "verbatim_quote": (
            "Only process monitoring caught it: one of us noticed the missing harness "
            "indicator and re-ran the prompt (in the same context appended with \"your prior "
            "response wasn't deep research\"; routine prompting in fresh context wasn't "
            "introduced until a few days after this incident)."
        ),
        "location": {"section": "Results", "subsection": "4.2 Tool discovery", "page": 13},
        "implements_methods": ["M023"],
        "expected_information_missing": [],
    },
]

save_group(
    {
        "group": "G7",
        "section_title": "Results 4.2 Tool discovery",
        "page_range": "11-13",
        "scan_note": (
            "Journal sampling frame (design + method), process monitoring, second-model "
            "verification trial, and the JOSS prompt lineage (superseded and revised "
            "versions). The o3-JOSS-run count-exclusion rule (Table 4 caption) noted but not "
            "extracted as a separate protocol; error-rate narratives are evidence."
        ),
    },
    research_designs=designs,
    methods=methods,
    protocols=protocols,
)
