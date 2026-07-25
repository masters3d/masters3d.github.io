#!/usr/bin/env python3
"""Generate deterministic Compiler Explorer ("godbolt") "Run" links for the
"Rust for Swift Practitioners" series.

The blog never adds a live code runner; instead every runnable snippet gets a
click-through link to Compiler Explorer with the exact source pre-loaded, so a
reader can run or tweak it themselves. The source encoded into each link is the
*same* authoritative file that verify.py compiles and runs, which means a link
can never point at code different from what CI proved works.

How it works
------------
Compiler Explorer restores an editor session from a URL of the form

    https://godbolt.org/clientstate/<base64-of-clientstate-json>

The route captures everything after ``/clientstate/`` and decodes it with
Node's ``Buffer.from(x, 'base64')`` (which also accepts the URL-safe alphabet),
so we emit URL-safe base64 and never make a network call at build time. The
clientstate schema (sessions -> source/language/executors) is defined by
Compiler Explorer's ``lib/clientstate.ts``.

This module is the single source of truth for those links. It writes
``godbolt-links.json`` (consumed by the ``compiler_explorer`` Zola shortcode)
and verify.py checks that the committed file still matches what this script
would generate, exactly like the post<->snippet byte-sync check.

Usage
-----
    python3 godbolt.py            # regenerate godbolt-links.json
    python3 godbolt.py --check    # exit non-zero if the committed file is stale
    python3 godbolt.py --print    # print every id -> URL (no writes)

Refreshing the pinned compilers
-------------------------------
``COMPILER_IDS`` pins Compiler Explorer's current default compiler for each
language. If a link should track a newer toolchain, refresh with e.g.

    curl 'https://godbolt.org/api/compilers/rust?fields=id,name'

and update the id below, then re-run ``python3 godbolt.py``.
"""

from __future__ import annotations

import argparse
import base64
import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RUST_DIR = os.path.join(HERE, "rust")
SWIFT_DIR = os.path.join(HERE, "swift")
LINKS_JSON = os.path.join(HERE, "godbolt-links.json")

GODBOLT_BASE = "https://godbolt.org"

# Compiler Explorer's current default compiler per language
# (etc/config/<lang>.amazon.properties -> defaultCompiler). Pinned so links are
# deterministic; see the module docstring for how to refresh.
COMPILER_IDS = {"rust": "r1970", "swift": "swift633"}
# Extra compiler arguments per language. Rust snippets are edition-2021 (matching
# how verify.py compiles them with `rustc --edition 2021`).
COMPILER_OPTIONS = {"rust": "--edition=2021", "swift": ""}

LANG_BY_EXT = {".rs": "rust", ".swift": "swift"}

# All four snippet kinds verify.py already compiles/runs.
SNIPPET_GLOBS = [
    os.path.join(RUST_DIR, "examples", "*.rs"),
    os.path.join(RUST_DIR, "compile_fail", "*.rs"),
    os.path.join(SWIFT_DIR, "snippets", "*.swift"),
    os.path.join(SWIFT_DIR, "compile_fail", "*.swift"),
]

# Side-by-side comparison links: each opens one Compiler Explorer tab per
# snippet, so a reader sees the Swift and Rust versions running next to each
# other. Each entry is (link id, [snippet basename per session]).
PAIRS = [
    ("point-value-vs-copy", ["value_struct_copy", "derive_copy_struct"]),
    ("scalar-copy-both", ["int_value_copy", "copy_scalars"]),
    ("consume-twice", ["noncopyable_use_after_consume", "use_after_move"]),
]


def _read(path: str) -> str:
    with open(path, "r", encoding="utf-8") as handle:
        return handle.read()


def _lang_for(path: str) -> str:
    ext = os.path.splitext(path)[1]
    try:
        return LANG_BY_EXT[ext]
    except KeyError as exc:  # pragma: no cover - guards future new extensions
        raise ValueError(f"no language mapped for extension {ext!r} ({path})") from exc


