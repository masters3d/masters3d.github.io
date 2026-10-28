+++
title = "Reporting Features Without a PM"
date = "2029-12-31"
draft = true
description = "Worklogs and product backlog items cover the next few days well. Feature and epic status used to be a product manager's or Scrum Master's job. A survey of how other teams report on features, and a low-maintenance roll-up to try on a team that has neither role."
template = "blog-post.html"
[taxonomies]
categories = ["Engineering Systems"]
tags = ["planning", "worklogs", "agile", "flow-metrics", "roadmaps", "reporting"]
[extra]
editorial_track = "engineering-systems"
related = ["a-year-of-worklogs", "why-i-love-worklogs", "effort-tracking-vs-task-tracking", "feature-cradle-to-grave"]
+++

> **Draft (idea only, unscheduled).** This is a survey and a proposal, not a
> report. It becomes publishable once the team has run some version of the
> roll-up below for a few weeks and the post can say what happened. The date is
> a placeholder that keeps the draft gate quiet.
>
> **Sources to verify and link before publishing** (the sandbox that wrote this
> draft could not reach them): the Azure DevOps Scrum process docs (Epic,
> Feature, Product Backlog Item, Task), Azure Boards Delivery Plans and
> dependency tracking, Azure DevOps cycle time and lead time widgets; Daniel
> Vacanti, _Actionable Agile Metrics for Predictability_ (WIP, cycle time,
> throughput, work item age); Monte Carlo forecasting from throughput; Ryan
> Singer, _Shape Up_ (appetite, six-week cycles, hill charts); Janna Bastow and
> ProdPad on Now/Next/Later roadmaps; Linear project updates; Amazon's Working
> Backwards PR/FAQ; OKRs; SAFe PI Planning and the program board; Conventional
> Commits. Each one needs a primary link on the claim itself, or the claim gets
> softened. The GitHub links in the body are already checked.

In [A Year of Worklogs](/blog/a-year-of-worklogs/) I described where worklogs
stop working: above the product backlog item (PBI). Daily work is covered. The
feature and epic level, where you see what is slow, what depends on what, and
what shipped this quarter, used to be kept up by a product manager or a Scrum
Master. My team has neither, so before trying to fix it I looked at how other
teams and tools approach the problem.

## What other teams do

**The work item hierarchy itself.** The Azure DevOps Scrum process defines four
levels: Epic, Feature, Product Backlog Item, and Task. Backlogs can show rollup
progress from children, and Delivery Plans lay features from several teams on a
timeline with dependency lines between them. GitHub has the same shape with
[sub-issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/adding-sub-issues),
which allow up to 100 children per issue and up to eight levels of nesting, and
a
[roadmap layout](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/customizing-the-roadmap-layout)
for projects. The structure is there in both tools. The weak point is upkeep:
the roll-up is only as good as the parent links, and someone has to keep every
PBI attached to the right feature.

**Flow metrics.** Kanban practice, as Daniel Vacanti lays it out, tracks four
numbers: work in progress, cycle time, throughput, and work item age. Work item
age answers "what is going slowly" without any estimates. An item that has been
open much longer than the team's usual cycle time gets flagged on its own.
Throughput history also feeds Monte Carlo forecasts, which answer "when will
this feature be done" as a date with a confidence level instead of a single
promise.

**Shape Up.** Basecamp's method replaces estimates with an appetite (how much
time the work is worth), works in fixed cycles, and reports progress on hill
charts. The uphill half means the team is still working out the unknowns; the
downhill half means it is executing. A dot that stops climbing is the early
signal that something is stuck. This fits agent-assisted work well, where the
unknowns cost more than the typing.

**Now, Next, Later roadmaps.** Three columns, ordered by outcome, with no dates.
They are light enough for a team without a product manager to revise every
quarter.

**Written status with a health flag.** Linear projects and GitHub Projects both
let a project post short regular updates with a status. GitHub's
[project status updates](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/sharing-project-updates)
use values such as "On track" and "At risk," with start and target dates. A
short paragraph and a flag per feature is the format a PM used to write by hand.

**Outcome framing.** Amazon's Working Backwards PR/FAQ defines an epic by
writing the customer announcement first, and OKRs tie features to measurable
outcomes. Both help decide what belongs at the epic level. Neither tracks
progress.

**Dependency boards.** SAFe's PI Planning puts every team's features on one
board and draws the dependencies between them. The full framework is heavy for a
team of a dozen people, but the dependency board is the piece we are missing.

**Bottom-up changelogs.** GitHub's
[automatically generated release notes](https://docs.github.com/en/repositories/releasing-projects-on-github/automatically-generated-release-notes)
list merged pull requests and contributors, and Conventional Commits make commit
history machine-readable. They report what shipped with no upkeep, but they say
nothing about what is in progress or blocked.

## A roll-up to try

None of these needs a PM to work, but most of them assume someone keeps the
links and writes the updates. That is the part to automate.

- **Links are required, not remembered.** Every worklog points at a PBI, and
  every PBI has a parent feature. An agent that opens a worklog asks for the
  parent; a weekly check lists the orphans.
- **Status comes from flow, not opinion.** Each feature's health starts from the
  age of its oldest open PBI and its recent throughput, compared with the team's
  usual cycle time.
- **An agent drafts, a person approves.** Once a week an agent reads each
  feature's PBIs, their worklogs, and their linked PRs, and drafts a status
  update: health flag, oldest item, blockers, and dependencies on other
  features. The feature owner edits and posts it.
- **One view for the whole picture.** Delivery Plans or a Now, Next, Later view
  shows features and their dependencies. Completed features come from closed
  parents, not from a hand-kept list.

This also draws a line around AI in macro planning. Agents are good at reading a
lot of worklogs and summarizing them. They are not a forecasting method. Dates
should come from the team's measured throughput, scaled up from the coarse PBI
effort described in
[Stop Conflating Effort Tracking with Work Tracking](/blog/effort-tracking-vs-task-tracking/),
not from a model's guess.

What is still open: who owns a feature when no one is the PM, how to handle a
dependency between teams that track work in different tools, and whether a
weekly cadence is too slow to catch a stall early.
