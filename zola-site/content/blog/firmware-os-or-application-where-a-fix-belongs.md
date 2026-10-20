+++
title = "Firmware, OS, or Application: Where a Fix Belongs"
date = "2026-11-08"
description = "Every fix or feature has to land somewhere in the stack: the firmware, the OS (host, image, or container), the application, or the client on the other end. The application is usually the cheapest place, but when the difference lives in the hardware, firmware is often the right place, and firmware is only software that runs lower and has to be held to a higher bar."
template = "blog-post.html"
[taxonomies]
categories = ["Software Engineering"]
tags = ["firmware", "operating-systems", "bare-metal", "keyboards", "abi-stability", "open-hardware", "fearless"]
[extra]
scheduled = true
editorial_track = "software-engineering"
related = ["fearless-engineering", "keyboard-layout-mapper-evolution", "2026-ten-years-later-ipad-pro-in-the-drawer", "language-choice-in-the-llm-era"]
+++

The keyboard I type on every day runs firmware I compile myself. When I want a
new layer, a different hold-tap timing, or a key that does something the
manufacturer never imagined, I do not open a settings app. I change a line in a
ZMK config, build, and flash. I wrote about keeping those layouts in sync across
keyboards in
[the keyboard layout mapper post](/blog/keyboard-layout-mapper-evolution/). I
recently bought a music keyboard for the same reason: I can flash it myself.

That habit followed me to work. I have been working close to bare metal for a
while now, and every time a bug or a feature request shows up, the first real
question is not how to fix it. It is where. There are a small number of places a
change can go, and picking the wrong one costs more than writing the wrong code.

## Three layers, and a fourth one you do not own

On the server side the stack has three layers I can reach. The firmware sits at
the bottom (BIOS, BMC, device firmware). Above it is the OS, which for me really
means several things: the host kernel, the distribution or custom Linux image,
the way we orchestrate it, and the container image the work runs in. On top is
the application, the code that does the thing the machine was bought for.

The keyboard has the same three layers. If the keyboard is open, the feature
goes into the firmware. If the keyboard is off the shelf, I usually cannot touch
its firmware, so the fix moves up into the OS: a program that sits there,
listens to keystrokes, and rewrites them. Karabiner-Elements does this on macOS,
AutoHotkey and the PowerToys Keyboard Manager do it on Windows, and kanata runs
across all three. And if neither of those is available, the application can
still define its own shortcuts, as long as they do not collide with the global
ones the OS reserves for itself. Firmware, OS, application. A mouse, an
appliance, and a rack of servers all decompose the same way.

The fourth place is the client on the other end. A server talks to a phone, a
browser, a laptop, or a terminal, and that client has its own stack running in
reverse from my point of view: client application, then client OS, then client
firmware. The difference is ownership. I cannot change the firmware on an Apple
or Google device, and I have very little say in how a browser behaves. Most
users never see that client firmware at all. Sometimes the client is a laptop
where I do control everything, and there the OS layer opens up again (security
tools work this way today, embedding themselves into the OS so they can watch
for worms, trojans, and viruses). But usually the client is the layer I have to
work around, not the one I get to change.

## The cheapest layer is usually the application

My default rule is simple: if the change can go into the application, put it
there. Even when it is a little more costly in code, keeping the firmware and
the OS identical across the whole fleet makes everything else easier. Fewer
variants to test, fewer images to track, fewer surprises when a machine is moved
from one pool to another.

When I find a bug that is well understood and that I can work around, I go up
the stack first. If the application can absorb it, that is the cheap fix. If
not, I look one layer down: can a package in the OS be updated, can the
container image change, can orchestration apply a small software patch that the
machines download and pick up? That is still cheap. Only when none of those work
do I go to the firmware.

The OS layer gives more room than people expect, as long as the thing you need
has real support behind it. Gaming shows both sides of that. Windows gaming
works well for most people because the support is already there. Linux gaming
had very little support for a long time, and the thing that changed it was a
company the size of Valve deciding to carry the work. Customizing the OS is easy
when someone is already maintaining the path you are on, and expensive when you
are the only one.

