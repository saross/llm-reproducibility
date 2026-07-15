# Agent content-routing design: skills, agents, and shared instruments

**Version:** 0.1
**Date:** 2026-07-15
**Status:** Draft for Shawn's review — resolves agentic-modernisation-plan §9 item 3
(reference-vs-migrate) with a routing rule rather than a binary. Intended as input to
`/review-implementation` and a prior-art-scout pass before Phase 1 build begins.
**Origin:** 2026-07-15 discussion of pull-failure risk (an agent instructed to read a
skill file may silently not read it, or fail the read and helpfully continue). Design
brief from Shawn: engineer for reliability first, accepting some duplication cost, but
split content cleanly between skills and agents, and among agents, so repetition never
creates update/maintenance drift.

---

## 1. The problem this solves

The agentic modernisation plan (v0.3) contains an internal contradiction flagged in its
§9 item 3: §4.1 says agents *reference* the existing skills; the Phase 1 task list says
skill content is *migrated into* agent definitions. These imply opposite maintenance
stories. Neither pure model is right:

- **Pure reference (pull):** a thin agent is told "Read file X before working". The
  content arrives only if the agent complies. Misses are *silent* — a scorer that never
  read the rubric still produces plausible scores. Per-invocation miss probability is
  low, but at census scale (300+ scoring invocations) even ~1% contaminates the
  dependent variable invisibly; and the most realistic variant is not disobedience but
  *error-then-continue* (a failed Read followed by "I know the FAIR principles anyway").
- **Pure migration (embed):** content is guaranteed in context, but every shared rubric
  is copied into several agent definitions. This repo has already logged that pathology
  (version history hand-maintained in four places — continuity task D), and duplicated
  instrument text breaks the preregistration's "instrument fixed at registration" claim,
  which must be auditable from a single file's git history.

## 2. The routing rule

Route each piece of content by *what happens when its delivery fails*:

| Class | Content type | Delivery | Failure mode if missing | Examples |
|---|---|---|---|---|
| **(a) Embedded** | Role behaviour: sequencing, stance, output contract, escalation rules | Written into the agent definition, imperative voice, tuned per role | N/A — always present | Executor's build-fix loop; reviewer's sceptic stance |
| **(b) Pushed** | Instruments: rubrics, taxonomies, verdict criteria — anything where two scorers diverging is a bug | Orchestrator inlines the canonical file verbatim into the task prompt at invocation | N/A — arrival is deterministic | FAIR instrument; availability taxonomy; verdict + precision definitions |
| **(c) Pulled** | Pattern libraries and troubleshooting knowledge, needed occasionally | Agent Reads the canonical file on demand (one hop, repo-rooted path) | **Loud** — a build fails and the agent goes looking; recoverable | Dockerfile patterns; wrapper-script patterns; PID systems guide |

The line between (b) and (c): if an unnoticed miss produces *plausible wrong output*
(silent), push it; if it produces a *visible failure* the agent must then resolve
(loud), pull is safe and cheaper.

Skills are not retired: `SKILL.md` files remain the human-lane interface (session-per-pass
fallback), consuming the same canonical files. The two lanes therefore cannot diverge on
instrument content — the comparability concern of plan §9 item 2, avoided by construction.

## 3. Reliability engineering (cross-cutting)

1. **Read receipts (decided, Shawn 2026-07-15).** Every agent output is structured and
   includes an `instrument_versions` field echoing the version line of each pushed
   instrument and of each pulled file actually read. The orchestrator validates receipts
   against expected versions as a hard gate; a wrong or missing receipt fails the run
   before its output enters study data. This converts the silent pull/attention failure
   into a machine-detectable one for a few tokens per call.
2. **Escalate, don't improvise.** Every agent definition embeds the same standing rule:
   on missing input, unreadable file, or ambiguity outside its brief, emit `ESCALATE`
   with a reason and stop. This directly counters the error-then-continue failure mode.
