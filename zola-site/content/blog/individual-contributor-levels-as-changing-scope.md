+++
title = "Individual Contributor Levels as Changing Scope"
date = "2027-09-04"
description = "Individual contributor levels are easiest to understand as changes in scope, and each change makes a different job. The work grows from learning and code, to components, to systems, to the systems that shape other teams, which is why excellence at one level does not by itself prove readiness for the next."
template = "blog-post.html"
[taxonomies]
categories = ["Engineering Systems"]
tags = ["career", "individual-contributor", "levels", "scope", "engineering-systems"]
[extra]
scheduled = true
editorial_track = "engineering-systems"
related = ["level-zero-is-an-apprenticeship", "career-levels-depend-on-context", "pie-theory-being-seen-at-work", "people-systems-and-the-hiring-pipeline", "ten-years-in-software-engineering"]
+++

When I wrote down how I think about software engineering careers, the first
thing I listed was a ladder of individual contributor (IC) levels, from 0
through 7 and beyond. I wrote it for software, but the ladder is really a scope
model, and that holds for any engineering organization. The job changes as the
system you are expected to hold in your head gets larger, and it changes enough
that I think of each level as a different job, not a harder version of the one
below it.

That is a better framing than treating levels as seniority badges. Time matters,
but time is not the mechanism. The mechanism is expanding responsibility: from
learning your own task, to owning a component, to guiding a system, to shaping
how multiple teams work.

## Level Is a Boundary of Responsibility

Level 0 in the source is Apprentice. The expected scope is small and concrete:
learn the fundamentals, use version control, complete well-defined tasks,
participate in code review as a learner, and document progress. The control
boundary is personal. You control your learning, your questions, your response
to feedback, and the quality of the code you touch.

Level 1 becomes Component Creator. The work is still bounded, but the boundary
now includes independent implementation from technical specifications, tests,
documentation, and maintenance of a component. The engineer begins mentoring
Level 0 engineers and participating in design discussions. The scope has moved
from "can I complete this task?" to "can I own this piece reliably enough that
others can build on it?"

Level 2 is Component Designer and Cross-Team Collaborator. Now the source starts
using words like design documents, integration, performance, scalability, and
cross-team coordination. The engineer is not only implementing within a design.
They are creating designs other engineers can implement. They also have to
understand how their component fits into other teams' work.

Level 3 is System Lifecycle Guide. The boundary expands again. The source names
end-to-end system design, technical debt management, strategic refactoring,
monitoring, mentoring, and contribution to organizational technical strategy.
The engineer is no longer only making a good local decision. They are guiding a
system from conception through maintenance.

Those first four levels already show the shape. More senior does not simply mean
harder tasks. It means a wider time horizon, more dependencies, more people
affected by the decision, and a larger obligation to preserve context for
others.

## Senior Scope Is Mostly System Design

The source compresses Levels 4 through 7+ more than the early levels, but the
same pattern continues.

Level 4 is System Maintainer and Integrator. The focus is maintaining complex
systems and integrating across multiple systems. Level 5 is Multi-System
Designer, with technology strategy, platform evolution, and domain thought
leadership. Level 6 coordinates system design across sister teams. Level 7+
architects systems of systems and shapes technical direction beyond one
organization.

That progression is not only a bigger title. It changes the medium of the work.
At Level 0, the medium is code and learning. At Level 2, the medium includes
design documents and cross-team interfaces. At Level 4, the medium includes
technical debt portfolios, platform seams, and organizational coordination. At
Level 7+, the medium is the relationship among systems and the people who evolve
them.

The source's Locus of Control section makes the same point from a different
angle. As levels progress, the sphere of control expands. Levels 0 and 1 control
learning and code while accepting architecture guidance. Levels 2 and 3 control
component design and influence team practices. Levels 4 through 7+ control
system architecture and influence organizational strategy. Career progression is
not escaping constraints. It is learning which constraints are yours to change.

## Each Level Is a Different Job

Looking back on
[ten years in software engineering](/blog/ten-years-in-software-engineering/), I
wrote that my work came to be judged less by whether my part compiled and more
by whether the whole system produced the intended result. That is a different
definition of done, and a different definition of done makes a different job.

Promotions get confusing when they are described only as performance. The
performance expected at each level is different in kind. A Level 1 who writes
excellent code is doing the Level 1 job well. That does not by itself prove
Level 3 readiness, because Level 3 asks whether systems can be guided across
time. A Level 3 may write less code than before because the highest value work
is now design, review, mentoring, and context preservation.