def _session(source: str, lang: str, sid: int) -> dict:
    """A single Compiler Explorer editor session that runs `source`.

    Uses an executor pane (program output) rather than an assembly view, since
    the point of these links is to run the snippet and see what it prints (or,
    for the compile-fail snippets, the exact error the post promises).
    """
    return {
        "id": sid,
        "language": lang,
        "source": source,
        "compilers": [],
        "executors": [
            {
                "compiler": {
                    "id": COMPILER_IDS[lang],
                    "options": COMPILER_OPTIONS[lang],
                },
                "arguments": "",
                "stdin": "",
            }
        ],
    }


def _encode(state: dict) -> str:
    # Compact + sorted so the same inputs always produce the same URL.
    payload = json.dumps(state, separators=(",", ":"), sort_keys=True, ensure_ascii=False)
    encoded = base64.urlsafe_b64encode(payload.encode("utf-8")).decode("ascii")
    return f"{GODBOLT_BASE}/clientstate/{encoded}"


def url_for_sources(sources: list[tuple[str, str]]) -> str:
    """Build a clientstate URL that opens one session per (source, lang)."""
    state = {
        "sessions": [
            _session(source, lang, i + 1) for i, (source, lang) in enumerate(sources)
        ]
    }
    return _encode(state)


def _discover_snippets() -> dict[str, str]:
    """Map snippet basename (no extension) -> absolute path.

    Basenames are the stable id used by the shortcode, so they must be unique
    across all snippet directories.
    """
    index: dict[str, str] = {}
    for pattern in SNIPPET_GLOBS:
        for path in sorted(glob.glob(pattern)):
            name = os.path.splitext(os.path.basename(path))[0]
            if name in index:
                raise ValueError(
                    f"duplicate snippet basename {name!r}: {index[name]} and {path}"
                )
            index[name] = path
    return index


def build_links() -> dict:
    """Return the full godbolt-links.json data structure."""
    snippets = _discover_snippets()

    singles: dict[str, dict] = {}
    for name, path in snippets.items():
        lang = _lang_for(path)
        singles[name] = {"lang": lang, "url": url_for_sources([(_read(path), lang)])}

    pairs: dict[str, dict] = {}
    for link_id, members in PAIRS:
        sources: list[tuple[str, str]] = []
        for member in members:
            if member not in snippets:
                raise ValueError(
                    f"pair {link_id!r} references unknown snippet {member!r}"
                )
            path = snippets[member]
            sources.append((_read(path), _lang_for(path)))
        pairs[link_id] = {"snippets": members, "url": url_for_sources(sources)}

    return {
        "_comment": (
            "GENERATED by code-examples/godbolt.py from the verified snippet "
            "files; do not edit by hand. Run `python3 godbolt.py` to refresh."
        ),
        "singles": singles,
        "pairs": pairs,
    }


def expected_file_text() -> str:
    """The exact text godbolt-links.json should contain (deterministic)."""
    return json.dumps(build_links(), indent=2, sort_keys=True) + "\n"


def write_file() -> None:
    with open(LINKS_JSON, "w", encoding="utf-8") as handle:
        handle.write(expected_file_text())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="exit non-zero if godbolt-links.json is missing or stale",
    )
    parser.add_argument(
        "--print",
        dest="do_print",
        action="store_true",
        help="print every id -> URL without writing any file",
    )
    args = parser.parse_args()

    if args.do_print:
        data = build_links()
        for name, entry in sorted(data["singles"].items()):
            print(f"{name} ({entry['lang']}):\n  {entry['url']}")
        for link_id, entry in sorted(data["pairs"].items()):
            print(f"[pair] {link_id} ({'+'.join(entry['snippets'])}):\n  {entry['url']}")
        return 0

    expected = expected_file_text()
    if args.check:
        if not os.path.isfile(LINKS_JSON):
            print("godbolt-links.json is missing; run `python3 godbolt.py`")
            return 1
        if _read(LINKS_JSON) != expected:
            print("godbolt-links.json is stale; run `python3 godbolt.py`")
            return 1
        print("godbolt-links.json is up to date.")
        return 0

    write_file()
    print(f"Wrote {os.path.relpath(LINKS_JSON, HERE)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
