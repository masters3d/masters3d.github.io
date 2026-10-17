+++
title = "Design Review Needs Governance"
date = "2026-10-17"
draft = true
description = "A design review that cannot approve, reject, or route a decision is mostly performance. Governance gives the review a body: who decides, what authority they have, how disagreement is resolved, and how the decision becomes part of the system."
template = "blog-post.html"
[taxonomies]
categories = ["Engineering Systems"]
tags = ["design-review", "governance", "working-groups", "architecture", "decision-making", "shared-understanding"]
[extra]
editorial_track = "engineering-systems"
+++

In July 2022 I wrote one sentence in my notes repository that still feels
sharper than the amount of text around it: design review without governance is
empty. I added that community governance is usually better when working groups
approve features. The note was short, and a separate issue nearby held a set of
references I was clearly thinking with: Microsoft's engineering playbook on
design reviews, the Swift Evolution process, Google's design docs, and Oxide's
Requests for Discussion.

What those references have in common is not the template. It is the presence of
a decision system. A design can be written beautifully and still go nowhere if
nobody knows who can approve it, who can block it, who has to be consulted, and
what happens when reasonable people disagree. A review meeting without that
structure can produce comments, but comments are not governance.

I have been in design reviews that felt productive in the room and evaporated
afterward. Everyone asked intelligent questions. Risks were named. Alternatives
were sketched. Then the author left with a pile of feedback and no decision. The
project either continued as planned, absorbed only the easiest comments, or
stalled because the review created uncertainty without a path through it. That
is the emptiness I was pointing at.

## Review is feedback; governance is authority

Design review is a learning mechanism. It exposes assumptions to people who hold
different context. It asks whether the problem is real, whether the shape of the
solution fits, and whether the system will be understandable later. That is
valuable work, but it does not answer the authority question by itself.

Governance answers a different set of questions. Who owns the decision? Who is
allowed to say no? Which decisions require a working group, an architect, a
service owner, or a broader community process? Which comments are advisory, and
which are binding? What evidence is required before the proposal moves forward?

Without those answers, design review becomes a social negotiation. Seniority
fills the vacuum. The loudest objection can feel like a veto. The person with
the most organizational confidence gets to proceed. People who need a clear
decision instead receive tone: seems fine, concerns remain, let's revisit, maybe
after launch. None of those phrases tell the team what to do next.

This is why I like working groups for certain classes of decisions. A working
group is not a committee for its own sake. At its best, it is a small body with
a declared scope, visible membership, and explicit authority. It says: for this
domain, these are the people entrusted to maintain coherence. They are not there
to own every implementation detail. They are there to keep local choices from
damaging the larger system.

## The useful parts of public processes

The references in the old issue point at a spectrum. Swift Evolution is a public
language process with proposals, review periods, core team decisions, and an
archive that lets future readers see how a feature entered the language.
Google's design doc culture emphasizes writing as a way to force clarity before
execution. Oxide's RFDs make discussion durable by turning it into a record.
Microsoft's design review guidance gives teams a practical shape for looking at
architecture before the cost of change goes up.

Most teams should not copy any of these processes whole. A five-person product
team does not need the same ceremony as a programming language. But the useful
parts are portable:

- There is a written proposal before the decision.
- Reviewers are chosen because of the context they hold, not because everyone is
  invited.
- The authority of the review is clear before the review starts.
- The final decision and rationale are recorded.
- The record remains findable after the people move on.

That last point matters more than I used to think. Design governance is not only
about making today's decision. It is about leaving a trail that future engineers
can trust. If someone later asks why the system works this way, the answer
should not depend on finding the one person who remembers the meeting. The
answer should live in the decision record.

This is also where governance prevents design review from becoming personal.
When the process defines who decides and why, disagreement can attach to
criteria instead of status. A reviewer can say, "This breaks the compatibility
rule owned by this working group," instead of "I do not like it." The author can
answer the rule, ask for an exception, or change the design. The conflict
becomes legible.

## Approval should produce responsibility

The danger in governance is that it becomes a gate people route around. A group
that only says no will eventually stop seeing proposals until the decision is
already irreversible. The fix is to make approval carry responsibility in both
directions. The working group that approves a design should also own the quality
of its standards, the clarity of its feedback, and the cost of the process it
imposes.

A healthy design governance system therefore has two promises. To the product
team: if you bring the decision early and in the right form, you will get a
timely answer and know what to do next. To the wider engineering organization:
decisions that change shared architecture, user contracts, reliability,
security, or long-term maintenance will not be made in isolation.

That second promise connects to
[Quality Engineering vs Engineering Quality](/blog/quality-engineering-vs-engineering-quality/).
Quality, security, and context have to be built by the engineers doing the work,
but some properties are shared across teams. Governance is how those shared
properties get an owner without turning every review into a fight over taste.

The smallest useful version is a design review checklist with named decision
rights. What category is this proposal? Who must approve it? What evidence is
required? Where will the final decision live? What is the escalation path if the
author and reviewers disagree? If a team cannot answer those questions, it may
still hold a review, but it should be honest about what the review can do. It
can advise. It cannot govern.

When I read the old note now, I hear frustration with a familiar theater: smart
people gathered around a design with no mechanism to turn their attention into a
decision. The better version is not more ceremony. It is less ambiguity. Review
gathers context. Governance converts that context into a responsible decision
that the organization can remember.
