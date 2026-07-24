+++
title = "The GUI Becomes an Output: Voice, Agents, and the End of the Mouse-First Era"
date = "2026-07-24"
description = "The last time I opened a GUI to edit code was back in December 2025. Since then everything moved to the terminal and to voice. A look at why the graphical interface is turning from an input into an output, and what that means for every visual-first tool from Final Cut to node-based shading."
template = "blog-post.html"
[taxonomies]
categories = ["AI & Tools"]
tags = ["agents", "cli", "tui", "voice", "interfaces", "ai-development", "prediction"]
[extra]
editorial_track = "ai-and-tools"
+++

The last time I opened a graphical editor to write code was back in December
2025, around the time I wrote about
[my AI tools journey since Opus 4.5](/blog/ai-tools-journey-opus-4-5/). That is
more than six months ago now. I spent most of my career inside Visual Studio (a
full IDE, the kind of tool I once could not imagine working without), and today
almost all of my code editing happens in the terminal, driven by an agent. That
change felt small at first. The more I sit with it, the more it looks like the
front edge of something larger: the graphical user interface is quietly turning
from the thing you type and click into to the thing you look at. From an input
into an output.

## The Last Time I Opened an IDE to Write Code

For years the IDE was where the work lived. I clicked through files, dragged
panels, watched a debugger, and moved the mouse thousands of times a day. Then
the agent got good enough (the Opus 4.5 threshold I wrote about earlier), and my
use cases for editing code moved to the terminal one by one until there was
almost nothing left in the graphical editor.

I do not think the terminal is the last environment I will use either. What it
gives me right now is simple: it lets me go from voice to text with almost no
friction, and then I can direct the agent with a phrase. The interface became a
little more human. Instead of hunting for a menu item, I say what I want. That
is not nostalgia for the command line, it is the shortest path between a thought
and a result. In
[my operating systems retrospective](/blog/twenty-five-years-of-operating-systems/)
I noticed the same drift: even when I connect to a server, a command line is
usually enough and the dashboard is just there for visibility. The graphical
layer stopped being where I do the work and became where I check the work.

## Visual-First Tools Were Built for Hands, Not Agents

Before I was an engineer I spent about a decade as a
[video editor and media producer](/blog/media-projects-portfolio/). That world
is visual-first in the extreme. Final Cut Pro, Avid, Photoshop, Excel, Word,
PowerPoint (all of them assume a human with a mouse). Every operation is a
click, a drag, a handle you grab and pull. That was the whole point: make it
easy for a person to see everything on the page and manipulate it directly.

Here is the twist. The tools that are easiest for a human are turning out to be
the hardest for an agent, and the ones that felt unfriendly (the ball-of-clay
custom tools you had to drive from a command line) are the easiest for an agent
to pick up. An agent can move a mouse, click, and drag, but that is a clumsy,
brittle interaction. Give the same agent a CLI or a
[TUI (terminal user interface)](/blog/ai-tools-journey-opus-4-5/), and it can
drive the tool directly, without anyone building a graphical bridge in between.
The terminal has quietly become an equalizer: a TUI is often the better choice
now precisely because an agent can talk to it.

In a way it feels like going backwards. Command lines were the Unix and Linux
way, and the reason macOS and Windows won was that a graphical interface was
easier for humans. But the programs that have become bottlenecks for me are
exactly the ones with no interface an agent can drive. I have a drag-and-drop
automation tool (very much like a visual logic-apps canvas) that I still cannot
fully hand to an agent, because the whole thing is a human-first, drag-the-boxes
environment. What was easy for the human is not easy for the agent, and that gap
is now the friction point.

## The GUI as Output, the Voice as Input

Think about node-based shading and node-based compositing (the kind of graph
editing that came out of tools like Shake). It is genuinely wonderful for a
human to build those graphs by hand: all the visual elements are laid out on the
page, and you drag connections and watch the result. I would not want to take
that view away. But I think the visual graph is becoming an output you look at
rather than the only way to input changes. Once an agent is in the loop, I can
just say "move this node left, lower the capacity, change the matte filter," and
the change lands faster than reaching for each control and dragging it. The same
goes for 3D modeling, where you click and drag even with a pen and tablet. Those
interactions are going to shift so that voice and text become the primary way to
drive them, with the canvas as the thing you review.

This is not a new dream. Back in
[my 2014 Swift prediction](/blog/apple-swift-apps-everywhere-prediction/) I was
already asking for node programming and pointing at Shake as the model to copy.
What is different now is the missing half of the loop: a capable agent, and in
many cases a small specialized local model that understands a tool's command
structure the way an expert operator did ten years ago. Where a program does not
grow that kind of interface on its own, I expect bridges to appear (a plug-in
that knows how to talk to the SDK, so an agent can drive music, video, editing,
animation, and effects through the application's own API instead of through the
pixels on screen).

## Retooling the Director's Chair

For a while I wanted to be an animator. Then I learned how long a single second
of animation takes by hand, and I set the idea aside. I think that math is about
to change. An animator will be able to take a captured pose as a base and then
put on a director's hat and shape the motion by describing it, rather than
setting every keyframe by hand. The way Toy Story was animated is not going to
be the way we animate ten years from now. All of those manual clicks and drags
become directions you give instead of motions you perform.

What already happened in software engineering is coming for every field that
works in the digital space. Media production companies will adopt these tools,
take workflows that were entirely human-driven, and make them agent-driven, and
it will happen fast. People will retool to become more like directors and less
like a set of hands on the mouse. That is exciting for someone like me, because
it puts sophisticated work within reach of people who are not full-time
specialists. It is also genuinely unsettling for people who have spent years
mastering those manual crafts and now have to redefine what their job is.

I have seen the leading edge of this before. When I was a video editor, we paid
people we called loggers: they would watch footage and categorize what each shot
was about, second by second, so we could find things later. That is the perfect
job for an agent today. It can look at a video, tag what is on screen every
second (every frame, if you want), and cross-reference objects and faces across
the whole archive. That used to require a room of people, and it was not even
that long ago.

---

_The change I keep coming back to is the one I can see from my own desk: I have
not opened a graphical editor to write code in more than six months, and I do
not miss it. The interface did not disappear, it changed roles. The GUI became
the output I glance at, and voice became the input I actually use. Every
visual-first tool I once drove with a mouse (from Final Cut to a node graph to a
3D scene) is on the same path, either by growing an interface an agent can talk
to or by getting a bridge that gives it one. That fits the pattern I traced
across
[twenty-five years of operating systems](/blog/twenty-five-years-of-operating-systems/)
and [my journey since Opus 4.5](/blog/ai-tools-journey-opus-4-5/): the surface
matters less over time than the work it connects me to. It matters now because
the people who move first from operator to director get to do the interesting
part, and the tools are finally good enough to let them._
