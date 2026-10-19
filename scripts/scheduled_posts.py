#!/usr/bin/env python3
"""Hold reviewed posts off the live site until their date.

A post the author has reviewed but wants released later drops ``draft = true``
and gets a ``scheduled`` flag under ``[extra]``, keeping its release ``date``:

    +++
    title = "..."
    date = "2026-11-01"
    ...
    [extra]
    scheduled = true
    +++

Zola has no publish-on-date feature: a non-draft post is built as soon as the
site is built. So the deploy workflow runs this script with ``--hide`` before
``zola build``. It adds ``draft = true`` to every non-draft post dated after
today (UTC) in the CI checkout only, so Zola leaves it out of every page,
feed, taxonomy, and the sitemap. The deploy workflow also runs daily, so a
scheduled post goes live on the first build on or after its date.

The default mode (``--check``) changes nothing. It prints the schedule and
fails when:

* a non-draft post is dated in the future but has no ``scheduled = true``
  (an un-drafted post with a future date must be marked on purpose), or
* a post has both ``draft = true`` and ``scheduled = true`` (pick one).

Local ``zola serve`` and ``zola build`` do not run this script, so scheduled
posts show up there for review, with a "Scheduled" notice at the top.

Usage
-----
    python3 scripts/scheduled_posts.py --self-test
    python3 scripts/scheduled_posts.py
    python3 scripts/scheduled_posts.py --hide
    python3 scripts/scheduled_posts.py --today 2026-11-01
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import sys
import tempfile

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOG_DIR = os.path.join(REPO_ROOT, "zola-site", "content", "blog")

DATE_RE = re.compile(r'^date\s*=\s*"?(\d{4}-\d{2}-\d{2})')
DRAFT_RE = re.compile(r"^draft\s*=\s*true\s*$")
SCHEDULED_RE = re.compile(r"^scheduled\s*=\s*true\s*$")


class Post:
    def __init__(self, path: str) -> None:
        self.path = path
        self.name = os.path.basename(path)
        with open(path, encoding="utf-8") as handle:
            self.lines = handle.read().split("\n")
        self.date: dt.date | None = None
        self.date_index = -1
        self.draft = False
        self.scheduled = False
        if not self.lines or self.lines[0].strip() != "+++":
            return
        table = ""
        for index, line in enumerate(self.lines[1:], start=1):
            stripped = line.strip()
            if stripped == "+++":
                break
            if stripped.startswith("["):
                table = stripped
                continue
            if table == "":
                match = DATE_RE.match(stripped)
                if match and self.date is None:
                    self.date = dt.date.fromisoformat(match.group(1))
                    self.date_index = index
                if DRAFT_RE.match(stripped):
                    self.draft = True
            elif table == "[extra]" and SCHEDULED_RE.match(stripped):
                self.scheduled = True

    def hide(self) -> None:
        """Insert ``draft = true`` after the date line and save the file."""
        self.lines.insert(self.date_index + 1, "draft = true")
        with open(self.path, "w", encoding="utf-8") as handle:
            handle.write("\n".join(self.lines))
        self.draft = True


def load(blog_dir: str) -> list[Post]:
    posts = []
    for name in sorted(os.listdir(blog_dir)):
        if name.endswith(".md") and name != "_index.md":
            posts.append(Post(os.path.join(blog_dir, name)))
    return posts


def run(blog_dir: str, today: dt.date, hide: bool) -> int:
    posts = load(blog_dir)
    where = "zola-site/content/blog/"
    errors = []
    upcoming = []
    for post in posts:
        if post.draft and post.scheduled:
            errors.append(
                f"{where}{post.name}: has both draft = true and scheduled = true;"
                " remove draft = true to schedule it, or remove scheduled to keep it a draft"
            )
        elif not post.draft and post.date and post.date > today:
            if not post.scheduled:
                errors.append(
                    f"{where}{post.name}: dated {post.date} (future) but not marked;"
                    " add `scheduled = true` under [extra], or add `draft = true`"
                )
            upcoming.append(post)

    upcoming.sort(key=lambda p: (p.date, p.name))
    print(f"Scheduled posts as of {today} ({len(upcoming)} waiting):")
    for post in upcoming:
        print(f"  {post.date}  {where}{post.name}")
    if not upcoming:
        print("  (none)")

    if errors:
        print(f"\nERROR: {len(errors)} scheduling problem(s):")
        for line in errors:
            print(f"  {line}")
        return 1

    if hide:
        for post in upcoming:
            post.hide()
        print(f"Held {len(upcoming)} scheduled post(s) back from this build.")
    return 0


def self_test() -> int:
    today = dt.date(2027, 1, 1)
    with tempfile.TemporaryDirectory() as tmp:
        def write(name: str, date: str, draft: bool = False, scheduled: bool = False) -> str:
            body = f'+++\ntitle = "t"\ndate = "{date}"\n'
            body += "draft = true\n" if draft else ""
            body += '[taxonomies]\ntags = ["x"]\n[extra]\nrelated = []\n'
            body += "scheduled = true\n" if scheduled else ""
            body += "+++\nbody with scheduled = true in it\n"
            path = os.path.join(tmp, name)
            with open(path, "w", encoding="utf-8") as handle:
                handle.write(body)
            return path

        write("old.md", "2026-06-01")
        write("draft.md", "2027-03-01", draft=True)
        soon = write("soon.md", "2027-01-15", scheduled=True)
        today_post = write("today.md", "2027-01-01", scheduled=True)
        assert run(tmp, today, hide=False) == 0, "scheduled future post must pass"
        assert not Post(soon).draft, "check mode must not edit files"

        write("bad.md", "2027-02-01")
        assert run(tmp, today, hide=False) == 1, "unmarked future post must fail"
        os.remove(os.path.join(tmp, "bad.md"))
        write("both.md", "2027-02-01", draft=True, scheduled=True)
        assert run(tmp, today, hide=False) == 1, "draft plus scheduled must fail"
        os.remove(os.path.join(tmp, "both.md"))

        assert run(tmp, today, hide=True) == 0
        hidden = Post(soon)
        assert hidden.draft and hidden.lines[hidden.date_index + 1] == "draft = true"
        assert not Post(today_post).draft, "a post dated today goes live"
        assert not Post(os.path.join(tmp, "old.md")).draft, "past posts are untouched"
    print("\nself-test passed")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="validate only (default)")
    mode.add_argument("--hide", action="store_true", help="mark future posts as drafts for this build")
    mode.add_argument("--self-test", action="store_true")
    parser.add_argument("--today", type=dt.date.fromisoformat, default=None)
    args = parser.parse_args()
    if args.self_test:
        return self_test()
    today = args.today or dt.datetime.now(dt.timezone.utc).date()
    return run(BLOG_DIR, today, args.hide)


if __name__ == "__main__":
    sys.exit(main())
