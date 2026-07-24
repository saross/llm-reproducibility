#!/usr/bin/env python3
"""Pass 1, Group G18: Supplement A.5 full evidence-collection error catalogue + per-model selection (pp. 38-39, ~640 words)."""

from pass1_lib import save_group

EVIDENCE = [
    {
        "evidence_id": "E278",
        "evidence_text": "All 1,040 evidence events were reviewed by hand and with LLM assistance (source exists; mentions the correct tool; stated year matches publication date), reconciling with discovery and metadata outcomes; 945 (90.9%) verified.",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "All 1,040 evidence events were reviewed, by hand and with LLM assistance. For each event we checked whether the cited source existed, whether it mentioned the correct tool, and whether the stated year matched the source's publication date, reconciling results with the discovery and metadata outcomes. Of the 1,040 events, 945 (90.9%) were verified.",
        "location": {"section": "Supplement A.5", "page": 38},
        "supports_claims": ["C112"],
        "notes": ""
    },
    {
        "evidence_id": "E279",
        "evidence_text": "Unlike metadata collection (whole-search failures for invalid tools), evidence-collection errors were event-level: real sources not mentioning the claimed tool, same-named tool from another field, or unverifiable URLs.",
        "evidence_type": "observation",
        "verbatim_quote": "Unlike metadata collection, where entire searches failed for invalid tools, evidence-collection errors were event-level: the model cited real sources that did not mention the claimed tool, attributed evidence to a same-named tool from another field, or could not be verified because the URL was inaccessible.",
        "location": {"section": "Supplement A.5", "page": 38},
        "supports_claims": ["C108", "C099"],
        "notes": "Contrast between the binary metadata failure mode and the fractal evidence failure mode."
    },
    {
        "evidence_id": "E280",
        "evidence_text": "The 52 confabulated events (5.0%) were dispersed across 26 tools; dplR (dendrochronology R package, most-documented tool) accounted for 12 of its 53 total events, while also yielding the most confirmed evidence (41 events over three decades).",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "The 52 confabulated evidence events (5.0%) were dispersed across 26 tools rather than localised to a few, with dplR — a dendrochronology R package, and the most-documented tool in the dataset — accounting for the largest share: 12 confabulated events out of 53 total for that tool. dplR also yielded the most confirmed evidence of any tool (41 confirmed events spanning three decades).",
        "location": {"section": "Supplement A.5 (The 52 confabulated events across 26 tools)", "page": 38},
        "supports_claims": ["C109", "C192"],
        "notes": "Detail behind E156."
    },
    {
        "evidence_id": "E281",
        "evidence_text": "All four collisions involved Tabula: a PDF-extraction tool sharing its name with Frerebeau's tabula R package for archaeological data analysis — real sources mentioning a different Tabula.",
        "evidence_type": "observation",
        "verbatim_quote": "All four collisions involved Tabula: a PDF-extraction tool sharing its name with the tabula R package by Frerebeau for archaeological data analysis. In each case the cited source was real and mentioned a tool called Tabula, but a different one from the package the event purported to evidence.",
        "location": {"section": "Supplement A.5 (The four collisions)", "page": 38},
        "supports_claims": ["C112"],
        "notes": ""
    },
    {
        "evidence_id": "E282",
        "evidence_text": "Twenty-two events (2.1%) could not be checked (paywalled, broken, or blocked URLs); they are recorded as a distinct category, asserted neither confirmed nor confabulated.",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "Twenty-two events (2.1%) could not be checked because the source could not be accessed to confirm or deny the claim. The causes were inaccessible URLs: paywalled, broken, or blocked. These are not asserted to be either confirmed or confabulated; they are recorded as a distinct category precisely because the verification could not be completed.",
        "location": {"section": "Supplement A.5 (The 22 unverifiable events)", "page": 38},
        "supports_claims": ["C112"],
        "notes": "Epistemically careful handling of the unverifiable residue."
    },
    {
        "evidence_id": "E283",
        "evidence_text": "Seventeen events (1.6%) were granularity errors: verified sources describing a project or framework rather than a discrete tool (e.g., VirtualArch).",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "Seventeen events (1.6%) were granularity errors: the source was verified, but the item it described was a project or framework rather than a discrete tool, so the tool classification was invalid (for example, VirtualArch, a project reported as though it were a specific tool).",
        "location": {"section": "Supplement A.5 (The 17 granularity errors)", "page": 38},
        "supports_claims": ["C112"],
        "notes": ""
    },
    {
        "evidence_id": "E284",
        "evidence_text": "Three event rows (0.3%) contained malformed provenance data — defective in recording where the evidence came from rather than in the substance of the claim.",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "Finally, three event rows (0.3%) contained malformed provenance data — defective in the recording of where the evidence came from rather than in the substance of the claim — and are noted separately for completeness.",
        "location": {"section": "Supplement A.5 (The three malformed-provenance rows)", "page": 38},
        "supports_claims": ["C112"],
        "notes": ""
    },
    {
        "evidence_id": "E285",
        "evidence_text": "Three services were trialled for evidence collection against FAIMS (ground truth); each exhibited a distinct failure pattern.",
        "evidence_type": "observation",
        "verbatim_quote": "Three services were trialled for evidence collection against FAIMS, where the authors hold groundtruth knowledge, and each exhibited a distinct failure pattern.",
        "location": {"section": "Supplement A.5 (Per-model selection comparison)", "page": 39},
        "supports_claims": ["C112"],
        "notes": "'groundtruth' preserves a line-break artefact of the processed md."
    },
    {
        "evidence_id": "E286",
        "evidence_text": "Claude Research fragmented FAIMS into four entries (each accurate but breaking data aggregation, requiring manual reconciliation), with similar fragmentation for other tools with variants.",
        "evidence_type": "observation",
        "verbatim_quote": "Claude Research fragmented FAIMS into four separate tool entries — FAIMS, FAIMS Mobile Platform, FAIMS 3.0, and Fieldmark — so that, while each entry contained accurate information, the fragmentation broke data aggregation: a researcher could not determine the complete evidence history without manual reconciliation, and similar naming fragmentation occurred with other tools that had variants.",
        "location": {"section": "Supplement A.5 (Per-model selection comparison)", "page": 39},
        "supports_claims": ["C112"],
        "notes": "Detail behind E148."
    },
    {
        "evidence_id": "E287",
        "evidence_text": "Gemini 2.5 Pro treated Wayback Machine snapshots as separate annual 'sources', producing duplicate rows across capture years, inflating counts without adding information and requiring manual deduplication.",
        "evidence_type": "observation",
        "verbatim_quote": "Gemini 2.5 Pro treated Wayback Machine snapshots as separate annual 'sources,' producing duplicate rows that captured the same webpage across different capture years, inflating evidence counts without adding information and requiring manual deduplication.",
        "location": {"section": "Supplement A.5 (Per-model selection comparison)", "page": 39},
        "supports_claims": ["C112"],
        "notes": "Detail behind E149."
    },
    {
        "evidence_id": "E288",
        "evidence_text": "ChatGPT Deep Research produced the highest-quality evidence results, explicitly classifying source types and noting verification status; it was selected for production because Claude and Gemini returned fewer valid rows and introduced the problems above.",
        "evidence_type": "observation",
        "verbatim_quote": "ChatGPT Deep Research produced the highest-quality results, explicitly classifying source types (for example, \"academic paper,\" \"GitHub repository,\" \"project website\") and noting verification status, and was selected for production because Claude and Gemini returned fewer valid evidence rows for the same tool sets and introduced the problems above.",
        "location": {"section": "Supplement A.5 (Per-model selection comparison)", "page": 39},
        "supports_claims": ["C112"],
        "notes": "Detail behind E150."
    },
]

