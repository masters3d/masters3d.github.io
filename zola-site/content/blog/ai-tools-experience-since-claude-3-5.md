+++
title = "My AI Tools Journey Since Claude 3.5: Rust, PowerShell, and the Evolution of Agent-Driven Development"
date = 2026-02-07
description = "Reflecting on my experience using AI coding tools since Claude 3.5, contrasting Rust and PowerShell development, and insights on multi-agent workflows."
template = "blog-post.html"
categories = ["ai", "development", "rust", "powershell"]
tags = ["claude", "copilot", "agents", "rust", "powershell", "ai-development"]
draft = true
+++

## Introduction

My journey with AI coding tools has been transformative, particularly since the release of Claude 3.5 Sonnet. The vast majority of my development work has been through GitHub Copilot CLI, and the experience has been nothing short of eye-opening. This post reflects on my experience contrasting two very different languages—Rust and PowerShell—and how AI agents handle each.

## The Claude Timeline: A Rapid Evolution

The pace of AI model releases has been remarkable. Here's the timeline that has shaped my development experience:

- **Claude 3 Family (Opus, Sonnet, Haiku)**: March 2024 - The flagship Opus model set new benchmarks
- **Claude 3.5 Sonnet**: June 20, 2024 - A game-changer that actually outperformed the previous flagship Opus
- **Claude 4.x series**: 2025-2026 - Including the recent Opus 4.6 release in February 2026

The jump from pre-3.5 models to Claude 3.5 Sonnet was particularly significant. Tasks that would have challenged earlier models became one-shot completions. The recent Opus 4.6 brings an even bigger context window and what I've noticed is a subtle but important improvement in correctness across various tasks.

## The Tale of Two Languages: Rust vs PowerShell

My recent development has been split between two completely opposite ends of the language spectrum: Rust (a compiled, notoriously hard-to-learn systems language) and PowerShell (an interpreted scripting language). The contrast has been illuminating.

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

**TUI Development**: I've been using Ratatui (a Rust TUI library), and it's been fantastic. Creating a nice command-line interface in Rust with Ratatui is actually easier than doing the same in PowerShell or even Bash. The type safety and library ecosystem make complex UIs surprisingly manageable.

**One-Shot Success Rate**: For Rust, I find that prompts typically result in working code on the first try. The combination of strong types, inline tests, and excellent tooling means less back-and-forth.

### PowerShell: The Scripting Trade-Off

PowerShell development with AI agents presents different challenges:

**Delayed Validation**: With scripting languages, you often don't know if something will work until you actually run it. Linters exist, but they're nowhere near as powerful as a compiler.

**Testing Infrastructure**: While PowerShell has testing frameworks like Pester, the testing infrastructure is not as seamlessly integrated as in Rust. Tests are typically in separate files, and the overall testing culture isn't as ingrained.

**Distribution Advantage**: The major upside? Distribution is incredibly easy. PowerShell scripts just run on most systems (unless you need PowerShell 7+). No compilation, no binary signing (in most cases), no cross-platform build matrices. For internal tools, this low barrier to entry is invaluable.

**Similarity to Bash**: The experience is very similar to writing Bash scripts on Linux. Both are great for quick automation, but both can become unwieldy when they grow to thousands of lines.

### When Does Each Language Make Sense?

**Choose Rust when**:
- The project will grow beyond a few hundred lines
- You need strong reliability guarantees
- Performance matters
- You're building CLIs or TUIs that need to feel polished
- You want comprehensive compile-time checking

**Choose PowerShell/scripting when**:
- You need quick automation
- Distribution ease is paramount
- The script will stay relatively small
- You're working in Windows-heavy environments
- Setup/installation burden needs to be minimal

**The crossover point**: Once a PowerShell or Bash script reaches thousands of lines, it might be time to consider porting to a compiled language that offers better long-term maintainability.

## Calling External Tools from Rust

One surprising discovery: calling external CLIs from Rust is extremely smooth. There are excellent crate packages that let you call tools like the GitHub CLI (`gh`) from Rust almost as if you were writing a shell script. This bridges the gap between "I need the robustness of a compiled language" and "I need to integrate with existing command-line tools."

## The Bigger Context Window: A Game Changer

One of the most significant improvements with Opus 4.6 is the larger context window. When working on large codebases, even the new Rust projects I've written, having more context available makes a huge difference.

**Multi-Agent Workflows**: One trick I've picked up is spinning up multiple agents to work on different parts of the codebase in parallel. Instead of having one agent refactor an entire large codebase, I'll have a "fleet" of agents each handle individual files. This approach has been much more effective overall.

## Opus 3.5 vs 4.6: Subtle But Important Improvements

I've been using Opus 4.6 for a couple of days now. While I'm not seeing night-and-day differences from 3.5 Sonnet, there's a noticeable improvement in correctness. The model seems to make fewer subtle errors, and responses feel more thought-through. It's the kind of improvement you might not notice in a single interaction but becomes clear over the course of a day's work.

## The Human Element Remains Critical

Despite all these advances, the fundamentals haven't changed:

- **What to build** is still the hardest decision
- **What NOT to build** might be even more important
- **Taste** and product sense can't be delegated
- **Judgment** about trade-offs remains deeply human

Agents are incredible tools for implementation, but the human aspects—vision, taste, prioritization—are more critical than ever.

## The Industry Is Changing

I believe we're in the middle of a fundamental shift in how software gets written. More and more coding will happen through agents. But this doesn't mean coding is "solved"—it means the problems we focus on are shifting from implementation details to architectural decisions, product vision, and user experience.

## Looking Forward

The pace of change is dizzying. New models are released every few months, each bringing incremental but meaningful improvements. The challenge isn't just keeping up with the technology—it's figuring out how to use it effectively while keeping our projects on the rails.

I'm having a lot of fun exploring this new landscape. The combination of powerful AI tools and languages with strong ecosystems (like Rust) creates a development experience that would have seemed like science fiction just a few years ago.

Here's to figuring out how to keep these agents on track and using them to build things that actually matter. 🚀

---

*This post is a draft reflection on my ongoing journey with AI coding tools. As the technology continues to evolve, I expect my perspectives will evolve with it.*
