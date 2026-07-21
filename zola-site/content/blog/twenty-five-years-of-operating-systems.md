+++
title = "25 Years of Operating Systems: Windows, macOS, and Back Again"
date = "2026-07-04"
description = "A personal retrospective spanning 25 years of operating systems, from Windows 98, 2000, and XP through a decade of macOS to a return to Windows 10 and 11, and a look at where a fully Linux development environment might fit next."
template = "blog-post.html"
[taxonomies]
categories = ["Field Notes"]
tags = ["windows", "macos", "linux", "retrospective", "wsl", "operating-systems"]
[extra]
editorial_track = "field-notes"
+++

Looking back across 25 years, the operating systems I have lived on tell a story
in three acts: a first five years anchored in Windows, a full decade on macOS
and only macOS, and then a return to Windows that is still going strong. Each
transition taught me something, and each one was less about chasing the newest
release and more about picking the tool that got out of my way.

## The First Five Years: Windows 98, 2000, and XP

My first operating system was
[Windows 98](https://en.wikipedia.org/wiki/Windows_98), and not because it was
the current release. It was simply the easiest one to get so I could load it
onto old computers. That was the appeal: I could take a machine apart, put it
back together, reset it to Windows 98, and everything was good again. It was a
forgiving starting point for someone learning the hardware alongside the
software.

[Windows ME](https://en.wikipedia.org/wiki/Windows_Me) came next, but it was not
stable. At the same time
[Windows 2000](https://en.wikipedia.org/wiki/Windows_2000) was becoming
available, targeted mostly at businesses and schools because it was built on a
different kernel (the [Windows NT](https://en.wikipedia.org/wiki/Windows_NT)
line rather than the consumer DOS-based line). I remember explicitly that many
of my friends skipped ME with me and went directly to Windows 2000. My last
Windows release of this era was
[Windows XP](https://en.wikipedia.org/wiki/Windows_XP), which was a great
operating system. Around that time I switched fully to a Mac, so I am glad to
say I never had to use
[Windows Vista](https://en.wikipedia.org/wiki/Windows_Vista). I skipped every
version until [Windows 10](https://en.wikipedia.org/wiki/Windows_10), jumping
straight from XP to 10 when I came back to Windows for work.

## A Decade of macOS and Only macOS

I used a Mac professionally for about ten years, and so far it has been one of
the most stable operating systems I have used for that length of time. Most of
my time was on
[Intel](https://en.wikipedia.org/wiki/Apple%E2%80%93Intel_architecture) Macs,
since that transition happened during this period, but as I moved onto different
projects I also dealt with [PowerPC](https://en.wikipedia.org/wiki/PowerPC)
machines running [Mac OS](https://en.wikipedia.org/wiki/MacOS). Honestly there
was not a lot of difference. Certain apps did not work on PowerPC, but the
transition was mostly flawless.

Most of that decade I used a Mac for video editing (I was a video editor for
about ten years). At the time we used
[Final Cut](https://en.wikipedia.org/wiki/Final_Cut_Pro), also made by Apple,
and yes there were other tools in the mix (Adobe products, and at some point a
transition to
[Avid Media Composer](https://en.wikipedia.org/wiki/Avid_Media_Composer)). For
the most part macOS was solid. I had it as a laptop, as a desktop for work, and
as a personal computer, and it ran great across all of them. Even my server at
the time was macOS based: an [Xserve](https://en.wikipedia.org/wiki/Xserve) that
held all the RAID storage. For a decade the Mac was simply everything.

Servers were making their own trip from rooms full of machines to the cloud. My
first real introduction to them was at work, when the company started hosting a
room full of them. I never had a server of my own back then, but that was the
first time I understood the idea of a machine that did things for me, running in
a work setting rather than under my desk. Around the same time, cloud platforms
like [AWS](https://en.wikipedia.org/wiki/Amazon_Web_Services) and
[Azure](https://en.wikipedia.org/wiki/Microsoft_Azure) were becoming relevant,
and suddenly you could run your code on someone else's infrastructure. I also
started deploying websites on hosts like
[GoDaddy](https://en.wikipedia.org/wiki/GoDaddy) using
[PHP](https://en.wikipedia.org/wiki/PHP) and
[WordPress](https://en.wikipedia.org/wiki/WordPress). Almost all of it was
Linux-based technology, similar to what
[Facebook](https://en.wikipedia.org/wiki/Facebook) was built on.

The shift really happened as the web exploded with mobile users. The back end
became more and more important, and it became something users could deploy
themselves. That is around the time I moved into becoming a developer, and it
lines up with my video-editing years in an interesting way. Back then there was
no way to stream that footage across the wire. We had to be in the same room as
the servers holding the data, especially once we moved into HD video and the
files got even bigger. You could not edit remotely the way you can now. Writing
and deploying code, on the other hand, was a natural fit for remote work (you
deploy your website remotely, from anywhere), which made it a perfect time for
AWS and Azure to take off. Both of those were mostly Linux-centric, even though
Windows Azure did support Windows.

By contrast, I never deployed into a macOS server world in the same way. When we
did have the option of macOS servers, it was mainly to serve files over the wire
with something like
[Final Cut Server](https://en.wikipedia.org/wiki/Final_Cut_Server). The internet
also was not as fast as it is today. Now I can connect remotely to a machine
that sits next to the data and get 1080p at a high frame rate on my screen, so I
could technically edit video remotely, which was simply not feasible back then.
The tooling and the server technology grew up together. These days, even when I
connect to a server I do not necessarily need a graphical interface. A command
line is enough to change the settings, and dashboards are helpful for visibility
into the full system, but they are really just another management entry point. I
know Windows servers exist, but I never used Windows that way. I was never a
Windows NT admin.

## Coming Back to Windows

When I switched to Windows 10, I was pleasantly surprised by how stable it was
compared to Windows XP (which was itself a stable release). I got that same Mac
feeling from Windows 10 and
[Windows 11](https://en.wikipedia.org/wiki/Windows_11), where there is no abrupt
change from version to version. Most versions are largely compatible with each
other, so I honestly do not have a lot of complaints.

By now I have been back on Windows for about a decade. Even while using Windows
development machines, most of my target machines have always been
[Linux](https://en.wikipedia.org/wiki/Linux): develop on Windows, deploy on
Linux. [WSL](https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux) has made
it much easier to stay inside the Windows environment while still working
against Linux, which has kept that split comfortable.

## What the Next Decade Might Look Like

I doubt I would move 100% to something like Linux for development, but I have
noticed lately that my usage has become mostly terminal based, driven by agents.
Sure, I have a couple of chat applications, email, and a few things that are
inherently Windows. But I do not do development in those, so there is a strong
case that I could start using a full Linux development environment where I edit
the code and deploy in the same place. I wonder about an environment where I run
my agents entirely inside Linux. I am not sure that is where things land, but
the pull is real.

Twenty-five years, three acts: the first five years on Windows 98, 2000, and XP;
a decade of macOS and only macOS; and a return to Windows that is still going
well. I am not sure what the next decade looks like, but there is a strong case
for a fully Linux development environment, or at the very least a remote one.
Whichever way it goes, it fits the same pattern I traced in
[my history of mobile computing](/blog/palm-sony-android-iphone-blackberry/):
the device and the operating system matter less over time than the work and the
services they connect me to.
