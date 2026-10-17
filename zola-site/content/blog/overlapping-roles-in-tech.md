+++
title = "Overlapping Roles in Tech"
date = "2027-05-15"
draft = true
description = "Engineering roles overlap on purpose. The risk is not the overlap itself, but the unowned intersection where product, design, engineering, data, operations, and management all assume someone else is carrying the decision."
template = "blog-post.html"
[taxonomies]
categories = ["Engineering Systems"]
tags = ["roles", "ownership", "collaboration", "engineering-management", "systems-thinking"]
[extra]
editorial_track = "engineering-systems"
+++

In April 2022 I saved a note with almost no prose of my own. It pointed to a
thread by Gergely Orosz about overlapping roles in tech and a picture of the
places where those roles cross. The useful part was the warning I wrote above
it: roles overlap in tech, and there is an intersection you should be aware of.
Orosz's broader product-minded engineering work argues that strong engineers do
not only write code. They also carry product sense, collaborate with design and
data, understand operations and support, and help align complicated work across
teams.

That sentence stayed unfinished because the picture was doing most of the work.
Product, program management, design, engineering, data, operations, support, and
leadership all touch the same product from different angles. A clean org chart
makes them look separate. The work does not. The work creates intersections, and
most serious confusion lives there.

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
shared. That map has to be built by the team doing the work. The warning in the
original note is still the one I would keep: beware the intersection where
everyone is near the decision and nobody owns it.
