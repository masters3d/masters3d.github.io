+++
title = "Hypothesis-Driven Agent Experiments"
date = "2029-02-15"
draft = true
description = "Agent experiments need predictions before the run, logs during the run, and skepticism afterward. Otherwise a design proposal can turn into a success story without evidence."
template = "blog-post.html"
[taxonomies]
categories = ["Software Engineering"]
tags = ["agents", "research", "validation", "feedback-loops", "ai-development"]
[extra]
editorial_track = "software-engineering"
related = ["testing-systems-that-change-themselves", "cognitive-continuous-integration-and-the-broken-agent-loop", "meta-learning-four-levels"]
+++

The experiment notes from December 2024 have a structure I wish more agent work
had: a hypothesis, specific predictions, a methodology, an activity log, and
thinking records. The content around it is still very aspirational. It claims an
agent might develop an engineering concept while improving its own development
method. I would not treat the notes as proof that happened. I would treat their
structure as the useful part.

Agent systems are especially good at generating plausible stories after the
fact. They can explain why a run succeeded, why a failure was instructive, and
why a new process is better. That is exactly why the experiment needs a
hypothesis before the run.

## Predictions Before the Work

The December notes make predictions: developing content while improving process
may slow work first and accelerate it later; patterns discovered in one concept
may transfer; each iteration may become measurably better. Those are not
results. They are bets.

That separation matters. A hypothesis is allowed to be wrong. A retroactive
explanation is harder to challenge. If the agent writes the goal after seeing
its own output, almost anything can look like progress.

A good agent experiment should say what it expects, what would count as
evidence, and what would weaken the claim. For example: if a new strategy is
supposed to improve a design workflow, define the comparison. Is it faster?
Clearer? Easier to review? More complete? Less likely to drift? Without that
decision up front, the system can choose the metric that flatters the run.

This is the same habit I want in software work with agents generally. Do not ask
only whether the agent completed the task. Ask what claim the task was meant to
test.

## Logs During the Work

The methodology emphasizes thinking records, decision rationale, pattern
recognition, and regular reflection. Again, the phrasing is grand, but the
engineering instinct is right. Agent runs need traceability while they are
happening, not just a polished summary afterward.

A useful log records the decision point, the options considered, the reason for
the choice, the validation that followed, and any uncertainty that remains. That
is not because logs are inherently virtuous. It is because later review needs
evidence. If an agent changes process, writes memory, or claims a learning, the
reviewer needs to see where that came from.

The activity log says documentation requirements forced clearer structure. That
may be true for that run, but the notes do not prove a general law. The safer
statement is narrower: logging created a review surface. It made the run easier
to inspect. Whether it improved the work would require comparison across enough
similar tasks to matter.

The August 2025 GitHub Actions experiment reinforces this. Session records
helped debug the workflow, but they were not the deliverable. Logs are
diagnostic instruments. They should support review, not replace it.

## Skepticism After the Work

The December notes also name risks: cognitive overload, process recursion,
quality degradation, confirmation bias, scope creep, and documentation overhead.
That list may be the strongest part of the experiment design.

Confirmation bias is the risk I would put first. An agent evaluating its own
improvement is both participant and analyst. That does not make the work
useless, but it means the standard of evidence has to be higher. Human review,
held-out tasks, baseline comparisons, and explicit failure criteria are not
bureaucracy. They are how the experiment avoids congratulating itself.

Process recursion is another real danger. A system that keeps asking how to
improve the improvement process can stop doing the actual work. Time boxes help
because they force a choice: learn enough to make the next run better, then
return to the task.

The practical pattern is simple. State the hypothesis before the run. Record the
decisions during the run. Review the evidence after the run against the original
prediction. Keep the learning only if the evidence is good enough, and label it
as local if it has only been seen once.

That is how I would translate the experiment notes into engineering practice.
The valuable artifact is not the claim that the agent became more cognitive. The
valuable artifact is a way to prevent an agent experiment from turning every
output into a win. Predictions, logs, and skeptical review keep the story
honest.
