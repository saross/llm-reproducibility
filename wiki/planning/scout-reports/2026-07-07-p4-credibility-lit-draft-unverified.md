# Scout report P4 (literature, UNVERIFIED DRAFT): credibility, repliCATS, and replication prediction

⚠ **VERIFICATION INCOMPLETE** — the lit-scout-verifier for this draft was terminated by the 2026-07-08 session usage limit early in its run. The proposer performed its own per-DOI Guard A grounding (all 35 DOIs resolved via lit-search.py metadata) and a 3-row self-check, but independent verification has NOT completed. Treat author/citation fields as provisional.

**To resume verification:** /lit-scout-verify /tmp/lit-scout-drafts/draft-20260707-233544-p4-credibility.md

---

All 175 claims verified and generated from grounded metadata. I have everything needed to compile the report. Here is my draft.

---

# Lit-scout draft: Assessment and prediction of research credibility/replicability — expert elicitation, machine prediction, and LLM-based approaches (with HASS emphasis)

⚠ **VERIFICATION PENDING** — this is a draft from the proposer (lit-scout). The `/lit-scout` slash command runs the `lit-scout-verifier` serial agent against this draft before returning the final output. If you are reading this marker in final output, verification failed — see the banner at top of the document.

## TL;DR

The field splits into five reasonably distinct conversations — human structured elicitation (repliCATS/IDEA, Melbourne), DARPA SCORE prediction markets and forecasting surveys, text/metadata machine-learning replicability prediction (the Uzzi group), a fast-growing 2024-2026 LLM-as-judge/LLM-prediction cluster, and a thin scatter of HASS/qualitative extensions — with the OSC (2015) and Camerer et al. (2018) replication datasets as the shared ground truth everyone predicts against. Top-3 must-reads for positioning: **Fraser et al. (2023)** repliCATS Seven Signals elicitation (`10.1371/journal.pone.0274429`), **Youyou et al. (2023)** discipline-wide text-based ML prediction (`10.1073/pnas.2208863120`), and **Thelwall et al. (2025)** implicit/explicit *repeated-run* research-quality score probabilities from ChatGPT (`10.1162/qss.a.393`) — the closest published analogue to your repeated-run LLM stability design. The biggest gap: **no published work computes repliCATS-style credibility *signals* with an LLM over a structured claims-evidence-methods extraction, none targets HASS/qualitative/fieldwork disciplines, and run-to-run stability is essentially never treated as an explicit reliability metric** — precisely the lane you are building.

## Findings table

| # | Fit | Cites | Authors (Year) | Title | DOI | Chain | Chains | Cluster | Status |
|---|-----|-------|----------------|-------|-----|-------|--------|---------|--------|
| 1 | HIGH | 17 | Fraser et al. (2023) | Predicting reliability through structured expert elicitation with the repliCATS process | 10.1371/journal.pone.0274429 | seed (S1) | 1 | A repliCATS/IDEA | NEW |
| 2 | HIGH | 393 | Hemming et al. (2018) | A practical guide to structured expert elicitation using the IDEA protocol | 10.1111/2041-210x.12857 | refs-of S1 | 1 | A repliCATS/IDEA | NEW |
| 3 | MEDIUM | 4 | Pearson et al. (2021) | Eliciting group judgements about replicability: a technical implementation of the IDEA Protocol | 10.24251/hicss.2021.055 | refs-of S1 | 1 | A repliCATS/IDEA | NEW |
| 4 | HIGH | 5 | Wintle et al. (2023) | Predicting and reasoning about replicability using structured groups | 10.1098/rsos.221553 | refs-of S1 | 2 | A repliCATS/IDEA | NEW |
| 5 | MEDIUM | 19 | Marcoci et al. (2022) | Reimagining peer review as an expert elicitation process | 10.1186/s13104-022-06016-0 | refs-of S1 | 2 | A repliCATS/IDEA | NEW |
| 6 | MEDIUM | 19 | Hanea et al. (2021) | Mathematically aggregating experts' predictions of possible futures | 10.1371/journal.pone.0256919 | refs-of S1 | 2 | A repliCATS/IDEA | NEW |
| 7 | HIGH | 5 | Nosek et al. (2026) | A framework for assessing the trustworthiness of scientific research findings | 10.1073/pnas.2536736123 | cited-by S1 | 1 | A repliCATS/IDEA | NEW |
| 8 | HIGH | 20 | Alipourfard et al. (2021) | Systematizing Confidence in Open Research and Evidence (SCORE) | 10.31235/osf.io/46mnb | refs-of S1 | 3 | B SCORE/markets | NEW |
| 9 | MEDIUM | 30 | Gordon et al. (2020) | Are replication rates the same across academic fields? Community forecasts from DARPA SCORE | 10.1098/rsos.200566 | seed (S5) | 3 | B SCORE/markets | NEW |
| 10 | MEDIUM | 210 | Dreber et al. (2015) | Using prediction markets to estimate the reproducibility of scientific research | 10.1073/pnas.1516179112 | seed (S3) | 4 | B SCORE/markets | NEW |
| 11 | MEDIUM | 28 | Gordon et al. (2021) | Predicting replicability—Analysis of survey and prediction market data from large-scale forecasting | 10.1371/journal.pone.0248780 | refs-of S7 | 3 | B SCORE/markets | NEW |
| 12 | HIGH | 4 | Marcoci et al. (2024) | Predicting the replicability of social and behavioural science claims in COVID-19 preprints | 10.1038/s41562-024-01961-1 | cited-by S1 | 1 | B SCORE/markets | NEW |
| 13 | MEDIUM | 13 | Holzmeister et al. (2024) | Examining the replicability of online experiments selected by a decision market | 10.1038/s41562-024-02062-9 | cited-by S7 | 1 | B SCORE/markets | NEW |
| 14 | MEDIUM | 8 | Brodeur et al. (2024) | Mass Reproducibility and Replicability: A New Hope | 10.2139/ssrn.4790780 | cited-by S1 | 1 | B SCORE/markets | NEW |
| 15 | HIGH | 79 | Yang et al. (2020) | Estimating the deep replicability of scientific findings using human and artificial intelligence | 10.1073/pnas.1909046117 | seed (S2) | 2 | C ML-text | NEW |
| 16 | HIGH | 65 | Youyou et al. (2023) | A discipline-wide investigation of the replicability of Psychology papers over the past two decades | 10.1073/pnas.2208863120 | seed (S7) | 2 | C ML-text | NEW |
| 17 | MEDIUM | 65 | Altmejd et al. (2019) | Predicting the replicability of social science lab experiments | 10.1371/journal.pone.0225826 | refs-of S1 | 3 | C ML-text | NEW |
| 18 | MEDIUM | 50 | Forsell et al. (2019) | Predicting replication outcomes in the Many Labs 2 study | 10.1016/j.joep.2018.10.009 | refs-of S2 | 3 | C ML-text | NEW |
| 19 | HIGH | 10 | Crockett et al. (2023) | The limitations of machine learning models for predicting scientific replicability | 10.1073/pnas.2307596120 | cited-by S7 | 1 | C ML-text | NEW |
| 20 | MEDIUM | 132 | Serra-Garcia et al. (2021) | Nonreplicable publications are cited more than replicable ones | 10.1126/sciadv.abd1705 | cited-by S2 | 3 | C ML-text | NEW |
| 21 | HIGH | 116 | Luo et al. (2024) | Large language models surpass human experts in predicting neuroscience results | 10.1038/s41562-024-02046-9 | seed (S4) | 0 | D LLM-judge | [IN ZOTERO] |
| 22 | HIGH | 168 | Liang et al. (2024) | Can Large Language Models Provide Useful Feedback on Research Papers? A Large-Scale Empirical Analysis | 10.1056/aioa2400196 | seed (S6) | 0 | D LLM-judge | NEW |
| 23 | HIGH | 11 | Lippert et al. (2024) | Can large language models help predict results from a complex behavioural science study? | 10.1098/rsos.240682 | cited-by S1 | 1 | D LLM-judge | NEW |
| 24 | HIGH | 58 | Thelwall (2024) | Can ChatGPT evaluate research quality? | 10.2478/jdis-2024-0013 | cited-by S6 | 1 | D LLM-judge | NEW |
| 25 | HIGH | 7 | Thelwall et al. (2025) | Implicit and explicit research quality score probabilities from ChatGPT | 10.1162/qss.a.393 | seed-search | 0 | D LLM-judge | NEW |
| 26 | MEDIUM | 21 | Thelwall (2025) | Is Google Gemini better than ChatGPT at evaluating research quality? | 10.2478/jdis-2025-0014 | seed-search | 0 | D LLM-judge | NEW |
| 27 | MEDIUM | 4 | Thelwall et al. (2026) | Can small and reasoning large language models score journal articles for research quality…? | 10.1007/s11192-026-05585-2 | seed-search | 0 | D LLM-judge | NEW |
| 28 | HIGH | 1 | Thompson et al. (2022) | Using prediction markets to estimate ratings of academic research quality in a mock REF exercise | 10.31222/osf.io/gsc8f | seed-search | 0 | E HASS/qual | NEW |
| 29 | MEDIUM | 14 | TalkadSukumar et al. (2019) | Replication and Transparency of Qualitative Research from a Constructivist Perspective | 10.31219/osf.io/6efvp | seed-search | 0 | E HASS/qual | NEW |
| 30 | MEDIUM | 28 | Freese et al. (2022) | Advances in transparency and reproducibility in the social sciences | 10.1016/j.ssresearch.2022.102770 | cited-by S5 | 1 | E HASS/qual | NEW |
| 31 | HIGH | 1 | Bellat (2026) | Recommendation of: Replication report for Marwick (2025) "Is archaeology a science?" | 10.24072/pci.archaeo.100616 | seed-search | 0 | E HASS/qual | NEW |
| 32 | MEDIUM | 1 | Singh et al. (2025) | Comparing expert assessments of research quality between the Global North and East Africa | 10.1098/rstb.2024.0275 | cited-by S1 | 1 | E HASS/qual | NEW |
| 33 | MEDIUM | 14 | Adler et al. (2023) | A toolbox to evaluate the trustworthiness of published findings | 10.1016/j.jbusres.2023.114189 | cited-by S7 | 1 | E HASS/qual | NEW |
| 34 | LOW | 5388 | Aarts (2015) [Open Science Collaboration] | Estimating the reproducibility of psychological science | 10.1126/science.aac4716 | refs (5 seeds) | 5 | F Benchmark | [IN ZOTERO] |
| 35 | MEDIUM | 1131 | Camerer et al. (2018) | Evaluating the replicability of social science experiments in Nature and Science 2010-2015 | 10.1038/s41562-018-0399-z | refs (5 seeds) | 5 | F Benchmark | [IN ZOTERO] |

