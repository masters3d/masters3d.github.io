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

### 5. Pull Request Target Branch
**DECIDED**: Always open pull requests against `master`
- **Rule**: Every PR must target the `master` branch as its base, unless the user explicitly asks for a different base
- **Rationale**: `master` is the default branch and the single source of truth; PRs accidentally based on another working branch (e.g. another `copilot/*` branch) do not reach `master` when merged
- **Before creating a PR**: verify the base branch is `master`; if a PR was opened against the wrong base, retarget it to `master`

### 6. Markdown Formatting (Prettier + markdownlint)
**DECIDED**: Blog Markdown is formatted with Prettier and linted with markdownlint; `scripts/format_markdown.py` is a thin wrapper that just calls these two tools
- **Rationale**: One-line-per-paragraph posts produce whole-paragraph diffs; Prettier wraps prose to 80 columns for small, reviewable line-level diffs, and markdownlint catches structural issues. Using standard tools (instead of a bespoke script) is portable and well understood
- **Guarantee**: Prettier is configured with `proseWrap: always` (soft breaks render as spaces) and `embeddedLanguageFormatting: off` (fenced sample code is untouched), so the generated HTML is byte-identical before and after formatting
- **Rule for agents (REQUIRED)**: ALWAYS run the formatter before committing. After creating or editing any Markdown, run `npm install` (once) then `python3 scripts/format_markdown.py`, and verify with `python3 scripts/format_markdown.py --check` (must exit clean). Never commit Markdown that has not been through the formatter
- **Enforced**: The PR Validation workflow runs `npm ci` + `python3 scripts/format_markdown.py --check`; incorrectly formatted or lint-failing Markdown fails CI
- **Config**: `.prettierrc.json`, `.markdownlint-cli2.jsonc`, and pinned versions in `package.json`
- **Do NOT** hand-wrap or hand-reflow paragraphs; always let Prettier do it so the result is deterministic and idempotent

## Session Consistency Rules

### When Starting New Sessions
1. **Always check** `plans/progress-tracking.md` first
2. **Review** previous decisions in this file
3. **Read** `plans/session-context.md` for immediate context
4. **Check** `plans/current-task.md` for active work
5. **Update** progress tracking with new session info
6. **Continue** from last recorded progress point

### When Copilot/Agent Restarts or Has Issues
1. **CRITICAL**: Read `plans/session-context.md` FIRST - contains immediate context
2. **Check branch status**: `git branch` and `git status` 
3. **Review recent commits**: `git log --oneline -5`
4. **Read current task**: `plans/current-task.md` for active objectives
5. **Check enhancement roadmap**: `plans/enhancement-roadmap.md` for comprehensive plan
6. **Verify local environment**: Check if Zola server running, test site accessibility
7. **Update session info**: Add new session entry to `plans/session-context.md`

### Session Context Preservation Protocol
**MANDATORY**: Every session must maintain detailed context in `plans/session-context.md`

#### Required Context Elements:
- **Current branch and status**
- **Last completed actions**
- **Active tasks and next steps**
- **Local development state** (server running, port, URLs)
- **Known issues and blockers**
- **Recent discoveries or important notes**
- **Handoff instructions for next session**

#### Context Update Frequency:
- **Start of session**: Read and update with new session info
- **Major milestone**: Document progress and state changes
- **End of session**: Complete handoff notes and next steps
- **Before any extended break**: Ensure context is current and detailed

### Decision Making
- **Never contradict** previously documented decisions without user input
- **Always document** new decisions in this file
- **Reference** this file when user asks "what did we decide before?"
- **Check session-context.md** for recent context and state

### Code Changes
- **Minimal modifications** - change as few lines as possible
- **Preserve working code** - don't delete unless absolutely necessary
- **Test incrementally** - build and test after each major change
- **Document changes** - update progress tracking

### Writing Style Preferences
- **Parentheses over em-dashes** - Use parentheses () instead of em-dashes (—) for parenthetical expressions
  - Example: "text (clarification)" instead of "text—clarification"
  - Maintains readability and follows user's preferred style
- **Bullet lists** - Use hyphens (-) for bullet lists (standard markdown format)
- **Avoid overloaded words** - Don't use "impact" (too overloaded). Use specific alternatives:
  - Instead of "user impact" → "user value" or "user outcomes"
  - Instead of "impact on the team" → "effect on the team" or "benefit to the team"
  - Instead of "business impact" → "business value" or "business results"
