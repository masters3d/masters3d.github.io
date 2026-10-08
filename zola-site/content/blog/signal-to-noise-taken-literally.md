+++
title = "Signal-to-Noise, Taken Literally"
date = "2026-10-08"
description = "People say someone has a 100% signal-to-noise ratio. Taken literally that is not a compliment, it is a category error: SNR is a power ratio, not a percentage, there is no such thing as a channel with zero noise, and a signal that is pure signal carries no information at all. This post takes the phrase down to its parts (the thermal noise floor, Shannon capacity, matched filters, processing gain, path loss, propagation delay) and asks what each one actually says about people, agents, time, and engineering work."
template = "blog-post.html"
[taxonomies]
categories = ["Leadership & Teams"]
tags = [
  "signal-to-noise",
  "systems-thinking",
  "information-theory",
  "context",
  "communication",
  "agents",
  "time-management",
]
[extra]
editorial_track = "leadership-and-teams"
+++

Someone will tell you that a particular person has a **100% signal-to-noise
ratio**. It is meant as high praise: everything that comes out of them is worth
hearing, nothing is filler. I know what they are reaching for. But taken
literally, the sentence does not survive contact with the thing it borrowed
from, and the ways it fails are more interesting than the compliment.

Signal-to-noise ratio is a ratio of two powers. It is dimensionless. It is not a
percentage and never was, which is why engineers write it in decibels: 10 dB, 30
dB, 60 dB. A good link might run at 40 dB, meaning the signal carries ten
thousand times the power of the noise. "100%" would mean the signal is equal to
the total, which would mean the noise is zero, which is not a very good link. It
is an impossible one.

That is the quest of this post: take the phrase apart down to the physics, find
out what is actually transmittable, and see which of those constraints are real
constraints on people, teams, agents, and time, rather than metaphors that
sounded good.

## There Is No Zero-Noise Channel

Start with the floor. Any resistor above absolute zero generates noise, because
the charge carriers inside it are moving thermally. This is Johnson-Nyquist
noise and its power is `kTB`: Boltzmann's constant times temperature times
bandwidth. At room temperature that works out to about -174 dBm per hertz, and
it is there whether or not anyone is transmitting. You cannot design it away.
You can cool the receiver, which is why radio astronomy uses cryogenic front
ends, and you can narrow the bandwidth, which is the `B` term. You cannot reach
zero without reaching absolute zero.

And even if you could, you would still be sitting in the cosmic microwave
background at about 2.7 kelvin, the leftover glow of the early universe arriving
from every direction at once. Below that there are quantum limits on measurement
itself. Noise is not a defect in the equipment. It is a property of being a
physical object in a universe with a temperature.

The first honest conclusion, then, is the one that quietly dissolves the
original compliment: **noise is a given**. The engineering question was never
how to eliminate it. It is what you can reliably push through a channel that
will never be clean. That reframing is the whole payload of this post, and
everything below is a consequence of it.

## A Pure Signal Carries Nothing

Here is the part that breaks the phrase from the other end.

Transmit an unmodulated carrier: a perfect, steady sine wave at a fixed
frequency. It is 100% signal by any definition you like. It is also completely
useless, because it carries zero information. You can predict every future
sample from the past ones. Nothing about it is capable of telling you anything.

Information lives in the part of a transmission the receiver could not have
predicted. That is Shannon's whole insight, and it has an uncomfortable
corollary: **the more information a signal carries, the more it looks like
noise**. A maximally compressed file and a maximally encrypted stream are both,
statistically, indistinguishable from random. The structure you can see is the
redundancy, the part that was not carrying anything new.

So "100% signal" is not just unachievable, it is pointing at the wrong end. A
transmission that looks perfectly clean and orderly is usually one that is
mostly carrying predictable content. The meeting where everyone agrees quickly
is extremely high signal by the colloquial definition and often conveys almost
nothing, because every statement in it was predictable before it was made.

## Noise Is Measured at the Receiver

Consider GPS. The signals arriving at your phone from those satellites are
**below the thermal noise floor**. Point a spectrum analyzer at that band and
you see nothing but noise. There is no peak to find. The transmission is
genuinely weaker than the hiss it is buried in.

