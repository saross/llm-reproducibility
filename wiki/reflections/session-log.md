---
priority: 5
scope: always
title: "Session Log"
audience: "project team"
tags: [session-shape, working-practices]
created: 2026-02-09
updated: 2026-07-21
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

- `e1e4cba` fix(assessment): standardise assessment.json schema across 5 pilot papers
- `c3654f6` fix(assessment): cascade schema v1.1 to assessment prompt templates
- `c026756` fix(assessment): update classifier_version to v1.0 in all pilot outputs

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
