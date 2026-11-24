#!/usr/bin/env python3
"""Run `zola check`, rechecking links that failed with a transient error.

`zola check` fails on any external link it cannot load, including a valid
link whose host was briefly unavailable. Valid links to github.com,
gutenberg.org and frontiersin.org have each failed CI this way.

This script runs `zola check` in zola-site and passes its output through. If
zola failed only because some external links returned a server error (5xx),
a rate limit (429) or no response at all (a timeout or dropped connection),
it fetches those links again in up to three rounds, waiting 10, 30 and 60
seconds before each, and passes only if every one of them loads (2xx or 304,
with the #anchor on the page when the link has one). A GitHub file page
(github.com/OWNER/REPO/blob/...) that still fails is also tried on
raw.githubusercontent.com, which serves the same file.

Any other failure stands as zola reported it, and nothing is rechecked: a
404 or 403, a missing anchor, a broken internal link, a template error. No
link is skipped, so `skip_prefixes` in zola-site/config.toml is only for
hosts that keep failing automated checks.

Usage
-----
    python3 scripts/zola_check.py --self-test
    python3 scripts/zola_check.py
    python3 scripts/zola_check.py -- /tmp/zola check    # another zola binary
"""

from __future__ import annotations

import argparse
import contextlib
import http.client
import io
import os
import re
import subprocess
import sys
import time
import tomllib
import urllib.error
import urllib.request

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_DIR = os.path.join(REPO_ROOT, "zola-site")
CONFIG_PATH = os.path.join(SITE_DIR, "config.toml")

WAITS = (10, 30, 60)  # seconds to wait before each recheck round
PAUSE = 1  # seconds between requests
TIMEOUT = 30  # seconds per request, as in zola
BUDGET = 300  # seconds for all rounds, well inside the 15-minute job limits
# Send what zola sends, so hosts treat the recheck like the original check.
HEADERS = {"User-Agent": "zola/0.19.2", "Accept": "text/html, */*"}

ANSI_RE = re.compile(r"\x1b\[[0-9;]*m")
HEADER_RE = re.compile(r"^Error: Found (\d+) broken external link\(s\)$")
ITEM_RE = re.compile(r"^\s+(\d+)\. Broken link in (.+?) to (\S+?): (.+)$")
# zola's reasons for a server error, a rate limit, and no response at all.
TRANSIENT_RE = re.compile(
    r"^(?:Server error status code \(5\d\d "
    r"|Client error status code \(429 "
    r"|error sending request for url )"
)
BLOB_RE = re.compile(r"^https://github\.com/([^/?#]+)/([^/?#]+)/blob/([^?#]+)")
LABELS = {"ok": "loaded", "down": "still failing", "broken": "broken"}

FIX_BROKEN = (
    "Fix or replace each broken link. If a page loads in a browser but its host"
    "\nblocks automated checks (often with a 403), add the narrowest URL prefix"
    "\nto skip_prefixes in zola-site/config.toml with a comment saying why."
)
FIX_DOWN = (
    "If a page does not load in a browser either, fix or replace the link. If it"
    "\ndoes, its host may still be down: rerun the workflow later, and if it keeps"
    "\nfailing from CI, add the narrowest URL prefix to skip_prefixes in"
    "\nzola-site/config.toml with a comment saying why."
)


def run(command: list[str]) -> tuple[int, str]:
    """Run command in zola-site, echoing its output; return (exit code, output)."""
    lines = []
    with subprocess.Popen(
        command,
        cwd=SITE_DIR,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        encoding="utf-8",
        errors="replace",
    ) as process:
        for line in process.stdout:
            print(line, end="", flush=True)
            lines.append(line)
    return process.returncode, "".join(lines)


def parse(output: str) -> list[tuple[str, str, str]] | None:
    """Return (page, url, reason) for each broken external link zola listed.

    Return None when zola failed for any other reason (a broken internal link,
    a template error, a URL it could not parse), since only external links
    that failed to load can be rechecked.
    """
    lines = ANSI_RE.sub("", output).splitlines()
    errors = [line for line in lines if line.startswith(("Error: ", "Reason: "))]
    if len(errors) != 2 or errors[0] != "Error: Failed to check the site":
        return None
    header = HEADER_RE.match(errors[1])
    if not header:
        return None
    count = int(header.group(1))
    start = lines.index(errors[1]) + 1
    items = []
    for number, line in enumerate(lines[start : start + count], start=1):
        item = ITEM_RE.match(line)
        if not item or int(item.group(1)) != number:
            return None
        items.append((item.group(2), item.group(3), item.group(4)))
    return items if len(items) == count else None


