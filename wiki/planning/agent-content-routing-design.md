# Agent content-routing design: skills, agents, and shared instruments

**Version:** 0.2.2
**Date:** 2026-07-24 (v0.2.1: 2026-07-24; v0.2: 2026-07-23; v0.1: 2026-07-15)
**v0.2.1:** adds §9 (Claude Code workflows adopted as the batch orchestration
engine), prompted by Shawn's review question 2026-07-24.
**v0.2.2:** applies the 2026-07-24 pre-build juncture review
(`wiki/planning/reviews/2026-07-24-pre-build-juncture-review.md`; 12 defects,
8 enhancements): §2.2 remediation ladder made preregistration-compliant
(amendment-gated, one attempt, §8(a) stability-check mislabel fixed); §9 made
conditional on a hook-verification spike with the headless `--agent` fallback
named, same-session-only resume corrected, Max-plan cost instrumentation
re-specified; blocking pre-flight moved to `PreToolUse[Agent]`; per-invocation
model-alias layer hard-gated; transcript-lag retry added; promptfoo and
cache-pipelining decisions recorded.
**Status: SIGNED OFF (Shawn, 2026-07-24, at v0.2.2)** — governs the Phase 1 build.
**D-2 hook spike PASSED (2026-07-24, Phase 1 opening): §9 engine = workflows,
CONFIRMED.** Empirical results (probe log + canary replies, two haiku probes):
(i) `SubagentStart`/`SubagentStop` both fire for workflow `agent()` spawns —
refuting the docs-based pessimism; (ii) injected `additionalContext` reaches
workflow-spawned agents (canary echoed verbatim); (iii) `SubagentStop` delivers
`agent_transcript_path`, so the transcript receipt gate works in workflows;
(iv) a named `agentType` reports that name to hook matchers (the generic
`workflow-subagent` label appears only for unnamed spawns) — **build rule:
production workflow `agent()` calls always pass `agentType`**, so per-agent
matcher scoping works. Hooks also register mid-session without a restart.
The headless `--agent` fan-out remains documented as the fallback engine but is
not needed. The §2.2 ladder is available only once the consolidated OSF
amendment lodges (registrant's timing decision 2026-07-24: defer lodgement to
just before the validation phase, accumulating any further errata).
**Origin:** 2026-07-15 discussion of pull-failure risk (an agent instructed to read a
skill file may silently not read it, or fail the read and helpfully continue). Design
brief from Shawn: engineer for reliability first, accepting some duplication cost, but
split content cleanly between skills and agents, and among agents, so repetition never
creates update/maintenance drift.

**v0.1 → v0.2 changes** (full analyses in the two review reports, §8):

- Routing *policy* (§2) retained unchanged; three refinements added from the
  implementation review — routing is per-(content, consumer) pair, loudness must be
  manufactured by structural gates, and class migration now has a trigger (§6).
- Reliability *mechanisms* (§3) rebuilt on native Claude Code harness primitives
  (`SubagentStart`/`SubagentStop` hooks, `skills:` preload, `--json-schema`) instead
  of hand-rolled orchestrator plumbing; read receipts upgraded from a version-line
  echo to a layered delivery + consumption + transcript-verification scheme; model
  identity and agent-definition version pinned and receipted (review D2, D4, E1–E3).
- Availability-taxonomy reference corrected to the preregistered six-level L1–L6
  scale, and the census-side use renamed `stated_availability` to prevent a shadow
  variant of the reproduction-time instrument (review D3).
- Canonical-homes table (§4) updated: FAIR instrument to be extracted to its own
  file at build time (review D1; the Pass 6 prompt's three defects were fixed
  2026-07-22, commit `abdc526`, and recorded in the OSF erratum log); shared canon
  relocated out of the recursively scanned `.claude/agents/` tree (D7);
  `shared_content` registry becomes machine-verified (D5).
- `corpus-screener` demoted from agent to deterministic script + narrow LLM triage
  step (E7, closing open question 4).
