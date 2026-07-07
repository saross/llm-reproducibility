# Cosmos Grants Application — Working Draft

**Version:** 0.2
**Date:** 2026-07-07
**Status:** Proposal draft v0.2 — Shawn's verdicts on all six drafting choices applied;
policy-question hook sharpened in Success; title, one-liner, self-pitch, and grant amount
not yet drafted
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
preregistered answers to live questions (for example: did JAS's January 2024 mandatory
reproducibility-review policy actually change practice?); and a measured per-paper cost demonstrating that verification can be
routine rather than heroic. The framework is HASS-native and extensible: the same
claims–evidence core will carry verification beyond the computational as the wider
programme grows.
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

## Preregistration sequencing (recommendation; awaiting Shawn's decision)

Question (Shawn, 2026-07-07): lodge the OSF preregistration before submitting the
application, so the application links a live registration?

Recommendation: **yes — draft immediately, lodge before submission.** The prereg must
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

## Still to draft (other form fields)

- Project title (field 15)
- One-sentence project description (field 16)
- Self-pitch, 1–2 sentences (field 6)
- Grant request integer (field 14) — refine from framing §6 brainstorm
- Field 19 "additional info" paragraph (see choice 2 above)
