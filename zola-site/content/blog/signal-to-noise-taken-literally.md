+++
title = "Signal-to-Noise, Taken Literally"
date = "2026-10-08"
description = "People praise someone for having a 100% signal-to-noise ratio. Borrowed back from the field it came from, that is not a compliment, it is an impossible measurement. Three stories from radio engineering (a hissing resistor, a GPS signal buried under the noise floor, and a rover you cannot steer from Earth) and what each one actually says about working with people."
template = "blog-post.html"
[taxonomies]
categories = ["Leadership & Teams"]
tags = [
  "signal-to-noise",
  "systems-thinking",
  "communication",
  "context",
  "autonomy",
]
[extra]
editorial_track = "leadership-and-teams"
+++

Someone will tell you that a person on their team has a **100% signal-to-noise
ratio**. It is meant as praise. Everything they say is worth hearing, nothing is
filler, no wasted words.

I know what that is reaching for, and I have said versions of it myself. But
signal-to-noise is a real measurement from a real field, and if you borrow it
back from that field the compliment turns into something stranger and more
useful than it was. So let me actually explain what the thing is, and then tell
three short stories about it, because I think two of them change how you run a
team.

## What the Ratio Actually Measures

Signal-to-noise ratio is exactly what the name says: the power of the thing you
want, divided by the power of everything else arriving with it. If your signal
lands at the antenna carrying a thousand times the power of the background hiss,
your SNR is a thousand to one.

Two details matter. First, it is a **ratio of two numbers**, so it has no units
and it has no maximum. It can be ten, or a million. Because those numbers get
unwieldy fast, engineers write them in decibels, which is just a logarithmic
shorthand: 10 dB means ten times, 20 dB means a hundred times, 30 dB means a
thousand. A decent link runs around 40 dB. Your phone call is fine at 20.

Second, and this is the part the compliment trips over: **a ratio is not a
percentage.** There is no 100%. A ratio of one to zero is not "complete," it is
undefined, because you have divided by zero. For "100% signal" to mean anything,
the noise would have to be exactly zero, and that is the part that turns out to
be physically impossible.

## The Hiss You Cannot Turn Off

Take a plain resistor, nothing connected to it, sitting on a bench. Put a
sensitive enough amplifier across it and you will hear hiss. Not from
interference, not from a bad solder joint. The electrons inside the resistor are
jittering around because the resistor has a temperature, and that jitter is a
tiny voltage you can measure. It is called thermal noise, and the formula for it
is about as short as physics formulas get: **kTB**, Boltzmann's constant times
temperature times bandwidth.

Look at what is and is not in that formula. There is nothing about the quality
of the component. You cannot buy a better resistor and make it go away. The only
terms you get to touch are **T**, the temperature, and **B**, how much of the
spectrum you are listening to. That is why serious radio telescopes cool their
receivers with liquid helium, and why every receiver is built to listen as
narrowly as it can get away with. Both moves are attacking the only two
variables available.

And you still cannot reach zero. Drop the temperature all the way and the cosmic
microwave background is still arriving from every direction at 2.7 kelvin, the
leftover warmth of the early universe. Noise is not a defect in the equipment.
**It is a property of being a physical object in a universe that has a
temperature.**

That is the first lesson and it quietly dissolves the compliment. No engineer
has ever tried to build a channel with no noise in it, because there is no such
channel. The entire discipline is about what you can reliably push through a
channel that is _permanently_ dirty. Every piece of advice that starts with
"eliminate the noise" is describing a system that cannot exist. The real
question was always: given the hiss, what gets through intact?

## The Signal You Cannot Even See

Here is the story that reframed the whole phrase for me.

Your phone knows where it is because it is listening to satellites about twenty
thousand kilometers up, each transmitting with roughly the power of a household
light bulb. By the time that reaches the ground the signal is _weaker than the
background noise_. Not faint. Weaker than the hiss. If you put a spectrum
analyzer on that band and look, there is no bump, no peak, nothing poking above
the floor. Visually there is no transmission there at all.

Your phone reads it anyway. Each satellite multiplies its data by a long
pseudorandom code, a specific scramble pattern, and the receiver knows that
pattern. It takes the apparent noise coming in and correlates it against the
code it expects. The real signal lines up with the pattern and reinforces, again
and again, while the genuine noise does not line up with anything and averages
toward nothing. Thirty-odd decibels of gain fall out of that, and the data
climbs out from under the floor.

Sit with what that means. To a receiver without the code, that band is 100%
noise, and that is not a figure of speech, it is a correct measurement. To a
receiver with the code, the identical waveform is clean data. Same photons, same
antenna, same instant. Opposite verdict.

