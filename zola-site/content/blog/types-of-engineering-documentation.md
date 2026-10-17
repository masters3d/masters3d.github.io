+++
title = "Types of Engineering Documentation"
date = "2026-10-17"
draft = true
description = "Documentation is not one thing. Team-private notes, organization-wide engineering docs, troubleshooting guides, onboarding material, diagrams, and recorded context all serve different jobs, and the medium should match the job."
template = "blog-post.html"
[taxonomies]
categories = ["Engineering Systems"]
tags = ["documentation", "context", "onboarding", "async-work", "engineering-systems"]
[extra]
editorial_track = "engineering-systems"
+++

In an engineering documentation deck from 2021, I wrote a sentence that still
makes me smile because it sounds too obvious until a team tries to act on it:
"You may think that documentation is self-explanatory, but you more than likely
are wrong." Nobody agrees on what documentation means. One person means an API
reference. Another means a runbook. Another means a diagram in a slide deck.
Another means the decision that was only explained in a meeting.

The disagreement matters because a team can say "we need better docs" for years
and never improve. The phrase is too large. Better docs for whom? For a new
engineer setting up a laptop? For an on-call engineer at 2 a.m.? For a leader
trying to understand risk? For a customer trying to use the product? These are
not the same document.

## Documentation Has an Audience

The first split in that old deck was between customer documentation and
engineering documentation. Customer documentation is its own discipline. It has
a product surface, a support function, and often a marketing function. The deck
put that aside to focus on engineering documentation: the context producers need
in order to build, operate, and change the system.

Even inside engineering documentation, there are at least two large audiences.
Some docs are private to the team. They are close to the work and may include
rough edges: setup instructions, access notes, service quirks, local debugging
steps, onboarding recordings, and troubleshooting guides. Other docs are private
to the organization. They need more polish because people outside the team use
them to coordinate: architecture overviews, service boundaries, dependency maps,
standards, decision records, and operating expectations.

When those two audiences are collapsed into one bucket, teams get stuck. Team
notes become too polished to maintain, or organization docs become too informal
to trust. The right question is not "is this documentation?" The right question
is "who needs to act differently after reading it?"

A ramp-up guide helps a new teammate become useful without borrowing a senior
engineer for every step. A troubleshooting guide helps on-call move from symptom
to diagnosis without rediscovering history. An architecture overview helps a
neighboring team know where to connect. A decision record helps future engineers
understand why the system is shaped this way, especially when the original
author is gone.

Each document is a tool. Tools have users.

## The Medium Is Part of the Message

In a contextual awareness deck, I split context sharing across several mediums.
Text can live in markdown, a wiki, or a document. Visual context can be a
diagram, a photo of a whiteboard, or a slide. Interactive context can happen in
pull requests, document comments, email, or chat. Recorded audio and video can
carry a presentation to people who could not attend. Synchronous conversation
can unlock confusion quickly, but it has to be repeated for every new person
unless someone turns it into an artifact.

That last point is the trap. Meetings feel efficient because they move context
in real time. They are useful, but they are single-use by default. A meeting
that solves a problem for five people may create no memory for the sixth person
who joins next month. If the decision matters after the meeting, the durable
artifact is part of the work.

The medium should match the rate of change and the cost of being wrong. Fast
changing team notes can live close to the code and be updated with the work.
Stable explanations can be published in a place with broader visibility. A
complex architecture may need a diagram because paragraphs hide shape. A fragile
operational procedure may need a checklist because memory is not a control
system. A nuanced decision may need a short narrative because the conclusion
without the tradeoff invites people to relitigate it later.

This is why "write more docs" is usually bad guidance. "Record the context in
the medium that lets the next person act" is better.

## Documentation Is Shared Infrastructure

The contextual awareness deck used the tragedy of the commons as the economic
model for documentation. Everyone benefits from good context. The cost of
creating and maintaining it lands on a smaller set of people, often at the exact
moment they are busiest. If the organization does not make documentation easy,
visible, required where it matters, and integrated with the work, the commons
will decay.

That decay is not moral failure. It is a system doing what it was designed to
do. If promotion, planning, and review systems only reward shipped features,
then context work becomes charity. A team may still do it for a while, but the
half life of the knowledge will be short.

Good documentation systems reduce the cost of contribution. They keep docs near
the code when the audience is engineering. They make ownership visible. They let
pull requests update the explanation at the same time as the behavior. They keep
large docs searchable. They allow questions to improve the page instead of
creating another private answer in chat.

The goal is not a perfect library. The goal is an information system where the
next engineer can find enough context to make a safe move.

I still like the phrase "document documentation" because it forces the team to
name the category before arguing about quality. A troubleshooting guide, an
onboarding guide, an architecture overview, a decision record, and a recorded
walkthrough are all documentation. They are not interchangeable. When the medium
fits the audience and the job, documentation stops being a chore performed after
the real work. It becomes part of how the work survives contact with time.
