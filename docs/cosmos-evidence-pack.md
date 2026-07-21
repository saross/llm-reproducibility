# Evidence pack — Cosmos Grants application (July 2026)

Supporting evidence for the application **"Making Verification of Published Research
Routine"** (Cosmos Institute, AI and Truth-seeking round, submitted July 2026). The
application form links here rather than carrying long-form additional information.
Every claim below is anchored to an artefact in this repository or to the Open Science
Framework (OSF) registration; verification provenance is at the end of this page.

## Key artefacts

- **Preregistration:** <https://osf.io/dqnhg/> — OSF Open-Ended Registration, lodged
  2026-07-20, public. DOI: [10.17605/OSF.IO/DQNHG](https://doi.org/10.17605/OSF.IO/DQNHG)
- **Pilot findings report:**
  [studies/open-science-compliance/reports/pilot-findings-report.md](../studies/open-science-compliance/reports/pilot-findings-report.md)
- **Variability analysis (25-run stability test):**
  [outputs/variability-test/variability-analysis-report.md](../outputs/variability-test/variability-analysis-report.md)
- **Preregistration lodgement materials:**
  [studies/open-science-compliance/prereg/](../studies/open-science-compliance/prereg/)
- **Verified landscape review (twelve adversarially verified reports):**
  [wiki/planning/scout-reports/](../wiki/planning/scout-reports/)

## Reliability

The credibility-assessment stack has been stress-tested for the failure mode most cited against LLM assessors: 25 independent runs (five papers, five runs each) yielded 96% verdict stability, reported as a first-class reliability metric — a practice almost absent from the LLM-as-assessor literature (the nearest published analogue treats repeated-run quality scores as probability distributions; Thelwall & Yang 2025).

## Positioning

A two-stage landscape review (July 2026; every bibliographic and repository claim re-verified against authoritative sources by independent audit agents) found no published or preprint system combining computational reproduction, FAIR assessment, and adversarial review for any HASS discipline. The nearest neighbours — the Center for Open Science's funded ReplicatorBench and the Institute for Replication's announced, pre-release replication engine — serve quantitative social science and re-execute analyses without scoring openness or credibility. No published work validates LLM scoring of the GO-FAIR sub-principles against human raters; the FAIR-evaluation literature itself calls for exactly this (Candela et al. 2024). The registered design addresses that gap directly, with a preregistered subsample of 12 census papers hand-scored by the registrant, blinded to machine scores, and per-sub-principle agreement and Cohen's kappa reported. A separate grey-literature guard pass (OSF/SocArXiv, Zenodo, Humanities Commons, DataCite, and six archaeology venues; 26 logged queries, July 2026) confirmed the null: to our knowledge, no prior work applies large language models to assess, extract from, or reproduce archaeological research (the nearest item, Spennemann 2023, audits the model rather than the literature). This proposal complements, rather than duplicates, funded Cosmos work on claim-level literature navigation (e.g. Metalens): it verifies what papers did, not only what they claim.

## Disciplinary anchor

The Journal of Archaeological Science has run human reproducibility reviews since its January 2024 policy (Marwick 2025 reports these alongside a 10,000-article analysis). That human effort is the baseline my measured per-paper cost is compared against, and whether the policy changed practice is preregistration hypothesis H1.

## Truth-seeking in practice

The landscape review itself ran on this project's proposer-plus-adversarial-verifier architecture: over 1,800 machine-checkable claims were independently re-verified, catching an approximately 1% metadata error rate — including one fabricated author name — and detecting and refusing two prompt-injection attempts in the web-search layer. A parallel internal audit measured a ~10% error rate in agent-relayed specifics absent source re-verification. The pipeline's deterministic gates exist to catch exactly that measured failure mode. The method the grant funds is the method that produced this application's evidence.

## Delivery and follow-on

The pipeline ships as open-source code, as installable agent skills for the Claude and Codex ecosystems, and as a self-hostable runner (built by collaborator Brian Ballsun-Stanton), so any group can run the verifier on its own literature rather than trusting our dashboard. FAIR for Research Software (FAIR4RS) scoring of code artefacts is a named next step, pre-committed in the registration to a dated amendment path and the same reliability protocol before use. Beyond the registration's CC BY 4.0 licence, census and reproduction data tables will be deposited under CC0, and archival costs are zero by design (Zenodo, OSF), keeping the budget open-by-default. The extraction and credibility lane (claim–evidence graphs, literature use and neglect) is the natural follow-on. It carries a known cost driver this budget excludes (bibliographic and citation-index API access, e.g. Web of Science), and Metalens's support from two Cosmos programmes is precedent for sequencing follow-on funding.

## Supporting bibliography

All DOIs verified against authoritative sources, 2026-07-07/08.

- Marwick, B. (2025) "Is archaeology a science? Insights and imperatives from 10,000 articles and a year of reproducibility reviews", J. Archaeological Science. doi:10.1016/j.jas.2025.106281 — disciplinary anchor; human-review baseline.
- Candela, L., Mangione, D., & Pavone, G. (2024) "The FAIR Assessment Conundrum", Data Science Journal. doi:10.5334/dsj-2024-033 — FAIR tools are rule-based and non-comparable; calls for LLM-based assessment.
- Peters-von Gehlen, K., et al. (2022) "Recommendations for Discipline-Specific FAIRness Evaluation…", Data Science Journal. doi:10.5334/dsj-2022-007 — evaluator-disagreement evidence; the validation-design template.
- Fraser, H., et al. (2023) "Predicting reliability through structured expert elicitation with the repliCATS process", PLoS ONE. doi:10.1371/journal.pone.0274429 — the seven-signals parent method (human-only to date).
- Thelwall, M., & Yang, Y. (2025) "Implicit and explicit research quality score probabilities from ChatGPT", Quantitative Science Studies. doi:10.1162/qss.a.393 — nearest repeated-run reliability analogue.
- Serghiou, S., et al. (2021) "Assessment of transparency indicators across the biomedical literature", PLoS Biology. doi:10.1371/journal.pbio.3001107 — the scale-detection template (rule-based; no LLM successor published).
- Crockett, M., et al. (2023) "The limitations of machine learning models for predicting scientific replicability", PNAS. doi:10.1073/pnas.2307596120 — the critique this project's quality gating and stability testing answer.
- Topaz, M., et al. (2026) "Fabricated citations: an audit across 2·5 million biomedical papers", The Lancet. doi:10.1016/S0140-6736(26)00603-3 — the integrity context making routine verification urgent.

## Provenance

Prepared 2026-07-21 from the application working draft
([wiki/planning/cosmos-application-draft.md](../wiki/planning/cosmos-application-draft.md)).
Every number, name, date, and factual claim above was verified against primary sources by
two independent passes on 2026-07-21 (a session-level claim audit and a clean-context
adversarial verification agent, reconciled); the verification ledgers are recorded in the
working draft's header.
