+++
title = "One Year After Opus 4.5: Software Engineering Moves Up the Stack"
date = "2026-11-24"
description = "A year after Claude Opus 4.5, my team is converting a few thousand lines of agent-written Bash and Python to Rust, still with agents. The compiler is a cheaper validator than tokens, Rust is becoming the new assembly, only about 20% of my time goes to code, and the job looks more like systems engineering every month. A year in review and a prediction for the next one."
template = "blog-post.html"
[taxonomies]
categories = ["Software Engineering"]
tags = ["claude", "agents", "rust", "bash", "ai-development", "abstraction", "systems-engineering", "validation", "career-growth", "predictions"]
[extra]
scheduled = true
editorial_track = "software-engineering"
related = ["overlapping-roles-in-tech", "five-levels-of-agent-capability", "software-3-0-needs-engineering-not-magic", "ten-years-in-software-engineering"]
+++

Claude Opus 4.5 came out on November 24, 2025. One year later, I am finishing a
port of a few thousand lines of Bash and Python into Rust. The scripts were
written with agents over the last few months, and the Rust is being written with
agents too. Nobody on the team typed most of either version by hand. What
changed between the two is not who writes the code. It is what checks it.

In February I wrote about
[my AI tools journey since Opus 4.5](/blog/ai-tools-journey-opus-4-5/), and the
claim in that post was that capable agents make compiled languages practical for
work I used to reserve for scripts. Later I turned that into a
[decision matrix for language choice](/blog/language-choice-in-the-llm-era/)
that leaned toward static languages for anything new. This year I got to test
the prediction on real work, and it came full circle: we went the other way
first, and ended up where the prediction said we would.

## The Experiment: Scripts in Production

We put a lot of scripting languages into production this year. It was not a
principled experiment at the start; Bash and Python were the fastest way to get
automation running, and agents produce them as easily as anything else. That
part of my February claim held up completely. There is no difference between an
agent writing Bash and an agent writing Rust. The authoring cost is the same.

The difference showed up after authoring. With the scripts, the only way to know
whether a change was correct was to run it, so validation meant spending agent
tokens reading the script back, reasoning about quoting and exit codes, and
executing it to see what happened. With Rust, the compiler does a large share of
that checking before anything runs, and it does it the same way every time.
Instead of paying tokens to confirm that a script is probably fine, I let the
compiler confirm that the code is well-formed and spend the tokens on the
behavior that actually matters.

Rust does not remove the need for a good signal; it moves where the signal comes
from. What made the port work was a strong compile step plus end-to-end
validation suites that run locally. Between the two, an agent can tell on its
own whether something works, and so can I. That is the setup I would ask for now
on any new piece of software: a compiler that rejects bad code early and a local
suite that proves the whole path.

The real cost of the switch is deployment. A script can be copied onto a machine
and run. A compiled tool has to have its deployment figured out ahead of time:
build targets, artifacts, where the binary lives, how it gets updated. That is
real work, and it is the honest reason scripts are still tempting. But it is
work you do once per tool, while the validation savings show up on every change.

Scripts still have a place, at runtime. An agent that writes a few lines of
Python or PowerShell on the fly to automate a task in the middle of a session is
doing exactly what scripting languages are good at, and that is fine while
developing. The line I draw now is between code the agent uses once and software
we keep. Software we keep gets a compiler.

## Rust Is Becoming the New Assembly

Before compilers, programming meant understanding how assembly worked, because
that was the layer you wrote in. Compilers moved most programmers one layer up,
and assembly became something some people understand deeply and most people
rarely read. I think the same move is happening again, one layer higher.

Agents are the new layer, and the language underneath them is shifting toward
whatever gives the agent and the compiler the clearest signal. Memory safety is
part of that, but not all of it. Strong types, explicit errors, and tests that
live next to the code all make "is this working?" a question the toolchain can
answer instead of a question someone has to investigate. My bet for that layer
is Rust. It is going to be here to stay, and it is going to play the part
assembly used to play: some people will understand it well, others will work
above it, and abstractions will keep getting built on top.

