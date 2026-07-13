# Agentic Modernisation Plan — Reproduction and Open-Science Apparatus

**Version:** 0.3
**Date:** 2026-07-07
**Status:** Direction approved — study shape decided (Option A, §6, 2026-07-03); Phase 0
complete; Phase 1 build ON HOLD — guided review walkthrough done 2026-07-07; six judgement
calls recorded (§9) awaiting Shawn's verdicts
**Author:** Claude (Fable 5), with Shawn Ross
**Supersedes:** Extends (does not replace) `wiki/planning/automation-and-scaling-strategy.md` (2025-12-09)

---

## 1. Purpose

Plot the path from the current session-per-pass, human-driven pipeline to a modern agentic
implementation — subagents, workflows, and deterministic orchestration gates — starting with
the most contained subsystem: the **reproduction workflow** plus the **open-science/FAIR
(Findable, Accessible, Interoperable, Reusable) assessment lane**. The near-term goal is a
production run over recent Journal of Archaeological Science (JAS) articles, building on the
completed and successful Phase 1 pilot (5/5 papers, 4 SUCCESSFUL, 1 PARTIAL reproduction
verdicts; see `studies/open-science-compliance/reports/pilot-findings-report.md`).

## 2. Why now: what changed in the harness

The December 2025 automation strategy rejected headless automation for two reasons, both now
resolved by the Claude Code harness itself:

1. **Context management.** Sessions could not monitor their own context; session boundaries
   doubled as context-management boundaries. Now every pipeline stage runs in a *fresh
   subagent context* by construction, and orchestration state lives in workflow scripts, not
   in a single long conversation.
2. **Artefact-persistence enforcement.** The v1.0 reproduction review found 2 of 5 pilot
   papers had no artefacts on disk despite queue entries claiming completion
   (`outputs/reproduction-system-review-v1.0.md`, issue C1). Skills could *specify* save
   locations but not *enforce* them. Workflow orchestration code can gate every stage
   transition on deterministic file checks (exists, non-empty, parses).

A third change is a direct gift to this project: the adversarial review session (R-C)
*requires* a fresh context with no memory of the reproduction. In the old harness this
demanded a manual new session; a subagent provides the guarantee architecturally.

## 3. Current state (verified 2026-07-03)

- **Pilot complete.** All 5 JAS papers through extraction (Pass 0-7), classification and
  credibility assessment (Pass 8-9), FAIR scoring (15 binary GO-FAIR sub-principles, data
  and code scored independently), and Docker-based reproduction with adversarial review
  coverage documented in the pilot findings report.
- **Headline pilot finding:** data availability — not code availability or environment
  specification — was the dominant predictor of reproduction outcome. Five Phase 2
  hypothesis candidates drafted (H1-H5, pilot findings report).
- **Reliability licence for scaling:** the 25-run variability test
  (`outputs/variability-test/variability-analysis-report.md`) showed assessment verdicts and
  scores are stable across runs (aggregate score CV 1.9-3.4%); a single run per paper
  suffices for assessment-grade output.
- **Scaffolding is pre-agentic:** two skills (`research-assessor` v2.6,
  `reproduction-assessor` v1.1), session prompts, CLAUDE.md. No project agents or workflows
  exist yet.
- **Interface artefacts already file-based:** each reproduction session consumes and
  produces files in `outputs/{slug}/reproduction/attempt-{NN}/` — the sessions are already
  loosely coupled enough to become subagents without redesigning the artefact set.
- **New asset since the pilot:** PR #1 (merged 2026-06-07, from the paper-b project) added a
  matching-grade PDF extraction layer to `extraction-system/scripts/pdf_processing/` —
  per-page text with page indices and section locators, normalisation for deterministic
  quote checking, and promoted cleaners (24/24 tests). Directly reusable for Phase 3 corpus
  tooling. One known defect is logged (lossy de-hyphenation of genuine compounds,
  `wiki/continuity.md` task C).
- **Cross-session state now lives in `wiki/continuity.md`** (seeded 2026-06-07). Its
  pending tasks: A — untrack committed `venv/` (mechanical); B — migrate docs to the wiki
  layout (has an open decision on `docs/` disposition); C — the de-hyphenation fix.

## 4. Target architecture

### 4.1 Project agents (`.claude/agents/`)

| Agent | Replaces | Responsibilities | Judgment level |
|-------|----------|------------------|----------------|
| `fair-assessor` | Manual Pass 0 + Pass 6 + FAIR scoring | Metadata, infrastructure extraction, FAIR sub-principle scoring, data-availability inventory (5-level taxonomy) — **without** the full 8-pass extraction | Medium |
| `reproduction-planner` | Session R-Plan | Paper read, repo/data landscape, Type A/B/C/D classification, verification-target enumeration, risk assessment, `reproduction-plan.md` | High |
| `reproduction-executor` | Sessions R-A + R-B | Materials acquisition, Docker build-fix loop, script adaptation (wrapper rules unchanged), execution, quantitative comparison, verdict, artefact writing | Medium-high |
| `adversarial-reviewer` | Session R-C | 5-dimension sceptical audit from artefacts only; fresh context guaranteed by the subagent boundary | High |
| `corpus-screener` | (new) | CrossRef/OpenAlex sweep of JAS issues, open-access status, computational-component screening, language triage (R vs Python vs other) | Medium |

