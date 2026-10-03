#!/usr/bin/env bash
# ===========================================================================
# run-all.sh — full pipeline for the Dye et al. (2023) reproduction, attempt 02
#
# Runs, in order, inside the Docker image llmr-dye-et-al-2023-attempt-02:
#   1. scripts/check-labels.R      read-only transcription/label check
#   2. run-analysis.R              the authors' transcribed code (supplement
#                                  sections 3-10), batch wrapper
#   3. scripts/verification-aids.R R1 verification aids (not authors' code)
#   4. scripts/compare.R           value-level comparison -> comparisons/values/
#
# Usage (host):
#   docker build -t llmr-dye-et-al-2023-attempt-02 .
#   docker run --rm --network none --user "$(id -u):$(id -g)" \
#       -v "$PWD":/project -w /project llmr-dye-et-al-2023-attempt-02
# ===========================================================================
set -euo pipefail
cd /project
mkdir -p outputs/logs
# Verify the analysis input before anything runs (plan data_retrieval_plan).
echo "02cf52d4ace408b6329e69e7a0e4bd457084ae9605f2fa5eccc2abad20ab9051  data/beads-1.csv" \
    | sha256sum -c - | tee outputs/logs/input-checksum.txt
for step in scripts/check-labels.R run-analysis.R scripts/verification-aids.R scripts/compare.R; do
    echo "=== $(date -u +%Y-%m-%dT%H:%M:%SZ) start ${step}"
    Rscript "${step}"
    echo "=== $(date -u +%Y-%m-%dT%H:%M:%SZ) end ${step}"
done
