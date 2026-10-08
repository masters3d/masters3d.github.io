+++
title = "Goal, Effort, Verification: Three Directives on the Quest Engine Map"
date = "2026-10-08"
description = "A widely shared note on prompting says the model now needs three things: what you want it to do, how much effort to spend, and how it should verify it did the right thing. Those three are not a prompting trick. Two of them are the Quest Engine's Why and Renew, one of them is a dial inside the Drive, and the Search step is conspicuously missing because the agent took it."
template = "blog-post.html"
[taxonomies]
categories = ["Quest Engine"]
tags = [
  "quest-engine",
  "agents",
  "prompting",
  "search-drive-renew",
  "primary-directive",
  "verification",
  "effort-tracking",
]
[extra]
editorial_track = "quest-engine"
series = "quest-engine"
+++

A note went around recently from one of the people closest to how Claude Code
actually gets built, and the surprising part was how unsurprising the advice
was: talk to the model the way you would talk to a coworker. Do not overly
scaffold. Do not be prescriptive for most tasks. Give it a goal and it will
figure out the rest. Then the part worth keeping, which is that back in the
Sonnet 3.5 days your prompt mattered a lot, and now what matters is
communicating three things:

1. What you want it to do
2. How much effort you want it to spend
3. How it should verify that it did the right thing

I want to take that list seriously rather than treat it as prompting folklore,
because when I put it next to [the three steps](/blog/the-meta-structure/) I
already use, it does not line up the way I expected it to. It lines up better.

## The ceiling moved, it did not disappear

The headline claim is that prompt craft used to be the constraint and is not
anymore. That is a ceiling argument, and ceilings are the thing I pay attention
to, because a ceiling tells you which skill is currently load-bearing and which
one has quietly stopped paying.

In the Sonnet 3.5 era the ceiling was phrasing. The model had the capability but
needed to be walked to it, so people who were good at decomposition, few-shot
examples, and rigid output contracts got visibly better results than people who
were not. That skill was real and it was scarce, which is exactly what a binding
ceiling looks like.

The models got better, and that particular ceiling lifted. What did not happen
is that the work became unbounded. The limit relocated. When the model can
figure out the mechanics from a goal, the quality of the goal becomes the
binding constraint, and the quality of the check at the end becomes the other
one. Nobody is getting worse output today because they phrased something
awkwardly. They are getting worse output because they asked for the wrong thing
precisely, or because they had no way to tell whether what came back was right.

That is the useful reading of "there is no secret to prompting." It is not that
nothing matters. It is that the scarce skill moved from the middle of the
process to both ends of it. The middle is where
[agents took the Drive](/blog/agents-are-taking-the-drive/). The two ends are
the parts that were always mine.

## The question I actually want answered

So here is the question this post exists to ask, stated plainly, because I would
rather pose it sharply than smuggle in an answer:

**Do those three directives map one-to-one onto Search, Drive, and Renew, or do
they map onto something else that only looks like the three steps from a
distance?**

My answer is the second one, and the mismatch is the interesting part. Here is
the mapping as I read it.

### 1. What you want it to do → the Primary Directive, plus the locating step

"What you want it to do" sounds like one thing and is reliably two.

The first is the [Why](/blog/the-primary-directive/): the standing order, the
thing that decides what counts as better when the agent hits a fork I did not
anticipate. This is the half that cannot be delegated and the half people skip.
"Add retries to the client" is not a directive. "This call must not drop user
writes, and I would rather be slow than lossy" is a directive, and an agent that
holds it will make a defensible choice at every fork downstream without asking
me.

The second is the [Contextual Core](/blog/the-four-ws/): who it is for, what
exactly is in and out, when it has to exist, where it lives and what it touches.
This is the locating step, and it is the one the agent will now do for me if I
let it. It will crawl callers, map the blast radius, and tell me what the change
touches. It cannot tell me what counts as better.

So directive one is not a single Quest Engine step. It is the Why with the four
W's folded underneath it, which is exactly the shape I described as the
[Why doc and the locating doc](/blog/why-doc-how-doc-steering-agents-from-the-middle/)
when the audience was human.

### 2. How much effort to spend → a dial inside the Drive, not a step

This is the one with no clean counterpart, and I think that is why it is the
most skipped of the three.

