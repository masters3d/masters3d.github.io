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

My journey with AI coding tools has been transformative, particularly since the release of Claude Opus 4.5 on November 24, 2025. This post reflects on how AI tooling has evolved and what that means for language choices in CLI development, using my experience with Rust and scripting languages as a case study.

## My Journey with GitHub Copilot CLI

The vast majority of my development work has been through GitHub Copilot CLI, and the experience has been nothing short of eye-opening. I've been using it consistently since Sonnet 4.5 came out around September 2025, and it's been a gradual evolution in how I approach coding.

## The Game Changer: Claude Opus 4.5

Claude Opus 4.5, released on November 24, 2025, was an absolute game-changer. This wasn't just another incremental update (it represented a fundamental leap in capability that transformed how I approach coding).

Before Opus 4.5, getting value from agents required significantly more steering. The harness you used had to do more of the heavy lifting, which could be annoying if you were working with a less sophisticated setup. With Opus 4.5, the amount of steering needed dropped dramatically. When I do need to steer now, it's typically because there are multiple valid approaches and I need to apply personal preferences or taste that are difficult to codify.

The model brought significant improvements in coding, agentic systems, and overall accuracy. Tasks that would have required multiple iterations became reliable one-shot completions.

## A Shift in What's Possible: From Shell Scripts to Rust

Here's where things get interesting. Before Opus 4.5, I only wrote shell scripts for my CLI tooling. Rust seemed too complex, too error-prone to attempt with AI assistance. But when Opus 4.5 came out, writing Rust became doable. The vast majority of my Rust journey has been since Opus 4.5, and it's been a revelation (especially within the Rust ecosystem where the model excels).

This shift from scripting languages to compiled languages like Rust showcases the progression in AI tooling capability. It's not just about the language choice, it's about what becomes feasible when the AI assistance reaches a certain threshold of reliability.

## Why This Matters: Rust vs Scripting Languages for CLI Tools

The choice between Rust and scripting languages for CLI tooling isn't just about language preference. It's about understanding how AI agents interact with different validation paradigms, and what that means for investing in long-term tooling solutions.

Rust development with AI agents has been surprisingly smooth. In Rust, tests live right alongside the code in the same file. This means when an agent is writing or modifying Rust code, it has immediate context about how the code should behave. This contextual awareness leads to significantly better one-shot solutions.

My Rust projects have comprehensive CI steps that check code coverage, linting, compilation errors, and integration with tools like `cargo`. But here's where the real magic happens with compiled languages: The agent can write code, run the compiler, and get immediate feedback without executing anything. The compiler acts as a validation step that guides the agent to make fixes and edits on its own. In scripting languages, the only way to validate is to actually run the code, but with compiled languages like Rust, the agent can validate by compiling. This creates a tight feedback loop where the agent iterates and fixes issues independently, without requiring me to run the code myself. I prefer to validate the final result myself, but the compilation step means the agent can get much further on its own.

Rust's strict type system acts as inline documentation. The compiler catches a vast majority of issues, which means the agent's code is validated thoroughly before it ever runs. Even CLI tools and TUIs (Terminal User Interfaces) benefit from this. I've been using Ratatui (a Rust TUI library), and it's been fantastic. Creating a nice command-line interface in Rust with Ratatui is actually easier than doing the same in scripting languages like PowerShell or Bash. The type safety and library ecosystem make complex UIs surprisingly manageable.

For Rust, I find that prompts typically result in working code on the first try. The combination of strong types, inline tests, and excellent tooling means less back-and-forth.

Scripting languages like PowerShell or Bash present different challenges with AI agents. With scripting languages, you often don't know if something will work until you actually run it. Linters exist, but they're nowhere near as powerful as a compiler. Testing frameworks exist (like Pester for PowerShell), but the testing infrastructure is not as seamlessly integrated as in Rust. Tests are typically in separate files, and the overall testing culture isn't as ingrained.

