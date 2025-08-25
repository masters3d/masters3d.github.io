# Static Site Generator Migration Strategy

## Current State Analysis

**Repository**: masters3d.github.io  
**Current Setup**: Traditional GitHub Pages with static HTML  
**Domain**: masters3d.com (via CNAME)  
**Content Structure**:
- Single-page portfolio site
- Sections: About, 3D Projects, Video Projects, GitHub Projects, Plans
- Custom styling with Architect theme
- Google Analytics integration

## Migration Goals

1. **Move away from Ruby/Jekyll dependency**
2. **Enable easy content management and blogging**
3. **Maintain existing content and styling**
4. **Keep custom domain (masters3d.com)**
5. **Preserve GitHub Pages hosting**

## Static Site Generator Options

### Option 1: Zola (Rust) ⭐ RECOMMENDED
**Pros**:
- Single binary installation (`brew install zola`)
- Zero runtime dependencies
- Fast build times
- Built-in Sass compilation
- Simple configuration (TOML)
- Good theming system
- Native blog support

**Cons**:
- Smaller community than Hugo
- Fewer pre-built themes

**Implementation Complexity**: Low

### Option 2: Hugo (Go)
**Pros**:
- Largest static site generator community
- Thousands of themes available
- Excellent documentation
- Very fast builds
- Mature ecosystem

**Cons**:
- More complex configuration
- Can be overwhelming with options

**Implementation Complexity**: Medium

### Option 3: Publish (Swift)
**Pros**:
- Native Swift experience
- Type-safe content management
- Excellent for developers familiar with Swift

**Cons**:
- More complex setup
- Smaller community
- Requires Swift knowledge

**Implementation Complexity**: High

## Recommended Approach: Zola

### Phase 1: Setup & Infrastructure
- [ ] Install Zola locally
- [ ] Create basic Zola site structure
- [ ] Set up GitHub Actions for deployment
- [ ] Test deployment pipeline

### Phase 2: Content Migration
- [ ] Extract content from index.html
- [ ] Convert to Markdown format
- [ ] Create page templates
- [ ] Migrate styling (CSS)

### Phase 3: Enhancement
- [ ] Add blog functionality
- [ ] Improve responsive design
- [ ] Add new sections as needed
- [ ] SEO optimization

### Phase 4: Go Live
- [ ] Final testing
- [ ] Switch deployment
- [ ] Monitor and fix issues

## Deployment Strategy

Since GitHub Pages only natively supports Jekyll, we'll use **GitHub Actions** to:
1. Build the site with Zola
2. Deploy to `gh-pages` branch
3. Maintain the same URL structure

## Rollback Plan

Keep the current `index.html` in a `legacy/` folder for quick rollback if needed.