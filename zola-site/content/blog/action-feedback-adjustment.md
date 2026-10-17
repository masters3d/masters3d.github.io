+++
title = "Action, Feedback, Adjustment"
date = "2027-05-01"
draft = true
description = "Action and feedback are as fundamental to engineering as action and reaction are to physics, but adjustment is the human part. It is where judgment turns noisy signals into a better next move."
template = "blog-post.html"
[taxonomies]
categories = ["Engineering Systems"]
tags = ["feedback-loops", "judgment", "observability", "retrospectives", "systems-thinking"]
[extra]
editorial_track = "engineering-systems"
related = ["sprintspective-one-loop", "kaizen-and-the-observe-orient-decide-act-return-loop", "adaptive-control"]
+++

In February 2025 I wrote one rough sentence to myself: "Action and reaction
(feedback) are as fundamentals as physics. Adjustment signals judgment, decision
making, alignment." The grammar was rough, but the idea was clean. Engineering
organizations talk constantly about action. They talk about feedback when
something breaks. They talk less about the adjustment in between.

That missing middle is where judgment lives.

An action without feedback is just motion. Feedback without adjustment is just
noise. Adjustment without judgment is overcorrection. The useful loop is all
three: do something, observe what came back, and change the next move because of
what you learned.

## Feedback Is Not Automatically Learning

Software teams already have feedback everywhere. Tests fail. Customers complain.
Dashboards move. Incidents happen. Code reviews produce comments. Sprint
retrospectives collect notes. Performance reviews arrive. Build times get worse.
Costs rise. Logs fill with warnings.

The presence of feedback does not mean the system is learning. A smoke alarm
that nobody can hear is not safety. A dashboard that nobody uses to make a
decision is not observability. A retrospective that produces the same action
item every two weeks is not improvement. Feedback becomes useful only when it
reaches the person or system that can adjust behavior.

Latency matters. If the feedback arrives after the decision can no longer be
changed, it becomes history instead of guidance. Signal quality matters too. Too
little feedback leaves the team guessing. Too much creates alert fatigue and
ritualized ignoring. The work is not simply to collect more signal. The work is
to design loops where the signal is timely, interpretable, and connected to a
choice.

This is why unit tests feel different from an annual review. One gives feedback
close to the action and close to the author. The other may be useful for a
larger conversation, but it is a slow loop. Slow loops are not bad.
Architecture, career, product-market fit, and culture often need longer
observation windows. The mistake is using a slow loop for a fast correction, or
a fast noisy loop for a decision that needs patience.

## Adjustment Is the Part That Reveals the System

When feedback arrives, the next question is not "what happened?" It is "what do
we change?" That is where the real system becomes visible.

A team may learn that incidents are rising and still keep feature commitments
unchanged. That is a feedback loop with no adjustment. A team may learn that
code review is slow and add a rule that every review must happen within a day,
without asking whether reviewers have enough context or time. That is adjustment
without diagnosis. A team may learn that customers do not use a feature and
respond by adding more prompts to force usage. That is action captured by the
wrong story.

Good adjustment requires judgment. It asks whether the signal is real, whether
it matches other evidence, whether the system has enough authority to change,
and whether the cure is cheaper than the disease. Sometimes the correct
adjustment is to move faster. Sometimes it is to wait for more signal. Sometimes
it is to stop measuring the thing that is distorting behavior.

This is the part I meant by alignment in the original note. Adjustment aligns
the next action with what the system has learned. Without adjustment, alignment
is only stated intention.

## Designing the Loop

When I later expanded the idea, the common antipatterns were easy to name:
vanity metrics that make the dashboard look better without changing the work,
late feedback that arrives after the useful decision point, noisy signal that
teaches people to tune out, and blame feedback that makes people protect
themselves. I would group them under one larger rule: every feedback loop should
be designed around the decision it is meant to improve.

For code quality, the loop should be close to the code: tests, static checks,
local validation, and review comments that teach a reusable pattern. For
production, the loop should connect system behavior to operational choices:
alerts that indicate action, logs that explain state, metrics that show whether
users are receiving the promised service. For team process, the loop should help
the team change how it works, not perform a ceremony of complaint. For career
growth, the loop should be specific enough to guide practice and frequent enough
that the person can still use it.

Blame breaks these loops because it teaches people to manage exposure instead of
learning. If feedback is punishment, the rational move is to hide weak signals
until they become undeniable. A learning loop needs accountability, but
accountability should attach to improving the system, not protecting the story
that the system was fine.

The physics analogy is useful only up to a point. In physics, reaction follows
action whether or not we are wise enough to notice it. In engineering
organizations, feedback can be delayed, distorted, ignored, or turned into
politics. Adjustment is not automatic. It is a practice.

The loop I want to keep is simple enough to fit in daily work: act, observe, and
change the next action because of what came back. When that loop is healthy, the
organization does not need to be right on the first try. It needs to be honest
enough to see the signal and disciplined enough to adjust.
