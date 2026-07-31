+++
title = "Verification-Driven Development: Let Proofs of Concept Write the Spec"
date = "2026-07-29"
description = "Spec-driven development is a vague enough term that it can mean anything from a paragraph of intent to a fully waterfalled design. I tried the fully-specified version and it backfired: it left no room for an autonomous agent to explore alternatives. What worked instead was naming the actual sequence. Build multiple proofs of concept, verify each one against something real, and only then write the design document, informed by what the proofs of concept actually showed."
template = "blog-post.html"
[taxonomies]
categories = ["Engineering Systems"]
tags = [
  "agents",
  "verification-driven-development",
  "autonomous-agents",
  "proof-of-concept",
  "definition-of-done",
  "workflow",
  "waterfall",
]
[extra]
editorial_track = "engineering-systems"
+++

I was a believer in spec-driven development, and I still think the instinct
behind it is right. The trouble is the term itself does not mean one thing.
Sometimes it means a paragraph of intent shared before starting. Sometimes it
means a fully waterfalled design document that specifies architecture,
dependencies, and every component before a line of code exists. I built my
workflow around the second version for a while, wanted the contract it promised,
an agent that follows the design like rails, badly enough to ignore how vague
the label actually was.

Then I watched what happens when the spec is detailed enough to guide an agent
through a full autonomous run. The spec has to commit to an architecture, a set
of dependencies, a shape for every component, before any of that has been tested
against real code. Writing all of that down does not remove the guesswork, it
just moves the guesswork earlier and hides it inside confident-sounding prose.
The document reads like a decision, but it is still a hypothesis. Committing to
it before anything has run is the same move a waterfall plan makes: define the
whole thing up front, then execute, and treat any deviation as scope creep
instead of information. That is the version of spec-driven development I no
longer trust, and the vagueness of the term is part of the problem: it lets a
genuinely useful design document and a prematurely fully-specified plan hide
under the same name.

## An over-specified spec removes the room to explore

The actual cost only shows up once the agent starts working. If the spec is
tight enough to fully constrain the build, it is also tight enough to prevent
the agent from trying more than one approach to the problem you are solving. You
lose the thing autonomous execution is supposed to be good at: spinning up
several candidate solutions and letting you see which one is actually good,
instead of committing to the first idea that sounded right in a planning
conversation.

This matters more, not less, the more autonomous you want the run to be. A tight
spec plus a fully autonomous agent is close to a worst case: nobody is in the
loop to notice that the constraint was wrong, and the agent has no permission to
route around it. It will follow the rails straight into a wall a looser brief
would have let it walk past.

## Build the proof of concept, let the spec come out the other end

What has actually worked for me is close to the opposite order, and I want to be
precise about the vocabulary here, because I have been sloppy about it myself. I
have been saying "demo" when I meant proof of concept, and the distinction
matters. A demo is something you show. A proof of concept is something you build
to find out whether an idea survives contact with real code, and that is the
more important thing to name at this stage. The value of a proof of concept is
not that it is presentable, it is that it validates (or kills) an approach
before you have committed a design document to it, and that you can spin up more
than one in parallel to explore genuinely different alternatives instead of
committing to the first idea that sounded right in a planning conversation.

Talk to the agent long enough to land on a direction, not a full architecture,
something closer to a session-scoped plan than a design document. Then let it
start building toward a full proof of concept, not a finished product. It is
going to hit blockers. A dependency will not do what you assumed. A pattern that
sounded fine out loud will not survive contact with the actual code. When that
happens, the move is to let the agent flag the blocker and keep going, not to
have pre-specified the answer to a question you had not actually asked yet.

The end goal on a first pass is a working proof of concept, not finished
software. That means there is real scaffolding to stand up and synthetic data to
generate along the way, and that is fine, because the point of this pass is to
prove the shape of the solution, not to ship it. Once that proof of concept
exists, commit it to its own branch. Then you can say: now try a different
approach. Maybe you did not like an implementation detail. Maybe there is a
dependency you would rather not carry. Steer toward v2, v3, v4, each one a
working proof of concept on its own branch, each one disagreeing with the last
in some concrete way you can actually point at.

