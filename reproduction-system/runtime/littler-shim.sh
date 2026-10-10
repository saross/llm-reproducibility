#!/bin/sh
# Reproduction lane littler shim (gate 1.3, spec §8).
#
# littler's r embeds libR, so it starts R without the front end: it passes
# neither the exec shim nor any profile, and the gate could not see what it
# loaded. run-container mounts this file read-only over every littler binary
# in the image (/usr/local/bin/r in the rocker images resolves to
# site-library/littler/bin/r), so "r" runs Rscript with the same arguments,
# which goes through the front end, the exec shim, and the hook.
#
# r and Rscript share "r file.R" and "r -e expr". littler's other options
# (-l, -d, -i, ...) are not Rscript's, and Rscript refuses them, so such a
# run fails visibly rather than silently. A wrapper that calls littler is a
# static error in any case (spec §10).

exec Rscript "$@"
