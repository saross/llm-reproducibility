# repliCATS → LLM‑Assisted Credibility Assessment for HASS
_A practical primer and blueprint for landscape archaeology & related fields_

**Author:** Prepared for CWTS Leiden visiting fellowship planning  
**Last updated:** 28 Oct 2025

---

## TL;DR

- **repliCATS** is a structured **human‑elicitation** workflow (IDEA: Investigate → Discuss → Estimate → Aggregate) used at scale under DARPA’s SCORE program to forecast research credibility/replicability from published papers.  
- It achieved **strong predictive performance** in held‑out tests while collecting **structured reasons** and **paper‑level “credibility signals”** (clarity, transparency, plausibility, validity, robustness, replicability, generalisability).  
- For **HASS and landscape archaeology**, we can adapt repliCATS by using **LLMs for semantic extraction** (Claim–Evidence–Method graphs) and **multi‑agent scoring** of the same signals, with human panels reserved for **escalations** and **calibration**.  
- This document explains what repliCATS did, what to borrow, and gives a **six‑month build plan** for an LLM‑assisted credibility pipeline.

---

## 1) What repliCATS actually did (in one page)

**Goal.** Produce reliable, scalable judgments about the credibility/replicability of claims made in published research by coordinating **small expert groups** using the **IDEA protocol**: private estimation → structured discussion → revised estimation → principled aggregation.

**Process.**
1. Curated claims from papers in target fields.  
2. Ran **small groups** (4–8) through IDEA on a web platform: each person gave a private probability + short justification; saw the group’s reasoning; revised their estimate.  
3. Aggregated final probabilities using calibrated methods (e.g., trimmed means/quantile aggregations).  
4. Logged **justifications** and **paper‑level signals** to explain _why_ a claim looked credible or shaky.

**Scale & outputs.**
- Assessed thousands of claims from social/behavioral science journals under the SCORE program.
- Delivered (i) probabilities that a claim would replicate, (ii) **seven credibility signals** per paper, and (iii) a large corpus of structured rationales.

**Performance (headline).**
- On claims linked to eventual replication outcomes, repliCATS achieved **competitive AUC/accuracy** relative to prediction‑market and expert‑survey baselines—strong enough to be operationally useful.
- A focused validation study on a small set of “known‑outcome” claims showed **very high discriminative accuracy** (demonstrating the potential of structured elicitation).

**What it is _not_.** Not “conventional ML.” It is **human‑in‑the‑loop structured deliberation** whose outputs can be used to **train and benchmark** automated systems (continued in COS’s SMART program).

---

## 2) What repliCATS produced that is useful for HASS/archaeology

1) **A generalizable decision protocol** under uncertainty that yields probabilities **and** explanations (IDEA).  
2) **A seven‑signal rubric** broadening “replicability” into **credibility** (clarity/comprehensibility; transparency; plausibility; validity; robustness; replicability; generalisability).  
3) **Evidence of effectiveness** comparable to other forecasting methods.  
4) **A ground‑truth spine** (replication/reproduction outcomes on subsets) to calibrate/validate automated scoring.

---

## 3) Translating repliCATS into an LLM‑assisted pipeline

### 3.1 LLM‑augmented IDEA

- **Investigate →** Use LLMs to extract a **CEM (Claim–Evidence–Method) graph** from each paper, with verbatim text spans for provenance.  
- **Discuss →** Run **multi‑agent LLM ensembles** (optionally mixed models) to draft reasons per signal; synthesize once; optionally expose to **human moderators** for escalation cases.  
- **Estimate →** For each signal, require a **probability or 0–100 score** with **interval bounds** (lower / best / upper) + 2–4 sentence justification tied to node IDs in the CEM graph.  
- **Aggregate →** Combine agent/human scores with trimmed means or quantile aggregation; **calibrate** against a small human‑rated validation set using proper scoring rules.

### 3.2 Adapting the seven signals to HASS (with automatable checks)

| Signal | HASS‑oriented question | Automatable features | Typical metrics |
|---|---|---|---|
| **Comprehensibility** | Are main claims explicit and bounded? | Detect claim statements; scope (space/time/population); link claims ↔ evidence | % claims with explicit scope; claim‑evidence linkage ratio |
| **Transparency** | Are aims (exploratory/confirmatory) and methods/sampling documented and aligned? | Extract aims; sampling frames; strategy rationales; decision logs | Methods‑linked‑to‑claims ratio; presence of key design elements |
| **Plausibility** | Do interpretations fit chronology/typology/geomorphology and comparanda? | RAG over period/typology/gazetteers; conflict flags | # comparanda cited; conflict flags |
| **Validity (Evidential adequacy)** | Is evidence sufficient/representative; are alternatives engaged? | Evidence‑to‑claim density; coverage stats; detection of rival interpretations | Coverage metric; rival‑interpretations present |
| **Robustness** | Do results survive reasonable analytic alternatives; triangulated? | Sensitivity checks; multiple independent indicators | # sensitivity checks; triangulation indicators |
| **Replicability (analysis)** | Can others reproduce outputs from the same inputs? | Data/code DOIs; environment docs; link resolution | Data+code availability; execution metadata present |
| **Generalisability** | Are limits on transfer across time/space explicit? | Detect limitation statements; map extents | Limitations present; extrapolation flags |

