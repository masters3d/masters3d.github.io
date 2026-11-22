#!/usr/bin/env python3
"""Report phrases repeated across blog posts and fail on the ones the author banned.

Some phrases read fine once and become house style when post after post uses
them: "I keep coming back to", "the risk is real, but", "genuinely". This
script counts each phrase family in ``scripts/repeated_phrases.toml`` across
every post in ``zola-site/content/blog`` (drafts and scheduled posts too,
since they go live later) and reports every family used more than ``limit``
times (3), with each use.

The report alone does not fail the check. A family fails it only when the
author lists it under ``[enforce]`` with the most uses it may have (0 bans it)
and the posts go past that. Families under ``[allow]`` are ones the author
accepted, and they are not flagged. Only the author edits those two tables.

Matching rules:

* Each family is one regular expression, matched without regard to case, so
  the usual rewordings ("I keep returning to") count with the original. An
  optional ``unless`` regex drops a use when its sentence matches, so "the
  root is real" in a sentence about real numbers does not count.
* Prettier wraps prose at 80 columns, so each paragraph is joined into one
  line, with runs of whitespace collapsed to one space, before matching. A
  phrase split across two source lines still counts, at its first line.
* Fenced code, inline code, URLs, HTML tags and comments, and Zola shortcodes
  are skipped. Link text, image alt text, headings, and the front matter
  ``title`` and ``description`` count, because readers see them.

``--discover`` lists other 3 to 5 word phrases used more than ``limit`` times
in more than ``limit`` posts, as candidates for new families. Most of them are
topic names; the useful ones are formulas that could sit in any post.

Usage
-----
    python3 scripts/check_repeated_phrases.py --self-test
    python3 scripts/check_repeated_phrases.py
    python3 scripts/check_repeated_phrases.py --report report.md
    python3 scripts/check_repeated_phrases.py --show x-is-real
    python3 scripts/check_repeated_phrases.py --discover
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import tempfile
from collections import Counter, defaultdict
from dataclasses import dataclass

try:
    import tomllib
except ModuleNotFoundError:  # Python < 3.11
    sys.exit("check_repeated_phrases.py needs Python 3.11 or newer (tomllib).")

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOG_DIR = os.path.join(REPO_ROOT, "zola-site", "content", "blog")
CONFIG_PATH = os.path.join(REPO_ROOT, "scripts", "repeated_phrases.toml")
CONFIG_NAME = "scripts/repeated_phrases.toml"

ID_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
SENTENCE_END = re.compile(r"[.!?](?=\s|$)")
PHRASE_FIELDS = ("id", "phrase", "pattern", "example", "why", "instead")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
FRONT_TEXT_RE = re.compile(r'^(title|description)\s*=\s*"(.*)"\s*$')
LINK_DEF_RE = re.compile(r"^\s*\[[^\]]+\]:\s*\S+\s*$")
LINE_MARKER_RE = re.compile(r"^\s*(?:>\s*)*(?:#{1,6}\s+|[-*+]\s+|\d+[.)]\s+)?")
LINK_TEXT = r"\1"
# Applied in order to each paragraph. Replacements keep line breaks, so a
# match still maps back to its source line.
STRIP_RULES = [
    (re.compile(r"<!--.*?-->", re.S), ""),
    (re.compile(r"\{\{.*?\}\}|\{%.*?%\}", re.S), ""),
    (re.compile(r"`[^`]*`"), ""),
    (re.compile(r"!?\[([^\]]*)\]\([^)]*\)"), LINK_TEXT),
    (re.compile(r"\[([^\]]*)\]\[[^\]]*\]"), LINK_TEXT),
    (re.compile(r"<[A-Za-z/!][^<>]*>"), ""),
    (re.compile(r"https?://\S+"), ""),
    (re.compile(r"\*+|(?<!\w)_+|_+(?!\w)"), ""),
]
QUOTES = str.maketrans({"\u2018": "'", "\u2019": "'", "\u201c": '"', "\u201d": '"'})
STOPWORDS = frozenset(
    "a an and are as at be been but by can could did do does for from had has "
    "have he her his how i if in into is it its me my no not of on or our she so "
    "than that the their them then there these they this those to too us was we "
    "were what when where which who why will with would you your".split()
)


class ConfigError(Exception):
    pass


@dataclass
class Phrase:
    id: str
    phrase: str
    regex: re.Pattern
    why: str
    instead: str
    unless: re.Pattern | None = None


@dataclass
class Config:
    limit: int
    phrases: list[Phrase]
    enforce: dict[str, int]
    allow: dict[str, str]


@dataclass
class Post:
    path: str
    title: str
    blocks: list[tuple[str, list[int]]]


@dataclass
class Hit:
    path: str
    line: int
    before: str
    match: str
    after: str


@dataclass
class Result:
    phrase: Phrase
    hits: list[Hit]
    cap: int | None
    allowed: bool
    limit: int

    @property
    def count(self) -> int:
        return len(self.hits)

    @property
    def posts(self) -> int:
        return len({hit.path for hit in self.hits})

    @property
    def failed(self) -> bool:
        return self.cap is not None and self.count > self.cap

    @property
    def flagged(self) -> bool:
        return self.cap is None and not self.allowed and self.count > self.limit

    @property
    def status(self) -> str:
        if self.cap is not None:
            return f"FAIL (max {self.cap})" if self.failed else f"enforced (max {self.cap})"
        if self.allowed:
            return "allowed"
        return "over limit" if self.flagged else "ok"


def parse_config(text: str) -> Config:
    """Parse and validate the watchlist. Raises ConfigError listing every problem."""
    try:
        data = tomllib.loads(text)
    except tomllib.TOMLDecodeError as error:
        raise ConfigError([f"not valid TOML ({error})"]) from error
    problems = []
    unknown = sorted(set(data) - {"limit", "phrase", "enforce", "allow"})
    if unknown:
        problems.append(f"unknown top-level keys: {', '.join(unknown)}")
    limit = data.get("limit")
    if not isinstance(limit, int) or isinstance(limit, bool) or limit < 0:
        problems.append("limit must be a whole number, 0 or more")
    phrases, seen = [], set()
    for number, entry in enumerate(data.get("phrase", []), start=1):
        missing = [key for key in PHRASE_FIELDS if not str(entry.get(key, "")).strip()]
        if missing:
            problems.append(f"[[phrase]] #{number} is missing {', '.join(missing)}")
            continue
        pid = entry["id"]
        extra = sorted(set(entry) - set(PHRASE_FIELDS) - {"unless"})
        if extra:
            problems.append(f"{pid}: unknown keys {', '.join(extra)}")
        if not ID_RE.fullmatch(pid):
            problems.append(f"{pid}: id must be lowercase words joined by hyphens")
        if pid in seen:
            problems.append(f"{pid}: duplicate id")
        seen.add(pid)
        try:
            regex = re.compile(entry["pattern"], re.IGNORECASE)
            unless = re.compile(entry["unless"], re.IGNORECASE) if "unless" in entry else None
        except re.error as error:
            problems.append(f"{pid}: pattern or unless does not compile ({error})")
            continue
        if regex.search(""):
            problems.append(f"{pid}: pattern matches empty text")
        phrase = Phrase(pid, entry["phrase"], regex, entry["why"], entry["instead"], unless)
        found = len(list(uses(phrase, entry["example"])))
        if found != 1:
            problems.append(f"{pid}: pattern matches its example {found} times, not once")
        phrases.append(phrase)
    enforce, allow = data.get("enforce", {}), data.get("allow", {})
    for pid, cap in enforce.items():
        if pid not in seen:
            problems.append(f"[enforce] {pid}: no [[phrase]] has this id")
        if not isinstance(cap, int) or isinstance(cap, bool) or cap < 0:
            problems.append(f"[enforce] {pid}: the cap must be a whole number, 0 or more")
    for pid, note in allow.items():
        if pid not in seen:
            problems.append(f"[allow] {pid}: no [[phrase]] has this id")
        if pid in enforce:
            problems.append(f"{pid}: listed under both [enforce] and [allow]")
        if not isinstance(note, str) or not note.strip():
            problems.append(f'[allow] {pid}: give the reason as a string, e.g. "my voice"')
    if problems:
        raise ConfigError(problems)
    return Config(limit, phrases, enforce, allow)


def load_config(path: str = CONFIG_PATH) -> Config:
    with open(path, encoding="utf-8") as handle:
        return parse_config(handle.read())


def keep_breaks(match: re.Match, replacement: str) -> str:
    out = match.expand(replacement)
    return out + "\n" * (match.group(0).count("\n") - out.count("\n"))


def join_lines(lines: list[str], first: int, link_text: bool = True) -> tuple[str, list[int]]:
    """Join one paragraph into a single line; return it with each character's source line."""
    text = "\n".join(lines)
    for rule, replacement in STRIP_RULES:
        if replacement == LINK_TEXT and not link_text:
            replacement = " | "
        text = rule.sub(lambda match, r=replacement: keep_breaks(match, r), text)
    chars, where, number = [], [], first
    for char in text.translate(QUOTES):
        if char.isspace():
            if chars and chars[-1] != " ":
                chars.append(" ")
                where.append(number)
            if char == "\n":
                number += 1
            continue
        chars.append(char)
        where.append(number)
    return "".join(chars), where


