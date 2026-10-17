+++
title = "The Sprintspective: One Loop for Looking Back and Planning Next"
date = "2026-10-17"
draft = true
description = "Retrospective and sprint planning are usually scheduled as separate ceremonies, but they are parts of one feedback loop. A team should look back, regain context, choose the next direction, and sprint again while the evidence is still fresh."
template = "blog-post.html"
[taxonomies]
categories = ["Engineering Systems"]
tags = ["agile", "retrospective", "planning", "feedback-loops", "contextual-awareness", "continuous-improvement"]
[extra]
editorial_track = "engineering-systems"
+++

In May 2022 I wrote down an awkward word: sprintspective. The issue title tried
to define it before the word settled: combine the prospective and retrospective
in the same flow or feedback loop. In agile we usually stop after a sprint to
run a retrospective, and around the same time we plan the next sprint. I wanted
to combine those activities so people could see what was done and plan what
comes next without losing the thread.

The image I added was stranger and better than the word. Some bugs move very
fast, then stop to saccade and scan their environment, regain contextual
awareness, and sprint again. That was the mechanism I was after. Movement is
useful, but only if the creature stops often enough to reorient. Planning
without looking back is motion without vision. Retrospective without planning is
vision that does not change the next movement.

The usual agile calendar splits the loop. Retrospective asks what happened.
Planning asks what we will do. Because they are separate meetings, they often
develop separate moods. The retro becomes a place for feelings, process
complaints, or generic improvements. Planning becomes a place for capacity math
and ticket selection. The bridge between them is assumed rather than built.

## The missing hinge

A feedback loop needs a hinge between observation and action. The team has to
ask: given what we just learned, what should change in the next interval? If
that question is not explicit, improvement becomes optional. A retro can produce
a list of concerns, but the next sprint plan can still proceed as if none of
those concerns were discovered.

The failure is easy to recognize in small ways. A team says in retro that review
was the bottleneck, then plans another sprint at the same story count. A team
notices that production interruptions consumed a third of the last two weeks,
then treats interruptions as an anomaly again. A team says requirements arrived
late, then accepts new work with the same missing context. Everyone agrees with
the retrospective, and then planning silently denies it.

The sprintspective is a way to force the hinge into the ceremony. It does not
need to be fancy. It can be a single meeting with four movements:

- What did we intend to do?
- What actually happened?
- What changed in our understanding of the work or environment?
- Given that change, what should we do next?

The third question is the important one. It turns the meeting from a status
review into a contextual awareness exercise. The team is not only checking
whether tasks were completed. It is updating its model of reality.

## Stop, scan, sprint

The bug metaphor still works for me because it respects both motion and pause.
The pause is not a failure to sprint. It is what makes the next sprint
intelligent. In knowledge work, the pause has to surface three kinds of
information.

First, it should surface facts about the work. Which estimates were wrong? Which
dependency took longer than expected? Which piece of code resisted change? These
facts improve planning only if they are carried into the next plan.

Second, it should surface facts about the team. Who was overloaded? Where did
handoffs slow down? Which review pattern created delay? Which meeting helped,
and which one only made everyone feel busy? These are not side issues. They are
the operating conditions of the sprint.

Third, it should surface facts about the environment. Did production generate
work? Did a stakeholder change direction? Did a customer support pattern reveal
a missing feature? Did another team ship something that changes our assumptions?
A sprint plan made without this scan is already stale.

Once those facts are visible, the team can decide what to do with them
immediately. Not someday. Not in a process improvement backlog that nobody
opens. Immediately. The next sprint should include the adjustment: reduce
planned feature work because operational load is real, add a quality task
because review pain showed a deeper problem, change how discovery happens
because late context was the repeated failure.

This is the same action-feedback-adjustment rhythm that keeps showing up in
engineering systems. Action creates evidence. Evidence changes the plan. The
next action tests the changed plan. If the rhythm is broken, teams either act
without learning or learn without changing action.

## A ceremony is only useful if it changes behavior

A sprintspective should not become a larger meeting that combines the worst
parts of two smaller meetings. The point is not to make everyone sit longer. The
point is to preserve the causal chain from last sprint's evidence to next
sprint's commitments.

A practical version could be short. Bring the completed work, abandoned work,
unplanned work, incidents, and open questions into one view. Ask what changed in
the team's understanding. Decide on one or two process adjustments. Then plan
the next sprint with those adjustments already applied. If review capacity was
the constraint, planning must show it. If production support is steady work,
planning must reserve room. If the team needs discovery before commitment,
planning must include discovery rather than pretending every story is ready.

The test is simple: can someone point to a change in the next sprint that exists
because of the retrospective? If not, the loop did not close. The team may have
talked honestly, but the system did not learn.

This also connects to
[Development vs Production](/blog/development-vs-production/). Production
feedback needs its own path back into planning. The sprintspective is one local
version of that path. It gives teams a regular moment to say, "Reality spoke
during the last sprint; how will the next sprint answer?"

I am not attached to the word. It still sounds like something invented on a
whiteboard five minutes before lunch. I am attached to the motion: sprint, stop,
scan, adjust, sprint. Teams already do the pieces. The work is to make them one
loop, so the energy of moving fast is matched by the discipline of looking
around before moving again.
