+++
title = "Five Levels of Agent Capability"
date = "2027-06-19"
description = "\"Agent\" now decides what gets write access, memory, and a place in CI, yet it names almost nothing. A five-level ladder, from reactive to cognitive, turns the word back into an engineering claim about state, permissions, and how much validation a system needs."
template = "blog-post.html"
[taxonomies]
categories = ["Software Engineering"]
tags = ["agents", "ai-development", "systems-thinking", "validation", "software-engineering"]
[extra]
scheduled = true
editorial_track = "software-engineering"
related = ["cognitive-continuous-integration-and-the-broken-agent-loop", "software-3-0-needs-engineering-not-magic", "agents-are-taking-the-drive"]
+++

In August 2025 I ran an agent whose design notes called it cognitive. Its
[README](https://github.com/masters3d/ingenio/blob/main/cognitive_systems/README.md)
placed it on a five-level ladder that ended in self-awareness and autonomous
goal generation. The bugs I actually spent my time on were much lower on that
ladder: it picked up work it should have skipped, it raced its own previous run,
and it mixed its working notes into its deliverables. The
[full story of that agent](/blog/cognitive-continuous-integration-and-the-broken-agent-loop/)
is about its missing purpose. This post is about the ladder, because I think the
ladder is the part worth keeping.

The reason to care is simple: the word "agent" now decides what software
engineers ship, and it tells us almost nothing. A script that answers one
command, a coding assistant that plans across files, and a workflow that
remembers prior runs all get called agents. The same noun hides very different
engineering obligations. Call something an agent and someone will give it
repository write access, a memory store, or a place in CI. Whether those are
safe depends on which kind of agent it really is.

## Why the Level Is an Engineering Decision

Every older discipline in software already has this kind of vocabulary. We do
not ask whether a database is "smart." We ask what consistency it promises, what
state it keeps, and what happens on failure, and the answer decides how we test
it, back it up, and operate it. Agents need the same treatment. The level of an
agent is a claim about state and permissions, and every claim about state and
permissions is a claim about testing, reproducibility, review, and rollback.

Get the level wrong in one direction and you trust a system more than its
validation supports: a planning assistant with production credentials, or a
learning system tested like a pure function. Get it wrong in the other direction
and you wrap simple automation in ceremony it does not need. Both are ordinary
engineering mistakes with familiar costs, outages on one side and wasted effort
on the other.

The generated ladder in those design notes describes agents moving from reactive
behavior to deliberative planning, learning, meta-learning, and finally a
cognitive system. I do not read that as a report of a finished platform. I read
it as a proposed vocabulary for one narrow question: what is this system allowed
to remember, change, and decide?

## The First Two Levels Still Look Like Software

A reactive agent responds to a direct command. It has no durable memory and no
learning loop. Most automation lives here. It can still be valuable, but the
safety model is familiar: constrain the input, constrain the output, test the
behavior, and keep the blast radius small.

A deliberative agent adds planning and short-term context. It can break a
request into steps, reason about order, and adjust while the session is active.
This is where many coding tools already feel different from scripts. The system
does not merely run a command. It carries a temporary model of the task.

The design proposal treats this as a capability increase, and that is fair. The
practical engineer's addition is that temporary planning creates temporary
failure modes. A bad plan can touch several files before a test fails. A
half-remembered constraint can survive long enough to guide the wrong edit. At
Level 1, validation has to follow the plan, not just the final diff.

That was one lesson from the agent I described at the start, which ran from a
[GitHub Actions workflow](https://github.com/masters3d/ingenio/blob/main/.github/workflows/cognitive-issue-processor.yml)
in my notes repository. The useful work did not come from declaring an agent
cognitive. It came from ordinary boundaries: process only explicitly labeled
issues, exclude pull requests, separate session traces from deliverables, and
make repeated runs safe. The capability label mattered less than the guardrails
around the loop.

## Learning Changes the Contract

The third level in the design is a learning agent. It improves over time,
recognizes patterns, and accumulates experience. This is where the vocabulary
gets tempting and dangerous. Improvement sounds positive, but an engineered
system has to say what counts as improvement and who verifies it.

A learning agent is not just a better assistant. It is a system with state that
can affect future behavior. That state might be a worklog, a memory store, a
strategy ranking, or a set of preferences. Once that state exists, it needs
ownership. Can a human inspect it? Can a mistaken lesson be removed? Can one
project inherit another project's habits by accident?

The design proposal names long-term memory, episodic memory, procedural memory,
and meta-memory. That taxonomy is useful as a checklist, not as evidence that
the system has those faculties. Each memory type creates a testable engineering
question. What is stored? How is it retrieved? How does it decay? Which
decisions is it allowed to influence?

Without those answers, learning becomes a place to hide uncertainty. With those
answers, it becomes part of the product surface.

## Meta-Learning Needs a Brake

The upper levels are meta-learning and cognitive systems. In the design,
meta-learning means learning how to learn better. A cognitive system adds
self-awareness, collaboration, and strategic reasoning. These are interesting
goals, but they should raise skepticism before excitement.

A system that changes its learning strategy is also changing the path by which
future behavior is produced. That can be useful. It can also make the system
harder to debug. If yesterday's run changed today's method, a failing result may
not reproduce by rerunning the same input.

So the ladder needs a companion rule: higher capability requires stronger
reversibility. Reactive automation can be tested like a small component.
Deliberative agents need session review. Learning agents need memory inspection.
Meta-learning agents need experiment isolation and rollback. Cognitive systems,
if they deserve the name at all, need governance around goals, tools, memory,
and collaboration.

The five levels do not prove that cognitive agents exist in the strong sense.
They help prevent category errors. Do not give Level 0 validation to a Level 3
system. Do not give Level 4 permissions to a Level 1 assistant. And do not
mistake a generated architecture diagram for operational maturity.

The better use of the ladder is modest: name the level, name the state, name the
permissions, then build the smallest validation loop that matches them. Autonomy
is not a badge. It is an engineering burden that grows one level at a time.