3. **Orchestrator pre-flight.** Before any agent is invoked, the workflow verifies that
   every file the agent will be given or pointed at exists and is non-empty. Missing
   canon fails the batch before compute or token spend.
4. **Deterministic gates between stages** (plan §4.2–4.3, unchanged): Docker image
   builds, scripts parse, expected artefacts exist and are non-empty, queue updated.
   Artefact persistence is verified by the orchestrator, never asserted by the agent.
5. **Structured outputs everywhere.** Agent-to-agent handoffs are schema-validated
   objects, not prose to be re-parsed.
6. **Fresh-context boundaries.** Adversarial review runs in a subagent with no shared
   context (invariant 4); assessment-before-reproduction blinding is enforced by
   workflow sequencing plus lock commits (preregistration §8).
7. **Regression gate on change.** Any edit to instrument files or agent definitions, and
   any model version change, re-runs the Phase 2 pilot regression test before production
   use (preregistration §8 permitted-changes clause).

## 4. Canonical homes: designate, don't duplicate

Every shared content item gets exactly one canonical file. Existing files are designated
where possible; new files are created **only** where content currently lives in prose
with no machine-consumable home. Instrument-bearing files gain a header:
`Status: FROZEN by OSF registration <date> — changes require regression gate + OSF amendment`,
plus a version line (the string agents echo as their read receipt).

| Item | Canonical home | Notes |
|---|---|---|
| FAIR instrument v2.0 (15 sub-principles, A1 rule, bands) | `extraction-system/prompts/06-infrastructure_pass6_prompt.md` | Already the operational implementation attached to the preregistration; `study-protocol.md` §4 is the narrative statement — the lodgement check (§6) confirms they match |
| Data-availability taxonomy L1–L5 + 3-level collapse | **new:** `studies/open-science-compliance/protocol/instruments/data-availability-taxonomy.md` | Currently exists only inside the preregistration draft §7.3 |
| Reproduction verdicts + precision categories + tolerance rules | **new:** `.../instruments/verdicts-and-precision.md` | Currently spread across reproduction SKILL.md and preregistration §7.2/§7.4 |
| Environment-specification levels (0–5) | same file as verdicts, or its own | Small; decide at build time |
| Verification-target coverage rules (denominator lock) | **new:** `.../instruments/coverage-rules.md` | Preregistration §7.6; consumed by planner and executor |
| Census/reproduction eligibility criteria | preregistration §4–§5 → extracted to `.../instruments/eligibility-criteria.md` at lodgement | Includes the compute-cap rule (168 h + archived-intermediates partial path) |
| Pipeline invariants (the six in plan §4.3) | **new:** `.claude/agents/shared/invariants.md` | Pushed to every reproduction-lane agent |
| Dockerfile / wrapper patterns, templates, examples | existing `references/` files under `.claude/skills/` | Unchanged; pulled |

The preregistration's §7 text is a frozen *copy* by design — that is what a registration
is. The repo instrument files are the operational canon; a consistency check at lodgement
confirms they match, and any post-lodgement divergence is what the OSF-amendment rule
exists to catch.

**Version registry:** `manifest.yaml` (already the component-version source of truth)
gains a `shared_content` section listing each canonical file, its version, and which
agents consume it by which mechanism. No new registry file — extending the existing one
avoids creating a fifth version-history location (task D pathology).

## 5. Per-agent routing

