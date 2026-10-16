#!/usr/bin/env python3
"""Fail when text files contain covert Unicode or whitespace marks.

Some generators hide a mark in characters a reader does not see: zero-width
spaces, Unicode tag characters, bidirectional overrides, a byte-order mark, or
a space that is not U+0020. Others swap in a letter that looks like ASCII but
is not (for example Cyrillic U+0430 inside an English word). This script finds
those characters and exits non-zero. It does not rewrite files. The failure
text names the file, line, character column, code point, and the edit.

Word-choice watermarks are a different channel. SynthID-Text and the
Kirchenbauer green-list scheme bias which token is chosen. They do not insert
a character, so there is no line to point at. Detection needs the secret key
used at generation time. The public implementation is
https://github.com/google-deepmind/synthid-text and it does not detect a mark
without that key. Public descriptions of Claude's text watermark say it is
this kind of keyed statistical mark, not hidden Unicode, and no detector key
is published. This script says so, and it does not invent an edit for that
channel.

The same invisible characters are also a source-code hazard (Trojan Source
bidirectional overrides, ASCII smuggling via tag characters). Rejecting them
in CI keeps them out of content and out of code.

Usage
-----
    python3 scripts/check_content_marks.py --self-test
    python3 scripts/check_content_marks.py
    python3 scripts/check_content_marks.py path/to/file.md
"""

from __future__ import annotations

import argparse
import os
import sys
import unicodedata

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SKIP_DIRS = {".git", "node_modules", "public", ".venv"}
SKIP_FILES = {"package-lock.json"}
TEXT_EXTENSIONS = {
    ".css",
    ".html",
    ".js",
    ".json",
    ".jsonc",
    ".md",
    ".mno",
    ".py",
    ".sh",
    ".svg",
    ".toml",
    ".txt",
    ".xml",
    ".yaml",
    ".yml",
}
TEXT_NAMES = {
    ".gitignore",
    ".markdownlint-cli2.jsonc",
    ".prettierignore",
    "CNAME",
    "Dockerfile",
    "Makefile",
}

# Letters that render as ASCII in common fonts. Code points only, so this
# source file does not itself contain a lookalike.
COVERT_CONFUSABLES = {
    "\u0391": "A",
    "\u0392": "B",
    "\u0395": "E",
    "\u0397": "H",
    "\u0399": "I",
    "\u039a": "K",
    "\u039c": "M",
    "\u039f": "O",
    "\u03a1": "P",
    "\u03a4": "T",
    "\u03bf": "o",
    "\u0410": "A",
    "\u0412": "B",
    "\u0415": "E",
    "\u041a": "K",
    "\u041c": "M",
    "\u041d": "H",
    "\u041e": "O",
    "\u0420": "P",
    "\u0421": "C",
    "\u0422": "T",
    "\u0425": "X",
    "\u0430": "a",
    "\u0435": "e",
    "\u043e": "o",
    "\u0440": "p",
    "\u0441": "c",
    "\u0443": "y",
    "\u0445": "x",
    "\u0455": "s",
    "\u0456": "i",
    "\u0458": "j",
    "\u04bb": "h",
    "\u04cf": "l",
}

FULLWIDTH_DIGITS = {
    "ZERO": "0",
    "ONE": "1",
    "TWO": "2",
    "THREE": "3",
    "FOUR": "4",
    "FIVE": "5",
    "SIX": "6",
    "SEVEN": "7",
    "EIGHT": "8",
    "NINE": "9",
}

# Variation selectors kept only when they follow a symbol (emoji presentation).
EMOJI_VARIATION_SELECTORS = {0xFE0E, 0xFE0F}
# Zero-width joiner is part of emoji sequences. Between letters it is a mark.
ZWJ = "\u200d"


class Finding:
    def __init__(self, path, line, column, codepoint, channel, change, context):
        self.path = path
        self.line = line
        self.column = column
        self.codepoint = codepoint
        self.channel = channel
        self.change = change
        self.context = context

    def render(self) -> str:
        name = unicodedata.name(chr(self.codepoint), "UNNAMED CHARACTER")
        return (
            f"{self.path}:{self.line}:{self.column}\n"
            f"  found: U+{self.codepoint:04X} {name} ({self.channel})\n"
            f"  column: character {self.column} on this line (not a byte offset)\n"
            f"  change: {self.change}\n"
            f"  context: {self.context}"
        )


