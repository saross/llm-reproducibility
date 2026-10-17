#!/bin/bash
# =============================================================================
# run.sh -- lane entry point for herskind-riede-2024, reproduction attempt 04
#
# Started by `reproduction-lane.py run-container ... --entry run.sh`, with the
# work copy mounted at the image's WORKDIR (/project). Two R processes:
#   1. run-analysis.R      runs the authors' S2.R unmodified and captures
#                          its objects under captured/;
#   2. verification-aids.R the labelled verification aids (ruling R1), in a
#                          separate process so that nothing they define can
#                          reach the authors' run.
# =============================================================================
set -euo pipefail
Rscript run-analysis.R
Rscript verification-aids.R
