# Cosmos Institute Grant — Application Framing

**Version:** 0.1
**Date:** 2026-07-05
**Status:** Framing agreed (project choice + pitch shape); budget section is brainstorm-grade,
for refinement before submission
**Author:** Claude (Fable 5), with Shawn Ross
**Provenance:** Externalised from a personal-assistant hub session (2026-07-05) so the
candidate evaluation could compare projects *across* repositories (especially the paper-b
alternative) rather than being framed from inside any one of them.

---

## 1. Grant facts (verified 2026-07-05)

- **Programme:** Cosmos Grants — "AI x Truth-seeking" track, run with the Foundation for
  Individual Rights and Expression (FIRE).
- **Deadline:** Sunday 26 July 2026. Rolling review; decisions ~4 weeks after submission,
  so submitting in the week of 7 July targets a decision in early August.
- **Amount:** US$1k–10k+, for a **90-day build project**.
- **Format:** Airtable application form. Anyone eligible; individuals fine; existing
  efforts accepted.
- **Selection criteria (stated):** "clarity of purpose, technical feasibility, and a
  commitment to truth-seeking"; the programme funds AI that "empowers open inquiry rather
  than suppresses it", surfacing counter-arguments and flagging uncertainties.
- **Selectivity calibration:** cohort 1 selected 27 builders from 300+ applications (~9%).
  Concrete, demonstrated feasibility is a genuine differentiator.