def _is_symbol(ch: str | None) -> bool:
    if not ch:
        return False
    return unicodedata.category(ch) in {"So", "Sk"}


def _ascii_letter(ch: str) -> str | None:
    """Return the ASCII letter a stylized Unicode letter stands in for."""
    name = unicodedata.name(ch, "")
    if name.startswith("FULLWIDTH DIGIT "):
        return FULLWIDTH_DIGITS.get(name.rsplit(" ", 1)[-1])
    if " LETTER " not in name:
        return None
    letter = name.rsplit(" ", 1)[-1]
    if len(letter) == 1 and letter.isascii() and letter.isalpha():
        if name.startswith("MATHEMATICAL ") or name.startswith("FULLWIDTH LATIN "):
            return letter
    return None


def _delete(codepoint: int, why: str) -> str:
    name = unicodedata.name(chr(codepoint), "UNNAMED CHARACTER")
    return f"Delete U+{codepoint:04X} {name}. {why}"


def _replace_space(codepoint: int) -> str:
    name = unicodedata.name(chr(codepoint), "UNNAMED CHARACTER")
    return (
        f"Replace U+{codepoint:04X} {name} with a normal space (U+0020), "
        "or delete it if the gap should not be there."
    )


def _replace_letter(codepoint: int, ascii_char: str) -> str:
    name = unicodedata.name(chr(codepoint), "UNNAMED CHARACTER")
    target = unicodedata.name(ascii_char)
    return (
        f"Replace U+{codepoint:04X} {name} with U+{ord(ascii_char):04X} "
        f"{target} ({ascii_char!r})."
    )


def _token_at(line: str, index: int) -> str:
    start = index
    while start > 0 and not line[start - 1].isspace():
        start -= 1
    end = index + 1
    while end < len(line) and not line[end].isspace():
        end += 1
    return line[start:end]


def _line_has_ascii_letter(line: str) -> bool:
    return any("A" <= ch <= "Z" or "a" <= ch <= "z" for ch in line)


def classify(ch: str, prev: str | None, nxt: str | None, line: str, index: int):
    """Return (channel, change) or None if this character is allowed."""
    codepoint = ord(ch)
    category = unicodedata.category(ch)

    if ch in "\n\r\t":
        return None

    if 0xE0001 <= codepoint <= 0xE007F:
        return (
            "unicode-tag",
            _delete(
                codepoint,
                "Unicode tag characters can hide an ASCII payload. "
                "Delete every tag character in the sequence.",
            ),
        )

    if codepoint in {0x202A, 0x202B, 0x202C, 0x202D, 0x202E, 0x2066, 0x2067, 0x2068, 0x2069}:
        return (
            "bidi-control",
            _delete(
                codepoint,
                "Bidirectional controls can reorder how a line looks versus how it is stored. "
                "Delete this character.",
            ),
        )

    if ch == ZWJ and _is_symbol(prev) and _is_symbol(nxt):
        return None

    # U+FE00-U+FE0F are nonspacing marks, not format characters. U+FE0E and
    # U+FE0F are the emoji/text presentation selectors and are kept only when
    # they follow a symbol. Any other use is a hidden-character channel.
    if 0xFE00 <= codepoint <= 0xFE0F:
        if codepoint in EMOJI_VARIATION_SELECTORS and _is_symbol(prev):
            return None
        return (
            "variation-selector",
            _delete(
                codepoint,
                "A variation selector is only kept when U+FE0E or U+FE0F immediately "
                "follows an emoji or other symbol. Delete this one.",
            ),
        )

    if category == "Cf" or codepoint in {0x00AD, 0x034F, 0x180E}:
        if codepoint == 0xFEFF:
            why = (
                "It is invisible. If it is the first character, the file has a "
                "byte-order mark; save the file as UTF-8 without a BOM."
            )
        else:
            why = "It is invisible or ignored when the text is displayed, so delete it."
        return ("invisible-format", _delete(codepoint, why))

    if 0xE0100 <= codepoint <= 0xE01EF:
        return (
            "variation-selector",
            _delete(codepoint, "Variation selectors in this range are a hidden-character channel."),
        )

    if category == "Co" or (0xF0000 <= codepoint <= 0xFFFFD) or (0x100000 <= codepoint <= 0x10FFFD):
        return (
            "private-use",
            _delete(codepoint, "Private-use characters are not standard text. Delete this character."),
        )

    if category == "Cc":
        return (
            "disallowed-control",
            _delete(
                codepoint,
                "Control characters other than tab and newline do not belong in this file.",
            ),
        )

    if category == "Zs" and ch != " ":
        return ("unusual-space", _replace_space(codepoint))

    if codepoint == 0xFFFD:
        return (
            "replacement-character",
            _delete(
                codepoint,
                "U+FFFD means a byte sequence was not valid text. "
                "Replace this spot with the character that was intended.",
            ),
        )

    ascii_char = COVERT_CONFUSABLES.get(ch)
    if ascii_char is not None:
        token = _token_at(line, index)
        mixed = any("A" <= item <= "Z" or "a" <= item <= "z" for item in token)
        isolated = len(token) == 1
        swapped_word = not mixed and _line_has_ascii_letter(line)
        if mixed or isolated or swapped_word:
            return ("lookalike-letter", _replace_letter(codepoint, ascii_char))
        return None

    stylized = _ascii_letter(ch)
    if stylized is not None:
        token = _token_at(line, index)
        mixed = any(("A" <= item <= "Z" or "a" <= item <= "z" or item.isdigit()) and item.isascii() for item in token)
        if mixed:
            return ("lookalike-letter", _replace_letter(codepoint, stylized))
    return None


