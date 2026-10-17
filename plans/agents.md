# Agent Consistency Guidelines

**Purpose**: Ensure consistent decision-making and approaches across multiple agent sessions for the masters3d.github.io migration project.

## Core Decisions & Principles

### 1. Technology Stack
**DECIDED**: Zola (Rust-based static site generator)
- **Rationale**: User prefers non-Ruby solution, wants simplicity, mentioned Rust interest
- **Alternative considered**: Hugo (Go), Publish (Swift)
- **Do NOT change** unless user explicitly requests reconsideration

### 2. Migration Approach
**DECIDED**: Incremental migration with preservation
- **Preserve**: All existing content, custom domain, external links
- **Enhance**: Add blog functionality, improve responsive design
- **Maintain**: Same URL structure, Google Analytics

### 3. Deployment Strategy
**DECIDED**: GitHub Actions → GitHub Pages artifact
- **Rationale**: GitHub Pages doesn't natively support Zola
- **How**: `.github/workflows/static.yml` runs `zola build` on push to `master` and publishes
  `zola-site/public` via `upload-pages-artifact` + `deploy-pages`. There is **no `gh-pages`
  branch** — the built output is never committed, so you cannot inspect the live site by
  reading a branch.
- **Preserve**: masters3d.com custom domain via CNAME
- **Rollback**: Keep original files in legacy/ folder

### 4. File Management
**DECIDED**: Minimal changes, surgical approach
- **Create**: New Zola structure alongside existing
- **Preserve**: Original index.html, stylesheets, images
- **Document**: All changes in plans/ folder

### 5. Pull Request Target Branch
**DECIDED**: Always open pull requests against `master`
- **Rule**: Every PR must target the `master` branch as its base, unless the user explicitly asks for a different base
- **Rationale**: `master` is the default branch and the single source of truth; PRs accidentally based on another working branch (e.g. another `copilot/*` branch) do not reach `master` when merged
- **Before creating a PR**: verify the base branch is `master`; if a PR was opened against the wrong base, retarget it to `master`

### 6. Markdown Formatting (Prettier + markdownlint)
**DECIDED**: Blog Markdown is formatted with Prettier and linted with markdownlint; `scripts/format_markdown.py` is a thin wrapper that just calls these two tools
- **Rationale**: One-line-per-paragraph posts produce whole-paragraph diffs; Prettier wraps prose to 80 columns for small, reviewable line-level diffs, and markdownlint catches structural issues. Using standard tools (instead of a bespoke script) is portable and well understood
- **Guarantee**: Prettier is configured with `proseWrap: always` (soft breaks render as spaces) and `embeddedLanguageFormatting: off` (fenced sample code is untouched), so the generated HTML is byte-identical before and after formatting
- **Rule for agents (REQUIRED)**: ALWAYS run the formatter before committing. After creating or editing any Markdown, run `npm install` (once) then `python3 scripts/format_markdown.py`, and verify with `python3 scripts/format_markdown.py --check` (must exit clean). Never commit Markdown that has not been through the formatter
- **Enforced**: The PR Validation workflow runs `npm ci` + `python3 scripts/format_markdown.py --check`; incorrectly formatted or lint-failing Markdown fails CI
- **Config**: `.prettierrc.json`, `.markdownlint-cli2.jsonc`, and pinned versions in `package.json`
- **Do NOT** hand-wrap or hand-reflow paragraphs; always let Prettier do it so the result is deterministic and idempotent

## Session Consistency Rules

### When Starting New Sessions
1. **Always check** `plans/progress-tracking.md` first
2. **Review** previous decisions in this file
3. **Read** `plans/session-context.md` for immediate context
4. **Check** `plans/current-task.md` for active work
5. **Update** progress tracking with new session info
6. **Continue** from last recorded progress point

### When Copilot/Agent Restarts or Has Issues
1. **CRITICAL**: Read `plans/session-context.md` FIRST - contains immediate context
2. **Check branch status**: `git branch` and `git status` 
3. **Review recent commits**: `git log --oneline -5`
4. **Read current task**: `plans/current-task.md` for active objectives
5. **Check enhancement roadmap**: `plans/enhancement-roadmap.md` for comprehensive plan
6. **Verify local environment**: Check if Zola server running, test site accessibility
7. **Update session info**: Add new session entry to `plans/session-context.md`

### Session Context Preservation Protocol
**MANDATORY**: Every session must maintain detailed context in `plans/session-context.md`

#### Required Context Elements:
- **Current branch and status**
- **Last completed actions**
- **Active tasks and next steps**
- **Local development state** (server running, port, URLs)
- **Known issues and blockers**
- **Recent discoveries or important notes**
- **Handoff instructions for next session**

#### Context Update Frequency:
- **Start of session**: Read and update with new session info
- **Major milestone**: Document progress and state changes
- **End of session**: Complete handoff notes and next steps
- **Before any extended break**: Ensure context is current and detailed

### Decision Making
- **Never contradict** previously documented decisions without user input
- **Always document** new decisions in this file
- **Reference** this file when user asks "what did we decide before?"
- **Check session-context.md** for recent context and state

### Code Changes
- **Minimal modifications** - change as few lines as possible
- **Preserve working code** - don't delete unless absolutely necessary
- **Test incrementally** - build and test after each major change
- **Document changes** - update progress tracking

### Writing Style Preferences
- **Parentheses over em-dashes** - Use parentheses () instead of em-dashes (—) for parenthetical expressions
  - Example: "text (clarification)" instead of "text—clarification"
  - Maintains readability and follows user's preferred style
- **Bullet lists** - Use hyphens (-) for bullet lists (standard markdown format)
- **Avoid overloaded words** - Don't use "impact" (too overloaded). Use specific alternatives:
  - Instead of "user impact" → "user value" or "user outcomes"
  - Instead of "impact on the team" → "effect on the team" or "benefit to the team"
  - Instead of "business impact" → "business value" or "business results"
