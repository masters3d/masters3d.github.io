+++
title = "Signal-to-Noise, Taken Literally"
date = "2026-10-08"
description = "People praise someone for having a 100% signal-to-noise ratio. Taken literally that is not a compliment: SNR is a power ratio, no channel has zero noise, and a signal that is pure signal carries no information at all. Borrowing the real engineering terms gives a sharper set of leadership lessons than the phrase does."
template = "blog-post.html"
[taxonomies]
categories = ["Leadership & Teams"]
tags = [
  "signal-to-noise",
  "systems-thinking",
  "communication",
  "context",
  "agents",
]
[extra]
editorial_track = "leadership-and-teams"
+++

Someone will tell you that a particular person has a **100% signal-to-noise
ratio**. It is meant as praise: everything they say is worth hearing. I know
what that is reaching for, but the phrase does not survive contact with the
field it borrowed from, and the ways it fails are more useful than the
compliment.

SNR is a ratio of two powers. It is dimensionless, which is why engineers write
it in decibels. "100%" would mean the noise is zero, and no such channel exists.

## Noise Is the Floor You Build On

Any resistor above absolute zero generates noise, because the charge carriers
inside it are moving thermally. Its power is **kTB**: Boltzmann's constant times
temperature times bandwidth. You can cool the receiver or narrow the bandwidth.
You cannot reach zero without reaching absolute zero, and even then the cosmic
microwave background is still arriving from every direction at 2.7 kelvin.

Noise is not a defect in the equipment. It is a property of being a physical
object in a universe with a temperature. **The engineering question was never
how to remove it. It is what you can reliably push through a channel that will
never be clean.** Everything below follows from that.

## A Pure Signal Carries Nothing

Transmit an unmodulated carrier, a perfect steady sine wave. It is 100% signal
and completely useless, because every future sample is predictable from the past
ones.

Information lives in the part a receiver could not have predicted, which has an
uncomfortable corollary: the more a transmission carries, the more it looks like
noise. Compressed and encrypted streams are statistically indistinguishable from
random. The structure you can see is the redundancy.

So the meeting where everyone agrees quickly is high signal by the colloquial
definition and nearly empty by the technical one. Every statement in it was
predictable before it was made.

## The Ratio Lives at the Receiver

GPS signals arrive **below the thermal noise floor**. Point an analyzer at that
band and there is no peak to find. Your phone recovers them anyway by
correlating against the pseudorandom code each satellite uses, and thirty-odd
decibels of processing gain pull the data out from underneath. Without the code,
that band is pure noise. With it, the same waveform is clean data.

Encryption is the deliberate version: a good cipher is designed so the output is
indistinguishable from random to everyone without the key.

**SNR is not a property of a message. It is a measurement taken at one receiver,
with one bandwidth, holding one key.** Which means that calling something noise
is a report on the instrument, not the transmission. It is the mechanism under
the failure in [Independent Fire](/blog/independent-fire/): the edge was
transmitting and the center had no correlator for it. Shared context is the
decryption key, which makes
[story mapping](/blog/story-mapping-shared-understanding/) and
[context as code](/blog/context-as-code/) key distribution rather than
paperwork.

## Capacity, and Why Shouting Is the Worst Move

Shannon-Hartley sets the ceiling for a noisy channel: capacity equals bandwidth
times the log of one plus the signal-to-noise ratio. **Power sits inside a
logarithm; bandwidth is a multiplier out front.**

Repeating yourself louder, in more meetings, escalated harder, is a power
increase, and it pays logarithmically. Opening a channel of a different shape
(write the doc, build the prototype, show the trace) pays linearly. The instinct
to turn up the volume when you are not being heard is, literally, the worst
available move.

The ceiling is also finite, which is the same wall as
[there is no speedup for shared understanding](/blog/no-speedup-for-shared-understanding/).
Producing above capacity does not transmit faster; it drops the excess. But
below capacity, error-free transmission over a dirty channel is possible, paid
for in redundancy. Reviews, tests, and worked examples are redundancy bought on
purpose.

## Four Filters Worth Naming

**Band-limiting.** Noise power is kTB, so every hertz you accept is noise taken
in for free. A receiver open everywhere is not better informed, just hotter.
Narrowing also cuts capacity, so every filter is a bet about where the signal
will be.