- All five §7 open questions closed with verified evidence; §7 is now the
  resolutions record.

---

## 1. The problem this solves

The agentic modernisation plan (v0.3) contains an internal contradiction flagged in its
§9 item 3: §4.1 says agents *reference* the existing skills; the Phase 1 task list says
skill content is *migrated into* agent definitions. These imply opposite maintenance
stories. Neither pure model is right:

- **Pure reference (pull):** a thin agent is told "Read file X before working". The
  content arrives only if the agent complies. Misses are *silent* — a scorer that never
  read the rubric still produces plausible scores. Per-invocation miss probability is
  low, but at census scale (280+ scoring invocations) even ~1% contaminates the
  dependent variable invisibly; and the most realistic variant is not disobedience but
  *error-then-continue* (a failed Read followed by "I know the FAIR principles anyway").
- **Pure migration (embed):** content is guaranteed in context, but every shared rubric
  is copied into several agent definitions. This repo has already logged that pathology
  (version history hand-maintained in four places — continuity task D), and duplicated
  instrument text breaks the preregistration's "instrument fixed at registration" claim,
  which must be auditable from a single file's git history.

## 2. The routing rule (policy — unchanged from v0.1)

Route each piece of content by *what happens when its delivery fails*:

| Class | Content type | Delivery | Failure mode if missing | Examples |
|---|---|---|---|---|
| **(a) Embedded** | Role behaviour: sequencing, stance, output contract, escalation rules | Written into the agent definition, imperative voice, tuned per role | N/A — always present | Executor's build-fix loop; reviewer's sceptic stance |
| **(b) Pushed** | Instruments: rubrics, taxonomies, verdict criteria — anything where two scorers diverging is a bug | Injected deterministically at agent spawn (mechanism §3.1) | N/A — arrival is harness-guaranteed | FAIR instrument; availability taxonomy; verdict + precision definitions |
| **(c) Pulled** | Pattern libraries and troubleshooting knowledge, needed occasionally | Agent Reads the canonical file on demand (one hop, repo-rooted path) | **Loud** — a build fails and the agent goes looking; recoverable | Dockerfile patterns; wrapper-script patterns; PID systems guide |

The line between (b) and (c): if an unnoticed miss produces *plausible wrong output*
(silent), push it; if it produces a *visible failure* the agent must then resolve
(loud), pull is safe and cheaper.

Skills are not retired: `SKILL.md` files remain the human-lane interface (session-per-pass
fallback), consuming the same canonical files. The two lanes therefore cannot diverge on
instrument content — the comparability concern of plan §9 item 2, avoided by construction.

The prior-art pass found no external framework that solves this division better:
the community norm for Claude Code agents is fat self-contained definitions (the
embed pathology), and PydanticAI's static/dynamic instruction split independently
validates the (a)/(b) distinction as recognised practice (verified report rows 2, 5).

### 2.1 Three refinements to the criterion (v0.2)

1. **Routing is per-(content, consumer) pair, not per-file.** The same file can be
   silent-on-miss for one agent and loud for another. Live instance:
   `verification-strategies.md` is pulled for `reproduction-planner`, yet the
   planner's verification-target enumeration is the locked H2 denominator — a
   planner that never reads it produces a plausible-but-thin target list with no
   loud failure. Mitigation: the enumeration-completeness check in §5 (planner row).
2. **"Loud" is only as loud as the gates.** A malformed-but-non-empty artefact
   passes an exists-and-non-empty gate silently. Loudness is *manufactured*:
   stage gates validate artefact structure (schema-validated comparison-report
   tables, template conformance), not just presence (§3.5). This is what licenses
   leaving templates in the pulled class.
3. **Class migration needs a trigger.** Content moves class as its role hardens
   (the wrapper cardinal rule moved from pattern guidance to pushed invariant;
   `adversarial-review-framework.md` is promoted to pushed in this document).
   The migration trigger is now a maintenance rule (§6 rule 6).

### 2.2 Empirical backstop for the pull class

