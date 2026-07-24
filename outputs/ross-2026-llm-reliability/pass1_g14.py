#!/usr/bin/env python3
"""Pass 1, Group G14: Supplement A intro + A.1 per-tool literature-discovery detail + source overlap + Gemini anecdote (pp. 30-32, ~920 words)."""

from pass1_lib import save_group

EVIDENCE = [
    {
        "evidence_id": "E211",
        "evidence_text": "ChatGPT Deep Research identified 43 valid sources (37 unique) from a 93-source corpus; it required two prompting attempts; of 58 returned, 4 were irrelevant and 11 could not be located despite extensive searching (most likely confabulations).",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "ChatGPT Deep Research identified 43 valid sources (37 unique to this system) from a corpus of 93 total unique sources across all methods. It required two prompting attempts: an initial standard prompt produced unusable output, while a revised prompt emphasising scholarly sources yielded the documented results. Of 58 total sources returned, 4 were irrelevant to the research topic and 11 could not be located despite extensive searching and most likely represent confabulations.",
        "location": {"section": "Supplement A.1", "page": 30},
        "supports_claims": ["C082", "C083"],
        "notes": "Granular backing for Table 2 main-text figures."
    },
    {
        "evidence_id": "E212",
        "evidence_text": "ChatGPT DR's valid output decomposed into 20 journal articles, 13 reports, 4 conference papers, 2 academic blog posts, 2 preprints, 1 presentation, and 1 web page — all meeting academic seriousness thresholds.",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "The service's valid output decomposed into 20 journal articles, 13 reports, 4 conference papers, 2 academic blog posts, 2 preprints, 1 presentation, and 1 web page; all met academic seriousness thresholds, with no lightweight or non-academic content requiring exclusion.",
        "location": {"section": "Supplement A.1", "page": 30},
        "supports_claims": ["C083"],
        "notes": ""
    },
    {
        "evidence_id": "E213",
        "evidence_text": "ChatGPT DR citation accuracy: 10 sources with incorrect URLs requiring manual rediscovery, at least 5 with incorrect DOIs, at least 13 with poorly formatted or incomplete author information.",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "Citation accuracy was the weak point: 10 sources carried incorrect URLs requiring manual rediscovery, at least 5 contained incorrect DOIs, and at least 13 featured poorly formatted or incomplete author information.",
        "location": {"section": "Supplement A.1", "page": 30},
        "supports_claims": ["C084"],
        "notes": "Quantifies the two-thirds manual-correction figure of the main text. Following BibTeX sentence spans the p30/p31 page break."
    },
    {
        "evidence_id": "E214",
        "evidence_text": "21 of ChatGPT DR's sources on national and international initiatives came from targeted follow-up queries, demonstrating responsiveness to prompt refinement.",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "Of its returns, 21 sources on national and international initiatives came from targeted follow-up queries, demonstrating responsiveness to prompt refinement.",
        "location": {"section": "Supplement A.1", "page": 31},
        "supports_claims": ["C083"],
        "notes": ""
    },
    {
        "evidence_id": "E215",
        "evidence_text": "Perplexity: 20 valid (14 unique); initial query 9 valid + 6 invalid; follow-ups 11 more valid with diminishing returns; of 34 items 14 invalid (5 non-academic web pages, 8 irrelevant, 1 predatory journal).",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "Perplexity Research identified 20 valid sources (14 unique). The initial standardised query produced 9 valid sources alongside 6 invalid items, and follow-up queries yielded the remaining 11 valid sources — demonstrating diminishing returns, as subsequent searches returned proportionally more irrelevant results. Of 34 total items, 14 were invalid: 5 web pages failed to meet academic seriousness thresholds, 8 sources were irrelevant to the research topic despite potential value elsewhere, and 1 article appeared in a predatory journal.",
        "location": {"section": "Supplement A.1", "page": 31},
        "supports_claims": ["C082"],
        "notes": ""
    },
    {
        "evidence_id": "E216",
        "evidence_text": "Tasked with a cited literature review, Perplexity claimed to have analysed 25 sources while providing only 3 references — a claimed-versus-actual gap making its outputs closer to sophisticated web searches than research assistance.",
        "evidence_type": "observation",
        "verbatim_quote": "When tasked with producing a literature review with citations, it claimed to have analysed 25 sources while providing only 3 references — a gap between claimed and actual performance that, combined with minimal reasoning and poor academic database access, made its outputs closer to sophisticated web searches than to research assistance.",
        "location": {"section": "Supplement A.1", "page": 31},
        "supports_claims": ["C082", "C085"],
        "notes": ""
    },
    {
        "evidence_id": "E217",
        "evidence_text": "Elicit: 10 valid (8 unique), smallest yield but zero invalid references (superior precision); citation accuracy best of the services though 3 of 10 records had incorrectly formatted or incomplete author information.",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "Elicit identified 10 valid sources (8 unique) — the smallest yield among tested platforms — but returned no invalid or unusable references at all, demonstrating superior precision despite limited coverage. Its citation accuracy exceeded the other services, though 3 of 10 records contained incorrectly formatted or incomplete author information.",
        "location": {"section": "Supplement A.1", "page": 31},
        "supports_claims": ["C082"],
        "notes": ""
    },
    {
        "evidence_id": "E218",
        "evidence_text": "Elicit separated discovery, evaluation, and synthesis into explicit phases (architecture aligned with research workflows), but Semantic Scholar reliance severely limited coverage (particularly humanities) and TLDR-summary screening was low quality; from identical prompts it yielded 9 useful sources against Deep Research's 55.",
        "evidence_type": "observation",
        "verbatim_quote": "The service separated source discovery, evaluation, and synthesis into explicit phases, a conceptual architecture that aligned well with research workflows; its reliance on Semantic Scholar, however, severely limited coverage (particularly in the humanities), and its dependence on AI-generated \"TLDR\" summaries rather than full-text analysis produced low-quality screening. From identical prompts, Elicit yielded only 9 useful sources against 55 from Deep Research.",
        "location": {"section": "Supplement A.1", "page": 31},
        "supports_claims": ["C082"],
        "notes": ""
    },
    {
        "evidence_id": "E219",
        "evidence_text": "Overlap detail: no source appeared in all three services' results; only seven were identified by more than one platform (five ChatGPT–Perplexity, including Barats, Schafer, and Fickers 2020 and Tucker 2022; one ChatGPT–Elicit, Imran and Kosar 2019).",
        "evidence_type": "quantitative_measurement",
        "verbatim_quote": "The services overlapped strikingly little, which reflects divergent search strategies rather than systematic coverage: no source appeared in all three results, and only seven were identified by more than one platform. Five sources overlapped between ChatGPT and Perplexity, including foundational works on digital-humanities sustainability by Barats, Schafer, and Fickers (2020) and Tucker (2022). One source, a systematic literature review on software sustainability by Imran and Kosar (2019), was identified by both ChatGPT and Elicit.",
        "location": {"section": "Supplement A.1 (Source overlap)", "page": 31},
        "supports_claims": ["C083"],
        "notes": ""
    },
    {
        "evidence_id": "E220",
        "evidence_text": "Gemini returned fewer quality-threshold sources, confabulated at high rates with plausible-sounding but non-existent citations, and unlike other systems' useful near-misses offered no serendipitous value.",
        "evidence_type": "observation",
        "verbatim_quote": "Gemini returned fewer sources meeting quality thresholds and confabulated at high rates, frequently inventing plausible-sounding citations that did not correspond to real publications; unlike other systems' useful near-misses, which could lead to relevant literature, Gemini's offered no serendipitous value.",
        "location": {"section": "Supplement A.1 (The Gemini 'source soup' anecdote)", "page": 31},
        "supports_claims": ["C082", "C014"],
        "notes": ""
    },
    {
        "evidence_id": "E221",
        "evidence_text": "Gemini's 'thinking' logs revealed a tendency to conflate multiple complex tasks into single operations.",
        "evidence_type": "observation",
        "verbatim_quote": "Examination of its \"thinking\" logs revealed a tendency to conflate multiple complex tasks into single operations.",
        "location": {"section": "Supplement A.1 (The Gemini 'source soup' anecdote)", "page": 31},
        "supports_claims": ["C085"],
        "notes": ""
    },
    {
        "evidence_id": "E222",
        "evidence_text": "In one digital-humanities search Gemini declared a systematic plan, then claimed to have 'successfully analysed a chapter from Debates in the Digital Humanities' after downloading only a snippet.",
        "evidence_type": "observation",
        "verbatim_quote": "In one digital-humanities search, Gemini declared: \"My next steps involve a more systematic approach to understanding the academic landscape by exploring a directory of DH centers. I also plan to analyze a key chapter discussing the future of DH research.\" It then claimed to have \"successfully analysed a chapter from Debates in the Digital Humanities\" after downloading only a snippet.",
        "location": {"section": "Supplement A.1 (The Gemini 'source soup' anecdote)", "page": 31},
        "supports_claims": ["C085", "C014"],
        "notes": "Expanded transcript detail behind the main-text E084 episode. Following sentence (Google Scholar non-use) spans the p31/p32 page break."
    },
    {
        "evidence_id": "E223",
        "evidence_text": "The authors termed the Gemini result 'source soup': search results collected without meaningful evaluation.",
        "evidence_type": "observation",
        "verbatim_quote": "We termed the result 'source soup': search results collected without meaningful evaluation.",
        "location": {"section": "Supplement A.1 (The Gemini 'source soup' anecdote)", "page": 32},
        "supports_claims": ["C085"],
        "notes": ""
    },
]

CLAIMS = [
    {
        "claim_id": "C185",
        "claim_text": "Because each service surfaced literature the others missed, their combined contribution exceeded any single one.",
        "claim_type": "interpretation",
        "claim_role": "supporting",
        "verbatim_quote": "Because each service surfaced literature the others missed, their combined contribution exceeded any single one.",
        "location": {"section": "Supplement A.1 (Source overlap)", "page": 31},
        "supported_by": ["E219"],
        "supports_claims": ["C083"],
        "notes": ""
    },
]

save_group(
    {
        "group": "G14",
        "section_title": "Supplement A intro + A.1 per-tool literature-discovery detail, source overlap, Gemini 'source soup'",
        "page_range": "30-32",
        "estimated_words": 920,
        "natural_boundary": "Before 'Source synthesis: per-model detail' heading (p. 32)",
        "split_rationale": "Supplement A split at its own subsection boundaries; this group covers the per-service literature-discovery record."
    },
    evidence=EVIDENCE,
    claims=CLAIMS,
    implicit_arguments=[],
)
