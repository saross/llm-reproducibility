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
# stdin is tty, pipe, file, or other; for a script read from a pipe or file
# it is <kind>:<md5>:<bytes>:<hex text, for at most 1,024 bytes>. Strings
# are hex-encoded UTF-8, so tabs and newlines in arguments (a multi-line -e
# expression) cannot break the line framing. Sequence 0 is the shim's; the
# hook counts from 1 in the same process.
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

# When no option names the code R runs, a pipe or file on standard input is
# the script. The shim reads it to a file and records its md5 and size, and
# for a short script (at most 1,024 bytes, such as R CMD INSTALL's
# "tools:::.install_packages()") its text in hex, so the gate can bind it by
# content. R then reads the same bytes from that file, which is unlinked
# first and so leaves nothing behind. Options after --args are R's
# arguments to the script, not options, and are not scanned.
script=yes
case "${1:-}" in CMD|RHOME|--version) script=no ;; esac
for arg do
    case "$arg" in
        --args) break ;;
        -f|--file|--file=*|-e) script=no ;;
    esac
done
if [ "$script" = yes ] && { [ "$stdin" = pipe ] || [ "$stdin" = file ]; }; then
    copy=$(mktemp /tmp/lane-stdin-XXXXXX) && cat > "$copy" || {
        echo "lane shim: could not read the script on standard input" >&2
        exit 125
    }
    size=$(wc -c < "$copy" | tr -d ' ')
    text=
    [ "$size" -le 1024 ] && text=$(od -An -v -tx1 < "$copy" | tr -d ' \n')
    stdin="$stdin:$(md5sum < "$copy" | cut -d' ' -f1):$size:$text"
    exec 0< "$copy"
    rm -f "$copy"
fi

# The lane pins the hook through R_ENVIRON_USER (spec §8). A launcher that
# substitutes its own user environ file outranks the pin: callr writes one
# holding ours and then its own R_PROFILE_USER line (callr 3.7.5,
# make_environ). Such a process gets a copy of that file with the pin
# appended, so the hook loads and then sources the launcher's profile, which
# the pin saves as LANE_PARENT_PROFILE (the order the spec intends for
# callr). A process with no user environ file at all gets the lane's.
case "${R_ENVIRON_USER:-}" in
    /lane/Renviron) ;;
    "") export R_ENVIRON_USER=/lane/Renviron ;;
    *)
        if [ -f "$R_ENVIRON_USER" ]; then
            environ=$(mktemp /tmp/lane-renviron-XXXXXX) && {
                cat "$R_ENVIRON_USER"
                printf '\n# Reproduction lane pin, re-applied by the exec shim:\n'
                printf 'LANE_PARENT_PROFILE=${R_PROFILE_USER}\n'
                printf 'R_PROFILE_USER=/lane/hook.R\n'
            } > "$environ" || {
                echo "lane shim: could not re-pin the lane hook" >&2
                exit 125
            }
            export R_ENVIRON_USER="$environ"
        else
            export R_ENVIRON_USER=/lane/Renviron
        fi
        ;;
esac

# The run's nonce: from the environment, or, for a child whose environment
# was cleared (env -i), from the lane directory, so that its event still
# counts and the census sees whether it loaded the hook.
nonce=${LANE_RUN_NONCE:-$(cat /lane/nonce 2>/dev/null)}

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

printf 'LANE1 %s %s %s %s 0 EXEC\t%s\n' "${nonce:-none}" "$token" "$$" "$PPID" \
    "$fields" \
    > /proc/1/fd/2 || {
    echo "lane shim: the event stream is not writable; refusing to start R" >&2
    exit 125
}
exec /lane/R.orig "$@"