The major upside? Distribution is incredibly easy. Scripts just run on most systems. No compilation, no binary signing (in most cases), no cross-platform build matrices. For internal tools, this low barrier to entry is invaluable. Scripting languages excel at quick automation tasks, but they can become unwieldy when they grow to thousands of lines.

The progression I experienced (shell scripts before Opus 4.5, Rust after) highlights important considerations for investing in CLI tooling. Choose Rust for CLI tools when the project will grow beyond a few hundred lines, you need strong reliability guarantees, performance matters, you're building CLIs or TUIs that need to feel polished, you want comprehensive compile-time checking, and AI agents are capable enough to make it feasible (post-Opus 4.5). Choose scripting languages when you need quick automation, distribution ease is paramount, the script will stay relatively small, setup burden needs to be minimal, or you're working with less capable AI models.

With capable AI models like Opus 4.5, Rust becomes viable even for smaller CLI tools where you might have previously defaulted to scripts. Once a script reaches thousands of lines, the case for Rust becomes even stronger.

## Calling External Tools from Rust

One surprising discovery: calling external CLIs from Rust is extremely smooth. There are excellent crate packages that let you call tools like the GitHub CLI (`gh`) from Rust almost as if you were writing a shell script. This bridges the gap between "I need the robustness of a compiled language" and "I need to integrate with existing command-line tools."

## Multi-Agent Workflows

One trick I've picked up is spinning up multiple agents to work on different parts of the codebase in parallel. Instead of having one agent refactor an entire large codebase, I'll have a "fleet" of agents each handle individual files. This approach has been much more effective overall, especially when working with the larger codebases that Rust projects tend to become.

This feature became available in GitHub Copilot as of January 2026, though it's not particularly visually obvious. You can explicitly tell the agent to spin up sub-agents and even specify which model each agent should use (Opus, GPT, Gemini, etc.). This is incredibly helpful for tasks like inline code reviews where you can have different models review your code to get different perspectives.

For example, you can use a prompt like: "Increase the unit test coverage percentage to 80. Spin up a fleet of parallel Opus sub-agents." The agent will then coordinate multiple parallel agents, each working on different parts of the codebase to achieve the goal.

## Continuing Evolution: Opus 4.6 and 4.6 Fast

I've been using Opus 4.6 since its release a couple of days ago. While the jump from 4.5 to 4.6 isn't as dramatic as the leap to 4.5 itself, there's a noticeable improvement in correctness. The model seems to make fewer subtle errors, and responses feel more thought-through.

More recently, the 4.6 Fast model has tightened up the feedback loop even further, providing another boost in productivity. The faster response times mean I can iterate more quickly, which is particularly valuable when working through multiple small refinements.

## The Human Element Remains Critical

Despite all these advances, the fundamentals haven't changed:

- **What to build** is still the hardest decision
- **What NOT to build** might be even more important
- **Taste** and product sense can't be delegated
- **Judgment** about trade-offs remains deeply human

Agents are incredible tools for implementation, but the human aspects (vision, taste, prioritization) are more critical than ever. When I need to steer agents now, it's less about correcting errors and more about expressing preferences and taste that are inherently subjective.

## The Industry Is Changing

I believe we're in the middle of a fundamental shift in how software gets written. More and more coding will happen through agents. But this doesn't mean coding is "solved" (it means the problems we focus on are shifting from implementation details to architectural decisions, product vision, and user experience).

## Looking Forward

The timeline has been remarkably tight (all of this transformation has happened in just about three months since Opus 4.5's release in late November 2025). The improvement is more subtle than it might appear: while there was extensive steering to get to the first version before, now we typically get one-shot results. The total steering effort hasn't necessarily decreased, but it's shifted to things that matter like taste and preferences rather than getting basic functionality working.

I'm having a lot of fun exploring this new landscape. The combination of powerful AI tools and languages with strong ecosystems (like Rust) creates a development experience that would have seemed like science fiction just a few years ago.

Here's to figuring out how to keep these agents on track and using them to build things that actually matter. 🚀

---

*This post is a draft reflection on my ongoing journey with AI coding tools. As the technology continues to evolve, I expect my perspectives will evolve with it.*
