+++
title = "The GUI Is Becoming an Output"
date = "2026-07-24"
description = "For thirty years we optimized software to be easy for a human hand. Agents invert that goal. The graphical interface is turning from the thing you drive into the thing you read, and the tools that survive the shift are the ones an agent can talk to."
template = "blog-post.html"
[taxonomies]
categories = ["AI & Tools"]
tags = ["agents", "cli", "tui", "voice", "interfaces", "ai-development", "prediction"]
[extra]
editorial_track = "ai-and-tools"
+++

Here is the observation that started this: I have not opened a graphical editor
to write code since December 2025, when I wrote about
[my AI tools journey since Opus 4.5](/blog/ai-tools-journey-opus-4-5/). More
than six months. I spent most of my career inside a full IDE and could not have
imagined leaving it. Now the editing happens in the terminal, driven by an
agent, and the graphical window is just where I glance to confirm the result.

That is a small personal data point, but it points at a larger inversion. For
about thirty years we optimized software around one assumption: the user is a
human with a mouse, so make everything visible and directly manipulable. Agents
break that assumption. The interface that is easiest for a hand is often the
hardest for an agent, and the reverse is just as true. The graphical layer is
not disappearing. It is changing roles, from the primary input to a secondary
output.

## Human-Friendly and Agent-Friendly Are Pulling Apart

The reason the command line lost to macOS and Windows is not mysterious: a
graphical interface was easier for people. Direct manipulation (see the thing,
grab the thing, move the thing) is a genuinely good match for human perception
and motor skills. That was the right optimization for thirty years, and it is
why Final Cut, Photoshop, Excel, and every node editor look the way they do.

An agent has neither hands nor eyes in the way a person does. It can be told to
move a mouse and click, but that path is slow, brittle, and easy to break with a
layout change. Give the same agent a CLI or a
[TUI](/blog/ai-tools-journey-opus-4-5/) and it drives the tool directly through
text, with no pixel-hunting in between. So the property that made a tool
pleasant for a person (a rich, spatial, mouse-first surface) is now the property
that makes it expensive to automate. The two audiences want opposite things, and
for the first time the machine audience matters enough to design for.

You can feel this line in your own toolchain. The tools that have become
bottlenecks for me are the ones with no interface an agent can reach. I have a
drag-and-drop automation canvas (think a visual logic-apps board) that I still
cannot fully hand off, because the whole product is boxes you wire together by
hand. Meanwhile the awkward, scriptable, command-driven tools I used to tolerate
turned out to be the easy ones: the agent picks them up immediately. What felt
like going backwards to the command line is really the surface migrating to
where an agent can operate it.

## Affordances Are Moving From Space to Language

The deeper change is where the "how" of an action lives. In a GUI, the
affordance is spatial: a slider means "drag me," a handle means "pull me," a
node graph means "wire these together." You express intent by performing a
motion. The new interface expresses the same intent in language: "lower the
capacity, move this node upstream of that one, swap the matte filter." The graph
is still there, and it is still the best way to _see_ the state of the system.
It is just no longer the fastest way to _change_ it.

This is why I keep saying the GUI becomes an output. Node-based shading and
compositing (the lineage that runs through tools like Shake) are wonderful to
read: everything is laid out, and you can see the whole signal flow at a glance.
Keep that. But the editing move (reach for a control, drag it, check, drag
again) collapses into a sentence once an agent sits between you and the canvas.
The same logic applies to 3D modeling, where even a pen and tablet is still a
manual drag. Direct manipulation does not vanish; it demotes to the review step
while described intent becomes the input.

None of this is a new wish. In
[my 2014 Swift prediction](/blog/apple-swift-apps-everywhere-prediction/) I was
already asking for node programming and pointing at Shake. What was missing then
was the other half of the loop: something that could turn intent into the right
sequence of tool operations. That half now exists, either as a general agent or
as a small specialized model that knows a program's command vocabulary the way
an expert operator once did. Where a tool refuses to grow a text interface,
expect a bridge instead: a plug-in that speaks to the SDK so an agent can drive
music, video, animation, and effects through the application's own API rather
than its pixels. The surface an agent needs is smaller than a full GUI, and it
is far cheaper to expose.

## What This Does to the People Who Use These Tools

The uncomfortable part is that this is not confined to code. Whatever happened
first in software engineering tends to arrive next in every field that works in
the digital space, because those fields are already made of files, timelines,
and tool operations. Media, animation, design, and post-production are all
sitting on top of software that assumed a human at the mouse.

I take that personally because I spent about a decade as a
[video editor and media producer](/blog/media-projects-portfolio/) before I was
an engineer. I once wanted to be an animator and gave up when I learned how many
hours go into a single second of hand animation. That arithmetic is what
changes: start from a captured pose, then direct the motion by describing it
instead of setting every keyframe. The way Toy Story was animated is not how the
next one gets animated. And I have watched a version of this before. As an
editor we paid people we called loggers to watch footage and tag what was in
each shot, second by second, so we could find it later. That is now a trivial
job for an agent that can label every frame and cross-reference objects and
faces across an entire archive. It used to take a room of people, and that was
not long ago.

So the winners are not the people with the fastest hands anymore. They are the
people who can direct: state intent clearly, judge the output, and decide what
is worth making at all. That is the same conclusion I keep reaching about coding
itself, where the human work moved up toward
[taste and architecture](/blog/ai-tools-journey-opus-4-5/) once the agent got
good enough to handle the mechanics. It is exciting if you like directing, and
genuinely unsettling if your craft was the manual execution, because the job
description is being rewritten either way.

---

_I am confident about the direction and unsure about the timing. The evidence I
trust most is the boring kind: I have not reached for a graphical editor to
write code in more than six months, and the only tools that still slow me down
are the ones an agent cannot talk to. The safe bet is that every visual-first
tool eventually grows a text or API surface, or gets a bridge that gives it one,
and that "how easily can an agent drive this?" becomes a first-class question
when you choose software. That fits the longer arc I traced across
[twenty-five years of operating systems](/blog/twenty-five-years-of-operating-systems/):
the surface in front of me keeps mattering less than the work it connects me
to._
