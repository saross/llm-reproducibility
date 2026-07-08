# Stack positioning synthesis — 2026-07-07/08 scout sweep

**Status:** Final — all twelve runs verified (the last, P5 literature, passed 130/130
claims with zero corrections)
**Method:** Six paired pipelines (literature scout + prior-art scout, one pair per stack
component), every run adversarially verified by a fresh-context verifier that re-queried
every DOI, repository, and service against its authoritative source. Twelve runs total,
~330 candidate rows, ~1,600 machine-checkable claims verified. Individual verified reports
live alongside this file; see `README.md` in this directory for the index.
**Requested by:** Shawn (overnight instruction, 2026-07-07): assess our position versus the
state of the art across the entire llm-reproducibility stack; all disciplines, highlight
HASS (humanities, arts, and social sciences); find what to learn from and which gaps we can
productively fill.

---

## 1. The one-paragraph answer

Every lane of the stack shows the same shape: a mature core built for biomedicine,
clinical trials, or computer science; a fast 2024–2026 turn toward Large Language Model
(LLM) methods that is still preprint-dominated and thin on validation; and an essentially
empty HASS/archaeology centre. In **no lane** did any scout find a system occupying our
specific combination — and several verifiers explicitly confirmed that searches for our
approach surface only this repository. The project is not re-inventing anything; in each
lane it threads together two or three adjacent traditions that do not currently cite each
other, in a discipline none of them serve.

## 2. Position by lane

| Lane | Adjacent territory (crowded) | Our combination | HASS/archaeology |
|------|------------------------------|-----------------|------------------|
| P1 Reproduction | Agentic repro benchmarks for CS/quant-soc-sci (CORE-Bench, SocSci-Repro-Bench, PaperBench); most 2026 "assessment" tools do NOT execute code | Docker execution + FAIR pass + fresh-context adversarial review — found nowhere as a combination | **Unclaimed** |
| P2 CEM extraction | Claim-vs-corpus verification (SciFact line); citation stance (scite); flat-table systematic-review extraction (Elicit et al.) | Full-paper explicit+implicit claims–evidence graph with linkage strength and reliability QA | **Unclaimed** (nearest: ATR4CH/SEBI, cultural-heritage Wikipedia text, 2 categories) |
| P3 RDMAP | Biomedical compliance/presence checkers (statcheck, SciScore, CONSORT-NLP, AutoReporter); PICO extraction; wet-lab protocol corpora | Three-tier design/method/protocol hierarchy, explicit+implicit, with APPROPRIATENESS judgement | **Unclaimed**; "RDMAP" acronym itself unclaimed |
| P4 Credibility | Human elicitation (repliCATS/IDEA — LLMs absent); ML replication predictors (binary outcome); LLM quality scorers (scalar score) | LLM-computed multi-signal credibility profile from structured extraction, stability-tested | **Unclaimed** ("a SciScore for HASS" confirmed absent) |
| P5 FAIR | ~20 repository-side evaluators (all need a persistent identifier); paper-side statement DETECTORS (oddpub/DataSeer, rule-based) | Paper-side entry → repository → 15 binary GO-FAIR sub-principles, LLM-judged, data and code scored independently | **Unclaimed** (only archaeology initiative is a manual questionnaire in development) |
| P6 Literature engagement (planned) | Citation-intent classifiers (CS-trained); quotation-error studies (biomedical); retraction checking (solved) | Fairness + accuracy + coverage + discourse jointly, on a CEM graph, single-paper granularity | **Unclaimed**; the whole coverage/discourse side is empty for HASS |

## 3. What to adopt or adapt (concrete, ranked)

**Adopt directly (near-zero cost):**

1. **Retraction checking via Crossref.** Retraction Watch data is now served free through the
   standard `api.crossref.org/works/{DOI}` endpoint. A per-DOI lookup over each paper's
   reference list is a few lines of code and gives the P6 lane its first working component.
2. **aggreCAT** (metamelb-repliCATS/aggreCAT, MIT — licence verified in-file despite the
   GitHub API's NOASSERTION) — purpose-built repliCATS judgement-aggregation maths from the
   original team, directly reusable for signal combination.

**Adapt as design references (read, don't wrap):**

3. **CORE-Bench's three-tier difficulty ladder** (pre-run output → Dockerfile-only →
   README-only) as an internal maturity classification for each paper's materials before
   reproduction starts.
4. **SemanticCite's four-class citation-support scheme** (Supported / Partially Supported /
   Unsupported / Uncertain, with confidence + evidence snippet) as the schema shape for the
   citation-accuracy lane — but reimplement natively; the repo advertises MIT yet ships no
   licence file.
