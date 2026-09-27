+++
title = "Models Are Tools: Portability, Watermarks, and the Work I Want to Keep"
date = "2026-09-26"
description = "A few weeks of running Astra next to Opus 5 left me with three conclusions: the behavior I depend on is mostly harness and habit rather than intelligence, watermarking every output treats a shared piece of work as if the model made it alone, and I want a personal profile that travels with me so the model stops being the thing I have to learn."
template = "blog-post.html"
[taxonomies]
categories = ["AI & Tools"]
tags = [
  "agents",
  "ai-development",
  "portability",
  "watermarking",
  "authorship",
  "tools",
  "harness",
  "film-editing",
  "quest-engine",
]
[extra]
editorial_track = "ai-and-tools"
+++

For the last few weeks I have been running Astra next to my usual model for the
same daily work. Opus 5 is still my primary, and that is the part that makes the
comparison useful: same tasks, same repositories, same harness, different model
underneath. What I expected was a capability difference. What I got was a
behavior difference, and it has been larger and stranger than I planned for.

I ask Astra to do something and it does less than I asked. I ask again and it
does considerably more than I asked. Opus sits closer to the place I want, which
is the thing I asked for plus a small, sensible amount of initiative, and not
one step past that. The gap is not that one model is smarter. The gap is that I
have spent months learning where one of them sits, and I have spent weeks
learning where the other one does.

That is not a model review. It is a portability problem, and it is the actual
subject of this post.

## The thing I am comparing is not the model

When I say Astra gets stuck and Opus does not, I am being sloppy, and I want to
correct myself in public before anyone else does it for me.

What I am comparing is a whole stack. There is the model. There is the harness,
which for almost all of my work is GitHub Copilot. There are the instruction
files I have tuned over a long time, the skills, the sub-agent patterns I picked
up while
[building agent infrastructure](/blog/no-speedup-for-shared-understanding/), and
a large amount of unwritten habit about how I phrase a request. Most of my
leverage lives in those layers, not in the weights. I wrote most of that
scaffolding while watching one model respond to it, so of course it fits that
model better. It would be surprising if it did not.

So the honest version of my complaint is this: my scaffolding is
model-dependent, and I did not design it that way. It happened because I tuned
against whatever was in front of me, which is exactly how you end up with a tool
you cannot put down.

But there is a real residue after I subtract the harness, and the residue is
what bothers me. A good amount of the behavior I rely on does not require
intelligence at all. Staying on a task for a long stretch without wandering off
does not require intelligence. Asking a clarifying question before a destructive
change does not require intelligence. Finishing the thing rather than doing
three quarters of it and declaring victory does not require intelligence. Those
are dispositions, and dispositions should be portable.

Capabilities, I accept, are not portable. A newer model will be able to do
things an older one cannot, and no amount of prompting closes that. Fine. Speed
is not portable either, and I care about that less than I expected to. If I hand
a long task to a model and walk away to have dinner with my wife and my kids, I
genuinely do not care whether it took one hour or two. I care what is there when
I come back. I am not serving a thousand users. I am one person with a
repository and an evening.

What I want is the boring layer standardized: a profile I own that says how I
want to be worked with, which travels across whichever model I point at the
problem. Be proactive in these specific ways. Ask me before these specific
things. Use the Quest Engine loop. Keep a worklog. Do not stop at the first
green check. Right now I rebuild that by hand for every model, and rebuilding it
by hand is the tool getting in my way.

## The watermark question

The other thing pushing me to look around is watermarking.

As I understand the change, Opus 5.5 puts a signature into everything it
produces. I want to be careful here, because I am reasoning about a policy from
the outside and I could be wrong about the details. But if I take it at face
value, my discomfort is not about the mechanism. It is about what the mechanism
assumes.

It assumes the output belongs to the model.

It does not. Almost none of what comes out of one of these sessions is the model
working alone. There is the problem framing, which is mine. There is the
steering, which is mine and which is most of the actual effort. There is the
decision about what not to build, which I have said before is the harder half of
the job. There is the taste applied to three valid approaches, and the
validation pass where I go hunting for the place it breaks. The characters came
from the model. The shape of the thing came from a conversation, and my name is
the one on the pull request. Marking that as machine output is not a lie
exactly, but it is a bad summary of what happened, and it is the kind of bad
summary that gets treated as ground truth by the next system that reads it.

I also think the blast radius is uneven, and code gets off lightly. Code has to
compile. The structure is constrained, the language will not tolerate decorative
variation, and whatever signature survives is going to live in comments, which
get stripped on the way to a binary anyway. If a model wants to claim its
comments, it can have them. The customer is running the binary and does not
care.

