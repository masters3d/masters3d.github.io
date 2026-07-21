+++
title = "Shift Left Until the PR Is Just a Confirmation"
date = "2026-07-10"
description = "Agentic tooling made pull requests cheap and plentiful, so the bottleneck moved from writing code to trusting it. The answer is not another review loop but front-loaded rigor: invest the engineering effort ahead of time to build a full, production-shaped synthetic environment you run locally, so that validation itself becomes cheap and the PR turns into a context-sharing mechanism instead of an approval gate. Tools like .NET Aspire and Dapr show what that inner loop can look like, and the same principles carry over to homegrown systems."
template = "blog-post.html"
categories = ["engineering", "workflow", "ai"]
tags = ["shift-left", "testing", "synthetic-environments", "digital-twin", "ci-cd", "developer-velocity", "agents", "contract-testing", "dapr", "aspire", "systems-thinking"]
+++

I have been watching my own pull request queue change shape over the last year.
It used to be that writing the change was the slow part and review was a quick
nod at the end. Now the ratio has flipped. Agents help me produce changes faster
than anyone can read them, so more pull requests land in the queue than ever,
and the queue backs up not at authoring but at review. The bottleneck moved. If
code is cheap to produce, the scarce thing is no longer the code. It is the
trust that the code is correct. So the question I keep chasing is this: how do
we make a change cheap to trust, not just cheap to write?

The reflexive answer floating around is to point another agent at the pull
request and have it review. That helps at the margins, and I use it, but I do
not think it is the main move. A reviewing agent gives you an opinion, and an
opinion (human or synthetic) is a probabilistic thing. What actually earns trust
is proof: an environment that demonstrates the behavior of the change by running
it. The reframe I keep coming back to is about where the engineering effort
should go. Instead of spending it in the review cycle (making PRs move faster,
adding another reviewer, tuning the queue), spend it ahead of time building the
environment that validates the change. Once that full end-to-end validation
exists, the cost flips: running it is cheap, and reviewing a change that has
already been verified is cheap too, because the hard proof is already done by
the time anyone looks.

## The review bottleneck is a trust problem

There are only two ways to believe a change is safe. You can form a judgment
about it, or you can watch it run and prove it. Judgment is what a reviewer does
when they read a diff and reason about what it probably does. Proof is what an
environment does when it executes the change against real pathways and shows you
the result. Judgment scales badly (it is bounded by human attention, and a
second agent giving an opinion does not remove that bound, it just adds another
opinion). Proof scales differently: it is front-loaded. Compute is not free and
it is not getting cheaper, so the win does not come from throwing more of it at
the problem. It comes from paying the construction cost once (building the
synthetic environment) and then running it as many times as you like for very
little. The rigor lives in the environment, not in the individual run.

The analogy I keep reaching for is a mathematical proof. The statement can be a
single line, but the proof behind it runs for pages, and it is the pages that
make the one line trustworthy. A validated change is the same shape. The diff is
short, but the rigor that makes it safe (every path exercised, every dependency
stood up, every real scenario replayed) is long, and it belongs in front of the
pull request, not inside it. Building that proof machinery is the priority. Once
it exists, the statement it certifies becomes cheap to accept.

Shift left is usually said as a direction: move testing earlier. I want to say
it as a rule, because a direction with no ceiling is a trap. Pushing everything
left has a cost, since the more your local setup mirrors production, the heavier
and slower it gets, and that weight fights the velocity you were trying to buy.
So the rule is narrower than "test earlier." Shift left the validation that is
cheap to run locally and expensive to discover in production. That is the
validation worth pulling all the way back to the inner loop: not just unit tests
(those already run everywhere) but the integration and end-to-end pathways that
today only light up after the pull request, in a pipeline, in a staging
environment you share with everyone else. A normal PR validation pipeline runs
unit and integration tests but almost never a full end-to-end scaled
environment. The goal is to make that environment cheap enough to run that it
can move all the way left into the local inner loop, and cheap enough that it
can even run as part of PR validation.

The payoff is not abstract. The cost of a defect scales roughly with how late
you catch it (a bug caught in the local inner loop costs minutes, the same bug
caught in production costs an incident, a rollback, and a postmortem). Every
rung you move validation earlier is a strict reduction in that cost. And there
is a second payoff that matters just as much: when the full gate has already run
locally, the pull request stops being the approval mechanism. It becomes a
context-sharing mechanism, a place where other people learn what changes are
coming, rather than the gate where correctness is decided for the first time.
The gate has moved all the way left.

## The ladder of fidelity

Here is the concrete version of what I want. Say I have three services (A, B,
and C) and I am only changing B. I should be able to stand up an environment on
my own machine where A and C are present, make my change to B, and see exactly
how it ripples through to A and C, before I open anything. The catch is that "A
and C are present" hides a whole spectrum, and collapsing that spectrum is where
most conversations about this go wrong.

