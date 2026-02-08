+++
title = "My AI Tools Journey Since Claude Opus 4.5: Rust, Scripting Languages, and the Evolution of Agent-Driven Development"
date = 2026-02-07
description = "Reflecting on my experience using AI coding tools since Claude Opus 4.5, contrasting Rust and scripting language development, and insights on multi-agent workflows."
template = "blog-post.html"
categories = ["ai", "development", "rust", "scripting"]
tags = ["claude", "copilot", "agents", "rust", "powershell", "bash", "ai-development"]
draft = true
+++

## Introduction

My journey with AI coding tools has been transformative, particularly since the release of Claude Opus 4.5 on November 24, 2025. The vast majority of my development work has been through GitHub Copilot CLI, and the experience has been nothing short of eye-opening. This post reflects on my experience contrasting two very different paradigms—Rust and scripting languages like PowerShell or Bash—and how AI agents handle each.

## The Game Changer: Claude Opus 4.5

Claude Opus 4.5, released on November 24, 2025, was an absolute game-changer for AI-assisted development. This wasn't just another incremental update—it represented a fundamental leap in capability that transformed how I approach coding.

Before Opus 4.5, getting value from agents required significantly more steering. The harness you used had to do more of the heavy lifting, which could be annoying if you were working with a less sophisticated setup. With Opus 4.5, the amount of steering needed dropped dramatically. When I do need to steer now, it's typically because there are multiple valid approaches and I need to apply personal preferences or taste that are difficult to codify.

The model brought significant improvements in coding, agentic systems, and overall accuracy. Tasks that would have required multiple iterations became reliable one-shot completions. The vast majority of my Rust journey has been since Opus 4.5, and it's been a revelation—especially within the Rust ecosystem where the model excels.

## The Tale of Two Paradigms: Rust vs Scripting Languages

My recent development has been split between two completely opposite ends of the language spectrum: Rust (a compiled, notoriously hard-to-learn systems language) and scripting languages like PowerShell or Bash (interpreted, dynamic languages). The contrast has been illuminating.

### Rust: The Compiled Advantage

Rust development with AI agents has been surprisingly smooth. Here's why:

**Testing in Context**: In Rust, tests live right alongside the code in the same file. This means when an agent is writing or modifying Rust code, it has immediate context about how the code should behave. This contextual awareness leads to significantly better one-shot solutions.

**Strong CI/CD Integration**: My Rust projects have comprehensive CI steps that check:
- Code coverage
- Linting
- Compilation errors
- Integration with tools like `cargo`

These guardrails catch issues immediately. The agent can write code, I can run `cargo test`, and I'll know right away if something's wrong—before runtime.

**Type System as Documentation**: Rust's strict type system acts as inline documentation. The compiler catches a vast majority of issues, which means the agent's code is validated thoroughly before it ever runs. Even CLI tools and TUIs (Terminal User Interfaces) benefit from this.

**TUI Development**: I've been using Ratatui (a Rust TUI library), and it's been fantastic. Creating a nice command-line interface in Rust with Ratatui is actually easier than doing the same in scripting languages like PowerShell or Bash. The type safety and library ecosystem make complex UIs surprisingly manageable.

**One-Shot Success Rate**: For Rust, I find that prompts typically result in working code on the first try. The combination of strong types, inline tests, and excellent tooling means less back-and-forth.

### Scripting Languages: The Trade-Off

Scripting languages like PowerShell or Bash present different challenges with AI agents:

**Delayed Validation**: With scripting languages, you often don't know if something will work until you actually run it. Linters exist, but they're nowhere near as powerful as a compiler.

**Testing Infrastructure**: Testing frameworks exist (like Pester for PowerShell), but the testing infrastructure is not as seamlessly integrated as in Rust. Tests are typically in separate files, and the overall testing culture isn't as ingrained.

**Distribution Advantage**: The major upside? Distribution is incredibly easy. Scripts just run on most systems. No compilation, no binary signing (in most cases), no cross-platform build matrices. For internal tools, this low barrier to entry is invaluable.

**Quick Automation**: Scripting languages excel at quick automation tasks, but they can become unwieldy when they grow to thousands of lines.

### When Does Each Language Make Sense?

**Choose Rust when**:
- The project will grow beyond a few hundred lines
- You need strong reliability guarantees
- Performance matters
- You're building CLIs or TUIs that need to feel polished
- You want comprehensive compile-time checking

**Choose scripting languages when**:
- You need quick automation
- Distribution ease is paramount
- The script will stay relatively small
- Setup/installation burden needs to be minimal

**The crossover point**: Once a script reaches thousands of lines, it might be time to consider porting to a compiled language that offers better long-term maintainability.

## Calling External Tools from Rust

One surprising discovery: calling external CLIs from Rust is extremely smooth. There are excellent crate packages that let you call tools like the GitHub CLI (`gh`) from Rust almost as if you were writing a shell script. This bridges the gap between "I need the robustness of a compiled language" and "I need to integrate with existing command-line tools."

## The Bigger Context Window

One of the most significant improvements with the Claude 4.x series is the larger context window. When working on large codebases, even the new Rust projects I've written, having more context available makes a huge difference.

**Multi-Agent Workflows**: One trick I've picked up is spinning up multiple agents to work on different parts of the codebase in parallel. Instead of having one agent refactor an entire large codebase, I'll have a "fleet" of agents each handle individual files. This approach has been much more effective overall.

## Continuing Evolution: Opus 4.6 and 4.6 Fast

I've been using Opus 4.6 since its release a couple of days ago. While the jump from 4.5 to 4.6 isn't as dramatic as the leap to 4.5 itself, there's a noticeable improvement in correctness. The model seems to make fewer subtle errors, and responses feel more thought-through.

More recently, the 4.6 Fast model has tightened up the feedback loop even further, providing another boost in productivity. The faster response times mean I can iterate more quickly, which is particularly valuable when working through multiple small refinements.

## The Human Element Remains Critical

Despite all these advances, the fundamentals haven't changed:

- **What to build** is still the hardest decision
- **What NOT to build** might be even more important
- **Taste** and product sense can't be delegated
- **Judgment** about trade-offs remains deeply human

Agents are incredible tools for implementation, but the human aspects—vision, taste, prioritization—are more critical than ever. When I need to steer agents now, it's less about correcting errors and more about expressing preferences and taste that are inherently subjective.

## The Industry Is Changing

I believe we're in the middle of a fundamental shift in how software gets written. More and more coding will happen through agents. But this doesn't mean coding is "solved"—it means the problems we focus on are shifting from implementation details to architectural decisions, product vision, and user experience.

## Looking Forward

The timeline has been remarkably tight—all of this transformation has happened in just about three months since Opus 4.5's release in late November 2025. The rapid pace of improvement is striking: we've gone from needing extensive steering to mostly hands-off development, with the harness doing less work and the models doing more.

I'm having a lot of fun exploring this new landscape. The combination of powerful AI tools and languages with strong ecosystems (like Rust) creates a development experience that would have seemed like science fiction just a few years ago.

Here's to figuring out how to keep these agents on track and using them to build things that actually matter. 🚀

---

*This post is a draft reflection on my ongoing journey with AI coding tools. As the technology continues to evolve, I expect my perspectives will evolve with it.*
