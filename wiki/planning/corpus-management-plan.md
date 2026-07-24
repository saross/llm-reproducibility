# Corpus management plan: articles, supplements, and third-party materials

**Version:** 0.2.1
**Date:** 2026-07-24 (v0.2: 2026-07-23; v0.1: 2026-07-13)
**v0.2.1:** applies the 2026-07-24 pre-build juncture review
(`wiki/planning/reviews/2026-07-24-pre-build-juncture-review.md`, D-9/D-10/D-11 +
E-2): backup promoted to census-blocking; copy-then-verify migration; `meta.json`
machine-generated from the canonical manifest; fetch-script politeness specified;
Elsevier TDM enquiry and manual-acquisition budget added.
**Status:** Agreed direction (Shawn, 2026-07-13); implementation SCOPED 2026-07-23
(repo audit + build order + target structure below, §Implementation scope) —
execution on hold pending Shawn's confirmation of decisions 1 and 3 and his
routing-design v0.2 review. Sequenced as pre-Phase-1 infrastructure for the agentic
modernisation plan (the JAS census and corpus-screener need the manifest this plan
creates).
**Origin:** The 2026-07-13 open-access audit and history purge. A publisher supplement
(dye-et-al-2023) entered public git history because a third-party file landed under a
*tracked* output directory and the blanket `*.pdf` LFS rule swept it in; the extracted
text of a closed-access article (marwick-2025) had the same problem, compounded by
`source: null` extraction metadata that forced forensic reconstruction of its origin.
Both were purged via `git filter-repo` (2026-07-13). At census scale this failure mode
recurs unless the design changes.

## Principle

**Never redistribute third-party content, regardless of licence.** Once nothing
third-party is ever in git, open-access checking stops being a compliance gate and
becomes optional metadata recorded once. The default is safe by construction; safety
must not depend on files landing in the correctly gitignored directory.

## 1. Corpus store (outside the repository tree)

A single store, e.g. `~/corpora/llm-reproducibility/<slug>/`, holding per paper:
`vor.pdf`, `preprint.pdf`, `supplement-*.pdf`, `extracted.txt`, and `meta.json`.
All third-party material lives ONLY here — including extracted full text, which is
derivative of the article and carries its copyright. Being outside the tree beats
gitignore: there is no pattern to get wrong. The pipeline locates it via a single
`CORPUS_ROOT` configuration value (or transitional symlinks from the current
gitignored paths: `studies/*/corpus/pdfs/`, `input/sources/`).

## 2. Manifest in git (the citable, shareable corpus)

Extend the existing queue.yaml or add `corpus/manifest.yaml`: per paper — DOI,
bibliographic basics, open-access status and licence (recorded once, informational),
source URLs (version of record, preprint, supplements, datasets), sha256 of each
retrieved file, and retrieval date. Pair with `scripts/fetch-corpus.py`:

- resolves each DOI via Unpaywall and downloads the best open-access copy;
- verifies stored hashes on every fetch;
- lists closed items requiring manual acquisition (with their URLs).

This dissolves the "partial corpora" problem in the sense that matters: the public
manifest is always complete; the local store is complete; third parties can rebuild
the open-access portion with one command and know exactly what to obtain manually.

**Provenance rule:** every extraction records its source file and hash in
extraction.json (the marwick `source: null` gap must not recur).

## 3. What stays in git

Original research data only: extraction.json graphs, scores and verdicts, assessment
outputs, reproduction code, Dockerfiles, logs, comparison reports, and generated
figures. Short location-anchored quotations inside extraction.json are fine
(quotation/fair dealing); derived full text is not, and lives in the store.

## 4. Reproduction runs (fetch-with-checksum — endorsed by Shawn 2026-07-13)

Anything an agent downloads mid-run — publisher supplements, datasets from CDNs —
goes to the corpus store or run scratch, never under `outputs/`, with the URL and
sha256 recorded in the run's `log.md`. Wherever inputs are accessible in open
repositories (Zenodo, OSF, journal data links), the Dockerfile or run script
**fetches with checksum verification at build/run time rather than vendoring the
file** — good reproduction practice independent of licensing, and the preferred
default. Vendor into the store only what cannot be re-fetched reliably.
The reproduction-assessor skill/prompts need a corresponding update.

## 5. Deterministic guardrails (gates, not vigilance)

- **Narrow the blanket LFS rule:** `.gitattributes` `*.pdf filter=lfs` scoped to
  own-artefact directories only (e.g. `**/reproduction/**/outputs/`, `docs/`), so a
  stray third-party PDF cannot be swept into history by the pattern.