For the scoring lane, per-invocation silent misses of *interpretive* pulled material
(e.g. `fair-principles-guide.md`) surface in aggregate as inter-run variance — which
the preregistration §8 reliability check (three pilot papers × three runs,
≥0.90 mean per-sub-principle agreement) is positioned to measure. That check is the
empirical backstop for every class-(c) entry in the `fair-assessor` row of §5.
The preregistration's pre-specified consequence of a below-threshold result is
majority-vote census scoring (a 3× cost multiplier). A cheaper remediation exists —
one routing-fix attempt (push a trimmed interpretive core, ~2k tokens) followed by a
re-run of the **§8(a) stability check** — but substituting it for the registered
consequence is a **deviation, not an implementation change** (2026-07-24 review,
D-1), so it is available only if pre-specified in the consolidated OSF amendment
lodged **before the validation phase runs** (queued in the erratum log). As
pre-specified there: one attempt maximum — a still-below-threshold re-run means
majority vote applies with no further iteration; both pre-fix and post-fix
reliability results are reported with study outcomes. The routing fix *itself*
(delivery mechanism only; instrument text untouched) remains an ordinary §8
implementation change, gated by the pilot regression test plus an erratum-log
entry.

## 3. Reliability engineering (cross-cutting — rebuilt on harness primitives in v0.2)

The v0.1 mechanisms (hand-rolled orchestrator prompt assembly, version-line echo as
"hard gate", script-only pre-flight) are replaced. Native harness primitives are
deterministic at the harness level, behave identically in the scripted and
interactive lanes (a hook fires however the agent is invoked), and leave
harness-recorded evidence that does not depend on the model's honesty.

1. **Push mechanism: `SubagentStart` hook injection (primary).** A hook matched on
   agent type injects the canonical file content into the subagent's context before
   its first prompt, and logs the sha256 and version line of exactly what it
   injected — an **orchestrator-side receipt that does not depend on the model at
   all**. Alternative where hook infrastructure is unavailable: the `skills:`
   frontmatter field (full skill content injected at spawn, harness-guaranteed).
   Caveat, verified against live docs: a missing/disabled skill is *silently
   skipped* with only a debug-log warning — so pre-flight (item 4) and receipts
   (item 2) remain necessary as the backstop under either mechanism. Hand-rolled
   prompt assembly is not used.
2. **Read receipts, layered (supersedes the v0.1 version-line echo).** The echo
   alone verifies delivery/assembly for pushed content (it arrives in the same
   prompt it is echoed from) and is defeasible for pulled content (header-only
   reads; guessable `Version:` conventions). v0.2 layers:
   - *Delivery check:* version-line echo retained, validated against
     `manifest.yaml` — catches stale-file pushes.
   - *Consumption check:* an unguessable receipt token at the **end** of each
     canonical file (random, generated once, registered in the manifest) — cannot
     be echoed from convention or a header-only read.
   - *Hard gate:* a `SubagentStop` hook parses the harness-recorded agent
     transcript and verifies the Read tool calls actually made (paths; absence of
     `limit`/`offset` truncation) against the agent's declared pulled-file
     receipts. Harness evidence, not self-report. (Transcripts are written
     asynchronously and can lag — the hook retries briefly on missing expected
     entries before blocking, and parses outputs from `last_assistant_message`;
     2026-07-24 review, D-12.)
   - *Structural requirement:* receipts are required fields of the output schema
     (item 6), so a missing receipt is a schema failure, not a soft omission.
   - *Self-healing:* on receipt/contract failure the `SubagentStop` hook returns
     `decision: "block"` with the reason, re-prompting the same subagent
     ("re-read X in full and re-emit receipts") instead of failing the batch item.