def paragraphs(lines: list[str], link_text: bool = True):
    """Yield (text, line_of_each_char) for the title, the description, and each paragraph."""
    body_start = 0
    if lines and lines[0].strip() == "+++":
        in_table = False
        for index in range(1, len(lines)):
            line = lines[index]
            if line.strip() == "+++":
                body_start = index + 1
                break
            if line.lstrip().startswith("["):
                in_table = True
            match = FRONT_TEXT_RE.match(line)
            if match and not in_table:
                yield join_lines([match.group(2).replace('\\"', '"')], index + 1, link_text)
    block, first, fenced = [], 0, False
    for index in range(body_start, len(lines)):
        line = lines[index]
        if FENCE_RE.match(line):
            fenced = not fenced
            line = ""
        if fenced or not line.strip() or LINK_DEF_RE.match(line):
            if block:
                yield join_lines(block, first, link_text)
                block = []
            continue
        if not block:
            first = index + 1
        block.append(LINE_MARKER_RE.sub("", line, count=1).replace("|", " "))
    if block:
        yield join_lines(block, first, link_text)


def load_posts(blog_dir: str = BLOG_DIR, link_text: bool = True) -> list[Post]:
    posts = []
    for name in sorted(os.listdir(blog_dir)):
        if not name.endswith(".md") or name == "_index.md":
            continue
        with open(os.path.join(blog_dir, name), encoding="utf-8") as handle:
            lines = handle.read().splitlines()
        title = next((m.group(2) for m in map(FRONT_TEXT_RE.match, lines) if m and m.group(1) == "title"), "")
        blocks = list(paragraphs(lines, link_text))
        posts.append(Post(f"zola-site/content/blog/{name}", title, blocks))
    return posts


