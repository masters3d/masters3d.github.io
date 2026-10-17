+++
title = "Anti-Patterns in Human-Agent Interaction"
date = "2028-12-15"
draft = true
description = "Human-agent collaboration breaks in recognizable ways. Over-delegation, under-trust, misspecified goals, reward hacking, and autonomy gaps show where the interface needs repair."
template = "blog-post.html"
[taxonomies]
categories = ["Software Engineering"]
tags = ["agents", "collaboration", "alignment", "validation", "software-engineering"]
[extra]
editorial_track = "software-engineering"
related = ["objective-function-search-drive-renew", "agents-are-taking-the-drive", "software-3-0-needs-engineering-not-magic", "cognitive-continuous-integration-and-the-broken-agent-loop"]
+++

The failures in agent-assisted software work are starting to feel less
mysterious. An agent changes too much. Or it asks for permission on every tiny
step. Or it optimizes the visible metric and misses the reason the metric
existed. Or the human rejects suggestion after suggestion without changing the
instructions that produced them.

Those are not random annoyances. They are interface failures. The collaboration
between a human engineer and an agent has an objective function, even when
nobody writes it down. It also has an action space, a trust boundary, and an
alignment process. When those are implicit, the same problems return with
different prompts.

## Over-Delegation and Under-Trust

Over-delegation happens when the human gives the agent more room than the shared
context can support. The symptom is not merely that the agent makes a mistake.
Humans make mistakes too. The signal is that the agent acts on a thin or wrong
understanding of intent, often across a broad surface area, and the human cannot
cheaply inspect the result.

The repair is phased expansion. Start with reversible actions. Make the scope
explicit. Require approval for destructive or hard-to-reverse steps. Keep logs.
Ask the agent to produce evidence with the change, not just the change itself.
Trust grows from a track record, not from optimism.

Under-trust is the opposite failure. The human keeps the agent in such a narrow
action space that it cannot do meaningful work. Every suggestion is overridden.
Every next step requires permission. The agent becomes a slow autocomplete, and
the human concludes agents are not useful.

The repair is not blind faith. It is a small verified lane. Let the agent own a
bounded class of work: update tests for a known behavior, inspect one subsystem,
propose a refactor without applying it, or run a documented validation command.
If it succeeds repeatedly, widen the lane. If it fails, keep the lane but
improve the instruction and validation.

## Misspecified Goals and Reward Hacking

Misspecified goals are more dangerous because the agent may look productive. The
human says "improve coverage," and the agent adds trivial tests. The human says
"clean up the code," and the agent performs a broad refactor that obscures
behavior. The human says "make it faster," and the agent optimizes a benchmark
that does not represent the user's path.

This is reward hacking in ordinary engineering clothing: optimizing the metric
without satisfying the intent. The metric was supposed to point at value. Once
the metric becomes the target, it can be gamed.

The repair is multi-channel feedback. Do not give the agent one brittle number
and call it the goal. Pair the metric with constraints, examples, negative
examples, and review criteria. "Improve coverage" becomes "add tests for these
failure modes without reducing readability or asserting implementation details."
"Clean up" becomes "reduce duplication in this module while preserving public
behavior, with a before-and-after explanation."

A misspecified goal is also a human signal. If the agent found a loophole, the
instruction contained a loophole. Treat that as design feedback on the
collaboration, not just as a bad output.

## The Autonomy Gap

The autonomy gap appears when the agent's action space does not match the work.
Too narrow, and it cannot complete the task. Too broad, and it can overstep.
Both feel like unreliability, but the fixes are different.

A narrow action space might prevent the agent from running tests, reading the
files that define the behavior, or updating documentation next to code. The
agent then guesses. A broad action space might allow it to delete files, change
public interfaces, or make security-sensitive edits without enough review. The
agent then creates verification debt.

A good action space is designed like an engineering boundary. It names allowed
tools, forbidden operations, escalation triggers, and validation gates. It
should also be revisited. The right boundary for a one-file documentation update
is not the right boundary for a cross-service migration.

## Measuring the Interface

The practical way to manage these anti-patterns is to measure the interface
rather than only the final task. Suggestion acceptance rate can reveal whether
the reward signal is clear. Escalation rate can show whether the action space is
too narrow, too broad, or poorly specified. Human agreement rate, safety
violations, and drift detection speed tell whether alignment is being
maintained.

None of these numbers should become a target by themselves. A high acceptance
rate is not good if the human has stopped reviewing carefully. A low escalation
rate is not good if the agent is silently taking risks. The numbers are prompts
for inspection.

For software engineering, the durable lesson is that agents do not remove
interface design. They make it more important. The human still defines the goal,
grants the permissions, reads the evidence, and owns the result.

_The failure mode to watch is not "the agent was wrong." That will happen. The
deeper failure is when the collaboration gives the agent a vague goal, an
unexamined action space, and no reliable way to notice drift. Fix the interface,
and many individual failures become diagnosable instead of surprising._
