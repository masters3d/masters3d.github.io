# Blog Post Backlog

Candidate posts mined from [masters3d/ingenio](https://github.com/masters3d/ingenio),
the author's notes and framework repository. Each row is an idea that has source
material in ingenio but no matching post in `zola-site/content/blog/` yet.

How to add rows and how to close them is described in
[agents.md, "Post Backlog: Finding and Closing Ideas"](./agents.md#post-backlog-finding-and-closing-ideas).

**Status values**: `open` (no post yet), `draft` (post file exists with
`draft = true`; not built or listed until the author reviews it and removes the
flag), `published` (post is live; slug in the Post column), `covered` (an existing post already makes the argument; extend it
instead of writing a new one), `dropped` (not worth a post; give the reason).

**Priority**: `P1` has a clear thesis and enough author-written source to draft
from now. `P2` needs more of the author's own view first. `P3` is thin or niche.

Most ingenio `specs/*/VISION.md` files are generated templates. The author's real
words are in the "Engineering Context" paragraph of the spec and in the
original GitHub issue body (all ingenio issues are closed but still readable).
Always read the issue, not only the spec.

## Release Schedule

Drafts go out two per month (the 1st and the 15th) in this order, which is
also the author's review order. Every draft keeps `draft = true` until the
author reviews it. `scripts/check_upcoming_drafts.py` fails PR validation and
deploy once a draft is within 7 days of its date, so each one must be published
or moved before its slot arrives. New drafts join the end of the queue.

| # | Date | ID | Title | Post |
| --- | --- | --- | --- | --- |
| 1 | 2027-01-01 | B26 | Ingenio: The Engine Inside Engineering | `ingenio-the-engine-inside-engineering` |
| 2 | 2027-01-15 | B03 | A Feature Needs a Life Cycle From Cradle to Grave | `feature-cradle-to-grave` |
| 3 | 2027-02-01 | B20 | PIE Theory: Being Seen Is Part of the Work | `pie-theory-being-seen-at-work` |
| 4 | 2027-02-15 | B21 | Locus of Control at Work | `locus-of-control-at-work` |
| 5 | 2027-03-01 | B22 | Seeking Is the Reward | `seeking-is-the-reward` |
| 6 | 2027-03-15 | B04 | Design Review Needs Governance | `design-review-needs-governance` |
| 7 | 2027-04-01 | B05 | The Sprintspective: One Loop for Looking Back and Planning Next | `sprintspective-one-loop` |
| 8 | 2027-04-15 | B06 | Open Guides Over Closed Answers | `open-guides-over-closed-answers` |
| 9 | 2027-05-01 | B08 | Promotion-Driven Development | `promotion-driven-development` |
| 10 | 2027-05-15 | B09 | Overlapping Roles in Tech | `overlapping-roles-in-tech` |
| 11 | 2027-06-01 | B10 | Types of Engineering Documentation | `types-of-engineering-documentation` |
| 12 | 2027-06-15 | B11 | The Kernel of Strategy | `kernel-of-strategy` |
| 13 | 2027-07-01 | B12 | Action, Feedback, Adjustment | `action-feedback-adjustment` |
| 14 | 2027-07-15 | B14 | Guiding Policies and Behavior Alignment | `guiding-policies-behavior-alignment` |
| 15 | 2027-08-01 | B23 | Story Is Engineering Memory | `story-is-engineering-memory` |
| 16 | 2027-08-15 | B24 | Build Mode, Reflect Mode, and Quality Without a Name | `build-mode-reflect-mode-quality-without-a-name` |
| 17 | 2027-09-01 | B25 | Philosophy, Manifesto, Principle, North Star | `philosophy-manifesto-principle-north-star` |
| 18 | 2027-09-15 | B30 | Dotnet Actor Systems and Testable Concurrency | `dotnet-actor-systems-and-testable-concurrency` |
| 19 | 2027-10-01 | B32 | Cognitive Continuous Integration and the Broken Agent Loop | `cognitive-continuous-integration-and-the-broken-agent-loop` |
| 20 | 2027-10-15 | B40 | Kaizen and the Observe, Orient, Decide, Act Return Loop | `kaizen-and-the-observe-orient-decide-act-return-loop` |
| 21 | 2027-11-01 | B41 | The Fractal Pattern Inside the Quest Engine | `the-fractal-pattern-inside-the-quest-engine` |
| 22 | 2027-11-15 | B42 | Anti-Patterns Show Where the Loop Broke | `anti-patterns-show-where-the-loop-broke` |
| 23 | 2027-12-01 | B50 | Career Quest Engineering, the 2021 Talk | `career-quest-engineering-2021-talk` |
| 24 | 2027-12-15 | B07 | Conversation Formats Are Engineering Tools | `conversation-formats-fishbowl` |
| 25 | 2028-01-01 | B13 | Remote Work Needs Context, Not Just Tools | `remote-work-needs-context-not-just-tools` |
| 26 | 2028-01-15 | B15 | People Systems and the Hiring Pipeline | `people-systems-and-the-hiring-pipeline` |
| 27 | 2028-02-01 | B27 | Resourcefulness, Agency, and Inheritance | `resourcefulness-agency-and-inheritance` |
| 28 | 2028-02-15 | B31 | Software 3.0 Needs Engineering, Not Magic | `software-3-0-needs-engineering-not-magic` |
| 29 | 2028-03-01 | B43 | Individual Contributor Levels as Changing Scope | `individual-contributor-levels-as-changing-scope` |

## Engineering Systems

| ID | Idea | Source in ingenio | Priority | Status | Post |
| --- | --- | --- | --- | --- | --- |
| B01 | Quality engineering vs engineering quality: quality, security, and documentation belong to the engineer, and rewards must follow behaviors | `specs/quality_engineering_qe_vs_engineering_quality/VISION.md`, issue #25 | P1 | published | `quality-engineering-vs-engineering-quality` |
| B02 | Development vs production: running a product at scale is different work, and production feedback must flow back as its own work stream | `specs/development_vs_production/VISION.md`, issue #21 (and its COGS vs OpEx comment) | P1 | published | `development-vs-production` |
| B03 | A feature's life cycle "cradle to the grave": how features are born, spread, and retired | `specs/feature_cradle_to_the_grave_life_cycle/VISION.md`, issue #18 | P1 | draft | `feature-cradle-to-grave` |
| B04 | Design review without governance is empty; working groups that approve features | `specs/design_governance/VISION.md` (#20), `specs/design_reviews_references/VISION.md` (#9) | P2 | draft | `design-review-needs-governance` |
| B05 | One loop for retrospective and planning (a "sprintspective") | `specs/define_the_act_pro-spective_and_retro-spective_in_the_same_flowfeedback_loop_maybe_sprintspective/VISION.md`, issue #17 | P2 | draft | `sprintspective-one-loop` |
| B06 | Open guides over closed answers: answer once on a wiki instead of in one email | `specs/behavior_general_open_guides_over_specify_closed_guides/VISION.md`, issue #7 | P2 | draft | `open-guides-over-closed-answers` |
| B07 | Conversation types for collaboration (fishbowl and other formats) | `specs/conversation_types_for_collaborations/VISION.md`, issue #16 | P3 | draft | `conversation-formats-fishbowl` |
| B08 | Promotion-driven development: how promotion incentives shape what gets built | `specs/promotion_driven_development_pdd/VISION.md`, issue #11 | P2 | draft | `promotion-driven-development` |
| B09 | Overlapping roles in tech and the risks where they intersect | `specs/roles_overlapping_in_tech_and_the_intersection_you_should_be_beware_of/VISION.md`, issue #14 | P2 | draft | `overlapping-roles-in-tech` |
| B10 | Kinds of documentation and which medium fits each (team-private vs engineering docs) | `presentation/eng_meta_documenation.md`, `presentation/eng_contextual_awareness.md` | P2 | draft | `types-of-engineering-documentation` |
| B11 | The kernel of strategy (Rumelt, *Good Strategy / Bad Strategy*) | `specs/from_good_strategy_bad_strategy/VISION.md` (#26), `media/synergies_strategy_kernel.drawio` | P2 | draft | `kernel-of-strategy` |
| B12 | Action, feedback, adjustment: slow and noisy feedback loops | `specs/action_feedback_adjustment/VISION.md`, `specs/action-feedback-adjustment/VISION.md`, issue #30 | P2 | draft | `action-feedback-adjustment` |
| B13 | Research on remote and async work (Microsoft New Future of Work) | `specs/async_workplace_public_research_from_microsoft/VISION.md`, issue #10 | P3 | draft | `remote-work-needs-context-not-just-tools` |
| B14 | Guiding policies that align individual behavior with organizational goals | `specs/behavior_alignment/VISION.md`, issue #29 | P2 | draft | `guiding-policies-behavior-alignment` |
| B15 | People systems and the hiring pipeline | `presentation/career_progression.md`, `presentation/career_init.md` | P3 | draft | `people-systems-and-the-hiring-pipeline` |

## Human Systems

| ID | Idea | Source in ingenio | Priority | Status | Post |
| --- | --- | --- | --- | --- | --- |
| B20 | PIE theory (Performance, Image, Exposure): being seen, not only doing the work | `specs/PIE_theory_integration/`, `specs/pie_theory_integration_to_quest_engine_framework/VISION.md` (#32), `career.md` "PIE Theory Integration" | P1 | draft | `pie-theory-being-seen-at-work` |
| B21 | Locus of control at work: control, influence, accept, and widening what you control (check overlap with `burnout-is-a-control-problem`) | `specs/locus_of_control/`, issue #47, `career.md` "Locus of Control in Engineering Excellence" | P1 | draft | `locus-of-control-at-work` |
| B22 | Seeking is the reward: building matters more than finishing | `specs/seeking_is_the_reward/VISION.md`, issue #23 | P1 | draft | `seeking-is-the-reward` |
| B23 | Story as how people store information; where story fits in engineering | `specs/where_does_story_fit_into_the_engineering_process_and_the_cognitive_storage_of_information_via_story_telling/VISION.md` (#34), `media/synergies_narrative.md` | P2 | draft | `story-is-engineering-memory` |
| B24 | Build mode vs reflect mode; judgement and "quality without a name" | `specs/cognitive_architecture_wrt_build_mode_and_reflect_mode/VISION.md`, issue #56 | P2 | draft | `build-mode-reflect-mode-quality-without-a-name` |
| B25 | Philosophy, manifesto, principle, north star: how they differ (drafted in Engineering Systems) | `specs/philosophy_manifesto_principle_northstar/VISION.md`, issue #19 | P2 | draft | `philosophy-manifesto-principle-north-star` |
| B26 | Ingenio: the engineering background and history of the word (ingenium, engine, engineer, sugar mill), plus ingenious vs ingenuous | `specs/ingenious_vs_ingenuous/VISION.md` (#13), `README.md` | P3 | draft | `ingenio-the-engine-inside-engineering` |
| B27 | Resourcefulness and agency as inherited vs learned traits | `specs/resourceful_agency_genetic_systems_relationships/VISION.md`, issue #38 (check overlap with `resourcefulness-is-its-own-quest-engine`) | P3 | draft | `resourcefulness-agency-and-inheritance` |

## Software Engineering

| ID | Idea | Source in ingenio | Priority | Status | Post |
| --- | --- | --- | --- | --- | --- |
| B30 | Actor systems in .NET (Coyote); pairs with the Swift actors vs Rust ownership post | `specs/dotnet_actor_system/VISION.md`, issue #15 | P2 | draft | `dotnet-actor-systems-and-testable-concurrency` |
| B31 | Software 3.0 as an engineering framework | `specs/software_3_0_engineering_framework/VISION.md` | P3 | draft | `software-3-0-needs-engineering-not-magic` |
| B32 | INGENIO-1 and "cognitive CI": an agent turning issues into specs, and what broke | `cognitive_systems/`, `experiments/`, `COGNITIVE_CI_*.md`, `RACE_CONDITION_FIX.md`, issues #36, #37, #42, #54 | P2 | draft | `cognitive-continuous-integration-and-the-broken-agent-loop` |

## Quest Engine (only if the post changes or defines the model)

| ID | Idea | Source in ingenio | Priority | Status | Post |
| --- | --- | --- | --- | --- | --- |
| B40 | Kaizen and the OODA loop (observe, orient, decide, act) as the roots of Systematic Improvement | `presentation/eng_systematic_improvement.md`, `pillars/systematic_improvement.md` | P2 | draft | `kaizen-and-the-observe-orient-decide-act-return-loop` |
| B41 | The fractal pattern: sub-pillars repeat the know, act, improve cycle | `pillars/FRAMEWORK_STRUCTURE.md`, `presentation/blog_quest_engine_intro.md` | P2 | draft | `the-fractal-pattern-inside-the-quest-engine` |
| B42 | Anti-patterns per pillar (information hoarding, stale docs, meeting culture, analysis paralysis, scope creep) | `pillars/contextual_awareness.md`, `pillars/clear_strategy.md`, `pillars/systematic_improvement.md` | P2 | draft | `anti-patterns-show-where-the-loop-broke` |
| B43 | Behaviors by individual contributor (IC) level 0 to 7+ (drafted in Engineering Systems) | `career.md` "People Systems Framework" | P3 | draft | `individual-contributor-levels-as-changing-scope` |

## Field Notes

| ID | Idea | Source in ingenio | Priority | Status | Post |
| --- | --- | --- | --- | --- | --- |
| B50 | Career Quest Engineering, the 2021 talk: video editor to project manager to software engineer | `presentation/career_quest_engineering.md`, `presentation/career_cheyo.md`, `presentation/presented/Career_Quest_Engineering_CheyoJimenez_2021_11.pptx`, `media/journey_cheyo.md` | P2 | draft | `career-quest-engineering-2021-talk` |

## Covered by Existing Posts

These ingenio topics already have a post. Extend the post rather than writing a
new one.

| Idea | Source in ingenio | Status | Post |
| --- | --- | --- | --- |
| Where does determination fit | issue #24 | covered | `determined-driven-consistent` |
| Engineering leverage, bicycle of the mind | issue #28 | covered | `leverage-and-the-stairs-you-build`, `bicycle-of-the-mind-fast-slow-agents` |
| High agency and bias toward action | issue #51 | covered | `quest-engine-building-high-agency-teams`, `fearless-engineering` |
| Personal lab notebook for running notes | issue #8 | covered | `why-i-love-worklogs`, `nine-years-of-copious-notes` |
| Story mapping whiteboard app | issue #12 | covered | `user-story-mapping-shared-understanding` |
| Mastery, autonomy, relatedness (self-determination theory) | `pillars/intrinsic_motivation.md` | covered | `find-your-why-intrinsic-motivation`, `search-mastery-drive-autonomy-renew-purpose` |
| Quest Engine introduction deck | `presentation/blog_quest_engine_intro.md` | covered | `quest-engine-introduction` |

## Dropped

| Idea | Source in ingenio | Reason |
| --- | --- | --- |
| Spec-generation and workflow fixes | issues #36, #37, #39, #42, #65 | Repository maintenance; folded into B32 if anywhere |
