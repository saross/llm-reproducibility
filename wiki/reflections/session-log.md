---
priority: 5
scope: always
title: "Session Log"
audience: "project team"
tags: [session-shape, working-practices]
created: 2026-02-09
updated: 2026-08-02
status: active
---

# Session Log

Structured session entries documenting accomplishments, issues, and
pending work.

## Format

```text
## Session: YYYY-MM-DD — Brief title

### Overview

One-sentence session summary.

### Accomplishments

1. First accomplishment
2. Second accomplishment

### Issues

- Any issues encountered

### Commits

- `abc1234` Commit message (if applicable)

### Pending Work

- [ ] Outstanding task
```

## Session: 2026-02-11 — Artefact consolidation and Key et al. lesson capture

### Overview

Executed pre-planned consolidation of study reproduction artefacts and integrated Key et al. 2024 lessons into implementation notes, closing both remaining known gaps.

### Accomplishments

1. **Consolidated 3 reproduction directories** from root `outputs/` into `studies/open-science-compliance/outputs/` (52 files moved via `git mv`)
2. **Updated 3 queue.yaml report paths** and 1 session-handoff.md internal reference
3. **Added `output_dir` field** to all 5 study queue.yaml entries for prevention
4. **Added Step 2a** to reproduction-assessor SKILL.md for output directory determination
5. **Added study layout note** to CLAUDE.md
6. **Integrated Key et al. 2024 lessons** into `wiki/planning/reproduction-implementation-notes.md` — 9 gotchas, 3 key lessons, updated 5-paper comparison table
7. **Resolved both known gaps** in active-todo-list.md

### Issues

- Edit tool requires re-reading files after `git mv` changes their path (tool tracks read state by path, not content)

### Commits

- `47a40fd` refactor(study): consolidate reproduction artefacts under study outputs
- `ba3dae9` feat(reproduction): add output_dir field for queue-driven output routing
- `3b7b841` docs(reproduction): integrate Key et al. 2024 lessons into implementation notes

### Pending Work

- [ ] Phase 7 Step 5: Foundational clarity cluster prompt (next priority)
- [ ] Consider whether SKILL.md artefact path templates (§F, §G, checklists) should reference `{output_dir}` instead of hardcoded `outputs/{slug}/`
- [ ] Consider whether 5-column comparison table in implementation notes needs a different format before adding a 6th paper

## Session: 2026-02-12 — Schema standardisation, version hygiene, and Phase 2 readiness

### Overview

Standardised assessment.json schema across 5 pilot papers, cascaded schema v1.1 to prompt templates with prevention checklist, fixed classifier_version in all pilot outputs, and assessed readiness for Phase 2 study design.

### Accomplishments

1. **Standardised 5 assessment.json files** to flat canonical structure — unwrapped `assessment_metadata` wrappers (crema, marwick, dye), renamed field variants (`paper_slug`→`paper_id`, `system_version`→`assessor_version`, `signal_scores`→`signals`), bumped `schema_version` to `"1.1"`
2. **Updated assessment-schema.md** canonical example to match new structure
3. **Cascaded schema v1.1 to 4 prompt templates** — `paper_slug`→`paper_id` in 3 cluster prompts, `schema_version` bump in final report prompt
4. **Added Schema Compliance section** to assessment-schema.md with 4-location update checklist
5. **Fixed classifier_version** in all 5 classification.json files (4× `v0.2-alpha`, 1× `v2.1-alpha` → all `v1.0`) plus 1 stray alpha in crema's credibility-report.md footer
6. **Assessed Phase 2 readiness** — surveyed full todo list, pilot findings report, and study protocol; concluded infrastructure is ready with two minor refinements (wrapper script metric + data availability taxonomy) foldable into protocol design

### Issues

- Context compaction mid-session — earlier work (Item 1, Commit 1 of Item 2) completed by prior instance
- Edit tool requires reading files before editing (tripped on cluster-2 prompt)
- `grep -c` returning exit code 1 on zero matches broke `&&` chains in verification scripts

### Commits

- `aa75817` fix(assessment): standardise assessment.json schema across 5 pilot papers
- `faef450` fix(assessment): cascade schema v1.1 to assessment prompt templates
- `be7271a` fix(assessment): update classifier_version to v1.0 in all pilot outputs

<!-- Hashes remapped 2026-08-02. As recorded, these read `e1e4cba`, `c3654f6`,
     and `c026756`, none of which resolve in current history — they are
     pre-rewrite hashes. Each was re-identified by exact commit-message match
     against current history; all three land on 2026-02-12, the original date.
     The commit contents are unchanged; only the identifiers were orphaned. -->


### Pending Work

- [ ] Phase 2 study protocol design (user pausing to think — will return in 1-2 days)
- [ ] Queue.yaml FAIR score comments still show old-format scores (e.g., "30/32", "10/16")
- [ ] Credibility-report.md files (crema, marwick) not audited for structural consistency beyond version string

## Session: 2026-07-03/06 — Project revival, modernisation plan, wiki migration, loose ends

### Overview

