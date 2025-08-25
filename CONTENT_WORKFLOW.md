# Content Management Workflow

This project uses **Zola** static site generator with **Markdown as the source of truth** for content.

## 🚀 Quick Start

### Making Content Changes

1. **Edit the markdown source:**
   ```bash
   # Edit main content
   nano zola-site/content/_index.md
   
   # Edit site config (title, tagline, etc.)
   nano zola-site/config.toml
   
   # Edit HTML template (layout, styling)
   nano zola-site/templates/index.html
   ```

2. **Build and deploy:**
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
│   │   └── _index.md       # Main content in markdown
│   ├── templates/
│   │   └── index.html      # HTML template with Zola templating
│   ├── static/
│   │   ├── css/            # Stylesheets (copied from root)
│   │   └── images/         # Images (copied from root)
│   └── config.toml         # Site configuration
├── index.html              # 🤖 GENERATED (don't edit directly)
├── media.html              # Manual HTML pages
├── tech.html               # Manual HTML pages
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
# Edit main content
nano zola-site/content/_index.md

# Build and update static files
./build.sh

# Preview locally (optional)
cd zola-site && zola serve
```

### Template/Design Updates
```bash
# Edit HTML template
nano zola-site/templates/index.html

# Edit site configuration
nano zola-site/config.toml

# Rebuild
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
# Serve locally with live reload
cd zola-site
zola serve

# Site available at http://127.0.0.1:1111
```

## ⚠️ Important Notes

- **DON'T edit `index.html` directly** - it gets overwritten by the build
- **DO edit `zola-site/content/_index.md`** - this is the source of truth
- **Run `./build.sh`** after any content changes
- **The build script copies assets automatically** from root to zola-site/static/

## 📋 Content Structure in _index.md

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

This workflow ensures content is maintainable, version-controlled, and professional! 🌟