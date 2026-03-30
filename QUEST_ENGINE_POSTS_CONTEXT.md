# Quest Engine Time-Scale Specific Posts

## Context

Three detailed Quest Engine blog posts have been created that explore how the framework applies at different time scales. These posts are currently marked as drafts and should be published after the introduction post is live.

## Posts Created

### 1. Quest Engine: Day-to-Day Tactics
**File:** `zola-site/content/blog/quest-engine-day-to-day-tactics.md`
**Date:** 2026-04-15
**Status:** Draft

Focuses on tactical daily workflow application:
- Connects to worklogs, effort tracking, and dev days
- Shows practical examples of applying three pillars at daily level
- Debugging sessions, daily planning, capacity allocation
- Links to existing workflow posts

### 2. Quest Engine: 6-18 Month Strategy
**File:** `zola-site/content/blog/quest-engine-6-18-month-strategy.md`
**Date:** 2026-04-22
**Status:** Draft

Focuses on project-level planning (6-18 months):
- Design documents, vision documents, retrospectives
- Project selection based on intrinsic motivation (mastery, autonomy, purpose)
- Dev day budgets and effort allocation over quarters
- Quarterly planning rhythm

### 3. Quest Engine: Career Vision and the Long Game
**File:** `zola-site/content/blog/quest-engine-career-vision.md`
**Date:** 2026-04-29
**Status:** Draft

Focuses on decade-long career arcs (10+ years):
- Applies genetic algorithm metaphor at career level
- Career transitions: specialist/generalist, IC/leadership, domain shifts
- How the three pillars compound over time
- Career arc examples spanning 20 years

## Publication Plan

These posts should be published in sequence after the introduction post:

1. **First:** Publish [Quest Engine: A Framework for Agent-Human Collaboration](zola-site/content/blog/quest-engine-introduction.md)
   - Establishes Quest Engine as methodology for agent-human collaboration
   - Explains three pillars: contextual awareness, intrinsic motivation, clear strategy
   - Shows where agents and humans differ

2. **Then:** Update time-scale posts to reference introduction post
   - Each post should link back to introduction for framework context
   - Ensure cross-references between all four posts work correctly

3. **Finally:** Publish time-scale posts in order
   - Day-to-day tactics (April 15)
   - 6-18 month strategy (April 22)
   - Career vision (April 29)

## Publishing Steps

For each post:
1. Open the markdown file in `zola-site/content/blog/`
2. Change `draft = true` to `draft = false` in frontmatter
3. Verify the date is appropriate for publication
4. Commit and push changes

## Notes

- All posts link back to source material in the [ingenio repository](https://github.com/masters3d/ingenio/tree/main/presentation)
- Posts use `draft = true` to prevent early publication
- Total content: ~30KB across four posts
- Posts form a cohesive series exploring Quest Engine at different scales
- Each post is practical and shows how Quest Engine helps get work done

## Why These Posts Were Created

The original request was to extract a blog post about Quest Engine from the ingenio repository, connecting it to genetic engineering/genetic algorithm metaphors and focusing on:
- Intrinsic motivation
- Contextual awareness
- Clear strategy

The work was split into three time-scale posts based on feedback that a single comprehensive post lacked day-to-day practicality. However, a subsequent request identified the need for an introduction post first, establishing Quest Engine as a methodology for agent-human collaboration before diving into time-scale specifics.

The time-scale posts remain valuable and should be published after the introduction provides the necessary foundation.
