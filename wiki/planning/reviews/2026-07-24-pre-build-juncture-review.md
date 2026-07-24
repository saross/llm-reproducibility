# Pre-build juncture review: routing design v0.2.1, corpus plan v0.2, combined validation phase

**Protocol:** `~/.claude/skills/review-implementation/SKILL.md` — all phases applied,
including the Study Designs and Preregistrations checklist.
**Date:** 2026-07-24. No repository files modified.
**Targets:** (1) `wiki/planning/agent-content-routing-design.md` v0.2.1 —
(a) fidelity to the two 2026-07-22 review passes, (b) new content §2.1–2.2, §3 rebuild,
§9; (2) `wiki/planning/corpus-management-plan.md` v0.2 implementation scope;
(3) the combined validation phase (regression gate + reliability spot-check,
`wiki/continuity.md` "Repo state (2026-07-23)" + preregistration §8).
**Sources verified this session:** the three planning documents in full; the
preregistration §7–§11 (`studies/open-science-compliance/protocol/phase-2-preregistration-draft.md`,
including §8 "Instrument reliability" at lines 473–483 verbatim); the erratum log;
`manifest.yaml`; `agentic-modernisation-plan.md` (full); current Claude Code
documentation via the local mirror `~/.claude-code-docs` (synced 2026-07-22:
`workflows.md`, `hooks.md`, `sub-agents.md`, `headless.md`, `costs.md`,
`agent-sdk__cost-tracking.md`, `agent-sdk__typescript.md`, `prompt-caching.md`,
`cli-reference.md`, `changelog.md`).

**Verdict up front:** the design corpus is in strong shape — the fidelity audit found
no dropped or mistranslated findings from the 2026-07-22 review passes, and the corpus
implementation scope is sound. The build should proceed, but four things need fixing
first, all cheap: (1) the §2.2 remediation ladder deviates from the preregistration's
pre-specified below-threshold consequence and must be pre-specified in the
already-owed Open Science Framework (OSF) amendment *before* the reliability check
runs; (2) §9's adoption of Claude Code workflows rests on a hook-firing assumption the
current documentation actively undercuts — the verification spike must run first and a
fallback engine (headless `--agent` fan-out) should be named now; (3) the §3.4
pre-flight is attached to a hook that cannot block, and should move to
`PreToolUse[Agent]`; (4) the validation phase re-scores papers whose canonical answers
sit readable in the same repository — an isolation rule must be pre-specified or the
reliability estimate is contaminable. A model-selection rule for the multi-model
spot-check is missing entirely and the spot-check cannot statistically supply one; it
must be pre-specified on other grounds (gates-plus-cost), also in the amendment.

---

## Fidelity audit (target 1a): v0.2/v0.2.1 against the two review reports

Checked every finding of
`wiki/planning/reviews/2026-07-22-routing-design-implementation-review.md` (D1–D10,
E1–E8) and the verified scout report against the design text. Translation is audited,
not the findings themselves.