- Sources: [round announcement](https://blog.cosmos-institute.org/p/cosmos-grants-are-back),
  [first-cohort post](https://blog.cosmos-institute.org/p/introducing-the-first-cohort-of-ai),
  [second-cohort post](https://blog.cosmos-institute.org/p/ai-x-truth-seeking-grant-winners),
  [grantee directory](https://community.cosmos-institute.org/).

## 2. Project-choice decision

**Decision (2026-07-05): base the application on this repository (llm-reproducibility).**

Candidates evaluated across repositories:

| Candidate | Assessment |
|-----------|------------|
| **llm-reproducibility** (this repo) | **Chosen.** A build, not a paper; completed pilot (5/5 Journal of Archaeological Science papers end-to-end, 4 SUCCESSFUL / 1 PARTIAL reproduction verdicts); approved 90-day-shaped next phase (agentic modernisation plan → JAS production run); clean track fit |
| Paper-b-derived verification tool (decompose outputs into claims → fresh-context / orthogonally-framed review → sampled human verification via a purpose-built interface) | Considered seriously; **folded in rather than pitched separately** — see §3 and §4. Core mechanism overlaps a crowded funded cluster; lower maturity (new build extracted from paper-b's AB+ scripts vs a finished pilot here) |
| Other active projects (map-reader, inscriptions, etc.) | Papers in their end-game, not 90-day builds; not competitive for a prototype-funding programme |

## 3. Portfolio proximity scan (all five Cosmos programmes, 186 grantees)

Swept the full grantee directory (Fellowship 30, Grants Team 4, AI x Truth-seeking 47,
General Track 74, AI-Accelerated Scholarship 31) via the community-site API, 2026-07-05.

**Result: no project in the portfolio does computational reproduction or open-science
assessment of published research.** Nearest neighbours:

- **Metalens** (Johanna Einsiedler; Truth-seeking cohort 1, also AI-Accelerated
  Scholarship): interactive, continuously-updated **meta-analysis** platform — automated
  extraction of reported statistics for evidence synthesis. The *synthesis* layer;
  this project is the *verification* layer (re-executes analyses, checks the paper's own
  numbers, audits transparency). Complementary, not competing — and evidence the programme
  funds AI-for-science-credibility work.
- **Replication Radar** (Rhea Karty; General Track): despite the name, a relational
  knowledge graph of academic literature — metadata layer, not execution.

The claim-decomposition-and-verification space, by contrast, is the most crowded pattern
in the portfolio (Alexandria, Argument Debugger, Bridge, Hydrangea, Claim Drafter,
CoTShield, Whitebox Tools, Socratic Trident, formal-coherence hallucination detection).
This is what argues against pitching the paper-b-derived tool as a standalone application —
a reviewer would file it next to Alexandria/Argument Debugger regardless of internals.

## 4. Pitch framing

- **Track:** AI x Truth-seeking.
- **Headline:** reproduction-and-transparency pipeline for published research, **with AI
  and human checks** — the tool is the deliverable; the JAS production run (per the
  agentic modernisation plan, study-shape Option A) is the 90-day demonstration.
- **Frame:** the full verification stack — does the paper's evidence support its claims
  (argumentative layer); do its numbers reproduce (computational layer); can anyone check
  (FAIR — Findable, Accessible, Interoperable, Reusable — / transparency layer). The
  reproduction lane is the first production lane of that stack.
- **Differentiators to name explicitly:**
  - Completed pilot = unusual technical-feasibility evidence in a field where most
    grantees start from zero.
  - The fresh-context adversarial-review agent is a literal implementation of "open
    contestation of ideas" — say so in those terms.
  - The **sampled human-verification interface** (UX pattern proven in the map-reader
    project's feature-review app): most funded neighbours are AI-side; centring the human
    reviewer's ergonomics is the distinctive element, and it carries the paper-b
    decomposition-for-verification idea forward inside this pitch.
- **Tone:** making verification cheap enough that scientific claims can be openly
  contested and trust earned — not compliance policing.

## 5. Role of the extraction / credibility side of this repo

Three distinct roles; only the third is constrained:

1. **Frame — use fully.** The claim–evidence–method graph is the intellectually
   distinctive asset and speaks the portfolio's native vocabulary (claim-testing,
   evidence-vs-claims) applied to published science with a working implementation.
2. **Evidence of capability — use as track record.** Five papers through the complete
   stack (extraction, credibility assessment, FAIR scoring, reproduction); extraction
   quality-assurance system with stratified sampling; 25-run variability study showing
   verdict stability. Show it; don't promise more of it.
3. **90-day deliverable — exclude, with one cheap exception.** The 8-pass extraction is
   session-per-pass and expensive; the credibility metrics are self-declared exploratory
   (v1.0, "for iterative refinement"); and the build window must survive a possible
   return to full-time employment (~Aug 2026), so scope stays sized for out-of-hours
   delivery. **Exception:** the human-verification interface can present sampled
   claim–evidence pairs from the *existing* pilot extraction outputs alongside
   reproduction verdicts — full-stack vision demonstrated at near-zero marginal cost.
   Frame as a stretch goal.

**Follow-on pointer (one sentence in the application):** the extraction/credibility lane
is the natural follow-on; Cosmos mentions follow-on funding, and Metalens holds support
from two Cosmos programmes simultaneously — precedent for sequencing rather than
sacrificing the claims-vs-evidence work.

## 6. Budget brainstorm (beyond inference credits)

Context for later refinement: the primary motivations are **credibility and visibility**
for the project, secondarily **inference credits** for large-scale runs (Anthropic
Fable-class + the best available OpenAI model). At US$1k–10k the budget is a signal of
scope and seriousness, not a funding plan — anchor items to what makes the demonstration
*public, credible, and checkable*. Candidate lines:

- **Inference credits (core, already planned):** Anthropic + OpenAI Application
  Programming Interface (API) credits. Note the two-vendor line is methodological, not
  redundancy — cross-model verification/consensus is part of the design.
- **Cloud compute for reproductions:** modest virtual-machine hours for Docker-based
  reproduction runs. Two justifications: multi-hour jobs (e.g. Markov chain Monte Carlo
  reruns) shouldn't block the pipeline on a single local host, and running on commodity
  cloud hardware demonstrates the pipeline is host-independent — itself a reproducibility
  claim.
- **Hosting + domain for the public results dashboard / human-verification interface:**
  small annual cost, high visibility value. A browsable FAIR-census + reproduction-verdict
  site is the demo artefact reviewers and press can actually click.
- **Human-verification honoraria:** small payments for independent domain experts to
  adjudicate a sample of verdicts/claim–evidence pairs through the interface. Directly
  strengthens the "AI **and human** checks" pitch; adds admin overhead — decide
  deliberately.
- **Dissemination:** conference presentation contribution (e.g. Computer Applications and
  Quantitative Methods in Archaeology — CAA); preprint is free; an open-access article
  processing charge (APC) probably exceeds what this grant should carry — note that the
  confirmatory study targets a venue/route decided separately.
- **Data acquisition:** near-zero by design (corpus screened for open access); keep a
  token line for edge-case document delivery only if needed.
- **Archival: explicitly zero.** Zenodo/Open Science Framework (OSF) deposits and
  preregistration are free — worth *saying* in the application as evidence of an
  efficient, open-by-default budget.
- **Small contingency** (~10%).

## 7. Timing and constraints

- Submit **week of 7 July 2026** (rolling review → decision ~early August; deadline
  26 July is the hard stop).
- The application itself should be a **half-day artefact** (short form, small grant,
  ~9% selectivity rewards sharpness over length). The real decision is the scope of the
  90-day build, which §5 fixes: reproduction lane + FAIR census + human-verification
  surface; extraction lane excluded.
- Build window ≈ August–October 2026; deliberately sized to remain deliverable
  out-of-hours if full-time employment resumes in that window.

## 8. Next actions

1. Open the Airtable application form and capture its actual questions (scoping the
   half-day drafting session).
2. Draft responses against §4/§5 framing; refine budget from §6.
3. Confirm sequencing with the agentic modernisation plan phases (Phase 1 build is
   currently ON HOLD pending review — the application does not depend on it starting,
   but the 90-day plan narrative should match §5 of that document).