Revived the project after the February pause. Mapped repo state with three parallel
explorers, reconciled stale metadata, wrote the agentic modernisation plan (direction
approved; Phase 1 build on hold), migrated to the four-artefact wiki layout, cleared
all three continuity pending tasks (venv untrack, wiki migration, de-hyphenation fix),
and refreshed README/CHANGELOG to v3.0.1. Study-shape decision taken: Option A
(census + preregistered subset).

### Accomplishments

1. **State assessment** — pilot confirmed complete (5/5 JAS papers, 4 SUCCESSFUL /
   1 PARTIAL reproductions); discovered June lateral work (PR #1 PDF matching layer,
   continuity seed) via pre-push fetch after local clone proved 8 commits stale
2. **Metadata reconciliation** (manifest → v3.0.1) — todo list, planning README,
   study README, cluster_1 version, assessment_json schema entry
3. **Agentic modernisation plan** (`wiki/planning/agentic-modernisation-plan.md`,
   v0.2) — five agents + three workflows for the reproduction/FAIR lanes; phased
   path with regression test on pilot papers and a hard cost gate
4. **Decisions recorded**: study shape Option A (preregister → JAS census →
   confirmatory reproduction subset); docs/ stays at repo root, wiki/ = process
   record (generalises to cross-repo template; promoted to PA in a parallel session)
5. **Wiki migration** (continuity task B) — planning/ and docs/notes/ into wiki/;
   created index, user-observations, claude-observations; reference sweep;
   README docs-vs-wiki map
6. **Venv untracked** (task A) — 2,114 files out of the index per prescription
7. **De-hyphenation fix** (task C) — compound-prefix + frozen-dictionary heuristic
   in `pdf_cleaner.py` (`affix-joined-words.txt`, 9,810 words); 32/32 tests incl.
   8 new regressions; dictionary-precedence refinement over the prescribed direction
8. **README/CHANGELOG refresh** — Features (incl. new Reproduction System section),
   Validation, Project Status, Citation, Development History; CHANGELOG entries
   2.7.0–3.0.1 added; all quantitative claims re-verified at source
9. **Three memories saved** (study shape, repo-layout convention, build-on-hold)
   with anchors and why/how_to_apply fields

### Issues

- Local clone 8 commits behind origin at session start → initial "dormant" claim
  needed correction; session-start hook had read the stale snapshot
- Explorer agents misdated cluster prompts (mtime vs header) and over-generalised
  version claims — every relayed specific re-verified before use, ~1 in 10 corrected
- AskUserQuestion timed out mid-session (user AFK) → proceeded on invariant-only
  work (housekeeping + plan doc), deferred the study-shape decision

### Commits

- `11f5734` chore: reconcile stale status metadata on revival
- `bab66ce` docs(planning): add agentic modernisation plan v0.1
- `5440d12` chore: untrack committed virtualenv (already in .gitignore)
- `8845a45` refactor: migrate to four-artefact wiki layout (task B)
- `245d820` fix(pdf): compound-aware de-hyphenation (task C)
- `3c7313c` docs: refresh README deeper sections and CHANGELOG to v3.0.1

### Pending Work

- [ ] Shawn reviews `wiki/planning/agentic-modernisation-plan.md` → unlocks Phase 1
      (agent definitions + workflows); build explicitly ON HOLD until then
- [ ] OSF preregistration of the five pilot hypotheses — must precede FAIR scoring
      of any new JAS papers (Option A ordering constraint)
- [ ] Version-history consolidation candidate: manifest/CHANGELOG/README history
      maintained by hand in parallel (see llm-observations 2026-07-06)

### Contextual assumptions

Phase 1 build deferred by explicit user instruction (deliberation, not blockage).
Cosmos Institute grant framing and the PA template promotion were handled in
parallel sessions by the user — this session deliberately did not touch them
beyond providing the paste-ready prompt. The pre-Claude-5 session prompts remain
authoritative until the agentic lane replaces them; nothing in this session
changed extraction/assessment/reproduction behaviour except the de-hyphenation
fix, which alters canonical matching keys only for affix-prefixed compounds
absent from the frozen dictionary.

## Session: 2026-07-07/14 — Verified stack sweep, Cosmos evidence, licence purge, corpus plan

*(One conversation across eight days; compaction boundary early 2026-07-08; two
usage-limit interruptions with agent relaunch. Facts below verified against the repo.)*

**Scout programme (2026-07-07/08):** six-lane positioning sweep (P1–P6, lit + prior-art,
all adversarially verified), cross-stack synthesis, scout-reports README index. Follow-ups
same window: arXiv blind-spot sweeps S1 (citation integrity, 30 rows) and S2 (protocol
extraction, 27 rows); approved deeper chains C1 (competitor watch — no direct rival;
Chakravorti 2026 and Zhu 2026 named nearest), C2 (citation toolchain — accuracy engine
off-the-shelf), C3 (CEM/RDMAP — 7 competitor flags; appropriateness niche zero citers);
G1 grey-literature guard pass (documented 26-query null; first-mover claims scoped
"to our knowledge" with Spennemann 2023 demarcated). Nineteen verified reports total.

