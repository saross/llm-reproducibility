# Labelled copy: herskind-riede-2024 attempt 04, for the reviewer-only pilot

**This is a pilot copy, not study data.** Study reporting and export read
an attempt's adjudicated result under
`studies/open-science-compliance/outputs/<slug>/reproduction/`, and never
this folder. Nothing here enters the study's coverage figures.

## What it is

`herskind-riede-2024/reproduction/attempt-04/` is a byte-identical copy of
`studies/open-science-compliance/outputs/herskind-riede-2024/reproduction/attempt-04/`
as committed at `ad0d50f` (339 files; artefact state
`f549d2f5121199bb…`, equal to the original's). It was copied on 2026-10-30
for gate 1.3.2's criterion 4: the reviewer-only pilot, one run of the
review-only mode (`reproduction-review.workflow.js`) with a fresh
`adversarial-reviewer` and no executor.

## Why a copy

Shawn's choice (2026-10-30): the pilot reviews a labelled copy, so that the
original attempt's review, rulings, and adjudicated result stay untouched.
The review-only mode is built to replace a review of record; running it on
this copy exercises that path (the earlier review and the adjudicated
result move to `superseded/<workflow run>/` inside the copy) without
changing the study's record.

## What may change here

Only the lane's own commands write into this copy, as a review-only run
does: the gate step's `check-attempt` (the gate report), `audit-run` (the
run audit, its predecessor kept under `superseded/`), `rule-flags`,
`persist-results`, and `adjudicate`. Never edit the copy's reviewable
files by hand: the review-only mode refuses an attempt whose state differs
from the one its executor's run audit cleared.

## Records

The run configuration, the Application Programming Interface (API) gate
brief, the pre-run review, the run audit, and the results are kept in
`studies/open-science-compliance/outputs/validation/gate-1-3-2-reviewer-pilot/`.
The design is in `wiki/planning/reproduction-gate-1-3-design.md`, "The
review-only mode as designed".
