+++
title = "Cognitive Continuous Integration and the Broken Agent Loop"
date = "2027-10-01"
draft = true
description = "INGENIO-1 was a real experiment in using GitHub Actions to turn opted-in notes issues into reviewable VISION.md specifications. The lesson was that agent output only became useful after the workflow had explicit boundaries, review seams, and failure handling."
template = "blog-post.html"
[taxonomies]
categories = ["Software Engineering"]
tags = ["agents", "continuous-integration", "specs", "github-actions", "validation"]
[extra]
editorial_track = "software-engineering"
+++

INGENIO-1 was an experiment I ran on my own notes repository. The idea was
simple enough to sound obvious: a GitHub Actions workflow would run on a
schedule, read open issues, use the Three Pillars Quest Engine framework to
analyze them, generate a `VISION.md` specification for each issue, and comment
back on the issue with the generated artifact.

The workflow ran hourly. It also had issue-event triggers. The agent announced
when it was working, created a session record, produced a spec directory, and
posted a completion comment. In the happy-path version, an unstructured note
became a reviewable engineering document without me having to perform the same
translation by hand every time.

That is the story the experiment wanted to tell. The more useful story is what
broke.

## The First Loop Was Too Broad

The first serious problem was scope. The workflow looked at open issues as if
all of them were assignments for the agent. That made the notes repository feel
less like a place to think and more like an accidental work queue. A reminder, a
half-formed idea, and an actual request all looked eligible if the only rule was
"open issue."

The same boundary problem showed up with pull requests. GitHub's API can return
pull requests through issue-shaped endpoints, so a processor that asks for
issues has to say whether it means issues only. INGENIO-1 did not begin with
that distinction strongly enough. The fix was not a deeper prompt. It was a
smaller input contract: only process real issues, and exclude pull requests.

The second boundary was consent. The workflow needed an explicit opt-in signal.
The rule became: process only issues carrying the `Ingenio-1` label. The label
turned an ordinary note into an agent assignment. Without it, the issue remained
human context. With it, the issue entered the cognitive CI loop.

That one change made the system easier to reason about. The agent no longer had
to infer whether every open issue deserved a generated spec. The human marked
the item as ready for processing. The workflow enforced the mark.

## The Scheduler and the Race Were Part of the System

The next failure was less philosophical and more operational: some issues were
not picked up by the scheduler. The system was supposed to run every hour, find
eligible issues, and process them. When an issue with the right intent did not
move, the question shifted from agent capability to workflow mechanics.

That investigation exposed ordinary continuous-integration details. Was the
workflow file present on the default branch? Did the issue event trigger fire?
Did the scheduled run have the right dependencies? Was the label spelled in a
way the processor recognized? Did the code treat label matching
case-insensitively? The agent system depended on those mundane answers.

A later workflow fix made the dependency installation less magical. Instead of
initializing a fresh package file inside the action run, the workflow used the
repository's existing `package.json`. The accompanying notes also clarified that
scheduled runs were working, while issue-event triggers had their own rules: the
workflow had to exist on the default branch, the event had to happen after the
workflow existed, and the issue needed the opt-in label.

That is a useful lesson for agent systems. A broken scheduler and a weak prompt
can produce the same visible symptom: nothing useful happens. The repair is
completely different. In this case, the loop needed observable workflow
behavior, not more abstract agent ambition.

Once the workflow could run from more than one trigger, the next bug was
predictable. Two GitHub Actions runs could start almost at the same time for the
same issue. One run might be caused by an issue event. Another might be caused
by a label event or a nearby scheduled run. Both would decide they owned the
same work.

The visible failure was duplicate pull request creation. The first workflow run
created the branch and pull request. The second reached the same step and failed
because a pull request already existed for that branch. The agent did not need
more intelligence to fix that. The processor needed idempotency.

The race-condition fix handled the duplicate as an expected state. If pull
request creation failed because one already existed, the processor looked up the
existing pull request for the branch and returned it instead of failing the
whole run. If it could not retrieve the pull request, it logged a warning and
posted a generic completion comment rather than treating a harmless duplicate as
a fatal error.

That changed the meaning of repeated execution. Before the fix, running twice
was a failure mode. After the fix, running twice was something the system could
absorb. That is the difference between a demo workflow and an engineered loop.

Another failure came from confusing deliverables with session metadata. A pull
request was created by the cognitive CI system, but the useful `VISION.md`
specification already existed on the main branch. The new pull request contained
only session context. The description claimed a spec had been generated, but the
diff showed metadata rather than the deliverable a reviewer needed.

The root cause was broad git behavior. Adding everything meant adding cognitive
session files along with real output. The repair was surgical: ignore session
metadata, add only the `specs/` content, and skip redundant pull requests when a
spec already exists and no new deliverable content was produced.

That distinction matters because logs are still valuable. Session traces,
validation reports, and processing records are how the system remembers what it
tried. But they are not the same thing as the artifact under review. A human can
review a `VISION.md` spec. A pile of session metadata is evidence for debugging,
not the product of the loop.

## Cognitive CI Is a Product, Not a Prompt

By the time I validated the system end to end, the checklist looked like normal
software engineering. The tests covered label filtering, cognitive analysis,
framework application, spec generation, meta-learning, session management, and
pull request creation. The dry-run validation checked configuration,
dependencies, workflow structure, historical sessions, label behavior, and
recent workflow runs.

That validation was the point. INGENIO-1 was not trustworthy because it could
write a spec. It became more trustworthy when the surrounding system could say
which issues were eligible, exclude pull requests, avoid redundant work, survive
duplicate processing, separate logs from deliverables, and report what happened.

The phrase "cognitive continuous integration" can make the experiment sound more
mysterious than it was. The plain version is better: an agent was allowed to
transform explicitly labeled notes into structured specifications, but only
inside a workflow that preserved review, limited scope, and recorded the run.

That gives the pattern a few hard requirements.

First, the trigger must be explicit. A label, command, or queue entry tells the
system that this item is ready for agent processing. Without that boundary, the
agent confuses notes with assignments.

Second, the input type must be constrained. If the workflow is meant to process
issues, it must exclude pull requests. Similar-looking API objects are not the
same work.

Third, the output must be reviewable. A generated `VISION.md` belongs in a
change that a human can inspect, comment on, merge, or reject.

Fourth, logs and deliverables must be separate. Session traces are memory for
the system. They should not masquerade as the artifact the human is reviewing.

Fifth, the workflow must be idempotent. If the same issue is processed twice,
the second run should find the existing branch, spec, or pull request and settle
cleanly. Agent systems do not get an exemption from race conditions.

That is why the broken loop is the useful part of the story. A broad cognitive
ambition became one small invariant, then another: use the explicit opt-in
label, exclude pull requests, make scheduled processing observable, skip
existing specs, handle duplicate pull requests, and validate the whole path. The
agent may produce the spec, but the engineering system produces trust. Without
that system, cognitive continuous integration is a prompt with a cron job. With
it, it becomes a loop a human can let run again.