Only after you have two or three of these, each an actual working solution
instead of a description of one, does it make sense to write the design
document. I want to be clear that I am not arguing against specifications. A
design document is genuinely useful: it communicates intent, and it can lay out
the different approaches you actually tried, the trade-offs between them, a
barbell of options considered rather than a single path presented as inevitable.
What changes is when you write it. At this point the design document is not
speculation, it is a summary of what already ran. It also tends to reveal
decomposition you could not have seen from the whiteboard: this is not one
thing, it is three components, and component two is the one that needs the
careful spec because that is where the proofs of concept actually disagreed.
Writing the design document after the proofs of concept exist means every claim
in it is backed by code that already executed, not by confidence about code that
has not been written yet.

There is a second effect worth naming, because it is not just about agent
autonomy: a design document is nearly impossible to argue against and a working
proof of concept is nearly impossible to argue with. Send a ten-page design
document to a group of people and you will get ten pages of questions, most of
them reasonable, some of them just people finding their own footing in the
discussion. Send a working proof of concept, even with mock data behind it, and
the conversation changes shape. Nobody can credibly say "this will not work"
about code that is already running in front of them. Working code is closer to a
photograph than an argument: it does not need to persuade anyone, it just is
what it is.

## Verification is the part that actually matters

If there is one piece of this I would put above all the others, it is this: the
proof of concept is only as good as what you can verify it against. A proof of
concept that "looks right" is not much better than a spec that "sounds right,"
they are the same unverified confidence wearing different clothes. What makes
the proof of concept trustworthy is a strong, specific verification sequence the
agent can run against itself: real data where you have it, real use cases where
you do not, and a definition of done that is a check, not a description. "Send a
message and receive it back through this import path" is a definition of done.
"Implement a robust pop-up service" is not, no matter how carefully you specify
robust.

Get the verification step solid first, before worrying about how tight the spec
should be. Once an agent can check its own work against something real, the
exact shape of the plan matters much less, because the agent can explore, fail,
and correct itself without you in the loop catching every wrong turn. Without
solid verification, even a loose plan is dangerous, because there is nothing to
catch the agent when it convinces itself something works when it does not.

This is also where a good amount of the token spend and context actually goes,
and it is worth being deliberate about it: build the scaffolding that lets
verification happen locally, inside the agent's own loop, rather than depending
on a slow, external, or manual check. A local test suite, a seeded database with
real or realistic data, a script that replays an actual use case end to end,
these cost time to build once and then pay for themselves every single
iteration, because the agent can run them itself, as many times as it needs,
without spending a round trip (or a chunk of context) waiting on you. The
alternative, where verification only happens when a human looks at the result,
is slow in exactly the way that kills a long autonomous run: the agent either
stalls waiting for you, or worse, it keeps going without ever actually checking
whether it is right.

## Give the agent a test to run toward, not a plan to follow

The version of this that actually earned my trust was a session I set running
overnight against a component I needed: a pop-up service and a way for other
parts of the system to send and receive messages through it. I did not write a
spec for the internals. I gave it a target and a test: here is the library, here
is a test file, do not stop until you can send and receive a message through it,
using this import path, in this environment. That is a boundary I could verify
mechanically, not an architecture I had to guess at ahead of time. It ran
overnight and came back with something working in the morning.

That is a stronger contract than a spec, and it does not have the same failure
mode. A spec constrains the shape of the answer before you know if the shape is
right. A test constrains the definition of done and leaves the shape open. The
agent still has room to try things, fail, back out, and try again, all the
behavior that a tight spec would have foreclosed, but it cannot wander away from
the goal, because the goal is something it can check against itself. That
combination, a clear, locally runnable verification harness plus a genuinely
open path to it, is what let a fully autonomous, overnight run turn into a
working solution instead of a plausible-sounding one.

I still think alignment matters, and a loose plan going in is worth having:
something short enough that it reads more like "here is roughly what I am
thinking" than a committed design. But the moment that loose plan calcifies into
a fully specified document before any code has run, it stops being alignment and
starts being premature commitment, and premature commitment is just waterfall
wearing a newer name. The proof of concept, checked against a real verification
step, is not a shortcut around the design document. It is where the design
document should have been coming from the entire time.

---

_This extends the workflow ideas in
[Why I Switched to Worklogs](/blog/why-i-love-worklogs/), where the session plan
and the durable design doc are already treated as different artifacts with
different lifetimes. The local, self-checking verification loop described here
rests on the same rails discussed in
[Fearless Engineering](/blog/fearless-engineering/): confidence to let an agent
run unattended comes from the guardrails around it, not from a tightly specified
plan._
