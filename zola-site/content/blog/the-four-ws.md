+++
title = "The Contextual Core: Who, What, When, Where"
date = "2026-10-05"
description = "Why is the directive and How is the action, which leaves out the entire middle. Who, What, When, and Where are the locating step: four separate questions, each with its own failure mode, that tell you where you are standing before you move. Splitting them out of the How is what makes the whole model work."
template = "blog-post.html"
[taxonomies]
categories = ["Quest Engine"]
tags = [
  "quest-engine",
  "five-ws",
  "search-drive-renew",
  "context",
  "contextual-awareness",
  "shift-left",
  "triads",
]
[extra]
editorial_track = "quest-engine"
series = "quest-engine"
+++

Most work starts at How. Somebody describes a problem, somebody opens an editor,
and the first real artifact is an attempt at a solution. The usual correction is
"start with why," which is good advice and incomplete, because there is a whole
step between the directive and the action that neither word covers.

[Why is the Primary Directive](/blog/the-objective-function/). It tells you what
counts as better. [How is the action](/blog/quest-engine-introduction/). It is
where the work gets done. In between sits the step that tells you **where you
are standing**, and it has four parts: **Who, What, When, Where.**

This is the Contextual Core, and it is the searching force
([Search, in the triad](/blog/quest-engine-the-why/)). It is also the step
people skip most reliably, because skipping it does not feel like skipping
anything. The directive is clear and the work is obvious, so you start. Four
weeks later it turns out the thing was for a team you never spoke to, or it
needed to exist by a date nobody said out loud, or it had to live in a system
that cannot host it. None of those is a How failure. All of them are a locating
failure, and all four have a different question attached.

## Why They Have to Be Split Out of the How

The reason these four normally live inside the How is that each one eventually
shows up as an implementation detail. Who the users are becomes an interface
decision. What exactly is being built becomes a scope cut. When it ships becomes
a sequencing decision. Where it runs becomes a deployment target. Because they
all surface as decisions during execution, they get treated as part of
execution.

They are not. **Each of the four is a question about reality that has a true
answer independent of what you build.** The users exist whether or not you
identified them. The deadline exists whether or not anyone said it. The
constraint of the surrounding system exists whether or not you checked. Deciding
is a How activity. Finding out is not, and conflating the two means you find out
by deciding wrong first.

The other reason to split them out is that **they are the part you can actually
delegate.** An agent cannot issue your directive and should not be unsupervised
on consequential execution, but crawling a codebase to find every caller, pulling
the calendar constraints, mapping which services a change touches, and listing
who has opinions is exactly the work agents are good at. If the four Ws stay
buried inside the How, that leverage is invisible. Pulled out, they are a
well-defined, highly delegable step with a clear completion condition.

## The Four Questions

Each of the four has its own question, its own completion test, and its own
distinctive failure. They are not a checklist to recite; they are four different
kinds of being lost.

**Who — who is this for, and who else has a stake?** The question covers users,
the people who maintain it afterwards, whoever has veto power, and whoever gets
surprised if it changes. The completion test is that you can name them, not
describe them in the abstract ("the users" is not an answer). The failure mode is
building for an imagined person: technically sound work that nobody specific ever
asked for, discovered at the review where someone real finally reads it.

**What — what exactly is the thing, and what is explicitly not it?** The
boundary matters more than the description. Most "what" answers are too vague to
disprove, and a scope that cannot be disproved cannot be finished. The completion
test is that you can state what is out of scope and have someone disagree with
you. The failure mode is scope that quietly grows because it was never fenced,
which reads as slowness and is actually ambiguity.

**When — what is the actual timing, and what does it depend on?** Not only the
deadline but the ordering: what has to exist first, what is waiting on this, what
window closes if you miss it. The completion test is knowing what breaks if this
lands a month late, specifically. The failure mode is correct work delivered into
a moment that has already passed, which is the most demoralizing way to be right.
([Timing is its own subject.](/blog/quest-engine-timing-momentum-resonance/))

**Where — where does this live, and what does it touch?** The system, the
codebase, the team, the layer of the stack, the surrounding constraints you did
not choose. The completion test is being able to draw the boundary and name what
is on the other side of it. The failure mode is the integration surprise: a
component that is correct on its own and cannot be installed anywhere.

Four questions, four different ways to be wrong, and no amount of being right on
three covers for being wrong on the fourth. That is the argument for giving each
one its own bullet instead of collapsing them into "gather context." "Gather
context" has no completion condition. These four do.

## The Directive Is What Bounds the Search

Without a directive the four Ws are unbounded. Who? Everyone with an opinion.
What? Anything adjacent. When? No particular time. Where? Every system it
touches, transitively, forever. The search does not terminate, and what that
feels like from the inside is not ignorance but overwhelm. Plenty of
information, no way to tell which of it matters.

The directive supplies the filter. **Who matters is who matters _to the
directive_.** What is in scope is what the directive would rank as better. The
deadline that counts is the one the directive cares about. This is why Why has
to be answered first and not just stated first: an unanswered directive produces
a search with no edges, which is the most common form of "we spent two months in
discovery."

It also gives the step a real stopping rule, which is the thing most
context-gathering advice lacks. **You are done locating when you can predict
what the directive would say about each of the four answers.** Not when you have
read everything. When more information would not change the ranking.

## Then, and Only Then, How

With the directive answered and the four Ws located, How becomes a much smaller
and much better-posed problem. Most of what makes execution hard is not technical
difficulty; it is executing against unknowns that were knowable. A How step that
begins after the locating step is finished is mostly craft, which is the part
that is actually enjoyable and the part agents can help with most.

This is a [shift-left](/blog/shift-left-synthetic-environments/) move in the
plainest sense: the cost of a wrong answer rises the further right you find it.
A Who you got wrong costs a conversation during the locating step and a rewrite
during the How. The order **Why → Who/What/When/Where → How** is not ceremony.
It is paying for information at the point where it is cheapest.

Then the cycle closes: you execute, the execution produces evidence, and the
evidence is what the directive gets audited against before the next cycle starts.
How the three steps fold back into each other, and why the labels for "before"
and "after" move around depending on which step you are standing in, is the
subject of [the meta post](/blog/the-meta-structure/).

---

_The Contextual Core is the Search force of the
[Quest Engine](/blog/quest-engine-introduction/), expressed as the four question
words that are not Why. It follows the
[Primary Directive](/blog/the-objective-function/) and precedes the
[action phase](/blog/quest-engine-introduction/). For the underlying pillar, see
[Contextual Awareness](https://github.com/masters3d/ingenio/tree/main/pillars)
in the ingenio repository._
