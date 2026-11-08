+++
title = "Reward Prediction Error: Dopamine Fires on the Surprise"
date = "2027-01-15"
description = "Reward prediction error sounds like three things, but it names two: a prediction and an outcome. When the outcome beats the prediction it lands as a reward, and when it falls short it lands as an error. That gap is the teaching signal behind learning and positive reinforcement. Prediction is Search and outcome is Renew. What the name leaves out is the action in between, which is Drive, and that hidden part is where the learning gets used."
template = "blog-post.html"
[taxonomies]
categories = ["Human Systems"]
tags = ["motivation", "dopamine", "learning", "reinforcement", "feedback", "reward-prediction-error", "search-drive-renew", "quest-engine"]
[extra]
editorial_track = "human-systems"
scheduled = true
series = "quest-engine"
related = ["seeking-is-the-reward", "quest-engine-introduction", "action-feedback-adjustment", "cohesive-narrative", "iterative-integration", "deliberate-practice-for-engineers", "update-propagation", "adaptive-control", "the-progress-principle", "overjustification-effect-at-work", "objective-function-search-drive-renew"]
+++

In [Seeking Is the Reward](/blog/seeking-is-the-reward/) I started from a
five-word note I wrote on December 30, 2022: the act of building is greater than
finishing it. The explanation there was wanting versus liking. Dopamine drives
the pursuit, and the pleasure at the finish runs on smaller, briefer circuitry,
so shipping feels flat.

That answered why the finish line is quiet. It left a second puzzle right next
to it. The same kind of win does not feel the same twice. The first green build
on a hard change, the first time a talk lands, the first raise: each one lights
you up. The fifth one barely registers, even when the outcome is identical.
Nothing about the reward changed. Something about you did, and that something is
learning.

The research behind that puzzle has a three-word name: reward prediction error.
When I first lined those three words up against the three moves of the
[Quest Engine](/blog/quest-engine-introduction/), I tried to give each word its
own move, and it did not fit. It fit once I stopped counting words. The name
describes two things, and it quietly leaves out a third.

## A prediction and an outcome

In the late 1980s and 1990s, Wolfram Schultz recorded single dopamine neurons in
monkeys while they learned that a light or a tone meant juice was coming. Before
learning, the juice itself caused a burst of firing. After the monkey learned
that the cue predicted the juice, the burst moved: the neurons fired at the cue,
and the juice, now fully expected, produced no change at all. And if the cue
appeared but the juice did not, the neurons dipped below their baseline at the
exact moment the juice should have arrived.

Schultz's [2016 review](https://pmc.ncbi.nlm.nih.gov/articles/PMC4826767/)
states the rule in three cases. More reward than predicted: the neurons fire.
Exactly the reward predicted: they stay at baseline. Less than predicted: their
activity drops. As arithmetic, it is one line:

> outcome - prediction

Look at what is actually in that line. There is a prediction, made before
anything happens, and there is an outcome, which arrives afterward. Everything
else is the comparison between them. The literature calls the result a
prediction error and gives it a sign: a positive prediction error when the
outcome beats the prediction, a negative one when it falls short. I find it
clearer to say it the way I would say it about my own work. There is a
prediction, and the outcome lands as a reward (better than I expected) or as an
error (worse than I expected). "Reward" and "error" are not two separate
ingredients. They are the two directions the same outcome can land, measured
against the same prediction. A fully expected outcome lands as neither, and that
is the flat fifth win.

