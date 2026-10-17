+++
title = "The Kernel of Strategy"
date = "2027-06-15"
draft = true
description = "Rumelt's kernel of strategy (diagnosis, guiding policy, and coherent action) maps cleanly onto engineering work. Diagnosis is contextual awareness, coherent action is clear strategy in motion, and guiding policy is where purpose becomes behavior."
template = "blog-post.html"
[taxonomies]
categories = ["Engineering Systems"]
tags = ["strategy", "contextual-awareness", "guiding-policy", "clear-strategy", "systems-thinking"]
[extra]
editorial_track = "engineering-systems"
+++

In May 2024 I wrote a small reading note from Richard Rumelt's _Good Strategy /
Bad Strategy_. The note had two parts. First, it named Rumelt's three-part
kernel of strategy: diagnosis, guiding policy, and coherent action. Second, it
translated that kernel into my own engineering language: diagnosis maps to
contextual awareness, coherent action maps to clear strategy, and guiding policy
connects to intrinsic motivation, although it is larger than intrinsic
motivation alone.

That last caveat is the reason the note became more than a book summary. The
kernel of strategy is useful because it refuses to let strategy remain a slogan.
It asks for a view of the situation, a policy that channels behavior, and
actions that fit together. Engineering organizations need all three.

## Diagnosis Is Contextual Awareness

A diagnosis is not a list of facts. It is an interpretation of the situation
that makes action possible. In medicine, the symptoms matter, but the diagnosis
is the shape that explains them. In engineering, the symptoms may be late
projects, slow reviews, production incidents, duplicated platforms, low trust
between teams, or customer confusion. The diagnosis is the story that says what
is actually going on.

This is why diagnosis belongs with contextual awareness. Context is not trivia.
It is the map that lets a team orient itself. What changed? Which constraint is
real? Which signal is noise? What history keeps repeating? Which dependency is
quietly controlling the schedule? A team without this awareness can still be
busy, but its motion will be poorly aimed.

The danger is treating diagnosis as blame. "The team is slow" is usually not a
diagnosis. It is a label. A better diagnosis might be that the team is carrying
production work with no planned capacity, that every feature crosses an unclear
ownership boundary, or that the architecture makes small changes require many
reviews. Those diagnoses point to different guiding policies. They also give
people a system to improve instead of a character flaw to defend against.

The best engineering diagnosis compresses complexity without lying about it. It
names the few forces that matter most right now. It gives the team enough truth
to stop thrashing.

## Guiding Policy Turns Purpose Into Behavior

The phrase "guiding policy" is easy to underuse. It can sound like governance,
as if the answer to strategy is a rule document. I think it is more useful to
see a guiding policy as a behavioral bridge. It connects the diagnosis to
everyday choices.

If the diagnosis is that production work is invisible, a guiding policy might
be: production load must be planned as first-class work. If the diagnosis is
that teams are duplicating platforms, a guiding policy might be: shared
capabilities must have named owners and adoption paths. If the diagnosis is that
quality is being inspected late, a guiding policy might be: validation should
move as close to the author as practical.

This is where the connection to intrinsic motivation appears, but only
partially. A good guiding policy can preserve autonomy because it does not
prescribe every move. It says what kind of move is preferred and why. It can
support mastery because repeated choices under a clear policy teach judgment. It
can connect to purpose because the policy makes the larger goal visible in local
decisions.

But guiding policy is bigger than motivation because it also constrains the
system. It changes budgets, review expectations, planning defaults, architecture
standards, and promotion signals. A policy that asks for one behavior while the
organization rewards another is not guiding anything. It is decoration.

## Coherent Action Is Strategy Becoming Real

Coherent action is where many strategies fail. The diagnosis may be insightful
and the guiding policy may sound right, but the actions do not reinforce each
other. One team invests in reliability while another is rewarded for shipping
around the reliability work. Leadership asks for fewer meetings but keeps every
approval path synchronous. A platform team is told to build shared
infrastructure but is measured like a feature team.

Coherence means the actions fit together. They do not have to be grand. In fact,
the most credible strategy often shows up as a sequence of small actions that
all point the same way: change the planning template, add the missing metric,
fund the platform owner, rewrite the review checklist, update the career rubric,
stop starting work that violates the policy.

This is the recursive connection to clear strategy. Vision, design, sprint, and
daily work should carry the same strategic shape at different scales. If the
vision says reliability matters, the design should include failure modes, the
sprint should reserve capacity for hardening, and the daily work should make
operational feedback visible. Otherwise the strategy exists only at the altitude
where nobody has to make a tradeoff.

A strategy is not good because the statement is elegant. It is good when the
kernel holds under pressure: the diagnosis explains the friction, the guiding
policy channels choices, and the actions reinforce each other.

That is why Rumelt's kernel fits engineering so well. Software teams live inside
complex systems, but they still need a small enough strategy to act on.
Contextual awareness gives the diagnosis. Guiding policy converts purpose into
behavior. Clear strategy makes the action coherent. If one piece is missing, the
team may still work hard, but the work will not add up.
