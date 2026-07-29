+++
title = "Spec-Driven Engineering Gets the Order Backwards"
date = "2026-07-29"
description = "Spec-driven development promises that a fully written design ahead of time will let an agent execute autonomously. I tried it and it backfired: an over-specified spec removes the room an agent needs to try different approaches. Working proofs of concept, built first and compared against each other, are what the spec should come from, not the other way around."
template = "blog-post.html"
[taxonomies]
categories = ["Engineering Systems"]
tags = [
  "agents",
  "spec-driven-development",
  "autonomous-agents",
  "proof-of-concept",
  "workflow",
  "waterfall",
]
[extra]
editorial_track = "engineering-systems"
+++

I was a believer in spec-driven development. The pitch is straightforward: write
down what you want ahead of time, completely, the way you would write a design
document, and the agent follows it like rails. Fewer surprises, more
predictability, a contract between what you asked for and what got built. I
wanted that contract badly enough that I built my workflow around it for a
while.

Then I watched what actually happens when the spec is detailed enough to guide
an agent through a full autonomous run. The spec has to commit to an
architecture, a set of dependencies, a shape for every component, before any of
that has been tested against real code. Writing all of that down does not remove
the guesswork, it just moves the guesswork earlier and hides it inside
confident-sounding prose. The document reads like a decision, but it is still a
hypothesis. Committing to it before anything has run is the same move a
waterfall plan makes: define the whole thing up front, then execute, and treat
any deviation as scope creep instead of information.

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

What has actually worked for me is close to the opposite order. Talk to the
agent long enough to land on a direction, not a full architecture, something
closer to a session-scoped plan than a design document. Then let it start
building toward a full proof of concept, not a fully finished product. It is
going to hit blockers. A dependency will not do what you assumed. A pattern that
sounded fine out loud will not survive contact with the actual code. When that
happens, the move is to let the agent flag the blocker and keep going, not to
have pre-specified the answer to a question you had not actually asked yet.

The end goal on a first pass is a working demo, not finished software. That
means there is real scaffolding to stand up and synthetic data to generate along
the way, and that is fine, because the point of this pass is to prove the shape
of the solution, not to ship it. Once that demo exists, commit it to its own
branch. Then you can say: now try a different approach. Maybe you did not like
an implementation detail. Maybe there is a dependency you would rather not
carry. Steer toward v2, v3, v4, each one a working, demoable branch, each one
disagreeing with the last in some concrete way you can actually point at.

Only after you have two or three of these, each an actual working solution
instead of a description of one, does it make sense to write the spec. At that
point the spec is not speculation, it is a summary of what already ran. It also
tends to reveal decomposition you could not have seen from the whiteboard: this
is not one thing, it is three components, and component two is the one that
needs the careful spec because that is where the branches actually disagreed.
Writing the spec after the demos exist means every claim in it is backed by code
that already executed, not by confidence about code that has not been written
yet.

There is a second effect worth naming, because it is not just about agent
autonomy: a spec is nearly impossible to argue against and a working demo is
nearly impossible to argue with. Send a ten-page design document to a group of
people and you will get ten pages of questions, most of them reasonable, some of
them just people finding their own footing in the discussion. Send a working
demo, even with mock data behind it, and the conversation changes shape. Nobody
can credibly say "this will not work" about code that is already running in
front of them. Working code is closer to a photograph than an argument: it does
not need to persuade anyone, it just is what it is.

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
combination, a clear test harness plus a genuinely open path to it, is what let
a fully autonomous, overnight run turn into a working solution instead of a
plausible-sounding one.

I still think alignment matters, and a loose plan going in is worth having:
something short enough that it reads more like "here is roughly what I am
thinking" than a committed design. But the moment that loose plan calcifies into
a fully specified document before any code has run, it stops being alignment and
starts being premature commitment, and premature commitment is just waterfall
wearing a newer name. The proof of concept is not a shortcut around the spec. It
is where the spec should have been coming from the entire time.

---

_This extends the workflow ideas in
[Why I Switched to Worklogs](/blog/why-i-love-worklogs/), where the session plan
and the durable design doc are already treated as different artifacts with
different lifetimes. The overnight, fully autonomous run described here rests on
the same rails discussed in [Fearless Engineering](/blog/fearless-engineering/):
confidence to let an agent run unattended comes from the guardrails around it,
not from a tightly specified plan._
