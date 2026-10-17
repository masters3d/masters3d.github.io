+++
title = "The Last 20% and the Next Nine"
date = "2026-10-15"
description = "The first 80% of a feature gets the demo, the congratulations, and the promotion packet. The last 20% (the part that makes the thing actually usable) costs a magnitude more and is rewarded far less. The reason is structural: every additional nine of reliability is a different engineering problem than the one before it, and you cannot reach it by extending a design that was never built for it. In the age of AI, when the token cost of writing the scalable version is roughly the token cost of writing the disposable one, the V1-then-rewrite habit deserves a second look."
template = "blog-post.html"
[taxonomies]
categories = ["Software Engineering"]
tags = [
  "reliability",
  "nines",
  "architecture",
  "rewrites",
  "incentives",
  "shift-left",
  "quality",
  "agents",
  "systems-thinking",
]
[extra]
editorial_track = "software-engineering"
+++

The pattern I have watched repeat, in more than one team and more than one
company, goes like this. Somebody has an idea, builds it fast, and demos it. It
works. There are congratulations, a thread full of celebration emoji, a mention
in the review packet. The feature is maybe 80% there, which at demo time is
indistinguishable from done. Then people start using it, and the remaining 20%
turns out to be where the actual engineering lives: the error paths, the
concurrent case, the migration, the thing that happens on the second Tuesday of
the month. Closing that 20% takes longer than the first 80% took. And the
closing is almost never rewarded at the same level as the demo was.

That asymmetry bothered me for a long time because I read it as an incentive
problem, which it partly is. But the more interesting half is that it is also a
measurement problem. The first 80% and the last 20% are described with the same
unit (percent of a feature) when they are not the same kind of work at all.
Percent complete implies the remaining work is the same work, just less of it.
It is not. The honest unit is reliability, and reliability is counted in nines.

## Each nine is a different engineering problem

Going from "it works when I run it" to 90% (one nine) is mostly finishing. You
handle the obvious failures, you write the retry, you fix the three bugs the
first users find. Going from 90% to 99% is different: now you are touching code
you already shipped. In my experience you cannot reach the next nine by adding
to the edges; you end up revisiting something like half of what was delivered,
because the assumptions that made the fast version fast are exactly the ones
that fail under the next class of load or failure. Each nine after that costs
more than the one before it, and at some point the cost stops being effort and
becomes architecture. You are not improving the system anymore. You are
replacing it.

That is the part I want to state plainly, because it is the part that gets
discovered late: past a certain point, another nine requires a different design,
not a better version of the current one. The number of nines you can reach is
decided at design time, by the choices that determine whether state can be
recovered, whether work is idempotent, whether a single machine is in the path,
whether the data model can be migrated without downtime. One nine is achievable
almost by accident. Two is work. Three starts demanding real design intent. Four
and five are a different discipline, and they are mostly unreachable by
incrementing a design that was written on the assumption that nothing would go
wrong. Whatever ceiling the original design set, the team hits it and then
spends quarters pushing against it.

So the design question is not "will this work?" It is "how many nines is this
shape capable of?" If the answer is one and the requirement is three, the
rewrite is not a risk; it is already scheduled, it just has not been put on the
calendar yet. Naming that at the start is cheap. Discovering it two years in,
after the thing is load-bearing for real customers, is the most expensive way to
learn it.

## The reward curve runs opposite to the cost curve

Here is where the structural part meets the human one. The cost per nine rises.
The reward per nine falls. Somebody shipping the first 80% of a new feature gets
visible credit for new capability. Somebody spending two quarters taking a
system from two nines to three produces no new capability at all, which is the
entire point of the work, and has nothing to demo. Meanwhile other people are
shipping their own first 80%, accumulating the visible wins, and moving up. The
engineer doing the rigor that makes the product dependable in the long term is
doing the work that keeps the company's promises, and that work is described
with a diminishing phrase: maintenance.