The existing skills remain the knowledge base (decision frameworks, Dockerfile and wrapper
pattern libraries, discrepancy taxonomies); agents reference them rather than duplicating.

### 4.2 Workflows

- **Plan-triage workflow:** fan `reproduction-planner` out over the queue → collect plans →
  produce a single triage report (feasibility, type, estimated compute, risks, data-access
  levels) for **batched human approval**. Human attention is batched, not eliminated.
- **Execution workflow:** pipeline approved papers through prep → execute → verify →
  adversarial review, with deterministic gates between stages (Docker image builds; script
  parses; expected artefacts exist and are non-empty; queue updated). Long-running jobs
  (>1 h) route to a designated compute host and re-enter the pipeline on completion.
- **FAIR-lane workflow:** fan `fair-assessor` over the full corpus independently of
  reproduction — this is the cheap lane that scales to a census.

### 4.3 Invariants preserved from v1.1 (non-negotiable)

1. Plan before execution; **human approval of plans** before any compute spend (batched).
2. Change *how* code runs, never *what* it computes (wrapper cardinal rule).
3. Every verification target accounted for — no silent scope reduction.
4. Adversarial review runs for **every** paper, always in a fresh context.
5. All execution inside Docker; host contamination is a review-detectable failure.
6. Artefact persistence verified by the orchestrator, not asserted by the agent.

### 4.4 Human-in-the-loop points (redesigned, not removed)

- Batch plan approval (triage report; approve/hold/reject per paper).
- Escalation queue: QUALIFIED or CHALLENGED adversarial reviews, PAPER_ERROR findings, and
  CANNOT_COMPARE calls surface for human confirmation before entering study data.
- Spot-check sampling of SUCCESSFUL verdicts (e.g. 1 in 5) against artefacts.

## 5. Phased path

### Phase 0 — Housekeeping ✅ (2026-07-03)

Version-drift reconciliation: manifest v3.0.1, cluster_1 prompt v1.1 recorded,
assessment_json schema entry added, `active-todo-list.md` and `wiki/planning/README.md` brought
up to date, study README Phase 1 marked complete.

### Phase 1 — Build the agentic lane

**Prerequisite (added 2026-07-13):** implement the corpus-management redesign in
`corpus-management-plan.md` (out-of-tree corpus store; DOI manifest + fetch-with-checksum
script; LFS/pre-commit guardrails) BEFORE the census acquires papers at scale — it
prevents the third-party-content-in-history failure mode that required the 2026-07-13
`git filter-repo` purge, and the corpus-screener agent consumes the manifest directly.

- Author the five agent definitions; wire the three workflows.
- Add deterministic gate scripts (artefact checklist verification, Docker build/parse
  checks, queue updates) under `scripts/`.
- Parameterise the compute-host assumption (currently hard-coded to `sapphire` in prompt 02
  §1.2 and SKILL.md §D) so local vs remote is a config value, not prose.
- Reconcile the reproduction prompt/skill version story (prompts v1.0, skill v1.1) while
  migrating their content into agent definitions.

### Phase 2 — Regression-test the harness on pilot papers

Re-run two fast pilot papers (herskind-riede-2024 and dye-et-al-2023; both ~30 s compute)
through the new pipeline as `attempt-02`, then compare verdicts, comparison tables, and
adversarial review outcomes against the pilot's `attempt-01` artefacts. **Pass criterion:**
same verdicts, same value-level matches, no new unexplained discrepancies. No new data is
examined, so this is preregistration-safe.

### Phase 3 — Corpus tooling and the JAS run

- Build the sampling frame: JAS 2023-2026 sweep via CrossRef/OpenAlex; screen for
  open-access status and computational components; triage analysis language.
- Run the FAIR lane and reproduction lane per the study-shape decision (§6).
- **Cost gate:** measure per-paper cost (tokens, wall-clock, human minutes) on the first
  2-3 papers and present the N× aggregate for explicit approval before scaling. "The last
  few years of JAS" could be 20 papers or several hundred depending on screening criteria —
  these are different commitments and will be priced before launch.

## 6. Study shape — DECIDED: Option A (census + preregistered subset)

**Decision (Shawn, 2026-07-03):** Option A. Preregister the five pilot hypotheses on OSF
first; sweep JAS 2023-2026 as a descriptive FAIR census (which doubles as the sampling
frame); reproduce the eligible computational subset as the preregistered confirmatory
study. Options B and C below are retained for the record.

