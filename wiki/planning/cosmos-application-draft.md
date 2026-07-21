# Cosmos Grants Application — Working Draft

**Version:** 0.4
**Date:** 2026-07-21
**Status:** Proposal draft v0.4 — pre-submission integration pass (2026-07-21, academic-prose
skill): body aligned with the lodged registration (already-preregistered sentence with
osf.io/dqnhg; 2022–2026 window; control-series clause; pilot error-detection instance;
499/500 words); field 19 gains the human-validation link, the agent-relay audit line, and
a delivery-and-follow-on paragraph (Claude/Codex skills + self-hostable runner with
B. Ballsun-Stanton, FAIR4RS, CC0 data outputs, follow-on API-cost driver); field 18 entry
added; candidate drafts for fields 15/16/6/14 below for Shawn's selection. Awaiting
Shawn's manual editing pass. (v0.3's "left uncommitted" note superseded — committed since
`7435865`.)
**Inputs:** `cosmos-grant-application-framing.md` (§4 pitch, §5 lane roles, §6 budget);
`cosmos-application-form-questions.md` (field 17 five-part structure, <500 words);
Shawn's framing feedback 2026-07-07 (broader-programme positioning; HASS-native emphasis)

---

## Framing resolutions (agreed direction, 2026-07-07)

1. **Broader programme as substrate, not ask.** The Claims–Evidence–Methods (CEM) graph and
   Research Design and Methods Assessment Protocol (RDMAP) framework appears as *working
   infrastructure* (five papers piloted; implicit claims; claim–evidence strength; methods
   appropriateness) with the grant funding its *verification lanes* (reproduction + FAIR).
   Rationale: the claim-decomposition space is the most crowded funded cluster in the Cosmos
   portfolio (framing doc §3); reproduction is unoccupied. Positioning the graph as substrate
   turns the crowded cluster into a moat — no funded claims tool re-executes analyses.
   Future capabilities named briefly (literature use/neglect); discourse-level analysis left
   out of the 500 words.
2. **"HASS-native framework, computational bridgehead."** Reproducibility infrastructure
   serves biomedicine and quantitative social science; HASS is left out. Archaeology as
   entry point *because* interpretive (excavation consumes its own evidence — primary
   observations unrepeatable, so the analysis layer is the checkable one) *and* possessed of
   a growing computational core where verification is tractable. The framework is HASS-native;
   the first production lane is deliberately computational; the graph core carries
   verification beyond the computational later. Avoids overclaiming non-computational
   reproducibility (Shawn's caution). Supporting context from Shawn (2026-07-07; for our
   use, not necessarily the grant text): archaeology's quantitative tradition is old and
   institutionalised — the Computer Applications and Quantitative Methods in Archaeology
   (CAA) organisation dates to the early 1970s — making the discipline a credible bridge
   from the "usual suspects" (biomedicine, quantitative social sciences) while still
   involving humanities-adjacent historical investigation. Candidate material for the
   self-pitch or form field 19.

## Proposal draft (form field 17, <500 words)

<!-- proposal-body-start -->
**Alignment.** I am applying to the AI x Truth-seeking stream to build infrastructure that
makes verification of published research cheap enough to be routine — so that trust in a
paper is earned through open contestation rather than presumed from authority. The pipeline
implements contestation literally: every reproduction is audited by an adversarial AI
reviewer in a fresh context, with no memory of the work it audits, and its
challenges are published alongside the verdict. The aim is not compliance policing but
lowering the cost of checking until open inquiry into published claims is normal.

**Problem.** Most published findings are never independently checked: verifying that numbers
reproduce, that data and code are available and usable, and that evidence supports claims is skilled,
tedious, unrewarded work. Existing reproducibility infrastructure serves biomedicine and the
quantitative social sciences; an independently verified landscape review (July 2026) found
no comparable system for the humanities, arts, and social sciences (HASS) — and most new
assessment tools never execute code. Archaeology is the ideal bridgehead — an interpretive field discipline whose
primary observations are unrepeatable (excavation consumes its own evidence), yet with a
fast-growing computational core where verification is tractable. My wider framework, already
running, decomposes a paper into a graph of claims (explicit and implicit), evidence,
methods, and research designs, and evaluates claim–evidence strength and method
appropriateness; planned lanes will assess how papers use — and ignore — the
literature. This project builds the framework's verification lanes: computational
reproduction and FAIR (Findable, Accessible, Interoperable, Reusable) assessment.