5. **Fair-Way's divide-and-conquer prompt decomposition** (per-indicator sub-tasks) for the
   FAIR lane's prompt structure; **SOMEF/codemetapy** as a machine-extracted metadata
   pre-pass for the code-FAIR score (reduces hallucination surface); **howfairis's**
   five binary checks as a free rule-based sanity cross-check on the code side.
6. **Generalisability-theory variance decomposition** (Liu 2026, SSRN) and Thelwall & Yang's
   repeated-run score probabilities (QSS 2025) — adopt as the statistical framing that
   upgrades the 25-run stability test from an implementation detail to a named
   methodological contribution.
7. **Evaluation protocols** from SocSci-Repro-Bench and "Read the Paper, Write the Code"
   (cell-level comparison; information isolation) for validating reproduction faithfulness.

**Cite as validation/critique literature (grant and papers):**

- Candela, Mangione & Pavone 2024 (FAIR tools are rule-based and developer-subjective;
  explicitly recommends LLM-based assessment; warns against beyond-FAIR scope creep and
  under-weighted Accessibility sub-principles — audit our rubric against both).
- Peters-von Gehlen et al. 2022 (five-evaluator ensemble; manual scores systematically
  exceed automated — the validation-design template for our human-vs-LLM comparison).
- Windhouwer et al. 2025 (generic FAIR metrics misalign with community FAIR Implementation
  Profiles — write archaeology-specific interpretation notes for the 15 sub-principles).
- Crockett et al. 2023 (limitations of ML replicability prediction — our quality gating and
  stability testing answer this critique; internalise its evaluation standards).
- Tan & D'Souza 2026 and Simmons et al. 2025 (LLM extraction collapses on relational,
  multi-property, cross-document binding; single-pass RAG hit only 42% full accuracy —
  citable evidence that the multi-pass CEM/RDMAP design addresses a genuinely hard problem).
- Hellqvist 2010 (humanities citation practice breaks the assumptions of biomedical
  citation analysis — the caveat to internalise before porting any P6 method).

## 4. Competitive watch list

- **Center for Open Science — ReplicatorBench/ReplicatorAgent** (Apache-2.0, KDD 2026
  paper, Open Philanthropy funding): LLM agents re-executing social/behavioural-science
  replications in Docker. Different construct from our signal-scoring, same funders'
  ecosystem — the strongest candidate for a scoping conversation or grant-narrative
  differentiation.
- **Institute for Replication — AI Replication Engine**: pre-release, three-agent design,
  active SSHRC Insight Development Grant application (~CAD 95k, 2026–2028), NeurIPS 2026
  target. Closest institutional analogue; watch RePEc for their discussion paper.
- **Marwick 2025** (J. Archaeological Science 106281): 10,000-article analysis plus a year
  of JAS reproducibility reviews. This is not a competitor to differentiate from but the
  disciplinary anchor to engage — our JAS census and reproduction study sit directly on
  the ground his reviews prepared, and the paper is an obvious methodological reference
  point (and he a likely reviewer).
