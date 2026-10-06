+++
title = "Elon's Algorithm Applied to the Manual Process"
date = "2026-10-06"
description = "Musk's five-step algorithm is usually quoted at factories, but the ordering is really a general claim about where the return is, and it maps cleanly onto the manual processes software teams run every day. Question the requirement, delete the step, simplify, speed up the loop, and only then automate. Automation is step five for a reason, and most of the value is in the four steps you skipped to get there."
template = "blog-post.html"
[taxonomies]
categories = ["Engineering Systems"]
tags = [
  "automation",
  "manual-process",
  "elons-algorithm",
  "process",
  "roi",
  "systems-thinking",
  "quest-engine",
  "deployment",
]
[extra]
editorial_track = "engineering-systems"
+++

Elon Musk's five-step algorithm gets quoted mostly at hardware people, because
that is where it came from: a production line, a part that should not have
existed, a factory that was fast at building the wrong thing. The steps
themselves are not about hardware at all. They are a claim about ordering, and
the ordering holds anywhere there is a process.

Software teams have processes everywhere, and most of them are manual. Not
because anyone designed them that way, but because they accumulated. Somebody
has to approve the release. Somebody has to run the migration. Somebody has to
confirm the on-call handoff happened. The algorithm is a very good tool for
these, and applying it has consistently told me something different from what I
assumed going in.

## The Five Steps

1. **Make the requirements less dumb.** Every requirement needs a person's name
   attached, not a department's.
2. **Delete the part or process step.** If you are not adding back at least ten
   percent of what you delete, you are not deleting enough.
3. **Simplify or optimize.** Only after the first two, because the most common
   mistake is optimizing something that should not exist.
4. **Accelerate cycle time.** Speed up what is left.
5. **Automate.**

The famous part is that most people run these in reverse. They automate first,
then speed it up, then simplify, and only when something breaks badly enough do
they finally ask whether the requirement made sense. Musk's own stated version
of the mistake is that he has personally done all of this backwards more than
once, which is the only reason the list is worth anything. It is a description
of a trap, written by someone who fell in it.

## What a Manual Process Actually Is

Before running the steps, it helps to be precise about the target, because the
phrase hides the problem. "Manual process" sounds like the absence of a process.
It is not. It is a process whose rules are distributed across people's heads and
whose messages travel over channels nobody wrote down.

People text each other. Someone says "you're good to go." Someone else says "we
got the green light," and the deploy happens. On my teams the signal was
literally a thumbs up in a chat thread, and everyone knew exactly what it meant:
the checks the person had done before sending it, the conditions under which
they would not have sent it, who they would have pinged instead.

That is the part worth noticing. The message is one emoji; the process behind
the message is enormous. A human sent that signal after running an unwritten
checklist, and that checklist is the actual system. The manual part is not the
typing. The manual part is a person holding a model of the whole thing and
making a judgment call.

So "let's automate the green light" is never a proposal to automate a message.
It is a proposal to externalize somebody's model of the system, and you usually
have no idea how big that model is until you are halfway through.

## Step 1: Make the Requirements Less Dumb

Start with why the step exists, and insist on a name.

"Compliance requires a manual approval before production deploys" is not an
auditable statement. It is a sentence that has survived because no one can be
blamed for repeating it. "Dana requires it, and here is the incident in 2021
that made her ask for it" is auditable. You can go find Dana. You can find out
whether the control she wanted is the control you are performing, which in my
experience is roughly a coin flip.

The failure mode here is specific to software and worth naming: the requirement
outlives the person, the incident, and sometimes the system. A manual step gets
added to compensate for a deploy pipeline that had no rollback. The pipeline
gains rollback two years later. The manual step stays, because removing it would
require someone to claim ownership of the removal, and the step costs ten
minutes a week, which is never worth a fight.

Attaching a name is how you break that. Requirements with owners can be
renegotiated. Requirements owned by "the process" cannot.

## Step 2: Delete the Step

Try to remove it entirely, and expect to put some of it back.

The ten percent rule is the part people quote and the part people skip. If you
delete only things you are certain are safe, you were never near the boundary,
and the boundary is where the information is. Deleting a step and having to
restore it teaches you precisely what it was for, which is knowledge you did not
have before and could not have gotten by asking.

