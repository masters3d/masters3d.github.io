+++
title = "Guiding Policies and Behavior Alignment"
date = "2027-07-15"
draft = true
description = "Guiding policies are useful only when they align behavior. They should help people make local decisions that fit organizational goals without turning every choice into permission seeking or compliance theater."
template = "blog-post.html"
[taxonomies]
categories = ["Engineering Systems"]
tags = ["guiding-policy", "behavior", "alignment", "strategy", "engineering-culture"]
[extra]
editorial_track = "engineering-systems"
+++

In May 2024 I wrote a short question to myself: "How does one go about creating,
updating and enforcing guiding policies?" I put it under the heading of behavior
alignment, but the question is really about the distance between what an
organization says and what people actually do.

Every company has stated values. Every engineering organization has principles.
Some are useful. Some are posters. The difference is not the wording. The
difference is whether the policy changes local decisions when nobody senior is
in the room.

## Policies Should Reduce Permission Seeking

A guiding policy is not a rule for every case. If it tries to be, it becomes a
manual, and manuals fail at the edge where judgment is needed. A good guiding
policy gives people a way to choose among tradeoffs without escalating every
choice.

"Prefer boring technology for core systems" is a guiding policy. It does not ban
experimentation. It says where novelty has to earn its place. "Production work
is first-class work" is a guiding policy. It does not list every operational
task. It says planning must account for the work required to keep the service
healthy. "Move validation closer to the author" is a guiding policy. It does not
prescribe every test. It says late inspection is a smell.

The best policies increase autonomy because they make the organization's desired
shape clear. People can act without waiting for a meeting because they
understand which direction the system prefers.

Bad policies do the opposite. They sound important but provide no decision help:
"be customer obsessed," "move fast," "raise the bar." Those phrases can be true
and still weak. When two values conflict, which one wins? When speed and safety
compete, what does the policy ask the engineer to do? When a customer asks for a
shortcut that will hurt the platform, what is the expected tradeoff?

A policy that cannot answer conflict is not guiding behavior. It is naming an
aspiration.

## Enforcement Is a System, Not a Scolding

The hard part of behavior alignment is enforcement. The word sounds punitive, so
teams often avoid it until the gap between stated policy and actual behavior is
large enough to become cynical. But enforcement does not have to mean
punishment. It means the environment consistently reinforces the behavior the
policy asks for.

If an organization says quality belongs to engineers, then tests, review time,
tooling, and release processes must support that. If it says documentation
matters, planning and promotion must recognize context work. If it says teams
own production, then production load must be visible in capacity and career
systems.

Otherwise the policy asks for one behavior while the system buys another.

This is where behavior alignment becomes a people system. Code standards,
architecture principles, operational practices, incident response, career
progression, and performance evaluation all teach behavior. People learn what is
really valued by watching which tradeoffs are rewarded, which shortcuts are
forgiven, and which invisible work is expected but not counted.

The enforcement mechanism can be lightweight: templates, checklists, review
questions, dashboards, rituals, leadership modeling, and peer accountability.
The important part is consistency. A policy enforced only during crises teaches
that normal work is exempt.

## Policies Need Feedback Loops

Behavior alignment connects directly to action, feedback, and adjustment. The
policy asks for an action. The organization observes the behavior and its
outcomes. Then the policy, incentive, or surrounding system has to adjust. A
guiding policy is a hypothesis about behavior. It should be observed and
updated.

Maybe the policy is too vague. Maybe it produces gaming. Maybe it works for one
team and fails for another because the context changed. Maybe the metric chosen
to observe it became the target, and Goodhart's law arrived on schedule. Maybe
the policy is correct but the surrounding incentives still fight it.

Updating a policy should not be treated as failure. It is how the organization
keeps the policy alive. Old policies can become cultural fossils: repeated
often, rarely examined, and no longer connected to the work. A living policy has
a lifecycle. It is created for a reason, tested in behavior, adjusted with
feedback, and retired when it no longer helps.

This is especially important as organizations scale. Early teams align through
shared memory. Larger organizations need explicit policy because not everyone
was in the room where the original judgment formed. But explicit policy without
feedback becomes bureaucracy. The goal is coherence, not compliance theater.

## Alignment Over Compliance

The phrase behavior alignment can sound mechanical, as if people are parts to be
lined up. I think the better reading is that a healthy organization makes it
easier for people to act in ways that support the shared goal. It does not
remove judgment. It gives judgment a direction.

A good guiding policy says: given what we know, here is the kind of decision
that will keep us aligned. It leaves room for context. It names the reason
behind the preference. It is backed by systems that reward the behavior it asks
for. It has a feedback loop so the policy can learn from reality.

That is the answer I would give now. Create guiding policies by starting from
the behavior you need, not the slogan you want. Update them when feedback shows
the behavior is not matching the goal. Enforce them by designing the surrounding
system so the aligned behavior is easier, visible, and rewarded. The policy is
only real when it changes what people do.
