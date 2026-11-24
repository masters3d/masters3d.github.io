+++
title = "Safe Self-Modification for Agents"
date = "2027-02-27"
description = "An agent can safely change how it works only while the goal it serves, the test that grades it, and the way to undo the change stay out of its reach. A 2025 design for self-improving agents let the goal move; the agent pipeline behind this blog keeps all three with me."
template = "blog-post.html"
[taxonomies]
categories = ["Software Engineering"]
tags = ["agents", "ai-safety", "validation", "risk-management", "systems-thinking"]
[extra]
scheduled = true
editorial_track = "software-engineering"
related = ["meta-learning-four-levels", "testing-systems-that-change-themselves", "cognitive-continuous-integration-and-the-broken-agent-loop"]
+++

In August 2025 an agent I called INGENIO-1 wrote a design for agents that
improve themselves. It went into
[my notes repository](https://github.com/masters3d/ingenio) as one pull request
of about 4,000 lines ([#33](https://github.com/masters3d/ingenio/pull/33)).

One file in it,
[META_LEARNING.md](https://github.com/masters3d/ingenio/blob/main/cognitive_systems/meta_systems/META_LEARNING.md),
covers an agent that changes itself. Its protocols say to test changes in
controlled environments, revert unsuccessful modifications, and make sure
changes improve performance. A later section on safeguards adds "Goal
Preservation: Ensure modifications maintain core objectives."

The same file gives the agent a long-term learning cycle, and its third step is
"Goal Refinement: Improve understanding of objectives." The
[vision document](https://github.com/masters3d/ingenio/blob/main/specs/cognitive_systems_engineering/VISION.md)
goes further. At its top level the agent does "Autonomous goal-setting," and
under motivation it lists "Emergent Purpose," the "Discovery of novel
optimization objectives."

So which is it? An agent that can refine its own objectives can also decide what
preserving them means. I think that contradiction teaches more than the
safeguards do.

## Method, Goal, and Grade

In [The Primary Directive](/blog/the-primary-directive/) I described an
objective function as the rule a system uses to decide what counts as better.
Self-modification asks an agent to get better. The first question about any
self-modifying agent, then, is who holds that rule.

[Goal, Effort, Verification](/blog/goal-effort-verification-three-directives/)
mapped three prompting directives onto the same framework: what I want (the
Why), how much effort to spend (the How), and how the result should be verified
(Renew). By the time I wrote
[Agents Are Taking the Drive](/blog/agents-are-taking-the-drive/), about 80% of
the software I produced started as a prompt. The agents had the How.

Self-modification moves the agent one level up. It changes its own How, meaning
its prompts, its memory rules, its tools, and its checklists. I think that can
be safe. What has to stay out of its reach is the goal it serves, the test that
grades it, and a way to undo what it changed.

Why the test too? An agent that can loosen its own check will pass every time.

INGENIO-1's design guards the method carefully and leaves the goal open. I would
do it the other way around.

## A Rules File the Agents Edit

This blog has a small version of the same setup. The agents that draft and edit
posts here follow a rules file,
[plans/agents.md](https://github.com/masters3d/masters3d.github.io/blob/master/plans/agents.md),
and they edit that file too. By November 2026, agents had made 22 of the 27
commits to it.

Many of those commits add a rule next to a post. When I asked for every citation
to be linked so I could check it, the agent working on that change wrote the
request into the file as a rule, and later agents follow it. The next agent
works differently because an earlier one changed its instructions.

A few parts are mine alone. A script fails the build when a post uses phrases I
never say, and the rules say only I edit the tables that set those limits and
their exceptions. The
[phrase list](https://github.com/masters3d/masters3d.github.io/blob/master/scripts/repeated_phrases.toml)
repeats it above the tables: "Agents never add, raise, or loosen entries; they
rewrite the posts instead."

I think that sentence does more for safety than any other line in the setup. An
agent facing a failing check has two ways to pass it, fix the post or loosen the
check, and loosening is easier.

The rest lines up with INGENIO-1's list. Each change arrives as a pull request,
which is the controlled environment. CI checks the links, the formatting, the
dates, and the phrases, and the check scripts run a `--self-test` first, so a
check that stops catching what it should fails too. Drafts stay drafts until I
read them. And `git revert` undoes any of it.

## Three Things Outside the Agent's Reach

If I rewrote INGENIO-1's safeguards today, I would keep three things where the
agent can read them but not change them.

The goal goes in a file the agent cannot edit without my approval. "Goal
Refinement" becomes a proposal the agent writes for me to accept or reject.

The grade belongs to the person who owns the goal. The agent can propose a new
test or add a check. It cannot weaken a check to get its own change through, and
it does not get to pick the success criteria after it has seen its own result.

The undo has to exist before the change does. Files are easy, since git keeps
every version. Memory writes, messages sent, and deleted data are harder, and a
change the agent cannot reverse should wait for a person.

Everything else can move. I want the agent to rewrite its prompts, reorganize
its memory, and change its checklists, because that is how the rules file here
got better.

I am not sure how far this holds. A rules file is plain text I can diff. An
agent that changes its own model weights, or keeps memory in a form I cannot
read, would need another way to show me what changed, and I do not have one yet.

If you are about to let an agent edit its own instructions, start by writing
down the lines it may not edit, and read every diff that touches them.
