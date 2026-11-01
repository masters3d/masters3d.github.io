+++
title = "Understand, Then Execute: Unpacking the First Word"
date = "2026-10-29"
description = "A video reduced problem solving to two steps: understand the problem, then execute on that understanding. The order is right, but the first word is overloaded. Understanding breaks into five steps with their own completion tests (what counts as solved, where you stand, the facts, the model, the test against reality), and shared understanding is a separate step again, because a team executes on as many understandings as it has people."
template = "blog-post.html"
[taxonomies]
categories = ["Engineering Systems"]
tags = ["problem-solving", "shared-understanding", "contextual-awareness", "quest-engine", "strategy", "mental-models"]
[extra]
editorial_track = "engineering-systems"
series = "quest-engine"
related = ["kernel-of-strategy", "proactive-curiosity", "cohesive-narrative", "shared-understanding-as-a-practice", "adaptive-control"]
+++

I watched a video recently that reduced every problem to a two-step strategy:
understand the problem, then execute on that understanding. It is a good slogan.
It fits on a sticky note and it is hard to disagree with. I went looking for the
video again afterwards to cite it properly and could not find it, but the search
turned up older sources that turned out to be more useful. So treat the video as
what prompted this post, not as a source.

What stuck with me was how much the first word is asked to carry. "Execute" at
least sounds like a verb you can start doing. "Understand" sounds like a state
you either have or do not, and that is where the trouble is. When someone says
"first, understand the problem," nobody can tell when that step is finished. A
step with no completion condition gets skipped (the work looks obvious, so you
start) or never ends (there is always more to read).

## The two steps were always more than two