def _context(line: str, column: int) -> str:
    index = column - 1
    visible = []
    for i, ch in enumerate(line):
        if i == index:
            visible.append("[HERE]")
            continue
        if ch.isprintable() and ch != "\t":
            visible.append(ch)
        elif ch == "\t":
            visible.append("\\t")
        else:
            visible.append(f"[U+{ord(ch):04X}]")
    text = "".join(visible)
    marker = "[HERE]"
    at = text.find(marker)
    start = max(0, at - 36)
    end = min(len(text), at + len(marker) + 36)
    snippet = text[start:end]
    if start > 0:
        snippet = "..." + snippet
    if end < len(text):
        snippet = snippet + "..."
    return snippet


def iter_lines(text: str):
    """Yield (line_number, line_without_ending) for LF, CRLF, and CR endings."""
    line_number = 1
    start = 0
    i = 0
    length = len(text)
    while i < length:
        ch = text[i]
        if ch == "\n":
            yield line_number, text[start:i]
            line_number += 1
            i += 1
            start = i
            continue
        if ch == "\r":
            yield line_number, text[start:i]
            line_number += 1
            i += 2 if i + 1 < length and text[i + 1] == "\n" else 1
            start = i
            continue
        i += 1
    if start < length or text.endswith(("\n", "\r")):
        if start <= length:
            yield line_number, text[start:]


def scan_text(path: str, text: str) -> list[Finding]:
    findings = []
    for line_number, line in iter_lines(text):
        for index, ch in enumerate(line):
            prev = line[index - 1] if index > 0 else None
            nxt = line[index + 1] if index + 1 < len(line) else None
            classified = classify(ch, prev, nxt, line, index)
            if classified is None:
                continue
            channel, change = classified
            column = index + 1
            findings.append(
                Finding(
                    path,
                    line_number,
                    column,
                    ord(ch),
                    channel,
                    change,
                    _context(line, column),
                )
            )
    return findings


def _should_scan(filename: str) -> bool:
    if filename in SKIP_FILES:
        return False
    if filename in TEXT_NAMES:
        return True
    return os.path.splitext(filename)[1].lower() in TEXT_EXTENSIONS


def scan_path(path: str) -> list[Finding]:
    rel = os.path.relpath(path, REPO_ROOT)
    try:
        data = open(path, "rb").read()
    except OSError as exc:
        return [
            Finding(
                rel,
                1,
                1,
                0,
                "unreadable",
                f"Could not read this file ({exc}). Restore it as UTF-8 text or remove it from the scan set.",
                "",
            )
        ]
    if b"\0" in data:
        return []
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        return [
            Finding(
                rel,
                1,
                exc.start + 1,
                0,
                "not-utf8",
                (
                    f"Byte offset {exc.start} is not valid UTF-8 ({exc.reason}). "
                    "Re-save the file as UTF-8 without a byte-order mark, "
                    "and replace the invalid byte with the character that was intended."
                ),
                "",
            )
        ]
    return scan_text(rel, text)


