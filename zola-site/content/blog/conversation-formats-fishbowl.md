+++
title = "Conversation Formats Are Engineering Tools"
date = "2027-12-15"
draft = true
description = "Collaboration is shaped by the container that holds the conversation. A fishbowl, a design review, an RFC thread, and a one-on-one all produce different information, so the format should be chosen as deliberately as any other engineering tool."
template = "blog-post.html"
[taxonomies]
categories = ["Engineering Systems"]
tags = ["collaboration", "conversation", "fishbowl", "meetings", "facilitation", "shared-understanding"]
[extra]
editorial_track = "engineering-systems"
+++

In May 2022 I wrote the phrase "conversation types for collaborations" and put
one example underneath it: a fishbowl conversation. Wikipedia describes the
fishbowl as a format where a small inner circle actively discusses a topic while
a larger outer circle observes. In an open version, someone from the outside can
take an empty seat and join, while someone else leaves the inner circle; in a
closed version, the inner circle is replaced after a set interval. That was the
entire note. Looking back, the thinness is almost useful. I was not collecting
meeting tricks. I was noticing that conversation has formats, and those formats
change what a group is able to learn.

Engineers often talk about meetings as if the only variables are duration and
attendance. Is this meeting necessary? Can it be thirty minutes? Who needs to be
there? Those questions matter, but they miss the structure of the conversation
itself. A one-on-one, a design review, a broadcast update, an RFC thread, a
fishbowl, and an incident review are different tools. Put the same people and
the same topic into each format, and you will get different information.

That should not surprise us. We accept this everywhere else. A debugger, a load
test, and a type checker all inspect a system differently. Nobody says, "testing
is testing," and then picks one at random. Collaboration deserves the same care.
If the goal is shared understanding, the container matters.

## The format decides who can think out loud

A fishbowl conversation is useful because it separates speaking from observing
without turning observation into absence. A small inner circle discusses the
topic while an outer circle listens. Seats can be opened or rotated so observers
enter when they have something to add. The format creates a visible boundary
around the active conversation while keeping the wider group present.

That boundary changes behavior. In a normal large meeting, people compete for
airtime, hesitate because the room is too big, or assume silence means
agreement. In a fishbowl, the inner circle can go deeper because it is small,
and the outer circle can listen without having to perform participation every
minute. The group gets both focus and audience.

This is especially useful when a topic has more stakeholders than active
decision makers. A platform team may need to discuss a migration with service
owners watching. A design group may need to expose tradeoffs to a broader
engineering community. A leadership group may need to model how it reasons
through constraints. The fishbowl lets the reasoning happen in public without
turning the conversation into a town hall.

But the fishbowl is not better for every problem. If the goal is to make a
decision, the format still needs governance. If the goal is to collect broad
feedback, an async RFC may be better. If the goal is psychological safety after
an incident, a fishbowl can be too performative unless trust already exists. The
point is not to praise one format. The point is to choose the format based on
the work the conversation has to do.

## Meetings are not one category

I find it useful to name the job before naming the meeting. Is the group trying
to decide, discover, align, teach, repair, or explore? Those verbs imply
different structures.

A decision conversation needs authority and a record. A discovery conversation
needs open questions and enough looseness for surprising information to appear.
An alignment conversation needs a shared artifact that people can point to
afterward. A teaching conversation needs a path from novice questions to expert
context. A repair conversation needs honesty, safety, and attention to harm. An
exploration conversation needs permission not to decide too early.

When the format and job mismatch, the meeting feels wrong even if the people are
doing their best. A planning meeting used for discovery creates fake
commitments. A design review used for teaching frustrates the author because the
feedback arrives too late. A broadcast update that pretends to be discussion
gives people the appearance of participation without changing anything. A retro
that never changes the next sprint becomes therapy without system learning.

The fix can be as small as saying the format out loud. "This is a fishbowl, so
the inner circle will reason through the tradeoff while the outer circle listens
for missing constraints." "This is a decision review, so comments are advisory
unless they come from the named owner." "This is discovery, so we are not
committing today." Naming the container prevents people from bringing the wrong
expectations into the room.

## Choose the container on purpose

Conversation formats are part of engineering infrastructure because they shape
how information moves. A team that only knows status meetings will turn every
problem into reporting. A team that only knows open discussion will struggle to
make decisions. A team that only knows async documents may miss the trust and
speed that live conversation can provide. Maturity is having several containers
and knowing when to use each.

This connects to
[Design Review Needs Governance](/blog/design-review-needs-governance/) because
design review is one conversation format that fails when its authority is
unclear. It also connects to
[There Is No Speedup for Shared Understanding](/blog/no-speedup-for-shared-understanding/)
because shared understanding is not produced by dumping information into a room.
It is produced by creating the conditions under which the right people can
exchange the right kind of context.

A small operating habit helps: before scheduling a meeting, write the desired
output and choose the format from that output. If the output is a decision,
define the decider. If the output is surfaced concerns, use a structure that
lets quiet concerns appear. If the output is shared reasoning, consider a
fishbowl. If the output is durable context, write first and meet second.

The original note only had one example, but I think the instinct was right.
Collaboration is not merely people plus topic. It is people plus topic plus
form. The form can hide information or reveal it, concentrate authority or
distribute it, create safety or remove it. That makes conversation formats
engineering tools. We should pick them deliberately.
