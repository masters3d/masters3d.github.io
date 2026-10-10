+++
title = "Signal-to-Noise, Taken Literally"
date = "2026-10-09"
description = "People praise someone for having a 100% signal-to-noise ratio. Borrowed back from the field it came from, that is not a compliment, it is an impossible measurement. What SNR actually means, why the opposite of noise is information rather than signal, and what a headset with a microphone on it says about being a transmitter and a receiver at the same time."
template = "blog-post.html"
[taxonomies]
categories = ["Leadership & Teams"]
tags = [
  "signal-to-noise",
  "communication",
  "listening",
  "context",
  "systems-thinking",
]
[extra]
editorial_track = "leadership-and-teams"
+++

Someone will tell you that a person on their team has a **100% signal-to-noise
ratio**. It is meant as praise: everything they say is worth hearing, nothing is
filler. I know what that is reaching for, and I have said versions of it myself.
But signal-to-noise is a real measurement from a real field, and borrowed back
from that field the compliment turns into something stranger and more useful.

## What SNR Actually Measures

**SNR** stands for **signal-to-noise ratio**, and it is exactly what the name
says: the power of the thing you want, divided by the power of everything else
arriving with it. If what you care about lands carrying a thousand times the
power of the background hiss, it is a thousand to one.

Two details matter. First, it is a **ratio**, so it has no units and no maximum.
It can be ten, or a million. Because those numbers get unwieldy, engineers write
them in **decibels (dB)**, a logarithmic shorthand where 10 dB means ten times,
20 dB a hundred times, 30 dB a thousand. A decent link runs around 40 dB.

Second, and this is where the compliment trips: **a ratio is not a percentage.**
For "100% signal" to mean anything the noise would have to be exactly zero, and
dividing by zero does not give you a perfect score, it gives you an undefined
one.

Zero noise is also not merely rare, it is impossible. Put a sensitive amplifier
across a plain resistor sitting on a bench with nothing connected to it and you
will hear hiss, because the electrons inside are jittering at whatever
temperature the room happens to be. That is **thermal noise**, and the formula
is short: **kTB**, Boltzmann's constant times temperature times bandwidth.
Nothing in it describes component quality. You cannot buy a quieter resistor,
only cool it or listen to less of the spectrum, which is why radio telescopes
bathe their receivers in liquid helium. Noise is not a defect in the equipment,
it is a property of being a physical object in a universe that has a
temperature. Nobody has ever built a clean channel, and the discipline is
entirely about what you can pull out of a permanently dirty one.

One more word is worth getting precise about. **Signal** is not the opposite of
noise; signal is just the part of the transmission you meant to send. The
opposite of noise, the thing you are actually after, is **information**: the
part of a message the receiver could not have predicted.

That has a sharp edge. Transmit a perfect, unchanging sine wave: pure signal, no
noise riding on it, and exactly zero information, because once you have heard a
second of it you can predict every second after. The status meeting where
everybody agrees immediately is this tone, beautifully clean and telling you
nothing. And because information lives in the unpredictable part, **the more a
transmission carries, the more it looks like noise**: compressed files and
encrypted streams are both nearly indistinguishable from random. The question is
not "was that clean?" but "did I learn something I could not have predicted?"
Those come apart more often than you would like.

## Headphones and a Microphone

The clearest model I have for how this plays out with people is the headset on
my desk: headphones that transmit into my ears, a microphone that receives. Two
transducers, two directions, one device, which is what each of us is in every
conversation. **The two jobs have completely different failure modes.**

On the transmit side, what makes a good speaker is not volume, it is
**fidelity**: what comes out matches what you meant. A speaker that distorts at
high volume has a terrible SNR even though it is loud, because it adds noise of
its own. Hedging, jargon aimed at the wrong audience, and confident delivery of
something you are unsure about are all self-generated distortion. Engineers
measure this as **noise figure**: how much noise a component adds beyond what it
received. Some people have a low one, and what arrives from them is what they
meant, including the parts where they were not certain.

On the receive side, what makes a good microphone is not sensitivity. One that
picks up everything is just picking up the air conditioner. The useful property
is **selectivity**, which is a choice about what you are willing to miss.

Which brings me to the part that genuinely changed how I think about this. Your
phone knows where it is because it listens to satellites twenty thousand
kilometers up, each transmitting with roughly the power of a household light
bulb. **GPS** (the **Global Positioning System**) signals arrive at the ground
_weaker than the background noise_. Put a spectrum analyzer on that band and
there is no peak, nothing above the floor, no visible transmission at all.

