#!/usr/bin/env python3
"""SubagentStop receipt gate (routing design §3.2–§3.3; hardened 2026-08-03).

For governed agents (registered in manifest `agent_definitions`), validates
the layered read receipts in the agent's structured output:

- delivery check — `instrument_versions` matches the manifest per pushed
  instrument (catches stale-file pushes);
- consumption check — `instrument_receipts` quotes each end-of-file receipt
  token (for pulled instruments this defeats header-only reads; for pushed
  instruments the token is present in the injected context, so this check
  evidences delivery-and-echo rather than independent consumption — audit
  2026-08-03 M10);
- identity check — `model_id` matches the manifest's pinned model for the
  agent, tolerating the harness's ``[1m]`` context-window marker suffix
  (hard gate, review D-7; marker observed on the 2026-08-03 opus arm);
- version check — `agent_version` matches "<agent_type> v<registry version>";
- pull check — every path declared in `pulled_files_read` was read in full:
  a successful Read call with no `limit`/`offset`, or (since 2026-10-12, the
  gate 1.3 final review's F2) a successful Bash `cat`, `less`, `more`, or
  `nl` whose output was not truncated, or was spilled to a file the agent
  then Read in full. `head`, `tail`, `sed`, `awk`, and `cut` reads are
  partial and `grep` is a search, so none of them verifies a declared pull.
  A Bash read counts only in a command whose success shows it was delivered:
  one `&&` chain of `cd`, full reads, and `echo`, with no pipe, redirection
  of output, or substitution (Astra's delta review of gate 1.3.1,
  D-Astra-1). Every path, Read or shell, matches as a whole normalised path.
  Transcripts are written asynchronously and can lag — the hook retries
  briefly before blocking (review D-12).

The structured output is located in the final assistant message OR, for
workflow-lane spawns whose schema-forced output rides a structured-output
tool call, in the transcript's tool_use inputs (audit 2026-08-03 C4: the
final-message-only search blocked every workflow spawn once).

`status: ESCALATE` outputs are passed through to the orchestrator ONLY after
the receipt and model-identity checks pass — escalation is a valid outcome,
but it is not an exemption from provenance (audit 2026-08-03 C5). An
ESCALATE that carries a result (a verdict, a review, or a target list) must
also pass the pull check (2026-10-12, F2: the herskind pilot's executor
returned a complete SUCCESSFUL result as ESCALATE and so was never checked).

Fail-closed (policy decided ONCE for both hooks, audit item 3, 2026-08-14):
unexpected payload shapes, unattributable events (unparseable or non-object
stdin, undecodable bytes — M-2), hook-environment import failures, and
internal errors all block rather than crash-allow (audit 2026-08-03 C9).
Unattributable-event blocks name the fault class so an operator reads them
as environment/parse faults, not receipt verdicts (pre-run audit N2). On
failure the hook returns `decision: "block"` with the reason, re-prompting
the same subagent instead of failing the batch item (§3.2 self-healing).
"""

from __future__ import annotations

import fnmatch
import json
import posixpath
import re
import sys
import time
from pathlib import Path

# Fail-closed import (mirrors preflight-agent.py, audit item 3 2026-08-14):
# if the shared library or PyYAML is unavailable, block rather than
# crash-allowing unvalidated output.
try:
    from hooklib import (GATE_LOG, REPO_ROOT, extract_json_object,
                         governed_agents, load_manifest, log_jsonl,
                         pushed_instruments)
    _IMPORT_ERROR = None
except Exception as _exc:  # pragma: no cover - environment defect
    _IMPORT_ERROR = _exc

RECEIPT_FIELDS = ("instrument_versions", "instrument_receipts", "agent_version",
                  "model_id", "pulled_files_read")
# Harness marker appended to a model ID when the 1M context window is active;
# the underlying model is the pinned one (recorded verbatim in run records).
CONTEXT_MARKER = "[1m]"
# Retry budget raised 4x0.75s -> 8x1.0s (C2 probes, 2026-08-14): all 45
# benchmark transcripts held valid payloads yet 39 searches failed at hook
# time — write lag beyond the old 3 s budget is the only surviving
# explanation, so the budget is insurance, and the orchestrator-side
# reconciliation (plan C9) is the authoritative backstop.
TRANSCRIPT_RETRIES = 8
TRANSCRIPT_RETRY_DELAY_S = 1.0


def block(agent_type: str, reason: str, ctx: dict | None = None) -> int:
    """Emit a block decision (re-prompts the subagent) and log it.

    `ctx` carries the re-audit C-1 decision context — the event's key names
    (so the real SubagentStop field names are learned from live traffic),
    the agent_id where the event supplies one, the branch that supplied the
    payload, and the item identifier (M-9) — logged on every decision.
    """
    log_jsonl(GATE_LOG, {"event": "block", "agent_type": agent_type,
                         **(ctx or {}), "reason": reason})
    print(json.dumps({"decision": "block",
                      "reason": f"Receipt gate (routing design §3.2): {reason}"}))
    return 0


