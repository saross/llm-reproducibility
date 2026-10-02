# Supplements as scoring inputs (dated protocol note, 2026-10-02)

**Status:** adopted by the registrant (Shawn) on 2026-10-02, during the E8-v2
reference adjudication (Option A; `outputs/validation/e8-v2-rederivation/adjudication-log.md`).
**Governance:** recorded here and in the plan decision log. No Open Science
Framework (OSF) amendment, because this is a reading of the lodged text
(below) rather than a departure from it. The F-010 ruling used the same
route.

## Ruling

Census scoring spawns receive the paper's **published supplementary files**
alongside the paper PDF.

**Rationale:** the adjudication's forward principle AP-2 holds that "paper"
includes its published supplement. The research-surface rule assesses the
artefacts reachable from the published paper. A census blind to supplements
cannot see the defects of artefacts hosted in them. Two examples from the
first sittings:

- a personal-server data link that exists only inside supplement code
  (AP-3);
- code published only as text inside a supplement PDF (AP-9).

## Reading of the lodged text

Amendment 2 §2 specifies that scoring spawns receive "the paper source, the
pushed instruments, and a per-paper verified evidence pack". This note reads
"the paper source" as the published paper together with its supplementary
files.

The benchmark workflow's exclusion entered with the original benchmark
harness (commit `d34edd9`, rescued into the repository 2026-08-03), with no
recorded protocol decision behind it. Its wording is: "The paper PDF is the
sole paper source: supplementary files are deliberately not provided"
(`protocol/validation/fair-benchmark-arm.workflow.js:100`).

## Consequences for the completed benchmark

The 2026-08-17 benchmark and effort-study arms are **not re-run**. Every
governed spawn in those cycles read only `vor.pdf`.

E8-v2 reference items whose adjudicated score depends on supplement contents
carry the beyond-instrument tag `input`. The gates then report concordance
with and without tagged items, so the arms are not graded on evidence they
were never given.

## Pre-census implementation

These items are tracked in the plan's pre-census item.

1. **Supplement collection in corpus curation.** Collect every census
   paper's published supplementary files into the corpus store as
   `supplement-N.<ext>`. On 2026-10-02 only 1 of the 16 papers in the store
   had one.
   - Some publishers block scripted download (ScienceDirect returned HTTP
     403 in dye-et-al-2023 reproduction attempt-01). Those files come by
     manual or institutional download, or through the harvester's planned
     rendering step.
   - Record each paper's supplement status as none, collected, or
     unobtainable. An unobtainable supplement is itself a finding.
2. **Readable formats.** Scoring spawns have only read-only tools.
   - Archives and spreadsheets need a recorded curation conversion before
     spawns can read them.
   - AP-9 (I1) is still judged on the format as *served*, not on the
     converted copy.
3. **Workflow and argument builder.**
   - Supply the supplement paths to each scoring spawn and replace the
     exclusion line in the prompt.
   - Require full reads of the supplements, verified by the reconciler as
     for the evidence pack: a read whose every attempt errored is not a
     read.
   - The corpus store is already on the reconciler's allowed-prefix list.
4. **Pre-census check.** The census input will then differ from what the
   benchmark validated. Before census, run the selected arm on the five
   pilots with supplements (15 spawns) under the standing API review gate.
