#!/usr/bin/env bash
# =============================================================================
# fetch-held-out-inputs.sh — restore attempt-02's two git-excluded inputs
# =============================================================================
#
# PURPOSE
#   Operator addition (2026-10-04; shakedown human queue item 8, Shawn's
#   ruling: keep both files out of git and restore them by script). Two inputs
#   of this attempt are deliberately not committed (the repository is public):
#
#   - data/beads-1.csv — the authors' OxCal MCMC output. It carries no
#     licence; a byte-identical copy is already tracked at
#     ../attempt-01/beads-1.csv, so a second copy adds nothing.
#   - vendor/ArchaeoPhases_1.8.tar.gz — the CRAN archive tarball (GPL-3)
#     that the Dockerfile COPYs and verifies (Dockerfile line 59-61).
#
#   Each file is verified against the sha256 the executor recorded. An
#   existing file that passes is left alone, so the script is safe to re-run.
#
# USAGE
#   ./fetch-held-out-inputs.sh        # run from any directory
#   docker build -t llmr-dye-et-al-2023-attempt-02 .   # then build as usual
# =============================================================================

set -euo pipefail

here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

BEADS_SHA="02cf52d4ace408b6329e69e7a0e4bd457084ae9605f2fa5eccc2abad20ab9051"
BEADS_URL="https://tsdye.online/AP/beads-1.csv"
BEADS_TRACKED="${here}/../attempt-01/beads-1.csv"

AP_SHA="728a0d0c3a487e8f90b8c550a977a7678855d0c355a0347629d4a4afd5a5a801"
AP_URL="https://cran.r-project.org/src/contrib/Archive/ArchaeoPhases/ArchaeoPhases_1.8.tar.gz"

# Return success if file $1 exists and has sha256 $2.
sha_ok() {
    [[ -f "$1" ]] && echo "$2  $1" | sha256sum --check --status -
}

# Place a verified copy at $1 (expected sha256 $2), trying each source in
# turn: a local file path or an https URL.
restore() {
    local dest="$1" sha="$2"; shift 2
    if sha_ok "$dest" "$sha"; then
        echo "ok (already present): ${dest#"$here"/}"
        return 0
    fi
    mkdir -p "$(dirname "$dest")"
    local src tmp
    for src in "$@"; do
        tmp="$(mktemp)"
        if [[ "$src" == https://* ]]; then
            curl -fsSL "$src" -o "$tmp" || { rm -f "$tmp"; continue; }
        elif [[ -f "$src" ]]; then
            cp "$src" "$tmp"
        else
            rm -f "$tmp"; continue
        fi
        if sha_ok "$tmp" "$sha"; then
            mv "$tmp" "$dest"
            echo "restored from ${src}: ${dest#"$here"/}"
            return 0
        fi
        echo "checksum mismatch from ${src}; trying next source" >&2
        rm -f "$tmp"
    done
    echo "FAILED: no source gave a verified ${dest#"$here"/}" >&2
    return 1
}

restore "${here}/data/beads-1.csv" "$BEADS_SHA" "$BEADS_TRACKED" "$BEADS_URL"
restore "${here}/vendor/ArchaeoPhases_1.8.tar.gz" "$AP_SHA" "$AP_URL"
