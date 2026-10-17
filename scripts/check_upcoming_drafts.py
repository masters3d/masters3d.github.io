#!/usr/bin/env python3
"""Fail when a draft blog post is due within the review window.

Upcoming posts are kept as drafts (``draft = true``) with the date they are
meant to go out. Zola skips drafts, so a draft whose date arrives simply never
appears, and nobody notices. This check turns that into a hard stop: if any
draft is dated within the next ``--days`` days (default 7), or its date has
already passed, the check fails and the deploy stops until the post is either
published (remove ``draft = true``) or rescheduled (move its ``date``).

It also prints the upcoming draft queue by month, so the runway of planned
posts is visible on every run. It does not rewrite files.

Usage
-----
    python3 scripts/check_upcoming_drafts.py --self-test
    python3 scripts/check_upcoming_drafts.py
    python3 scripts/check_upcoming_drafts.py --days 14 --today 2027-01-01
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import sys
import tempfile
from collections import Counter

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOG_DIR = os.path.join(REPO_ROOT, "zola-site", "content", "blog")

DATE_RE = re.compile(r'^date\s*=\s*"?(\d{4}-\d{2}-\d{2})')
DRAFT_RE = re.compile(r"^draft\s*=\s*true\s*$")


def read_front_matter(path: str) -> list[str]:
    """Return the top-level TOML front matter lines (before any [table])."""
    with open(path, encoding="utf-8") as handle:
        lines = handle.read().splitlines()
    if not lines or lines[0].strip() != "+++":
        return []
    out = []
    for line in lines[1:]:
        stripped = line.strip()
        if stripped == "+++" or stripped.startswith("["):
            break
        out.append(stripped)
    return out


def scan(blog_dir: str) -> list[tuple[dt.date, str]]:
    """Return (date, filename) for every draft post that has a date."""
    drafts = []
    for name in sorted(os.listdir(blog_dir)):
        if not name.endswith(".md") or name == "_index.md":
            continue
        front = read_front_matter(os.path.join(blog_dir, name))
        if not any(DRAFT_RE.match(line) for line in front):
            continue
        for line in front:
            match = DATE_RE.match(line)
            if match:
                drafts.append((dt.date.fromisoformat(match.group(1)), name))
                break
    return sorted(drafts)


def check(blog_dir: str, today: dt.date, days: int) -> int:
    drafts = scan(blog_dir)
    cutoff = today + dt.timedelta(days=days)
    due = [(date, name) for date, name in drafts if date <= cutoff]

    print(f"Draft queue as of {today} ({len(drafts)} drafts):")
    for month, count in sorted(Counter(d.strftime("%Y-%m") for d, _ in drafts).items()):
        print(f"  {month}: {count}")
    if drafts:
        print(f"Runway ends {drafts[-1][0]}.")

    if not due:
        print(f"OK: no draft is dated on or before {cutoff} ({days}-day window).")
        return 0

    print(f"\nERROR: {len(due)} draft(s) dated on or before {cutoff}:")
    for date, name in due:
        state = "overdue" if date < today else "due"
        print(f"  zola-site/content/blog/{name}: date = {date} ({state})")
    print(
        "\nFor each one, either publish it (delete the `draft = true` line)"
        "\nor reschedule it (move `date` past the window), then push again."
    )
    return 1


def self_test() -> int:
    today = dt.date(2027, 1, 1)
    with tempfile.TemporaryDirectory() as tmp:
        def write(name: str, date: str, draft: bool) -> None:
            body = f'+++\ntitle = "t"\ndate = "{date}"\n'
            body += "draft = true\n" if draft else ""
            body += '[extra]\ndraft = true\n+++\nbody\n'
            with open(os.path.join(tmp, name), "w", encoding="utf-8") as handle:
                handle.write(body)

        write("published-soon.md", "2027-01-02", draft=False)
        write("far-draft.md", "2027-03-01", draft=True)
        assert check(tmp, today, 7) == 0, "far draft must pass"
        write("near-draft.md", "2027-01-08", draft=True)
        assert check(tmp, today, 7) == 1, "draft on the cutoff must fail"
        assert check(tmp, today, 6) == 0, "draft past a shorter window must pass"
        write("old-draft.md", "2026-12-01", draft=True)
        assert check(tmp, today, 0) == 1, "overdue draft must fail"
    print("\nself-test passed")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--days", type=int, default=7, help="review window in days")
    parser.add_argument("--today", type=dt.date.fromisoformat, default=None)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        return self_test()
    today = args.today or dt.datetime.now(dt.timezone.utc).date()
    return check(BLOG_DIR, today, args.days)


if __name__ == "__main__":
    sys.exit(main())