def transcript_lines(transcript_path: str) -> list[str] | None:
    """Return transcript lines, retrying briefly (async write lag, D-12)."""
    path = Path(transcript_path) if transcript_path.startswith("/") \
        else REPO_ROOT / transcript_path
    for _ in range(TRANSCRIPT_RETRIES):
        try:
            return path.read_text(encoding="utf-8").splitlines()
        except OSError:
            time.sleep(TRANSCRIPT_RETRY_DELAY_S)
    return None


def tool_use_inputs(lines: list[str], names: tuple[str, ...] | None) -> list[dict]:
    """Collect tool_use input dicts from transcript lines.

    With `names`, only calls to those tools; with None, every tool_use input.
    """
    inputs: list[dict] = []
    for line in lines:
        try:
            entry = json.loads(line)
        except json.JSONDecodeError:
            continue
        content = ((entry.get("message") or {}).get("content")
                   if isinstance(entry.get("message"), dict) else entry.get("content"))
        if not isinstance(content, list):
            continue
        for blk in content:
            if isinstance(blk, dict) and blk.get("type") == "tool_use" \
                    and (names is None or blk.get("name") in names) \
                    and isinstance(blk.get("input"), dict):
                inputs.append(blk["input"])
    return inputs


def read_calls(lines: list[str]) -> list[dict]:
    """Read tool calls paired with their result status from the transcript.

    Returns [{"input": dict, "error": bool, "cwd": str}]. A call with no
    recorded result counts as errored: an unverifiable read must not verify
    a declared pull. Added 2026-08-15 (C6/C8 reconciliation finding): a
    benchmark spawn declared pulls whose only Read attempts had failed
    with file-not-found — attempt-matching passed them, success-matching
    must not. ``cwd`` is the working directory the transcript records for
    the call (the repository root when it records none), from which a
    relative path is read.
    """
    uses: list[tuple[str, dict, str]] = []
    errors: dict[str, bool] = {}
    for line in lines:
        try:
            entry = json.loads(line)
        except json.JSONDecodeError:
            continue
        content = ((entry.get("message") or {}).get("content")
                   if isinstance(entry.get("message"), dict) else entry.get("content"))
        if not isinstance(content, list):
            continue
        for blk in content:
            if not isinstance(blk, dict):
                continue
            if blk.get("type") == "tool_use" and blk.get("name") == "Read" \
                    and isinstance(blk.get("input"), dict):
                uses.append((str(blk.get("id")), blk["input"],
                             str(entry.get("cwd") or REPO_ROOT)))
            elif blk.get("type") == "tool_result":
                errors[str(blk.get("tool_use_id"))] = bool(blk.get("is_error"))
    return [{"input": call_input, "error": errors.get(use_id, True), "cwd": cwd}
            for use_id, call_input, cwd in uses]


# Reads made through Bash (2026-10-12, the gate 1.3 final review's F2). Agents
# in the harness's auto mode are told to read files with cat or sed -n, so a
# Read-only check failed every such run while saying nothing true about it.
FULL_READERS = frozenset({"cat", "less", "more", "nl"})
PARTIAL_READERS = frozenset({"head", "tail", "sed", "awk", "cut"})
SEARCHERS = frozenset({"grep", "egrep", "fgrep", "rg", "ugrep", "ag"})
COMMAND_PREFIXES = frozenset({"sudo", "env", "time", "nohup", "nice", "command"})
# Steps that may share a command with a verified read: none of them can skip,
# end, or redirect a later step (Astra's delta review, D-Astra-1).
QUIET_STEPS = frozenset({"echo", "printf", "true", ":"})
# Options that change how cat prints a file, not whether it does. Any other
# option, or any option to nl, less, or more, leaves a read uncredited:
# `cat --help guide.md` exits 0 having printed only help (Astra's closure
# review, D-Astra-1 residual).
CAT_OPTIONS = frozenset({"--number", "--number-nonblank", "--squeeze-blank",
                         "--show-nonprinting", "--show-ends", "--show-all", "--show-tabs"})
CAT_SHORT_OPTIONS_RE = re.compile(r"-[AbeEnstTuv]+")
SPILL_PATH_RE = re.compile(r"Full output saved to:\s*(\S+)")
SPILL_MARKERS = ("<persisted-output>", "Full output saved to:")
HEREDOC_START_RE = re.compile(r"(?<!<)<<(?!<)-?[ \t]*(['\"]?)([A-Za-z_][A-Za-z0-9_]*)\1")
# A redirection at the start of a word: an optional descriptor (digits, or &
# for both streams) and the operator. A heredoc's delimiter is its target.
REDIRECT_RE = re.compile(r"([0-9]+|&)?(>>|>\||>&|>|<<<|<<-?|<&|<>|<)")
RESULT_KEYS = ("verdict", "overall", "verification_targets", "coverage", "dimensions")


