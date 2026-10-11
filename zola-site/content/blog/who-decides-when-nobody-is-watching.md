+++
title = "Who Decides When Nobody Is Watching"
date = "2026-10-12"
description = "At 11pm an engineer found the config flag that would have stopped the errors, and instead of flipping it he paged me and waited forty minutes. He was not timid and he was not wrong. He had no way to know whether that flag was his to flip, because nobody had ever said. Autonomy is not a permission you grant in the moment, it is three things written down before the moment: intent, boundary, and a way to report back."
template = "blog-post.html"
[taxonomies]
categories = ["Leadership & Teams"]
tags = [
  "autonomy",
  "decision-boundaries",
  "ownership",
  "high-agency",
  "team-dynamics",
  "agents",
  "escalation",
]
[extra]
editorial_track = "leadership-and-teams"
+++

Around eleven at night, an engineer on my team found the thing. Error rates had
been climbing for an hour on a service he had been in all week, he traced it to
a recently changed configuration value, and he was fairly confident that putting
it back would stop the bleeding. He did not put it back. He paged me, wrote a
clear summary, and waited. I got to it about forty minutes later, read what he
had written, agreed with every word of it, and told him to go ahead.

Forty minutes of errors for a decision that did not change. And he had done
nothing wrong: he was not timid, he was not junior, and he was not asking me to
check his work. He was asking whether the work was his. That configuration value
belonged to a service our team ran but another team had opinions about, it had
been changed by someone outside both teams, and nothing anywhere said who was
allowed to change it back under pressure. In the absence of an answer he picked
the move that could not be held against him, which is what everybody picks.

I have argued twice that authority has to sit where the information is, once
from [terrain](/blog/independent-fire/) and once from
[latency](/blog/far-away-is-the-same-as-far-in-the-future/). Both posts are
about why the center cannot make the call. Neither says how a team decides, in
advance and in daylight, which calls belong to whom. That night made the gap
obvious to me: I had been advocating for autonomy without ever writing one down.
So this is the mechanical version. What has to exist before the moment, who has
to produce it, and what it looks like when the person on the spot is not a
person at all.

## The Default Is Not Caution, It Is the Defensible Move

The first thing to get right is what actually happens when the boundary is
undefined, because "people escalate when in doubt" undersells it.

An undefined boundary does not produce caution. It produces whichever action is
easiest to defend afterward, and those are not the same thing. Flipping the flag
and being wrong is a story about an engineer who exceeded his authority.
Flipping the flag and being right is a story about an engineer who got lucky.
Paging and waiting is a story about an engineer who followed process, and it
reads identically whether the outcome was good or bad. One of those three has a
fixed, acceptable outcome regardless of what happens, so that is the one a
rational person takes under uncertainty. The forty minutes of errors are a real
cost that lands on the company, and the career cost of overstepping is a real
cost that lands on him. He paid the cheaper one.

This is why "we trust our engineers, they should just use judgment" does not
work as an instruction. It describes the outcome you want without changing
anything about the calculation the person is running. Trust that is only
discoverable by testing it is not usable in the moment, because testing it is
precisely the risk they are trying to avoid. The person needs to know
beforehand, and the only way to know beforehand is for someone to have said it
beforehand.

The cost also does not show up anywhere you would look for it. There is no
metric for decisions that were correct and delayed. The incident review records
forty minutes of elevated errors and a root cause in a configuration change, and
everyone involved behaved well, so there is nothing to flag. The structural
problem leaves no trace, which is how teams run for years with an escalation tax
nobody has measured.

## Three Things, Written Before the Moment

What he was missing is specific, and it has three parts. Any one of them missing
sends you back to the defensible move.

The first is **intent**: what we are actually trying to win, stated clearly
enough to be used when the situation is not one anyone anticipated. "Keep the
error rate down even at the cost of a stale configuration overnight" is intent.
It tells you what to optimize when the runbook has nothing to say, which is
every interesting case. A list of approved actions is not intent, because the
list is always written for last quarter's incidents, and the moment the
situation falls outside the list the person is back to guessing.