**Bibliography:** ~330 verified finds imported to eleven dated Zotero staging
subcollections (P1–P6, S1–S2, C1–C3), DOI-deduplicated; arXiv items via the DataCite path.

**Agent hardening (personal-assistant):** length-gated author-rendering rule (`cfa0c3d`);
arXiv/preprint handling for proposer + verifier (`096c48e`); standing injection-defence
rule across the scout quartet (`b31342b`).

**Cosmos application:** proposal v0.3 (body 482/500) with verifier-backed positioning
sentence; field 19 evidence pack + 8-item verified bibliography; guard-pass null folded
in. OSF preregistration confirmed as next task after Paper B. §9 verdicts captured to
Shawn's inbox.

**Publications planning:** framework-paper plan externalised
(`long-tail-credibility-framework-paper.md`) — state-of-play/agenda genre, phase × status
decomposition, RSOS/QSS venue read, solo-vs-consortium open (COS/CWTS/RDA contacts noted).

**Working notes:** Obs 5 (injection sightings) and Obs 6 (verifier catch taxonomy)
written via obs-writer, which also caught and corrected an unverified orchestrator claim.

**Licence reckoning:** OA audit of eight untracked papers (six CC BY CLEAR); corpus-queue
DOI fix for key-et-al-2024; `git filter-repo` purge of the dye supplement (two historical
paths + LFS pointer) and marwick-2025.txt from all 242 commits; full pre-purge backup at
`~/Code/repo-backups/llm-reproducibility-pre-purge-20260713/`; Shawn force-pushed; remote
verified clean. CC BY SocArXiv preprint of Marwick 2025 downloaded for future
licence-clean extraction. Corpus-management redesign agreed and externalised
(`corpus-management-plan.md`), wired into the modernisation plan as a pre-Phase-1
prerequisite.

**Contextual assumptions:** all commit hashes cited in documents written before
2026-07-13 predate the history rewrite and no longer resolve (commit-map in the backup;
subjects still search). GitHub-side LFS storage may retain the unreferenced supplement
object (Support ticket or repo recreate; low urgency). The Cosmos deadline (26 Jul) and
the competitor-convergence finding jointly drove the "bank everything immediately"
tempo; incremental commits after every verified artefact were a deliberate response to
two prior usage-limit outages.

## Session: 2026-07-14/15 — Preregistration drafted + stress-tested, identity fix, machine switch

*(Single conversation on zbook, no compaction; closed for the switch to amd-tower.
/handoff ran mid-session after the sync; /reflect ran last.)*

**Preregistration:** Phase 2 OSF preregistration drafted as an open-ended registration
(`studies/open-science-compliance/protocol/phase-2-preregistration-draft.md`, v0.1
`9405182`) from pilot report §7, protocol v1.0, and the Cosmos drafting-care
constraints; then stress-tested via /review-implementation and revised to v0.2
(`885e664`): H2 endpoint switched to verification-target coverage (denominator locked
pre-execution; exact Jonckheere–Terpstra primary, fractional-logit secondary,
verdict-based Fisher demoted to consistency check); H1 restricted to quantitative
papers (post-treatment conditioning argument) with trend-adjusted secondary and a
code-sharing-prevalence outcome; JAS: Reports DiD control arm added (Shawn approved;
FAIR lane, reproduction exploratory; Marwick 2025 grounds AER absence; pre-launch
re-check + fallback pre-specified); H4 reworded to match its test; blinding, 0.90
stability threshold, human-validation subsample (n=12), and power table added. NINE
decision points open — drafted but deliberately NOT lodged.

**Identity fix (`38adf36`):** confabulated author identity (Shawn Graham / Carleton /
`github.com/shawngraham`) corrected to Shawn Ross / Macquarie / `saross` + ORCID
0000-0002-6492-9025 across CITATION.cff, codemeta.json, CONTRIBUTING.md, pilot report,
and two living planning docs; archive and verbatim extracted texts left untouched.

**Machine switch:** amd-tower pre-purge clone quarantined to
`~/Code/repo-backups/llm-reproducibility-pre-purge-clone-20260715`; fresh clone
verified clean (0 purged-path hits), hooks installed, 30 gitignored corpus/text assets
rsynced with checksums verified; remote is HTTPS+gh (SSH key needs interactive agent).

**Rituals and verdicts:** /handoff (continuity `9f16fd4`, obs `69b9e11`); same-session
verdicts — WN-a/WN-b accepted as working-notes Obs 7–8, user-obs 1–3 accepted
(`d4c1ac3`, `9ee5209`, `ac1fd36`). Skill-fitness question answered: protocol fit,
checklist gap; study-design checklist applied to canonical skill (personal-assistant
`5b76a87`). Skill-deployment convention verified on disk and memorised
(`2026-07-15-db8154bebefb`): canonical in personal-assistant `skills/`, symlinked to
`~/.claude/skills/` by `sync-symlinks.sh`.

