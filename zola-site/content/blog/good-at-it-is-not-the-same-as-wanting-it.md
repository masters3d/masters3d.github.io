+++
title = "Good at It Is Not the Same as Wanting It"
date = "2026-10-18"
description = "I am a good directly responsible individual in an emergency, and I do well against a reasonable deadline. That does not mean I want to live there. Manual toil is shoveling fertilizer: someone has to do it sometimes, it should rotate, and once it passes half the job you stop building. The way out is to build the machine that does the shoveling, and the hardest pile is the one that arrives from another team's pipeline."
template = "blog-post.html"
[taxonomies]
categories = ["Engineering Systems"]
tags = ["toil", "incidents", "on-call", "automation", "ownership", "alignment", "career", "stress"]
[extra]
editorial_track = "engineering-systems"
related = ["promotion-driven-development", "overlapping-roles-in-tech", "locus-of-control-at-work"]
+++

I can tell you, without much false modesty, that I am a good DRI. DRI stands for
directly responsible individual: the one name attached to a problem when
something has to get done and there is no time to argue about whose job it is. I
do well in emergencies. When the system is down and everyone is looking for the
person who will hold the thread, I like being that person. There is a real
excitement in it. Part of it is the chance to be the hero, and I would be lying
if I said that part does not feel good.

I also do well with date-driven development, especially when the date is
reasonable. Give me a fixed launch and a scope that can actually fit, and I will
get there. I narrow down, I cut what does not matter, and I move.

For a long time I treated those two facts as a description of what I should be
doing. If I am good at it, the reasoning went, then this is my lane. It took me
a while to separate the two halves of that sentence. Being good at something
tells you what you can do. It does not tell you what you want to keep doing.

## Shoveling fertilizer is manual toil

The reason I am fast in an emergency is the same reason I cannot stay in one. My
best guess at what is going on is plain stress physiology: the deadline or the
outage raises my cortisol (the hormone the body releases under stress), and I
drop into solve mode. Solve mode is narrow on purpose. It ignores everything
that is not the current problem, it does not ask whether the problem should
exist, and it does not stop until the thing is fixed. That is exactly what an
incident needs. It is also not a state a body is built to hold for months, and I
have written before about how
[burnout was a control problem](/blog/burnout-is-a-control-problem/) for me
rather than an hours problem.

