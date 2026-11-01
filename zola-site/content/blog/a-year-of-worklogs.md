+++
title = "A Year of Worklogs: From a Personal Habit to a Team Practice"
date = "2026-11-29"
description = "A year after I started keeping what I then called plans, worklogs are how my team tracks work in flight. They work well from today out to a few days from now. Above that, at the feature and epic level, nobody owns the roll-up anymore."
template = "blog-post.html"
[taxonomies]
categories = ["Engineering Systems"]
tags = ["worklogs", "agents", "planning", "agile", "retrospectives", "workflow"]
[extra]
scheduled = true
editorial_track = "engineering-systems"
related = ["why-i-love-worklogs", "effort-tracking-vs-task-tracking", "nine-years-of-copious-notes", "reporting-features-without-a-pm"]
+++

In November 2025 I started keeping a running file for each piece of work I
handed to an agent. I called them plans. They were not the `plan.md` an agent
writes for itself at the start of a session; they were mine, and they outlived
the session. By the time I wrote
[Why I Switched to Worklogs](/blog/why-i-love-worklogs/) in March, they had a
better name and a home in GitHub Issues, and that post spends a paragraph
separating worklogs from agent plans because I had spent months blurring the
two.

That makes this the first anniversary of the habit. My team has been using
worklogs for about nine months. This is a look back at how the idea moved from
my notes to something a team of more than a dozen people relies on, what held
up, and where it has started to show its limits.

## From one person's notebook to a team's

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

## What held up

For the near horizon, this works. Today, tomorrow, and a few days out are well
covered. The board shows what is done, what is in flight, and what is blocked.
Agents are good at this range: they read the open worklogs, check dependencies
and sizes, and suggest what to pick up next. Short-term planning with AI has
become routine for us.

PBIs are the right grain for a person. A PBI is small enough that one person
owns it and large enough that tracking it does not become the work. We stopped
breaking PBIs into tasks with hours on them, and nobody misses it.

## Where it falls short

The gap is above the PBI. On a classic Scrum team the backlog has more levels:
epics break into features, features into PBIs, and PBIs into tasks. Someone
keeps those upper levels honest. I know, because I used to be that someone as a
Scrum Master. On most teams it is a product manager or a Scrum Master who links
the PBIs to their feature, notices that a feature has stalled, and tells the
rest of the organization what shipped.

We do not have that role. Nobody on the team is paid to maintain the hierarchy,
so it drifts. Worklogs roll up nicely into "what did I do this week," but they
do not roll up on their own into "where is this feature," "which feature is
waiting on which," or "what did we finish this quarter."

Once a team grows past about a dozen people, those questions matter more than
the daily ones. You want to know when something is going slowly, early enough to
unblock it. You want to know when one feature depends on another before the
dependency becomes a delay. And you want to report completed features without
someone assembling the list by hand every few weeks.

AI has not closed this gap for us. We use it constantly for the current work and
the next few days. We have not found a good way to use it for macro planning:
the quarter-level view of features and epics, their order, and their
dependencies.

## The next year

The first year took worklogs from my notebook to the team's default. The second
year has a clearer problem: report on features and epics with the same low
effort that worklogs brought to daily work, without bringing back a role we do
not have. I am collecting how other teams and tools approach this and will write
up what we try once we have a few weeks of practice with it.
