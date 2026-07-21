+++
title = "Proof-Carrying Work: Demonstrating Human Mastery in an AI-Assisted World"
date = "2026-07-20"
description = "A proposal for making human and AI contributions visible through provenance, reproducible work, and demonstrated understanding."
template = "blog-post.html"
categories = ["Engineering Systems"]
tags = ["ai", "academia", "research", "authorship", "provenance", "interviews", "proof-carrying-work"]
[extra]
editorial_track = "engineering-systems"
+++

I have been dictating long-form thoughts into AI sessions and asking agents to
help me turn them into blog posts. Sometimes my prompts, corrections, and source
material are longer than the finished post. If you saw only the final page,
though, you would not see any of that. You would see a polished artifact and
have to guess where every phrase came from, what the agent changed, and whether
I understood the argument or merely asked for something that sounded convincing.

That opacity is becoming a problem anywhere an artifact is used as evidence of
ability. A graduate paper is supposed to show that a student can form a
question, find relevant work, gather data, reason about it, and defend a
conclusion. A software interview is supposed to show that a candidate can
understand a problem, make trade-offs, and build a solution. AI can now produce
both artifacts. Banning it does not restore the old signal, because the
technology is already part of how people work. Accepting the artifact without
asking how it was made does not solve the problem either.

The question I want to chase is not, "Did AI touch this work?" The more useful
question is, "Can every phrase be traced to something the human already
communicated, while the machine remains useful without receiving any authorship
authority?"

## From Correction to Collaboration

Spell-checkers and grammar tools removed mechanical friction without taking
authorship away from the writer. We generally do not care whether a student
remembered the spelling of every word. We care whether the words express the
student's thinking. Word processors also made revision, formatting, citation
management, and document assembly easier. Each tool moved some labor from the
human into the machine while leaving the human responsible for the result.

AI continues that progression, but it crosses a more important boundary. It can
reorganize an argument, discover a source, identify a gap, write a paragraph,
generate code, or propose a conclusion. Those operations do not all represent
the same kind of assistance. Fixing punctuation is not equivalent to introducing
a new claim. Reordering ideas already present in a transcript is not equivalent
to inventing the ideas. For the kind of academic authorship tool I am imagining,
the boundary should be stricter: the agent must not generate new prose for the
artifact at all.

The closest familiar analogy may be an executive working with an assistant. The
assistant can arrange the material, prepare a memo, verify its format, and keep
the process moving. The executive can still provide the direction, content,
edits, and final approval. Responsibility remains with the executive. That
relationship works because the people involved understand the roles. With AI,
the assistant is invisible inside the document, so we need a way to make the
roles visible again.

This blog is already one example of why the boundary needs to become visible. I
provide long transcripts, lived examples, connections to earlier ideas,
corrections, and the direction I want the argument to take. An agent helps
organize that material into a cohesive story. I then steer, reject, revise, and
approve it. That workflow is collaborative, but it is not yet the constrained
system I am proposing. Clicking "accept" on agent-written prose does not make
the prose human-authored. In the stricter mode, a suggestion can only become
part of the document after the human says or types the substance of the change
back into the system. The final prose should be traceable to human input, not
merely approved by a human.

## A File That Carries Its Own History

Imagine a local-first desktop application built around a research workspace
rather than a blank page. It could hold the original dictation, notes,
hypotheses, papers read, human-written source summaries, data, experiments,
prompts, AI responses, edits, and final document in one place. Every
transformation would become an append-only event in a timeline. More
importantly, every phrase in the final document would carry lineage back to
recorded human speech, human keystrokes, or an explicitly attributed external
source.

The workspace would have an authorship mode with a hard capability boundary. The
agent could delete, split, reorder, format, correct mechanical errors, or apply
a declared dictionary mapping to words the human supplied. It could not invent a
transition, complete a thought, add an argument, or silently strengthen a
conclusion. Even a mechanically transformed sentence would retain links to its
source spans and a record of the operation that changed it.

Other capabilities would operate outside the authored document:

- **Review mode** could identify repetition, unsupported claims, unclear
  reasoning, or missing connections. It could ask a question, but not answer it
  inside the paper.
- **Research mode** could search for sources and preserve what was retrieved. A
  machine summary would remain research material, not authored prose.
- **Citation mode** could insert a selected quotation with attribution and a
  link to the source passage.
- **Organization mode** could propose a new order, but every moved phrase would
  remain connected to its original human input.

There would be no one-click acceptance of generated content. If the review says
an argument needs stronger evidence, the student must respond with the evidence
and instruct the tool what to change. If research mode finds a new idea, the
student must read it, cite it where appropriate, and explain the connection in
their own recorded words. The agent can query the user for missing knowledge,
much like an oral examiner, but it cannot answer on the user's behalf.

The capture layer matters as much as the editor. Dictation could preserve the
original audio alongside its transcript. Typed input could preserve the text as
it appeared, with optional keystroke timing in a proctored setting. Pasted
material would be quarantined until the user identified it as an external
source, linked it to its origin, or restated it as their own thought. These
signals would not prove what happened inside a person's mind, but they would
make the path into the document inspectable.

