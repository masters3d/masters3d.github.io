+++
title = "Development vs Production"
date = "2026-10-17"
description = "Building a product and running it are two different kinds of work. Development ends when the thing exists; production never ends, and what it teaches has to flow back into the product as its own stream of work. Treating the two as one job hides the second one, and the accounting split between cost of goods sold and operating expenses turns out to describe the same line."
template = "blog-post.html"
[taxonomies]
categories = ["Engineering Systems"]
tags = ["production", "operations", "feedback-loops", "reliability", "ownership", "systems-thinking"]
[extra]
editorial_track = "engineering-systems"
+++

In July 2022 I wrote a two-sentence note in my notes repository,
[ingenio](https://github.com/masters3d/ingenio/issues/21): the act of developing
a product differs from actually running that product, especially at scale.
Feedback from production should create work streams that flow back to improve
the product, but that improvement flow is different from just making the
product. A day later I added a question under it that I did not know how to
answer: how much of this correlates to cost of goods sold versus operating
expenses?

That second question is the one that made the note worth keeping. It suggested
the split I was noticing was not a matter of team preference. It was showing up
in how businesses already count money.

## Two Kinds of Work That Share a Codebase

Development is the work of making something exist. It has a shape most engineers
recognize: a goal, a design, a sequence of changes, and a point where the
feature is done. The questions are about correctness and fit. Does it do what we
said it would do? Does it solve the problem the customer has?

Production is the work of keeping that thing alive in the real world. It has no
done state. The questions change from "does it work" to "does it keep working":
under load, during a dependency outage, at three in the morning, after a
configuration change someone made for a different reason. The inputs are not
requirements. They are signals: alerts, latency curves, support tickets, cost
reports, and incidents.

The two kinds of work happen in the same repository and are often done by the
same people, which is why it is easy to treat them as one job. They are not one
job. Development is a project, and production is a process. A project can be
estimated and finished. A process can only be staffed, measured, and improved.
When a team plans as if production were a project, the production work does not
go away. It shows up as interruptions in a sprint that was planned with no room
for them, and the team experiences its own operational load as a series of
surprises.

This split is not unique to software. A car company designs a model once and
then runs an assembly line every day for years. The design team and the plant
share the product, but nobody confuses designing the car with keeping the line
running. The plant has its own engineers, its own metrics, and its own budget,
and what it learns (a part that keeps failing inspection, a step that keeps
slowing the line) goes back to design as a specific request. Software teams tend
to blur that line because the "factory" is a deployment pipeline and a few
dashboards, and it is easy to forget that something is running at all.

## The Accounting Already Knows

The question I left under the note took a while to make sense to me. In a
software business, the cost of goods sold (COGS) covers what it costs to deliver
the product to customers who already have it: hosting, support, and the
operations needed to keep the service up. Operating expenses (OpEx) cover the
cost of running the business beyond delivering the product, and research and
development is one of the largest lines in it for most software companies.

That is the same line I was drawing in the note. Running the product lives in
COGS, close to every customer and every dollar of revenue. Building the product
lives in the research and development part of OpEx, where it is treated as an
investment in the future. The finance team already keeps the two apart, because
they behave differently: one scales with usage, the other scales with ambition.

When the engineering organization does not make the same distinction, two things
go wrong. First, production work becomes invisible in planning. It is not on the
roadmap, so it competes with roadmap work for the same hours, and it loses until
an incident forces it to win. Second, the cost of production gets attributed to
development. A team that spends half its time keeping a service alive looks like
a team that is slow at building features. I wrote about a related reward problem
in
[The Last 20% and the Next Nine](/blog/the-last-twenty-percent-and-the-next-nine/):
the work that makes a system dependable is the work least likely to be noticed.

## Feedback as Its Own Stream

The part of the note I care most about now is the last clause: the improvement
flow from production is different from just making the product. Production is
the only place where the product meets reality at full scale, so it is the best
source of information about what to build next. But that information arrives in
a different form from a feature request. It arrives as a pattern of pages, a
cost curve that bends the wrong way, a class of tickets that keeps coming back.

If that signal has no destination, it gets handled as a one-off every time. An
engineer fixes the immediate problem, writes a short note, and moves on. The
same problem returns next month, handled by someone else. The fix for that is
not more heroics. It is a deliberate work stream that turns production signals
into product changes: incident follow-ups that are tracked like features, cost
and reliability goals that sit next to feature goals in planning, and a regular
review where the people running the system tell the people building it what
reality said. Blameless review is what makes that review honest
([Blameless Engineering](/blog/blameless-engineering-debugging-systems-not-people/)
covers why).

This stream has a different rhythm from feature development. It is driven by
evidence rather than by a roadmap, and its success looks like nothing happening.
That makes it easy to underfund. A useful test is to look at last quarter's
incidents and ask how many of them produced a tracked change in the product, not
just a fix in production. If the answer is close to zero, the feedback stream
does not exist yet, whatever the team believes about its own process.

None of this argues for separate teams that throw work across a wall. My view on
that has not changed since writing
[Quality Engineering vs Engineering Quality](/blog/quality-engineering-vs-engineering-quality/):
the people who build a thing should own how it behaves. The point here is
narrower. Even when the same engineers do both kinds of work, they should know
which kind they are doing, plan for both, and give the second one a real path
back into the first.

Reading that note again four years later, the question I left under it was the
useful part. I suspected the difference between building and running a product
was more than a matter of taste, and the books already said so. What I would add
today is the step the note only pointed at: once production is treated as its
own kind of work, its lessons stop being interruptions and start being one of
the most reliable inputs to what gets built next.
