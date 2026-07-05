+++
title = "My Swift Journey: Why I Love It but Can't Use It at Work"
date = "2026-07-05"
description = "Swift might be my favorite language, striking a rare balance between low-level and high-level features, yet I've never been able to use it professionally. This is why, and what it takes for a language to break out of its home ecosystem."
template = "blog-post.html"
categories = ["development", "languages", "personal"]
tags = ["swift", "rust", "csharp", "go", "apple", "languages", "open-source"]
+++

Swift was the second language I ever learned, right after Python. Apple had just released it as the new language for their ecosystem, and it was beautiful. I wrote about that moment [back in 2014](/blog/apple-swift-apps-everywhere-prediction/), when I predicted Swift would become the backbone of Apple's connected app frameworks. More than a decade later, I still think Swift is one of the best-designed languages I have ever used. It strikes a very, very good balance between low-level and high-level features. It reads almost like a scripting language, but it compiles down to something fast, and it made the correct choice to stay close to C++ when it comes to compatibility and interoperability. And yet, in all these years, I have never once been able to use it professionally. This post is my attempt to explain that gap, because it says more about how languages spread than it does about Swift itself.

## A Language Can Be Great and Still Be Trapped

Apple did almost everything right with Swift on the technical side. They made it the required language for the Apple ecosystem and then pushed it everywhere: macOS, iOS, watchOS, and every system in between. They wired it into the low-level pieces too, from the security chips to Metal, the parts of the platform where you would normally expect nothing but C and C++. If you measure Swift by how deeply it is embedded inside one company's stack, it is a runaway success.

The trouble is that "one company's stack" is exactly the boundary Swift has never managed to cross. It has had a really, really hard time becoming popular outside of macOS and iOS. And most of the professional world does not want to spend time learning a language that is only used inside a single company. That is the quiet rule that governs language adoption, and it is easy to underestimate. Engineers invest their careers in tools they can carry between jobs. A language perceived as belonging to one vendor's platform feels like a career dead end, no matter how elegant it is.

This is the same wall C# ran into for years. C# is a genuinely good language, but it struggled to become popular outside the Windows ecosystem because for a long time it was seen as a Microsoft-only thing. (I still think that reputation lingers even now that ASP.NET Core runs happily on Linux and macOS, something I get into in [Language Choice in the LLM Era](/blog/language-choice-in-the-llm-era/).) What makes the contrast interesting is Go. Go was created inside Google, arguably just as much a "company language" as Swift or C#, and yet it is enormously popular outside of Google. The difference was never purely technical. Go was pitched from day one as a general-purpose language for servers and tooling that anyone could pick up, and it never asked you to buy into a single vendor's hardware to get value out of it.

## Adoption Needs Buy-In From the Top

If a great language is not enough, what actually moves a new language into a workplace? In my experience, it takes buy-in from the higher-ups. A language does not spread through a company because a few engineers love it. It spreads when leadership decides it is worth the switching cost and pushes it deliberately.

Rust is the clearest example I can point to right now. Rust is popular today even in places that would not necessarily have wanted to adopt it, and that did not happen by accident. Within Microsoft, for instance, you have leadership publicly pushing for Rust to be used instead of C++ for new systems work. That is the type of buy-in you need to move to a new language in a real work setting. Once the people who own the roadmap say "we are doing this," the tooling, the hiring, the training, and the internal libraries all follow. Without that top-down commitment, even a superior language stays a hobby project.

Swift never got that outside of Apple, and Apple had little reason to fight for it beyond their own platforms. So Swift ended up in a strange position: technically ahead of many of its peers, but organizationally stranded. I genuinely think Swift is better than Go and C# for a wide range of problems. It is safer than C++, more expressive than Go, and closer to the metal than C#. None of that mattered, because the decision to adopt a language at work is rarely made on technical merit alone.

## The Open Source Chance Swift Missed

There was a path out of this trap, and it ran through open source. The way a company language earns credibility outside its home turf is by powering serious, visible projects that have nothing to do with the original vendor. That is how you convince skeptical engineers that a language has a life of its own.

Swift got a real shot at this with Ladybird, the new web browser being built from scratch. A browser is exactly the kind of ambitious, low-level, high-visibility open source project that could have showcased everything Swift does well, its balance of performance and safety, its C++ interoperability, its modern design. If Swift had become the language of a from-scratch browser, it would have done more for Swift's reputation in the open source community than a decade of Apple marketing. But the project ultimately went with Rust instead, running into capability and tooling gaps along the way (I touched on this in [Language Choice in the LLM Era](/blog/language-choice-in-the-llm-era/)). That was a real loss for Swift, and it is the kind of loss that compounds. Every marquee project that picks Rust or Go over Swift makes the next team a little more likely to do the same.

So here I am, a self-described language fanatic (or at least I used to be, as I confessed in [Language Choice in the LLM Era](/blog/language-choice-in-the-llm-era/)), holding onto a favorite language I have never been paid to write. Most of my professional career has been C#, Go, Python, C++, and Rust, and more recently I have leaned into [Rust for internal tooling](/blog/ai-tools-journey-opus-4-5/). Swift deserved to be on that list. It is not that Swift failed as a language. It is that being a great language was never the thing that mattered. What matters is ecosystem, community alignment, and someone with authority willing to bet on you. Swift had the design; it never got the bet.