def uses(phrase: Phrase, text: str):
    """Yield the matches of phrase in text, skipping those whose sentence matches unless."""
    for match in phrase.regex.finditer(text):
        if phrase.unless:
            left = 0
            for end in SENTENCE_END.finditer(text, 0, match.start()):
                left = end.end()
            end = SENTENCE_END.search(text, match.end())
            if phrase.unless.search(text[left : end.end() if end else len(text)]):
                continue
        yield match


def find_hits(posts: list[Post], phrase: Phrase) -> list[Hit]:
    hits = []
    for post in posts:
        for text, where in post.blocks:
            for match in uses(phrase, text):
                before = text[max(0, match.start() - 50) : match.start()]
                after = text[match.end() : match.end() + 40]
                hits.append(Hit(post.path, where[match.start()], before, match.group(0), after))
    return hits


def evaluate(posts: list[Post], config: Config) -> list[Result]:
    results = [
        Result(p, find_hits(posts, p), config.enforce.get(p.id), p.id in config.allow, config.limit)
        for p in config.phrases
    ]
    rank = lambda r: (not r.failed, r.cap is None, not r.flagged, r.allowed, -r.count, r.phrase.id)
    return sorted(results, key=rank)


def plural(count: int, word: str) -> str:
    return f"{count} {word}{'' if count == 1 else 's'}"