def _tool_calls(lines: list[str], name: str) -> list[dict]:
    """Calls to one tool, each with its result: {input, error, text}.

    A call with no recorded result counts as errored, as in read_calls().
    """
    uses: list[tuple[str, dict, str | None]] = []
    results: dict[str, tuple[bool, str]] = {}
    for line in lines:
        try:
            entry = json.loads(line)
        except json.JSONDecodeError:
            continue
        content = ((entry.get("message") or {}).get("content")
                   if isinstance(entry.get("message"), dict) else entry.get("content"))
        if not isinstance(content, list):
            continue
        for blk in content:
            if not isinstance(blk, dict):
                continue
            if blk.get("type") == "tool_use" and blk.get("name") == name \
                    and isinstance(blk.get("input"), dict):
                uses.append((str(blk.get("id")), blk["input"], entry.get("cwd")))
            elif blk.get("type") == "tool_result":
                raw = blk.get("content")
                text = ("".join(str(part.get("text", "")) for part in raw
                                if isinstance(part, dict))
                        if isinstance(raw, list) else str(raw or ""))
                results[str(blk.get("tool_use_id"))] = (bool(blk.get("is_error")), text)
    return [{"input": call_input, "error": results.get(use_id, (True, ""))[0],
             "text": results.get(use_id, (True, ""))[1], "cwd": cwd}
            for use_id, call_input, cwd in uses]


def _mask_quoted(text: str) -> str:
    """The text with quoted and escaped characters blanked (same length)."""
    out: list[str] = []
    quote: str | None = None
    escaped = False
    for ch in text:
        if escaped:
            out.append(" ")
            escaped = False
        elif quote == "'":
            out.append(ch if ch == "'" else " ")
            quote = None if ch == "'" else quote
        elif ch == "\\":
            out.append(" ")
            escaped = True
        elif quote == '"':
            out.append(ch if ch == '"' else " ")
            quote = None if ch == '"' else quote
        else:
            if ch in "'\"":
                quote = ch
            out.append(ch)
    return "".join(out)


def _mask_comments(text: str) -> str:
    """The text with shell comments blanked (same length, newlines kept).

    A ``#`` starts a comment only at the start of an unquoted word, so
    ``$#``, ``${#x}``, ``a#b``, and a quoted ``#`` stay. Without this, a
    comment holding ``; cat guide.md`` was split into a read (Astra's delta
    review, D-Astra-2, which found the same fault in the transcript audit).
    """
    out = list(text)
    quote: str | None = None
    word_start = True
    i = 0
    while i < len(text):
        ch = text[i]
        if quote == "'":
            quote = None if ch == "'" else quote
        elif quote == '"':
            if ch == "\\":
                i += 1
            elif ch == '"':
                quote = None
        elif ch == "\\":
            i += 1
            word_start = False
        elif ch in "'\"":
            quote = ch
            word_start = False
        elif ch == "#" and word_start:
            end = text.find("\n", i)
            end = len(text) if end == -1 else end
            out[i:end] = " " * (end - i)
            i = end
            continue
        else:
            word_start = ch in " \t\n;&|()<>"
        i += 1
    return "".join(out)


def _shell_pipelines(command: str) -> list[dict]:
    """A command's pipelines, in order.

    Heredoc bodies and comments are dropped. Pipelines are split at unquoted
    ``&&``, ``||``, ``;``, ``&``, and newlines, and stages at unquoted ``|``
    and ``|&``; a newline after ``&&``, ``||``, or ``|`` continues the line,
    as in the shell.

    Returns:
        ``[{"before", "after", "stages"}]``: the separator on each side
        (``""`` at the command's ends) and the stripped stage texts.
    """
    kept: list[str] = []
    delimiter: str | None = None
    for line in command.splitlines():
        if delimiter is not None:
            if line.strip() == delimiter:
                delimiter = None
            continue
        visible = _mask_comments(line)
        found = HEREDOC_START_RE.search(visible)
        if found and _mask_quoted(visible)[found.start():found.start() + 2] == "<<":
            delimiter = found.group(2)
        kept.append(line)
    text = _mask_comments("\n".join(kept))
    masked = _mask_quoted(text)
    pipelines: list[dict] = []
    stages: list[str] = []
    before = ""
    start = i = 0
    while i < len(text):
        pair, ch = masked[i:i + 2], masked[i]
        if ch == "\n" and not text[start:i].strip() and (stages or before in ("", "&&", "||")):
            i += 1
            continue
        if pair in ("&&", "||"):
            separator = pair
        elif ch in ";\n":
            separator = ch
        elif ch == "&" and masked[i + 1:i + 2] != ">" and masked[i - 1:i] not in ("<", ">"):
            separator = "&"
        elif ch == "|" and masked[i - 1:i] != ">":
            stages.append(text[start:i])
            i += 2 if masked[i + 1:i + 2] == "&" else 1
            start = i
            continue
        else:
            i += 1
            continue
        stages.append(text[start:i])
        pipelines.append({"before": before, "after": separator, "stages": stages})
        stages, before = [], separator
        i += len(separator)
        start = i
    stages.append(text[start:])
    pipelines.append({"before": before, "after": "", "stages": stages})
    return [{**pipe, "stages": [st.strip() for st in pipe["stages"]]} for pipe in pipelines
            if any(st.strip() for st in pipe["stages"])]


