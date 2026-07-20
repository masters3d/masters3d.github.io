+++
title = "Why I Switched to Worklogs (and You Should Too)"
date = "2026-03-28"
description = "How worklogs transformed my workflow with AI coding agents (capturing context across sessions, using GitHub Issues as a backend, and turning structured logs into an agentic work queue)."
template = "blog-post.html"
categories = ["ai", "development", "productivity"]
tags = ["worklogs", "agents", "copilot", "github", "workflow", "ai-development"]
+++

I wanted to share something that's been a game-changer for how I organize my
work with AI coding agents: **worklogs**.

## What worklogs are (and what they're not)

At its core, a worklog is about **capturing context so it doesn't vanish when
your session ends**.

Think of it like a **scientist's lab notebook** 📓. You're running experiments,
writing down your thoughts, documenting failures, documenting things that
worked. Back in the day you would have used a Notepad file, or a Word doc, or
maybe sticky notes. Now you have a super lightweight way to let an agentic loop
hold this context for you, so you can reference it and search it easily, without
it disappearing.

A worklog captures: what you're working on, the status, blockers, notes, links
to PRs, and outcomes. It's a living log that both you and your AI agent can read
and update.

To be clear: worklogs are not **agent plans** (the `plan.md` files that AI
coding agents create at the start of a task). Some people check these into their
repo, others don't. Either way, they're ephemeral: they help the agent think
through a problem within a single session.

**This is NOT about design documents or vision documents.** Those still exist
and are still important. Worklogs don't replace them. In fact, you can use a
worklog to *track the creation* of a design doc as a deliverable.

The distinction is simple:

- **Agent plans** = how the agent will execute a task right now (ephemeral,
  session-scoped)
- **Worklogs** = a log of work in flight (persistent, cross-session)
- **Design docs / vision docs** = formal artifacts that describe what and why
  (durable, reviewed)

Agent plans are great for the session they live in. But when you close the
session and come back tomorrow, you need something that remembers where you left
off, what you tried, and what's next. That's the worklog.

|                | Agent Plans        | Worklogs              | Design Docs        |
|----------------|--------------------|-----------------------|--------------------|
| **Scope**      | Single session     | Cross-session         | Cross-project      |
| **Purpose**    | Execute a task     | Track work over time  | Define what and why|
| **Lifetime**   | Session ends       | Until work completes  | Permanent record   |
| **Analogy**    | Whiteboard sketch  | Lab notebook          | Published paper    |

Right now I have **seven sessions running in parallel**, each working on a
different area. Each session has its own worklog. These worklogs give me clarity
on:

- What am I working on across all sessions?
- What's the status of each piece of work?
- Which PRs are open, which are blocked, which are done?
- What did I try that didn't work? What decisions did I make and why?

Without worklogs, that context lives in scattered session histories. With
worklogs, it's all in one place, searchable, and any new session can pick up
right where I left off.

## How we built it

**GitHub Issues is just the backend we chose.** You don't have to implement it
this way. You could use Azure DevOps work items, a storage account, or roll out
your own endpoint and API. The concept is what matters.

A worklog backend needs to be:

- **Easy for agents to push context to** (create, update, close via CLI)
- **Easy for agents to pull context from** (read, search, filter)
- **Easy for humans to review** (readable UI, no special tooling)
- **Easy to categorize and search** (labels, filters, full-text search)

We went with GitHub because the API is incredibly simple. Authentication is
straightforward, the `gh` CLI just works, and saving context requires zero
ceremony. You could build this on Azure DevOps too, but we found the GitHub API
to be so effortless that it just removes all friction. If something better comes
along, we swap the backend and the workflow stays the same.

The whole thing is powered by a **skill file** (just a markdown file). That's
it. A skill file is a set of instructions that teaches the AI agent a workflow.
It defines conventions (how to name things, what labels to use, what template to
follow), the CLI commands to run (`gh issue create`, `gh issue edit`, etc.), and
the decision logic (check for duplicates before creating, ask for a size
estimate, link related items).

When you say *"open a worklog"*, the agent loads this skill file and follows the
instructions. It knows:

- **The template**: every worklog has four sections (Context, What to Build,
  Dependencies, Notes)
- **The conventions**: title format, label taxonomy, t-shirt sizing (XS through
  XL)
- **The lifecycle**: not-started → in-progress → pr-open → closed
- **The guardrails**: check for duplicates, confirm before creating, never
  overwrite existing content

Because it's just a markdown file, **anyone can write one**. You don't need a
framework, a plugin system, or a deployment pipeline. You write the
instructions, drop the file in your repo, and the agent picks it up. Want to
change the template? Edit the markdown. Want to add a new workflow (like syncing
from Azure DevOps)? Add a new section to the file.

```
# Example: the entire skill is structured like this
.claude/skills/worklog/SKILL.md
├── Conventions (title format, labels, sizing)
├── Issue body template (Context, What to Build, ...)
├── Workflow: Add a work item
├── Workflow: Update an existing item
├── Workflow: Review backlog
└── Workflow: Sync from Azure DevOps
```

The skill is the **recipe**. GitHub Issues is the **storage**. The `gh` CLI is
the **interface**. And the AI agent is the one following the recipe. You just
talk to it in plain English.

```
YOU                 COPILOT CLI           YOU CODE             DONE
"open a worklog  →  creates issue,     →  do your work,    →  "mark worklog
 for this task"     adds labels + size     update as you go     as done"
```

All from your terminal. The agent handles GitHub issue creation, sizing, labels,
and status updates. 🚀