def is_transient(reason: str) -> bool:
    """True when zola got a server error, a rate limit, or no response at all."""
    return TRANSIENT_RE.match(reason) is not None


def anchor_of(url: str) -> str | None:
    """Return the #fragment zola looks for on the page, if any."""
    _, sign, fragment = url.partition("#")
    if not sign or not fragment or fragment[0] in "/!":
        return None
    return fragment


def has_anchor(page: str, anchor: str) -> bool:
    """zola's test: an id or name attribute with that value, in any case."""
    pattern = r"""\s(?i:(?:id|name) *= *(?:"|')*""" + re.escape(anchor) + r"""(?:"|'| |>)+)"""
    return re.search(pattern, page) is not None


def anchor_skips() -> list[str]:
    """Return zola's skip_anchor_prefixes, so rechecks skip the same anchors."""
    with open(CONFIG_PATH, "rb") as handle:
        config = tomllib.load(handle)
    return config.get("link_checker", {}).get("skip_anchor_prefixes", [])


def raw_url(url: str) -> str | None:
    """Return the raw.githubusercontent.com URL of a GitHub file page, if url is one."""
    match = BLOB_RE.match(url)
    if not match or anchor_of(url):
        return None
    owner, repo, rest = match.groups()
    return f"https://raw.githubusercontent.com/{owner}/{repo}/{rest}"


def fetch(url: str, anchor: str | None = None) -> tuple[str, str]:
    """Load url once; return ("ok" | "down" | "broken", what happened)."""
    request = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
            status = response.status
            body = response.read() if anchor else b""
    except urllib.error.HTTPError as error:
        status, body = error.code, b""
        error.close()
    except ValueError as error:
        return "broken", f"not a valid URL ({error})"
    except (OSError, http.client.HTTPException) as error:
        return "down", f"no response ({error})"
    if status == 429 or status >= 500:
        return "down", f"HTTP {status}"
    if not (200 <= status < 300 or status == 304):
        return "broken", f"HTTP {status}"
    if anchor:
        try:
            page = body.decode("utf-8")
        except UnicodeDecodeError:
            return "broken", f"HTTP {status}, but the page is not valid UTF-8"
        if not has_anchor(page, anchor):
            return "broken", f"HTTP {status}, but anchor #{anchor} is not on the page"
    return "ok", f"HTTP {status}"


def recheck(
    links: dict[str, str], skips: list[str], fetch=fetch, sleep=time.sleep, clock=time.monotonic
) -> tuple[dict[str, str], dict[str, str]]:
    """Fetch links again in rounds; return {url: error} for broken and still-down links."""
    down = dict(links)
    broken: dict[str, str] = {}
    deadline = clock() + BUDGET
    for number, wait in enumerate(WAITS, start=1):
        if not down or broken:
            break
        if clock() + wait >= deadline:
            print(f"\nStopped rechecking: the {BUDGET}s time budget is used up.")
            break
        print(
            f"\nRound {number} of {len(WAITS)}: waiting {wait}s, then rechecking"
            f" {len(down)} link(s)...",
            flush=True,
        )
        sleep(wait)
        for url in list(down):
            if clock() >= deadline:
                break
            anchor = None if url.startswith(tuple(skips)) else anchor_of(url)
            state, detail = fetch(url, anchor)
            raw = raw_url(url)
            if state == "down" and raw:
                sleep(PAUSE)
                raw_state, raw_detail = fetch(raw)
                if raw_state == "ok":
                    state = "ok"
                detail += f"; raw.githubusercontent.com: {raw_detail}"
            print(f"  {LABELS[state]}: {url} ({detail})", flush=True)
            if state == "down":
                down[url] = detail
            else:
                del down[url]
                if state == "broken":
                    broken[url] = detail
            sleep(PAUSE)
    return broken, down


def relative(path: str) -> str:
    """Return path relative to the repo root when it is inside the repo."""
    rel = os.path.relpath(path, REPO_ROOT)
    return path if rel.startswith("..") else rel