def print_hits(result: Result, indent: str = "  ") -> None:
    print(f"{indent}Why: {result.phrase.why}")
    print(f"{indent}Instead: {result.phrase.instead}")
    for hit in result.hits:
        print(f"{indent}{hit.path}:{hit.line}: ...{hit.before}[{hit.match}]{hit.after}...")


def markdown(results: list[Result], config: Config, post_count: int) -> str:
    out = [
        "## Repeated phrases",
        "",
        f"{len(results)} watched phrases across {post_count} posts (drafts included). "
        f"Each phrase used more than {config.limit} times is listed with every use. "
        f"Only phrases under `[enforce]` in `{CONFIG_NAME}` fail the check.",
        "",
        "| Status | Phrase | ID | Uses | Posts |",
        "| --- | --- | --- | ---: | ---: |",
    ]
    for r in results:
        phrase = r.phrase.phrase.replace("|", "\\|")
        out.append(f"| {r.status} | {phrase} | `{r.phrase.id}` | {r.count} | {r.posts} |")
    for r in results:
        if not (r.failed or r.flagged):
            continue
        out += ["", f"<details><summary><code>{r.phrase.id}</code>: {plural(r.count, 'use')} "
                f"in {plural(r.posts, 'post')}</summary>", "",
                f"Why: {r.phrase.why} Instead: {r.phrase.instead}", ""]
        out += [f"- `{h.path}:{h.line}` ...{h.before}**{h.match}**{h.after}..." for h in r.hits]
        out += ["", "</details>"]
    return "\n".join(out) + "\n"


def check(
    blog_dir: str, config: Config, report: str | None = None, annotate: bool = False
) -> int:
    posts = load_posts(blog_dir)
    results = evaluate(posts, config)
    failed = [r for r in results if r.failed]
    flagged = [r for r in results if r.flagged]

    print(
        f"Repeated phrases: {len(results)} watched across {len(posts)} posts. A phrase "
        f"used more than {config.limit} times is flagged; only [enforce] entries fail.\n"
    )
    print(f"{'Status':<18}{'Uses':>5}{'Posts':>7}  Phrase")
    for r in results:
        print(f"{r.status:<18}{r.count:>5}{r.posts:>7}  {r.phrase.phrase}  ({r.phrase.id})")

    if report:
        with open(report, "a", encoding="utf-8") as handle:
            handle.write(markdown(results, config, len(posts)))
    if annotate:
        for r in failed:
            for hit in r.hits:
                print(f"::error file={hit.path},line={hit.line},title=Banned phrase::"
                      f'"{hit.match}" ({r.phrase.id}): {r.phrase.instead}')
        if flagged:
            uses = sum(r.count for r in flagged)
            print(f"::warning title=Repeated phrases::{plural(len(flagged), 'phrase')} "
                  f"used more than {config.limit} times ({uses} uses) wait for the "
                  "author's decision. See the job summary.")

    if flagged:
        print(f"\n{plural(len(flagged), 'phrase')} used more than {config.limit} times wait "
              "for the author's decision (enforce or allow). List the uses with --show ID.")
    if not failed:
        print(f"\nOK: {plural(len(config.enforce), 'enforced phrase')} within the cap.")
        return 0
    print(f"\nERROR: {plural(len(failed), 'enforced phrase')} over the cap:")
    for r in failed:
        print(f"\n{r.phrase.id} (\"{r.phrase.phrase}\"): {plural(r.count, 'use')}, "
              f"at most {r.cap} allowed. Rewrite these sentences:")
        print_hits(r)
    print(
        "\nSay the specific thing instead of swapping in a synonym; the pattern counts "
        f"the usual rewordings. Only the author changes [enforce] in {CONFIG_NAME}."
    )
    return 1


