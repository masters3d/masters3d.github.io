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
ratio**. It is meant as praise. Everything they say is worth hearing, nothing is
filler.

I know what that is reaching for, and I have said versions of it myself. But
signal-to-noise is a real measurement from a real field, and if you borrow it
back from that field the compliment turns into something stranger and more
useful. So let me actually explain the thing, and then talk about the piece I
think matters most at work: that every one of us is a transmitter and a receiver
at the same time, and those are two completely different jobs.

## What SNR Actually Measures

**SNR** stands for **signal-to-noise ratio**, and it is exactly what the name
says: the power of the thing you want, divided by the power of everything else
arriving with it. If what you care about lands carrying a thousand times the
power of the background hiss, your SNR is a thousand to one.

Two details matter.

First, it is a **ratio** of two numbers, so it has no units and no maximum. It
can be ten, or a million. Because those numbers get unwieldy, engineers write
them in **decibels (dB)**, a logarithmic shorthand where 10 dB means ten times,
20 dB means a hundred times, and 30 dB means a thousand. A decent link runs
around 40 dB. A phone call is fine at 20.

Second, and this is where the compliment trips: **a ratio is not a percentage.**
There is no 100%. For "100% signal" to mean anything, the noise would have to be
exactly zero, and dividing by zero does not give you a perfect score, it gives
you an undefined one.

It is also worth knowing that zero noise is not merely rare, it is impossible.
Put a sensitive amplifier across a plain resistor sitting on a bench with
nothing connected to it and you will hear hiss, because the electrons inside are
jittering around at whatever temperature the room happens to be. That is called
**thermal noise**, and the formula is short: **kTB**, Boltzmann's constant times
temperature times bandwidth. Nothing in it describes component quality. You
cannot buy a quieter resistor. You can only cool it down or listen to less of
the spectrum, which is exactly why radio telescopes bathe their receivers in
liquid helium.

So noise is not a defect in the equipment. It is a property of being a physical
object in a universe that has a temperature. Nobody has ever built a clean
channel, because there is no such thing. The whole discipline is about what you
can reliably pull out of a channel that is permanently dirty.

## The Opposite of Noise Is Information

Here is a thing worth getting precise, because the everyday version of the
phrase blurs it.

**Signal** is not the opposite of noise. Signal is just the part of the
transmission you meant to send. The opposite of noise, the thing you are
actually after, is **information**, which has a specific meaning: the part of a
message the receiver could not have predicted.

That distinction has a sharp edge. Transmit a perfect, steady tone, an
unchanging sine wave. It is pure signal with no noise riding on it at all, and
it carries exactly zero information, because once you have heard a second of it
you can predict every second after. The status meeting where everybody agrees
immediately is this tone. It is beautifully clean and it told you nothing,
because every statement in it was predictable before it was made.

The flip side is stranger. Because information lives in the unpredictable part,
**the more information a transmission carries, the more it looks like noise.** A
compressed file and an encrypted stream are both, statistically, almost
indistinguishable from random. The tidy structure you can see in a signal is
mostly the redundancy, the part that was not carrying anything new.

So when you are judging whether something was worth hearing, the question is not
"was that clean?" It is "did I learn something I could not have predicted?"
Those come apart more often than you would like.

## Headphones and a Microphone

The clearest model I have found for how this plays out with people is the
headset sitting on my desk. It has headphones, which transmit into my ears, and
a microphone, which receives. Two transducers, two directions, one device. That
is what each of us is in every conversation.

The reason I like the analogy is that **the two jobs have completely different
failure modes, and almost everyone is much better at one than the other.**

On the transmit side, the thing that makes a good speaker is not volume, it is
**fidelity**: what comes out matches what you meant. A speaker that distorts at
high volume has a terrible SNR even though it is loud, because it is adding
noise of its own on top of the signal. Every bit of hedging, jargon aimed at the
wrong audience, or confident delivery of something you are actually unsure about
is self-generated distortion. Engineers measure this as **noise figure**: how
much noise a component adds beyond what it received. Some people have a low
noise figure. What arrives from them is what they meant, including the parts
where they were not certain.

On the receive side, the thing that makes a good microphone is not sensitivity.
A microphone that picks up everything is not better, it is just picking up the
air conditioner. The useful property is **selectivity**: capturing what was
aimed at it and rejecting what was not. And selectivity is a choice about what
you are willing to miss.

## Decoding Is Not the Same as Hearing

Which brings me to the part that genuinely changed how I think about this.

Your phone knows where it is because it listens to satellites about twenty
thousand kilometers up, each transmitting with roughly the power of a household
light bulb. **GPS** (the **Global Positioning System**) signals arrive at the
ground _weaker than the background noise_. Not faint. Weaker than the hiss. Put
a spectrum analyzer on that band and there is no bump, no peak, nothing poking
above the floor. Visually, there is no transmission there.