def _read_word(text: str, i: int) -> tuple[dict, int]:
    """The shell word starting at ``i`` and the offset after it.

    Returns:
        ``({"text", "glob", "plain"}, end)``: the word with its quotes
        removed; whether it has an unquoted ``*``, ``?``, or ``[`` (a glob
        the shell expands); and whether it is plain, with no ``$`` or
        backtick outside single quotes, so nothing in it is substituted.
    """
    word: list[str] = []
    glob, plain = False, True
    quote: str | None = None
    while i < len(text):
        ch = text[i]
        if quote == "'":
            if ch == "'":
                quote = None
            else:
                word.append(ch)
        elif quote == '"':
            if ch == '"':
                quote = None
            elif ch == "\\" and i + 1 < len(text) and text[i + 1] in '$`"\\\n':
                i += 1
                word.append(text[i])
            else:
                plain = plain and ch not in "$`"
                word.append(ch)
        elif ch in "'\"":
            quote = ch
        elif ch == "\\" and i + 1 < len(text):
            i += 1
            if text[i] != "\n":
                word.append(text[i])
        elif ch in " \t\n<>|&;()":
            break
        else:
            glob = glob or ch in "*?["
            plain = plain and ch not in "$`"
            word.append(ch)
        i += 1
    return {"text": "".join(word), "glob": glob, "plain": plain}, i


def _stage_parts(stage: str) -> tuple[list[dict], list[tuple[str, str, str]]]:
    """A pipeline stage's words and redirections, read as the shell reads them.

    Version 1.0 (``_stage_words``) dropped redirections, so ``cat x > copy``
    read as a read of both files; here a redirection keeps its descriptor
    and target (D-Astra-1). A parenthesis or other operator character is a
    word of its own that is not plain, so a subshell or substitution is
    never mistaken for a simple read.

    Returns:
        ``(words, redirects)``: words as ``_read_word`` gives them, and each
        redirection as ``(descriptor, operator, target)``.
    """
    words: list[dict] = []
    redirects: list[tuple[str, str, str]] = []
    i = 0
    while i < len(stage):
        if stage[i] in " \t\n":
            i += 1
            continue
        found = REDIRECT_RE.match(stage, i)
        if found:
            i = found.end()
            while i < len(stage) and stage[i] in " \t":
                i += 1
            target, i = _read_word(stage, i)
            redirects.append((found.group(1) or "", found.group(2), target["text"]))
            continue
        if stage[i] in "|&;()":
            words.append({"text": stage[i], "glob": False, "plain": False})
            i += 1
            continue
        word, i = _read_word(stage, i)
        words.append(word)
    return words, redirects


def _command(words: list[dict]) -> tuple[str, list[dict]]:
    """A stage's command name (basename) and the words after it, past
    assignments and prefixes such as ``env`` or ``time``."""
    k = 0
    while k < len(words) and (words[k]["text"] in COMMAND_PREFIXES or re.fullmatch(
            r"[A-Za-z_][A-Za-z0-9_]*=.*", words[k]["text"], re.DOTALL)):
        k += 1
    if k >= len(words):
        return "", []
    return posixpath.basename(words[k]["text"]), words[k + 1:]


def _operands(words: list[dict]) -> tuple[list[dict], list[str]]:
    """A command's operands and options, as getopt reads them.

    A word starting with ``-`` (other than ``-`` alone) is an option until a
    ``--``; every word after ``--`` is an operand, so ``cat -- -x.md`` reads
    a file named ``-x.md``.
    """
    operands: list[dict] = []
    options: list[str] = []
    ended = False
    for word in words:
        text = word["text"]
        if not ended and text == "--":
            ended = True
        elif not ended and text.startswith("-") and text != "-":
            options.append(text)
        else:
            operands.append(word)
    return operands, options


def _prints_whole(name: str, options: list[str]) -> bool:
    """Whether a full reader's options leave it printing its files whole:
    cat's display options only, and no option to nl, less, or more."""
    if name == "cat":
        return all(o in CAT_OPTIONS or CAT_SHORT_OPTIONS_RE.fullmatch(o) for o in options)
    return not options


def _established(pipelines: list[dict],
                 parsed: list[list[tuple[list[dict], list[tuple[str, str, str]]]]]) -> bool:
    """Whether a successful call's exit status shows that every step ran,
    succeeded, and sent its output to the agent (Astra's delta review,
    D-Astra-1).

    Only one shape does: a single chain of ``&&`` whose steps are each one
    stage — ``cd``, a full reader, or a quiet step — with no pipe, no
    redirection except of standard error, nothing substituted, and nothing
    in the background. Every other shape can succeed without delivering a
    read: ``true || cat x`` never runs it, ``cat x; true`` succeeds when cat
    fails, ``cat x > copy`` hides it, and ``cat x | cat y`` replaces it. A
    read in any other shape is not credited, and the agent is asked for a
    plain one instead; this rejects some reads that did deliver, which is
    the safe direction.
    """
    if not pipelines:
        return False
    for pipe, stages in zip(pipelines, parsed):
        if pipe["before"] not in ("", "&&") or pipe["after"] == "&" or len(stages) != 1:
            return False
        words, redirects = stages[0]
        if any(not (fd == "2" and op in (">", ">>", ">&")) for fd, op, _ in redirects):
            return False
        if not all(word["plain"] for word in words):
            return False
        if _command(words)[0] not in FULL_READERS | QUIET_STEPS | {"cd"}:
            return False
    return True