- **Words to avoid** - Do not use these words in blog posts; prefer more precise, respectful alternatives:
  - "stupid" - avoid entirely (dismissive and imprecise). Use "misguided", "flawed", "ill-suited", "not optimal", or name the specific problem instead
  - "impact" - see "Avoid overloaded words" above
  - When adding new posts or editing existing ones, survey the text for these words and remove them where they are not needed
- **Phrases to avoid** - Do not use the costume metaphor for "two things are really the same thing": "wearing a costume", "wearing different clothes", "in disguise", "by another name", "dressed up as". It reads as a stock figure of speech rather than an explanation, and it hides the thing worth stating. Name the actual relationship instead: what converts into what, at what exchange rate, or which property the two share. "Distance and delay are one constraint measured in two units" says something; "distance is delay wearing a costume" does not
- **Minimize section breaks for narrative flow** - Avoid excessive section headings that break narrative flow
  - Write blog posts as cohesive stories rather than overly segmented documentation
  - Minimize h2 (##) section headings - use only for major inflection points (aim for 3-4 max in a blog post)
  - Avoid subsection headings (###) entirely in blog posts - they fragment the narrative
  - Integrate related content into flowing paragraphs instead of creating separate sections
  - Let content flow naturally without artificial breaks
  - Goal: Improve readability and maintain storytelling quality
  - Example: A blog post should have 3 major sections marking key turning points, not 10+ sections for every topic

### Voice Guidance: Common Authorial Voice

**DECIDED**: The author writes as a curious practitioner making sense of something
he has lived, built, watched, or changed his mind about. The voice is personal
without becoming confessional, technically precise without becoming academic,
and opinionated without claiming more certainty than the evidence supports.
Specific experience earns the abstraction: the writing starts close to an
object, moment, failure, or reaction, follows the friction honestly, and only
then names the larger pattern.

Preserve the historical wording of old posts rather than rebuilding them around
newer conventions. Correct factual errors, broken links, and clear typos in place.
When later knowledge changes the interpretation, prefer a dated editor's note or
a linked retrospective over silently making the old prediction sound wiser.

- **Begin with something noticed or lived** - Open on a moment, object, problem,
  or reaction that actually prompted the idea. Do not begin with an abstract
  summary of what the post will cover.
- **Choose an opening that fits the evidence** - Valid openings include a physical
  moment ("I picked up my iPad"), a reaction to news ("Swift was released last
  week"), a statement of personal position ("I am a nontraditional software
  developer"), or a retrospective observation ("Looking back across a decade").
  The requirement is concrete footing, not a repeated "I noticed" formula.
- **Use first person when it carries evidence** - "I remember," "I noticed," and
  "I think" should introduce direct experience or honest judgment, not decorate a
  generic explanation.
- **Keep specific details** - Names, dates, prices, tools, failed attempts, and
  surprising preferences make the voice recognizable. Do not sand those details
  into generic professional prose.
- **Keep friction and limits in the story** - The author regularly admits what did
  not click, what felt intimidating, what could not be made to work, and what a
  purchase failed to replace. These are evidence for the conclusion, not
  weaknesses to edit away.
- **Move from concrete to abstract** - Tell the story or show the example first,
  then extract the principle, then explain where else it applies.
- **Be opinionated without pretending certainty** - State conclusions directly,
  and clearly label predictions, incomplete evidence, or changes of mind.
- **Prefer conversational precision** - Use short declarative sentences,
  occasional questions, and natural transitions. Avoid corporate language,
  inflated claims, generic enthusiasm, and tutorial voice unless the post is
  actually a tutorial.
- **Keep the author's energy** - Curiosity, delight, frustration, and surprise
  are part of the voice. Edit for clarity without making every post sound
  detached or academically uniform.
- **Vary the rhetorical surface** - Shared voice does not require shared
  wording. Before publishing, compare openings, transitions, section names, and
  closings with recent posts. Phrases such as "I keep coming back to," "the key
  insight," "the pattern is clear," "this is also why," and "the same instinct"
  are useful once but become house-style filler when repeated across the
  corpus. Name the actual relationship instead: something may have stayed with
  the author, recurred in several examples, survived testing, connected two
  ideas, or changed the conclusion. Do not mechanically rotate synonyms; make
  the sentence say which of those things happened. Also check for substantial
  overlap in the argument itself: revise or extend the existing post instead of
  publishing a second post that differs mainly in title or framing.
- **End with earned reflection** - Return to the opening observation, say what
  changed in the author's understanding, connect to related posts where useful,
  and state why the idea matters.

**Review test**: After a resolved narrative, a reader should be able to answer
four questions: What did the author notice? What specific experience supports it?
What principle did the author extract? Why does it matter now? A Field Note may
replace the extracted principle with an honest open question, but the reader
should still understand why preserving that question matters.

### Voice Guidance: Contemporary Techniques

Use these techniques when the subject needs them. They extend the common voice
without turning it into generic technical documentation:

- **Treat AI agents as tools in the lived environment** - When agent collaboration
  is part of the work, describe it as ordinary practice with concrete settings,
  constraints, failures, and results. Keep the authorial perspective singular.
  The agent does not become a "we," and tool output does not replace the author's
  judgment.
- **Use structure to clarify mechanisms** - Engineering and framework posts may
  use compact tables, matrices, or lists for genuine comparisons. Introduce the
  reason for the structure in prose and interpret what it shows afterward.
- **Let headings name conceptual movement** - A newer post may move by problem,
  mechanism, application, and consequence rather than by chronology. Headings
  should mark those real turns instead of merely labeling topics.
- **Link ideas where they do work** - Cross-links may appear inside the argument,
  not only in the closing reflection. Use them to supply a prerequisite, extend a
  claim, or show a change of mind (not as promotional decoration).
- **State the boundary of current evidence** - Newer experiment logs often close
  with what remains uncertain or what evidence could change the conclusion. This
  is the contemporary form of being opinionated without pretending certainty.
- **Use visual accents rarely** - Emoji may reinforce a specific metaphor or
  moment, but should not decorate headings or substitute for precise language.

### Editorial Tracks: Stable Voices by Post Type

**DECIDED**: Every blog post belongs to exactly one editorial track. The common
authorial voice remains the baseline, while the track determines the post's
emphasis, evidence, and pacing. Tags connect related ideas across tracks; they do
not replace the primary track.

#### Placing a Post in a Track

**Not everything that says Quest Engine goes into Quest Engine.** Most posts
on this blog use Search, Drive, and Renew somewhere. That vocabulary is a lens
the author applies everywhere; it is not evidence of the track. The Quest
Engine track grew to 30 posts once because framework mentions were treated as
membership, and it was cut back to the ~10 posts that actually build the model.

Decide the track from what the post is really about, not from the vocabulary
it uses. Ask the questions in this order and stop at the first yes. A later
track only gets the post when every earlier track has said no.

1. **Does it have to do with computer languages or creating software?**
   Languages (design, safety, concurrency, runtimes, adoption, ecosystems),
   code, architecture, verification, tooling, agent workflows for building
   software, learning to program, and a career or expertise built in software.
   → **Software Engineering**. This wins even when the post is dated (a
   launch-week language prediction, a projects portfolio), personal (an origin
   story, why a language never made it to work), or told through a cognitive
   model or the Quest Engine.
2. **Is it a general engineering practice that is not only about software?**
   Risk and blast radius, scaffolding and iteration, process improvement,
   ownership, incidents, blamelessness, incentives and rewards, team identity,
   context flow, work personalities, the words engineers use. The practice
   would hold for any engineering discipline or team. → **Engineering
   Systems**.
3. **Is it about humans rather than engineering?** One person as a system:
   cognitive (attention, habit, creativity, motivation, meaning, spirituality,
   a familiar phrase or triad tested as a pattern of how people keep going),
   physical (the body, energy, movement, rest), or health (sleep, stress,
   burnout, recovery). → **Human Systems**.
4. **Is the framework itself the subject?** The post defines a part of the
   model, connects parts, or extends it (a new layer, a corrected mapping, the
   structure of the loop). If you deleted every non-framework example, the
   argument would still stand. → **Quest Engine**. The model is largely
   settled, so this track grows only when a post builds a new version of it
   or questions it deeply enough (human factors, systems thinking, cognitive
   framing) that the model itself changes. Using Search, Drive, and Renew as a
   lens is not enough, and a model-defining post does not move to Software
   Engineering just because the model applies to agents.
5. **Nothing above fits?** A dated personal record: a device, a year, a
   hardware prediction, a media portfolio, a show review, a history where the
   chronology matters more than the lesson. → **Field Notes**. This is the
   fallback, not a first choice.

   **Where the lines fall:** a post that only works for software is Software
   Engineering; the same idea stated for any engineering team is Engineering
   Systems; the person behind the work, outside any engineering practice, is
   Human Systems. Burnout is Human Systems even when work caused it; on-call
   rotations that cause burnout are Engineering Systems.

**When a post is about more than one thing.** The order above applies to the
post's main subject, not to every subject it touches. A software example, an
agent workflow in one section, or a closing paragraph about engineering does
not make the post Software Engineering. Most posts here mix a person, a
practice, and some code, so find the main subject first:

1. **Thesis test** - Write the post's claim in one sentence from its title,
   description, and closing paragraph. The track is whatever that sentence is
   about. "Expertise comes from new constraints, not hours" is about a person
   learning, even when the evidence is a software career.
2. **Domain swap test** - Replace the software examples with examples from
   another field (video editing, sports, cooking, a different kind of
   engineering). If the claim still holds, software is the setting, not the
   subject: go to Engineering Systems if it is a practice, Human Systems if it
   is about a person. If the claim falls apart, it is Software Engineering.
3. **Weight test** - If the thesis is still split, count where the body goes.
   The subject that holds most of the sections wins; one section on agents
   in a post about attention does not move it.
4. **Tie-break** - If two subjects are truly even, prefer the broader one
   (Human Systems over Engineering Systems over Software Engineering), so a
   post reaches the readers its idea applies to. Software Engineering keeps
   posts that are specifically about languages, code, or building software.

Quick tests:

- **Swap test** - Replace "Quest Engine" with a generic phrase like "this
  model". If the post still makes its point, the framework is the lens, not the
  subject.
- **Title test** - A title that pairs the framework with something else
  ("Agents Are Taking the Drive", "Faith. Guts. Stamina.", "Independent Fire")
  usually belongs to the something else.
- **Tag and series are not the track** - `series = "quest-engine"` and the
  `quest-engine` tag put a post in the reading order. Use them freely on any
  track; the reading order spans all five tracks.

Examples of the current split:

| Post | Track | Why not Quest Engine |
| --- | --- | --- |
| The Meta Structure, The Primary Directive, The Contextual Core | Quest Engine | (These define the model.) |
| Agents Are Taking the Drive; Goal, Effort, Verification | Software Engineering | Subject is agent-driven engineering work |
| Independent Fire; World Cup 2026 | Engineering Systems | Subject is how teams distribute authority |
| Faith. Guts. Stamina.; Secular Meaning of Life; Running the Health Quest | Human Systems | Subject is motivation (cognitive), meaning (cognitive), or the body (physical, health) |
| Burnout Is a Control Problem | Human Systems | Subject is one person's health and recovery, told with history |
| The Media Consumption Arc | Human Systems | Subject is how media competes for one person's attention across life stages |
| The Bicycle of the Mind; 10,000 Hours Was Never Enough; The MOOC Era | Human Systems | Mixed posts whose thesis is how a person builds automaticity, expertise, or learning; software is the evidence and the claim survives the domain swap |
| Craftsmanship, Judgment, and Taste; There Is No Speedup for Shared Understanding; Ten Years in Software Engineering | Software Engineering | Subject is what the human brings to building software with agents, validating generated code, or a software career |
| Joy, Freedom, Motivation: Matz's Triad | Human Systems | Mixed post; it closes by saying the triad "is not a Ruby feature," so the thesis is motivation, with a language as the setting |
| My Swift Journey; What Apple Swift Means to Apple; From Creative Tools to Software Engineering; Longest Path into Data Structures and Algorithms; Technical Projects Portfolio | Software Engineering | Subject is a language or creating software, so it skips Field Notes even though it is dated and personal |
| Fearless Engineering; Leverage and the Stairs You Build; Director and Thinker | Engineering Systems | Subject is a general engineering practice (risk, scaffolding, work personalities), not only software |
| The Last 20% and the Next Nine; From Manual to Self-Sustaining | Engineering Systems | Subject is how organizations reward work and build shared understanding of a process |
| The Background Brain | Human Systems | Subject is how one mind does creative work, outside any engineering practice |

**Track order mirrors the framework.** Templates list tracks in this fixed order,
not alphabetically: Quest Engine (the Why), Field Notes (the four Ws: who, what,
when, where), Software Engineering (Search: mastery), Engineering Systems (Drive:
autonomy), Human Systems (Renew: purpose). The mapping holds for each track as
a whole, not for every post in it, and it is not a placement rule. Place by
subject using the steps above. Keep the order list in
`templates/partials/editorial-tracks.html` and `templates/taxonomies/single.html`
in sync when adding a track.

#### Quest Engine (`quest-engine`)

Write as a framework builder finding the same underlying shape in lived
experience, stories, psychology, engineering, and history. The tone is
diagnostic rather than inspirational: give readers language for recognizing
where they are, not slogans about where they should be.

This track is reserved for posts whose main contribution is the model itself:
defining a part, connecting parts, or extending the framework. A post that uses
the framework as a lens on something else belongs to that subject's track
(Software Engineering for languages, building software, and agents;
Engineering Systems for general engineering practice and teams; Human Systems
for the person: cognitive, physical, and health) and joins the reading order through
`extra.series = "quest-engine"` and the `quest-engine` tag instead.

- **Opening and movement** - Begin with a concrete experience, cultural scene, or
  stubborn question. Extract the structural pattern, define it, test it against
  other domains, and return to what the pattern helps a person see or choose.
- **Evidence** - Build confidence through convergence. Pair personal experience
  with two or more independent frames when useful, but do not treat a familiar
  story or named theory as proof by itself. Each additional frame must test or
  sharpen a distinction rather than repeat the same mapping in new nouns.
- **Inherited phrases and triads** - When a familiar sequence supplies the
  opening, test whether its original order expresses salience, dramatic timing,
  or actual dependency. Reorder it only when the new order exposes a mechanism,
  and explain what the change reveals rather than presenting wordplay as proof.
- **Language** - Define Search, Drive, and Renew and their relationships
  precisely. Preserve meaningful distinctions such as sequence versus cycle,
  enablement versus identity, and a missing force versus a personal deficiency.
  Favor structural words such as phase, loop, timing, momentum, resonance, drift,
  and renewal.
- **Posture** - Present the framework as one map of the territory, not the only
  correct map. State where a mapping is strong, partial, or metaphorical. Do not
  force every triad into a one-to-one equivalence.
- **Closing** - Return to the opening and leave the framework as a practical
  diagnostic. Link backward to the concept this post depends on and forward to
  the choice or application it enables.
- **Avoid** - Motivational hype, mystical certainty, repeated definitions without
  a new distinction, or references that display breadth without advancing the
  model.

#### Human Systems (`human-systems`)

Write as an engineer turning the same diagnostic lens on the person running
the loop. Software Engineering is the craft (Search), Engineering Systems is the
team (Drive), and Human Systems is the human-specific part of Renew: the
person running the loop, treated as a system with three parts.

- **Cognitive** - attention, habit, automaticity, creativity, motivation,
  meaning, and belonging.
- **Physical** - the body, energy, movement, posture, and rest.
- **Health** - sleep, stress, burnout, and recovery: what happens when the
  cognitive and physical parts are run past capacity, and how they come back.

The tone is warm but still diagnostic; the post earns its conclusion rather
than cheering for it.

- **Opening and movement** - Start with a phrase, quote, film scene, or personal
  moment (a speech, a coach's answer, a camp motto, a burnout). Question its
  order or completeness, propose the sharper version, and show what the change
  lets a person notice or do differently.
- **Evidence** - Lived experience plus one or two independent sources (research,
  history, a named thinker). The Quest Engine may supply the mapping, but the
  post must stand on its subject; if the framework is the main contribution, the
  post belongs in Quest Engine.
- **Language** - Plain, human words: attention, habit, motivation, meaning,
  joy, rest, energy, control, belonging. Name cognitive models precisely (System
  1 and System 2, diffuse and focused mode) and cite where they come from.
  Define framework terms on first use instead of assuming the reader has read
  the series.
- **Posture** - Secular and non-prescriptive. Offer a lens, not a regimen. Admit
  where a mapping is partial or where one life does not generalize.
- **Closing** - Return to the opening phrase or moment and leave the reader with
  a question or a small choice they can make.
- **Avoid** - Motivational hype, self-help imperatives, mystical certainty,
  health or medical advice presented as universal, and triads forced into a
  one-to-one mapping.

#### Engineering Systems (`engineering-systems`)

Write as an engineer diagnosing the design beneath an apparent people problem.
The tone is calm, exact, and fair. Authority comes from exposing the mechanism
and its boundary conditions, not from sounding certain. The subject is how
engineering teams and organizations work as systems (incidents, ownership,
risk, glue work, context flow, process design, incentives, and the words teams
use), and general engineering practices that are not only about software
(risk, scaffolding, iteration, work personalities).
Programming-language and code-level deep dives belong in Software Engineering.

- **Opening and movement** - Start with a failure mode, constraint, surprising
  behavior, or a phrase that stopped being useful. Show why the obvious model
  breaks (often at scale), introduce a more precise model, and trace what changes
  when the system is designed around it.
- **Evidence** - Combine implementation detail, an actual system or incident, and
  lived engineering judgment. Include enough technical detail for the reader to
  challenge the claim. Name the weakest case, the cost of the preferred design,
  and prerequisites such as observability, production access, team size, or
  existing tooling that bound where the recommendation applies.
- **Language** - Prefer scope and mechanism over verdicts: boundary, invariant,
  guardrail, seam, blast radius, affected cohort, fidelity, and tradeoff. Test
  apparent opposites for orthogonal dimensions before presenting a compromise.
- **Posture** - Treat heroics, glue work, blame, and repeated manual effort as
  signals from the system. Critique choices without flattening the people who
  made them; acknowledge why the old design was reasonable under its original
  constraints.
- **Systems containing agents** - Name what the agent may explore or generate,
  what deterministic validation gates its output, and where human judgment
  remains. Stochastic execution does not make the surrounding system exempt
  from explicit invariants or ownership.
- **Closing** - Restate the design principle at system scale and show what it
  makes possible. Prefer a durable reframing over a checklist of commands.
- **Avoid** - Moralizing technical choices, vague quality labels, unexplained
  jargon, recommendations before mechanisms, or a clean solution with hidden
  operating costs.

#### Software Engineering (`software-engineering`)

Write as a reflective practitioner documenting how the craft and career of
software engineering change while agents take on more of the execution. The
tone is curious, empirical, and provisional. The post should feel like a
field-tested account of changed work, not a product announcement. Agents are
the setting more often than the subject: the question is what the engineer now
does, verifies, owns, and learns.

- **Opening and movement** - Anchor the post in a date, version, duration,
  workflow, task, or career moment that previously felt impractical or
  different. Describe what was tried, what changed, what failed, and which
  conclusions survived the experiment.
- **Evidence** - Use concrete artifacts such as commits, pull requests, commands,
  elapsed time, session counts, validation results, or before-and-after workflow
  steps. Include failed trials when they explain why the surviving workflow
  earned confidence. Distinguish a demonstration from a durable capability
  claim, and calibrate the claim to the number and variety of runs behind it.
- **Language** - Say agent when autonomy is the relevant property and name the
  model or vendor only when it affects the result. Use context, validation loop,
  scaffolding, execution, friction, and tradeoff precisely. Distinguish
  session-scoped plans, cross-session worklogs, and durable design documents.
- **Posture** - Keep judgment singular and human. The tool may generate, inspect,
  or execute, but the author chooses the goal, evaluates the result, and owns the
  claim. Separate confidence in the direction from uncertainty about timing.
- **Career and craft** - Posts about learning to program, building expertise
  in software, or a software career belong here, including dated and personal
  ones. Treat personal history as evidence of how the job is changing, not as
  nostalgia. Name the skill that mattered, the one that turned out to matter
  more, and what a person entering the field now should practice.
- **Languages and code** - Programming-language, runtime, and code-architecture
  deep dives (concurrency models, safety checks, cross-language boundaries)
  belong here as part of the craft. Lead with the mechanism, show the code or
  standard-library detail that proves it, and name the tradeoff and where the
  comparison stops holding.
- **Closing** - Name the higher-level workflow change, what remains uncertain,
  and what evidence would change the conclusion. Let the account remain revisable
  as the tools change. Express that boundary in language specific to the
  experiment rather than repeatedly closing with the same
  confidence-versus-timing formula.
- **Avoid** - Vendor excitement as evidence, anthropomorphizing the tool into a
  coauthorial "we," universal claims from one successful run, or benchmark detail
  disconnected from actual work.

#### Field Notes (`field-notes`)

Write as an observer preserving a useful record: what happened, what it felt
like at the time, and what became visible only later. The tone is candid,
chronological, and self-correcting. A Field Note may remain unresolved when the
record supports a question more honestly than a conclusion. Unlike the other
tracks, the record takes precedence over building a framework, proving a design,
evaluating a tool, or recommending a team practice.

- **Opening and movement** - Start with a dated memory, object, habit, prediction,
  purchase, or reversal. Reconstruct the earlier expectation before introducing
  later knowledge, then follow the moments that changed the author's view. Keep
  the sequence intact even when a thesis-first arrangement would sound cleaner.
- **Evidence** - Use artifacts and period details to distinguish what the author
  knew then from what he knows now. Personal experience establishes the record;
  it does not automatically prove a universal rule. Structured examples belong
  when they document what happened; if they leave the reader with a procedure
  to copy rather than a clearer record to understand, they have turned the note
  into instruction.
- **Language** - Favor sensory and temporal specificity over retrospective
  polish: what was used, noticed, missed, kept, abandoned, or misunderstood.
  Technical language is welcome when grounded in the object or event being
  described.
- **Posture** - Write as witness and participant. Admit wrong predictions,
  incomplete memory, mixed motives, and unresolved tension. Preserve the earlier
  self's reasoning rather than making the past sound wiser.
- **Closing** - Return to the opening artifact or expectation, say what changed,
  and connect the personal record to a broader pattern. A productive question is
  a valid ending when certainty would be invented.
- **Avoid** - Turning the note into a how-to guide, erasing chronology to make a
  cleaner thesis, claiming representativeness from one life, or replacing vivid
  detail with generic nostalgia.

Front matter uses one human-readable `categories` value plus the matching
`extra.editorial_track` slug. Posts that participate in the Quest Engine series
also use `extra.series = "quest-engine"`. The reading-order number is derived
automatically from post dates at build time (oldest post is 1), so it is never
stored per post — add the post with the correct `date` and its position follows.

**Content-type exceptions**: Portfolio pages, reference guides, tutorials,
historical artifacts, source lists, and appendices may use more headings, tables,
or lists than narrative posts. Do not force the Quest Arc onto reference
material. Portfolio introductions may be short and structural rather than
first-person, and portfolios and tutorials do not require an italicized closing
reflection. They still need specific language, meaningful context, and an
organizing point of view. Historical chronicles may use one heading per era;
short predictions and opinion pieces may need no headings at all.

### Blog Post Meta-Structure: The Quest Arc (Exploration → Execution → Reflection)

**DECIDED**: Use the Quest Arc as the default backbone for reflective narrative
posts, not as a template imposed on every form. Before writing (or revising) a
narrative post, name the quest: what is the angle, what question is being chased,
and what is the "why" the reader should leave with. Then carry that one thread
from the first line to the last. Predictions may instead move from signal to
evidence to speculation, tutorials from obstacle to turning point to method, and
reference material by the structure readers need to retrieve information.

The backbone has three phases, which map directly to the [Quest Engine](/blog/quest-engine-introduction/) cycle (Search/Mastery = before, Drive/Autonomy = during, Renew/Purpose = after):

1. **Exploration (Searching, the "before")** — Open with a real, personal observation or a noticed pattern, and name the question it raises. This sets up the quest and pulls the reader into Searching mode. Do not lead with the thesis; lead with what you noticed.
2. **Execution (Driven, the "during")** — Develop the idea across 3-4 h2 sections
   when that division fits. Move from concrete example to abstracted principle to
   application. Each h2 develops one component of the thesis. This is where the
   mechanism or definition gets pinned down.
3. **Reflection (Renew, the "after")** — Close by looking back and answering the
   "why." For contemporary narrative posts, prefer an italicized reflection that
   points backward to the synthesis, outward to related posts, and upward to why
   it matters. Do not retrofit this ending onto preserved historical posts,
   portfolios, tutorials, or reference material.

**Why this matters**: A post without this backbone feels incoherent even when each paragraph is fine (the reader receives no single message). The point of the quest arc is coherence: one thread the reader can follow, ending in a takeaway that answers the "why."

**Observed defaults across narrative posts** (use these as a checklist, then test
whether the post's form calls for an exception):

- **Concrete opening**: begin with an observation, scene, artifact, reaction, or
  personal position.
- **Earned closing**: synthesize what changed and why it matters. Contemporary
  narratives usually use an italicized, cross-linked reflection; older and
  instructional posts use several valid alternatives.
- **3-4 h2 sections when useful**: use them for major turns. A historical
  chronicle may need more, while a compact prediction may need none.
- **Quest movement when the post is a quest**: reflective narratives usually move
  through search, action, and renewed understanding. Do not claim that portfolios,
  predictions, or reference pieces secretly follow that arc.
- **Concrete before abstract**: lead with lived evidence, then generalize, then
  connect to the broader idea web.

**For agent authors and reviewers**: When drafting or revising a post, check that all three phases are present and that a single "why" runs through them. If a draft is "a collection of individuals who happen to wear the same shirt" (paragraphs with no shared thread), the fix is to name the quest and re-cohere the post around it, not to add more sections.

### Recurring Framing: Personality Styles (DOPE / Director-Thinker)

**DECIDED**: When writing about communication or personality styles (for example
the DOPE bird model: Dove/Relater, Owl/Thinker, Peacock/Socializer,
Eagle/Director), hold these positions consistently:

- **No personality is good or bad** - Never rank the four styles from best to
  worst. Fit depends on context: the Dove is ideal for therapy and the social
  sciences, the Peacock for many performing/creative roles (though plenty of
  artists are secluded). Ranking a style as the "worst" is a category error.
- **Personalities are contextual and can change** - A person shows different
  personalities across rooms (family, friends, work) and across seasons of life.
  Personality is mostly what you are and partly what you have learned; it is not
  a fixed grade.
- **There is a learnable work personality** - The best performers cue the
  communication style a moment calls for and step back out. This is a skill you
  can exercise, not a trait you were issued.
- **Engineering fit is Director + Thinker only** - For engineering, the Director
  (Eagle) and Thinker (Owl) are the two work-mode personalities worth
  practicing. Map only these to the Quest Engine: Thinker → Searching, Director →
  Being Driven. Do not force the Dove or Peacock onto the framework; not every
  personality maps cleanly, and forcing it cheapens the mapping.

Reference post: `zola-site/content/blog/director-and-thinker-work-mode-personalities.md`.

## Project Structure Standards

```
masters3d.github.io/
├── plans/                 # All planning docs (CRITICAL FOR CONTEXT)
│   ├── README.md
│   ├── session-context.md # READ FIRST - Current session state
│   ├── current-task.md    # Active task details
│   ├── enhancement-roadmap.md # Comprehensive improvement plan
│   ├── progress-tracking.md   # Overall project progress
│   └── agents.md         # This file - Agent guidelines
├── legacy/               # Original files (backup) 
├── zola-site/           # New Zola structure (MAIN WORKING DIRECTORY)
├── CNAME                # Preserve custom domain
└── [original files]     # Keep until migration complete
```

## Content Guidelines

### Existing Content to Preserve
- **About section**: "Designer, Developer, Product Owner"
- **3D Projects**: Community profile link
- **Video Projects**: All YouTube/Vimeo links (20+ items)
- **GitHub Projects**: iOS Swift, Python, Java project links
- **Styling**: Architect theme appearance

### Content to Enhance
- **Blog functionality**: ✅ **COMPLETED** - Full blog system implemented
- **Responsive design**: Improve mobile experience
- **SEO**: Add meta tags, structured data
- **Performance**: Optimize images, CSS

## Technical Standards

### Zola Specifics
- **Config**: Use `config.toml` for site configuration
- **Content**: Markdown files in `content/` directory
- **Templates**: Tera templating engine
- **Styling**: Preserve existing CSS, convert to Sass if beneficial

### GitHub Actions
- **Trigger**: On push to `master`
- **Build**: `zola build` with Zola pinned to a specific version in `static.yml`
- **Deploy**: Upload `zola-site/public` as a Pages artifact (no `gh-pages` branch)
- **Preserve**: CNAME file in output

### Verifying What Is Actually Deployed

Agent sandboxes usually cannot reach masters3d.com or masters3d.github.io (DNS is blocked), and
there is no `gh-pages` branch to read. Pages artifacts also expire, so they are typically
unavailable for older runs. To check the live site without guessing:

1. **Find the deployed commit**: list runs of `static.yml` on `master` and take the most recent
   successful one. Its `head_sha` is what is live.
2. **Reproduce that build exactly**: check the commit out in a worktree and build it with the
   same Zola version `static.yml` pins. The build is deterministic, so the output matches what
   was published.
   ```bash
   git worktree add /tmp/deployed <head_sha>
   cd /tmp/deployed/zola-site && zola build
   ```
3. **Inspect `public/`** to answer the question (does a URL exist, does a redirect resolve), then
   `git worktree remove /tmp/deployed --force`.

Never assert that something is or isn't live based on the source tree alone — a declared
`aliases` entry does not mean a redirect was published.

## Common Questions & Answers

**Q**: "What static site generator are we using?"  
**A**: Zola (Rust-based), decided in Session 1

**Q**: "How are we deploying?"  
**A**: GitHub Actions builds the Zola site and publishes it as a GitHub Pages artifact (no gh-pages branch)

**Q**: "What about the custom domain?"  
**A**: Preserving masters3d.com via CNAME file

**Q**: "What's the current project status?"  
**A**: Portfolio migration COMPLETED and DEPLOYED. Now in Enhancement & Optimization phase.

**Q**: "What branch should I be on?"  
**A**: `enhancements-and-optimizations` for current work (check session-context.md). **Always open pull requests against `master`** (see Core Decision 5).

**Q**: "Where is the live site?"  
**A**: https://masters3d.com (deployed) and https://masters3d.github.io (GitHub Pages)

**Q**: "How do I get current context if copilot restarts?"  
**A**: Read `plans/session-context.md` FIRST, then current-task.md and enhancement-roadmap.md

**Q**: "Can we change the technology choice?"  
**A**: Only if user explicitly requests reconsideration; document reasoning

## Version History

- **v1.0** (2024-12-28): Initial guidelines established
- **v1.1** (2024-09-07): Blog system implementation completed
  - Full Zola blog architecture with RSS support
  - Responsive design matching site theme
  - Taxonomy system (categories/tags)
  - SEO optimization with meta tags
  - Markdown-first content creation workflow
  - **Created using coding agents** - demonstrates AI-assisted development
  - **Repository-based context** - agent instructions stored in codebase
- **v1.2** (2024-09-14): Clean-up and validation session
  - Branch: `clean-up-and-validations`
  - Focus: Deployment fixes, code cleanup, issue resolution
  - Major issue identified: Blog system not deploying (404 on /blog/)
  - Repository cleanup and optimization
- **v1.3** (2024-01-06): Enhancement & Optimization Phase Launch
  - Branch: `enhancements-and-optimizations`
  - **DEPLOYED**: Portfolio migration successfully completed (PR #9 merged)
  - **NEW PHASE**: Performance, SEO, content expansion, UX improvements
  - **Context System Enhanced**: Robust session preservation for agent continuity
  - **Live Site**: https://masters3d.com - Fully functional blog-centric portfolio
  - **Agent Restart Protocol**: Enhanced guidelines for seamless context restoration
- **v1.4** (2026-07-08): Blog post meta-structure formalized
  - Documented the Quest Arc backbone for posts: Exploration → Execution → Reflection
  - Derived from analyzing the full blog corpus for the exploration/execution/reflection pattern
  - Purpose: keep every post coherent around a single "why" instead of a set of disconnected sections
- **Future versions**: Update when major decisions change

## Blog System Implementation (Added v1.1)

### Blog Architecture
**IMPLEMENTED**: Complete blog system using Zola
- **Location**: `zola-site/content/blog/` for posts
- **Templates**: `zola-site/templates/blog.html`, `blog-post.html`
- **RSS Feed**: Automatic generation at `/blog/atom.xml`
- **Styling**: Responsive CSS in `static/css/blog.css`

### Content Workflow
**DECIDED**: Markdown-first approach
- **Create posts**: Add `.md` files to `zola-site/content/blog/`
- **Frontmatter**: TOML format with title, date, description, taxonomies
- **Build**: `zola build` generates static site
- **Deploy**: Same GitHub Actions workflow

### Blog Features Implemented
- ✅ **RSS/Atom feed** support
- ✅ **Taxonomy system** (categories and tags)
- ✅ **SEO optimization** (meta tags, Open Graph)
- ✅ **Social sharing** buttons
- ✅ **Responsive design** matching site theme
- ✅ **Navigation integration** across all pages

### Adding New Posts - Instructions for Future Agents
1. **Create file**: `zola-site/content/blog/post-name.md`
2. **Add frontmatter**:
   ```toml
   +++
   title = "Post Title"
   date = 2024-09-07
   description = "SEO description"
   template = "blog-post.html"
   categories = ["category"]
   tags = ["tag1", "tag2"]
   +++
   ```
3. **Write content**: Standard Markdown below frontmatter
4. **Format Markdown**: `python3 scripts/format_markdown.py` (required; runs Prettier + markdownlint, keeps diffs small, does not change rendered output)
5. **Test locally**: `cd zola-site && zola serve`
6. **Build**: `zola build` before committing

### Retitling or Renaming Posts - Never Break a Published URL

A post's URL comes from its filename, so renaming the file changes the URL and 404s every
existing link to it. When you retitle a post, rename the file to match **and** keep the old URL
alive with `aliases`.

1. **Rename the file** so the slug matches the new title: `git mv old-slug.md new-slug.md`
2. **Add the old URL to `aliases`** in the frontmatter, listing every slug the post was
   previously published under:
   ```toml
   aliases = ["/blog/old-slug/"]
   ```
3. **Put `aliases` at the top level, before any `[...]` table header.** This is the most common
   mistake. In TOML, every key after a table header belongs to that table, so an `aliases` line
   placed after `[extra]` parses as `page.extra.aliases`, which Zola does not read. It generates
   **no** redirect and fails silently — the build still succeeds. Keep `aliases` above
   `[taxonomies]` and `[extra]`.
4. **Update internal links** to the new slug across `zola-site/content/`. Do not blanket-`sed`
   the old slug: that also rewrites the `aliases` value you just added, which must keep pointing
   at the old URL.
5. **Verify the redirect was actually generated** after `zola build`:
   ```bash
   cat zola-site/public/blog/old-slug/index.html   # expect a meta refresh to the new URL
   ```
   If that file does not exist, the alias was not picked up — recheck step 3.

**Auditing for lost URLs**: to prove no live URL was dropped, build the currently-deployed
commit in a worktree and diff its slug list against the new build. Anything present in the old
build but missing from the new one is a 404 waiting to happen.

### Post Backlog: Finding and Closing Ideas

**DECIDED**: Candidate posts live in [`plans/post-backlog.md`](./post-backlog.md).
Each row has an ID, the idea, its source location, an editorial track, a priority,
and a status. When asked for "the next post", take the highest-priority `open` row
unless the user names one.

**Finding more ideas.** The main source is
[masters3d/ingenio](https://github.com/masters3d/ingenio). Look in this order:

1. **Ingenio issues** (all closed, still readable). The issue body holds the
   author's own words. Use `list_issues` with `state` unset, then `issue_read`.
2. **`specs/*/VISION.md`**. Most of each file is generated template text
   (Mission Statement, Cognitive Agent Enhancement, Success Metrics). Only the
   "Problem Statement" / "Engineering Context" paragraph is the author's; ignore
   the rest as evidence of the author's view.
3. **`pillars/`, `presentation/`, `career.md`, `media/`**. These hold framework
   detail, talk decks, and diagrams.
4. **`cognitive_systems/`, `experiments/`, and the root `*_FIX*.md` /
   `COGNITIVE_*.md` files**. These document the INGENIO-1 experiment itself.

Before adding a row, check that no existing post already makes the argument:
grep `zola-site/content/blog/` for the topic's key terms and read any hit. If a
post covers it, add the idea to "Covered by Existing Posts" instead. Pick the
track with "Placing a Post in a Track" above. Assign `P1` only when the source
already states a thesis in the author's words.

**Closing an item.**

1. Read the source issue and spec, then write the post following the voice,
   track, and writing-style rules in this file. Use the issue's `created_at`
   for any date you mention. Do not invent personal anecdotes the sources do
   not support.
   **Every post must stand on its own.** Do not link to the ingenio repository,
   its issues, or its files, and do not point the reader at "the issue", "the
   spec", or "the repo". State what the note said in the post itself. When the
   note was mostly a link to an outside article, explain that article's idea
   with attribution; the link may stay as a citation, but the post must make
   sense without it.
2. Run `python3 scripts/format_markdown.py`,
   `python3 scripts/check_content_marks.py`, and `cd zola-site && zola build`.
3. In the same PR, set the row's Status to `published` and put the post's slug
   in the Post column. Do not delete the row; it is the record of where the idea
   came from.
4. When asked to write posts without publishing them, add `draft = true` to the
   frontmatter (after `date`) and set the row's Status to `draft`. Zola skips
   drafts in `zola build` and the feed. Date each draft for its planned release:
   new drafts join the end of the queue at two per month (the 1st and the 15th),
   and the queue order is the author's review order. The list lives in the
   "Release Schedule" section of `plans/post-backlog.md`. To publish a draft,
   the author reviews it, removes `draft = true`, and the row moves to
   `published`.
   **Draft gate:** `scripts/check_upcoming_drafts.py` runs in PR validation and
   in the deploy workflow. It fails when any draft is dated within the next 7
   days or is overdue, and it prints the queue by month so the runway is
   visible. A failing gate means: publish that draft or move its date. Run it
   locally with `python3 scripts/check_upcoming_drafts.py` (add `--today
   YYYY-MM-DD` to preview a future date).
   **Cross-references follow release order.** An inline link
   `[text](/blog/<slug>/)` may only point at a published post, or (from a
   draft) at a draft dated on or before this one, because those go out first.
   Anything later goes in `related` under `[extra]`:
   `related = ["slug-a", "slug-b"]`. The post template lists related posts
   that are published, in both directions (posts this one names plus posts
   that name it), so when a later post goes out, the earlier one picks up the
   link on the next build without editing it. When publishing a draft out of
   order, check its inline links first. `scripts/check_post_links.py` enforces
   this in PR validation and deploy (it also fails on missing slugs).
5. Use `covered` (with the existing slug) or `dropped` (with a reason) to close
   a row without writing a new post.

### Blog Guidelines for Agents
- **Preserve workflow**: Keep simple file-based posting
- **Maintain design**: Blog matches existing site theme
- **RSS consistency**: All posts auto-include in feed
- **Markdown source**: Always prioritize `.md` files as source of truth
- **Template consistency**: Use `blog-post.html` for all posts
- **Model agnostic**: System works with various coding AI models (GPT-4, Claude, Gemini, etc.)
- **Context preservation**: Agent instructions are part of the repository for consistency

## Enhancement Phase Guidelines (Added v1.3)

### Current Phase: Enhancement & Optimization
**Status**: ACTIVE - Portfolio migration completed, now optimizing
**Branch**: `enhancements-and-optimizations`
**Live Site**: https://masters3d.com

### Enhancement Priorities
1. **Performance optimization** - Speed, loading, asset optimization
2. **SEO enhancement** - Search visibility and ranking
3. **Content expansion** - Blog posts and portfolio updates
4. **User experience** - Mobile, accessibility, navigation
5. **Technical excellence** - Code quality, maintainability

### Agent Restart Recovery Process
When copilot restarts or has issues:

1. **IMMEDIATE**: Read `plans/session-context.md` 
2. **Check branch**: `git branch` (should be `enhancements-and-optimizations`)
3. **Check status**: `git status` and `git log --oneline -5`
4. **Read tasks**: `plans/current-task.md` for active work
5. **Review roadmap**: `plans/enhancement-roadmap.md` for comprehensive plan
6. **Test environment**: Verify local development setup
7. **Update context**: Add new session entry to session-context.md

### Context Maintenance Requirements
- **Update session-context.md** at start, milestones, and end of session
- **Document all discoveries** and important decisions
- **Maintain handoff notes** for seamless transitions
- **Preserve technical details** about local development state
- **Record next steps** clearly for continuation