**Matched filtering.** The optimal detector for a known waveform is a correlator
shaped like the thing you are hunting. The precondition nobody mentions is that
**you cannot filter for a signal you cannot describe.** This is why
[context hunting beats context gathering](/blog/context-hunting-vs-context-gathering/),
and why a genuinely new failure goes undetected: monitoring is a bank of filters
for failures we have already seen.

**Processing gain.** Integrate longer and coherent signal adds up linearly while
random noise adds as the square root, so a signal below the floor climbs out of
it. Time buys SNR. The weak repeated signal beats the loud one-off, which is the
arithmetic behind [nine years of notes](/blog/nine-years-of-copious-notes/) and
behind prevention work, which has a terrible instantaneous reading and an
excellent integrated one.

**Noise figure.** Every stage adds noise, and Friis's formula says the first
stage dominates, because everything after it is divided by the gain already
applied. **Who hears it first sets the ceiling for every review that follows.**

## Distance Sets Where Authority Lives

Free space still punishes you: power falls off as the inverse square of
distance, and light speed is a hard floor. A round trip to Mars runs six to
forty-four minutes, and no budget changes that.

So a rover cannot be joysticked around a rock. By the time the image lands and
the command returns, it has already stopped or fallen in, which is why the
autonomy gets moved onto the vehicle. **When feedback latency exceeds the
timescale of the decisions, centralized control is not inefficient, it is
impossible.** That is the same conclusion as
[Independent Fire](/blog/independent-fire/), reached from propagation delay
instead of terrain, and I find the physical version more convincing.

## Output, Input, and Agents

For **output**, what people are actually praising is low noise figure and low
error rate: this person adds little of their own noise and what arrives decodes
correctly. That is calibration, not brevity. Stating confidence accurately keeps
the noise figure low even when you are often uncertain; stating everything with
equal confidence makes the receiver estimate your reliability from outside the
channel. Shipping the evidence with the claim, as in
[proof-carrying work](/blog/proof-carrying-work/), is how you let them stop
guessing.

For **input**, kTB is a calendar argument. The number of channels you monitor
sets your noise intake directly, which is part of why
[burnout is a control problem](/blog/burnout-is-a-control-problem/): a receiver
that cannot choose its own filter is swamped no matter how few hours it runs.
And long integration over a quiet band is exactly how the
[background brain](/blog/the-background-brain-boredom-makes-ideas/) pulls
something weak out from under the floor, which fails if you keep retuning.

For **agents**, this stops being analogy. A context window is a
bandwidth-limited channel, and filling it with marginally relevant material is
kTB: accepted bandwidth, accepted noise, worse decoding. The sharpest mapping is
that a good decoder has an **erasure symbol**, a way to report "could not decode
this" instead of guessing. A system without one must emit something for every
input, so feeding it noise returns confident garbage. That is hallucination in
channel terms, and the countermeasures are the standard ones: narrow the band,
give it a template to match, add redundancy. Humans fail the same way under the
same conditions.

## The Extraction

- **Noise is a given.** Any advice premised on removing it describes a system
  that does not exist.
- **There is no SNR without a receiver.** "That is just noise" is a statement
  about the instrument.
- **Perfect signal means zero information.** Smooth and entirely expected is
  nearly empty.
- **Power pays logarithmically, bandwidth linearly.** A different channel beats
  a louder one.
- **Reliability over a dirty channel costs redundancy**, bought deliberately.
- **Time buys SNR.** Quiet work that repeats will out-resolve a loud one-off.
- **The first receiver dominates the noise figure.**
- **You cannot filter for what you cannot describe**, so filter attention hard
  and capture wide. New signal always arrives looking like noise.

What people mean by a 100% signal-to-noise ratio is closer to: low noise figure,
honest error bars, no wasted bandwidth, and a receiver disciplined enough to
stay tuned. All of those are achievable. None of them require the noise to go
away, which is fortunate, because it is not going to.

---

_Related reading: [Independent Fire](/blog/independent-fire/) on why authority
belongs where the information already is,
[There Is No Speedup for Shared Understanding](/blog/no-speedup-for-shared-understanding/)
on capacity into another person's head, and
[The Word "Impact" Considered Harmful at Work](/blog/word-impact-at-work/) on
work with a poor instantaneous reading and an excellent integrated one._
