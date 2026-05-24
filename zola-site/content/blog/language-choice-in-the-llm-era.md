+++
title = "Language Choice in the LLM Era"
date = "2026-05-24"
description = "A practical guide to choosing programming languages for frontend, CLI, and server development with decision matrices that account for modern LLM-assisted development."
template = "blog-post.html"
categories = ["development", "ai", "languages"]
tags = ["rust", "python", "typescript", "go", "csharp", "swift", "llm", "ai-development"]
+++

I started programming in 2014, but I could have started much earlier. C and C++ were barriers for me. The syntax was esoteric, the learning curve steep, and the error messages felt like they were written in a different language. It wasn't that I lacked interest in programming (it was that the most visible languages at the time felt deliberately inaccessible). Then I found Python. Python was the language that got me excited about learning to code. It read like pseudocode. The barrier to entry was low enough that I could start building things immediately. This was around the time when people were still calling it "big data" (before the AI craze took over, though deep learning and supervised learning were already in motion).

JavaScript won on the browser by accident. It was never meant to be the lingua franca of the web. It was a 10-day prototype that happened to ship at the right time in the right place. No committee designed JavaScript to be universal (it became universal by being the only option). That accident shaped decades of web development. We built frameworks on top of frameworks to make JavaScript bearable, then usable, then powerful. The language's flaws became features we learned to work around. While I took a couple of classes in JavaScript, it never really caught my attention. The language that caught my attention was TypeScript. I like TypeScript a lot, and if I ever need to write anything for the web, you bet I'll use TypeScript.

