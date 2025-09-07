# Content Management Workflow

This portfolio uses **markdown as the source of truth** for all content. Pages are generated from markdown files using Zola static site generator, providing a professional content management workflow.

## 🎯 Quick Start

**To edit content:**
1. Edit markdown files in `zola-site/content/`
2. Run `./build.sh` to regenerate HTML
3. Commit and push changes

**To preview during editing:**
```bash
cd zola-site
zola serve --port 8084
# Visit http://127.0.0.1:8084/
```

## 📁 File Structure

### ✏️ Edit These (Source Files)

**Content Sources:**
- `zola-site/content/_index.md` - Main portfolio page content
- `zola-site/content/tech/_index.md` - Technical projects portfolio
- `zola-site/content/media/_index.md` - Media portfolio

**Template Sources:**
- `zola-site/templates/index.html` - Main page layout
- `zola-site/templates/tech.html` - Tech page layout
- `zola-site/templates/media.html` - Media page layout

**Configuration:**
- `zola-site/config.toml` - Site configuration

### 🚫 Don't Edit These (Generated Files)

**Generated HTML files that will be overwritten:**
- `index.html` - Generated from `_index.md`
- `tech.html` - Generated from `tech/_index.md`
- `media.html` - Generated from `media/_index.md`

## 🔄 Build Process

The `./build.sh` script handles the complete build process:

1. **Copies assets** - CSS and images to Zola static folder
2. **Builds with Zola** - Generates HTML from markdown
3. **Copies output** - Moves generated files to root
4. **Converts URLs** - Transforms Zola URLs to static HTML URLs

### 🌐 URL Structure

**Development (Zola serve):**
- Main page: `http://127.0.0.1:8084/`
- Tech page: `http://127.0.0.1:8084/tech/`
- Media page: `http://127.0.0.1:8084/media/`

**Production (Static files):**
- Main page: `index.html`
- Tech page: `tech.html`
- Media page: `media.html`

## 💻 Development Commands

**Local Development:**
```bash
# Start Zola development server with live reload
cd zola-site
zola serve --port 8084

# Visit http://127.0.0.1:8084/
# Navigate to http://127.0.0.1:8084/tech/ and http://127.0.0.1:8084/media/
```

**Build and Test Production:**
```bash
# Generate all HTML files from markdown
./build.sh

# Test production files
python3 -m http.server 8083
# Visit http://127.0.0.1:8083/
```

**Content Update Workflow:**
```bash
# Edit content
nano zola-site/content/_index.md
nano zola-site/content/tech/_index.md
nano zola-site/content/media/_index.md

# Regenerate HTML
./build.sh

# Commit changes
git add .
git commit -m "Update content from markdown source"
git push origin master
```

## 📝 Content Structure Examples

### Main Page Content (`_index.md`)
```markdown
+++
title = "Masters3d Portfolio"
description = "Software Engineer & Digital Creator"
+++

# About Me
Your bio and introduction content here...

## Featured Work
Portfolio highlights...
```

### Section Pages (`tech/_index.md`, `media/_index.md`)
```markdown
+++
title = "Technical Projects & Development"
description = "Software development portfolio"
template = "tech.html"
+++

# Technical Projects Portfolio
Your technical content here...
```

## 🎨 Template Customization

Templates use Zola's templating syntax. Key variables:
- `{{ section.title }}` - Page title from frontmatter
- `{{ section.content | safe }}` - Rendered markdown content
- `{{ config.title }}` - Site title from config.toml

## ⚠️ Important Notes

1. **Never edit generated HTML files directly** - they will be overwritten
2. **Use correct URLs for development vs production** - build script handles conversion
3. **Test both environments** - Zola serve for development, static files for production
4. **Run build script after every content change** - ensures HTML is up to date
5. **Commit source files, not just generated files** - maintain markdown as source of truth

## 🚀 Benefits of This Workflow

- **Content-focused editing** - Write in markdown, not HTML
- **Version control friendly** - Clear diffs of content changes
- **Error prevention** - Automated generation reduces manual mistakes
- **Consistent output** - Templates ensure uniform styling
- **Professional workflow** - Industry-standard static site generation
- **Future-proof** - Easy to migrate or extend

## 🔧 Troubleshooting

**Page not found in development?**
- Use `/tech/` not `/tech.html` with Zola serve
- Check that content file exists with correct frontmatter

**URLs broken after build?**
- Run `./build.sh` to ensure URL conversion completed
- Check that sed commands in build script completed successfully

**Styling broken?**
- Ensure CSS files are copied: `cp -r css zola-site/static/`
- Check that build script copies assets properly

**Content not updating?**
- Run `./build.sh` after every content change
- Check that you're editing source files, not generated files