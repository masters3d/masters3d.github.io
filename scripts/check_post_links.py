#!/usr/bin/env python3
"""Fail when a blog post links to a post that will not be live yet.

Upcoming posts wait as drafts (``draft = true``) dated for release, and they go
out in date order. An inline link to ``/blog/<slug>/`` only works once the
target is published, so this check enforces release order for links:

* A published post may only link to published posts. A link to a draft would
  be a broken link on the live site.
* A draft may link to published posts, and to drafts dated on or before its
  own date (those go out first). A link to a later draft would ship broken.
* Every linked slug must exist.

Forward references go in ``related`` under ``[extra]`` instead of inline:

    [extra]
    related = ["later-post-slug", "earlier-post-slug"]

The blog template shows a "Related posts" list that only includes related
posts that are published, plus every published post that lists this one.
So when a later post goes out, the earlier posts it names (or that name it)
pick up the cross-reference on the next build, with no edits to old posts.
This check only verifies that each ``related`` slug exists and is not the
post itself. It does not rewrite files.

Usage
-----
    python3 scripts/check_post_links.py --self-test
    python3 scripts/check_post_links.py
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import tempfile

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOG_DIR = os.path.join(REPO_ROOT, "zola-site", "content", "blog")

DATE_RE = re.compile(r'^date\s*=\s*"?(\d{4}-\d{2}-\d{2})', re.M)
DRAFT_RE = re.compile(r"^draft\s*=\s*true\s*$", re.M)
LINK_RE = re.compile(
    r"\]\((?:https://masters3d\.github\.io)?/blog/([a-z0-9][a-z0-9-]*)/?[)#]"
)
RELATED_RE = re.compile(r"^related\s*=\s*\[([^\]]*)\]", re.M)


class Post:
    def __init__(self, slug: str, text: str) -> None:
        parts = text.split("+++")
        front = parts[1] if len(parts) > 2 else ""
        body = "+++".join(parts[2:]) if len(parts) > 2 else text
        top = front.split("\n[", 1)[0]
        date = DATE_RE.search(top)
        self.slug = slug
        self.date = date.group(1) if date else "0000-00-00"
        self.draft = bool(DRAFT_RE.search(top))
        self.links = sorted(set(LINK_RE.findall(body)))
        extra = front.split("\n[extra]", 1)[1] if "\n[extra]" in front else ""
        extra = extra.split("\n[", 1)[0]
        match = RELATED_RE.search(extra)
        self.related = re.findall(r'"([^"]+)"', match.group(1)) if match else []


def load(blog_dir: str) -> dict[str, Post]:
    posts = {}
    for name in sorted(os.listdir(blog_dir)):
        if not name.endswith(".md") or name == "_index.md":
            continue
        with open(os.path.join(blog_dir, name), encoding="utf-8") as handle:
            posts[name[:-3]] = Post(name[:-3], handle.read())
    return posts


def problems(posts: dict[str, Post]) -> list[str]:
    out = []
    for post in posts.values():
        where = f"zola-site/content/blog/{post.slug}.md"
        for slug in post.links:
            target = posts.get(slug)
            if target is None:
                out.append(f"{where}: links to /blog/{slug}/, which does not exist")
            elif target.draft and not post.draft:
                out.append(
                    f"{where}: published post links to draft /blog/{slug}/ "
                    f"({target.date}); publish that post first or move the "
                    "link into [extra] related"
                )
            elif target.draft and target.date > post.date:
                out.append(
                    f"{where} ({post.date}): links to /blog/{slug}/, a later "
                    f"draft ({target.date}); move the link into [extra] related"
                )
        for slug in post.related:
            if slug == post.slug:
                out.append(f"{where}: related lists the post itself")
            elif slug not in posts:
                out.append(f"{where}: related slug '{slug}' does not exist")
    return out


def check(blog_dir: str) -> int:
    posts = load(blog_dir)
    found = problems(posts)
    links = sum(len(p.links) for p in posts.values())
    related = sum(len(p.related) for p in posts.values())
    if not found:
        print(f"OK: {links} internal links and {related} related entries respect release order.")
        return 0
    print(f"ERROR: {len(found)} cross-reference problem(s):")
    for line in found:
        print(f"  {line}")
    return 1


def self_test() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        def write(slug: str, date: str, draft: bool, body: str = "", related: str = "") -> None:
            text = f'+++\ntitle = "t"\ndate = "{date}"\n'
            text += "draft = true\n" if draft else ""
            text += f"[extra]\nrelated = [{related}]\n" if related else ""
            text += f"+++\n{body}\n"
            with open(os.path.join(tmp, slug + ".md"), "w", encoding="utf-8") as handle:
                handle.write(text)

        write("old", "2026-01-01", False)
        write("early", "2027-01-01", True, "See [old](/blog/old/).")
        write("late", "2027-02-01", True, "See [early](/blog/early/).", '"old", "early"')
        assert check(tmp) == 0, "links back in release order must pass"
        write("old", "2026-01-01", False, "", '"late"')
        assert check(tmp) == 0, "related may point at a later draft"
        write("early", "2027-01-01", True, "See [late](/blog/late/#x).")
        assert check(tmp) == 1, "inline link to a later draft must fail"
        write("early", "2027-01-01", True)
        write("old", "2026-01-01", False, "See [early](/blog/early/).")
        assert check(tmp) == 1, "published post linking to a draft must fail"
        write("old", "2026-01-01", False, "See [gone](/blog/gone/).")
        assert check(tmp) == 1, "missing link target must fail"
        write("old", "2026-01-01", False, "", '"nope"')
        assert check(tmp) == 1, "missing related slug must fail"
    print("\nself-test passed")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        return self_test()
    return check(BLOG_DIR)


if __name__ == "__main__":
    sys.exit(main())
