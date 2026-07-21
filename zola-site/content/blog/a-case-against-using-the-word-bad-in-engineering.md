+++
title = "A Case Against Using the Word 'Bad' in Engineering"
date = "2026-07-02"
description = "I used to say bad version, bad rollout, bad payload. I stopped, because a version isn't good or bad in the abstract. It's a distribution of outcomes across a population of users, configs, and use cases. The same payload can be flawless for 99% and broken for 0.5%, and calling it bad collapses that spectrum onto one label that quietly dictates how you triage, communicate, and remember the incident."
template = "blog-post.html"
categories = ["Engineering Systems"]
tags = ["systems-thinking", "incidents", "reliability", "false-tradeoffs", "blast-radius", "blameless"]
[extra]
editorial_track = "engineering-systems"
+++

For years, my incident vocabulary had one word doing all the heavy lifting: bad.
A bad version. A bad rollout. A bad payload. It felt precise in the moment.
Something broke, we found the thing that changed, and we labeled it. Ship the
good one, roll back the bad one, done. Somewhere along the way I stopped saying
it, and the reason I stopped is the whole point of this post: a version isn't
good or bad in the abstract. It's a distribution of outcomes across a population
of users, configurations, and use cases. The payload that took down one customer
was running perfectly fine for everyone else at the exact same moment. Calling
it "bad" wasn't wrong so much as it was low-resolution, a binary word smeared
over a reality that was never binary.

This is the same move as
[Orthogonal, Not Opposite](/blog/orthogonal-not-opposite/): the mistake is
collapsing something with structure onto a single line. There, sweet and salty
got folded into one slider that was never real. Here, "good version" and "bad
version" get treated as the two ends of one axis, when what you actually have is
an artifact meeting a population and producing a spread of results. Good and bad
are not the two ends of a version. They are a summary statistic we compute
(badly) in our heads and then mistake for the thing itself.

## The Word Smuggles In a Response

The reason "bad" is so sticky is that it works, right up until it doesn't. It's
fast. It's emotionally satisfying at 2am when a graph is red and people are
angry and you need something to point at. It rallies a room. But the word
carries a hidden passenger: a response. "Bad version" doesn't just describe, it
prescribes, and what it prescribes is _roll it back for everyone_. That's the
correct move when the thing really is bad across the board. It's the wrong move
when the truth is "this regresses one cohort running one configuration," where
the right response might be to roll back for that 0.5% and leave the 99% who are
perfectly happy exactly where they are. The label picks the mitigation before
you've looked at the distribution, and a label that chooses your action for you
is a label worth distrusting.

