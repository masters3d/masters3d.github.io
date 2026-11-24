+++
title = "Cognitive Continuous Integration Had a Loop but No Why"
date = "2027-06-05"
description = "INGENIO-1 was a GitHub Actions agent that turned my labeled notes into VISION.md specifications. I fixed its scope, its races, and its pull requests until every check was green, and it still produced nothing anyone used, because its goal was the agent itself. It was a good organizer with no Why. The goal it should have had, getting my notes into a form other people can use, is what this blog's pipeline does now."
template = "blog-post.html"
[taxonomies]
categories = ["Software Engineering"]
tags = ["agents", "continuous-integration", "specs", "github-actions", "quest-engine", "primary-directive"]
[extra]
scheduled = true
editorial_track = "software-engineering"
related = ["software-3-0-needs-engineering-not-magic", "five-levels-of-agent-capability", "hypothesis-driven-agent-experiments", "testing-systems-that-change-themselves"]
+++

INGENIO-1 was an agent I ran on
[my notes repository](https://github.com/masters3d/ingenio) in 2025. A GitHub
Actions workflow woke up every hour, read my open issues, applied the Quest
Engine framework to each one, wrote a `VISION.md` specification, and commented
back on the issue with what it had made. I called it cognitive continuous
integration.

I spent most of my time on it fixing the pipe. It took far too long to ask what
the pipe was for.

## The Goal Was the Agent

The
[cognitive systems README](https://github.com/masters3d/ingenio/blob/main/cognitive_systems/README.md)
states the vision in one line: "Transform the ingenio repository into a testbed
for cognitive agent systems that autonomously improve engineering excellence."
It names TARS and CASE from _Interstellar_ as the inspiration. It lays out five
agent levels, from reactive to fully cognitive, and four phases ending in
"autonomous goal generation."

Then it lists the success metrics: autonomy level, learning rate, innovation
capacity, collaboration quality, emergent intelligence, self-improvement rate.
Every one of them measures the agent. None of them asks whether a note became
more useful to a person.

That is the flaw underneath everything else in this post. The goal of INGENIO-1
was INGENIO-1.

## What It Actually Did Was Organize

Strip away the vocabulary and the agent did something useful. It took a note I
had marked as ready, gave it a folder under `specs/`, wrote a document with a
consistent structure, and linked the result back to the original issue. A pile
of one-line issues became a directory you could browse. In the
[Quest Engine](/blog/quest-engine-introduction/), that is Proactive Curiosity,
the first step of Search: systematically find and organize information. The
agent was good at it.

The trouble was what went inside each document. On December 30, 2022 I wrote
[issue #23](https://github.com/masters3d/ingenio/issues/23), and the whole body
was: "The act of building > than finish it." INGENIO-1 turned that into a
[130-line specification](https://github.com/masters3d/ingenio/blob/main/specs/seeking_is_the_reward/VISION.md).
Its mission statement reads: "Transform the engineering challenge 'Seeking is
the reward' into a cognitive agent-enhanced system that autonomously improves
engineering excellence through recursive meta-learning and human-cognitive
collaboration." Its central question is "How can cognitive agents autonomously
improve the concepts in 'Seeking is the reward'?"

That is a question about the agent, not about seeking. Twenty-eight of the 37
specification files in the repository open with the same mission statement, with
only the title swapped in. The one line in that spec that held any thinking was
my own sentence, copied into the "Engineering Context" field. When I finally
wrote [the post about that note](/blog/seeking-is-the-reward/), none of it came
from the spec. It came from the note and from what I have learned since writing
it.

So the agent organized my notes and then buried each one under a template. That
padding added length but no understanding.

## Fixing the Pipe

The pipe itself did get fixed, and those fixes are still the right ones for any
agent that writes into a repository.

- **Explicit opt-in.** The first version treated every open issue as an
  assignment, so a reminder and a request looked the same.
  [Issue #36](https://github.com/masters3d/ingenio/issues/36) restricted it to
  issues carrying an `Ingenio-1` label. Later the match was made
  case-insensitive.
- **Constrained input.** GitHub's issues API also returns pull requests, so the
  processor had to filter them out explicitly
  ([#37](https://github.com/masters3d/ingenio/pull/37)).
- **Reviewable output.** The agent first committed specs straight to `main`.
  After #37 every spec went through a branch and a pull request I could reject.
- **Idempotency.** An issue event and a scheduled run could pick up the same
  issue seconds apart. The second run failed because the pull request already
  existed. The fix treated "already exists" as an expected state: look up the
  existing pull request and settle.
- **Deliverables separate from logs.** A broad `git add` once produced a pull
  request containing only session metadata, while the spec was already on
  `main`. The repair added only `specs/` content and skipped pull requests that
  had nothing new to review.
- **Observable scheduling.** When an issue was not picked up
  ([#42](https://github.com/masters3d/ingenio/issues/42)), the answer was
  ordinary CI mechanics: workflow on the default branch, events after the
  workflow existed, dependencies installed from the repository's own
  `package.json`.

Each fix made the system more reliable at producing a document. None of them
asked whether the document helped anyone.

The session logs show how that ended. The workflow recorded 33 sessions between
August 23 and August 25, 2025, then went quiet. In January 2026 I ran a full
end-to-end validation ([#54](https://github.com/masters3d/ingenio/issues/54)): 7
of 7 tests passed, 20 of 20 dry-run checks passed, and the latest workflow run
"correctly identified no issues with 'Ingenio-1' label." Every check was green,
and the system had nothing to do. Green told me the loop could run. It could not
tell me whether the loop was worth running, because nobody had said what
"better" meant.

## Where the Quest Engine Would Have Started

The Quest Engine opens with a Why, and
[the Why is the Primary Directive](/blog/the-primary-directive/): the standing
order that says what counts as better before any Search, Drive, or Renew
happens. In [Agents Are Taking the Drive](/blog/agents-are-taking-the-drive/) I
argue that agents now handle much of the How, and the part left for me is the
Why and the context still trapped in people's heads.

INGENIO-1 got that division backwards. Its template asked the agent to supply
the Why ("autonomously improve engineering excellence") and left the context in
my head, where a five-word note keeps it. The agent had the Drive and a Search
step. It had no Why to aim at and therefore no Renew, because Renew compares
what happened with what you expected, and nothing was expected except that the
agent run.

The same gap shows up in two other frames I use.
[Rumelt's kernel of strategy](/blog/kernel-of-strategy/) starts with a
diagnosis. INGENIO-1 never had one. "Engineering excellence could be better" is
a wish, not a diagnosis.
[Musk's algorithm](/blog/elons-algorithm-manual-process/) puts automation last,
after you have questioned the requirement and done the step by hand. I put the
cron job first. I had never turned one of my notes into something useful by
hand, so I had no idea what the agent should be doing when it tried.

## The Goal It Should Have Had

Looking back, the goal was always there in the shape of the repository: get the
thinking out of my notes and into a form other people can use. That is the
argument of
[Open Guides Over Closed Answers](/blog/open-guides-over-closed-answers/) and
[Story Is Engineering Memory](/blog/story-is-engineering-memory/). A note only
helps someone else once it has been worked into a guide or a story, and that is
where the context starts to compound.

That goal now has a working system, and it is the one producing this post.
Agents mine the ingenio notes into a backlog of post ideas, which is Search, the
part INGENIO-1 was already good at. The backlog carries one rule INGENIO-1
taught me: read the original issue, not only the generated spec, because the
author's real words are in the issue. An agent drafts the post, which is Drive.
I review every draft, and it stays `draft = true` until I do. That review is
where the Why lives. A post goes out on a schedule. A check fails the build if a
draft gets close to its date without review, so the loop cannot quietly stall
the way INGENIO-1 did. When a review finds a problem, the fix goes into the
agents' instructions as a rule, so the next draft starts from it. That is Renew.

It has the same parts as INGENIO-1: an agent, a schedule, a repository, pull
requests, and checks. The difference is that the success test is about the
output, not the agent: is this post worth someone's time to read? The fixes from
INGENIO-1 carried over. The goal did not, because there wasn't one.

## What I Would Keep

Cognitive continuous integration was not a bad idea. An agent that organizes raw
notes on a schedule is useful, and the engineering around it (opt-in triggers,
constrained input, reviewable output, idempotency, logs kept apart from
deliverables) is the minimum for any agent that writes into a repository.

What I would change is the order. Write the Why before the workflow. Measure the
output's usefulness to a person, not the agent's autonomy. Do the transformation
by hand a few times before automating it. And when an agent is good at
organizing, call it an organizer. Calling it a cognitive system set it a goal it
could not meet and left the one it could meet unnamed.