def bash_reads(lines: list[str]) -> list[dict]:
    """Files that Bash commands read, and how.

    Returns:
        ``[{"path", "glob", "cwd", "kind", "error", "spill"}]``. ``kind`` is
        ``complete`` (cat, nl, less, or more, in a command whose success
        establishes the read's delivery, ``_established``, with no option
        but cat's display options, ``_prints_whole``), ``undelivered`` (the
        same readers otherwise, such as ``cat --help x``), ``piped`` (a full reader
        piped into another stage, such as head, wc, grep, or a cat of
        another file), ``partial`` (head, tail, sed, awk, cut, or less or
        more from a ``+`` offset), or ``searched`` (grep and the like).
        ``glob`` says whether the path is a pattern the shell expands.
        ``cwd`` is the directory a relative path is read from: a ``cd`` in
        the command, else the working directory the transcript records for
        the call, else the repository root; it is None (unknown) after
        ``pushd``, ``popd``, or ``cd -``. ``spill`` is the file the harness
        saved a truncated output to, if it did.
    """
    reads: list[dict] = []
    for call in _tool_calls(lines, "Bash"):
        command = str(call["input"].get("command") or "")
        spilled = SPILL_PATH_RE.search(call["text"])
        truncated = any(marker in call["text"] for marker in SPILL_MARKERS)
        spill = (spilled.group(1) if spilled else "") if truncated else None
        cwd: str | None = call.get("cwd") or str(REPO_ROOT)
        pipelines = _shell_pipelines(command)
        parsed = [[_stage_parts(stage) for stage in pipe["stages"]] for pipe in pipelines]
        established = _established(pipelines, parsed)
        for stages in parsed:
            for position, (words, _) in enumerate(stages):
                name, rest = _command(words)
                operands, options = _operands(rest)
                args = [w for w in operands if w["text"] != "-"]
                if name == "cd" and len(stages) == 1:
                    # cd - goes to a directory the transcript does not hold,
                    # and cd --help prints help and stays put.
                    target = args[0]["text"] if args else "~"
                    cwd = (None if any(w["text"] == "-" for w in operands)
                           or set(options) - {"-L", "-P"} else _resolve(target, cwd))
                    continue
                if name in ("pushd", "popd"):
                    cwd = None
                    continue
                if name in FULL_READERS:
                    paged = name in ("less", "more")
                    offset = paged and any(w["text"].startswith("+") for w in args)
                    files = [w for w in args if not (paged and w["text"].startswith("+"))]
                    kind = ("partial" if offset
                            else "piped" if position < len(stages) - 1
                            else "complete" if established and _prints_whole(name, options)
                            else "undelivered")
                elif name in PARTIAL_READERS:
                    kind = "partial"
                    files = args[1:] if name in ("sed", "awk") else args
                elif name in SEARCHERS:
                    kind, files = "searched", args[1:]
                else:
                    continue
                for word in files:
                    reads.append({"path": word["text"], "glob": word["glob"], "cwd": cwd,
                                  "kind": kind, "error": call["error"], "spill": spill})
    return reads


def _resolve(written: str, cwd: str | None) -> str | None:
    """A path as a command or call wrote it, absolute and normalised.

    A relative path is read from ``cwd``; with ``cwd`` unknown (None) its
    file is unknown too, and None is returned.
    """
    if not written.startswith(("/", "~")):
        if cwd is None:
            return None
        written = posixpath.join(cwd, written)
    return posixpath.normpath(posixpath.expanduser(written))


def _glob_match(pattern: str, path: str) -> bool:
    """Whether the shell's expansion of ``pattern`` would include ``path``.

    As in the shell, ``*``, ``?``, and ``[...]`` match within one path
    component, and a leading dot only literally. ``fnmatch`` alone lets
    ``*`` cross ``/``, so ``/ref/*.md`` would have verified a declared
    ``/ref/sub/x.md`` that the command never read.
    """
    patterns, parts = pattern.split("/"), path.split("/")
    return len(patterns) == len(parts) and all(
        fnmatch.fnmatchcase(part, glob) and (glob.startswith(".") or not part.startswith("."))
        for glob, part in zip(patterns, parts))


def _names(declared: str, written: str, cwd: str | None, glob: bool | None = None) -> bool:
    """Whether a path or glob as written in a command names a declared file.

    Both are compared as whole, normalised paths: a relative path is read
    from ``cwd`` (the command's own cd, or the working directory the
    transcript records), and a relative declaration from the repository
    root. A bare file name never matches a same-named file elsewhere (Fable's
    delta review, D-2). ``glob`` says whether the shell expanded ``written``
    (``bash_reads`` records it); when it is not given, any ``*``, ``?``, or
    ``[`` makes a pattern.
    """
    path = _resolve(written, cwd)
    if path is None:
        return False
    target = _resolve(declared, str(REPO_ROOT))
    if glob is None:
        glob = any(ch in written for ch in "*?[")
    return _glob_match(path, target) if glob else target == path


