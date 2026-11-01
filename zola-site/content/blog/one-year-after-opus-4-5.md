+++
title = "One Year After Opus 4.5: Rust Is the New Assembly and the Job Is Systems Engineering"
date = "2026-11-24"
description = "A year after Claude Opus 4.5, the prediction held: an agent writing Bash and an agent writing Rust cost about the same, so the compiler should do the checking instead of tokens. The abstraction layer moved up again, Rust is becoming the new assembly, and the job that is left looks more like systems engineering than typing code. It also turned out to be more work, not less."
template = "blog-post.html"
[taxonomies]
categories = ["Software Engineering"]
tags = ["claude", "agents", "rust", "bash", "ai-development", "systems-engineering", "abstraction", "hiring", "predictions"]
[extra]
scheduled = true
editorial_track = "software-engineering"
related = ["five-levels-of-agent-capability", "software-3-0-needs-engineering-not-magic", "ten-years-in-software-engineering"]
+++

Right now I am finishing a conversion. Over the last few months, a few thousand
lines of Bash went into production at work, all of it written with agents. This
week, still using agents, I am moving every one of those lines to Rust. Nobody
asked me to rewrite working scripts. I did it because the experiment had
answered the question it was set up to answer.

Claude Opus 4.5 came out on November 24, 2025. A few months later I wrote about
[what it changed for me](/blog/ai-tools-journey-opus-4-5/): before it, I only
trusted agents with shell scripts, and after it, Rust became something an agent
could write well. A year in, I want to look at what held up, what I got wrong,
and where I think this goes next. The short version is that the way software
gets made has turned all the way around in a year, and what software engineering
means turned with it.

## Bash or Rust, the Agent Does Not Care

The bet a year ago was that agents would move us toward static languages. We ran
the experiment anyway. We put a lot of scripting language into production, and
what came back confirmed it: there is no difference between an agent writing
Bash and an agent writing Rust. The agent produces either one at about the same
speed, with about the same amount of steering from me.

The difference is everything around the code. With Bash, the only way to know
the script is good is to run it, or to spend tokens having an agent read it
carefully and reason about whether it is good. With Rust, the compiler does that
checking for free, every time, and it does not get tired or skim. In all
honesty, that is the whole trade. Instead of spending tokens convincing myself a
script is correct, I let the compiler tell the agent whether the code is
correct, and the agent fixes what it finds before I ever look at it.

The one real cost is deployment. A script you can copy and paste and run. A
binary needs a compile phase, a build per platform, and a decided story for how
it gets onto the machine. With Rust you have to figure out deployment ahead of
time, which is the same point I landed on in
[language choice in the LLM era](/blog/language-choice-in-the-llm-era/): the
language barely matters to the agent anymore, and the deployment story matters a
lot to everyone else. Once deployment is solved once, it stays solved, and the
compiler keeps paying out on every change after that.

There is a distinction worth keeping here. While I am developing, an agent will
happily write a little Python or PowerShell on the fly to automate a task, look
something up, or reshape some data. That is fine, and I do not expect it to
stop. Runtime glue that lives for an afternoon is a different thing from
software that ships. For the software that ships, I think Rust won.

## The Abstraction Layer Moved Up Again

The way I make sense of this is the arrival of compilers. Before compilers, you
had to really understand how assembly worked, because that was the program.
After compilers, most people wrote in a higher-level language and trusted the
compiler to produce the assembly. Some people still understood assembly deeply,
and they still mattered (someone has to write the compiler, and someone has to
find out why the hot loop is slow), but most programmers stopped needing to read
it.

I think that is happening again, one layer up. Rust is becoming the new
assembly: the thing the agent emits, the thing the compiler checks, the thing
some people understand deeply and most people never read line by line. And the
reason it is Rust (or a language like it) and not Bash or Python is the same
reason assembly was never written by hand once compilers were good. You want the
lowest layer to give the strongest signal. Memory safety is part of that, but
the bigger part is that a strict compiler is the best automated reviewer an
agent has. If the compiler accepts it and a local end-to-end validation suite
passes, the agent knows something is working without me in the loop. A year ago,
building that kind of full validation locally felt like a stretch. I think we
are there now.

Abstractions will keep getting built on top of this, the same way they got built
on top of C. I do not know what they will look like. I do expect that most of
the people building software a year from now will not be reading the Rust their
agents wrote, any more than most of us read the assembly our compilers write.

