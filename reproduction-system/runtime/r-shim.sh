#!/bin/sh
# Reproduction lane exec shim (gate 1.3, F1).
#
# run-container mounts this file read-only over the image's $R_HOME/bin/R
# and over every byte-identical copy of it on the PATH, and mounts the
# image's own front-end script at /lane/R.orig. Every start of the R
# interpreter through the front end (Rscript, R -f, system() children,
# PSOCK workers, callr) therefore passes through here first.
#
# The shim writes one EXEC event to the authoritative stream, which is PID
# 1's stderr: the Docker log pipe, held by the daemon on the host. It then
# execs the original front end, so the R process keeps this PID and inherits
# the per-process token minted here. The hook's events carry the same token,
# and the census pairs on it (spec §8). PIDs alone can repeat in a long run
# once the PID space wraps (Fable's specification review, D-2).
#
# Event: LANE1 <nonce> <token> <pid> <ppid> 0 EXEC <tab> stdin <tab> cwd
#        <tab> args...
# Strings are hex-encoded UTF-8, so tabs and newlines in arguments (a
# multi-line -e expression) cannot break the line framing. Sequence 0 is
# the shim's; the hook counts from 1 in the same process.
#
# Fails closed: if the stream cannot be written, R is not started.

hex() { printf '%s' "$1" | od -An -v -tx1 | tr -d ' \n'; }

# Where standard input comes from: a script fed on stdin (R < file) is
# code that no load event covers, so the gate needs to know.
if [ -t 0 ]; then stdin=tty
elif [ -p /dev/stdin ]; then stdin=pipe
elif [ -f /dev/stdin ]; then stdin=file
else stdin=other
fi

token="$$-$(od -An -N8 -tx1 /dev/urandom | tr -d ' \n')"
export LANE_PROC="$token" LANE_PROC_PID="$$"

tab=$(printf '\t')
fields="$stdin$tab$(hex "$PWD")"
for arg do fields="$fields$tab$(hex "$arg")"; done
# One write of at most 4,096 bytes is atomic on the pipe, so an over-long
# argv is cut rather than wrapped, and marked: the hex of "<truncated>".
if [ "${#fields}" -gt 3800 ]; then
    fields="$(printf '%.3800s' "$fields")${tab}3c7472756e63617465643e"
fi

printf 'LANE1 %s %s %s %s 0 EXEC\t%s\n' "${LANE_RUN_NONCE:-none}" "$token" "$$" "$PPID" \
    "$fields" \
    > /proc/1/fd/2 || {
    echo "lane shim: the event stream is not writable; refusing to start R" >&2
    exit 125
}
exec /lane/R.orig "$@"
