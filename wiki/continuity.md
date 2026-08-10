---
title: "llm-reproducibility — Continuity (Living Doc)"
tags: [infrastructure, coding-practices]
created: 2026-06-07
updated: 2026-08-10
status: active
---

# llm-reproducibility — Continuity (Living Doc)

**Purpose:** cross-session state, pending work, and a session-by-session log
for this repo. Updated in place at session end (no new file per session).

**Status: ACTIVE** (promoted from seed 2026-07-06). The four-artefact wiki
layout is fully in place (migration completed 2026-07-03, task B below):
continuity, working-notes, reflections/, user-observations, claude-observations,
and planning/ all live under `wiki/`; `docs/` stays at repo root as product
documentation (decided 2026-07-03). This file was created 2026-06-07 as the
migration seed, from a session working primarily in the
`2026-mq-llm-dh-judgement-paper-b` repo (the matching-grade PDF extractor
merged here as PR #1).

**How to update at session end** (per the canonical convention —
`~/personal-assistant/global-claude-md/handoff-protocol.md`):

1. Mark done items in place: `[ ]` → `[x] YYYY-MM-DD`; never delete.
2. Add new items as `[ ]` with a brief note.
3. Append a new "Session log" entry at the bottom (most recent first).
4. Carry forward open questions.

---

## Repo state (2026-08-10)

- **§2 ROUTING-FIX CARD DECLINED (Shawn, 2026-08-03/10) — INSTRUMENT
  CLARIFICATION ROUTE ADOPTED.** Receipts evidence killed the candidate's
  premise (sonnet pulled the guide 9/15; opus and fable 15/15 and failed
  both gates anyway; the guide is silent on the disputed cases). Route:
  erratum → OSF amendment 2 → re-benchmark. **Plan of record:
  `wiki/planning/instrument-clarification-plan.md`** (phases A–D, decision
  log, all rulings). Phase A COMPLETE except A3 (guide alignment, rides
  D1): A1 mining pass verified and reduced 68/150 disputed items to three
  root causes; A2 drafted as **erratum-log Entry 3 + "Queued amendment 2
  scope"** (ten items of operative text, PROPOSED — Shawn's ratification
  read pending).
- **ALL EIGHT DECISION POINTS RULED (Shawn, 2026-08-10):** research-surface
  rule (unit = artefacts required to reproduce, status scored, fault never;
  provenance as non-scoring per-input flag); two-rung evidence ladder with
  closed platform table; A1.2 open-case satisfied; R1.3 deposit-level
  standards only; R1.1 licence semantics (supplements default same-as-paper;
  repository licences checked at the service; conflicts → most restrictive);
  F-block gradient (F1 explicit-association; 4/4 vs 1/4 vs 0/4);
  unscoreable→0 only after the ladder. **Deterministic artefact-metadata
  harvester approved** (plan C6; extensible platform list — Dataverse/ADA/
  Figshare flagged); amendment 2 re-specifies §4 read-scope as paper +
  receipt-covered evidence pack. **Reference re-derivation (Phase B1) is
  now ENTAILED** — rulings flip identified reference scores (dye data
  R1.3, key A2, F-block items).
- **SCOUT/VERIFIER PIPELINE:** prior-art survey verified with material
  corrections — four fabricated quotations, ACM v1.1 claim INVERTED
  (origin-gated "Author-created artifacts…" → named deliberate departure);
  JIE badges survive as closest precedent. Cite only
  `wiki/planning/scout-reports/2026-08-10-fair-third-party-artefacts-prior-art-verified.md`.
  Countermeasure shipped: prior-art-scout must emit a claim per direct
  quotation (personal-assistant `a3f5793`). Eleven verified refs in Zotero
  staging `2026-08-10-fair-third-party-artefacts-prior-art`; Marwick 2017 +
  Tedersoo 2021 read directly (both support the ruling).