3. **Receipt the whole instrument identity.** The effective instrument at census
   scale is (instrument files × agent definition × model). Receipts therefore carry
   `{instrument_versions, agent_version, model_id}`. Every scoring agent pins a
   **full model ID** in its `model:` frontmatter (the default `inherit` is
   uncontrolled); agent-definition versions are registered in the manifest; and
   pre-flight fails the run if `CLAUDE_CODE_SUBAGENT_MODEL` is set unexpectedly
   (it silently outranks frontmatter). Any model change is a §8 regression-gate
   trigger — now detectable, not just declared. Two further controls (2026-07-24
   review, D-7): the per-invocation `model` parameter *also* outranks the
   frontmatter pin and accepts only floating aliases, so orchestration never
   passes per-call model overrides — model identity lives in agent definitions
   only (per-model variants with pinned full IDs, as files or via the `--agents`
   JSON flag); and the receipted `model_id` comparison against the manifest pin
   is a **hard gate** — a mismatch blocks the item rather than merely logging.
4. **Pre-flight as a `PreToolUse` hook matched on the Agent tool** — `SubagentStart`
   cannot block a spawn, while `PreToolUse` can deny it before token spend
   (2026-07-24 review, D-3). Checks: every file the agent will be given or
   pointed at exists and is non-empty; the manifest-consistency check (§4) passes;
   agent-definition file hashes match the manifest (guarding against the harness's
   hot-reload of edited definitions bypassing the regression gate); the model
   environment override is unset. `SubagentStart` retains what it can do: content
   injection (item 1) and advisory warnings. The scripted lane additionally runs
   pre-flight in the runner before any invocation.
5. **Deterministic gates between stages** (plan §4.2–4.3), extended: Docker image
   builds, scripts parse, expected artefacts exist and are non-empty, queue updated
   — **plus structural validation of quantitative artefacts**: the comparison
   report's value table is a schema-validated machine-readable artefact, checked at
   the stage gate (it feeds the adversarial review and the H2 coverage
   computation). Artefact persistence is verified by the orchestrator, never
   asserted by the agent.
6. **Structured outputs everywhere, harness-enforced.** Headless lane:
   `--output-format json --json-schema <schema>` per agent. Interactive lane: the
   same schema validated by the `SubagentStop` hook. `status` is an enum that
   includes `ESCALATE`, making the escalate-don't-improvise rule machine-readable:
   on missing input, unreadable file, or ambiguity outside its brief, an agent
   emits `status: ESCALATE` with a reason and stops — countering
   error-then-continue.
7. **Fresh-context boundaries, enforced not requested.** Adversarial review runs in
   a subagent with no shared context (invariant 4); its artefacts-only rule is a
   hard constraint via `tools:`/`disallowedTools` frontmatter (Read/Grep/Glob/Bash
   only) with `maxTurns` bounding runaway loops. Assessment-before-reproduction
   blinding is enforced by workflow sequencing plus lock commits
   (preregistration §8).
8. **Regression gate on change.** Any edit to instrument files or agent
   definitions, and any model version change, re-runs the Phase 2 pilot regression
   test before production use (preregistration §8 permitted-changes clause), and
   re-confirms the routing class of every changed file (§6 rule 6). Post-lodgement
   instrument corrections additionally get an erratum-log entry
   (`studies/open-science-compliance/prereg/erratum-log.md`) pending an OSF
   amendment.
9. **No persistent memory on scoring agents.** `memory:` frontmatter is prohibited
   for `fair-assessor` (and any scoring role): cross-session memory would make
   paper N's score depend on papers 1…N−1, quietly violating the fixed-instrument
   assumption.

## 4. Canonical homes: designate, don't duplicate

Every shared content item gets exactly one canonical file. Existing files are designated
where possible; new files are created **only** where content currently lives in prose
with no machine-consumable home. Instrument-bearing files gain a header:
`Status: FROZEN by OSF registration <date> — changes require regression gate + erratum-log entry + OSF amendment`,
a version line, and an end-of-file receipt token (§3.2).

