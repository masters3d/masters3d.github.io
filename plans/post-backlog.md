# Blog Post Backlog

Candidate posts mined from [masters3d/ingenio](https://github.com/masters3d/ingenio),
the author's notes and framework repository. Each row is an idea that has source
material in ingenio but no matching post in `zola-site/content/blog/` yet.

How to add rows and how to close them is described in
[agents.md, "Post Backlog: Finding and Closing Ideas"](./agents.md#post-backlog-finding-and-closing-ideas).

**Status values**: `open` (no post yet), `draft` (post file exists with
`draft = true`; not built or listed until the author reviews it and removes the
flag), `scheduled` (reviewed; `draft = true` replaced with `scheduled = true`
under `[extra]`, and the daily deploy releases it on its date), `published` (post is live; slug in the Post column), `covered` (an existing post already makes the argument; extend it
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
deploy once a draft is within 7 days of its date, so each one must be published,
scheduled, or moved before its slot arrives. New drafts join the end of the queue.
To approve a post ahead of its slot, replace `draft = true` with
`scheduled = true` under `[extra]`: the daily deploy keeps it off the site until
its date, then releases it (`scripts/scheduled_posts.py`).
Cross-references follow the same order: inline links only point back to
posts that are already out, and forward references go in `[extra] related`,
which the template shows once both posts are published
(`scripts/check_post_links.py` enforces this).

| # | Date | ID | Title | Post |
| --- | --- | --- | --- | --- |
| 1 | 2026-11-01 | B26 | Ingenio: The Engine Inside Engineering | `ingenio-the-engine-inside-engineering` |
| 2 | 2026-11-15 | B03 | A Feature Needs a Life Cycle From Cradle to Grave | `feature-cradle-to-grave` |
| 3 | 2026-12-01 | B20 | PIE Theory: Being Seen Is Part of the Work | `pie-theory-being-seen-at-work` |
| 4 | 2026-12-15 | B21 | Locus of Control at Work | `locus-of-control-at-work` |
| 5 | 2027-01-01 | B22 | Seeking Is the Reward | `seeking-is-the-reward` |
| 6 | 2026-10-26 | B04 | Design Review Needs Governance | `design-review-needs-governance` |
| 7 | 2027-02-01 | B05 | The Sprintspective: One Loop for Looking Back and Planning Next | `sprintspective-one-loop` |
| 8 | 2027-02-15 | B06 | Open Guides Over Closed Answers | `open-guides-over-closed-answers` |
| 9 | 2027-03-01 | B08 | Promotion-Driven Development | `promotion-driven-development` |
| 10 | 2027-03-15 | B09 | Overlapping Roles in Tech | `overlapping-roles-in-tech` |
| 11 | 2027-04-01 | B10 | Types of Engineering Documentation | `types-of-engineering-documentation` |
| 12 | 2027-04-15 | B11 | The Kernel of Strategy | `kernel-of-strategy` |
| 13 | 2027-05-01 | B12 | Action, Feedback, Adjustment | `action-feedback-adjustment` |
| 14 | 2027-05-15 | B14 | Guiding Policies and Behavior Alignment | `guiding-policies-behavior-alignment` |
| 15 | 2027-06-01 | B23 | Story Is Engineering Memory | `story-is-engineering-memory` |
| 16 | 2027-06-15 | B24 | Build Mode, Reflect Mode, and Quality Without a Name | `build-mode-reflect-mode-quality-without-a-name` |
| 17 | 2027-07-01 | B25 | Philosophy, Manifesto, Principle, North Star | `philosophy-manifesto-principle-north-star` |
| 18 | 2027-07-15 | B30 | Dotnet Actor Systems and Testable Concurrency | `dotnet-actor-systems-and-testable-concurrency` |
| 19 | 2027-08-01 | B32 | Cognitive Continuous Integration and the Broken Agent Loop | `cognitive-continuous-integration-and-the-broken-agent-loop` |
| 20 | 2027-08-15 | B40 | Kaizen and the Observe, Orient, Decide, Act Return Loop | `kaizen-and-the-observe-orient-decide-act-return-loop` |
| 21 | 2027-09-01 | B41 | The Fractal Pattern Inside the Quest Engine | `the-fractal-pattern-inside-the-quest-engine` |
| 22 | 2027-09-15 | B42 | Anti-Patterns Show Where the Loop Broke | `anti-patterns-show-where-the-loop-broke` |
| 23 | 2027-10-01 | B50 | Career Quest Engineering, the 2021 Talk | `career-quest-engineering-2021-talk` |
| 24 | 2027-10-15 | B07 | Conversation Formats Are Engineering Tools | `conversation-formats-fishbowl` |
| 25 | 2027-11-01 | B13 | Remote Work Needs Context, Not Just Tools | `remote-work-needs-context-not-just-tools` |
| 26 | 2027-11-15 | B15 | People Systems and the Hiring Pipeline | `people-systems-and-the-hiring-pipeline` |
| 27 | 2027-12-01 | B27 | Resourcefulness, Agency, and Inheritance | `resourcefulness-agency-and-inheritance` |
| 28 | 2027-12-15 | B31 | Software 3.0 Needs Engineering, Not Magic | `software-3-0-needs-engineering-not-magic` |
| 29 | 2028-01-01 | B43 | Individual Contributor Levels as Changing Scope | `individual-contributor-levels-as-changing-scope` |
| 30 | 2028-01-15 | B60 | Proactive curiosity: seek context before it is handed to you (first sub-pillar of Contextual Awareness) | `proactive-curiosity` |
| 31 | 2028-02-01 | B72 | Career levels depend on context: startup, enterprise, product, platform, and culture | `career-levels-depend-on-context` |
| 32 | 2028-02-15 | B61 | Cohesive narrative: turning scattered facts into one story a team can act on | `cohesive-narrative` |
| 33 | 2028-03-01 | B82 | Five levels of agent capability: reactive to cognitive, and why systems engineering changes | `five-levels-of-agent-capability` |
| 34 | 2028-03-15 | B62 | Shared understanding as a practice with components, behaviors and checks | `shared-understanding-as-a-practice` |
| 35 | 2028-04-01 | B78 | The overjustification effect: when rewards crowd out the reason you did the work | `overjustification-effect-at-work` |
| 36 | 2028-04-15 | B63 | Challenge matching: fit the task to the skill so flow is possible | `challenge-matching-and-flow` |
| 37 | 2028-05-01 | B73 | Motivation, ability, narrative: three forces in a career and what happens when one is missing | `motivation-ability-narrative` |
| 38 | 2028-05-15 | B64 | Directed intentionality: choosing on purpose what not to do | `directed-intentionality` |
| 39 | 2028-06-01 | B83 | Agent memory in three tiers: short-term, long-term, and memory about learning | `agent-memory-short-long-and-meta` |
| 40 | 2028-06-15 | B65 | Adaptive control: steering a plan as feedback arrives | `adaptive-control` |
| 41 | 2028-07-01 | B75 | Level zero is an apprenticeship, a two-sided contract between the new engineer and the team | `level-zero-is-an-apprenticeship` |
| 42 | 2028-07-15 | B66 | Iterative integration: small changes merged often beat big batches | `iterative-integration` |
| 43 | 2028-08-01 | B79 | The regulation continuum: from external pressure to work that is yours | `the-regulation-continuum` |
| 44 | 2028-08-15 | B67 | Deliberate practice for engineers: targeted, feedback-rich repetition | `deliberate-practice-for-engineers` |
| 45 | 2028-09-01 | B84 | Meta-learning in four levels: learning about learning up to improving the improver | `meta-learning-four-levels` |
| 46 | 2028-09-15 | B68 | Update propagation: a lesson only counts once it reaches the docs, code and people | `update-propagation` |
| 47 | 2028-10-01 | B80 | The progress principle: small visible wins renew purpose | `the-progress-principle` |
| 48 | 2028-10-15 | B69 | Measuring the three pillars: discovery, strategy and improvement metrics | `measuring-the-three-pillars` |
| 49 | 2028-11-01 | B85 | Safe self-modification for agents: sandbox, validate, check goals, roll back | `safe-self-modification-for-agents` |
| 50 | 2028-11-15 | B70 | The objective function as the human-agent interface: reward signal, action space, value alignment | `objective-function-search-drive-renew` |
| 51 | 2028-12-01 | B74 | Juggling projects at different stages: one person, many projects, many people | `juggling-projects-at-different-stages` |
| 52 | 2028-12-15 | B71 | Anti-patterns in human-agent interaction and how to measure the interface | `anti-patterns-in-human-agent-interaction` |
| 53 | 2029-01-01 | B86 | Testing systems that change themselves: adaptive tests and emergent behavior | `testing-systems-that-change-themselves` |
| 54 | 2029-01-15 | B76 | Humans and agents on one team: who does what, and how roles shift | `humans-and-agents-on-one-team` |
| 55 | 2029-02-01 | B81 | Growth mindset as the base of mastery, by IC level | `growth-mindset-and-mastery` |
| 56 | 2029-02-15 | B87 | Hypothesis-driven agent experiments: predictions, logs, and risks like confirmation bias | `hypothesis-driven-agent-experiments` |
| 57 | 2029-03-01 | B77 | Career success metrics, individual and organizational, and growth strategies | `career-success-metrics-individual-and-organizational` |
| 58 | 2029-03-15 | B88 | Measuring an agent beyond task completion | `measuring-an-agent-beyond-task-completion` |

## Engineering Systems

| ID | Idea | Source in ingenio | Priority | Status | Post |
| --- | --- | --- | --- | --- | --- |
| B01 | Quality engineering vs engineering quality: quality, security, and documentation belong to the engineer, and rewards must follow behaviors | `specs/quality_engineering_qe_vs_engineering_quality/VISION.md`, issue #25 | P1 | published | `quality-engineering-vs-engineering-quality` |
| B02 | Development vs production: running a product at scale is different work, and production feedback must flow back as its own work stream | `specs/development_vs_production/VISION.md`, issue #21 (and its COGS vs OpEx comment) | P1 | published | `development-vs-production` |
| B03 | A feature's life cycle "cradle to the grave": how features are born, spread, and retired | `specs/feature_cradle_to_the_grave_life_cycle/VISION.md`, issue #18 | P1 | scheduled | `feature-cradle-to-grave` |
| B04 | Design review without governance is empty; working groups that approve features | `specs/design_governance/VISION.md` (#20), `specs/design_reviews_references/VISION.md` (#9) | P2 | scheduled | `design-review-needs-governance` |
| B05 | One loop for retrospective and planning (a "sprintspective") | `specs/define_the_act_pro-spective_and_retro-spective_in_the_same_flowfeedback_loop_maybe_sprintspective/VISION.md`, issue #17 | P2 | scheduled | `sprintspective-one-loop` |
| B06 | Open guides over closed answers: answer once on a wiki instead of in one email | `specs/behavior_general_open_guides_over_specify_closed_guides/VISION.md`, issue #7 | P2 | scheduled | `open-guides-over-closed-answers` |
| B07 | Conversation types for collaboration (fishbowl and other formats) | `specs/conversation_types_for_collaborations/VISION.md`, issue #16 | P3 | draft | `conversation-formats-fishbowl` |
| B08 | Promotion-driven development: how promotion incentives shape what gets built | `specs/promotion_driven_development_pdd/VISION.md`, issue #11 | P2 | scheduled | `promotion-driven-development` |
| B09 | Overlapping roles in tech and the risks where they intersect | `specs/roles_overlapping_in_tech_and_the_intersection_you_should_be_beware_of/VISION.md`, issue #14 | P2 | scheduled | `overlapping-roles-in-tech` |
| B10 | Kinds of documentation and which medium fits each (team-private vs engineering docs) | `presentation/eng_meta_documenation.md`, `presentation/eng_contextual_awareness.md` | P2 | scheduled | `types-of-engineering-documentation` |
| B11 | The kernel of strategy (Rumelt, *Good Strategy / Bad Strategy*) | `specs/from_good_strategy_bad_strategy/VISION.md` (#26), `media/synergies_strategy_kernel.drawio` | P2 | scheduled | `kernel-of-strategy` |
| B12 | Action, feedback, adjustment: slow and noisy feedback loops | `specs/action_feedback_adjustment/VISION.md`, `specs/action-feedback-adjustment/VISION.md`, issue #30 | P2 | scheduled | `action-feedback-adjustment` |
| B13 | Research on remote and async work (Microsoft New Future of Work) | `specs/async_workplace_public_research_from_microsoft/VISION.md`, issue #10 | P3 | draft | `remote-work-needs-context-not-just-tools` |
| B14 | Guiding policies that align individual behavior with organizational goals | `specs/behavior_alignment/VISION.md`, issue #29 | P2 | draft | `guiding-policies-behavior-alignment` |
| B15 | People systems and the hiring pipeline | `presentation/career_progression.md`, `presentation/career_init.md` | P3 | draft | `people-systems-and-the-hiring-pipeline` |

## Human Systems

| ID | Idea | Source in ingenio | Priority | Status | Post |
| --- | --- | --- | --- | --- | --- |
| B20 | PIE theory (Performance, Image, Exposure): being seen, not only doing the work | `specs/PIE_theory_integration/`, `specs/pie_theory_integration_to_quest_engine_framework/VISION.md` (#32), `career.md` "PIE Theory Integration" | P1 | scheduled | `pie-theory-being-seen-at-work` |
| B21 | Locus of control at work: control, influence, accept, and widening what you control (check overlap with `burnout-is-a-control-problem`) | `specs/locus_of_control/`, issue #47, `career.md` "Locus of Control in Engineering Excellence" | P1 | scheduled | `locus-of-control-at-work` |
| B22 | Seeking is the reward: building matters more than finishing | `specs/seeking_is_the_reward/VISION.md`, issue #23 | P1 | scheduled | `seeking-is-the-reward` |
| B23 | Story as how people store information; where story fits in engineering | `specs/where_does_story_fit_into_the_engineering_process_and_the_cognitive_storage_of_information_via_story_telling/VISION.md` (#34), `media/synergies_narrative.md` | P2 | draft | `story-is-engineering-memory` |
| B24 | Build mode vs reflect mode; judgement and "quality without a name" | `specs/cognitive_architecture_wrt_build_mode_and_reflect_mode/VISION.md`, issue #56 | P2 | draft | `build-mode-reflect-mode-quality-without-a-name` |
| B25 | Philosophy, manifesto, principle, north star: how they differ (drafted in Engineering Systems) | `specs/philosophy_manifesto_principle_northstar/VISION.md`, issue #19 | P2 | draft | `philosophy-manifesto-principle-north-star` |
| B26 | Ingenio: the engineering background and history of the word (ingenium, engine, engineer, sugar mill), plus ingenious vs ingenuous | `specs/ingenious_vs_ingenuous/VISION.md` (#13), `README.md` | P3 | scheduled | `ingenio-the-engine-inside-engineering` |
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

## Second Pass (October 2026)

A full read of ingenio's `career.md`, `pillars/`, `presentation/`,
`cognitive_systems/`, and `experiments/` for ideas the first pass missed. Most
of `cognitive_systems/` was written by the INGENIO-1 agent as a design
proposal, so posts drawn from it present those designs as proposals, not as
results.

| ID | Idea | Source in ingenio | Track | Priority | Status | Post |
| --- | --- | --- | --- | --- | --- | --- |
| B60 | Proactive curiosity: seek context before it is handed to you (first sub-pillar of Contextual Awareness) | `pillars/contextual_awareness.md` "1. Proactive Curiosity", `presentation/eng_contextual_awareness.md` | Quest Engine | P2 | draft | `proactive-curiosity` |
| B61 | Cohesive narrative: turning scattered facts into one story a team can act on | `pillars/contextual_awareness.md` "2. Cohesive Narrative" | Quest Engine | P2 | draft | `cohesive-narrative` |
| B62 | Shared understanding as a practice with components, behaviors and checks | `pillars/contextual_awareness.md` "3. Shared Understanding" | Quest Engine | P2 | draft | `shared-understanding-as-a-practice` |
| B63 | Challenge matching: fit the task to the skill so flow is possible | `pillars/clear_strategy.md` "1. Challenge Matching", `pillars/intrinsic_motivation.md` "Flow State Connection" | Quest Engine | P2 | draft | `challenge-matching-and-flow` |
| B64 | Directed intentionality: choosing on purpose what not to do | `pillars/clear_strategy.md` "2. Directed Intentionality" | Quest Engine | P2 | draft | `directed-intentionality` |
| B65 | Adaptive control: steering a plan as feedback arrives | `pillars/clear_strategy.md` "3. Adaptive Control" | Quest Engine | P2 | draft | `adaptive-control` |
| B66 | Iterative integration: small changes merged often beat big batches | `pillars/systematic_improvement.md` "1. Iterative Integration" | Quest Engine | P2 | draft | `iterative-integration` |
| B67 | Deliberate practice for engineers: targeted, feedback-rich repetition | `pillars/systematic_improvement.md` "2. Deliberate Practice" | Quest Engine | P2 | draft | `deliberate-practice-for-engineers` |
| B68 | Update propagation: a lesson only counts once it reaches the docs, code and people | `pillars/systematic_improvement.md` "3. Update Propagation" | Quest Engine | P2 | draft | `update-propagation` |
| B69 | Measuring the three pillars: discovery, strategy and improvement metrics | "Measuring ..." sections of `pillars/contextual_awareness.md`, `pillars/clear_strategy.md`, `pillars/systematic_improvement.md` | Quest Engine | P2 | draft | `measuring-the-three-pillars` |
| B70 | The objective function as the human-agent interface: reward signal, action space, value alignment | `pillars/objective_function.md`, `presentation/eng_objective_function.md` | Quest Engine | P2 | draft | `objective-function-search-drive-renew` |
| B71 | Anti-patterns in human-agent interaction and how to measure the interface | `pillars/objective_function.md` "Anti-Patterns in Human-Agent Interaction", "Measuring the Interface" | Software Engineering | P2 | draft | `anti-patterns-in-human-agent-interaction` |
| B72 | Career levels depend on context: startup, enterprise, product, platform, and culture | `career.md` "Contextual Considerations", "Future Evolution" | Engineering Systems | P2 | draft | `career-levels-depend-on-context` |
| B73 | Motivation, ability, narrative: three forces in a career and what happens when one is missing | `presentation/career_cheyo.md`, `media/synergies_narrative.md` | Human Systems | P2 | draft | `motivation-ability-narrative` |
| B74 | Juggling projects at different stages: one person, many projects, many people | `presentation/career_behaviors.md`, `media/temporal_group_*.drawio` | Human Systems | P2 | draft | `juggling-projects-at-different-stages` |
| B75 | Level zero is an apprenticeship, a two-sided contract between the new engineer and the team | `career.md` "Level 0: Apprentice" | Engineering Systems | P2 | draft | `level-zero-is-an-apprenticeship` |
| B76 | Humans and agents on one team: who does what, and how roles shift | `specs/human_cognitive_career_alignment/VISION.md`, `cognitive_systems/COGNITIVE_ENGINEERING_INTEGRATION.md` | Engineering Systems | P2 | draft | `humans-and-agents-on-one-team` |
| B77 | Career success metrics, individual and organizational, and growth strategies | `career.md` "Career Development Principles" | Engineering Systems | P2 | draft | `career-success-metrics-individual-and-organizational` |
| B78 | The overjustification effect: when rewards crowd out the reason you did the work | `pillars/intrinsic_motivation.md` "Intrinsic vs Extrinsic Motivation" | Human Systems | P2 | draft | `overjustification-effect-at-work` |
| B79 | The regulation continuum: from external pressure to work that is yours | `pillars/intrinsic_motivation.md` "The Regulation Continuum" | Human Systems | P2 | draft | `the-regulation-continuum` |
| B80 | The progress principle: small visible wins renew purpose | `pillars/intrinsic_motivation.md` "Sub-Pillar 3: Purpose", "Progress Principle" | Human Systems | P2 | draft | `the-progress-principle` |
| B81 | Growth mindset as the base of mastery, by IC level | `pillars/intrinsic_motivation.md` "Sub-Pillar 1: Mastery" | Human Systems | P2 | draft | `growth-mindset-and-mastery` |
| B82 | Five levels of agent capability: reactive to cognitive, and why systems engineering changes | `cognitive_systems/README.md`, `cognitive_systems/agents/AGENT_TEMPLATE.md`, `specs/cognitive_systems_engineering/VISION.md` | Software Engineering | P2 | draft | `five-levels-of-agent-capability` |
| B83 | Agent memory in three tiers: short-term, long-term, and memory about learning | `cognitive_systems/agents/cognitive/INGENIO-1.md` | Software Engineering | P2 | draft | `agent-memory-short-long-and-meta` |
| B84 | Meta-learning in four levels: learning about learning up to improving the improver | `cognitive_systems/meta_systems/META_LEARNING.md`, `specs/meta_cognitive_development/VISION.md` | Software Engineering | P2 | draft | `meta-learning-four-levels` |
| B85 | Safe self-modification for agents: sandbox, validate, check goals, roll back | `cognitive_systems/meta_systems/META_LEARNING.md`, `specs/cognitive_systems_engineering/VISION.md` | Software Engineering | P2 | draft | `safe-self-modification-for-agents` |
| B86 | Testing systems that change themselves: adaptive tests and emergent behavior | `cognitive_systems/COGNITIVE_ENGINEERING_INTEGRATION.md` | Software Engineering | P2 | draft | `testing-systems-that-change-themselves` |
| B87 | Hypothesis-driven agent experiments: predictions, logs, and risks like confirmation bias | `experiments/2024-12-19_pie_theory_cognitive_development/`, `cognitive_systems/experiments/EXPERIMENTATION_FRAMEWORK.md` | Software Engineering | P2 | draft | `hypothesis-driven-agent-experiments` |
| B88 | Measuring an agent beyond task completion | `AGENTS.md` agent metrics, `cognitive_systems/agents/cognitive/INGENIO-1.md` | Software Engineering | P2 | draft | `measuring-an-agent-beyond-task-completion` |

## Unscheduled Ideas (Author's Own)

Ideas the author has not acted on yet. Each has a draft so the thinking is
written down, but it stays out of the Release Schedule until the author has
practiced it for a few weeks and the post can report what happened (see
"Publish what was done, not what is planned" in `plans/agents.md`). The draft
date is a placeholder far enough out to keep the draft gate quiet.

| ID | Idea | Source | Track | Status | Post |
| --- | --- | --- | --- | --- | --- |
| U01 | Wacky health ideas: a plank desk for working horizontally and the resting squat, building on the six-month move to standing in `monitor-the-body-running-the-work` | Author's notes, October 2026 | Human Systems | draft (unscheduled, placeholder date 2028-12-31) | `wacky-health-ideas-plank-desk-and-resting-squat` |

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
