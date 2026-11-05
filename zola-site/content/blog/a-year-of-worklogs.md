+++
title = "A Year of Worklogs: What They Are For, Where They Stop"
date = "2026-11-29"
description = "I have kept worklogs for a little over a year and my team for about a year. They are the best tool we have for tracking work as you do it. They are not a board, a feature tracker, or an epic tracker, and the year's growing pains came from stretching them toward those jobs and from working with teams that track everything in Azure DevOps."
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
better name and a home in GitHub Issues. I have kept them for a little over a
year now, and my team has used them for about a year.

This is not a victory lap. Worklogs earned their place, and they are still the
first thing I reach for. But most of what we learned this year was about their
edges: what they are for, what they are not for, what happened when we pushed
them past that line, and what happened when we had to work with teams that never
used them at all.

(This month is also a year since Claude Opus 4.5, which I wrote about in
[One Year After Opus 4.5](/blog/one-year-after-opus-4-5/). That is a different
story. As the next section explains, worklogs never depended on a strong model.)

## What worklogs are for

A worklog tracks work as you do it. That is the whole job, and it is the reason
they work.

When I am in the middle of a feature and notice something off to the side, such
as a bug, an edge case nobody is handling, or a cleanup that does not belong in
this PR, I file it away in one sentence and keep going. The agent opens a
worklog with what it already knows: the file, the call path, what I was doing
when I saw it, and why it matters. Later one of three things happens. I pick it
up myself, I hand it to another agent session, or a teammate takes it. In every
case the context is already written down, so whoever picks it up starts from
where I stopped instead of from a one-line title.

That is something a planning board does not give you. A board item is written
before the work, from memory, by someone deciding what should happen. A worklog
is written during the work, by the person, or the agent, who is looking at the
code. Planned work can go in a worklog too, but the format is built for the
things you discover while working.

The second thing worklogs give us is visibility of current progress. Anyone on
the team can see what is in flight, in which area, and what is blocked, without
a status meeting. As a personal notebook and as a view of work in progress, they
are better than anything we used before.

## They never needed a strong agent