## The Job Is Systems Engineering Again

So what is the job, if not typing code? I looked back at where my time went this
year, and I would put coding at roughly 20% of it. That number needs a little
care next to the one in
[agents are taking the Drive](/blog/agents-are-taking-the-drive/), where I said
about 80% of the software I produce starts as a prompt. Both are true. One
measures where the code comes from; this one measures where my hours go.

Most of my hours went into the loop around the code: figuring out what was
actually needed, running the thing and validating that it did what was needed,
and then doing another loop. The last part of my time went to managing agents,
and to managing what they cost. Agent consumption is still a big cost factor,
and keeping it aligned with the value of the work is now a regular part of the
job. It is becoming ordinary, though: one more tool in the toolbox, with a
budget like any other.

The rest of my time was never code to begin with. My job already meant working
with operations folks, with project management, and with security folks. Code
was always one part of the solution space, not the whole of it. That is the
reason "software engineering is solved" has never sounded right to me. It is not
solved. It is shifting, and I think it is shifting back toward something older.

Before computers were everywhere, systems engineering was its own discipline:
people whose job was to look at the whole system (the parts, the people who
operate it, the way it gets deployed, the way data gets in and out) and make the
pieces work together. Software made a large share of engineering about writing
the software itself. Now that the writing is cheap, I think we are moving to a
place where humans are less involved with the machinery of the code and more
involved with the questions around it. How do we deploy this? How do we get the
data in? Who operates it, and how will we know when it breaks? Integration,
specification, and validation are where my time goes now, and I would not be
surprised if "systems engineering" comes back as the name for what software
engineers do. It fits the work better than the name we have.

The other thing I did not predict: the last year created more work, not less.
The old idea was that AI would free us from doing so much work. So far it has
mostly let us do a lot more of it. We can get to a V1 really fast. Getting to a
V2 and a V3 (the versions that are reliable, operable, and actually used) is
still hard, and now there are many more V1s waiting for that. There is more that
could be done than I can do. That can be a good thing or a bad thing, depending
on how deliberately you choose. It is not less work.

## What I Expect From the Next Year

These are predictions, not observations, so take them with that label.

The models will keep getting better, but the jump will feel smaller than the one
Opus 4.5 brought. Very unscientifically, the agents I use now (Opus 5.5 being
the most recent) feel maybe 25% better than Opus 4.5. I am fairly sure it is not
actually 25%, but it does feel better: I can get through a lot more, a lot
faster. I also have access to some newer models, like GPT-6 Astra, that I mostly
do not use, because they are too slow for the loop I run. There are still bugs,
like in any other system. The leap that matters now is not in the model. It is
in the systems we build around it.

People who are not adopting AI are going to be left behind. I do not like
writing that sentence, and I do not think it is a game anyone wins by waiting it
out. The job is changing, and it is a different job now. You become a manager of
agents, and you need to understand the business case more than before. It looks
a lot like the move up a career ladder, where the higher you go, the less you do
with your own hands. The difference is that you are still doing a lot of coding;
it just goes through your agents instead of your hands.

That changes what I look for when we hire. Agency is very important. Taste is
very important (I wrote about this in
[craftsmanship, judgment, and taste](/blog/quest-engine-building-high-agency-teams/)).
More than either, I want people who can move up the stack themselves and stop
writing assembly, so to speak. Deep expertise still matters. Depending on the
abstraction you work at, there will be stretches where something really needs to
go fast or use less memory, and you will have to dig in and understand it at the
bottom. Reliability still matters everywhere. But those are dives you take for a
while and then come back up from, not where you live.

I also do not think anyone can now be a software engineer just because agents
write the code. The bar did not drop. It moved to integration, specification,
and validation, and that is where the opportunity is for people who want to grow
into it. If we design our systems around this, I think there is a real
renaissance in software engineering available, and room for the humans in it to
do steadier, more durable work.

---

_A year ago I was surprised that an agent could write Rust I would trust. This
year, the surprise was that the language stopped being the interesting choice at
all: the compiler is the reviewer, deployment is the price, and the work that is
left is deciding what the system should be and proving that it is. That is
systems engineering, and it feels like a different career from the one I had two
years ago. I am excited about it. We get to be the directors of our own movie
now, and I expect next year's review to find that the change I am least sure
about here (the name of the job) is the one that moved the most._
