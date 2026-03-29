+++
title = "Stop Conflating Effort Tracking with Work Tracking"
date = "2026-04-01"
description = "Why effort tracking (where is my time going?) needs to be separate from work tracking (what am I building?) and how centralizing effort in one tool provides visibility that scattered work-tracking systems can't."
template = "blog-post.html"
categories = ["productivity", "workflow"]
tags = ["effort-tracking", "time-management", "azure-devops", "workflow", "productivity"]
+++

I've written before about [why I use worklogs](/blog/why-i-love-worklogs/) to track individual pieces of work. Worklogs answer "what am I working on?" But there's a different question: **where is my time actually going?**

That's what effort tracking is for. And here's the key insight: **effort tracking and work tracking are fundamentally different things that shouldn't be conflated**.

## The Conflation Problem

Most systems conflate effort tracking with work tracking. You have a live site incident system that tracks incidents. You have GitHub for features. You have a security portal for compliance work. Each system tracks the **work** (what needs to be done, what got done), but none of them are designed to answer "where is my time going?"

If you try to track effort in those systems, you run into problems. Live site incidents are about tracking incidents, not tracking your time. GitHub issues are about tracking work items, not tracking effort patterns. When you conflate the two, you lose visibility into your actual time allocation.

**The solution: separate effort tracking from work tracking.** Work tracking stays where it naturally belongs (incidents in your incident system, features in GitHub, compliance work in your security portal). Effort tracking lives in one centralized place focused on one question: where is my time going?

## What Makes a Good Effort Group

My effort groups represent **types of work**, not individual deliverables:

- **Live Site / Production Support**
- **Feature Development**
- **POC / Spike Work**
- **Technical Debt**
- **Security / Compliance**
- **Planning / Design**

These aren't project names or feature names. They're **categories of activity**. Multiple features roll up to "Feature Development." Multiple incidents roll up to "Live Site / Production Support." I use tags to group related tasks together (no hierarchy, just tags), and that gives me the flexibility to see patterns without maintaining a complex structure.

## The "Dev Day" Concept

I track effort in "dev days," which isn't a solar day but what an average day would have of capacity to do work (minus meetings). For my team, that's 4-6 hours of actual work per day, but we track dev days, not hours. There's no strict math, and it's not meant to be super precise.

