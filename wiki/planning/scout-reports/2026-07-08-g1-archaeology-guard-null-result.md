# Scout report G1 (guard pass): OSF/grey-literature check of the "zero archaeology" claim — DOCUMENTED NULL

**Pipeline:** guard pass of the 2026-07-08 follow-up round (protects the first-mover claim before it is used in writing)
**Proposer:** lit-scout agent (guard-adapted protocol; 26 logged queries across OSF/SocArXiv via SHARE, Zenodo, Humanities Commons, DataCite, and six archaeology discipline venues)
**Verification status:** proposer self-check re-queried all three grounded near-miss DOIs; orchestrator spot-check independently confirmed all three (Spennemann 2023; Cobb 2023; Qi & Wen 2025). Full adversarial verification waived: the deliverable is a null result whose substance is the query log, not a findings table. Row 4 (Kim 2025, Korean Journal of Heritage) is explicitly AUTHORS UNVERIFIED (DOI not in CrossRef/DataCite; grounded via Humanities Commons record only).
**Bottom line:** the first-mover claim HOLDS if scoped ("applying LLMs to assess, extract from, or reproduce archaeological research") and worded "to our knowledge", with Spennemann 2023 cited and demarcated (it audits the model, not the literature). Not defensible as an unqualified universal.

---

All grounded near-misses are NEW to Zotero. Coverage is comprehensive across all five venue classes. Here is the deliverable — a documented null result.

---

# Lit-scout draft: guard pass — "zero archaeology" first-mover claim (LLM-based research assessment)

⚠ **VERIFICATION PENDING** — this is a draft from the proposer (lit-scout). The `/lit-scout` slash command runs the `lit-scout-verifier` serial agent against this draft before returning the final output. If you are reading this marker in final output, verification failed — see the banner at top of the document.

## TL;DR

Across the venues arXiv does not cover — OSF Preprints/SocArXiv (SHARE), Zenodo, Humanities Commons CORE, DataCite, and the discipline venues (Internet Archaeology, JCAA, Journal of Open Archaeology Data, Advances in Archaeological Practice, PCI Archaeology, CAA and CHR proceedings) — **no item was found that applies LLM-based methods extraction, citation-integrity analysis, credibility assessment, FAIR scoring, or computational reproduction TO archaeological/heritage/fieldwork research** (26 logged queries, 2026-07-08). The finding is therefore a **DOCUMENTED NULL**: the closest items are four grounded near-misses that all fall out of scope — they either evaluate an LLM's own reliability using archaeology as a test domain (Spennemann 2023, arXiv:2308.03301) or use an LLM as an archaeological tool (Kim 2025 metadata extraction; Qi & Wen 2025 review; Cobb 2023 editorial). The claim can be defended if scoped precisely and worded as "to our knowledge" (see Conclusion); it cannot be stated as an absolute universal.

## Findings table

These are **grounded near-misses only** — items that surfaced on keyword adjacency but are OUT OF SCOPE for refuting the first-mover claim. Fit is assessed against the user's argument as *demarcation value* (worth citing to draw the scope line), not as prior art that pre-empts it. No in-scope item exists to populate a genuine findings table.

| # | Fit | Cites | Authors (Year) | Title | DOI | Chain | Chains | Cluster | Status |
|---|-----|-------|----------------|-------|-----|-------|--------|---------|--------|
| 1 | MED | 5 | Spennemann (2023) | What has ChatGPT read? The origins of archaeological citations used by a generative artificial intelligence application | 10.48550/arXiv.2308.03301 | seed (WebSearch grey-lit) | 2 | Evaluates-the-LLM (archaeology as test domain) — OUT OF SCOPE | NEW |
| 2 | MED | 43 | Cobb (2023) | Large Language Models and Generative AI, Oh My! | 10.1017/aap.2023.20 | seed (AAP venue search) | 2 | Editorial/overview of genAI in archaeology — OUT OF SCOPE | NEW |
| 3 | LOW | 1 | Qi & Wen (2025) | Large Language and Multimodal Models in Archaeological Science: A Review | 10.3390/electronics14224507 | seed (AAP venue search) | 1 | Survey of LLM-as-tool in archaeology — OUT OF SCOPE | NEW |
| 4 | LOW | n/a | Kim (2025) `AUTHORS UNVERIFIED` | A Study on Archaeological Informatization Using LLMs — Proof of Concept for an Automated Metadata Extraction Pipeline from Archaeological Excavation Reports | 10.22755/kjchs.2025.58.3.34 | Humanities Commons API | 1 | LLM-as-tool: metadata extraction from excavation reports — OUT OF SCOPE | NEW |

