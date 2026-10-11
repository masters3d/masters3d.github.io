+++
title = "Onboarding Is a Shared-Understanding Problem, Not a Documentation Problem"
date = "2026-10-11"
description = "A new engineer on my team had read everything by day three and still could not do anything. The docs were accurate and current, which is what made it interesting: he knew what every service did and still had no idea who to ask, which decisions were his, or why the weird part was weird. Documentation transfers descriptions. Onboarding needs the part of the picture that was never written down because nobody experienced it as information."
template = "blog-post.html"
[taxonomies]
categories = ["Leadership & Teams"]
tags = [
  "onboarding",
  "shared-understanding",
  "team-identity",
  "ownership",
  "documentation",
  "belonging",
  "team-dynamics",
]
[extra]
editorial_track = "leadership-and-teams"
+++

A new engineer joined and did the thing you hope for: he read everything. By day
three he had been through the architecture page, the runbooks, the design
documents, and most of the wiki. He could describe what every service in our
area did. On day four he picked up a small first task and sat on it until
Thursday, and when I finally asked how it was going he said something that stuck
with me. He said he knew what all the pieces were, he just did not know whether
he was allowed to change this one.

That was not a documentation gap. The documentation was unusually good for that
team (accurate, current, written by people who had actually built the thing),
and it had answered every question it was capable of answering. What it could
not tell him was who owned the file he was looking at, whether the odd retry
logic was a deliberate decision or an accident nobody had cleaned up, which of
the four people in the channel would have an opinion about his change, and
whether a two-line fix in that area was a thing you just do or a thing you
raise. He had the descriptions. He did not have the picture.

I have written about
[building that picture in a room](/blog/story-mapping-shared-understanding/),
with a map on a visible surface and every actor's goal laid out in sequence.
That is the right tool for a team entering new territory together. Onboarding is
a different shape of the same problem: one person entering territory everyone
else already holds, where the knowledge gap is lopsided and the map already
exists in several heads. What I want to work out here is why writing more things
down does not close that gap, what the missing part actually is, and why the
first two weeks are where belonging gets adopted or quietly does not.

## What Documentation Cannot Carry

Good documentation records what a system is. It is much worse at recording the
three things a new person actually needs, and that is not a quality failure, it
is a property of how documents get written.

The first is ownership. Not the `CODEOWNERS` entry, which was stale on our repo
and is stale on most repos, but the real answer to "if I change this, whose
afternoon does it become." That answer changes with reorgs, with who left, with
who happens to care. It is current in people's heads and out of date everywhere
else within about a quarter.

The second is history. Every system has parts that look wrong and are wrong, and
parts that look wrong and are load-bearing. A document describes the current
behavior of both identically, because at the moment of writing both are simply
what the code does. The distinction between them lives in whoever remembers the
incident, and it is the single most expensive thing for a new person not to
have, because the only way to discover it empirically is to break the
load-bearing one.

The third is the decision boundary, which is what my new engineer was actually
stuck on. Nothing in a wiki tells you the size of change you are expected to
make without asking. That threshold is real, it differs by team, and everyone
who has been there a year knows it precisely without ever having said it out
loud. It is the most consequential unwritten rule on any team, and it is
unwritten everywhere.

None of these got left out through laziness. They got left out because the
people who hold them do not experience them as information. Ownership feels like
a fact about the world, not a thing you would write down, in the same way you
would not document which door of the building actually opens. You just know.
Knowledge stops looking like knowledge once it is shared by everyone in the
room, and that is exactly the knowledge onboarding has to transfer.

## The Gap Shows Up as Silence

The expensive part is that a new person's missing context does not announce
itself. It shows up as someone being quiet.

My engineer did not come ask me on Monday. He read more documentation instead,
which was the responsible-looking move and the one the environment rewarded,
because asking a question in week one is a claim that you could not figure it
out yourself and there is no cheap way to make that claim. So he spent three
days doing the thing that could not possibly work, and from the outside it
looked like a new hire diligently ramping up. The gap and the ramp are
indistinguishable from the outside, which is why teams routinely discover the
problem in week five.