In software this is cheap in a way it never is in hardware. Removing a manual
gate for one sprint costs a revert. Removing a part from a car costs a tooling
change. The asymmetry should make software teams far more aggressive about
deletion than they actually are, and the reason they are not is social rather
than technical: the person who deletes a check owns the next incident, whether
or not the deletion caused it.

Worth being clear that deletion here means the step, not the intent. If the
manual approval existed to catch schema changes, you are not deleting the
catching of schema changes. You are deleting a human being as the mechanism.

## Step 3: Simplify What Survives

Only now, and only on what is left.

Simplification of a manual process usually means collapsing handoffs. Three
people sign off; find out whether the second one ever says no. A ticket moves
through four states; find out whether any behavior differs between two of them.
Most ugly manual processes are not complicated because the work is complicated.
They are complicated because each incident in the past added a participant and
nobody ever removed one.

This is also where you fix the shape of the signal. A thumbs up is a terrible
interface not because it is informal, but because it carries no record of what
was checked. "Approved: migrations reviewed, feature flag off, rollback tested"
is the same amount of human effort and an enormously better artifact. You have
not automated anything. You have made the process legible, which is the
precondition for everything after this point.

## Step 4: Accelerate the Cycle

Speed up the loop before mechanizing it.

Manual processes are usually slow in the waiting, not in the doing. The approval
takes thirty seconds and arrives nine hours later because the approver is in
another timezone and the request landed at the end of their day. Scripting the
thirty seconds does nothing about the nine hours. Adding a second approver in a
different timezone fixes most of it, and it is a change you can make this
afternoon.

There is a trap at this step that is specific to the modern version of this
problem: agents and tooling make it very easy to accelerate a loop that should
have been deleted at step two. Fast is not the same as valuable, and a
well-instrumented fast loop around an unnecessary step is harder to kill than a
slow one, because now it has dashboards.

## Step 5: Automate

Now, and only on what survived the four steps above.

Two things will be true if you got here honestly. The thing you are automating
is smaller than what you started with, and you can state what it is for in one
sentence. Both matter, and the second one matters more, because the automation
you can explain is the automation somebody will maintain after you move on.

The reason to put this last is not that automation is hard. It is that every
step above it changes what you would have automated. Automate first and you have
industrialized a requirement nobody questioned, a step that should have been
deleted, and a shape that was never simplified. You end up with a fast, reliable
machine for doing something that did not need doing, plus a maintenance tail you
now own forever.

And the cost is genuinely unknowable from the outside. You script the happy path
in two days and it feels fantastic, because two days of automation feels like
more progress than two days of asking questions. Then the exceptions arrive: the
team that does the step differently, the quarter-end variant, the case where the
human would have simply not sent the green light and walked over to someone
instead, and your script has no concept of "walk over to someone." Now you are
deep enough in that stopping feels like waste, so the automation grows a long
tail of special cases that is harder to maintain than the manual process ever
was.

Some processes genuinely resist automation, and that is a legitimate finding.
But you cannot tell "hard to automate" apart from "I do not understand this yet"
without doing the understanding first, and the four steps above are what
understanding looks like when it is written down.

## Why the Order Is the Whole Point

The same claim shows up in the [Quest Engine](/blog/the-meta-structure/) from a
different direction, which is part of why I trust it.

Automation is **How**. It is the Action Phase, the part where the typing
happens, and the default failure of the whole framework is starting there
because that is where progress is visible. The ROI question (what does this buy,
for whom, measured how) is **Why**, the
[Primary Directive](/blog/the-primary-directive/) that everything downstream
gets ranked against. And steps one through four are really the
[Contextual Core](/blog/the-four-ws/): who sends the signal and who accepts it,
what actually gets checked, when it fires, where the state lives when nobody is
looking at it.

A step that runs twice a year and takes ten minutes can be perfectly automatable
and still rank below everything else you could do. Without the directive there
is no ranking, so the step you automate ends up being whichever one annoyed you
most recently. That is not a strategy, it is a mood.

## The Part Worth Keeping

Run the process yourself for a few cycles before you touch it. Not observe it,
run it. Be the person who sends the green light. You will find the unwritten
rules faster than any interview does, because you will feel the moment where you
hesitate, and the hesitation is the undocumented rule.

Automating a process you do not understand is not automation. It is encoding
your current confusion at machine speed, and machines are very good at repeating
things.

The manual process is not the enemy. It is the specification, written in the
only medium it has ever existed in. Read it first, then run the algorithm, and
automate whatever is still standing at the end.
