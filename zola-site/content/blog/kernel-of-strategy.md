+++
title = "The Kernel of Strategy"
date = "2027-04-15"
description = "Rumelt's kernel of strategy is diagnosis, guiding policy, and coherent action. Run it against the Quest Engine and two parts line up cleanly, one part sits in a place the Quest Engine predicts, and two differences are worth more than the matches: the kernel has no Why and no Renew."
template = "blog-post.html"
[taxonomies]
categories = ["Engineering Systems"]
tags = ["strategy", "contextual-awareness", "guiding-policy", "clear-strategy", "systems-thinking"]
[extra]
scheduled = true
editorial_track = "engineering-systems"
related = ["guiding-policies-behavior-alignment", "philosophy-manifesto-principle-north-star", "directed-intentionality"]
+++

In May 2024 I wrote a short note while reading Richard Rumelt's
[_Good Strategy / Bad Strategy_](https://www.penguinrandomhouse.com/books/208668/good-strategy-bad-strategy-by-richard-rumelt/).
It was a list of three words and three arrows:

> Kernel of Strategy: Diagnosis, Guiding Policy, Coherent action.
>
> There is an interesting connection between Diagnostic and Contextual
> Awareness, Coherent Action to Clear Strategy (Recursive), Guiding Policy to
> Intrinsic Motivation. Though guiding policy expands beyond being intrinsic.

I want to take that note literally and run it against the
[Quest Engine](/blog/quest-engine-introduction/), the way I ran
[Boris Cherny's three prompting directives](/blog/goal-effort-verification-three-directives/)
against it. Not to fold Rumelt into my framework. The kernel is older, sharper,
and was built for a different job. The point is to see which parts are the same
idea seen from two directions, and which parts are different ideas that happen
to sit next to each other.

The short version: two arrows in my note hold up. The third lands somewhere more
interesting than where I put it. And the two places where the kernel and the
Quest Engine disagree are more useful than the three where they agree.

## The kernel, in Rumelt's words

Rumelt's claim, which he also laid out in a
[2011 McKinsey Quarterly article](https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/the-perils-of-bad-strategy),
is that most of what organizations call strategy is not strategy. It is goals,
slogans, and wish lists. A real strategy has a kernel of three parts:

- **Diagnosis.** A judgment about what is going on: which challenge matters
  most, simplified enough to act on.
- **Guiding policy.** The overall approach chosen to deal with that challenge.
  It rules some moves in and many moves out.
- **Coherent action.** Coordinated steps that carry out the policy and reinforce
  each other instead of pulling apart.

He also names what bad strategy looks like: fluff, failure to face the
challenge, mistaking goals for strategy, and objectives that cannot be reached.
Keep the third one in mind. It comes back below.

To keep this concrete I will carry one example through the whole post. A
platform team is "too slow." Every quarter it misses its dates, and every
quarter the fix is to ask it to try harder.

## Diagnosis is Search, and specifically the synthesis half

My first arrow was diagnosis to contextual awareness, which is the Search move
in the Quest Engine. That holds, but it is more specific than I wrote.

Search has three steps: proactive curiosity (find the information), cohesive
narrative (build a model of what it means), and shared understanding (get the
team to hold the same model). Diagnosis is not the first step. A pile of
metrics, incident reports, and survey results is not a diagnosis. Rumelt is
explicit that a diagnosis is a judgment that simplifies. That is the cohesive
narrative step: the moment a heap of facts becomes one story about what is
actually going on.

In the example, "the team is slow" is a label, not a diagnosis. A diagnosis
would sound like this: _two thirds of the team's tickets cross an ownership
boundary with another team, and every crossing waits for a review nobody has
planned capacity for._ That sentence came from
[hunting context](/blog/context-hunting-vs-context-gathering/), not collecting
it: tracing where the tickets actually stalled. It points at a system, not at
people, and it already suggests what kind of move would help.

The Quest Engine adds one thing Rumelt only implies. A diagnosis held by one
leader is half done. If the team does not share it, the guiding policy that
follows will look arbitrary to the people who have to carry it out. Shared
understanding is the step that turns a leader's diagnosis into a team's.

## Coherent action is Drive, and the recursion is the point

My second arrow was coherent action to clear strategy, which is the Drive move,
and I wrote "recursive" next to it. That word is the part of the note I would
keep.

Rumelt's coherence means the actions fit together. In the Quest Engine,
[every step contains the whole shape again](/blog/the-meta-structure/): a
quarter, a sprint, and a single pull request each have their own why, their own
locating, and their own execution. Put those two ideas together and coherence
gets a precise test. The strategy is coherent when the same shape survives at
every scale. If the quarterly plan says "review capacity is the constraint," the
sprint plan has to reserve review time, and the pull request has to be small
enough to review in that time. When the shape breaks at one level, the strategy
exists only at the altitude where nobody has to make a tradeoff.

There is a second match inside Drive. Rumelt argues that a leader's job is to
turn a distant, ambiguous ambition into a proximate objective: a near target the
team can reasonably be expected to hit. That is challenge matching, the first
step of Drive, almost word for word. A target far past the team's capability is
anxiety. A target well inside it is boredom. "Ship the new platform" is not
proximate. "Cut cross-team review wait from five days to one by the end of the
quarter" is.

## Guiding policy is the directive one level down

My third arrow was guiding policy to intrinsic motivation, with a hedge: "though
guiding policy expands beyond being intrinsic." I think the hedge was right and
the arrow was pointing at the wrong thing.

The arrow has some truth in it. A good guiding policy rules out a class of moves
without prescribing every move, which leaves room for autonomy. It connects
local choices to a larger reason, which is purpose. Repeated choices under a
clear policy build judgment, which is mastery. So a good policy feeds all three
motivations. But that is an effect of the policy, not what it is.

Here is where it actually sits. In the Quest Engine,
[each level's directive is issued by the level above it](/blog/the-meta-structure/).
The [Primary Directive](/blog/the-primary-directive/) says what counts as better
at the top. Inside the How, there has to be a smaller directive that says what
counts as better _for this piece of work_. A guiding policy is exactly that: the
directive the strategy hands down to the people doing the actions. That is why
it sits between diagnosis and action in Rumelt's kernel. It is the hinge where
Search becomes Drive.

In the example, the guiding policy might be: _every shared surface has one named
owner, and that owner's review time is planned work._ It does not say who owns
what or how reviews run. It says which kind of answer counts as better, and it
rules out the default answer, which was "ask the team to try harder."

That also explains the hedge. Because a guiding policy is a directive, it does
not only work through motivation. It also binds the extrinsic system: budgets,
planning templates, review expectations, and who gets promoted. A policy that
says "ownership is planned work" while the promotion process only rewards new
launches is the pattern I described in
[Promotion-Driven Development](/blog/promotion-driven-development/). The
incentive wins, and the policy becomes a sentence on a slide.

## Where they differ: the kernel has no Why

Here is the first real difference. The Quest Engine starts with Why: the
directive that decides what counts as better. Rumelt's kernel starts with
diagnosis. And one of his marks of bad strategy is mistaking goals for strategy.

These look like they conflict. I do not think they do, but the gap is
instructive. The Primary Directive is not a strategy, and Rumelt would be right
to call it fluff if someone presented it as one. "Our engineers should do their
best work" is a fine Why and a useless strategy. What the Why does is make the
diagnosis possible. A challenge is only a challenge relative to something you
want. "Review wait is five days" is a fact. It becomes the crux only because the
team's directive says that shipping safely to other teams is what counts.

So the two models answer different questions. The Why answers "what are we
optimizing for?" The kernel answers "given that, what is in the way, and what
are we going to do about it?" Rumelt does not need a Why step because his reader
is usually a leader whose goal is already set. The Quest Engine needs one
because it runs at every scale, including the ones where nobody handed you the
goal.

## Where they differ: the kernel has no Renew

The second difference is larger. The Quest Engine is a loop, and
[renewal is the step I call the secret sauce](/blog/quest-engine-introduction/):
compare what happened with what you expected, find the pattern, and make the
improvement permanent. The kernel, as three parts, has no step after the action.
It reads like a snapshot: here is the situation, here is the approach, here are
the moves.

Rumelt does not ignore learning. Later in the book he treats a strategy as a
hypothesis about what will work, to be tested against what happens. But that
idea lives outside the kernel. If a team takes only the three-part kernel, it is
easy to treat the diagnosis as finished once it is written down.

The meta-structure post has a line for a structure that only passes directives
down without evidence coming back up: it is a bureaucracy, "orders with no
evidence that they are working." A kernel without Renew drifts toward that. The
diagnosis was true in January. By June the review wait is down to a day, the
crux has moved somewhere else, and the team is still executing a policy aimed at
last quarter's problem. Like the
[tiger beetle that has to stop to see](/blog/pause-scan-sprint/), the strategy
needs a planned stop where someone asks whether the diagnosis still holds.

The Quest Engine also says the first directive is a guess and the loop is what
upgrades it. Rumelt's "strategy is a hypothesis" is the same claim. That is the
place the two models meet again, from opposite ends.

## The map, one line each

| Kernel                                       | Quest Engine                                           | Fit                                                                                      |
| -------------------------------------------- | ------------------------------------------------------ | ---------------------------------------------------------------------------------------- |
| (none)                                       | Why: the Primary Directive                             | Different job. The Why says what counts as better; the kernel assumes it is already set. |
| Diagnosis                                    | Search, especially cohesive narrative                  | Same idea. Diagnosis is the synthesis step, not the information gathering.               |
| Guiding policy                               | The directive one level down, between Search and Drive | Same position. Feeds intrinsic motivation, but also binds incentives.                    |
| Proximate objective                          | Challenge matching                                     | Same idea, almost word for word.                                                         |
| Coherent action                              | Drive, held coherent across every scale                | Same idea. Recursion is the test of coherence.                                           |
| (outside the kernel: strategy as hypothesis) | Renew                                                  | The kernel's biggest gap, and the Quest Engine's main addition.                          |

What I take from the exercise is narrower than "everything maps." Rumelt gives
me a sharper test for the middle of the loop: a strategy that cannot name its
crux, or whose actions do not reinforce each other, is not a strategy no matter
how good the Why is. The Quest Engine gives the kernel the two ends it leaves
open: a reason to call one challenge the crux, and a planned moment to check
whether it still is.
