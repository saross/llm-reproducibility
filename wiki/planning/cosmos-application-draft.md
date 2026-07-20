# Cosmos Grants Application — Working Draft

**Version:** 0.3
**Date:** 2026-07-08
**Status:** Proposal draft v0.3 — Shawn's review edits (2026-07-08) preserved; body
enriched with one verifier-backed positioning sentence (Problem); field 19 evidence pack
and supporting bibliography drafted from the 2026-07-07/08 scout sweep; title, one-liner,
self-pitch, and grant amount still to draft. File deliberately left uncommitted while
under Shawn's review.
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
reviewer running in a fresh context, with no memory of the work it audits, and its
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
methods, and research designs, and evaluates the strength of claim–evidence links and the
appropriateness of methods; planned lanes will assess how papers use — and ignore — the
literature. This project builds the framework's verification lanes: computational
reproduction and FAIR (Findable, Accessible, Interoperable, Reusable) assessment.

**Medium.** Open-source code plus a public demonstration: an agentic pipeline (Docker-based
reproduction, FAIR scoring, fresh-context adversarial review), a browsable results
dashboard, and a human-verification interface through which domain experts audit samples of
AI verdicts — AI and human checks by design.

**Plan.** This is not a from-zero build: a completed pilot ran five Journal of
Archaeological Science (JAS) papers through the full stack, yielding four successful and one
partial reproduction and a measurable headline finding — data availability, not code
availability, predicts whether a paper reproduces. Five hypotheses are already
preregistered on the Open Science Framework (osf.io/dqnhg). In 90 days I will: (1) convert
the piloted workflow into an autonomous agentic pipeline with deterministic quality gates
and batched human approval; (2) regression-test it against pilot artefacts; (3) run a FAIR
census of JAS 2022–2026 and reproduce the eligible computational subset; (4) publish the
dashboard and verification interface, with expert spot-audits of sampled verdicts.

**Success.** A public, clickable census of open-science practice in a flagship archaeology
journal, with every reproduction verdict traceable to artefacts anyone can re-run;
preregistered answers to live questions (for example: did JAS's January 2024 mandatory
reproducibility-review policy actually change practice?); and a measured per-paper cost 
demonstrating that verification can be routine rather than heroic. The framework is 
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

**[x] 2026-07-20 LODGED: <https://osf.io/dqnhg/>** (Open-Ended Registration, no
embargo; artefacts frozen at `ee3fda3`; tag `osf-prereg-phase2-2026-07-20`). The
proposal body now says "already preregistered" and links the registration; the
fallback below is moot. At lodgement the registration was in OSF's admin-approval
window — **verify the URL resolves publicly before submitting the application**.

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
> mode most cited against LLM assessors: twenty-five independent runs on the same paper
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
> exactly this (Candela et al. 2024). A separate grey-literature guard pass (OSF/SocArXiv,
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
> embedded in web-search results. The method the grant funds is the method that produced
> this application's evidence.
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

## Still to draft (other form fields)

- Project title (field 15)
- One-sentence project description (field 16)
- Self-pitch, 1–2 sentences (field 6)
- Grant request integer (field 14) — refine from framing §6 brainstorm
- ~~Field 19 "additional info" paragraph~~ — drafted above (v0.3); guard-pass null folded
  in 2026-07-08 (source: scout-reports/2026-07-08-g1-archaeology-guard-null-result.md);
  trim to form limits at submission
