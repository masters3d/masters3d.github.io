+++
title = "Being Glue Is a Staffing Decision, Not a Personality"
date = "2026-10-10"
description = "Nobody ever assigned me the onboarding. A new engineer joined, somebody said 'you should talk to Cheyo,' and that was the whole decision. Glue work gets allocated by a question in a channel, which means it gets allocated to whoever answers fastest rather than to whoever should own it. The person who routes the question is the person who made the staffing call, and usually they do not know they made one."
template = "blog-post.html"
[taxonomies]
categories = ["Leadership & Teams"]
tags = [
  "glue-work",
  "ownership",
  "team-dynamics",
  "staffing",
  "incentives",
  "promotion",
  "boundaries",
]
[extra]
editorial_track = "leadership-and-teams"
+++

A new engineer joined the team on a Monday. By Wednesday somebody had written
"you should talk to Cheyo, he knows that area" in a channel, and that sentence
was the entire decision. No one staffed me on onboarding. No one estimated it,
scheduled it, or wrote it into anybody's goals. A person with a question got
pointed at a person with an answer, which is a completely reasonable thing to
do, and the next six weeks of my calendar were set by it.

I have written before about
[getting out of being glue](/blog/minimize-humans-as-glue/), and everything in
that post still holds: say no, hand the skill off, automate the recurring
patches, put your own oxygen mask on first. But that post is advice to the
person stuck in the seam, and it quietly accepts the premise that the seam is
where that person ended up by temperament. Reading it back, I think it lets
something important off the hook. I did not end up there because I am helpful by
nature. I ended up there because of how the work got routed, and routing work is
a staffing decision. The question this post is chasing is who actually made that
decision, what the reward structure paid them to do, and what has to change for
the next person not to land in the same seam by default.

## The Allocation Happens in a Channel

Here is what makes glue work different from every other kind of work on a team:
it is the only work that gets assigned without anyone deciding to assign it.

Feature work goes through a visible allocation. Somebody writes it down,
somebody sizes it, a name goes next to it, and if it is large enough, somebody
has to say out loud what is getting dropped to make room. The cost shows up
somewhere. Glue work skips that entire apparatus. The onboarding, the context
hunt for another team, the explanation of why the deployment behaves that way,
the half-hour of debugging someone else's failure: each of those got allocated
by a person asking a question and another person answering it. That exchange
looks like helpfulness. Structurally it is a work assignment made by whoever
typed the question.

Which means the allocation is made by the person with the least information
about its cost. The person asking knows their own blocked state. They do not
know the answerer's week, they do not know how many identical questions arrived
that day, and they genuinely cannot see the aggregate. Each asker is making a
local, correct, small decision. The sum of those decisions is a full-time job
that nobody created and nobody is tracking. That is not a character flaw in the
askers. It is a routing system with no visibility into load, which is the thing
you would never accept in a service you operate.

And the routing is not random. It lands on whoever answers fastest, which
selects for availability and conscientiousness rather than for ownership. The
person who answers in four minutes gets the next question too. I was fast, so I
got routed to, so I learned more of the system, so I became more obviously the
right person to route to. That loop tightens on its own. By the time it looked
like a personality trait, it was really just a cache: the cheapest place in the
org to get an answer, and traffic goes to the cheapest path.

## Who Could Actually Redistribute It

The useful question is not "why does Cheyo keep doing this" but "who had both
the information and the authority to send that work somewhere else."

Split those two, because they almost never sit in the same person. The
information about where glue is accumulating lives at the edge. I knew. The
other people answering questions knew. We could each see our own load and we
could usually see each other's, because we were the ones in the threads. What we
did not have was any ability to reassign it, since the work was never assigned
in the first place and you cannot hand back a thing you were never given. The
authority to redistribute sat with the lead, who could have named an owner,
rotated the duty, or said "that question goes to the team that owns that
service." But the lead could not see the load, because the whole category is
invisible by construction. Nothing about it enters a tracking system. It is
distributed across a dozen channels and a hundred small exchanges that
individually look like nothing.

This is the same split that
[Far Away Is the Same as Far in the Future](/blog/far-away-is-the-same-as-far-in-the-future/)
describes from the other direction. There, the person at the edge holds
information the center cannot get in time, so authority has to move to the edge.
Here the asymmetry is the same but the cost is reversed: the edge holds the
information and the center holds the authority, and because the edge has no way
to make the load legible, the center never learns there is a decision to make.
The work keeps flowing down the cheapest path and everybody involved is behaving
reasonably.

