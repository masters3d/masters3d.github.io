#!/usr/bin/env python3
"""Verify every code snippet used in the "Rust for Swift Practitioners" series.

This script is the single source of truth behind the series' promise that every
code block in a post is real: it (1) compiles and runs the authoritative snippet
files and checks their behavior, and (2) confirms that the code fences printed
in the blog posts are byte-identical to those authoritative files, so prose and
compiled code can never drift apart.

Layout (all paths relative to this file):

    rust/examples/<name>.rs        runnable Rust; stdout must equal
                                   rust/expected/<name>.out
    rust/compile_fail/<name>.rs    Rust that MUST be rejected; the compiler's
                                   stderr must contain rust/compile_fail/<name>.err
    swift/snippets/<name>.swift    runnable Swift; stdout must equal
                                   swift/expected/<name>.out
    swift/compile_fail/<name>.swift Swift that MUST be rejected; the compiler's
                                   stderr must contain swift/compile_fail/<name>.err

The sync check scans every post matching content/blog/rust-for-swift-*.md. Any
fenced block tagged exactly ```rust or ```swift must match one authoritative
snippet file. Fragments that are not meant to compile use ```text instead.

Usage:
    python3 verify.py              # everything (compile/run + sync)
    python3 verify.py --rust       # only the Rust snippets
    python3 verify.py --swift      # only the Swift snippets
    python3 verify.py --sync       # only the post<->file sync check

Exit code is non-zero if any check fails, so CI fails the build.
"""

from __future__ import annotations

import argparse
import glob
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
RUST_DIR = os.path.join(HERE, "rust")
SWIFT_DIR = os.path.join(HERE, "swift")
# content/blog lives two levels up from code-examples/ (zola-site/content/blog).
BLOG_DIR = os.path.join(HERE, os.pardir, "content", "blog")
SERIES_GLOB = os.path.join(BLOG_DIR, "rust-for-swift-*.md")


# --------------------------------------------------------------------------- #
# small helpers
# --------------------------------------------------------------------------- #
def _read(path: str) -> str:
    with open(path, "r", encoding="utf-8") as handle:
        return handle.read()


def _norm(text: str) -> str:
    """Normalize for comparison: strip a trailing newline and any leading or
    trailing blank lines, but keep the internal bytes exactly."""
    return text.replace("\r\n", "\n").strip("\n")


class Reporter:
    def __init__(self) -> None:
        self.failures: list[str] = []
        self.warnings: list[str] = []

    def ok(self, msg: str) -> None:
        print(f"  \u2713 {msg}")

    def fail(self, msg: str) -> None:
        print(f"  \u2717 {msg}")
        self.failures.append(msg)

    def warn(self, msg: str) -> None:
        print(f"  ! {msg}")
        self.warnings.append(msg)


# --------------------------------------------------------------------------- #
# Rust
# --------------------------------------------------------------------------- #
def verify_rust(rep: Reporter) -> None:
    print("Rust: runnable examples")
    if shutil.which("cargo") is None:
        rep.fail("cargo not found on PATH")
        return

    for src in sorted(glob.glob(os.path.join(RUST_DIR, "examples", "*.rs"))):
        name = os.path.splitext(os.path.basename(src))[0]
        expected_path = os.path.join(RUST_DIR, "expected", f"{name}.out")
        if not os.path.isfile(expected_path):
            rep.fail(f"examples/{name}.rs has no expected/{name}.out fixture")
            continue
        proc = subprocess.run(
            ["cargo", "run", "-q", "--example", name],
            cwd=RUST_DIR,
            capture_output=True,
            text=True,
        )
        if proc.returncode != 0:
            rep.fail(f"examples/{name}.rs failed to build/run:\n{proc.stderr}")
            continue
        if _norm(proc.stdout) != _norm(_read(expected_path)):
            rep.fail(
                f"examples/{name}.rs output mismatch\n"
                f"    expected: {_norm(_read(expected_path))!r}\n"
                f"    actual:   {_norm(proc.stdout)!r}"
            )
        else:
            rep.ok(f"examples/{name}.rs runs and matches expected output")

    print("Rust: compile-fail examples")
    if shutil.which("rustc") is None:
        rep.fail("rustc not found on PATH")
        return
    for src in sorted(glob.glob(os.path.join(RUST_DIR, "compile_fail", "*.rs"))):
        name = os.path.splitext(os.path.basename(src))[0]
        err_path = os.path.join(RUST_DIR, "compile_fail", f"{name}.err")
        if not os.path.isfile(err_path):
            rep.fail(f"compile_fail/{name}.rs has no {name}.err fixture")
            continue
        needle = _read(err_path).strip()
        with tempfile.TemporaryDirectory() as tmp:
            out = os.path.join(tmp, "out")
            proc = subprocess.run(
                ["rustc", "--edition", "2021", "--crate-type", "bin", "-o", out, src],
                capture_output=True,
                text=True,
            )
        if proc.returncode == 0:
            rep.fail(f"compile_fail/{name}.rs compiled but was expected to fail")
        elif needle not in proc.stderr:
            rep.fail(
                f"compile_fail/{name}.rs failed but not with the expected error\n"
                f"    expected substring: {needle!r}"
            )
        else:
            rep.ok(f"compile_fail/{name}.rs is rejected with the expected error")