Apple solved part of this problem in a way I admire. On iOS, apps do not
statically link the system libraries the way most server software does. The code
I write for an app is a thin layer that calls into frameworks the OS provides,
dynamically, at launch. Because Swift has had a stable ABI on Apple platforms
since Swift 5, the OS knows exactly what shape the calls will arrive in, so it
is free to swap the library underneath and route each call to whatever
implementation it now supports. Compile once, and the OS carries the long-term
support. That is a big part of why a lot of older apps (games included) keep
running on newer phones. The application stays fixed while the layer beneath it
moves, which is exactly the trade I want on servers.

## When firmware is the right place

The default flips when the difference lives in the hardware. If I am running the
same software across machines from different OEMs and one of them misbehaves, I
can paper over it with a conditional in the application, a special image, or a
per-vendor patch in the OS. Each of those makes the layer above less uniform. Or
the firmware on the odd machine can change so that it behaves like the rest, and
the software above it stays the same everywhere. Given that choice, I would
rather go to the firmware. The goal of the whole exercise is to write the
software once; the layer to fix is the one where the variation comes from.

That is not always possible. Fleets are heterogeneous, and the more esoteric the
hardware, the less likely a firmware change is on the table. This is why I am
excited about approaches like Mojo, which I mentioned in
[the language choice post](/blog/language-choice-in-the-llm-era/): one language
that understands the differences between accelerators and produces something
that runs across them. When you cannot make the hardware uniform, push the
handling of its differences into a tool built for that job rather than into
every application.

Getting a firmware change also depends on leverage. A consumer asking a
manufacturer for custom firmware gets nowhere. A company with a lot of business
with that manufacturer can ask, and I happen to work at a company that does. So
"is this a firmware change?" is a real option on the table for us, not a
hypothetical. And when you are the one building the servers and you control the
firmware yourself, deploying a firmware update is often cheaper than every
alternative stacked above it.

None of this means running a forked OS with a pile of local patches. I want a
stable OS that stays close to upstream. When a machine misbehaves on one OEM,
that is the case for a firmware update. And firmware updates are getting more
frequent anyway. Between quality and security, we are now looking at updating
firmware on a much shorter cycle than before, because a lot can be improved at
that level, and a lot of security features belong there.

## Firmware is only software that runs lower

The reason I am not afraid of flashing firmware is probably the keyboards. When
you have flashed something a hundred times, recovered from a bad build, and
flashed again, firmware stops feeling like a sealed box and starts feeling like
what it is: software that runs at a lower level. Changes there carry higher
stakes, because a mistake can take the device down rather than one feature, so
firmware needs to be held to a higher bar for reliability. But it is not a
different kind of thing. That is the same argument I made in
[Fearless Engineering](/blog/fearless-engineering/): the confidence comes from
being able to recover, not from being sure nothing will break.

Firmware should also be the thing that lets hardware live longer than anyone
expected. I have several iPads sitting around (one of them is the subject of
[the post about the iPad in my drawer](/blog/2026-ten-years-later-ipad-pro-in-the-drawer/)).
They are perfectly good hardware. If I could flash new firmware onto them, they
could become Linux thin clients instead of sitting there. The same is true for
phones. Hardware is good enough now that there is no reason to replace a device
just because the vendor stopped supporting it. A firmware update could turn it
into something narrower (a device that only makes calls, or only shows a
display) and keep it useful for years.

I would like to see hardware move in that direction more broadly. Graphics and
AI acceleration are controlled by a couple of vendors today, and I would rather
have open hardware where people can run their own firmware and make small
changes for their own use cases. We are not there yet. But with agents taking on
more of the execution, the cost of working at the firmware layer is dropping,
and that makes it more reasonable to invest in owning that layer instead of
treating it as untouchable.

I know plenty of engineers who take the opposite position: stay away from
firmware and find a way to handle everything higher in the stack. I understand
why, and I may change my mind later. For now, my view is that firmware updates
should be part of normal software updates, done often and recovered from easily,
not a thing you receive once at the factory and never touch again. Start at the
application because it is cheapest. Go to the OS when the application cannot
hold it. And when the difference lives in the hardware and the firmware is yours
to change, go all the way down and fix it there.