- **AutoReporter** (JAMIA 2026) and **Fair-Way** (CIKM'25): the most current LLM
  compliance/FAIR tools; both young, both worth re-checking at grant-report time.

## 5. Verification meta-findings (evidence for our own thesis)

The sweep itself demonstrated the proposer-plus-adversarial-verifier architecture the
project advocates:

- **~1,600 claims re-checked; hard-failure rate ≈ 1%. Zero fabricated papers, repositories,
  or tools across all twelve runs** — every resource in every table exists.
- The failures had a taxonomy: **11 of 14 hard failures were one systematic defect** —
  "et al." rendered on two-author papers (suppressing named co-authors such as Heathers,
  Gneezy, Auer, Spillias, Wallace) across three lit-scout runs. The one run whose proposer
  used a length-gated rendering rule scored 0/120 errors — the fix is known and should be
  patched into the lit-scout agent definition. The remainder: one genuinely confabulated
  author given name ("Yiling Yang" for PNAS's Yang Yang — caught, corrected), and two
  wrong-field metadata reads (dates).
- Failures concentrated exactly where proposers said confidence was lowest (WebSearch
  snippets vs API-grounded fields) — honest self-flagging predicted the error surface.
- **Two prompt-injection attempts** were encountered in the web-search layer (fake
  system-reminder and fake MCP-server instructions); both agents recognised and refused
  them. Worth a working-note: the search layer is an adversarial input channel.
- One session-limit outage interrupted four agents mid-run; all four were relaunched after
  reset with lessons carried forward (contamination warnings, author-count checks), and
  the rerun verifications were materially better targeted for it.

## 6. Gaps we can productively fill (accumulated, deduplicated)

1. First end-to-end computational reproduction pipeline for HASS/archaeology (P1).
2. Defining what agentic "reproduction" means for non-code-based scholarship — a
   conceptual contribution no benchmark attempts (P1).
3. Full-paper explicit+implicit claims–evidence graph with linkage-strength grading and a
   reliability-QA layer (P2) — implicit-claim identification is near-first-mover territory.
4. Repeated-run stability of structured *extraction* (not classification) as a published
   method (P2/P4) — currently confined to SSRN/OSF preprints.
5. Three-tier methods hierarchy + appropriateness judgement for narrative fieldwork
   methods (P3) — presence-vs-appropriateness is the qualitative leap past the SciScore
   family.
6. LLM-computed repliCATS-style credibility signals — "an in-silico IDEA panel" — with
   quality gating as a named evaluation-hygiene practice (P4).
7. Validated LLM scoring of GO-FAIR sub-principles against human raters; paper-side entry;
   independent data/code scores (P5). Cheap adjacent publication: LLM-vs-ODDPub
   head-to-head on availability-statement detection, calibrated on the PLOS Open Science
   Indicators dataset (~139k articles; DOI to be verified before use).
8. The data-vs-code asymmetry in predicting reproduction — our pilot finding has almost no
   direct literature (P5).
9. Citation fairness + accuracy + coverage + discourse assessed jointly on a CEM graph at
   single-paper granularity, with humanities-aware categories bridging the Hyland/Hellqvist
   tradition to the computational strands (P6).

## 7. Follow-up queue (not yet done)

- **Patch the lit-scout agent**: gate author rendering on author-list length (n=1 bare
  surname; n=2 "A & B"; n≥3 "et al."). Three runs' verifiers independently prescribed this.
- **Deeper-chaining go/no-gos** accumulated in each lit report (each gated on your
  approval); highest-value across the sweep: forward chains of Fraser 2023 and Thelwall
  2024 (nearest-competitor detection), Sarol 2025 references (citation-integrity
  toolchain), Serghiou 2021 citers (LLM-vs-rule-based detection), and Micropublications
  forward L2 (direct CEM competitors).
- **Dedicated arXiv/preprint sweep** for the 2025–26 citation-integrity and
  novelty-assessment work without CrossRef DOIs (RMC, NovBench, GhostCite, BibAgent,
  CiteGuard, ALCE lineage) and for LLM-era protocol extraction (P3's weakest recall).
- **Zotero imports**: each verified lit report carries an import-priority list; the
  staging importer dedups by DOI. Notable: the library holds none of the FAIR-validation
  or transparency-detection clusters — the two most load-bearing for the preregistered
  study's methods section.
- **Canonical-version substitutions** before citing: ODDPub journal version (Data Science
  Journal 2020 — the P5 lit run verified `10.5334/dsj-2020-042`); the SciScore
  Rigor-and-Transparency-Index *iScience* paper (DOI not yet verified).
- **BibTeX**: generated per lane in `/tmp/lit-scout-bibtex-*`; arXiv-DOI entries need
  import via arXiv ID instead.

## 8. Grant-relevant one-liners (all verifier-backed)

- "No published system performs end-to-end computational reproduction, FAIR assessment,
  and adversarial review for archaeology or the wider humanities and social sciences; the
  nearest analogues serve economics, psychology, and machine learning, and a majority of
  2026 'reproducibility assessment' tools do not execute code at all."
- "Automated FAIR evaluation is a crowded repository-side field whose own literature now
  calls for LLM-based assessment (Candela et al. 2024); no published work combines
  paper-side entry, LLM judgement of the full GO-FAIR sub-principle rubric, independent
  data/code scoring, and a HASS application."
- "The repliCATS Seven Signals have never been computed by an LLM from structured
  extractions; run-to-run stability is almost never reported as a reliability metric —
  our 25-run protocol is a methodological contribution in its own right."
- "This positioning is not self-assessed: every claim in the underlying landscape reports
  was re-verified against authoritative sources by independent fresh-context audit agents."
