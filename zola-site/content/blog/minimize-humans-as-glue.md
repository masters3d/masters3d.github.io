+++
title = "Minimize Humans as Glue"
date = "2026-05-30"
description = "Tanya Reilly's 'Being Glue' names the invisible human work that holds a team together but never shows up on your own record. The deeper pattern is the same one behind every high-maintenance system: a person standing in for a fix that was never made. The goal is not to be better glue, it is to build systems that heal themselves so humans are needed as glue as rarely as possible."
template = "blog-post.html"
[taxonomies]
categories = ["Engineering Systems"]
tags = ["glue-work", "career-growth", "boundaries", "on-call", "saying-no", "systems-thinking", "self-healing", "promotion"]
[extra]
editorial_track = "engineering-systems"
+++

Tanya Reilly's talk [_Being Glue_](https://www.noidea.dog/glue) is one of those
pieces of writing that reorganizes how you see your own week. The idea is simple
and uncomfortable: every team runs on a layer of invisible work (coordinating,
unblocking, onboarding, documenting, smoothing over the rough edges between
people). That work is real, the team genuinely needs it, and it is almost never
the work that gets you promoted. Reilly calls it glue, and she points out the
trap inside it. The people who hold the team together with glue often watch less
helpful, more visible colleagues move up the ladder while their own careers
quietly stall.

I lived the trap before I had a name for it. A few years back I learned about
_Being Glue_, and it landed hard because I was exactly the person being
described. I ran the ad hoc meetings, I jumped on every quick debug session, I
taught everyone my process before I had even finished proving it worked. The
team was genuinely better for all of it. And yet none of it pointed back at me.
When promotion season came around, the work that moved the dial was the work
with a clear, individual attribution, and almost nothing I did had my name
cleanly on it. The team rose; I stayed put. That is the part of the talk I wish
someone had handed me earlier: glue is most dangerous precisely for the people
who are not yet at the top of the ladder, because that is the stage where you
most need legible, attributable wins, and glue is the work that refuses to be
attributed.

## Practicing the way out

So once I recognized myself in the talk, I started to implement a way to get out
of being glue. It might seem hard, especially if folks already expect you to do
it (you are the one who runs the meetings, onboards new people, keeps the docs
current, and nobody else has stepped up). But over a few semesters of practicing
not being the glue, not being the firefighter, and not doing things for other
teams just to be helpful, the habit reshaped itself. A few concrete moves did
most of the work:

- **Start saying no.** This is the unglamorous core of it. Notice the tasks that
  are easy for you and hard for the team, the ones you grab on reflex because
  grabbing them feels good, and let them go when they will not move the dial.
- **Give other people the opportunity to learn something only you know how to
  do.** Hoarding a skill makes you the permanent glue for it. Handing it off
  creates a second owner and frees you.
- **Better yet, have an agent do it instead of you (or have the agent send the
  PR).** A lot of recurring glue is now automatable. If a coding agent can
  produce the change and open the pull request, your hands stay free for the
  work that moves you up.
- **Instead of setting up the meeting, have an agent write the email and send
  it.** Most coordination glue is a communication task in disguise. Draft once,
  automate the rest, and reserve synchronous time for the things that genuinely
  need it.
- **Spend more time on learning.** The hours you reclaim from glue are best
  reinvested in getting more proficient, which is the thing that actually
  compounds.

A useful way to budget the reclaimed time is to split it deliberately: **80% on
what will move you up the ladder, 15% on novel things, and 5% on moonshot,
high-leverage bets.** The 80% keeps your trajectory honest, the 15% keeps you
growing, and the 5% is where the outsized wins occasionally come from.

