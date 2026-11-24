+++
title = "If Everything Is a Sev 2, Nothing Is"
date = "2028-01-29"
description = "A phrase I picked up on a team long ago: if everything is a severity 2, nothing is. Severity is a shared signal, and once people raise it to buy attention it stops carrying information. How PagerDuty, Atlassian, Google, Microsoft, and AWS define their levels, why severity inflation is usually a tooling gap that got turned into process, and why the way out is funding the lower severities and keeping manual toil between 0.1% and 1%, counted in nines like availability, so engineers can still write the code that removes it."
template = "blog-post.html"
[taxonomies]
categories = ["Engineering Systems"]
tags = ["incidents", "severity", "on-call", "sre", "toil", "process", "tooling", "prioritization"]
[extra]
editorial_track = "engineering-systems"
scheduled = true
+++

There is a phrase I started saying on a team long ago, sometimes calmly and
sometimes out of plain frustration: if everything is a severity 2, nothing is a
severity 2.

The ladder on that team looked roughly like most incident ladders. A severity 0
was global. A severity 1 was several regions. A severity 2 was one region down.
A severity 3 said "this might turn into a problem, we need help with it before
it does." A severity 4 was the one where, after a look, you admitted it probably
should have been a bug report. Severities 0 through 2 called someone. Severities
3 and 4 did not.

You can predict what happened next. The lowest severity that got a person on the
phone became the severity that people wanted. File a 3 and it waited. File a 2
and somebody got called. So a lot of things that were really "please work on
this soon" got filed as 2s, and the queue of live severity 2 incidents grew
until we had to prioritize _within_ severity 2: which of these 2s is the real
one? That second sort is the tell. Once you need a priority system inside a
severity, the severity has stopped carrying information. It no longer means what
the person reading it thinks it means.

I wrote in
[Signal-to-Noise, Taken Literally](/blog/signal-to-noise-taken-literally/) about
habituation: we stop perceiving anything that repeats, whether it is harmless or
urgent. A severity level is a signal that people are supposed to perceive. Fill
the queue with it and the responders do what every nervous system does. They
tune it out.

## A severity is a promise about who gets woken up

