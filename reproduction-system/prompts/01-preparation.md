# Preparation Prompt — Session R-A

**Version:** 1.3
**Last Updated:** 2026-10-05 (v1.3: §1.0.2 provenance anchors, execution
snapshots, generated code, and conversion evidence, after the cross-model
review of PR #7; v1.2, 2026-10-04: §1.0.2 authors' code manifest; §3.3–3.4
no longer invite restructuring the authors' code)
**Session:** R-A (Preparation)
**Skill:** reproduction-assessor
**Prerequisite:** Approved reproduction plan from Session R-Plan

---

## Your Task

Acquire all materials, construct the Docker environment, and adapt scripts for batch execution. By the end of this session, the reproduction should be ready to run.

**Input:** Approved reproduction plan, paper PDF, code repository

**Output:** Working Dockerfile, batch-executable analysis script(s), all data files, output directory structure

---

## Critical Rules

1. **Follow the approved plan.** Execute the steps from the R-Plan session. If you encounter unexpected issues, adapt and document.
2. **NO algorithmic modifications.** Wrapper scripts reorganise execution flow and add output capture. They must NEVER change statistical methods, parameters, data filtering, or model specifications.
3. **Document everything.** Every modification, every failed build attempt, every workaround. This feeds into the log.md artefact.
4. **Test the build.** The Docker image must build successfully before ending this session.
5. **Work autonomously within the session.** Complete all sub-phases without stopping for confirmation.

---

## Procedure

### Phase 1: Material Acquisition

#### 1.0 Fetch with checksum — the default

**Hash everything you fetch, at the moment you fetch it, and record the hash
with the URL it came from.** This is not bookkeeping: a reproduction whose
inputs are unidentified cannot distinguish "the analysis is irreproducible"
from "the data changed under us". Personal servers and `latest`-style
repository endpoints both serve mutable content, and neither announces a
change.

```bash
sha256sum <file>          # record the full 64-hex digest, not a prefix
```

For a git clone the commit hash is the equivalent identifier — record it
(`git rev-parse HEAD`) and note whether the repository was pinned to a tag or
release, or taken from a moving branch.

Record each fetch in `log.md` under **Materials Acquired** (URL or DOI,
retrieval date, digest, destination) as you go. Reconstructing this at the end
of the session does not work — by then the retrieval dates are guesses.

**If an artefact cannot be hashed** (streamed through a portal, hand-assembled
from a PDF), say so explicitly in that row rather than leaving it blank. A
stated gap is evidence; a blank cell is ambiguous between "not applicable" and
"not done".

#### 1.0.1 Destinations — store, attempt directory, scratch

Three destinations, and the distinction matters because one of them is
governed by a hard rule:

| Destination | What goes there | Notes |
|---|---|---|
| **Corpus store** (`~/corpora/llm-reproducibility/<slug>/`, reachable in-repo via the gitignored `corpus/store/<slug>/` symlink) | The paper itself and its supplements — publisher content | **Never** into git. The pre-commit corpus gate blocks third-party PDFs and extracted article text; do not work around it. Add new holdings to the corpus manifest with their hashes rather than leaving them loose. |
| **Attempt directory** (`outputs/{paper-slug}/reproduction/attempt-{NN}/`) | Author-released code and data that the reproduction actually consumes, plus everything this session produces | This is the citable artefact set. Author-released materials under an open licence may live here; publisher content may not. |
| **Scratch** (the session scratchpad directory) | Build intermediates, failed download attempts, throwaway probes | Never referenced by the artefact set. Anything a reader would need to see must be promoted out of scratch before the session ends. |

When in doubt about whether an artefact is publisher content or an
author-released material, treat it as publisher content — the recoverable
error is an unnecessary store entry, not a licence breach in public history.

#### 1.0.2 Authors' code manifest — hash at retrieval, run byte-identical

Registrant ruling (2026-10-04): the authors' code files are hashed at
retrieval, and the copies the run executes must be byte-identical. Any
difference is a declared wrapper or a flagged edit.

- **At retrieval,** add each authors' file to `authors-code-manifest.json`
  at the attempt root (schema
  `reproduction-system/schemas/authors-code-manifest.json`). Record its id
  (its path in the deposit), sha256, source, version, and retrieval time.
  Keep a pristine `local_copy` that is never edited; if its licence does not
  allow it in git, hold it out (`.gitignore` plus a fetch script with
  sha256 checks), as §1.0.1 requires for publisher content. For code that
  exists only as printed listings, record the transcription under
  `derivation`; a transcription is always flagged, because the gate can show
  the source's identity but not the transcription's fidelity to the page.
- **Anchor each original to a record you did not write.** Your manifest
  alone cannot show that a file was unedited when you hashed it, so the gate
  verifies an `anchor` against a committed record:
  - `evidence-pack`: for a deposit file (a Zenodo zip or single file), name
    the committed evidence pack, the record id of the version the registry
    selects (AP-12), and the file key. The gate checks the deposit file you
    kept (`archive.path` or `local_copy`) against the checksum the record
    publishes.
  - `corpus-manifest`: for a file in the corpus store (a publisher
    supplement, or a transcription's source), name the committed corpus
    manifest, this paper's entry, and the filename. An archive held in the
    store is named `$CORPUS_ROOT/<slug>/<file>`. It verifies only a journal
    supplement of a paper whose registry holds its principal artefact in the
    supplement; anything else is flagged. Anchor a deposit kept in the store
    through its evidence-pack record, which carries the version binding.
  - `git`: repository, commit, path, and blob id. The gate checks the blob id
    against the bytes, but a reviewer must confirm it at the remote, so it is
    flagged.
  - `none`, with a reason, when no independent record exists. The result is
    flagged, never `identical`.
- **Run the authors' files unmodified.** Paths, seeds, output capture, and
  error handling belong in your own files, listed under `wrappers` with a
  role. Never edit an authors' file, and never inline its code into a
  wrapper.
- **An unavoidable edit is declared** under `declared_edit`, with the
  targets it affects. It is flagged for a human ruling.
- **Snapshot the execution boundary.** The run mounts the attempt directory,
  so its code files are what the run can execute. Immediately before the
  container run: `venv/bin/python scripts/reproduction-lane.py snapshot-code
  <attempt dir> --phase pre`; immediately after: the same with
  `--phase post`. Change no code file afterwards. Nothing is exempt, including
  `outputs/`: declare any code file the run itself writes as a wrapper with
  role `generated`. No wrapper may load generated code.
- **A format conversion needs machine-readable evidence.** The wrapper
  declares the conversion it performs (`conversion: {"input", "output"}`).
  Its `value_identity_check` names a JSON record: `{"check":
  "value-identity", "result": "identical", "converter": {"path", "sha256"},
  "input": {"path", "sha256"}, "output": {"path", "sha256"},
  "values_compared": n, "values_total": n}`. The record must name this
  wrapper at its current sha256 and exactly the declared input and output,
  match the files as they are, and cover every value. Anything else is
  flagged.
- **Check:** `venv/bin/python scripts/reproduction-lane.py check-code <attempt dir>`.
  It fails on an undeclared difference, on code that changed after or during
  the run, and on any code file that is neither an authors' file nor a
  declared wrapper. `pass` means only that every code file is accounted for:
  flags still need a human ruling, and a repaired result never counts toward
  coverage.

#### 1.1 Code Retrieval

- **GitHub repository:** `git clone {url}` — record the commit hash (`git rev-parse HEAD`) and whether it is a tag/release or a moving branch
- **Zenodo deposit:** Download via DOI or direct URL — record the version *and* the file digest; Zenodo DOIs can be version-specific or concept-level, and the concept DOI resolves to whatever is newest
- **Journal supplement:** Download — record access method and any barriers
- **Personal server:** Download, hash, and note persistence risk explicitly

**Document access barriers.** If programmatic access fails (HTTP 403, authentication required), document this as a FAIR/machine-actionability finding.

#### 1.2 Data Retrieval

- Download all required data files and hash each one (§1.0)
- Verify file sizes and row/column counts against expectations
- Record data provenance in `log.md`: URL or DOI, access date, SHA-256, destination
- If data is on an unreliable host, make a local copy — and hash it before *and* after copying, so a truncated transfer is caught here rather than surfacing later as an analytical discrepancy

#### 1.3 Supplement Processing

For papers with code in supplement PDFs:

- Extract R code sections (numbered blocks, inline listings)
- Track code block numbering and dependencies
- Watch for PDF line-wrapping that breaks string literals
- Verify column names and indices against actual data files

### Phase 2: Docker Environment Construction

Follow the Dockerfile Strategy framework from the skill (§A).

#### 2.1 Author-Provided Dockerfile (Types A, B)

1. Read the Dockerfile — understand the base image, dependencies, and build steps
2. Attempt to build: `docker build -t reproduction-{slug} .`
3. If build fails:
   - Read error output carefully
   - Fix the specific issue (typo, missing package, version conflict)
   - Document the fix
   - Rebuild
4. Expect 0-2 iterations for author Dockerfiles

#### 2.2 Constructed Dockerfile (Types B, C)

1. Determine R version:
   - From renv.lock, sessionInfo(), paper text, or publication date
   - Use `rocker/r-ver:{version}` as base image
2. Add system dependencies:
   - Consult the Common R System Dependencies table in the skill
   - Install via `apt-get install -y --no-install-recommends`
3. Install R packages:
   - From CRAN: `install.packages(c('pkg1', 'pkg2'))`
   - From GitHub: `remotes::install_github('user/repo')`
   - From r-universe: `install.packages('pkg', repos='https://{user}.r-universe.dev')`
4. Build and iterate:
   - Attempt build
   - Read error output for missing system libraries
   - Add missing deps
   - Rebuild
   - **Expect 1-3 iterations** for transitive dependencies

**For common system dependency mappings:**
→ Consult `references/dockerfile-patterns.md`

#### 2.3 renv Pathway

If the repository includes an renv.lock:

1. Copy renv.lock into the Docker image
2. Install renv: `RUN R -e "install.packages('renv')"`
3. Restore: `RUN R -e "renv::restore()"`
4. System deps still needed (renv manages R packages, not system libraries)
5. R version mismatch between renv.lock and Docker image produces a warning, not usually a failure

### Phase 3: Script Adaptation

Follow the Script Adaptation Strategy framework from the skill (§B).

#### 3.1 Batch-Ready Scripts

No adaptation needed. Verify they run with `Rscript script.R`.

#### 3.2 Literate Programming (Rmd/Qmd)

Use `rmarkdown::render()` or equivalent:

```r
Rscript -e "rmarkdown::render('analysis.Rmd', output_dir='outputs/')"
```

Some Dockerfiles render during build (`RUN R -e "rmarkdown::render(...)"`). This is valid — the build IS the reproduction.

#### 3.3 Interactive Scripts → Wrapper

Write a wrapper script (`run-analysis.R`) that:

1. Sources the original analysis files unmodified (never edits or inlines
   them; §1.0.2)
2. Parameterises repeated operations (loops instead of manual re-runs)
3. Adds output capture (`pdf()`, `ggsave()`, `write.csv()`, `sink()`)
4. Creates output directories
5. Runs non-interactively from start to finish

**The cardinal rule:** The wrapper changes HOW the code runs, not WHAT it computes.

**For wrapper script patterns and examples:**
→ Consult `references/wrapper-script-patterns.md`

#### 3.4 Incremental Code Blocks → Assembled Script

For supplement code in numbered sections:

1. Read all sections sequentially
2. Transcribe each section verbatim, one file per section, and record the
   transcription in the manifest (§1.0.2)
3. Track variable state (list indices, accumulated objects)
4. Verify column names against actual data (PDF line-wrapping breaks strings)
5. Keep the authors' indexing and construction as printed: restructuring
   (for example, positional to named) is an edit to the authors' code
6. Test incrementally

### Phase 4: Output Directory Setup

Create the standard artefact directory structure:

```text
outputs/{paper-slug}/reproduction/attempt-{NN}/
├── Dockerfile
├── run-analysis.R  (or wrapper script)
├── outputs/        (for generated files)
└── data/           (if data needs local copy)
```

### Phase 5: Verification

Before ending this session:

1. Docker image builds successfully
2. Analysis script syntax is valid (`Rscript --vanilla -e "parse('run-analysis.R')"`)
3. All data files are in place
4. Output directory exists
5. **Every fetched artefact has a URL-and-digest row in `log.md`** — count the rows against the files you actually acquired; a missing row is a provenance gap, and it is cheap to close now and impossible to close later
6. **No publisher content sits inside the repository** — paper PDFs and extracted article text belong in the corpus store (§1.0.1)
7. **`check-code` passes** — every executed authors' file is byte-identical to its retrieved original, or its edit is declared (§1.0.2)

---

## Handoff

```text
Session R-A complete for {paper-slug}

Completed:
- Materials acquired: {code source, data source, supplements}
- Docker image: {image name, base image, N build iterations}
- Script adaptation: {none / wrapper / assembled, N lines}
- Modifications: {list of changes made}

Environment: {Docker base image, key packages}
Build iterations: {N}

Materials provenance: {N} artefacts fetched, {N} with URL + SHA-256 recorded
  ({state any unhashable artefact and why})

Artefact persistence check:
- [ ] Dockerfile saved to outputs/{paper-slug}/reproduction/attempt-{NN}/
- [ ] Wrapper script saved to outputs/{paper-slug}/reproduction/attempt-{NN}/
- [ ] Source data copied to outputs/{paper-slug}/reproduction/attempt-{NN}/
- [ ] Output directory created: outputs/{paper-slug}/reproduction/attempt-{NN}/outputs/
- [ ] Materials Acquired table in log.md complete (URL/DOI + digest + destination per artefact)
- [ ] authors-code-manifest.json written at retrieval; `check-code` passes
- [ ] Publisher content in the corpus store, not the repository

Next session: R-B (Execution and Verification)
Ready to continue when you are.
```

---

## Common Pitfalls

- **Modifying analytical logic.** The most critical error. Wrapper scripts must be strictly non-algorithmic.
- **Not documenting failed build attempts.** These attempts are valuable for the log.md artefact and for future reproductions.
- **Forgetting output directories.** `dir.create("outputs", showWarnings = FALSE)` at script start.
- **Hardcoded paths.** Use relative paths or `here::here()`. Add `.here` sentinel for volume-mounted directories.
- **Missing `.here` file.** Volume-mounted directories lack `.git`, so the `here` package cannot find the project root. Touch `.here` in the working directory.
- **Special characters in filenames.** Ampersands, spaces, and other special characters cause Docker mount issues. Rename files for compatibility.

---

## Decision Framework References

- **SKILL.md** §A — Dockerfile Strategy
- **SKILL.md** §B — Script Adaptation Strategy
- **SKILL.md** §D — Compute Resource Allocation
- **references/dockerfile-patterns.md** — Rocker hierarchy, common deps, iterative build
- **references/wrapper-script-patterns.md** — Interactive-to-batch conversion patterns
