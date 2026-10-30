+++
title = "I Am Tired, Boss: Team Culture Is the Team's Operating System"
date = "2029-04-01"
draft = true
description = "I said \"I'm tired, boss\" in a team meeting as a Green Mile joke, and someone took it literally. That small miss says a lot about team culture: whether people can report how they really feel, whether the team plans at max capacity until it is always underwater, and whether the many asynchronous nodes of a team ever stop to sync. Culture is the operating system of the team, and the first thing a struggling team uninstalls is the part that keeps it in sync."
template = "blog-post.html"
[taxonomies]
categories = ["Human Systems"]
tags = ["team-culture", "team-identity", "retrospectives", "capacity", "on-call", "async", "shared-vocabulary", "toil"]
[extra]
editorial_track = "human-systems"
related = ["team-identity-ownership", "good-at-it-is-not-the-same-as-wanting-it", "sprintspective-one-loop", "remote-work-needs-context-not-just-tools"]
+++

The other day in a team meeting I said, "I'm tired, boss." I was being tongue in
cheek. It is the line from
[The Green Mile](<https://en.wikipedia.org/wiki/The_Green_Mile_(film)>) (a great
movie, by the way), and it has been a meme for years. Somebody took it
literally.

Nothing bad happened. But the miss stuck with me, because it was a small,
precise reading of the culture in the room. I was using a shared joke to say
something true in a low-stakes way, and the joke was not shared. That is the
part worth writing about.

## Memes are a status report

People deal with change differently: changes in company culture, changes in
workload, changes in what is expected of them. I tend to like teams that are
open and vocal about it. I like being able to say "man, lots of hours this week"
or "this is moving very slowly" and have that land as information, not as a
complaint.

Memes and emoji do a lot of this work. When I reply to someone with 🍳, I am not
cooking. I am saying "let him cook": I am working on it, give me a minute. Other
teams use 🔥 for "this is on fire," 🚒 for "I'm going in," 🩻 when someone is
looking under the surface of a problem, and 💀 when someone is thinking about
something they would rather not be thinking about. Some of these are not for
public settings, and that is fine. Inside a team, they are a compressed status
report.

That compression only works if everyone has the same codebook. "I'm tired, boss"
means one thing to someone who knows the movie and another thing to someone who
does not. When the vocabulary is shared, a person can say how they really feel
in three words and an emoji, and the rest of the team gets a good gauge of how
everyone is doing. When it is not shared, people either stop reporting or start
sending only the safe, formal version, and the team loses its cheapest early
warning signal.

So the question is not whether a team uses memes. It is whether people feel
confident sharing their real state, and whether the team has a common language
for it. Both of those are culture.

## Planning at max capacity means always underwater

The early warning signal matters most for one failure mode I have seen more than
once. A team slowly, slowly drifts into working at its maximum. Then it starts
planning at its maximum. Every planning session fills the plate to the edge, and
the team is always underwater: too much to do, too much on the plate, never able
to deliver what it planned.

The plan does not get done because emergent work has nowhere to go. A plan at
full capacity has no room for the incident, the escalation, or the urgent
request from another team, so every one of those pushes planned work out. After
a few cycles the planned work is the thing that never happens, and the emergent
work is the job.

I have written before about
[toil](/blog/good-at-it-is-not-the-same-as-wanting-it/) and the SRE book's
[target of keeping it under 50%](https://sre.google/sre-book/eliminating-toil/)
of an engineer's time. The culture side of that number is what happens when a
team passes it and stops noticing. Toil above half the work becomes the everyday
norm, and it is very hard to grow on a team like that. Nobody remembers choosing
it. It just became how things are.

"I'm tired, boss" is exactly the kind of signal that should catch this drift
early. If the team cannot hear it, the team plans at max again next cycle.

## The first thing a struggling team cuts

When everything goes badly, the first things that go out the door are the
planning session and the retrospective. That is probably the worst thing a team
can drop, because those are the two meetings whose whole purpose is to change
what happens next (I make the case that they are
[one loop](/blog/sprintspective-one-loop/)).

They do not leave a gap, either. They get replaced: dedicated meetings,
firefighting meetings, war room meetings. All of a sudden there are meetings
about meetings about meetings. A lot of work gets done, but almost none of it is
work anyone planned, and it becomes very difficult to grow in that environment.

I love being async. Async is a good default and I would not give it up. But I
think it is very hard to have a team culture without dedicated time to talk
things through: time to talk about the things that bother people, time to look
back, time to decide together. Async handles the work. Sync time handles the
team.

## Night pages and other time zones

One thing I have noticed about myself: if I get woken up at night, I do not
really recover. I have had those cases. The next day is gone, and sometimes the
day after that. I do not know if that is true for everyone, but I know it is
true for me, and I suspect I am not alone.

I have argued that
[waking a human should be rare](/blog/minimize-humans-as-glue/), and that a page
is usually a sign the system needs fixing. The culture side is what you do in
the meantime. The best answer I have seen is fostering real relationships with
teams in other time zones, so that each team can cover the other's night. That
is not a staffing trick. It is a skill a team has to develop: sharing context
well enough, and trusting another group enough, that the work can cross time
zones without waking anyone up. It takes the same shared vocabulary and the same
habit of talking things through, just with a wider team.

## Nodes that go out of sync

I think of culture as the operating system of the team. Each person is a node
running asynchronously, and the operating system's job is to make sure the nodes
regularly share context and sync context.

The failure I watch for is a node that runs on its own for too long. Someone
does something by themselves, without checking with the team, and starts making
promises the team now has to answer for. That is not a good team culture,
because the team is now accountable for a decision it never saw.

At the same time, going out of sync is sometimes unavoidable. There are times
you have to make a call without being able to talk to someone right away. That
is fine. What matters is the return path: the information comes back to the
team, the team can talk it out, and if it was the wrong call, the team can walk
it back. A decision made alone is acceptable. A decision that never comes back
to the team is what breaks the operating system.

## One team, one identity

All of that to say: culture is important, and having a singular identity is
super important. I have written about
[team identity](/blog/team-identity-ownership/) before: a team that names itself
and writes down how it works. This is the other half. A team with one identity
can talk as a team, has a shared vocabulary for how it is doing, keeps the
meetings that keep it in sync even when things are on fire, and can rely on each
other across hours and time zones.

And when someone says "I'm tired, boss," the team knows exactly what it means,
and what to do about it.