**Contextual assumptions:** the prereg's nine decision points were left open
deliberately (post-lodgement changes are public amendments); the DiD arm is
conditional on the pre-launch Reports policy re-check; amd-tower's venv is not
recreated and its remote protocol changed — both noted in continuity. Cosmos deadline
26 Jul unchanged.

*New session entries should be appended above this line.*

## Session: 2026-07-15/18 — Prereg resolved to v0.7, OSF materials, lodgement eve

*(One conversation resumed across 15–18 July on amd-tower; no compaction. /handoff
and /reflect both ran at the 07-18 close; /handoff wrote the obs registers first.)*

**07-15/16:** all nine prereg decision points resolved with Shawn (D3 revised to
168 h on named hardware + archived-intermediates partial path; rest as drafted);
all six modernisation-plan §9 verdicts delivered; agent-content-routing design
v0.1 written and committed (`10947aa`) — embed role behaviour / push instruments
with read receipts / pull pattern libraries; session closed for machine swap with
full data sync.

**07-18 (Paper B done; Shawn returned):** four review batches took the prereg from
v0.2 to lodgement-ready v0.7 — resolutions applied (`d85bde9`); window → 2022-01-01
with power table recomputed, H5 + credibility lane reclassified exploratory,
*Reports* census option (`5407c0f`); descriptive-only credibility outputs,
six-level friction-ordered availability taxonomy with standardised L4 request
protocol, sampling-cap gate clause, pre-specified descriptive-reporting block
(`c7d2165`); two schema-verified RDMAP metrics for H5, three-week L4 window with
late-response clause, FAIR4RS as amendment-path extension, FAIR×coverage
estimation, human-validation wording fix (`2c10768`); pilot per-paper-scores
bridging note (`ba43599`); dangling analysis-plan reference fixed (`d003ade`).
Lodgement materials built on the inscriptions `wiki/prereg/` convention
(`2d26d95`): plain-prose summary, two glyph-verified PDFs, README recipe +
checklist. Authorship policy applied (`ee3fda3`): pilot report v1.2 sole human
author + §10 LLM-use statement; CITATION.cff/codemeta author fields cleaned; git
trailers retained (Shawn confirmed). OSF project `llm-assisted-reproducibility`
created by Shawn (programme-level description + six keywords supplied); lodgement
approach saved to memory (`2026-07-18-10b38c994a0a`). READY TO LODGE at `ee3fda3`.

### Contextual assumptions

Lodgement deferred overnight by choice, not blockage. The Cosmos deadline (26 Jul)
drives next week's sequencing; the weekend run intention is pilot-papers-only
(reliability checks + regression gate), safe before or after lodgement. pandoc is
absent from amd-tower's PATH — PDFs build via Quarto's bundled 3.6.3; the recipe is
pinned in the prereg README. The census cutoff (2026-06-30) has passed, so
lodgement timing cannot affect frame membership.

## Session: 2026-07-20/21 — Prereg lodged on OSF; Cosmos application submitted

**Preregistration lodged (2026-07-20, by hand, Claude-guided):** browser extension
unavailable, so Shawn drove OSF while the session supplied verified paste
artefacts. Upload set (4 md + 2 pdf) confirmed byte-identical to `ee3fda3`;
five-file form cap dodged by lodging from the project (all six artefacts froze
from OSF Storage); duplicate PDF upload caught by size-check and deleted.
Paste-file convention extended twice under fire: hard line-breaks unwrapped to
one flowing line per paragraph (`e873026`, `f2f467a`; OSF text boxes render
breaks literally), and the §10 power table pasted as run-together pipes —
accepted, not re-lodged; tables now banned from paste-field content
(`6577119`, README recipe + convention memory updated). Tag
`osf-prereg-phase2-2026-07-20`; registration <https://osf.io/dqnhg/>.

**Embargo arc:** lodged WITH embargo (double-blind contingency; deviation
recorded `90b0c37`). Journal-policy agent: JAS single-anonymised; JAS: Reports
dropped its mid-2024 double-blind mandate; JCAA author's choice — no candidate
venue requires it. Shawn lifted the embargo 2026-07-21; public resolution
verified by anonymous API; **DOI 10.17605/OSF.IO/DQNHG** (`13261c1`).

**Cosmos application v0.4→v0.7 and submission (2026-07-21):** v0.4
registration-alignment pass under the academic-prose skill (error-detection
sentence, DiD clause, hypothesis wording, 499/500; `7d37530`); v0.5 CV-verified
affiliations and credentials, both CVs read from ~/Downloads and kept out of
the repo (`cd0065b`); v0.6 clean-context adversarial verification reconciled
against the PA-hub session's ledger (`ef8a6cb`) — all claims confirmed, three
ledger pointers corrected, six field 19 wording fixes, self-pitch
overstatements fixed (`c897cce`); v0.7 Shawn's body revision tightened 566→498,
we-voice (Brian named), truth-seeking token restored (`44bef42`+). Field
selections: title "Making Verification of Published Research Routine"
(statement-of-mission, no colon); merged one-liner; two-sentence self-pitch
(builder + domain leadership, preregistration claims toned to "argued the case
for"); parity-length Brian entry (philosopher of science and technologist,
supporting role calibrated via "my long-time collaborator"). Live-form deltas
(links-only additional-info field; multi-file CV upload) → evidence pack
published at `docs/cosmos-evidence-pack.md`; paste file + committed generator
(`build-cosmos-form-paste.py`) keep form text and verified draft in lockstep.
**SUBMITTED 2026-07-21**, US$8,000, five days ahead of deadline (`f9c14b0`).

