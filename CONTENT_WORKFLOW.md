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
categories = ["category"]
tags = ["tag1", "tag2"]
+++
```
3. Write content in markdown below the frontmatter
4. Format the Markdown: run `python3 scripts/format_markdown.py`
5. Commit and push

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
categories = ["optional"]
tags = ["optional", "multiple"]
+++
```