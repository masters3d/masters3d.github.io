+++
title = "Agent Memory: Short, Long, and Meta"
date = "2028-06-01"
draft = true
description = "Agent memory is not one bucket of context. Short-term, long-term, and meta-memory each change what the system can do and what engineers must be able to inspect."
template = "blog-post.html"
[taxonomies]
categories = ["Software Engineering"]
tags = ["agents", "memory", "context", "ai-development", "validation"]
[extra]
editorial_track = "software-engineering"
related = ["five-levels-of-agent-capability", "context-as-code", "cognitive-continuous-integration-and-the-broken-agent-loop"]
+++

One of the cleaner ideas in the generated agent design is the split between
short-term memory, long-term memory, and meta-memory. The proposal attaches them
to an autonomous engineering agent, with short-term memory for active work,
long-term memory for knowledge and episodes, and meta-memory for learning
history and strategy effectiveness. I would not treat the document as proof that
such a system was built. I would treat the split as a practical review
checklist.

Memory is where agent systems stop being disposable sessions. A single prompt
can be wrong and vanish. A stored lesson can keep steering future work after
everyone has forgotten where it came from. That makes memory a software
engineering concern, not a poetic one.

## Short-Term Memory Is the Working Surface

Short-term memory is the context the agent is using now. It includes the task,
constraints, files already inspected, plans made during the session, and
observations from commands or tests. In a coding agent, this is the difference
between answering one question and carrying a thread across several edits.

The engineering question is not whether short-term memory exists. It plainly
does, at least as session context. The question is how visible and stable it is.
Can the human see the plan? Can the agent correct a mistaken assumption? Does
the session remember validation failures strongly enough to avoid repeating
them?

The August 2025 GitHub Actions experiment exposed this in a different form. A
workflow could produce useful output, but the useful parts had to be separated
from session metadata. The system needed records for debugging, but those
records were not the deliverable. That is a memory boundary. Working traces help
explain the run. They should not pretend to be the artifact under review.

Short-term memory also has a natural expiration point. Once the task is done,
most of it should die. Keeping everything is not maturity. It is hoarding
context without deciding what deserves to become knowledge.

## Long-Term Memory Is a Product Surface

Long-term memory is more serious. The design proposal names a knowledge base,
episodic memory, and procedural memory. In plainer terms: what the agent knows,
what it has experienced, and how it thinks tasks should be done.

That is powerful because it can reduce repeated explanation. It is risky for the
same reason. If a team lets an agent remember patterns, those patterns need
source, scope, and a way to be corrected. A memory like "this project prefers
small pull requests" is useful. A memory like "this error is harmless" can
become costly if it was learned from one unusual run.

Long-term memory should therefore behave more like documentation than vibes. It
needs provenance. It needs review. It needs a distinction between project
policy, observed tendency, and temporary preference. It also needs deletion,
because an agent that cannot forget is not more reliable. It is more likely to
preserve old wrongness.

This is where [Context as Code](/blog/context-as-code/) becomes relevant.
Durable context should be stored where the team can inspect and version it when
possible. Hidden memory may be convenient, but engineering depends on shared
artifacts. If memory changes behavior, it belongs inside the system's review
surface.

## Meta-Memory Is the Dangerous One

Meta-memory is memory about learning. The proposal describes learning history,
strategy effectiveness, and a self-model of capabilities and limitations. That
is the most interesting tier because it shapes how the agent chooses future
approaches.

It is also the easiest tier to overclaim. A table that says one strategy has an
effectiveness score is not automatically evidence. Was it measured across
comparable tasks? Was the outcome reviewed by a human? Did the strategy work, or
did it merely correlate with easier assignments?

A practical meta-memory should be humble. It can record that a previous approach
passed tests, that a review found a blind spot, or that a certain command gives
better evidence for this project. It should not silently rewrite the agent's
identity after a few successes. Strategy memory needs the same skepticism
engineers bring to flaky benchmarks.

The useful pattern is a promotion path. Session context starts as short-term
memory. A human or deterministic rule promotes a small piece into long-term
memory when it has durable value. Meta-memory changes only when there is
evidence about the process itself, not just one good outcome.

That gives the system a brake. Memory can help an agent become less repetitive
and more project-aware, but only if memory remains inspectable. The goal is not
an agent that remembers everything. The goal is an agent whose memory has shape:
what it is for, where it came from, when it expires, and who can say it is
wrong.