Documentation is where this actually bites. I write a lot of it, and the reason
I write it is the reason I gave in
[There Is No Speedup for Shared Understanding](/blog/no-speedup-for-shared-understanding/):
documentation written in the same session as the code is the highest-value
artifact I produce that week, and it is increasingly what the next agent reads
to get grounded. That is [Context as Code](/blog/context-as-code/) with a second
audience. Now imagine every one of those documents carrying a mark that says a
model made it. The first document spreads into the wiki, into the onboarding
path, into the context another agent loads next quarter. It propagates like a
fire through dry grass, and at the end of it the written record of how my
systems work says it was written by something other than the people who decided
how those systems work.

I am not arguing against provenance. I argued for it directly in
[Proof-Carrying Work](/blog/proof-carrying-work/): I want to be able to show
what I understand and what I actually did. That is a claim about people
demonstrating mastery. A blanket watermark is the opposite trade. It attributes
by default, at the source, with no room for the human contribution that made the
output worth keeping. It is provenance pointed at the wrong end of the
collaboration.

I understand where it comes from. There are jurisdictions that want machine
output labeled, and I am not going to pretend that pressure is illegitimate. I
just do not think a signature on every token is the right answer for an industry
where the interesting artifacts are joint work. That is why I am spending time
with more permissive models, and why open weights have gotten more attractive to
me than they were a year ago. Not because of benchmark scores. Because I would
control the output, where it runs, and what goes in and out.

I say this fully aware that there may turn out to be a good reason for the
watermark that I have not thought of, and that stripping one may be neither easy
nor wise. I am describing where my discomfort sits, not announcing a workaround.

## Avid, Premiere, Final Cut

There is a version of this argument I have had before, in a different life.

When I was editing video, there were camps. Avid people, who treated Media
Composer as the professional default. Premiere people, who thought they had the
superior tool. Final Cut people, who thought they had the modern one. The
arguments were real and occasionally heated, and the audience never once cared.
Nobody walked out of a film asking which NLE cut it. The cuts, the fades, the
pacing, the choice to hold a shot two seconds longer than comfortable: all of
that was a person. The tool was a control surface for a decision that had
already been made in someone's head.

The same was true one step down the chain. Color grading happened somewhere
else, with people who did nothing but that. You did not hand them a project
file. You handed over the highest resolution export you had, and they attached a
look to each shot with tools they knew better than anyone in your building, and
handed it back transformed. The interchange format was the whole point. Nobody
had to standardize on the same software to collaborate; they had to standardize
on what passed between them.

And nobody asks whether the award-winning shot came from a Nikon, a Canon, or a
Sony. What I have watched people do instead is shoot on a Sony body with an
adapter so they can keep the Canon glass they already trust. That is the exact
move I want with models. Keep the parts I have invested in. Swap the part
underneath. Do not make me relearn the craft because the mount changed.

I have made this argument about operating systems too, in
[25 Years of Operating Systems](/blog/twenty-five-years-of-operating-systems/):
Windows, macOS, and Linux will all get you where you are going, and the one
worth using is the one that gets out of your way. Models are at the stage where
they have not gotten out of the way yet. Every switch still costs me a learning
tax, and the tax is paid in my evenings.

## The part I still want to do myself

There is one more thread, and it is the one I care about most.

I have an idea I keep circling: a mode where the model guides and the human does
the work. Not to be precious about typing, and not because more turns are
better. Because the small amount of work I do with my own hands is where the
comprehension gets manufactured. I made this case about validation already, and
it applies to authoring too. Reading generated code gives me a pleasant and
largely false sense of understanding. Typing a piece of it, even a small piece,
does not let me fool myself.

This is the darkroom argument. When I was taking film classes, digital cameras
were already mainstream and perfectly good, and some of my classmates still
insisted on learning to develop in a darkroom. Not for nostalgia. For footing.
They wanted to understand the process well enough to reason about it when the
higher-level tool did something unexpected, and to have the vocabulary to talk
to the people who did this for a living. Anyone who jumps straight to the
high-level tool inherits its abstractions without the ability to debug beneath
them, and that shows up the first time the abstraction leaks.

That is my objection to going one hundred percent hands-off. Not that the output
would be bad. The output is often excellent. It is that comprehension is still
paramount, and comprehension has no speedup, and handing over the last piece of
manual work removes the only reliable place where mine was still being made.

So here is where I land. The tools work for me. I do not work for the tools.
When a tool stops producing the quality I want, or starts claiming work that was
not solely its own, or changes enough that I cannot drive it anymore, I should
be free to move, and moving should be cheap. Today it is not cheap, and that is
the actual problem to solve. Not which model is best. How little it should cost
to change my mind about which model is best.

I want the model in the background. I want to do the work, understand the
product end to end, go home, and hang out with my kids. If the industry gets
portability right, the choice of model becomes an implementation detail, which
is exactly what a tool should be.

---

_I am writing this a few weeks into using Astra seriously, which is not long
enough to be sure of anything. The most likely correction is that most of what I
am blaming on the model turns out to be my harness, and that a properly portable
profile closes most of the gap. I would consider that a good outcome. The part I
do not expect to revise is the attribution one: a shared piece of work should
not be signed by only one of the parties that made it._
