+++
title = "Two Left Socks"
date = "2026-12-08"
draft = true
description = "My spouse recently ended up with two left toe socks and no way to wear them, because each one had lost its only valid partner. My drawer, and now our kids' drawers, cannot have that problem: the kids and I wear one style of sock for every occasion, so any two make a pair. The difference is a design choice that shows up far outside the laundry basket. Do not build systems that need a specific matched pair when a part that fits anywhere would do."
template = "blog-post.html"
[taxonomies]
categories = ["Engineering Systems"]
tags = ["interchangeability", "design", "simplicity", "decision-fatigue", "systems-thinking", "redundancy"]
[extra]
editorial_track = "engineering-systems"
+++

Our laundry recently produced two left socks. Both belonged to my spouse, both
were toe socks (the kind knit with a separate pocket for each toe), and each one
had a different design. Somewhere between the hamper, the washer, and the dryer,
their right-foot partners went missing. What was left was two perfectly good
socks that could not be worn together. A left toe sock goes on the left foot the
same way a left shoe does. There is no turning it around, and no borrowing
another left sock to stand in for the missing right one.

My half of the drawer cannot get into that state, and that is on purpose.

## How My Drawer Got Simple

My family owns every kind of sock. Short ones, long ones, thin ones, thick ones,
compression socks, soccer socks, socks that have started to pill. I used to have
a version of most of those myself: dress socks, cotton socks, long socks for
different occasions. Each morning that meant a small search through the drawer
for two socks that actually matched, and each laundry day meant sorting them
back into pairs.

A few years ago I simplified. I picked one sock (a black ankle sock), bought
enough of them, and let the rest go. The idea came from the way Barack Obama
described his wardrobe to Michael Lewis in a 2012 Vanity Fair profile: he wore
only gray or blue suits because he was "trying to pare down decisions," so he
could spend his deciding on things that mattered more. I did not need two
colors. I went all in on one.

The result is that my socks are interchangeable. Any sock goes on either foot,
and any two socks make a pair. There is no sorting step after laundry, no search
step in the morning, and no such thing as a missing partner. If one sock gets a
hole, I throw away one sock. If the dryer eats one, the drawer has one fewer
sock and nothing else changes.

The kids have since joined me. They now follow the same rule I do: one style of
sock for school, sports, and everything else. Their socks used to be one more
pile to sort after every wash. Now they work the same way mine do, and the
laundry basket has one fewer kind of sock to match. It is a simple life, and it
got simpler with each person who moved to it.

## What a Matched Pair Costs

Her drawer works differently, and it is worth being precise about why, because
toe socks are not a mistake. People wear them for real reasons: fit, comfort,
keeping toes separated, and, for her, the designs she likes. But every one of
those socks carries two constraints at once. It is **handed** (it only fits one
foot) and it is **unique** (only one other sock in the house matches its
design). Put together, that means each sock has exactly one valid partner in the
whole drawer.

That one fact changes what a loss does:

| Drawer                     | Valid partners per sock | Losing one sock costs | Leftover after losing one |
| -------------------------- | ----------------------- | --------------------- | ------------------------- |
| Identical, unhanded (mine) | Every other sock        | One sock              | Nothing stranded          |
| Unique, handed (hers)      | Exactly one             | A whole pair          | One orphan sock           |

In my drawer, losses are linear: lose three socks and I have three fewer socks.
In hers, each loss also strands a survivor. Lose one sock from each of two
different pairs and you are holding two orphans, and if both orphans happen to
be lefts, they cannot even be pressed into service as an odd pair. That is how
we ended up with two left socks: two losses produced zero wearable pairs and two
socks that still take up space in the drawer.

The cost also shows up before anything is lost. Every matched pair has to be
found again after each wash, so sorting is work proportional to the number of
socks. In a drawer of identical socks, that work is zero.

## Design for the Spare That Fits

The principle underneath the laundry is one engineers have relearned many times:
**when a part must match one specific partner, every loss costs double and every
repair needs that exact partner. When a part fits anywhere, losses cost only
themselves and any spare is a repair.**

Manufacturing learned it with interchangeable parts. Before standardized parts,
a musket was hand-fitted, and a broken lock could only be repaired by a
craftsman fitting a new piece to that particular gun. Once parts were made to a
common specification, a field repair meant grabbing any spare from the box.

Connectors learned it more recently. The older USB-A plug (USB stands for
Universal Serial Bus) only goes in one way, and most people know the ritual of
trying it, flipping it, and trying again. USB-C is symmetric: it has no left or
right, and it goes in either way on the first try. The cable gave up nothing to
lose its orientation.

Software learned it with servers. A hand-configured machine that only works with
one particular database, holding settings nobody wrote down, is a toe sock: when
it fails, you need that one partner back, and there is no spare that fits. A
stateless service behind a load balancer is my sock drawer. Any instance can
handle any request, a failed instance costs one instance, and the fix is to
start another one from the same image.

The same check works on almost any design: **if I lose one of these, what else
stops working, and can any spare replace it?** If losing one piece strands
another, the design has built a matched pair. Sometimes that is the right call.
Shoes have to be handed because feet are. A primary database and its replica may
need to know about each other. Uniqueness can be the whole point, as it is with
her socks. But the matched pair should be a cost someone chose to pay for a
specific benefit, not the default nobody questioned.

_Two left socks are what a matched-pair design looks like when it fails: losses
that cost double, and leftovers that cannot be used. My drawer of identical
black socks is not better taste. It is a system with no pairs to break, so
nothing in it can be stranded. The same question applies to the systems I build
at work, and it connects to the habit in
[Minimize Humans as Glue](/blog/minimize-humans-as-glue/) of fixing the design
instead of becoming the person who keeps it running: before adding a part that
needs one specific partner, ask whether a part that fits anywhere would do. Most
of the time it would, and then the dryer can eat whatever it wants._