Put the levels side by side and very little about the work stays fixed. The unit
of work grows from a task, to a component, to a system, to systems of systems.
The output changes from code, to code other people build on, to designs other
people implement, to decisions other teams carry. The feedback loop stretches
from minutes (a test run, a review comment), to quarters (whether a design holds
up once other teams build on it), to years (whether a platform bent the way the
organization needed). And the people the work flows through change from
yourself, to your team, to teams you do not manage, to people who may never
learn your name.

Each of those changes asks for a skill the previous level did not train. A short
feedback loop teaches you to trust what you can verify today. A long one asks
you to act on judgment and wait a year to find out whether you were right.
Working through other people asks you to make your reasoning clear enough that
they can carry it when you are not in the room.

The old job keeps pulling, too. It is the job you were good at, the one that
earned the promotion, and its feedback arrives in minutes instead of quarters. A
newly promoted engineer who grabs the hardest ticket on the board is doing the
previous job very well and neglecting the current one. The pull makes sense:
merged code feels like progress in a way a design review rarely does.

There is a name for what happens when an organization treats the next job as a
reward for the current one. Laurence J. Peter and Raymond Hull published
[_The Peter Principle_](https://archive.org/details/peterprinciple0000pete_q9s7)
in 1969 as satire: in a hierarchy, people tend to rise to their level of
incompetence, because each promotion is earned in the job they are leaving
rather than the one they are entering. Fifty years later,
[Benson, Li, and Shue](https://academic.oup.com/qje/article/134/4/2085/5550760)
tested the idea with data on sales workers at 131 firms. Firms did promote their
best salespeople, yet among those promoted, the better someone had sold before
the promotion, the worse their team sold under them as a manager. The authors
estimate that a policy promoting fewer top sellers would raise average manager
quality, measured by their teams' sales, by about 30%.

That study covers a sharp job change, from selling to managing people who sell,
and IC levels change the job less abruptly. The mechanism still applies.
Excellence at the current level is the easiest evidence to see, so it is the
evidence promotion processes lean on, whether or not it predicts the next job.

I take three things from this:

- Promotion evidence should include some of the next job's work, not only the
  current job done brilliantly.
  [Promotion-Driven Development](/blog/promotion-driven-development/) covers
  what happens when the evidence a process rewards drifts from the work the
  system needs.
- A promotion is a job change, not a prize.
  [Good at it is not the same as wanting it](/blog/good-at-it-is-not-the-same-as-wanting-it/):
  an excellent Level 3 who does not want the Level 4 job is making a career
  decision, not failing to grow.
- Every new level starts cold. A team change cost me six to twelve months while
  trust and context rebuilt, as I described in
  [Warming Up the Tires](/blog/warming-up-the-tires/), and a new level asks for
  some of the same patience. The first months of a new job rarely look like
  mastery.

## Visibility Follows the System

The source also connects levels to Performance, Image, and Exposure. I would
translate that carefully. Performance is the work actually done. Image is the
representation others can form from that work. Exposure is whether the right
people and systems can see it.

At low levels, visibility can stay close to the team. A learning journal, a good
pull request description, and thoughtful code review questions are enough to
show growth. At middle levels, visibility has to cross team boundaries because
the work itself crosses team boundaries. Design docs, demos, architecture notes,
and cross-team relationships become part of the job. At high levels, visibility
has to reach the forums where standards, platforms, and long-term tradeoffs are
set.

That does not mean career growth is self-promotion instead of engineering. It
means system-level work cannot be evaluated if it remains invisible. A component
can prove itself by running. A strategy has to be explained, adopted, and
carried by other people. The artifact changes with the level.

This is the engineering systems reason to care about levels. A good level guide
is not a status hierarchy. It is an operating manual for where responsibility
lives. It tells an apprentice which things are theirs to control, tells a system
maintainer which decisions must be made durable, and tells an organization what
kind of evidence should count for growth.

There is a boundary to this model. Companies do not use levels consistently, and
a title at one company may map to a different scope somewhere else. That is why
the scope framing is safer than the title framing. Ask what system the person is
expected to improve, how long the time horizon is, and who must carry the
decision after they make it. Those answers reveal the real level more clearly
than the label on the ladder.

The opening source calls this a people systems framework, and that phrase is the
most useful part. Levels are not only about people. They are about how an
engineering system allocates ownership across people. When the scope is clear,
growth is not a mystery ladder. It is a visible series of different jobs: task,
component, system, systems of systems.
