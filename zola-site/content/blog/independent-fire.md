+++
title = "Independent Fire"
date = "2026-07-08"
description = "A George Washington film handed me a phrase that stuck: 'independent fire.' I cannot vouch that Washington ever said it, but the tactic it points at is real history. The colonists could not win by copying British linear volleys on open fields; they had to use cover and let soldiers pick their own targets. Independent fire is the perfect model for how high-agency engineering teams should be allowed to operate."
template = "blog-post.html"
categories = ["leadership", "teams", "culture"]
tags = ["quest-engine", "autonomy", "high-agency", "team-dynamics", "independent-fire", "command-and-control"]
+++

I was watching a movie about George Washington the other night, and one small
moment caught my attention far more than the big battles did. There was a phrase
in the film that stuck with me: **independent fire.** One thing I want to flag
up front is the attribution: I heard the phrase in the _movie_, and I cannot
confirm that the real George Washington ever said it. That is the only claim I
am making about the sourcing (not that the phrase is invented, just that I do
not know whether Washington used it). What matters more, and is much better
documented, is the tactic underneath it. The film's setup was the years in the
colonies leading into the War of Independence, and the thing it kept circling
was how the colonists fought. They had inherited the European way of war (tight
formations, coordinated volleys fired on command, an officer calling the flanks
and the rows), because that was the only model anyone knew. But that model was
built for open European fields, and much of the fighting in the New World
happened in trees and broken ground and cover. The old formations did not always
fit the terrain, and men who stood in neat lines where the ground did not reward
it paid for it.