The protocol (`studies/open-science-compliance/protocol/study-protocol.md`) requires OSF
preregistration of Phase 2 hypotheses **before** Phase 2 corpus selection. FAIR scores are
the independent variable in H1/H2, so computing FAIR scores over the corpus before
preregistering would contaminate the confirmatory design.

| Option | Shape | Trade-off |
|--------|-------|-----------|
| **A. Census + preregistered subset** (recommended) | Preregister H1-H5 first; sweep JAS 2023-2026 as a descriptive FAIR census; reproduce the eligible computational subset as the confirmatory study | Two publishable outputs; census doubles as sampling frame; largest scope |
| B. Protocol as written | Preregister; select 15-25 fresh papers; full pipeline on those only | Cheapest and cleanest; leaves the population-level question unanswered |
| C. Engineering first | Complete Phases 1-2, measure throughput, then decide | Defers the decision at no methodological cost |

Phases 0-2 are identical under all three options.

## 7. Risks and mitigations

| Risk | Mitigation |
|------|------------|
| ScienceDirect returns HTTP 403 to programmatic PDF/supplement downloads | Manual acquisition step in corpus tooling; known CDN workaround documented in pilot notes; treat as a FAIR finding in its own right |
| R-only reproduction scope; JAS corpus will include Python papers | Language triage at screening; defer non-R reproductions in first run; Python extension (documented extension points) as a follow-on phase |
| Harness/model drift vs pilot-era results | Phase 2 regression test before any new-corpus runs |
| Preregistration contamination | Study-shape decision (§6) resolved before Phase 3; Phases 1-2 touch no new data |
| Long-running jobs (multi-hour MCMC) in an autonomous pipeline | Detached Docker execution with orchestrator polling; compute-host parameterisation (Phase 1) |
| Cost blow-out at corpus scale | Hard cost gate after first 2-3 Phase 3 papers (§5) |

## 8. Relationship to existing plans

- `wiki/planning/automation-and-scaling-strategy.md` — this plan implements that document's
  long-term option ("API pipeline replicating skills") using native harness workflows; its
  quality arguments for human-attention batching are retained.
- `wiki/planning/credibility-implementation-plan-v2.0.md` — untouched; the full credibility
  assessment pipeline is out of scope for this modernisation phase and can be agentised
  later using the same pattern.
- `wiki/planning/fair-vocabularies-development-plan.md` — the FAIR-lane census would generate
  exactly the evidence base that plan needs; potential convergence in Phase 3.

## 9. Open judgement calls from plan review (2026-07-07)

Recorded from the guided walkthrough (Claude, with Shawn) so the revival can resume without
reconstructing them. Phase 1 remains ON HOLD until Shawn returns verdicts on these. Walkthrough
recommendation: **go**, with items 1, 3, and 5 folded into Phase 1–2 scope.

1. **The FAIR-lane reliability licence is thinner than §3 states.** The 25-run variability
   test (`outputs/variability-test/variability-analysis-report.md`, dated 2025-12-06, re-read
   2026-07-07) covered the extraction → *credibility assessment* pipeline (96% verdict
   stability) and never mentions FAIR. FAIR sub-principle scoring stability is untested — yet
   FAIR scores are the independent variable in preregistered H1/H2. Proposed fix: a small FAIR
   variability spot-check (~3 pilot papers × 3 runs; pilot papers only, so
   preregistration-safe) folded into Phase 2.

2. **Pilot-vs-census FAIR comparability.** Pilot FAIR scores were computed on top of full
   8-pass extractions; the census `fair-assessor` would score from a lighter Pass 0 + Pass 6
   path. If pilot and census papers ever sit in one analysis, that is a method change
   mid-dataset. The item-1 spot-check can test both concerns at once (does the lightweight
   path yield the same scores?).

3. **Internal contradiction to resolve before building.** §4.1 says agents *reference* the
   existing skills rather than duplicating them; the Phase 1 task list (§5) says "migrating
   their content into agent definitions". Opposite maintenance stories. Walkthrough
   recommendation: reference-not-duplicate — skills remain the single source of truth for
   decision frameworks and pattern libraries; agent definitions stay thin (role + routing).

4. **R-A + R-B merge into `reproduction-executor`.** The executor verifies its own
   preparation; the genuinely load-bearing fresh-context boundary (R-C adversarial review) is
   preserved. Walkthrough view: the merge is acceptable — noted for the record.

5. **Phase 2 pass criterion needs a pre-committed drift clause.** Pilot artefacts were
   produced by earlier models. Decide *in advance* what counts as benign drift (prose
   differences, Docker build iteration counts) versus failure (verdict or value-level
   changes), or the regression test's verdict becomes a post-hoc judgement call.

6. **Sequencing opportunity: Open Science Framework (OSF) preregistration × Cosmos grant.**
   Preregistration must precede the FAIR census anyway (§6); a live preregistration by
   mid-July would be a concrete artefact for the 26 July 2026 Cosmos Institute application.
   Drafting the preregistration is independent of the Phase 1 hold and can run in parallel.