| Item | Canonical home | Notes |
|---|---|---|
| FAIR instrument v2.0 (15 sub-principles, A1 rule, bands, data-completeness coverage procedure) | **new at build time:** `studies/open-science-compliance/protocol/instruments/fair-instrument.md`, extracted from `extraction-system/prompts/06-infrastructure_pass6_prompt.md` (which then points to it) | Review D1: the Pass 6 prompt mixes the frozen instrument with 700+ lines of evolving workflow guidance; extraction separates them so workflow edits stop triggering instrument governance. The prompt's three defects (stale /16 example; colliding legacy access-tier labels; dead pointer) were fixed 2026-07-22 (`abdc526`) and recorded in the erratum log. `study-protocol.md` §4 remains the narrative statement |
| Data-availability taxonomy **L1–L6** + 3-level collapse (open = L1–L2; mediated = L3; effectively closed = L4–L6) | **new:** `studies/open-science-compliance/protocol/instruments/data-availability-taxonomy.md`, built from preregistration §7.3 | **Corrected from v0.1's superseded L1–L5** (prereg v0.5, 2026-07-18, moved to six friction-ordered levels). L-levels are assigned **only at reproduction time from actual retrieval attempts** (§7.3); the census records `stated_availability` (descriptive, never mapped to L1–L6) — see §5 |
| Reproduction verdicts + precision categories + tolerance rules | **new:** `.../instruments/verdicts-and-precision.md` | Currently spread across reproduction SKILL.md and preregistration §7.2/§7.4 |
| Environment-specification levels (0–5) | same file as verdicts, or its own | Small; decide at build time |
| Verification-target coverage rules (denominator lock) | **new:** `.../instruments/coverage-rules.md` | Preregistration §7.6; consumed by planner and executor |
| Census/reproduction eligibility criteria | preregistration §4–§5 → extracted to `.../instruments/eligibility-criteria.md` | Includes the compute-cap rule (168 h + archived-intermediates partial path) |
| Pipeline invariants (the six in plan §4.3) | **new:** `.claude/shared/invariants.md` | **Moved out of `.claude/agents/`** (review D7: that tree is recursively scanned and parsed as agent definitions; parking prose there relies on undocumented behaviour). Pushed to every reproduction-lane agent |
| Dockerfile / wrapper patterns, templates, examples | existing `references/` files under `.claude/skills/` | Unchanged; pulled |

The preregistration's §7 text is a frozen *copy* by design — that is what a registration
is. The repo instrument files are the operational canon; the lodgement consistency check
confirmed they matched at `ee3fda3`, and post-lodgement divergence is caught by the
erratum-log + OSF-amendment mechanism (first exercised 2026-07-22).

**Version registry, machine-verified:** `manifest.yaml` (already the component-version
source of truth) gains a `shared_content` section listing each canonical file, its
version, its receipt token, and which agents consume it by which mechanism. Because the
registry hand-duplicates facts that live in file headers and agent definitions, it gets
a **consistency-check script** (parse version lines/receipt tokens and diff against the
manifest; grep agent definitions and hook config for pushed/pulled paths and diff
against the consumer lists), wired into the existing pre-commit hook and orchestrator
pre-flight (review D5). The manifest can then drift for at most one commit. The same
script's agent-file hash check implements the hot-reload guard (§3.4).

## 5. Per-agent routing