Before arguing about my own ladder I wanted to see how others write theirs down.
PagerDuty publishes its
[incident response guide](https://docs.pagerduty.com/ops-guides/incident-response-guide/severity-levels),
and its first paragraph says the thing that matters most: lower numbers are more
urgent, and "in general you are able to take more risky moves to resolve a
higher severity issue." A severity is not a label of how upset someone is. It is
a contract that says who gets woken up, how fast, and how much risk they are
allowed to take to stop the damage.

Severity 2 is not a local quirk. PagerDuty and Atlassian both use SEV 2 for a
major incident that pages on-call, and most scales I found start at 0 or 1 and
run down to 3, 4, or 5. The public scales differ in how many levels they have,
but they share a shape. Here are two internal incident scales next to the one
that team used:

| Scale                                                                                      | Pages someone now | Top priority, but during the day                      | Becomes a ticket  |
| ------------------------------------------------------------------------------------------ | ----------------- | ----------------------------------------------------- | ----------------- |
| That old team                                                                              | Sev 0 to Sev 2    | (nothing)                                             | Sev 3, Sev 4      |
| [PagerDuty](https://docs.pagerduty.com/ops-guides/incident-response-guide/severity-levels) | SEV-1 to SEV-3    | SEV-4: low-urgency page, worked ahead of normal tasks | SEV-5             |
| [Atlassian](https://www.atlassian.com/incident-management/kpis/severity-levels)            | SEV 1, SEV 2      | SEV 3: handled during working hours                   | (below the scale) |

The middle column is the one that old ladder was missing. PagerDuty's SEV-4 is
"minor issues requiring action," and the response is a low-urgency page with the
instruction to work on it as your first priority, above normal work. One of its
listed examples is an individual host failing out of a cluster. Atlassian says
outright that its SEV 3 incidents can be handled during working hours while SEV
1 and SEV 2 alert on-call at any time of day, and its
[guidance for app partners](https://developer.atlassian.com/developer-guide/app-incident-severity-levels/)
describes minor incidents as high priority during local business hours. That is
the level people on that team kept reaching for when they filed a 2: a daytime
severity 2. Important, owned, worked first, and nobody stays up all night for
it.

There is an honest counterweight in PagerDuty's guide. Under "Always Assume The
Worst," it says that if you are unsure whether something is a SEV-2 or a SEV-1,
treat it as the higher one, because the middle of an incident is not the time to
litigate severity; review it in the postmortem. I agree with that during the
incident. The part that keeps the rule from becoming inflation is the second
half. If nobody ever comes back to downgrade, "assume the worst" turns into a
ratchet that only moves one direction.

## Who gets to set the number

The cloud vendors' support plans are useful here, because they face the same
pressure from customers that an internal incident queue faces from colleagues.
Every customer would like the fastest response.
[AWS](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html)
offers five case severities, from general guidance (a day) to business-critical
system down (15 minutes on Enterprise Support). The interesting part is how the
others handle the filer's choice.
[Google Cloud's support guidelines](https://cloud.google.com/terms/tssg) let the
customer designate the priority, then say Google may reclassify a designation it
believes is incorrect, and that its determination is final.
[Azure's top severity](https://azure.microsoft.com/en-us/support/plans/response/)
asks the customer to confirm the business is seriously degraded and to commit to
working the issue around the clock alongside Microsoft; if the customer does not
keep that up, Microsoft may lower the case to the next severity.

Both of those encode the same rule: the person filing proposes, and someone else
decides. That is my ideal for an internal queue too. Every incident gets
verified. The filer can say "I think this is a severity 0," and that is useful
input. Then triage decides. Sometimes the answer is that it really is a 0.
Sometimes the answer is that it is not an incident at all, and the right move is
to close it and file a bug.

The reason people inflate, though, is usually not bad faith. It is a tool. If
the only way the incident system will call a person is a severity 2, then a
person who needs a call will file a 2. That is a tooling gap, and the fix is to
change the tool, not to raise the number. If you want someone called for a
severity 3, the tool should let you say "call someone for this one." Nothing
more, nothing less.

I hold a general rule about this. Tooling should be the thing that gets improved
and moved. Process should come in only where there is a real gap that tooling
cannot close yet, and it should be temporary, a bridge until the tool catches
up. When process is built around a tooling gap and then left there, the
organization pays for the gap forever, one inflated incident at a time. It is
the first step of [Elon's Algorithm](/blog/elons-algorithm-manual-process/):
question the requirement before you optimize around it.

Changing the tool is not enough on its own. The work that a 2 was buying still
has to get done. The only way I see to take pressure off severity 2 is to make
severities 3 and 4 real: an owner, a timeline, and somebody actually doing the
work. The gap stays open until the bug is fixed, and that is fine, as long as
someone is fixing it for real, long-term, rather than patching it at the next
rollout. Those bugs are high priority. They are not live site.

The other pressure valve is rollback. If a rollout broke something, rolling it
back should be easy, simple, and straightforward, with as close to zero friction
as possible. PagerDuty's SEV-3 response includes the line "if related to recent
deployment, rollback." When reverting a change is cheap, a lot of things that
would have become incidents become a quick undo and a bug.

## Software engineers on the pager

The setup that makes this sharpest is infrastructure, where software engineers
are on call for the holistic health of a compute node, a GPU node, or a storage
node. That turns software engineers into site reliability engineers more or less
by default. I do not object to that in principle. I like the SRE model the way
Google describes it, and I think it describes more and more of what software
engineering looks like now. As agents write more of the code, a larger share of
an engineer's day moves toward operating what was written.

But the SRE model comes with its limits attached, and those limits are the part
that tends to get dropped. Google's chapter on
[being on-call](https://sre.google/sre-book/being-on-call/) commits at least 50%
of an SRE's time to engineering, caps on-call at 25%, and sets a maximum of two
incidents per 12-hour shift so that each one can be handled properly and
followed up. The chapter on
[monitoring distributed systems](https://sre.google/sre-book/monitoring-distributed-systems/)
says every page should be actionable and should require intelligence: "If a page
merely merits a robotic response, it shouldn't be a page." A queue full of live
severity 2s breaks all three at once.

My role as a software engineer is to remove problems with code. If you give me
issues, I am going to write code to fix them. When the queue takes away the time
to write that code, the problem is no longer the number of issues. It is a
process that has decided manual work matters more than the tools that would
remove it.

## Toil counted in nines

I wrote about the 50% toil cap in
[Good at It Is Not the Same as Wanting It](/blog/good-at-it-is-not-the-same-as-wanting-it/),
and about why
[humans should be the glue as rarely as possible](/blog/minimize-humans-as-glue/).
Fifty percent is a ceiling, not a target. My perfect amount of manual toil is
zero. At the scale large services run at, the number I am willing to accept is
somewhere between 0.1% and 1%. Some manual work is needed from time to time. But
when weeks or months go by and the manual work has not shrunk because everyone
was too busy doing it, that is a different problem. If 90% of the job is toil,
there will never be the bandwidth to get it to zero.

That range sounds extreme until you count it the way reliability gets counted.
Availability is written in nines: 99% is two nines, 99.9% is three. Google's
chapter on [embracing risk](https://sre.google/sre-book/embracing-risk/) notes
that each additional nine is an order of magnitude closer to 100%, and that an
incremental improvement in reliability may cost 100 times more than the previous
one. Read toil from the other side and it is the same scale. At 10% toil, 90% of
the time is free for engineering: one nine. 1% toil is two nines, and 0.1% is
three. Each nine takes more work than the one before it, which is exactly why
starting at 10% does not work. The work to reach the next nine needs time that a
10% budget has already spent.

Years ago I looked at the PMP application, and one section asked you to describe
the projects you had been part of. That question clarified something for me.
[PMI defines a project](https://www.pmi.org/about/what-is-a-project) as a
temporary endeavor undertaken to create a unique product, service, or result. If
you do the same thing every day (running scripts, pushing buttons), that is not
a project. That is maintenance. You have a project when you take the manual
maintenance and ask what it would take to remove it from the table entirely, so
nobody has to deal with it again. That is also why nobody gets promoted for
manual toil.

The reason this matters at scale is arithmetic. Toil grows linearly with the
service, so ten times the scale means ten times the toil. Start at 1% and a
tenfold jump puts you at 10%: painful, but 90% of the team is still free to
build the tooling that brings it back down to 1%, and that work is what earns
the next magnitude. Start at 10% and the same jump leaves the whole job as toil,
with nobody left to do the cutting. You never level up; the growth gets spent on
manual work. Getting to the next nine is a project. Staying where you are is
maintenance.

---

_The phrase started as a complaint about a queue, and I still think it is true:
a severity only means something while it is scarce. What changed for me while
looking at how other teams write their levels down is where I think the fix
lives. Not in telling people to file lower. In giving them a tool that can call
someone for a 3, a daytime tier that is worked first, a triage step that owns
the final number, and lower severities with real owners and dates. The same
logic runs through [Minimize Humans as Glue](/blog/minimize-humans-as-glue/) and
[Good at It Is Not the Same as Wanting It](/blog/good-at-it-is-not-the-same-as-wanting-it/):
the pager is a signal about the system, and the response that lasts is code that
makes the next page unnecessary._
