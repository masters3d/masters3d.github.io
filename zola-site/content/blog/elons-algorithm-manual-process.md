+++
title = "Elon's Algorithm: A Reference for the Manual Process"
date = "2026-10-06"
description = "A reference write-up of Musk's five-step algorithm and what each step is supposed to mean when the thing being improved is a manual process in software engineering. Question the requirement, delete the step, simplify, accelerate, automate. Mostly a description of what the algorithm claims rather than an argument that it is correct, with a short closing note on where I do agree, in particular the rule that if you are not occasionally adding things back you are not cutting enough."
template = "blog-post.html"
[taxonomies]
categories = ["Engineering Systems"]
tags = [
  "automation",
  "manual-process",
  "elons-algorithm",
  "process",
  "reference",
  "systems-thinking",
  "quest-engine",
  "deployment",
]
[extra]
editorial_track = "engineering-systems"
+++

This is a reference post. The five-step algorithm associated with Elon Musk gets
cited often and paraphrased loosely, so what follows is an attempt to write down
what the steps are supposed to be, and what each one is supposed to mean when
the thing being improved is a manual process in software engineering rather than
a production line.

To be explicit about the frame: this post is mostly not making the case that the
algorithm is right, and it is not making the case that it is wrong. The walk
through the steps below reports the algorithm's claims as the algorithm's
claims. Whether they hold for any particular team, process, or organization is a
separate question that this post does not try to settle. The one place I do give
an opinion is the short section at the end, and it stays general.

## The Five Steps

As usually stated, in order:

1. **Make the requirements less dumb.** Question every requirement, and attach a
   person's name to each one rather than a department's.
2. **Delete the part or process step.** The stated heuristic is that if you are
   not adding back at least ten percent of what you delete, you are not deleting
   enough.
3. **Simplify or optimize.** Explicitly after the first two, on the grounds that
   the common error is optimizing something that should not exist.
4. **Accelerate cycle time.** Speed up what remains.
5. **Automate.** Last.

Two things are claimed about the list itself. First, that the order is load
bearing rather than decorative. Second, that the common failure is running it in
reverse: automating first, accelerating next, simplifying later, and questioning
the requirement only after something breaks. The account Musk gives is that he
arrived at the ordering by making that mistake himself.

## What "Manual Process" Is Taken to Mean Here

The steps are stated in terms of parts and process steps, so applying them to
software requires saying what the target is.

A manual process in this sense is not the absence of a process. It is a process
whose rules live in people's heads and whose messages travel over channels that
were never written down. Someone says "you're good to go." Someone says "we got
the green light," and the deploy happens. The signal is often a single message
or a thumbs up in a chat thread, and the people involved understand what it
carries: the checks the sender performed first, the conditions under which they
would not have sent it, and who they would have escalated to instead.

The framing the algorithm depends on is that the message is small and the
process behind it is not. The manual part is not the typing. The manual part is
a person holding a model of the system and making a judgment call with it. On
that reading, a proposal to automate the green light is a proposal to
externalize that model, and the size of the model is generally not known in
advance.

## Step 1: Make the Requirements Less Dumb

The step says to start with why the requirement exists and to insist on a named
owner for it.

The distinction drawn is between a requirement stated institutionally
("compliance requires a manual approval before production deploys") and one
stated personally ("this person asked for it, in response to this incident").
The claim is that only the second is auditable, because only the second gives
you somebody to go ask whether the control they wanted is the control currently
being performed.

The software-specific version of the problem this is meant to catch: a manual
gate gets added to compensate for a deploy pipeline with no rollback, the
pipeline gains rollback later, and the gate remains, because removing it
requires someone to own the removal and the gate is individually cheap. The
step's claim is that requirements with named owners can be renegotiated and
requirements owned by "the process" cannot.

## Step 2: Delete the Step

The step says to attempt removal of the whole thing, and to expect to restore
part of it.

The ten percent heuristic is the operative part. Its stated logic is that if
nothing ever has to be added back, the deletions were never near the boundary of
what is actually load bearing, and the boundary is where the information is.
Deleting something and being forced to restore it is treated as a measurement,
not as a failure.

Applied to software, the asymmetry usually noted is cost: suspending a manual
gate for a sprint is a revert, while removing a part from a vehicle is a tooling
change. The counter-pressure usually noted alongside it is social rather than
technical, in that whoever removes a check tends to be associated with the next
incident regardless of cause.

