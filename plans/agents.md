# Agent Consistency Guidelines

**Purpose**: Ensure consistent decision-making and approaches across multiple agent sessions for the masters3d.github.io migration project.

## Core Decisions & Principles

### 1. Technology Stack
**DECIDED**: Zola (Rust-based static site generator)
- **Rationale**: User prefers non-Ruby solution, wants simplicity, mentioned Rust interest
- **Alternative considered**: Hugo (Go), Publish (Swift)
- **Do NOT change** unless user explicitly requests reconsideration

### 2. Migration Approach
**DECIDED**: Incremental migration with preservation
- **Preserve**: All existing content, custom domain, external links
- **Enhance**: Add blog functionality, improve responsive design
- **Maintain**: Same URL structure, Google Analytics

### 3. Deployment Strategy
**DECIDED**: GitHub Actions → gh-pages branch
- **Rationale**: GitHub Pages doesn't natively support Zola
- **Preserve**: masters3d.com custom domain via CNAME
- **Rollback**: Keep original files in legacy/ folder

### 4. File Management
**DECIDED**: Minimal changes, surgical approach
- **Create**: New Zola structure alongside existing
- **Preserve**: Original index.html, stylesheets, images
- **Document**: All changes in plans/ folder

## Session Consistency Rules

### When Starting New Sessions
1. **Always check** `plans/progress-tracking.md` first
2. **Review** previous decisions in this file
3. **Update** progress tracking with new session info
4. **Continue** from last recorded progress point

### Decision Making
- **Never contradict** previously documented decisions without user input
- **Always document** new decisions in this file
- **Reference** this file when user asks "what did we decide before?"

### Code Changes
- **Minimal modifications** - change as few lines as possible
- **Preserve working code** - don't delete unless absolutely necessary
- **Test incrementally** - build and test after each major change
- **Document changes** - update progress tracking

## Project Structure Standards

```
masters3d.github.io/
├── plans/                 # All planning docs (NEW)
│   ├── README.md
│   ├── migration-strategy.md
│   ├── progress-tracking.md
│   └── agents.md         # This file
├── legacy/               # Original files (backup)
├── zola-site/           # New Zola structure
├── CNAME                # Preserve custom domain
└── [original files]     # Keep until migration complete
```

## Content Guidelines

### Existing Content to Preserve
- **About section**: "Designer, Developer, Product Owner"
- **3D Projects**: Community profile link
- **Video Projects**: All YouTube/Vimeo links (20+ items)
- **GitHub Projects**: iOS Swift, Python, Java project links
- **Styling**: Architect theme appearance

### Content to Enhance
- **Blog functionality**: ✅ **COMPLETED** - Full blog system implemented
- **Responsive design**: Improve mobile experience
- **SEO**: Add meta tags, structured data
- **Performance**: Optimize images, CSS

## Technical Standards

### Zola Specifics
- **Config**: Use `config.toml` for site configuration
- **Content**: Markdown files in `content/` directory
- **Templates**: Tera templating engine
- **Styling**: Preserve existing CSS, convert to Sass if beneficial

### GitHub Actions
- **Trigger**: On push to main branch
- **Build**: Use official Zola action
- **Deploy**: To gh-pages branch
- **Preserve**: CNAME file in output

## Common Questions & Answers

**Q**: "What static site generator are we using?"  
**A**: Zola (Rust-based), decided in Session 1

**Q**: "How are we deploying?"  
**A**: GitHub Actions building to gh-pages branch

**Q**: "What about the custom domain?"  
**A**: Preserving masters3d.com via CNAME file

**Q**: "Can we change the technology choice?"  
**A**: Only if user explicitly requests reconsideration; document reasoning

## Version History

- **v1.0** (2024-12-28): Initial guidelines established
- **v1.1** (2024-09-07): Blog system implementation completed
  - Full Zola blog architecture with RSS support
  - Responsive design matching site theme
  - Taxonomy system (categories/tags)
  - SEO optimization with meta tags
  - Markdown-first content creation workflow
  - **Created using coding agents** - demonstrates AI-assisted development
  - **Repository-based context** - agent instructions stored in codebase
- **v1.2** (2024-09-14): Clean-up and validation session
  - Branch: `clean-up-and-validations`
  - Focus: Deployment fixes, code cleanup, issue resolution
  - Major issue identified: Blog system not deploying (404 on /blog/)
  - Repository cleanup and optimization
- **Future versions**: Update when major decisions change

## Blog System Implementation (Added v1.1)

### Blog Architecture
**IMPLEMENTED**: Complete blog system using Zola
- **Location**: `zola-site/content/blog/` for posts
- **Templates**: `zola-site/templates/blog.html`, `blog-post.html`
- **RSS Feed**: Automatic generation at `/blog/atom.xml`
- **Styling**: Responsive CSS in `static/css/blog.css`

### Content Workflow
**DECIDED**: Markdown-first approach
- **Create posts**: Add `.md` files to `zola-site/content/blog/`
- **Frontmatter**: TOML format with title, date, description, taxonomies
- **Build**: `zola build` generates static site
- **Deploy**: Same GitHub Actions workflow

### Blog Features Implemented
- ✅ **RSS/Atom feed** support
- ✅ **Taxonomy system** (categories and tags)
- ✅ **SEO optimization** (meta tags, Open Graph)
- ✅ **Social sharing** buttons
- ✅ **Responsive design** matching site theme
- ✅ **Navigation integration** across all pages

### Adding New Posts - Instructions for Future Agents
1. **Create file**: `zola-site/content/blog/post-name.md`
2. **Add frontmatter**:
   ```toml
   +++
   title = "Post Title"
   date = 2024-09-07
   description = "SEO description"
   template = "blog-post.html"
   categories = ["category"]
   tags = ["tag1", "tag2"]
   +++
   ```
3. **Write content**: Standard Markdown below frontmatter
4. **Test locally**: `cd zola-site && zola serve`
5. **Build**: `zola build` before committing

### Blog Guidelines for Agents
- **Preserve workflow**: Keep simple file-based posting
- **Maintain design**: Blog matches existing site theme
- **RSS consistency**: All posts auto-include in feed
- **Markdown source**: Always prioritize `.md` files as source of truth
- **Template consistency**: Use `blog-post.html` for all posts
- **Model agnostic**: System works with various coding AI models (GPT-4, Claude, Gemini, etc.)
- **Context preservation**: Agent instructions are part of the repository for consistency