def check(command: list[str], fetch=fetch, sleep=time.sleep, clock=time.monotonic) -> int:
    try:
        code, output = run(command)
    except FileNotFoundError:
        print(
            f"ERROR: could not run {command[0]!r}. Install zola 0.19.2 (the version"
            "\npinned in .github/workflows/static.yml) or pass another binary after --."
        )
        return 127
    if code == 0:
        return 0
    items = parse(output)
    if items is None:
        print(
            "\nzola check failed for a reason other than external links it could not"
            "\nload (see above), so nothing was rechecked."
        )
        return code

    pages: dict[str, list[str]] = {}
    reasons: dict[str, str] = {}
    for page, url, reason in items:
        pages.setdefault(url, [])
        if relative(page) not in pages[url]:
            pages[url].append(relative(page))
        reasons.setdefault(url, reason)

    def show(failures: dict[str, str]) -> None:
        for url, detail in failures.items():
            print(f"  {url}\n    {detail}")
            for page in pages[url]:
                print(f"    in {page}")

    permanent = {url: reason for url, reason in reasons.items() if not is_transient(reason)}
    if permanent:
        print(
            f"\nERROR: {len(permanent)} link(s) failed with something other than a"
            " server error, rate limit or timeout, so nothing was rechecked:"
        )
        show(permanent)
        print("\n" + FIX_BROKEN)
        return code

    print(
        f"\nzola could not load {len(reasons)} link(s) because of a server error,"
        " rate limit or timeout. Rechecking them before failing."
    )
    broken, down = recheck(reasons, anchor_skips(), fetch, sleep, clock)
    if broken or down:
        print(f"\nERROR: {len(broken) + len(down)} link(s) still fail after rechecking:")
        show({**broken, **down})
        if broken:
            print("\n" + FIX_BROKEN)
        if down:
            print("\n" + FIX_DOWN)
        return code
    print(f"\n✓ All {len(reasons)} link(s) loaded on recheck, so the link check passes.")
    if os.environ.get("GITHUB_ACTIONS") == "true":
        print(
            f"::warning title=Links rechecked::zola check could not load {len(reasons)}"
            " link(s) at first (server error, rate limit or timeout); all loaded on recheck."
        )
    return 0