def show(blog_dir: str, config: Config, ids: list[str]) -> int:
    by_id = {r.phrase.id: r for r in evaluate(load_posts(blog_dir), config)}
    unknown = [pid for pid in ids if pid not in by_id]
    if unknown:
        print(f"ERROR: no phrase with id {', '.join(unknown)} in {CONFIG_NAME}")
        return 1
    for pid in ids:
        r = by_id[pid]
        print(f"{pid} (\"{r.phrase.phrase}\"): {plural(r.count, 'use')} in "
              f"{plural(r.posts, 'post')}, {r.status}")
        print_hits(r)
        print()
    return 0


def discover(blog_dir: str, config: Config, top: int) -> int:
    """Print repeated phrases that no watched pattern covers, as candidates."""
    posts = load_posts(blog_dir, link_text=False)
    titles = [post.title.lower() for post in posts]
    uses, spread = Counter(), defaultdict(set)
    for post in posts:
        for text, _ in post.blocks:
            for phrase in config.phrases:
                text = phrase.regex.sub(" | ", text)
            for clause in re.split(r"[^\w\s'-]+", text.lower()):
                words = [w.strip("'-") for w in clause.split() if w.strip("'-")]
                for size in (3, 4, 5):
                    for start in range(len(words) - size + 1):
                        gram = words[start : start + size]
                        if all(word in STOPWORDS for word in gram):
                            continue
                        uses[" ".join(gram)] += 1
                        spread[" ".join(gram)].add(post.path)
    limit = config.limit
    rows = sorted(
        (
            (len(spread[gram]), count, gram)
            for gram, count in uses.items()
            if count > limit and len(spread[gram]) > limit and not any(gram in t for t in titles)
        ),
        key=lambda row: (-row[0], -row[1], -len(row[2])),
    )
    kept: list[tuple[int, int, str]] = []
    for row in rows:
        if not any(row[2] in other[2] and row[0] == other[0] for other in kept):
            kept.append(row)
        if len(kept) == top:
            break
    print(f"Phrases used more than {limit} times in more than {limit} posts that no "
          f"watched pattern covers (post titles skipped). Top {len(kept)}:\n")
    print(f"{'Posts':>5}{'Uses':>6}  Phrase")
    for posts_with, count, gram in kept:
        print(f"{posts_with:>5}{count:>6}  {gram}")
    print(f"\nTopic names are expected here. Add a formula to {CONFIG_NAME} as a [[phrase]].")
    return 0