### 3.3 Where LLMs add unique value

- **Semantic extraction at scale** of claims, evidence, and methods into an auditable graph.  
- **Rationale mining**: summarizing patterns across thousands of justifications (e.g., common weaknesses).  
- **Low‑cost triage**: route clear cases to automation; escalate uncertain or controversial ones to humans.

### 3.4 What to keep from repliCATS—almost verbatim

- **Group deliberation** (two‑round critique) to reduce overconfidence.  
- **Quantified judgments with uncertainty** (intervals, not point guesses).  
- **Reasons, not just scores** (make every score traceable to passages and artifacts).

---

## 4) Forecasting context: how strong are these methods overall?

- Prediction markets and expert surveys routinely achieve **~0.70–0.85 classification accuracy** in replication forecasting across several disciplines.  
- **repliCATS** sits in that band while producing **richer, auditable reasoning data**, suggesting a credible baseline for hybrid LLM+human systems to match or exceed after calibration.

---

## 5) Six‑month CWTS blueprint (from your proposal)

**A. Sept–Oct: Corpus & schema**  
- 30–50 open‑access HASS papers emphasizing landscape archaeology; add some history/anthropology.  
- Define the **CEM graph** schema (see separate spec) and light **CIDOC‑CRM/CRMarchaeo** crosswalk.  
- Draft signal rubrics & auto‑heuristics (v0.1).

**B. Nov–Dec: Extraction prototypes**  
- Implement multi‑turn LLM extraction to build CEM graphs with provenance.  
- Build repository checkers (e.g., Zenodo/OSF/Open Context/tDAR/ARIADNE) for data/code links and metadata completeness.  
- Hand‑label 10–15 papers to benchmark extraction accuracy.

**C. Jan: Credibility assessors**  
- Per‑signal assessors ingest the graph + snippets and output `score`, `lower`, `upper`, `justification`, `evidence_refs`.  
- Run **5‑agent ensembles**; aggregate with trimmed mean; compute inter‑agent variance to drive **escalation**.

**D. Feb: Validation & calibration**  
- Expert panel (3–5 scholars). Compute **inter‑rater reliability** and compare model vs. human via **correlations, Brier scores, calibration curves**.  
- Error analysis focusing on: missed alternatives, style bias, stewardship mis‑scoring.  
- Freeze **v0.1** prompts, weights, and documentation.

**Deliverables**  
- **Per‑paper scorecards** (seven signals + narrative justifications + provenance).  
- **Cross‑paper dashboard** surfacing recurrent issues (e.g., sampling rationales, repository rot).  
- **Technical spec** for scaling; open‑source code & validation dataset.

---

## 6) HASS‑specific edge cases (and handling)

- **Non‑repeatable events**: shift “replicability” to **analytic reproducibility** and **convergent evidence** robustness.  
- **Narrative/theory papers**: emphasize **transparency, plausibility, generalisability, reflexivity**; mark analytic replicability as **NA** (don’t penalize).  
- **Indigenous/community data**: apply **CARE** alongside FAIR; don’t penalize restricted access if properly justified and governed.

---

## 7) Risks & mitigations (from repliCATS lessons)

- **Overconfidence/anchoring** → two‑round scoring + interval estimates; show dissenting rationales.  
- **Style bias** → require claim‑to‑evidence links; penalize unsupported rhetoric.  
- **Assessment reproducibility** → version models/prompts/seeds; store inputs/outputs and aggregation settings.  
- **Cost** → reserve human time for high‑uncertainty cases and periodic calibration.

---

## 8) Positioning relative to the “credibility revolution”

This pipeline provides **direct, content‑based indicators** (design transparency, evidential adequacy, analytic reproducibility, stewardship) that complement or replace proxy metrics. It respects interpretive epistemologies while bringing **auditable structure** to evaluation.

---

## 9) Pointers for references & further reading (fill with links you prefer)

- repliCATS project overviews and methodology papers.  
- DARPA SCORE program reports/datasets.  
- COS **SMART** program (automation + deliberation).  
- Extraction with conversational LLMs (e.g., Polak & Morgan 2024).  
- Anthropic’s **Clio** (large‑scale summarization/analysis).  
- FAIR (Wilkinson et al., 2016) and CARE principles (GIDA).  
- CIDOC‑CRM/CRMarchaeo, ARIADNE, Open Context, tDAR.

---

## 10) Implementation checklist

- [ ] Finalize CEM schema and crosswalk.  
- [ ] Build extraction prompts + provenance capture.  
- [ ] Wire repository checkers (links resolve; metadata present; license).  
- [ ] Implement per‑signal assessors + ensemble aggregation.  
- [ ] Define escalation thresholds and human moderation flow.  
- [ ] Design validation protocol and score reporting.  
- [ ] Freeze v0.1 and publish the spec + pilot results.

---

### Attribution & reuse
This document is intended for rapid adoption in pilot studies. License your implementation artifacts under a permissive license (MIT/Apache‑2.0) and publish the rubrics/specs as open standards to support community refinement.