Some days are longer than others. Some weeks have more days than others (5 vs 6 if you're on-call, for example). A 10-hour day might count as "2 days of effort," though that's rare. The simplicity is the point. I'm trying to understand patterns, not account for every hour.

## Why This Matters

Effort groups answer questions that task-level tracking can't:

**"How much time did I spend on live site work last quarter?"**
With effort groups: one query. Done.

**"Why didn't I finish the planned features this sprint?"**
With effort groups: "60% of my time went to unplanned live site work, leaving only 40% for planned features."

**"Where should I focus to improve things?"**
With effort groups: "I'm spending 50% of my time in reactive mode. If I can reduce that to 30%, I'd have 20% more time for strategic work."

## Tasks vs. Worklogs vs. Effort Groups

To be clear how these differ:

- **Tasks**: What needs to be done ("Implement OAuth login")
- **Worklogs**: Document work in progress with context for AI agents
- **Effort Groups**: Where time is going in aggregate ("Feature Development")

You might have 20 tasks for authentication, 3 worklogs documenting phases of that work, and all of it logs to one effort group: "Feature Development."

## Cross-System Work

One of the biggest benefits: work spans multiple systems. Live site incidents are in one system, security tickets in another, feature work in GitHub, IT requests somewhere else.

With effort groups, I don't care which system a task lives in. At the end of the week, I categorize my time: "1 day on live site, 2 days on features, 0.5 days on POC work." The effort tracking system sees all of it in one place.

## My Implementation: Azure DevOps

My centralized effort tracking lives in Azure DevOps. This is just my implementation detail - you could use any system that lets you centralize effort data.

In ADO, I track effort in tasks or bugs, but these aren't the same as my work-tracking tasks. These are effort-tracking entries. The key is separating the concerns even when they live in the same system. You might use different teams, different iteration paths, or different areas to keep effort tracking separate from work tracking.

I've built simple keyboard-driven tooling that makes logging effort take seconds. I can log a full day, half day, or even 1/3 of a day with just keyboard shortcuts. The tooling automatically subtracts from what's left to do. The granularity stops at thirds - that's coarse enough to be simple, fine enough to be useful.

Here's what an effort entry looks like:

```
Title: Feature Development
Days: 2.5
Week: 2026-W13
Tags: backend, frontend
```

The key distinction: **This ADO task tracks effort (where my time went), not work (what I built)**. The actual feature work is tracked in GitHub, live site work is tracked in the incident system, etc. But the effort for all of it gets centralized here.

**ADO is for tracking effort numbers, not detailed notes.** Detailed notes, context, and work-in-progress documentation go in worklogs (GitHub Issues) or in the actual work-tracking systems. ADO just tracks: which effort group, how many dev days, when.

## Update Frequently (But Not Obsessively)

This only works if you update it regularly. **Minimum: twice a week.** Ideally: daily, or at least three times a week.

The pattern I follow: Monday, Wednesday, Friday. Update effort at the end of those days. If you wait a whole week, you'll forget. If you update twice a week, you can still remember what you did in the last 2-3 days. Daily is better if you can swing it.

The tooling makes it fast enough that daily updates don't feel like a burden. Think about your day, categorize your time, log the numbers. 30 seconds per update, maybe a minute if it was a complex week.

## Why This Matters: Detecting Team Overload

Here's the real value: **visibility into whether your team is overloaded.**

You have three ongoing projects. You planned to spend a third of your time on each. But Project A needs to be done right away, so your team is actually spending all their time on Project A. And they're logging 1.5x normal effort - long days, working weekends.

You need to know that. Effort tracking tells you that.

Or: you planned 50% feature work, but you're spending 80% of your time on live site incidents and zero on development. That's a signal. Maybe it's temporary, maybe it's a problem that needs fixing. But you can't fix what you can't see.

Think of it like CPU monitoring. You don't care about every individual task the CPU is running. You care what those tasks roll up to. Which process is consuming resources? If a game is spawning a thousand tasks and pegging your CPU, you don't debug each task - you see "oh, this game is the problem" and you shut it down. Same concept.

This isn't contractor or lawyer billing where you track hours for invoicing. That requires precision. This is monitoring where you need signal, not perfection. 80-90% accuracy is plenty. You're trying to detect patterns: is the team overloaded? Is time going where we planned? Are we spending more time on one thing than another?

## Effort Groups Evolve

My effort groups have evolved over time. I'm still an individual contributor, but the mix of work changes. Some quarters "Feature Development" is 80% of my time. Other quarters I'm doing more POC work or handling more live site incidents.

The groups adapt to reflect how you spend your time. You can add categories when you take on new work, retire ones that aren't relevant. The framework is flexible because groups represent activities, not organizational structures.

## The Point

**Stop conflating effort tracking with work tracking.** They answer different questions:

- **Work tracking**: What needs to be done? What got done? (the actual deliverables - this feature, that bug fix, this incident)
- **Effort tracking**: Where is my time going? (the aggregate patterns - how much on features vs live site vs debt)

You might have 10 tasks that took 2 days. You don't need to log 0.2 days per task. You log 2 days to the effort group those tasks roll up to. That's the separation.

Effort tracking provides a coarser-grained view than work tracking. You organize work by deliverable (this feature, that incident, this compliance task). You organize effort by type of activity (Feature Development, Live Site Support, POC Work).

The centralization is what makes it work. Work tracking can be distributed across multiple systems - that's fine, each system is optimized for its type of work. But effort tracking needs to be in one place, focused on one thing: where is my time going?

Even if you use the same system (like ADO) for both, keep them separate. Different teams, different areas, different iteration paths. The separation of concerns matters more than the physical location.

Combined with worklogs (what I'm working on, captured with context for AI agents) and work tracking (individual deliverables in their respective systems), centralized effort tracking gives me visibility into whether my time allocation aligns with what matters most. Whether I'm spending more time on areas that I didn't plan for and want to address in the next quarter or month.

---

*This post builds on my earlier post about [worklogs](/blog/why-i-love-worklogs/). Worklogs and effort tracking serve different purposes and complement each other in my workflow.*
