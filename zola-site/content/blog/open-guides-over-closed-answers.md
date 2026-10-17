+++
title = "Open Guides Over Closed Answers"
date = "2026-10-17"
draft = true
description = "When someone asks for the same explanation by email, the durable answer is usually a guide that others can find, reuse, and improve. Answering once in a shared place turns private help into organizational context."
template = "blog-post.html"
[taxonomies]
categories = ["Engineering Systems"]
tags = ["documentation", "knowledge-management", "context", "wiki", "async-work", "collaboration"]
[extra]
editorial_track = "engineering-systems"
+++

In November 2021 I wrote a small behavioral rule to myself: instead of
responding to an email, consider opening a wiki with all the requested
information so it can be shared. The issue title was clumsy (general open guides
over specific closed guides), but the behavior was clear. When the same
explanation wants to travel from one person to another, do not trap it in a
private reply if it can become shared context.

This is one of those ideas that sounds like extra work until the third request
arrives. The first time someone asks, an email feels faster. The second time,
forwarding the first email feels efficient. By the third time, the organization
has taught you that the information is not a one-off answer. It is missing
infrastructure.

A closed answer solves one person's problem in one moment. An open guide changes
the environment. It gives the next person a place to start, gives the author a
place to improve the explanation, and gives future agents or teammates a durable
object to read. The difference is not politeness. It is whether the knowledge
becomes part of the system or remains a private transaction.

## Private help does not compound

Most teams leak knowledge through helpfulness. Someone asks a question. Someone
else writes a thoughtful answer in Slack, email, or a direct message. The answer
is useful, maybe even excellent, but it disappears into a channel whose default
state is forgetting. Later, another person asks the same thing. The expert
answers again, a little shorter this time. Eventually the expert becomes a help
desk for context that should have been written once.

This is especially costly in engineering because the most valuable explanations
are rarely pure facts. They are maps: why the system works this way, which path
is safe, what error means the database is lying to you, which deployment step is
ceremonial and which one will wake someone up at night. Those maps should not
depend on finding the right person in the right mood.

The open-guide habit changes the default. When a question arrives, answer in a
shared place first. Then send the link. If the guide does not exist, create the
smallest useful version. If it exists but did not answer the question, improve
it and send the updated link. The requester still gets help, but the next person
gets a better world.

This is not a call to turn every sentence into documentation. Some answers are
genuinely private, temporary, or sensitive. Some conversations need trust before
they need a page. The point is to notice when a private answer is pretending to
be private only because the shared version has not been made yet.

## A guide is a reusable path

The word "guide" matters. A guide is not a dumping ground for information. It is
a path through a problem. It should start where the reader actually stands, name
the decision they are trying to make, and show the next few steps. A useful
guide does not need to be complete. It needs to reduce the cost of doing the
right thing.

For an engineering team, open guides can cover recurring questions:

- How do I run this service locally?
- How do I choose the right deployment path?
- What does this alert mean?
- How do I request a design review?
- What should be in a production readiness review?
- What is the current migration path away from an old feature?

Each guide should have an owner, a last-reviewed date, and a clear invitation to
improve it. Without ownership, a wiki becomes a museum of outdated confidence.
With ownership, it becomes shared memory that can be maintained like any other
part of the system.

The guide also has to be findable. A perfect page with a title nobody would
search for is only slightly better than an email. The best guides use the
language of the question. If people ask, "How do I fix the staging deploy?" then
the page should say that, even if the formal system name is more precise. Search
is part of the user experience of knowledge.

## Answer once where the organization can learn

Open guides are a small practice with a large cultural signal. They say that
knowledge is not a favor granted by experts. It is a shared asset the team is
responsible for improving. They also make expertise less extractive. The person
who knows the answer still contributes, but the contribution compounds instead
of resetting to zero with every new request.

This connects to [Context as Code](/blog/context-as-code/) and
[There Is No Speedup for Shared Understanding](/blog/no-speedup-for-shared-understanding/).
If understanding remains the scarce resource, then making context cheap to
consume is not administrative work. It is engineering work. The guide is part of
the system that lets people act safely without rediscovering every reason from
scratch.

The behavior I would write now is slightly sharper than the 2021 note: when a
private answer explains a reusable path, move the path into the open before
sending it back. Do not wait until the guide is perfect. A rough shared answer
beats a polished private one because it can be found, corrected, linked, and
improved.

I still answer emails. I still send quick messages. Not every exchange deserves
a document. But when a question touches something the team will need again, the
private answer feels unfinished to me now. The real answer is the guide plus the
link. One helps the person in front of me. The other helps the next person I
have not met yet.
