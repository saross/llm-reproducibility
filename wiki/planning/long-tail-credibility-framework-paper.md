# Framework paper plan: long-tail research credibility assessment with AI

**Version:** 0.1
**Date:** 2026-07-13
**Status:** Externalised plan, not yet prioritised — Shawn will rank this against other
publications after finishing the current paper (week of 2026-07-13). Authorship model
(solo vs consortium) undecided; see §6.
**Origin:** Session discussion 2026-07-12/13, building on the verified scout sweeps of
2026-07-07/08 (`scout-reports/`, start at `2026-07-08-stack-positioning-synthesis.md`).

## 1. Concept and rationale

A second paper — separate from, and mutually reinforcing with, the computational
reproduction study — that stakes out the wider terrain: decomposing the problem of
assessing research credibility in humanities, arts, and social sciences (HASS) /
small-science / small-data / long-tail domains with AI assistance; surveying what exists
at each phase (verifier-backed, from the scout sweeps); demonstrating partial solutions
per phase from the project's pilots; and setting the agenda for what remains. Genre
precedents: the FAIR Guiding Principles paper, persistent-identifier roadmaps, the
preregistration/TOP manifestos — decompose-survey-demonstrate-propose papers that became
the reference point for their space.

Why it is worth doing (assessment of 2026-07-12):

- **Unique asset.** Nineteen adversarially verified landscape reports (~450 candidate
  works, ~2,300 re-checked claims, a documented 26-query archaeology null) mean the
  survey sections can be *documented* rather than asserted. Nobody entering this space
  soon will have equivalent coverage; the paper becomes what they must cite.
- **Precedence dynamics.** The competitor watch (report C1) found the empty middle
  converging from two sides — Chakravorti et al. 2026 (elicitation camp adding AI) and
  the Zhu et al. 2026 pair (LLM-scoring camp adding social science). A framework paper
  stakes the decomposition and vocabulary faster than any empirical study can.
- **Programme effect.** Each future lane paper (census, citation engagement,
  appropriateness) slots into a published roadmap; grant assessors read "component N of
  a published agenda" very differently from standalone papers.

