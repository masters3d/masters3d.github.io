# Content Management Workflow

This portfolio uses **markdown as the source of truth** for all content. Pages are generated from markdown files using Zola static site generator with automatic deployment via GitHub Actions.

## 🎯 Quick Start

**To edit content:**
1. Edit markdown files in `zola-site/content/`
2. Commit and push changes
3. GitHub Actions automatically builds and deploys the site

**To preview during editing:**
```bash
cd zola-site
zola serve
# Visit http://127.0.0.1:1111/
```

## 📁 File Structure

### ✏️ Edit These (Source Files)

**Content Sources:**
- `zola-site/content/_index.md` - Main portfolio page content
- `zola-site/content/tech/_index.md` - Technical projects portfolio
- `zola-site/content/media/_index.md` - Media portfolio
- `zola-site/content/blog/` - Blog posts (markdown files)

**Template Sources:**
- `zola-site/templates/index.html` - Main page layout
- `zola-site/templates/tech.html` - Tech page layout
- `zola-site/templates/media.html` - Media page layout
- `zola-site/templates/blog.html` - Blog listing layout
- `zola-site/templates/blog-post.html` - Individual blog post layout

**Configuration:**
- `zola-site/config.toml` - Site configuration (URL, title, analytics)

### 🚫 Don't Edit These (Generated Files)

**Generated Output:**
- `zola-site/public/` - Complete built website (auto-generated)
- All files in `public/` are rebuilt on every Zola build

## 📏 Markdown Formatting (Required)

Blog Markdown is formatted with **[Prettier](https://prettier.io/)** (the
formatter) and checked with **[markdownlint](https://github.com/DavidAnson/markdownlint)**
(the linter). Prettier wraps prose to 80 columns so edits show up as small,
line-level diffs instead of whole-paragraph diffs.

**This does not change the rendered page.** Prettier is configured with
`proseWrap: always` (a single newline inside a paragraph is a Markdown "soft
break" that renders as a space) and `embeddedLanguageFormatting: off` (sample
code shown inside fenced blocks is left untouched). The generated HTML is
byte-identical before and after formatting; only the `.md` source line breaks
change.

**Before committing any blog Markdown change**, install the tooling once, then
run the formatter:

```bash
npm install                                # one-time: install Prettier + markdownlint
python3 scripts/format_markdown.py         # format + lint-fix all blog posts
python3 scripts/format_markdown.py --check  # verify only (used by CI)
```

`scripts/format_markdown.py` is a thin, portable (Linux/macOS/Windows) wrapper
that just calls Prettier and markdownlint; the tools are pinned in
`package.json`. Configuration lives in `.prettierrc.json` and
`.markdownlint-cli2.jsonc`. The PR Validation workflow runs the `--check` mode,
so a PR whose blog Markdown is not correctly formatted (or fails lint) will fail
the `validate` check.

## 🔎 Covert character check (required)

Some model outputs hide a mark in characters a reader never sees: a zero-width
space, a Unicode tag character, a bidirectional override, a byte-order mark, or
a space that is not U+0020. Others swap in a lookalike letter (Cyrillic U+0430
standing in for Latin a). `scripts/check_content_marks.py` scans the text files
in this repository and fails if it finds one. The failure names the file, line,
character column, code point, and the edit: delete that character, or replace
it with the named ASCII character. It does not rewrite the file.

```bash
python3 scripts/check_content_marks.py --self-test   # detector fixtures
python3 scripts/check_content_marks.py               # scan the repository
```

PR Validation and the deploy workflow both run those two commands. Ordinary
punctuation (em dash, accented Latin, emoji, and a variation selector that
follows an emoji) is left alone. Two trailing ASCII spaces at the end of a
Markdown line are a hard line break, not a mark.

Word-choice watermarks are a different channel, and this check cannot fail
them. SynthID-Text and the Kirchenbauer green-list scheme bias which token is
picked. They do not insert a character, so there is no line to edit. Detecting
them requires the secret key used when the text was generated. The public
implementation is [google-deepmind/synthid-text](https://github.com/google-deepmind/synthid-text);
the detector does nothing useful without that key. Public descriptions of
Claude's text watermark say it is this kind of keyed statistical mark, not
hidden Unicode, and no detector key is published. The check says that in its
output. It does not paraphrase text to chase a signal it cannot locate.

## 🔄 Deployment Process

**Automatic via GitHub Actions:**
1. Push changes to `master` branch
2. GitHub Actions triggers workflow
3. Zola builds the site from markdown
4. Site deploys automatically to https://masters3d.com

**No manual build steps required!**

## 💻 Development Commands

**Local Development:**
```bash
# Start Zola development server with live reload
cd zola-site
zola serve

# Visit http://127.0.0.1:1111/
# All pages accessible: /, /tech/, /media/, /blog/
```

**Manual Build (for testing):**
```bash
cd zola-site
zola build
# Output in public/ directory
```

## ✍️ Creating Content

### 📝 Adding a Blog Post

1. Create new file: `zola-site/content/blog/your-post-name.md`
2. Add frontmatter:
```toml
+++
title = "Your Post Title"
date = 2024-09-14
description = "SEO description"
template = "blog-post.html"
categories = ["Engineering Systems"]
tags = ["tag1", "tag2"]
[extra]
editorial_track = "engineering-systems"
+++
```
3. Choose exactly one editorial track: `Quest Engine`, `Field Notes`,
   `Software Engineering`, `Engineering Systems`, or `Human Systems`. Mentioning
   the Quest Engine does not make a post a Quest Engine post. Check the tracks
   in priority order and stop at the first fit: Software Engineering (computer
   languages or creating software, even when dated or personal), Engineering
   Systems (general engineering practices not only about software), Human
   Systems (about humans rather than engineering), Quest Engine (only posts
   that change the model), then Field Notes as the fallback. Apply the order
   to the post's main subject: if a post mixes subjects and its claim still
   holds with the software examples swapped for another field, it does not go
   in Software Engineering. See "Placing a Post in a Track" in
   `plans/agents.md`
4. Use tags for series and ideas that cross editorial tracks
5. Write content in markdown below the frontmatter
6. Format the Markdown: run `python3 scripts/format_markdown.py`
7. Commit and push

### 📄 Editing Existing Pages

1. Edit the appropriate markdown file:
   - Homepage: `zola-site/content/_index.md`
   - Tech page: `zola-site/content/tech/_index.md`
   - Media page: `zola-site/content/media/_index.md`
2. Commit and push changes

## 🌐 URL Structure

**All environments use clean URLs:**
- Homepage: `/`
- Tech portfolio: `/tech/`
- Media portfolio: `/media/`
- Blog listing: `/blog/`
- Blog posts: `/blog/post-name/`
- RSS feed: `/atom.xml`

## 🔍 Troubleshooting

**Local server not starting?**
```bash
# Make sure you're in the right directory
cd zola-site
zola serve
```

**Changes not showing?**
- Check file is saved
- Zola auto-reloads on file changes
- Check browser console for errors

**Deployment failed?**
- Check GitHub Actions tab for error messages
- Verify markdown syntax is correct
- Ensure all required frontmatter is present

## 📚 Markdown Reference

**Basic formatting:**
```markdown
# Heading 1
## Heading 2
**bold text**
*italic text*
[link text](URL)
![image alt](image-path)
```

**Blog post frontmatter:**
```toml
+++
title = "Required: Post title"
date = 2024-09-14
description = "Required: SEO description"
template = "blog-post.html"
categories = ["Required: one editorial track"]
tags = ["optional", "cross-track", "topics"]
[extra]
editorial_track = "required-track-slug"
+++
```