Your phone reads it anyway. Each satellite multiplies its data by a long
pseudorandom scramble pattern, and the receiver knows that pattern. It takes the
apparent noise coming in and correlates it against the pattern it expects. The
real signal lines up and reinforces, over and over, while actual noise lines up
with nothing and averages toward zero. The data climbs out from under the floor.

To a receiver without the code, that band is 100% noise, and that is a correct
measurement, not a figure of speech. To a receiver with the code, the identical
waveform is clean data. Same photons, same antenna, same instant. Opposite
verdict.

Encryption is the deliberate version of the same trick: a good cipher is
designed so its output is statistically indistinguishable from random to anyone
without the key. We engineer transmissions to be pure noise to everybody except
one intended receiver.

So: **SNR is not a property of a message. It is a measurement taken at one
particular receiver, listening on one particular band, holding one particular
key.** Ask what the SNR of a transmission is without specifying a receiver and
the question has no answer.

Which means that when someone says "that was just noise" about a colleague's
concern, they have not described the concern. They have described their own
instrument: what they were tuned to, what vocabulary they share, what context
they hold. The transmission may have been perfectly clean, and they may simply
not have had the code.

I think this is the real mechanism under the failure I wrote about in
[Independent Fire](/blog/independent-fire/), where a command structure breaks
down because the people at the edge see more than the center can. The soldier
behind the tree was transmitting. The formation had no correlator for him. It
also reframes [story mapping](/blog/story-mapping-shared-understanding/) and
[context as code](/blog/context-as-code/) as something other than documentation
chores. They are **key distribution**. You are handing people the code that
makes your transmissions decodable.

## Your Best Filter Is Also Your Biggest Blind Spot

Now the receive side, where the everyday examples are better than the
engineering ones.

Noise-canceling headphones work by sampling the sound around you and playing
back its inverse, so the two cancel. What they are good at is **steady,
repeating sound**: engine drone, air conditioning, the hum of a plane. What they
are bad at is a sudden voice. The filter is tuned for the predictable, and it
lets the unpredictable through. That is not a limitation, it is the design, and
it is a remarkably good one, because the predictable part is also the part
carrying no information.

Your brain does the same thing and does it better. Walk into someone else's
house and you notice the smell immediately. Twenty minutes later it is gone, not
because the air changed but because your olfactory system stopped reporting a
constant. Move in next to a freeway and for the first week you cannot sleep. A
month later you genuinely do not hear it, and you only notice it again when a
visitor mentions it. We call this **tuning it out**, and the technical name is
habituation: the nervous system suppressing a stimulus that stopped carrying
news. It is the single most effective noise filter any of us owns, running
continuously, for free, on every sense at once.

It is also the thing I would most want to argue with at work, for exactly the
reason it works so well. **Habituation filters on repetition, not on
importance.** The constant is suppressed whether it is harmless or urgent.

Which describes most of the dangerous situations I have been in professionally.
The flaky test everyone reruns. The alert that fires every morning. The
onboarding step that has been broken for a year and that everybody warns new
hires about verbally. None of these are being tolerated by a decision. They are
being filtered out below the level where decisions happen, which is why the
honest answer to "how did nobody notice?" is usually that everybody did, once, a
long time ago, and then their filters did what filters do.

The only reliable counter I know is to borrow a receiver that has not
habituated. The new hire in their first two weeks is an uncalibrated instrument,
and that is temporary and enormously valuable. Everything they flag as strange
is something the rest of us stopped being able to perceive. If their questions
get treated as noise, you have thrown away the only clean measurement you were
going to get.

## What I Keep

The thing people are grasping at when they praise someone's signal-to-noise
ratio is real. I just think they have the mechanism backwards.

The colleagues I would describe that way are not the ones who talk least. They
are the ones whose statements decode to the same thing every time: when they say
they are confident they turn out to be right, and when they are unsure they say
so, which means I never have to estimate their reliability from outside the
conversation. That is not compression. It is low noise figure. Fidelity, not
volume.

Three things I took from the physics:

**Noise is the floor, not the enemy.** It never reaches zero for anyone. Every
plan that assumes a clean channel is a plan that will not run, which is why the
redundancy you know is redundant (the second reviewer, the worked example, the
thing said once out loud and once in writing) is not waste. It is how messages
survive a dirty channel.

**There is no SNR without a receiver.** "That was noise" is a statement about
the listener. Before using it on someone else's input, the honest version is
_noise to me, from here, with what I currently know_, and sometimes the right
move is to go get the key rather than tune them out.

**Every filter trades the predictable for the important.** Habituation is superb
and it is indiscriminate. Whatever has been constant around you long enough has
already stopped reaching you, and the only way back is a receiver that has not
yet adapted.

None of that requires the noise to go away, which is fortunate, because it is
not going to.

---

_Related reading: [Independent Fire](/blog/independent-fire/) on what happens
when the center has no way to decode what the edge is sending, and
[There Is No Speedup for Shared Understanding](/blog/no-speedup-for-shared-understanding/)
on the hard capacity limit of the channel into another person's head._