def pull_verdict(declared: str, reads: list[dict], shell: list[dict]) -> tuple[str, str]:
    """How a declared pull was read: ``read``, ``truncated``, ``undelivered``,
    ``searched``, ``errored``, or ``missing``, with a short account of how.

    Read calls, and the Read of a spill file, match by whole normalised path,
    as shell reads do (Astra's delta review, D-Astra-1): a Read of
    ``guide.md.bak`` does not verify ``guide.md``.

    Args:
        declared: the path the agent declared in ``pulled_files_read``.
        reads: ``read_calls(lines)``.
        shell: ``bash_reads(lines)``.
    """
    target = _resolve(declared, str(REPO_ROOT))

    def read_path(call: dict) -> str | None:
        written = str(call["input"].get("file_path") or "")
        return _resolve(written, call.get("cwd") or str(REPO_ROOT)) if written else None

    def in_full(call: dict) -> bool:
        return "limit" not in call["input"] and "offset" not in call["input"]

    tool = [c for c in reads if read_path(c) == target]
    tool_ok = [c for c in tool if not c["error"]]
    bash = [b for b in shell if _names(declared, b["path"], b["cwd"], b.get("glob"))]
    bash_ok = [b for b in bash if not b["error"]]

    def spill_read(spill: str | None) -> bool:
        """No spill, or the spill file Read in full by its whole path."""
        if spill is None:
            return True
        spilled = _resolve(spill, None) if spill else None
        return spilled is not None and any(
            read_path(c) == spilled and not c["error"] and in_full(c) for c in reads)

    if any(in_full(c) for c in tool_ok) or \
            any(b["kind"] == "complete" and spill_read(b["spill"]) for b in bash_ok):
        return "read", ""
    if tool_ok or any(b["kind"] in ("complete", "partial", "piped") for b in bash_ok):
        how = ("Read with limit/offset" if tool_ok else
               "a partial shell read (head, tail, sed, awk, or cut)"
               if any(b["kind"] == "partial" for b in bash_ok)
               else "a shell read piped into another command"
               if any(b["kind"] == "piped" for b in bash_ok)
               else "a shell read whose output the harness truncated")
        return "truncated", how
    if any(b["kind"] == "undelivered" for b in bash_ok):
        return "undelivered", ("read in a shell command whose success does not show that "
                               "you received it (its output redirected, its step conditional "
                               "or in the background, one step among others, or the reader "
                               "given an option such as --help that the check does not "
                               "recognise)")
    if bash_ok:
        return "searched", "only searched (grep), never read"
    if tool or bash:
        return "errored", "every attempt errored"
    return "missing", ""


def structured_output_from_transcript(lines: list[str]) -> dict | None:
    """Find the last schema-shaped structured output among tool_use inputs.

    Workflow-lane spawns emit their schema-forced output through a
    structured-output tool call rather than the final message. Anchor on the
    output contract (a `status` plus receipt content) rather than a tool
    name, which is harness-internal and may change.
    """
    candidates = [inp for inp in tool_use_inputs(lines, None)
                  if "status" in inp and ("receipts" in inp or "instrument_versions" in inp)]
    return candidates[-1] if candidates else None


def receipt_fields(payload: dict) -> dict | None:
    """Return the five receipt fields from a payload, flat or nested.

    The benchmark output schema nests them under `receipts`; the agent
    definitions list them without specifying nesting. Try the nested
    carrier first, then the payload itself (L-1, 2026-08-14: an incomplete
    `receipts` dict must not mask complete flat fields). None if no
    carrier holds all five fields well-typed.
    """
    nested = payload.get("receipts") \
        if isinstance(payload.get("receipts"), dict) else None
    for carrier in (nested, payload):
        if carrier is None or not all(f in carrier for f in RECEIPT_FIELDS):
            continue
        fields = {f: carrier[f] for f in RECEIPT_FIELDS}
        if isinstance(fields["instrument_versions"], dict) \
                and isinstance(fields["instrument_receipts"], dict) \
                and isinstance(fields["pulled_files_read"], list):
            return fields
    return None


def model_matches(got: str, pinned: str) -> bool:
    """Exact pin match, tolerating the harness context-window marker."""
    return got == pinned or got == pinned + CONTEXT_MARKER


