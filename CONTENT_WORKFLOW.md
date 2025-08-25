# Content Management Workflow

This project uses **Zola** static site generator with **Markdown as the source of truth** for ALL content pages.

## 🚀 Quick Start

### Making Content Changes

1. **Edit the markdown source files:**
   ```bash
   # Edit main page content
   nano zola-site/content/_index.md
   
   # Edit tech portfolio content
   nano zola-site/content/tech/_index.md
   
   # Edit media portfolio content  
   nano zola-site/content/media/_index.md
   
   # Edit site config (title, tagline, etc.)
   nano zola-site/config.toml
   ```

2. **Edit templates (if needed for layout changes):**
   ```bash
   # Edit main page template
   nano zola-site/templates/index.html
   
   # Edit tech page template
   nano zola-site/templates/tech.html
   
   # Edit media page template
   nano zola-site/templates/media.html
   ```

3. **Build and deploy:**
   ```bash
   ./build.sh
   git add .
   git commit -m "Update content from markdown source"
   git push origin master
   ```

## 📁 File Structure

```
masters3d.github.io/
├── zola-site/              # 📝 SOURCE FILES (edit these)
│   ├── content/
│   │   ├── _index.md       # Main page content in markdown
│   │   ├── tech/
│   │   │   └── _index.md   # Tech portfolio content in markdown
│   │   └── media/
│   │       └── _index.md   # Media portfolio content in markdown
│   ├── templates/
│   │   ├── index.html      # Main page template with Zola templating
│   │   ├── tech.html       # Tech page template with Zola templating
│   │   └── media.html      # Media page template with Zola templating
│   ├── static/
│   │   ├── css/            # Stylesheets (copied from root)
│   │   └── images/         # Images (copied from root)
│   └── config.toml         # Site configuration
├── index.html              # 🤖 GENERATED (don't edit directly)
├── tech.html               # 🤖 GENERATED (don't edit directly)
├── media.html              # 🤖 GENERATED (don't edit directly)
└── build.sh                # Build script
```

## ⚡ Workflow Benefits

### ✅ Markdown as Source of Truth
- **Easy editing** - Write content in clean markdown
- **Version control friendly** - Clear diffs for content changes
- **No HTML mistakes** - Markdown prevents broken tags
- **Focus on content** - Separate content from presentation

### ✅ Automated Generation
- **Consistent output** - Template ensures uniform styling
- **Build script** - One command to update everything
- **Asset management** - Automatically copies CSS and images
- **Error prevention** - Build fails if there are issues

### ✅ Professional Workflow
- **Content separation** - Markdown content, HTML templates, CSS styling
- **Maintainable** - Easy to update content without touching HTML
- **Scalable** - Can easily add more pages or sections
- **Documentation** - Clear process for future updates

## 🛠️ Commands

### Content Updates
```bash
# Edit main page content
nano zola-site/content/_index.md

# Edit tech portfolio content
nano zola-site/content/tech/_index.md

# Edit media portfolio content
nano zola-site/content/media/_index.md

# Build and update all static files
./build.sh

# Preview locally (optional)
cd zola-site && zola serve --port 8084
```

### Template/Design Updates
```bash
# Edit main page template
nano zola-site/templates/index.html

# Edit tech page template
nano zola-site/templates/tech.html

# Edit media page template
nano zola-site/templates/media.html

# Edit site configuration
nano zola-site/config.toml

# Rebuild all pages
./build.sh
```

### Asset Updates
```bash
# Update CSS or images in root directory
# They will be copied to zola-site/static/ automatically during build
./build.sh
```

## 🔍 Local Development

```bash
# Serve locally with live reload (Zola development server)
cd zola-site
zola serve --port 8084
# Site available at http://127.0.0.1:8084

# OR serve final built files (production preview)
./build.sh
python3 -m http.server 8083
# Site available at http://127.0.0.1:8083
```

## ⚠️ Important Notes

- **DON'T edit HTML files directly** - `index.html`, `tech.html`, and `media.html` get overwritten by the build
- **DO edit markdown files** - these are the source of truth:
  - `zola-site/content/_index.md` for main page
  - `zola-site/content/tech/_index.md` for tech portfolio
  - `zola-site/content/media/_index.md` for media portfolio
- **Run `./build.sh`** after any content or template changes
- **The build script copies assets automatically** from root to zola-site/static/

## 📋 Content Structure Examples

### Main Page (_index.md)
```markdown
+++
title = "Masters3d"
+++

<nav>...</nav>  # HTML is allowed in markdown

## About
Content in **markdown** with emphasis...

### 💻 Software Development
- **Mobile Development:** Details...
- **Web Development:** Details...

### 🎬 Media Production & Digital Content  
- **Documentary Production:** Details...
```

### Tech Portfolio (tech/_index.md)
```markdown
+++
title = "Technical Projects & Development"
description = "Software development projects..."
template = "tech.html"
+++

# Technical Projects Portfolio

## 📱 Mobile Development
- [**Project Name**](link) - Description
- [**Another Project**](link) - Description

## 🌐 Web Development
- Project listings...
```

### Media Portfolio (media/_index.md)
```markdown
+++
title = "Media Projects & Digital Production"
description = "Video production work..."
template = "media.html"
+++

# Media Projects Portfolio

## Humanitarian & Ministry Work
Content with embedded videos:

<iframe width="560" height="315" src="..."></iframe>
```

## 🎯 Summary

This workflow ensures **all portfolio content** is:
- ✅ **Maintainable** - Edit in clean markdown
- ✅ **Version-controlled** - Clear content diffs
- ✅ **Professional** - Consistent template output
- ✅ **Scalable** - Easy to add new sections or pages

**Markdown is now the source of truth for ALL pages!** 🌟