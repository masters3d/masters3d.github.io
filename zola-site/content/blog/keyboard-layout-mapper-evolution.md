+++
title = "The Evolution of Keyboard Layout Config Mapper: When Agents Are Better Than Automation"
date = 2025-12-11
description = "A deep dive into how a keyboard configuration project evolved from manual Go programming to agent-assisted development, and the surprising realization that having agents make direct changes is simpler than writing code to automate everything."
template = "blog-post.html"
categories = ["development", "ai", "meta"]
tags = ["agents", "automation", "keyboards", "golang", "copilot", "productivity"]
draft = true
+++

Sometimes the best way to understand the future of software development is to watch a project evolve through different paradigms. The [Keyboard Layout Config Mapper (KLCM)](https://github.com/masters3d/keyboard_layout_config_mapper) project is a perfect case study in how AI-assisted development is fundamentally changing our approach to automation.

## The Problem: Managing Multiple Keyboard Configurations

If you use multiple ergonomic keyboards—Kinesis Advantage360, MoErgo Glove80, custom mods with Nice!Nano controllers—you face a unique challenge: keeping your keyboard layouts synchronized across different firmware systems (QMK, ZMK) with different configuration formats.

The vision was clear: create a tool that could parse, validate, and sync keyboard configurations across multiple keyboards, acting as a single source of truth for your layout preferences.

## Phase 1: The Manual Coding Approach (2022)

### The Initial Implementation

In April 2022, the project started with what any experienced developer would do: **write comprehensive code to solve the problem programmatically**.

The initial PR (#1) was massive—a proper software engineering solution with:

- **Complete Go packages** for keyboard configuration parsing
- **HID to keycode mappings** for different firmware types
- **Parser infrastructure** for QMK and ZMK config formats
- **Validation and testing framework** with proper test coverage
- **Merge and sync algorithms** to copy layouts between keyboards
- **String manipulation** for in-place file editing

The commit messages tell the story of deep technical work:
- "we are now able to parse qmk configs with out any changes to the source text"
- "tests are passing"
- "adding logic to edit files in place"
- "success: automated config change. Still need to validate on hardware"

This was **proper software engineering**. Parser generators, type systems, test-driven development, abstractions for different firmware formats. The kind of code that feels satisfying to write because it's solving a hard problem with elegance.

### The Reality Check

But here's what actually happened: the tool worked, but it was complex. Every new keyboard layout feature required updating parsers. Every firmware update could break the mappings. The "simple" problem of keeping keyboard configs in sync required maintaining a sophisticated parsing and transformation pipeline.

The code existed. It technically worked. But the maintenance burden was real.

## Phase 2: The Stalling Period (2023)

After the initial burst of development, 2023 saw minimal activity:
- A couple of config file updates
- Some layout experiments
- But no major development on the tooling itself

This is the classic pattern: the automation tool exists, but maintaining it feels like more work than just... manually editing the configs. The tool that was supposed to save time required its own time investment.

The sophisticated Go codebase sat largely dormant, a monument to the challenge of maintaining automation infrastructure.

## Phase 3: The Copilot Renaissance (2025)

Fast forward to August 2025, and something interesting happened. The project came back to life, but with a completely different approach.

### Building Better Tools with AI Assistance

The V5 target release (PR #12) rebuilt the project with modern CLI tooling:
- Complete CLI tool with Cobra framework
- Git-style diff functionality
- GitHub PR automation
- Interactive workflows
- **2000+ lines of old code removed**

The commit message is revealing:
> "🧹 Cleanup Completed: Removed old source/ directory (2000+ lines unused code)"

But here's the key insight: this wasn't about abandoning the parsing and automation. It was about using AI coding assistants to **build better tools faster**.

### The Critical Realization

Then came the recent PRs in November-December 2025, and you can see the pattern shift:

**PR #28**: "Add screenshot key to right pinky column on all ZMK keyboards"
- Direct changes to `adv360.keymap`, `pillzmod_pro.keymap`, `glove80.keymap`
- Simple, surgical modifications across three files
- No parser infrastructure needed

**PR #26**: "Streamline KLCM for ZMK-only keyboards + add pedal docs"
- Focused on simplification
- Documentation updates
- Direct config changes

**PR #23**: Multiple keyboard config updates with clear, specific changes

The pattern is clear: **Instead of writing code to automate changes across keyboards, just ask an AI agent to make the changes directly**.

## The Paradigm Shift: Why This Matters

Here's the profound realization that emerged from this project's evolution:

### The Old Way: Write Code to Automate
1. Identify a repetitive task (syncing keyboard configs)
2. Write parsers to understand the config format
3. Write transformers to modify configs
4. Write validators to ensure correctness
5. Maintain this infrastructure as formats evolve
6. Run your tool whenever you need changes

**Time investment**: Hours to write, ongoing maintenance burden

### The New Way: Use Agents Directly
1. Identify a repetitive task
2. Tell an AI agent: "Add this key to all three keyboards"
3. Agent understands the context, makes the changes
4. Review and merge

**Time investment**: Minutes per change, no maintenance

### When Agents Are Better Than Automation

The KLCM project reveals a crucial insight: **For many tasks, having an AI agent make direct changes is simpler than writing code to automate those changes**.

This is especially true when:
- Changes are needed infrequently (monthly keyboard layout tweaks, not hourly deployments)
- The task requires contextual understanding (keyboard layouts have ergonomic considerations)
- Formats evolve over time (firmware updates change config syntax)
- The automation infrastructure would need maintenance

It's not that the initial Go implementation was wrong—it was a necessary exploration of the problem space. But it taught an important lesson: **the best automation is sometimes no automation at all, just better tools for making changes**.

## The Modern KLCM Workflow

Today, KLCM has found its optimal form:

1. **CLI tools** for pulling configs, validation, and PR creation
2. **Git-based workflow** for version control and change tracking
3. **AI agents** for making actual configuration changes
4. **Human review** before merging changes

The Go code that remains is focused on:
- Downloading configs from multiple repositories
- Validating syntax before committing
- Creating PRs with proper branching
- Comparing local vs. remote versions

These are the coordination tasks that genuinely benefit from automation—the scaffolding around the changes, not the changes themselves.

## Lessons for Software Development

### 1. Question Your Automation Assumptions

Just because something *can* be automated doesn't mean it *should* be automated with custom code. Sometimes the better solution is:
- Better tools for manual work
- AI assistance for contextual changes
- Automation only for scaffolding and coordination

### 2. Maintenance Burden Is Real

That sophisticated parser you built? It's now technical debt. Every line of code is a liability that needs maintenance. AI agents don't accumulate technical debt—they work with whatever the current state is.

### 3. Context Matters More Than Consistency

Traditional automation excels at consistency but struggles with context. AI agents are the opposite—they excel at understanding context and can handle inconsistency gracefully.

### 4. The Future Is Hybrid

The best solution isn't "no automation" or "full automation"—it's **strategic automation**:
- Automate the workflow (git operations, PR creation, validation)
- Use AI for the transformations (actual config changes)
- Keep humans in the loop for review and decisions

## A New Development Paradigm

The KLCM project's evolution mirrors a broader shift in software development:

**Traditional**: Write code that generates code  
**Modern**: Ask AI to write code directly

**Traditional**: Build tools to automate repetitive tasks  
**Modern**: Use AI assistants that understand intent

**Traditional**: Maintain complex infrastructure for rare operations  
**Modern**: Describe what you want when you need it

This doesn't make traditional programming obsolete—the KLCM CLI tools are still valuable Go code. But it changes what we choose to automate and how we approach repetitive tasks.

## The Irony of Software Automation

There's a delicious irony here: a project designed to automate keyboard configuration management taught us that sometimes **the best automation is helping a human work better**, not replacing their work entirely.

The failed promise of automation has always been: "Write this code once, save time forever."

The real promise of AI assistance is: "Describe what you want, and it happens, with context understood and edge cases handled."

## Practical Applications

This pattern applies beyond keyboard configurations:

- **Infrastructure as Code**: Instead of writing Terraform modules for every variation, describe your infrastructure needs to an AI agent
- **Configuration Management**: Rather than maintaining Ansible playbooks, ask agents to make specific changes across services
- **Documentation**: Don't build doc generators—have agents update docs when code changes
- **Testing**: Supplement test frameworks with agents that understand what should be tested

The key question isn't "Can I automate this?" but "What's the lightest-weight way to handle this task reliably?"

## Conclusion: Embracing the Agent-Assisted Future

The Keyboard Layout Config Mapper started as an ambitious automation project and evolved into something more interesting: **a case study in knowing when NOT to automate**.

The remaining Go code serves a clear purpose: coordination, validation, and workflow management. The actual configuration changes? Those are better handled by AI agents that understand context, can read documentation, and don't need maintenance.

This is the future of development: not replacing programmers with AI, but **replacing unnecessary automation infrastructure with AI-assisted direct work**.

The code you don't write is the code you don't have to maintain. And sometimes, the best code is a well-crafted prompt to an AI agent that already understands the problem domain.

---

*This post is itself a meta-artifact of this paradigm: rather than building a tool to generate blog posts about project histories, I simply asked an AI agent to research the repository and write this analysis. The agent read commit messages, analyzed the evolution, and synthesized insights—exactly the kind of contextual work that traditional automation struggles with.*

## Appendix: Timeline

**March 2022**: Initial commit  
**April 2022**: PR #1 - Massive Go implementation with parsers, tests, and automation  
**2023**: Minimal activity, mostly config tweaks  
**August 2025**: PR #12 - V5 target with streamlined CLI, 2000+ lines of old code removed  
**September 2025**: PR #13-15 - Agent-assisted integration of new keyboards  
**November 2025**: PR #20-28 - Direct configuration changes across keyboards  
**December 2025**: This reflection on the evolution  

The pattern is clear: from ambitious automation to pragmatic agent assistance.