One clarification that belongs with this step: what is being deleted is the
step, not the intent behind it. If a manual approval exists to catch schema
changes, the step does not claim that catching schema changes should stop. It
claims that a human being is one mechanism among others.

## Step 3: Simplify or Optimize

The step says to simplify only what survived the first two.

For a manual process, simplification generally refers to collapsing handoffs:
whether the second of three approvers ever declines, whether any behavior
differs between two adjacent ticket states, whether a participant added after
some past incident is still doing anything. The claim is that such processes are
usually complex because participants accumulated, not because the underlying
work is complex.

A related point that often gets filed here is the form of the signal. A thumbs
up carries no record of what was checked, while a line such as "approved:
migrations reviewed, flag off, rollback tested" carries the same human cost and
leaves an artifact. Nothing is automated by that change; what it produces is
legibility, which the later steps depend on.

## Step 4: Accelerate Cycle Time

The step says to speed up the remaining process before mechanizing it.

The observation it rests on is that manual processes are typically slow in the
waiting rather than in the doing. An approval that takes thirty seconds may
arrive nine hours later because of timezones and queueing. On that reading,
reducing the thirty seconds addresses the smaller term.

The ordering warning attached to this step is that accelerating a process is
only sensible for one that survived step two, since a fast version of an
unnecessary step is still unnecessary, and is arguably more durable once it has
instrumentation around it.

## Step 5: Automate

The step says automation comes last, and only to what survived.

The stated reason is not that automation is difficult. It is that each earlier
step changes what you would have automated, so automating first encodes a
requirement that was never questioned, a step that might have been deleted, and
a shape that was never simplified.

The cost argument usually given alongside it is that the true cost of automating
a process is not visible from outside it. The happy path is quick; the
exceptions are where the work is (the team that does it differently, the
period-end variant, the case where a human would have declined to send the
signal and escalated in person). The claim is that a long tail of special cases
can end up more expensive to maintain than the manual process was.

The algorithm does not claim that every process should end up automated. A
process that resists automation is a possible outcome of running the steps. What
it claims is that the steps are what distinguishes "resistant to automation"
from "not yet understood."

## How This Lines Up With the Quest Engine

Worth noting, without arguing that either framework validates the other, that
the ordering claim resembles the one in the
[Quest Engine](/blog/the-meta-structure/).

Under that mapping, automation is **How**, the action phase, which the Quest
Engine also places last and also describes as the default starting point people
drift toward because it is where visible progress happens. The question of
whether a given process is worth automating corresponds to **Why**, the
[Primary Directive](/blog/the-primary-directive/) that downstream work is ranked
against. Steps one through four correspond to the
[Contextual Core](/blog/the-four-ws/): who sends the signal and who accepts it,
what gets checked, when it fires, where the state lives.

The parallel is structural. It is noted here because readers of one framework
tend to encounter the other, not as evidence for either.

## Where I Land, Generally

Having kept the rest of this descriptive, it is worth saying briefly where I
actually come down, without relitigating each step.

Broadly, the ordering claim matches what I have seen. Automating first has
consistently cost me more than the four steps it skipped would have, and I have
never regretted understanding a process before mechanizing it.

The piece I agree with most specifically is the add-back heuristic in step two:
if you are not occasionally putting things back, you are not cutting enough.
That one has held up every time. Deletions that never need reversing are a sign
you stayed comfortably inside the safe margin, and the margin is exactly where
you learn what a step was really doing. Treating the occasional restore as
expected (rather than as a mistake to be avoided) is what makes it safe to cut
aggressively in the first place.

What I am less sure about is the universality. The steps assume you have the
authority to question requirements and delete things, and plenty of manual
processes in software sit inside constraints where that is not on the table.
That is a limit on applicability, not a disagreement with the sequence.

## Summary

Stated plainly, the algorithm's position on manual processes is: understand what
the process is for and who asked for it, try removing it, simplify what is left,
shorten the loop, and automate only at the end. Its central assertion is about
sequence, and its central warning is that automation performed first is
indistinguishable from progress while it is happening.

Whether that sequence is the right one for a given process is left to the
reader. Apart from the section above, this post has only tried to state what the
algorithm says it is supposed to be.