Your phone recovers it anyway, by correlating the incoming stream against the
exact pseudorandom code that satellite is known to be using. Thirty-odd decibels
of processing gain fall out of that correlation, and the signal emerges from
underneath the floor. To a receiver without the code, that band is 100% noise.
To a receiver with it, the same waveform is clean data. Same photons, same
antenna, opposite verdict.

Encryption is the deliberate version of this. The design goal of a good cipher
is literally that the ciphertext be indistinguishable from random to anyone
without the key. We engineer transmissions specifically so that they are noise
to everyone except one holder of a decryption key, for whom they are perfectly
intelligible.

Which settles the question of where the ratio lives. **SNR is not a property of
the transmission. It is a measurement taken at a particular receiver, with a
particular bandwidth, at a particular temperature, holding a particular key.**
There is no such thing as the signal-to-noise ratio of a message in the
abstract.

The team version of this follows immediately. When something is dismissed as
noise, that is not a measurement of the message, it is a report on the receiver:
what it was tuned to, what vocabulary it shares, what key it holds. This is the
mechanism underneath the failure I described in
[Independent Fire](/blog/independent-fire/), where centralized command breaks
down because the edge sees more than the center. The soldier behind the oak was
transmitting. The formation had no correlator for it. Shared context is the
decryption key, which is why
[story mapping](/blog/story-mapping-shared-understanding/) and
[context as code](/blog/context-as-code/) are not documentation chores. They are
key distribution.

## The Capacity Equation and What It Says About Shouting

Shannon-Hartley gives the hard ceiling for a noisy channel:

```text
C = B * log2(1 + S/N)
```

Capacity in bits per second equals bandwidth times the log of one plus the
signal-to-noise ratio. Three things fall out of that shape and all three
transfer.

**Power buys you almost nothing; bandwidth buys you proportionally.** `S/N` is
inside a logarithm and `B` is a multiplier out front. Doubling your transmit
power adds one bit per hertz. Doubling your bandwidth doubles the whole result.
In human terms: saying it louder, repeating it in more meetings, escalating
harder, these are power increases, and they pay logarithmically. Opening a new
channel with a different shape (write the doc, build the prototype, show the
trace) pays linearly. The instinct to turn up the volume when you are not being
heard is, in the literal engineering sense, the worst available move.

**The ceiling is finite and real.** There is a maximum rate for a given channel,
and no cleverness gets you past it. This is the same wall as
[there is no speedup for shared understanding](/blog/no-speedup-for-shared-understanding/):
you can generate ten thousand lines of code in a day, but the channel into
another person's head has a capacity, and that capacity did not change because
the generation side got faster. Producing above channel capacity does not
transmit faster. It just drops the excess.

**Below the ceiling, error-free transmission is possible.** This is the
counterintuitive half of Shannon's theorem and it is the actual good news. You
do not need a clean channel to get a perfect result. You need to transmit below
capacity and spend the difference on coding. Reliability is purchased with
redundancy, deliberately, in known amounts. That is what a design review, a
test, a second reviewer, and a worked example all are: redundancy bought on
purpose so the message survives a channel you already know is noisy.

## The Filter Catalogue

"Filter out the noise" is the advice everyone gives. Engineering has actual
filters, and each one carries a precondition that the advice version leaves out.

**Band-limiting.** The cheapest move is refusing to listen where the signal is
not. Since noise power is `kTB`, every hertz of bandwidth you accept is noise
power you take in for free. A receiver open across the whole spectrum is
guaranteed to be swamped. But narrowing `B` also cuts capacity, per the equation
above, so there is no free lunch: a very narrow filter is a very slow channel
and it will miss anything outside the band. Every filter is a bet about where
the signal will be.

**Matched filtering.** The optimal detector for a known waveform is a correlator
shaped exactly like the thing you are looking for. This is the precondition
nobody mentions: **you cannot filter for a signal you cannot describe.** You can
only lock onto what you already have a template for. This is the technical
reason
[context hunting beats context gathering](/blog/context-hunting-vs-context-gathering/).
Gathering is an open band; hunting is a correlator. It is also why a new failure
mode goes undetected for so long. Monitoring is a bank of matched filters for
failures we have already seen.

**Processing gain.** Integrate longer and the signal, being coherent, adds up
linearly while the noise, being random, adds up as the square root. Stare at the
same spot long enough and a signal below the floor climbs out of it. Time buys
SNR, and there is no other way to buy what it is selling. The weak-but-repeated
signal beats the loud one-off, which is the same arithmetic behind
[nine years of notes](/blog/nine-years-of-copious-notes/) and behind the
compounding, quiet accomplishments I argued for in
[the post on the word "impact"](/blog/word-impact-at-work/). Prevention work has
a terrible instantaneous SNR and an excellent integrated one.