Your phone reads it anyway. Each satellite multiplies its data by a long
pseudorandom scramble pattern, and the receiver knows that pattern. Correlate
the incoming noise against the expected pattern and the real signal reinforces,
over and over, while actual noise lines up with nothing and averages toward
zero. The data climbs out from under the floor.

To a receiver without the code, that band is 100% noise, and that is a correct
measurement rather than a figure of speech. To a receiver with the code, the
identical waveform is clean data. Same photons, same antenna, same instant,
opposite verdict. Encryption is the deliberate version of that: we engineer
transmissions to be pure noise to everybody but one intended receiver.

So: **SNR is not a property of a message. It is a measurement taken at one
particular receiver, listening on one particular band, holding one particular
key.** Ask what the SNR of a transmission is without specifying a receiver and
the question has no answer.

So when someone says "that was just noise" about a colleague's concern, they
have described their own instrument rather than the concern: what they were
tuned to, what vocabulary they share, what context they hold. The transmission
may have been perfectly clean, and they may simply not have had the code.

I think that is the mechanism under the failure I wrote about in
[Independent Fire](/blog/independent-fire/), where a command structure breaks
down because the people at the edge see more than the center can. The soldier
behind the tree was transmitting; the formation had no correlator for him. It
also reframes [story mapping](/blog/story-mapping-shared-understanding/) and
[context as code](/blog/context-as-code/) as **key distribution** rather than
documentation chores: handing people the code that makes your transmissions
decodable.

## Your Best Filter Is Also Your Biggest Blind Spot

On the receive side the everyday examples beat the engineering ones.
Noise-canceling headphones sample the sound around you and play back its inverse
so the two cancel. They are excellent at **steady, repeating sound** (engine
drone, air conditioning) and bad at a sudden voice. The filter is tuned for the
predictable and lets the unpredictable through, which is the design and a good
one, because the predictable part carries no information.

Your brain does the same thing better. Walk into someone else's house and you
notice the smell immediately; twenty minutes later it is gone, because your
olfactory system stopped reporting a constant. Move in next to a freeway and for
the first week you cannot sleep, and a month later you do not hear it at all. We
call this **tuning it out**; the technical name is habituation, and it is the
most effective noise filter any of us owns, running free, on every sense at
once.

It is also the thing I would most want to argue with at work, for exactly the
reason it works so well. **Habituation filters on repetition, not on
importance.** The constant is suppressed whether it is harmless or urgent.

That describes most of the genuinely dangerous situations I have been in
professionally. The flaky test everyone reruns. The alert that fires every
morning. The onboarding step broken for a year that everybody warns new hires
about verbally. None of these are tolerated by a decision, they are filtered out
below the level where decisions happen, which is why the honest answer to "how
did nobody notice?" is that everybody did, once, and then their filters did what
filters do.

The only reliable counter is to borrow a receiver that has not habituated. A new
hire in their first two weeks is an uncalibrated instrument, and everything they
flag as strange is something the rest of us stopped being able to perceive. If
their questions get treated as noise, you have thrown away the only clean
measurement you were going to get.

## What I Keep

The thing people are grasping at with the compliment is real, but the mechanism
is backwards. The colleagues I would describe that way are not the ones who talk
least. They are the ones whose statements decode to the same thing every time:
when they say they are confident they turn out to be right, and when they are
unsure they say so, so I never have to estimate their reliability from outside
the conversation. That is not compression, it is low noise figure. Fidelity, not
volume.

Three things I took from the physics. **Noise is the floor, not the enemy**, so
any plan assuming a clean channel will not run, and the redundancy you know is
redundant (the second reviewer, the worked example, the thing said once out loud
and once in writing) is how messages survive. **There is no SNR without a
receiver**, so "that was noise" is a statement about the listener, and the
honest version is _noise to me, from here, with what I currently know_. **Every
filter trades the predictable for the important**, so whatever has been constant
around you long enough has already stopped reaching you, and the only way back
is a receiver that has not yet adapted.

None of that requires the noise to go away, which is fortunate, because it is
not going to.

---

_Related reading: [Independent Fire](/blog/independent-fire/) on what happens
when the center has no way to decode what the edge is sending, and
[There Is No Speedup for Shared Understanding](/blog/no-speedup-for-shared-understanding/)
on the hard capacity limit of the channel into another person's head._