The clearest example is the AI engineering work I have been doing. The old me
would never have started that journey alone. I would have insisted on bringing
the whole team along, spending hours teaching folks my process one at a time,
pacing myself to the slowest shared understanding. The new me moves as fast as I
can. If, as a byproduct, other people see what I am doing and learn from it,
wonderful. But guiding and teaching is no longer the goal. The goal is to be as
proficient as I can be, and then, only if it does not become too much overhead,
I show other people. That reordering sounds selfish written down. In practice it
has worked better for everyone than the martyrdom did. My PR count is higher. My
synchronous meetings are down. The work has my name on it now.

I used to get a real hit of satisfaction from unblocking someone while my own
task sat untouched. That feeling is seductive and it is a trap, because it pays
you in the currency of being needed rather than the currency of progress. Now I
put my own oxygen mask on first. The airline instruction is not a metaphor for
selfishness; it is the observation that you cannot help anyone if you have
passed out.

## Patching versus fixing

The biggest lesson underneath all of this is about systems, not personalities.
The longer I thought about _Being Glue_, the more I realized it describes the
same thing as a high-maintenance system: something that only keeps working
because a person keeps manually intervening to hold it together. The article
catalogs the human version (onboarding, unblocking, documentation, all the work
that keeps a human system effective), but a lot of those pain points now have
real solutions. Onboarding can run through an agent. Coordination can be
automated. The glue does not have to be a person.

When I was a kid I had an uncle with an old car. He never used glue to keep it
going, but he had something better: he cut up old bicycle tire tubes into rubber
bands and used them for everything. Binding two pieces of pipe together,
stopping a rattling panel, holding things in place. Rubber is, technically, a
kind of glue (a stretchy patch you apply to a problem so it holds for a while
longer). I always thought about how unnecessary a lot of those patches were. It
is the same instinct as a slow leak in a tire: you keep pumping air into it
every morning instead of taking it apart and fixing the puncture once. Now,
whenever I face a system that needs constant maintenance, that is the image in
my head. Stop pumping air. Take it apart. Repair the underlying cause, not the
symptom that keeps resurfacing.

On-call is where this bites hardest, and I would extend the _Being Glue_ idea
straight into it. In my mind, on-call is the exception, not the rule. It is a
gap where you did not design the system to heal itself. Yes, sometimes you carry
the pager, and yes, sometimes you get called, but the threshold for waking a
human up (or interrupting their weekend) has to be very, very high. Any
situation that requires a hero to save the day is a situation where a human is
being used as glue: the system does not work without that person standing in the
seam. That is not a system that needs more glue. That is a system that needs
fixing. Throwing humans at a problem that should not require humans is the core
mistake.

Reilly's framing is that you should be deliberate about which glue you pick up
and make sure your visible, attributable work does not starve. The extension I
would add is that the glue you are tempted to apply is usually a signal that
something underneath is broken, and the higher-value move is to fix it at the
root rather than to keep patching the seam with your own time. So when something
breaks, fix it for good and add a monitor that catches the same deviation next
time, instead of patching it and waiting for it to break again. Self-healing
first; humans only for the genuinely novel failure.

The way to keep yourself honest is to measure where your time is actually going.
Track it, and clearly see how much of it is glue work. Some glue will always be
needed (you want awareness across the whole team, and a person is often the
right carrier for that), and as long as it stays minimal and is shared evenly,
that is fine. The problem is only when the glue is one overloaded person, or
when we keep using people where a self-healing system belongs.

So this is not an argument for never helping. It is an argument for minimizing
the cases where a human has to be the glue at all. Put your own oxygen mask on
first (you cannot help anyone if you have passed out), automate or hand off the
recurring patches, and reserve human attention for the rare, novel break that
genuinely needs a person. Build systems that heal themselves and monitor
themselves, repair them at the source when they fail, and let people do real
work instead of being the glue holding a patch in place.

---

_This post is a reflection on Tanya Reilly's
[Being Glue](https://www.noidea.dog/glue). The systems-over-heroics theme also
runs through
[Leverage and the Stairs You Build](/blog/leverage-and-the-stairs-you-build/),
and the team-ownership counterpart is in
[Team Identity Ownership](/blog/team-identity-ownership/)._
