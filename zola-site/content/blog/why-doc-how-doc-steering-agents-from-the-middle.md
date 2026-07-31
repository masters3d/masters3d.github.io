+++
title = "The Why Doc and the How Doc: Steering Agents from the Middle"
date = "2026-07-31"
description = "Start with the code works for the software engineering circle of the Venn diagram, but a technical program manager naturally starts from the why, not the code. Once agents act like subordinates, the person steering them sits in the overlap and needs two documents: a Why doc facing outward toward the problem and stakeholders, and a How doc facing inward toward the agent's technical direction."
template = "blog-post.html"
[taxonomies]
categories = ["Engineering Systems"]
tags = [
  "context-as-code",
  "technical-program-management",
  "design-docs",
  "agents",
  "alignment",
  "leadership",
]
[extra]
editorial_track = "engineering-systems"
+++

I have written before about the
[Venn diagram between software engineering and technical program management](/blog/ten-thousand-hours-was-never-enough/):
one circle is deep technical execution, another is alignment and coordination,
another is strategic framing, and the overlap between them is getting more
valuable, not less. I did not fully follow that idea to where it actually leads,
so let me go deeper.

## Start with the code is engineering-circle advice

When I argue for building the proof of concept before the design document, or
for [treating context as code](/blog/context-as-code/) that gets distilled out
of what you built rather than written before it, that advice sits inside the
engineering circle. It assumes someone who can sit down and start typing, whose
natural entry point into a problem is the system: what would this look like if
it existed, what breaks first, what the shape of a working answer actually is.

That is not the natural entry point for a technical program manager, and it
never was. A TPM's job starts one layer up: what problem are we actually
solving, why does it matter to the business or the customer right now, what does
success look like before any component exists. Start with the code is fine
advice if code is where your instinct already lives. It is backwards advice if
your instinct lives in the why. Neither instinct is wrong. They are just
different entry points into the same overlap, and the industry does not have
great language yet for the fact that both need to feed the same autonomous
system.

## The agent turns you into a manager whether you wanted the role or not

Here is the part that changes the shape of the problem. An agent behaves like a
subordinate: it does not independently generate the reason the work matters, it
executes against whatever context it was given and asks for direction when the
context runs out. That makes the human steering it structurally a manager, even
if their title says engineer, even if they have never managed a person in their
life. And a manager's actual job, the part that is easy to forget when you are
heads-down inside a single repository, is standing in the middle of two
different audiences that speak different languages and need different documents.

One audience is outward: the stakeholders, the customer, the business context
that explains why this work exists at all. The other is inward: the system being
built, the technical constraints, the tradeoffs that only make sense to someone
who understands the code. A manager translates continuously between those two
directions. Miss the outward-facing translation and you build something
technically sound that solves the wrong problem. Miss the inward-facing
translation and you end up with a beautifully argued business case that no
agent, and frankly no engineer, can act on, because it never specifies a
boundary, a constraint, or a definition of done. Managing agents did not invent
this tension. It just removed the option of quietly skipping one side of it,
because the agent will not intuit the missing half for you the way a seasoned
engineer sometimes could.

## Two documents, not one, and neither is optional

This is where I think the Why doc and the How doc earn their place as distinct
artifacts rather than two sections of the same design document.

The Why doc faces outward. It exists to align stakeholders, leadership, whoever
is not going to read a line of the implementation, on the problem being solved
and why it matters right now. It carries the business rationale, the priority
against other work, the definition of the outcome in terms a non-engineer would
recognize as success. Its audience is people, and its job is persuasion and
alignment, not precision about mechanism.

The How doc faces inward. It exists to give the agent (and the engineers
reviewing the agent's output) the technical direction that turns the why into
something buildable: the architecture decision, the constraint that must hold,
the boundary the agent is not allowed to cross, the verification step that
defines when the work is actually done. Its audience is the system, human or
agent, that has to execute, and its job is precision, not persuasion.

Collapse these into one document and you get the failure mode every engineer has
lived through: a design doc that spends three pages justifying the business case
to people who already agreed to the project, then rushes the one paragraph that
actually specifies the technical boundary the whole implementation depends on.
Or the opposite failure, a document so thick with architecture diagrams that
nobody outside engineering can tell whether it solves the actual problem, so it
gets rubber-stamped instead of genuinely reviewed. Neither document does its job
when it is asked to do both jobs at once.

Keeping them separate is not extra process. It is the same discipline that makes
[context as code](/blog/context-as-code/) work at all: context is only
load-bearing if it is written for the reader who actually has to act on it. The
Why doc is context for the humans deciding whether this is worth doing. The How
doc is context for the agent (and the engineer supervising it) deciding how to
do it correctly. A technical program manager, working from the why outward, and
a software engineer, working from the code inward, are writing toward the same
overlap from opposite directions. The person steering the agent is the one
standing in the middle of that Venn diagram, and the two documents are what keep
that middle position from collapsing into "outward alignment with no technical
teeth" or "technical precision nobody upstream can evaluate."

---

_This extends the Venn diagram from
[10,000 Hours Was Never Enough](/blog/ten-thousand-hours-was-never-enough/),
where the overlap between engineering, coordination, and strategy was named but
not yet given its own artifacts. It also sits next to
[Context as Code](/blog/context-as-code/): the Why doc and the How doc are both
context, held to the same standard, just aimed at different readers on either
side of the middle._