What caught me was the idea the phrase points at. Instead of an officer
directing every soldier (aim here, fire now, reload, wheel left), the soldiers
were free to fire independently: to read the ground, pick their own targets, and
act on their own judgment. And this is where the phrase lands on real history.
The Continental Army and especially the militia leaned on exactly this kind of
fighting (open-order skirmishing, aimed fire, using cover and concealment, and
riflemen who could pick off officers and gun crews at ranges where massed musket
volleys were useless). It was a genuine departure from the rigid linear tactics
the British and most European armies fought by, and it is well described in
accounts of the
[Continental soldier](https://history.army.mil/Revwar250/Continental-Soldier/).
So whatever the exact provenance of the words, the tactic they dramatize is
real. And the reason I keep turning it over is that it is not really about
muskets. _Independent fire_ is a statement about where decision authority should
live when the environment stops fitting the plan. That is the quest of this
post: what "independent fire" actually is, why distributed authority beats
centralized command in certain terrain, and why it is the cleanest picture I
have found of how a high-agency engineering team should be allowed to operate.

## The Terrain Broke the Formation

The British formation was not misguided. On an open European field, a wall of
soldiers firing on command is genuinely the optimal design. Coordinated volleys
concentrate force, the officer has a full view of the line, and the individual
soldier does not need to think (he needs to be reliable and synchronized). The
whole system is built on a bet: that the officer's single vantage point sees the
battlefield better than any one soldier does, so decisions should flow down from
that vantage point and the soldiers should be faithful extensions of it.

That bet holds right up until the terrain changes. In the New World, no officer
had a clean view of the whole engagement. The trees that gave the colonists
cover also broke the line of sight the command model depended on. The soldier
crouched behind an oak could see a target the officer could not, and by the time
the order to fire traveled down the chain, the moment was gone. The formation
had turned the soldier's local knowledge into wasted information, because the
system had no way to act on anything the officer did not personally see.

This is the failure mode worth naming precisely: **centralized command does not
fail because the commander is incompetent. It fails when the people at the edge
can see more than the center can, and the system gives them no authority to act
on it.** The formation was optimized for a world where the center had the best
information. The New World was a world where the edge did. When that flips and
the command structure does not, every soldier becomes a bottleneck waiting on an
order that arrives too late or never comes.

## Independent Fire Is Distributed Authority

So what does "independent fire" actually change? It moves the fire decision from
the officer to the soldier. It says: you can see your slice of this fight better
than I can, so you do not need me to tell you when to pull the trigger. Pick
your target, judge your moment, act.

The important thing is what it does _not_ remove. Independent fire is not every
man for himself, and it is not the absence of a plan. The commander still set
the objective (hold this ground, break that advance), still positioned the men,
still owned the strategy. What was delegated was the _local execution decision_,
the one that depends on information only the person on the spot can have. The
soldier inherited autonomy over the moment; the commander kept ownership of the
mission. That split is the whole design. Clear intent from the top, independent
judgment at the edge. It is the same shape as
[being driven inside explicit boundaries](/blog/quest-engine-building-high-agency-teams/):
the freedom is real precisely because the frame around it is clear.

That is also why independent fire is a multiplier and not just a delegation.
When a hundred soldiers can each act on what they see, the team effectively has
a hundred sensors and a hundred decision points instead of one. The center is no
longer the ceiling on how fast or how well the group responds. Contrast that
with the command model, where every soldier is an
[extension of the officer](/blog/minimize-humans-as-glue/), a relay passing the
commander's intent forward but adding no judgment of their own. In easy terrain
the relay works. In hard terrain the relay is exactly where the information
dies. Independent fire replaces relays with agents.

## The Same Fight on an Engineering Team

Here is why the phrase would not leave me alone: I have watched this exact
battle play out on engineering teams, just with tickets instead of muskets.

The command-and-control team is the British formation. A lead (or a manager, or
a process) directs each move. Aim at this ticket. Fire (write the code). Reload.
Now the next one. The engineers are reliable and synchronized, but they are
extensions of the person at the center, and their own read of the ground is
treated as noise, not signal. On simple, well-mapped work, this is fine
(sometimes it is even optimal, the same way a volley is optimal on an open
field). But most real engineering is not an open field. It is trees. The
engineer in the code sees the race condition, the bad abstraction, the thing
that is about to break in six months, long before it reaches the lead's vantage
point. And a team built purely on command turns that local knowledge into wasted
information for exactly the reason the formation did: there is no authority at
the edge to act on what only the edge can see.

Notice that "aim, fire, reload" is not itself the problem. That little
three-beat sequence is actually a complete Quest Engine loop in miniature:
**aim** is Search (read the terrain, pick the target), **fire** is Drive
(commit, apply directed force), and **reload** is Renew (carry state forward and
arm for the next shot). It is the same loop I mapped in
[Set. Action. Reload.](/blog/set-action-reload/), the same three-beat structure
as [Knowing, Walking, Returning](/blog/knowing-walking-returning/) and the
[Search / Drive / Renew](/blog/search-mastery-drive-autonomy-renew-purpose/)
core of the [Quest Engine](/blog/quest-engine-introduction/). Aim-fire-reload is
one of the cleanest small versions of that cycle there is, because a soldier can
run the whole loop in a few seconds and repeat it all day. So the difference
between the formation and independent fire is not _whether_ the loop runs. The
loop runs either way. The difference is _who owns it_. In the formation, the
officer runs the loop and the soldier is just the trigger finger (the aim and
the reload decisions live at the center). Under independent fire, each soldier
owns their own aim-fire-reload, running a full Quest Engine loop on their own
slice of the ground. Distributing authority is really distributing the loop.

The high-agency team is independent fire. The intent is set clearly at the top
(this is the mission, these are the boundaries, this is what we are trying to
win), and then the individual engineer is trusted to read their own slice of the
terrain and act on it without waiting for an order that would arrive too late.
They can fix the thing they see. They can pick the moment. They own the local
decision because they hold the local information. This is not chaos, and it is
not the absence of leadership; it is leadership that has recognized where the
good information actually lives and pushed the decision to meet it. It is also
not recklessness (independent fire still demands a
[calculated read of risk and reach](/blog/fearless-engineering/), just made by
the person closest to the ground rather than the one farthest from it).

The reason this matters more every year is that the terrain keeps getting more
like the New World and less like the open field. The problems are more
distributed, the systems more complex, the relevant information more spread out
across the people actually touching the work. In that world, a team that insists
on routing every decision through a central commander is not being disciplined.
It is standing in neat lines in a forest. The teams that win are the ones
allowed to fire independently: clear intent, distributed authority, a hundred
autonomous reads of the ground instead of one.

---

_Independent fire is the picture I keep coming back to for
[high-agency teams](/blog/quest-engine-building-high-agency-teams/): set the
mission and the boundaries at the center, then push the decision to the edge
where the real information lives. It is the
[autonomy pillar of the Quest Engine](/blog/quest-engine-the-why/) stated in a
single phrase, the opposite of turning people into
[relays for someone else's judgment](/blog/minimize-humans-as-glue/), and a
reminder that the command that worked on the open field is exactly the command
that gets you cut down in the trees. Give the soldiers independent fire, and
give the engineers the same._
