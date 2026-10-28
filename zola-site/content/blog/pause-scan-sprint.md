+++
title = "Pause, Scan, Sprint: The Beetle That Cannot See While It Runs"
date = "2027-01-22"
description = "The tiger beetle runs so fast that its eyes cannot form an image, so it chases prey in bursts: pause, scan, sprint, and loop. Work has the same trade-off between speed and sight. The pause is not lost time. It is the only part of the loop where you can see where you are going."
template = "blog-post.html"
[taxonomies]
categories = ["Engineering Systems"]
tags = ["feedback-loops", "contextual-awareness", "focus", "planning", "tiger-beetle", "pacing", "rest", "search-drive-renew"]
[extra]
scheduled = true
editorial_track = "engineering-systems"
related = ["sprintspective-one-loop", "action-feedback-adjustment", "kaizen-and-the-observe-orient-decide-act-return-loop", "adaptive-control"]
+++

In May 2022 I wrote a note about "some bugs" that move very fast, then stop to
scan their environment, then sprint again. I did not name the bug. It has a
name, and the reason it stops is better than the one I had assumed.

The tiger beetle is one of the fastest runners for its size. In 1998 Cornell
reported Cole Gilbert's finding that
[tiger beetles go blind temporarily](https://news.cornell.edu/stories/1998/01/tiger-beetles-go-blind-chasing-prey-high-speeds)
when they chase prey at full speed. Their eyes cannot gather enough light to
form an image of the prey while the beetle itself is moving that fast. So the
beetle does not chase in one smooth line. In
[Gilbert's 1997 study of how tiger beetles pursue prey](https://doi.org/10.1007/s003590050108),
the chase is a series of runs broken by stops. The beetle runs toward where the
prey was, stops, finds the prey again, turns, and runs again. It repeats this
until it catches the prey.

I had pictured the stop as a rest, or as caution. It is neither. The stop is
where the seeing happens. While running, the beetle is committed to the last
direction it chose. It cannot update that direction, because it has no image to
update it with. Speed and sight compete for the same eyes.

## Pause, scan, sprint, loop

That gives the loop four parts, and each one does a different job.

- **Pause.** Stop moving long enough for the picture to settle. For the beetle
  this is mechanical: the image stops blurring. For a person or a team it means
  stopping the work long enough that new information can register instead of
  bouncing off momentum.
- **Scan.** Find the target again and check where you are relative to it. The
  prey has moved. The ground has changed. The direction chosen at the last stop
  is now old.
- **Sprint.** Commit to a direction and move fast without second-guessing it.
  The sprint is valuable precisely because it does not stop to look.
- **Loop.** Go back to the pause. The sprint is planned to end, not left to run
  until something goes wrong.

The order matters. A sprint without a scan before it is a guess carried out at
full speed. A scan without a sprint after it is observation that never becomes
progress. And a pause without a scan is rest that never turns into a new
direction: the legs recover, but the beetle sets off toward the same old spot.

The loop lines up with the three moves of the
[Quest Engine](/blog/quest-engine-introduction/), which I use as a lens here
rather than as the subject. The pause is **Renew**: rest first, the plain
recovery that lets the picture settle, and then the comparison of where the last
run ended against where it was meant to end. The scan is **Search**: find what
is true right now, before acting on it. The sprint is **Drive**: commit to a
goal and execute without reopening the decision every step. The model writes the
cycle as Search, Drive, Renew; the beetle enters the same cycle at Renew,
because every chase after the first one begins by stopping. What the beetle adds
is a hard constraint the model only implies. The moves cannot overlap. Drive
blinds Search, so the loop has to take turns, and the turn that makes the others
possible is the rest.

## Work has the same blind spot

Focused work behaves like the beetle's run. When I am deep in an implementation
I am fast because I have stopped looking around. I am not reading the team
channel, rechecking the requirement, or asking whether the problem changed this
morning. That is what focus is for. It is also why focus has a blind spot: the
same narrowing that makes the sprint fast means the world can move without my
noticing.

The failure is not sprinting. The failure is believing you can scan while
sprinting. A team that tries to stay fully aware at all times never gets the
speed. Every interruption, status check, and context switch is an attempt to
look while running, and like the beetle's eyes, the picture comes back blurred.
A team that never stops gets the opposite failure. It runs hard in the direction
it chose weeks ago, toward where the target used to be.

The beetle shows a third option: separate the two modes in time. Run without
looking, then stop and look without running. Neither mode has to compromise for
the other, because they never happen at once.

The beetle does have one sense that works during the run. A later study from
Gilbert's lab found that tiger beetles hold their antennae rigidly forward while
running, and
[use them to feel obstacles that their blurred vision misses](https://doi.org/10.1098/rspb.2013.3072)
(Zurek and Gilbert, 2014). The antennae keep the beetle from running into a
wall. They do not tell it where the prey went. I think that is a useful
distinction for engineering work. Tests, builds, alerts, and code review are
antennae. They catch the obstacle directly in front of you while you are moving
fast, and they should run during the sprint. They cannot tell you whether you
are still chasing the right thing. Only the pause and scan can do that.

This is also why [context hunting](/blog/context-hunting-vs-context-gathering/)
belongs at the stop and not in the middle of the run. The scan is active. The
beetle does not wait for the prey to reappear in front of it; it turns and looks
for it. A useful pause asks the same kind of question: what moved since the last
time I looked, and where is the target now?

## How long to run before stopping

The hard part is the length of the sprint. I do not know exactly how the beetle
tunes it, but the trade-off is easy to see. Stop too often and the beetle never
reaches the prey; stop too rarely and it ends up far from where the prey went.
The right length depends on how fast the target moves. A slow target allows a
long run. A target that changes direction often needs short runs and frequent
looks.

The same rule holds for work. A well-understood migration with a fixed end state
can run for weeks between checks. A new product feature, an incident, or a
project whose stakeholders are still deciding what they want needs short sprints
and frequent scans. The mistake is using one cadence for both, usually the one
written in the process document rather than the one the target requires.

I now think of every pause as a small scan with three questions. Where is the
target now? Where am I relative to it? What direction will I commit to for the
next run? If the pause answers those, it was not lost time. It was the only part
of the loop where I could see.

The note I wrote in 2022 was about agile ceremonies, and how a team closes that
loop together is a separate argument from this one. The beetle's lesson is
smaller and personal. It does not need a ceremony to know when to stop. It stops
because it is blind while it runs and knows it. The habit worth building is the
same admission: I cannot see while I sprint, so I will stop on purpose, look,
and then run again.