The best-known version of this advice is George Pólya's
[_How to Solve It_](https://press.princeton.edu/books/paperback/9780691164076/how-to-solve-it),
first published in 1945. Pólya has four phases, not two: understanding the
problem, devising a plan, carrying out the plan, and looking back. Even his
first phase is not one action. He breaks it into questions. What is the unknown?
What are the data? What is the condition? Is the condition sufficient to
determine the unknown? Draw a figure, introduce notation, separate the parts of
the condition. The oldest common source for "understand first" already treats
understanding as a sequence of moves, and it already has a step after execution
(looking back) that the two-step version leaves out.

The other version that gets passed around is "if I had an hour to solve a
problem, I would spend 55 minutes thinking about the problem and 5 minutes
thinking about solutions," usually credited to Einstein.
[Quote Investigator found no evidence that Einstein said it](https://quoteinvestigator.com/2014/05/22/solve/).
The attribution is wrong, but the ratio keeps circulating because people
recognize it from their own work.

Education research names the overload directly. In the revised version of
Bloom's taxonomy, "Understand" is not one skill but a category of seven
cognitive processes: interpreting, exemplifying, classifying, summarizing,
inferring, comparing, and explaining
([Krathwohl, 2002](https://doi.org/10.1207/s15430421tip4104_2)). One word, seven
different things you might mean by it, and each one is checked a different way.
Being able to summarize a system and being able to infer what it will do in a
case you have never seen are not the same achievement.

## Unpacking "understand"

When I take the word apart against my own work, I get five steps. They line up
with parts of the framework I have been writing about on this blog, which is not
a coincidence: the framework grew out of the same complaint that "understand" is
too big to act on.

| Step                     | Question                                           | Done when                                                        | Where it lives here                                                  |
| ------------------------ | -------------------------------------------------- | ---------------------------------------------------------------- | -------------------------------------------------------------------- |
| 1. What counts as solved | What is the unknown, and what would "better" mean? | You can rank two candidate outcomes                              | [The Primary Directive](/blog/the-primary-directive/)                |
| 2. Where you stand       | Who, What, When, Where?                            | Each of the four has a specific answer someone could dispute     | [The Contextual Core](/blog/the-four-ws/)                            |
| 3. The facts             | What is true right now that is not written down?   | The questions you started with have answers from primary sources | [Context hunting](/blog/context-hunting-vs-context-gathering/)       |
| 4. The model             | How do the facts fit together?                     | You can predict a case you have not looked at                    | Cohesive Narrative                                                   |
| 5. The test              | Does the model hold against reality?               | You tried to break it and know where it bends                    | [Validation as learning](/blog/no-speedup-for-shared-understanding/) |

The first step is Pólya's "what is the unknown?" asked before the data. Without
it, every later step has no edges, because nothing tells you which facts matter.
It is also where the first step of
[Musk's algorithm](/blog/elons-algorithm-manual-process/) belongs: question the
requirement before you optimize anything.

The second step is Pólya's "what are the data, what is the condition," split
into the four questions that each fail in their own way: building for an
imagined person, scope nobody fenced, correct work delivered after the window
closed, and a component that cannot be installed anywhere.

The third step is the one most people mean when they say "understand," and it is
the least of the five. Collecting facts is not comprehension. It is also not
passive: the facts that matter are usually not lying around, which is why I
prefer hunting to gathering.

The fourth step is where Bloom's list lives. Summarizing, inferring, comparing,
and explaining are all ways of turning a pile of facts into a model you can
reason with. The test I use is prediction. If I can say what the system will do
in a case I did not trace, I have a model. If I can only repeat what I read, I
have notes.

The fifth step is Pólya's "is it possible to satisfy the condition?" turned on
your own model. It is the one I underrated longest. Reading generated code gives
me a pleasant and mostly false sense of comprehension, because it was written to
look reasonable. Running it and trying to break it is where the understanding
actually forms.

Each skipped step has a recognizable symptom. Skip the first and you solve the
wrong problem well. Skip the second and you hit the integration surprise. Skip
the third and the model is built on whatever was handy. Skip the fourth and you
have facts with no predictions. Skip the fifth and you execute on a model that
was never checked. "We didn't understand the problem" is true of all five, which
is exactly why it is not a useful diagnosis.

## Understanding is not yet shared understanding

All five steps can happen inside one head. Most problems worth the effort are
executed by more than one, and this is where the slogan breaks a second time.
"Execute on that understanding" assumes there is one understanding. On a team
there are as many as there are people, and each person executes on the one they
hold.

Shared understanding is a different thing, not a larger amount of the same
thing. Herbert Clark and Susan Brennan's
[_Grounding in Communication_](https://web.stanford.edu/~clark/1990s/Clark,%20H.H.%20_%20Brennan,%20S.E.%20_Grounding%20in%20communication_%201991.pdf)
(1991) describes common ground as the mutual knowledge, beliefs, and assumptions
that people in a joint activity rely on, and grounding as the collaborative
process of establishing that what was said has been understood well enough for
current purposes. Two parts of that definition matter here. Grounding needs
evidence from the other side: rereading your own document does not tell you
whether someone else understood it. And the bar is "well enough for current
purposes," which is a completion test, not a demand for perfect agreement.

Unpacked the same way, shared understanding has three steps of its own. First,
externalize: put the model somewhere outside your head where others can see it,
which is why a
[story map on a shared wall](/blog/user-story-mapping-shared-understanding/)
beats a three-hour meeting. Second, ground: get evidence back. Someone restates
it, predicts a case with it, or disagrees with it. A document nobody argued over
is still one person's assumptions. Third, maintain: when reality changes, the
shared model has to change with it, or the team quietly goes back to private
versions.

The completion test is not "everyone read it." It is closer to this: two people
independently make the same call about a case the document did not cover. And
this is the part with a hard rate limit. Agents made producing a change much
faster. They did not make a colleague absorb that change much faster, which is
the argument in
[There Is No Speedup for Shared Understanding](/blog/no-speedup-for-shared-understanding/).

## Putting the strategy back together

Rewritten with the parts named, the two-step strategy reads: decide what counts
as solved, locate yourself, hunt the facts, build a model, test it, ground it
with the people who will act on it, then execute, then look back. That is longer
than a sticky note, but every step now has a way to tell when it is done.

It also lines up with the [Quest Engine](/blog/quest-engine-introduction/) more
closely than I expected when I started. Everything before "execute" is
Contextual Awareness (Search), with shared understanding as its last sub-step.
"Execute" is Clear Strategy (Drive), and Pólya's split between devising a plan
and carrying it out is already a hint that it needs unpacking too. Pólya's
"looking back" is Systematic Improvement (Renew), the column the two-step slogan
cuts off. And because, as [the meta structure](/blog/the-meta-structure/)
argues, every step contains the whole shape again, "understand" has its own
search (the facts), its own drive (the model), and its own renew (the test and
the grounding). That is why it was never a single step.

I am not claiming five is the right number. Bloom has seven processes, Pólya has
a handful of questions, and I suspect a different kind of work would split the
word differently. The claim is narrower. "Understand" is a composite, and a
composite step needs named parts with completion tests or it gets skipped. And
when more than one person executes, individual understanding is necessary but
not sufficient.

The video had the order right. Understanding comes before execution, and the
work goes badly when the order flips. What it got wrong is the size of the first
step. The next time someone tells me to "first understand the problem," I want
to ask which part they mean.