### Contextual assumptions

Three-way concurrency shaped the session: Shawn edited the draft live, the
PA-hub session committed its verification ledger to this repo mid-stream, and
this session spliced generated text — two edit collisions and one
stale-buffer warning were the visible cost; re-read-before-edit and
diff-before-commit were the discipline. The 26 Jul deadline and rolling review
drove same-day iteration. The form capture of 2026-07-07 had drifted from the
live form by submission day — future form-fill work should re-screenshot at
fill time. Body word limit is strictly <500; the generator asserts it.

## Session: 2026-07-22/24 — Review cascade, corpus infrastructure, Phase 1 opens

Three-day amd-tower session, remote-controlled from campus for much of days two
and three (Shawn on zbook; four zbook paper-b commits rebased over mid-session).

**Day 1 (07-22):** Routing-design review passes run and adversarially verified —
implementation review (D1–D10, E1–E8) + prior-art scout (110 claims, 107
confirmed, 0 corrected). Critical catch: three defects in the Pass 6 FAIR prompt,
present in the OSF-frozen copy at `ee3fda3`; fixed in-repo (`abdc526`), erratum
log started (`f4dfa0e`, path approved by Shawn: accumulate errata, amend at the
hard stop). Reports externalised (`c9a6ecd`). Model-testing decisions recorded:
three-Claude-model spot-check, Sonnet 5 + Opus 4.8 on Max first, ask-before-Fable
gate, OpenAI Sol arm to be designed later (needs own harness + amendment). The
standalone weekend run superseded by one post-build validation phase.

**Day 2 (07-23):** Design v0.2 written (`3914f81`) — policy retained, mechanisms
rebuilt on native harness primitives, all five open questions closed.
Corpus-management implementation scoped (`edf7f56`): repo audit, 8-item build
order, target structure (out-of-tree store, study-scoped manifests). zbook synced
(repo + 31 gitignored corpus files).

**Day 3 (07-24):** §9 added — workflows as batch engine (v0.2.1, `74e7ed9`) after
Shawn's review question. Pre-build juncture /review-implementation (his request):
12 defects, 8 enhancements; headline catches — §2.2 ladder was a prereg deviation
(now amendment-gated), §9 hook assumption doubted, spot-check statistics
undefined, contamination risk (repo-readable pilot scores). All cheap fixes
applied same day (design v0.2.2, corpus plan v0.2.1, amendment scope queued in
erratum log — `3080022`). **Shawn signed off v0.2.2; amendment scope ratified;
corpus decisions confirmed** (`01fd8d4`). Corpus census blockers executed
(`fbf477c`): store live (16 papers, 28 files, 71.7 MB, sha256-verified),
manifests + `fetch-corpus.py` (verify 28/28) + `sync-corpus.sh` (first QNAP sync,
44 files), LFS narrowed, pre-commit corpus gate installed and block-tested.
**Phase 1 opened:** D-2 hook spike PASSED on all four counts (two haiku probes) —
engine = workflows confirmed; FAIR instrument extracted to its canonical file
with receipt token; manifest `shared_content` registry started (`25d1c0d`).
Elsevier TDM trail: three diagnostic 403s (entitlement → provisioning →
checkbox-insufficient), support email drafted, route deprioritised on Brian's
field intelligence — Zotero-proxy recorded as the probable path
(`c903b89`…`5b77b78`). Migration script archived (`cb7a24c`).

**Carry-forward:** WN-a/b/c/d/e verdicts (Shawn, owed since 07-18/21); amendment
drafting + lodgement before the validation phase; build queue (D5 consistency
script → instrument files → agent definitions → production hooks → corpus items
5–6); Elsevier/Zotero investigation + amd-tower `.env` key (Shawn); Cosmos watch
~mid-August.

### Contextual assumptions

Concurrent zbook sessions pushed paper-b work throughout — every push here
required a fetch-first/rebase discipline. Fable usage windows gated session
timing ("usage has reset" opened day 2). The cost-gate re-specification assumes
Max-plan billing (usage windows, notional `total_cost_usd`); if the census moves
to an API key the §Phase-3.2 arithmetic changes. Elsevier diagnostics ran through
Shawn's campus terminal because entitlement is network-dependent — the session
itself sits on the home network. The corpus store's second copy is manual-cadence
(no automated sync schedule exists anywhere on rpi-server).

## Session: 2026-07-24 — Phase 1 build queue executed; decision pass (second session)