**The key insight:** If you're already using Copilot CLI, worklogs add *zero*
extra work. You just tell the agent:

```
> "open a worklog for this task"
> "update my worklog, just finished the database migration"
> "mark this worklog as done"
```

You stay focused on your actual work. The agent does the rest.

**What I love about it:**

- **No context switching**: you create and update worklogs in the same terminal
  where you're coding
- **Automatic tracking**: sized, labeled, and assigned without you touching
  GitHub
- **Team visibility**: everyone can see what's in flight on the worklog board
- **Built-in history**: when you close a worklog, the agent links the PR and
  summarizes what was done
- **No merge friction**: it's just GitHub Issues, no PRs or file conflicts

We still use Azure DevOps to track effort. That hasn't changed. The distinction
is what makes this work:

|                    | Azure DevOps                          | Worklogs                                |
|--------------------|---------------------------------------|-----------------------------------------|
| **Purpose**        | Effort tracking (where is the time going?) | Work documentation (what am I doing right now?) |
| **Granularity**    | One block of effort (may cover multiple tasks) | Individual task (notes, context, outcomes) |
| **Updated by**     | You (manually)                        | You + your AI agent                     |
| **Analogy**        | Timesheet                             | Lab notebook                            |
| **AI-native**      | Not yet                               | Built for it                            |

This **separation of concerns** is what makes it powerful. A single Azure DevOps
work item might have multiple worklogs under it, each capturing a different
piece of the work. You can link them: the agent tags worklogs with the work item
ID and you can tell it *"sync worklogs from Azure DevOps"* to import items. But
the worklog is yours: your notes, your pace, your documentation of what actually
happened.

The architecture boils down to three layers:

1. **You in Terminal** (*"open a worklog for auth refactor"* | *"update worklog,
   found the root cause"* | *"close it, PR merged"*)
2. **Copilot CLI + Worklog Skill** (the agent understands your intent and
   invokes the skill, which contains templates, labels, sizing, dedup, and sync
   logic)
3. **GitHub Issues (storage)** (worklogs, notes, context, outcomes; labels for
   status, size, category; searchable, persistent, no merge friction; optionally
   linked to **Azure DevOps** for effort/sprint tracking)

## Worklogs as an agentic work queue

Here's where it gets really interesting 🔄. Because worklogs are structured
(title, context, deliverables, dependencies, size), they become a **queue of
work that an agent can pick up and execute**.

The flow looks like this:

1. **Enqueue**: Create worklogs throughout the day as ideas come up,
   investigations reveal new tasks, or work items land. Takes seconds.
2. **Prioritize**: Ask the agent "what should I focus on next?" It reads your
   backlog, checks dependencies and sizes, and recommends.
3. **Execute**: Pick a worklog and start working. The agent already has all the
   context (what to build, dependencies, notes). No ramp-up time.
4. **Document**: As you work, the agent updates the worklog with progress,
   blockers, and outcomes. Your future self (or teammate) can read exactly what
   happened.
5. **Close**: Done? The agent closes the worklog, links the PR, and your backlog
   shrinks. On to the next one.

The speed gain is in the **enqueue step**. Capturing work traditionally means
stopping, switching to a browser, filling out forms. With worklogs, you say one
sentence mid-conversation and it's tracked. That low friction means you actually
capture *everything*, not just the big items you remember to log later.

My recommendation: **start using worklogs as you go**. Don't batch them up or
plan a big migration. Just next time you start a task, tell the agent to open a
worklog. Update it when you hit a milestone. Close it when you're done. That's
it.

## Where this is heading

All of this is in flux. I'm aware of sprints. I'm aware of Agile. I'm aware of
all the different methodologies for organizing work. Worklogs are not trying to
replace any of that.

The main difference is that a worklog is **personal**. Think of a scientist's
notebook 🧪: you keep your notes in there, you document every experiment, what
you tried, what the results were. And then you file it away in a shared space so
others can go look at your notes if they need to understand an experiment, or
how a result came about. That's exactly what this is.

It brings **rigor to the engineering process**. It moves us closer to how
scientific discovery and progress actually work: you hypothesize, you
experiment, you document, you share. When a teammate sees a PR and wants to
understand how it came about, they can go look at the worklog and find the full
story. But it's not a status report for management. It's not a sprint board.
It's a **lab notebook for software engineering**.

And here's the beautiful thing: **it's not process**. You're not manually
filling out forms or updating tickets. Your agent is doing it. The rigor comes
for free because the agent is already in the loop, already has the context, and
captures everything as a natural byproduct of the work itself. You get the
discipline of documentation without the overhead of documentation.

I also don't think worklogs are their final state. This is an evolution. (I
traced how I got here, [from sort-of-daily Markdown files in 2017 to monthly
Word docs to today's agent-maintained logs](/blog/nine-years-of-copious-notes/),
in a separate post.) We're in the early days of figuring out how to work with AI
agents, and I think we're going to discover that we need **more agent-native
ways of working**. The old tools were designed for humans coordinating with
other humans. The new tools need to account for humans coordinating with agents,
and agents coordinating with each other.

Worklogs are one step in that direction. They give agents a place to read
context, write progress, and pick up where they left off. But I expect new
patterns will emerge as the tooling matures. Better ways to interface with
agents. Better ways to hand off work between sessions. Better ways to let agents
propose, prioritize, and execute autonomously.

These are the kinds of new ways of thinking that will start to surface as we
build more tools around agentic workflows. Worklogs are where we are today.
Tomorrow will look different, and that's the point.
