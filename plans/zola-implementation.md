# Zola Implementation Plan

## Overview
Detailed implementation plan for migrating masters3d.github.io to Zola static site generator.

## Phase 1: Environment Setup

### Install Zola
```bash
brew install zola
```

### Verify Installation
```bash
zola --version
```

### Create Zola Site Structure
```bash
# From repo root
zola init zola-site --force
cd zola-site
```

Expected structure:
```
zola-site/
├── config.toml          # Site configuration
├── content/             # Markdown content
├── static/              # Static assets (CSS, images, JS)
├── templates/           # Tera templates
└── themes/              # Themes (if using external)
```

## Phase 2: Content Migration

### Extract Current Content

**From index.html, extract:**
1. **About Section**: "Designer, Developer, Product Owner"
2. **3D Projects**: Community profile links
3. **Video Projects**: 11+ YouTube/Vimeo links
4. **GitHub Projects**: Organized by language (Swift, Python, Java)

### Create Content Files

**Main Pages:**
- `content/_index.md` - Homepage/About
- `content/projects/_index.md` - Projects overview
- `content/blog/_index.md` - Blog section (new)

**Project Categories:**
- `content/projects/3d.md` - 3D projects
- `content/projects/video.md` - Video projects  
- `content/projects/github.md` - GitHub projects

### Content Structure Example
```markdown
+++
title = "About"
date = 2024-12-28
template = "page.html"
+++

# About
Designer, Developer, Product Owner.
```

## Phase 3: Template Creation

### Base Template (`templates/base.html`)
- HTML5 structure
- Include meta tags, stylesheets
- Google Analytics integration
- Header/footer layout

### Page Templates
- `templates/index.html` - Homepage
- `templates/page.html` - Standard pages
- `templates/section.html` - Section overviews

### Component Templates
- Header with navigation
- Project cards/listings
- Footer

## Phase 4: Styling Migration

### Copy Existing Styles
1. Move `stylesheets/` to `static/css/`
2. Update paths in templates
3. Consider converting to Sass (optional)

### Preserve Current Look
- Architect theme styling
- Google Fonts integration
- Responsive layout

## Phase 5: Configuration

### config.toml Setup
```toml
base_url = "https://masters3d.com"
title = "Masters3d"
description = "Technical. Creative. Tactical. Director."

[markdown]
highlight_code = true

[extra]
google_analytics = "UA-5533092"
github_username = "masters3d"
```

## Phase 6: GitHub Actions Setup

### Workflow File (`.github/workflows/deploy.yml`)
```yaml
name: Deploy Zola site

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - uses: taiki-e/install-action@v2
      with:
        tool: zola
    - name: Build site
      run: |
        cd zola-site
        zola build
    - name: Deploy to GitHub Pages
      uses: peaceiris/actions-gh-pages@v3
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: ./zola-site/public
        cname: masters3d.com
```

## Phase 7: Testing & Validation

### Local Testing
```bash
cd zola-site
zola serve
# Visit http://127.0.0.1:1111
```

### Content Validation
- [ ] All sections present
- [ ] All external links working
- [ ] Styling matches original
- [ ] Mobile responsive
- [ ] Google Analytics working

### Deployment Testing
- [ ] GitHub Actions runs successfully
- [ ] Site deploys to gh-pages
- [ ] Custom domain resolves
- [ ] HTTPS works

## Implementation Checklist

### Environment
- [ ] Install Zola
- [ ] Create site structure
- [ ] Test local build

### Content
- [ ] Extract content from HTML
- [ ] Create Markdown files
- [ ] Organize project sections
- [ ] Add blog structure

### Templates
- [ ] Create base template
- [ ] Create page templates
- [ ] Implement navigation
- [ ] Add Google Analytics

### Styling
- [ ] Migrate CSS files
- [ ] Update asset paths
- [ ] Test responsive design
- [ ] Verify fonts/icons

### Deployment
- [ ] Create GitHub Action
- [ ] Test build process
- [ ] Verify custom domain
- [ ] Monitor first deployment

### Launch
- [ ] Final content review
- [ ] Performance testing
- [ ] SEO verification
- [ ] Create rollback plan

## Timeline Estimate

- **Phase 1-2**: 1 session (Setup + Content)
- **Phase 3-4**: 1 session (Templates + Styling)  
- **Phase 5-6**: 1 session (Config + Deployment)
- **Phase 7**: 1 session (Testing + Launch)

**Total**: ~4 focused sessions