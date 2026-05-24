+++
title = "Language Choice in the LLM Era"
date = "2026-05-24"
description = "Reflecting on my journey through programming languages—from C/C++ as a barrier to Python, Swift, and TypeScript—and how LLMs change the equation for language choice in modern development."
template = "blog-post.html"
categories = ["development", "ai", "languages"]
tags = ["rust", "python", "typescript", "go", "csharp", "swift", "llm", "ai-development"]
+++

I started programming in 2014, but I could have started much earlier. C and C++ blocked me. The syntax was esoteric, the learning curve steep, and the error messages felt like they were written in a different language. It wasn't that I lacked interest in programming—it was that the most visible languages at the time felt deliberately inaccessible.

Then I found Python. Python was the language that got me excited about learning to code. It read like pseudocode. The barrier to entry was low enough that I could start building things immediately. This was around the time when people were still calling it "big data" (before the AI craze took over, though deep learning and supervised learning were already in motion).

## The Accidental Winners

JavaScript won on the browser by accident. It was never meant to be the lingua franca of the web. It was a 10-day prototype that happened to ship at the right time in the right place. No committee designed JavaScript to be universal—it became universal by being the only option.

That accident shaped decades of web development. We built frameworks on top of frameworks to make JavaScript bearable, then usable, then powerful. The language's flaws became features we learned to work around.

## The Language Fanatic Phase

After Python, I learned Swift. Apple had just released it as the new language for their ecosystem, and it was beautiful. I was hooked. Then I formally learned Java at a nearby college (and again during my master's degree).

When I started working at Microsoft, I worked with C# and C++ 11. Rust had come out in 2010, and I knew about it then, but the language seemed very esoteric. After learning C++ and Swift, Rust didn't seem that esoteric anymore—but it was still a niche language.

At some point during my work at Microsoft, I learned Go, and I really liked it. Swift had taken a lot of ideas from Go (the `defer` keyword, the `func` naming convention, the overall simplicity). While I took a couple of classes in JavaScript, it never really caught my attention. The language that caught my attention was TypeScript. I like TypeScript a lot, and if I ever need to write anything for the web, you bet I'll use TypeScript.

Most of my professional career so far has been C#, with a little bit of Go, a little bit of Python in some applications here and there, a little bit of C++ in some old apps I needed to touch. More recently (during a break), I wrote a couple of Rust applications for some internal tools I use for work.

I say all of that to say: I do consider myself a language fanatic. Or at least I was. When I was learning Python, Python was the only thing I could think of. How do I find excuses to use Python? When I learned Swift, I wanted to write everything in Swift. I went through that process with Go as well. I have been through that mental model.

I don't feel like I'm like that anymore. That phase has faded. I don't tend to say "let's write everything in X language." I've written plenty of PowerShell and Bash, but for some reason, I don't consider those to be languages (same with XML or HTML—it's not a language in my book).

## The Decision Matrix

Now that we're in this world of LLM-driven development, I do wonder about the next language that we would use—the next language that could address many of the issues. Rust does come to mind. Rust does come to the rescue in many different areas. I do feel that Rust checks many of the boxes.

No, I'm not going to port anything to Rust that's already written in a different language. I don't think that's pragmatic. But I do think new things—new things that don't have dependencies or existing infrastructure—should probably, at the very least, not be written in a dynamic language. It should be a static language. That's my high-level thinking.

Here's my decision matrix when I need to choose a language, and it has to do with the use case. I'm going to exclude PowerShell and Bash from this (they're in their own category).

**For frontend (things users interact with):**

There are a couple of different environments: the web, mobile (Android vs iOS), desktop (Windows, macOS, or Linux).

- **Web:** TypeScript
- **Mobile Android:** Kotlin
- **Mobile iOS:** Swift
- **Desktop Windows:** C#
- **Desktop macOS:** Swift
- **Desktop Linux:** Rust

That's for front-facing stuff—things that people have to interact with.

**For the server:**

The server is a different problem. There are different methodologies, different things that certain languages do really well, and it depends on the use case.

If I have to stand up a server that needs to serve REST endpoints, talk to databases, and support a big team that needs to be onboarded—I think you cannot go wrong with an ASP.NET Core (C#-based) solution. The same thing could be said for Go. You can be very successful with a Go-based backend.

I don't think Python is the right solution for this. I know there are successful projects that use Python for the server. I just don't feel that Python is the right solution as of today.

For utilities that need to run on servers—C#, Python, and Go are probably good solutions.

As you go down the stack and you have to run on smaller, more constrained environments, Rust comes into play again. Anytime you would have used C/C++, Rust is a good replacement. It doesn't make sense to me to use Go or C# when you were supposed to use C++, because languages like Go and C# introduce a garbage collector.

We can see this very well in the world of game engines. The Godot game engine is written in C++, but all of the client code (what people use for scripting) is usually in different languages. I've seen how the garbage collector's global stop or global pause can introduce issues for end users.

In AI, every time there is an issue with performance or control, we tend to use a combination of C++ and Python. C++ for the performance-critical parts, Python for the glue and the high-level logic.

## The LLM Era Changes the Equation

Those are all my thoughts at a high level. I think there is the right tool for the job. I think there are always constraints and trade-offs.

But the equation does change when it comes to AI. LLMs are able to write Rust just as easily as they can write PowerShell. I covered this extensively in my [previous article about Rust and scripting languages](/blog/ai-tools-journey-opus-4-5/), where I discussed how Claude Opus 4.5 made writing Rust feasible for me in ways it wasn't before.

The question now comes down to: What are the capabilities of the language? What area do you need to address? Deployment of the code becomes a big issue. You need to have a very well-understood deployment story.

I don't think I'm picky when it comes to languages. I just probably don't see myself writing C++, C, or JavaScript unless I have to. And right now, I don't feel like I have to, given that we have so many other languages.

I don't think I have to write JavaScript anymore. The languages that probably are most popular—C, C++, JavaScript—those languages are probably ones we don't need to write anymore. They could be targets. You write TypeScript, and then that gives you JavaScript as a compiled output. That's fine. I'll probably do something like that.

## Summary

There is the right language for the right problem. I am very excited about Mojo, which is meant to bridge the gap between Python and Rust. As of this writing, it's not yet GA, so it's not something I could even consider. But even then, in a world where we have Mojo (meant for accelerators), I will probably still choose Rust, Go, C#, or another compile-time language for most cases.

In the LLM era, the barriers that once made certain languages intimidating have lowered significantly. The C and C++ that once blocked me from programming are still languages I avoid—but now by choice, not necessity. The esoteric syntax that kept me away in 2014 is no longer the barrier it once was.

What matters now isn't just syntax or learning curve—it's the entire ecosystem: tooling, deployment, compile-time guarantees, and how well the language fits the problem. LLMs can write in any language, but that doesn't mean all languages are equally good choices. Choose the language that gives you the guarantees you need, the deployment story you can live with, and the ecosystem that supports the problem you're solving.

---

*For more on my experience with Rust development in the LLM era, see [My AI Tools Journey Since Claude Opus 4.5](/blog/ai-tools-journey-opus-4-5/).*
