+++
title = "Fearless Engineering"
date = "2026-07-02"
description = "When I was starting out, hesitation held me back from trying things. Over time it faded, not because I got braver, but because I got a better handle on risk. Fearless engineering is not the absence of caution. It is a calculated read of what you know, what you do not, and how far a change can reach."
template = "blog-post.html"
categories = ["engineering", "mindset", "workflow"]
tags = ["quest-engine", "fearless", "risk-management", "bias-to-action", "systems-thinking"]
+++

When I was starting out as a software engineer, a lot of hesitation held me back
from trying things. I was reluctant to touch my git repository in case I
destroyed it. I hesitated to make a change that might break other people's work.
I was careful (I am still careful), but back then careful and hesitant were the
same feeling. Today that hesitation is mostly gone, and the confidence is high.
What changed is worth examining, because I do not think I simply got braver. I
think I got a better handle on risk, and I built the systems that made the
hesitation unnecessary.

The hesitation I felt when I was starting out was not irrational. It was
accurate. I did not understand what the systems did, I could not estimate the
radius of a change, and I could not see what would happen after I hit enter.
What I labeled as fear was really a signal that I had a poor handle on the risk
and no way to manage it. That reframing matters, because you cannot willpower
your way out of an emotion, but you can absolutely improve a risk assessment.
The moment I stopped treating the feeling as fear to push through and started
treating it as a risk to categorize, the hesitation had somewhere to go. It
became a to-do item: name the risk, measure the radius, build the rail, then
act.

## Calculated Risk: The Known and Unknown Matrix

The core move that lowers hesitation is turning a vague dread into a calculated
risk, and the tool for that is the old known/unknown matrix. Fear thrives in the
fog of not knowing what you do not know. The matrix drags each concern into a
quadrant so you can see what you are actually dealing with:

|             | You know it                                                                       | You do not know it                                                                                                  |
| ----------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Known**   | **Known knowns**: tested behavior, documented facts, things you can rely on.      | **Unknown knowns**: tacit assumptions, "everybody knows" folklore, things the team knows but you have not surfaced. |
| **Unknown** | **Known unknowns**: mapped gaps you can research, measure, or test before acting. | **Unknown unknowns**: the surprises, the true blast-radius risk you cannot see yet.                                 |

Most hesitation lives in the two right-hand cells. Known unknowns are the easy
win: they are already named, so you research them, write a test, or run a small
experiment, and they convert into known knowns. Unknown knowns are the sneaky
ones, the assumptions you inherited without examining, and a pre-mortem or a
second reader tends to flush them out. The unknown unknowns are the only
quadrant you genuinely cannot shrink by studying harder, so you manage them
structurally instead: small blast radius, gradual rollout, high visibility, and
a fast rollback. Calculated risk is not the elimination of the unknown. It is
knowing which quadrant each concern sits in and having a matching move for each.
Once every concern is placed, there is very little left to feel vaguely afraid
of, and what remains is a bias toward action, because the cost of acting on a
small, reversible, well-instrumented change is lower than the cost of stalling.

## Fearless Is Something the System Grants You

Fearless engineering is a bias toward action that the system has earned the
right to give you. I run agents at pretty high settings, fully autonomous, and I
do not hesitate much about it. But that confidence is not a personality trait I
decided to adopt. It is downstream of very specific rails. The main branch sits
behind permissions, so it will not be lost. The agent does not get access to
things like email. If my development machine were wiped, I lose nothing that
matters (I keep two or three machines fully configured, and spinning up a new
one takes a few minutes). Drop any one of those rails and the same fearlessness
becomes recklessness. So the honest version of the claim is not "just be
fearless." It is "earn fearlessness by managing the risk, and until you have,
respect the hesitation, because it is telling you the risk is still
uncategorized."

There is a subtlety about what the blast radius actually is. "My laptop is
disposable" protects my source code, but a fully autonomous agent's radius is
not my hardware. It is whatever credentials and permissions it can reach:
production APIs, cloud spend, outbound messages, third-party systems. The unit
of risk is the permission surface, not the machine. Withholding email access is
exactly that principle in action (scope the blast radius, not the box it runs
on). This is also why a bias toward action in production does not feel like
recklessness. We have established patterns: a rollout starts in a region or zone
with very low usage, proves itself, and only then moves slowly toward high-usage
areas. The rails do the reassuring, so the default can be to move rather than to
stall.

The one thing I protect fiercely is not feeling rushed. A high-blast-radius
change needs to be thoughtful and methodical, and rushing is usually imposed
from the outside. Reversibility is the variable that decides how bold to be.
Two-way doors (things you can easily undo) deserve a strong bias toward action,
because the calculated risk is genuinely low and stalling costs more than
trying. The danger is misclassifying a one-way door as a two-way one: deleted
data, leaked secrets, sent messages, spent money, and eroded trust do not roll
back. Sometimes a flicker of hesitation is precisely what makes me look twice at
whether a door is really reversible, and that is the hesitation doing its job,
moving a concern out of the unknown-unknown corner before I commit.

