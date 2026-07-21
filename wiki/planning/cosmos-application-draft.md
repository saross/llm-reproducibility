# Cosmos Grants Application — Working Draft

**Version:** 0.7 (body revised by Shawn and jointly tightened; submission-ready)
**Date:** 2026-07-21
**v0.7 (same day):** Shawn's manual revision of the body (long-tail reframing,
combined-approaches problem statement, JAS: Reports named, survey clause, Plan
restructure) reviewed and tightened from 566 to 499/500 with correctness fixes
(computational not quantitative subset; broken Alignment sentence rebuilt; grammar/typo
fixes; unanchored earth/environmental-sciences claim dropped). Voice changed to
first-person plural (Brian now a named collaborator — supersedes drafting verdict 1);
"truth-seeking" token restored to the Alignment close. Literature-lanes sentence cut
from the body (word budget) — it survives in field 19's Delivery-and-follow-on
paragraph.
**v0.6 (same day):** clean-context adversarial verification run and reconciled against
the PA-hub ledger below (three ledger pointers corrected; wording fixes applied to field
19 and both self-pitch candidates); self-pitch recomposed to the done-things steer;
final paste set added covering every form field (1–21), with recommendations for title,
one-liner, self-pitch, and amount.
**Pre-submission claim verification (2026-07-21, PA-hub session):** every number, name,
date, and factual claim in the field 17 body, field 19, and the v0.5 candidate fields was
listed and checked verified-against-record; the from-memory set is EMPTY. Key anchors:
499/500 words (counted); four-successful-one-partial, two calculation errors, data-not-code
headline (`studies/open-science-compliance/reports/pilot-findings-report.md` §§1, 5.2, 6);
"mandatory" Jan 2024 policy wording matches the frozen pilot report verbatim (its §1 and
§7 H1); H1–H4 confirmatory + H5 pre-specified exploratory, 2022–2026 window, JAS: Reports
control, 12-paper blinded hand-scoring with Cohen's kappa
(`studies/open-science-compliance/prereg/osf-registration-summary.txt`); landscape nulls +
"most tools never execute code" (`scout-reports/2026-07-08-stack-positioning-synthesis.md`
§§2, 5); "over 1,800 claims" is conservative — the scout-report claim ledgers hold 2,118
records (grep count; the synthesis's ~1,600 predates the five follow-up runs); one
fabricated author name + two prompt-injection refusals (synthesis §5); ~10% agent-relay
rate (this repo's `wiki/working-notes.md` Obs 4); 96% verdict stability
(`outputs/variability-test/variability-analysis-report.md`, 24/25 majority-verdict runs); 26-query guard null (g1 report);
ReplicatorBench + I4R engine (p4 prior-art + p1 lit reports — I4R's engine is pre-release
and its named funding is a SSHRC application, so field 19 scopes "funded" to
ReplicatorBench); all CV specifics for both authors
re-read from `~/Downloads/Ross_CV_Cosmos_Institute.pdf` +
`Ballsun-Stanton_CV_Cosmos_Institute.pdf` ($4,799,690/$2,628,673 grants summary; 41
publications; Nature 2023; both fellowships; ORCIDs; Brian's 2025 VC award, 40+
workshops/1,500+ researchers, "Prompt Engineering, Harness Engineering, LLM deployment on
HPC" verbatim; jcaa.96 in both CVs; the UP Florida chapter is listed in Ballsun-Stanton's
CV only — the Ross CV counts its 11 chapters in aggregate without listing them). "Stream"
is the form's own term (field 13).
**Adversarial re-verification (2026-07-21, clean-context agent, reconciled with the
ledger above):** independent pass confirmed every submission-facing claim (499/500
recounted; 2,118 ledger records recounted, so "over 1,800" is conservative); three
ledger pointers corrected in place (Obs 4 not Obs 6; pilot §1/§7 not §2.1; Florida
chapter in one CV); wording-level corrections applied to field 19 and the self-pitch
candidates per the agent's ranked list. **Cleared to submit once the OSF embargo on
osf.io/dqnhg is lifted.**
**v0.5 (same day):** affiliations resolved from both CVs (read from ~/Downloads/, kept
out of the repo — Shawn's CV not yet public): applicant = Honorary Professor (MQ) +
EFN director; Brian = Lecturer, Faculty of Arts, MQ, with research-integrity-award and
FAIMS-architect credentials; team-pedigree line added (preregistration chapter + JCAA
FAIRer-data paper); self-pitch credential fragments added.
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
**Alignment.** We propose to build LLM-assisted assessment and reproduction infrastructure that makes verification of published research inexpensive enough to be routine, so that trust in a publication is earned through open contestation rather than presumed from authority. The pipeline implements contestation literally: every reproduction is audited by an adversarial AI reviewer with no memory of the work it audits, and its challenges are published alongside the verdict. The aim is to combine automated compliance checking and reproduction into a routine part of truth-seeking about published research.

**Problem.** Most published findings are never independently checked: verifying that analyses reproduce, that data and code are available and usable, and that evidence supports claims is skilled, tedious, unrewarded work. A landscape review in July 2026 found LLM-assisted reproducibility tools emerging in computer science and quantitative social science (which do not assess other credibility markers) alongside Findable, Accessible, Interoperable, Reusable (FAIR) evaluators and rigour-criteria presence checkers in biomedicine (which do not execute code). No system combines the two approaches, and none serves long-tail disciplines like most of the Humanities, Arts, and Social Sciences (HASS).

**Medium.** Open-source code plus a public demonstration: an agentic pipeline (Docker-based reproduction, FAIR scoring, fresh-context adversarial review), a results dashboard, and a human-verification interface where domain experts audit sampled AI verdicts — AI and human checks by design.

**Plan.** Our pilot system already decomposes a paper into a graph of claims (explicit and implicit), evidence, methods, and research designs, and evaluates claim–evidence strength and method appropriateness. This project builds the verification lanes: computational reproduction and FAIR assessment of data and software. Work to date focuses on archaeology, an interpretive field discipline serving as a bridgehead: its primary observations are unrepeatable (excavation consumes its own evidence; survey assesses a changing landscape), yet it has a computational core where reproduction is tractable.

A completed pilot ran five Journal of Archaeological Science (JAS) papers through the full stack, yielding four successful and one partial reproduction and finding that data availability, not code availability, predicts whether a paper reproduces. The pilot also caught two calculation errors that peer review had missed.

Four confirmatory hypotheses (and a pre-specified exploratory analysis) are preregistered on the Open Science Framework (osf.io/dqnhg). In 90 days we will: (1) convert the piloted workflow into an autonomous agentic pipeline with deterministic quality gates and batched human approval; (2) regression-test it against pilot artefacts; (3) run a FAIR census of JAS 2022–2026, with a control series from its sister journal (JAS: Reports), and reproduce the eligible computational subset; (4) publish the dashboard and verification interface, with expert spot-audits of sampled verdicts.

**Success.** A public census of open-science practice in a flagship archaeology journal, with every reproduction verdict traceable to artefacts anyone can re-run; preregistered answers to live questions (did JAS's January 2024 mandatory reproducibility-review policy actually change practice?); and a measured per-paper cost showing verification can be routine rather than heroic. The framework is long-tail-native and extensible: the same claims-evidence core will carry verification beyond the computational as the programme grows.
<!-- proposal-body-end -->

## Drafting choices — Shawn's verdicts (2026-07-07)

1. First person singular ("I") — **confirmed**. ~~SUPERSEDED~~ 2026-07-21: body voice
   changed to "we" after Brian Ballsun-Stanton joined as named collaborator (field 18);
   the field 6 self-pitch remains first-person singular (it is a pitch-yourself field).
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
fallback below is moot. The lodgement-time embargo (double-blind contingency) was
**LIFTED 2026-07-21** after the journal-policy check cleared all three candidate
venues; the registration is publicly resolvable (verified by anonymous API) with
**DOI 10.17605/OSF.IO/DQNHG** — the submission gate is closed.

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
submission. Every specific below is source-backed (scout-reports series 2026-07-07/08;
the variability-analysis report; the working-notes register; both CVs).

> **Reliability.** The credibility-assessment stack has been stress-tested for the failure
> mode most cited against LLM assessors: 25 independent runs (five papers, five runs each)
> yielded 96% verdict stability, reported as a first-class reliability metric — a practice
> almost absent from the LLM-as-assessor literature (the nearest published analogue treats
> repeated-run quality scores as probability distributions; Thelwall & Yang 2025).
>
> **Positioning.** A two-stage landscape review (July 2026; every bibliographic and
> repository claim re-verified against authoritative sources by independent audit agents)
> found no published or preprint system combining computational reproduction, FAIR
> assessment, and adversarial review for any HASS discipline. The nearest neighbours
> — the Center for Open Science's funded ReplicatorBench and the Institute for
> Replication's announced, pre-release replication engine — serve quantitative social
> science and re-execute analyses without scoring openness or credibility. No published work validates LLM scoring of the GO-FAIR
> sub-principles against human raters; the FAIR-evaluation literature itself calls for
> exactly this (Candela et al. 2024). The registered design addresses that gap directly,
> with a preregistered subsample of 12 census papers hand-scored by the registrant,
> blinded to machine scores, and per-sub-principle agreement and Cohen's kappa reported.
> A separate grey-literature guard pass (OSF/SocArXiv, Zenodo, Humanities Commons,
> DataCite, and six archaeology venues; 26 logged queries, July 2026) confirmed the
> null: to our knowledge, no prior work applies large language models to assess,
> extract from, or reproduce archaeological research (the nearest item, Spennemann
> 2023, audits the model rather than the literature). This proposal complements,
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
> in the web-search layer. A parallel internal audit measured a ~10% error rate in
> agent-relayed specifics absent source re-verification. The pipeline's deterministic
> gates exist to catch exactly that measured failure mode. The method the grant funds is
> the method that produced this application's evidence.
>
> **Delivery and follow-on.** The pipeline ships as open-source code, as installable
> agent skills for the Claude and Codex ecosystems, and as a self-hostable runner (built
> by collaborator Brian Ballsun-Stanton), so any group can run the verifier on its own
> literature rather than trusting our dashboard. FAIR for Research Software (FAIR4RS)
> scoring of code artefacts is a named next step, pre-committed in the registration to a
> dated amendment path and the same reliability protocol before use. Beyond the
> registration's CC BY 4.0 licence, census and reproduction data tables will be
> deposited under CC0, and archival costs are zero by design (Zenodo, OSF), keeping the
> budget open-by-default.
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

## Applicant affiliation (fields 1–5; decided 2026-07-21, CV-verified)

Primary: Honorary Professor of History and Archaeology, School of Humanities, Macquarie
University (Feb 2026–present). Secondary where the form allows: Co-Founder and Director,
Electronic Field Notebooks Pty Ltd (EFN). Rationale: the honorary MQ line matches the
author line on the frozen pilot report; EFN evidences the infrastructure-builder claim.
Contact identifiers on the CV: ORCID 0000-0002-6492-9025; shawn@fieldnote.au.

## Field 18 — collaborators (added 2026-07-21; CV-verified)

Dr Brian Ballsun-Stanton (Lecturer, Faculty of Arts, Macquarie University; ORCID
0000-0003-4932-7912) — packages the pipeline as installable Claude and Codex agent
skills and builds the self-hostable runner for public deployment. Role from Brian's own
feedback (relayed by Shawn, 2026-07-21): "ship it as a claude, codex skill", "build it
into a self-hostable runner online". Supporting credentials from his CV (2026-06-01):
FAIMS founding data architect (2012); winner, Macquarie Vice-Chancellor's Excellence in
Research Integrity Award 2025, for leading the university's responsible-AI-in-research
framework (40+ workshops, 1,500+ researchers trained); AI and NLP skills listed include
prompt and harness engineering and LLM deployment on HPC. He has no JAS or *JAS:
Reports* papers in the census window; if his role makes him study personnel, prereg §5
criterion 5 (study-personnel papers excluded from reproduction) applies automatically at
no practical cost.

**Team-pedigree line (candidate for field 19 or self-pitch, CV-verified):** the
applicant and collaborator co-authored the chapter introducing preregistration of
research design to archaeology (Ross & Ballsun-Stanton 2022, in *Digital Heritage and
Archaeology in Practice*, University Press of Florida) and the FAIMS FAIRer-data paper
(Ross et al. 2022, *Journal of Computer Applications in Archaeology*,
doi:10.5334/jcaa.96) — preregistration and FAIR are not new commitments for this team.

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

Steer (Shawn, 2026-07-21): lead with what we have done — infrastructure built, products
and teams managed at national and international scale, complementing the academic
background — not memberships or fellowships. Both candidates verification-corrected
(pilot outcome = four complete + one partial, not "reproduced five").

1. Archaeologist and open-infrastructure builder: co-founder and director of EFN
   (Fieldmark), which commercialised the FAIMS field-data platform, and formerly
   product manager of the RAiD persistent identifier — delivered into the European
   Open Science Cloud — and manager of the national-infrastructure products team at
   the Australian Research Data Commons. My verification pipeline has run five
   published archaeology papers through full reproduction, reproducing four
   completely and catching calculation errors that peer review missed.
2. I am an archaeologist working in the discipline's half-century-old quantitative
   tradition (Computer Applications and Quantitative Methods in Archaeology, founded
   early 1970s), and I build open research infrastructure, from the FAIMS field-data
   platform to national persistent-identifier services. My pipeline has run five
   published papers through full reproduction, reproducing four completely, and
   caught calculation errors that peer review missed.

Credential fragments to weave in, all CV-verified (2026-07-21), done-things first per
the steer: took FAIMS from research grants to commercial spin-out (EFN/Fieldmark;
CSIRO bushfire-recovery monitoring contract); managed ARDC teams delivering Research
Data Australia, Research Vocabularies Australia, and Persistent Identifier Services;
RAiD delivered as a European Open Science Cloud component (FAIRCORE4EOSC); led
Macquarie's research-data transformation (5,000+ researchers); co-introduced
preregistration of research design to archaeology (Ross & Ballsun-Stanton 2022);
41 publications including a 2023 *Nature* co-authorship; AUD $4.8M competitive grant
income ($2.6M as lead chief investigator); Honorary Professor, Macquarie.

### Grant request (field 14) — worked candidate

**US$8,000** (form integer: 8000). Composition (framing §6 lines plus Brian's runner):

| Line | US$ | Justification |
|------|-----|---------------|
| Inference credits, two vendors | 4,000 | Anthropic + OpenAI; cross-model verification is methodological, not redundancy |
| Cloud compute for reproductions | 1,200 | Long jobs off the local host; host-independence is itself a reproducibility claim |
| Hosting + domain (dashboard, runner, skills distribution) | 500 | The clickable public demo; Brian's runner distribution |
| Human-verification honoraria | 1,000 | Strengthens "AI and human checks"; framing §6 flags the admin overhead — confirm deliberately |
| Dissemination (CAA contribution) | 600 | The discipline's computational-methods community (framing §6) |
| Contingency (~10%) | 700 | |
| Archival | 0 | Zenodo + OSF free by design — say so in the application |

Lean variant without honoraria: ≈ US$7,000. Range anchor from framing §6: US$1k–10k as
a signal of scope and seriousness, not a funding plan.

## Final paste set (v0.6, post-verification — every form field, form order)

| Field | Entry |
|-------|-------|
| 1–5 name/email/phone/location | Factual. Suggested email shawn@fieldnote.au (CV contact); location Sydney, NSW, Australia. **Check the phone**: the CV letterhead renders "+61 1 04 758 300", which looks like a typesetting slip |
| 6 self-pitch | Candidate 1 above (recommended; candidate 2 as alternate) |
| 7 website | No personal site on the CV — EFN/Fieldmark company site (Shawn supplies URL) or leave blank |
| 8 LinkedIn / 9 X / 11 Substack | Shawn supplies or blank (form says optional fields aid review) |
| 10 GitHub repository | <https://github.com/saross/llm-reproducibility> (visibility re-confirmed PUBLIC 2026-07-21) |
| 12 CV upload | `~/Downloads/Ross_CV_Cosmos_Institute.pdf` (tailored copy, 15 pp) |
| 13 stream | Select the verbatim option "AI and Truth-seeking: Cosmos x FIRE" |
| 14 grant request | **8000** (integer, USD); lean variant 7000 without honoraria — see table above |
| 15 title | Recommended: candidate 2, "Cheap Enough to Check: AI-Assisted Reproduction and Openness Scoring of Published Archaeological Science" — echoes the body's "cheap enough to be routine"; candidates 1 and 3 as safer descriptive alternates |
| 16 one-liner | Candidate 1 above (recommended) |
| 17 proposal | Paste the body between the proposal-body markers (499/500 after the v0.7 revision; underlying claims verified by two independent passes 2026-07-21, new phrasings re-checked against the synthesis and registration) |
| 18 collaborators | Paste block below |
| 19 website / additional info | Paste block below: two project links, then the field 19 evidence pack above (trim to any form limit) |
| 20 how-did-you-hear | Factual — the help text asks for recommenders' names if any; Shawn supplies |
| 21 applicant agreement | Shawn ticks (note: submitters are auto-added to the Cosmos Substack) |

### Field 18 paste block

> Dr Brian Ballsun-Stanton (Lecturer, Faculty of Arts, Macquarie University) — packages
> the pipeline as installable Claude and Codex agent skills and builds its self-hostable
> runner. FAIMS founding data architect; winner of Macquarie's 2025 Vice-Chancellor's
> Excellence in Research Integrity Award for leading the university's
> responsible-AI-in-research framework. With the applicant he co-authored the chapter
> introducing preregistration of research design to archaeology (Ross & Ballsun-Stanton
> 2022) and the FAIMS FAIRer-data paper (Journal of Computer Applications in
> Archaeology, 2022).

### Field 19 paste block — lead with the links

> Preregistration: https://osf.io/dqnhg/ (OSF Open-Ended Registration, lodged
> 2026-07-20; DOI 10.17605/OSF.IO/DQNHG).
> Project repository: https://github.com/saross/llm-reproducibility
>
> [then the field 19 evidence-pack paragraphs above]

## Remaining at submission (Shawn)

- Select and edit the candidates above (affiliations now resolved from CVs)
- Field 20 (how-did-you-hear) — factual, Shawn supplies
- Optional profile links (website, LinkedIn, X, Substack) — form says they aid review;
  from the CVs: Brian lists techethicsai.au; Shawn's CV carries ORCID only
- [x] 2026-07-21 Lift the OSF embargo and verify <https://osf.io/dqnhg/> resolves
  publicly with DOI (lifted by Shawn; verified via anonymous API: public, accepted,
  DOI 10.17605/OSF.IO/DQNHG)
- Trim field 19 to any form limit at submission (guard-pass null folded in 2026-07-08;
  source: scout-reports/2026-07-08-g1-archaeology-guard-null-result.md)
