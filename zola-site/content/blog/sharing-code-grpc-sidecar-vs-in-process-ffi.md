+++
title = "Sharing Code Across Languages: The gRPC Sidecar (and the One Place It Breaks)"
date = "2026-07-19"
description = "Why running your shared logic as a local gRPC subprocess is the well-supported way to reuse one codebase across languages on desktop and server, and why iOS is the exception that forces in-process FFI."
template = "blog-post.html"
categories = ["development", "architecture"]
tags = ["grpc", "rust", "ffi", "ios", "sdk", "protobuf", "cross-platform"]
+++

I spent a while chasing a question that sounds simple: if I write my logic once (say in Rust), how do other languages actually call it? I went down the protocol buffers road first, looking at how projects like Signal expose a Rust core to Swift and Java. That path works, but it is heavy: you hand-write a foreign-function interface, you generate C headers, you manage memory across the boundary, and you maintain a thin wrapper per language. After much more research, I landed on a cleaner answer for most cases: don't link the code into every language at all. Run it as a local server, and let every language talk to it over gRPC. The surprise at the end of the quest was that this pattern works almost everywhere (and there is exactly one platform where it does not).

## The sidecar is the well-supported path

The pattern is straightforward. You take all your shared logic and compile it into a single executable that speaks gRPC. That executable gets spawned as a child process at the same time as your application. Your application (in whatever language you like) becomes a gRPC client. The two talk over a local socket. Because gRPC is defined by protocol buffers, and protobuf has mature, first-class code generation for Go, C#, Python, TypeScript, Swift, Kotlin, Java, C++, and Rust, every language gets a native, typed client for free. You write the schema once, and the contract is the same everywhere.

This is what people mean by a "sidecar" or a local service. Your SDK in each language stops being a re-implementation of your logic and becomes a thin front end to the gRPC service. The heavy code lives in one place, in one language, and never gets ported. Adding support for a new language is not a rewrite (it is generating a client stub and writing a small ergonomic wrapper around it). This is a well-documented, well-supported scenario across the whole gRPC ecosystem, which is exactly why it feels safe to build on.

It is also the shape a lot of tools already take. A local language server that your editor spawns and talks to over a socket is the same idea (a subprocess that acts as a service, with clients written in whatever language the editor happens to use). GitHub Copilot's tooling follows this pattern too: the logic runs in a spawned process, and the front ends talk to it. Once you see the pattern, you notice it everywhere: the durable, reusable logic runs as a service, and the per-language surface is just a client.

For Linux, Windows, and macOS (desktop and server) this is the answer I would reach for first. Spawning a child process is a normal, supported operation on all of them. You get process isolation (a crash in the logic does not take down the host), clean language boundaries, and a deployment story where you ship one service binary plus thin clients.

## Where it breaks: iOS does not let you spawn a subprocess

The entire pattern rests on one assumption: that your application is allowed to spawn a child process. On desktop and server operating systems, that assumption holds. On iOS, it does not.

iOS apps run in a strict sandbox, and that sandbox forbids creating child processes. The traditional UNIX mechanisms (`fork()`, `exec()`, `posix_spawn()`, `system()`) are not available to third-party apps. This is enforced by the kernel, not just by App Review, so there is no entitlement that turns it back on. An Apple Developer Technical Support engineer states it directly on the Apple Developer Forums: iOS apps are not allowed to spawn child processes, and neither signals nor any other traditional UNIX mechanism for launching child processes is supported. Apple's own sandboxing model backs this up: each app is confined to its container.

These are the authoritative sources. They live on `developer.apple.com`, which sits behind bot protection that blocks automated link checkers, so our CI cannot validate them (they are valid in a browser). The full URLs are exposed here so you can verify them directly:

- Apple Developer Forums, "system("") function" (Apple DTS engineer: iOS apps are not allowed to spawn child processes): [https://developer.apple.com/forums/thread/72265](https://developer.apple.com/forums/thread/72265)
- Apple Developer Forums, the "fork" discussion (why `fork()` is unavailable on iOS): [https://developer.apple.com/forums/thread/747499](https://developer.apple.com/forums/thread/747499)
- Apple File System Programming Guide (the app sandbox / container model): [https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/FileSystemOverview/FileSystemOverview.html](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/FileSystemOverview/FileSystemOverview.html)

That single restriction is what breaks the sidecar pattern on iOS. You cannot spawn your gRPC service as a local subprocess, because you cannot spawn a subprocess at all. Everything has to run inside your app's one process. So the very thing that makes the sidecar clean on every other platform (a separate process you talk to over a socket) is the thing iOS will not let you do.

## When in-process FFI actually earns its cost

This is where the earlier, heavier path comes back. When you cannot run a separate process, you have to bring the code inside your own process, and that means linking a library and calling it through a foreign-function interface. On iOS, this is not a preference (it is the only option). You compile your Rust (or C, or C++) core into a static library, expose a C ABI, and call into it directly. Projects like Signal's `libsignal` do exactly this: a Rust core, a generated C header, and a thin hand-written Swift layer on top. It is more work and more careful memory management, but it runs entirely in-process, which is what the platform requires.

There is a second reason to reach for in-process FFI even off iOS: overhead. Talking to another process, even a local one, costs more than a direct function call (you are serializing arguments, crossing a socket, and deserializing on the other side). For almost all applications that cost is irrelevant next to the clarity you get from process isolation. But when you genuinely need the lowest possible latency (tight loops, real-time media, high-frequency calls where every microsecond counts), collapsing the boundary into a direct in-process call is worth the extra maintenance. That is the honest trade: in-process FFI buys you no-subprocess compatibility and minimal overhead, and it costs you a hand-maintained boundary in every language you support.

So the decision comes down to two questions. Can you spawn a subprocess (yes on desktop and server, no on iOS)? And do you actually need to eliminate cross-process overhead (rarely)? If you can spawn a process and you do not have an extreme latency requirement, run your logic as a gRPC sidecar and let protobuf give every language a typed client. If you are on iOS, or you are in the rare case where the overhead genuinely matters, pay for the in-process FFI. Reach for the heavier tool only when the lighter one is not available.

---

*This is the practical follow-through to my thinking on [language choice in the LLM era](/blog/language-choice-in-the-llm-era/): the point was never to pick one language for everything, but to let each layer use the language that fits and keep the shared logic in one place. The gRPC sidecar is how you honor that on desktop and server; in-process FFI is the exception you accept when the platform (iOS) takes the subprocess away.*
