+++
title = "Context Hunting vs Context Gathering"
date = "2026-05-05"
description = "Why the word 'hunting' matters: context doesn't just lie around waiting to be picked up. Real context requires active investigation, tracing code, chasing state transitions, and turning what you found into something the whole team can use."
template = "blog-post.html"
categories = ["productivity", "workflow", "engineering"]
tags = ["context", "knowledge-management", "high-agency", "documentation", "workflow"]
+++

I've started replacing the phrase "context gathering" with **"context hunting"**
in how I talk about this kind of work. The word swap is small. The mindset shift
is not.

Gathering implies that context is already out there, loosely scattered, waiting
to be collected. Like picking up seashells on a beach. You walk around, you
crouch down, you put things in a bucket. The context is just... there.

Hunting is different. Hunting means the thing you're after is not lying around.
It's hidden. It might be moving. It requires patience, skill, and a willingness
to go somewhere uncomfortable to find it. **You don't find context because it
was sitting in plain sight. You find it because you went and chased it.**

## The Hunt Looks Like This

The other day, someone asked me about a very specific way a system gets into a
particular state. One of those questions that's deceptively narrow on the
surface but implies a whole chain of events underneath.

My honest answer: I didn't know.

But I knew something else: **the code exists**. The system is in production. The
behavior happens. Whatever causes it is written down somewhere in the codebase,
because code is the only thing that actually runs.

So I went to the code.

I started from the state in question and worked backwards. What writes to this
field? What triggers that function? Which callers pass this flag? I read through
the logic, followed the branches, traced the transitions. I wasn't reading
documentation (there wasn't any for this). I wasn't asking someone who might
know (that person might not exist). I was reading the primary source: the code
itself.

After working through it, I could describe exactly how the system arrives at
that state. The sequence of events. The conditions that have to be true. The
edge cases. I had extracted from the code something that wasn't written down
anywhere else.

I wrote it up, put it on the wiki, opened a PR, and now the team has that
context permanently. The next person who asks that question gets an answer in
seconds, not an investigation.

**That's context hunting.** You start with nothing except the belief that the
answer exists somewhere. You go find it. You bring it back and make it
permanent.

## Why "Gathering" Gets It Wrong

The word "gathering" has a quiet problem: it implies someone else created the
context and you're just picking it up.

In a mature, well-documented codebase, sometimes that's true. There's a wiki
page. There's a design doc. There's a comment in the code that explains why
things work this way. You "gather" it. Fine.

But most of the interesting questions (the ones people actually ask you) are
interesting precisely because the context doesn't already exist in a form you
can just consume. The behavior is emergent. The state was never explicitly
documented. The reason it works this way got lost when the person who built it
left the team. **The context is latent, embedded in behavior and code, and it
takes work to surface it.**

Calling that "gathering" undersells what's required. It makes the process sound
passive, almost accidental. "I gathered context while working on the ticket."
What actually happened? You spent forty-five minutes tracing calls across four
services, figured out why the retry logic behaves differently under a specific
race condition, and documented it so no one ever has to do that again. That's
not gathering. **That's hunting.**

The word signals something important about what the work actually demands:
**agency, curiosity, and a willingness to go into the unknown rather than wait
for someone to hand you the answer.**

## The High-Agency Version

There's a broader principle here that I keep coming back to: **low-agency
behavior waits for context to arrive, high-agency behavior goes and gets it.**

When you're stuck because you don't understand how something works, the
low-agency move is to block yourself on the ticket and wait for someone to
explain it. The high-agency move is to go read the code, run the thing, trace
the logs, form a hypothesis, test it. You might be wrong. You'll definitely
learn something. And when you do track down the answer, you document it.

The documentation step is non-negotiable. This is what separates a private hunt
from a team asset. If you figure out how something works and keep it in your
head, you've helped yourself once. If you write it up and put it somewhere the
team can find it, you've permanently reduced the number of future hunts your
team has to go on for that question. You turned your investigation into
infrastructure.

This is why I always pair the hunt with a PR (or at minimum a wiki edit). The
effort was already spent. The cost of writing it down is small. **The
compounding value of having it documented is high.** Three months from now when
someone else asks, they get the answer immediately. A year from now when you've
forgotten, you can look it up yourself.

Think about how an actual hunt works. Finding the prey is step one, but it is
not the end. You have to field-dress the catch, pack it out, keep it cold, and
transport it back in a form the whole party can actually use. If you track
something down and leave it where it fell, the hunt was wasted. **Context
hunting works exactly the same way.** The trace you ran through the codebase,
the state transition you reconstructed, the conditions you mapped out (that's
the catch). The wiki page, the PR, the write-up someone else can read and
immediately understand (that's dressing it and bringing it back). Context that
lives only in your head is a catch left in the field. The documentation is how
you make it distributable.

## What Gets Better When You Hunt

When teams operate in gathering mode, they develop a kind of learned
helplessness around missing context. "We don't really know why it works this
way." "That knowledge left when Alex left." (Alex is a placeholder name here,
not anyone in particular.) "It's just one of those things." These become
explanations that close the loop instead of open it.

Hunting mode treats those statements as the start of a hunt, not the end of a
conversation. "We don't know why it works this way" means: the answer is in the
code, let's go find it. "That knowledge left when Alex left" means: the behavior
still exists, and behavior is traceable. "It's just one of those things" means:
nobody has hunted for it yet.

And increasingly, you don't have to hunt alone. Agents with the right skills
(code search, documentation search, semantic analysis) can take on a substantial
part of the tracking work. You give an agent a starting point and it ranges
through the codebase, traces call chains, surfaces relevant patterns, and brings
back candidates for you to evaluate. That's the hunting dog: it covers ground
faster than you can on foot. But you're still directing. You decide where to
start, what counts as a valid find, and when to call it back. **The human role
shifts from tracker to hunt director.** You guide the search party. You make the
judgment calls about what's worth pursuing and what isn't. And you become the
essential piece in the places the tools can't reach (the ambiguous, the
contextual, the "why does this feel wrong" that no search query surfaces on its
own). The agent finds the code. The human knows which code matters, why it
belongs in the documentation, and what the team actually needs to understand
from it.

**You can't always hunt everything at once.** But when someone asks a question
you can't answer, and you know the answer exists somewhere in the system, that's
the moment to go hunting rather than shrugging. The question is a signal. The
question is where the hunt starts.

The difference between a team that accumulates context and a team that
perpetually re-investigates the same mysteries often comes down to this: one
hunts and documents, the other gathers what's already there and stops at the
boundary of what's documented.

Context hunting builds the documentation that makes future gathering possible.
It's not the opposite of gathering (eventually you'll want to just grab the wiki
page). It's what has to happen first, in all the places where the documentation
doesn't exist yet.

**Go find the context. Bring it back. Write it down. That's the whole job.**