I think a lot of onboarding design is aimed at the wrong half of this. We
optimize the supply of information (more pages, better pages, a curated reading
order) and leave the demand side untouched, when the thing that is actually
broken is that the new person cannot tell which of their questions is
legitimate. They are rationing. Every question has a perceived cost, they cannot
calibrate the real cost yet, so they ask the safe ones and sit on the ones that
would unblock them. The result is that the most important questions are
systematically the least likely to be asked, which is the opposite of what you
need in week one.

Making it cheap to ask is mostly a structural move rather than an encouraging
one. "My door is always open" costs nothing to say and does not change the
calculation, because the cost the new person is worried about is not your
availability, it is what asking says about them. A standing slot on the calendar
changes it, because a question asked in a meeting that already exists is not an
interruption anyone has to justify. Pairing changes it more, since questions get
asked in the flow of work where they do not have to be formulated as requests.
Both work by removing the need to decide whether a question is worth asking,
which is the step where the rationing happens.

## Belonging Is Decided in the First Two Weeks

There is a reason this window matters beyond the ramp-up time, and it is the
thing I underrated for years.

[Team identity has to be adopted rather than assigned](/blog/team-identity-ownership/),
and the first two weeks are when a new person decides whether to adopt it. They
are not deciding consciously. They are forming a working answer to a simple
question: is this a group I am inside of, or a group I work next to. Everything
in those two weeks is evidence toward that answer, and the evidence is mostly
not the official kind. Whether anyone used the team's name around them. Whether
the shorthand got explained or whether people just kept using it. Whether the
first question they asked got a real answer or a link. Whether they got to see a
decision being made rather than a decision being reported.

A reading list says: here is the system, learn it. Walking someone through a
decision the team is currently arguing about says: here is how we think, and you
are in the room for it. The second one is where adoption actually happens,
because being present for an unresolved decision is the clearest available
signal that you are inside the group rather than being briefed by it. A
finished, documented decision carries none of that, which is why a perfectly
documented onboarding can leave someone feeling like a contractor on month
three.

The practical version of this is small. Name an owner for the new person's first
two weeks, not a buddy in the sense of a social greeter but someone whose actual
job that fortnight includes this person getting unstuck. Point them at a real
task on day two, something that touches production and is small enough to be
safe, because a new person learns more about ownership and decision boundaries
from one shipped change than from a week of reading. State the decision
threshold explicitly, out loud, as a sentence: here is the size of change you
should just make, here is where you should check first. Nobody has ever said
that to me on joining a team, and it would have saved weeks every time.

I want to be honest about the limit, because this is where my own advice has
overreached before. None of this replaces time on the system. A new person who
has been walked through every decision and handed a perfect map still has not
been paged at 2am for the service, still has not watched the weird retry logic
save them, and still does not have the instinct that tells an experienced
engineer which part of a change is the dangerous part. That instinct is built
from accumulated contact and it cannot be transferred in a meeting. What good
onboarding does is remove the artificial delays (the silence, the rationed
questions, the three days spent reading because asking felt expensive) so the
real learning can start in week one instead of week five. The clock on
experience still has to run. You are just not wasting the first month of it.

---

_Documentation answers what the system is, and a team that has written it well
should keep writing it. The three things a new person needs most (who owns this,
which strange parts are load-bearing, and how big a change I can make without
asking) are held collectively and written down nowhere, because the people who
hold them stopped experiencing them as knowledge. The
[story map](/blog/story-mapping-shared-understanding/) is how a whole team
builds that picture at once; onboarding is the one-directional version, and it
runs on a visible owner, an early real task, a stated decision boundary, and
questions made cheap enough to actually get asked. Get those right and the new
person starts [adopting the team's identity](/blog/team-identity-ownership/) in
week one instead of deciding, quietly and permanently, that they work near it._
