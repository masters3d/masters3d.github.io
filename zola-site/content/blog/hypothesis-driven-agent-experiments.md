+++
title = "Hypothesis-Driven Agent Experiments"
date = "2027-05-08"
description = "An agent's experiment log claimed measurable improvement in the same commit that stated the hypothesis, and dated itself eight months early. A hypothesis counts only when it is written before the run, by whoever owns the goal, and checked against evidence the agent did not write."
template = "blog-post.html"
[taxonomies]
categories = ["Software Engineering"]
tags = ["agents", "research", "validation", "feedback-loops", "ai-development"]
[extra]
scheduled = true
editorial_track = "software-engineering"
related = ["safe-self-modification-for-agents", "testing-systems-that-change-themselves", "cognitive-continuous-integration-and-the-broken-agent-loop"]
+++

One folder in [my notes repository](https://github.com/masters3d/ingenio) is
named `experiments/2024-12-19_pie_theory_cognitive_development`. Its log names
the agent, INGENIO-1, and gives a start time of December 19, 2024.

Git disagrees. The repository has no commit from that day. The hypothesis, the
methodology, and the log all arrived in
[one commit](https://github.com/masters3d/ingenio/commit/747b804c3b9f6e3ddbd5319fa860060bbdb0754a)
of a pull request I merged on August 23, 2025, eight months after the date in
the folder's name. The pull request was open for two minutes, so nobody asked
about the date.

The date is the small problem. The bigger one is inside the files.

The
[hypothesis](https://github.com/masters3d/ingenio/blob/main/experiments/2024-12-19_pie_theory_cognitive_development/HYPOTHESIS.md)
predicts that each iteration of the work "will be measurably better than the
previous." The
[log](https://github.com/masters3d/ingenio/blob/main/experiments/2024-12-19_pie_theory_cognitive_development/EXPERIMENT_LOG.md),
written in the same commit, reports "Each iteration shows measurable quality
improvement" and "Recursive self-improvement is naturally emerging from the
process." None of the three files contains a number anyone measured.

So the prediction and its confirmation came from the same agent, at the same
time, with nothing measured in between. I would call that a story about an
experiment.

## The Agent Named the Risk

The hypothesis file lists its own risks, and one of them is "Confirmation Bias:
Agent confirming its own hypotheses." Its mitigations include time boxing,
quality gates, rollback, and "External Validation: Structure for human auditing
and feedback."

The plan for an audit was there. No audit followed. The log was never touched
again, and its status still says ACTIVE.

Reading it now, I count three things a hypothesis needs before I would trust a
result against it.

It is written before the run, and the history can prove it. A prediction in a
commit of its own, dated before any results, costs almost nothing. Here git
shows the prediction and the result landing together.

It is written by whoever owns the goal. The log's "Meta-Objective" is to
"Demonstrate autonomous learning and self-improvement." An agent asked to
demonstrate its own improvement has picked the result before the run starts.

It is checked against evidence the agent did not write. Timestamps from git,
results from CI, and a baseline from before the agent existed all qualify. The
agent's summary of its own run does not.

In
[Goal, Effort, Verification](/blog/goal-effort-verification-three-directives/) I
treated "how it should verify" as a definition of done that goes into the prompt
before the work starts. A hypothesis does the same job for an experiment.

## A Baseline the Agent Did Not Write

The closest I have come to that standard is a measurement, without the
prediction.

In November 2026 I had an agent count stock phrases across this blog. The
baseline was four posts I wrote between 2014 and 2020, before AI tools were part
of my writing. The older posts used 0.9 of those phrases per 1,000 words. Posts
dated 2025 on used 6.8.

The agent did the counting, but the posts it measured against were written years
before it existed. The phrase list and the script that counts uses are in the
repository. The
[voice guide](https://github.com/masters3d/masters3d.github.io/blob/master/plans/voice.md)
that reports the numbers also states its limit: "Four posts are a small sample,
so read the rows as direction, not targets."

What it lacks is a prediction. To make it an experiment, I would first commit a
prediction that posts drafted under the voice guide will use fewer of those
phrases per 1,000 words than the posts before it. If they do not, the guide is
not working, and the script would say so whether or not the agent agrees.

## Before the Next Run

I am not sure a second agent can be the external validator. Two agents on the
same model may share the same blind spots, and I have not run that comparison.

Until I have, I would set it up this way. Before an agent runs an experiment on
itself, commit the prediction on its own, name the result that would prove it
wrong, and pick evidence the agent cannot edit. Then read the log against the
prediction instead of against the agent's summary of it.