CLAIMS = [
    {
        "claim_id": "C192",
        "claim_text": "That the most heavily documented tool also attracted the most fabrication is suggestive: abundant genuine material appears to lend borrowed plausibility to fabricated entries beside it.",
        "claim_type": "interpretation",
        "claim_role": "supporting",
        "verbatim_quote": "That the most heavily documented tool also attracted the most fabrication is suggestive: abundant genuine material appears to lend borrowed plausibility to the fabricated entries beside it.",
        "location": {"section": "Supplement A.5 (The 52 confabulated events across 26 tools)", "page": 38},
        "supported_by": ["E280"],
        "supports_claims": ["C109"],
        "notes": "Supplement articulation of C109; Pass 2 consolidation candidate."
    },
]

save_group(
    {
        "group": "G18",
        "section_title": "Supplement A.5 full evidence-collection error catalogue + per-model selection comparison",
        "page_range": "38-39",
        "estimated_words": 640,
        "natural_boundary": "End of document (p. 39)",
        "split_rationale": "Final supplement subsections; kept separate from G17 to respect the 1,500-word cap. Slightly larger than planned (~440) as the A.5 heading sits at L2158 rather than L2168."
    },
    evidence=EVIDENCE,
    claims=CLAIMS,
    implicit_arguments=[],
)
