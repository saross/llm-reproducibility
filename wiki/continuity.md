---
title: "llm-reproducibility — Continuity (Living Doc)"
tags: [infrastructure, coding-practices]
created: 2026-06-07
updated: 2026-06-10
status: seed
---

# llm-reproducibility — Continuity (Living Doc)

**Purpose:** cross-session state, pending work, and a session-by-session log
for this repo. Updated in place at session end (no new file per session).

**Status: SEED.** This file bootstraps the wiki-style documentation layout in
this repo. The repo is otherwise still on the **legacy `docs/notes/` layout**
(`docs/notes/working-notes.md` + `docs/notes/reflections/`) and has no
`user-observations.md`. This file exists to (a) carry the two pending
infrastructure tasks below across sessions, and (b) **initiate the migration**
to the current per-project wiki layout. It was created 2026-06-07 from a
session working primarily in the `2026-mq-llm-dh-judgement-paper-b` repo (the
matching-grade PDF extractor merged here as PR #1).

**How to update at session end** (per the canonical convention —
`~/personal-assistant/global-claude-md/handoff-protocol.md`):

1. Mark done items in place: `[ ]` → `[x] YYYY-MM-DD`; never delete.
2. Add new items as `[ ]` with a brief note.
3. Append a new "Session log" entry at the bottom (most recent first).
4. Carry forward open questions.

---

## Repo state (2026-06-07)

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

### C. Fix lossy de-hyphenation of genuine compounds  [ ]

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

## Open decisions

- [x] 2026-07-03 `docs/` disposition: **stays at repo root** (decided with the
  conventions rationale recorded in task B note above and README's docs-vs-wiki map).
- [x] 2026-07-03 Sequencing: done as separate commits (A on 2026-07-03 standalone;
  B as its own migration commit).

## Session log

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