def self_test() -> int:
    config = load_config()
    by_id = {p.id: p for p in config.phrases}

    def count(pid: str, text: str) -> int:
        joined, _ = join_lines(text.split("\n"), 1)
        return len(list(uses(by_id[pid], joined)))

    assert count("keep-coming-back", "The idea I keep\ncoming back to.") == 1, "wrapped line"
    assert count("keep-coming-back", "The frame I keep returning to.") == 1, "rewording"
    assert count("x-is-real", "The risk is real, but it is small.") == 1, "concession"
    assert count("x-is-real", "The **gap is real**.") == 1, "emphasis is stripped"
    assert count("x-is-real", "There is real value in it.") == 0, "attributive real"
    assert count("x-is-real", "Every root is real. 2 is a real number.") == 0, "numbers"
    assert count("x-is-real", "The latency is real-time.") == 0, "real-time"

    with tempfile.TemporaryDirectory() as tmp:
        def post(name: str, body: str, description: str = "d") -> None:
            text = f'+++\ntitle = "t"\ndescription = "{description}"\n[extra]\n'
            text += 'description = "the gap is real."\n+++\n' + body
            with open(os.path.join(tmp, name), "w", encoding="utf-8") as handle:
                handle.write(text)

        post("a.md", "Intro.\n\nI keep\ncoming back to it.\n\n```\nI keep coming back to\n```\n\n"
             "`I keep coming back to` and [this](https://x.test/i-keep-coming-back-to).\n",
             description="The gap is real.")
        post("b.md", "- [The pull is real](/blog/a/), and\n  the risk was real.\n")
        posts = load_posts(tmp)
        keep = find_hits(posts, by_id["keep-coming-back"])
        assert [(h.path[-4:], h.line) for h in keep] == [("a.md", 9)], keep
        real = find_hits(posts, by_id["x-is-real"])
        assert [(h.path[-4:], h.line) for h in real] == [("a.md", 3), ("b.md", 7), ("b.md", 8)], real

        phrases = [by_id["keep-coming-back"], by_id["x-is-real"]]
        assert check(tmp, Config(3, phrases, {}, {})) == 0, "report alone never fails"
        assert check(tmp, Config(3, phrases, {"keep-coming-back": 0}, {})) == 1, "banned"
        assert check(tmp, Config(3, phrases, {"x-is-real": 3}, {})) == 0, "within the cap"
        assert check(tmp, Config(2, phrases, {"x-is-real": 2}, {})) == 1, "over the cap"
        flagged = evaluate(posts, Config(2, phrases, {}, {}))
        assert [r.phrase.id for r in flagged if r.flagged] == ["x-is-real"], "3 > limit 2"
        allowed = evaluate(posts, Config(2, phrases, {}, {"x-is-real": "fine"}))
        assert not any(r.flagged for r in allowed), "allowed phrases are not flagged"

    base = "limit = 3\n[[phrase]]\nid = 'a'\nphrase = 'a'\npattern = '\\bab\\b'\n"
    base += "example = 'ab'\nwhy = 'w'\ninstead = 'i'\n"
    assert parse_config(base).limit == 3
    for broken in (
        base + "[enforce]\nb = 0\n",
        base + "[enforce]\na = -1\n",
        base + "[enforce]\na = 0\n[allow]\na = 'x'\n",
        base.replace("example = 'ab'", "example = 'abc'"),
        base.replace("\\bab\\b", "\\bab\\b|^"),
        base + "[[phrase]]\nid = 'a'\nphrase = 'a'\npattern = 'x'\nexample = 'x'\nwhy = 'w'\ninstead = 'i'\n",
        base.replace("why = 'w'", "why = 'w'\nunles = 'ab'"),
        base.replace("why = 'w'", "why = 'w'\nunless = 'ab'"),
    ):
        try:
            parse_config(broken)
        except ConfigError:
            continue
        raise AssertionError(f"config must be rejected:\n{broken}")
    print("\nself-test passed")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--report", metavar="FILE", help="append a Markdown report to FILE")
    parser.add_argument("--show", nargs="+", metavar="ID", help="list every use of these phrases")
    parser.add_argument("--discover", action="store_true", help="list repeated phrases not watched yet")
    parser.add_argument("--top", type=int, default=40, help="how many --discover rows to print")
    args = parser.parse_args()
    try:
        if args.self_test:
            return self_test()
        config = load_config()
    except ConfigError as error:
        print(f"ERROR: {CONFIG_NAME} has problems:")
        for problem in error.args[0]:
            print(f"  {problem}")
        return 1
    if args.show:
        return show(BLOG_DIR, config, args.show)
    if args.discover:
        return discover(BLOG_DIR, config, args.top)
    annotate = os.environ.get("GITHUB_ACTIONS") == "true"
    return check(BLOG_DIR, config, args.report or None, annotate)


if __name__ == "__main__":
    sys.exit(main())