Moving up a layer does not mean the lower layer stops mattering. Some work
really does need to go faster or use less memory, and on those problems someone
has to dig in, read what the agent produced, and understand why it is slow. I
expect to spend stretches of time doing exactly that. Reliability also still
sits underneath everything; a faster way to write code is not a faster way to
make it dependable.

## Where the Other 80% of My Time Went

In October I wrote that
[roughly 80% of my software now starts as a prompt](/blog/agents-are-taking-the-drive/).
Looking at where my time went this year instead of where the code came from
gives a matching number from the other side: about 20% of my time was coding,
and most of that coding went through agents rather than my hands.

The rest went to everything around the code. Deploying it and running it.
Validating that it does what was needed, figuring out what is needed in the
first place, and then going around the loop again. A real share went to managing
agents themselves, and another share went to managing the cost of agent
consumption. Cost is still a big factor, and so is alignment (getting the agent
to do the thing I meant rather than a plausible neighbor of it). When a pattern
of agent work proves itself, it turns into tooling and ends up in the toolbox,
which is its own piece of engineering.

My job also has always involved people who are not writing code: operations,
project management, and security. None of that went away. When people say
software engineering is solved, what I see instead is the work shifting. It is
not that different from before; it moved up the stack, and that is fine.

The surprise of the year is that agents created more work, not less. The old
expectation was that AI would free us from work. So far it has done the
opposite: it made much more work possible. Getting to a V1 is fast now. Getting
to a V2 and a V3 (the versions that survive real users, real operations, and
real change) is still slow, and there is more of that later work in front of me
than I can do. Whether that is good or bad depends on the day, but it is not the
story of engineers running out of things to do. I also still do not think
anybody can just be a software engineer now. The typing got cheaper. Knowing
what to build, proving it works, and keeping it working did not.

This is where systems engineering comes back. Before computers were everywhere,
systems engineering was the discipline of making a whole system work, and
software, when there was any, was only one part of the solution space. Software
engineers have always dealt with the rest of that space (the operators, the
security reviews, the project plans), but the code used to dominate the
calendar. With the code mostly generated, what is left is the system: how it is
deployed, how the data gets in, how it is operated, and how all the parts meet.
Humans are going to be less involved with the machinery of the code and more
involved with those questions.

## What I Expect Next Year

These are predictions, labeled as such.

People who are not adopting AI are going to be left behind. I do not see a way
to win this by waiting it out. The job is completely different now: an engineer
becomes an agent manager, and an agent manager needs to understand the business
case far better than an engineer who only had to implement a ticket. It looks a
lot like moving up a career ladder, where each step up means doing less of the
work with your own hands. The difference is that you are still doing a lot of
coding; it just goes through your agents.

That changes hiring. When we talk about what to look for in new hires, agency
and taste come up first. I wrote about
[craftsmanship, judgment, and taste](/blog/quest-engine-building-high-agency-teams/)
as what humans bring to agent collaboration, and a year of practice made the
list sharper rather than different. A candidate has to be able to move up the
stack themselves, stop writing the equivalent of assembly, and still go deep
when a problem demands it.

On the models: my unscientific sense is that the agents I use now are maybe 25%
better than Opus 4.5 was. The step from Opus 4.5 to Opus 5.5 is real. I can
watch a lot of things get done a lot faster, though I would not defend the exact
number. I have access to Astra as well, but it is too slow for how I work today.
The agents still have bugs, like any other system, and that is the point: we are
moving to systems, and systems need engineering.

So my forecast for the next year is that systems engineering becomes an actual
named thing in software again, not a background skill. A lot of opportunity sits
in that space for people willing to move into it. I am excited about it. We get
to become directors of our own movie, and that is a different career from the
one I started in.

---

_A year ago my bet was on compiled languages for agent-written code; this year
the Bash-to-Rust port is the evidence, from one team and one set of tools. What
would change my mind is a scripting toolchain that gives agents a validation
signal as strong and as cheap as the Rust compiler, or a year in which agents
make V2 and V3 as fast as V1. If either shows up, the stack moves again, and I
will write that one too._