def iter_repo_files():
    for dirpath, dirnames, filenames in os.walk(REPO_ROOT):
        dirnames[:] = sorted(name for name in dirnames if name not in SKIP_DIRS)
        for filename in sorted(filenames):
            if not _should_scan(filename):
                continue
            yield os.path.join(dirpath, filename)


def collect(paths: list[str] | None) -> list[Finding]:
    if paths:
        findings = []
        for path in paths:
            findings.extend(scan_path(os.path.abspath(path)))
        return findings
    findings = []
    for path in iter_repo_files():
        findings.extend(scan_path(path))
    return findings


OUT_OF_SCOPE = """
Not a failure, because there is no character to edit:
  Word-choice watermarks (SynthID-Text, Kirchenbauer green-list marks, and the
  keyed statistical mark described for Claude) do not change Unicode or
  whitespace. A detector needs the vendor secret. Public code:
  https://github.com/google-deepmind/synthid-text
  That detector does not work without the key, and no Claude detector key is
  published. This check does not paraphrase text to chase that signal.
""".strip()


def render_report(findings: list[Finding]) -> str:
    if not findings:
        return (
            "No covert Unicode or unusual whitespace marks in the scanned text.\n"
            + OUT_OF_SCOPE
        )
    lines = [
        f"Content mark check failed: {len(findings)} edit(s) required.",
        "This check does not rewrite files. Apply each change below and rerun.",
        "",
    ]
    for index, finding in enumerate(findings, 1):
        lines.append(f"{index}. {finding.render()}")
        lines.append("")
    lines.append(OUT_OF_SCOPE)
    return "\n".join(lines)


def _self_test() -> int:
    failures = []

    def expect(label, text, check):
        findings = scan_text("fixture", text)
        if not check(findings):
            rendered = "\n".join(item.render() for item in findings) or "(no findings)"
            failures.append(f"{label}\n{rendered}")

    expect(
        "zero-width space",
        "ab\u200bcd",
        lambda found: (
            len(found) == 1
            and found[0].line == 1
            and found[0].column == 3
            and found[0].codepoint == 0x200B
            and found[0].change.startswith("Delete U+200B")
        ),
    )
    expect(
        "second line",
        "ok\n\u200b",
        lambda found: len(found) == 1 and found[0].line == 2 and found[0].column == 1,
    )
    expect(
        "unusual space",
        "hello\u00a0world",
        lambda found: len(found) == 1 and "U+0020" in found[0].change and found[0].codepoint == 0x00A0,
    )
    expect(
        "tag characters",
        "\U000e0068\U000e0069",
        lambda found: len(found) == 2 and all(item.channel == "unicode-tag" for item in found),
    )
    expect(
        "bidi override",
        "ok \u202etx",
        lambda found: len(found) == 1 and found[0].channel == "bidi-control",
    )
    expect(
        "lookalike inside a word",
        "caf\u0435",
        lambda found: len(found) == 1 and "U+0435" in found[0].change and "'e'" in found[0].change,
    )
    expect(
        "emoji variation selector stays",
        "\u2705\ufe0f ok",
        lambda found: found == [],
    )
    expect(
        "variation selector after a letter",
        "a\ufe0f",
        lambda found: len(found) == 1 and found[0].codepoint == 0xFE0F,
    )
    expect(
        "ordinary prose stays",
        "An em dash \u2014, an accented \u00e9, and a check \u2713.\n",
        lambda found: found == [],
    )
    expect(
        "markdown hard break stays",
        "line with a break  \nnext\n",
        lambda found: found == [],
    )
    expect(
        "private use",
        "x\ue000y",
        lambda found: len(found) == 1 and found[0].channel == "private-use",
    )
    expect(
        "cr line endings are not marks",
        "one\rtwo\r",
        lambda found: found == [],
    )

    if failures:
        print("Self-test failed:", file=sys.stderr)
        print("\n\n".join(failures), file=sys.stderr)
        return 1
    print(f"Self-test passed ({12} fixtures).")
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Fail if text files contain covert Unicode or whitespace marks.",
    )
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="Run built-in fixtures and exit. Does not scan the repository.",
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help="Files to scan. Default: text files in this repository.",
    )
    args = parser.parse_args(argv)

    if args.self_test:
        return _self_test()

    findings = collect(args.paths or None)
    print(render_report(findings))
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
