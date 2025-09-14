# 🚀 GitHub Pages Deployment Instructions

## ✅ **ZOLA DEPLOYMENT APPROACH** (Current Setup)

This repository uses **Zola static site generator** with **GitHub Actions** for automated deployment.

### 🎯 **How It Works:**
1. **Markdown content** in `zola-site/content/` is the source of truth
2. **GitHub Actions** builds the Zola site on every push to master
3. **Automated deployment** to GitHub Pages from `zola-site/public/`
4. **Blog system included** with RSS feeds and responsive design

### 📝 **Content Update Workflow:**

**To update content:**
```bash
# 1. Edit your content
vim zola-site/content/_index.md

# 2. Test locally (optional)
cd zola-site && zola serve

# 3. Commit and push
git add .
git commit -m "Update content"
git push origin master

# ✨ GitHub Actions builds and deploys automatically!
```

### 🛠️ **Deployment Details:**

**GitHub Actions Workflow** (`.github/workflows/static.yml`):
- ✅ **Triggers**: Push to `master` branch
- ✅ **Build**: Installs Zola and builds the site
- ✅ **Deploy**: Deploys from `zola-site/public/` to GitHub Pages
- ✅ **Includes**: Blog system, RSS feeds, and responsive design

### 📁 **Repository Structure:**

```
masters3d.github.io/
├── 📁 zola-site/           # ← Source of truth (Zola site)
│   ├── 📁 content/         # ← Edit content here
│   │   ├── _index.md       # ← Homepage content
│   │   ├── tech/_index.md  # ← Tech portfolio content
│   │   ├── media/_index.md # ← Media portfolio content
│   │   └── blog/           # ← Blog posts
│   ├── 📁 templates/       # ← HTML templates
│   ├── 📁 static/          # ← CSS, images, assets
│   ├── 📁 public/          # ← Generated site (auto-built)
│   └── config.toml         # ← Site configuration
├── 📁 .github/workflows/   # ← Deployment automation
├── 📁 plans/               # ← Planning and documentation
├── CNAME                   # ← Custom domain (masters3d.com)
└── README files            # ← This documentation
```

**Content Sources (Edit These):**
- **Homepage**: `zola-site/content/_index.md`
- **Tech Portfolio**: `zola-site/content/tech/_index.md`
- **Media Portfolio**: `zola-site/content/media/_index.md`
- **Blog Posts**: `zola-site/content/blog/*.md`
- **Site Config**: `zola-site/config.toml`

**Generated Files (Don't Edit):**
- **Built Site**: `zola-site/public/` (auto-generated)
- **Live Site**: https://masters3d.com (auto-deployed)
### ⚡ **Benefits of This Approach:**

1. **✅ Markdown-first content management** - Professional workflow
2. **✅ Automated deployment** - No manual build steps
3. **✅ Blog system included** - RSS feeds, responsive design
4. **✅ Version control** - All content tracked in git
5. **✅ Fast and reliable** - Zola builds are lightning fast
6. **✅ SEO optimized** - Proper meta tags, sitemaps, feeds

### 🔍 **Troubleshooting:**

**Blog not showing?**
- Check that blog posts are in `zola-site/content/blog/`
- Verify GitHub Actions workflow completed successfully
- Blog is available at `/blog/` after deployment

**Local preview not working?**
```bash
cd zola-site
zola serve
# Visit http://127.0.0.1:1111/
```

**Need to rollback?**
```bash
git revert <commit-hash>
git push origin master
```

1. **🚀 Lightning Fast Deployment** - No build time
2. **🛡️ Zero Build Failures** - Static files always work  
3. **🔧 Simple Debugging** - You can see exactly what gets deployed
4. **📱 Reliable** - No dependency issues or version conflicts
5. **⚡ Instant Rollbacks** - Just revert a git commit

### 🎯 **One-Time GitHub Setup:**

Ensure GitHub Pages is configured:
1. **Repository Settings** → **Pages**
2. **Source**: "GitHub Actions" 
3. **Done!** - All future pushes to master will deploy automatically

---

## 📋 **Change History:**

### ✅ v2.0 - Static Deployment (Current)
- **Switched to static file deployment**
- **Added build.sh script** for easy content updates
- **Simplified workflow** - just push to deploy
- **Faster, more reliable** than build-on-deploy

### ✅ v1.1 - Fixed Deployment Issues  
- **Fixed GitHub Actions permissions** 
- **Updated to modern deployment methods**
- **Branch protection compliance**

### ✅ v1.0 - Initial Zola Setup
- **Migrated from Jekyll** to Zola
- **Modern static site structure**
- **Repository cleanup** (removed 44KB of legacy files)