def validate(event: dict) -> int:
    """Validate one governed agent's receipts; block on failure."""
    agent_type = str(event.get("agent_type") or "")
    # Decision context, logged on every outcome (re-audit C-1): the event's
    # key names teach us the real SubagentStop field shape from live traffic
    # (design-doc names like agent_transcript_path are unconfirmed until the
    # C2 capture), agent_id attributes the decision where the event carries
    # one, payload_source records which branch supplied the payload, and
    # paper_slug identifies the item (M-9).
    ctx = {"event_keys": sorted(str(k) for k in event.keys()),
           "agent_id": str(event.get("agent_id") or ""),
           "payload_source": "none",
           "transcript_state": "not-needed"}

    try:
        manifest = load_manifest()
    except Exception as exc:
        return block(agent_type,
                     f"manifest unreadable ({exc}) — cannot validate receipts", ctx)

    registry = governed_agents(manifest)
    if agent_type not in registry:
        return 0

    # Payload selection (re-audit C-2, re-specified 2026-08-14): prefer a
    # WELL-FORMED receipt payload from the final message; only when the final
    # message carries none may the transcript's tool calls supply one — and a
    # receipt-less JSON object in the final message must not suppress that
    # search (the C4-era regression). A transcript payload adopted while the
    # final message names a different paper_slug is substitution, not
    # fallback, and blocks: receipts must be bound to this item.
    output_text = event.get("last_assistant_message") or ""
    final_payload = extract_json_object(output_text) if output_text else None
    payload = None
    lines = None
    if final_payload is not None and receipt_fields(final_payload) is not None:
        payload = final_payload
        ctx["payload_source"] = "final_message"
    else:
        transcript_path = str(event.get("agent_transcript_path") or "")
        if not transcript_path:
            lines = None
            ctx["transcript_state"] = "none-declared"
        else:
            lines = transcript_lines(transcript_path)
            ctx["transcript_state"] = ("read" if lines is not None
                                       else "unavailable-after-retries")
        from_tool = structured_output_from_transcript(lines) if lines else None
        if from_tool is not None and receipt_fields(from_tool) is not None:
            final_slug = str((final_payload or {}).get("paper_slug") or "")
            tool_slug = str(from_tool.get("paper_slug") or "")
            if final_slug and tool_slug and final_slug != tool_slug:
                ctx["payload_source"] = "transcript_tool_call"
                return block(agent_type,
                             f"final message names paper_slug {final_slug!r} but the "
                             f"transcript's structured output names {tool_slug!r} — "
                             f"receipts are not bound to this item; re-emit your full "
                             f"structured output including receipts", ctx)
            payload = from_tool
            ctx["payload_source"] = "transcript_tool_call"
        elif from_tool is not None:
            # Malformed in both places (or final absent): report against the
            # transcript candidate so the reason names real receipt fields.
            payload = from_tool
            ctx["payload_source"] = "transcript_tool_call"
        elif final_payload is not None:
            payload = final_payload
            ctx["payload_source"] = "final_message"
    if payload is None:
        # Distinct reasons per branch (re-audit C-1; C2 finding 2026-08-14):
        # "transcript unavailable" and "searched and found nothing" are
        # different faults with different remedies — conflating them hid the
        # benchmark's write-lag failure mode for eleven days.
        if ctx["transcript_state"] == "unavailable-after-retries":
            return block(agent_type, "no structured output in the final message and "
                                     "the agent transcript was unavailable after "
                                     "retries — transcript write lag suspected, not "
                                     "a missing payload; re-emit your full "
                                     "structured output including receipts", ctx)
        return block(agent_type, "no structured output found in the final message or "
                                 "the transcript's tool calls — re-emit your full "
                                 "structured output including receipts", ctx)
    ctx["paper_slug"] = str(payload.get("paper_slug") or "")

    fields = receipt_fields(payload)
    if fields is None:
        return block(agent_type, "receipt fields missing or malformed (need "
                                 + ", ".join(RECEIPT_FIELDS)
                                 + ", flat or under 'receipts') — re-emit receipts", ctx)

    versions, receipts = fields["instrument_versions"], fields["instrument_receipts"]
    for spec in pushed_instruments(manifest, agent_type):
        got_version = str(versions.get(spec["name"], "")).strip()
        if got_version != spec["version"]:
            return block(agent_type, f"instrument_versions[{spec['name']}] is "
                                     f"{got_version!r}, manifest says {spec['version']!r} — "
                                     f"re-read the injected instrument and re-emit receipts",
                         ctx)
        got_token = str(receipts.get(spec["name"], "")).strip()
        if got_token != spec["token"]:
            return block(agent_type, f"instrument_receipts[{spec['name']}] does not match "
                                     f"the end-of-file Receipt-token — read the injected "
                                     f"instrument to its final line and re-emit receipts",
                         ctx)

    entry = registry[agent_type]
    pinned = str(entry.get("model", "")).strip()
    got_model = str(fields["model_id"]).strip()
    if pinned and not model_matches(got_model, pinned):
        return block(agent_type, f"model_id {got_model!r} does not match the manifest pin "
                                 f"{pinned!r} — model identity is part of the instrument "
                                 f"(design §3.3); this item is blocked, not retried: escalate",
                     ctx)

    expected_agent_version = f"{agent_type} v{str(entry.get('version', '')).strip()}"
    got_agent_version = str(fields["agent_version"]).strip()
    if got_agent_version != expected_agent_version:
        return block(agent_type, f"agent_version {got_agent_version!r} does not match "
                                 f"{expected_agent_version!r} — re-emit receipts from your "
                                 f"agent brief", ctx)

    # Delivery verification for the output contract (audit S3, 2026-08-14):
    # v1.1+ payloads carry a validator-enforced schema_version; when present
    # it must match the registered contract. v1.0-era payloads lack the
    # field and pass unchanged (the old contract predates
    # self-identification).
    declared_schema = str(payload.get("schema_version") or "").strip()
    if declared_schema:
        registered = str((((manifest.get("assessment") or {}).get("schemas") or {})
                          .get("benchmark_fair_output") or {}).get("version", "")).strip()
        if registered and declared_schema != registered:
            return block(agent_type, f"schema_version {declared_schema!r} does not match "
                                     f"the registered output contract {registered!r} — "
                                     f"the spawn was supplied a stale or unregistered "
                                     f"schema; orchestrator attention needed, not a "
                                     f"retry: escalate", ctx)

    # ESCALATE passes through to the orchestrator only after provenance holds,
    # and, when it carries a result, only after the pull check too (F2).
    escalated = str(payload.get("status", "")) == "ESCALATE"
    if escalated and not any(key in payload for key in RESULT_KEYS):
        log_jsonl(GATE_LOG, {"event": "escalate-passthrough", "agent_type": agent_type,
                             **ctx, "model_id": got_model,
                             "reason": payload.get("escalate_reason")})
        return 0

    pulled = fields["pulled_files_read"]
    if pulled:
        if lines is None:
            transcript_path = str(event.get("agent_transcript_path") or "")
            lines = transcript_lines(transcript_path) if transcript_path else None
        if lines is None:
            return block(agent_type, "agent transcript unavailable after retries — cannot "
                                     "verify declared pulled-file reads (D-12 fail-closed)",
                         ctx)
        calls = read_calls(lines)
        shell = bash_reads(lines)
        for declared in pulled:
            declared_path = str(declared).strip()
            if not declared_path:
                # L-3 (2026-08-14): "" is a substring of every path — an
                # empty declaration must not be a free pass.
                return block(agent_type, "pulled_files_read contains an empty path — "
                                         "declare the actual file read or remove the "
                                         "entry", ctx)
            verdict, how = pull_verdict(declared_path, calls, shell)
            if verdict == "read":
                continue
            # 2026-08-15: attempts are not reads — a declared pull whose
            # every attempt errored never entered the agent's context. Any
            # verdict but "read" blocks, including one added later and not
            # named here (fail-closed, D-Astra-1).
            reasons = {
                "missing": f"declared pulled read {declared!r} has no matching Read call or "
                           f"shell read in the transcript — re-read it in full and re-emit "
                           f"receipts",
                "errored": f"declared pulled read {declared!r} was attempted but every "
                           f"matching Read errored — the file was never actually read; "
                           f"re-read it in full from its canonical path and re-emit receipts",
                "searched": f"declared pulled read {declared!r} was {how} — read the file in "
                            f"full and re-emit receipts",
                "truncated": f"pulled read {declared!r} was truncated ({how}) — re-read the "
                             f"file in full",
                "undelivered": f"declared pulled read {declared!r} was {how} — read it on its "
                               f"own, with the Read tool (no limit or offset) or a command that "
                               f"is only `cat <path>`, and re-emit receipts",
            }
            return block(agent_type, reasons.get(verdict, f"declared pulled read {declared!r} "
                                                          f"has the unrecognised verdict "
                                                          f"{verdict!r} — fail-closed"), ctx)

    log_jsonl(GATE_LOG, {"event": "escalate-passthrough" if escalated else "pass",
                         "agent_type": agent_type, **ctx, "model_id": got_model,
                         "pulled": len(pulled),
                         **({"reason": payload.get("escalate_reason"), "checked": True}
                            if escalated else {})})
    return 0