## When the Human Is Blamed, the System Failed

Most of the large outages I have seen that were attributed to a person were not
really human problems. They were system problems, and often engineering design
problems: a single point of failure, no way to roll out gradually without going
global, or low visibility into what was actually happening. If a system allows
one person's ordinary change to trigger an extensive radius of failure, that is
not primarily that person's failing. It is a design that handed one keystroke
too much reach. The fix is not to make people more hesitant. It is to shrink the
radius, add the gradual rollout, and raise the visibility, so that a mistake is
caught small instead of felt globally, and so the default posture can stay a
bias toward action.

This is why I try not to hold things in my head. If I ever do something
manually, I document it (not so much for other people as for my future self) and
then I try to make it repeatable. If the system needs a manual step, the
question becomes how to make that step repeatable, so I can offload the
self-doubt to the system instead of carrying it. Then I test the system, and I
deliberately try to make it fail in low-risk situations, so that by the time I
am rolling out to high-risk locations I can say we tried it everywhere else and
saw no issues. One caution I hold onto: automating a manual step only helps if
the step was correct to begin with. Encode a flawed process and you have made
the mistake fast and repeatable. Automation removes vigilance along with toil,
and vigilance is what catches the novel failure the automation was never written
for. So the low-risk-first testing is not a formality. It is what keeps
automated confidence honest and turns unknown unknowns into known unknowns
before they reach production.

I also worry, sometimes, that I am too confident and simply wrong. The tempting
answer is "I have systems that check my thinking." But if those are the same
systems that produced my confidence, they cannot independently falsify it, and
overconfidence tends to peak right before an incident (nothing broke the last
fifty times, so the margin quietly erodes). The real counter is checks I do not
control: a pre-mortem, a designated dissenter, tracking near-misses and close
calls rather than only failures. This is also the honest version of "share the
load with the team." Team decisions genuinely distribute responsibility, and
they are usually the right call. But shared decisions can also produce shared
blind spots, where everyone's comfort masks the same missing question.
Distributing the decision reduces individual hesitation without necessarily
reducing actual risk, unless someone's explicit job is to argue against.
Socialize the scrutiny, not just the comfort.

## The Quest Engine View of Risk

None of this means risk goes to zero. I am privileged not to work on systems
where lives are at stake. In that world (a rocket carrying people who are
breathing) the caution would be appropriate, and the answer is the same in kind
but far larger in degree: many independent systems checking each other, many
batteries of validation, run longer and longer, because you never get 100
percent certainty, only high certainty that keeps climbing. Even there, the
useful posture is not fear but methodical risk management plus independence. The
framework I keep returning to explains why. The
[Quest Engine](/blog/quest-engine-the-why/) puts the WHY above the HOW, and runs
three forces: Searching (what does better look like), being Driven (what can I
control), and Renewal (am I still aligned). The risk matrix maps cleanly onto
it. Searching is how you convert known unknowns into known knowns and surface
the unknown knowns you were carrying as assumptions. Being Driven is naming what
you actually control versus what the system controls, which is where the bias
toward action lives. Renewal is the guardrails, rollouts, and reviews that carry
forward, so the next change starts with a smaller unknown-unknown corner than
the last.

Read that way, hesitation is not an emotion to override. It is a risk assessment
that has not finished running. It says "you have not yet categorized this," and
the work is to place it in the matrix and build the matching rail. The one place
this is weakest, and worth naming, is the genuinely first-of-its-kind change (no
prior pattern, no meaningful canary, blast radius truly unknown). That is
exactly where fearlessness is least earned and where slow, methodical,
more-people matters most. The model is strongest for recurring operations and
weakest for the novel one-off, and I would rather say that plainly than pretend
the rails cover everything.

So at a high level: staying hesitant at the work you do for eight hours a day is
not a place to remain. If you feel empowered to make changes, you should feel
empowered to take bold, reversible actions with a bias toward action, and keep
people aware as you go. But that fearlessness is earned, not asserted. It rests
on a blameless culture (in a blameful org, hesitation is rational, and no amount
of mindset fixes that), on the standing to refuse the rush, and on the rails you
built while you were still learning the risk. Fear is not the enemy. Unmanaged
blast radius is. Hesitation is just the alarm telling you the risk is not
categorized yet. You do not silence the alarm. You place each concern in the
matrix, build the rail it points at, and then the hesitation is gone, because
there is nothing left for it to warn you about, only a calculated risk worth
taking.

---

_This maps onto the [Quest Engine framework](/blog/quest-engine-introduction/):
risk assessment as a Searching move (converting unknowns to knowns), a Driven
question (what you actually control), and a Renewal answer (the guardrails that
carry forward). For the WHY-above-the-HOW structure, see
[The Why Behind the How](/blog/quest-engine-the-why/). Related:
[Set. Action. Reload.](/blog/set-action-reload/) on closing the loop so gains
compound, and [Faith. Guts. Stamina.](/blog/faith-guts-stamina/) on courage that
has a direction._
