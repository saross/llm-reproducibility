#!/bin/bash
# Sync the out-of-tree corpus store to the QNAP array on rpi-server.
# Corpus-management-plan v0.2.1 item 7 (census-blocking): the store holds
# manually acquired closed-access PDFs that cannot be re-fetched, so a second
# copy must exist before census acquisition begins.
#
# Guardrails (network-resources.md): verify the QNAP is mounted BEFORE writing;
# never attempt to mount it (LUKS requires interactive passwords); bulk data
# goes under /mnt/qnap/, never the Pi's home directory.
#
# Usage: ./scripts/sync-corpus.sh
# NOTE: no automated schedule exists — run after each acquisition session.

set -euo pipefail

STORE="${CORPUS_ROOT:-$HOME/corpora/llm-reproducibility}"
REMOTE="rpi-server"
DEST="/mnt/qnap/corpora/llm-reproducibility"

if [ ! -d "$STORE" ]; then
    echo "❌ store not found at $STORE" >&2
    exit 1
fi

echo "Checking QNAP mount on ${REMOTE}..."
if ! ssh "$REMOTE" 'mount | grep -q qnap'; then
    echo "❌ /mnt/qnap is NOT mounted on ${REMOTE} — flag to Shawn (interactive" >&2
    echo "   LUKS unlock required); do not attempt to mount it remotely." >&2
    exit 1
fi

echo "Syncing ${STORE}/ -> ${REMOTE}:${DEST}/"
ssh "$REMOTE" "mkdir -p '$DEST'"
rsync -a --info=stats2 --human-readable "$STORE"/ "$REMOTE":"$DEST"/

echo "Verifying file count..."
local_count=$(find "$STORE" -type f | wc -l)
remote_count=$(ssh "$REMOTE" "find '$DEST' -type f | wc -l")
if [ "$local_count" -eq "$remote_count" ]; then
    echo "✅ sync complete: ${local_count} files on both sides"
else
    echo "⚠️  count mismatch: local=${local_count} remote=${remote_count}" >&2
    exit 1
fi
