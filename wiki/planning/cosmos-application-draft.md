# Cosmos Grants Application — Working Draft

**Version:** 0.1
**Date:** 2026-07-07
**Status:** Proposal draft v0.1 for co-development with Shawn; title, one-liner, self-pitch,
and grant amount not yet drafted
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
   reproducibility (Shawn's caution).

## Proposal draft v0.1 (form field 17, <500 words)

<!-- proposal-body-start -->
**Alignment.** I am applying to the AI x Truth-seeking stream to build infrastructure that
makes verification of published research cheap enough to be routine — so that trust in a
paper is earned through open contestation rather than presumed from authority. The pipeline
implements contestation literally: every reproduction is audited by an adversarial AI
reviewer running in a fresh context, with no memory of the work it audits, and its
challenges are published alongside the verdict. The aim is not compliance policing but
lowering the cost of checking until open inquiry into published claims is normal.

**Problem.** Most published findings are never independently checked: verifying that numbers
reproduce, that data and code are usable, and that evidence supports claims is skilled,
tedious, unrewarded work. Existing reproducibility infrastructure serves biomedicine and the
quantitative social sciences; the humanities, arts, and social sciences (HASS) have been
left out. Archaeology is the ideal bridgehead — an interpretive field discipline whose
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
availability, predicts whether a paper reproduces. In 90 days I will: (1) convert the
piloted workflow into an autonomous agentic pipeline with deterministic quality gates and
batched human approval; (2) regression-test it against pilot artefacts; (3) preregister five
hypotheses on the Open Science Framework; (4) run a FAIR census of JAS 2023–2026 and
reproduce the eligible computational subset; (5) publish the dashboard and verification
interface, with expert spot-audits of sampled verdicts.

**Success.** A public, clickable census of open-science practice in a flagship archaeology
journal, with every reproduction verdict traceable to artefacts anyone can re-run;
preregistered answers to live questions (did JAS's 2024 mandatory reproducibility policy
change practice?); and a measured per-paper cost demonstrating that verification can be
routine rather than heroic. The framework is HASS-native and extensible: the same
claims–evidence core will carry verification beyond the computational as the wider
programme grows.
<!-- proposal-body-end -->

## Drafting choices awaiting Shawn's reaction

1. First person singular ("I") throughout — standard grant voice; adjust if preferred.
2. The 25-run variability study is *omitted* from the proposal for word budget; candidate
   for form field 19 ("additional info") along with the follow-on-funding pointer
   (framing §5) and the Metalens-complementarity line — none of these burn proposal words.
3. The JAS January 2024 policy question is named as the concrete success hook (it is
   preregistration hypothesis H1 in the pilot findings report §7).
4. The human-verification interface is a committed deliverable; the *stretch* framing
   (per framing §5) applies only to adding sampled claim–evidence pairs from the pilot
   extractions — currently not mentioned in the 500 words; could be one clause if wanted.
5. "A flagship archaeology journal" rather than "archaeology's flagship journal" —
   deliberately hedged.
6. Discourse-engagement analysis (Shawn's future-capability list) summarised only as
   "how papers use — and ignore — the literature" to hold the word budget.

## Still to draft (other form fields)

- Project title (field 15)
- One-sentence project description (field 16)
- Self-pitch, 1–2 sentences (field 6)
- Grant request integer (field 14) — refine from framing §6 brainstorm
- Field 19 "additional info" paragraph (see choice 2 above)
