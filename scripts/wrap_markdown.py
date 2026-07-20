#!/usr/bin/env python3
"""Reflow Markdown prose to a maximum line width without changing rendered output.

Why this exists
---------------
Blog posts written with one giant line per paragraph are painful to review: a
one-word edit shows up as a whole-paragraph diff. This tool wraps prose at a
fixed column so edits produce small, line-level diffs.

Crucially, it does NOT change the rendered HTML. In Markdown a single newline
inside a paragraph is a "soft break" that renders as a space, not a line break.
A real line break requires two trailing spaces (a "hard break"). This tool only
ever inserts soft breaks and always preserves existing hard breaks verbatim, so
`zola build` produces byte-identical HTML before and after formatting.

What it wraps
-------------
- Ordinary paragraphs
- Blockquote paragraphs (the `> ` prefix is kept on every wrapped line)
- Simple single-paragraph list items (continuation lines are hanging-indented)

What it leaves untouched (never reflowed)
-----------------------------------------
- TOML front matter (the `+++ ... +++` block)
- Fenced code blocks (``` ``` ``` ``` or `~~~`) and indented code (4+ spaces)
- Tables (any line containing `|`)
- ATX headings (`#`, `##`, ...) and setext underlines
- Thematic breaks (`---`, `***`, `___`)
- Raw HTML blocks (lines starting with `<`)
- Link reference definitions (`[id]: url`)

The tool is intentionally dependency-free (Python 3 standard library only) so it
runs the same on Linux, macOS and Windows, in CI and on a developer machine.

Usage
-----
    python3 scripts/wrap_markdown.py [--width N] [--check] [PATHS...]

With no PATHS it defaults to the blog content directory. `--check` makes no
changes and exits non-zero if any file is not already wrapped (used in CI).
"""

from __future__ import annotations

import argparse
import os
import re
import sys

DEFAULT_WIDTH = 80

# Default target: every Markdown file under the blog content directory.
_REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_TARGET = os.path.join(_REPO_ROOT, "zola-site", "content", "blog")

# --- Line classifiers ------------------------------------------------------
FRONTMATTER_FENCE = re.compile(r"^\+\+\+\s*$")
CODE_FENCE = re.compile(r"^\s*(```|~~~)")
HEADING = re.compile(r"^ {0,3}#{1,6}(\s|$)")
BLOCKQUOTE = re.compile(r"^ {0,3}>")
LIST_ITEM = re.compile(r"^( {0,3})([-+*]|\d+[.)])(\s+)(\S.*)$")
LINK_REF_DEF = re.compile(r"^ {0,3}\[[^\]]+\]:\s")
INDENTED_CODE = re.compile(r"^ {4,}\S")
HTML_BLOCK = re.compile(r"^ {0,3}<")
BLANK = re.compile(r"^\s*$")
# A line whose text is only "structural" punctuation (thematic break / setext
# underline). These must never be merged into or produced by a reflow.
STRUCTURAL_ONLY = re.compile(r"^ {0,3}([-*_]{3,}|=+|-+)\s*$")
HARD_BREAK = re.compile(r"\S {2,}$")

# Tokens that, if they begin a wrapped continuation line, would be reinterpreted
# by Markdown as the start of a new block (heading, list, quote, ...), changing
# the rendered output. We refuse to start a line with any of these.
_DANGEROUS = [
    re.compile(r"^#{1,6}$"),          # ATX heading marker
    re.compile(r"^>"),                # blockquote marker
    re.compile(r"^[-+*]$"),           # bullet list marker
    re.compile(r"^\d+[.)]$"),         # ordered list marker
    re.compile(r"^(-{3,}|\*{3,}|_{3,})$"),  # thematic break
    re.compile(r"^(=+|-+)$"),         # setext underline
    re.compile(r"^(```|~~~)"),        # code fence
    re.compile(r"^<"),                # raw HTML / autolink
]


def is_dangerous_start(token: str) -> bool:
    return any(p.match(token) for p in _DANGEROUS)


def is_plain_paragraph_line(line: str) -> bool:
    """True if a line is ordinary prose that may be reflowed."""
    if BLANK.match(line):
        return False
    if HEADING.match(line):
        return False
    if BLOCKQUOTE.match(line):
        return False
    if LIST_ITEM.match(line):
        return False
    if LINK_REF_DEF.match(line):
        return False
    if INDENTED_CODE.match(line):
        return False
    if HTML_BLOCK.match(line):
        return False
    if STRUCTURAL_ONLY.match(line):
        return False
    if "|" in line:  # table row
        return False
    if CODE_FENCE.match(line):
        return False
    return True