The work a worklog asks of an agent is small and repetitive. A
[skill file](/blog/why-i-love-worklogs/#how-we-built-it) describes the template,
the labels, the sizes, and the `gh issue` commands to run. When I say "file a
worklog for that edge case" or "I just finished the migration," the agent fills
in a section and runs a command. Nothing in that loop calls for deep reasoning.
It calls for consistency: the same template and the same labels every time.

That is why worklogs held up while the models underneath kept changing. The
agent is not designing anything. It follows behind the work, writes down what
happened, and puts it where other people can find it. That is documentation and
surfacing, the part of engineering that always got skipped because a person had
to stop and do it.

## What worklogs are not

A worklog is not a replacement for the Azure DevOps board. It is not a feature
tracker. It is not an epic tracker, and it is not the kanban-style view of a
whole area of work that a team or a VP looks at to answer "what is the update
here?"

The reason is the same as the reason they work. A worklog captures work while it
happens, at the grain of what one person, or one agent, is doing. Feature and
epic tracking answers a different question: what did we commit to, in what
order, which piece is waiting on which, and when will it land. Those questions
are asked before the work and across many people's work. It took us most of the
year to say this plainly, because the first instinct with a tool that works is
to give it more jobs.

## How we stretched them

The metadata is where the stretching started. The first worklogs had a title,
four sections, a size, and a status. Over the year we added more because each
addition solved a real problem.

The first useful addition was a role. Most worklogs are roughly a task. Some are
bugs. Some are bigger than one piece of work and act like a product backlog item
(PBI). GitHub
[sub-issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/adding-sub-issues)
let a worklog be the parent of other worklogs, so a PBI-sized worklog can hold
the tasks and bugs under it. Two roles, a unit of work (task or bug) and a PBI
that spans more than one unit, fit the format well.

The PBI role already shows strain. A PBI works best when it is scoped to a
sprint or a month: you open it with that period's goal, close it at the end, and
open the next one with the next goal. Worklogs do not fit that rhythm. A
worklog's value is its history in one place, so moving it between periods,
copying it forward, or re-scoping it every sprint works against what makes it
useful. A long-lived worklog that plays the part of a PBI either never closes or
loses its history when it is split.

Then we tried features. A feature is several PBIs, and some of us started using
a worklog to track several PBIs under a feature. That pushes the format to its
limit. The worklog stops being about the work in front of you and becomes a
summary of other people's work. It needs owners, dates, and dependencies that
the template never had. Epics, which are several features, are another level up
again. That is the level where a VP, or a team looking at the whole area, wants
an update, and no amount of metadata on a worklog makes it the right place for
that answer.

Every level we added made the skill file longer, the template more complicated,
and the agent's job less mechanical. Simplicity was the reason the practice
spread, and we were trading it away one field at a time. The lesson I take into
year two is to keep worklogs to those two roles, the unit of work and the PBI,
and to stop there.

## Growing pains with other teams

The pressure to stretch did not only come from inside the team. Most of the
teams we work with track everything in Azure DevOps, at every level, and
worklogs mean nothing to them. When they depend on something we are building,
they push back with fair questions. How do we know it is progressing? Where is
it on the board? What is the timeline? A link to a set of GitHub issues written
in our template does not answer those questions in a form they can use.

From our side, keeping Azure DevOps up to date at the same detail feels like
pure overhead. The agent already has the context. It wrote the worklog. Copying
the same facts into another system by hand, at a level of detail nobody on our
team reads, is exactly the busywork worklogs removed.

Both sides are right, and that is the growing pain. Our partners need the
hierarchy: features, epics, dependencies, and dates. We need the low-friction
capture. The temptation was to make worklogs carry the hierarchy so we would not
have to maintain both, and the previous section is what that temptation cost.

There is a second gap under the first one. On a classic Scrum team, someone
keeps the upper levels honest. The Azure DevOps
[Scrum process](https://learn.microsoft.com/en-us/azure/devops/boards/work-items/guidance/scrum-process-workflow)
maps PBIs to features for portfolio visibility, and features roll up to epics.
On most teams a product manager or a Scrum Master links the PBIs to their
feature, notices when a feature has stalled, and tells the rest of the
organization what shipped. I know, because I used to be that Scrum Master. We do
not have that role, so even when the hierarchy exists in Azure DevOps, it
drifts. Once a team grows past about a dozen people, the questions at that level
matter more than the daily ones: what is going slowly, which feature is waiting
on which, and what we finished this quarter.

AI has not closed this gap for us yet. We use it constantly for the current work
and the next few days. We have not found a good way to use it for macro
planning, the quarter-level view of features and epics, their order, and their
dependencies.

## What other teams use

So I went looking at how other teams and tools handle the level above the PBI.
None of it is new, and most of it assumes someone has time to keep it up.

The hierarchy is already in the tools. Azure DevOps
[Delivery Plans](https://learn.microsoft.com/en-us/azure/devops/boards/plans/track-dependencies)
draw predecessor and successor lines between work items across teams and flag a
dependency in red when it is scheduled to finish after the work that needs it.
That is the view our partner teams are asking for. GitHub has a similar shape
with sub-issues and a
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
confidence level instead of a single promise, which is a better answer to "what
is the timeline?" than a guess. Ryan Singer's _Shape Up_ makes a similar point
visually with [hill charts](https://basecamp.com/shapeup/3.4-chapter-13): uphill
is still figuring the work out, downhill is executing, and a scope that stops
climbing is stuck. The chapter opens with the observation that managers would
rather see status themselves than ask for it, which is what our partner teams
keep telling us.

For the whole picture, Janna Bastow's
[Now, Next, Later roadmap](https://www.prodpad.com/blog/invented-now-next-later-roadmap/)
drops dates in favor of three horizons, light enough to revise every quarter
without a product manager. For the report itself, GitHub
[project status updates](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/sharing-project-updates)
pair a short note with a status such as "On track" or "At risk," and
[generated release notes](https://docs.github.com/en/repositories/releasing-projects-on-github/automatically-generated-release-notes)
list merged pull requests with no upkeep at all, though they say nothing about
what is in progress or blocked.

## Year two: keep them small, build the bridge

The direction for the second year is to stop asking worklogs to be the hierarchy
and to bridge to it instead.

Worklogs stay at two roles: the unit of work and the PBI. Features and epics
live where our partners already look, in Azure DevOps. The connection between
the two is a link, every PBI-sized worklog pointing at the work item it belongs
to, rather than a copy of the same facts in two places.

The upkeep that a PM or Scrum Master used to do looks a lot like a worklog's
job, one level up: follow behind, write down what happened, surface it. It does
not need a strong model either. An agent can read each feature's linked worklogs
and PRs on a schedule and draft the status our partners ask for: health, the
oldest open item, blockers, and dependencies. A person approves it before it
lands on the board. Feature health comes from the age of the oldest open PBI
rather than from someone's opinion. Completed features come from closed parents
instead of a hand-kept list.

What the agent should not do is guess dates. Timelines belong to measured
throughput, scaled up from the coarse PBI effort
[we already track](/blog/effort-tracking-vs-task-tracking/), not to a model's
estimate.

The first year took worklogs from my notebook to the team's default and showed
us where they stop. The second year is about respecting that line: worklogs for
the work as it happens, the board for the commitments other teams depend on, and
an agent following behind to keep the two in step. Who owns a feature when no
one is the PM is still an open question.
