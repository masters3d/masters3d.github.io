+++
title = "9 Years of Copious Notes"
date = "2026-06-29"
description = "Nine years of work notes, from sort-of-daily Markdown files in 2017 to monthly Word docs to a single yearly running document, and how AI agents finally took over the writing through worklogs."
template = "blog-post.html"
categories = ["AI & Tools"]
tags = ["worklogs", "notes", "agents", "copilot", "workflow", "ai-development", "quest-engine"]
[extra]
editorial_track = "ai-and-tools"
series = "quest-engine"
series_order = 16
+++

This whole thing started as a development journal in 2017. Nine years later, the
notes are still going, but almost everything about how I write them has changed.
The medium changed, the cadence changed, and most recently the author changed:
it's now mostly AI driven. I want to walk through that evolution, because the
shape of those files tells the story of how my relationship with note-taking
shifted from manual discipline to something an agent does for me as a byproduct
of the actual work.

## From sort-of-daily Markdown to one doc a year

In 2017 I kept a development journal in Markdown. One file per day, sort of, at
least once a week. The names were dated: `2018-01-08-masters3d.md`,
`2018-01-09-masters3d.md`, on and on through the year. It was a development log,
mostly manual, and the friction was real. You had to remember to write, create
the file, and actually fill it in. Skip a few days and the gaps showed up right
there in the filenames.

Then I moved to Word, one document per month (`2024_01_masters3d.docx`,
`2024_02_masters3d.docx`, and so on). Fewer files, less ceremony, but the same
manual habit underneath. Eventually that collapsed into one document per year,
which I still maintain. The cadence kept relaxing because the discipline of
daily logging never really stuck. The medium was always trying to make the
writing cheaper.

## How AI changes the game

The break came when the notes stopped being something I had to write. With AI
coding agents in the loop, the log writes itself as a side effect of the work.
That's the whole premise behind [worklogs](/blog/why-i-love-worklogs/): the
agent captures context, status, and outcomes as you go, so you get the rigor of
a lab notebook without the overhead. This is the
[Quest Engine's](/blog/quest-engine-introduction/) Searching step made cheap:
building the context that shapes a better decision, except you no longer pay for
it by hand. Nine years of relaxing my cadence to fight friction, and the answer
turned out to be removing the human from the writing step entirely. I don't open
a file anymore. I tell the agent what's happening and it logs it, sizes it, and
links the PR.

The real value shows up later, in consistency. Because the agent logs everything
the same way every time, those worklogs become a structured record you can mine.
That mining is the framework's Renewing step: looking back at what happened and
compounding it into something durable. Writing a brag document used to mean
trying to reconstruct months of forgotten work from memory; now I just point the
agent at the logs and a summary of what I shipped falls out. Consistency is what
makes that possible: same format, same cadence, every entry there because it was
free to write.

There's a second payoff that hits every single day: picking up where you left
off. The expensive part of resuming work was never the typing, it was reloading
all the context you had paged out (what you were doing, what you'd already
tried, what was blocked, what came next). A worklog is a warm cache for that
state. Instead of a cold start where you spend the first half hour
reconstructing where you were, the agent reads the log and you're back in the
thick of it. That shorter startup time is what gets you into flow faster, and
flow lives in the Driven step (the right-sized challenge with tight feedback).
The warm cache doesn't size the work, but it removes the cold-start tax that
breaks flow before you ever reach it. This is also why worklogs stay separate
from [effort tracking](/blog/effort-tracking-vs-task-tracking/): one answers
"what am I working on right now?", the other answers "where is my time going?"

## Feeding the agent meeting transcripts

The biggest recent change is what I feed the agent from meetings, especially the
ones with more than two people. We've had recorded meetings and transcripts
available for a while. For a long time I just took the summary (the
auto-generated recap and the action items) and worked from that. The problem
with a summary is that it has already thrown away most of the context. It tells
you the decision but not the reasoning, the action item but not the disagreement
that shaped it.

Now I hand the agent the full transcript instead. The difference is night and
day: the agent pulls the complete context, not someone else's compression of it.
It can see who raised which concern, what was considered and dropped, the
offhand comment that turns out to matter three weeks later. I don't always need
to keep the full transcript around, but it is genuinely useful to have it
sitting inside the worklog alongside the rest of the work it relates to. The
meeting and the code it affects live in the same place, so the agent reads them
together.

This is the part that finally let me stop manually updating context. I used to
be the one transcribing decisions into notes, distilling a meeting into the
three lines I thought I'd need later, and I was always guessing wrong about
which three lines mattered. Dropping the raw transcript into the worklog removes
that step entirely. The agent does the distillation on demand, against the full
record, with the surrounding work as context. The summary was lossy by design;
the transcript-in-the-worklog keeps everything and lets the agent decide what's
relevant when the question actually comes up.

I still keep some notes private. Worklogs are internal to the team, not public,
but they aren't the place for personal meeting notes either. That single yearly
running document survives for exactly those things: 1:1 notes and private action
items. I've also been looking into private worklogs to bring the same AI-driven
flow to that material. But the trajectory is clear: from manual daily Markdown,
to manual monthly and yearly Word docs, to a log an agent maintains for me. The
notes never stopped; I just finally stopped being the one typing them.
