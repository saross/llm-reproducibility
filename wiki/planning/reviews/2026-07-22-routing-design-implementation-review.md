> **Externalisation note (2026-07-22):** this report was produced in-session on
> 2026-07-22 and is externalised verbatim below. One framing item is stale: the
> reviewing agent believed the OSF lodgement was still pending ("fix before
> lodgement", finding D1) — in fact the registration was lodged 2026-07-20 and
> made public 2026-07-21 (DOI 10.17605/OSF.IO/DQNHG), so D1's corrections were
> applied post-lodgement via the approved erratum path instead
> (`studies/open-science-compliance/prereg/erratum-log.md`, entry 1; corrections
> in commit `abdc526`). D1's remaining recommendation — extracting a clean
> instrument file — is queued for the Phase 1 build. All other findings stand as
> written and feed routing-design v0.2.

# Implementation review: agent content-routing design v0.1

**Target:** `wiki/planning/agent-content-routing-design.md` (v0.1, 2026-07-15)
**Protocol:** `~/.claude/skills/review-implementation/SKILL.md` — all phases applied
**Reviewer context read in full:** agentic-modernisation-plan.md v0.3 (§4, §5, §9);
phase-2-preregistration-draft.md v0.7 (§4–§8); manifest.yaml v3.0.1;
`.claude/skills/research-assessor/SKILL.md`;
`extraction-system/prompts/06-infrastructure_pass6_prompt.md`; current Claude Code
documentation (sub-agents, hooks, skills, headless) via the local docs mirror
(v0.3.3, synced this session); current Application Programming Interface (API)
pricing via the claude-api skill (cached 2026-06-24).
**Date:** 2026-07-22. No repository files were modified by this review.

**Verdict up front:** the routing rule itself (embed / push / pull by
failure-mode) is sound and well-motivated, and the design correctly resolves the
plan's §9 item 3 contradiction. The build should proceed — but not as specified.
The review found one critical pre-lodgement defect (the proposed canonical home
for the Findable, Accessible, Interoperable, Reusable (FAIR) instrument contains
internally contradictory scoring text and is about to be frozen by the Open
Science Framework (OSF) registration), two high-severity gaps (model identity is
uncontrolled; the design cites a superseded version of the availability
taxonomy), and a cluster of discovery findings: Claude Code now natively provides
almost every mechanism the design proposes to hand-roll (deterministic content
push, structured-output enforcement, read verification, pre-flight hooks).

---

## Phase 1 — Capability scan (what else exists?)

The design proposes a hand-rolled orchestrator that (a) inlines canonical files
into task prompts, (b) validates version-line echoes, (c) runs pre-flight file
checks, and (d) schema-validates outputs. Current Claude Code (verified against
the docs mirror this session) provides native primitives for each. These are
**discovery findings** — capabilities the design does not mention:

| Design mechanism (hand-rolled) | Native Claude Code capability | Doc source |
|---|---|---|
| Orchestrator inlines canonical file verbatim into the task prompt (class (b) push) | **`SubagentStart` hook `additionalContext`**: a hook script matched on agent type injects arbitrary content into the subagent's context before its first prompt — deterministic, scriptable, works even when the agent is invoked ad hoc from an interactive session, and the hook script can log the sha256 of exactly what it injected | hooks.md § SubagentStart |
| (alternative push) | **`skills:` frontmatter on the agent definition**: full skill content is injected into the subagent's context at startup ("The full skill content is injected, not only the description") | sub-agents.md § Preload skills |
| Read-receipt echo validated by the orchestrator | **`SubagentStop` hook**: receives `last_assistant_message` and `agent_transcript_path`; can parse the structured output *and* grep the harness-recorded transcript for actual Read tool calls; returning `decision: "block"` with a reason keeps the subagent running with that reason as its next instruction (self-healing retry, not batch failure) | hooks.md § SubagentStop |
| "Structured outputs everywhere" by convention | **Headless `--output-format json --json-schema <schema>`**: harness-enforced schema-conforming output in a `structured_output` field | headless.md § Get structured output |
| Orchestrator pre-flight (files exist, non-empty) | **`SubagentStart` / `SessionStart` hooks** run scripts before the agent works; `PreToolUse` hooks can gate individual tool calls | hooks.md |
| Cost gate measurement (plan §5 Phase 3) | **`--output-format json` returns `total_cost_usd` and a per-model cost breakdown per invocation** — the pre-scale cost gate's data collection is free | headless.md |
| Not in the design at all | **`model:` frontmatter** — pins a subagent to a full model ID; default is `inherit` (the interactive session's model, i.e. uncontrolled). `CLAUDE_CODE_SUBAGENT_MODEL` env var silently outranks frontmatter | sub-agents.md § Choose a model |
| Not in the design at all | **`maxTurns`**, **`tools`/`disallowedTools`** (allow/deny lists incl. Model Context Protocol (MCP) patterns), **`permissionMode`**, **`Agent(agent_type)` spawn allowlists** for an orchestrating agent | sub-agents.md |
| Not in the design at all (rightly) | **`memory:` frontmatter** — persistent per-agent memory across sessions. Powerful, but a hazard here (see D10) | sub-agents.md § Enable persistent memory |

Two non-harness alternatives considered and set aside:

- **Anthropic Message Batches API** (50% discount, 100k requests/batch) would be
  the cheapest way to run a 280-paper census — but it bypasses the Claude Code
  harness, skills, and agent machinery entirely, so the preregistration's §8
  regression/comparability requirement would have to be re-satisfied for a
  completely different pipeline. Not worth it at this corpus size (see Phase 3:
  the entire census is tens of dollars, not thousands). No change recommended.
- **Generated agent definitions assembled by a build step** (design open
  question 5): with `SubagentStart` injection and `skills:` preloading available,
  generation solves a problem the harness has already solved. Agree with the
  design's instinct — over-engineering at five agents. Question 5 can be closed.

**Phase 1 conclusion:** the solution space is materially larger than the design
assumes. The push mechanism, the receipt gate, pre-flight, and structured
outputs should all be built on harness primitives rather than hand-rolled prompt
assembly. This is not cosmetic: the native mechanisms are deterministic at the
harness level, they work identically in the scripted lane and the interactive
human lane (a hook fires however the agent is invoked — the hand-rolled push
only exists when the orchestrator script is the caller), and they leave
harness-recorded evidence (transcripts, hook logs) that does not depend on the
model's own honesty.

---

## Phase 2 — Exploitation review (is the design using the envelope fully?)

Assessed dimension by dimension, including the five pressure points named in
the review brief.

### 2.1 The silent-vs-loud routing criterion (pressure point 1)

The criterion is good but has three failure modes of its own:

1. **Consumer-dependent class.** The same file can be silent-on-miss for one
   agent and loud for another. Concrete instance already in the design:
   `verification-strategies.md` is *pulled* for `reproduction-planner`, yet the
   planner's verification-target enumeration is the locked H2 denominator — the
   design itself labels target enumeration "silent-failure risk" one column to
   the left. A planner that never reads the strategies file produces a
   plausible-but-thin target list; nothing fails loudly. The batched human plan
   approval mitigates but does not reliably catch under-enumeration (reviewers
   anchor on what is presented). See finding D8.
2. **"Loud" is only as loud as the gates.** Templates are pulled for the
   executor on the theory that a malformed artefact is visible. The plan's
   deterministic gates check *exists and non-empty* — a comparison report that
   exists, is non-empty, and is structurally wrong (missing tolerance column,
   free-prose table) passes the gate, degrades the adversarial review, and
   corrupts the H2 coverage computation downstream. Loudness must be
   *manufactured* by validating artefact structure, not just presence. See D6.
3. **Class migration over time.** Content moves class as its role hardens (the
   design has already lived this: the wrapper cardinal rule migrated from
   pattern guidance to pushed invariant; `adversarial-review-framework.md` is
   promoted from pulled to pushed in this very document). There is no trigger
   for the next migration. See D9.

A fourth, subtler point: for the scoring lane, per-invocation silent misses of
*interpretive* material (e.g. `fair-principles-guide.md`, 55 KB, pulled) surface
in aggregate as inter-run variance — which the preregistration's §8 reliability
check (3 papers × 3 runs, ≥0.90 agreement threshold) is positioned to measure.
The design should say this explicitly: the reliability check is the empirical
backstop for every class-(c) pull in the fair-assessor's list, and **if the
0.90 threshold fails, the first remediation to try is a routing fix (push a
trimmed interpretive core, ~2k tokens, re-run the pilot comparability check) —
not the preregistration's 3× majority-vote fallback, which triples the census
cost**. The routing fix is an implementation change under §8's permitted-changes
clause (regression gate on pilot papers only); the majority-vote path costs
roughly an extra one to two hundred dollars and days of wall-clock.

### 2.2 The read-receipt version-line echo (pressure point 2)

**Is it a hard gate? No — and it is weaker than §3.1 of the design claims, in
two different ways depending on delivery class:**

- **Pushed content:** the version line arrives *in the same prompt* the agent
  echoes it from. The echo can essentially never fail if orchestrator assembly
  worked, and can never fail *because the agent ignored the content*. It
  verifies **delivery and assembly** (worth keeping — it catches the
  orchestrator pushing a stale file when the manifest expects a newer version),
  but it is not evidence of attention. The design's claim that it "converts the
  silent pull/attention failure into a machine-detectable one" holds only for
  the delivery half.
- **Pulled content:** an agent can satisfy the echo without reading past the
  header — `Read` with a `limit` parameter, or a header-only glance — or without
  reading at all: version strings follow a guessable convention (`Version: 2.0`)
  and the expected values sit in `manifest.yaml`, which an agent may have in
  context. The most realistic failure the design worries about
  (error-then-continue) defeats the echo exactly when it matters.

**Strengthenings, all at negligible cost:**

1. **Move the receipt line to the end of the file and make it unguessable.**
   A footer line such as `Receipt-token: 7f3a9c2e` (random, generated once,
   registered in the manifest) cannot be echoed from convention and cannot be
   obtained by a header-only read. One-off cost per canonical file.
2. **Transcript-grounded verification (the real hard gate).** A `SubagentStop`
   hook receives `agent_transcript_path`; ~30 lines of script can extract every
   Read tool call the agent actually made — file paths, and whether `limit`/
   `offset` truncation was used — and compare against the agent's declared
   pulled-file receipts. This is harness-recorded evidence, not self-report.
   Cost: half a day once, shared by all five agents.
3. **Make the receipt field structurally mandatory** via `--json-schema`
   (headless lane) or the same SubagentStop hook (interactive lane): a missing
   `instrument_versions` block is then a schema failure, not a soft omission.
4. **Self-healing instead of batch failure:** the SubagentStop hook can return
   `decision: "block"` with the reason ("re-read X in full and re-emit
   receipts"), which re-prompts the same subagent rather than failing the run.
5. **Receipt the whole instrument, not just the text** — see D2: the effective
   instrument at census scale is (instrument files × agent definition × model
   ID), and the design receipts only the first.

### 2.3 The manifest `shared_content` registry (pressure point 3)

Yes — as designed it recreates a milder form of the task-D pathology it cites.
The registry hand-duplicates three facts that already live elsewhere: the
version (in each file's header), the consumer list (in agent definitions and
orchestrator/hook config), and the mechanism (ditto). Every routing change or
version bump now has two-to-three touch points, with no machine check that they
agree — and this repository has already needed a "version-drift reconciliation"
release (manifest v3.0.1, Phase 0 of the plan) to repair exactly this kind of
drift, so the base rate is not hypothetical.

The fix is not to abandon the registry (a single queryable inventory is
genuinely useful, and extending manifest.yaml rather than adding a fifth file is
right). The fix is to make it **machine-verified**: a ~50-line script that
(a) parses each canonical file's version line/receipt token and diffs against
the manifest, and (b) greps agent definitions and hook config for pulled/pushed
paths and diffs against the consumer lists. Run it in the existing pre-commit
hook and in orchestrator pre-flight. Then the manifest can drift for at most
one commit. Cost: an hour or two, once.

### 2.4 Claude Code-native capabilities being re-invented (pressure point 4)

Covered in Phase 1. The headline exploitations left on the table, restated as
actions:

- Push via `SubagentStart` hook (or `skills:` preload) — not hand-rolled prompt
  assembly. The hook script logs sha256 + version of what it injected: an
  **orchestrator-side receipt that does not depend on the model at all**.
- Enforce structured output via `--json-schema` / SubagentStop validation;
  make `ESCALATE` an enum value of a required `status` field so the escalation
  rule (design §3.2) is machine-readable rather than string-matched prose.
- Pre-flight as a `SubagentStart` hook, so it also protects ad hoc interactive
  invocations, not only scripted batches.
- Pin `model:` in every agent definition (D2).
- Use `tools:`/`disallowedTools` to *enforce* the adversarial reviewer's
  artefacts-only rule (currently prose): the reviewer needs Read/Grep/Glob/Bash
  only; denying everything else converts a stance instruction into a hard
  constraint. `maxTurns` bounds runaway loops.
- One caution the docs surface that the design should record: agent definition
  files are **hot-reloaded** (a file watcher applies edits within seconds).
  Convenient in development; in production it means an edited agent definition
  takes effect immediately, bypassing the regression-gate discipline unless the
  pre-flight hash-checks agent definitions against the manifest. See D10.

### 2.5 Concurrency and parallelism

The design is silent on execution mode. The FAIR lane is embarrassingly
parallel (independent papers, no shared state beyond the queue file). Serial
execution at ~8–15 min/paper is 37–70 hours of wall-clock for ~280 papers;
4–6 concurrent headless workers bring it to ~8–14 hours. The queue file needs a
trivial locking discipline (per-paper status files, or flock) either way.
Reproduction-lane parallelism is already bounded by Docker/compute and human
plan approval — serial is fine there.

### 2.6 Preregistration-constraint check (does the design break §8? — mostly no, with three catches)

Checked against phase-2-preregistration-draft.md v0.7 and the review skill's
study-design checklist:

- Blinding (assessment-before-reproduction, fresh-context adversarial review):
  **preserved and strengthened** — architectural subagent boundaries plus
  workflow sequencing match prereg §8. ✓
- Regression gate on instrument/agent/model change (design §3.7): **matches**
  prereg §8 permitted-changes clause. ✓
- Lodgement consistency check (design §6.4): **present**. ✓
- Instrument reliability plan: **present** (prereg §8), and interacts with
  routing as described in §2.1 above — the interaction should be written down.
- **Catch 1 (D1):** the file the design designates as the FAIR instrument's
  canonical home — and which the preregistration attaches and freezes — is
  internally inconsistent (see D1). Frozen-with-a-bug is the worst of both
  worlds: fixing it later requires an OSF amendment; not fixing it pushes
  contradictory scoring instructions to every census invocation.
- **Catch 2 (D3):** the design cites "taxonomy L1–L5 + 3-level collapse"; the
  preregistration was revised 2026-07-18 (v0.5) to **six** friction-ordered
  levels with a different collapse composition (open = L1–L2, mediated = L3,
  effectively closed = L4–L6). The design predates the revision and must be
  updated before Phase 1 builds the instrument file from the wrong spec.
- **Catch 3 (D3):** the design pushes the availability taxonomy to
  `fair-assessor` for "statement-level" assignment at census. Prereg §7.3 is
  explicit that levels are "assigned at reproduction time from actual retrieval
  attempts, not statements alone". A census-time statement-based L-assignment is
  a *shadow variant* of the preregistered instrument; if its values ever leak
  into analysis under the same name, H2's predictor is contaminated. The census
  frame-recording (§4) only requires availability-*statement* presence. Fix by
  naming: record a census field called e.g. `stated_availability` (descriptive
  only, never mapped to L1–L6), and keep the L-scale exclusively
  reproduction-side.

---

## Phase 3 — Quantitative audit (pressure point 5: push economics at census scale)

Assumptions, stated: ~4 characters/token; census scale per the preregistration's
power table — ~160 eligible quantitative *Journal of Archaeological Science*
(JAS) papers + ~120 *JAS: Reports* control = **~280 fair-assessor invocations**
(unknown until the sweep; could be 80–400); reproduction subset ≤25 papers ×
3 agents. Pricing (claude-api skill, cached 2026-06-24): Claude Opus 4.8
$5/$25 per million tokens (MTok) input/output; Claude Sonnet 5 $3/$15; prompt
cache reads ~0.1×, writes 1.25×.

Measured pushed-content sizes:

| Pushed item | Size | ≈ tokens |
|---|---|---|
| Pass 6 prompt (proposed FAIR instrument home, whole file) | 32,575 B | ~8,100 |
| Availability taxonomy (prereg §7.3 as its own file) | ~3 KB | ~750 |
| Inventory/frame fields | ~1 KB | ~250 |
| **fair-assessor push, per invocation** | | **~9,100** |
| Executor push (invariants + verdicts/precision + coverage) | ~12 KB | ~3,000 |
| Planner push (coverage + eligibility + taxonomy) | ~11 KB | ~2,750 |
| Adversarial framework (promoted to pushed) | 11,986 B | ~3,000 |

Aggregates (formula: invocations × pushed tokens × price):

| Scenario | Pushed tokens total | Cost @ Sonnet 5 | Cost @ Opus 4.8 | With prompt caching |
|---|---|---|---|---|
| FAIR lane, baseline (280 inv.) | ~2.5 M | ~$7.60 | ~$12.70 | ~$1–3 |
| FAIR lane, 3× majority-vote fallback (840 inv.) | ~7.6 M | ~$23 | ~$38 | ~$3–8 |
| Reproduction lane (25 papers × 3 agents) | ~0.22 M | <$1 | ~$1.10 | negligible |

For context, the paper text itself (~30k tokens/paper as PDF) plus multi-turn
working context dominates: the whole FAIR lane is very roughly 30–90 M input
tokens ≈ **$150–600 at Opus-class API pricing (uncached mix), or well under
half that with caching / on a subscription plan** — and `--output-format json`
reports `total_cost_usd` per invocation, so the pre-scale cost gate (plan §5
Phase 3) gets exact numbers from the first 2–3 papers for free.

**Answer to design open question 3 (prompt-size economics):** push cost is
~2–5% of the lane's total token bill and single-digit-to-tens of dollars in
absolute terms at any plausible census size. **Do not trim the instrument for
cost.** The only defensible reason to trim is *attention quality* — an 833-line
mixed-content prompt dilutes the salience of the actual scoring rubric — and
that argues for extracting the clean instrument core (D1), which is needed
anyway.

Wall-clock (Phase 2.5): serial ~37–70 h; 4–6 concurrent workers ~8–14 h.
Failure-cascade: per-paper independence means a failed paper costs one paper
either way; the queue checkpoint design already handles this. ✓

---

## Phase 4 — Findings and recommendations

**Defects** would produce wrong study data, break the preregistration's
auditability, or cause maintenance drift. **Enhancements** are better use of
the capability envelope. Ranked by severity within each class.

### Defects

**D1 — CRITICAL (fix before OSF lodgement). The FAIR instrument's designated
canonical home is internally inconsistent and mixes frozen with evolving
content.** `06-infrastructure_pass6_prompt.md` — which the design designates
canonical (§4) and the preregistration attaches and freezes — contains:
(a) a stale scoring remnant at STEP 6: "Total FAIR score (e.g., 14/16)" and
"87.5%" (line ~662), contradicting the v2.0 /15 rubric defined at lines
119–163 — pushed verbatim to ~280 scoring invocations, this is a
silent-wrong-output hazard for the study's central variable, and frozen into
the registration it becomes an amendment-requiring embarrassment;
(b) the *legacy 5-level (0–4) access taxonomy* inside `data_completeness`
(lines ~204–208), which will collide in agents' context with the
preregistration's L1–L6 availability taxonomy — two different level-schemes
with overlapping vocabulary travelling in one prompt;
(c) a dead pointer to `wiki/planning/REPRODUCIBILITY_INFRASTRUCTURE_SCHEMA.md`
(line ~802; file does not exist — verified) — a live instance of the pull
failure the design is engineered against, inside its own canon;
(d) 700+ lines of workflow guidance (extraction order, ORCID protocol, ethics
sections, pitfalls) that would be frozen alongside the instrument, so any
workflow improvement later triggers regression gate + OSF amendment, or tempts
an ungated edit.
*Recommendation:* extract a clean instrument file
(`studies/open-science-compliance/protocol/instruments/fair-instrument.md`:
15 sub-principles, A1 completeness rule, bands, independent data/code scoring
rule, and the data-completeness coverage procedure it depends on), consistent
with the design's own pattern for the other new instrument files; the Pass 6
prompt points to it; fix the /16 remnant and the dead pointer in the prompt
regardless; rename the legacy 0–4 levels (e.g. "access tiers") to break the
collision. Do all of this **before** lodgement while fixes are free — the
preregistration is at "awaiting final read-through". *Cost:* 1–2 hours.

**D2 — HIGH. Model identity and agent-definition version are uncontrolled and
unreceipted.** The design's receipts cover instrument text only, but the
effective instrument at census scale is (instrument × agent definition ×
model). `model:` defaults to `inherit` — whatever model the invoking session
happens to run — and `CLAUDE_CODE_SUBAGENT_MODEL` silently overrides
frontmatter. The design's own §3.7 makes model change a regression-gate
trigger, yet nothing in the design detects one. *Recommendation:* pin a full
model ID in each scoring agent's frontmatter; register agent-definition
versions in the manifest; extend the receipt/output metadata to
`{instrument_versions, agent_version, model_id}`; have pre-flight fail if
`CLAUDE_CODE_SUBAGENT_MODEL` is set unexpectedly. *Cost:* trivial (frontmatter
lines + two receipt fields + one env check).

**D3 — HIGH. The design cites a superseded instrument and creates a shadow
variant of it.** (i) Design §4 says "Data-availability taxonomy L1–L5 +
3-level collapse"; prereg v0.5+ (2026-07-18) defines **six** levels with a
changed collapse (open L1–L2 / mediated L3 / effectively closed L4–L6). If
Phase 1 builds `data-availability-taxonomy.md` from the design's spec, the
canonical file is born wrong. (ii) Design §5 pushes the taxonomy to
`fair-assessor` for "statement-level" assignment at census, but prereg §7.3
assigns levels only at reproduction time from actual retrieval attempts — a
census-time L-assignment is a second, non-preregistered instrument variant
that risks contaminating H2's predictor if ever conflated. *Recommendation:*
update the design to L1–L6 before build; rename the census-side field
(`stated_availability`, descriptive only, never mapped to L1–L6) and state in
the instrument file that L-levels are reproduction-side only. This is also a
neat vindication of the design's own thesis — the stale reference exists
*because* the taxonomy currently lives inside a prose document rather than one
canonical file. *Cost:* 30 minutes of edits.

**D4 — MEDIUM. The read-receipt echo is not the hard gate the design claims.**
For pushed content it verifies delivery/assembly only; for pulled content it is
defeasible by partial reads or convention-guessing (full analysis §2.2).
*Recommendation:* (1) unguessable receipt token at end-of-file, registered in
the manifest; (2) SubagentStop hook that verifies Reads from the
harness-recorded agent transcript (paths + absence of `limit` truncation);
(3) receipts structurally required via schema; (4) `decision: "block"` for
in-session remediation. Keep the echo as the assembly check it actually is.
*Cost:* one-off token insertion + ~half a day for the hook script, shared by
all agents.

**D5 — MEDIUM. `shared_content` recreates the hand-synchronisation pathology
it warns against** (§2.3). *Recommendation:* manifest-consistency check script
(file version lines + consumer greps vs manifest) wired into the existing
pre-commit hook and orchestrator pre-flight; the registry becomes verified
rather than merely maintained. *Cost:* 1–2 hours.

**D6 — MEDIUM. "Loud" failure depends on gates that only check existence and
non-emptiness.** Template-conformance and comparison-report structure feed the
adversarial review and the H2 coverage computation; a malformed-but-non-empty
artefact passes the plan's gates silently. *Recommendation:* make the
comparison report's quantitative table a schema-validated machine-readable
artefact (the design already wants "structured outputs everywhere" — extend
the principle from agent handoffs to persisted artefacts) and validate at the
stage gate. This is what actually licenses leaving templates in the pulled
class. *Cost:* half a day for validators.

**D7 — LOW. `.claude/agents/shared/invariants.md` puts non-agent content
inside the recursively scanned agent-discovery tree.** The docs state
`.claude/agents/` is scanned recursively and files are parsed as agent
definitions; behaviour for a frontmatter-less content file there is
undocumented. Don't rely on it. *Recommendation:* relocate shared canon to
`.claude/shared/` or the `protocol/instruments/` directory. *Cost:* a path.

**D8 — LOW. Planner's silent-failure surface is wider than the routing table
admits.** Verification-target enumeration (the H2 denominator) is influenced by
pulled `verification-strategies.md` (§2.1 item 1). *Recommendation:* add a
deterministic enumeration-completeness check to plan validation — count
display items (tables/figures/named values) detected in the paper text vs
targets enumerated; flag plans below a threshold ratio for explicit human
attention at batch approval. Cheap, and converts the silent miss to a visible
one. *Cost:* small script + one line in the planner's output contract.

**D9 — LOW. No trigger for routing-class migration.** *Recommendation:* add
one line to the §3.7 regression-gate checklist: "re-confirm the routing class
of every changed file"; plus a standing rule that any pulled file cited as
decisive for a score/verdict gets a promotion review. *Cost:* two sentences.

**D10 — LOW. Two harness behaviours need explicit governance lines in the
design:** (i) **prohibit `memory:` on scoring agents** — persistent agent
memory would make paper N's score depend on papers 1…N−1 (order-dependence),
quietly violating the fixed-instrument assumption; (ii) **agent hot-reload** —
edited agent definitions take effect within seconds, so the regression-gate
discipline must be enforced procedurally (pre-flight compares agent-file hashes
to the manifest, refusing to run on unregistered edits). *Cost:* two paragraphs
+ the hash check already implied by D5's script.

### Enhancements (capability envelope)

**E1 — Build the push mechanism on `SubagentStart` `additionalContext` (first
choice) or `skills:` preloading (second), not hand-rolled prompt assembly.**
Deterministic at the harness level; identical behaviour in scripted and
interactive lanes; the hook logs sha256/version of what it injected — an
orchestrator-side receipt independent of the model. Largely answers design open
questions 1 and 5. *Cost:* the hook script is ~30 lines; less code than the
hand-rolled alternative.

**E2 — Enforce output contracts with `--json-schema` (headless) plus
SubagentStop validation (interactive).** Make `status` an enum including
`ESCALATE`, and `instrument_versions`/`agent_version`/`model_id` required
fields. *Cost:* one schema file per agent.

**E3 — Use SubagentStop `decision: "block"` for self-healing receipt/contract
failures** instead of failing the batch item. *Cost:* part of the E2 hook.

**E4 — Feed the pre-scale cost gate from `total_cost_usd`** in headless JSON
output; per-paper cost tracking becomes a byproduct. *Cost:* nil.

**E5 — Parallelise the FAIR lane** (4–6 concurrent headless workers; per-paper
lock discipline): ~37–70 h serial → ~8–14 h. *Cost:* small runner script.

**E6 — Enforce the adversarial reviewer's isolation with `tools:` restrictions
and `maxTurns`**, converting the artefacts-only rule from stance prose to hard
constraint. *Cost:* frontmatter.

**E7 — Endorse design open question 4:** `corpus-screener` should be a script
(CrossRef/OpenAlex sweep is deterministic) with a narrow LLM triage step for
the quantitative/computational flags — implementable as `claude -p` with
`--json-schema` per paper, receipts included. The quantitative flag is H1
sample-defining, so the triage prompt is instrument-like: give it a canonical
file, a version line, and a receipt like the others.

**E8 — Close design open question 3 with the Phase 3 numbers:** push economics
are negligible (≤~$40 worst case across the whole census); trim only for
salience, which D1's instrument extraction delivers anyway.

### Overall recommendation

**Significant redesign of the *mechanism*, none of the *policy*.** Adopt the
routing rule, canonical-home principle, and maintenance rules as written
(after D3's taxonomy correction); replace the hand-rolled push/receipt/
pre-flight plumbing with the native hook + frontmatter + json-schema
implementations (E1–E3); and treat D1 as a lodgement blocker — it is the one
finding where a few hours now avoids a public OSF amendment later. Everything
else is an hour-scale fix that fits naturally into the Phase 1 build.

### Priority order (effort vs risk retired)

1. D1 (pre-lodgement, 1–2 h) — protects the registration itself.
2. D3 (30 min) — stops a wrong canonical file being built.
3. D2 + D10 (1 h) — pins the full instrument identity.
4. E1 + E2 + E3 + D4 (≈1 day) — the reliability core of Phase 1.
5. D5 + D6 (≈1 day) — drift-proofing and manufactured loudness.
6. D7, D8, D9, E4–E8 — fold into Phase 1 as encountered.