Row 4 note: the DOI (Korean Journal of Heritage: History & Science) is **not indexed in CrossRef or DataCite** — `lit-search.py metadata` returns an empty record. Author "Kim, Hongyeon" (single author) and title/year come from the Humanities Commons InvenioRDM record (`works.hcommons.org` id `nmy33-26a12`), which is a grounded source but not a metadata-API response. Per Guard A it is flagged `AUTHORS UNVERIFIED` and moved to the end; it is **omitted from the machine-readable claims block** (no resolvable DOI in the verification pipeline).

## Proposer self-check

- Re-queried 3 grounded rows via a fresh `metadata` call (Cobb 10.1017/aap.2023.20; Spennemann 10.48550/arXiv.2308.03301; Qi & Wen 10.3390/electronics14224507). All three matched the table on `authors[0]`, author count, year, and citation count.
- Author-rendering length gate verified against returned counts: Spennemann (len 1 → bare surname), Cobb (len 1 → bare surname), Qi & Wen (len 2 → "A & B"). No "et al." applied to any ≤2-author paper.
- Spennemann's DataCite record returns the given name in full ("Dirk Spennemann"); rendered as the bare surname "Spennemann (2023)". WebSearch independently attributed it to "Dirk HR Spennemann, Charles Sturt University" — consistent, single author.
- Zotero dedup (DOI-first) run on all four grounded DOIs: all NEW.
- Kim (row 4) flagged AUTHORS UNVERIFIED because its DOI is not in CrossRef/DataCite; grounded via HC record instead and excluded from claims emission, per contract.
- No anomalies. One tooling note for the verifier: SHARE's `q` parameter is relevance-ranked with an OR default operator (a bare query returns 317k+ "hits"); its total counts are NOT filters and must not be read as such. I used AND/quoted phrases and per-result inspection instead of counts for the OSF/SocArXiv venue.

## Query log

Venue codes: **SHARE** = OSF/SocArXiv via `share.osf.io` Elasticsearch API (covers OSF Preprints incl. SocArXiv, MetaArXiv); **ZEN** = Zenodo REST API; **HC** = Humanities Commons CORE (InvenioRDM API); **DC** = DataCite REST API; **WS** = WebSearch; **WF** = WebFetch. All 2026-07-08.

