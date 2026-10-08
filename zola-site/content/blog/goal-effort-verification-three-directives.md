+++
title = "Goal, Effort, Verification: Three Directives on the Quest Engine Map"
date = "2026-10-08"
description = "Boris Cherny's three prompting directives map onto the Quest Engine exactly: what you want is the Why (the problem statement), how it should verify is Renew (the definition of done), and how much effort is the How. The middle one is the subtle one, because effort is no longer a procedure, it is a strategy, a topology of agents, and a budget of resource plus time. The list is short because Search and execution are assumed."
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

Boris Cherny, who built Claude Code, posted a short note on how he prompts it.
Here it is in full:

> _"I am surprised that people are surprised this is how I prompt Claude._
>
> _Talk to Claude the way you would a coworker. There's no secret to prompting.
> Don't overly scaffold, don't be prescriptive for most tasks -- give Claude a
> goal, and it will figure it out._
>
> _Back in the Sonnet 3.5 days, your prompt mattered a lot. Nowadays, it's much
> more important to communicate to the model:_
>
> _1. What you want it to do_
>
> _2. How much effort you want it to spend_
>
> _3. How it should verify that it did the right thing"_
>
> — Boris Cherny,
> [Threads, posted publicly](https://www.threads.com/@boris_cherny/post/DeKrEiy)

Three fields. That is the whole prompt. I want to take the list literally and
run it against [the three steps](/blog/the-meta-structure/) I already use,
because the mapping is cleaner than I expected at the top and bottom, and much
more subtle in the middle.

The short version: directive one is the **Why**, directive three is the
**definition of done**, and directive two is the **How** — but the How
compressed into a single variable, which is the part worth unpacking.

## Read it for what it does not say

A three-item list is short because of everything it assumes, and the assumptions
here are doing more work than the items.

**It assumes the agent does its own Search.** "Don't overly scaffold" is a
statement about [contextual awareness](/blog/quest-engine-introduction/). The
elaborate prompt structures of the Sonnet 3.5 era — the decomposition, the
few-shot examples, the rigid output contracts — were a prosthetic for a Search
step the model could not perform yet. It can now. It will crawl the callers,
read the neighboring files, and locate the work on its own, which is why none of
that appears in the list.

**It assumes the agent drives.** "Give Claude a goal and it will figure it out"
means the mechanics of execution are no longer yours to specify. You do not
describe the steps. You describe the destination.

So the list is not three steps. It is the **residue** of the steps: what is left
over for the human once an agent absorbs the searching and most of the driving.
And the residue is exactly the two ends plus one dial in the middle — the
directive going in, the verification coming out, and the sizing knob that says
how hard to push between them.

That relocation is the real claim in "there's no secret to prompting." It is not
that nothing matters. The binding constraint moved out of the phrasing and into
the ends: nobody is getting worse output today because they worded something
awkwardly, they are getting worse output because they asked for the wrong thing
precisely, or because they had no way to tell whether what came back was right.
The middle is where [agents took the Drive](/blog/agents-are-taking-the-drive/).

Here is the mapping, one directive at a time.

### 1. What you want it to do → the Why, and the problem statement

This is the [Primary Directive](/blog/the-primary-directive/): the standing
order that decides what counts as better when the agent hits a fork I did not
anticipate. An agent cannot generate this. It is the one input with no
substitute.

"Add retries to the client" is a task. "This call must not drop user writes, and
I would rather be slow than lossy" is a directive, and an agent holding it will
make a defensible choice at every fork downstream without asking me. The second
version is also, in plain agile terms, a **problem statement** — what is wrong
and what better looks like, stated before anyone proposes a solution.

The agent will fill in the [four W's](/blog/the-four-ws/) underneath it — who it
is for, what is in scope, when, where it lives and what it touches — by going
and looking. That is the locating step, and it is now mostly delegable. What is
not delegable is the ranking on top of it. The agent can tell me what the change
touches. It cannot tell me which outcome is worth more. That split is the same
one I drew between the
[Why doc and the How doc](/blog/why-doc-how-doc-steering-agents-from-the-middle/)
when both readers were human.

### 2. How much effort to spend → the How, compressed into one dial

This is the directive that looks the least important and is, I think, the most
important, because it is the only place in the list where the How survives.

Effort **is** the Drive. That part maps cleanly. The subtlety is that it no
longer looks like the How used to look. The old How was procedural: do this,
then this, then that. The agent handles that now. What is left of the How is one
dial that selects the **strategy** the agent uses to get there, and a dial is a
strange-looking thing to call a step, which is why it reads like a footnote
instead of a third of the framework.

Think about automatic transmissions. An automatic will downshift for you most of
the time, and most of the time that is fine, which is the whole argument for not
scaffolding. But every modern car still ships with explicit modes: a hill
descent setting, a snow setting, a tow mode, a four-wheel-drive option that
takes the same engine and splits the power across four wheels instead of two.
Those modes exist because there are conditions where the automatic cannot infer
the right strategy from the road alone. It knows the grade. It does not know you
are towing.

An agent is in the same position. It can infer a lot from the repository. It
cannot infer how much this particular problem is worth to you, how deep the
unknowns run, or whether you want one careful pass or a search across the space.
And the strategies available at different effort levels are not the same
strategy run harder. They are structurally different shapes:

- **Low effort.** One agent, smallest change that satisfies the check, no
  exploration.
- **Medium.** One agent, but told to explore alternatives before committing, and
  to show the discarded options.
- **High, parallel.** A fleet: several agents attacking the same problem
  independently, then a comparison pass over their outputs.
- **High, adversarial.** A swarm where sub-agents critique each other's work
  before anything surfaces to me — the shape I reach for on a port of a codebase
  from one language to another, where correctness is hard to eyeball and cheap
  to check adversarially.
- **High, hierarchical.** Ten cheap agents summarize chunks, five summarize
  those summaries, two summarize again. Each individual agent is running at
  trivial effort. The aggregate is enormous.

That last one makes the point sharpest. The effort there is not located in any
single agent's intensity. It is in the **topology** — how many, arranged how,
checking whom. That is a strategy decision, and strategy is the How. Effort is
how you state it when you are not the one executing.

Which also means effort is not a quality adjective. It resolves into two
measurable things: **resource and time**. How many agents, how many tokens, how
many passes, and how long I am willing to wait for the answer. Effort is the
cost I am authorizing, and like any power budget it is finite — ten agents at
low effort and one agent at high effort can cost the same, and they buy
completely different things. Going up the mountain, you can either floor it in
the gear you are in or downshift. Same engine. Different distribution.

This is the same distinction I keep insisting on for humans, where
[effort and work are different quantities](/blog/effort-tracking-vs-task-tracking/)
that should never be tracked in the same field. A task says what. Effort says
how much of a budget it is allowed to consume. That was already load-bearing
when the budget was my own week. It is more load-bearing now, because the thing
spending the budget is not me, will not ask, and whatever it assumes is a
decision I made by staying quiet.

### 3. How it should verify → Renew, pulled to the front, as a definition of done

The third directive is [Renewal](/blog/quest-engine-introduction/) with the
timing changed.

In the framework, Renewal runs after the work: compare actual against expected,
find the root pattern, make the fix permanent. The directive version hands the
agent the verification method before it starts. Same activity, moved to the
front of the loop, so the agent can run the comparison itself dozens of times
instead of handing me an artifact and waiting for me to discover what is wrong
with it.

Stated that way it is the most familiar idea in the list: a **definition of
done**. The acceptance criteria. The test case written before the
implementation. Agile has argued for a decade that work without one is not
really defined, and an agent makes the argument unanswerable, because an agent
without a definition of done will declare victory with total confidence and
nothing behind it.

This is what makes output [proof-carrying](/blog/proof-carrying-work/) rather
than merely plausible. "Run the integration suite and show me the diff in the
failing case" produces evidence. "Make it work" produces an assertion.

What stays mine is the harder half of Renewal: deciding what the delta between
expected and actual _means_, and whether the lesson generalizes beyond this
case. The agent can run the check. It cannot decide the check was measuring the
wrong thing.

## The whole thing on one line each

| Directive                 | Quest Engine                       | Ordinary name            |
| ------------------------- | ---------------------------------- | ------------------------ |
| 1. What you want it to do | Why (the Primary Directive)        | The problem statement    |
| 2. How much effort        | How (the Drive), as strategy       | The resource + time cost |
| 3. How it should verify   | Renew, moved to the front          | The definition of done   |
| _(unstated)_              | **Search** — assumed, delegated    | —                        |
| _(unstated)_              | **Execution** — assumed, delegated | —                        |

The list is not a replacement for the three steps. It is the three steps with
the delegable parts removed. You supply the directive, you set the budget, and
you supply the check. The agent fills the middle.

Which is why "there's no secret to prompting" and "the Quest Engine still
describes this" are both true at once. The steps did not change. The division of
labor did.

This is also the second time I have read Boris Cherny and found the same engine
underneath. His
[six-step system for solving problems](/blog/i-am-often-wrong-and-the-quest-engine/)
collapses into Search, Drive, and Renew with the seams still showing, and the
part he treats as an aside — going back and redefining the plan when new
information arrives — is Renew carrying as much weight as Drive. The note above
is the same framework again, aimed at an agent instead of a team, with Search
and execution handed off. Renew survives both times, in both directions: as the
correction after, and as the definition of done before.

## What I am changing

**State the directive, not the task.** If the agent hits a fork I did not
anticipate, it should resolve it from what I wrote. If it cannot, I wrote a
task.

**Say the effort out loud, and say it as a strategy.** Not "try hard." One
careful pass, or a fleet, or a swarm that critiques itself. Name the shape and
the budget. The agent will not ask.

**Hand over the definition of done before the work, not after.** The command to
run, the condition that must hold, the evidence I expect. If I cannot state how
the work gets checked, I have not finished stating the Why either.

Of the three, effort is the one I still get wrong most often, and I think that
is because it is the only one that has no natural artifact. The Why gets a
document. The definition of done gets a test. Effort gets a sentence I usually
forget to write, and its default — whatever the agent assumed — is invisible
until the bill arrives or the work comes back three times larger than the
problem deserved.

---

_The three directives quoted at the top are from
[a public note by Boris Cherny on how he prompts Claude](https://www.threads.com/@boris_cherny/post/DeKrEiy);
the mapping onto Search, Drive, and Renew, and the gear-selection analogy, are
mine. The companion reading is
[his six-step system](/blog/i-am-often-wrong-and-the-quest-engine/). The
framework posts referenced throughout are
[The Meta Structure](/blog/the-meta-structure/),
[The Primary Directive](/blog/the-primary-directive/),
[The Contextual Core](/blog/the-four-ws/), and
[the Quest Engine introduction](/blog/quest-engine-introduction/)._