| Agent | (a) Embedded role behaviour | (b) Pushed instruments | (c) Pulled references |
|---|---|---|---|
| `fair-assessor` | Pass 0 + Pass 6 sequencing; output contract; unscoreable-sub-principle handling; receipts + escalation; **no `memory:`** (§3.9) | FAIR instrument; availability-statement inventory fields (recorded as `stated_availability` — descriptive only, **never mapped to L1–L6**; L-assignment is reproduction-side per prereg §7.3) | `infrastructure/pid-systems-guide.md`; `credit-taxonomy.md`; `fair-principles-guide.md`; `checklists/expected-information.md` — all backstopped by the §2.2 reliability check |
| `reproduction-planner` | Paper-analysis sequencing; Type A/B/C/D classification workflow; risk-assessment framing; plan output contract; **enumeration-completeness check** — a deterministic count of display items (tables/figures/named values) detected in the paper vs targets enumerated, with below-threshold plans flagged for explicit human attention at batch approval (review D8) | Coverage rules (target enumeration is the H2 denominator — silent-failure risk); eligibility criteria incl. compute cap; availability taxonomy (L1–L6, for reproduction-time assignment) | `verification-strategies.md`; `examples/pilot-reproduction-summary.md` |
| `reproduction-executor` | Merged R-A + R-B workflow; build-fix loop; script-adaptation procedure; receipts + escalation | Invariants (esp. the wrapper cardinal rule); verdicts + precision + tolerances; coverage rules | `dockerfile-patterns.md`; `wrapper-script-patterns.md`; `templates/` (log, environment, comparison report — conformance validated at the stage gate, §3.5) |
| `adversarial-reviewer` | Sceptic stance; artefacts-only rule **enforced via `tools:` allowlist (Read/Grep/Glob/Bash) + `maxTurns`**; no access to any reproduction conversation; verdict-challenge output contract | `adversarial-review-framework.md` — promoted from pulled to pushed: it is the *instrument* of the review, so a miss is silent | Discrepancy examples if needed |
| `corpus-screener` → **script + narrow LLM triage** (not a general agent) | The sweep is deterministic API work: a Python script over CrossRef/OpenAlex (mature MIT clients: `habanero`, `pyalex`) enumerates and frame-records; judgement enters only at the quantitative/computational triage flag, run as a per-paper `claude -p` call with `--json-schema` | The triage prompt is **instrument-like** (the quantitative flag defines the H1 sample): canonical file, version line, receipt, like the others | — (consumes the DOI manifest from `corpus-management-plan.md`) |

