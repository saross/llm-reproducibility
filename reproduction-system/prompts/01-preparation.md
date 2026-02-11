# Preparation Prompt — Session R-A

**Version:** 1.0
**Last Updated:** 2026-02-10
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

#### 1.1 Code Retrieval

- **GitHub repository:** `git clone {url}` — note the commit hash
- **Zenodo deposit:** Download via DOI or direct URL — note the version
- **Journal supplement:** Download PDF — note access method and any barriers
- **Personal server:** Download and note persistence risk

**Document access barriers.** If programmatic access fails (HTTP 403, authentication required), document this as a FAIR/machine-actionability finding.

#### 1.2 Data Retrieval

- Download all required data files
- Verify file sizes and row/column counts against expectations
- Note data provenance (URL, DOI, access date)
- If data is on an unreliable host, make a local copy

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

1. Sources or incorporates the original analysis code
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
2. Track variable state (list indices, accumulated objects)
3. Verify column names against actual data (PDF line-wrapping breaks strings)
4. Use named construction for robustness (instead of positional indexing)
5. Test incrementally

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

Artefact persistence check:
- [ ] Dockerfile saved to outputs/{paper-slug}/reproduction/attempt-{NN}/
- [ ] Wrapper script saved to outputs/{paper-slug}/reproduction/attempt-{NN}/
- [ ] Source data copied to outputs/{paper-slug}/reproduction/attempt-{NN}/
- [ ] Output directory created: outputs/{paper-slug}/reproduction/attempt-{NN}/outputs/

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
