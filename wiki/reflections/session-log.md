---
priority: 5
scope: always
title: "Session Log"
audience: "project team"
tags: [session-shape, working-practices]
created: 2026-02-09
updated: 2026-07-14
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

*New session entries should be appended above this line.*