# --------------------------------------------------------------------------- #
# Swift
# --------------------------------------------------------------------------- #
def verify_swift(rep: Reporter) -> None:
    print("Swift: runnable snippets")
    if shutil.which("swift") is None:
        rep.fail("swift not found on PATH")
        return

    for src in sorted(glob.glob(os.path.join(SWIFT_DIR, "snippets", "*.swift"))):
        name = os.path.splitext(os.path.basename(src))[0]
        expected_path = os.path.join(SWIFT_DIR, "expected", f"{name}.out")
        if not os.path.isfile(expected_path):
            rep.fail(f"snippets/{name}.swift has no expected/{name}.out fixture")
            continue
        proc = subprocess.run(
            ["swift", src], capture_output=True, text=True
        )
        if proc.returncode != 0:
            rep.fail(f"snippets/{name}.swift failed to build/run:\n{proc.stderr}")
            continue
        if _norm(proc.stdout) != _norm(_read(expected_path)):
            rep.fail(
                f"snippets/{name}.swift output mismatch\n"
                f"    expected: {_norm(_read(expected_path))!r}\n"
                f"    actual:   {_norm(proc.stdout)!r}"
            )
        else:
            rep.ok(f"snippets/{name}.swift runs and matches expected output")

    print("Swift: compile-fail snippets")
    if shutil.which("swiftc") is None:
        rep.fail("swiftc not found on PATH")
        return
    for src in sorted(glob.glob(os.path.join(SWIFT_DIR, "compile_fail", "*.swift"))):
        name = os.path.splitext(os.path.basename(src))[0]
        err_path = os.path.join(SWIFT_DIR, "compile_fail", f"{name}.err")
        if not os.path.isfile(err_path):
            rep.fail(f"compile_fail/{name}.swift has no {name}.err fixture")
            continue
        needle = _read(err_path).strip()
        # `-typecheck` can miss ownership diagnostics that only fire during full
        # compilation, so compile all the way to a throwaway binary.
        with tempfile.TemporaryDirectory() as tmp:
            out = os.path.join(tmp, "out")
            proc = subprocess.run(
                ["swiftc", "-o", out, src], capture_output=True, text=True
            )
        if proc.returncode == 0:
            rep.fail(f"compile_fail/{name}.swift compiled but was expected to fail")
        elif needle not in proc.stderr:
            rep.fail(
                f"compile_fail/{name}.swift failed but not with the expected error\n"
                f"    expected substring: {needle!r}"
            )
        else:
            rep.ok(f"compile_fail/{name}.swift is rejected with the expected error")


# --------------------------------------------------------------------------- #
# Post <-> file sync
# --------------------------------------------------------------------------- #
FENCE_RE = re.compile(r"^```([A-Za-z0-9_-]*)[^\n]*\n(.*?)^```", re.MULTILINE | re.DOTALL)


def _authoritative_snippets() -> dict[str, list[str]]:
    """Map normalized snippet content -> list of source file paths."""
    index: dict[str, list[str]] = {}
    patterns = [
        os.path.join(RUST_DIR, "examples", "*.rs"),
        os.path.join(RUST_DIR, "compile_fail", "*.rs"),
        os.path.join(SWIFT_DIR, "snippets", "*.swift"),
        os.path.join(SWIFT_DIR, "compile_fail", "*.swift"),
    ]
    for pattern in patterns:
        for path in glob.glob(pattern):
            index.setdefault(_norm(_read(path)), []).append(path)
    return index


def verify_sync(rep: Reporter) -> None:
    print("Sync: post code fences <-> authoritative snippet files")
    index = _authoritative_snippets()
    used: set[str] = set()
    posts = sorted(glob.glob(SERIES_GLOB))
    if not posts:
        rep.warn("no rust-for-swift-*.md posts found to sync yet")
    for post in posts:
        text = _read(post)
        for match in FENCE_RE.finditer(text):
            lang = match.group(1).lower()
            if lang not in ("rust", "swift"):
                continue  # ```text and friends are illustrative, not compiled
            body = _norm(match.group(2))
            if body in index:
                used.add(body)
                rep.ok(
                    f"{os.path.basename(post)}: a {lang} block matches "
                    f"{os.path.basename(index[body][0])}"
                )
            else:
                first_line = (body.splitlines() or ["<empty>"])[0]
                rep.fail(
                    f"{os.path.basename(post)}: a ```{lang} block does not match any "
                    f"snippet file under code-examples/ (starts: {first_line!r}). "
                    f"Add it as a real snippet, or tag it ```text if it is only "
                    f"illustrative."
                )
    for content, paths in index.items():
        if content not in used:
            rep.warn(
                f"snippet {os.path.basename(paths[0])} is verified but not shown "
                f"in any series post yet"
            )


# --------------------------------------------------------------------------- #
# main
# --------------------------------------------------------------------------- #
def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rust", action="store_true", help="verify Rust snippets")
    parser.add_argument("--swift", action="store_true", help="verify Swift snippets")
    parser.add_argument("--sync", action="store_true", help="check post/file sync")
    args = parser.parse_args()

    run_all = not (args.rust or args.swift or args.sync)
    rep = Reporter()

    if run_all or args.rust:
        verify_rust(rep)
    if run_all or args.swift:
        verify_swift(rep)
    if run_all or args.sync:
        verify_sync(rep)

    print()
    if rep.warnings:
        print(f"{len(rep.warnings)} warning(s).")
    if rep.failures:
        print(f"FAILED: {len(rep.failures)} check(s) did not pass.")
        return 1
    print("All snippet checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