There is a ladder of fidelity, and each rung trades cost for trust. The bottom
rung is mocking A and C (fast to stand up, cheap to run, but it only proves your
change against your assumptions about the neighbors). The middle rung is running
A and C as real processes in containers with seeded data (slower and heavier,
but now you are exercising the actual code of your dependencies). The top rung
is replaying recorded production traffic through the real neighbors (the highest
fidelity, because the scenarios are ones that genuinely happened, and the
highest cost to capture and maintain). Fidelity, cost, and trust all rise
together as you climb. The skill is choosing the right rung for the change in
front of you, not always reaching for the top.

This is where .NET Aspire and Dapr are worth studying, because between them they
show what a serious local inner loop looks like. Aspire is the orchestrator. It
models your infrastructure dependencies (the databases, the caches, the message
brokers) in type-safe application code instead of a sprawl of compose files,
generates and injects the connection strings and ports automatically, and spins
up a local dashboard that gives you distributed traces, structured logs, and
metrics across every service out of the box (the kind of control-plane
visibility you normally only get in production). Notably, the model it pushes is
a lightweight orchestrated graph of containers with a control plane, not a full
local Kubernetes cluster. That is the right instinct. You want production shape,
not production weight, in the inner loop.

Dapr is the complement, and it attacks the portability half of the problem. By
running as a sidecar that your service talks to over local HTTP or gRPC, it lets
your business logic stay agnostic about the infrastructure underneath (a local
Redis pub/sub queue in your inner loop and a production cloud queue become a
one-file swap, with the application code untouched). That is precisely what
makes a local synthetic environment honest: the code path you exercise on your
laptop is the same code path that runs in production, because the only thing
that changed is the sidecar's configuration. It is also polyglot by
construction, so a Python service, a Go backend, and a Node web app can share
state and call each other locally through the same building blocks, which is
what my A/B/C example actually looks like in a real system.

Most systems are not built on Aspire or Dapr, and that is fine, because the
principle is what transfers, not the tooling. The homegrown version of this is a
discipline: every external resource your service touches (the database, the
relay, the pub/sub, the cache, the object store) must have a local stand-in that
behaves like the real thing. A container running the same database engine with
seeded schema, an in-memory or containerized broker for the queue, a fake for
the object store that speaks the same API. The point is to remove every reason
you would otherwise have to deploy in order to test. "Deploy to test" is the
mess this is trying to end. The moment testing a change requires pushing it to a
shared environment, you have lost the inner loop, you are serializing on
infrastructure other people also need, and you have made validation expensive
again. Modeling all of those resources locally is the homegrown path to the same
cheap, repeatable proof that Aspire and Dapr hand you out of the box.

## The hard part is the data (and keeping it honest)

The moment you climb toward the top of the fidelity ladder, you hit the real
problem, and it is not orchestration. It is data. "Replay real customer
scenarios" is the crux of the whole idea and also a minefield, because real
customer data carries real privacy, compliance, and personally identifiable
information obligations. You cannot just copy production into your laptop. So
the mechanism matters: capture production traffic and sanitize it, generate
synthetic data that preserves the statistical shape of the real thing without
the sensitive contents, and lean on contract tests to pin the boundaries between
services so the replayed interactions stay valid. The goal is a recording of
what happened that is safe to replay, not a copy of who it happened to.

The second hard part is drift, and it is the one people forget. A synthetic
environment that quietly diverges from production is worse than no environment
at all, because it hands you false confidence (you prove your change against a
world that no longer exists and ship the bug anyway). So fidelity has to be
owned. Contract tests are the parity guarantee, sampled production traffic is
the honesty check, and the environment has to be treated as a living system that
heals and monitors itself rather than a fixture someone set up once and forgot.
This is the same principle I keep landing on: build systems that keep themselves
correct, and reserve human attention for the genuinely novel case. An
environment you have to babysit is just another human standing in a seam.

None of this removes the value of rolling changes out safely once they land.
Progressive delivery, canaries, and feature flags all still matter. My argument
is that we have poured enormous effort into making the right of the pipeline
safe (how to roll out a change carefully after it merges) and comparatively
little into making the left of it provable (how to know the change is right
before it merges). The synthetic environment is how you rebalance that, by
pulling the proof all the way back to the moment before the pull request exists.
It also does something specific for agents: an agent is stochastic, and its
output is unpredictable by nature, but a deterministic validation scheme wrapped
around it makes the outcome predictable again. You cannot make the agent
certain, but you can make the gate certain, and that is enough. The environment
turns "the agent probably got it right" into "the change passed every path,"
which is the difference between a guess and a proof.

---

_The point is not to review harder, it is to arrive at the pull request with the
validation already done, so the review stops being the gate and becomes a place
to share context (a way for other people to learn what changes are coming)
rather than the first place anyone finds out whether the change works. That
reframes the whole velocity-versus-quality trade: the two stop fighting once the
rigor is front-loaded into an environment instead of spent in the review cycle.
This is the [self-healing systems](/blog/minimize-humans-as-glue/) idea applied
to validation, the
[proof-over-opinion](/blog/bicycle-of-the-mind-fast-slow-agents/) distinction
applied to review, and the reason
[fearless engineering](/blog/fearless-engineering/) is possible at all: you move
fast because the rail was built before you needed it, and the context that makes
the environment reproducible is itself
[context as code](/blog/context-as-code/)._