- **PENDING VERDICTS (no silent discard):** WN-l, WN-m (2026-08-03, still
  held); user-obs candidates A–C (2026-08-03) and A–C (2026-08-10) pending
  in `wiki/user-observations.md`; NEW working-notes candidates **WN-n**
  (audit surface must equal the reader's trust surface — claims ledger
  passed 65/68 while every fabricated quote sat outside the emitted set;
  Obs-16 shape, third sighting) and **WN-o** (test a one-shot resource's
  premise against primary artefacts before spending it — the receipts count
  reversed the session's opening plan), presented 2026-08-10.
- **PRE-CENSUS REQUIREMENTS UNCHANGED:** audit fix round 2 + schema v1.1
  (now also carries the provenance flag) + receipt-gate operative demo
  (`wiki/planning/audit-2026-08-03-follow-ups.md`); C7 GOVERNED decision
  still open; monitoring Phase 4 unstarted.

## Repo state (2026-08-03)

- **AMENDMENT 1 LODGED — TASK E COMPLETE.** Filed via the OSF API as
  registration Version 2 (revision `6a7017da97adb06288afef80`, DOI
  unchanged, tag `osf-amendment-1-2026-08-03`); lodgement text is the
  promoted academic-prose re-expression + a §5 cross-vendor
  pre-declaration (OpenAI arms considered, deferred to the FAIR4RS
  extension pattern). Details in the task-E block and the draft's status
  header.
- **MONITORING PHASES 0–3 SHIPPED** (plan §8/§10): 57-entity enumeration,
  `entity_checks` registry + E8 reference-dataset registration, per-class
  checker with undeclared-entity failure, coverage self-report line.
  §9 all resolved. Phase 4 (E7 hashes) remains.
- **BENCHMARK COMPLETE — ALL THREE ARMS BELOW BOTH 0.90 GATES.**
  Stability 0.807 (sonnet) / 0.873 (opus) / 0.813 (fable); concordance
  0.773 / 0.807 / 0.820. Item-structured disagreement shared across arms
  (A1.2, R1.1, A2, R1.3, F-block upstream crediting) = instrument
  evidence. Full package:
  `studies/open-science-compliance/outputs/validation/benchmark-2026-08/`
  (benchmark-summary.md + per-arm run-records with per-spawn tokens).
  **NEXT SESSION'S FIRST DECISION (Shawn, amendment §2): the single
  permitted routing-fix attempt** — candidate: push
  `fair-principles-guide.md` uniformly (receipts show inconsistent
  pulling) — then one re-run; else the registered majority-vote census
  (arm choice to be recorded explicitly). The workflow harness is rescued
  at `studies/open-science-compliance/protocol/validation/fair-benchmark-arm.workflow.js`.
- **AUDIT ROUND 2 OPEN.** Two-lens audit + fix pass `3b01676` (tests
  48→84, committed hook suite) + re-audit that found regressions in the
  fixes. Register: `wiki/planning/audit-2026-08-03-follow-ups.md` —
  fix round 2 and schema v1.1 are PRE-CENSUS requirements; C7 (instrument
  sha256) is a GOVERNED decision for Shawn. **Correction owed:** the
  2026-07-24 records claim "17 synthetic pipe-tests" for the hooks — those
  were ephemeral and never committed (audit C4); `tests/test_hooks.py`
  now exists. This note is the dated correction's anchor.
- **PENDING VERDICTS (no silent discard):** working-notes candidates WN-l,
  WN-m; user-obs candidates A–C (2026-08-03 batch); user-obs A–C from
  2026-07-27 — A and B ACCEPTED 2026-08-02/03, C discarded (systematised
  as handoff step 0).

## Repo state (2026-07-27, second session)

- **FOUR HELD-OVER VERDICTS CLEARED (2026-07-27, amd-tower, second session).**
  The block flagged below under "HELD OVER" is resolved:
  1. **WN-h/WN-i ACCEPTED** → `wiki/working-notes.md` Observations 16
     (structural instrument checks have a prose-shaped blind spot) and 17
     (independent reimplementation is a review technique). Both existed only as
     one-line summaries in this file; drafted against their sources (erratum-log
     Entry 2, and the `03f10ad`→`ceb1d79` commit range) before the verdict.
  2. **User-obs candidates A–C: HELD AGAIN.** Reviewed, not accepted, not
     discarded — annotated as such in `wiki/user-observations.md` so they read
     as triaged rather than untouched. Re-present at the next handoff.
  3. **Opus-5 benchmark arm CONFIRMED, plus a third arm authorised.** Shawn
     approved the deferred Fable 5 variant, discharging the 2026-07-22
     "ask-before-Fable" condition. Benchmark arms are now **Sonnet 5 + Opus 5 +
     Fable 5**.
  4. **Amendment §3 provenance paragraph: read at lodgement**, per the
     2026-07-24 one-read decision. Text unchanged
     (`amendment-1-draft.md:113–125`); the pre-lodgement checklist governs.
- **FABLE 5 ARM BUILT.** `.claude/agents/fair-assessor-fable-5.md` generated
  *from* the Opus 5 file rather than hand-transcribed, then diffed: the three
  variants differ only in name, description, model pin, role heading, sibling
  sentence, and `agent_version` — the "only the model pin differs" claim is now
  verified, not asserted. (Hand-transcription had silently introduced a
  `sub-principle`→`sub principle` defect; the diff caught it.) Registered in
  `manifest.yaml` with sha256; the sibling-sentence edit changed the Sonnet 5
  and Opus 5 hashes too, all three updated in the same commit. **32 tests green,
  live gate PASS (0 errors, 0 warnings)** — and because the D5 gate enforces the
  agent registry in both directions, that PASS is positive evidence the new file
  is registered and correctly hashed.
- **Fable 5 caveats recorded in the manifest comment, neither blocking
  authorship:** $10/$50 per MTok (2× Opus 5, 3.3× Sonnet 5 standard), and it
  requires 30-day data retention — unavailable under zero data retention, which
  surfaces as a 400 on *every* call rather than as a capability difference.
  **The benchmark run itself is still ungated:** authoring a definition is not
  an API call, so the run needs explicit approval with a billing route decided.
  Three arms × 5 pilot papers × 3 runs = 45 scoring spawns.
- **CORPUS ITEMS 5 AND 6 DONE — the corpus plan's build list is now closed.**
  Both were already *specified* in `corpus/README.md`; only the implementations
  were missing.
  - **Item 5 (`bd5bc40`, on main):** reproduction preparation prompt v1.0→v1.1.
    New §1.0 (hash at fetch time — reconstructing at session end makes the
    retrieval dates guesses) and §1.0.1 (three destinations: corpus store for
    publisher content and never git; attempt directory for author-released
    materials; scratch for what nothing references). `log-template.md` gains a
    **Materials Acquired** table. Verification and handoff gained matching
    checks.
  - **Item 6 (PR #2, branch `feat/schema-v2.7-source-provenance`):** schema
    v2.7 adding optional `source_file` + `source_sha256`. Branched not pushed,
    per the standing schema-change rule. Additivity verified mechanically (no
    v2.6 property or top-level key dropped; `required` unchanged), not asserted.
    **v2.6 retained and the pilots deliberately not back-filled** — the field
    records what a run actually read, so retro-fitting a digest would make it
    lie in its first use. Out of scope and flagged in the PR:
    `docs/user-guide/schema-reference.md` and `docs/README.md` still say v2.6
    (prose rewrite; belongs with task D).
- **FINDING — the D5 gate's version check covers 7 of 25 registered entries.**
  Found by probing this session's own change: setting the reproduction
  preparation prompt's manifest version to a deliberately wrong `9.9` still
  produced `PASS`. Cause is scope, not a bug — `check_canonical_entry`
  (`scripts/check-manifest-consistency.py:180`) runs **only** over
  `shared_content`, so `components.*`, `assessment.prompts.*`,
  `reproduction.prompts.*` and the rest are unchecked. Same shape as
  Observation 16: a gate reporting PASS over a narrower scope than a reader
  assumes — and this file described D5 as "verifies version lines" without the
  qualifier. A sweep of all 25 registered `file`+`version` entries found:
  8 matching, 6 cosmetic `v1.0`-vs-`1.0` prefix differences, 8 with no
  `**Version:**` line (the six agent definitions use frontmatter and are
  hash-checked instead — stronger, not weaker), and 1 apparent mismatch that
  **turned out not to be one** (see below).
  **Shawn's decision 2026-08-02: WIDEN — every registered entity is to be
  checked hard.** A reorganisation to support that is acceptable. Plan drafted
  at `wiki/planning/artefact-integrity-monitoring-plan.md`; not implemented.

- **CORRECTED 2026-08-02 — the `assessment_json` "mismatch" was mine, not the
  repo's.** On 2026-07-27 this was logged as a genuine conflict needing a
  verdict on which number was right. It is not: `1.1` and `2.1` measure
  different things, and both are correct. `**Version:** 2.1` is the *document*
  version of `assessment-schema.md` (2.0→2.1 at `05e9706`, 2025-11-29; never
  1.x). `schema_version: "1.1"` is the *payload* version stamped into each
  `assessment.json` (1.0→1.1 at `faef450`, 2026-02-12). The manifest entry
  tracks the payload axis while its `file:` points at the guide documenting it.
  The naive sweep compared the two axes and reported a conflict that does not
  exist; a note in `manifest.yaml` now says so, so the next reader does not
  "reconcile" them into one number.
- **STALE COMMIT HASHES — a history rewrite orphaned pre-rewrite references.**
  The real defect behind the above. `c3654f6` does not resolve; nor do the two
  hashes logged beside it. All three were re-identified by exact
  commit-message match (`e1e4cba`→`aa75817`, `c3654f6`→`faef450`,
  `c026756`→`be7271a`, all 2026-02-12, contents unchanged). Fixed in
  `manifest.yaml` and `wiki/reflections/session-log.md` (with an inline note
  recording the remap rather than silently swapping).
  **Scale, measured 2026-08-02:** of backticked commit-shaped references across
  `wiki/`, `manifest.yaml`, `studies/`, and `corpus/`, **115 resolve and 21 do
  not**; all 21 sit in `wiki/` (continuity, session-log, reflections,
  working-notes). Three are now fixed; **18 remain** and each needs
  message-match re-identification. Deliberately not batch-fixed here — the
  remap must be verified per commit, not guessed. A resolve-check is a
  candidate control in the monitoring plan.

## Repo state (2026-07-27)

- **D5 GATE HARDENED (2026-07-27, amd-tower; `03f10ad`→`ceb1d79`).** A third
  session, resuming from the 2026-07-24 handoff, independently reimplemented D5
  before discovering the zbook build had already landed (7 commits pulled
  mid-session). Rather than discard either, the two were compared; the second
  implementation caught two gaps in the first, both now ported in and tested:
  - **Byte-exact mirror regions.** The structural check (fenced blocks + table
    rows) cannot see prose. **The Pass 6 prompt's "verbatim mirror" banner was
    untrue** — four normative statements from prereg §7.1 were missing
    (unscoreable→0; never aggregated; the A1 majority rule; FAIR4RS out of
    scope) while every block and row matched, so the gate reported PASS.
    Marker pairs now delimit the region and it is compared byte for byte.
    **Erratum-log Entry 2**; impact checked against persisted pilot outputs —
    no pilot score revised (all /15, none unscored, none aggregated,
    key-et-al-2024 shows the A1 rule operating).
  - **Reverse sweep.** An unregistered `.md` dropped into the instruments
    directory passed the old gate. Every file in
    `shared_content_policy.scan_directories` must now be registered.
  - Mirrors that cannot be one contiguous region declare
    `mirror_mode: structural` and warn every run that prose divergence is
    undetected — the weaker guarantee is announced, not assumed.
  - Tests 17→28. Amendment 1 draft updated (§1 gains Entry 2; §3 gains the
    model-identifier provenance limit — pinned IDs are the provider's exact
    complete strings with no dated snapshot available, so an ID names a model
    as served at call time, not a frozen weight set).
- **SECOND MIRROR CONVERGED (2026-07-27, Shawn's call).**
  `verdicts-and-precision` → reproduction-assessor `SKILL.md` is now byte-exact
  in six **named segments** (`#verdicts`, `#precision`, `#tolerances`,
  `#discrepancy`, `#scope`, `#environment`) — the check gained segment support
  so a mirror can land in several places in a document without giving up
  byte-exactness. Convergence replaced reworded restatements with canon's
  wording and added two things the skill never carried: the PAPER_ERROR
  human-escalation sentence and environment-spec levels 0–5 (new SKILL.md
  section H). **No erratum, no amendment** — SKILL.md is not in the frozen
  artefact set, the discrepancy vocabulary is not registered text, and
  converging a mirror changes delivery not instrument semantics; ordinary §8
  implementation change riding the Phase 1 regression gate. Reasoning recorded
  in erratum-log Entry 2 under "related finding". `mirror_mode: structural`
  survives as the declared-weaker fallback; nothing uses it.
- **FORWARD MODEL PINS → OPUS 5 (2026-07-27, Shawn's call).** Every pin that
  was `claude-opus-4-8` is now `claude-opus-5`: `fair-assessor-opus-4-8.md`
  renamed to `fair-assessor-opus-5.md`, plus reproduction-planner,
  reproduction-executor, adversarial-reviewer. Same price ($5/$25 per MTok),
  higher capability, no reason to prefer 4.8 for new work. **History is not
  rewritten** — no scored artefact ever ran on 4.8 (existing extractions record
  `claude-opus-4-5`/`claude-sonnet-4-5` and keep those), and the dated decision
  records in the session log and reflections stand as written; the manifest
  comment records 2026-07-22 → 2026-07-24 → superseded-2026-07-27 as a chain.
  The validation benchmark's Opus arm is now Opus 5. Selection still happens at
  the validation phase under the amendment's gates-plus-cost rule.
- **Session close (2026-07-27):** `/reflect` written — session-reflection Entry
  10, llm-observations (independent reimplementation as a review technique),
  abductive entry (the sync check that could not fail, reflog-anchored),
  session log, claude-obs 25–28. Secret-safety fix outside this repo:
  `~/personal-assistant/.env.bak-2026-07-27` held live API keys and was not
  gitignored (`.env` was covered, `.env.*` was not) — broadened, committed,
  pushed.
- **HELD OVER — needs Shawn's verdict (no silent discard):** [x] 2026-07-27
  ALL FOUR CLEARED — see the second-session block above. Two working-notes
  candidates drafted at this handoff, **WN-h** (structural instrument checks
  have a systematic blind spot: fenced blocks and table rows pass while
  normative prose diverges — measured on the live Pass 6 mirror) and **WN-i**
  (independent reimplementation as a review technique: two readings of one
  specification map where the spec was silent; the delta was two real gaps).
  Plus **user-obs candidates A–C for 2026-07-27** in `wiki/user-observations.md`
  (pending review). Also still open from earlier: the Opus-5 benchmark-arm
  change and the amendment's provenance paragraph, both flagged in-session but
  not explicitly signed off.
- **Process fix for concurrent sessions — IMPLEMENTED.** The collision cost a
  full duplicate build. Root cause: `git status` and
  `git rev-list origin/main...HEAD` read the *local* `origin/main` ref and never
  contact the remote, so without a `git fetch` they report "in sync" from a
  stale pointer — indistinguishable from real sync. The harness's session-start
  snapshot does not fetch either. Reflog confirms this repo's `origin/main`
  pointer had not moved since 2026-07-24 14:16 until a fetch at 2026-07-27
  11:25, while the zbook commits landed 14:29–20:01 on 24 July. Fix: fetch-first
  is now the opening instruction in this repo's `CLAUDE.md`, and the `/handoff`
  resume-prompt template opens with `git fetch && git status -sb`
  (`~/personal-assistant/global-claude-md/handoff-protocol.md` step 6).

## Repo state (2026-07-24)

- **PHASE 1 BUILD QUEUE EXECUTED (2026-07-24, second session; commits
  `b1aab17`→`115d202`):** the four-item queue from the bullet below is DONE.
  (1) **D5 gate live:** `scripts/check-manifest-consistency.py` wired into
  pre-commit (block-tested) — verifies version lines, end-of-file receipt
  tokens, mirror normative blocks (fenced code + table rows byte-identical),
  push/pull consumer routing evidence, agent-definition hashes (§3.4),
  model pins (§3.3, no `inherit`), and the `memory:` prohibition (§3.9);
  17 unit tests in `tests/test_manifest_consistency.py`. (2) **Instrument
  canon complete — 7 `shared_content` entries:** FAIR instrument + five new
  canonical files (data-availability-taxonomy, verdicts-and-precision incl.
  env levels 0–5, coverage-rules, eligibility-criteria,
  `.claude/shared/invariants.md`) + adversarial-review-framework promoted
  pull→push and registered (v1.1, governed header + token); reproduction
  SKILL.md registered as a second machine-checked mirror (verdict/tolerance/
  scope tables). (3) **Five agent definitions** with pinned models:
  fair-assessor ×2 per-model variants (`claude-sonnet-5`, `claude-opus-4-8`
  — NB Sonnet 5/Opus 4.8 expose NO dated snapshot IDs; the aliases ARE the
  exact IDs, never append dates); reproduction-planner/executor/
  adversarial-reviewer provisionally `claude-opus-4-8` pending the
  validation-phase benchmark (pin changes are governed manifest edits).
  `agent_definitions` hash registry added to the manifest. (4) **Production
  hooks live** (probe archived to `archive/phase1-spike/`): manifest-driven
  SubagentStart push + sha256/version receipt log; SubagentStop receipt gate
  (version echo, token quote, model_id hard gate, transcript-verified full
  pulled reads, D-12 retry-then-fail-closed, ESCALATE passthrough,
  decision:block self-healing); PreToolUse[Agent|Task] pre-flight denying
  governed spawns on D5 failure / missing instruments /
  `CLAUDE_CODE_SUBAGENT_MODEL`; 17 synthetic pipe-tests green. **Consolidated
  OSF amendment DRAFTED** from the ratified scope:
  `studies/open-science-compliance/prereg/amendment-1-draft.md` (lodge just
  before the validation phase; pre-lodgement checklist inside; erratum log
  cross-references it). **NEXT (Phase 1 remainder):** census screener
  (deterministic script + instrument-like triage prompt, design §5); output
  schemas for the structured-output layer + census/validation workflow
  scripts (§9); corpus items 5–6; then amendment lodgement → validation
  phase.
- **PHASE 1 OPENED (2026-07-24):** D-2 hook spike **PASSED** on all four
  datapoints (two haiku probes: hooks fire for workflow spawns; injected
  context arrives; transcript path delivered; named `agentType` reaches
  matchers) — **engine = workflows CONFIRMED**; build rule: workflow
  `agent()` calls always pass `agentType`; headless `--agent` fan-out stays
  as documented fallback. FAIR instrument v2.0 extracted to its canonical
  file (`studies/open-science-compliance/protocol/instruments/fair-instrument.md`,
  receipt token `3ddcbfd82575a2f8`; Pass 6 prompt keeps a banner-marked
  verbatim mirror); `manifest.yaml` `shared_content` registry started
  (`25d1c0d`). Probe hook neutered to log-only scaffolding. **Elsevier TDM
  trail:** three diagnostic 403s (entitlement → key-provisioning →
  TDM-checkbox-insufficient; full chain in corpus plan decision 5); support
  email drafted but deprioritised on Brian's field intelligence — **Zotero +
  institutional proxy is the probable acquisition route** (Shawn
  investigating); key still to add on amd-tower. **BUILD QUEUE NEXT:** D5
  manifest-consistency script (pre-commit + pre-flight) → remaining
  instrument files (taxonomy L1–L6, verdicts+precision, coverage rules,
  eligibility, `.claude/shared/invariants.md`) → five agent definitions with
  pinned full model IDs → production push/receipt hooks +
  `PreToolUse[Agent]` pre-flight → corpus items 5–6.
- **ROUTING DESIGN SIGNED OFF (Shawn, 2026-07-24, at v0.2.2)** — Phase 1
  design gate CLEARED. Amendment scope RATIFIED same day; lodgement timing:
  defer to the hard stop (just before the validation phase), accumulating any
  further errata into one amendment.
- **CORPUS MANAGEMENT EXECUTED (2026-07-24) — census blockers DONE:** store
  live at `~/corpora/llm-reproducibility/` (16 papers, 28 files, 71.7 MB, all
  sha256-verified; originals retained, copy-then-verify); manifests written
  (`corpus/development-manifest.yaml` 11 papers;
  `studies/open-science-compliance/corpus/manifest.yaml` 5 pilots);
  `scripts/fetch-corpus.py` operational (verify 28/28 OK; gen-meta done);
  LFS narrowed to own-artefact scopes; pre-commit corpus gate installed +
  block-tested (override: `CORPUS_GATE_OVERRIDE=1`); first QNAP sync complete
  via `scripts/sync-corpus.sh` (44 files both sides; NO automated schedule —
  run after each acquisition session). Remaining corpus items 5–6 ride
  Phase 1. **Elsevier TDM:** Shawn requested an API key 2026-07-24; storage
  convention `ELSEVIER_API_KEY_TDM` in `~/personal-assistant/.env`;
  entitlement test (closed JAS article from campus) pending — see corpus plan
  decision 5 for the nuances. ~~NEXT: Phase 1 build, opening with the D-2
  hook spike~~ [x] 2026-07-24 spike RUN and PASSED — see the Phase 1 bullet
  at the top of this list.
- **Pre-build juncture /review-implementation COMPLETE (2026-07-24, Shawn's
  request):** fresh-context review of design v0.2.1 + corpus scope v0.2 +
  validation-phase plan. Verdict: proceed, four cheap fixes first. 12 defects
  (1 critical compliance: the §2.2 remediation ladder was a deviation from
  prereg §8's registered majority-vote consequence — must be pre-specified by
  amendment BEFORE the validation phase) + 8 enhancements. Fidelity audit of
  v0.2 vs the 2026-07-22 findings: clean. Report externalised to
  `wiki/planning/reviews/2026-07-24-pre-build-juncture-review.md`. ALL cheap
  fixes APPLIED same day: design → v0.2.2 (§2.2 compliant ladder; §9
  conditional-on-spike with headless `--agent` fallback named; pre-flight →
  `PreToolUse[Agent]`; model-alias layer hard-gated; D-12 transcript-lag
  retry; cost gate re-specified for Max-plan window consumption); corpus plan
  → v0.2.1 (item 7 backup PROMOTED to census-blocking; copy-then-verify;
  `meta.json` machine-generated; fetch politeness; Elsevier TDM enquiry =
  ACTION Shawn); erratum-log gains a **Queued amendment scope** section
  (ladder, unanimity statistic, all-five-pilots, gates-plus-cost model
  selection with E-4 concordance floor, read-scope isolation, robustness
  annex) — PROPOSED, pending Shawn's ratification; consolidated amendment must
  lodge before the validation phase. D-2 hook spike = Phase 1 opening hour.
- **Routing design v0.2 WRITTEN (2026-07-23, `3914f81`) — superseded by
  v0.2.2 above; still awaiting Shawn's
  review/sign-off** (he is reading it; the four judgement calls to check: hook
  injection as primary push; §2.2 remediation ladder; instrument extraction
  deferred to build; memory prohibition + hot-reload governance). Phase 1 build
  blocked on this sign-off.
- **Corpus-management implementation SCOPED (2026-07-23):** repo audit, build
  order (8 items, ≈1 day, items 1–4 census-blocking), target structure, and
  decision log now in `wiki/planning/corpus-management-plan.md` v0.2. Decision
  status: path mechanism AGREED; out-of-tree store and study-scoped manifests
  recommended (registration-integrity argument: purges rewrite history and
  would invalidate the hashes the OSF registration pins) — awaiting Shawn's
  confirmation; execution ON HOLD until the routing-design review lands.
- **Routing-design review passes COMPLETE + externalised (2026-07-22):**
  implementation review at
  `wiki/planning/reviews/2026-07-22-routing-design-implementation-review.md`
  (10 defects D1–D10, 8 enhancements E1–E8; headline: build push/receipt/
  pre-flight on native harness primitives — SubagentStart/SubagentStop hooks,
  `skills:` preload, `--json-schema` — not hand-rolled plumbing; pin model IDs);
  prior-art scout, adversarially verified 110/110 claims clean, at
  `wiki/planning/scout-reports/2026-07-22-routing-design-prior-art-verified.md`
  (headline: subagent cold-cache caveat + open issue anthropics/claude-code#29966
  — census cost gate must NOT assume prompt-cache discount without an empirical
  `cache_read_input_tokens` check). Design v0.2 fold-in is the next design task.
- **Pass 6 instrument defects FIXED (2026-07-22, `abdc526`):** stale /16
  example, legacy 5-level access taxonomy (renamed Tier 0–4 + demarcation
  note vs prereg L1–L6), dead schema pointer — all three were in the
  OSF-frozen copy at `ee3fda3`. **Erratum log started** (Shawn approved
  erratum-then-amendment path):
  `studies/open-science-compliance/prereg/erratum-log.md` — amendment must
  lodge before census scoring; instrument-file extraction (review D1) queued
  for Phase 1 build.
- **Sequence BLESSED (Shawn, 2026-07-22):** Pass 6 fix → routing design v0.2
  + sign-off → corpus-management implementation → Phase 1 agentic build →
  ONE combined validation phase (regression gate ≥2 pilots incl. Crema
  posterior-table leg + FAIR reliability spot-check 3 papers × 3 runs) →
  census. The previously planned standalone "weekend run" is superseded —
  both checks now ride the post-build validation phase, run once on the
  pipeline + model(s) that will score the census.
- **Model-testing decisions (Shawn, 2026-07-22):** step-5 spot-check
  benchmarks ALL THREE Claude models. Sonnet 5 + Opus 4.8 first, on the
  Claude Max subscription; **ASK before running Fable 5** (may go via API
  instead — Max coverage unclear). Shawn also wants an OpenAI **Sol** arm
  (GPT-5.6 Sol, released ~Jul 2026:
  <https://openai.com/index/previewing-gpt-5-6-sol/>; "capable but not
  Fable-level") — possibly a Fable-driving-Sol combination; design discussion
  deferred; cross-provider arm needs its own harness and an OSF amendment if
  adopted for the census (registration documents Claude as the instrument).
  API-call approval gate applies to every run as usual.
- `main` current through 2026-07-15 @ `885e664` (history rewritten 2026-07-13 —
  pre-purge hashes are stale). Earlier landmarks: plan v0.3 review,
  Cosmos form capture + proposal draft v0.2, article-text untracking, and the
  scout-report series). Project v3.0.1.
- **Scout sweep COMPLETE (2026-07-08), all follow-ups executed:** whole-stack
  positioning (12 verified reports + synthesis), arXiv blind-spot sweeps (S1/S2),
  approved deeper chaining (C1–C3), and the OSF/grey-literature guard pass (G1)
  all live in `wiki/planning/scout-reports/` (start at the synthesis; README
  indexes everything). Headlines: no direct competitor to any lane, but the
  middle is converging (Chakravorti 2026; Zhu 2026 pair) — speed-to-publish now
  matters; the zero-archaeology null is DOCUMENTED (G1, 26-query log) so
  first-mover claims must be scoped + "to our knowledge" with Spennemann 2023
  demarcated; Zotero staging holds all verified finds (P1–P6, S1–S2, chains).
  lit-scout + verifier agents patched (author-count rule; arXiv handling).
- **Cosmos application: SUBMITTED 2026-07-21** 🎉 (deadline 26 Jul; rolling
  review, decision ~1 month — watch for Cosmos correspondence mid-August).
  Submitted content = `cosmos-application-form-paste.txt` at `de30d7c`: title
  "Making Verification of Published Research Routine"; merged one-liner;
  498-word we-voice body; parity-length Brian entry; US$8,000; evidence pack
  live at `docs/cosmos-evidence-pack.md`; both CVs attached (Ross letterhead
  phone corrected + re-uploaded); field 20 = Lukianoff Substack. Draft
  history below. Proposal draft v0.4 (2026-07-21, academic-prose pass)
  in `wiki/planning/cosmos-application-draft.md` — body 499/500 aligned with the
  lodged registration (already-preregistered + osf.io/dqnhg, control series,
  pilot error-detection, window 2022–2026); field 19 extended (human-validation
  link, agent-relay audit line, delivery-and-follow-on paragraph: Claude/Codex
  skills + self-hostable runner with Brian Ballsun-Stanton, FAIR4RS, CC0 data
  outputs, follow-on API-cost driver); field 18 Brian entry (v0.5: CV-verified
  — Lecturer, Faculty of Arts, MQ; research-integrity award; both CVs read
  from ~/Downloads/, kept out of repo); applicant affiliation resolved
  (Honorary Professor MQ primary + EFN director secondary); team-pedigree
  line (preregistration chapter + JCAA FAIRer-data paper); candidates
  drafted for title/one-liner/self-pitch/amount (worked US$8,000) with
  CV-verified credential fragments. **v0.6 (2026-07-21): clean-context
  adversarial verification run + reconciled with the PA-hub session's ledger**
  — all submission-facing claims confirmed (499/500 recounted; 2,118 scout
  ledger records so "over 1,800" conservative); three ledger pointer errors
  fixed (Obs 4 not 6; pilot §1/§7; Florida chapter in Brian's CV only);
  field 19 wording corrected (registrant hand-scoring, ReplicatorBench/I4R
  scoping, DataCite + Spennemann demarcation, web-search-layer, CC0
  demarcated from registration); self-pitch recomposed to Shawn's
  done-things steer; **final paste set drafted for every form field (1–21)**.
  Body revised by Shawn 2026-07-21 (long-tail reframing, combined-approaches
  problem, JAS: Reports named, survey clause) and jointly tightened to v0.7 at
  499/500 — voice now "we" (Brian named collaborator; supersedes the
  first-person-singular verdict; field 6 self-pitch stays "I"), truth-seeking
  token restored, computational-subset wording protected. Remaining: field
  selections, profile links, field 20, phone check, submit. ~~Pre-submission
  gates~~ [x] 2026-07-21 BOTH CLEARED: embargo lifted by Shawn (journal
  check had cleared JAS / JAS:R / JCAA — none requires double-blind);
  registration verified public via anonymous API, DOI 10.17605/OSF.IO/DQNHG
  (recorded in draft, paste blocks, prereg README). Deadline 26 Jul 2026.
  (v0.3 was `7435865`, body 482/500.)
- **OSF preregistration DRAFTED + STRESS-TESTED (2026-07-14/15):**
  `studies/open-science-compliance/protocol/phase-2-preregistration-draft.md`
  v0.2 (`885e664`; v0.1 `9405182`). Open-ended registration format; honours all
  three drafting-care constraints (instrument fixed, regression-gated pipeline
  changes, no-new-corpus-contact). /review-implementation revisions: H2
  de-circularised (verification-target coverage endpoint, exact
  Jonckheere–Terpstra primary, fractional-logit secondary), H1 restricted to
  quantitative papers (post-treatment conditioning argument) with
  trend-adjusted secondary, **JAS: Reports DiD control arm (Shawn approved
  2026-07-14** — FAIR lane; reproduction = exploratory stretch; AER absence
  grounded in Marwick 2025, re-verify guidelines pre-launch), H4 reworded to
  match its test, assessment-before-reproduction blinding, 0.90 stability
  threshold, human-validation subsample (n=12), power table. **v0.7
  LODGEMENT-READY at `ee3fda3` (2026-07-18)** — all resolutions applied plus
  four review-batch revisions (see the 2026-07-18 session log entry);
  lodgement materials in `studies/open-science-compliance/prereg/` (plain
  summary, two glyph-verified PDFs, README with recipe + checklist).
  **LODGED 2026-07-20: <https://osf.io/dqnhg/>** — by hand from the project
  flow (standalone Registries flow caps form attachments at five files; the
  project flow froze all six artefacts from OSF Storage); embargoed at
  lodgement (Shawn 2026-07-21: deliberate deviation from the no-embargo
  plan — double-blind peer-review contingency; the lodgement tag's
  annotation still says "no embargo", predating the correction).
  **Embargo LIFTED 2026-07-21** (journal check cleared JAS / JAS:R / JCAA:
  none requires double-blind; JAS:R dropped its double-blind mandate
  between mid-2024 and 2026-07-21). **Registration PUBLIC, verified by
  anonymous API 2026-07-21; DOI 10.17605/OSF.IO/DQNHG.**
  Tag `osf-prereg-phase2-2026-07-20`;
  paste files unwrapped to flowing lines (OSF text boxes render line-breaks
  literally). Known cosmetic defect: §10 power table pasted as run-together
  pipe text — accepted, fix rides with any future amendment (tables rule
  now in prereg README + convention memory). Option A ordering satisfied:
  new-corpus FAIR scoring is unblocked. Live URL linked from the Cosmos draft (body now reads "already
  preregistered", census window corrected 2023→2022, 484/500 words).
- **Current gates:** the §9 verdicts are DELIVERED (2026-07-15/16), so the
  Phase 1 hold on the agentic modernisation plan
  (`wiki/planning/agentic-modernisation-plan.md`, v0.3) is now gated only on
  (a) review of the content-routing design (below) and (b) the
  corpus-management-plan implementation (pre-Phase-1 prerequisite). ~~OSF
  preregistration must precede FAIR scoring of any new JAS papers (Option A
  ordering constraint, plan §6).~~ [x] 2026-07-20 SATISFIED — registration
  lodged (<https://osf.io/dqnhg/>).
- **Agent content-routing design v0.1 WRITTEN (2026-07-15, `10947aa`):**
  `wiki/planning/agent-content-routing-design.md` — resolves plan §9 item 3
  with a three-way routing rule (embed role behaviour / push instruments
  verbatim with read receipts / pull pattern libraries; silent-vs-loud
  failure as the routing criterion). Read receipts decided by Shawn
  (reliability-first, duplication acceptable if cleanly split;
  no-agent-to-agent-duplication rule; shared_content registry folds into
  manifest.yaml). Queued: `/review-implementation` + prior-art-scout passes
  against it (Shawn wants both) → v0.2 before Phase 1 build.
- **Framework paper QUEUED (2026-07-13):** plan externalised to
  `wiki/planning/long-tail-credibility-framework-paper.md` (v0.1) — a
  state-of-play/agenda paper staking out long-tail research credibility
  assessment with AI, built on the verified scout sweeps. Prioritisation
  deferred until Shawn finishes his current paper (week of 2026-07-13); open
  question is authorship model (solo lit-review-and-state-of-play — his
  current lean — vs consortium via COS/CWTS Leiden/RDA contacts).
- **Deferred watch list (from chain reports C1/C3):** re-check forward citers
  of Chakravorti et al. 2026 (10.48550/arXiv.2605.27394) and the
  ReplicatorBench cluster around Sep–Oct 2026; Cheng & Khoo 2025
  (10.31083/ko44513) and Bolanos-Burgos et al. 2026 (10.7717/peerj-cs.3921)
  around Oct 2026–Jan 2027. Sources: c1/c3 reports' deeper-chaining sections.
- **Working notes WRITTEN (2026-07-13):** Obs 5 (prompt-injection sightings)
  and Obs 6 (verifier catch taxonomy) in `wiki/working-notes.md` (`f51737b`).
  The gap Obs 5 flagged — no standing anti-injection rule in the scout agent
  definitions — was closed the same day (personal-assistant `b31342b`,
  injection-defence rule added to all four scout agents' Constraints).
- ~~**§9 verdicts: Shawn has committed (2026-07-13)** to delivering the six
  judgement-call verdicts~~ [x] 2026-07-15/16 ALL DELIVERED: items 1–2 =
  prereg Decision 7 (reliability checks + 0.90 threshold, confirmed); item 3
  = content-routing design (sign-off pending the review passes); items 4–5
  accepted (R-A+R-B merge; drift clause as encoded in prereg §8); item 6
  realised by the prereg draft itself.
- **HISTORY PURGE COMPLETE (2026-07-13, pushed by Shawn; remote verified
  clean):** git filter-repo removed the dye-et-al-2023 supplement.pdf (both
  historical paths) and marwick-2025.txt from all 242 commits; local
  untracked copies intact; full pre-purge backup (mirror, LFS objects, plain
  files, commit-map) at
  `~/Code/repo-backups/llm-reproducibility-pre-purge-20260713/`.
  Residual notes: (1) commit hashes cited in wiki/docs before 2026-07-13 are
  stale — translate via the backed-up commit-map or search by commit
  subject; (2) GitHub's server-side LFS storage may retain the unreferenced
  supplement object — full scrub needs a GitHub Support ticket or repo
  delete/recreate (low urgency: nothing references it); (3) other local
  clones must be re-cloned or hard-reset. The CC BY SocArXiv preprint of
  Marwick 2025 is at
  `studies/open-science-compliance/corpus/pdfs/marwick-2025-socarxiv-preprint.pdf`
  (gitignored dir) for future licence-clean extraction.
- **Corpus management redesign AGREED (2026-07-13), implementation queued:**
  `wiki/planning/corpus-management-plan.md` — out-of-tree corpus store, DOI
  manifest + fetch-with-checksum script (Shawn endorsed fetch-with-checksum
  as the reproduction-run default), LFS/pre-commit guardrails, rpi-server
  sync. Sequenced as a PRE-PHASE-1 prerequisite in the agentic modernisation
  plan; must land before the JAS census acquires papers at scale.
- **OA check RESOLVED (2026-07-13):** six of eight
  papers are CC BY 4.0 — no purge needed (ballsun-stanton-et-al-2018,
  penske-et-al-2023, sobotkova-et-al-2016 [OA book], sobotkova-et-al-2024
  [Emerald page confirms CC BY despite Unpaywall "bronze"], crema-et-al-2024,
  key-et-al-2024). ~~PENDING~~ [x] 2026-07-13 both actions COMPLETED (see
  HISTORY PURGE COMPLETE above); original scoping notes retained: (1) `git filter-repo` purge of
  dye-et-al-2023's `reproduction/attempt-01/supplement.pdf` — publisher
  (Elsevier) supplement to a green-only article, no open licence; NOTE it
  was tracked via Git LFS, so the purge must remove the LFS object as well
  as the pointer; history rewrite of the public repo awaits Shawn's go.
  (2) `marwick-2025.txt` near-certainly from the closed VoR: the on-disk
  source PDF (studies/open-science-compliance/corpus/pdfs/marwick-2025.pdf)
  IS the Elsevier JAS version of record (first-page check 2026-07-13) and no
  preprint PDF is present — joins the purge list pending Shawn's one-word
  confirmation. LOCAL COPIES CONFIRMED before any purge (Shawn's
  requirement, 2026-07-13): dye supplement intact on disk (820,582 bytes,
  real PDF, not an LFS pointer) and marwick text + VoR PDF both on disk.
  Purge scoping: the dye supplement exists at TWO historical paths
  (pre-reorg `outputs/dye-et-al-2023/...` and the current `studies/...`
  path) — filter by basename/blob, not one path — and the LFS object must
  be removed too. History audit of all ever-tracked PDFs found one other
  publisher PDF (Sobotkova et al. 2023, old `sources/PDF/` path) — checked:
  Applied Geography, 10.1016/j.apgeog.2023.102967, hybrid OA, CC BY →
  CLEAR, no purge. The corpus PDFs and `input/sources/original-pdf/` were
  never tracked; all currently tracked PDFs are the project's own artefacts
  (reproduction figures; a draft proposal). Side-fix applied:
  key-et-al-2024's DOI in the corpus queue corrected to the resolving
  2023-prefix form (recorded 2024-prefix form 404s; verified at CrossRef).
- **Identity confabulation CORRECTED (2026-07-14, `38adf36`):** CITATION.cff,
  codemeta.json, CONTRIBUTING.md, and the pilot findings report had carried
  "Shawn Graham" / Carleton University / github.com/shawngraham since their
  2025-11-13 creation. Now Shawn Ross / Macquarie University /
  github.com/saross, ORCID 0000-0002-6492-9025 (verified against author lines
  in Shawn's published papers). archive/ and verbatim extracted texts left
  untouched (the sobotkova-et-al-2016 mention is the real Shawn Graham).
- **Machine sync COMPLETE (2026-07-15):** amd-tower ready for resume. Old
  pre-purge clone quarantined (NOT deleted) at
  `~/Code/repo-backups/llm-reproducibility-pre-purge-clone-20260715` on
  amd-tower — never pull/push from it (pre-purge history; also holds on-disk
  copies of the purged files, consistent with keep-local-copies). Fresh clone
  at `~/Code/llm-reproducibility`: purged paths absent from history (verified
  0 hits), pre-commit hooks installed, 30 gitignored corpus/text assets
  rsynced from zbook with all checksums verified (incl. dye supplement
  820,582 bytes; marwick CC BY preprint). Gotchas: amd-tower remote is now
  **HTTPS + gh credentials** (its GitHub SSH key needs an interactive agent;
  `git remote set-url origin git@github.com:saross/llm-reproducibility.git`
  to switch back); venv not recreated (`python -m venv venv &&
  venv/bin/pip install -r requirements.txt` when scripts are needed);
  `.claude/settings.local.json` deliberately not copied (machine-local).
- **Immediate priority (displaces the above):** draft the Cosmos Institute
  grant application (deadline 26 Jul 2026); framing in
  `wiki/planning/cosmos-grant-application-framing.md`.
- Stale-carry-forward note for future resumes: the 2026-07-06 handoff
  verdicts were already applied in `a1e52de` — do not re-solicit them.

### Earlier state (2026-06-07)

- `main` @ `1c4650e` (merge of PR #1). Working tree clean.
- **PR #1** added a matching-grade extraction layer to
  `extraction-system/scripts/pdf_processing/`: `normalise_for_matching`,
  `normalise_text_readable`, `PDFExtractor.extract_pages` (per-page text with
  page-index + section locators), and promoted cleaners (`strip_running_headers`,
  `drop_fragment_headings`, `split_body_references`, `strip_affiliation_tail`,
  `looks_like_heading`). First tests in the repo at
  `extraction-system/scripts/pdf_processing/tests/test_matching_layer.py`
  (24/24 pass). Additive/opt-in: existing `extract()` behaviour unchanged.
  Built for an annotated-bibliography (AB+) pipeline in the paper-b project;
  design context in that repo's
  `planning/pdf-extractor-consolidation-plan-2026-06-07.md`.

## Pending tasks

### E. AMENDMENT LODGEMENT — three tasks, then the validation phase unblocks  [x] 2026-08-03

**This is the critical path.** The consolidated OSF amendment must lodge
*before* the validation phase runs (hard stop, registrant's 2026-07-24 timing
call). Three items stand between here and the OSF form; the checklist itself
lives at the foot of
`studies/open-science-compliance/prereg/amendment-1-draft.md`.

- [x] **E1. Fold the third benchmark arm into §3.** 2026-08-02 — **Shawn:
      add the Fable arm** (option (a), name all three identifiers). Done: §3's
      provenance paragraph now pins `claude-sonnet-5`, `claude-opus-5`,
      `claude-fable-5`. Two further edits followed from it, both pre-declaring
      rather than reconstructing:
      - §3's selection rule now states that the three arms are strictly
        ordered by published price, so **the Fable arm cannot be selected for
        the census under any spot-check outcome** — it is run to test whether a
        more capable model clears the same reliability gates (evidence about
        the instrument, not the model) and to supply §5 robustness data. A
        pricing-change clause applies the rule to prices in force at selection.
      - §5 now says the annex explicitly covers an arm excluded from selection
        by construction.
      **Billing route settled the same day:** Max-plan Fable allocation first
      (if that route is feasible for subagent spawns), with a configured
      Anthropic API billing account for direct calls or excess-of-plan usage.
      No per-arm approval outstanding — the run is governed by the ordinary
      standing API review gate, presented once before it runs.
- [x] **E2. §1 word-for-word consistency check — done 2026-08-02.**
      Checked against canonical `fair-instrument.md`, the Pass 6 prompt mirror
      (byte-identical to canon, 5,123 bytes, re-diffed), prereg §7.1, the
      frozen copy at `ee3fda3`, and the persisted pilot outputs. Record in
      `amendment-1-draft.md` (final section): 7 deliberate differences
      recorded; 3 flags raised and **adjudicated same day** — (1) quotation
      placement FIXED (parenthetical moved outside the quotes, Shawn's
      verdict); (2) en dash inside quotes ACCEPTED as typography; (3) the
      "four of five persisted FAIR assessments" scope flag DISSOLVED: a fifth
      persisted assessment exists (crema run-02, key `infrastructure` not
      `reproducibility_infrastructure`, one level below the `outputs/*/`
      glob — the two reasons erratum Entry 2's sweep and this check's first
      pass both missed it). Verified: 12/15 + 12/15 matching Table 5, none
      unscored, no aggregate, A1 present. §1's sentence stands as written for
      all five pilots. Run-01 was archived not lost (`c41242b`). **Candidate
      follow-ups, Shawn's call:** dated correction note on erratum Entry 2's
      "the four papers carrying FAIR assessments" scoping; working-notes obs
      candidate (Observation-16 shape again — a sweep scoped narrower than
      its readers assume, this time by glob depth + key name).
- [x] **E3. Build the paste artefact — done 2026-08-03.**
      `prereg/osf-amendment-1.txt`, generated mechanically from the promoted
      amendment text and unwrapped via `unwrap-paste-file.py`. Docstring
      verification passed: word count unchanged by unwrap (1,263 → 1,263),
      numbered lines 5 → 5 (the section headings), 0 bullets, 0 table rows,
      no markdown residue; token comparison against the canonical section
      identical (68 numeric, 4 quoted, 10 § refs).
      **Context for E4 (2026-08-03 decisions):** the lodgement text is the
      promoted academic-prose re-expression (registrant read both versions;
      skill-test record archived at `archive/prereg/`); rule-4 check re-run
      against it, PASS (13 frozen phrases verbatim, addendum in the draft's
      record section). §5 gained a two-sentence cross-vendor pre-declaration:
      **OpenAI arms (Sol/Terra/Luna) considered and deferred** to a possible
      post-census extension via dated amendment plus the §8 reliability
      protocol — not folded into this registration's validation phase
      (confound: cross-vendor arms cannot hold the delivery apparatus
      constant, so they compare model+harness bundles, not models).
- [x] **E4. LODGED 2026-08-03 — route changed to API filing on Shawn's
      decision.** Not by-hand paste: filed as an OSF versioned registration
      update (SchemaResponse revision `6a7017da97adb06288afef80`) after an
      Opus-agent sweep of the developer docs, a staged in-progress draft
      verified byte-identical on round-trip (39,725 chars; original 30,907
      untouched), and Shawn's placement decision (append at end — the
      summary field is the landing content). Submit + approve in one
      sitting. **DOI unchanged by design**; amendment version URL
      <https://osf.io/dqnhg?revisionId=6a7017da97adb06288afef80>; tag
      `osf-amendment-1-2026-08-03`. Reading done at promotion.
      **TASK E COMPLETE — the validation phase is unblocked.** Same-day
      follow-through (2026-08-03): **PR #2 MERGED** (`58c3fe7`) as the one
      change — schema v2.7 + eight-prompt cascade + project.version 3.0.1 →
      3.1; Pass 6 edits outside the mirror region, classified an ordinary
      §8 implementation change (no erratum, no amendment; classification
      presented, standing land decision applied). **Monitoring §9 all
      RESOLVED** (Shawn: wiki not registered; E7 warn-first; one verified
      remap pass early Phase 4; crema register-without-rewrite) and
      **Phase 0 COMPLETE** — 55 entities enumerated and classified, plan
      §10; per-entry re-check found no true drift, four
      missing-version-carrier flags for Phase 1. Phase 0 gate passed and
      **Phase 1 COMPLETE same day** (Shawn's go, 2026-08-03): central
      `entity_checks:` map (56 declarations) + `reference_datasets:` E8
      registration (five pilot FAIR assessments, crema's key declared
      as-is) + two version carriers added (workflow.md, credibility JSON
      schema). Two Phase 0 flags dissolved — the skills and the
      credibility template already carried versions under labels the
      Phase 0 regex missed; carriers declared instead of added. Gate
      PASS, 32/32. **Phase 2 COMPLETE same day** (`e2b6568`): the gate now reads
      `entity_checks` — per-class verification E3-E8, undeclared-entity
      and unresolvable-declaration failures, declared normalisation.
      Tests 32 → 46 (one injected defect per class). Closure probe: the
      2026-08-02 probe (9.9 on the preparation prompt) that then
      produced PASS now FAILS with a named error. **Next gate:
      Phase 3** (coverage self-report line + pre-flight wiring). Remaining
      after that: the three-arm benchmark run (still gated on the
      standing API review presentation: model, batch vs real-time, 45
      spawns, estimated cost). Flag from the docs sweep, low priority: the
      original registration text's two escaped comparators ("post &gt; pre
      on all measures", "pinned &lt; unpinned") may render as literal
      entity strings on the public page; eyeball, and if wrong it is
      erratum-log material for a future revision, not a ride-along edit.

### A. Git hygiene — untrack the committed virtualenv  [x] 2026-07-03

> Done 2026-07-03 exactly as prescribed below: 2,114 index deletions, files kept
> on disk; post-check `git ls-files | grep -c '^venv/'` = 0; stray-bytecode sweep
> outside venv = 0 tracked files.

The repo tracks the **entire `venv/`** — **2,114 files** (verified 2026-06-07:
`git ls-files | grep -c '^venv/'`), including thousands of `.pyc`. `.gitignore`
**already** lists `venv/`, `__pycache__/`, and `*.py[cod]` (lines ~5–10), so
these were force-added or pre-date the ignore (tracked files are not
auto-ignored).

Fix (own commit/PR — large, mechanical):

```bash
git rm -r --cached venv
git commit -m "chore: untrack committed virtualenv (already in .gitignore)"
```

Caveats:

- ~2,114 deletions from the index (files stay on disk). Do it standalone.
- Anyone relying on the committed venv must recreate it:
  `python -m venv venv && venv/bin/pip install -r requirements.txt` — note this
  in the commit body and/or README.
- After: `git ls-files | grep -c '^venv/'` should be `0`.
- Also sweep any other tracked bytecode outside venv:
  `git ls-files | grep -E '__pycache__|\.pyc$' | grep -v '^venv/'` (should be
  empty — PR #1 already removed the one stray
  `extraction-system/scripts/pdf_processing/__pycache__/pdf_cleaner.cpython-312.pyc`).

### B. Migrate docs to the wiki-style layout  [x] 2026-07-03

> Done 2026-07-03. `docs/notes/working-notes.md` → `wiki/working-notes.md`;
> `docs/notes/reflections/` → `wiki/reflections/`; repo-root `planning/` →
> `wiki/planning/` (all via `git mv`); created `wiki/index.md`,
> `wiki/user-observations.md`, `wiki/claude-observations.md`; wiki frontmatter
> merged into migrated pages (additive — `/reflect`'s priority/scope/audience
> keys preserved); reference sweep across all living docs (archive/ and frozen
> reproduction artefacts deliberately untouched); CLAUDE.md continuity pointer
> added; README gained a docs-vs-wiki disambiguation map. **docs/ disposition
> decided (Shawn, 2026-07-03): stays at repo root** — product documentation
> follows the GitHub/JOSS convention (Pages builds from /docs); only the
> process layer moved to wiki/.

This repo uses the **legacy `docs/notes/` layout** and lacks `continuity.md`
(this seed) and `user-observations.md`. Target = the canonical per-project
wiki layout (authoritative reference: `~/personal-assistant/wiki/index.md`,
"PA project layer" table; migration precedent:
`~/personal-assistant/wiki/planning/wiki-index-draft.md`).

| Artefact | Target | Source now |
|---|---|---|
| `continuity.md` | `wiki/continuity.md` | **this file (seed, in place)** |
| `index.md` | `wiki/index.md` | new (small index; model on PA's) |
| `working-notes.md` | `wiki/working-notes.md` | `docs/notes/working-notes.md` |
| `reflections/` | `wiki/reflections/` | `docs/notes/reflections/*` (session-log, session-reflection, abductive-reasoning, llm-observations) |
| `user-observations.md` | `wiki/user-observations.md` | new (model on paper-b's `docs/notes/user-observations.md`) |
| `planning/` | `wiki/planning/` | repo-root `planning/` |
| Documentation | decide: keep `docs/` vs `wiki/docs/` | repo-root `docs/` |

Steps:

1. `git mv` legacy files into `wiki/` (preserve history).
2. Create `wiki/index.md` + `wiki/user-observations.md` from the convention.
3. Add wiki frontmatter (`title`/`tags`/`created`/`updated`/`status`) to
   migrated pages; tags from the 24-term vocabulary in PA's `wiki/index.md`.
4. Add a "Session continuity → `wiki/continuity.md`" pointer to this repo's
   `CLAUDE.md` (belt-and-braces; the global session-start protocol already
   reads `wiki/continuity.md`).
5. Resolve the `docs/` disposition (see open decision).

Caveats:

- `docs/` here is large and public-facing (assessment guides, background
  research, FAIR docs) — unlike PA's, it may warrant staying at repo root
  rather than moving under `wiki/docs/`. Decide deliberately.
- `/reflect`, `/observe`, `/handoff` are layout-aware and fall back to legacy
  paths; after migration they target `wiki/`.

### C. Fix lossy de-hyphenation of genuine compounds  [x] 2026-07-06

> Done 2026-07-06, following the fix direction below with one refinement: the
> dictionary check takes precedence over the affix list (if the joined form is
> a known closed-form word, join — so `multi-\nple` → `multiple` even though
> `multi-` is a compound prefix; otherwise a compound prefix keeps its hyphen —
> `self-\ncorrection` → `self-correction`). Dictionary = frozen subset of
> wamerican 2020.12.07-2 shipped at
> `extraction-system/scripts/pdf_processing/affix-joined-words.txt` (9,810
> affix-prefixed words) so canonical matching keys stay machine-independent.
> Chained breaks handled (dict check sees the flattened fragment:
> `multi-\nfa-\nceted` → `multifaceted`). Idempotence preserved; golden tests
> green; 8 regression tests added incl. the Huang self-correction case
> (32/32 pass). Residual ambiguity documented in the `_dehyphenate` docstring:
> a deliberate hyphen broken at exactly that hyphen resolves to the closed
> form when that form is a dictionary word; non-prefix compounds
> (`decision-\nmaking`) keep the historical joining behaviour.

`_dehyphenate` (`extraction-system/scripts/pdf_processing/pdf_cleaner.py:348-361`,
regex `re.sub(r"(?:-\s*\n\s*)+([a-z])", r"\1", text)`) joins any end-of-line
hyphen followed by a **lowercase** letter and **drops the hyphen
unconditionally**. This is correct for line-break artefacts
(`archaeo-\nlogy` → `archaeology`) but **lossy for genuinely-hyphenated
compounds broken before a lowercase letter** — e.g. `self-\ncorrection` →
`selfcorrection` (hyphen lost). The existing guard only protects compounds
broken before a **capital** (`well-\nKnown` stays). Feeds **both**
`normalise_for_matching` and `normalise_text_readable`.

Concrete case (re-verifiable): Huang et al. 2023 (Zotero attachment
`K294C8KD`), `page_index 3`, "...after self-\ncorrection, the accuracies..." →
the matching key contains `selfcorrection`, so a naturally-written quote
("after self-correction, ...") **fails** the deterministic quote-checker even
though the content is present. Discovered 2026-06-10 during the paper-b AB+
co-design (`planning/section2-grounding/ab-plus/huang2023large.md`, "Extraction /
fidelity notes").

Impact: a quote spanning a line-broken hyphenated compound silently fails the
checker; paper-b currently works around it (quote from text-as-extracted +
display-cleanup) but the canonical key itself is wrong here.

Fix direction (heuristic — full de-hyphenation is ambiguous): keep the hyphen
when the prefix is a known hyphenating affix (`self-`, `multi-`, `non-`, `pre-`,
`co-`, `anti-`, `inter-`, `intra-`, `well-`, `re-`, `e-`, …) or when **both**
fragments are independently valid words (wordlist check); drop it otherwise.
Must preserve `_dehyphenate`'s **idempotence** (the readable + matching
normalisers depend on it) and keep golden tests green; add a regression test
for the `self-correction` case. Additive/worktree discipline.

### D. Consolidate version-history sources  [ ]

Version history is now maintained by hand in four places (`manifest.yaml`
`version_history` — nominally canonical; `CHANGELOG.md`; README "Development
History"; `docs/research-assessor-guide/version.md`). The 2026-07-06 session
updated three of them in parallel to say the same thing. Candidate fix: derive
the CHANGELOG and README sections from the manifest (script or documented
cascade checklist, mirroring the assessment-schema compliance pattern from
February). Low priority; logged from llm-observations 2026-07-06.

## Open decisions

- [x] 2026-07-03 `docs/` disposition: **stays at repo root** (decided with the
  conventions rationale recorded in task B note above and README's docs-vs-wiki map).
- [x] 2026-07-03 Sequencing: done as separate commits (A on 2026-07-03 standalone;
  B as its own migration commit).

## Session log

### 2026-08-03 (second) / 2026-08-10 — §2 declined, research-surface rulings, A2 drafted

One session, two sittings a week apart (52a81f4b; renamed
"LLM-Repro-2026-08-06"); twelve commits `b686b6f`→`8521d50` + handoff, plus
personal-assistant `a3f5793`. The §2 card was declined on receipts evidence
gathered before presenting; Shawn chose the instrument-clarification route
(robust instrument over speed-to-census) and, across two sittings, ruled
all eight benchmark-derived decision points — anchored by his
research-surface reframing of the assessment target. Prior-art scout +
adversarial verifier ran the evidence leg (four fabricated quotations
caught; ACM inverted claim converted to a named departure; agent-definition
countermeasure shipped); Marwick and Tedersoo read directly; eleven
verified references staged in Zotero. Phase A closed bar A3: mining pass
verified all published benchmark figures from primary artefacts, and A2's
ten items of drafted operative text sit in erratum-log Entry 3 awaiting
ratification. Full factual log: `wiki/reflections/session-log.md`
2026-08-03/10 entry; plan of record:
`wiki/planning/instrument-clarification-plan.md`.

**NEXT (in order):** (1) Shawn's ratification read of erratum Entry 3's
drafted text; (2) Phase C build — audit fix round 2, schema v1.1 (+
provenance flag), C6 harvester, C7 GOVERNED decision; (3) A3 + D1
consolidation → lodge amendment 2 → re-benchmark; (4) Phase B reference
re-derivation design (entailed, needs Shawn's shape decision).

**Carry-forward:** zbook still needs `./scripts/install-git-hooks.sh` after
pull. Shawn: Fable Max-vs-API billing split check still open; Zotero-proxy;
`ELSEVIER_API_KEY_TDM` still absent; **Cosmos decision window now open**
(~1 month from 2026-07-21 submission). New this session: lit-scout may want
the same quotation-claim rule (deferred pending evidence); COPE case URL
unverifiable by automation (browser-check before ever citing); Marwick 2017
now has duplicate Zotero items (573 + 4151, merge when convenient);
`published/agents/prior-art-scout.md` drift picked up at next `/retro`.
Pending verdicts: see the 2026-08-10 repo-state block.

### 2026-08-03 — Lodgement, monitoring 0–3, benchmark, two audit rounds

One very long session (0360402e); ~28 commits `a208f9d`→`9f67480` + tag
`osf-amendment-1-2026-08-03` + reflections/handoff. Task E closed:
E2 re-check, crema "missing assessment" dissolved (pre-v2.6 key), prose
re-expression promoted, §5 cross-vendor pre-declaration added, lodged via
the OSF API as registration Version 2 (DOI unchanged). PR #2 + cascade
merged; monitoring §9 resolved and Phases 0–3 shipped same day. Benchmark
ran per amendment §3 (45 spawns, 4.25M tokens, ≈$27): all arms below both
gates, item-structured — the §2 remediation decision is deliberately
parked for next session. Two audit rounds: fix pass 3b01676 (tests
48→84), re-audit found regressions in the fixes; everything registered in
audit-2026-08-03-follow-ups.md. Full factual log:
`wiki/reflections/session-log.md` 2026-08-03.

**NEXT (in order):** (1) Shawn's §2 decision (routing-fix candidate:
uniform push of fair-principles-guide) → possible single re-run via the
rescued workflow script; (2) audit fix round 2 + schema v1.1 — both
PRE-CENSUS; before the census the gate needs one captured SubagentStop
event and one live pass-plus-catch demonstration; (3) C7 GOVERNED
decision; (4) monitoring Phase 4; (5) census frame.

**Carry-forward:** zbook must run `./scripts/install-git-hooks.sh` after
pulling. Shawn: check Fable Max-allocation vs API billing split after this
session's ~1.4M Fable tokens; Zotero-proxy investigation;
`ELSEVIER_API_TDM` key still absent; Cosmos watch ~mid-August. Pending
verdicts listed in the 2026-08-03 repo-state block.

### 2026-07-27 (second session) / 2026-08-02 — Verdicts cleared, corpus list closed, monitoring planned

Two sittings on amd-tower off the 2026-07-27 resume prompt; seven commits
(`640ffbb`→`8a4e946`) plus PR #2 opened and deliberately held. **Sitting one:**
all four held-over verdicts cleared — WN-h/WN-i accepted as working-notes
Observations 16–17 (drafted against sources first, since only one-line summaries
existed), user-obs A–C held again, Opus-5 arm confirmed and a Fable 5 arm
authorised, provenance paragraph deferred to the lodgement read. Fable 5 agent
definition *generated from* the Opus 5 file and diffed rather than transcribed —
which caught a `sub-principle`→`sub principle` defect the hand-written attempt
had introduced. Corpus items 5 (fetch-with-checksum, destinations, Materials
Acquired table) and 6 (schema v2.7, PR #2) closed the corpus build list.
**Sitting two:** walked a returning collaborator through two findings and
corrected one of them; fixed the orphaned commit hashes; drafted the monitoring
plan; named the Fable arm in amendment §3, closing task E1.

**Findings.** The D5 gate's version check covers **7 of 25** registered entries
(`check_canonical_entry` iterates `shared_content` only) — found by probing this
session's own change with a deliberately wrong version. Backticked commit
references: **115 resolve, 21 do not**, all 21 in `wiki/`; 3 remapped by exact
message match, 18 outstanding.

**Correction.** The `assessment_json` "genuine mismatch" escalated on 2026-07-27
was a measurement error, not repo drift — `1.1` (payload `schema_version`) and
`2.1` (document version) are different axes, both correct. Withdrawn 2026-08-02
with evidence; a manifest note now prevents the next reader "reconciling" them.

**Decisions (Shawn, 2026-08-02):** widen the gate so every registered entity is
checked hard, reorganisation acceptable; add the Fable arm to the lodged
amendment text; billing route settled (Max-plan first, API account for excess,
ordinary API review gate before the run); PR #2 held until after lodgement.

**NEXT:** task E — E2 (§1 consistency check) and E3 (paste artefact) are
Claude's; E3 follows Shawn's read, not precedes it. Then PR #2 plus the prompt
cascade as one change; then monitoring Phase 0.

**Carry-forward:** user-obs candidates A–C (2026-07-27) **still held and
un-adjudicated** — carried a second time. Of the 2026-08-02 batch, F accepted,
D and E discarded (Shawn, 2026-08-02). Working-notes candidates WN-j/WN-k
**accepted** as Observations 18 and 19. zbook must run
`./scripts/install-git-hooks.sh` after pulling. Shawn: Zotero-proxy investigation; `ELSEVIER_API_KEY_TDM` still absent
from `~/personal-assistant/.env`; Cosmos watch ~mid-August.

### 2026-07-24 (second session) — Phase 1 build queue executed; amendment drafted

Single autonomous session off the resume prompt. Four build-queue items + the
amendment draft, five commits (`b1aab17` D5 gate → `18cb659` instrument canon
→ `de175d3` agent definitions → `115d202` production hooks → amendment/
continuity commit): D5 consistency gate (pre-commit-wired, block-tested,
17 unit tests incl. §3.3 model-pin and §3.9 memory-prohibition checks);
instrument canon to 7 registered entries (five new canonical files + the
adversarial framework promoted pull→push; reproduction SKILL.md became a
second machine-checked mirror); five agent definitions with pinned models
(claude-api reference confirmed Sonnet 5/Opus 4.8 have no dated snapshot IDs
— the aliases are the exact IDs; reproduction-lane pins provisional
`claude-opus-4-8` pending the validation benchmark); production hooks
(manifest-driven push + receipt log, receipt gate with model_id hard gate and
transcript-verified pulled reads, PreToolUse pre-flight; 17 synthetic
pipe-tests). OSF amendment 1 drafted at
`prereg/amendment-1-draft.md` from the ratified scope — lodgement deferred to
just before the validation phase per Shawn's timing call. One mid-session
rebase over a parallel session's handoff commits (the 2026-07-22/24 entry
below landed while this session ran).

**NEXT:** Phase 1 remainder per the repo-state bullet — census screener,
output schemas + workflow scripts, corpus items 5–6; amendment lodgement then
validation phase.

**Decision pass (Shawn, 2026-07-24, same session, all seven queued decisions
resolved):** (1) reproduction-lane model pins stay provisional (Opus 5
expected imminently; real selection at the validation phase — rationale
recorded in the manifest comment); (2) fair-assessor Fable 5 variant deferred
— authored only when Shawn approves the Fable benchmark run (billing route
decided then); (3) amendment-1 draft gets one read, at lodgement; (4) all
three build judgement calls RATIFIED (env-levels co-location, invariants to
all three reproduction agents, SKILL.md mirror); (5) WN-a–g ALL ACCEPTED →
working-notes Observations 9–15; (6) user-obs candidates A–C ALL ACCEPTED —
C makes confidence labels on external-system predictions a bilateral
standing rule; (7) MQ TDM enquiry DROPPED (rely on Zotero-proxy route +
Elsevier support-email fallback). Parallel session confirmed finished, no
conflict.

**Carry-forward (pruned):** Shawn: Zotero-proxy investigation, amd-tower
`.env` key; Cosmos watch ~mid-August; PA data-submodule unpushed inbox
commit (PA session to sweep); zbook: re-run `./scripts/install-git-hooks.sh`
after pulling (hook now includes the D5 manifest gate).

### 2026-07-22/24 — Review cascade; corpus infrastructure; Phase 1 opens

Three-day amd-tower session (remote-controlled from campus days 2–3; four
zbook paper-b commits rebased over mid-session). **Day 1:** routing-design
review passes run + adversarially verified (110/110 clean); Pass 6 instrument
defects found in the OSF-frozen copy and fixed (`abdc526`); erratum log
started (`f4dfa0e`, Shawn-approved accumulate-then-amend path); reports
externalised (`c9a6ecd`); model-testing decisions recorded (three-model
spot-check; Sonnet 5 + Opus 4.8 on Max first; ask-before-Fable;
Sol arm later). **Day 2:** design v0.2 (`3914f81`); corpus implementation
scoped (`edf7f56`); zbook synced. **Day 3:** §9 workflows added (v0.2.1,
`74e7ed9`, from Shawn's review question); pre-build juncture
/review-implementation (his request) found 12 defects incl. one critical
compliance catch (§2.2 ladder = prereg deviation) — all cheap fixes applied
(v0.2.2 + corpus v0.2.1 + ratified amendment scope queued in erratum log,
`3080022`); **Shawn SIGNED OFF v0.2.2 and confirmed corpus decisions**
(`01fd8d4`); corpus census blockers EXECUTED (`fbf477c`: store 16 papers /
71.7 MB verified, manifests, fetch-corpus.py, LFS narrowed, corpus gate
tested, first QNAP sync); **Phase 1 opened** — D-2 spike PASSED, engine =
workflows, FAIR instrument extracted to canon (`25d1c0d`); Elsevier trail
diagnosed to unresolved key-provisioning failure, Zotero-proxy now the
probable route (`c903b89`…`5b77b78`); migration script archived (`cb7a24c`).
Reflections + claude-obs 19–21 written at close.

**NEXT:** (1) build queue per the Phase 1 bullet (D5 consistency script
first); (2) draft the consolidated OSF amendment from the ratified scope
(lodge just before the validation phase — Shawn's timing call); (3) Shawn:
Zotero-proxy investigation, amd-tower `.env` key, MQ TDM enquiry optional;
(4) Cosmos correspondence watch ~mid-August.

~~**Held over pending Shawn's verdicts (no silent discard):**~~ [x] 2026-07-24
ALL RESOLVED in the second session's decision pass: WN-a–g all ACCEPTED
(now working-notes Observations 9–15); user-obs candidates A–C all ACCEPTED
(C → bilateral confidence-label rule). Original hold-over text: working-notes
candidates WN-a/b (2026-07-18) + WN-c/d/e (2026-07-21) — still owed — plus
NEW this session: WN-f (docs-vs-harness canary-probe method: settings-hook
canary + control/test spawns settled in 20 s what three doc citations
mispredicted) and WN-g (reliability-gate statistics: n=90 gives ~12%
false-pass at true 0.85, halved by all-five pilots; agreement definition
shifts the 0.90 gate across 10–30% item-flip rates; model ranking
structurally unavailable pre-census). User-obs candidates for 2026-07-24
written to `wiki/user-observations.md` (pending review).

### 2026-07-20/21 — Prereg LODGED on OSF; Cosmos application SUBMITTED

amd-tower session, two days. Preregistration lodged by hand (browser extension
unavailable; Claude supplied verified paste artefacts): project-flow lodgement
dodged the standalone form's five-file cap; paste files unwrapped to flowing
lines (`f2f467a`) after OSF text boxes rendered breaks literally; §10 power
table pasted as pipe soup — accepted, tables now banned from paste-field
content (`6577119`, README + convention memory). Lodged WITH embargo
(double-blind contingency); journal-policy agent found no candidate venue
requires it (JAS:R dropped its mid-2024 mandate); embargo lifted, registration
public, **DOI 10.17605/OSF.IO/DQNHG** (`13261c1`). Cosmos application then
driven v0.4→v0.7: registration alignment, CV-verified credentials, two-pass
claim verification (PA-hub ledger `ef8a6cb` reconciled against a clean-context
adversarial agent — three ledger pointer errors and six wording drifts fixed),
Shawn's body revision tightened 566→498 in we-voice, all fields selected
(statement-of-mission title; merged one-liner; two-sentence self-pitch and
parity-length Brian entry, preregistration claims deflated to "argued the case
for"). Live form differed from the 2026-07-07 capture (links-only
additional-info field; multi-file CV upload) → evidence pack published at
`docs/cosmos-evidence-pack.md`; paste file + committed generator
(`build-cosmos-form-paste.py`) keep form text and verified draft in lockstep.
**SUBMITTED 2026-07-21** (`f9c14b0`), US$8,000, five days ahead of deadline.
Reflections + claude-obs 15–18 written (`f7450dc`).

**NEXT:** (1) weekend run: FAIR reliability spot-check + pilot regression gate
(pilot papers only; prereg-safe); (2) routing-design review passes
(/review-implementation + prior-art-scout) → v0.2; (3) corpus-management
implementation before census; (4) watch for Cosmos correspondence ~mid-August;
(5) census sweep once gates pass.

**Held over pending Shawn's verdicts (no silent discard):** working-notes
candidates WN-a/WN-b (2026-07-18: xelatex glyph-drop hazard; emphasis-stripping
fixpoint) plus NEW WN-c/d/e (2026-07-21: paste-surface conventions;
external-fact half-life — the JAS:R policy drift; verification ledgers drift
from sources) — WN verdicts still owed. ~~user-obs candidates 1–8~~ [x]
2026-07-22 ALL RESOLVED: 1–5 and 7 accepted (7 elevated to a standing
default: interface-shaped paste artefacts for any web-form output; riders on
1 and 2: critical-friend pushback on domain judgements stays welcome; hold
ground when pushback is off-base), 6 and 8 discarded.

### 2026-07-18 — Prereg v0.3→v0.7 lodgement-ready; OSF materials; authorship posture

Shawn returned (Paper B finished on the train) and final-reviewed the prereg
through four revision batches; everything committed and pushed; lodgement is
the morning of 2026-07-19. Version chain (all 2026-07-18):

- **v0.3** — nine decision-point resolutions applied (D3 → 168 h on named
  hardware + archived-intermediates partial path; others as drafted).
- **v0.4** — census window start → 2022-01-01 (two full pre-policy years;
  H1b parallel trends partially checkable; power table recomputed, δ ≈ 0.28
  at 80/80); H5 + credibility lane reclassified pre-specified exploratory;
  *Reports* control census option via cost gate.
- **v0.5** — credibility outputs constrained to descriptive structural
  metrics; availability taxonomy → six friction-ordered levels (machine
  boundary L2/L3, discretion boundary L3/L4; "on request" split from
  archive registration; standardised L4 request protocol); sampling-cap gate
  clause; pre-specified descriptive reporting block; R-only limitation
  sharpened (Marwick-adjacent oversampling caveat).
- **v0.6** — H5 gains two schema-verified RDMAP metrics (implicit-status
  proportion; expected-information gaps); L4 window → 3 weeks + late-response
  clause; credibility signals computable internally with aggregate-only
  reporting (per-paper scores never published); FAIR4RS named as
  amendment-path extension; FAIR×coverage estimation added; human-validation
  wording fixed (one instrument, data + code applications).
- **v0.7 + pilot report v1.2** — LLM removed from authorship per
  journal/university policy: report has sole human author + §10 LLM-use
  statement (v1.0–v1.1 correction recorded in-document); CITATION.cff and
  codemeta author fields cleaned (tooling disclosure retained in
  runtimePlatform/softwareRequirements); git Co-Authored-By trailers stay
  (Shawn confirmed — VCS provenance, not scholarly authorship).

Lodgement materials (`studies/open-science-compliance/prereg/`, convention
transferred from `~/Code/inscriptions/wiki/prereg/`): plain-prose summary
(4,347 words, emphasis stripped to fixpoint), glyph-verified PDFs of prereg +
pilot report (DejaVu fonts — Latin Modern silently dropped α/δ/≤; verified by
pdftotext), README with regeneration recipe + lodgement checklist. Study
protocol and Pass 6 prompt upload as markdown only (✅/❌ glyphs drop silently
under xelatex). Upload set: 4 canonical .md + 2 PDFs at `ee3fda3`; commit
hash goes in the OSF project description; tag `osf-prereg-phase2-<date>`
after submission. OSF approach memorised (memory `2026-07-18-10b38c994a0a`);
Quarto-workflow discussion captured to PA inbox for a future session.

**NEXT:** (1) lodge on OSF (morning 2026-07-19; checklist in prereg README);
(2) Cosmos application remaining fields + link the live registration
(deadline 26 Jul); (3) weekend run: FAIR reliability spot-check + pilot
regression gate (pilot papers only — prereg-safe before and after lodgement);
(4) routing-design review passes (/review-implementation + prior-art-scout);
(5) corpus-management implementation before census.

**Held over pending Shawn's verdicts (no silent discard):** working-notes
candidates WN-a (xelatex silently drops out-of-font glyphs — meaning-inversion
hazard for instruments; verify builds by text extraction) and WN-b
(markdown-emphasis stripping needs fixpoint iteration — nested/line-wrapped
spans survive one pass); ~~user-obs candidates 1–4 in
`wiki/user-observations.md` (pending review)~~ [x] 2026-07-22 all four
accepted (with riders; see user-observations.md).

### 2026-07-15/16 — All prereg decision points resolved; content-routing design v0.1

amd-tower resume session, closed for machine swap to the laptop (train). All nine
preregistration decision points resolved with Shawn:

- **D1** sole registrant + LLM disclosure in Summary §8. **D2** cutoff 2026-06-30,
  **D4** 15–25 band, **D5** per-hypothesis families (Holm only within H1a's pair),
  **D6** availability taxonomy, **D8** *Reports* 120/60, **D9** n = 12 — all confirmed
  as drafted.
- **D3 REVISED:** compute cap raised 48 h → **168 h wall-clock on named reference
  hardware**, with the archived-intermediates/table-regeneration partial path written
  into §5 criterion 4 (over-cap papers scoped down via archived posteriors, not
  excluded). Rationale: ad-hoc drops would systematically exclude Bayesian/MCMC papers
  — exactly H4's stochastic side.
- **D7** reliability checks + 0.90 threshold confirmed (= §9 items 1–2).
- Verdict-capture caveat: D3, D7, and §9 items 4–5 arrived via rejected
  AskUserQuestion dialogs (provisional but consistent; D7 twice) — reconfirm wording
  when applying the draft edits.

§9 verdicts thereby all delivered (see repo-state bullet). Item 3 resolved by the new
`wiki/planning/agent-content-routing-design.md` v0.1 (`10947aa`): embed role behaviour
/ push instruments with read receipts / pull pattern libraries. Shawn's design brief:
reliability first, duplication acceptable if split cleanly; read receipts definitely
in. Discussion en route covered pull-miss risk calibration (low per-call, silent,
non-trivial at census scale; stability checks don't catch a consistently-wrong scorer
— the n = 12 human subsample does).

**NEXT ACTIONS (laptop):** (1) apply D1–D9 resolutions to the prereg draft and close
its decision table; (2) run `/review-implementation` + prior-art-scout against the
routing design → v0.2; (3) lodge prereg on OSF; (4) Cosmos remaining fields (deadline
26 Jul); (5) corpus-management implementation before census. PA data synced for the
swap (data `38b78d3`, pointer `183d5e0`). Interaction lesson recorded in the PA
scratchpad: don't pair substantive prose with an AskUserQuestion dialog in one turn —
the prose may not render.

### 2026-07-14/15 — Prereg drafted + stress-tested to v0.2; identity fix; amd-tower sync

One-day session on zbook, closed for machine switch to amd-tower. Phase 2 OSF
preregistration drafted (v0.1 `9405182`) then stress-tested via
`/review-implementation` and revised to v0.2 (`885e664`) — see the repo-state
bullet for the full change list; nine decision points open. Author-identity
confabulation corrected across public metadata and living docs (`38adf36`).
amd-tower brought into sync (quarantine + fresh clone + verified asset rsync;
repo-state bullet has gotchas). Also: prereg v0.1 commit `9405182` includes the
seven-decision table later superseded by v0.2's nine.
~~**Held over pending Shawn's verdicts (no silent discard):**~~ [x] 2026-07-15
all verdicts returned same session: WN-a and WN-b both ACCEPTED (now
Observations 7–8 in `wiki/working-notes.md`); user-obs candidates 1–3 all
ACCEPTED (pending marker cleared). Follow-on question from Shawn: is
`/review-implementation` fit for purpose for study-design reviews, or does it
need a checklist update? Assessment delivered 2026-07-15: protocol phases
generalise; a "Study Designs and Preregistrations" domain checklist is the
gap (circularity, criterion contamination, post-treatment conditioning,
wording-vs-test match, counterfactual presence, pre-specification
completeness, blinding, instrument validation, power-as-estimation) —
APPLIED 2026-07-15 to the canonical skill (personal-assistant `5b76a87`,
`skills/review-implementation/SKILL.md`; live everywhere via the
sync-symlinks convention — canonical skills in personal-assistant
`skills/`, symlinked into `~/.claude/skills/` by
`scripts/sync-symlinks.sh`; amd-tower gets it on next pull/cron sync).

### 2026-07-07/14 — Verified stack sweep, Cosmos evidence, licence purge, corpus plan

Eight-day conversation (compaction 2026-07-08; two usage-limit interruptions).
Full detail in `wiki/reflections/session-log.md` (2026-07-07/14 entry); highlights:
19 verified scout reports + synthesis (P1–P6, S1–S2, C1–C3, G1) with the
speed-to-publish competitor finding; eleven Zotero staging collections; three
scout-agent patches (author gating, arXiv handling, injection defence); Cosmos
draft v0.3 + field-19 evidence pack; framework-paper and corpus-management plans
externalised; working notes Obs 5–6; OA audit → `git filter-repo` purge of two
copyrighted files (Shawn pushed; remote verified clean; backup + commit-map at
`~/Code/repo-backups/llm-reproducibility-pre-purge-20260713/`); Marwick CC BY
preprint downloaded. Held-over gates: none new — queue is Paper B → OSF prereg →
§9 verdicts → corpus implementation → Phase 1. No unreviewed working-note
candidates (Obs 5–6 written and pushed).

### 2026-07-03/06 — Revival: modernisation plan, wiki migration, tasks A-C closed

Project revived after the February pause (one conversation spanning four days,
Shawn intermittently AFK). Three parallel explorers mapped repo state: the JAS
pilot is COMPLETE (5/5 papers, 4 SUCCESSFUL / 1 PARTIAL reproductions; headline
finding: data availability, not code availability, predicts reproduction
outcome). Wrote the agentic modernisation plan and took two structural
decisions with Shawn: **study shape Option A** (OSF preregistration first →
JAS 2023-2026 FAIR census as sampling frame → preregistered confirmatory
reproduction subset) and **docs/ stays at repo root** (wiki/ = process record;
convention promoted to the PA template in a parallel session). Executed the
wiki-layout migration (task B), untracked the committed venv (task A), fixed
lossy de-hyphenation with a frozen-dictionary heuristic (task C; 32/32 tests),
reconciled all stale metadata to v3.0.1, and refreshed README/CHANGELOG.
**Phase 1 build of the modernisation plan is ON HOLD by explicit instruction**
until Shawn reviews the plan. Gotcha for future revivals: the local clone was 8
commits behind origin at session start — fetch before characterising repo state.

- Commits: `11f5734` (metadata reconciliation), `bab66ce` (modernisation plan),
  `5440d12` (venv untrack), `8845a45` (wiki migration), `245d820` (task C fix),
  `3c7313c` (README/CHANGELOG refresh), plus session-close commits
- Key docs: `wiki/planning/agentic-modernisation-plan.md` (v0.2, Option A
  recorded in §6); `extraction-system/scripts/pdf_processing/affix-joined-words.txt`
  (frozen dictionary, regeneration command in header)
- Memories saved: study shape (2026-07-04-856141514e0f), repo-layout convention
  (2026-07-04-e6d2685b35b4), build-on-hold (2026-07-04-f24eccedb145)
- Handoff verdicts (Shawn, 2026-07-06): both working-notes candidates ACCEPTED
  (now Observations 3-4 in `wiki/working-notes.md`); user-obs candidate 1
  accepted, candidates 2-4 discarded. Nothing held over.

### 2026-07-05 — Cosmos grant application framing externalised

From a personal-assistant hub session (cross-repo candidate evaluation deliberately run
there, not here). Decision: this repo is the basis for the Cosmos Institute grant
application (AI x Truth-seeking track, deadline 26 Jul 2026). Full record — grant facts,
portfolio proximity scan (186 grantees, no overlap; Metalens is complementary), pitch
framing (reproduction + FAIR lanes with a sampled human-verification surface; extraction/
credibility lanes as frame and track record, not deliverable), and a brainstorm-grade
budget section — in `wiki/planning/cosmos-grant-application-framing.md`. Also indexed the
agentic modernisation plan + the new doc in `wiki/planning/README.md` (the former was
missing from the index).

### 2026-06-10 — de-hyphenation defect logged (task C)

From a paper-b AB+ co-design session (no code changes to this repo). Building
the first AB+ entry surfaced a lossy-de-hyphenation defect in `_dehyphenate`:
genuinely-hyphenated compounds broken across a line before a lowercase letter
(e.g. `self-\ncorrection`) lose their hyphen in the canonical matching key,
breaking otherwise-valid quote checks. Logged as **pending task C** with a
re-verifiable concrete case and a fix direction. Shawn asked for this to be
recorded here for a proper fix later; paper-b proceeds with the
quote-from-extracted-text + display-cleanup workaround for now.

### 2026-06-07 — seed created

Created this `wiki/continuity.md` as the seed of the wiki migration, from a
session centred on the paper-b repo (matching-grade PDF extractor, merged here
as **PR #1**, `1c4650e`; 24/24 tests; validated on real PDFs). Logged the two
pending infrastructure tasks: untrack the committed `venv/` (2,114 files) and
migrate docs to the wiki layout. No other changes to this repo in that session
beyond PR #1.