| Finding | Where it landed in v0.2.1 | Fidelity |
|---|---|---|
| D1 instrument extraction + 3 prompt defects | §4 row 1; erratum path recorded | Faithful (incl. post-lodgement reframing) |
| D2 model pinning, env-var check, receipt triple | §3.3 | Faithful |
| D3 L1–L6 correction + `stated_availability` | §4 row 2, §5 fair-assessor row | Faithful, correct collapse (open L1–L2 / mediated L3 / effectively closed L4–L6) |
| D4 layered receipts (token, transcript gate, schema, self-heal) | §3.2 | Faithful — all four strengthenings present plus the delivery check |
| D5 machine-verified `shared_content` | §4 registry paragraph | Faithful (pre-commit + pre-flight wiring, one-commit drift bound) |
| D6 structural artefact gates | §3.5, §2.1 item 2 | Faithful |
| D7 relocate invariants out of `.claude/agents/` | §4 invariants row (`.claude/shared/`) | Faithful |
| D8 planner enumeration-completeness check | §5 planner row | Faithful |
| D9 migration trigger | §6 rule 6, §2.1 item 3 | Faithful |
| D10 `memory:` prohibition + hot-reload governance | §3.9, §6 rule 7, §3.4 hash check | Faithful |
| E1–E3 native push / schema / self-heal | §3.1, §3.6, §3.2 | Faithful |
| E4 cost gate from `total_cost_usd` | Appendix | Faithful (but see defect D-8 below — the claim itself needs a subscription caveat) |
| E5 parallelism numbers | Appendix | Faithful |
| E6 reviewer `tools:` + `maxTurns` | §3.7, §5 row | Faithful |
| E7 screener demotion | §5 row, §7.4 | Faithful |
| E8 push economics closure | §7.3 | Faithful (incl. cold-cache caveat and issue #29966) |
| Scout: `skills:` + silent-skip caveat | §3.1 | Faithful, verbatim caveat |
| Scout: cold cache / #29966 / empirical check | §7.3 | Faithful |
| Scout: pyalex/habanero, Affinage, LLMSurver, ASReview | §5 screener row + note | Faithful |

**Two soft drops (record a decision, nothing more):**

1. **promptfoo (scout row 8, "Adapt" recommendation).** The scout suggested
   promptfoo's pass-rate-drop continuous-integration pattern as a ready-made way to
   implement the §8 regression gate mechanically. v0.2 mentions neither adoption nor
   rejection. Not an error — the hand-rolled gate is small — but the design should
   record the reject/adopt call so the drop is deliberate. *Cost: one sentence.*
2. **Cache-warmth pipelining (scout verdict 3, remediation (b)).** The scout offered
   "pipeline invocations to preserve cache warmth within 5-minute windows" as the
   remediation if subagent caching does not materialise; §7.3 keeps the empirical
   check but drops the remediation option. Superseded in part by enhancement E-3
   below, but worth carrying. *Cost: one clause.*

**One inherited wording defect (now normative in §2.2, so flagged as a defect
below, D-1c):** both the review (§2.1) and design §2.2 say the post-routing-fix
re-run is "the pilot comparability check". The check that measures inter-run
variance is preregistration §8(a) — the *stability* check (3 papers × 3 runs) —
not §8(b) comparability. Faithful translation of a source slip.

**No finding was dropped, weakened, or mistranslated.** The v0.2 change summary's
"verified 107/110 claims; 0 corrections" is accurate to the scout report (107 pass,
3 unverifiable-by-design, 0 corrections).

---

## Phase 1 — Capability scan

What exists in the solution space that the three targets do not yet use or
mis-describe. Verified against the docs mirror (synced 2026-07-22).

1. **Headless single-agent sessions: `claude -p --agent <name>`** (cli-reference.md).
   Runs a named agent definition *as the main session*: frontmatter hooks fire on
   this path by documentation ("when the agent runs as the main session via
   `--agent`", sub-agents.md §Define hooks for subagents), the frontmatter `model:`
   full-ID pin applies, `--json-schema` output enforcement applies, and — decisive on
   a subscription — the **main conversation gets the automatic 1-hour prompt-cache
   TTL** (prompt-caching.md §Subagents and the cache), where subagents get a cold
   5-minute-TTL cache per spawn. A per-paper `claude -p --agent fair-assessor`
   fan-out is therefore the best-documented engine for the census lane, and §9 never
   considers it. See defect D-2 and enhancement E-3.
2. **`PreToolUse` hooks can block the Agent tool call** (hooks.md: PreToolUse
   supports deny decisions; SubagentStart explicitly "can't block subagent
   creation"). The blocking pre-flight the design wants exists — on a different
   hook than the one §3.4 names. See defect D-3.
3. **`--agents` JSON flag** (cli-reference.md): define subagents dynamically with
   the same fields as frontmatter, including `model` (full ID) — a clean way to
   generate the per-model agent variants the validation matrix needs without
   duplicating definition files. See defect D-7.
4. **OpenTelemetry workflow attributes** (changelog v2.1.2xx): workflow-spawned
   agents emit `workflow.run_id` and `workflow.name`, so if workflows are adopted, a
   machine-readable run journal can be reconstructed from OTel — the "run journal"
   §9 promises to archive is not otherwise a documented artefact.
5. **Elsevier text-and-data-mining (TDM) API** (non-harness): for a census that is
   mostly *Journal of Archaeological Science* (JAS; Elsevier), institutional TDM
   entitlement can legally automate closed-access full-text retrieval that the
   Unpaywall-only fetch script cannot, and that ScienceDirect's HTTP 403 (known from
   pilot notes, modernisation plan §7) actively blocks. Not yet considered anywhere
   in the corpus plan. See enhancement E-2.
6. **Anthropic Message Batches API** — reconsidered and re-rejected for the same
   reason as the July review (bypasses the harness the preregistration's regression
   gate validates); noted for completeness.

## Phase 2 — Exploitation review

Where the current plans use less of the envelope than is available, or claim more
than the envelope provides. Each item is expanded as a ranked finding in Phase 4.

- **§9 workflow engine (target 1b).** Doc surface contradicts two of §9's load-bearing
  assumptions: (i) hooks — `SubagentStart`/`SubagentStop` are documented as firing for
  spawns "via the Agent tool", and sub-agents.md separately distinguishes "agents a
  workflow script spawns with `agent()`" from Agent-tool spawns (they do not even
  share the subagent count limit); frontmatter hooks are likewise documented for
  Agent-tool spawns and `--agent` main sessions only. §9's build-time verification
  (i) is thus more likely to fail than pass on current documentation, and no fallback
  engine is named. (ii) resume — `resumeFromRunId` is documented "Same session only"
  (agent-sdk__typescript.md, WorkflowInput); combined with workflows' documented lack
  of filesystem access, the claim that workflow resume replaces "the queue's
  checkpoint/resume without hand-built locking" does not hold across session
  boundaries, which is exactly when a 280-paper run needs it.
  What §9 gets right, verified: no mid-run user input; no script filesystem access;
  schema-enforced structured outputs with bounded retries (validation aborts after 5
  attempts per the changelog); per-run agent caps; script persisted to disk.
- **Concurrency:** workflows support up to 16 concurrent agents; the design plans
  4–6. Modest headroom, usable if the engine survives verification.
- **Model control:** subagent model resolution order (sub-agents.md) is
  env var → **per-invocation `model` parameter** → frontmatter → session model. The
  per-invocation parameter is *alias-only* (`sonnet`/`opus`/`haiku`/`fable`) and
  **outranks the frontmatter full-ID pin**. §3.3 guards the env var but not this
  middle layer. Receipts detect it; nothing yet blocks on it.
- **Cost instrumentation on the Max plan:** `total_cost_usd` is a **client-side
  estimate from a bundled price table** ("not authoritative billing data",
  agent-sdk__cost-tracking.md) and on a subscription "the session cost figure isn't
  relevant for billing" (costs.md). The binding constraint on Max is the shared
  session/weekly usage windows, which none of the plans measure.
- **Reliability spot-check n:** preregistration §8 says "at least three pilot
  papers" — five exist. Using all five is free precision inside the preregistered
  wording (E-1).
- **Corpus:** backup (item 7) sequenced after the census blockers; meta.json schema
  undefined; fetch politeness undefined; closed-access human-time unbudgeted.

## Phase 3 — Quantitative audit

### 3.1 Statistical adequacy of the reliability spot-check (pressure point c)

**Setup as pre-specified:** ≥3 pilot papers × 3 runs; 30 binary sub-principles per
paper (15 data + 15 code); gate = mean per-sub-principle agreement ≥ 0.90.

**A pre-specification gap first:** with three runs of a binary item, "agreement" has
at least three inequivalent definitions — unanimity proportion (all three runs
match), pairwise proportion (agreeing pairs / 3; values 1 or 1/3), and match-to-mode
(2/3 for a 2–1 split). At the same underlying instability they cross the 0.90 gate at
very different flip rates: a 0.90 mean corresponds to ~10% of items split under
unanimity, ~15% under pairwise, ~30% under match-to-mode. The statistic must be
defined before the check runs (amendment item; see D-5).

**Gate precision (computed under unanimity; binomial, n = 3 × 30 = 90 items):**

| True agreement p | Behaviour at the 0.90 gate (n=90) | At n=150 (5 papers) |
|---|---|---|
| 0.95 | false-fail ≈ 0.8% | ≈ 0.1% |
| 0.90 | pass ≈ coin flip (inherent to a point threshold) | same |
| 0.85 | **false-pass ≈ 12%** | ≈ 5.5% |
| standard error of the estimate at p=0.90 | 0.032 (95% CI ±0.062) | 0.024 (±0.048) |

These are best-case figures: items cluster within paper (shared documentation
quality) and within sub-principle across papers (shared ambiguity), so the effective
n is below 90 and a design effect of 1.5–3 would widen the confidence interval to
roughly ±0.08–0.11. Two further inflators: (i) papers with little or no
infrastructure make many items deterministic zeros (the instrument's
unscoreable-scores-0 rule), which pads agreement with uninformative items — with the
five pilots this is material for the code-side items of papers without code
artefacts; (ii) three papers give only three draws of the paper-level effect.
**Adequacy verdict for the pass/fail gate: adequate as a coarse gate, marginal near
threshold.** Moving to all five pilot papers (n=150) halves the false-pass rate at
p=0.85 and costs six extra invocations per model — and is permitted by the
preregistration's own "at least three pilot papers" wording, no amendment needed.

**Model discrimination: not achievable at this n, and not achievable at any
preregistration-compliant n.** For two models on the same 90 items, the unpaired
standard error of the agreement difference at p≈0.9 is √(2×0.09/90) ≈ 0.045 — a 95%
confidence interval of ±0.09 (pairing on items might shrink this to ±0.05–0.07). The
spot-check therefore cannot distinguish, say, 0.96 from 0.92. Distinguishing a
4-point difference at 80% power needs ≈550 items per arm unpaired (≈18 papers) or
roughly 250–300 paired (≈9–10 papers) — but §8 restricts reliability checks to
**pilot papers only**, of which five exist (150 items). A statistically grounded
model ranking is structurally unavailable before the census. The selection rule must
therefore not depend on ranking by agreement — see D-5 for the pre-specifiable
alternative (gates-plus-cost, with accuracy against the pilot reference scores as a
second gate). Incremental cost of the multi-model spot-check itself is small: 5
papers × 3 runs × 2 models = 30 invocations ≈ US$17–65 at
Application Programming Interface (API)-equivalent prices (per-invocation ≈$0.55–2.15
from the July review's Phase 3 numbers), ~4–8 h wall-clock at 4–6 workers; a Fable 5
arm adds 15 invocations (ask-first gate applies).

### 3.2 Census-scale aggregates on the Max subscription (pressure point b/f)

Whole Findable, Accessible, Interoperable, Reusable (FAIR) lane (~280 invocations):
~30–90 M input tokens, ~37–70 h serial, ~8–14 h at 4–6 workers (review Phase 3,
re-confirmed). At API prices this is ~US$150–600 uncached. **On the Max plan the
number that matters is different:** usage is bounded by shared 5-hourly/weekly
windows, `total_cost_usd` is a notional estimate, and a census of this size will
plausibly exhaust one or more weekly windows mid-run. The pre-scale cost gate must
therefore instrument three things from the first 2–3 papers: token counts including
the `cache_read_input_tokens` split (already mandated by §7.3), the notional USD
estimate, and **the fraction of the plan's usage bar consumed per paper** (read
`/usage` before/after the probe) — yielding a weeks-to-census figure and an explicit
decision point: pace the census across windows, buy usage credits, or run the lane on
an API key. Failure-cascade economics are unchanged (per-paper independence, queue
checkpoint).

### 3.3 Corpus acquisition (pressure point d)

Frame ~160 JAS + ~120 *JAS: Reports* papers. Unpaywall resolves the open fraction;
the closed fraction needs manual or TDM acquisition. Planning range (to be replaced
by the sweep's own frame report, per preregistration §10): 40–70% closed →
~110–200 papers; at 2–3 min each via library proxy that is **4–10 h of human time
the plans nowhere budget**, and the pilot-documented ScienceDirect 403 rules out
naive scripted download. The pilot's own open-access audit (6 of 8 papers CC BY) is
a biased sample of reproducibility-friendly papers and should not be extrapolated.
Politeness for `fetch-corpus.py`: Unpaywall requires an email parameter
(100k req/day free); CrossRef polite pool wants a `mailto` User-Agent; neither rate
limits nor retry/backoff are specified in the plan. All cheap to add (D-11).

---

## Phase 4 — Findings and recommendations

**Defects** would produce wrong study data, break preregistration auditability, or
build on a mechanism that does not exist as described. **Enhancements** are unused
capability. Ranked by severity within each class.

### Defects

**D-1 — CRITICAL (compliance). The §2.2 remediation ladder is a deviation from
preregistration §8 as written, and must be pre-specified in the pending OSF
amendment before the reliability check runs.** The preregistration (lines 473–477)
pre-specifies exactly one below-threshold consequence: "If below threshold, the
census is scored by majority vote of three independent runs per paper." §2.2 instead
inserts a routing fix + re-run ahead of that fallback, claiming shelter under §8's
permitted-changes clause. The claim is half right: **(a)** the routing fix *itself*
(delivery-mechanism change, instrument text untouched) is a legitimate implementation
change under §8 — regression gate on pilot artefacts + erratum-log entry, exactly as
§2.2 says. **(b)** But *substituting* fix-and-re-test for the pre-specified
consequence of a failed gate is not an implementation change — it alters what the
registration says happens on failure, so it falls under §9's catch-all: "Any
deviation from this registration will be lodged as a dated OSF amendment with
rationale before the affected analysis runs." Deciding the ladder *after* observing a
failure would also be data-contingent (test-until-pass on an n=90–150 gate with a
~12% false-pass rate at p=0.85 — see Phase 3.1). **The compliant path, precisely:**
an OSF amendment is already committed before census scoring (erratum-log header,
approved 2026-07-22). Fold the ladder into that amendment and lodge it **before the
validation phase runs**, specifying: (i) one routing-fix attempt maximum — if the
re-run gate still fails, majority vote applies with no further iteration; (ii) the
re-run is §8(a) *stability* (and §8(b) comparability only if the push changes the
census-path prompt) — fixing the inherited "comparability check" mislabel (fidelity
note); (iii) both pre-fix and post-fix reliability results are reported with study
outcomes (§8 already requires outcome reporting). *Cost: one paragraph in the
amendment + two line edits in §2.2. Zero if done before the validation phase;
a public data-contingent-deviation problem if done after.*

**D-2 — HIGH (mechanism). §9's adoption of workflows as the batch engine rests on a
verification the documentation suggests will fail, and no fallback engine is
named.** Three independent doc statements point the same way: hooks.md scopes
`SubagentStart` to spawns "via the Agent tool"; sub-agents.md explicitly
distinguishes workflow `agent()` spawns from Agent-tool spawns (separate limits);
and frontmatter hooks are documented for Agent-tool spawns and `--agent` main
sessions only. If hooks do not fire for workflow-spawned agents, the census lane
loses push injection, the transcript hard gate, self-healing, and pre-flight — the
whole §3 reliability layer — in the one lane that scores the study's dependent
variable. Additionally, nothing in the docs says workflow `agent()` can spawn a
*named* agent definition at all, which §9's "or via the agent definitions" push
route quietly assumes. *Recommendation:* (1) run §9's verification spike **first, in
Phase 1's opening hour**, not as a background item; (2) name the fallback now:
per-paper **`claude -p --agent fair-assessor` fan-out** (Phase 1 capability scan
item 1) — frontmatter hooks documented to fire, full-ID model pin applies,
`--json-schema` applies, 1-hour cache TTL on subscription, 4–6 workers via a small
runner + `flock` (review E5); (3) reword §9 from "adopted" to "adopted conditional
on verification (i); fallback: headless `--agent` fan-out" so the engine choice is
falsifiable rather than committed. *Cost: spike ~1 h; wording 15 min; the fallback
runner is the ~50-line script E5 already priced.*

**D-3 — HIGH (mechanism). §3.4's blocking pre-flight is attached to a hook that
cannot block.** hooks.md is explicit: "SubagentStart hooks can't block subagent
creation"; its exit-code-2 stderr is a transcript notice the model never sees, and
the subagent proceeds. As written, "missing canon fails the batch before token
spend" is unenforceable on the interactive lane. *Recommendation:* move the blocking
pre-flight to a **`PreToolUse` hook matched on the Agent tool** (documented deny
capability — it can refuse the spawn before token spend); keep `SubagentStart` for
what it can do (inject content + warnings); scripted lane runs pre-flight in the
runner before invocation, as the design already implies. *Cost: same script,
different hook event — ~30 min.*

**D-4 — HIGH (validation design, pressure point e). The reliability spot-check is
contaminable: the answers are in the repository the scoring agent can read.** The
pilot papers' canonical FAIR scores (extraction.json), the pilot findings report
(Table 5 /15 scores), and reproduction verdicts all sit in the working tree. A
fair-assessor run that greps its own repo can reproduce the recorded scores across
all three runs — perfect agreement, zero information — and the
assessment-before-reproduction blinding clause (§8) is likewise moot if reproduction
outcomes are readable. This is the Study-Designs checklist's criterion-contamination
item in operational form. *Recommendation:* pre-specify (amendment, with D-1's
paragraph): validation-phase scoring runs execute with read access **only** to the
paper source and the pushed/pulled instrument files — enforced via `tools:`
allowlist/sandbox scope, and *verified from the harness transcript* by the same
SubagentStop machinery §3.2 already builds (synergy: the contamination check is the
receipt check pointed at a deny-list). Record per-run file-access lists with the run
artefacts. Same rule applies at census for any paper with pre-existing repo
artefacts (the five pilots are excluded from confirmatory analyses, but hygiene
should be uniform). *Cost: one allowlist + one transcript grep — inside the D-4/E2
hook work already planned.*

**D-5 — MEDIUM-HIGH (validation design, pressure points c+e). Two missing
pre-specifications: the agreement statistic and the model-selection rule.**
(i) "Mean per-sub-principle agreement" is undefined for three runs of a binary item
(Phase 3.1: the three natural definitions cross 0.90 at flip rates from 10% to 30%).
(ii) No document records what happens when **both** Sonnet 5 and Opus 4.8 clear
0.90 — and Phase 3.1 shows the spot-check cannot rank models (±0.09 CI on the
difference; a compliant n does not exist pre-census). *Recommendation (both items
into the D-1 amendment):* define agreement (recommend unanimity proportion — it is
the strictest and simplest to audit); pre-specify selection as **gates-plus-cost**:
any model passing (a) the 0.90 stability gate and (b) a concordance floor against
the pilot reference scores (see E-4) is eligible; among eligible models the
cheapest/fastest (Sonnet 5) scores the census; agreement differences inside the
confidence interval are pre-declared not to be selection grounds; non-selected
passing arms are archived as robustness data (E-7). Also pre-specify *which* pilot
papers (recommend: all five — E-1) and the within-phase ordering: spot-check →
select model → regression-gate the *selected* configuration (both lanes pinned) →
census. Running the regression gate before selection validates a configuration that
may then change, which §8 would require re-gating anyway. Finally, state the
run-independence conditions: each of the three runs is a fresh spawn (no shared
context, `memory:` prohibited per §3.9 — already designed); sampling seeds are not
controllable in this harness, so record instead session ID, timestamp, and the full
receipt triple per run, and state in the report that run-to-run variation reflects
default-temperature sampling. *Cost: one paragraph; saves a full re-run of the
gate.*

**D-6 — MEDIUM (§9 claim). Workflow resume does not replace the queue's
checkpoint/resume.** `resumeFromRunId` is "Same session only" (SDK reference), and
workflows.md: "If you exit Claude Code while a workflow is running, the next session
starts the workflow fresh." Since the script has no filesystem access, it cannot
consult queue.yaml to skip completed papers either — the invoking session must
compute the remaining set and pass it as `args`. *Recommendation:* keep queue.yaml
as the cross-session checkpoint (it already exists); correct §9's census-lane row to
"same-session resume via run-ID; cross-session resume via the queue, with the
invoking session enumerating the remaining papers". *Cost: two sentences + ~10 lines
in the runner.*

**D-7 — MEDIUM (model control). A per-invocation `model` parameter outranks the
frontmatter full-ID pin, and it is alias-only.** Resolution order (sub-agents.md):
env var → per-invocation parameter → frontmatter → session model. §3.3 guards only
the env var. An orchestrating session (or workflow stage routing) that passes
`model: "opus"` silently overrides the pin with a floating alias — and aliases move
when Anthropic releases a new model, which mid-census is precisely the §8
regression-gate trigger the design wants to catch *before* spend, not after.
*Recommendation:* (1) make the SubagentStop/schema receipt check a **hard gate** on
`model_id` — mismatch against the manifest pin blocks the item (the design says
model change is "detectable"; make it blocking); (2) for the validation matrix, do
not use per-call alias overrides — generate one agent variant per model with a
pinned full ID (three frontmatter files, or the `--agents` JSON flag which accepts
full IDs); (3) note in §3.3 that only definition-level `model:` accepts full IDs —
per-call overrides cannot pin. *Cost: one comparison in the existing hook + two
agent-variant files.*

**D-8 — MEDIUM (cost gate). `total_cost_usd` cannot instrument the cost gate on the
Max plan.** It is a client-side estimate from a bundled price table, explicitly "not
authoritative billing data", and subscription usage is not billed per token — the
binding constraint is the shared session/weekly usage windows (Phase 3.2).
*Recommendation:* re-specify the pre-scale cost gate to record, per probe paper:
token counts with cache splits (the §7.3 empirical check — unchanged), notional USD
(as a comparable index, labelled as such), and **plan-window consumption** (`/usage`
before/after), yielding weeks-to-census and a pace/credits/API decision point.
Appendix E4's "exact per-paper numbers for free" should read "exact token numbers;
notional cost; window consumption measured manually". *Cost: 15 min of wording + a
two-line measurement step in the probe.*

**D-9 — MEDIUM (corpus, pressure point d). Backup ordering leaves a single-copy
window that is fine for 17 papers and not fine for a census.** Items 1–4 are
census-blocking; item 7 (rsync to rpi-server + backups) trails. For the current 17
papers the exposure is low *if* migration copies rather than moves (open-access
items are re-fetchable from the manifest; manual items re-acquirable with effort).
But census acquisition will pour 100–200 manually acquired closed-access PDFs into a
store that nothing backs up. *Recommendation:* (1) migrate copy-then-verify —
originals deleted only after item 7 lands; (2) **promote item 7 to census-blocking**
(join items 1–4; it is 30 min); (3) verify `~/corpora/` actually falls inside an
existing backup scope on the machine that hosts it — "include the store in the
normal backup regime" is currently an assertion, not a configuration. *Cost: re-order
only; the work was already priced.*

**D-10 — LOW-MEDIUM (corpus). `meta.json` is schema-less and duplicates the
manifest — the D5 pathology in miniature.** The store holds per-paper `meta.json`;
the git manifest holds DOI, bibliographics, licence, source URLs, hashes, retrieval
dates. Two hand-maintained records of the same facts is the exact drift pattern the
routing design just engineered out of the instrument layer. Also, build order writes
`meta.json` *stubs* in item 1 but defines the manifest schema in item 2.
*Recommendation:* declare the manifest canonical and make `meta.json`
**machine-generated** by `fetch-corpus.py` (a per-paper projection of the manifest
plus store-local facts: file inventory, acquisition method, licence-evidence URL);
define both schemas in item 2 and write stubs after. *Cost: nil — ordering and a
decision, not new work.*

**D-11 — LOW (corpus). Fetch-script operational gaps.** No rate limiting,
retry/backoff, or `mailto`/User-Agent (Unpaywall requires an email parameter;
CrossRef polite pool expects `mailto`); the closed-item human-acquisition time
(~4–10 h, Phase 3.3) is unbudgeted; the ScienceDirect 403 needs its manual-path
statement in the item-3 spec, not just in pilot notes. *Recommendation:* add
politeness config (≤1 req/s, exponential backoff, `mailto`), a closed-items report
that estimates the manual queue, and see E-2 for the TDM route. *Cost: ~1 h inside
item 3.*

**D-12 — LOW (mechanism nuance). Transcript lag can race the SubagentStop hard
gate.** hooks.md warns transcripts are written asynchronously and may lag the
in-memory conversation. A SubagentStop hook parsing `agent_transcript_path` for
Read calls may miss the final turn's calls. *Recommendation:* the hook should retry
briefly on missing expected entries before blocking, and prefer
`last_assistant_message` for output parsing (already the documented pattern).
*Cost: five lines.*

### Enhancements

**E-1 — Use all five pilot papers in the reliability spot-check.** Preregistration
§8 says "at least three"; five exist. n rises 90→150 items, the false-pass rate at
true 0.85 halves (12%→5.5%), the paper-level effect gets five draws instead of
three, and the deterministic-zero padding dilutes. Cost: +6 invocations per model
(≈US$5–15 API-equivalent or the window fraction thereof). No amendment needed.

**E-2 — Elsevier TDM API for the closed fraction of the census.** Institutional
text-and-data-mining entitlement (api.elsevier.com, institutional token) can legally
automate closed-access full-text retrieval for a mostly-Elsevier corpus, replacing
most of the 4–10 h manual queue and the 403-workaround fragility. Action: one query
to the Macquarie University library about TDM entitlement before item 3 is built; if
available, add a TDM leg to `fetch-corpus.py`. Cost: ~1 h enquiry now, ~half day of
script if adopted; saves 4–10 h of Shawn's time and a fragile workaround.

**E-3 — Exploit the 1-hour subscription cache TTL with a stable prompt prefix in
the headless lane.** If the census runs as `claude -p --agent` main sessions (D-2's
fallback), the documented 1-hour TTL applies, and prompt caching is keyed on
identical prefixes: structure the invocation so agent definition + pushed
instruments form a byte-identical prefix and the paper content comes last, then
papers processed within the TTL window read the instrument tokens at ~0.1×. This
inverts §7.3's subagent cold-cache pessimism for the fallback engine — and the §7.3
empirical `cache_read_input_tokens` check (already mandated) will confirm or refute
it on the first probe at zero extra cost.

**E-4 — Add an accuracy gate against the pilot reference scores, not just a
stability gate.** Stability cannot catch a consistently-wrong scorer (recorded in
continuity, 2026-07-15, as known); the n=12 human subsample catches it only at
census time, after model selection. The five pilot papers carry standardised
reference FAIR scores (pilot findings report v1.2, Table 5) — comparing each model's
modal scores against them yields a concordance measure at zero additional scoring
cost, doubles as §8(b) comparability evidence, and gives D-5's selection rule its
second gate. Pre-specify the floor in the amendment (e.g. concordance ≥ 0.90 on the
same definition as the agreement statistic).

**E-5 — If workflows survive verification: use the headroom.** Concurrency to 16
(design assumes 4–6) subject to Max window pacing; archive OTel `workflow.run_id`
traces as the machine-readable run journal §9 promises but the docs do not otherwise
provide.

**E-6 — Record the promptfoo adopt/reject decision** (fidelity soft-drop 1) — if
rejected, one sentence in §7 prevents the next reviewer re-surveying it.

**E-7 — Archive non-selected model arms as robustness data.** The multi-model
spot-check produces 15 scored runs per model; the arms not selected for the census
are a free cross-model robustness annex for the paper (and evidence for the
FAIR-scoring-validation gap the preregistration cites as unfilled). One sentence in
the amendment makes them citable rather than drawer data.

**E-8 — One consolidated OSF amendment, lodged before the validation phase.**
Already owed (erratum entry 1 must precede census scoring). Fold in: the D-1
remediation ladder, D-5's agreement statistic + model-selection rule + pilot-paper
set + phase ordering, D-4's isolation rule, and E-4's concordance floor. One
amendment, one date, everything pre-specified before any gate runs — this converts
four would-be deviations into pre-specifications at the cost of a single lodgement.

### Study Designs and Preregistrations checklist (as applied at this juncture)

| Item | Status |
|---|---|
| Definitional circularity | None introduced by the three targets |
| Criterion contamination | **Flagged — D-4** (repo-resident answers readable by the scorer) |
| Treatment-invariant sample restrictions | Not touched at this juncture |
| Wording claims only what tests establish | **Flagged — D-5** (model "benchmarking" language vs no discriminating power; reword as gates-plus-cost selection) |
| Causal counterfactual | Unchanged (DiD arm; not in scope) |
| Everything analysis-relevant pre-specified | **Flagged — D-1, D-5** (ladder; agreement statistic; selection rule; paper set) |
| Blinding/ordering commitments | **Flagged — D-4, D-5** (isolation rule; select-then-gate ordering); assessment-before-reproduction otherwise preserved |
| Instrument reliability plan with thresholds and fallbacks | Present; ladder-vs-fallback tension resolved by D-1 |
| Power computed per test | Done here for the gate and the model comparison (Phase 3.1); model comparison reframed as ineligible for inference |
| Amendment policy stated; review before commitment boundary | Present; this review sits at the boundary; E-8 consolidates |

### Overall recommendation

**Low-effort improvements across the board; no significant redesign.** The routing
*policy* and the corpus *scope* stand. Before the Phase 1 build starts: lodge the
consolidated amendment (E-8, carrying D-1/D-4/D-5/E-4 — one to two hours of drafting
against text that already exists); run the §9 hook spike and name the headless
`--agent` fallback (D-2, ~1 h); move pre-flight to `PreToolUse[Agent]` (D-3);
promote corpus item 7 to census-blocking and declare `meta.json` generated (D-9,
D-10 — re-ordering only). Everything else folds into the build as specified. The
single highest-leverage cheap action is E-8: it converts every open compliance
question this review found into a pre-specification, dated before any gate runs.

### Priority order (effort vs risk retired)

1. E-8 amendment incl. D-1, D-4, D-5, E-4 (≈2 h drafting) — protects the
   registration's confirmatory character before any validation run.
2. D-2 spike + fallback naming (≈1 h) — settles the engine before agent authoring.
3. D-3 + D-7 + D-12 (≈1 h total) — correct hook events and hard-gate the model pin.
4. D-9 + D-10 re-ordering (nil) — before corpus item 1 executes.
5. E-1 + E-3 (nil to trivial) — free precision and probably-free cache economics.
6. D-6, D-8, D-11, E-2, E-5–E-7 — fold into Phase 1/corpus build as encountered.