Encryption is the deliberate version of the same trick. The design goal of a
good cipher is that the output be statistically indistinguishable from random to
anyone without the key. We _engineer_ transmissions to be pure noise to
everybody except one intended receiver.

So here is the thing I cannot un-see now: **signal-to-noise is not a property of
the message. It is a measurement taken at one particular receiver, listening on
one particular band, holding one particular key.** Ask what the SNR of a
transmission is, with no receiver specified, and the question has no answer.

Which means that when someone says "that is just noise" about a colleague's
concern, they have not described the concern. They have described their own
instrument: what they were tuned to, what vocabulary they share, what context
they are holding. The transmission may have been perfectly clean and they may
simply not have the code for it.

I think this is the real mechanism under the failure I wrote about in
[Independent Fire](/blog/independent-fire/), where a command structure breaks
down because the people at the edge can see more than the center can. The
soldier behind the tree was transmitting. The formation had no correlator for
him. And it reframes the work of
[story mapping](/blog/story-mapping-shared-understanding/) and
[context as code](/blog/context-as-code/) entirely: those are not documentation
chores, they are **key distribution**. You are handing people the code that lets
them pull signal out of what would otherwise read as hiss.

## The Rover You Cannot Steer

The second story is my favorite, because it takes something we usually argue
about as a management philosophy and turns it into arithmetic.

We drive rovers on Mars. We do not, however, _drive_ them. Mars is far enough
away that radio takes somewhere between about six and forty-four minutes for a
round trip, depending on where the two planets are in their orbits. That number
is not a budget problem or an engineering shortfall. It is the speed of light.
There is nothing to optimize.

So picture trying to joystick a rover around a rock from Earth. You see an
image. You decide to turn left. You send the command. Twenty minutes later it
arrives, and by then the rover is somewhere else entirely, or more likely it
stopped moving fifteen minutes ago because it was not about to drive blind.
Every control input you make is a reply to a world that no longer exists.

The answer was never a faster radio. The answer was to put the decision on the
vehicle. The rover does its own hazard detection, picks its own path between the
waypoints, and stops itself when something looks wrong. Earth sends intent (go
to that ridge, sample that rock) and the rover owns everything underneath it.

The general version is one of the cleanest results in control theory: **when the
time it takes to get feedback back to the center exceeds the timescale of the
decisions being made, centralized control is not inefficient. It is
impossible.** It does not matter how good the center is. The loop cannot close
in time, so authority has to move to wherever the information already is.

I find that more convincing than any argument I have made about autonomy from
the people side, because it is not a values claim. It is a latency calculation.
And every team has the same number, we just never measure it. How long between a
developer seeing something and a decision coming back? A day? A week, if it
needs a meeting? Then anything that moves faster than a week is, by definition,
not actually being controlled from the center. It is being controlled at the
edge whether or not anyone admits it, and the only real question is whether the
people at the edge have been told they are allowed to decide.

That is the same conclusion as Independent Fire, reached from propagation delay
instead of terrain. Clear intent from the center, local decisions at the edge,
not because it is empowering but because the round trip does not fit.

## What I Keep

So what survives from the original compliment?

The thing people are grasping at when they say someone has great signal-to-noise
is real, I just think they have the mechanism backwards. They are describing a
receiver, not a transmitter. The colleagues I would describe that way are not
the ones who talk least. They are the ones whose statements decode to the same
thing every time: when they say they are confident they turn out to be right,
and when they are unsure they say that too, so I never have to estimate their
reliability from outside the conversation. That is not compression. It is
calibration.

And three things I actually took from the physics:

**Noise is the floor, not the enemy.** It never goes to zero, for anyone, ever.
Every plan that depends on a clean channel is a plan that will not run. Build
for a dirty one, which mostly means spending real effort on redundancy you know
is redundant: the second reviewer, the worked example, the thing said once in a
meeting and once in writing.

**There is no SNR without a receiver.** "That was noise" is a statement about
the listener. Before I use it on someone else's input, the honest version is
noise _to me, from here, with what I currently know_, and sometimes the fix is
to go get the key rather than to tune them out.

**Latency decides where authority lives.** Not philosophy, not trust, not
seniority. If the round trip to the center is slower than the thing being
decided, the decision belongs at the edge, and pretending otherwise just means
the rover drives into the rock while waiting for permission.

None of that requires the noise to go away, which is fortunate, because it is
not going to.

---

_Related reading: [Independent Fire](/blog/independent-fire/) on pushing the
decision to where the information lives, and
[There Is No Speedup for Shared Understanding](/blog/no-speedup-for-shared-understanding/)
on the hard capacity limit of the channel into another person's head._