- **Words to avoid** - Do not use these words in blog posts; prefer more precise, respectful alternatives:
  - "stupid" - avoid entirely (dismissive and imprecise). Use "misguided", "flawed", "ill-suited", "not optimal", or name the specific problem instead
  - "impact" - see "Avoid overloaded words" above
  - When adding new posts or editing existing ones, survey the text for these words and remove them where they are not needed
- **Minimize section breaks for narrative flow** - Avoid excessive section headings that break narrative flow
  - Write blog posts as cohesive stories rather than overly segmented documentation
  - Minimize h2 (##) section headings - use only for major inflection points (aim for 3-4 max in a blog post)
  - Avoid subsection headings (###) entirely in blog posts - they fragment the narrative
  - Integrate related content into flowing paragraphs instead of creating separate sections
  - Let content flow naturally without artificial breaks
  - Goal: Improve readability and maintain storytelling quality
  - Example: A blog post should have 3 major sections marking key turning points, not 10+ sections for every topic

### Common Authorial Voice

**DECIDED**: Use the posts published before 2015 as the primary voice reference,
especially `palm-sony-android-iphone-blackberry.md` (2009) and
`apple-swift-apps-everywhere-prediction.md` (2014). Preserve their historical
wording rather than rewriting them to match newer conventions.

- **Begin with something noticed or lived** - Open on a moment, object, problem,
  or reaction that actually prompted the idea. Do not begin with an abstract
  summary of what the post will cover.
- **Use first person when it carries evidence** - "I remember," "I noticed," and
  "I think" should introduce direct experience or honest judgment, not decorate a
  generic explanation.
- **Keep specific details** - Names, dates, prices, tools, failed attempts, and
  surprising preferences make the voice recognizable. Do not sand those details
  into generic professional prose.
- **Move from concrete to abstract** - Tell the story or show the example first,
  then extract the principle, then explain where else it applies.
- **Be opinionated without pretending certainty** - State conclusions directly,
  and clearly label predictions, incomplete evidence, or changes of mind.
- **Prefer conversational precision** - Use short declarative sentences,
  occasional questions, and natural transitions. Avoid corporate language,
  inflated claims, generic enthusiasm, and tutorial voice unless the post is
  actually a tutorial.
- **Keep the author's energy** - Curiosity, delight, frustration, and surprise
  are part of the voice. Edit for clarity without making every post sound
  detached or academically uniform.
- **End with earned reflection** - Return to the opening observation, say what
  changed in the author's understanding, connect to related posts where useful,
  and state why the idea matters.

**Review test**: A reader should be able to answer four questions after a post:
What did the author notice? What specific experience supports it? What principle
did the author extract? Why does it matter now?

### Editorial Tracks: Stable Voices by Post Type

**DECIDED**: Every blog post belongs to exactly one editorial track. The common
authorial voice remains the baseline, while the track determines the post's
emphasis, evidence, pacing, and visual treatment. Tags connect related ideas
across tracks; they do not replace the primary track.

- **Quest Engine** (`quest-engine`) - Build one connected framework. Define terms
  precisely, show how each idea changes or extends Search, Drive, and Renew, and
  link backward to a prerequisite and forward to an application. Use conceptual
  comparisons only after grounding the framework in a concrete observation.
- **Engineering Systems** (`engineering-systems`) - Lead with a failure mode,
  constraint, or working system. Explain mechanisms before recommendations,
  name tradeoffs and boundaries, and include enough technical evidence that a
  reader can evaluate the argument rather than accept it on authority.
- **AI & Tools** (`ai-and-tools`) - Write as an experiment log, not a product
  announcement. State what was tried, what changed in the work, what failed, and
  which judgment remained human. Prefer measured capability claims over model
  or vendor enthusiasm.
- **Leadership & Teams** (`leadership-and-teams`) - Begin with observed team
  behavior. Trace incentives, ownership, communication, and system boundaries
  before giving advice. Avoid generic management language and keep claims tied
  to specific operating conditions.
- **Field Notes** (`field-notes`) - Preserve first-person detail, chronology,
  artifacts, and uncertainty. Let the lesson emerge from the record. Portfolio
  and reference entries may use lists and more headings, but their introductions
  and conclusions retain the common voice.

Front matter uses one human-readable `categories` value plus the matching
`extra.editorial_track` slug. Posts that participate in the Quest Engine series
also use `extra.series = "quest-engine"`. The reading-order number is derived
automatically from post dates at build time (oldest post is 1), so it is never
stored per post — add the post with the correct `date` and its position follows.

**Content-type exceptions**: Portfolio pages, reference guides, historical
artifacts, source lists, and appendices may use more headings, tables, or lists
than narrative posts. Do not force the Quest Arc onto reference material. Keep
the narrative introduction and conclusion in the common voice, and use the
structure that makes the reference content easiest to navigate.

### Blog Post Meta-Structure: The Quest Arc (Exploration → Execution → Reflection)

**DECIDED**: Every narrative blog post should be built on a single Quest-Engine backbone so it reads like a quest, not a pile of notes. Before writing (or revising) a post, name the quest: what is the angle, what question is being chased, and what is the "why" the reader should leave with. Then carry that one thread from the first line to the last.

The backbone has three phases, which map directly to the [Quest Engine](/blog/quest-engine-introduction/) cycle (Search/Mastery = before, Drive/Autonomy = during, Renew/Purpose = after):

1. **Exploration (Searching, the "before")** — Open with a real, personal observation or a noticed pattern, and name the question it raises. This sets up the quest and pulls the reader into Searching mode. Do not lead with the thesis; lead with what you noticed.
2. **Execution (Driven, the "during")** — Develop the idea across 3-4 h2 sections. Move from concrete example to abstracted principle to application. Each h2 develops one component of the thesis. This is where the mechanism or definition gets pinned down.
3. **Reflection (Renew, the "after")** — Close by looking back and answering the "why." End with an italicized reflection paragraph that (a) points backward to the synthesis, (b) points outward to related posts (cross-links), and (c) points upward to why it matters. This is a near-universal convention across existing posts and should be preserved.

**Why this matters**: A post without this backbone feels incoherent even when each paragraph is fine (the reader receives no single message). The point of the quest arc is coherence: one thread the reader can follow, ending in a takeaway that answers the "why."

**Observed invariants across existing posts** (verified by analyzing the current blog corpus; use these as a checklist when writing or reviewing a post):
- **Opening observation**: present in essentially every post ("I have been watching...", "The first time I really tasted...", "I've started replacing...").
- **Italicized closing reflection**: present in nearly every post; it always cross-links to related posts and states the takeaway.
- **3-4 h2 sections** organizing the execution phase (see the section-break guidance above).
- **Quest Engine mapping**: implicit or explicit, but always present — each post is itself a small search → drive → renew loop.
- **Concrete-before-abstract**: lead with the lived example, then generalize, then connect to the broader idea web.

**For agent authors and reviewers**: When drafting or revising a post, check that all three phases are present and that a single "why" runs through them. If a draft is "a collection of individuals who happen to wear the same shirt" (paragraphs with no shared thread), the fix is to name the quest and re-cohere the post around it, not to add more sections.

### Recurring Framing: Personality Styles (DOPE / Director-Thinker)

**DECIDED**: When writing about communication or personality styles (for example
the DOPE bird model: Dove/Relater, Owl/Thinker, Peacock/Socializer,
Eagle/Director), hold these positions consistently:

- **No personality is good or bad** - Never rank the four styles from best to
  worst. Fit depends on context: the Dove is ideal for therapy and the social
  sciences, the Peacock for many performing/creative roles (though plenty of
  artists are secluded). Ranking a style as the "worst" is a category error.
- **Personalities are contextual and can change** - A person shows different
  personalities across rooms (family, friends, work) and across seasons of life.
  Personality is mostly what you are and partly what you have learned; it is not
  a fixed grade.
- **There is a learnable work personality** - The best performers cue the
  communication style a moment calls for and step back out. This is a skill you
  can exercise, not a trait you were issued.
- **Engineering fit is Director + Thinker only** - For engineering, the Director
  (Eagle) and Thinker (Owl) are the two work-mode personalities worth
  practicing. Map only these to the Quest Engine: Thinker → Searching, Director →
  Being Driven. Do not force the Dove or Peacock onto the framework; not every
  personality maps cleanly, and forcing it cheapens the mapping.

Reference post: `zola-site/content/blog/director-and-thinker-work-mode-personalities.md`.

## Project Structure Standards

```
masters3d.github.io/
├── plans/                 # All planning docs (CRITICAL FOR CONTEXT)
│   ├── README.md
│   ├── session-context.md # READ FIRST - Current session state
│   ├── current-task.md    # Active task details
│   ├── enhancement-roadmap.md # Comprehensive improvement plan
│   ├── progress-tracking.md   # Overall project progress
│   └── agents.md         # This file - Agent guidelines
├── legacy/               # Original files (backup) 
├── zola-site/           # New Zola structure (MAIN WORKING DIRECTORY)
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

**Q**: "What's the current project status?"  
**A**: Portfolio migration COMPLETED and DEPLOYED. Now in Enhancement & Optimization phase.

**Q**: "What branch should I be on?"  
**A**: `enhancements-and-optimizations` for current work (check session-context.md). **Always open pull requests against `master`** (see Core Decision 5).

**Q**: "Where is the live site?"  
**A**: https://masters3d.com (deployed) and https://masters3d.github.io (GitHub Pages)

**Q**: "How do I get current context if copilot restarts?"  
**A**: Read `plans/session-context.md` FIRST, then current-task.md and enhancement-roadmap.md

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
- **v1.3** (2024-01-06): Enhancement & Optimization Phase Launch
  - Branch: `enhancements-and-optimizations`
  - **DEPLOYED**: Portfolio migration successfully completed (PR #9 merged)
  - **NEW PHASE**: Performance, SEO, content expansion, UX improvements
  - **Context System Enhanced**: Robust session preservation for agent continuity
  - **Live Site**: https://masters3d.com - Fully functional blog-centric portfolio
  - **Agent Restart Protocol**: Enhanced guidelines for seamless context restoration
- **v1.4** (2026-07-08): Blog post meta-structure formalized
  - Documented the Quest Arc backbone for posts: Exploration → Execution → Reflection
  - Derived from analyzing the full blog corpus for the exploration/execution/reflection pattern
  - Purpose: keep every post coherent around a single "why" instead of a set of disconnected sections
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
4. **Format Markdown**: `python3 scripts/format_markdown.py` (required; runs Prettier + markdownlint, keeps diffs small, does not change rendered output)
5. **Test locally**: `cd zola-site && zola serve`
6. **Build**: `zola build` before committing

### Blog Guidelines for Agents
- **Preserve workflow**: Keep simple file-based posting
- **Maintain design**: Blog matches existing site theme
- **RSS consistency**: All posts auto-include in feed
- **Markdown source**: Always prioritize `.md` files as source of truth
- **Template consistency**: Use `blog-post.html` for all posts
- **Model agnostic**: System works with various coding AI models (GPT-4, Claude, Gemini, etc.)
- **Context preservation**: Agent instructions are part of the repository for consistency

## Enhancement Phase Guidelines (Added v1.3)

### Current Phase: Enhancement & Optimization
**Status**: ACTIVE - Portfolio migration completed, now optimizing
**Branch**: `enhancements-and-optimizations`
**Live Site**: https://masters3d.com

### Enhancement Priorities
1. **Performance optimization** - Speed, loading, asset optimization
2. **SEO enhancement** - Search visibility and ranking
3. **Content expansion** - Blog posts and portfolio updates
4. **User experience** - Mobile, accessibility, navigation
5. **Technical excellence** - Code quality, maintainability

### Agent Restart Recovery Process
When copilot restarts or has issues:

1. **IMMEDIATE**: Read `plans/session-context.md` 
2. **Check branch**: `git branch` (should be `enhancements-and-optimizations`)
3. **Check status**: `git status` and `git log --oneline -5`
4. **Read tasks**: `plans/current-task.md` for active work
5. **Review roadmap**: `plans/enhancement-roadmap.md` for comprehensive plan
6. **Test environment**: Verify local development setup
7. **Update context**: Add new session entry to session-context.md

### Context Maintenance Requirements
- **Update session-context.md** at start, milestones, and end of session
- **Document all discoveries** and important decisions
- **Maintain handoff notes** for seamless transitions
- **Preserve technical details** about local development state
- **Record next steps** clearly for continuation