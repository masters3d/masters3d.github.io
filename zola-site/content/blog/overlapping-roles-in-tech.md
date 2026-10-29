+++
title = "Overlapping Roles in Tech"
date = "2027-03-15"
description = "Engineering roles overlap on purpose. A Venn diagram of writing code, stakeholder management, and people management shows which roles share which work, why the center where all three meet is a warning, what changes when software engineers start managing agents, and why every overlap needs a named owner."
template = "blog-post.html"
[taxonomies]
categories = ["Engineering Systems"]
tags = ["roles", "ownership", "collaboration", "engineering-management", "systems-thinking"]
[extra]
scheduled = true
editorial_track = "engineering-systems"
related = ["quality-engineering-vs-engineering-quality", "why-doc-how-doc-steering-agents-from-the-middle", "people-systems-and-the-hiring-pipeline"]
+++

In April 2022 I saved a note with almost no prose of my own. It pointed to a
[December 2021 post by Gergely Orosz](https://xcancel.com/GergelyOrosz/status/1468606386439344139)
about overlapping roles in tech, with a picture of the places where those roles
cross. The useful part was the title I wrote above it: roles overlap in tech,
and there is an intersection you should beware of. Orosz's broader
product-minded engineering work argues that strong engineers do not only write
code. They also carry product sense, collaborate with design and data,
understand operations and support, and help align complicated work across teams.

That title stayed unfinished because the picture was doing most of the work.
Here is the picture redrawn, so the argument does not depend on a social media
link staying online.

![A Venn diagram of three overlapping circles labeled writing code, stakeholder management, and people management. Software engineer sits in writing code only. Product manager and technical program manager sit in stakeholder management only. Staff engineer sits where writing code and stakeholder management overlap. Engineering manager sits in people management only. Tech lead manager sits where writing code and people management overlap. A product or program manager with reports sits where stakeholder and people management overlap. The center, where all three overlap, is labeled beware.](/images/blog/overlapping-roles-in-tech.svg)

## Where the Roles Overlap

The picture does not sort roles by title. It sorts them by three kinds of work:

- **Writing code**: designing, building, and changing the system with your own
  hands.
- **Stakeholder management**: agreeing with people outside the team on what gets
  built, when, and why. That means customers, partners, leadership, and
  neighboring teams.
- **People management**: hiring, growing, and evaluating the people on the team,
  and carrying their careers.

Each role sits in the region that matches the work it does every week. Reading
from the edges in:

- **Writing code only: software engineer.** The work is the system itself.
  Stakeholder and people decisions reach this role through someone else.
- **Stakeholder management only: product manager and technical program
  manager.** The work is the agreement about what to build and when. They do not
  write the production code, and they do not manage the people who do.
- **People management only: engineering manager.** The work is the team: hiring,
  growth, performance, and the health of how the team works. An engineering
  manager no longer writes the production code and is not the one who decides
  what the product should be. An engineering manager still talks to
  stakeholders, but on behalf of the team, not as the owner of the product
  agreement.
- **Writing code and stakeholder management: staff engineer.** Still writes
  code, and also negotiates direction with other teams and leaders, without
  direct reports. The overlap here is with the product manager: both talk to
  stakeholders about what the system should become.
- **Writing code and people management: tech lead manager.** Still writes code,
  and also has reports. The overlap is with both neighbors: with the software
  engineers on the code, and with the engineering manager on the people.
- **Stakeholder and people management: a product manager or technical program
  manager with reports.** Owns the agreement about what to build, and also
  manages other product or program managers. The overlap is with the product
  manager on stakeholders, and with the engineering manager on people.
- **All three: beware.** The picture puts no title in the center, only a
  warning. One person writing code, managing people, and managing stakeholders
  is doing three jobs with one calendar. Something gets dropped, and it is
  rarely clear which one until later: the review that waits, the one-on-one that
  keeps moving, or the partner team that hears about a change late. When one
  person holds all three, nobody else is close enough to notice the drop.

So the overlaps are specific. Each two-circle region shares one kind of work
with each of its neighbors, and the shared work is where two roles can both
claim the same decision. A staff engineer and a product manager can both be
right about direction and still disagree. A tech lead manager and an engineering
manager can both be right about the team and still pull it two ways.

The picture has three circles. A real product adds more: design, data,
operations, and support all touch the same product from different angles. A
clean org chart makes them look separate. The work does not. Every circle added
creates new intersections, and most serious confusion lives there.

## The Overlap Is Not the Bug

It is tempting to solve role confusion by drawing harder boundaries. Product
owns the what. Engineering owns the how. Design owns the experience. Data owns
the measurement. Operations owns the running system. Management owns the people
system. The clean version is easy to teach, but the real version starts failing
as soon as the product becomes complicated.

A feature is never only a feature. It is a customer promise, an interface, a set
of tradeoffs, a support burden, a cost curve, a metric, and a future maintenance
surface. If only one role can speak into it, the feature is weaker. Product
needs engineering judgment to know whether the promise is cheap or expensive.
Engineers need product judgment to know whether a technical simplification
changes the user value. Design needs data to know whether a flow works after
launch, and data needs context to avoid measuring the wrong thing with
confidence.

Overlap is where the product becomes real. The problem is not that two roles
care about the same decision. The problem is when both roles care about it from
a different angle and nobody names who is allowed to make the final call.

That is the dangerous intersection: not shared attention, but shared ambiguity.

## What Goes Wrong at the Intersection

The first failure mode is the invisible handoff. Everyone thinks the decision
belongs just across the boundary. Product assumes engineering will flag the edge
case. Engineering assumes product accepted the edge case by prioritizing the
feature. Design assumes the behavior follows the requirements. Support assumes
someone has thought about the troubleshooting path. Nobody is negligent. The
system simply allowed responsibility to evaporate at the border.

The second failure mode is duplicate authority. Two groups make different
versions of the same decision and discover the conflict late. A product goal
says "reduce friction." A security requirement says "add verification." An
operational need says "make recovery explicit." Each goal is valid. Without a
named owner for the intersection, the conflict becomes personal because there is
no decision system to hold it.

The third failure mode is local optimization. Each role makes the right choice
for its own surface area and the combined result is worse. Engineering
simplifies the implementation by pushing complexity into the user flow. Design
simplifies the experience by hiding state the operator needs. Data simplifies
reporting by choosing a metric that can be captured cheaply, even if it changes
the team's behavior in the wrong direction. The individual decisions are
defensible. The system result is not.

This is why I do not think role overlap should be treated as an exception. It is
a normal part of engineering work. The organization needs a way to work inside
that overlap without pretending it can be eliminated.

## Name the Decision, Then Name the Owner

A useful role boundary does not say, "stay out." It says, "here is the decision
being made, here is who contributes context, and here is who decides when the
context conflicts."

For example, product may own the customer outcome, engineering may own the
technical design, and operations may own the production readiness standard. But
for a risky launch, the intersection itself needs an owner. Is the launch a
product bet with known operational risk? Is it an operational decision where the
system is not ready? Is it an engineering design decision because the risk comes
from architecture? The answer can change by situation, but it cannot remain
implicit.

Teams that handle this well tend to use lightweight rituals rather than heavy
governance. They write decision records. They state assumptions in design docs.
They ask, "who is the directly responsible individual for this boundary?" They
invite the adjacent roles early, before the cost of changing direction becomes
political. They separate input from authority, which lets people contribute
without turning every disagreement into a power contest.

That separation matters. Being consulted is not the same as being responsible.
Being responsible is not the same as ignoring everyone else. A role intersection
works when the owner is clear enough to decide and humble enough to carry the
context from the neighboring roles.

## When Software Engineers Manage Agents

The picture is from 2021, and one region has moved since then. A software
engineer who steers coding agents is no longer only in the writing-code circle.
As I wrote in
[the Why doc and the How doc](/blog/why-doc-how-doc-steering-agents-from-the-middle/),
an agent turns the person steering it into a manager whether they wanted the
role or not: it executes against the context it was given and comes back for
direction when that context runs out. Read against the three circles, that has a
few consequences.

**The engineer reaches into the people circle, but only half of it.** Steering
an agent uses the delegation half of people management: stating intent,
supplying context, setting boundaries, reviewing the result, and correcting
without starting over. It does not use the career half. An agent is not hired,
does not grow, and has no performance review. So the engineer picks up the
management skills without the management job, and the region the engineer moves
into is closer to tech lead manager than to engineering manager.

**The engineer also reaches into the stakeholder circle.** An agent cannot
supply the reason the work matters. Someone has to carry the outward agreement
into the task, which is why I ended up writing a Why doc for stakeholders and a
How doc for the agent. The software engineer who used to receive stakeholder
decisions through someone else now has to hold enough of them to steer.

**Together, that moves the software engineer toward the center.** Writing code,
carrying the stakeholder context, and directing workers is the region the
picture labels beware. The calendar problem looks different with agents, because
the agents take much of the typing, but the drop is the same kind. What gets
dropped is review. An engineer running several agents can produce more change in
a day than anyone, including that engineer, can understand in a day, and
[there is no speedup for shared understanding](/blog/no-speedup-for-shared-understanding/).
The review that waits is now the review of work nobody wrote by hand.

**Ownership does not move to the agent.** An agent can contribute context to an
intersection. It cannot be the named owner of one, because it cannot be held to
the decision afterward. Every rule in this post about naming the owner still
applies, and the owner is still a person. Delegating to an agent without naming
who is accountable for its output recreates the invisible handoff described
above, with one fewer person in the room to notice it.

**The edges between roles get thinner.** If a software engineer handles
delegation and carries stakeholder context, the line between that engineer, a
staff engineer, and a technical program manager narrows. In
[Agents Are Taking the Drive](/blog/agents-are-taking-the-drive/) I predicted
more individual contributors managing agents instead of people. That is still a
prediction, not an observation. What I can observe is the narrower version: the
skills that used to separate the managers from the engineers in this picture are
now expected of the engineers too.

**The work that grew new engineers is the work agents take first.** The small,
well-bounded tasks that used to go to a new engineer are the same tasks that are
easiest to hand to an agent. If senior engineers delegate those to agents
instead of to people, the people circle loses the work it used to grow people
with. That is a concern, not a finding, and it is the part of this shift I would
watch most closely.

## The Intersection Is a Design Surface

I saved that 2022 note because the diagram made visible something that is easy
to feel and hard to name. When roles overlap, the product is not being passed
from one person to another like a baton. It is being shaped by several kinds of
judgment at once.

The question is not whether product, design, engineering, data, operations, and
management should overlap. They already do. The useful question is whether the
team has designed the intersections with the same care it designs APIs. Where is
the contract? What is the expected input? Who resolves conflict? What happens
when the owner is wrong? How does feedback return to the boundary so the next
decision is better?

An org chart can show who reports to whom. It cannot show where judgment must be
shared. That map has to be built by the team doing the work. The original
picture put one word in the middle: beware. I would keep two versions of that
warning. Beware the role that sits in all three circles alone, where one person
owns every decision and nobody else can see what was dropped. And beware the
intersection where everyone is near the decision and nobody owns it. Agents make
both warnings more likely, because they let one engineer reach into every circle
at once, and they cannot be the owner of anything they touch.
