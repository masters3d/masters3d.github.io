+++
title = "Context as Code"
date = "2026-05-30"
description = "Configuration earned its place next to code: versioned, reviewed, owned. The corpus of context that aligns a team (design docs, contextual documents, the why behind the system) deserves the same standard. It's the operating system humans run on, and now the grounding agents read to understand how we work."
template = "blog-post.html"
categories = ["engineering", "productivity", "workflow"]
tags = ["context", "configuration", "alignment", "high-agency", "knowledge-management"]
+++

There was a time when configuration was treated as an afterthought. It lived in
a file someone edited by hand on a server, undocumented, unreviewed, owned by
whoever touched it last. Then the industry grew up. Configuration became code:
versioned in the same repository, reviewed in the same pull requests, tested in
the same pipelines, owned with the same seriousness. Infrastructure as code,
config as code. We stopped pretending the settings that determine how a system
behaves were somehow lesser than the logic inside it.

I want to make the same argument for context. **The corpus of context that
aligns a team should be held in the same regard as configuration and code.** Not
below it. Not the thing you write up afterwards if there's time. At the same
level.

I'm deliberately saying _context_ and not _documentation_. When people hear
"documentation" they think of a chore, the thing nobody wants to write, the
stale wiki page nobody reads. And there are genuinely different tiers of it. The
note you drop in an issue is short-lived context, useful in the moment and fine
to leave behind. The durable layer is different: the design docs, the contextual
documents, the written-down "why" that creates alignment and cohesion across a
team. If you want it to last, it eventually belongs in a real system (an
internal site, a corpus you can navigate), not buried in a ticket. That durable
layer is what I'm pointing at, and "context as code" names it better than
"documentation" ever did.

## Context Lives at Every Layer, Not Only Up Front

I used to think the cognitive artifacts always come first: write the design doc,
get alignment, then write the code. That's one valid order, but it's not the
only one, and insisting on it misses how the work actually happens now.

Code is cheap. It's getting cheaper every month. So it's entirely reasonable to
write the code first. You might have two or three demos going, different
approaches you're trying to align on, and you only know which one is right
_after_ you've built them and watched them run. Then you extract the design from
the one that worked. The context didn't precede the code there. It was distilled
out of it. That's still context as code, and it's still first-class.

The point isn't "documents before code." The point is that context shows up at
every layer, and wherever it shows up you treat it as a real artifact instead of
letting it evaporate. Sometimes you write the alignment doc to decide what to
build. Sometimes you build three things and write the alignment doc to capture
which one won and why. Both produce the same durable asset: a clear, shared
mental model that outlives the moment it was created in.

## The Operating System of a People

Here's the framing that makes context click for me: context is an operating
system for groups of people.

Think about how religious texts function. Whatever you believe about them, a
text like the Bible operates as the shared operating system of an enormous group
of people. It encodes the values, the guiding principles, the "this is who we
are and this is how we do things." It's the corpus that lets people who have
never met act with cohesion. We even borrow the metaphor in our own field. When
something becomes the definitive corpus of knowledge, we call it the Unix Bible,
or the bible of whatever domain it covers. The word signals exactly this: the
canonical body of context that aligns the people who follow it.

A team has the same need at a smaller scale. The thing that lets folks who
weren't in the original room build in the same direction, raise the quality bar,
and contribute without re-deriving every decision from scratch is the corpus of
context. Lose it and a team's quality ceiling is set by whoever happens to hold
the most in their head. Write it down and the ceiling is set by the whole group.

## Why Agents Make This Urgent

There's a new reason this matters, and it's the one that pushed me to name it.

LLMs run on data. Agents now operate inside our environments, and they're doing
exactly what a new teammate does on their first week: trying to understand what
we're about, how we work, what to do here and what not to do. They need a corpus
of grounding. They need something that says, within this team this is what we
do, these are our guiding principles, this is the way we do things.

Some of that grounding lives in configuration. Some of it lives in the code, in
comments that never surface to a user but explain the local "what." But the
hardest and most valuable part, the _why_, is exactly the part that resists
living in config or code. Why the system is shaped this way. Why we made this
tradeoff and not the obvious one. The single cohesive story that ties the pieces
into one mental model of how the team works and how this thing came to be. That
can't be a comment buried next to a function. It has to be an alignment
document, a context document, deliberately written and maintained.

That corpus is the operating system for the humans on the team, and now it's the
operating system for the agents reading alongside them. Which is why it deserves
the full treatment. Version it. Review it. Own it. Keep it current. Hold it to a
standard. We did all of that for configuration once we admitted it was as
load-bearing as the code. Context is more load-bearing still, because it's the
thing that produces both.

**Treat your context as code.**