**Medium.** Open-source code plus a public demonstration: an agentic pipeline (Docker-based
reproduction, FAIR scoring, fresh-context adversarial review), a browsable results
dashboard, and a human-verification interface where domain experts audit sampled
AI verdicts — AI and human checks by design.

**Plan.** This is not a from-zero build: a completed pilot ran five Journal of
Archaeological Science (JAS) papers through the full stack, yielding four successful and one
partial reproduction and a headline finding — data availability, not code availability,
predicts whether a paper reproduces. The pilot also caught two calculation errors that
peer review had missed. Four confirmatory hypotheses (and a pre-specified exploratory
analysis) are preregistered on the Open Science Framework (osf.io/dqnhg). In 90 days I
will: (1) convert the piloted workflow into an autonomous agentic pipeline with
deterministic quality gates and batched human approval; (2) regression-test it against
pilot artefacts; (3) run a FAIR census of JAS 2022–2026, with a control series from its
sister journal, and reproduce the eligible computational subset; (4) publish the
dashboard and verification interface, with expert spot-audits of sampled verdicts.

**Success.** A public, clickable census of open-science practice in a flagship archaeology
journal, with every reproduction verdict traceable to artefacts anyone can re-run;
preregistered answers to live questions (for example: did JAS's January 2024 mandatory
reproducibility-review policy actually change practice?); and a measured per-paper cost 
showing verification can be routine rather than heroic. The framework is 
HASS-native and extensible: the same claims–evidence core will carry verification 
beyond the computational as the wider programme grows.
<!-- proposal-body-end -->

## Drafting choices — Shawn's verdicts (2026-07-07)

1. First person singular ("I") — **confirmed**.
2. Variability study, follow-on-funding pointer, and Metalens-complementarity line go to
   form field 19 ("additional info"), not the 500 words — **confirmed**.
3. Policy-question hook: Shawn couldn't spot it (it was a parenthetical in Success); now
   sharpened to "(for example: did JAS's January 2024 mandatory reproducibility-review
   policy actually change practice?)". It is preregistration hypothesis H1 (pilot findings
   report §7).
4. No stretch clause for sampled claim–evidence pairs — **confirmed** (crowded-area
   caution; stay as drafted).
5. "A flagship archaeology journal" hedge — **confirmed**.
6. Literature-use compression ("how papers use — and ignore — the literature") —
   **confirmed**; discourse-level framing held back for later use.

## Preregistration sequencing — RESOLVED: lodged before submission

**[x] 2026-07-20 LODGED: <https://osf.io/dqnhg/>** (Open-Ended Registration;
artefacts frozen at `ee3fda3`; tag `osf-prereg-phase2-2026-07-20`). The
proposal body now says "already preregistered" and links the registration; the
fallback below is moot. **The registration is EMBARGOED** (Shawn 2026-07-21:
double-blind peer-review contingency; journal policy check under way) — **lift
the embargo before submitting the application** so the linked URL resolves for
Cosmos reviewers.

Question (Shawn, 2026-07-07): lodge the OSF preregistration before submitting the
application, so the application links a live registration?

Recommendation (adopted): **yes — draft immediately, lodge before submission.** The prereg must
precede the FAIR census anyway (Option A ordering, modernisation plan §6); its content is
largely written (H1–H5 in the pilot findings report §7; study protocol exists); and a live,
clickable OSF registration converts "I will preregister" into "already preregistered" —
strong feasibility and truth-seeking signal at a ~9%-selective programme. Drafting care
needed so Phases 1–2 need no amendment: specify the measures (15 binary GO-FAIR
sub-principles, data/code scored independently) as instrument, permit pipeline
implementation changes gated on regression tests against pilot artefacts, and commit that
no new-corpus data is touched before registration. Fallback if review time runs short:
submit the application citing "registration precedes any corpus contact" — weaker but
acceptable. Interacts with plan §9 items 1–2 (FAIR stability spot-check): the spot-check
uses pilot papers only, so it can run before or after registration without contaminating
the design.

## Field 19 draft — additional information (evidence pack, v0.3)

Draft text for the "anything else we should know" field; trim to any form limit at
submission. Every specific below is verifier-backed (sources: scout-reports series,
2026-07-07/08).