The second is **boundary**: the size and shape of what someone may do without
asking. This is the part that is almost never stated, and it has to be concrete
enough to apply at eleven at night. Reversible or not. Scoped to our services or
touching someone else's. Recoverable in minutes or in hours. Costing under some
dollar amount or over it. "Any change you can fully undo in under ten minutes,
on a service we own, without a schema change" is a boundary a tired person can
evaluate correctly. "Use good judgment on low-risk changes" is not, because the
word that needs defining is doing none of the work.

The third is **a way to report back**, and it is the one that makes the other
two affordable. The center does not actually need to approve the action; it
needs to know the action happened, in time to respond. Those are different
requirements and they have very different costs. If there is a reliable channel
(a message in a specific place, a ticket opened automatically, a note in the
incident log) then delegating the decision does not mean losing sight of it. The
reason reporting back is the price of autonomy rather than a bureaucratic
leftover is that without it, the only way for a lead to stay informed is to be
in the loop beforehand, and being in the loop beforehand is the thing we are
trying to remove.

Those three together are one artifact, not three, and it fits in a paragraph per
area. On the teams where I have seen it exist, it was usually a short section in
the way-of-work document that
[the team wrote for itself](/blog/team-identity-ownership/), and it was written
right after an incident like mine, because that is when the missing boundary is
freshest. The useful move is to write it from the specific case and then
generalize one step, rather than trying to enumerate the authority model for
every situation at once. Nobody finishes that document.

## The Same Three Artifacts, Applied to Agents

I run coding agents daily, and the structure of this problem shows up there in a
form that is almost uncomfortably literal.

An agent gets a goal, a set of tools it may call, and some record of what it
did. That is intent, boundary, and reporting back, except that with an agent you
are forced to make all three explicit, because the system will not run
otherwise. You cannot hand an agent "use good judgment on low-risk changes." You
configure which commands it may execute, whether it can write outside a
directory, whether it can open a pull request or merge one. The boundary becomes
a configuration file. The report-back becomes a log and a diff.

I want to be careful about what that similarity proves, which is less than it
first appears. It does not prove that people should be managed like agents, and
the differences cut in directions that matter. An agent has no career to
protect, so it never makes the defensible move for self-preservation reasons,
which removes the exact failure this post opened with. But that works the other
way too: a person who hits an undeclared boundary usually stops and asks,
because they can feel the edge of their authority even when nobody drew it. An
agent feels nothing. It proceeds, confidently and at speed, straight through an
boundary you forgot to declare. So the undefined boundary that costs you forty
minutes with a person costs you something considerably worse with an agent, and
the artifact has to be more complete, not less.

What the agent case is genuinely good for is as a forcing function. Writing the
tool permissions for an agent working in an area will surface, in about twenty
minutes, every decision boundary your team never agreed on. You have to answer
whether this thing may touch production configuration. You have to answer
whether a change of this size needs a human approver. Those are the same
questions that went unanswered on my team for years, and they went unanswered
because with people you can defer them indefinitely and absorb the cost as
occasional slow nights. With an agent you have to answer them on Tuesday
afternoon to get anything working at all. I have ended up with clearer written
boundaries for my agents than for the humans I have worked alongside, which says
more about how easy it is to defer the human version than about anything
intrinsic to agents.

The engineer from that night is the test I use now. If the same situation
happened again, could he answer "is this mine" from something that already
exists, without paging anybody? If the answer is no, that is not a gap in his
judgment. It is a decision somebody owes him, and the forty minutes are the
interest payment on not having made it yet.

---

_[Independent Fire](/blog/independent-fire/) and
[Far Away Is the Same as Far in the Future](/blog/far-away-is-the-same-as-far-in-the-future/)
both establish that the call is already being made at the edge, whether or not
anyone meant to put it there. What neither one supplies is the artifact: intent
so the person knows what to optimize when the situation is novel, a boundary
concrete enough to evaluate at eleven at night, and a reporting channel so
delegating the decision does not mean losing the thread. Write it from the last
incident where someone correct waited for permission. If you have never written
one and you have been advocating for autonomy, as I had been, that incident has
probably already happened and nobody filed it as a problem._