So the first move is not "stop being glue." It is to make the load visible to
the person who can act on it, which means counting. I started keeping a rough
tally for a few weeks, nothing elaborate, just a note of every interruption that
was somebody else's work. The number is what does the arguing. "I feel stretched
thin" is a mood, and a lead can sympathize with it and change nothing. "Eleven
hours last week, seven of them the same three questions about one service" is a
staffing report, and the three repeated questions are a documentation gap with a
price tag on it. Counting my own hours is the move I argued for in
[effort tracking versus work tracking](/blog/effort-tracking-vs-task-tracking/):
the thing you do not track cannot be argued about, and glue work is the purest
case of that, because it is almost defined by not being tracked.

## What the Structure Actually Paid For

I want to be exact about my own position in this, because it is the evidence and
not a complaint.

I was mid-career and not yet where I wanted to be on the ladder, which is the
worst possible stage to be carrying glue. Promotion at that level runs on
attributable work: a thing you built, with your name on it, that someone can
point at. Glue produces the opposite artifact. The team shipped faster, the new
engineer ramped in three weeks instead of eight, the other team unblocked on a
Thursday afternoon, and none of those outcomes have a single name attached.
Every one of them is correctly described as a team result. I could not even
claim them honestly, because claiming them would have meant taking credit for
other people's shipped work.

The reward structure was not broken, which is what took me longest to accept. It
was paying for exactly what it said it would pay for: individually attributable
results. The structure got the glue anyway, free, because it had no line item
for it and somebody supplied it regardless. A system that receives something
valuable for free will not spontaneously start charging for it, and it will not
notice when the supply stops either, until something it does measure starts
degrading.

That is the honest cost of my position. I subsidized the team with time that did
not come back to me, and I did it while telling myself it was generosity. It was
closer to a pricing error, mine as much as the org's. And the part I would warn
anyone about is that the subsidy is most expensive exactly for the people least
able to afford it. A principal engineer who spends a day unblocking three teams
is doing visible leadership work that their level is explicitly supposed to
include. A mid-level engineer doing the identical day is doing work their level
does not get measured on. Same hours, same value to the team, two entirely
different career outcomes. Seniority changes what glue is worth, which is
exactly why it should not be allocated by who answers fastest.

## When Glue Is Real Work

None of this makes the work illegitimate. The team genuinely needed every hour
of it, and the version of me that dropped it all to protect my own ladder
position would have made the team worse. The distinction that matters is not
whether to do it but whether it has been made into work rather than left as a
favor, and that needs three things to be true at once.

It needs a name. Whatever it is (onboarding, triage, the interface to another
team) has to exist as a thing the team acknowledges, not as an ambient property
of being nice. It needs an owner with a boundary and an end date. A rotation
works; "Cheyo knows that area" does not, because one has an exit and the other
accumulates. And it needs to appear in the record that decides compensation and
level, which is the step teams skip, because it is the only one that costs the
org something.

Fail any of the three and you do not have glue work, you have a subsidy. All
three and it is a real assignment someone can be credited for, which is also the
point at which it becomes negotiable: you can hand it off, size it, trade it,
and argue it is too much. Invisible work cannot be negotiated, which is the
actual trap.

The authority to do all three sits with whoever runs the team, and that is the
uncomfortable conclusion for me, because it is the one part of this I could not
fix from where I stood. I could count my hours and I could say no, and saying no
is a real tool. But saying no only relocates the work to the second-fastest
answerer, who is now where I was and probably has less standing to decline. On
the teams where this got genuinely better, it got better because a lead looked
at a tally, agreed it was a staffing problem, and named an owner with a
boundary. That is not a thing an individual can do for themselves. It is a
decision, it belongs to someone specific, and the first step is making sure that
person knows a decision exists at all.

---

_This is the leadership-side counterpart to
[Minimize Humans as Glue](/blog/minimize-humans-as-glue/), which argues for
fixing the system so the seam disappears. The part that post could not reach is
that someone is allocating the glue before any system design gets a vote, and
they are doing it with a sentence in a channel. Count the hours, hand the number
to the person with the authority to redistribute it, and insist that the work
get a name, a boundary, and a line in the record. Until then it is not a role,
it is a routing accident that looks like a personality._