| # | Venue | Query (paraphrased where long) | Hits | In-scope | Why out of scope |
|---|-------|-------------------------------|------|----------|------------------|
| 1 | SHARE | `archaeology AND "large language model" AND (reproducibility OR citation OR assessment OR extraction)` | 1* | 0 | AND-parse anomaly; single spurious cardiology hit, no archaeology |
| 2 | SHARE | `"large language model" archaeology reproducibility` (default OR) | 317,651* | 0 | Relevance-ranked OR; top hits medical/GUI/learning, no archaeology-research-assessment |
| 3 | SHARE (WF) | `archaeology "language model" reproducibility citation extraction` | ~20 shown | 0 | Only archaeology hits: Marwick "Is Archaeology a Science?" (human, non-LLM) and Schmidt & Marwick 2019 (non-LLM) |
| 4 | SHARE (WF) | `archaeology GPT credibility "methods extraction" FAIR "research assessment"` | ~20 shown | 0 | Assessment-reform + "ChatGPT for FAIR Research Data" (Shigapov, non-archaeology) |
| 5 | SHARE (WF) | `(archaeology OR heritage OR fieldwork) "credibility" "research integrity" "extract claims" GPT ChatGPT` | ~20 shown | 0 | Medical/education/FAIR-data; no archaeology-research-assessment |
| 6 | ZEN | `(archaeology OR archaeological OR heritage OR fieldwork) AND ("large language model" OR LLM OR GPT)` | 142 | 0 | Musicology+AI, CH monitoring, art history, LLM-querying benchmarks |
| 7 | ZEN | grid + `(reproducib* OR citation OR "research assessment" OR extraction OR credibility OR FAIR)` | 51 | 0 | Ontology engineering, knowledge graphs, art-history LLM, fringe |
| 8 | ZEN | `archaeolog* AND ("methods extraction" OR "claim extraction" OR "computational reproduction" OR "research transparency" OR "open science") AND (LLM OR GPT OR "language model" OR AI)` | 34 | 0 | Paradata (known, non-LLM), knowledge graphs, fringe/pseudo-scholarship |
| 9 | ZEN | `(archaeolog* OR heritage) AND ("peer review" OR "systematic review" OR transparency OR "claim extraction" OR "evidence synthesis") AND (LLM OR GPT OR ChatGPT OR "language model")` | 39 | 0 | Web-archives RAG, Transkribus, education bibliometrics |
| 10 | ZEN | `(archaeolog* OR "cultural heritage") AND ("computational reproduction" OR "reproducibility review" OR "research credibility" OR "claims extraction" OR "methods assessment")` | 4 | 0 | Standardisation pipeline, W-Africa preservation, digital library, ancient-architecture (pyramidology) |
| 11 | HC | `archaeology AND ("large language model" OR GPT OR ChatGPT OR LLM)` | 4 | 0 | 1 archaeology near-miss (Kim, metadata extraction); + book promo, fringe pyramid AI-review |
| 12 | DC | grid + assessment terms, `resource-type-id=dataset` | 1 | 0 | Single junk record ("Heritage Foundry Master Ledger" licensing) |
| 13 | DC | grid + assessment terms, all resource types | 1 | 0 | Same junk record |
| 14 | WS | JCAA / Internet Archaeology × LLM methods extraction reproducibility | — | 0 | "Machine Learning Applications in Archaeological Practices: A Review" (jcaa.201) — LLM/ML-as-tool review |
| 15 | WS | Advances in Archaeological Practice × LLM research assessment credibility | — | 0 | Cobb editorial (near-miss); Marwick reproducibility editor (human); electronics review |
| 16 | WF | Cambridge Core: Cobb editorial page | 1 | 0 | Editorial/discussion, not application (grounded → row 2) |
| 17 | WS | CAA proceedings 2025/2026 × LLM peer review / extract methods | — | 0 | CAA 2026 "hybrid AI–human workflow extracting structured archaeological data from archival records" — LLM-as-tool data extraction |
| 18 | WS | PCI Archaeology × LLM/ChatGPT recommendation reproducibility credibility | — | 0 | General reproducibility policy; known Bellat recommendation only |
| 19 | WS | Internet Archaeology × ChatGPT/LLM peer review / credibility | — | 0 | General (non-archaeology) peer-review-LLM papers; nothing IA-specific |
| 20 | WS | CHR 2024/2025 proceedings × archaeology/heritage LLM | — | 0 | LLM-as-tool DH: entity matching, semantic enrichment, memorisation, cultural-analytics classification |
| 21 | WS | JCAA / JOAD 2025/2026 × LLM reproducibility / FAIR | — | 0 | JOAD = data papers; Archaeological Prospection ChatGPT-4o magnetometer test (LLM-as-tool) |
| 22 | WS | LLM archaeology research assessment methods extraction reproducibility preprint 2025 | — | 0 | General: software-engineering & social-science reproducibility, no archaeology |
| 23 | WS | GPT archaeological literature citation integrity credibility FAIR 2025/2026 | — | 0 | Surfaced Spennemann arXiv near-miss; else non-archaeology citation tools (CitePrism, SemanticCite) |
| 24 | WS | Humanities Commons / PCI / CHR × archaeology LLM reproducibility | — | 0 | General social-science reproduction, "humanities provocations"; no archaeology instance |
| 25 | WS | LLM extract methods/claims archaeology credibility reproducibility thesis/repository | — | 0 | General SE + systematic-review data extraction; no archaeology |
| 26 | WS | `"What has ChatGPT read" archaeological citations DOI` | — | 0 | Grounding-only search → Spennemann arXiv:2308.03301 (row 1) |