def self_test() -> int:
    page = "/home/runner/work/site/site/zola-site/content/blog/a.md"
    other = "/home/runner/work/site/site/zola-site/content/blog/b.md"
    blob = "https://github.com/masters3d/ingenio/blob/main/AGENTS.md"
    raw = "https://raw.githubusercontent.com/masters3d/ingenio/main/AGENTS.md"
    book = "https://www.penguinrandomhouse.com/books/208668/good-strategy-bad-strategy-by-richard-rumelt/"
    s503 = "Server error status code (503 Service Unavailable) received"
    s429 = "Client error status code (429 Too Many Requests) received"
    s404 = "Client error status code (404 Not Found) received"
    timeout = f"error sending request for url ({book}): operation timed out"

    def zola_output(*items: tuple[str, str, str]) -> str:
        """What zola 0.19.2 prints when these (page, url, reason) links fail."""
        lines = [
            "Checking site...",
            "Checking 205 external link(s). Skipping 71 external link(s).",
            f"> Checked 205 external link(s): {len(items)} error(s) found.",
            "Error: Failed to check the site",
            f"Error: Found {len(items)} broken external link(s)",
        ]
        lines += [f"  {n}. Broken link in {p} to {u}: {r}" for n, (p, u, r) in enumerate(items, 1)]
        return "\n".join(lines) + "\n"

    output = zola_output((page, blob, s503), (other, blob, s503), (page, book, timeout))
    expected = [(page, blob, s503), (other, blob, s503), (page, book, timeout)]
    assert parse(output) == expected, "every broken link must be listed"
    colored = output.replace("Error: ", "\x1b[1;31mError: \x1b[0m")
    assert parse(colored) == expected, "terminal colors must be ignored"
    assert parse(output.replace("Found 3", "Found 4")) is None, "count mismatch"
    internal = (
        "Error: Failed to check the site\n"
        "Error: Found 1 broken internal anchor link(s)\n"
        "  1. The anchor in the link `@/blog/b.md#x` in content/blog/a.md does not exist.\n"
    )
    assert parse(internal) is None, "internal link errors are not rechecked"
    unparsable = (
        "Error: Failed to check the site\n"
        "Error: Found 1 broken external link(s)\n"
        "  1. could not parse domain `https:///x` from link\n"
    )
    assert parse(unparsable) is None, "unparsable URLs are not rechecked"

    for reason in (s503, s429, timeout):
        assert is_transient(reason), reason
    for reason in (
        s404,
        "Anchor `#x` not found on page",
        "Redirection status code (308 Permanent Redirect) received",
        "The page didn't return valid UTF-8",
    ):
        assert not is_transient(reason), reason

    assert raw_url(blob) == raw and raw_url(blob + "?plain=1") == raw
    assert raw_url(blob + "#L3") is None, "raw files have no anchors"
    assert raw_url("https://github.com/o/r/tree/main/docs") is None
    assert raw_url(book) is None
    assert anchor_of(book + "#x") == "x"
    assert anchor_of(book) is None and anchor_of(book + "#") is None
    assert anchor_of(book + "#/route") is None and anchor_of(book + "#!x") is None
    assert has_anchor('<h2 id="kernel">', "kernel")
    assert has_anchor("<a NAME='Kernel' href>", "kernel")
    assert not has_anchor('<h2 id="kernels">', "kernel")

    def run_check(text: str, code: int, answers: dict, cost: float = 0):
        """Run check() with zola replaced by a command printing text, and no network."""
        fetched: list[str] = []
        now = [0.0]

        def fake_fetch(url: str, anchor: str | None = None) -> tuple[str, str]:
            fetched.append(url)
            now[0] += cost
            queue = answers[url]
            return queue.pop(0) if len(queue) > 1 else queue[0]

        def fake_sleep(seconds: float) -> None:
            now[0] += seconds

        script = "import sys; print(sys.argv[1], end=''); sys.exit(int(sys.argv[2]))"
        printed = io.StringIO()
        with contextlib.redirect_stdout(printed):
            result = check(
                [sys.executable, "-c", script, text, str(code)],
                fake_fetch,
                fake_sleep,
                lambda: now[0],
            )
        return result, fetched, printed.getvalue()

    ok, down, gone = ("ok", "HTTP 200"), ("down", "HTTP 503"), ("broken", "HTTP 404")
    rounds = len(WAITS)

    result, fetched, _ = run_check("Checking site...\n", 0, {})
    assert (result, fetched) == (0, []), "a passing check is left alone"
    result, fetched, _ = run_check("Error: Failed to build the site\n", 3, {})
    assert (result, fetched) == (3, []), "other failures keep zola's exit code"
    result, fetched, _ = run_check(internal, 1, {})
    assert (result, fetched) == (1, []), "internal link errors fail as zola reported"

    result, fetched, _ = run_check(output, 1, {blob: [ok], book: [down, ok]})
    assert (result, fetched) == (0, [blob, book, book]), "links that load again pass"

    result, fetched, out = run_check(zola_output((page, blob, s503), (page, book, s404)), 1, {})
    assert (result, fetched) == (1, []), "a 404 fails without any recheck"
    assert "nothing was rechecked" in out and "skip_prefixes" in out

    result, fetched, out = run_check(zola_output((page, book, timeout)), 1, {book: [down]})
    assert (result, fetched) == (1, [book] * rounds), "a link that stays down fails"
    assert "still fail" in out and "rerun" in out
    slow = "https://example.com/slow"
    result, fetched, _ = run_check(
        zola_output((page, book, timeout), (page, slow, timeout)), 1, {book: [gone], slow: [down]}
    )
    assert (result, fetched) == (1, [book, slow]), "a link gone on recheck ends the recheck"

    result, fetched, _ = run_check(zola_output((page, blob, s503)), 1, {blob: [down], raw: [ok]})
    assert (result, fetched) == (0, [blob, raw]), "a GitHub file served raw passes"
    result, fetched, _ = run_check(zola_output((page, blob, s503)), 1, {blob: [down], raw: [gone]})
    assert (result, fetched) == (1, [blob, raw] * rounds), "a missing raw file never passes"

    many = [(page, f"https://example.com/{n}", timeout) for n in range(20)]
    result, fetched, out = run_check(
        zola_output(*many), 1, {url: [down] for _, url, _ in many}, cost=TIMEOUT
    )
    assert result == 1 and len(fetched) <= BUDGET // TIMEOUT + 1, "rechecks stop at the budget"
    assert "time budget" in out
    print("\nself-test passed")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument(
        "command",
        nargs=argparse.REMAINDER,
        help="command to run in zola-site instead of `zola check`, after --",
    )
    args = parser.parse_args()
    if args.self_test:
        return self_test()
    command = args.command[1:] if args.command[:1] == ["--"] else args.command
    return check(command or ["zola", "check"])


if __name__ == "__main__":
    sys.exit(main())