So the fix is not just to stop saying "bad." It's to replace it with words that
carry information instead of a verdict. Instead of "bad payload," say "payload
that regresses configuration X." Instead of "bad rollout," say "rollout that
affects the cohort on feature-flag Y." The vocabulary I try to reach for now is
about scope, not quality: the _blast radius_ (how much of the population is
affected), the _affected cohort_ (specifically who), the _regression scope_
(what exactly stopped working), and whether we've hit a _floor violation_ (data
loss, security, total outage) or merely a _ceiling degradation_ (something is
slower or uglier but nobody is losing anything they can't get back). Precision
in the words forces precision in the diagnosis. You cannot say "the rollout
regresses customers on the legacy auth path under high concurrency" without
having actually gone and looked, and the looking is the part that was always
missing when "bad" was doing the work.

That reach for precision has a prerequisite, and it's worth being honest about
it: you can only stop saying "bad" if you can actually _see_ the distribution.
Per-cohort success rates, per-config telemetry, the ability to slice an error
budget by customer and version and flag. If all you have is one global
red-or-green light, then "bad" is genuinely all the resolution you've got, and
better language is downstream of better instrumentation. The linguistic shift
I'm describing is really a bet that you built the observability to back it up.
When people can't move off the word, it's often the tooling talking, not the
maturity.

## At Scale, a Failing Corner Is Guaranteed

Here is the part that made me abandon "bad" for good, and it's less a philosophy
than a counting argument. Take your users, times your supported configurations,
times the versions still in the wild, times the feature flags, times the
locales, times the hardware. That product is enormous, and it is not decorative:
each of those combinations is a real place where your software actually runs.
Once the space is that large, the probability that _every single corner_ works
is essentially zero. Some combination will fail. Not because anyone was
careless, but because a space that big always has a corner nobody tested, nobody
imagined, and nobody could have. A nonzero failure corner isn't a defect of
judgment. It's a property of large systems, the way friction is a property of
moving parts.

And this is exactly where "bad" breaks down hardest, because if a
guaranteed-failing corner makes a version bad, then every version is bad,
always, forever, including the one you're about to roll back _to_. The word
stops distinguishing anything. It can't tell the difference between "one exotic
combination degrades" and "the whole fleet is down," and those are the two
situations you most need to tell apart in the first ten minutes of an incident.
When "bad" describes both the catastrophe and the rounding error, it has stopped
being information and started being a feeling. The newer version the small
cohort is running isn't a failed rollout just because it found a corner. Newer
isn't better and it isn't worse. It's newer, and it landed on a coordinate the
old one never visited.

The sharpest version of this is that the _fix_ has a blast radius too, and this
is the symmetry I most wish someone had told me early. We talk as if there's a
good state (before) and a bad state (after) and the rollback simply returns us
to good. But rolling back to help the 0.5% can re-break the 99% who had quietly
come to depend on the new behavior. Every mitigation is itself a payload landing
on a population, with its own distribution of winners and losers. "Roll it back"
is not a return to safety, it's another change with its own affected cohort, and
pretending otherwise is how a one-customer regression becomes a fleet-wide
outage at the hands of the people trying to help. There is no move that is
purely good. There are only changes and who they land on.

## Where Bad Is Still Earned

I want to be careful not to over-correct into the mush of "nothing is ever
really bad, it's all just perspective." It isn't. There is absolutely such a
thing as a bad payload, and I'll say it plainly: if it brings down all sites, if
it corrupts data, if it opens a security hole, if the blast radius is the whole
population or it punches through a floor, then "bad" is not lazy shorthand, it's
the accurate word and you should use it loudly. The point was never to retire
"bad." The point is to _earn_ it. Reserve it for floor violations and near-total
blast radius, and it snaps back to meaning something. Spend it on every
one-cohort regression and it means nothing when you finally need it.

The other reason to be careful with the word is that "bad payload" has a quiet
gravity that pulls toward "bad author." Scope language resists that pull. "This
rollout regresses the high-concurrency cohort" describes a system and invites a
fix. "That was a bad deploy" describes a person and invites a defense. This is
the same instinct behind a blameless postmortem: you get more truth, faster,
when your vocabulary points at coordinates instead of character. Describing the
blast radius is not just more accurate, it's more humane, and those turn out to
be the same thing more often than not.

I think this shift is mostly what experience did to me, though it took me a
while to notice. Early on, the model is binary because binary is all you can
hold: ship it or roll it back, good build or bad build. Later, the questions get
quieter and more useful. Who is affected? How many? Did we hit a floor or just
scratch the ceiling? Is the targeted fix smaller than the global one? None of
those questions have a "bad" in them. And underneath all of it is the acceptance
I resisted longest, which is simply that software has bugs. Not as a failure
state to be ashamed of, but as the baseline condition of the work. Every version
you have ever shipped or will ever ship goes out with failing corners you don't
know about yet. Once you actually believe that, "bad" stops working as a
verdict, because a verdict implies there was a clean version available and you
chose wrong. There wasn't. There was a distribution, and you picked the best one
you could see, and it had corners, like they all do. Bad stopped being a
judgment I passed on a release and became a coordinate on a map: not _is this
bad_, but _bad for whom, how many, and against which floor_.

---

_This is part of a running thread on names and dichotomies that don't survive a
second look. [Orthogonal, Not Opposite](/blog/orthogonal-not-opposite/) pulls
apart false opposites,
[Context Hunting vs Context Gathering](/blog/context-hunting-vs-context-gathering/)
shows how one word swap changes a whole mindset, and
[Stop Conflating Effort Tracking with Work Tracking](/blog/effort-tracking-vs-task-tracking/)
separates two things a single label had quietly fused. The "engineer away the
false state" instinct is the same systems-over-heroics idea in
[Minimize Humans as Glue](/blog/minimize-humans-as-glue/)._
