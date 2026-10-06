+++
title = "Automate Last: What the Quest Engine Says About the Manual Process"
date = "2026-10-06"
description = "Automation is the most satisfying thing to start with and almost always the wrong thing to start with. A manual process is not an absence of a process, it is a process whose rules live in people's heads and get passed around as 'you have the green light.' Read through the Quest Engine, automating first is jumping to How, and Musk's five-step algorithm puts automation last for the same reason."
template = "blog-post.html"
[taxonomies]
categories = ["Quest Engine"]
tags = [
  "quest-engine",
  "automation",
  "manual-process",
  "roi",
  "five-ws",
  "primary-directive",
  "process",
  "systems-thinking",
]
[extra]
editorial_track = "quest-engine"
series = "quest-engine"
+++

Someone says "we have a manual process here" and everyone in the room hears the
same thing: a defect, something embarrassing, a thing to be scripted away by the
end of the quarter. I have been that someone. The instinct is strong and it is
almost always the wrong first move.

What I want to pull apart is why, and the clearest way I have found to say it is
through the [Quest Engine](/blog/the-meta-structure/). Jumping straight into
automation is jumping straight to **How**, and the three steps are in the order
they are in for a reason.

## What a Manual Process Actually Is

Start with the phrase itself, because it hides the problem. "Manual process"
sounds like the absence of a process. It is not. It is a process whose rules are
distributed across people's heads and whose messages travel over channels nobody
wrote down.

People text each other. Someone says "you're good to go." Someone else says "we
got the green light" and the deploy happens. On my teams the signal was
literally a thumbs up in a chat thread, and everybody knew exactly what it
meant: the checks the person had done before sending it, the conditions under
which they would not have sent it, who they would have pinged instead.

That is the part worth noticing. The message is one emoji; the process behind
the message is enormous. A human sent that signal after running an unwritten
checklist, and that checklist is the actual system. The manual part is not the
typing. The manual part is a person holding a model of the whole thing and
making a judgment call.

Which means when you say "let's automate the green light," you are not
automating a message. You are proposing to externalize somebody's model of the
system, and you usually have no idea how big that model is until you are halfway
through.

## The Failure Mode: You Find Out Too Late

Here is the shape of the thing that goes wrong, and it has happened to me more
than once.

You pick the manual step. You script the obvious path. It works on the happy
case in about two days and it feels fantastic, because two days of automation
feels like more progress than two days of asking questions. Then the exceptions
arrive. The one team that does the step differently. The quarter-end variant.
The case where the human would have simply not sent the green light and instead
walked over to someone, and your script has no concept of "walk over to
someone."

Now you are deep enough in that stopping feels like waste, so you keep going,
and the automation grows a long tail of special cases that is harder to maintain
than the manual process ever was. The cost of automating a process is not
knowable from the outside. You only learn the true shape once you understand the
whole process, and the automation attempt is an extremely expensive way to run
that discovery.

Some processes genuinely resist automation, and that is a legitimate answer. But
you cannot distinguish "hard to automate" from "I don't understand it yet"
without doing the understanding first.

## This Is the Elon Musk Algorithm, Arriving From Another Direction

Musk's five-step algorithm is well traveled by now, and the ordering is the
entire content of it:

1. Make the requirements less dumb (and attach a name to each one).
2. Delete the part or process step.
3. Simplify or optimize.
4. Accelerate cycle time.
5. Automate.

Automation is step five. Not because it is unimportant, but because every step
above it changes what you would have automated. If you automate first, you have
industrialized a requirement nobody questioned, a step that should have been
deleted, and a shape that was never simplified. You end up with a fast, reliable
machine for doing something that did not need doing.

The part of that list I think gets underweighted is the first one, where the
requirement has to carry a person's name rather than a department's. "Compliance
requires it" is not auditable; "Dana requires it, here is her reasoning" is. In
practice half of what makes a manual process ugly is a requirement whose owner
left the company two years ago.

The five steps and the three steps are not rival frameworks. They are the same
claim from different angles, which is part of why I trust it.

## The Quest Engine Reading

The Quest Engine ordering is **Why → Who/What/When/Where → How → Why**. Map
automation onto that and the diagnosis is immediate.

**Automation is How.** It is the Action Phase: tooling, execution, the part
where typing happens. The [default failure](/blog/the-meta-structure/) of the
whole framework is starting at How, because How is where progress is visible.
Automating a manual process is the purest expression of that default I know. It
even comes with a virtuous story attached, which makes it harder to catch than
ordinary thrash.

**The ROI question is Why.** The
[Primary Directive](/blog/the-primary-directive/) is what everything downstream
gets ranked against, and the ranking question for automation is not "is this
automatable" but "what does automating this buy, for whom, measured how." A step
that runs twice a year and takes ten minutes can be fully automatable and still
rank below everything else you could do. Without the directive there is no
ranking, so the step you automate ends up being the one that happened to annoy
you most recently.

**The process map is the Contextual Core.** Who sends the green light and who
accepts it. What is actually checked before it goes out. When it fires, and what
makes it fire early or late. Where the state lives when nobody is looking at it.
These are [the four Ws](/blog/the-four-ws/), and each one is a separate way to
be lost. Notice that none of them require writing code, and all of them are
exactly the information whose absence sinks an automation project.

**And then it loops.** How produces evidence, and the evidence audits the
directive. Automation that nobody traced back to a Why has nothing to be audited
against, which is why these projects are so hard to kill once they start: there
is no criterion that could tell you to stop.

## What To Do Instead

The practical version is boring, which is a point in its favor.

**Run the manual process on purpose, with your name on it.** Not observe it. Run
it. Be the person who sends the green light for a few cycles. You will discover
the unwritten checks faster than any interview does, because you will feel the
moment where you hesitate, and the hesitation is the undocumented rule.

**Write it down before you script it.** The written version is cheap, it is the
artifact the four Ws produce, and it is independently useful even if you never
automate. A documented manual process is already a large upgrade over an
undocumented one.

**Delete and simplify while it is still manual.** This is the step people skip,
and it is where most of the actual return is. Changes are nearly free while the
process is still made of humans and messages. They get expensive the moment they
are encoded.

**Make the decision explicit before writing code.** How often does this run, how
long does it take, what does it cost when it goes wrong, what would automating
it cost including the maintenance tail. You do not need precision here. You need
the question asked out loud, because most of the time the answer is obvious once
somebody says the numbers.

**Then automate the part that survived.** It will be smaller than what you
started with, it will have a named owner, and you will know what it is for. That
last bit matters most, because the automation you can explain is the automation
somebody will maintain after you move on.

## The Part Worth Keeping

Automating a process you do not understand is not automation. It is encoding
your current confusion at machine speed, and machines are very good at repeating
things.

The manual process is not the enemy. It is the specification, written in the
only medium it has ever existed in. Read it first.
