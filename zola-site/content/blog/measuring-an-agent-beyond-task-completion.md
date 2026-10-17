+++
title = "Measuring an Agent Beyond Task Completion"
date = "2029-03-15"
draft = true
description = "Task completion is only the first measure of an agent. Useful evaluation also asks what context it preserved, what quality gates it respected, and whether future work became safer."
template = "blog-post.html"
[taxonomies]
categories = ["Software Engineering"]
tags = ["agents", "measurement", "validation", "quality", "ai-development"]
[extra]
editorial_track = "software-engineering"
related = ["hypothesis-driven-agent-experiments", "agent-memory-short-long-and-meta", "proof-carrying-work"]
+++

The generated agent profile and operating guidance include several proposed
measures for agent effectiveness: context preservation, quality consistency,
framework application, artifact completion, pull request quality, and redundancy
avoidance. A separate agent template adds task completion, quality score,
learning velocity, autonomy, collaboration, response time, and resource use.
Some of those sound measurable. Some sound like wishes waiting for a definition.

That is normal at the design proposal stage. The useful move is not to accept
the list as a dashboard. The useful move is to separate task completion from the
other things we actually care about.

## Completion Is the Shallow Metric

Did the agent finish the task? That is the first question, and it is not enough.
A system can finish by making a patch that compiles but violates the design. It
can finish by writing a document that sounds coherent but repeats unsupported
claims. It can finish by opening a pull request that contains logs instead of
the artifact a reviewer needed.

That last failure happened in the August 2025 GitHub Actions experiment. A
workflow could create a pull request and report completion, yet the diff did not
contain the expected deliverable. The system had done work, but the measure was
attached to the wrong object. Completion needed to mean reviewable output, not
merely a successful run.

So completion should be phrased as a contract: the requested artifact exists, in
the expected place, with the expected review surface, and the system reports
what validation ran. Anything less is activity.

## Quality Is Evidence, Not Confidence

Quality score is a tempting metric because it looks tidy. I would avoid it until
the components are named. For agent work, quality usually means several smaller
things: correctness, completeness, maintainability, traceability, and fit with
the surrounding system.

Correctness should use deterministic evidence where possible: tests, builds,
type checks, link checks, formatters, policy checks, and security scans.
Completeness asks whether the task's actual requirements were addressed.
Maintainability asks whether the change is understandable and local.
Traceability asks whether a reviewer can see why the agent made the choices it
made.

Fit is the hardest. It asks whether the output belongs in this codebase, this
workflow, and this team's current level of trust. That cannot be fully
automated, but it can be made reviewable. The agent can state assumptions, list
files changed, name risks, and separate evidence from judgment.

This connects to [Proof-Carrying Work](/blog/proof-carrying-work/). The agent
should bring proof with the work: not just the answer, but the checks and
reasoning that make the answer inspectable.

## Learning Measures Need Patience

The proposed metrics around learning velocity, autonomy, and context
preservation are more interesting, but they need patience. One successful run
does not prove learning. A faster second run may only mean the second task was
easier. A more autonomous run may only mean it skipped asking for clarification
it actually needed.

Context preservation is a better near-term measure. Did the agent keep the task
constraints in view? Did it avoid forbidden changes? Did it distinguish source
material from achieved results? Did it remember previous failures from the same
workflow without overgeneralizing them?

Redundancy avoidance is also concrete. Did the agent avoid creating duplicate
pull requests? Did it skip work when a deliverable already existed? Did it
prevent repeated processing of the same input? These sound mundane, but they are
the measures that make agent workflows operable.

Autonomy should be measured as earned permission, not personality. A Level 0
automation can run unattended inside a narrow boundary. A learning agent may
need more review because it carries state into future work. Higher autonomy is
not better unless the validation surface grows with it.

The metric I would add is reversibility. Can the agent's change be inspected,
tested, and rolled back? Can its memory be corrected? Can its process change be
disabled? A system that completes tasks but leaves irreversible confusion behind
is not improving the engineering system.

Measuring an agent beyond task completion means asking what the agent left
behind. Did it preserve context, produce reviewable evidence, respect quality
gates, avoid redundant work, and make the next run safer? Those are less
glamorous than a single score. They are also harder to fake. In agent systems,
the useful metrics are the ones that keep the human able to trust, correct, and
rerun the loop.