The picture I have for this work is shoveling fertilizer. I am very good at
shoveling fertilizer. I can clear a pile fast and get the path open again. And I
want to be precise about what the shovel stands for, because the picture is not
just a joke about unpleasant work. Shoveling is manual toil. Google's site
reliability engineering (SRE) book has a
[careful definition of toil](https://sre.google/sre-book/eliminating-toil/):
work tied to running a production service that is manual, repetitive,
automatable, tactical, without enduring value, and that grows linearly as the
service grows. Every part of that fits the shovel. You move the pile by hand,
the pile comes back, a machine could move it, it only matters today, nothing is
better afterward, and a bigger farm means more shoveling.

Fertilizer is not useless, either. A garden needs it, and every time someone
feeds their plants there is a lot of it involved. Some amount of shoveling comes
with running anything real. That is why I do not think the answer is to never
pick up the shovel. The answer is that the shovel should not belong to one
person. Toil should rotate. When the same name is on every incident, every
manual deploy, and every cleanup, the team has quietly decided that this person
is the shovel, and the team stops noticing how much shoveling there is.

## Firefighters do not get to build

At work we call these fires. You put out a fire, and if you put out enough of
them you become, in practice, a firefighter. I do not want to be a firefighter.
Sometimes we do have to put out a fire here and there, and I will. But when the
whole job becomes firefighting, something else stops happening.

The people I have seen run incidents best do the full job of an incident
commander. They do not stop at mitigation. They find the cause, they engage the
teams that own the broken piece, they chase the actual issue to the end, and
then they work to keep it from happening again. That follow-through is the right
way to run an incident, and it is expensive. Every hour of it is an hour not
spent on the engineering work that would have prevented the next fire, or on the
new features the team was supposed to be shipping.

The SRE book puts a number on this: their teams aim to keep toil below 50% of
each engineer's time. That matches what I have felt. Once toil passes half the
job, it becomes very hard to move the needle on anything else (on your career,
on finding new problems worth solving, on the product). The calendar fills with
bridge calls, incidents, and fires, and nothing is left for building.

I am a builder. I want to build. Infrastructure has to be built too, but much of
it is a different kind of building: putting pieces together by hand until they
hold. When I talk about building I mean building things that make the next thing
easier. Making the next build faster. Making a process hands-off so nobody has
to stand next to it. The upgrade path from shoveling looks like this:

1. Shovel, because the pile is in the way today.
2. Build a machine that helps you shovel, so the same person moves more, faster.
3. Build a machine that shovels by itself, so nobody has to stand there at all.

Each step moves from reacting to a problem toward solving it. That is the whole
difference between reactive and proactive work, and it is why nobody gets
promoted for shoveling, no matter how fast they shovel. The people who move up
are the ones who mechanize the process. I made the system version of this
argument in [Minimize Humans as Glue](/blog/minimize-humans-as-glue/): a
situation that needs a hero is a situation where a person is standing in for a
fix that was never made. The procedure for building the machine (question the
step, delete it, simplify, speed it up, and only then automate) is the subject
of [Elon's Algorithm](/blog/elons-algorithm-manual-process/).

## When the pile comes from someone else's pipeline

The hardest version of this is being responsible for someone else's code. Say
you are the infrastructure and deployment team, and you have a hard dependency
on another team. When that dependency fails, you are the front-facing team. The
deploy is yours, the page is yours, and the bridge call is yours. The fix is
not. You have to go to a team that does not share your urgency and ask them to
deliver.

That is not an engineering problem. It is an alignment problem. If I am holding
the pager for another team's service, why would that team care about fixing the
failure or shipping the fix? The cost lands on me, not on them. A lot of these
turn out to be what I call sociotechnical problems: the code is the easy part,
and the hard part is who feels the pain and who has the power to stop it. The
question I keep asking is not "how do I shovel this faster?" It is "why does
this pile show up on my doorstep so often, and what would make it stop?"

The fertilizer picture helps me here too. Think about a food processing plant.
Raw product comes in, it is meant to be processed, and it is perfectly good
food. Leave it sitting on the dock long enough and it starts to smell. Leave it
a little longer and you can no longer tell it apart from waste. Nobody shipped
garbage. It became garbage by waiting.

Most of the piles that land on a deployment team look like that. When the change
left the other team's pipeline it was fine. It was real work, meant to be
processed. Then it sat (blocked on a dependency, waiting on an owner, stuck
between two teams that each assumed the other was carrying it), and by the time
it reached my doorstep it smelled. I can shovel it. I am good at shoveling it.
But I can also tell you that this pile did not smell like this a week ago, and
that is the part worth fixing: the waiting, and the ownership gap that let it
wait.

## Choosing where the strength goes

I do not think the answer is to stop being good in a crisis. Emergencies happen,
deadlines are sometimes real, and a team is lucky to have someone who can hold
the thread when they do. I still want to be that person when it counts.

The change is in what I let the strength mean. I treat emergency competence as a
tool I am glad to have, not as a job description. When I notice that I am
enjoying the shoveling, I take that as a signal to ask how often this pile shows
up, who should be sharing the shovel, who is building the machine, and whose
pipeline the pile came from. When a fire is out, I try to spend the next stretch
on work that makes the next fire smaller, instead of waiting for the next alarm
to feel useful against.

The question I ask myself now is simple. Not "am I good at this?", because the
answer to that is often yes. The better question is "would I choose this if I
were not good at it?" If the honest answer is no, then the skill is something I
can lend to the team when it needs it, and the rest of my time belongs to
building the machine that makes sure it needs it less.