I do not think most of this is anybody acting in bad faith. It is what gets
measured. A demo is legible to everyone in the room in thirty seconds. An
absence of incidents is legible to nobody. This is the same shape as
[glue work](/blog/minimize-humans-as-glue/): a person absorbing a cost the
system should have handled, in a form the system cannot see. The fix is not to
ask people to admire maintenance more. It is to make the hard part visible as
engineering with its own stated goal, so that "we took the checkout path from
99% to 99.9% and here is the design change that made it possible" is a result
with a name, not an unexplained gap in someone's quarter.

There is also an honest version of the reward asymmetry that is worth
preserving. Not everything should reach three nines. An internal tool used by
four people and an experiment that might be deleted next month do not deserve
the rigor, and demanding it everywhere is its own failure mode. The problem is
not that we ship 80% versions. It is that we ship them without ever deciding
which ones are allowed to stay at 80%, and then the ones that quietly became
load-bearing never get reclassified.

## V1-then-rewrite was a cost calculation, and the cost changed

The usual defense of shipping the disposable version is sound, and I have made
it myself: you do not know what will work, so build the cheap thing, find out,
and rewrite it once it earns the investment. Dropbox ran on Python far longer
than anyone expected and only moved pieces to other languages when the scale
problem was real and specific. That is the startup case, and in the startup case
it is correct. The rewrite is paid for by the information you bought.

What I am less sure about now is the premise underneath it, which is that the
scalable version costs meaningfully more to write than the disposable one. That
was true when the cost was measured in engineer-months. With agents doing a
large share of the authoring, the cost I actually spend is closer to tokens and
review attention, and the token cost of producing the version in a scale-capable
language and framework is not far off the token cost of producing the version in
whatever was fastest to type. I am not arguing for C++ reflexes or for building
distributed infrastructure before there is a user. I am arguing that when the
delta has shrunk this much, "write the throwaway first" should be a decision
with a reason behind it rather than a default, because the throwaway has a way
of becoming the thing real customers depend on.

The field that keeps the most code alive is a useful check on this. Financial
systems written decades ago are still running, and I do not believe they were
written with a planned rewrite in five years. They were written as if the choice
would have to hold, and the choice held. What is happening now is that instead
of rewriting the logic, the industry builds compilers and translation layers to
carry it forward, which tells you what the durable asset was: the logic, not the
runtime it was first expressed in. I find that a better model than the serial
rewrite. Invest in the expression of the logic, keep it portable, and let the
tooling move it. That is the same bet I described when keeping
[one core across languages](/blog/sharing-one-core-across-languages/): the
durable thing is the shared logic, and everything around it is replaceable.

## Shift the nines left

If each nine is a design property rather than a polish phase, then the lever is
where quality gets decided, not how hard it gets inspected later. Quality
checked by a human reading a diff is the weakest possible placement, because it
is judgment applied once, by someone who cannot execute every path in their
head. The stronger placement is mechanical and early: the invariants the design
must satisfy, expressed as something that runs. This is what
[front-loading the validation environment](/blog/shift-left-synthetic-environments/)
buys, and it is why
[building proofs of concept first](/blog/spec-driven-engineering-poc-first/) is
more useful than specifying up front, as long as what the proof of concept
proves includes the failure behavior and not just the happy path.

The practical form is short. Before the first commit, state the target: how many
nines does this need to reach if it succeeds, and what in this design makes that
number reachable. Then state the ceiling you are accepting: the specific
property that caps it, so the next person knows what has to change and does not
spend a quarter discovering it. If the target and the ceiling do not match, you
have chosen a rewrite, and that is a legitimate choice as long as it is written
down and the organization knows it bought one.

---

_What I keep returning to is that "80% done" is a measurement that hides the
shape of the remaining work. The last 20% is not the same work at lower volume;
it is the work of moving a system from one reliability class to the next, and
each class is a different engineering problem with a cost that rises while the
recognition falls. Naming the target number of nines at design time converts an
argument about effort into an argument about architecture, where it belongs. The
rest is placement: decide quality early and mechanically, the way
[fearless engineering](/blog/fearless-engineering/) depends on rails built
before anyone needed them, and record the decision where the next person can
find it as [context as code](/blog/context-as-code/)._
