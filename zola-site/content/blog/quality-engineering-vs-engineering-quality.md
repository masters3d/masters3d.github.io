+++
title = "Quality Engineering vs Engineering Quality"
date = "2026-10-17"
description = "Engineering quality is a property of what ships. Quality engineering is the practice that produces it, and that practice cannot be handed to another team. Quality, security, and documentation belong to the engineer who builds the thing, and the reward system has to pay for those behaviors or they quietly stop."
template = "blog-post.html"
[taxonomies]
categories = ["Engineering Systems"]
tags = ["quality", "ownership", "security", "documentation", "incentives", "shift-left", "systems-thinking"]
[extra]
editorial_track = "engineering-systems"
related = ["overlapping-roles-in-tech", "guiding-policies-behavior-alignment", "development-vs-production"]
+++

In May 2024 I wrote myself a note with a title that looked like a typo: "Quality
Engineering vs Engineering Quality." The two phrases use the same words in a
different order, and they are easy to treat as interchangeable. They are not.
Swapping the order moves the responsibility to a different person, and that
difference shows up in how software gets built, who gets paged, and who gets
promoted.

The note I wrote that day was short. The main difference between quality
engineering (QE) and quality assurance (QA) is that we do not separate quality
from the responsibility of the software engineer. Quality is part of the
product, not a later step deferred to another team. Then I wrote two more
sentences that turned out to be the real point: the same is true for security,
and the same is true for documentation. This post is my attempt to finish that
note.

## Two Phrases, Two Owners

Engineering quality is a property of the output. It is what a user experiences:
the thing works, it does not lose data, it fails in ways that make sense, it can
be changed next year without fear. You measure it after the fact, by looking at
what shipped and what broke.

Quality engineering is the practice that produces that property. It is the set
of habits, tools, and decisions made while the work is happening: the test
written before the fix, the error path considered during design, the rollout
plan, the alarm that fires before the customer notices. You cannot measure it by
looking at a finished artifact alone, because it lives in the process that made
the artifact.

The traditional QA model treats engineering quality as something a separate
group can inspect into the product. Developers build, a QA team checks, and
defects travel back across the boundary. That model has a structural flaw that
has nothing to do with how skilled the QA team is: the people who make the
decisions that create defects are not the people who feel the cost of those
defects. The feedback arrives late, through a handoff, and addressed to someone
who has already moved on to the next task. Every boundary in that loop adds
delay and removes context.

Quality engineering removes the boundary. The engineer who writes the change
owns its tests, its failure modes, and its behavior in production. That does not
mean testing specialists disappear. It means their job changes from inspecting
other people's output to building the systems (test infrastructure, synthetic
environments, release tooling) that let every engineer own quality cheaply. I
wrote about one version of that system in
[Shift Left Until the PR Is Just a Confirmation](/blog/shift-left-synthetic-environments/):
when validation is cheap and local, the review step stops being a gate and
becomes a way to share context.

## Security and Documentation Follow the Same Rule

The second half of my note is where the idea gets more useful, because the same
reasoning applies to two other things organizations like to hand off.

Security is a quality attribute. An injection bug or an overly broad permission
is a defect that happens to have an attacker attached. If a separate security
team is responsible for it, the same late, context-poor loop appears: someone
else finds the problem after the design is settled, files it back across a
boundary, and the engineer fixes the symptom without learning the pattern. A
security team is valuable when it builds guardrails, libraries, threat models,
and reviews that raise every engineer's baseline. It is a liability when it
becomes the place where security responsibility goes so that nobody else has to
hold it.

Documentation is the third case, and the one I find people resist the most.
"Documentation" undersells what it is. It is context: why a decision was made,
what the system assumes, what the next person needs to know to change it safely.
There is no documentation team that can write that context, because only the
person who made the decision has it, and only while it is fresh. If that
engineer does not write it down, the context is lost, and what remains is a
system that works for reasons nobody can explain. I have argued elsewhere that
[context should be treated like code](/blog/context-as-code/), and this is the
ownership half of that argument: the person who produces the change produces its
context.

Put the three together and a pattern appears. Quality, security, and context are
not features you add to a product. They are properties of how the product was
made. Any property of how something was made has to be owned by whoever is
making it. Moving it to another team does not move the work; it moves the
discovery of the missing work to a later and more expensive moment.

This is not only a software idea. A kitchen does not have a separate team that
makes food taste good after the cooks are done, and a structural engineer does
not leave load calculations to an inspector. Inspectors and food critics exist,
but nobody expects them to supply the quality. They confirm it, or they catch
the rare thing that slipped through. Software is unusual only in how long it
tolerated the opposite arrangement.

## The Reward System Has to Agree

The last line of the original note was the hardest to act on: this mindset
change has to apply to reward systems. You can tell engineers that quality,
security, and context are their responsibility, but if promotions go to whoever
shipped the most visible feature, people will learn the actual rule very
quickly.

Quality engineering is mostly invisible when it works. The outage that did not
happen does not show up in a promotion packet. The design document that saved
the next team three weeks is rarely cited. The test that caught a regression
before review looks, from the outside, like nothing happened at all. Meanwhile,
the engineer who happened to land on a highly visible project gets credit for
outcomes that were partly luck. I wrote about the same imbalance from the
reliability side in
[The Last 20% and the Next Nine](/blog/the-last-twenty-percent-and-the-next-nine/):
the first 80% gets the demo, and the part that makes the thing actually usable
gets far less recognition.

The fix I wanted then, and still want, is to reward behaviors rather than
results that depend on luck or visibility. That requires measuring behaviors,
which is harder than counting launches, but not impossible. Some signals I
trust:

- **Defects found before merge versus after** for the changes an engineer owns,
  which shows whether quality is being built in or inspected in later.
- **Incidents traced to missing context**, such as an undocumented assumption or
  an alarm nobody understood, which shows whether context is being produced.
- **How often other engineers reuse someone's tests, tools, or write-ups**,
  which shows quality engineering spreading beyond one person.
- **Reviews and design feedback that changed a decision**, which shows
  responsibility being exercised before the work is done instead of after.

None of these are perfect, and any of them can be gamed once it becomes a
target. That is a reason to use several and to read them as evidence for a
conversation, not as a score. It is also why
[blameless incident review](/blog/blameless-engineering-debugging-systems-not-people/)
matters here: if finding a defect gets someone punished, people stop finding
them early and the measurements turn into a record of who hid problems best.

Looking back at that note, the word order still carries the whole idea.
Engineering quality is what you hope to get. Quality engineering is what you
have to do, and it only happens when the person doing the work owns the result
and the organization notices when they do. Handing quality, security, or context
to someone else feels like specialization, but in practice it is a delay with an
org chart attached. What I would add to the note today is the part I could not
answer then: the behaviors only last on teams that have found a way to see that
work and pay for it.
