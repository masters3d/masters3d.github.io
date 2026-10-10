+++
title = "Far Away Is the Same as Far in the Future"
date = "2026-10-09"
description = "You cannot drive a Mars rover with a joystick, because the round trip for a radio signal runs six to forty-four minutes. Distance and delay are one constraint measured in two different units, and once the round trip is slower than the thing you are controlling, central control stops being inefficient and becomes impossible. The physics version of the argument for autonomy at the edge."
template = "blog-post.html"
[taxonomies]
categories = ["Leadership & Teams"]
tags = [
  "autonomy",
  "latency",
  "feedback-loops",
  "high-agency",
  "team-dynamics",
  "systems-thinking",
]
[extra]
editorial_track = "leadership-and-teams"
+++

We drive rovers on Mars. We do not, however, _drive_ them.

Mars is far enough away that a radio round trip takes somewhere between about
six and forty-four minutes, depending on where the two planets are in their
orbits. That number is not a budget problem or an engineering shortfall. It is
the distance divided by the speed of light, and there is nothing in it to
optimize.

So picture joysticking a rover around a rock from a control room on Earth. You
see an image. You decide to turn left. You send the command. Twenty minutes
later it arrives, and by then the rover is somewhere else, or far more likely it
stopped fifteen minutes ago because it was not about to drive blind. Every input
you make is a reply to a world that no longer exists.

The fix was never a faster radio. The fix was to put the decision on the
vehicle. The rover does its own hazard detection, picks its own path between
waypoints, and stops itself when something looks wrong. Earth sends intent (go
to that ridge, sample that rock) and the rover owns everything underneath it.

What makes that worth writing about is not the space program. It is that the
same argument we usually have as a management philosophy (should people be
trusted to decide, how much autonomy is appropriate, is this person senior
enough) turns out to have an arithmetic version where none of those questions
come up.

## The Image on the Screen Is Always Old

Light covers about 300,000 kilometers per second, and that rate never changes,
so any distance can be written as a time. Mars is not "225 million kilometers
away" in any way that matters operationally. **Mars is twenty minutes in the
past.** The image in the control room is not a picture of Mars. It is a picture
of Mars twenty minutes ago, which is the only Mars anyone on Earth will ever
see.

Astronomers live with the extreme version. A galaxy a hundred million
light-years out is not far away so much as a hundred million years old, and
there is no other kind of looking available. Every observation of anything,
anywhere, is a historical document. Even your own hand is a couple of
nanoseconds stale.

The first time this landed for me at work was not dramatic. I was reading a
status summary that had gone through three people, and I caught myself about to
make a call on it. The summary was accurate. It was also four days old, and the
thing it described had been renamed and partly rewritten since. I was in the
control room looking at a picture of Mars and about to steer.

That is the uncomfortable conversion. "How far away is this person from the
work?" and "how old is the information they are deciding from?" are the same
question. Distance on the org chart, distance across time zones, distance
between the person in the code and the person approving the change: they all
convert into staleness at some exchange rate, and the only honest number is the
round trip. If you are three handoffs from the keyboard, you are not a careful
reviewer with less context. You are a careful reviewer deciding about a system
that no longer exists in the shape you were shown.

Which also means the standard remedy (ask for more frequent updates) is aimed at
the wrong thing. More frequent reports do not make the picture current, they
make it a faster stream of slightly-less-old pictures. The delay is in the path,
not the cadence.

## It Arrives Faint, Too

There is a second cost riding along with the first, and it is the one I think
gets missed.

Radiated power falls off as the **inverse square of distance**. Go twice as far
and you receive a quarter of the power; ten times as far and you get one
percent. Nothing is absorbing it. The same energy is just spread over the
surface of a bigger and bigger sphere.

Voyager 1 is the case I never get over. It transmits with about twenty-three
watts, roughly a bright household bulb, and by the time that reaches Earth from
interstellar distance the received power is on the order of a tenth of a
billionth of a billionth of a watt. We hear it at all because the receiving
dishes are seventy meters across and the data rate has fallen to a few hundred
bits per second. Those are the only three dials available: **more transmit
power, a bigger ear, or less data per second.** There is no fourth.

