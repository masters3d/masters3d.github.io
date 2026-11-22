# Voice Guide: How the Older Posts Sound

Read this before writing a new post or new paragraphs in an existing one. It
describes the author's sentence-level voice, taken from posts he wrote before AI
tools were part of his writing (2009 to 2020). `plans/agents.md` ("Voice
Guidance" and "Editorial Tracks") decides what a post says and how it is built;
this file covers how the sentences sound.

- New prose only. Do not restyle existing posts toward this guide or rewrite
  their phrases unless the author asks (see "What this guide does not change").
- Do not copy the typos or the `!!!!` of the 2009 note, and do not invent
  anecdotes, feelings, prices, or dates the sources do not support.

## Sources

| Source | Written | How close to his original |
| --- | --- | --- |
| `apple-swift-apps-everywhere-prediction.md` | 2014 | Reposted in #62 with grammar, spelling, and casing fixes only |
| `2016-one-year-of-ipad-pro-12-9.md` | 2016 | Reposted in #84 with grammar and typo fixes; names removed |
| `apple-chips-ar-glasses.md` | 2020 | Reposted in #83 with the original wording |
| `longest-path-learning-data-structures-algorithms-tech-interview.md` | 2020 | Restored in #85; the three section headings were added then |
| The May 2009 note quoted in the description of #42 | 2009 | His raw text (about 350 words, typos included) |

The posts are in `zola-site/content/blog/`. Not used as evidence of his voice:

- `palm-sony-android-iphone-blackberry.md`: an agent expanded the 2009 note
  (about 350 words) into a post of about 1,000 words. Use the note in #42
  instead.
- `from-creative-tools-to-software-engineering.md`: two Medium posts combined
  and revised in 2026 (#86).
- `technical-projects-portfolio.md` and `media-projects-portfolio.md`: project
  lists, not prose.

To check whether he uses a phrase at all, search what he wrote on GitHub before
AI writing tools: issues and pull requests created before June 2022 and comments
before ChatGPT's release on 30 November 2022 (about 50,000 words). For example,
`gh search issues "the real question" --author masters3d --created "<2022-06-01"`,
then the same with `gh search prs`. `--commenter masters3d` finds threads he
commented in; confirm the match is his. Later text may include output from AI
tools.

## How he sounds

- **Plain statements, often a paragraph of their own.** "The iPad Pro has
  impressive hardware." "JavaScript sucks. Everybody uses it because they are
  forced to use it. That is it."
- **The specific thing, with its numbers.** "I picked up my iPad Pro 12.9"
  128GB Wi-Fi + Cellular model the morning of November 11, 2015, at my local
  Apple Store." The 2009 note gives the price of each PDA (500 dollars).
- **Feelings in everyday words.** "It felt like Christmas had come early." "I
  love how loud the speakers are." "I love math, by the way."
- **Opinions marked as his.** "I think", "I believe", "I predict", "I am not
  sure", "I want to believe". The hedge qualifies the claim, never the writing.
- **Questions and short lines as turns.** "How about this?" "What is next for
  Apple and apps?" "Is this the curse of knowledge?" "Back to Swift."
- **"Imagine" for speculation.** "Imagine being able to feel that you are
  actually pushing down a button on the iPad."
- **Everyday idioms.** "eat Nintendo's lunch", "all bets are off", "steal the
  fire from the gods", "hitting an invisible wall".
- **A tradeoff in one sentence.** "It is not as convenient as something that is
  already attached, but it works for me." "It is a pretty expensive book reader,
  but that is the best use I get out of it."
- **A precedent instead of an abstraction.** "Real Player had a feature like
  this 10-15 years ago."
- **Short asides in parentheses.** "(but this will change)", "(the same way they
  did ARC)".
- **His own thoughts, quoted.** "'Oh, cool. This is a lecture about dynamic
  programming from MIT,' I thought to myself."
- **Light self-deprecation.** "I do not have the prettiest handwriting".
- **Direct advice.** "Do not just watch the lectures or recitations. Do the
  problems by hand. When I say by hand, I mean do the problem on a board or in a
  notebook."
- **Plain labels for headings, when there are any.** The 2009 note uses "The
  internet and phones" and "What I am looking for".
- **Endings that land on something.** A wish ("I hope for a future where I can
  type onscreen and have that feel natural."), a prediction ("It's going to be
  something between VR headset and HoloLens."), or a sign-off after advice
  ("Happy coding!"). None of them restates the thesis.

## What changed in newer posts

Measured on 2026-11-22 over prose paragraphs only (no front matter, headings,
lists, quotes, tables, code, or italic notes; drafts included). Four posts are a
small sample, so read the rows as direction, not targets.

| Per 1,000 words, unless noted | Older posts (4; 2,335 words) | Posts dated 2025 on (149; 177,089 words) |
| --- | ---: | ---: |
| Mean sentence length (words) | 15.1 | 14.6 |
| Sentences per paragraph | 2.9 | 4.4 |
| "I" | 47 | 10.5 |
| "I think / believe / predict / love / wish / hope / am not sure" | 4.7 | 0.4 |
| Exclamation marks | 1.3 | 0.03 |
| Colons | 1.7 | 7.9 |
| "X is not A. It is B." | 0.4 | 2.0 |
| Phrases in `scripts/repeated_phrases.toml` | 0.9 | 6.8 |

- Sentence length did not change. Do not chop sentences to sound like him.
- Paragraphs got longer, and the first person mostly left. The older posts say
  "I" more than four times as often and state opinions and feelings as his own.
- Colons multiplied. In newer posts many set up a reveal ("The short version:
  ..."). The older posts use four: a list, a quote, a source line, and one setup
  ("The game is this:").
- Short sentences changed kind. In the older posts a short sentence carries a
  fact, a feeling, or a turn ("I love my iPad.", "Back to Swift."). Newer posts
  often use abstract one-liners ("The loop compounds."). Write the first kind.
- The formulas are new. Newer posts lean on phrase families that his pre-AI
  GitHub writing almost never uses (0.2 per 1,000 words). The largest is the
  reframe "X is not A. It is B.": 377 uses in 133 of 157 posts, and one in that
  GitHub writing. `python3 scripts/check_repeated_phrases.py` lists every
  family with its current count.

## Writing a new post

1. Read at least two of the source posts above before drafting.
2. Write "I" when the post is about something he did, saw, or thinks, and mark
   opinions plainly ("I think", "I predict", "I am not sure").
3. Keep most paragraphs to one to three sentences. A one-line paragraph is fine
   for a verdict or a turn.
4. Give each section at least one concrete detail: a product, a date, a price, a
   number, a course or tool by name, or something he did. Use only details the
   sources support.
5. Turn with a question or a short line ("Back to Swift."), not with a colon
   reveal or an announcement ("Here's the real value:").
6. When a sentence starts to deny something nobody claimed ("X is not A. It is
   B."), write B.
7. Use the plain verb: "is in", not "lives in"; "blocks", not "sits between";
   "goes wrong", not "failure mode".
8. End on a wish, a prediction, advice, or a next step. One sentence of
   reflection is enough.
9. Run `python3 scripts/check_repeated_phrases.py` and add no uses of a family
   it flags. Rewrite the sentence; do not swap in a synonym.

## What this guide does not change

- Existing posts keep their wording. The phrase report is a diagnosis: only the
  families the author enforces get rewritten (as of 2026-11-22: "X is real", "I
  keep coming back to", "load-bearing", and the "I want to be careful" hedges).
  See "Repeated phrases" in `plans/agents.md`.
- Older posts keep their historical wording, per "Voice Guidance: Common
  Authorial Voice" in `plans/agents.md`.