The boundary of the evidence matters here. Kent Berridge, whose wanting and
liking research I leaned on in the earlier post, argued in
[2007](https://doi.org/10.1007/s00213-006-0578-x) that dopamine is better
explained as the cause of wanting than as the teaching signal itself, and that
learning can happen without it. That debate is about what dopamine causes, and I
am not going to settle it. The rest of this post leans on something narrower and
older than the dopamine recordings: the idea that learning is driven by the gap
between prediction and outcome, whichever chemistry carries it.

## Learning runs on the gap

Psychologists had the rule before neuroscientists found it in neurons. In 1972
Robert Rescorla and Allan Wagner proposed a model of conditioning that Rescorla
later summarized in one sentence: learning occurs
["not because two events co-occur but because that co-occurrence is unanticipated"](https://doi.org/10.4249/scholarpedia.2237).
One of the results their model was built to explain is called blocking. Once an
animal has learned that a tone predicts food, adding a light alongside the tone
teaches it almost nothing about the light. The food was already predicted, so
there was no gap left to assign to the new signal.

Richard Sutton turned the same idea into an algorithm in
["Learning to predict by the methods of temporal differences"](https://doi.org/10.1007/BF00115009)
(_Machine Learning_, 1988). Temporal difference learning keeps a running
prediction and nudges it after every outcome:

> new prediction = old prediction + learning rate × (outcome - prediction)

In 1997 Schultz, Peter Dayan, and Read Montague put the monkey recordings next
to that update rule in
["A neural substrate of prediction and reward"](https://pubmed.ncbi.nlm.nih.gov/9054347/)
(_Science_) and showed that the dopamine neurons were firing in the shape of its
gap term.

Read the update rule slowly and it says three things about learning. The gap is
the only thing that changes the prediction. A large gap teaches a lot, a small
one teaches a little, and no gap teaches nothing. And because each update
shrinks the next gap, learning is self-extinguishing: the better you get at
predicting something, the less it can teach you. You did not stop valuing the
fifth win. Your prediction caught up to it.

## The action the name leaves out

Notice what is missing from every one of those three sources. In the cleanest
version of Schultz's experiment, the monkey does not have to do anything: the
cue appears and the juice follows. Rescorla and Wagner were modeling Pavlovian
conditioning, where the tone and the food arrive regardless of what the animal
does. Sutton's 1988 paper is titled "learning to _predict_." All three are about
learning what will happen, not about learning what to do. The action is not
wrong to leave out of those experiments; it was left out on purpose, to isolate
the prediction. But the name carried over into everyday use, and in everyday use
there is almost always an action between the prediction and the outcome.

That is where the Quest Engine lines up, and it lines up on all three moves once
the hidden one is named.

| Part       | Quest Engine move | What it does                                           |
| ---------- | ----------------- | ------------------------------------------------------ |
| Prediction | Search            | Build the model of what will happen                    |
| Action     | Drive             | Do something the world can answer (hidden in the name) |
| Outcome    | Renew             | Compare what happened with what you predicted          |

**Prediction is Search.** Search builds the context and the mental model you act
from. Its middle step, Cohesive Narrative, is literally "build accurate mental
models," and a mental model is a prediction about what will happen when you act.
A thin Search produces a vague prediction, and a vague prediction cannot be
wrong in a useful way, because there is nothing precise enough to compare
against.

**Outcome is Renew.** The [introduction](/blog/quest-engine-introduction/)
defines Renew as "examine what happened against what you expected." That
sentence is the comparison. Iterative Integration (measure results against
expectations) reads the gap, Deliberate Practice finds the patterns in it, and
Update Propagation is the update rule itself: change the model, by an amount
that fits the size of the gap, so the next prediction is better. A Renew step
that records only "it worked" has read no gap and learned nothing.

**Action is Drive, and it is the part being taken for granted.** Drive is
committing to one objective, matching the challenge to your capability, and
adjusting as feedback arrives. None of that appears in the phrase "reward
prediction error," yet in real work the outcome is almost never something that
simply happens to you. It is the world's answer to something you did. Without
the action, the gap can only update what you believe. With the action, it can
update what you do.

This is also where positive reinforcement lives. Pavlovian conditioning, the
setting of those early models, needs no action. Positive reinforcement is
defined by one: a behavior is followed by a good outcome, and the behavior
becomes more likely. Put that next to the gap and the definition gets sharper. A
consequence reinforces an action only to the extent that it lands as a reward,
better than predicted. The first unexpected thank-you from a teammate
strengthens the behavior that earned it. The tenth, arriving on schedule, mostly
maintains it. When the outcome lands as an error, repeated often enough, the
prediction drops and the action fades with it, which is extinction. (This is not
negative reinforcement, which means removing something unpleasant, like an alarm
that stops when you get up. The words collide, but the two run in opposite
directions.)

Reinforcement learning, the field Sutton helped found, made the action explicit.
Sutton and Andrew Barto's textbook,
[_Reinforcement Learning: An Introduction_](http://incompleteideas.net/book/the-book-2nd.html)
(MIT Press, 2018), describes actor-critic methods, which split the loop into two
learners. The critic learns to predict how well things will go. The actor
chooses what to do. The same gap teaches both: it corrects the critic's
prediction and shifts the actor toward actions that landed better than expected.
In Quest Engine terms, Search and Renew are the critic, and Drive is the actor.
The scientific name describes the critic. The actor is what the critic is for.

Making the action visible also exposes the hardest part of learning from
outcomes, which the field calls credit assignment. When an outcome lands as an
error, was the prediction wrong, or was the action wrong? Did I misjudge the
problem, or did I misjudge the problem correctly and then execute poorly? The
same gap can mean either, and the update is different in each case. If I only
think in terms of prediction and outcome, I will always fix my model and never
look at what I did. Adaptive Control, the last step of Drive, is where that
question gets asked while the action is still running rather than after the
fact.

Put together, the three moves turn into a short practice. In Search, write the
prediction down before acting, so there is something to compare against. In
Drive, name the action you are taking and what you expect it to cause, so the
outcome can be credited to something specific. In Renew, read whether the
outcome landed as a reward or an error, decide whether the gap belongs to the
prediction or the action, and update that one, by about as much as the gap
warrants. And be careful about announcing a reward before the work is done,
including to yourself, because the announcement moves it into the prediction and
spends the surprise early. That is one mechanism behind the overjustification
effect, where a promised reward crowds out the reason someone cared in the first
place.

In the earlier post I admitted that I once read the flat feeling after shipping
as a defect in how I was wired. The flat fifth win invites the same misreading.
The gap offers a better one: it is evidence that I learned the thing. The
prediction caught up, the outcome stopped landing as a reward, and the
restlessness that follows is the loop asking for an action whose outcome is
still in doubt. The name only mentions the prediction and the outcome, but the
action between them is the part I actually get to choose.