> **Reliability.** The credibility-assessment stack has been stress-tested for the failure
> mode most cited against LLM assessors: 25 independent runs (five papers, five runs each)
> yielded 96% verdict stability, reported as a first-class reliability metric — a practice
> almost absent from the LLM-as-assessor literature (the nearest published analogue treats
> repeated-run quality scores as probability distributions; Thelwall & Yang 2025).
>
> **Positioning.** A two-stage landscape review (July 2026; every bibliographic and
> repository claim re-verified against authoritative sources by independent audit agents)
> found no published or preprint system combining computational reproduction, FAIR
> assessment, and adversarial review for any HASS discipline. The nearest funded neighbours
> — the Center for Open Science's ReplicatorBench and the Institute for Replication's
> replication engine — serve quantitative social science and re-execute analyses without
> scoring openness or credibility. No published work validates LLM scoring of the GO-FAIR
> sub-principles against human raters; the FAIR-evaluation literature itself calls for
> exactly this (Candela et al. 2024). The registered design addresses that gap directly,
> with a preregistered subsample of 12 census papers independently hand-scored, blinded
> to machine scores, and per-sub-principle agreement and Cohen's kappa reported. A
> separate grey-literature guard pass (OSF/SocArXiv,
> Zenodo, Humanities Commons, and six archaeology venues; 26 logged queries, July 2026)
> confirmed the null: to our knowledge, no prior work applies large language models to
> assess, extract from, or reproduce archaeological research. This proposal complements,
> rather than duplicates, funded Cosmos work on claim-level literature navigation (e.g.
> Metalens): it verifies what papers did, not only what they claim.
>
> **Disciplinary anchor.** The Journal of Archaeological Science has run human
> reproducibility reviews since its January 2024 policy (Marwick 2025 reports these
> alongside a 10,000-article analysis). That human effort is the baseline my measured
> per-paper cost is compared against, and whether the policy changed practice is
> preregistration hypothesis H1.
>
> **Truth-seeking in practice.** The landscape review itself ran on this project's
> proposer-plus-adversarial-verifier architecture: over 1,800 machine-checkable claims were
> independently re-verified, catching an approximately 1% metadata error rate — including
> one fabricated author name — and detecting and refusing two prompt-injection attempts
> embedded in web-search results. A parallel internal audit measured a ~10% error rate in
> agent-relayed specifics absent source re-verification. The pipeline's deterministic
> gates exist to catch exactly that measured failure mode. The method the grant funds is
> the method that produced this application's evidence.
>
> **Delivery and follow-on.** The pipeline ships as open-source code, as installable
> agent skills for the Claude and Codex ecosystems, and as a self-hostable runner (built
> by collaborator Brian Ballsun-Stanton), so any group can run the verifier on its own
> literature rather than trusting our dashboard. FAIR for Research Software (FAIR4RS)
> scoring of code artefacts is a named next step, pre-committed in the registration to a
> dated amendment path and the same reliability protocol before use. Census and
> reproduction data tables will be deposited under CC0 (documents under CC BY 4.0), and
> archival costs are zero by design (Zenodo, OSF), keeping the budget open-by-default.
> The extraction and credibility lane (claim–evidence graphs, literature use and neglect)
> is the natural follow-on. It carries a known cost driver this budget excludes
> (bibliographic and citation-index API access, e.g. Web of Science), and Metalens's
> support from two Cosmos programmes is precedent for sequencing follow-on funding.
>
> Supporting bibliography available on request (or see below if space permits).

### Supporting bibliography (offload; all DOIs verified 2026-07-07/08)

- Marwick, B. (2025) "Is archaeology a science? Insights and imperatives from 10,000
  articles and a year of reproducibility reviews", *J. Archaeological Science*.
  doi:10.1016/j.jas.2025.106281 — disciplinary anchor; human-review baseline.
- Candela, L., Mangione, D., & Pavone, G. (2024) "The FAIR Assessment Conundrum", *Data
  Science Journal*. doi:10.5334/dsj-2024-033 — FAIR tools are rule-based and
  non-comparable; calls for LLM-based assessment.
- Peters-von Gehlen, K., et al. (2022) "Recommendations for Discipline-Specific FAIRness
  Evaluation…", *Data Science Journal*. doi:10.5334/dsj-2022-007 — evaluator-disagreement
  evidence; the validation-design template.
- Fraser, H., et al. (2023) "Predicting reliability through structured expert elicitation
  with the repliCATS process", *PLoS ONE*. doi:10.1371/journal.pone.0274429 — the
  seven-signals parent method (human-only to date).
