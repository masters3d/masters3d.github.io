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
six and forty-four minutes, depending on where the two planets happen to be in
their orbits. That number is not a budget problem or an engineering shortfall.
It is the speed of light and the distance, and there is nothing in it to
optimize.

So picture trying to joystick a rover around a rock from a control room on
Earth. You see an image. You decide to turn left. You send the command. Twenty
minutes later it arrives, and by then the rover is somewhere else, or far more
likely it stopped moving fifteen minutes ago because it was not about to drive
blind. Every input you make is a reply to a world that no longer exists.

The fix was never a faster radio. The fix was to put the decision on the
vehicle. The rover does its own hazard detection, picks its own path between
waypoints, and stops itself when something looks wrong. Earth sends intent (go
to that ridge, sample that rock) and the rover owns everything underneath it.

I keep coming back to this because it takes something we usually argue about as
a management philosophy and turns it into arithmetic.

## Distance Converts Directly Into Delay

The thing I find genuinely clarifying here is that **distance and delay are not
two constraints. They are one constraint measured in two units.**

Light covers about 300,000 kilometers per second, and that conversion rate never
changes, so any distance can be written as a time and any delay can be written
as a distance. Mars is not "225 million kilometers away" in any way that matters
operationally. Mars is _twenty minutes in the past_. The image on the screen in
the control room is not a picture of Mars. It is a picture of Mars twenty
minutes ago, which is the only Mars anyone on Earth will ever see.

Astronomers live with the extreme version of this. Look at a galaxy a hundred
million light-years out and you are not looking far away, you are looking a
hundred million years into the past. There is no other kind of looking. Distance
_is_ time, and every observation of anything anywhere is a historical document.
Even your own hand is a couple of nanoseconds stale.

Once you accept that trade, a lot of organizational questions get easier,
because the question "how far away is this team from the decision?" and the
question "how old is the information the decider is working from?" collapse into
the same question. Distance in an org chart, distance across time zones,
distance between the person in the code and the person approving the change:
these all convert into staleness at some exchange rate. The only thing worth
measuring is the round trip.

## And the Signal Gets Weaker the Whole Way

There is a second cost that compounds the first.

Radiated power falls off as the **inverse square of distance**: go twice as far
and you receive a quarter of the power. Go ten times as far and you get one
percent. That is not attenuation from anything in the way, it is pure geometry.
The same energy is spread across the surface of a bigger and bigger sphere.

Voyager 1 is the extreme case I never get over. It transmits with roughly
twenty-three watts, about what a bright household bulb draws, and by the time
that reaches Earth from interstellar distance the received power is on the order
of a tenth of a billionth of a billionth of a watt. We hear it at all because
the receiving dishes are seventy meters across and the data rate has dropped to
a few hundred bits per second. Those are the only three dials: **more transmit
power, a bigger ear, or less data per second.** No cleverness adds a fourth.

So the full cost of distance is both halves at once. The farther away the
decision is made, the staler the information it is made from, _and_ the weaker
the signal that made it there. You are deciding from an old picture and a
degraded one.

Every long chain in an organization is paying both. A detail that was obvious
and urgent to the person touching the code arrives at the fourth person in the
chain as a dim summary of something that was true last week, and then we are
surprised when the decision made from it is wrong. It was not a judgment
failure. It was a link budget.

## The Rule This Produces

Control theory states the conclusion plainly: **when the time it takes to get
feedback back to the center exceeds the timescale of the decisions being made,
centralized control is not inefficient. It is impossible.**

Not slow. Not suboptimal. Impossible, in the same way that steering a rover
twenty light-minutes away is impossible. The loop cannot close in time, so
whatever happens next will happen without the center's input whether or not
anyone planned for that. The only real choice is whether the person at the edge
knows in advance that they are allowed to decide.

I find this more convincing than any argument I have made about autonomy from
the people side, because it is not a values claim. Nobody has to agree that
trusting people is good. It is a latency calculation, and the number either fits
or it does not.

And every team has the number. We just never measure it. How long from a
developer seeing something to a decision coming back? An hour? A day? A week, if
it needs a meeting that has to be scheduled? Whatever that number is, **anything
that moves faster than it is already being decided at the edge.** Not as a
proposal. As a description of what is currently happening. The only question is
whether those edge decisions are being made by someone who was told the mission
and the boundaries, or by someone guessing at what the center would have wanted.

That is the same conclusion I reached in
[Independent Fire](/blog/independent-fire/) from the terrain side, where the
problem was that the officer could not see what the soldier behind the tree
could. Here the officer might see everything perfectly and it still does not
work, because the view is twenty minutes old by the time it arrives and the
order is twenty minutes old when it lands. Terrain and latency are different
roads to the same place: authority has to live where the information already is.

## What to Do With the Number

The practical move is not to eliminate distance. You cannot; the org is the size
it is and the planets are where they are. The move is to stop pretending the
round trip is free and design around it the way the rover team did.

**Measure the actual round trip.** Pick a real decision from last month and
count the hours from "someone noticed" to "someone decided." That is your
latency. Everything faster than it is already autonomous.

**Send intent, not steps.** Earth does not send wheel commands, it sends
destinations. The instruction has to stay valid for the entire round trip, and
specific steps go stale in transit while objectives do not. "Get to that ridge"
survives twenty minutes. "Turn left now" does not.

**Push the hazard detection down.** The rover stops itself. It does not ask
permission to not fall into a hole. Anything that must be decided faster than
the round trip has to be delegated with the authority attached, or it will be
decided anyway, badly, by someone who thought they were not allowed to.

**Shorten the chain before you boost the power.** Cutting one link out of a
four-person chain buys more than any amount of louder, more frequent status
reporting, because the inverse square works in your favor in both directions.

None of this is about trust, or empowerment, or how senior anybody is. It is
about whether the loop closes in time. If it does not, the decision is already
at the edge. You are only choosing whether the person standing there knows it.

---

_Related reading: [Independent Fire](/blog/independent-fire/) on distributed
authority when the center cannot see the ground, and
[Signal-to-Noise, Taken Literally](/blog/signal-to-noise-taken-literally/) on
what happens to a message on the way across._