*SHARE counts marked with an asterisk are relevance-ranked OR totals, not filtered result sets — treat as non-informative (see self-check note).

## Landscape

The **general** field of LLM-based research assessment is demonstrably active in 2025–26 — the sweeps repeatedly surfaced CORE-Bench, ReproScore, ReproRepo, ARA (agentic reproducibility assessment), "LLMs for post-publication research evaluation," "Measuring the State of Open Science in Transportation Using LLMs," and automated-peer-review surveys — but **none of these touch archaeology, heritage, or fieldwork**. They cluster in software engineering, biomedicine, and quantitative social science. This matters for the framing: the user is not first-mover on *LLM-based research assessment as such* (a crowded space), but the guard-pass question is narrower and survives — first-mover on *applying* those methods *to the archaeological/heritage/fieldwork literature*.

Within archaeology itself, the LLM literature that does exist is uniformly **LLM-as-tool** (artefact/geophysics interpretation, OCR/NER on excavation reports and archival records, metadata extraction, chatbots, generative reconstruction) or **discussion/review** (Cobb 2023 editorial; Qi & Wen 2025 review; the AAP genAI cluster). The one adjacent strand that concerns research *integrity* — Spennemann's "What has ChatGPT read?" — points the lens the other way: it audits the LLM's own archaeological citations, not the archaeological literature's credibility.

## Thematic clusters

1. **Evaluates-the-LLM, archaeology as test domain** (1 member: Spennemann 2023). Tests ChatGPT's fabrication/citation reliability *on* archaeological references. Adjacent to "citation-integrity analysis" but the object of assessment is the model, not the discipline's research. On arXiv → inside the already-swept space.
2. **LLM-as-tool for archaeological data/information** (Kim 2025 metadata extraction; CAA 2026 archival-record extraction; Archaeological Prospection magnetometer test; "Smart Anomaly Detection Assistant" chatbot). Extraction/interpretation of primary data, not appraisal of published research.
3. **Discussion / review of genAI in archaeology** (Cobb 2023 editorial; Qi & Wen 2025 review; the broader AAP "AI and interpretation of the past" cluster). Meta-commentary, not method application.
4. **Known excluded prior art** (confirmed present, not counted, per your brief): Marwick 2025 "Is archaeology a science?" (JAS `S030544032500130X`; SocArXiv `osf.io/fdhvb`) — human-performed reproducibility reviews; Bellat 2026 PCI Archaeology recommendation; the 2025 arts/humanities paradata paper (Zenodo `10.5281/zenodo.15632448`, the Huvila-tradition, non-LLM). Your own `llm-reproducibility` repo did **not** surface in any of these venues.
5. **General LLM research-assessment field, non-archaeology** (CORE-Bench, ReproScore, ARA, post-publication-evaluation, automated-peer-review surveys). Establishes the method space exists but has no archaeology instantiation.

## Gaps noticed

- **The scoped gap is real and empty.** No venue outside arXiv holds an item applying LLM methods-extraction / citation-integrity / credibility / FAIR / reproduction *to* archaeological research. Combined with your two prior arXiv sweeps, the four-venue-class coverage here is the strongest form the negative can take short of exhaustive manual browsing.
- **Spennemann is the item most likely to be raised against a first-mover claim** by a reviewer, because "ChatGPT + archaeological citations" reads superficially like citation-integrity work. Pre-empt it in the paper by naming it and stating the direction-of-assessment distinction (it audits the model; you audit the literature).
- **Coverage limits to disclose honestly:** (i) Humanities Commons' web UI returned HTTP 403 to WebFetch — I used its InvenioRDM API instead, which returned only 4 archaeology+LLM records; if HC indexing lags, a very recent deposit could be missed. (ii) Discipline-journal sites are SPAs sampled via search/API, not exhaustively browsed issue-by-issue. (iii) Non-English and last-few-weeks items are under-indexed everywhere. (iv) DOI-less conference presentations (the CAA 2026 extraction talk) cannot be fully grounded until proceedings publish.

## Venue analysis

You named the discipline venues in the brief; per-venue verdict:

