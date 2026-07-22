+++
title = "User Story Mapping for Shared Understanding"
date = "2026-07-21"
description = "Around 2022, before AI was useful, I onboarded a whole team into a brand new area with two- and three-hour meetings every day. Documentation was thin, the knowledge lived in people's heads, and everyone was drowning. A working session built around user story mapping cut the fog: put every actor (human or system) on a visible surface, walk the flow out loud, and let the shared picture replace the marathon meetings."
template = "blog-post.html"
[taxonomies]
categories = ["Leadership & Teams"]
tags = ["user-story-mapping", "onboarding", "shared-understanding", "facilitation", "user-stories", "agile", "glue-work"]
[extra]
editorial_track = "leadership-and-teams"
+++

Around 2022, before AI was addictive or even useful, I was pulled into a brand
new area of a very large project. It was the first time I had worked on
something that big, and the area was new to everyone: new teams, new surface in
the platform, almost no documentation. The way we tried to onboard was the way
most teams try: long meetings. We would book time with whoever happened to know
a piece of the system, sit everybody in a room, and try to absorb it all at
once. Two to three hours a day, every day, for a while. It felt like carpeting a
floor by hand. People were sending each other fragments of context, we were
scheduling around calendars to catch the few folks who understood a subsystem,
and it was genuinely hard for anyone to hold the whole picture in their head.

At some point I suggested we stop doing marathon meetings and run a working
session instead, built around user story mapping. The idea is simple: instead of
narrating the system, you map it. You ask what each user is trying to do, where
a user is any actor in the flow, and you lay those actions out on a visible
surface so everyone is looking at the same picture at the same time. Once we
started framing the work in those terms, it got much, much easier to understand
and to write down the flow. The fog lifted faster than any three-hour meeting
had ever lifted it.

## Put the map on a visible surface

The technique is deliberately graphical. You put everything on a medium everyone
can see at once (sticky notes on a wall, or a shared whiteboard) so the model of
the system lives outside of any one person's head. That externalization is the
whole point. In a marathon meeting the picture exists only in the presenter's
mind, and everyone else is trying to reconstruct it from words. On a map, the
picture is the artifact. People can point at it, disagree with it, and fix it in
real time.

I found this genuinely helpful years ago, and it holds up. It is the same reason
we reach for diagrams and shared boards whenever we need to build a common
understanding quickly: a visible medium makes disagreement cheap and alignment
fast. One caution worth stating up front: a whiteboard is where the map is born,
not where it should live forever. Once the shape stabilizes, move it off the
whiteboard and into a longer-term artifact you can maintain over time. The map
is valuable as a living reference, not as a photo of a wall that slowly rots in
someone's camera roll.

## The system is a user too

The move that makes story mapping work for engineering, not just for product, is
letting systems be users. Personification (or anthropomorphism, if you want the
longer word) of the components is what lets you map parts that act on behalf of
a user without being the user. A retry loop, a scheduler, a provisioning
service: each one wants something and takes an action to get it. In a complex
system it helps to generalize the word "user" to "agent," meaning either a user
agent or a system agent. Once every actor (person or process) is an agent with a
goal, the whole flow becomes mappable, and the boundaries between human intent
and system behavior stop being blurry.

The goal of all of this is shared understanding, not more documents. It is easy
to confuse the two. Producing a document feels like progress, but a document
nobody argued over is just a record of one person's assumptions. The map exists
to force the conversation: to get everybody onto the same picture by walking
through stories out loud. User stories here are not requirements. They are a
tool for focusing on the outcomes that actually matter, and for surfacing the
ones that quietly don't.

## How it differs from writing plain user stories

A regular user story follows a familiar template:

- **As a** (who wants to accomplish something) — the persona
- **I want to** (what they want to accomplish) — the clear goal
- **So that** (why they want to accomplish that thing) — the motivation

User story mapping breaks and organizes those stories into groups of personas
and goals laid out along the flow. The motivation (the "so that") is encoded
implicitly by position: because you can see where a story sits in the sequence,
you can see why it is needed without spelling it out every time. So the map is
an intermediate tool. You use it to build the shared picture, and then you
generate the individual, template-shaped user stories out of it, the ones that
eventually land in a backlog. The map gives you the forest; the stories are the
trees you choose to plant.

I want to be honest about where this sits in the reward structure. Gathering
context, running the session, and maintaining the map is glue work: the kind of
connective effort a team genuinely needs but rarely credits, especially if you
are not already senior. That is one of the reasons I care about the technique
even as I try to spend less of my life being the glue. It is also where AI is
already changing the shape of the job. A lot of the heavy lifting (pulling
context out of scattered sources, drafting the first version of the map,
extracting the individual stories) is exactly the kind of work a capable agent
can now accelerate. What is harder to automate is the room itself: getting the
few people who hold the knowledge to talk through the flow together, once, with
a visible surface between them. For a small enough team trying to pull
understanding out of a system, that conversation is still the highest-value hour
you can spend.

## Reference

_User Story Mapping_ by Jeff Patton is the best introduction to using the
technique to scope problems down to their essence. It is available as both an
electronic book and an audio book (I listen to the audio version at about 1.8x
speed; the narration can stand to be sped up for most folks).

- [User Story Mapping (electronic book)](https://learning.oreilly.com/library/view/user-story-mapping/9781491904893/)
- [User Story Mapping (audio book)](https://learning.oreilly.com/videos/user-story-mapping/1491904909/)

---

_This started as an internal wiki I wrote to onboard a team into a brand new
area without burning three hours a day in meetings. The lesson that outlasted
the project is that shared understanding is built on a visible surface, not
narrated into existence. It is the same instinct behind
[Minimize Humans as Glue](/blog/minimize-humans-as-glue/) (the map is a system
that replaces a person standing in the seam) and
[Team Identity Ownership](/blog/team-identity-ownership/) (a picture the whole
team can point at is how belonging and ownership get built). Map the actors,
name their goals, move the map off the whiteboard, and let AI take the parts
that were always drudgery so the human hour can go to the conversation that
actually needs people._