| Agent | (a) Embedded role behaviour | (b) Pushed instruments | (c) Pulled references |
|---|---|---|---|
| `fair-assessor` | Pass 0 + Pass 6 sequencing; output contract; unscoreable-sub-principle handling; receipts + escalation | FAIR instrument; availability-statement inventory fields; taxonomy (statement-level at census; retrieval-level assignment happens in reproduction) | `infrastructure/pid-systems-guide.md`; `credit-taxonomy.md`; `fair-principles-guide.md`; `checklists/expected-information.md` |
| `reproduction-planner` | Paper-analysis sequencing; Type A/B/C/D classification workflow; risk-assessment framing; plan output contract | Coverage rules (target enumeration is the H2 denominator — silent-failure risk); eligibility criteria incl. compute cap; availability taxonomy | `verification-strategies.md`; `examples/pilot-reproduction-summary.md` |
| `reproduction-executor` | Merged R-A + R-B workflow; build-fix loop; script-adaptation procedure; receipts + escalation | Invariants (esp. the wrapper cardinal rule); verdicts + precision + tolerances; coverage rules | `dockerfile-patterns.md`; `wrapper-script-patterns.md`; `templates/` (log, environment, comparison report) |
| `adversarial-reviewer` | Sceptic stance; artefacts-only rule; no access to any reproduction conversation; verdict-challenge output contract | `adversarial-review-framework.md` — promoted from pulled to pushed: it is the *instrument* of the review, so a miss is silent | Discrepancy examples if needed |
| `corpus-screener` | Sweep/triage sequencing; per-paper logging contract | Eligibility criteria; frame-recording field list (preregistration §4) | — (consumes the DOI manifest from `corpus-management-plan.md`) |

## 6. Maintenance rules (the counterbalance)

1. **No agent-to-agent duplication, ever.** Content needed by two or more agents becomes
   a shared canonical file (pushed or pulled). If role text is being copied between two
   agent definitions, it has been misclassified — it is shared content; move it.
2. **Role text is agent-private.** It may be freely reworded per agent without any
   synchronisation duty; that is the point of class (a).
3. **One canonical file per instrument**, frozen header, version line, registered in
   `manifest.yaml shared_content`. Edits go through the regression gate; post-lodgement
   edits additionally require an OSF amendment before the affected analysis runs.
4. **Lodgement consistency check:** before the OSF registration is submitted, confirm the
   preregistration §7 text matches the canonical instrument files word-for-word (or
   record deliberate differences). One-off, manual, documented.
5. **Skills stay thin over the same canon.** Where a SKILL.md currently inlines
   instrument text, it gains a pointer to the canonical file instead (done opportunistically
   during Phase 1, not as a big-bang rewrite).

## 7. Open questions for review / prior-art scout

1. **Prior art on skill/agent content division.** Agents and skills have coexisted in
   Claude Code long enough for community patterns to exist. What do mature setups do —
   thin agents + injected content, fat self-contained agents, or generated agent files
   assembled from parts by a build step? Is there tooling worth adopting rather than
   hand-rolling the push mechanism?
2. **Read-receipt precedents.** Is there an established pattern for verifying that an
   agent actually consumed its instructions (hash echo, canary strings, structured
   attestation fields)? Anything better than version-line echo?
3. **Prompt-size economics of push.** Inlining the full FAIR instrument into every
   `fair-assessor` invocation at census scale — does prompt caching make this negligible,
   or should the instrument be trimmed to a scoring-operational core first?
4. **Is `corpus-screener` an agent at all?** The sweep is deterministic Application
   Programming Interface (API) work (CrossRef/OpenAlex); judgement is needed only for the
   quantitative/computational triage. Reliability-first argues for a script with a narrow
   LLM triage step, not a general agent. (Flagged here so the review considers it.)
5. **Generated-agent alternative.** A build script assembling agent definitions from
   parts would restore single-file legibility while keeping single-source content. Almost
   certainly over-engineering at five agents — but the scout should check whether cheap
   established tooling changes that calculus.

## 8. Relationship to other documents

- **Resolves:** agentic-modernisation-plan §9 item 3 (pending Shawn's sign-off of this
  design); reword plan §4.1 and the Phase 1 task list to cite this document.
- **Feeds:** Phase 1 build (agent authoring, workflow wiring, gate scripts).
- **Constrains / is constrained by:** phase-2-preregistration-draft.md §7 (instruments
  fixed at registration; canonical files must match at lodgement) and §8 (regression
  gate; permitted changes).
- **Depends on:** corpus-management-plan.md (DOI manifest consumed by `corpus-screener`).