def main() -> int:
    """Parse the SubagentStop event and validate fail-closed.

    Unattributable events (unparseable, undecodable, or non-object stdin)
    BLOCK: governedness cannot be determined, and refusing beats letting a
    governed scoring spawn stop ungated (policy decided once for both
    hooks, 2026-08-14). The block reason names the fault class so it reads
    as an environment/parse fault, not a receipt verdict.
    """
    if _IMPORT_ERROR is not None:
        print(json.dumps({"decision": "block",
                          "reason": f"Receipt gate: hook environment broken "
                                    f"({_IMPORT_ERROR}) — environment fault, not a "
                                    f"receipt verdict; fix the hook environment"}))
        return 0
    try:
        event = json.load(sys.stdin)
    except Exception as exc:  # includes non-UTF-8 bytes (M-2)
        return block("", f"unattributable SubagentStop event "
                         f"({exc.__class__.__name__}: {exc}) — parse fault, not a "
                         f"receipt verdict", {"event_keys": []})
    if not isinstance(event, dict):
        return block("", "SubagentStop event is not a JSON object — parse fault, "
                         "not a receipt verdict", {"event_keys": []})
    agent_type = str(event.get("agent_type") or "")
    try:
        return validate(event)
    except Exception as exc:  # fail-closed: block rather than crash-allow (C9)
        return block(agent_type, f"receipt gate internal error ({exc.__class__.__name__}: "
                                 f"{exc}) — blocking rather than passing unvalidated output",
                     {"event_keys": sorted(str(k) for k in event.keys())})


if __name__ == "__main__":
    sys.exit(main())