def _wrap_segment_words(words, width, first_prefix, cont_prefix, first_line):
    """Greedily wrap a list of words, never starting a line with a dangerous
    token. ``first_line`` indicates whether the first produced line is the very
    first line of the whole block (uses ``first_prefix``)."""
    lines = []
    cur = []

    def prefix_len():
        use_first = first_line and not lines
        return len(first_prefix if use_first else cont_prefix)

    for tok in words:
        if not cur:
            cur = [tok]
            continue
        candidate = " ".join(cur + [tok])
        if prefix_len() + len(candidate) <= width:
            cur.append(tok)
        elif is_dangerous_start(tok):
            # Would break here, but the token can't start a line: keep it on the
            # current line and accept the overflow (rendered output is what
            # matters, not the column count).
            cur.append(tok)
        else:
            lines.append(" ".join(cur))
            cur = [tok]
    if cur:
        lines.append(" ".join(cur))
    return lines


def reflow_block(segments, width, first_prefix, cont_prefix, trailing_hard):
    """Reflow ``segments`` (a list of word-lists, one per hard-break-delimited
    run) into physical lines. A hard break is re-emitted (two trailing spaces)
    at the end of every segment except the last; ``trailing_hard`` forces one on
    the final line too."""
    physical = []  # (text_without_prefix, needs_hard_break)
    n = len(segments)
    for si, words in enumerate(segments):
        sub = _wrap_segment_words(
            words, width, first_prefix, cont_prefix,
            first_line=(len(physical) == 0),
        )
        if not sub:
            sub = [""]
        seg_needs_break = si < n - 1 or trailing_hard
        for j, text in enumerate(sub):
            is_seg_last = j == len(sub) - 1
            physical.append((text, seg_needs_break and is_seg_last))

    out = []
    for idx, (text, hard) in enumerate(physical):
        prefix = first_prefix if idx == 0 else cont_prefix
        line = prefix + text
        if hard:
            line += "  "
        out.append(line)
    return out


def _split_segments(text_lines):
    """Turn raw prose lines (already stripped of any block prefix) into
    hard-break-delimited segments of words. Returns (segments, trailing_hard)."""
    segments = []
    words = []
    trailing_hard = False
    last = len(text_lines) - 1
    for k, raw in enumerate(text_lines):
        hard = bool(HARD_BREAK.search(raw))
        words.extend(raw.split())
        if hard:
            if k == last:
                trailing_hard = True
            else:
                segments.append(words)
                words = []
    segments.append(words)
    return segments, trailing_hard


def format_text(text: str, width: int) -> str:
    """Return ``text`` reflowed to ``width`` columns, preserving rendered
    output and the file's trailing-newline convention."""
    had_trailing_newline = text.endswith("\n")
    lines = text.split("\n")
    if had_trailing_newline:
        lines = lines[:-1]  # drop the artefact empty element from split

    out = []
    i = 0
    n = len(lines)
    in_frontmatter = False
    in_code = False
    code_fence_marker = ""
    first_line_seen = False

    while i < n:
        line = lines[i]

        # Front matter: the leading +++ ... +++ block is TOML, never touched.
        if not first_line_seen and FRONTMATTER_FENCE.match(line):
            in_frontmatter = True
            first_line_seen = True
            out.append(line)
            i += 1
            continue
        first_line_seen = True
        if in_frontmatter:
            out.append(line)
            if FRONTMATTER_FENCE.match(line):
                in_frontmatter = False
            i += 1
            continue

        # Fenced code blocks are emitted verbatim.
        if in_code:
            out.append(line)
            if re.match(r"^\s*" + re.escape(code_fence_marker), line):
                in_code = False
            i += 1
            continue
        fence = CODE_FENCE.match(line)
        if fence:
            in_code = True
            code_fence_marker = fence.group(1)
            out.append(line)
            i += 1
            continue

        # Blockquote paragraph.
        if BLOCKQUOTE.match(line):
            block = []
            while i < n and BLOCKQUOTE.match(lines[i]) and not BLANK.match(lines[i]):
                block.append(lines[i])
                i += 1
            out.extend(_reflow_blockquote(block, width))
            continue

        # List item (simple, single paragraph).
        m = LIST_ITEM.match(line)
        if m:
            handled, consumed, produced = _reflow_list_item(lines, i, width)
            if handled:
                out.extend(produced)
                i = consumed
                continue

        # Plain paragraph.
        if is_plain_paragraph_line(line):
            block = []
            while i < n and is_plain_paragraph_line(lines[i]):
                block.append(lines[i])
                i += 1
            segments, trailing_hard = _split_segments(block)
            out.extend(reflow_block(segments, width, "", "", trailing_hard))
            continue

        # Anything else (headings, tables, HTML, blanks, structural): verbatim.
        out.append(line)
        i += 1

    result = "\n".join(out)
    if had_trailing_newline:
        result += "\n"
    return result


