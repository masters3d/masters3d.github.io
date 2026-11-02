+++
title = "A Year of Worklogs: Following Behind the Work, and the Report Nobody Writes"
date = "2026-11-29"
description = "A year after I started keeping what I then called plans, worklogs are how my team tracks work in flight. They never needed a strong model, only an agent that follows behind the work, writes it down, and surfaces it. They cover today through the next few days well. Above that, at the feature and epic level, reporting used to be a PM's job, and we have no PM."
template = "blog-post.html"
[taxonomies]
categories = ["Engineering Systems"]
tags = ["worklogs", "agents", "planning", "agile", "flow-metrics", "reporting", "documentation"]
[extra]
scheduled = true
editorial_track = "engineering-systems"
related = ["why-i-love-worklogs", "effort-tracking-vs-task-tracking", "nine-years-of-copious-notes", "one-year-after-opus-4-5", "feature-cradle-to-grave"]
+++

In November 2025 I started keeping a running file for each piece of work I
handed to an agent. I called them plans. They were not the `plan.md` an agent
writes for itself at the start of a session; they were mine, and they outlived
the session. By the time I wrote
[Why I Switched to Worklogs](/blog/why-i-love-worklogs/) in March, they had a
better name and a home in GitHub Issues. My team has been using them for about
nine months.

This month is also a year since Claude Opus 4.5, and I wrote that review
separately in [One Year After Opus 4.5](/blog/one-year-after-opus-4-5/). The two
anniversaries landing together is a coincidence, and the two stories are
different. That one is about what a stronger agent changed in how code gets
written and checked. This one is about a practice that never depended on a
strong agent at all.

## Worklogs never needed a strong agent

The work a worklog asks of an agent is small and repetitive. A
[skill file](/blog/why-i-love-worklogs/#how-we-built-it) describes the template,
the labels, the sizes, and the `gh issue` commands to run. When I say "open a
worklog" or "I just finished the migration," the agent fills in a section and
runs a command. Nothing in that loop calls for deep reasoning. It calls for
consistency: the same template, the same labels, every time.

That is why worklogs held up while the models underneath kept changing. The
agent is not designing anything. It follows behind the work, writes down what
happened, and puts it where other people can find it. That is documentation and
surfacing, which is the part of engineering that always got skipped because a
person had to stop and do it. The strong model earns its cost on the work
itself; the worklog only needs something reliable enough to follow a recipe.

## From my notebook to the team's default

The first version was a lab notebook for me and my agents: what I was working
on, what I tried, what was blocked, and which PR closed it. The value was
continuity. A new session could read the worklog and pick up where the last one
stopped, so I could run several sessions in parallel without holding all of them
in my head.

The team adopted it for the same reason, not because anyone asked for a new
process. Capturing work became one sentence in a conversation instead of a form
in a browser, so people captured the small things too. A teammate looking at a
PR could open the worklog and read how it came about. Effort stayed where
[I had already put it](/blog/effort-tracking-vs-task-tracking/): coarse, at the
product backlog item (PBI) level, in a separate place, and not on every task.

For the near horizon, this works. Today, tomorrow, and a few days out are well
covered. The board shows what is done, what is in flight, and what is blocked.
Agents read the open worklogs, check dependencies and sizes, and suggest what to
pick up next. PBIs are the right grain for a person: small enough that one
person owns one and large enough that tracking it does not become the work. We
stopped breaking PBIs into tasks with hours on them, and nobody misses it.

## The report nobody writes

The gap is above the PBI. On a classic Scrum team the backlog has more levels:
the Azure DevOps
[Scrum process](https://learn.microsoft.com/en-us/azure/devops/boards/work-items/guidance/scrum-process-workflow)
maps PBIs to features for portfolio visibility, features roll up to epics, and
PBIs break down into tasks. Someone keeps those upper levels honest. I know,
because I used to be that someone as a Scrum Master. On most teams it is a
product manager or a Scrum Master who links the PBIs to their feature, notices
that a feature has stalled, and tells the rest of the organization what shipped.

We do not have that role, so the hierarchy drifts. Worklogs roll up nicely into
"what did I do this week," but they do not roll up on their own into "where is
this feature," "which feature is waiting on which," or "what did we finish this
quarter." Once a team grows past about a dozen people, those questions matter
more than the daily ones. You want to know when something is going slowly, early
enough to unblock it. You want to know when one feature depends on another
before the dependency becomes a delay. And you want to report completed features
without someone assembling the list by hand every few weeks.

AI has not closed this gap for us. We use it constantly for the current work and
the next few days. We have not found a good way to use it for macro planning:
the quarter-level view of features and epics, their order, and their
dependencies.

## What other teams use

So I went looking at how other teams and tools handle the level above the PBI.
None of it is new, and most of it assumes someone has time to keep it up.

The hierarchy is already in the tools. Azure DevOps
[Delivery Plans](https://learn.microsoft.com/en-us/azure/devops/boards/plans/track-dependencies)
draw predecessor and successor lines between work items across teams and flag a
dependency in red when it is scheduled to finish after the work that needs it.
GitHub has the same shape with
[sub-issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/adding-sub-issues)
and a
[roadmap layout](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/customizing-the-roadmap-layout)
for projects. The weak point in both is upkeep: the roll-up is only as good as
the parent links, and someone has to keep every PBI attached to the right
feature.

For "what is going slowly," the most useful idea I found comes from flow
metrics. Daniel Vacanti's
[_Actionable Agile Metrics for Predictability_](https://leanpub.com/actionableagilemetrics)
builds on work in progress, cycle time, throughput, and work item age, and has a
chapter on forecasting with the Monte Carlo method. Age is the one that needs no
estimate: an item that has been open much longer than the team's usual cycle
time is the signal. Throughput history then gives a finish date with a
confidence level instead of a single promise. Ryan Singer's _Shape Up_ makes the
same point visually with
[hill charts](https://basecamp.com/shapeup/3.4-chapter-13): uphill is still
figuring the work out, downhill is executing, and a scope that stops climbing is
stuck. The chapter opens with the observation that managers would rather see
status themselves than ask for it, which is the job nobody on my team has.

For the whole picture, Janna Bastow's
[Now, Next, Later roadmap](https://www.prodpad.com/blog/invented-now-next-later-roadmap/)
drops dates in favor of three horizons, light enough to revise every quarter
without a product manager. For the report itself, GitHub
[project status updates](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/sharing-project-updates)
pair a short note with a status such as "On track" or "At risk," and
[generated release notes](https://docs.github.com/en/repositories/releasing-projects-on-github/automatically-generated-release-notes)
list merged pull requests with no upkeep at all, though they say nothing about
what is in progress or blocked.

## The same kind of agent, one level up

Put together, the missing piece is not a method. It is the person who kept the
links and wrote the update, and that work looks a lot like a worklog: follow
behind, write down what happened, surface it. It does not need a strong model
either. It needs every worklog to point at a PBI and every PBI at a feature,
feature health that comes from the age of the oldest open PBI rather than from
someone's opinion, and a weekly pass where an agent reads each feature's PBIs,
worklogs, and linked PRs and drafts the status (health, oldest item, blockers,
dependencies) for a person to approve. Completed features then come from closed
parents instead of a hand-kept list.

What the agent should not do is guess dates. Forecasts belong to measured
throughput, scaled up from the coarse PBI effort we already track, not to a
model's estimate.

The first year took worklogs from my notebook to the team's default. The second
year is about taking the same habit one level up, so the report nobody writes
gets written anyway. Who owns a feature when no one is the PM, and how to track
a dependency on a team that uses a different tool, are still open.