The result could be exported as a portable evidence package containing the final
artifact, phrase-level lineage, its revision history, source references,
research data or links to it, AI tool metadata, reproduction instructions, and a
human-readable contribution report. Hashes and signatures could make later
alterations detectable. Selective disclosure would also be essential, because
raw research histories can contain private notes, confidential sources,
unpublished data, or personal information. A verifier should be able to confirm
the integrity of the package without automatically receiving every private
thought inside it.

This should not become an "authenticity score" or a percentage claiming that a
paper is 73 percent human. A score would hide uncertainty while creating a new
target to game. The claim should be narrower and verifiable: every phrase in the
submitted artifact has a recorded path to human input or an attributed source,
and the constrained editor had no capability to insert untraceable prose. The
tool still cannot prove that an idea is original or that the human understands
it. It can show when the idea entered the record, what the author had read at
that point, how it changed, and which questions caused the author to add more
material. The outcome is an audit trail, not a verdict.

There could also be a stronger proctored mode for specific certifications. A
student might complete a designated research exercise in an environment that
records source intake, tool access, notes, and transformations. That could be
useful when the process itself is under examination, but it should not become
the default. Constant recording introduces privacy, accessibility, surveillance,
and power concerns. Ordinary provenance and high-assurance proctoring solve
different problems and should remain separate.

## The Artifact, the Process, and the Defense

An audit trail alone is not enough. A person could carefully stage a transcript,
repeat suggestions they do not understand, or learn how to produce a convincing
history. The final artifact is not enough either, because an unconstrained agent
can generate one. Validation becomes stronger when three forms of evidence
agree:

- **The artifact** shows what was produced.
- **The process** shows how it was produced.
- **The defense** shows that the person understands and can extend it.

For graduate work, a teacher could inspect whether the research question emerged
from the student's notes, whether claims trace back to evidence, whether sources
were summarized and connected rather than merely cited, and whether experiments
can be reproduced. The recorded history could then generate specific
oral-defense questions. Why did you reject this alternative? What changed your
interpretation of this result? Reproduce this analysis with a different
assumption. Explain the strongest source that disagrees with you. Those
questions test the student's relationship to the work rather than their ability
to recite the final paper.

The same model applies to hiring. A candidate could bring an AI-assisted
implementation together with its work history, then explain the architecture,
identify weaknesses, debug a failure, or extend the system under a new
constraint.
[CoderPad describes Meta's pilot of AI-enabled coding interviews](https://coderpad.io/blog/hiring-developers/ai-in-the-interview-is-not-cheating-it-is-the-job-according-to-meta/)
as a way to give candidates tools resembling those used in real engineering
work. That is one sign that interviews are moving from pretending the multiplier
does not exist toward evaluating how a person uses it.

The appropriate level of autonomy depends on the context. In day-to-day software
engineering, I may want an agent to implement, test, and iterate with broad
autonomy while I guide the outcome. In a qualification interview, the system may
need to expose what the candidate knows and how they direct the tool. In a
graduate paper, the constrained editor should have no authority to write new
prose. These are different modes with different trust boundaries, not one
universal policy for AI use.

The point would not be to prove that the candidate can work without AI any more
than we ask an engineer to work without an editor, compiler, or search engine.
The point would be to show judgment: knowing what to delegate, recognizing when
the machine is wrong, understanding trade-offs, and remaining accountable for
the result. A defense remains necessary because traceable words demonstrate
provenance, not understanding.

That changes what we measure. Remembering syntax becomes less important when
syntax is readily available. Forming useful questions, evaluating evidence,
designing experiments, connecting ideas, and defending decisions become more
important. AI does not remove the need for mastery. It makes weak proxies for
mastery easier to see.

## Showing the Work Without Rejecting the Tool

The first version of this system does not need to decide who is qualified or
whether a paper is valid. A minimum useful product could capture voice and typed
input, quarantine pasted text, preserve sources, version a document, enforce a
mechanical transformation policy, display phrase-level lineage and diffs, and
export a self-contained evidence package. A read-only reviewer could explore the
history and create questions for a defense. Judgment would remain with the
teacher, reviewer, or interviewer, while responsibility would remain with the
author.

This is closer to a scientist's lab notebook than an AI detector. Detection
guesses whether a machine generated the surface of the artifact. A constrained
environment prevents the machine from inserting unattributed prose and records
what happened instead. Provenance shows where the language and evidence entered.
Reproducibility asks whether another person can follow the method. Defense asks
whether the author understands the decisions. Together they offer more
confidence than a prohibition that cannot be enforced or a detector that can be
wrong.

The larger shift is from submitting artifacts to submitting accountable work. We
should expect people to use capable tools for mechanical and organizational
labor. We should also expect them to disclose material assistance, preserve the
path from evidence to conclusion, and stand behind what they submit. The
technology should make that discipline easier, not make every student or
candidate reconstruct it after the fact.

_This post began as dictated exploration and became an argument through
collaboration with an agent, making it an example of both the opportunity and
the unresolved problem. Its current history can show extensive human direction,
but it was not produced inside the phrase-level constrained environment proposed
here. That distinction matters. The next step beyond the persistent context in
[Why I Switched to Worklogs](/blog/why-i-love-worklogs/) and the deliberate
handoff in
[The Bicycle of the Mind](/blog/bicycle-of-the-mind-fast-slow-agents/) is a tool
whose limits provide the evidence: the machine can organize, question, and
correct, but the human must supply every idea and every piece of prose they
claim as their own._
