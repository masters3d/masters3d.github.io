+++
title = "A Feature Needs a Life Cycle From Cradle to Grave"
date = "2027-01-15"
draft = true
description = "Features are easier to start than to retire, so they need a visible life cycle. A feature is born as an idea, grows through implementation and deployment, reproduces when other teams copy the pattern, and eventually needs a deliberate path to decommissioning."
template = "blog-post.html"
[taxonomies]
categories = ["Engineering Systems"]
tags = ["features", "life-cycle", "decommissioning", "production", "ownership", "systems-thinking"]
[extra]
editorial_track = "engineering-systems"
+++

In July 2022 I wrote myself a short note with a question that looked almost
biological: how is a feature born, how does it scale or reproduce, and how does
it die? The list underneath was not complicated: idea, implementation,
deployment, postmortem, decommission. What made the note worth keeping was the
last sentence. There needs to be a clear way to define when a feature is going
into production and when it gets decommissioned.

That sounds obvious until you look at how most product work is planned. We are
much better at births than deaths. We know how to write a pitch, open a ticket,
build a prototype, find a launch date, and celebrate the release. We have
rituals for the beginning. The end is usually handled by exhaustion. A feature
dies when nobody remembers why it exists, when it breaks often enough that
someone finally removes it, or when a migration drags on so long that every team
silently learns to work around it.

The feature is not the code alone. It is the promise made to users, the
dashboards that watch it, the docs that explain it, the support scripts that
mention it, the permissions model that protects it, and the mental model other
engineers carry when they change nearby systems. If the feature has a life, all
of those things are organs in the same body. Shipping only creates the first
stable version of that body. Production is where we find out whether it can
live.

## Birth is a decision, not a merge

A feature starts before implementation. It starts when someone decides that a
behavior should exist in the product and that the organization is willing to
carry it. That carrying cost is easy to hide at the beginning. A small flag, a
small endpoint, a small configuration page, a small exception for one customer.
The birth looks cheap because most of the cost is in the future.

This is why I do not like treating the first ticket as the start of the feature.
The first ticket is already downstream of a choice. The real start should be a
short statement of ownership: who wants this to exist, what condition would
prove it is working, what signals would show it is harming the system, and who
has authority to remove it later. Without that statement, implementation
inherits a vague promise and turns it into code.

The minimum birth certificate for a feature is not a full design document. It
can be small, but it should answer four questions:

- What user or operator behavior should change because this exists?
- What production signal will tell us the feature is healthy?
- Who owns the feature after launch?
- What condition would make us retire it?

The fourth question is the one teams skip. It feels pessimistic to talk about
the death of a feature while people are still excited about its birth. But the
retirement condition is not a prediction of failure. It is a boundary around
commitment. We are saying, before emotion and sunk cost take over, what would
make the promise no longer worth carrying.

## Deployment is adolescence

Deployment is not the end of the life cycle. It is the point where the feature
leaves the protected environment and starts interacting with reality. This is
where the postmortem in my original list belongs, but I would broaden the word.
We should not reserve learning for incidents. Every launch deserves a short
after-action review, even when nothing dramatic happened.

Did users find the feature? Did they use it in the way we expected? Did support
get new questions? Did latency or cost move? Did another team copy the pattern,
or did they route around it? These are not vanity questions. They tell us
whether the feature is becoming part of the system or merely sitting inside it.

This is where a feature can reproduce. Sometimes reproduction is good: a pattern
proves useful, and other teams adopt it. Sometimes it is a warning sign: a
workaround spreads because the original abstraction is not strong enough. The
feature may be copied into another service, documented in a runbook, added to
onboarding, or assumed by downstream teams. Once that happens, removal becomes
more expensive. The feature has descendants now, and decommissioning requires
finding them.

Production feedback should therefore update the feature record. If a launch
teaches us something, the design should not remain frozen in the optimistic
language from before launch. The feature's current state should say what reality
taught us: which assumptions survived, which metrics matter now, which teams
depend on it, and whether the retirement condition changed.

## Death should be a normal path

The grave is where engineering systems reveal their maturity. A team that can
only add features is eventually trapped by its own success. Every old flag,
partial migration, one-off screen, and compatibility mode consumes attention.
The product gets heavier, and the people maintaining it become archaeologists.

Decommissioning should be treated as a first-class project with its own
definition of done. The work is not complete when the code path is deleted. It
is complete when the product no longer promises the behavior, the metrics no
longer expect it, the docs no longer teach it, customers have been moved or
told, and the people who depended on it have a replacement or an explicit
answer.

A useful decommission plan looks like the launch plan in reverse:

- Announce the intent and the reason.
- Identify users, teams, dashboards, docs, and downstream systems that still
  depend on the feature.
- Provide a migration path or state that no migration will be provided.
- Remove access gradually when risk requires it.
- Delete the code, tests, flags, docs, and alarms together.
- Record what the removal taught the next feature.

The last step matters. Retirement is one of the best sources of product truth.
It tells us what we overestimated, what became obsolete, what dependencies
surprised us, and which parts of the organization could not tolerate change. A
grave marker is not ceremony. It is context for the next birth.

This connects directly to the distinction I made in
[Development vs Production](/blog/development-vs-production/). Development can
create a feature, but production reveals its real shape. If production has no
path back into planning, features accumulate like sediment. They exist because
they once made sense, not because they still do.

Reading that 2022 note now, I think the biological language was right. A feature
is not a task. It is a living commitment inside a larger system. If we only
describe the moment of creation, we teach teams to launch. If we describe the
whole life cycle, we teach them to steward what they launch, learn from what
grows, and make room by retiring what has finished its work.