- **Pre-commit hook extension** (the filename-convention hook already exists): block
  any newly added `.pdf`/`.txt` outside a whitelist without an explicit override.
  This makes the supplement incident structurally impossible — the working-notes
  Obs 4 point (deterministic gates over agent/human assertions) applied to licensing.

## 6. Cross-machine sync (out of git)

Canonical copy of the store on rpi-server (verify drives mounted before writing, per
network guardrails) with an rsync pull script. This matters less than it sounds: the
fetch script regenerates the open-access majority on any machine from the manifest;
only closed/manually acquired items truly need syncing. Include the store in the
normal backup regime.

## Alternatives considered (and passed on)

- **DataLad / git-annex:** the principled heavyweight solution; real operational load
  for a solo project; revisit only if collaborators need versioned blob access.
- **Zotero storage as the store:** attractive given existing infrastructure, but
  attachment-key paths make pipeline access awkward. Keep Zotero as the bibliographic
  layer and the store as the blob layer, joined by DOI.

## Implementation scope (v0.2, 2026-07-23)

Repo audited against this plan (session of 2026-07-23). **Already in place:** the
gitignore pattern layer (both `corpus/pdfs/` paths, `input/sources/`, extracted-text
patterns, reproduction supplements); every tracked `.pdf`/`.txt` verified to be an
own-artefact; queue.yaml carries rich per-paper metadata to seed the manifest.
**Missing — all six substantive pieces:** no store; no manifest; no fetch script;
the blanket `*.pdf` Large File Storage (LFS) rule is still in force; the pre-commit
hook gates filenames only; no source-provenance fields in the extraction schema.
**Migration inventory:** 11 PDFs in `input/sources/original-pdf/` (41 MB,
publisher-named files to be renamed to slugs), 6 PDFs in the study corpus dir
(27 MB, five pilots + marwick preprint), plus untracked extracted texts in output
dirs.

**Registration-integrity rationale (new since v0.1):** the OSF registration pins
commit `ee3fda3` / tag `osf-prereg-phase2-2026-07-20`. Any future third-party-content
purge would rewrite history and invalidate the hashes the public registration cites —
so "never need a purge again" is now a hard requirement, which the out-of-tree store
satisfies by construction.

**Target structure:**

```text
~/corpora/llm-reproducibility/            # the store, out of tree
  <slug>/                                 # flat, one dir per paper slug
    vor.pdf  preprint.pdf  supplement-*.pdf  extracted.txt  meta.json

repo:
  corpus/
    README.md                             # entry point: architecture, CORPUS_ROOT,
                                          # fetch recipe, index of all manifests
    development-manifest.yaml             # the 11 pre-study papers
    store -> ~/corpora/llm-reproducibility  # gitignored convenience symlink
                                          # (safe even if committed: git stores the
                                          # path string, never the content)
  studies/open-science-compliance/corpus/
    manifest.yaml                         # 5 pilots now; census entries appended
    queue.yaml                            # unchanged — workflow state, churns
  scripts/fetch-corpus.py                 # --manifest <path>; one schema, any manifest
```

Principle: **manifest = stable citable record of a corpus; queue = workflow state** —
side by side per study, never merged. Store stays flat by slug (slugs are
project-unique), so `CORPUS_ROOT/<slug>/` resolves without knowing the study.

**Build order and effort** (items 1–4 **and 7** are census blockers — item 7
promoted per the 2026-07-24 review, D-9: census acquisition will pour 100–200
manually acquired closed-access PDFs into what would otherwise be a single-copy
store; 5–6 and 8 trail; ≈1 day total; no Large Language Model (LLM) API spend —
Unpaywall/CrossRef are free public APIs):

| # | Work item | Effort |
|---|---|---|
| 1 | Create store; migrate all 17 papers (PDFs + extracted texts) **copy-then-verify — originals deleted only after item 7 lands**; transitional symlinks; verify pipeline paths | ~1 h |
| 2 | Manifest schema **+ `meta.json` schema** + populate all holdings (sha256 everything; metadata from queue.yaml/CrossRef); `meta.json` written after this item defines both schemas (D-10) | ~1–2 h |
| 3 | `fetch-corpus.py` (Unpaywall resolution, checksum verify, closed-item report estimating the manual queue; politeness: ≤1 req/s, exponential backoff, `mailto`/User-Agent + Unpaywall email param; ScienceDirect 403 manual path stated in-spec) | ~half day |
| 4 | Narrow LFS to own-artefact dirs; pre-commit gate on new PDF/txt outside whitelist | ~30 min |
| 5 | reproduction-assessor prompt updates (fetch-with-checksum default; store/scratch destinations; log URL+hash) — §8 implementation change, rides the post-build regression gate | ~1 h |
| 6 | Additive schema bump v2.6→v2.7: `source_file` + `source_sha256` in extraction metadata | ~30 min |
| 7 | **CENSUS-BLOCKING (promoted 2026-07-24):** rsync script to rpi-server (drive-mount check per network guardrails) + **verify `~/corpora/` falls inside an actual backup scope** — configuration, not assertion | ~30 min |
| 8 | CLAUDE.md PDF-handling update + cross-references | ~15 min |