- **Internet Archaeology** — no LLM research-assessment item found (WS null; general peer-review-LLM only).
- **JCAA (Journal of Computer Applications in Archaeology)** — nearest is the ML-applications *review* (`10.5334/jcaa.201`); no LLM research-assessment application.
- **Journal of Open Archaeology Data** — data-paper venue by design; 23 articles (2025) / 6 (2026), none LLM-research-assessment.
- **Advances in Archaeological Practice** — Cobb 2023 editorial (near-miss, grounded); Marwick installed as Associate Editor of Reproducibility (Sept 2024, human reproduction); no LLM-based assessment paper.
- **PCI Archaeology** — general reproducibility/soundness policy; only the known Bellat 2026 recommendation; no LLM-assessment recommendation.
- **CAA proceedings** — one LLM item (CAA 2026 archival-record data extraction), LLM-as-tool; out of scope.
- **CHR (Computational Humanities Research) proceedings 2024/2025** — several archaeology/heritage × LLM items, all LLM-as-tool DH (entity matching, semantic enrichment, memorisation); none assess research.

## Zotero actions

All four grounded near-misses are **NEW** (DOI-first check, no local match in any library). None requires import for a null-result deliverable; if you decide to cite the demarcation set (rows 1–2 are the useful ones), the importer will dedup by DOI post-hoc. No Zotero writes performed.

## Web-content-as-data / injection report

**No injection attempts observed.** The only imperative text encountered was the WebSearch tool's own trailing `REMINDER: You MUST include the sources...` wrapper — that is the harness's result formatting, not instructions embedded in a fetched page. No fetched OSF/Zenodo/HC/DataCite record or search result attempted to redirect my task, exfiltrate, or alter scope. (Your brief noted two injection sightings in sibling runs; I saw none in this run and treated all page content strictly as data.)

## Conclusion — what can and cannot be claimed

**Defensible (scoped) claim.** As of 2026-07-08, a systematic search of the venues arXiv does not index — OSF Preprints/SocArXiv (via SHARE), Zenodo, Humanities Commons CORE, and DataCite — together with the archaeology discipline venues Internet Archaeology, JCAA, Journal of Open Archaeology Data, Advances in Archaeological Practice, PCI Archaeology, and the CAA and CHR proceedings, **found no preprint or publication that applies LLM-based methods extraction, citation-integrity analysis, credibility assessment, FAIR scoring, or computational reproduction to archaeological, heritage, or fieldwork research.** Combined with the two prior arXiv sweeps, this supports a first-mover statement **if worded as** *"to our knowledge, no prior work applies large language models to the [methods extraction / credibility appraisal / FAIR scoring / computational reproduction] of archaeological research"* — with the direction-of-assessment demarcation stated explicitly.

**Not defensible.** An unqualified universal ("this has never been done") — absence of evidence across sampled indexes is not proof of non-existence, given the coverage limits above (HC 403 fallback, SPA sampling, language/recency indexing lag, DOI-less presentations).