Precedence realism: what actually establishes the stake is the triad of timestamped
preprint + OSF preregistration + released artefacts (Zenodo-DOI'd repo tag), plus the
named decomposition being adopted by others. Being the generous reference point beats
claiming firstness; competitors cited fairly become citers.

## 2. Conditions for success (from the 2026-07-12 assessment)

1. **Timestamp early, journal later.** Preprint on SocArXiv or MetaArXiv (DOI'd,
   HASS-native) as soon as the draft is solid; cross-link the OSF preregistration and a
   Zenodo release of the repo. Journal review can then take its time.
2. **The decomposition is the contribution, and it needs a name.** "Long-tail research
   credibility assessment" describes but does not brand. The "long tail of science"
   framing has lineage in the data-curation literature (Heidorn's "dark data in the long
   tail of science" — verify and read before anchoring). Name to be workshopped
   deliberately, not left to emerge from drafting.
3. **Decide the authorship model first** — it shapes tone, venue, and timeline (§6).

## 3. Proposed structure (phase × status matrix as organising device)

1. **Problem.** Why credibility assessment fails in the long tail: small heterogeneous
   data; narrative/interpretive methods; unrepeatable primary observation (excavation
   consumes its evidence); grey literature beyond the retrieval layer; and — decisive —
   no ground-truth replication corpora, which breaks ML-prediction approaches at the
   root (Crockett et al. 2023 becomes an ally, not an objection).
2. **The decomposition** (six phases = the project's lanes):
   - structured extraction (claims–evidence–methods graph, explicit + implicit);
   - methods/design assessment including *appropriateness* (not reporting presence);
   - verification lanes: computational reproduction + FAIR assessment;
   - credibility-signal synthesis (repliCATS-style, LLM-computed);
   - literature/discourse engagement (fairness + accuracy + coverage + discourse);
   - **reliability of the assessor itself** (repeated-run stability, adversarial
     verification, bias audits) — treated as a first-class phase; the sweeps showed
     nobody else does this, making it a distinctive move.
3. **Evidence-mapped survey per phase.** For each: solved (e.g. retraction checking via
   Crossref); transferable (MultiVerS + Sarol corpus + Liu verifiability metric as the
   accuracy engine, report C2; CORE-Bench difficulty tiers; aggreCAT aggregation);
   partial (scalar LLM quality scores from title+abstract, Thelwall line, report C1);
   missing for the long tail (appropriateness — zero citers on the only quality-scoring
   seed, report C3; implicit-methods inference as a named task, report S2; paper-side
   FAIR entry, report P5; discourse coverage, reports P6/S1; stability as a reported
   metric, report P4). Every cell cites a verified report. Optional meta move, light
   touch: the survey itself was run on the proposer/adversarial-verifier architecture
   the paper advocates, with a measured ~1% claim-error rate.
4. **Demonstrations, deliberately partial.** The five-paper pilot (four full, one
   partial reproduction; data availability — not code — predicting success); the
   25-run/96% verdict-stability result; implicit-claims extraction pilots. Feasibility
   per phase without overclaiming.
5. **Agenda.** What must be built; validation strategy where ground truth is absent
   (signals over binary replication; human-rater comparison; generalisability-theory
   reliability per Liu 2026/Thelwall & Yang 2025); community infrastructure asks (an
   annotated archaeology benchmark corpus is the obvious one); named risks
   (generalisation failure, bias per Thelwall & Kurt 2025, LLM monoculture); and the
   explicit boundary: assessment infrastructure is not automated gatekeeping (FAIR+CARE,
   equity thread per the Global South strand).

## 4. Evidence base (all in-repo, verifier-backed)

- `wiki/planning/scout-reports/` — 19 verified reports + synthesis + README index:
  P1–P6 (lanes), S1–S2 (arXiv blind spot), C1–C3 (deeper chains, competitor watch),
  G1 (archaeology guard null — first-mover claims must be scoped and worded
  "to our knowledge", with Spennemann 2023 cited and demarcated).
- Pilot artefacts: `outputs/*/reproduction/` and the pilot findings report (H1–H5).
- Zotero staging: eleven dated subcollections under My Library → staging hold every
  verified find for the reference list.

## 5. Venue analysis (from the sweeps' venue reads)

- **Primary: Royal Society Open Science** — hosts the conversation being joined
  (Wintle 2023, Heyard 2025, Hardwicke 2020, Lippert 2024 all surfaced there);
  takes long interdisciplinary pieces.
- **Strong alternative: Quantitative Science Studies** — the LLM-research-assessment
  corridor (Thelwall line; the likely reviewers) runs through Scientometrics/JDIS/QSS.
- PLoS ONE: publishable but weakest agenda-setting signal of the three.
- **PNAS: hold in reserve** — realistic only after the census yields a headline number
  ("N papers assessed at $X each"); front-matter Perspectives are effectively
  invitation territory.
- Discipline-facing translation (Advances in Archaeological Practice / JCAA /
  Internet Archaeology) is a later companion, not this paper.

## 6. Authorship model (OPEN QUESTION — Shawn deciding)

- **Solo route:** framed as an evidence-mapped *literature review and state of play*
  (explicitly not a manifesto), the verified survey carries the authority and solo is
  defensible. Shawn's current lean (2026-07-13).
- **Consortium route:** the manifesto genre's uptake historically comes from coalition
  authorship. Shawn has contacts at the Center for Open Science (COS), the Centre for
  Science and Technology Studies (CWTS Leiden), the Research Data Alliance (RDA), and
  other organisations who might be interested. Trade-offs: reach and legitimacy vs
  coordination time and dilution of the stake; a consortium version drifts toward
  principles/manifesto framing.
- Middle path: solo state-of-play paper now, consortium follow-on (principles,
  community benchmark) later — the review earns the invitation list.

## 7. Sequencing and next actions

Prioritisation deferred until Shawn's current paper is finished (week of 2026-07-13),
then ranked against: the Cosmos build + JAS census (empirical companion), the OSF
preregistration, and other queued publications.

When activated:

1. Decide authorship model (§6) — first, it shapes everything.
2. Workshop the name/handle (verify the Heidorn long-tail lineage first).
3. Skeleton draft: section-by-section with the phase × status matrix populated from the
   verified reports (Claude can generate this from the scout-reports corpus).
4. Draft → preprint (SocArXiv/MetaArXiv) + Zenodo repo release + cross-link to the OSF
   preregistration → journal submission (RSOS or QSS).
5. Deferred watch re-checks before submission (see continuity carry-forward): Chakravorti
   citers and the ReplicatorBench cluster (~2–3 months from 2026-07-08); Cheng & Khoo and
   Bolanos-Burgos citers (~3–6 months).