**Common-mode rejection.** Run a differential pair and take the difference
between two conductors instead of either one against ground. Any interference
that hit both equally subtracts to zero. Noise that is common to both paths
cancels; only the difference survives. Two independent reads of the same
situation do exactly this, which is the honest argument for a second reviewer:
not more eyes, but a second path whose shared interference cancels.

**Regenerate, do not amplify.** An amplifier multiplies everything in front of
it, noise included, so a chain of amplifiers accumulates garbage. A regenerative
repeater decodes the signal all the way down to bits, confirms them, and
transmits a clean copy. The difference matters enormously over distance. A
person who forwards a message is an amplifier; a person who understands it and
restates it from the decoded form is a regenerator. Every human relay in a chain
is one or the other, and a chain of amplifiers is exactly what
[humans as glue](/blog/minimize-humans-as-glue/) describes.

**Noise figure, and why the first stage dominates.** Every component adds its
own noise. Friis's formula says the total is dominated by the first stage,
because everything after it is divided by the gain already applied. Get the
first amplifier wrong and nothing downstream can save you. Organizationally this
is the most load-bearing result in the whole catalogue: **the first receiver in
a chain sets the noise figure for everything after it.** Who hears it first, and
how well they decode, matters more than every review stage that follows.

## Distance, Power, and the Latency Floor

Free space is the closest thing to a clean channel that exists, and it still
punishes you. Signal power falls off as the inverse square of distance, so
doubling the range costs four times the power. Voyager transmits with roughly
the power of a refrigerator bulb and we hear it across interstellar distance
only because the receiving apertures are seventy meters wide and the data rate
has fallen to a few hundred bits per second. Those are the three dials:
transmitter power, aperture, and time. You can trade among them. You cannot
escape them.

Then there is the floor you cannot buy your way past at all. Light speed is a
hard limit, so a round trip to Mars costs somewhere between about six and
forty-four minutes depending on orbital geometry. No budget changes that number.

That constraint has a direct consequence in control systems: **when the feedback
latency exceeds the timescale of the decisions, centralized control stops being
inefficient and becomes physically impossible.** A Mars rover cannot be
joysticked around a rock. By the time the image arrives and the command returns,
the rover has either stopped or fallen in. So the autonomy gets moved onto the
vehicle. The decision authority migrates to wherever the information already is,
because the channel will not carry it home fast enough to be useful.

That is the same conclusion as [Independent Fire](/blog/independent-fire/),
arrived at from propagation delay instead of from terrain, and I find the
physical version more convincing than the organizational one. Pushing authority
to the edge is not a management philosophy. In any system where the round trip
to the center is slower than the thing being controlled, it is the only
arrangement that works.

## What It Means for Output

Two completely different quantities get called signal-to-noise in conversation,
and the phrase is only useful once they are separated. The first is about
output.

Output SNR is not really a ratio of interesting words to boring ones. The
engineering analogue of what people are praising is **low noise figure and low
error rate**: this source adds little of its own noise, and what it delivers can
be decoded correctly. Reliability, in the bit error rate sense. Does the thing
they said turn out to match what happened?

That is a measurable property and it is mostly about calibration, not volume. A
source that states its confidence accurately has a low noise figure even when it
is often uncertain, because the uncertainty itself is correctly encoded. A
source that states everything with the same confidence has a terrible one, since
the receiver now has to estimate reliability from outside the channel. This is
why [proof-carrying work](/blog/proof-carrying-work/) matters: shipping the
evidence alongside the claim means the receiver does not have to guess at the
error rate.

And the high-output-SNR people I have actually worked with are not the ones who
talk the least. They are the ones whose statements decode to the same thing
every time. The compliment was never about compression. It was about fidelity.

## What It Means for Input

The second quantity is about what you let in, and here the physics is
unexpectedly prescriptive.

Noise power is `kTB`. Every unit of bandwidth you open takes in noise whether or
not anything is transmitting on it. A receiver tuned across every channel is not
more informed, it is just hotter. The engineering answer is to band-limit
aggressively and then spend the recovered margin on integration time in the band
you kept.

