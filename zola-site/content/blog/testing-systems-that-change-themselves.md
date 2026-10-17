+++
title = "Testing Systems That Change Themselves"
date = "2029-01-01"
draft = true
description = "Adaptive agent systems break the assumption that yesterday's behavior is today's behavior. Testing them means preserving baselines while watching the system, its tests, and its goals change."
template = "blog-post.html"
[taxonomies]
categories = ["Software Engineering"]
tags = ["testing", "agents", "validation", "quality", "ai-development"]
[extra]
editorial_track = "software-engineering"
related = ["safe-self-modification-for-agents", "shift-left-synthetic-environments", "quality-engineering-vs-engineering-quality"]
+++

The generated integration design for cognitive engineering proposes agents that
review code, design architecture, generate testing strategy, improve
documentation, and learn from all of it. The section on testing is the part I
keep returning to, because it exposes the central problem: how do you test a
system whose behavior is supposed to change?

Traditional testing assumes a stable target. The implementation changes, but the
expected behavior remains fixed enough to assert. Adaptive agents challenge that
assumption. If the system learns from prior runs, changes strategy, and updates
its own process, then yesterday's passing test may not describe today's
behavior.

That does not make testing obsolete. It makes the test boundary more important.

## Keep the Baseline Boring

The design proposal talks about adaptive testing, autonomous verification,
emergent behavior testing, and meta-quality. Those are interesting ideas, but
they should not replace ordinary checks. The first layer should remain boring:
deterministic tests, type checks, build checks, linting, link checks, policy
checks, and whatever domain-specific validation already exists.

A changing system still needs fixed invariants. It may improve its strategy, but
it should not lose data. It may adapt its communication, but it should not
invent unsupported results. It may generate tests, but it should not mark its
own unreviewed assertions as truth.

The August 2025 GitHub Actions experiment is a useful reminder. The agent
workflow did not become more credible because it had a grand theory of
cognition. It became more credible when specific failure modes were checked:
wrong issue selection, duplicate pull requests, scheduled trigger behavior, and
metadata pollution. Those checks were not glamorous. They made the loop
understandable.

For adaptive systems, the baseline should answer one question: what must remain
true no matter how the agent changes its approach?

## Test the Adaptation, Not Just the Answer

Once the baseline exists, the next layer tests adaptation itself. If an agent
changes strategy based on feedback, the test should inspect the trigger, the
decision, and the result. Did the system notice the right signal? Did it select
a reasonable response? Did it record why? Did the changed approach improve the
target without breaking a constraint?

This is different from testing only the final output. A patch may pass tests
while the agent learned the wrong process lesson. A generated document may read
well while the system silently updated memory from weak evidence. A code review
may find a real issue while also producing a strategy that is too noisy for
future reviews.

Testing adaptation means preserving traces. The system needs logs, but not as
decoration. It needs enough traceability to reconstruct why behavior changed.
That includes the input context, selected strategy, evidence used, validation
run, and any memory written afterward.

It also means holding out examples. If the system is allowed to learn from every
task and then claim better performance on those same tasks, the measurement is
suspect. Replays, control tasks, and regression sets are not old-fashioned. They
are how we keep a changing system comparable with itself.

## Emergence Is Not an Excuse

The proposal includes emergent behavior management. I understand the appeal.
Complex systems can produce useful behaviors their designers did not explicitly
program. But emergence cannot become a blanket explanation for behavior nobody
wants to debug.

A practical test strategy should classify unexpected behavior quickly. Is it
beneficial and repeatable? Is it harmless but noisy? Is it risky? Is it only a
symptom of an unclear goal? The label matters because the response differs. You
cultivate the first, ignore or suppress the second, contain the third, and
rewrite the goal for the fourth.

Adaptive tests can help, but they need authority limits. An agent may propose
new tests based on observed behavior. It should not be the only judge of whether
those tests define correctness. Otherwise the system can move the target toward
whatever it already does.

Testing systems that change themselves is really testing three things at once:
the artifact produced, the process that produced it, and the learning that will
affect the next run. If any one of those is invisible, the system may still be
useful, but it is not yet trustworthy.

That is the practical frame I would keep from the design proposal. Let agents
generate more evidence. Let them propose tests. Let them adapt. But keep a
boring baseline, test the adaptation path, and require human review before the
system rewrites what success means. The future of testing is not fewer
assertions. It is assertions around a larger surface.