After Python, I learned Swift. Apple had just released it as the new language for their ecosystem, and it was beautiful. I was hooked. Then I formally learned Java at a nearby college (and again during my master's degree). When I started my job at the time, I worked with C# and C++ 11. Rust had come out in 2010, and I knew about it then, but the language seemed very esoteric. After learning C++ and Swift, Rust didn't seem that esoteric anymore (but it was still a niche language). At some point during that job, I learned Go, and I really liked it. Swift had taken a lot of ideas from Go (the `defer` keyword, the `func` naming convention, the overall simplicity).

Most of my professional career so far has been C#, Go, Python, C++, and Rust. More recently (during a break), I wrote a couple of Rust applications for some internal tools I use for work. I say all of that to say: I do consider myself a language fanatic. Or at least I was. When I was learning Python, Python was the only thing I could think of. How do I find excuses to use Python? When I learned Swift, I wanted to write everything in Swift. I went through that process with Go as well. I have been through that mental model. I don't feel like I'm like that anymore. That phase has faded. I don't tend to say "let's write everything in X language." I've written plenty of domain-specific languages (DSLs) like PowerShell and Bash for scripting, SQL-like languages for data access, and even [XML-based configurations for calling C++ modules](https://github.com/nasa/fprime). You can get a lot done with DSLs. I've also seen plenty of cases where languages are shoehorned into JSON for configuration (those are DSLs too).

## The Decision Matrix

Now that we're in this world of LLM-driven development, the language choice landscape has shifted. What matters isn't whether I personally find a language elegant (it's whether the language solves the problem at hand with the right trade-offs). Here's my decision matrix, broken down by deployment target.

**Frontend (Visual UI for end users):**

- **Web:** TypeScript
- **Mobile Android:** Kotlin (the modern replacement for Java, though I wouldn't rewrite existing Java to Kotlin)
- **Mobile iOS:** Swift
- **Desktop Windows:** C#
- **Desktop macOS:** Swift
- **Desktop Linux:** Rust

**CLI (Command-line tools):**

This is the bridge most people miss. CLI tools are more portable than visual UIs, and while some are meant for end users, many are meant for servers or automation. Yes, you'll need platform-specific bash or PowerShell scripts, but I wouldn't write more than the bootstrap code there (the code that installs the executables). For actual CLI tools, assume cross-platform only.

- **Cross-platform CLI (automation, developer tools):** Go, Rust
- **Cross-platform CLI (quick scripts, one-offs):** Python
- **Performance-critical CLI:** Rust

The rule of thumb: If the CLI will grow beyond a few hundred lines or needs distribution as a binary, use Go or Rust. For quick automation that stays small, Python works great. Python won on portability for CLI tools. Even when the core logic is written in a compiled language, deploying code is often better using the Python ecosystem. I covered this extensively in my [previous article about Rust and scripting languages](/blog/ai-tools-journey-opus-4-5/), where I discussed how Claude Opus 4.5 made writing Rust feasible for CLI tools in ways it wasn't before.

**Server (Backend, APIs, services):**

The server is where the real diversity shows up.

- **REST APIs, web services, large teams:** C# (ASP.NET Core) or Go. C# is not a Windows-only thing (ASP.NET Core runs on Linux, macOS, and containers just as well as it runs on Windows). It's a fully viable cross-platform server solution.
- **Microservices, distributed systems:** Go or C#
- **Server utilities, automation, DevOps tools:** C#, Go, Python
- **Performance-critical servers, systems programming:** Rust
- **Constrained environments (embedded, IoT, real-time systems):** Rust

The rule of thumb: If you need to stand up a server with REST endpoints, talk to databases, and onboard a big team (you cannot go wrong with ASP.NET Core (C#) or Go). Both have excellent ecosystems, strong typing, and can handle large codebases. I don't think Python is the right solution for server work as of today. I know there are successful projects that use Python for servers, but the lack of static typing and the deployment complexity make it less ideal.

As you go down the stack and have to run on smaller, more constrained environments, Rust comes into play. Anytime you would have used C/C++, Rust is a good replacement. When you need the level of control that C++ provides, using Go or C# would introduce a garbage collector that might not be appropriate for the use case. We can see this very well in the world of game engines. The Godot game engine is written in C++, but all of the client code (what people use for scripting) is usually in different languages. I've seen how the garbage collector's global stop or global pause can introduce issues for end users. In AI, every time there is an issue with performance or control, we tend to use a combination of C++ and Python. C++ for the performance-critical parts, Python for the glue and the high-level logic.

## The LLM Era: Even Coding Agents Show This Diversity

The equation does change when it comes to AI. LLMs are able to write Rust just as easily as they can write PowerShell. The barriers that once made certain languages intimidating have lowered significantly. C and C++ were once barriers for me (but now by choice, I use other languages instead).

Interestingly, even coding agents themselves show this diversity in language choice:

- **[Codex CLI](https://github.com/openai/codex):** Written in Rust (performance-critical, cross-platform distribution)
- **[Aider](https://aider.chat/):** Written in Python (rapid iteration, pip-based distribution)
- **[Antigravity CLI](https://agentpedia.codes/blog/antigravity-cli-deep-dive):** Written in Go (server-like characteristics, cross-platform)
- **[Claude Code](https://github.com/anthropics/claude-code):** Written in TypeScript (web ecosystem integration, npm-based distribution)

The diversity is striking. While Aider does use Python, most newer coding agents prefer compiled languages or TypeScript. The deployment story matters tremendously. For internal tooling, I like the idea of using GitHub releases for distributing executables with a very clear deployment story. Each tool chose the language that best fits its deployment target and trade-offs. That's the lesson here (there is no single "best" language). The question now comes down to: What are the capabilities of the language? What area do you need to address? Deployment of the code becomes a big issue. You need to have a very well-understood deployment story.

I don't think I'm picky when it comes to languages. I just probably don't see myself writing C++, C, or JavaScript unless I have to. And right now, I don't feel like I have to, given that we have so many other languages. I don't think I have to write JavaScript anymore. The languages that probably are most popular (C, C++, JavaScript) are probably ones we don't need to write anymore. They could be targets. You write TypeScript, and then that gives you JavaScript as a compiled output. That's fine.

No, I'm not going to port anything to Rust (or Kotlin, or any other language) that's already written in a different language. I don't think that's pragmatic. But I do think new things (new things that don't have dependencies or existing infrastructure) should probably, at the very least, be written in a static language. That's my high-level thinking.

I am very excited about Mojo, which is meant to bridge the gap between Python and Rust. As of this writing, it's not yet GA, so it's not something I could even consider. But even then, in a world where we have Mojo (meant for accelerators), I will probably still choose Rust, Go, C#, or another compile-time language for most cases.

What matters now isn't just syntax or learning curve (it's the entire ecosystem). The deployment story has become critical. Language capability matters (can it interoperate with other languages in your stack?). Community alignment is crucial (it would be a hard sale to write something in C# at a company like Amazon where most of their stack is Java, though Go might still be chosen because of its different capabilities).

We've seen this play out in real projects. The Ladybird browser initially attempted to move to Swift, but they faced capability issues and needed to be pragmatic, so they moved to Rust instead. These are the kinds of trade-offs that matter now: tooling, deployment, compile-time guarantees, language interoperability, and how well the language fits both the problem and your community. LLMs can write in any language, but that doesn't mean all languages are equally good choices. Choose the language that gives you the guarantees you need, the deployment story you can live with, and the ecosystem that supports the problem you're solving.

---

*For more on my experience with Rust development in the LLM era, see [My AI Tools Journey Since Claude Opus 4.5](/blog/ai-tools-journey-opus-4-5/).*