Note on row 34: the `metadata` API returns a single author entry, `Alexander A. Aarts`, for what is canonically the *Open Science Collaboration* corporate author. The Authors value is grounded to the API response (`Aarts`); the corporate-author gloss is added for your recognition. The verifier may flag this as a partial match — that is expected and documented here.

## Proposer self-check

- **Tool availability:** The Scholar Gateway MCP tool (`mcp__claude_ai_Scholar_Gateway__semanticSearch`) and the Hugging Face MCP tools were **not available** in this environment (both returned "No such tool available"). Per methodology I compensated by running additional targeted OpenAlex/CrossRef/Semantic Scholar queries via `lit-search.py` plus WebSearch for grey literature. Because Scholar Gateway was not used, its known Wiley/Hindawi corpus bias did not enter the seed set; I nonetheless verified venue diversity independently (see Venue analysis — only 1 of 35 rows is a Wiley title).
- **Guard A self-check:** re-queried 3 random rows via fresh `metadata` calls — row 7 (Nosek et al., 2026, cites 5), row 19 (Crockett et al., 2023, cites 10), row 28 (Thompson et al., 2022, cites 1). All three matched `authors[0]` and `year` in the table. No drift detected; no rebuild required.
- **Grounding:** every Authors/Year/Cites/Title/DOI value in the table and the claims block was generated programmatically from the 35 individual `metadata` JSON responses (not from chain output or memory). Author labels use `authors[0]` surname verbatim + "et al." for multi-author works.
- **DOI resolution:** all 35 DOIs resolved and the returned DOI matched the queried DOI in every case (no DOI-diff).
- **Anomaly:** two Nature Human Behaviour COVID-preprint outputs exist as a near-pair — `10.1038/s41562-024-01961-1` (included, row 12) and `10.1038/s41562-024-01962-0` (the earlier-surfaced sibling, not separately tabled). They appear to be companion articles from the repliCATS/SCORE COVID-preprint effort; the verifier or your `/read` skill may wish to disambiguate.

## Landscape

The literature organises into five conversations plus a shared benchmark layer:

**A. repliCATS / IDEA structured expert elicitation (Melbourne; Fidler, Vazire, Hanea, Fraser, Wintle, Marcoci).** This is the direct parent tradition for your lane. The IDEA protocol (Investigate–Discuss–Estimate–Aggregate; Hemming et al. 2018, 393 cites) is the elicitation engine; Fraser et al. (2023) is the flagship repliCATS process paper and the origin of the **seven credibility signals** you are adapting (comprehensibility, transparency, plausibility, validity, robustness, replicability, generalisability). Wintle et al. (2023) is the most methodologically load-bearing recent piece on *reasoning* within structured groups. This cluster is human-elicitation-centric; **LLMs are essentially absent from it as of mid-2026** — that absence is your opening.

