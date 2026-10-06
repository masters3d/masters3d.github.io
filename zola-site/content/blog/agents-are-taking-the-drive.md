+++
title = "Agents Are Taking the Drive"
date = "2026-10-06"
description = "Roughly 80% of the software I produce now starts as a prompt, not a keystroke. Mapped onto the Quest Engine, that means agents have moved into the Drive (the How) and are eating into the four W's. What is left for me is the Why, the context still trapped in people's heads, and the work of running a fleet of agents predictably."
template = "blog-post.html"
[taxonomies]
categories = ["Quest Engine"]
tags = [
  "quest-engine",
  "agents",
  "search-drive-renew",
  "five-ws",
  "context",
  "technical-program-management",
  "tech-debt",
]
[extra]
editorial_track = "quest-engine"
series = "quest-engine"
+++

I keep a rough count of how my own software gets written now, and the number
surprised me when I finally said it out loud: something like 80% of it starts as
a prompt rather than a keystroke. Not because I cannot type it. Because for most
of what I build, I already know what I want, so the remaining act is description
rather than construction. I write the intent, an agent produces the code, and I
spend my attention on validating that it did the thing I meant. That shift
happened in about a year. It is still not a clean 80% of my time saved (I am in
the loop for nearly all of it, prompting, re-prompting, and checking), but the
construction itself is mostly no longer mine.

The interesting part is not the percentage. It is where the percentage landed on
the map. The Quest Engine splits work into
[Search, Drive, and Renew](/blog/quest-engine-the-why/), and those line up with
the questions: the [four W's](/blog/the-four-ws/) (Who, What, When, Where) are
the Search, the [How is the Drive](/blog/quest-engine-introduction/), and the
[Why is the Primary Directive](/blog/the-primary-directive/) that both opens and
closes the loop. Agents did not arrive and take a slice out of all three. They
walked straight into the Drive.

## The Drive Fell First, and the W's Are Falling Next

The Drive is where the How lives, and the How is the most predictable phase in
the cycle. It is bounded by a target that already exists, it has a legible
success condition, and it produces an artifact you can test. That is exactly the
shape of work an agent is good at: a known destination, a mechanical path, a
check at the end. Give an agent all the answers to the Why and it can usually
produce a plausible route.

What I did not expect is how fast the Search started going too. The four W's are
questions about reality, not decisions, and a surprising share of that reality
is already written down somewhere. Who calls this function. What else breaks if
I change it. When this dependency shipped. Where this service actually runs. An
agent can crawl a codebase, a ticket history, and a deployment config and answer
a large fraction of those without me. Call it half, with the honest caveat that
I have not measured it the way I would want to.

The half that does not fall is the half that was never written down. It is in
people's heads. Why this constraint exists, what the team learned the last time
someone tried this, who will quietly veto the approach in three weeks, what
"done" means to the person who asked. No crawl reaches that. And I do not think
we are close to sending an agent to go get it. There are narrow exceptions (a
drive-through order, a first-level customer service triage), but extracting real
context out of a knowledgeable person is still a human act, because the way you
get it is by talking to them about problems until the thing they did not know
they knew comes out.

So the job did not disappear. It moved. If the Drive is automated and half the
Search is automated, then my work is the Why plus the retrieval of everything
still locked in human memory, written down in a form an agent can read. That is
[context as code](/blog/context-as-code/) stated as a job description rather
than a practice: go find the context, get it out of heads, and put it on paper
so it can be siphoned by anyone (including the next agent).

## My Job Was Never the Code

There is a line engineers repeat, and I have never found a canonical source for
it, so I will state it as my own belief rather than a quote: my job is to solve
problems, and sometimes I use software to do it. I believed that before agents
and I believe it more now, because the clause that just got automated is the
"sometimes I use software" part, not the first half.

Solving a problem means generating a solution space and then choosing inside it.
An agentic solution is now one entry in that space, and often the right one, but
generating the space is still the work. Before I can even ask for the How, I
need enough of the W's answered to know what I am aiming at, and I need the Why
sharp enough that I can tell a correct result from a merely working one. That
validation step is the part I cannot delegate, because an agent handed an
unexamined Why will optimize for it with great enthusiasm.

There is a backlog waiting for exactly this. Large parts of the financial system
still run on technology from the 1960s. That code has been a known liability for
decades, and the reason it never got repaid is that the construction cost was
enormous relative to any one team's capacity. We have been living in a perpetual
state of technical debt because paying it down was never the economical choice.
The construction cost is what just dropped. I think this is the moment to go pay
that debt: not to generate more software faster, but to take the systems we have
been afraid to touch and rebuild them as something maintainable end to end. That
is a problem worth solving, and it is squarely a problem of recovering the Why
and the W's behind code nobody alive fully remembers.

## Everyone Becomes a Member of the Technical Staff

The role question follows from this, and it is the part I am least certain
about, so I will label it as a prediction rather than an observation.

A technical program manager's focus is managing projects. An engineering
manager's focus is managing people. I already sit in the overlap between
execution and coordination, which is why I ended up needing
[a Why doc and a How doc](/blog/why-doc-how-doc-steering-agents-from-the-middle/)
to steer agents from the middle. What I see coming is more individual
contributors who manage agents instead of managing people, and a layer of people
management that gets progressively more abstracted away. If that holds, then the
next version of software engineering is agent management, and the people who do
it best will be the ones who can drive a fleet of agents predictably rather than
impressively.

The strange thing about those skills today is that they are people skills.
Agents were modeled on us, so steering one rewards the same things that steering
a person rewards: stating intent clearly, supplying context, checking the work,
correcting without re-litigating. I expect that to change. There will be a push
and pull toward more structure, toward making an agent behave closer to a pure
function (same context in, same result out), and some of the people-shaped
scaffolding will get replaced by something more deterministic. We are early
enough that both styles are being tried at once.

Which makes the AI-lab convention (everyone is a member of the technical staff)
look less like a culture quirk and more like a preview. If the Drive is handled
and the W's are half handled, the remaining distinction between an engineer and
a technical program manager gets thin. What is left is people who hold a Why,
locate reality around it, and run agents through the How. That is one role with
different emphases, not two professions.

_I am aware this reads as good news for the way I happen to work, so the honest
caveat is that my evidence is one practitioner's year. The part I would bet on
is the direction: the predictable phase of the cycle is the one that automates
first, and the Drive is the most predictable phase there is. The part I would
not bet on is the timing, or on how gracefully anybody makes the transition. The
people most practiced at producing code by hand have the most to re-learn, and
what they would be re-learning is uncomfortably close to herding cats. Solving
problems is still the job. The tooling for the middle of it just changed, and
the work that remains is the work that was always hardest: figuring out what is
actually true, and why it matters._