So distance charges you twice. The farther the decision is made from the work,
the staler the information it rests on _and_ the fainter it arrives. An old
picture and a dim one.

I have watched the dim half play out more often than the stale half. Something
that was urgent and specific to the engineer touching the code ("this migration
will lock the table for about nine minutes under current row counts") becomes,
three handoffs later, "there may be some performance risk." Nobody lied. Each
person forwarded the part they understood, and the detail that made it
actionable did not survive the spreading. Then the decision made from that
summary is wrong, and we call it a judgment failure.

It was not a judgment failure. It was a link budget. And the three dials are the
same three: transmit more power (escalate, repeat, write it louder), build a
bigger ear (the decision maker invests in understanding the domain), or send
less data (compress to the one number that must survive). Most organizations
only ever reach for the first, which is why the engineer who was right ends up
feeling like they have to shout to be taken seriously.

If I had to pick one of the three, it is the third. "Nine minutes of write
downtime" survives four handoffs. Three paragraphs of correct nuance do not.
Decide what has to arrive intact, and send that.

## When the Loop Cannot Close

Control theory states the conclusion plainly: **when the time it takes to get
feedback back to the center exceeds the timescale of the decisions being made,
centralized control is not inefficient. It is impossible.**

Not slow. Not suboptimal. Impossible, the same way steering a rover twenty
light-minutes out is impossible. The loop cannot close in time, so whatever
happens next happens without the center's input whether or not anyone intended
that. The only real choice is whether the person at the edge knew in advance
that they were allowed to decide.

That framing is more convincing to me than anything I have argued from the
people side, because it is not a values claim. Nobody has to agree that trusting
people is good. The number either fits inside the decision window or it does
not.

And every team has the number, we just never measure it. Pick a real decision
from last month and count the hours from "someone noticed" to "someone decided."
Mine have come out at about a day for anything that needed one other person, and
closer to a week for anything that needed a meeting that had to be scheduled.
Once you have that number, the conclusion is not a proposal, it is a
description: **anything that moves faster than your round trip is already being
decided at the edge.** It is happening right now. The only question is whether
it is being done by someone working from the mission and the boundaries, or by
someone guessing at what the center would have wanted and hedging.

That guessing is the actual cost, and it is worse than a wrong decision. A
person who knows they own the call makes it and moves. A person who suspects
they do not, but cannot wait, makes the most defensible choice rather than the
best one, and the defensible choice is almost always the one that changes the
least. That is how a team ends up slow and risk-averse without anyone ever
deciding to be slow and risk-averse.

So the useful moves are the rover team's moves. **Send intent, not steps**:
Earth transmits destinations rather than wheel commands, because an instruction
has to stay valid for the entire round trip, and "get to that ridge" survives
twenty minutes while "turn left now" does not. **Push the hazard detection
down**: the rover stops itself, it does not request permission to avoid a hole,
and anything that must be decided faster than your round trip needs the
authority attached in advance. **Shorten the chain before boosting the power**:
removing one link from a four-person chain does more for both the staleness and
the fading than any amount of louder, more frequent reporting, because you are
buying back distance itself rather than fighting its effects.

This is where it meets [Independent Fire](/blog/independent-fire/) from the
other direction. There the problem was that the officer could not see what the
soldier behind the tree could see. Here the officer might see everything
perfectly and it still does not work, because the view is twenty minutes old
when it arrives and the order is twenty minutes old when it lands. Terrain and
latency are two different roads to the same destination: authority has to live
where the information already is.

What changed for me is that I stopped treating this as something to advocate
for. The decision is already at the edge if your round trip is slower than the
work. Nobody has to grant that, and no amount of process reclaims it. You are
only choosing whether the person standing there has been told the mission, or is
guessing at it while the clock runs.

---

_Related reading: [Independent Fire](/blog/independent-fire/) on distributed
authority when the center cannot see the ground, and
[Signal-to-Noise, Taken Literally](/blog/signal-to-noise-taken-literally/) on
what happens to a message on the way across._