**B. DARPA SCORE, prediction markets and forecasting surveys (Dreber, Johannesson, Pfeiffer, Gordon, Nosek's COS).** The programmatic backbone. Dreber et al. (2015) established prediction markets for reproducibility; the SCORE overview (Alipourfard et al. 2021) frames the whole "confidence score" enterprise; Gordon et al. (2020, 2021) extend forecasts across fields and combine survey+market signals. Marcoci et al. (2024, NHB) is where SCORE/repliCATS methods meet a live, fast-turnaround corpus (COVID-19 preprints) — the closest *applied* analogue to a pipeline that must score fresh claims. This cluster is crowded and mature for biomedicine/psychology/economics.

**C. Machine-learning / text-based replicability prediction (Uzzi group — Yang, Youyou; plus the Dreber/Altmejd feature-based line).** Yang et al. (2020) and Youyou et al. (2023) are the canonical "predict replication from the paper's text/narrative" SOTA you must position against. Crockett et al. (2023, PNAS) is the essential **critical counterpoint** — it argues these models generalise poorly and may exploit confounds. Serra-Garcia & colleagues (2021) add the cautionary finding that non-replicable papers are cited *more*, so citation-based signals are treacherous.

**D. LLM-as-judge and LLM prediction of results/quality (2024-2026, exploding).** The newest and fastest-moving cluster. Two modes: (i) LLMs predicting *empirical outcomes* (Luo et al. 2024 BrainBench; Lippert et al. 2024), and (ii) LLMs scoring *research quality* (Liang et al. 2024 on peer-review feedback; the Thelwall series on ChatGPT/Gemini research-quality scoring against REF-style departmental scores). Thelwall et al. (2025, `10.1162/qss.a.393`) is singular for your design because it studies **repeated-run score *probabilities*** — the same reliability concern as your 25-run/96%-stability testing, though framed as quality scores, not credibility signals.

**E. HASS, qualitative and cross-domain research-quality assessment (thin, scattered).** No dense conversation yet. Thompson et al. (2022) runs prediction markets over a mock REF (the clearest HASS-adjacent quality-assessment precedent); TalkadSukumar & Metoyer (2019) and Freese et al. (2022) cover qualitative/social-science transparency; Bellat (2026) is a PCI Archaeology overlay recommendation on Marwick's replication report — **your own discipline**. Adler et al. (2023) offers a "trustworthiness toolbox" from marketing that is structurally similar to a signal checklist.

**F. Benchmark replication datasets (ground truth).** OSC (2015) and Camerer et al. (2018) are the labelled corpora nearly every prediction study trains/tests against. High centrality (5 chains each), but they are targets, not methods.

## Thematic clusters

| Cluster | Label | Members | Density read |
|---|---|---|---|
| A | repliCATS / IDEA structured elicitation | 7 (rows 1-7) | Dense, mature, human-only; the parent method |
| B | DARPA SCORE / prediction markets / forecasting | 7 (rows 8-14) | Dense, mature; biomedicine/psych/econ focus |
| C | ML/text-based replicability prediction | 6 (rows 15-20) | Moderately dense; a clear SOTA line + its critique |
| D | LLM-as-judge / LLM prediction of results & quality | 7 (rows 21-27) | Exploding 2024-2026; Thelwall sub-line is a near-monoculture (4 papers, one author group) |
| E | HASS / qualitative / cross-domain quality assessment | 6 (rows 28-33) | Sparse and heterogeneous — a topical frontier, not a conversation |
| F | Benchmark replication datasets | 2 (rows 34-35) | Ground truth, universally cited |

Cross-signal reading: the highest-*centrality* papers (OSC 2015, Camerer 2018, Dreber 2015 — 4-5 chains) are datasets/foundational methods, i.e. background you likely already know. The highest-*Fit* papers cluster in D and A and mostly have **low chain counts (0-1)** — they were surfaced by targeted seed-search and forward chains, not by dense back-citation, which is exactly what you'd expect for a frontier you are trying to enter: the work closest to your idea is too new to be structurally central yet.

## Suggested reading (tiered)

**Tier 1 — read first (direct positioning; HIGH Fit with specific argument):**

- **Fraser et al. (2023)** `10.1371/journal.pone.0274429` — the parent method. Defines the seven credibility signals and the IDEA-based elicitation your pipeline automates. Your contribution is legible only *relative* to this.
- **Thelwall et al. (2025)** `10.1162/qss.a.393` — closest published analogue to your **repeated-run stability** design: it treats ChatGPT quality scores as *probability distributions* over runs. Read for how they quantify and report run-to-run variability; you can directly contrast their quality-score target with your credibility-*signal* target.
- **Youyou et al. (2023)** `10.1073/pnas.2208863120` and **Yang et al. (2020)** `10.1073/pnas.1909046117` — the text-based ML SOTA. Argument served: these predict a *binary replication outcome* from text; you compute *multi-dimensional credibility signals* from a structured extraction — a different and arguably richer output. Cite to draw that contrast.
- **Crockett et al. (2023)** `10.1073/pnas.2307596120` — the limitations critique. Argument served: pre-empts the obvious reviewer objection ("ML replicability prediction doesn't generalise"). Your quality-gating + stability testing is partly a *response* to exactly this critique; internalise its evaluation standards.

**Tier 2 — evaluation & calibration practice (learn the methods):**

- **Liang et al. (2024)** `10.1056/aioa2400196` — the large-scale template for evaluating LLM judgements against human experts (overlap metrics, human-preference studies). HIGH Fit for your calibration chapter.
- **Luo et al. (2024)** `10.1038/s41562-024-02046-9` [IN ZOTERO] and **Lippert et al. (2024)** `10.1098/rsos.240682` — LLM prediction of empirical results with calibration/confidence analysis; the state of the art for "LLM vs expert" claims you will be compared against.
- **Gordon et al. (2021)** `10.1371/journal.pone.0248780` and **Hanea et al. (2021)** `10.1371/journal.pone.0256919` — how human forecasts and expert predictions are *aggregated* and calibrated; relevant to how you combine signals and runs.
- **Thelwall (2024)** `10.2478/jdis-2024-0013` — the foundational LLM-research-quality-scoring paper and its validation-against-REF approach.

**Tier 3 — HASS/discipline framing (highlight; your differentiator):**

- **Thompson et al. (2022)** `10.31222/osf.io/gsc8f` — research-quality assessment in a mock **REF** setting (HASS-relevant institutional context).
- **Bellat (2026)** `10.24072/pci.archaeo.100616` — replication in **archaeology** (your discipline); follow through to Marwick's underlying replication report via this overlay recommendation.
- **Singh et al. (2025)** `10.1098/rstb.2024.0275` — cross-context (Global North vs East Africa) expert quality assessment; useful for the equity/generalisability dimension of extending signals beyond WEIRD samples.
- **TalkadSukumar et al. (2019)** `10.31219/osf.io/6efvp` and **Freese et al. (2022)** `10.1016/j.ssresearch.2022.102770` — qualitative/social-science transparency framing.

**Tier 4 — context/background (LOW-MEDIUM Fit):**

- OSC (2015) `10.1126/science.aac4716` [IN ZOTERO] and Camerer et al. (2018) `10.1038/s41562-018-0399-z` [IN ZOTERO] — benchmark datasets.
- Dreber et al. (2015) `10.1073/pnas.1516179112`, Alipourfard et al. (2021) `10.31235/osf.io/46mnb`, Nosek et al. (2026) `10.1073/pnas.2536736123` — programmatic framing of the whole prediction-of-credibility enterprise.

## Gaps noticed

1. **The core gap (your lane):** no published work computes repliCATS-style credibility *signals* with an **LLM** over a **structured claims-evidence-methods extraction**. Cluster A uses human elicitation; Cluster C/D LLMs predict a *binary replication outcome* or a *scalar quality score*, not a multi-signal credibility profile. Your combination is, on this search, unoccupied.
2. **HASS / qualitative / fieldwork is nearly empty.** Every prediction/elicitation method above is validated on biomedicine, psychology or economics (against OSC/SCORE/Camerer corpora). There is no labelled replication corpus and no signal framework for archaeology, history or qualitative HASS. This is both a gap *and* a hard problem (no ground truth) — worth stating explicitly as a limitation you address by design (signals over binary replication).
3. **Run-to-run stability is almost never a reported metric.** Only Thelwall et al. (2025) treats repeated-run variability seriously, and as quality-score probabilities. Your 25-run/96%-verdict-stability protocol is a genuine methodological contribution to *LLM-as-assessor reliability* — frame it as such, not as an implementation detail.
4. **"LLM simulating an expert elicitation panel" is essentially unpublished.** Targeted searching for silicon-sampling / LLM-simulated panels applied to *credibility elicitation* returned only generic "LLMs as survey respondents" work, none applied to repliCATS-style deliberation. If you frame your pipeline as an *in-silico IDEA panel*, you are first-movers; worth a dedicated forward-chain (see Deeper chaining candidates).
5. **Quality-gating before assessment is not a named practice.** None of the LLM-as-judge papers gate on extraction quality before scoring; they score whatever they are given. Your quality gate is a differentiator worth naming and citing against Liang/Thelwall as an evaluation-hygiene advance.

## Venue analysis

The user did not name specific target venues, but explicitly asked *what is published (journals vs preprints)* and *how crowded each sub-area is* — addressed here.

- **Journals vs preprints/working papers:** 31 of 35 are peer-reviewed (journal or overlay); **4 are preprints/working papers** — SCORE overview (SocArXiv, `46mnb`), Brodeur et al. (SSRN, `4790780`), Thompson et al. (MetaArXiv mock-REF, `gsc8f`), TalkadSukumar et al. (OSF, `6efvp`). Note two of the most HASS-relevant items (mock-REF; qualitative) are **only** available as preprints — a signal that HASS-side quality/credibility-assessment work is under-published in journals.
- **Venue diversity (strong):** PNAS (×5), Nature Human Behaviour (×4), Royal Society Open Science (×3), PLoS ONE (×4), Science/Science Advances (×2), plus single appearances in NEJM AI, Quantitative Science Studies, Journal of Data and Information Science (×2), Scientometrics, Social Science Research, Journal of Business Research, Phil Trans R Soc B, BMC Research Notes, HICSS, Journal of Economic Psychology, Methods in Ecology & Evolution, and PCI Archaeology. **Only 1 of 35 (Methods Ecol. Evol.) is a Wiley title; zero Hindawi** — no corpus-bias skew.
- **Where to submit (inference, not from a named list):** the applied-methods + HASS angle fits *Royal Society Open Science*, *Quantitative Science Studies*, or *PLoS ONE* (all represented here and receptive to metascience + LLM-tooling); the archaeology-specific framing fits *Journal of Archaeological Science* / *PCI Archaeology* (per Bellat/Marwick). Confirm against your actual target list.

## Zotero actions

Papers marked NEW (32 of 35) are candidates for import after verification. Three are already held: Luo et al. 2024 (row 21, My Library), OSC 2015 (row 34, *Open Research (Archaeology)* library), and Camerer et al. 2018 (row 35, *Archaeology-reproducibility* library). Suggested tags on import: `credibility-assessment`, `replicability-prediction`, `LLM-as-judge` (rows 21-27), `repliCATS` (rows 1-7), `SCORE` (rows 8-14), `HASS` (rows 28-33). The staging importer (`scripts/lit-scout-zotero-import.py`) will re-dedup by DOI, so the three held items will be skipped automatically.

## Deeper chaining candidates

The following exceed the automatic depth (backward L1-2, forward L1) and need your go/no-go:

```text
DEEPER CHAINING CANDIDATES (go/no-go required):

1. FORWARD L2: Chase citations of Thelwall (2024) 10.2478/jdis-2024-0013 — the
   LLM-research-quality cluster is the fastest-growing and most Fit-relevant
   sub-area; its 2025-2026 forward chain likely surfaces the newest LLM-as-judge
   + calibration + HASS-quality work not yet structurally central. HIGH VALUE.

2. FORWARD L2: Chase citations of Fraser et al. (2023) 10.1371/journal.pone.0274429
   — recent (2024-2026) work building directly on the repliCATS seven-signals
   process; most likely place to find anyone already attempting LLM automation of
   the signals (i.e. your nearest competitors). HIGH VALUE.

3. BACKWARD L3: Chase references of Marcoci et al. (2024) 10.1038/s41562-024-01961-1
   — the COVID-preprint repliCATS/SCORE application; its reference list is the
   fullest single map of the repliCATS methods corpus + rapid-assessment tooling.
   MEDIUM VALUE.

4. BACKWARD L3: Chase references of Nosek et al. (2026) 10.1073/pnas.2536736123 —
   newest trustworthiness-framework synthesis; refs map the current consensus and
   may name signal frameworks competing with the seven signals. MEDIUM VALUE.

5. SKIP: Forward L2 of Luo et al. (2024) BrainBench 10.1038/s41562-024-02046-9 —
   its forward chain (inspected at L1) is dominated by applied "LLMs vs humans"
   work in unrelated domains (urban planning, cytology, food science); low
   signal-to-noise for credibility assessment.
```

## Machine-readable claims (for orchestrator extraction)

<!-- BEGIN claims.jsonl -->
```jsonl
{"claim_id": "10.1371-journal.pone.0274429-authors", "doi": "10.1371/journal.pone.0274429", "category": "authors", "description": "Authors for row 1", "value": "Fraser et al. (2023)", "source_method": "lit-search.py metadata", "source_file": "Findings table row 1"}
{"claim_id": "10.1371-journal.pone.0274429-year", "doi": "10.1371/journal.pone.0274429", "category": "year", "description": "Publication year for row 1", "value": 2023, "source_method": "lit-search.py metadata", "source_file": "Findings table row 1"}
{"claim_id": "10.1371-journal.pone.0274429-title", "doi": "10.1371/journal.pone.0274429", "category": "title", "description": "Title for row 1", "value": "Predicting reliability through structured expert elicitation with the repliCATS (Collaborative Assessments for Trustworthy Science) process", "source_method": "lit-search.py metadata", "source_file": "Findings table row 1"}
{"claim_id": "10.1371-journal.pone.0274429-citation_count", "doi": "10.1371/journal.pone.0274429", "category": "citation_count", "description": "Citation count for row 1", "value": 17, "source_method": "lit-search.py metadata", "source_file": "Findings table row 1"}
{"claim_id": "10.1371-journal.pone.0274429-doi_resolves", "doi": "10.1371/journal.pone.0274429", "category": "doi_resolves", "description": "DOI resolves to expected paper for row 1", "value": true, "source_method": "lit-search.py metadata", "source_file": "Findings table row 1"}
{"claim_id": "10.1111-2041-210x.12857-authors", "doi": "10.1111/2041-210x.12857", "category": "authors", "description": "Authors for row 2", "value": "Hemming et al. (2018)", "source_method": "lit-search.py metadata", "source_file": "Findings table row 2"}
{"claim_id": "10.1111-2041-210x.12857-year", "doi": "10.1111/2041-210x.12857", "category": "year", "description": "Publication year for row 2", "value": 2018, "source_method": "lit-search.py metadata", "source_file": "Findings table row 2"}
{"claim_id": "10.1111-2041-210x.12857-title", "doi": "10.1111/2041-210x.12857", "category": "title", "description": "Title for row 2", "value": "A practical guide to structured expert elicitation using the IDEA protocol", "source_method": "lit-search.py metadata", "source_file": "Findings table row 2"}
{"claim_id": "10.1111-2041-210x.12857-citation_count", "doi": "10.1111/2041-210x.12857", "category": "citation_count", "description": "Citation count for row 2", "value": 393, "source_method": "lit-search.py metadata", "source_file": "Findings table row 2"}
{"claim_id": "10.1111-2041-210x.12857-doi_resolves", "doi": "10.1111/2041-210x.12857", "category": "doi_resolves", "description": "DOI resolves to expected paper for row 2", "value": true, "source_method": "lit-search.py metadata", "source_file": "Findings table row 2"}
{"claim_id": "10.24251-hicss.2021.055-authors", "doi": "10.24251/hicss.2021.055", "category": "authors", "description": "Authors for row 3", "value": "Pearson et al. (2021)", "source_method": "lit-search.py metadata", "source_file": "Findings table row 3"}
{"claim_id": "10.24251-hicss.2021.055-year", "doi": "10.24251/hicss.2021.055", "category": "year", "description": "Publication year for row 3", "value": 2021, "source_method": "lit-search.py metadata", "source_file": "Findings table row 3"}
{"claim_id": "10.24251-hicss.2021.055-title", "doi": "10.24251/hicss.2021.055", "category": "title", "description": "Title for row 3", "value": "Eliciting group judgements about replicability: a technical implementation of the IDEA Protocol", "source_method": "lit-search.py metadata", "source_file": "Findings table row 3"}
{"claim_id": "10.24251-hicss.2021.055-citation_count", "doi": "10.24251/hicss.2021.055", "category": "citation_count", "description": "Citation count for row 3", "value": 4, "source_method": "lit-search.py metadata", "source_file": "Findings table row 3"}
{"claim_id": "10.24251-hicss.2021.055-doi_resolves", "doi": "10.24251/hicss.2021.055", "category": "doi_resolves", "description": "DOI resolves to expected paper for row 3", "value": true, "source_method": "lit-search.py metadata", "source_file": "Findings table row 3"}
{"claim_id": "10.1098-rsos.221553-authors", "doi": "10.1098/rsos.221553", "category": "authors", "description": "Authors for row 4", "value": "Wintle et al. (2023)", "source_method": "lit-search.py metadata", "source_file": "Findings table row 4"}
{"claim_id": "10.1098-rsos.221553-year", "doi": "10.1098/rsos.221553", "category": "year", "description": "Publication year for row 4", "value": 2023, "source_method": "lit-search.py metadata", "source_file": "Findings table row 4"}
{"claim_id": "10.1098-rsos.221553-title", "doi": "10.1098/rsos.221553", "category": "title", "description": "Title for row 4", "value": "Predicting and reasoning about replicability using structured groups", "source_method": "lit-search.py metadata", "source_file": "Findings table row 4"}
{"claim_id": "10.1098-rsos.221553-citation_count", "doi": "10.1098/rsos.221553", "category": "citation_count", "description": "Citation count for row 4", "value": 5, "source_method": "lit-search.py metadata", "source_file": "Findings table row 4"}
{"claim_id": "10.1098-rsos.221553-doi_resolves", "doi": "10.1098/rsos.221553", "category": "doi_resolves", "description": "DOI resolves to expected paper for row 4", "value": true, "source_method": "lit-search.py metadata", "source_file": "Findings table row 4"}
{"claim_id": "10.1186-s13104-022-06016-0-authors", "doi": "10.1186/s13104-022-06016-0", "category": "authors", "description": "Authors for row 5", "value": "Marcoci et al. (2022)", "source_method": "lit-search.py metadata", "source_file": "Findings table row 5"}
{"claim_id": "10.1186-s13104-022-06016-0-year", "doi": "10.1186/s13104-022-06016-0", "category": "year", "description": "Publication year for row 5", "value": 2022, "source_method": "lit-search.py metadata", "source_file": "Findings table row 5"}
{"claim_id": "10.1186-s13104-022-06016-0-title", "doi": "10.1186/s13104-022-06016-0", "category": "title", "description": "Title for row 5", "value": "Reimagining peer review as an expert elicitation process", "source_method": "lit-search.py metadata", "source_file": "Findings table row 5"}
{"claim_id": "10.1186-s13104-022-06016-0-citation_count", "doi": "10.1186/s13104-022-06016-0", "category": "citation_count", "description": "Citation count for row 5", "value": 19, "source_method": "lit-search.py metadata", "source_file": "Findings table row 5"}
{"claim_id": "10.1186-s13104-022-06016-0-doi_resolves", "doi": "10.1186/s13104-022-06016-0", "category": "doi_resolves", "description": "DOI resolves to expected paper for row 5", "value": true, "source_method": "lit-search.py metadata", "source_file": "Findings table row 5"}
{"claim_id": "10.1371-journal.pone.0256919-authors", "doi": "10.1371/journal.pone.0256919", "category": "authors", "description": "Authors for row 6", "value": "Hanea et al. (2021)", "source_method": "lit-search.py metadata", "source_file": "Findings table row 6"}
{"claim_id": "10.1371-journal.pone.0256919-year", "doi": "10.1371/journal.pone.0256919", "category": "year", "description": "Publication year for row 6", "value": 2021, "source_method": "lit-search.py metadata", "source_file": "Findings table row 6"}
{"claim_id": "10.1371-journal.pone.0256919-title", "doi": "10.1371/journal.pone.0256919", "category": "title", "description": "Title for row 6", "value": "Mathematically aggregating experts’ predictions of possible futures", "source_method": "lit-search.py metadata", "source_file": "Findings table row 6"}
{"claim_id": "10.1371-journal.pone.0256919-citation_count", "doi": "10.1371/journal.pone.0256919", "category": "citation_count", "description": "Citation count for row 6", "value": 19, "source_method": "lit-search.py metadata", "source_file": "Findings table row 6"}
{"claim_id": "10.1371-journal.pone.0256919-doi_resolves", "doi": "10.1371/journal.pone.0256919", "category": "doi_resolves", "description": "DOI resolves to expected paper for row 6", "value": true, "source_method": "lit-search.py metadata", "source_file": "Findings table row 6"}
{"claim_id": "10.1073-pnas.2536736123-authors", "doi": "10.1073/pnas.2536736123", "category": "authors", "description": "Authors for row 7", "value": "Nosek et al. (2026)", "source_method": "lit-search.py metadata", "source_file": "Findings table row 7"}
{"claim_id": "10.1073-pnas.2536736123-year", "doi": "10.1073/pnas.2536736123", "category": "year", "description": "Publication year for row 7", "value": 2026, "source_method": "lit-search.py metadata", "source_file": "Findings table row 7"}
{"claim_id": "10.1073-pnas.2536736123-title", "doi": "10.1073/pnas.2536736123", "category": "title", "description": "Title for row 7", "value": "A framework for assessing the trustworthiness of scientific research findings", "source_method": "lit-search.py metadata", "source_file": "Findings table row 7"}
{"claim_id": "10.1073-pnas.2536736123-citation_count", "doi": "10.1073/pnas.2536736123", "category": "citation_count", "description": "Citation count for row 7", "value": 5, "source_method": "lit-search.py metadata", "source_file": "Findings table row 7"}
{"claim_id": "10.1073-pnas.2536736123-doi_resolves", "doi": "10.1073/pnas.2536736123", "category": "doi_resolves", "description": "DOI resolves to expected paper for row 7", "value": true, "source_method": "lit-search.py metadata", "source_file": "Findings table row 7"}
{"claim_id": "10.31235-osf.io-46mnb-authors", "doi": "10.31235/osf.io/46mnb", "category": "authors", "description": "Authors for row 8", "value": "Alipourfard et al. (2021)", "source_method": "lit-search.py metadata", "source_file": "Findings table row 8"}
{"claim_id": "10.31235-osf.io-46mnb-year", "doi": "10.31235/osf.io/46mnb", "category": "year", "description": "Publication year for row 8", "value": 2021, "source_method": "lit-search.py metadata", "source_file": "Findings table row 8"}
{"claim_id": "10.31235-osf.io-46mnb-title", "doi": "10.31235/osf.io/46mnb", "category": "title", "description": "Title for row 8", "value": "Systematizing Confidence in Open Research and Evidence (SCORE)", "source_method": "lit-search.py metadata", "source_file": "Findings table row 8"}
{"claim_id": "10.31235-osf.io-46mnb-citation_count", "doi": "10.31235/osf.io/46mnb", "category": "citation_count", "description": "Citation count for row 8", "value": 20, "source_method": "lit-search.py metadata", "source_file": "Findings table row 8"}
{"claim_id": "10.31235-osf.io-46mnb-doi_resolves", "doi": "10.31235/osf.io/46mnb", "category": "doi_resolves", "description": "DOI resolves to expected paper for row 8", "value": true, "source_method": "lit-search.py metadata", "source_file": "Findings table row 8"}
{"claim_id": "10.1098-rsos.200566-authors", "doi": "10.1098/rsos.200566", "category": "authors", "description": "Authors for row 9", "value": "Gordon et al. (2020)", "source_method": "lit-search.py metadata", "source_file": "Findings table row 9"}
{"claim_id": "10.1098-rsos.200566-year", "doi": "10.1098/rsos.200566", "category": "year", "description": "Publication year for row 9", "value": 2020, "source_method": "lit-search.py metadata", "source_file": "Findings table row 9"}
{"claim_id": "10.1098-rsos.200566-title", "doi": "10.1098/rsos.200566", "category": "title", "description": "Title for row 9", "value": "Are replication rates the same across academic fields? Community forecasts from the DARPA SCORE programme", "source_method": "lit-search.py metadata", "source_file": "Findings table row 9"}
{"claim_id": "10.1098-rsos.200566-citation_count", "doi": "10.1098/rsos.200566", "category": "citation_count", "description": "Citation count for row 9", "value": 30, "source_method": "lit-search.py metadata", "source_file": "Findings table row 9"}
{"claim_id": "10.1098-rsos.200566-doi_resolves", "doi": "10.1098/rsos.200566", "category": "doi_resolves", "description": "DOI resolves to expected paper for row 9", "value": true, "source_method": "lit-search.py metadata", "source_file": "Findings table row 9"}
{"claim_id": "10.1073-pnas.1516179112-authors", "doi": "10.1073/pnas.1516179112", "category": "authors", "description": "Authors for row 10", "value": "Dreber et al. (2015)", "source_method": "lit-search.py metadata", "source_file": "Findings table row 10"}
{"claim_id": "10.1073-pnas.1516179112-year", "doi": "10.1073/pnas.1516179112", "category": "year", "description": "Publication year for row 10", "value": 2015, "source_method": "lit-search.py metadata", "source_file": "Findings table row 10"}
{"claim_id": "10.1073-pnas.1516179112-title", "doi": "10.1073/pnas.1516179112", "category": "title", "description": "Title for row 10", "value": "Using prediction markets to estimate the reproducibility of scientific research", "source_method": "lit-search.py metadata", "source_file": "Findings table row 10"}
{"claim_id": "10.1073-pnas.1516179112-citation_count", "doi": "10.1073/pnas.1516179112", "category": "citation_count", "description": "Citation count for row 10", "value": 210, "source_method": "lit-search.py metadata", "source_file": "Findings table row 10"}
{"claim_id": "10.1073-pnas.1516179112-doi_resolves", "doi": "10.1073/pnas.1516179112", "category": "doi_resolves", "description": "DOI resolves to expected paper for row 10", "value": true, "source_method": "lit-search.py metadata", "source_file": "Findings table row 10"}
{"claim_id": "10.1371-journal.pone.0248780-authors", "doi": "10.1371/journal.pone.0248780", "category": "authors", "description": "Authors for row 11", "value": "Gordon et al. (2021)", "source_method": "lit-search.py metadata", "source_file": "Findings table row 11"}
{"claim_id": "10.1371-journal.pone.0248780-year", "doi": "10.1371/journal.pone.0248780", "category": "year", "description": "Publication year for row 11", "value": 2021, "source_method": "lit-search.py metadata", "source_file": "Findings table row 11"}
{"claim_id": "10.1371-journal.pone.0248780-title", "doi": "10.1371/journal.pone.0248780", "category": "title", "description": "Title for row 11", "value": "Predicting replicability—Analysis of survey and prediction market data from large-scale forecasting projects", "source_method": "lit-search.py metadata", "source_file": "Findings table row 11"}
{"claim_id": "10.1371-journal.pone.0248780-citation_count", "doi": "10.1371/journal.pone.0248780", "category": "citation_count", "description": "Citation count for row 11", "value": 28, "source_method": "lit-search.py metadata", "source_file": "Findings table row 11"}
{"claim_id": "10.1371-journal.pone.0248780-doi_resolves", "doi": "10.1371/journal.pone.0248780", "category": "doi_resolves", "description": "DOI resolves to expected paper for row 11", "value": true, "source_method": "lit-search.py metadata", "source_file": "Findings table row 11"}
{"claim_id": "10.1038-s41562-024-01961-1-authors", "doi": "10.1038/s41562-024-01961-1", "category": "authors", "description": "Authors for row 12", "value": "Marcoci et al. (2024)", "source_method": "lit-search.py metadata", "source_file": "Findings table row 12"}
{"claim_id": "10.1038-s41562-024-01961-1-year", "doi": "10.1038/s41562-024-01961-1", "category": "year", "description": "Publication year for row 12", "value": 2024, "source_method": "lit-search.py metadata", "source_file": "Findings table row 12"}
{"claim_id": "10.1038-s41562-024-01961-1-title", "doi": "10.1038/s41562-024-01961-1", "category": "title", "description": "Title for row 12", "value": "Predicting the replicability of social and behavioural science claims in COVID-19 preprints", "source_method": "lit-search.py metadata", "source_file": "Findings table row 12"}
{"claim_id": "10.1038-s41562-024-01961-1-citation_count", "doi": "10.1038/s41562-024-01961-1", "category": "citation_count", "description": "Citation count for row 12", "value": 4, "source_method": "lit-search.py metadata", "source_file": "Findings table row 12"}
{"claim_id": "10.1038-s41562-024-01961-1-doi_resolves", "doi": "10.1038/s41562-024-01961-1", "category": "doi_resolves", "description": "DOI resolves to expected paper for row 12", "value": true, "source_method": "lit-search.py metadata", "source_file": "Findings table row 12"}
{"claim_id": "10.1038-s41562-024-02062-9-authors", "doi": "10.1038/s41562-024-02062-9", "category": "authors", "description": "Authors for row 13", "value": "Holzmeister et al. (2024)", "source_method": "lit-search.py metadata", "source_file": "Findings table row 13"}
{"claim_id": "10.1038-s41562-024-02062-9-year", "doi": "10.1038/s41562-024-02062-9", "category": "year", "description": "Publication year for row 13", "value": 2024, "source_method": "lit-search.py metadata", "source_file": "Findings table row 13"}
{"claim_id": "10.1038-s41562-024-02062-9-title", "doi": "10.1038/s41562-024-02062-9", "category": "title", "description": "Title for row 13", "value": "Examining the replicability of online experiments selected by a decision market", "source_method": "lit-search.py metadata", "source_file": "Findings table row 13"}
{"claim_id": "10.1038-s41562-024-02062-9-citation_count", "doi": "10.1038/s41562-024-02062-9", "category": "citation_count", "description": "Citation count for row 13", "value": 13, "source_method": "lit-search.py metadata", "source_file": "Findings table row 13"}
{"claim_id": "10.1038-s41562-024-02062-9-doi_resolves", "doi": "10.1038/s41562-024-02062-9", "category": "doi_resolves", "description": "DOI resolves to expected paper for row 13", "value": true, "source_method": "lit-search.py metadata", "source_file": "Findings table row 13"}
{"claim_id": "10.2139-ssrn.4790780-authors", "doi": "10.2139/ssrn.4790780", "category": "authors", "description": "Authors for row 14", "value": "Brodeur et al. (2024)", "source_method": "lit-search.py metadata", "source_file": "Findings table row 14"}
{"claim_id": "10.2139-ssrn.4790780-year", "doi": "10.2139/ssrn.4790780", "category": "year", "description": "Publication year for row 14", "value": 2024, "source_method": "lit-search.py metadata", "source_file": "Findings table row 14"}
{"claim_id": "10.2139-ssrn.4790780-title", "doi": "10.2139/ssrn.4790780", "category": "title", "description": "Title for row 14", "value": "Mass Reproducibility and Replicability: A New Hope", "source_method": "lit-search.py metadata", "source_file": "Findings table row 14"}
{"claim_id": "10.2139-ssrn.4790780-citation_count", "doi": "10.2139/ssrn.4790780", "category": "citation_count", "description": "Citation count for row 14", "value": 8, "source_method": "lit-search.py metadata", "source_file": "Findings table row 14"}
{"claim_id": "10.2139-ssrn.4790780-doi_resolves", "doi": "10.2139/ssrn.4790780", "category": "doi_resolves", "description": "DOI resolves to expected paper for row 14", "value": true, "source_method": "lit-search.py metadata", "source_file": "Findings table row 14"}
{"claim_id": "10.1073-pnas.1909046117-authors", "doi": "10.1073/pnas.1909046117", "category": "authors", "description": "Authors for row 15", "value": "Yang et al. (2020)", "source_method": "lit-search.py metadata", "source_file": "Findings table row 15"}
{"claim_id": "10.1073-pnas.1909046117-year", "doi": "10.1073/pnas.1909046117", "category": "year", "description": "Publication year for row 15", "value": 2020, "source_method": "lit-search.py metadata", "source_file": "Findings table row 15"}
{"claim_id": "10.1073-pnas.1909046117-title", "doi": "10.1073/pnas.1909046117", "category": "title", "description": "Title for row 15", "value": "Estimating the deep replicability of scientific findings using human and artificial intelligence", "source_method": "lit-search.py metadata", "source_file": "Findings table row 15"}
{"claim_id": "10.1073-pnas.1909046117-citation_count", "doi": "10.1073/pnas.1909046117", "category": "citation_count", "description": "Citation count for row 15", "value": 79, "source_method": "lit-search.py metadata", "source_file": "Findings table row 15"}
{"claim_id": "10.1073-pnas.1909046117-doi_resolves", "doi": "10.1073/pnas.1909046117", "category": "doi_resolves", "description": "DOI resolves to expected paper for row 15", "value": true, "source_method": "lit-search.py metadata", "source_file": "Findings table row 15"}
{"claim_id": "10.1073-pnas.2208863120-authors", "doi": "10.1073/pnas.2208863120", "category": "authors", "description": "Authors for row 16", "value": "Youyou et al. (2023)", "source_method": "lit-search.py metadata", "source_file": "Findings table row 16"}
{"claim_id": "10.1073-pnas.2208863120-year", "doi": "10.1073/pnas.2208863120", "category": "year", "description": "Publication year for row 16", "value": 2023, "source_method": "lit-search.py metadata", "source_file": "Findings table row 16"}
{"claim_id": "10.1073-pnas.2208863120-title", "doi": "10.1073/pnas.2208863120", "category": "title", "description": "Title for row 16", "value": "A discipline-wide investigation of the replicability of Psychology papers over the past two decades", "source_method": "lit-search.py metadata", "source_file": "Findings table row 16"}
{"claim_id": "10.1073-pnas.2208863120-citation_count", "doi": "10.1073/pnas.2208863120", "category": "citation_count", "description": "Citation count for row 16", "value": 65, "source_method": "lit-search.py metadata", "source_file": "Findings table row 16"}
{"claim_id": "10.1073-pnas.2208863120-doi_resolves", "doi": "10.1073/pnas.2208863120", "category": "doi_resolves", "description": "DOI resolves to expected paper for row 16", "value": true, "source_method": "lit-search.py metadata", "source_file": "Findings table row 16"}
{"claim_id": "10.1371-journal.pone.0225826-authors", "doi": "10.1371/journal.pone.0225826", "category": "authors", "description": "Authors for row 17", "value": "Altmejd et al. (2019)", "source_method": "lit-search.py metadata", "source_file": "Findings table row 17"}
{"claim_id": "10.1371-journal.pone.0225826-year", "doi": "10.1371/journal.pone.0225826", "category": "year", "description": "Publication year for row 17", "value": 2019, "source_method": "lit-search.py metadata", "source_file": "Findings table row 17"}
{"claim_id": "10.1371-journal.pone.0225826-title", "doi": "10.1371/journal.pone.0225826", "category": "title", "description": "Title for row 17", "value": "Predicting the replicability of social science lab experiments", "source_method": "lit-search.py metadata", "source_file": "Findings table row 17"}
{"claim_id": "10.1371-journal.pone.0225826-citation_count", "doi": "10.1371/journal.pone.0225826", "category": "citation_count", "description": "Citation count for row 17", "value": 65, "source_method": "lit-search.py metadata", "source_file": "Findings table row 17"}
{"claim_id": "10.1371-journal.pone.0225826-doi_resolves", "doi": "10.1371/journal.pone.0225826", "category": "doi_resolves", "description": "DOI resolves to expected paper for row 17", "value": true, "source_method": "lit-search.py metadata", "source_file": "Findings table row 17"}
{"claim_id": "10.1016-j.joep.2018.10.009-authors", "doi": "10.1016/j.joep.2018.10.009", "category": "authors", "description": "Authors for row 18", "value": "Forsell et al. (2019)", "source_method": "lit-search.py metadata", "source_file": "Findings table row 18"}
{"claim_id": "10.1016-j.joep.2018.10.009-year", "doi": "10.1016/j.joep.2018.10.009", "category": "year", "description": "Publication year for row 18", "value": 2019, "source_method": "lit-search.py metadata", "source_file": "Findings table row 18"}
{"claim_id": "10.1016-j.joep.2018.10.009-title", "doi": "10.1016/j.joep.2018.10.009", "category": "title", "description": "Title for row 18", "value": "Predicting replication outcomes in the Many Labs 2 study", "source_method": "lit-search.py metadata", "source_file": "Findings table row 18"}
{"claim_id": "10.1016-j.joep.2018.10.009-citation_count", "doi": "10.1016/j.joep.2018.10.009", "category": "citation_count", "description": "Citation count for row 18", "value": 50, "source_method": "lit-search.py metadata", "source_file": "Findings table row 18"}
{"claim_id": "10.1016-j.joep.2018.10.009-doi_resolves", "doi": "10.1016/j.joep.2018.10.009", "category": "doi_resolves", "description": "DOI resolves to expected paper for row 18", "value": true, "source_method": "lit-search.py metadata", "source_file": "Findings table row 18"}
{"claim_id": "10.1073-pnas.2307596120-authors", "doi": "10.1073/pnas.2307596120", "category": "authors", "description": "Authors for row 19", "value": "Crockett et al. (2023)", "source_method": "lit-search.py metadata", "source_file": "Findings table row 19"}
{"claim_id": "10.1073-pnas.2307596120-year", "doi": "10.1073/pnas.2307596120", "category": "year", "description": "Publication year for row 19", "value": 2023, "source_method": "lit-search.py metadata", "source_file": "Findings table row 19"}
{"claim_id": "10.1073-pnas.2307596120-title", "doi": "10.1073/pnas.2307596120", "category": "title", "description": "Title for row 19", "value": "The limitations of machine learning models for predicting scientific replicability", "source_method": "lit-search.py metadata", "source_file": "Findings table row 19"}
{"claim_id": "10.1073-pnas.2307596120-citation_count", "doi": "10.1073/pnas.2307596120", "category": "citation_count", "description": "Citation count for row 19", "value": 10, "source_method": "lit-search.py metadata", "source_file": "Findings table row 19"}
{"claim_id": "10.1073-pnas.2307596120-doi_resolves", "doi": "10.1073/pnas.2307596120", "category": "doi_resolves", "description": "DOI resolves to expected paper for row 19", "value": true, "source_method": "lit-search.py metadata", "source_file": "Findings table row 19"}
{"claim_id": "10.1126-sciadv.abd1705-authors", "doi": "10.1126/sciadv.abd1705", "category": "authors", "description": "Authors for row 20", "value": "Serra-Garcia et al. (2021)", "source_method": "lit-search.py metadata", "source_file": "Findings table row 20"}
{"claim_id": "10.1126-sciadv.abd1705-year", "doi": "10.1126/sciadv.abd1705", "category": "year", "description": "Publication year for row 20", "value": 2021, "source_method": "lit-search.py metadata", "source_file": "Findings table row 20"}
{"claim_id": "10.1126-sciadv.abd1705-title", "doi": "10.1126/sciadv.abd1705", "category": "title", "description": "Title for row 20", "value": "Nonreplicable publications are cited more than replicable ones", "source_method": "lit-search.py metadata", "source_file": "Findings table row 20"}
{"claim_id": "10.1126-sciadv.abd1705-citation_count", "doi": "10.1126/sciadv.abd1705", "category": "citation_count", "description": "Citation count for row 20", "value": 132, "source_method": "lit-search.py metadata", "source_file": "Findings table row 20"}
{"claim_id": "10.1126-sciadv.abd1705-doi_resolves", "doi": "10.1126/sciadv.abd1705", "category": "doi_resolves", "description": "DOI resolves to expected paper for row 20", "value": true, "source_method": "lit-search.py metadata", "source_file": "Findings table row 20"}
{"claim_id": "10.1038-s41562-024-02046-9-authors", "doi": "10.1038/s41562-024-02046-9", "category": "authors", "description": "Authors for row 21", "value": "Luo et al. (2024)", "source_method": "lit-search.py metadata", "source_file": "Findings table row 21"}
{"claim_id": "10.1038-s41562-024-02046-9-year", "doi": "10.1038/s41562-024-02046-9", "category": "year", "description": "Publication year for row 21", "value": 2024, "source_method": "lit-search.py metadata", "source_file": "Findings table row 21"}
{"claim_id": "10.1038-s41562-024-02046-9-title", "doi": "10.1038/s41562-024-02046-9", "category": "title", "description": "Title for row 21", "value": "Large language models surpass human experts in predicting neuroscience results", "source_method": "lit-search.py metadata", "source_file": "Findings table row 21"}
{"claim_id": "10.1038-s41562-024-02046-9-citation_count", "doi": "10.1038/s41562-024-02046-9", "category": "citation_count", "description": "Citation count for row 21", "value": 116, "source_method": "lit-search.py metadata", "source_file": "Findings table row 21"}
{"claim_id": "10.1038-s41562-024-02046-9-doi_resolves", "doi": "10.1038/s41562-024-02046-9", "category": "doi_resolves", "description": "DOI resolves to expected paper for row 21", "value": true, "source_method": "lit-search.py metadata", "source_file": "Findings table row 21"}
{"claim_id": "10.1056-aioa2400196-authors", "doi": "10.1056/aioa2400196", "category": "authors", "description": "Authors for row 22", "value": "Liang et al. (2024)", "source_method": "lit-search.py metadata", "source_file": "Findings table row 22"}
{"claim_id": "10.1056-aioa2400196-year", "doi": "10.1056/aioa2400196", "category": "year", "description": "Publication year for row 22", "value": 2024, "source_method": "lit-search.py metadata", "source_file": "Findings table row 22"}
{"claim_id": "10.1056-aioa2400196-title", "doi": "10.1056/aioa2400196", "category": "title", "description": "Title for row 22", "value": "Can Large Language Models Provide Useful Feedback on Research Papers? A Large-Scale Empirical Analysis", "source_method": "lit-search.py metadata", "source_file": "Findings table row 22"}
{"claim_id": "10.1056-aioa2400196-citation_count", "doi": "10.1056/aioa2400196", "category": "citation_count", "description": "Citation count for row 22", "value": 168, "source_method": "lit-search.py metadata", "source_file": "Findings table row 22"}
{"claim_id": "10.1056-aioa2400196-doi_resolves", "doi": "10.1056/aioa2400196", "category": "doi_resolves", "description": "DOI resolves to expected paper for row 22", "value": true, "source_method": "lit-search.py metadata", "source_file": "Findings table row 22"}
{"claim_id": "10.1098-rsos.240682-authors", "doi": "10.1098/rsos.240682", "category": "authors", "description": "Authors for row 23", "value": "Lippert et al. (2024)", "source_method": "lit-search.py metadata", "source_file": "Findings table row 23"}
{"claim_id": "10.1098-rsos.240682-year", "doi": "10.1098/rsos.240682", "category": "year", "description": "Publication year for row 23", "value": 2024, "source_method": "lit-search.py metadata", "source_file": "Findings table row 23"}
{"claim_id": "10.1098-rsos.240682-title", "doi": "10.1098/rsos.240682", "category": "title", "description": "Title for row 23", "value": "Can large language models help predict results from a complex behavioural science study?", "source_method": "lit-search.py metadata", "source_file": "Findings table row 23"}
{"claim_id": "10.1098-rsos.240682-citation_count", "doi": "10.1098/rsos.240682", "category": "citation_count", "description": "Citation count for row 23", "value": 11, "source_method": "lit-search.py metadata", "source_file": "Findings table row 23"}
{"claim_id": "10.1098-rsos.240682-doi_resolves", "doi": "10.1098/rsos.240682", "category": "doi_resolves", "description": "DOI resolves to expected paper for row 23", "value": true, "source_method": "lit-search.py metadata", "source_file": "Findings table row 23"}
{"claim_id": "10.2478-jdis-2024-0013-authors", "doi": "10.2478/jdis-2024-0013", "category": "authors", "description": "Authors for row 24", "value": "Thelwall (2024)", "source_method": "lit-search.py metadata", "source_file": "Findings table row 24"}
{"claim_id": "10.2478-jdis-2024-0013-year", "doi": "10.2478/jdis-2024-0013", "category": "year", "description": "Publication year for row 24", "value": 2024, "source_method": "lit-search.py metadata", "source_file": "Findings table row 24"}
{"claim_id": "10.2478-jdis-2024-0013-title", "doi": "10.2478/jdis-2024-0013", "category": "title", "description": "Title for row 24", "value": "Can ChatGPT evaluate research quality?", "source_method": "lit-search.py metadata", "source_file": "Findings table row 24"}
{"claim_id": "10.2478-jdis-2024-0013-citation_count", "doi": "10.2478/jdis-2024-0013", "category": "citation_count", "description": "Citation count for row 24", "value": 58, "source_method": "lit-search.py metadata", "source_file": "Findings table row 24"}
{"claim_id": "10.2478-jdis-2024-0013-doi_resolves", "doi": "10.2478/jdis-2024-0013", "category": "doi_resolves", "description": "DOI resolves to expected paper for row 24", "value": true, "source_method": "lit-search.py metadata", "source_file": "Findings table row 24"}
{"claim_id": "10.1162-qss.a.393-authors", "doi": "10.1162/qss.a.393", "category": "authors", "description": "Authors for row 25", "value": "Thelwall et al. (2025)", "source_method": "lit-search.py metadata", "source_file": "Findings table row 25"}
{"claim_id": "10.1162-qss.a.393-year", "doi": "10.1162/qss.a.393", "category": "year", "description": "Publication year for row 25", "value": 2025, "source_method": "lit-search.py metadata", "source_file": "Findings table row 25"}
{"claim_id": "10.1162-qss.a.393-title", "doi": "10.1162/qss.a.393", "category": "title", "description": "Title for row 25", "value": "Implicit and explicit research quality score probabilities from ChatGPT", "source_method": "lit-search.py metadata", "source_file": "Findings table row 25"}
{"claim_id": "10.1162-qss.a.393-citation_count", "doi": "10.1162/qss.a.393", "category": "citation_count", "description": "Citation count for row 25", "value": 7, "source_method": "lit-search.py metadata", "source_file": "Findings table row 25"}
{"claim_id": "10.1162-qss.a.393-doi_resolves", "doi": "10.1162/qss.a.393", "category": "doi_resolves", "description": "DOI resolves to expected paper for row 25", "value": true, "source_method": "lit-search.py metadata", "source_file": "Findings table row 25"}
{"claim_id": "10.2478-jdis-2025-0014-authors", "doi": "10.2478/jdis-2025-0014", "category": "authors", "description": "Authors for row 26", "value": "Thelwall (2025)", "source_method": "lit-search.py metadata", "source_file": "Findings table row 26"}
{"claim_id": "10.2478-jdis-2025-0014-year", "doi": "10.2478/jdis-2025-0014", "category": "year", "description": "Publication year for row 26", "value": 2025, "source_method": "lit-search.py metadata", "source_file": "Findings table row 26"}
{"claim_id": "10.2478-jdis-2025-0014-title", "doi": "10.2478/jdis-2025-0014", "category": "title", "description": "Title for row 26", "value": "Is Google Gemini better than ChatGPT at evaluating research quality?", "source_method": "lit-search.py metadata", "source_file": "Findings table row 26"}
{"claim_id": "10.2478-jdis-2025-0014-citation_count", "doi": "10.2478/jdis-2025-0014", "category": "citation_count", "description": "Citation count for row 26", "value": 21, "source_method": "lit-search.py metadata", "source_file": "Findings table row 26"}
{"claim_id": "10.2478-jdis-2025-0014-doi_resolves", "doi": "10.2478/jdis-2025-0014", "category": "doi_resolves", "description": "DOI resolves to expected paper for row 26", "value": true, "source_method": "lit-search.py metadata", "source_file": "Findings table row 26"}
{"claim_id": "10.1007-s11192-026-05585-2-authors", "doi": "10.1007/s11192-026-05585-2", "category": "authors", "description": "Authors for row 27", "value": "Thelwall et al. (2026)", "source_method": "lit-search.py metadata", "source_file": "Findings table row 27"}
{"claim_id": "10.1007-s11192-026-05585-2-year", "doi": "10.1007/s11192-026-05585-2", "category": "year", "description": "Publication year for row 27", "value": 2026, "source_method": "lit-search.py metadata", "source_file": "Findings table row 27"}
{"claim_id": "10.1007-s11192-026-05585-2-title", "doi": "10.1007/s11192-026-05585-2", "category": "title", "description": "Title for row 27", "value": "Can small and reasoning large language models score journal articles for research quality and do averaging and few-shot help?", "source_method": "lit-search.py metadata", "source_file": "Findings table row 27"}
{"claim_id": "10.1007-s11192-026-05585-2-citation_count", "doi": "10.1007/s11192-026-05585-2", "category": "citation_count", "description": "Citation count for row 27", "value": 4, "source_method": "lit-search.py metadata", "source_file": "Findings table row 27"}
{"claim_id": "10.1007-s11192-026-05585-2-doi_resolves", "doi": "10.1007/s11192-026-05585-2", "category": "doi_resolves", "description": "DOI resolves to expected paper for row 27", "value": true, "source_method": "lit-search.py metadata", "source_file": "Findings table row 27"}
{"claim_id": "10.31222-osf.io-gsc8f-authors", "doi": "10.31222/osf.io/gsc8f", "category": "authors", "description": "Authors for row 28", "value": "Thompson et al. (2022)", "source_method": "lit-search.py metadata", "source_file": "Findings table row 28"}
{"claim_id": "10.31222-osf.io-gsc8f-year", "doi": "10.31222/osf.io/gsc8f", "category": "year", "description": "Publication year for row 28", "value": 2022, "source_method": "lit-search.py metadata", "source_file": "Findings table row 28"}
{"claim_id": "10.31222-osf.io-gsc8f-title", "doi": "10.31222/osf.io/gsc8f", "category": "title", "description": "Title for row 28", "value": "Using prediction markets to estimate ratings of academic research quality in a mock Research Excellence Framework exercise", "source_method": "lit-search.py metadata", "source_file": "Findings table row 28"}
{"claim_id": "10.31222-osf.io-gsc8f-citation_count", "doi": "10.31222/osf.io/gsc8f", "category": "citation_count", "description": "Citation count for row 28", "value": 1, "source_method": "lit-search.py metadata", "source_file": "Findings table row 28"}
{"claim_id": "10.31222-osf.io-gsc8f-doi_resolves", "doi": "10.31222/osf.io/gsc8f", "category": "doi_resolves", "description": "DOI resolves to expected paper for row 28", "value": true, "source_method": "lit-search.py metadata", "source_file": "Findings table row 28"}
{"claim_id": "10.31219-osf.io-6efvp-authors", "doi": "10.31219/osf.io/6efvp", "category": "authors", "description": "Authors for row 29", "value": "TalkadSukumar et al. (2019)", "source_method": "lit-search.py metadata", "source_file": "Findings table row 29"}
{"claim_id": "10.31219-osf.io-6efvp-year", "doi": "10.31219/osf.io/6efvp", "category": "year", "description": "Publication year for row 29", "value": 2019, "source_method": "lit-search.py metadata", "source_file": "Findings table row 29"}
{"claim_id": "10.31219-osf.io-6efvp-title", "doi": "10.31219/osf.io/6efvp", "category": "title", "description": "Title for row 29", "value": "Replication and Transparency of Qualitative Research from a Constructivist Perspective", "source_method": "lit-search.py metadata", "source_file": "Findings table row 29"}
{"claim_id": "10.31219-osf.io-6efvp-citation_count", "doi": "10.31219/osf.io/6efvp", "category": "citation_count", "description": "Citation count for row 29", "value": 14, "source_method": "lit-search.py metadata", "source_file": "Findings table row 29"}
{"claim_id": "10.31219-osf.io-6efvp-doi_resolves", "doi": "10.31219/osf.io/6efvp", "category": "doi_resolves", "description": "DOI resolves to expected paper for row 29", "value": true, "source_method": "lit-search.py metadata", "source_file": "Findings table row 29"}
{"claim_id": "10.1016-j.ssresearch.2022.102770-authors", "doi": "10.1016/j.ssresearch.2022.102770", "category": "authors", "description": "Authors for row 30", "value": "Freese et al. (2022)", "source_method": "lit-search.py metadata", "source_file": "Findings table row 30"}
{"claim_id": "10.1016-j.ssresearch.2022.102770-year", "doi": "10.1016/j.ssresearch.2022.102770", "category": "year", "description": "Publication year for row 30", "value": 2022, "source_method": "lit-search.py metadata", "source_file": "Findings table row 30"}
{"claim_id": "10.1016-j.ssresearch.2022.102770-title", "doi": "10.1016/j.ssresearch.2022.102770", "category": "title", "description": "Title for row 30", "value": "Advances in transparency and reproducibility in the social sciences", "source_method": "lit-search.py metadata", "source_file": "Findings table row 30"}
{"claim_id": "10.1016-j.ssresearch.2022.102770-citation_count", "doi": "10.1016/j.ssresearch.2022.102770", "category": "citation_count", "description": "Citation count for row 30", "value": 28, "source_method": "lit-search.py metadata", "source_file": "Findings table row 30"}
{"claim_id": "10.1016-j.ssresearch.2022.102770-doi_resolves", "doi": "10.1016/j.ssresearch.2022.102770", "category": "doi_resolves", "description": "DOI resolves to expected paper for row 30", "value": true, "source_method": "lit-search.py metadata", "source_file": "Findings table row 30"}
{"claim_id": "10.24072-pci.archaeo.100616-authors", "doi": "10.24072/pci.archaeo.100616", "category": "authors", "description": "Authors for row 31", "value": "Bellat (2026)", "source_method": "lit-search.py metadata", "source_file": "Findings table row 31"}
{"claim_id": "10.24072-pci.archaeo.100616-year", "doi": "10.24072/pci.archaeo.100616", "category": "year", "description": "Publication year for row 31", "value": 2026, "source_method": "lit-search.py metadata", "source_file": "Findings table row 31"}
{"claim_id": "10.24072-pci.archaeo.100616-title", "doi": "10.24072/pci.archaeo.100616", "category": "title", "description": "Title for row 31", "value": "Recommendation of: Replication report for Marwick (2025) “Is archaeology a science?”, including new data from OpenAlex. Round#3", "source_method": "lit-search.py metadata", "source_file": "Findings table row 31"}
{"claim_id": "10.24072-pci.archaeo.100616-citation_count", "doi": "10.24072/pci.archaeo.100616", "category": "citation_count", "description": "Citation count for row 31", "value": 1, "source_method": "lit-search.py metadata", "source_file": "Findings table row 31"}
{"claim_id": "10.24072-pci.archaeo.100616-doi_resolves", "doi": "10.24072/pci.archaeo.100616", "category": "doi_resolves", "description": "DOI resolves to expected paper for row 31", "value": true, "source_method": "lit-search.py metadata", "source_file": "Findings table row 31"}
{"claim_id": "10.1098-rstb.2024.0275-authors", "doi": "10.1098/rstb.2024.0275", "category": "authors", "description": "Authors for row 32", "value": "Singh et al. (2025)", "source_method": "lit-search.py metadata", "source_file": "Findings table row 32"}
{"claim_id": "10.1098-rstb.2024.0275-year", "doi": "10.1098/rstb.2024.0275", "category": "year", "description": "Publication year for row 32", "value": 2025, "source_method": "lit-search.py metadata", "source_file": "Findings table row 32"}
{"claim_id": "10.1098-rstb.2024.0275-title", "doi": "10.1098/rstb.2024.0275", "category": "title", "description": "Title for row 32", "value": "Comparing expert assessments of research quality between the Global North and East Africa", "source_method": "lit-search.py metadata", "source_file": "Findings table row 32"}
{"claim_id": "10.1098-rstb.2024.0275-citation_count", "doi": "10.1098/rstb.2024.0275", "category": "citation_count", "description": "Citation count for row 32", "value": 1, "source_method": "lit-search.py metadata", "source_file": "Findings table row 32"}
{"claim_id": "10.1098-rstb.2024.0275-doi_resolves", "doi": "10.1098/rstb.2024.0275", "category": "doi_resolves", "description": "DOI resolves to expected paper for row 32", "value": true, "source_method": "lit-search.py metadata", "source_file": "Findings table row 32"}
{"claim_id": "10.1016-j.jbusres.2023.114189-authors", "doi": "10.1016/j.jbusres.2023.114189", "category": "authors", "description": "Authors for row 33", "value": "Adler et al. (2023)", "source_method": "lit-search.py metadata", "source_file": "Findings table row 33"}
{"claim_id": "10.1016-j.jbusres.2023.114189-year", "doi": "10.1016/j.jbusres.2023.114189", "category": "year", "description": "Publication year for row 33", "value": 2023, "source_method": "lit-search.py metadata", "source_file": "Findings table row 33"}
{"claim_id": "10.1016-j.jbusres.2023.114189-title", "doi": "10.1016/j.jbusres.2023.114189", "category": "title", "description": "Title for row 33", "value": "A toolbox to evaluate the trustworthiness of published findings", "source_method": "lit-search.py metadata", "source_file": "Findings table row 33"}
{"claim_id": "10.1016-j.jbusres.2023.114189-citation_count", "doi": "10.1016/j.jbusres.2023.114189", "category": "citation_count", "description": "Citation count for row 33", "value": 14, "source_method": "lit-search.py metadata", "source_file": "Findings table row 33"}
{"claim_id": "10.1016-j.jbusres.2023.114189-doi_resolves", "doi": "10.1016/j.jbusres.2023.114189", "category": "doi_resolves", "description": "DOI resolves to expected paper for row 33", "value": true, "source_method": "lit-search.py metadata", "source_file": "Findings table row 33"}
{"claim_id": "10.1126-science.aac4716-authors", "doi": "10.1126/science.aac4716", "category": "authors", "description": "Authors for row 34", "value": "Aarts (2015)", "source_method": "lit-search.py metadata", "source_file": "Findings table row 34"}
{"claim_id": "10.1126-science.aac4716-year", "doi": "10.1126/science.aac4716", "category": "year", "description": "Publication year for row 34", "value": 2015, "source_method": "lit-search.py metadata", "source_file": "Findings table row 34"}
{"claim_id": "10.1126-science.aac4716-title", "doi": "10.1126/science.aac4716", "category": "title", "description": "Title for row 34", "value": "Estimating the reproducibility of psychological science", "source_method": "lit-search.py metadata", "source_file": "Findings table row 34"}
{"claim_id": "10.1126-science.aac4716-citation_count", "doi": "10.1126/science.aac4716", "category": "citation_count", "description": "Citation count for row 34", "value": 5388, "source_method": "lit-search.py metadata", "source_file": "Findings table row 34"}
{"claim_id": "10.1126-science.aac4716-doi_resolves", "doi": "10.1126/science.aac4716", "category": "doi_resolves", "description": "DOI resolves to expected paper for row 34", "value": true, "source_method": "lit-search.py metadata", "source_file": "Findings table row 34"}
{"claim_id": "10.1038-s41562-018-0399-z-authors", "doi": "10.1038/s41562-018-0399-z", "category": "authors", "description": "Authors for row 35", "value": "Camerer et al. (2018)", "source_method": "lit-search.py metadata", "source_file": "Findings table row 35"}
{"claim_id": "10.1038-s41562-018-0399-z-year", "doi": "10.1038/s41562-018-0399-z", "category": "year", "description": "Publication year for row 35", "value": 2018, "source_method": "lit-search.py metadata", "source_file": "Findings table row 35"}
{"claim_id": "10.1038-s41562-018-0399-z-title", "doi": "10.1038/s41562-018-0399-z", "category": "title", "description": "Title for row 35", "value": "Evaluating the replicability of social science experiments in Nature and Science between 2010 and 2015", "source_method": "lit-search.py metadata", "source_file": "Findings table row 35"}
{"claim_id": "10.1038-s41562-018-0399-z-citation_count", "doi": "10.1038/s41562-018-0399-z", "category": "citation_count", "description": "Citation count for row 35", "value": 1131, "source_method": "lit-search.py metadata", "source_file": "Findings table row 35"}
{"claim_id": "10.1038-s41562-018-0399-z-doi_resolves", "doi": "10.1038/s41562-018-0399-z", "category": "doi_resolves", "description": "DOI resolves to expected paper for row 35", "value": true, "source_method": "lit-search.py metadata", "source_file": "Findings table row 35"}
```
<!-- END claims.jsonl -->

---

## Notes for the orchestrator / user (outside the contract sections)

- **This is a proposer draft — verification is pending.** The `/lit-scout` slash command should now pass this document to `lit-scout-verifier`. I have not invoked the verifier and have not generated a BibTeX file (both are downstream steps by design).
- **Environment caveat worth flagging:** the Scholar Gateway and Hugging Face MCP tools were unavailable this run, so the semantic-seed and ML-dataset phases were replaced by additional `lit-search.py` and WebSearch queries. Coverage of the ML/LLM and HASS literature is nonetheless strong; if you want the HF dataset angle (e.g. any released replicability-prediction corpora or LLM-judge benchmark datasets), re-run once the HF MCP tools are back.
- **Working files** (scratchpad, not under `~`): raw chain JSON, `candidates.txt`, `rows.json`, and `claims.jsonl` live under `/tmp/claude-1000/-home-shawn-Code-llm-reproducibility/7611d1aa-3419-49ba-a23e-b887887a92ea/scratchpad/`.

Sources (grey-literature/web queries used during seed discovery):
- [repliCATS project (University of Melbourne)](https://replicats.research.unimelb.edu.au/)
- [Predicting reliability through structured expert elicitation with repliCATS (PLOS ONE / PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9879480/)
- [Nature Human Behaviour — LLMs surpass human experts in predicting neuroscience results](https://www.nature.com/articles/s41562-024-02046-9)
