+++
title = "Software 3.0 Needs Engineering, Not Magic"
date = "2028-02-15"
draft = true
description = "Software 3.0 is not a permission slip to trust agents. It is an engineering problem: define the human role, constrain the agent role, and build validation loops around the work they share."
template = "blog-post.html"
[taxonomies]
categories = ["Software Engineering"]
tags = ["software-3-0", "agents", "engineering", "validation", "collaboration"]
[extra]
editorial_track = "software-engineering"
+++

In 2025 I had an agent draft a vision document for what I was calling a
"Software 3.0 engineering framework," borrowing Andrej Karpathy's term for
software that is written as prompts and run by large models. It described a
world where traditional software engineering, built for human-only teams writing
deterministic code, has to make room for agents that write, test, and deploy
code. The generated document was too confident in places, but the question under
it was real: what changes when the thing helping build software is also a
software system with its own context window, tools, and failure modes?

I do not think the answer is that engineering becomes less important. The answer
is the opposite. Software 3.0 needs more engineering around the work, because
some of the execution has become cheaper, faster, and less predictable.

## The Three Software Eras

The source frames the progression in three stages. Software 1.0 is traditional
programming: humans write deterministic instructions. Software 2.0 adds machine
learning systems whose behavior is shaped by data and learned parameters.
Software 3.0 brings in agents that can plan, edit, test, and coordinate parts of
the development process.

That framing is useful if it stays modest. Software 1.0 did not disappear when
machine learning arrived. Software 2.0 did not remove the need for normal code.
Software 3.0 will not remove either one. It adds another layer to engineer. The
agent may generate a patch, but the repository still has invariants. The model
may summarize a codebase, but the build still decides what compiles. The tool
may propose a design, but someone still owns the goal and the tradeoff.

That is why I resist any version of Software 3.0 that sounds like magic. A magic
story says the agent replaces the process. An engineering story says the agent
enters the process as a powerful, fallible participant. The second story is less
exciting, but it is the one a team can operate.

The source names several properties that make this different from ordinary
automation: agent coordination, emergent behavior management, human-cognitive
collaboration, self-modifying systems, and meta-engineering. Those are not
marketing phrases if you translate them into obligations. Who can change what?
What validates the change? Where is the context stored? What happens when two
agents make incompatible edits? How does the system learn without quietly
rewriting its own success criteria?

## The Human Role Gets Narrower and More Important

The source divides responsibilities roughly this way: humans hold strategy,
creativity, ethics, and vision; agents handle implementation, testing,
optimization, and monitoring; both share architecture and problem solving. I
would soften the boundary, but keep the direction.

Agents are good at producing candidate work. They can fill in mechanical code,
scan alternatives, draft tests, and keep multiple files in motion. That changes
the value of the engineer's time. The scarce skill becomes choosing the target,
constraining the search, and verifying the result. I wrote about the validation
side in
[No Speedup for Shared Understanding](/blog/no-speedup-for-shared-understanding/):
comprehension does not become free just because drafting got cheaper.

So the human role does not vanish. It moves toward judgment. The engineer asks
what the system is allowed to optimize, which risks are acceptable, and what
kind of evidence would make the work trustworthy. If that sounds abstract, make
it concrete: an agent can write tests, but a human decides which behavior must
never regress. An agent can refactor a subsystem, but a human decides whether
the migration risk is worth taking now. An agent can produce documentation, but
a human notices whether the document answers the question the next maintainer
will actually have.

This is also where Software 3.0 can go wrong. If the agent gets broad execution
rights without a clear objective, the team has created velocity without a
steering system. If the human keeps all decisions but gives the agent no useful
context, the team has created an expensive autocomplete. The useful middle is a
protocol: enough context for the agent to act, enough limits for the system to
remain safe, enough validation for the human to trust what changed.

## Validation Is the Framework

The source file includes ambitious claims about autonomous testing, autonomous
quality monitoring, self-healing systems, and recursive improvement. I do not
want to dismiss those. I do want to place them behind a gate. A system only gets
to improve itself where the improvement can be measured and reversed.

That means Software 3.0 work needs more explicit validation loops than ordinary
software work, not fewer. The agent's output should pass deterministic checks
where possible: tests, builds, linters, type checks, security scanners, link
checks, policy checks. When deterministic checks are not enough, the review
should name the remaining human judgment: product fit, ethical boundary,
readability, operational risk, or architectural taste.

This is the part of the source I would keep as the core of the framework. The
future is not "agents write all the code." The future is systems where agents
can attempt more work because the surrounding engineering system is strong
enough to catch mistakes, preserve context, and channel learning back into the
next run.

That makes Software 3.0 less like replacing an engineer and more like extending
the engineering surface. The repository now includes code, tests, docs, prompts,
agent instructions, review rules, and memory. All of those are part of the
system. All of them need ownership.

One practical test for this framework is what it refuses to automate. If a team
cannot name the invariant, the agent should not be allowed to change the system
that depends on it. If a team cannot run the validation locally or in continuous
integration, the agent's draft should remain a draft. Software 3.0 becomes
credible when autonomy is earned one boundary at a time, with the evidence
attached to each new permission.

Reading that Software 3.0 vision now, I would keep the ambition and lower the
certainty. Cognitive agents will change the craft, but not by making engineering
optional. They make the old engineering questions sharper. What is the goal?
What is the boundary? What evidence proves this worked? What did the system
learn? If those questions are answered well, agents become leverage. If they are
not, Software 3.0 is just faster uncertainty with a nicer interface.