Single session in two movements. **Autonomous build (six commits, all pushed):**
D5 manifest-consistency gate (`scripts/check-manifest-consistency.py` +
17 unit tests, wired into pre-commit, block-tested; `b1aab17`); instrument
canon completed — five new canonical files extracted from prereg §4–§7 and
plan §4.3, adversarial-review framework promoted pull→push with governance
header, reproduction SKILL.md registered as second machine-checked mirror,
7 `shared_content` entries total (`18cb659`); five agent definitions with
pinned models + `agent_definitions` hash registry, D5 extended with model-pin
and memory-prohibition checks (`de175d3`); production hooks — manifest-driven
SubagentStart push with sha256 receipts, SubagentStop receipt gate (version/
token/model_id/transcript checks, fail-closed, ESCALATE passthrough),
PreToolUse pre-flight; probe archived; 17 synthetic pipe-tests (`115d202`);
consolidated OSF amendment 1 drafted from the ratified scope with
pre-lodgement checklist (`8f0cad8`). **Decision pass (Shawn, seven decisions,
`88f9c50`):** reproduction pins stay provisional (Opus 5 expected); Fable
variant deferred to benchmark approval; amendment read once at lodgement;
three build judgement calls ratified; WN-a–g all accepted → working-notes
Observations 9–15; user-obs A–C all accepted (C → bilateral confidence-label
rule); MQ TDM enquiry dropped. Mid-build rebase over the parallel session's
handoff commits (disjoint files, clean).

**Contextual assumptions.** The reproduction-lane pins were left provisional
specifically because Shawn expects Opus 5 imminently — the manifest comment
records this, but the session context is that model selection is deliberately
deferred to the validation phase, not unfinished. The pin vocabulary shifted
mid-session on discovering current models expose no dated snapshot IDs (the
aliases are exact; see abductive entry). A parallel session was running for
part of the build — known, coordinated, no conflict; its handoff wrote Entry 8
and claude-obs 19–21 before this session's reflect pass, which is why today's
registers carry two sessions' entries.

## 2026-07-27 — D5 hardening, mirror convergence, Opus 5 repin (third session)

Third session, amd-tower, resuming from the 2026-07-22/24 handoff. Roughly
bisected: an unwitting duplicate build, then reconciliation and three decisions
from Shawn.

**Collision.** The resume prompt opened Phase 1 with D5 first. Built
`scripts/check-manifest-consistency.py` (nine checks, pre-commit wiring,
fault-injection tested, hook block-tested), converged the Pass 6 mirror, and
drafted erratum Entry 2 — then a pre-commit `git fetch` revealed `origin/main`
seven commits ahead: zbook had executed the whole Phase 1 queue on 24 July,
including its own D5 checker (340 lines + 247 lines of pytest) and the
consolidated amendment draft. Stopped before committing; nothing was pushed over
the other session's work.

