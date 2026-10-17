+++
title = "Promotion-Driven Development"
date = "2026-10-17"
draft = true
description = "Promotion incentives shape engineering behavior whether a company admits it or not. If advancement rewards visible launches more than durable systems, engineers will learn to build work that reads well in a packet, even when the product needs maintenance, context, and quiet reliability."
template = "blog-post.html"
[taxonomies]
categories = ["Engineering Systems"]
tags = ["promotion", "incentives", "career", "engineering-culture", "ownership", "systems-thinking"]
[extra]
editorial_track = "engineering-systems"
+++

In December 2021 I saved a link under the title "Promotion Driven Development
(PDD)." The note was only a pointer to someone else's phrase, but the phrase
stayed with me because it names a behavior every engineering organization
creates whether it means to or not. People build toward the incentives they can
see. If promotion rewards certain kinds of evidence, development will bend
toward producing that evidence.

This is not cynicism. It is systems thinking. Engineers are rational enough to
learn which work counts. If the promotion packet rewards large visible launches,
people will seek large visible launches. If it rewards cross-team leadership,
people will find cross-team projects. If it rewards incident reduction,
documentation, mentoring, or operational excellence, those behaviors become
easier to justify. The ladder may say it values all of them, but the stories of
who advanced last year teach the real curriculum.

The trouble is that the work most valuable to the product is not always the work
most legible to a promotion process. A feature launch has a title, a date,
screenshots, metrics, and a narrative arc. Maintenance often has absence as its
result: the outage did not happen, the migration did not hurt customers, the
next engineer did not spend three weeks rediscovering context. Absence is harder
to put in a packet.

## Incentives become architecture

Promotion-driven development starts as career strategy and ends as product
shape. If engineers need visible scope, systems accumulate visible projects. If
maintenance is discounted, old features stay half-alive. If glue work is praised
in words but ignored in advancement, glue work falls to the people least able to
refuse it. If complexity reads as seniority, simple solutions can look too
small.

None of this requires bad intent. A manager wants to help someone grow. A team
wants a project that demonstrates leadership. A promotion committee wants
evidence. The engineer wants a fair shot. Those are reasonable motives. The
system problem appears when the easiest evidence to collect is not the same as
the most important work to do.

I think about this whenever a team chooses between a new platform rewrite and a
boring reliability improvement. The rewrite may be the right answer. Sometimes
the old system is truly blocking progress. But the rewrite also produces
promotion-shaped artifacts: design docs, stakeholder maps, migration plans,
launch announcements, broad visibility. The reliability improvement may remove a
source of pain for years and still look small because its success is quiet.

The architecture that results from these choices carries the incentive system
inside it. You can see what the organization paid for. Shiny entry points with
brittle internals. Multiple frameworks because each team needed a flagship
project. Dashboards nobody owns because observability work helped during launch
but not afterward. Libraries that were created for scope and then abandoned when
maintenance stopped counting.

## Reward behavior, not only theater

The antidote is not to shame engineers for caring about promotion. Career
systems are part of the work environment. People have families, ambitions, and
legitimate reasons to seek advancement. A healthy organization should make the
valuable path and the promoted path overlap as much as possible.

That means promotion evidence has to include behaviors that protect the system,
not only outcomes that photograph well. Some examples I trust:

- Reducing operational load in a way that is visible in pages, tickets, or
  support burden.
- Decommissioning features, flags, or services that no longer justify their
  carrying cost.
- Improving tests, tooling, or docs so other engineers move faster and safer.
- Turning production feedback into product changes.
- Making a smaller design decision that avoids unnecessary complexity.
- Mentoring in a way that leaves durable context rather than private dependency.

These are not lesser achievements. They are the work that lets an organization
keep moving after the first launch. They should be written down with the same
seriousness as new feature delivery. If a promotion process cannot read them,
the process is training engineers to neglect them.

There is a measurement trap here. Once a behavior is rewarded, it can be
performed for the metric. Documentation can become page count. Mentoring can
become calendar theater. Reliability can become selective storytelling. That
risk is real, but it is not a reason to reward only launches. It is a reason to
read evidence carefully and ask whether the behavior changed the system.

## Make the promotion story match the engineering story

The cleanest test is to compare two narratives. First, what does the engineering
organization say it needs this year? Better production ownership, fewer
incidents, simpler architecture, more reusable context, faster onboarding,
stronger security, clearer design decisions. Second, what stories do successful
promotion packets tell? If the lists do not overlap, promotion-driven
development will pull against the strategy.

This is the reward-system half of
[Quality Engineering vs Engineering Quality](/blog/quality-engineering-vs-engineering-quality/).
You can tell engineers that quality, security, and documentation belong to them,
but if advancement goes to whoever shipped the most visible feature, the spoken
value loses. The same is true for
[A Feature Needs a Life Cycle From Cradle to Grave](/blog/feature-cradle-to-grave/).
If decommissioning never helps a career, old features will live longer than they
should.

A better promotion packet would make room for stewardship. It would ask what
changed because of the engineer's work, who can now operate with less help,
which risks went down, which future work became cheaper, and what evidence
supports those claims. It would treat launches as one kind of contribution, not
the only kind that proves scope.

When I saved that PDD link in 2021, I think I was reacting to a joke with an
uncomfortable amount of truth in it. The phrase is funny because engineers
recognize the pattern immediately. The useful move is to stop treating it as a
joke. Promotion-driven development is what happens when the career system is
more explicit than the engineering strategy. If we want different software, we
have to make the incentives tell the same story as the system we say we are
building.
