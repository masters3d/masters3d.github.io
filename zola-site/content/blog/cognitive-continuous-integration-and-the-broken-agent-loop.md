+++
title = "Cognitive Continuous Integration and the Broken Agent Loop"
date = "2026-10-17"
draft = true
description = "INGENIO-1 was a real experiment in turning issues into specs, and the interesting lesson is not that it worked. It is that the surrounding workflow had to become an engineering system before the agent's output could be trusted."
template = "blog-post.html"
[taxonomies]
categories = ["Software Engineering"]
tags = ["agents", "continuous-integration", "specs", "github-actions", "validation"]
[extra]
editorial_track = "software-engineering"
+++

In August 2025 I opened
[issue 36](https://github.com/masters3d/ingenio/issues/36) in ingenio with a
very practical complaint: the automation that created specs from issues was
processing all issues, and it was not creating pull requests the way I expected.
The fix sounded small. Only act on the `Ingenio-1` label. Exclude pull requests.
Create a pull request instead of committing directly.

That small issue is the best source material for INGENIO-1, because it shows the
agent system at the moment where the idea met workflow reality. The repo had
cognitive system docs, experiment logs, and Software 3.0 language. But the
breakage was ordinary: a scheduler picked up the wrong things, session metadata
entered a pull request, and two workflow runs raced each other.

That is the useful lesson. Cognitive continuous integration is not proved by an
agent generating a spec. It is proved by the loop around the agent surviving
normal software failure modes.

## The First Loop Was Too Broad

The original INGENIO-1 idea was straightforward. A GitHub Actions workflow reads
issues, applies the Three Pillars Quest Engine framework, and generates a
`VISION.md` specification. The cognitive system docs describe agents with
levels, memory, learning, meta-learning, and collaboration. The experiment docs
ask the agent to log decisions, extract learnings, and improve its own process.

That sounds abstract until it touches GitHub. Then the system has to answer very
specific questions. Which issues are eligible? What branch should receive the
change? What files count as deliverable output? How does a human review the
result? What happens if the same issue is processed twice?

Issue 36 exposed the first missing boundary. Processing every open issue was too
broad. It converted the repository into an input queue with no explicit consent.
The corrected rule was better: only process issues labeled `Ingenio-1`, and do
not process pull requests. That label became the boundary between ordinary notes
and agent work.

The pull request requirement mattered just as much. A spec committed directly to
main skips the social and technical checkpoint where the author can decide
whether the generated document is useful. A pull request turns agent output into
reviewable work. It gives the system a seam.

## Then the Workflow Itself Became the Subject

The later documents are even more interesting because they stop talking about
agent capability in the abstract and start debugging the agent's environment.
`COGNITIVE_PR_PROBLEM_ANALYSIS.md` records a bad pull request that contained
only session metadata. The root cause was not that the agent failed to think. It
was that the processor used broad git operations and committed files that were
logs rather than deliverables. The fix was surgical: ignore cognitive session
metadata, add only `specs/`, and skip redundant pull requests when a spec
already exists.

`RACE_CONDITION_FIX.md` records a second ordinary failure. Two GitHub Actions
runs started almost simultaneously for the same issue. Both tried to create the
same pull request. One succeeded; the other failed because the pull request
already existed. The fix was not a deeper theory of intelligence. It was race
condition handling: catch the duplicate pull request error, look up the existing
pull request, and complete the workflow without turning a harmless duplicate
into a failed run.

This is what makes the experiment worth writing about. INGENIO-1 was supposed to
turn issues into specs. In practice, it also turned the continuous integration
workflow into a software product that needed scoping, idempotency, artifact
boundaries, and error-handling. The agent loop only became useful when the
surrounding system looked like engineering.

The validation report from January 2026 reads like a normal release note because
that is what the experiment became. Twenty validation checks passed. Seven core
tests passed. The workflow filtered labels case-insensitively, excluded pull
requests, skipped issues that already had specs, created pull requests for new
specs, and archived session logs. Those are not glamorous results. They are the
results that make the glamorous part safe to try again.

## Cognitive Continuous Integration Is a Product, Not a Prompt

The phrase "cognitive continuous integration" can make the system sound more
mysterious than it is. I think the plain version is better: an agent is allowed
to transform a human issue into a structured spec, but only inside a workflow
that preserves review, limits scope, and records what happened.

That gives the pattern a few hard requirements.

First, the trigger must be explicit. A label, command, or queue entry tells the
system that this item is ready for agent processing. Without that boundary, the
agent confuses notes with assignments.

Second, the output must be reviewable. Pull requests are not ceremony here. They
are the human judgment point. They also make the diff inspectable, commentable,
and reversible.

Third, logs and deliverables must be separate. Session traces are valuable for
debugging and meta-learning, but they are not the same as the spec the human is
supposed to review.

Fourth, the workflow must be idempotent. If the same issue is processed twice,
the second run should find the existing branch, spec, or pull request and settle
cleanly. Agent systems do not get an exemption from race conditions.

That is also why the experiment logs are not decoration. The session records,
validation reports, and race-condition notes are the memory of the workflow.
They let the next change start from what the system already learned instead of
from a vague sense that the agent once failed. The same rule applies to agents
as to any other production tool: if the failure cannot be reconstructed, the
learning will not survive.

Looking back at issue 36, I like that the first correction was not
philosophical. It was "use the label Ingenio-1" and "exclude pull requests."
That is how these systems become real. A broad cognitive ambition turns into one
small invariant, then another, then a validation script, then a race condition
fix. The agent may produce the spec, but the engineering system produces trust.
Without that system, Cognitive continuous integration is a prompt with a cron
job. With it, it becomes a loop a human can let run again.