**EXECUTED 2026-07-24 — items 1–4, 7, and 8 complete:** store live at
`~/corpora/llm-reproducibility/` (16 papers, 28 manifest-listed files, 71.7 MB,
every copy sha256-verified against its original; originals retained in place —
copy-then-verify); both manifests written and `verify` passes 28/28;
`fetch-corpus.py` operational (verify/fetch/report/gen-meta; meta.json generated
for all 16 papers); LFS narrowed to own-artefact scopes (existing LFS files
re-verified under the new patterns); pre-commit corpus gate installed and
block-tested; first QNAP sync complete (44 files both sides, mount-verified).
Remaining: items 5 (reproduction-assessor prompts) and 6 (schema v2.7
source-provenance fields) ride the Phase 1 build. **No automated sync schedule
exists** — run `scripts/sync-corpus.sh` after each acquisition session.

`meta.json` is **machine-generated** by `fetch-corpus.py` as a per-paper projection
of the canonical manifest plus store-local facts (file inventory, acquisition
method, licence-evidence URL) — never hand-maintained; the git manifest is
canonical (D-10: two hand-maintained records of the same facts is the drift
pathology the routing design just engineered out of the instrument layer).
**Manual-acquisition budget:** planning range 40–70% of the ~280-paper frame
closed-access → ~110–200 papers ≈ **4–10 h of Shawn's time** via library proxy,
unless the Elsevier TDM route (decision 5) lands.

**Decision log (2026-07-23):**

1. Store location in-repo vs out-of-tree — **CONFIRMED out-of-tree (Shawn,
   2026-07-24)** (registration-integrity argument above; public repo; clones can
   never be complete anyway), with the manifest + fetch script providing
   one-command rebuild and the gitignored symlink providing in-tree ergonomics.
2. Path mechanism — **AGREED (Shawn):** `corpus_root` key in manifest + env-var
   override + transitional symlinks from the old gitignored paths, retired after the
   census tooling is proven.
3. Manifest home — **CONFIRMED (Shawn, 2026-07-24):** study-scoped manifests
   beside each study's queue, plus root `corpus/README.md` as the index
   (structure above).
4. Timing — ~~HOLD (Shawn, 2026-07-23)~~ **CLEARED (Shawn, 2026-07-24):**
   routing design signed off at v0.2.2; execution of census-blocking items
   1–4 + 7 approved.
5. Elsevier text-and-data-mining (TDM) route (added 2026-07-24, review E-2) —
   **IN PROGRESS (Shawn, 2026-07-24):** API key requested from
   dev.elsevier.com the same day. Key storage convention: variable
   `ELSEVIER_API_KEY_TDM` in `~/personal-assistant/.env` (gitignored;
   target-suffixed per the Zotero credential convention; value never in any
   repo or chat transcript). Note the entitlement nuance: the free academic
   key alone returns metadata/abstracts/open-access text — **closed full text
   requires the institutional-subscription path** (requests from campus/VPN IP
   space, or an Elsevier-issued institutional token `inst_token`), plus MQ
   actually subscribing to JAS. First test once the key is stored: one known
   closed JAS article via the Article Retrieval API from campus; if full text
   returns, the TDM leg is viable. Also verify the response format — the API
   may return XML/JSON full text rather than the typeset PDF, which has
   implications for the page-anchored `location` fields the extraction
   workflow prefers.

## Implementation checklist (v0.1, superseded by the scoped build order above)

1. Create the store; move existing PDFs/extracted texts from
   `studies/*/corpus/pdfs/`, `input/sources/`, and outputs dirs; add symlinks or
   `CORPUS_ROOT` config; confirm pipeline paths still resolve.
2. Write manifest schema + populate from queue.yaml and existing holdings (hashes).
3. Write `fetch-corpus.py` (Unpaywall resolution, checksum verify, closed-item list).
4. Narrow `.gitattributes` LFS scope; extend the pre-commit hook.
5. Update reproduction-assessor prompts: store/scratch destinations;
   fetch-with-checksum default; log URL+hash.
6. Add source-file+hash fields to extraction metadata (schema note).
7. Sync: rsync script to rpi-server; add store to backups.
8. Update CLAUDE.md (PDF handling section) and the modernisation plan cross-reference.

Estimated effort: manifest + fetch script ≈ half a day of agent work; migration and
guardrails smaller. Must land before the JAS census acquires papers at scale.
