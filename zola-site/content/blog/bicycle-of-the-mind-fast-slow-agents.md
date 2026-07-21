+++
title = "The Bicycle of the Mind: Fast, Slow, and Automatic Thinking About Agents"
date = "2026-07-03"
description = "Kahneman's two modes of thinking (fast System 1 and slow System 2) map onto learning to ride a bicycle. Attention gives way to automaticity, and that same arc is a methodology for thinking about agents, leverage, and engineering systems."
template = "blog-post.html"
categories = ["engineering", "ai", "learning"]
tags = ["thinking-fast-and-slow", "system-1", "system-2", "automaticity", "bicycle-of-the-mind", "agents", "leverage", "quest-engine", "systems-thinking", "deliberate-practice"]
+++

Daniel Kahneman gave us a useful cartoon of the mind: two systems. System 1 is
fast, automatic, effortless, always running. System 2 is slow, deliberate,
effortful, and expensive to run. You use System 2 to multiply two three-digit
numbers. You use System 1 to know that 2 plus 2 is 4 without feeling like you
did anything at all. Most of what feels like "thinking" is System 2 straining
against a problem. Most of what actually gets you through the day is System 1
handling everything below the waterline.

The interesting part isn't that the two systems exist. It's that things move
between them. Skills that start their life in slow, effortful System 2 can
migrate down into fast, automatic System 1. That migration has a name
(automaticity), and the cleanest example of it is learning to ride a bicycle.

## Learning to Ride a Bicycle

When you first learn to ride a bike, everything demands attention. You are
consciously managing your balance, the handlebars, the pedals, your speed, the
curb, the fear of falling, and the person telling you to just keep pedaling. It
is pure System 2. It is exhausting, and it is slow, because every one of those
variables is being held in your working memory at once and none of them is free.
You fall over precisely because System 2 cannot keep that many plates spinning
in real time.

Then something changes. You practice, you fall, you correct, you practice again.
At some point balance stops being a problem you solve and becomes a thing your
body simply does. The whole tangle of variables collapses into a single
low-level routine that runs underneath your attention. You can ride and hold a
conversation. You can ride and plan your route. You can ride and think about
something else entirely, because riding no longer needs you. The skill has moved
from System 2 down into System 1. It became automatic.

This is not forgetting how hard it was. It is the reverse. The difficulty got
compiled into a reflex. All that effortful attention you spent up front bought
you a permanent, cheap, fast subroutine you will never have to consciously run
again. That is the whole point of practice: you are not just getting better at
the task, you are moving the task to a place where it costs you almost nothing.
You are freeing up System 2 for the next hard thing.

## The Bicycle of the Mind as a Methodology

Steve Jobs called the computer a "bicycle for the mind" because a human on a
bicycle is the most efficient creature on earth. I want to push that metaphor
one step further, because the bicycle is not only a symbol of leverage. It is
also a story about how a skill becomes automatic, and that story is a useful way
to think about agents.

An AI coding agent is, right now, mostly a System 2 device that you are still
learning to ride. Early on, working with an agent feels exactly like the first
day on a bike. You are consciously managing everything: the prompt, the context
you feed it, the guardrails, the review, the fear that it will confidently do
the wrong thing. Every variable is in your working memory. It is slow and
effortful, and some people conclude the bicycle doesn't work and go back to
walking. But the arc is the same as the bicycle. With practice you stop
consciously managing each variable. You develop an intuition for what to hand
off and what to hold, for when to steer and when to let it pedal. The
collaboration migrates from effortful oversight toward something closer to
automatic, and your own attention gets freed for the parts that actually need
judgment.

There are two migrations happening at once, and it is worth keeping them
separate. The first is your skill at riding the agent becoming automatic (you,
moving from System 2 to System 1 in how you work with the tool). The second is
which work you choose to make automatic (the tasks you deliberately push down
into a reliable, low-attention routine the agent can run). This is the same
instinct behind the [Quest Engine](/blog/quest-engine-introduction/): you don't
get better by working harder against the same wall. You search for the right
next step, you act on it, and you renew your understanding, and each cycle
compiles more of the work into something you no longer have to think about. The
danger, of course, is automating something before it is actually correct. A
reflex is only worth having if it is a good reflex. You do not want to reach
automaticity on a bike that steers you into the curb.

## Back Up to Systems and Leverage

Zoom out and this stops being about bicycles or agents specifically and becomes
a fact about engineering systems in general. A good system is one that has moved
the right things into System 1. The parts that used to demand attention
(deployment, testing, environment setup, the hundred small decisions of a build)
get pushed down into automatic, low-cost routines so that the humans on top can
spend their scarce, expensive System 2 attention on the problems that genuinely
need it. This is exactly the argument from
[Leverage and the Stairs You Build](/blog/leverage-and-the-stairs-you-build/):
you build the staircase so that climbing becomes trivial, and then you walk up
without thinking, and so does everyone who comes after you.

Automaticity is what leverage feels like from the inside. The bicycle converts
the same effort into more distance. A skill compiled into System 1 converts the
same attention into more thinking. A well-engineered system converts the same
team into more capability, because it has quietly absorbed everything that used
to require someone to stand there and manage it by hand. The craft of
engineering, and increasingly the craft of working with agents, is deciding what
deserves your slow, deliberate attention today and what should become fast,
automatic, and invisible tomorrow. You learn to ride so that you can stop
thinking about riding, and then you go somewhere with it.
