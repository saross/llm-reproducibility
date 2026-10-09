# Operator evidence run: dye section 7 (ledger ruling L9)

**Run:** 2026-10-09, by the drafting session, for ledger targets DYE-T01 and
DYE-T02. Not a pipeline output: no agent and no model call took part.

**What ran.** The authors' section 5 and section 7 code ran in order, as the
deterministic transcriptions of supplement-1.pdf held in
`dye-et-al-2023/reproduction/attempt-02/authors-code-raw/`. Both files are
byte-identical to the audit's originals: sha256 `b26be721…bcda623173` and
`98868ffb…4c19c44488` (md5s in `run.log`). The image was the kept
`llmr-dye-et-al-2023-attempt-02` (ArchaeoPhases 1.8, R 4.2.3), run with
`--network none`, with the code and data mounted read-only.

**The one mechanic** sits in `wrapper.R`, outside the authors' files.
Section 7 reads `https://tsdye.online/AP/beads-1.csv`, and the wrapper
redirects that read to the local copy of the same file (sha256
`02cf52d4…ab9051`). It does so with a global `read_oxcal` that calls the
package's own function.

**Result** (`run.log`): BE1-Cowrie(oFD)BE1-Disc = 0.999667 (1.00 at 2 dp);
BE1-Amethyst(oFD)BE1-Disc = 0.867167; BE3-Amber(oFD)BE1-Amethyst =
BE3-Amber(oFD)BE1-Cowrie = 1. These equal shakedown attempt-02's T05 and T06
values, which came from the path-edited copies.

**Command:**

```bash
docker run --rm --network none --user "$(id -u):$(id -g)" \
  -v <attempt-02>/authors-code-raw:/code:ro -v <attempt-02>/data:/data:ro \
  -v <this directory>:/work:ro --entrypoint Rscript \
  llmr-dye-et-al-2023-attempt-02 /work/wrapper.R
```