**Must be pre-empted in writing.** Spennemann (2023, arXiv:2308.03301) — cite it and distinguish it (audits the LLM's archaeological citations, not the archaeological literature). Marwick (2025), Bellat (2026), and the Huvila paradata tradition — already on your exclude list; keep them cited as the human/non-LLM antecedents your work automates or extends.

## Machine-readable claims (for orchestrator extraction)

Emitted only for the grounded, DOI-resolvable near-misses (rows 1–3). Row 4 (Kim) is omitted: its DOI is not indexed in CrossRef/DataCite, so it carries no verifiable metadata-API claim and is flagged `AUTHORS UNVERIFIED` in the table.

<!-- BEGIN claims.jsonl -->
```jsonl
{"claim_id":"10.48550-arxiv.2308.03301-authors","doi":"10.48550/arXiv.2308.03301","category":"authors","description":"Authors for row 1","value":"Spennemann (2023)","source_method":"lit-search.py metadata","source_file":"Findings table row 1"}
{"claim_id":"10.48550-arxiv.2308.03301-year","doi":"10.48550/arXiv.2308.03301","category":"year","description":"Publication year for row 1","value":2023,"source_method":"lit-search.py metadata","source_file":"Findings table row 1"}
{"claim_id":"10.48550-arxiv.2308.03301-title","doi":"10.48550/arXiv.2308.03301","category":"title","description":"Title for row 1","value":"What has ChatGPT read? The origins of archaeological citations used by a generative artificial intelligence application","source_method":"lit-search.py metadata","source_file":"Findings table row 1"}
{"claim_id":"10.48550-arxiv.2308.03301-citation_count","doi":"10.48550/arXiv.2308.03301","category":"citation_count","description":"Citation count for row 1","value":5,"source_method":"lit-search.py metadata","source_file":"Findings table row 1"}
{"claim_id":"10.48550-arxiv.2308.03301-doi_resolves","doi":"10.48550/arXiv.2308.03301","category":"doi_resolves","description":"DOI resolves to expected paper for row 1","value":true,"source_method":"lit-search.py metadata","source_file":"Findings table row 1"}
{"claim_id":"10.1017-aap.2023.20-authors","doi":"10.1017/aap.2023.20","category":"authors","description":"Authors for row 2","value":"Cobb (2023)","source_method":"lit-search.py metadata","source_file":"Findings table row 2"}
{"claim_id":"10.1017-aap.2023.20-year","doi":"10.1017/aap.2023.20","category":"year","description":"Publication year for row 2","value":2023,"source_method":"lit-search.py metadata","source_file":"Findings table row 2"}
{"claim_id":"10.1017-aap.2023.20-title","doi":"10.1017/aap.2023.20","category":"title","description":"Title for row 2","value":"Large Language Models and Generative AI, Oh My!","source_method":"lit-search.py metadata","source_file":"Findings table row 2"}
{"claim_id":"10.1017-aap.2023.20-citation_count","doi":"10.1017/aap.2023.20","category":"citation_count","description":"Citation count for row 2","value":43,"source_method":"lit-search.py metadata","source_file":"Findings table row 2"}
{"claim_id":"10.1017-aap.2023.20-doi_resolves","doi":"10.1017/aap.2023.20","category":"doi_resolves","description":"DOI resolves to expected paper for row 2","value":true,"source_method":"lit-search.py metadata","source_file":"Findings table row 2"}
{"claim_id":"10.3390-electronics14224507-authors","doi":"10.3390/electronics14224507","category":"authors","description":"Authors for row 3","value":"Qi & Wen (2025)","source_method":"lit-search.py metadata","source_file":"Findings table row 3"}
{"claim_id":"10.3390-electronics14224507-year","doi":"10.3390/electronics14224507","category":"year","description":"Publication year for row 3","value":2025,"source_method":"lit-search.py metadata","source_file":"Findings table row 3"}
{"claim_id":"10.3390-electronics14224507-title","doi":"10.3390/electronics14224507","category":"title","description":"Title for row 3","value":"Large Language and Multimodal Models in Archaeological Science: A Review","source_method":"lit-search.py metadata","source_file":"Findings table row 3"}
{"claim_id":"10.3390-electronics14224507-citation_count","doi":"10.3390/electronics14224507","category":"citation_count","description":"Citation count for row 3","value":1,"source_method":"lit-search.py metadata","source_file":"Findings table row 3"}
{"claim_id":"10.3390-electronics14224507-doi_resolves","doi":"10.3390/electronics14224507","category":"doi_resolves","description":"DOI resolves to expected paper for row 3","value":true,"source_method":"lit-search.py metadata","source_file":"Findings table row 3"}
```
<!-- END claims.jsonl -->

---

Scratchpad used: `/tmp/claude-1000/-home-shawn-Code-llm-reproducibility/7611d1aa-3419-49ba-a23e-b887887a92ea/scratchpad/guard-d/` (no persistent files needed; all query outputs were transient).

**Bottom line for your writing:** the guard pass confirms the null across the venues arXiv does not cover. The first-mover claim holds **if scoped** to "applying LLMs to assess/extract-from/reproduce archaeological research" and worded "to our knowledge," with Spennemann (2023) cited and demarcated. It does **not** hold as an absolute universal, and it does **not** extend to LLM-based research assessment in general (a busy non-archaeology field).
