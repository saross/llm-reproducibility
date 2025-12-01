# Variability Test Run

Execute the next pending run from the variability test queue.

## Instructions

1. **Read the queue** at `input/variability-queue.yaml` to find the next pending run
   - Look for `current_paper` and `current_run` fields
   - Or find first paper with `status: in_progress` and first run with `status: pending`

2. **Load the research-assessor skill** using the Skill tool

3. **Create output directory**: `outputs/variability-test/{paper-slug}/{run-id}/`

4. **Execute full extraction pipeline** (Passes 0-7):
   - Read the source PDF
   - Extract evidence, claims, implicit arguments, methods, protocols, research designs
   - Save to `extraction.json`

5. **Execute full assessment pipeline** (Passes 8-10):
   - Pass 8: Classification → `assessment/classification.json`
   - Pass 8.5: Quality gating → `assessment/track-a-quality.md`
   - Pass 9: Cluster assessments → `assessment/cluster-1-foundational-clarity.md`, `cluster-2-evidential-strength.md`, `cluster-3-reproducibility.md`
   - Pass 10: Final report → `assessment/credibility-report.md`

6. **Update the queue** (`input/variability-queue.yaml`):
   - Mark current run as `completed`
   - Add counts and aggregate_score
   - Update `current_run` to next pending (or `current_paper` if paper complete)

7. **Run validation**: `./scripts/validate-run-uniqueness.sh outputs/variability-test/{paper-slug}/`

8. **Report completion** with:
   - Paper and run ID
   - Item counts (evidence, claims, implicit_arguments)
   - Aggregate score
   - Next pending run (for user reference)

## Important

- This is a FRESH extraction - do not reference any previous runs
- Use the research-assessor skill for schema compliance
- Follow autonomous execution mode - do not stop for confirmation between passes
- After completion, user should run `/clear` before next run

## Queue Location

`input/variability-queue.yaml`

## Output Location

`outputs/variability-test/{paper-slug}/{run-id}/`
