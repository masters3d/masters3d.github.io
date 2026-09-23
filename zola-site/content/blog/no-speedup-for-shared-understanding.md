+++
title = "There Is No Speedup for Shared Understanding"
date = "2026-09-23"
description = "Six months of building AI infrastructure and coaching coworkers on their agent workflows taught me the bottleneck is no longer code creation. Someone can write ten thousand lines in a day, but nobody found a way to make a colleague understand those ten thousand lines any faster than in 2019. Validation is still the vehicle through which humans actually learn a system, and that work has not been automated."
template = "blog-post.html"
[taxonomies]
categories = ["AI & Tools"]
tags = ["shared-understanding", "agents", "ai-development", "validation", "documentation", "context", "code-review", "knowledge-management", "pull-requests"]
[extra]
editorial_track = "ai-and-tools"
+++

For the last six months most of my building has been infrastructure for agents
rather than features for users: harnesses, validation environments, context
scaffolding, the plumbing that lets a model do useful work in a real repository
instead of a demo. Alongside that I spend a meaningful part of each week talking
with coworkers about their own AI usage, which is its own kind of telemetry. You
see the same discoveries arrive in different people a few weeks apart, and you
see the same wall.

The wall is not code generation. That problem is, for my purposes, solved. I can
produce more change than I could two years ago by a margin that still surprises
me, and so can most of the people I talk to. What I did not predict is where the
line formed afterward. Someone can write ten thousand lines in a day. Nobody has
found a way to make a colleague understand those ten thousand lines any faster
than they could in 2019.

## The rate nobody improved

I want to state this as plainly as I can, because I think it is the part most
people have not absorbed: shared understanding has no speedup.

Every other step in the pipeline got cheaper. Drafting got cheaper. Refactoring
got cheaper. Writing tests got cheaper. Reading a system into your own head did
not. The input rate into a human brain is roughly what it was, and it is low.
You can skim, you can ask an agent for a layered summary, you can get a decent
high-level map in ninety seconds instead of an afternoon, and all of that is
real. But assimilation is not retrieval. The summary arrives fast and then sits
there while you do the slow part, which is building a model you can reason with
later, under pressure, when something breaks at 2am.

I want to be careful with the claim. It is not literally zero. Agents genuinely
compress the search: they tell you which of the twelve files matter, they
translate an unfamiliar subsystem into terms you already hold, they let you
choose where to go deep. Call it a modest constant factor on comprehension. The
trouble is what it sits next to. Production went up by something closer to an
order of magnitude. A modest improvement in understanding against a large
improvement in output is, in practice, a widening gap, and a gap that widens is
the thing you feel, not the ratio you can defend on a whiteboard.

There is a corollary people skip. If you can write features faster, you can
write bugs faster, and by the same multiple. Generation is indifferent to
correctness. The defects arrive at the new speed while the capacity to notice
them stays at the old one. That asymmetry is the actual risk in agentic
development, and it is not a risk about model quality.

The other thing that did not get faster is everything around the code. Writing
the message that explains the change to your team still takes as long as it
takes. Deploying takes what deploying takes. Validating takes what validating
takes. I can generate a change in twenty minutes and then spend two days getting
it understood, confirmed, and safely in front of people, and the two days are
not waste. They are the job now.

## Validation is how humans learn a system

Here is the part I did not expect and now believe firmly: the validation work is
not just a gate on correctness. It is the primary vehicle through which I
understand my own systems.

When I read generated code, I get a pleasant and largely false sense of
comprehension. Everything looks reasonable, because it was written to look
reasonable. When I run it against real pathways and try to break it, something
different happens. I find where it holds and where it does not. I find the edge
case nobody specified. I find the dependency that behaves differently under
load. Those discoveries stick in a way that reading never produced for me,
because I paid attention differently while I was hunting for a failure. This is
[context hunting rather than context gathering](/blog/context-hunting-vs-context-gathering/),
turned on my own output.

Notice what this does to an argument I made earlier this year. In
[Shift Left Until the PR Is Just a Confirmation](/blog/shift-left-synthetic-environments/)
I argued that the bottleneck had moved from writing code to trusting it, and
that the fix was to front-load rigor into a synthetic environment so validation
becomes cheap. I still think that is right about trust. I now think it is
incomplete about people. Automating the proof and automating the understanding
are different problems, and only the first one is tractable. A pipeline can
certify that a change is correct and leave exactly zero context in anybody's
head, mine included. If I let the machine do all the validating, I get correct
code I do not understand, which is a worse position than it sounds.

So I have stopped treating hands-on validation as a cost to be engineered away.
Some of it should be (the repetitive parts, the regression surface, everything
that is cheap locally and expensive in production). But the first pass, where I
am actively trying to falsify the thing and asking an agent to explain in plain
terms what the workflow does at a high level, is where my understanding is
manufactured. I do not need to read every line. I have let go of that. I need
the shape, the edge cases, the limits of the technology, and what happens when
it fails.

## The work is making knowledge cheap to consume

All of this has changed what I think quality means, and it costs me more time
rather than less.

It is more work to split a large pull request into small ones. I have carried
the mega-PR before and I know why it is tempting: the agent produced it all at
once, it works, and slicing it is tedious. I split them anyway, because a small
change is cheap to revert when it turns out to be wrong at 2am, and a large one
is an incident. It is more work to write documentation alongside the code rather
than after, and more work still to go back and read what I wrote. I do both,
because the documentation written at the moment the code was written is the
highest-value artifact I produce that week. It carries the reasoning while the
reasoning is still in my head. It is what my colleagues will actually read, and
increasingly it is what the next agent will read to get grounded (which is the
argument in [Context as Code](/blog/context-as-code/), now with a second
audience).

The reframe I have landed on is this. The question is no longer whether the code
is good. The question is how cheaply this knowledge can move into other people's
heads. Consumability is the scarce property. When ten thousand lines a day is
achievable, the constraint on the team is the rate at which understanding
diffuses, and every design choice should be evaluated against that rate: smaller
PRs, docs written in the same session, a clear high-level story about what the
system does and where it breaks.

None of that is a novel technique. The novel part is that it used to be hygiene
and is now the actual bottleneck, which means it deserves the engineering
attention we used to spend on writing the code faster.

What I am least sure about is how durable this is. This is six months of my own
practice plus a lot of conversations, not a controlled result, and the honest
boundary is that I am describing a constraint I feel rather than one I have
measured. If someone builds tooling that genuinely raises the rate at which a
team absorbs a system (not summarizes it, absorbs it), I will revise this. I
would watch for one specific signal: a team where a large generated change is
routinely understood well enough by three people to be safely modified a month
later. I have not seen that yet. Until then I am going to keep treating the slow
human work (validating, documenting, explaining, splitting) as the part of the
job that is still mine.