- Thelwall, M., & Yang, Y. (2025) "Implicit and explicit research quality score
  probabilities from ChatGPT", *Quantitative Science Studies*. doi:10.1162/qss.a.393 —
  nearest repeated-run reliability analogue.
- Serghiou, S., et al. (2021) "Assessment of transparency indicators across the biomedical
  literature", *PLoS Biology*. doi:10.1371/journal.pbio.3001107 — the scale-detection
  template (rule-based; no LLM successor published).
- Crockett, M., et al. (2023) "The limitations of machine learning models for predicting
  scientific replicability", *PNAS*. doi:10.1073/pnas.2307596120 — the critique this
  project's quality gating and stability testing answer.
- Topaz, M., et al. (2026) "Fabricated citations: an audit across 2·5 million biomedical
  papers", *The Lancet*. doi:10.1016/S0140-6736(26)00603-3 — the integrity context making
  routine verification urgent.

## Field 18 — collaborators (added 2026-07-21)

Brian Ballsun-Stanton [unverified: affiliation/title — Shawn to supply] — packages the
pipeline as installable Claude and Codex agent skills and builds the self-hostable
runner for public deployment. Role from Brian's own feedback (relayed by Shawn,
2026-07-21): "ship it as a claude, codex skill", "build it into a self-hostable runner
online". He has no JAS or *JAS: Reports* papers in the census window; if his role makes
him study personnel, prereg §5 criterion 5 (study-personnel papers excluded from
reproduction) applies automatically at no practical cost.

## Candidate drafts — fields 15, 16, 6, 14 (2026-07-21; Shawn selects and edits)

### Project title (field 15)

1. Routine Verification of Published Research: an AI Reproduction and FAIR-Assessment
   Pipeline, Piloted on Archaeology
2. Cheap Enough to Check: AI-Assisted Reproduction and Openness Scoring of Published
   Archaeological Science
3. Making Published Research Checkable: an AI-and-Human Verification Pipeline for
   Archaeology

### One-sentence description (field 16)

1. An open-source pipeline that reproduces the computational results of published papers
   and scores their openness, with AI and human checks, demonstrated as a live
   verification census of a flagship archaeology journal.
2. AI agents re-run published analyses and score data and code openness, adversarial
   reviewers audit every verdict, and human experts spot-check the output, delivered as
   a public census of a flagship archaeology journal.

### Self-pitch, 1–2 sentences (field 6)

1. Archaeologist and open-science infrastructure builder (co-founder of the
   FAIMS/Fieldmark field-data platform), now applying AI agents to make verification of
   published research routine. A completed five-paper pilot is already running, with
   every verdict auditable by humans.
2. I am an archaeologist working in the discipline's half-century-old quantitative
   tradition (Computer Applications and Quantitative Methods in Archaeology, founded
   early 1970s), and I build open research infrastructure. My verification pipeline has
   already reproduced five published papers and caught calculation errors that peer
   review missed.

### Grant request (field 14) — worked candidate

**US$8,000** (form integer: 8000). Composition (framing §6 lines plus Brian's runner):

| Line | US$ | Justification |
|------|-----|---------------|
| Inference credits, two vendors | 4,000 | Anthropic + OpenAI; cross-model verification is methodological, not redundancy |
| Cloud compute for reproductions | 1,200 | Long jobs off the local host; host-independence is itself a reproducibility claim |
| Hosting + domain (dashboard, runner, skills distribution) | 500 | The clickable public demo; Brian's runner distribution |
| Human-verification honoraria | 1,000 | Strengthens "AI and human checks"; framing §6 flags the admin overhead — confirm deliberately |
| Dissemination (CAA contribution) | 600 | Community the pilot papers come from |
| Contingency (~10%) | 700 | |
| Archival | 0 | Zenodo + OSF free by design — say so in the application |

Lean variant without honoraria: ≈ US$7,000. Range anchor from framing §6: US$1k–10k as
a signal of scope and seriousness, not a funding plan.

## Remaining at submission (Shawn)

- Select and edit the candidates above; supply Brian's affiliation line
- Field 20 (how-did-you-hear) — factual, Shawn supplies
- Optional profile links (website, LinkedIn, X, Substack) — form says they aid review
- Lift the OSF embargo and verify <https://osf.io/dqnhg/> resolves publicly with DOI
- Trim field 19 to any form limit at submission (guard-pass null folded in 2026-07-08;
  source: scout-reports/2026-07-08-g1-archaeology-guard-null-result.md)