That is a calendar argument, not a metaphor. The number of channels you are
monitoring sets your noise intake directly, which is part of why
[burnout turns out to be a control problem](/blog/burnout-is-a-control-problem/)
rather than an hours problem: losing control of your bandwidth means you cannot
band-limit, and a receiver that cannot choose its filter is swamped regardless
of how few hours it runs. It is also why the
[background brain](/blog/the-background-brain-boredom-makes-ideas/) works. Long
integration over a quiet band is how you pull a weak signal out from under the
floor, and it fails if you keep retuning.

But apply the matched-filter precondition before you congratulate yourself on a
tight filter. You can only correlate against templates you already have. A
filter tuned until the receiver is comfortable is a filter that will reliably
drop the first instance of anything genuinely new, because novel signal has no
template yet and arrives looking exactly like noise. This is the asymmetry I
have ended up with in practice: filter hard at the point of **attention**, and
barely at all at the point of **capture**. Private notes are the wide-open band
with no filter on it, which is what makes it possible to go back and correlate
later, once the third occurrence has finally given you the template that the
first one lacked.

## Agents Are a Channel With No Erasure Symbol

Agents make all of this literal rather than analogical. A context window is a
bandwidth-limited channel with a hard capacity. Retrieval is a filter. A prompt
is modulation. Filling the window with marginally relevant material is not free
context, it is `kTB`: accepted bandwidth, accepted noise, worse decoding.

But the sharpest mapping is about what a decoder does when there is no signal. A
good communications decoder has an **erasure symbol**: a way to output "I could
not decode this" rather than guessing. Systems without one are forced to emit a
symbol for every input, so when you feed them pure noise they return confident
garbage, because returning nothing was never an available output.

That is hallucination, described in channel terms. The model is a decoder
operating with no erasure state, and the failure is structural rather than
moral. Everything that helps is a known noise countermeasure: narrow the band
(retrieval and scoping), use a matched filter (tell it the shape of what you are
looking for), add redundancy (tests, types, verification), and regenerate rather
than amplify (make it decode to a working artifact instead of forwarding
plausible text). Humans do the same thing under the same conditions, which is
worth remembering before blaming the model for it.

## The Actual Extraction

So, running the phrase back through its own test. What survives decoding?

**Noise is not the enemy and never was.** It is the floor you build above. Any
advice premised on eliminating it is describing a system that does not exist.

**There is no SNR without a receiver.** The ratio is a property of a
measurement, not of a message, which makes "that is just noise" a statement
about the instrument.

**Perfect signal means zero information.** The parts you could not have
predicted are the only parts carrying anything. Smooth, agreeable, entirely
expected output is high signal by the colloquial definition and nearly empty by
the technical one.

**Power pays logarithmically, bandwidth pays linearly.** Shouting is the worst
available move. A different channel beats a louder one every time.

**Reliable transmission over an unreliable channel is possible, and costs
redundancy.** Stay under capacity and spend the margin on coding. This is the
entire basis for review, testing, and writing things down twice.

**Time is a way to buy SNR.** Coherent integration pulls signals out from under
the noise floor. Quiet work that repeats will out-resolve a loud one-off,
eventually, provided someone is still integrating.

**The first stage dominates the noise figure.** Who receives it first sets the
quality ceiling for everyone downstream.

**You cannot filter for what you cannot describe.** So filter attention hard and
capture wide, because new signal always arrives looking like noise.

What people mean when they praise a 100% signal-to-noise ratio is something
closer to: low noise figure, honest error bars, no wasted bandwidth, and a
receiver disciplined enough to stay tuned. Every one of those is achievable.
None of them require the noise to go away, which is fortunate, because it is not
going to.

---

_Related reading: [Independent Fire](/blog/independent-fire/) on why authority
belongs where the information already is,
[There Is No Speedup for Shared Understanding](/blog/no-speedup-for-shared-understanding/)
on channel capacity into another person's head,
[Context Hunting vs Context Gathering](/blog/context-hunting-vs-context-gathering/)
on correlating instead of listening wide,
[Minimize Humans as Glue](/blog/minimize-humans-as-glue/) on chains of
amplifiers, and
[The Word "Impact" Considered Harmful at Work](/blog/word-impact-at-work/) on
work with a poor instantaneous reading and an excellent integrated one._