Effort is not a phase. It is **Challenge Matching**, the sizing move inside the
Drive. In the human version of the framework it is the thing that keeps work in
flow: too large and you stall, too small and you coast. With an agent the same
dial exists and it is the one almost nobody states out loud. "Take the smallest
change that makes this test pass" and "go audit every caller in the repo and
propose a migration" are the same goal at two wildly different efforts, and if I
do not say which one I want, the agent picks for me. Usually it picks
ambitiously, because ambition reads as helpful.

It also fixes a long-standing confusion I have written about in the human
context: effort and work are
[different quantities and should not be conflated](/blog/effort-tracking-vs-task-tracking/).
A task says what; effort says how much of a budget it is allowed to consume.
That distinction was already load-bearing for people. It turns out to be
load-bearing for agents too, and for the same reason. The scope of the goal does
not imply the size of the attempt.

So: directive two sits inside the Drive. It is the knob I now have to set
explicitly because the thing doing the driving is not me.

### 3. How it should verify → Renew, pulled forward into the prompt

The third one is the one I would defend hardest, and it is
[Renewal](/blog/quest-engine-introduction/) with the timing changed.

In the framework, Renewal is what happens after: compare actual against
expected, find the root pattern, make the fix permanent. The directive version
says to hand the agent the verification method up front, before it starts. That
is not a different activity. That is the same activity moved earlier, so the
agent can run the loop itself instead of handing me an artifact and waiting for
me to discover what is wrong with it.

This is also what makes the output [proof-carrying](/blog/proof-carrying-work/)
rather than merely plausible. "Run the integration suite and show me the diff in
the failing case" produces evidence. "Make it work" produces an assertion. An
agent given a verification method will iterate against it dozens of times before
I ever look, which is the entire reason the Drive became cheap enough to
delegate in the first place.

What stays mine is the harder half of Renewal: deciding what the delta between
expected and actual _means_, and whether the lesson generalizes. The agent can
run the check. It cannot decide the check was measuring the wrong thing.

## The step that is missing, and why

Line the mapping up and one thing is obviously absent:

| Directive       | Quest Engine                           |
| --------------- | -------------------------------------- |
| What you want   | Why (Primary Directive) + the four W's |
| How much effort | Challenge Matching, inside the Drive   |
| How to verify   | Renew, moved to the front of the loop  |
| —               | **Search**                             |

Search does not appear, and it is not an oversight in the advice. It is the
whole reason the advice works. "Do not overly scaffold" is a statement about
Search: the model will do its own contextual awareness now, so the elaborate
prompt structures that used to substitute for the model's own searching have
become dead weight. Scaffolding was never the goal. It was a prosthetic for a
Search step the model could not perform yet.

Which means the three directives are not a replacement for the three steps. They
are what is left of the three steps once an agent can run the Search and the
Drive on its own: you supply the directive, you set the effort budget, and you
supply the verification. The agent fills the middle.

That is the same conclusion I reached from the other direction when I noticed
agents had taken 80% of my construction. It is mildly satisfying to see someone
who builds these tools for a living arrive at the three fields a prompt actually
needs, and have them turn out to be the Why, the sizing knob, and the Renewal
criteria.

## What I am changing

Three concrete habits, which is what I actually want out of reading something
like this:

**State the directive, not the task.** If the agent hits a fork I did not
anticipate, it should be able to resolve it from what I wrote. If it cannot, I
wrote a task, not a directive.

**Say the effort out loud.** Smallest viable change, or full audit. The agent
will not ask, and whatever it assumes is a decision I made by omission.

**Hand over the verification before the work, not after.** The command to run,
the condition that must hold, what evidence I expect to see. If I cannot state
how the work gets checked, then I have not finished the directive either, and
that is the real signal.

The open question I am still sitting with is the effort dial, because it is the
one with no home. Why and Renew have posts, vocabulary, and years of practice
behind them. Effort has a sentence. If the binding ceiling has moved to the two
ends of the process, the dial in the middle is the piece most likely to be
mis-set silently, and I do not yet have a good way to talk about it other than
naming it every time.

---

_The three directives summarized here are from a public note by Boris Cherny on
how he prompts Claude; the mapping onto Search, Drive, and Renew, and any
strained analogies in it, are mine. The framework posts referenced throughout
are [The Meta Structure](/blog/the-meta-structure/),
[The Primary Directive](/blog/the-primary-directive/),
[The Contextual Core](/blog/the-four-ws/), and
[the Quest Engine introduction](/blog/quest-engine-introduction/)._