The screener shape is the published pattern for this task — deterministic retrieval
first, scoped LLM triage, human oversight (Affinage's "Stage 0, no LLM"; the
peer-reviewed LLMSurver corpus-filtration paper, *Computers & Graphics* 2026;
ASReview's human-in-the-loop norm — verified report rows 18–23).

## 6. Maintenance rules (the counterbalance)

1. **No agent-to-agent duplication, ever.** Content needed by two or more agents becomes
   a shared canonical file (pushed or pulled). If role text is being copied between two
   agent definitions, it has been misclassified — it is shared content; move it.
2. **Role text is agent-private.** It may be freely reworded per agent without any
   synchronisation duty; that is the point of class (a).
3. **One canonical file per instrument**, frozen header, version line, receipt token,
   registered in `manifest.yaml shared_content` and covered by the consistency-check
   script. Edits go through the regression gate; post-lodgement edits additionally
   require an erratum-log entry and an OSF amendment before the affected analysis runs.
4. **Lodgement consistency check** (done for the Phase 2 registration at `ee3fda3`):
   before any future OSF lodgement or amendment, confirm the registration text matches
   the canonical instrument files word-for-word (or record deliberate differences).
5. **Skills stay thin over the same canon.** Where a SKILL.md currently inlines
   instrument text, it gains a pointer to the canonical file instead (done opportunistically
   during Phase 1, not as a big-bang rewrite).
6. **Routing-class migration trigger (new in v0.2).** The §8 regression-gate checklist
   includes: "re-confirm the routing class of every changed file". Standing rule: any
   pulled file found to be decisive for a score or verdict gets a promotion review
   (pull → push).
7. **Agent definitions are governed artefacts (new in v0.2).** The harness hot-reloads
   edited definitions within seconds; discipline is procedural: pre-flight refuses to
   run on agent files whose hashes are not registered in the manifest (§3.4), so an
   ungated edit stops the batch rather than silently changing the instrument.

## 7. Open questions — resolved (v0.2)

All five v0.1 open questions were answered by the 2026-07-22 review passes
(implementation review + adversarially verified prior-art scout; reports in §8).

1. **Skill/agent content division — RESOLVED.** No external framework or community
   pattern solves it better; the community norm is fat self-contained agents (the
   embed pathology). The harness itself provides the push mechanism: `SubagentStart`
   injection (primary) or `skills:` preload (secondary), each with the silent-skip
   backstop caveat (§3.1). No tooling worth adopting over the native primitives.
2. **Read-receipt precedents — RESOLVED.** The strongest external pattern found
   (runtime-HMAC "tool receipts", zeroclaw / Basu 2026 preprint) verifies tool-call
   fidelity, not context consumption, and would require re-routing pushed content
   through a tool call. The version-line echo is close to the field's state of the
   art for this sub-problem; v0.2 strengthens it with the layered scheme of §3.2
   (unguessable end-of-file token + transcript-grounded `SubagentStop` verification),
   which exceeds anything found in the survey.
3. **Prompt-size economics of push — RESOLVED.** Push cost is ~2–5% of the lane's
   token bill: ~$8–13 uncached across a ~280-invocation census at current prices,
   ~$23–38 under the 3× majority-vote fallback — negligible either way. **Trim only
   for salience, never for cost** (the D1 instrument extraction delivers the salience
   trim anyway). One caveat survived verification and is time-sensitive: Claude Code
   subagents get a **cold prompt cache per spawn (5-minute TTL even on
   subscription)**, and open issue anthropics/claude-code#29966 alleges subagent
   caching may be off entirely in some code paths — so the Phase 3 cost gate must
   price from an **empirical `cache_read_input_tokens` check on this harness**, not
   from the API caching discount assumed by comparator eval harnesses (Inspect AI
   pushes full rubrics per call and relies on provider caching).
4. **Is `corpus-screener` an agent at all? — RESOLVED: no.** Deterministic script +
   narrow instrument-like LLM triage (§5), the published and tooling-supported
   pattern.
5. **Generated-agent alternative — RESOLVED: not needed.** With harness-native
   injection there is no assembly problem for a build step to solve. Closed in the
   opposite direction from the v0.1 hypothesis ("cheap tooling might justify it").

## 8. Relationship to other documents

- **Resolves:** agentic-modernisation-plan §9 item 3 (pending Shawn's sign-off of this
  design); on sign-off, reword plan §4.1 and the Phase 1 task list to cite this
  document.
- **Informed by (v0.2):**
  `wiki/planning/reviews/2026-07-22-routing-design-implementation-review.md`
  (findings D1–D10, E1–E8) and
  `wiki/planning/scout-reports/2026-07-22-routing-design-prior-art-verified.md`
  (verified 107/110 claims; 0 corrections).
- **Feeds:** Phase 1 build (agent authoring, hook scripts, schema files, gate
  scripts, instrument-file extraction), then the combined post-build validation
  phase (regression gate + reliability spot-check, per the sequence blessed
  2026-07-22) before census.
- **Constrains / is constrained by:** phase-2-preregistration-draft.md §7 (instruments
  fixed at registration; §7.3 L1–L6 reproduction-time assignment) and §8 (regression
  gate; permitted changes; reliability thresholds); the erratum log
  (`studies/open-science-compliance/prereg/erratum-log.md`) for any post-lodgement
  instrument correction.
- **Depends on:** corpus-management-plan.md (DOI manifest consumed by the
  corpus-screener script).

## 9. Execution engine: Claude Code workflows (v0.2.1)

The v0.2 text specified orchestrator *behaviour* (pre-flight, push, receipts,
gates) without committing to an engine, implicitly assuming a hand-rolled runner
over headless invocations. **Claude Code workflows are adopted — conditional on a
verification spike — as the batch orchestration engine** wherever control flow
must be deterministic. The spike runs in Phase 1's opening hour and must show the
§3 reliability layer functions for workflow-spawned agents: current documentation
scopes `SubagentStart`/`SubagentStop` to Agent-tool spawns and explicitly
distinguishes workflow `agent()` spawns, so hook firing is more likely to fail
than pass (2026-07-24 review, D-2). **Named fallback if the spike fails: a
per-paper headless `claude -p --agent fair-assessor` fan-out** — on that path
frontmatter hooks are documented to fire, the full-ID `model:` pin applies,
`--json-schema` output enforcement applies, and the main-session **1-hour
subscription cache TTL** replaces the subagent cold-cache penalty: with a
byte-stable prefix (agent definition + pushed instruments first, paper content
last), papers processed within each window read the instrument tokens at ~0.1× —
the §7.3 empirical check confirms or refutes this on the first probe at no extra
cost. Same architecture, different engine; the appendix's runner + `flock`
provides the 4–6-worker concurrency either way.

| Lane | Workflow role |
|---|---|
| Census FAIR scoring | `pipeline()` over the paper list: per-paper `agent()` calls with schema-enforced structured outputs (tool-layer validation with bounded retries), native concurrency (4–6 workers planned; headroom to 16 subject to Max-window pacing), and resume-from-run-ID with completed calls cached — **same-session only** (D-6): cross-session resume stays with queue.yaml, the invoking session enumerating the remaining papers as `args`. Provenance: persisted workflow script + OpenTelemetry `workflow.run_id` traces archived with study outputs |
| Validation phase (regression gate + reliability spot-check) | Deterministic matrix fan-out (papers × runs × models) with per-call model override; the ask-before-Fable gate is honoured by which models the approved script enumerates |
| Adversarial review | Each `agent()` call is a fresh context, so invariant 4 (no shared context with any reproduction conversation) holds by construction |
| Screener triage (E7) | The narrow LLM step runs as a pipeline over the DOI batch with the same schema + receipt treatment |

**Not used for:** deterministic corpus tooling (fetch/hash/manifest — plain
Python, no LLM), and reproduction *execution* (Docker/compute-bound with batched
human plan approval between stages — a background workflow cannot pause for a
human, so workflows at most bracket the stages: plan-generation batch → approval
→ execution batch).

**Complements, does not replace, §3.** Workflow scripts deliberately have no
filesystem access, so pushed content enters via script arguments (assembled by
the invoking session from the canonical files) or via the agent definitions; the
hook/receipt layer remains the reliability mechanism. Two build-time
verifications: (i) `SubagentStart`/`SubagentStop` hooks fire for
workflow-spawned agents; (ii) workflow model selection uses aliases, so the
receipted `model_id` (§3.3) is the authoritative record of what ran, with
pre-flight checking the alias→pinned-ID mapping.

## Appendix: execution notes for the Phase 1 build (from review E4–E5)

- **Parallelism (census lane):** the FAIR lane is embarrassingly parallel. Serial
  execution at ~8–15 min/paper is ~37–70 h wall-clock for ~280 papers; 4–6
  concurrent headless workers bring it to ~8–14 h. Requires only a per-paper lock
  discipline on the queue (status files or `flock`). Reproduction-lane parallelism
  stays bounded by Docker/compute and human plan approval — serial is fine there.
- **Cost-gate instrumentation (re-specified per 2026-07-24 review, D-8):** per
  probe paper the pre-scale cost gate (plan §5 Phase 3) records three things:
  exact token counts with cache splits (the §7.3 empirical check); the notional
  `total_cost_usd` estimate (a client-side price-table figure, labelled as such —
  not billing data, and billing-irrelevant on the Max plan); and **plan-window
  consumption** (`/usage` read before and after the probe). Together these yield a
  weeks-to-census figure and an explicit decision point: pace the census across
  usage windows, buy usage credits, or run the lane on an API key.
- **Recorded decisions (2026-07-24 review, E-6 + fidelity notes):** promptfoo's
  pass-rate-drop continuous-integration pattern (scout report row 8) is **not
  adopted** for the §8 regression gate — the gate compares a handful of pinned
  pilot artefacts, small enough to hand-roll; revisit if gate comparisons grow.
  Cache-warmth pipelining (scheduling invocations inside the 5-minute subagent
  cache window) is **retained as a §7.3 remediation option** should workflows
  survive the spike but subagent caching prove absent.