**Reconciliation (Shawn's call: port my checks into theirs).** Reset, fast-
forwarded, then compared the two implementations. Theirs survives — broader
registry (7 entries), wired to the agents, hooks, and tests. Two gaps ported in
(`03f10ad`): **byte-exact mirror regions** via HTML-comment marker pairs, and a
**reverse sweep** for unregistered instrument files. Both verified as live gaps
first: their gate reported `PASS (0 errors)` on a tree whose Pass 6 mirror was
missing four normative statements from prereg §7.1, and an unregistered `.md`
dropped into the instruments directory passed silently.

**Erratum Entry 2 (`a867319`).** The Pass 6 prompt — in the OSF-frozen artefact
set — restated the FAIR instrument incompletely: unscoreable→0, never-aggregate,
the A1 majority rule, and the FAIR4RS scope statement all absent. Impact checked
against persisted pilot outputs rather than asserted: four pilots, all /15, none
unscored, none aggregated, key-et-al-2024 showing the A1 rule operating
("Only 3 of 13 datasets (23.1%)"). Erratum-class; no pilot score revised. Folded
into amendment §1, with a model-identifier provenance limit added to §3.

**Second mirror converged (`700173c`, Shawn's call).** `verdicts-and-precision`
→ reproduction-assessor `SKILL.md` carried canon's prose *reworded*, and omitted
the PAPER_ERROR human-escalation sentence and environment-spec levels 0–5
entirely. Because the content lands in three separate workflow sections, added
**named segments** (`canon-begin: id#part`); the instrument now mirrors in six
segments plus a new SKILL.md section H. Determined no erratum and no amendment
required, on three grounds: SKILL.md is not in the frozen set (four files are),
the discrepancy vocabulary is not registered text, and converging a mirror
changes delivery not instrument semantics. `mirror_mode: structural` retained as
a declared-weaker fallback; unused.

**Opus 5 repin (`9d35221`, Shawn's call).** All four `claude-opus-4-8` pins →
`claude-opus-5`; `fair-assessor-opus-4-8.md` renamed. Verified no scored
artefact ever ran on 4.8 (extractions record `claude-opus-4-5`/
`claude-sonnet-4-5`); history untouched, manifest comment carries the
22 Jul → 24 Jul → superseded-27 Jul chain. All five agent hashes recomputed and
independently re-verified.

**Process fix (`8e485b2`).** Fetch-first added to this repo's `CLAUDE.md` and to
step 6 of the handoff protocol, with the mechanism recorded (remote-tracking
refs are local caches). Separately, `~/personal-assistant/.env.bak-2026-07-27`
held live API keys and was not gitignored — `.env` was covered, `.env.*` was
not; broadened and pushed.

Tests 17 → 32. Both repos clean and `0/0` at close.

**Contextual assumptions.** The duplicate build was not a coordination failure
between Shawn and me — he was on zbook on 24 July and told me so at session
start; the resume prompt simply predated that work, and my sync check read a
stale ref rather than reporting it. Two items were flagged and remain
unconfirmed at close: the repin changes the validation benchmark's Opus arm
(an input to the ratified 22 July three-model decision), and the amendment's
provenance paragraph is an addition beyond the ratified scope. Both were
executed and flagged rather than deferred, on the reading that Shawn's repin
instruction was general and the provenance caveat is load-bearing for a
reproducibility claim — but neither has an explicit sign-off.

## Session: 2026-07-27 (second) / 2026-08-02 — Verdicts cleared, corpus list closed, monitoring planned

### Overview

Two sittings on amd-tower, resumed from the 2026-07-27 handoff. First: clear the
four held-over verdicts and close the corpus build list. Second, five days later:
walk a returning collaborator through two findings, correct one of them, and
plan the gate widening. Six commits to `main` (`640ffbb` → `11c4066`), one PR
opened and deliberately held.

### Accomplishments

- **Four held-over verdicts cleared.** WN-h/WN-i accepted as working-notes
  Observations 16 (structural checks have a prose-shaped blind spot) and 17
  (independent reimplementation as a review technique) — both drafted against
  sources first, since only one-line summaries existed. User-obs candidates A–C
  held again and annotated as triaged. Opus-5 benchmark arm confirmed. Amendment
  §3 provenance paragraph deferred to the lodgement read.
- **Fable 5 census arm built** (`640ffbb`). Generated from the Opus 5 definition
  and diffed rather than transcribed; registered in `manifest.yaml` with sha256.
  The sibling-sentence edit changed the Sonnet 5 and Opus 5 hashes too — all
  three updated in the same commit.
- **Corpus item 5** (`bd5bc40`): reproduction preparation prompt v1.0 → v1.1 —
  fetch-with-checksum default, store/attempt/scratch destinations, Materials
  Acquired table in `log-template.md`.
- **Corpus item 6** (PR #2, unmerged): extraction schema v2.7 adding optional
  `source_file` + `source_sha256`. Additivity verified mechanically; v2.6
  retained; pilots deliberately not back-filled.
- **Commit-hash defect fixed** (`92aa098`): three orphaned pre-rewrite hashes
  remapped by exact message match, with an inline note recording the remap.
- **Monitoring plan drafted**: `wiki/planning/artefact-integrity-monitoring-plan.md`
  — seven entity classes, per-entity `check:` declarations, generated coverage
  self-report, five gated phases.
- **Amendment §3 now names three model identifiers** (`11c4066`), closing task E1.

### Decisions

- **Widen the D5 gate so every registered entity is checked hard** (Shawn,
  2026-08-02). Reorganisation acceptable. Plan drafted, not implemented.
- **Add the Fable arm to the lodged amendment text** (Shawn, 2026-08-02), with
  the pre-declaration that it cannot be selected for the census under the cost
  rule — its role is instrument evidence plus §5 robustness data.
- **Billing route settled**: Max-plan Fable allocation first, API billing account
  for excess; the run is governed by the ordinary standing API review gate.
- **PR #2 held until after lodgement** — merging would register v2.7 while eight
  extraction prompts still emit `2.6`, and completing the cascade edits a frozen
  artefact in the pre-lodgement window.
- **User-obs A–C held over a second time** rather than accepted or discarded.

### Corrections

- The `assessment_json` "genuine mismatch" reported 2026-07-27 was a measurement
  error, not repo drift: `1.1` (payload) and `2.1` (document) are different
  version axes, both correct. Escalated to Shawn as a decision; withdrawn
  2026-08-02 with the evidence.
- An initial stale-hash sweep returned a meaningless 187 (DOIs, ORCIDs, corpus
  IDs, placeholders). Corrected before reporting: 115 resolving, 21 not.

### Measurements

- D5 version check covers **7 of 25** registered `file`+`version` entries.
- Backticked commit references: **115 resolve, 21 do not**; all 21 in `wiki/`;
  3 fixed, 18 outstanding.
- 32/32 tests green and gate PASS at every commit; `0 behind / 0 ahead` at open
  and close of both sittings.

### Commits

- `640ffbb` feat(agents): add Fable 5 benchmark arm to the census lane
- `9091706` docs(wiki): clear the four held-over verdicts
- `bd5bc40` feat(repro): corpus item 5 — fetch-with-checksum, destinations, URL+hash log
- `aedc7f5` docs(continuity): corpus items 5-6; D5 version-check coverage finding
- `92aa098` fix(manifest): remap orphaned commit hashes; plan artefact-integrity monitoring
- `11c4066` docs(prereg): name the Fable 5 arm in amendment §3; close task E1
- `134eb04` feat(schema): v2.7 — source_file + source_sha256 provenance *(PR #2, deliberately unmerged)*

### Pending work

Task E in `continuity.md`: E1 closed; **E2** (§1 word-for-word consistency check)
and **E3** (OSF paste artefact) are Claude's and unstarted; **E4** is Shawn's
read-and-lodge. E3 should follow E4, not precede it. Then PR #2 plus the prompt
cascade as one change, then monitoring Phase 0.

### Contextual assumptions

The second sitting opened with Shawn cold after several days on map-reader-llm,
which shaped it into an explain-then-act session rather than a build session —
and the `assessment_json` correction surfaced precisely because the finding had
to be laid out for a reader. The monitoring plan draws on map-reader's
verification charter at Shawn's suggestion; that charter already names this
repository as a future target, so the borrowing is anticipated rather than
opportunistic. Sequencing throughout assumes the amendment lodges before any
gate work begins.

## Session: 2026-08-03 — Lodgement, monitoring phases 0–3, the benchmark, two audit rounds

Single long session on amd-tower (session
0360402e-e4b8-4e21-9de6-1eb48c14b416), resumed from the 2026-08-02 handoff.
Roughly 25 commits, `a208f9d` → `9f67480`, plus reflections/handoff.

**Amendment (task E, closed).** E2 rule-4 consistency check (13 frozen
phrases verified at source; three flags raised and adjudicated same day —
one fixed, one accepted as typography, one dissolved when the "missing"
fifth pilot FAIR assessment was found intact under crema's pre-v2.6
`infrastructure` key). Erratum entry 2 gained a dated coverage correction;
working-notes Observation 20 accepted; monitoring plan gained finding (c) +
class E8. User-obs A–C adjudicated (A, B accepted — B generalised to
"investigate, explain, avoid"; C discarded and systematised as
handoff-protocol step 0). Academic-prose skill's first test re-expressed
the amendment (token-invariant, register exit-checks clean); registrant
promoted it, added a §5 cross-vendor pre-declaration (OpenAI arms
considered, deferred to the FAIR4RS-style extension pattern), and E3's
paste artefact passed its docstring verification. **Lodged via the OSF API**
as a versioned registration update (SchemaResponse revision
`6a7017da97adb06288afef80`; DOI unchanged; tag
`osf-amendment-1-2026-08-03`) after an Opus-agent sweep of the developer
docs, a staged byte-identical draft, and the registrant's
placement decision (append at end). Validation phase unblocked.

**Post-lodgement queue.** PR #2 merged as one change with the
eight-prompt v2.6→v2.7 cascade and project.version 3.1 (`58c3fe7`).
Monitoring plan §9 resolved (wiki unregistered; E7 warn-first; one
verified remap pass in Phase 4; crema register-without-rewrite). Phases
0–3 shipped same day: 55-entity enumeration and classification (§10);
central `entity_checks` map + E8 reference-dataset registration; checker
widened with per-class verification and undeclared-entity failure (closure
probe: the 2026-08-02 false-PASS probe now fails); coverage self-report
line. Tests 32 → 48.

**Benchmark (amendment §3).** API gate presented and approved (billing:
Max first, API for Fable excess). Built the missing pieces: benchmark
output schema v1.0 (registered E4) and validation output home. Three arms
× 5 pilots × 3 runs via per-arm workflows; per-arm verification (receipts,
push log, isolation sweeps, arithmetic), run records with per-spawn
tokens. **Result: all arms below both 0.90 gates** — stability
0.807/0.873/0.813, concordance 0.773/0.807/0.820 — with item-structured
disagreement shared across arms (A1.2, R1.1, A2, R1.3, F-block upstream
crediting). 4.25M tokens, ≈$27 API-equivalent. Decision package in
`benchmark-summary.md`; §2 remediation decision deliberately deferred to
next session.

**Audits.** Two-lens /audit (Opus agents, read-only, GOVERNED fencing) of
all code since the 2026-07-27 review: 9+ Criticals including a receipt
gate that had never validated a production receipt (15 blocks, 0 passes in
arm 1) and fail-open pre-flight paths. Fix pass `3b01676` (tests 48 → 84,
committed hook suite replacing the never-committed "17 pipe-tests");
re-audit of the fix found real regressions (gate still blocked 9/15 fable
spawns; cross-item receipt substitution; blast-radius and encoding holes)
— registered in `wiki/planning/audit-2026-08-03-follow-ups.md` with
deferred-by-design items (schema v1.1 pre-census; C7 instrument sha256
GOVERNED; unwrap-paste fixes pre-lodgement; wiki pipe-tests correction).

**Contextual assumptions.** Sonnet 5 intro pricing ($2/$10) runs to
2026-08-31, which the amendment's price-ordering tolerates either way. The
`[1m]` model-id marker on the opus arm is treated as the harness's
1M-context surface of the pinned model, accepted by prefix and recorded
verbatim. Schema fixes were deliberately withheld mid-benchmark to keep
arm configs identical — v1.1 must land before the census, not merely
eventually.
