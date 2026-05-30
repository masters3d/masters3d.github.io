+++
title = "Documentation. Configuration. Code."
date = "2026-05-30"
description = "Configuration earned its place next to code: versioned, reviewed, owned. Documentation deserves the same treatment. And the cognitive artifacts that precede code (design docs, context docs, the operating system humans run the whole thing by) often carry more value than the code itself, because they're what produces the code."
template = "blog-post.html"
categories = ["engineering", "productivity", "workflow"]
tags = ["documentation", "configuration", "alignment", "high-agency", "knowledge-management"]
+++

There was a time when configuration was treated as an afterthought. It lived in a file someone edited by hand on a server, undocumented, unreviewed, owned by whoever touched it last. Then the industry grew up. Configuration became code: versioned in the same repository, reviewed in the same pull requests, tested in the same pipelines, owned with the same seriousness. Infrastructure as code, config as code. We stopped pretending the settings that determine how a system behaves were somehow lesser than the logic inside it.

I want to make the same argument for documentation. **Documentation should be held in the same regard as configuration and code.** Not below it. Not as the thing you write up afterwards if there's time. At the same level.

And when I say documentation, I don't just mean the manual we hand to users. I mean the operating system that humans use to run the whole thing: the design documents, the context documents, the written-down shared understanding that lets a group of people build the same system in the same direction. That layer, in my view, often carries more value than the code, because it's what produces the code in the first place.

## The Precursor Has Higher Value Than the Product

Here's the part that sounds backwards until you sit with it: the cognitive artifacts that come *before* the code are worth more than the code.

You can dive straight into the code. You can skip the design doc, skip the alignment, skip writing anything down, and produce something that works. That's real, and I'm not going to pretend otherwise. A single person with enough skill can hold the whole model in their head and ship. For a while, that's faster.

But the code is a *result*. It's the output of a series of decisions about what to build, why, for whom, with what tradeoffs, under what constraints. Those decisions are the expensive part. The code is the cheap part (and getting cheaper every month). When you write the design document, the context document, the shared description of what you're trying to do and why, you're creating the thing that *generates* the code. Get the precursor right and the code follows almost mechanically. Get the precursor wrong and no amount of clean code saves you, because you built the wrong thing beautifully.

This is why I treat the artifacts that come ahead of the code as the high-value layer. **You create them to get alignment, and then you write the code.** Not the other way around. The order matters. If you produce alignment after the fact (writing the doc to describe what already got built), you've inverted the value. The doc becomes a transcript instead of a blueprint. The expensive thinking already happened in private, in someone's head, unreviewed, and now you're just recording it.

## To Be Clear, Not All Artifacts Are the Same

I want to draw a line here, because "documentation" gets used to mean very different things.

I'm not talking about the issue you filed, the ticket, the scratch notes from a meeting. Those cognitive artifacts have their own value, both in the moment and as a record you can return to later. It's genuinely good to be able to go back to them. But that's intermediate value: useful, real, and not what I'm pointing at.

What I'm pointing at is the durable layer that drives long-term, highly effective execution across a team. The documents that encode how the system is meant to work, why it's shaped the way it is, what the constraints are, and how a new contributor is supposed to reason about it. That's the operating system humans run the whole thing by, and it's the thing that lets a team scale past the size where one person can hold everything in their head.

## What You're Actually Buying

So why pay the cost? If you can ship without it, what does treating documentation at the level of code actually buy you?

It buys you a holistic system that everyone understands. It buys you the ability for new folks to contribute at scale, because the context they need is written down and reviewable instead of locked in the heads of the people who were in the room. It buys you a raised quality bar, because when the shared understanding is explicit, anyone can spot where reality has drifted from intent and pull it back. **A system that only one person understands has a quality ceiling set by that one person. A system whose cognitive artifacts are first-class has a ceiling set by the whole team.**

This is the same trade configuration made. We didn't move configuration into version control because it was fun. We did it because settings that drift silently, owned by no one, reviewed by no one, are a liability that compounds. Documentation that lives only in someone's memory is exactly that same liability, one resignation away from being lost.

Treat your cognitive artifacts the way you treat your code. Version them. Review them. Own them. Keep them current. Hold them to a standard. They are not the thing you do after the work; for the work that matters, they *are* the work, and the code is what falls out the other side.

**Documentation should be held in just as high regard as configuration and code.**
