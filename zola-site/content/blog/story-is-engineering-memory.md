+++
title = "Story Is Engineering Memory"
date = "2027-06-01"
description = "Engineering information does not survive because it was written down once. It survives when people can store it, retell it, and use it under pressure. Story is one of the ways technical context becomes memory."
template = "blog-post.html"
[taxonomies]
categories = ["Human Systems"]
tags = ["story", "engineering", "memory", "documentation", "context", "narrative"]
[extra]
scheduled = true
editorial_track = "human-systems"
related = ["cohesive-narrative", "motivation-ability-narrative", "types-of-engineering-documentation"]
+++

In August 2025 I wrote down a question I had been circling: where does story fit
into the engineering process, and how much of what we know do we store as story?
Next to it I had a few small diagrams, each one a link between two or three
words.

The question came from a familiar gap. A technically correct document can leave
almost no memory behind. Every field is filled in. Every section has the
expected heading. The diagram is there, the alternatives are there, the decision
is there. A week later, nobody can explain why the decision happened without
reopening the document and scanning for the one sentence that mattered.

Compare that with a five-minute incident story, something like this one. We
thought the cache was harmless. The deploy changed the read path. The metrics
looked healthy because the dashboard averaged away the cohort that was failing.
We fixed the bug, but the real lesson was about observability lying politely
when the question is too broad. A story with that shape can stay with a team for
years. Not because it is dramatic, though incidents usually are, but because one
event leads to the next.

That story stores more than facts. It stores sequence, surprise, cause, and
consequence. That is why story belongs in engineering.

## Facts need a retrieval path

Engineering organizations often treat documentation as storage. Put the
information somewhere durable and the knowledge is preserved. That is only half
true. Picking the
[right kind of document](/blog/types-of-engineering-documentation/) helps, but a
document can store facts without giving people a reliable way to retrieve the
meaning under pressure.

Story gives facts a retrieval path. It tells a person where to start, what
changed, what somebody believed at the time, what broke that belief, and what
rule survived the experience. The same information written as a flat list may be
accurate, but it asks the reader to reconstruct the movement themselves.

This does not mean every technical document should become a memoir. A runbook
should still be direct. An API reference should still be reference material. But
the parts of engineering that depend on judgment (architecture decisions,
incident reviews, migrations, product tradeoffs) usually need narrative because
judgment lives in context. The answer matters less without the path that made it
the answer.

That is what the small diagrams in my note were reaching for. Will connects to
way. Motivation and ability feed each other. Then a third word joins each pair:
narrative sits between motivation and ability, and narrative sits between why
and how. Story is the bridge between intent and method. Without it, the "why"
stays abstract and the "how" becomes a ritual people copy without understanding.

## Narrative is not decoration

The word story can sound soft in engineering, as if it belongs to presentations
rather than systems. But engineers already use story constantly. We tell the
story of a bug. We ask for the user story. We reconstruct the sequence of an
outage. We explain why a design exists by describing the constraints that
surrounded it. Even a commit history is a rough story of changing belief.

The question is not whether engineering uses story. The question is whether it
uses story deliberately.

A useful engineering story has a few pieces. It has an initial belief. It has a
constraint or event that challenged that belief. It has the decision that
followed. It has the result and the lesson. Remove any one of those and the
memory weakens. A decision without the original belief sounds arbitrary. A
lesson without the failure that taught it sounds like a slogan. A result without
the constraint invites someone to repeat the answer in the wrong situation.

This is why story also belongs in knowledge transfer. The new person on a team
does not only need the current architecture. They need the ghosts inside it: the
failed rewrite, the compliance constraint, the customer behavior that surprised
everyone, the optimization that was removed because it made incidents worse.
Story is how a team hands over the lived part of the system, not as folklore but
as context with a retrieval path.

## The story must serve the work

There is a bad version of this. A story can become mythology. The team repeats
the old incident until it prevents a better design. The founder story crowds out
new evidence. The narrative becomes more important than the system it was
supposed to explain. That is why engineering stories need renewal. They should
be retold with dates, constraints, and expiration conditions.

The best engineering stories are not entertainment. They are compressed context
with a testable lesson. They help a person remember what happened, but more
importantly, they help a person notice when a similar shape is appearing again.

A document tells you what the system is. A story tells you how it became that
way, what it cost, and which mistake it is trying not to repeat. Both matter.
But when the information has to survive in human heads and move between people,
story is not a layer on top of engineering memory. It is one of the formats
engineering memory uses.