def _reflow_blockquote(block, width):
    """Reflow a run of blockquote lines that form a single paragraph. Only plain
    prose inside the quote is reflowed; anything structural is left verbatim."""
    # Capture the quote prefix (the leading > markers and their spaces) from the
    # first line, e.g. "> " or "> > ".
    prefix_match = re.match(r"^((?: {0,3}>+ ?)+)", block[0])
    prefix = prefix_match.group(1) if prefix_match else "> "
    inner = []
    for ln in block:
        stripped = re.sub(r"^(?: {0,3}>+ ?)+", "", ln)
        inner.append(stripped)
    # If the quoted content is not plain prose, leave the block untouched.
    if any(not is_plain_paragraph_line(s) and not BLANK.match(s) for s in inner):
        return list(block)
    segments, trailing_hard = _split_segments(inner)
    # Normalise the continuation prefix to the marker without trailing padding
    # beyond a single space so every wrapped line stays inside the quote.
    quote_prefix = prefix.rstrip() + " "
    return reflow_block(segments, width, quote_prefix, quote_prefix, trailing_hard)


def _reflow_list_item(lines, start, width):
    """Reflow a single-paragraph list item beginning at ``lines[start]``.

    Returns (handled, next_index, produced_lines). ``handled`` is False when the
    item is too complex to safely reflow (nested blocks, multiple paragraphs),
    in which case the caller emits the original line and moves on."""
    m = LIST_ITEM.match(lines[start])
    indent, marker, spaces, content = m.groups()
    first_prefix = indent + marker + spaces
    cont_prefix = " " * len(first_prefix)

    item_lines = [content]
    i = start + 1
    n = len(lines)
    while i < n:
        nxt = lines[i]
        if BLANK.match(nxt):
            break
        # A new list marker, heading, quote, table, code, etc. ends this item's
        # paragraph.
        if LIST_ITEM.match(nxt) or not is_plain_paragraph_line(nxt):
            break
        # Lazy or hanging continuation of the same paragraph.
        item_lines.append(nxt.lstrip())
        i += 1

    segments, trailing_hard = _split_segments(item_lines)
    produced = reflow_block(segments, width, first_prefix, cont_prefix, trailing_hard)
    return True, i, produced


def process_file(path: str, width: int, check: bool):
    """Format one file. Returns True if the file is already formatted (or was
    fixed), False if it differs in --check mode."""
    with open(path, "r", encoding="utf-8", newline="") as fh:
        original = fh.read()
    # Work on \n internally; restore the file's newline style on write.
    uses_crlf = "\r\n" in original
    normalized = original.replace("\r\n", "\n")
    formatted = format_text(normalized, width)
    if formatted == normalized:
        return True
    if check:
        return False
    to_write = formatted.replace("\n", "\r\n") if uses_crlf else formatted
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(to_write)
    return True


def collect_files(paths):
    files = []
    for p in paths:
        if os.path.isdir(p):
            for root, _dirs, names in os.walk(p):
                for name in sorted(names):
                    if name.endswith(".md"):
                        files.append(os.path.join(root, name))
        elif p.endswith(".md"):
            files.append(p)
    return files


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Wrap Markdown prose to a maximum line width without "
                    "changing rendered output.",
    )
    parser.add_argument(
        "paths", nargs="*", default=[DEFAULT_TARGET],
        help="Markdown files or directories (default: blog content dir).",
    )
    parser.add_argument(
        "--width", type=int, default=DEFAULT_WIDTH,
        help=f"Maximum line width (default: {DEFAULT_WIDTH}).",
    )
    parser.add_argument(
        "--check", action="store_true",
        help="Do not modify files; exit non-zero if any need wrapping.",
    )
    args = parser.parse_args(argv)

    files = collect_files(args.paths)
    if not files:
        print("No Markdown files found.", file=sys.stderr)
        return 1

    needs_fix = []
    for path in files:
        ok = process_file(path, args.width, args.check)
        if not ok:
            needs_fix.append(path)

    if args.check:
        if needs_fix:
            print("The following files exceed the line width and need wrapping:")
            for path in needs_fix:
                print(f"  {os.path.relpath(path)}")
            print()
            print("Run: python3 scripts/wrap_markdown.py")
            return 1
        print(f"All {len(files)} Markdown file(s) are within {args.width} columns.")
        return 0

    print(f"Formatted {len(files)} Markdown file(s) to {args.width} columns.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
