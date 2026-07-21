#!/usr/bin/env python3
"""Format and lint the blog Markdown with Prettier and markdownlint.

This is a thin, portable dispatcher. It does not implement any formatting logic
itself; it simply calls the two industry-standard tools that own that job:

  - Prettier          formats Markdown (wraps prose to `printWidth`, normalizes
                      tables, emphasis, spacing). Config: `.prettierrc.json`.
  - markdownlint-cli2 lints Markdown for structural issues. Config:
                      `.markdownlint-cli2.jsonc`.

Both tools are pinned in `package.json`; run `npm install` (or `npm ci`) once so
they are available under `node_modules`. The script works the same on Linux,
macOS and Windows because it invokes the tools through the local
`node_modules/.bin` (falling back to `npx`).

Why this preserves rendered output
-----------------------------------
Prettier is configured with `proseWrap: always` (wrap at 80 columns using
Markdown soft breaks, which render as spaces) and `embeddedLanguageFormatting:
off` (do not reformat sample code shown inside fenced blocks). With those
settings the generated HTML is byte-identical before and after formatting; only
the `.md` source line breaks change, which keeps diffs small.

Usage
-----
    python3 scripts/format_markdown.py            # fix: format + lint --fix
    python3 scripts/format_markdown.py --check     # verify only (used by CI)

In `--check` mode nothing is written; the script exits non-zero if any file is
not already formatted or has a lint violation, which fails the build.
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Only the blog Markdown is managed by this tool (its rendering has been
# verified to be unchanged by formatting).
MARKDOWN_GLOB = "zola-site/content/blog/**/*.md"


def _bin_path(name: str) -> str | None:
    """Return the local node_modules binary for `name`, honoring the
    platform-specific extension on Windows."""
    candidates = [name]
    if os.name == "nt":
        candidates = [name + ".cmd", name + ".exe", name]
    for cand in candidates:
        path = os.path.join(REPO_ROOT, "node_modules", ".bin", cand)
        if os.path.isfile(path):
            return path
    return None


def _resolve(tool: str):
    """Resolve how to invoke a tool: prefer the pinned local binary, then a
    globally installed one, then `npx`. Returns an argv prefix list or None."""
    local = _bin_path(tool)
    if local:
        return [local]
    on_path = shutil.which(tool)
    if on_path:
        return [on_path]
    npx = shutil.which("npx") or ("npx.cmd" if os.name == "nt" else None)
    if npx:
        return [npx, "--no-install", tool]
    return None


def _run(argv, label) -> int:
    print(f"$ {' '.join(argv)}")
    try:
        proc = subprocess.run(argv, cwd=REPO_ROOT)
    except OSError as exc:  # pragma: no cover - defensive
        print(f"ERROR: failed to run {label}: {exc}", file=sys.stderr)
        return 1
    return proc.returncode


def _missing_tools_message() -> str:
    return (
        "ERROR: Prettier / markdownlint-cli2 are not installed.\n"
        "Install the pinned tooling first:\n\n"
        "    npm install\n\n"
        "(They are dev dependencies declared in package.json.)"
    )


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Format and lint blog Markdown via Prettier + markdownlint.",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Do not modify files; exit non-zero if formatting or lint fails.",
    )
    args = parser.parse_args(argv)

    prettier = _resolve("prettier")
    markdownlint = _resolve("markdownlint-cli2")
    if prettier is None or markdownlint is None:
        print(_missing_tools_message(), file=sys.stderr)
        return 1

    if args.check:
        prettier_cmd = prettier + ["--check", MARKDOWN_GLOB]
        # markdownlint-cli2 is check-only by default (non-zero on violations).
        markdownlint_cmd = markdownlint + [MARKDOWN_GLOB]
    else:
        prettier_cmd = prettier + ["--write", MARKDOWN_GLOB]
        markdownlint_cmd = markdownlint + ["--fix", MARKDOWN_GLOB]

    print("== Prettier ==")
    rc_prettier = _run(prettier_cmd, "prettier")
    print("\n== markdownlint ==")
    rc_markdownlint = _run(markdownlint_cmd, "markdownlint-cli2")

    if rc_prettier != 0 or rc_markdownlint != 0:
        if args.check:
            print(
                "\nMarkdown is not correctly formatted. Run:\n"
                "    npm install && python3 scripts/format_markdown.py",
                file=sys.stderr,
            )
        return 1

    print(
        "\n✓ Markdown "
        + ("is correctly formatted and lint-clean." if args.check else "formatted and linted.")
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
