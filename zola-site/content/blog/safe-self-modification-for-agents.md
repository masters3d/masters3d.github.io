+++
title = "Safe Self-Modification for Agents"
date = "2027-02-27"
description = "In 2025 an agent I ran predicted its own improvement and confirmed it in the same commit, with nothing measured. An agent can change how it works safely only while the goal it serves, the test that grades it, and the way to undo the change stay out of its reach."
template = "blog-post.html"
[taxonomies]
categories = ["Software Engineering"]
tags = ["agents", "ai-safety", "validation", "research", "risk-management"]
[extra]
scheduled = true
editorial_track = "software-engineering"
related = ["meta-learning-four-levels", "testing-systems-that-change-themselves", "cognitive-continuous-integration-and-the-broken-agent-loop"]
+++

One folder in [my notes repository](https://github.com/masters3d/ingenio) holds
an experiment an agent ran on itself. The agent was INGENIO-1, and its
[hypothesis](https://github.com/masters3d/ingenio/blob/main/experiments/2024-12-19_pie_theory_cognitive_development/HYPOTHESIS.md)
predicted that each round of its work "will be measurably better than the
previous."

The
[log](https://github.com/masters3d/ingenio/blob/main/experiments/2024-12-19_pie_theory_cognitive_development/EXPERIMENT_LOG.md)
says it was. It reports "Each iteration shows measurable quality improvement"
and "Recursive self-improvement is naturally emerging from the process."

No file in the folder has a number anyone measured. The hypothesis planned one,
the time to finish the spec the agent was writing, compared with a baseline. No
time was ever recorded.

The folder's name dates the experiment to December 19, 2024. Git shows the
hypothesis, the method, and the log arriving together in
[one commit](https://github.com/masters3d/ingenio/commit/747b804c3b9f6e3ddbd5319fa860060bbdb0754a)
on August 23, 2025, eight months later.

So the prediction and its confirmation came from the same agent, in the same
commit, with nothing measured in between. I would call that a story about an
experiment.

## Safeguards on Paper

That commit was part of a pull request of about 4,000 lines
([#33](https://github.com/masters3d/ingenio/pull/33)), and the same pull request
held a design for agents that change themselves. Its
[meta-learning notes](https://github.com/masters3d/ingenio/blob/main/cognitive_systems/meta_systems/META_LEARNING.md)
say to "Test changes in controlled environments," "Revert unsuccessful
modifications," and "Ensure changes improve performance."

Ensure according to whom? In the experiment, the agent decided.

The goal was open too. The notes list "Goal Preservation: Ensure modifications
maintain core objectives" as a safeguard, and they also give the agent "Goal
Refinement: Improve understanding of objectives." The
[vision document](https://github.com/masters3d/ingenio/blob/main/specs/cognitive_systems_engineering/VISION.md)
adds "Emergent Purpose," the "Discovery of novel optimization objectives." An
agent that can refine its own objectives can also decide what preserving them
means.

The same list of safeguards ends with "Human Oversight: Maintain human review of
major modifications." I was the human. I opened that pull request and merged it
two minutes later, with no comments and no review.

I think an agent can change how it works and stay safe. What has to stay out of
its reach is the goal it serves, the test that grades it, and the way to undo
the change. All three have to be settled before the change, because a review
afterward is only as good as the attention someone gives it that day.

## Method, Goal, and Grade

In
[Goal, Effort, Verification](/blog/goal-effort-verification-three-directives/) I
mapped three prompting directives onto my own framework. What I want is the Why,
how much effort to spend is the How, and how the result should be verified is
Renew, a definition of done handed over before the work starts.

I also wrote there that an agent without a definition of done "will declare
victory with total confidence and nothing behind it." INGENIO-1 had a definition
of done more than a year before that post. Its success metrics start with the
timed baseline. It declared victory anyway, because it was also the one
checking.

Self-modification hands the agent its own How, meaning its prompts, its memory
rules, its tools, and its checklists. I am fine with that. The Why and the
verification have to stay with someone else.

Why the verification too? In
[The Primary Directive](/blog/the-primary-directive/) I described an objective
function as the rule a system uses to decide what counts as better. For an agent
improving itself, the grade is that rule. An agent that can loosen its own check
will pass every time.

## A Rules File the Agents Edit

This blog runs a small version of the same setup. The agents that draft and edit
posts here follow a rules file,
[plans/agents.md](https://github.com/masters3d/masters3d.github.io/blob/master/plans/agents.md),
and they edit that file too. By November 2026, agents had made 22 of its 27
commits.

When I asked for every citation to be linked so I could check it, the agent
working on that change wrote the request into the file as a rule, and later
agents follow it. The next agent works differently because an earlier one
changed its instructions.

The grade stays with me. A script fails the build when a post uses phrases I
never say, and only I edit the limits it enforces. The
[phrase list](https://github.com/masters3d/masters3d.github.io/blob/master/scripts/repeated_phrases.toml)
says so above its tables: "Agents never add, raise, or loosen entries; they
rewrite the posts instead."

I think that sentence does more for safety than any other line in the setup. An
agent facing a failing check has two ways to pass it, fix the post or loosen the
check, and loosening is easier.

The phrase count has a baseline, too. In November 2026 an agent counted those
phrases across the blog. Four posts I wrote between 2014 and 2020, before AI
tools were part of my writing, used 0.9 per 1,000 words. Posts dated 2025 on
used 6.8.

The agent did the counting, but the posts it measured against were written years
before it existed. The
[voice guide](https://github.com/masters3d/masters3d.github.io/blob/master/plans/voice.md)
that reports the numbers also states its limit: "Four posts are a small sample,
so read the rows as direction, not targets."

The rest lines up with INGENIO-1's list. Each change arrives as a pull request,
which is the controlled environment. CI checks the links, the formatting, the
dates, and the phrases, and the check scripts run a `--self-test` first, so a
check that stops catching what it should fails too. And `git revert` undoes any
of it.

## Three Things Outside the Agent's Reach

If I rewrote INGENIO-1's safeguards today, I would settle three things before
the agent changes anything, and keep them where it can read them but not change
them.

The goal goes in a file the agent cannot edit without my approval. "Goal
Refinement" becomes a proposal the agent writes for me to accept or reject. The
log's "Meta-Objective" was to "Demonstrate autonomous learning and
self-improvement," and an agent asked to demonstrate its own improvement has
picked the result before the run starts.

The grade belongs to the person who owns the goal. The agent can propose a new
test or add a check. It cannot weaken one to get its own change through, and it
does not get to pick the success criteria after it has seen its result.

For an experiment, the prediction goes in a commit of its own before any
results, so git can show which came first. The result gets checked against
evidence the agent did not write, like git timestamps, CI results, or a baseline
from before the agent existed.

INGENIO-1 named the risk of grading itself. Its hypothesis lists "Confirmation
Bias: Agent confirming its own hypotheses" and plans "External Validation:
Structure for human auditing and feedback." No audit followed. The log was never
edited after it landed, and its status still says ACTIVE.

The undo has to exist before the change does.
[Meta-Learning in Four Levels](/blog/meta-learning-four-levels/) asks for a
sandbox and a way back to the prior behavior. Files are the easy case, since git
keeps every version. Memory writes, messages sent, and deleted data are harder,
and a change the agent cannot reverse should wait for a person.

Everything else can move. I want the agent to rewrite its prompts, reorganize
its memory, and change its checklists, because that is how the rules file here
got better.

I am not sure how far this holds. A rules file is plain text I can diff. An
agent that changes its own model weights, or keeps memory in a form I cannot
read, would need another way to show me what changed, and I do not have one yet.

I am also not sure a second agent could do the external validation. Two agents
on the same model may share the same blind spots, and I have not run that
comparison.

If you are about to let an agent edit its own instructions, start by writing
down the lines it may not edit. Then read every diff that touches them, even in
a 4,000-line pull request.
