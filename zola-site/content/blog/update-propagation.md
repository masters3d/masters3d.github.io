+++
title = "Update Propagation Turns Lessons Into System Changes"
date = "2028-09-15"
draft = true
description = "A lesson only counts after it reaches the places that can use it. Update propagation turns local learning into changed code, current documentation, and shared practice."
template = "blog-post.html"
[taxonomies]
categories = ["Quest Engine"]
tags = ["quest-engine", "systematic-improvement", "documentation", "feedback-loops", "systems-thinking"]
[extra]
editorial_track = "quest-engine"
related = ["iterative-integration", "deliberate-practice-for-engineers", "shared-understanding-as-a-practice", "types-of-engineering-documentation"]
+++

A retrospective can feel productive while changing almost nothing. The room has
the right tone. The notes are careful. The action items sound reasonable. Then
the same failure mode returns in the next quarter, not because nobody learned,
but because the learning stayed trapped in the meeting where it was named.

That is the problem Update Propagation is meant to catch. In the Quest Engine,
Systematic Improvement is the retrospective pillar, the part of the loop that
asks what reality taught us. Update Propagation is the last step inside that
pillar. It asks a harder question than "what did we learn?" It asks whether the
lesson reached the system.

## A Lesson Is Not a Fix Yet

The useful distinction is between a local correction and a propagated update. A
local correction handles the visible problem. A propagated update changes the
conditions that allowed the problem to recur.

If a deploy failed because one service lacked a health check, adding the health
check to that service is a correction. The update is larger. It asks which other
services share the same blind spot, which templates created the omission, which
runbooks still describe the old process, and which people will repeat the old
pattern because nobody told them the standard changed.

That may sound like documentation hygiene, but it is more than that. It is the
difference between memory as a private event and memory as a property of the
system. A person can remember. A team only remembers when the lesson has been
encoded into code, checks, templates, runbooks, reviews, and habits.

The source idea comes from several improvement traditions. Yokoten in the Toyota
Production System means horizontal deployment, spreading a useful change
wherever it applies. Poka-yoke means mistake-proofing, designing the system so a
known error is hard to repeat. Standardize-Do-Check-Act locks in a gain before
the next improvement cycle begins. The exact terms matter less than the order:
stabilize the improvement, make it visible, then spread it.

## Propagation Has Three Destinations

When I look at an engineering lesson, I want to know whether it reached three
destinations: the artifacts, the machinery, and the people.

The artifacts are the durable explanations: design records, runbooks, diagrams,
checklists, onboarding notes, and the comments that explain non-obvious intent.
If those stay stale, the old model keeps teaching itself to every new reader.

The machinery is the executable part of memory: tests, continuous integration
checks, deploy gates, linters, generators, templates, dashboards, and alerts. A
lesson that can be checked mechanically should not remain a human reminder
forever. But the order matters. Do not automate a confused process. Question it,
delete waste, simplify the remaining path, and only then automate the part that
has earned automation.

The people are the shared understanding. A change that sits in a document nobody
knows exists has not propagated. A change announced once in a meeting has not
propagated either. The update has to reach the people who will make related
decisions later, and it has to reach them in a form they can retrieve when the
decision returns.

## The Engineer's Skeptical Check

There is a practical danger here. Propagation can become bureaucracy. Teams can
turn every small lesson into a ceremony, every fix into a policy, and every
policy into a new surface area that must be maintained. That is not systematic
improvement. That is sediment.

The engineer's check is applicability. Where else does this lesson actually
apply? What would make recurrence structurally less likely? Which artifact or
check would someone naturally encounter at the moment they need it? If the
answer is vague, the update is not ready to spread. If the answer is specific,
propagation is not overhead. It is the completion of the fix.

This is why Update Propagation belongs at the end of the improvement loop, not
the beginning. First verify the gap between expected and actual behavior. Then
practice the improvement until the pattern is understood. Only after that does
propagation make sense. Spreading an untested fix horizontally just distributes
uncertainty.

## The Ratchet

The best improvements behave like a ratchet. Once made, the system should not
slip all the way back to its earlier state. The ratchet might be a test that
prevents regression, a template that includes the safer default, a runbook that
no longer depends on one person's memory, or a review norm that asks the missing
question before merge.

A postmortem without propagation is a story. A fix without propagation is local
repair. Update Propagation is what turns both into compounding capability. It
closes the loop by making the next loop start from a better place.

_The useful test is simple: if the same class of problem appears six months
after the lesson was supposedly learned, where did the update fail to travel?
The answer is the real action item._
