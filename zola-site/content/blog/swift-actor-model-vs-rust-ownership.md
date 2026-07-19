+++
title = "Swift's Actor Model vs Rust's Ownership: Why Rust Doesn't Need Actors"
date = "2026-07-19"
description = "A deep dive into why Swift's actor model feels like it under-delivers on isolation, why Rust achieves data-race freedom without actors at all, and how backward compatibility with C and C++ shaped Swift into retrofitting safety it can only approximate."
template = "blog-post.html"
categories = ["development", "languages"]
tags = ["swift", "rust", "concurrency", "actors", "memory-safety", "type-systems", "languages"]
+++

I keep coming back to Swift's [actor model](https://developer.apple.com/documentation/swift/actor) and feeling that it did not go far enough. The whole pitch for actors was memory isolation and thread safety: give each unit of concurrency its own protected state so the compiler can rule out data races. That goal is exactly right, and I think it was absolutely needed. But as an outsider looking in, the payoff feels thin. The model carries a lot of complexity (non-isolated code, region checks, `Sendable` everywhere), and at the end of it an actor is still, essentially, a class that is a little different for thread safety. Meanwhile [Rust](https://www.rust-lang.org/) has no actor model at all and gets stronger, more versatile thread isolation almost for free. This post is my attempt to explain why, and where I think Swift's model is genuinely lacking.

## Two Different Goals, Attacked at Different Layers

The first thing worth separating is that "thread safety" is really two properties:

- **Data-race freedom** — no two threads touch the same mutable memory at once without synchronization.
- **Isolation** — a unit of concurrency owns its state, and nothing else can reach into it.

Rust guarantees the first with essentially no runtime concept of an "actor." Swift's actors are a mechanism aimed at the second, and they get the first as a consequence. That asymmetry is the root of almost everything that feels off to me. Rust bakes safety into the *type system* uniformly; Swift bolts it onto a *reference type* that lives inside a language full of shared mutable class references.

## Why Rust Doesn't Need Actors

Rust's data-race freedom falls out of [ownership and borrowing](https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html) plus two marker traits, all checked at compile time:

- **Aliasing XOR mutability.** At any moment you can have many shared references (`&T`) *or* exactly one mutable reference (`&mut T`), never both. A data race requires aliasing *and* mutation *and* concurrency. Rust statically forbids the aliasing-plus-mutation combination through its [references and borrowing rules](https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html), so the race is impossible before threads even enter the picture.
- **`Send` and `Sync`.** [`Send`](https://doc.rust-lang.org/std/marker/trait.Send.html) means a type can be moved to another thread; [`Sync`](https://doc.rust-lang.org/std/marker/trait.Sync.html) means `&T` can be shared across threads. These are auto-derived and *compositional*: `Rc<T>` is `!Send` because its reference count is non-atomic, while `Arc<T>` is `Send`. The compiler propagates this through every type automatically, as [the Rustonomicon on Send and Sync](https://doc.rust-lang.org/nomicon/send-and-sync.html) lays out.
- **Move by default.** When you send a value across a [channel](https://doc.rust-lang.org/book/ch16-02-message-passing.html), ownership transfers and the sender statically *cannot* touch it afterward.

That last point is where I want to correct my own intuition. I kept describing Rust's safety in terms of *copies* — "the copies are completely independent." The thing that actually makes Rust both safe *and* cheap is that a transfer is a [move that invalidates the source](https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html#variables-and-data-interacting-with-move), not a deep copy. There is no performance penalty and no size limit, because nothing is duplicated — ownership simply relocates. My worry about "structs too big to copy" mostly dissolves once you internalize move semantics instead of copy semantics.

So Rust gives you per-unit isolation exactly when you want it — channels, [`Mutex<T>`](https://doc.rust-lang.org/std/sync/struct.Mutex.html), thread-local ownership — without imposing an actor runtime. Actors in Rust are a library pattern (for example [Actix](https://actix.rs/)), not a language feature, because the language already provides the guarantee that actors elsewhere provide at runtime.

## What Swift Actually Chose, and Why It Looks Lacking

Swift's model is [actors](https://github.com/swiftlang/swift-evolution/blob/main/proposals/0306-actors.md) plus [`Sendable`](https://github.com/swiftlang/swift-evolution/blob/main/proposals/0302-concurrent-value-and-concurrent-closures.md), later reinforced by [region-based isolation](https://github.com/swiftlang/swift-evolution/blob/main/proposals/0414-region-based-isolation.md) and [`sending` parameters](https://github.com/swiftlang/swift-evolution/blob/main/proposals/0430-transferring-parameters-and-results.md). My critique has three parts, and honestly they do not all hold up equally.

### "Actors are just classes that are trivially different." — Mostly true, and the deepest point.

An [`actor`](https://developer.apple.com/documentation/swift/actor) is a reference type. Its identity is a heap pointer that gets copied around freely. What the actor guarantees is only that access to its *mutable stored properties* is serialized through its executor. It does **not** guarantee that the things you put inside it are themselves isolated. That is exactly why [`Sendable`](https://developer.apple.com/documentation/swift/sendable) has to exist as a separate, viral constraint: the actor boundary is only as strong as the `Sendable`-ness of what crosses it. In Rust, the equivalent guarantee is woven into *every* type uniformly; in Swift it is layered onto a reference-type actor whose surrounding language is full of shared mutable class references. The actor is a serialization box, not a true isolation boundary — so the instinct that it is weaker than advertised is, I think, correct.

### "The non-isolated regions and complexity were not worth it." — This is where I'm weakest.

The [region-based isolation analysis](https://github.com/swiftlang/swift-evolution/blob/main/proposals/0414-region-based-isolation.md) and `sending` exist *precisely because* Swift refused to make invalidate-on-move the core of the language the way Rust did. Given that constraint, region isolation is a clever and *necessary* retrofit: it lets the compiler prove that a non-`Sendable` value is "disconnected" from every other region and can therefore be transferred into an actor safely, without full ownership tracking. It feels like complexity for its own sake only because it is compensating for the absence of a real ownership system. The complexity is a *symptom* of the backward-compatibility choice, not a standalone design failure.

### "C and C++ compatibility is the root cause." — My strongest point.

Swift committed early to reference-semantics classes with shared mutable state, [automatic reference counting](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/automaticreferencecounting/) everywhere, seamless [C and Objective-C interop](https://www.swift.org/documentation/cxx-interop/), and a stable ABI. Those commitments make an ownership-first, move-by-default *core* impossible to retrofit as the default. Rust started from ownership; Swift started from "a nicer Objective-C." So Swift now reaches for [data-race safety](https://www.swift.org/migration/documentation/migrationguide/) in Swift 6 via `Sendable` plus actors plus regions layered *on top of* a language whose default is shared mutable reference semantics. That is why it feels like scaffolding around a building that was not designed for it. [Noncopyable types](https://github.com/swiftlang/swift-evolution/blob/main/proposals/0390-noncopyable-structs-and-enums.md) (`~Copyable`) and the [`borrowing` and `consuming`](https://github.com/swiftlang/swift-evolution/blob/main/proposals/0377-parameter-ownership-modifiers.md) modifiers are Swift importing Rust's ideas after the fact — and, exactly as it feels, they land in the middle of an existing model, so they read like patches rather than foundations.

## The Mailbox Question

Classic [actor-model](https://en.wikipedia.org/wiki/Actor_model) systems like [Erlang](https://www.erlang.org/) get strong isolation because each actor has private state, communicates *only* through asynchronous messages, and those messages are copied or immutable so no shared references escape. Swift deliberately did not do full copy-on-send message passing, because copying arbitrary Swift objects would be expensive and would fight ARC and class semantics. Instead you write `await someActor.method(arg)` — which looks like a method call, passes references, and leans on `Sendable` to stay honest.

So the "mailbox" is conceptually present (the actor's serial executor *is* the mailbox), but the isolation-by-value discipline that gives Erlang its robustness is missing. That is the gap I keep feeling: Swift got the *serialization* of the actor model without the *isolation-by-value*.

And here is the counterpoint I talked myself into: you do not need Erlang's process-per-actor model today, because hypervisors, orchestration platforms, and OS process boundaries already provide heavyweight isolation above the language. The real squeeze is that on iOS you cannot lean on cheap multi-process isolation the way a server runtime can — an app is a single sandbox. That pushes the entire isolation burden back into the type system, which is precisely where Swift is weakest relative to Rust.

## Where I Land

I started out wanting to say "the complexity of Swift's actor model did not pay off." I think the sharper, more defensible version is this:

> Swift's actor model delivers **serialized access** and a **best-effort isolation boundary**. But because the surrounding language is built on copyable shared references and C interop, the actor cannot be a *truly* isolated environment. All the hard guarantees have to be reconstructed with `Sendable` plus region analysis plus move-only types — a large, viral complexity budget spent to *approximate* what Rust gets for free from ownership. The payoff is real (Swift 6 genuinely catches data races), but the cost-to-benefit is worse than Rust's, because it is compensating for foundational decisions rather than building on them.

Actors were not the mistake. Expecting actors to provide Rust-grade isolation on a reference-semantics substrate is the mismatch.

## Would a "Strict Swift" Mode Fix It?

I floated the idea of a dialect where assignment defaults to move (like Rust) and actors are *fully* isolated with no escaping references. My honest assessment:

- **The pieces already exist**, just not as defaults: `~Copyable` types, `consuming` and `borrowing` ownership, `@Sendable` closures, and [`-strict-concurrency`](https://www.swift.org/migration/documentation/migrationguide/) checking together add up to roughly "strict Swift."
- **The blocker is defaults and interop, not capability.** A true strict mode would need move-by-default and a ban on non-`Sendable` capture — the exact things that break source compatibility and C/Objective-C bridging, which Swift refuses to give up. So it can only ever be an *opt-in* island, never the language default.
- **The realistic trajectory** is not a separate named language but *progressive tightening*: strict concurrency becomes mandatory in Swift 6, move-only types get more ergonomic, and isolation rules keep getting refined. It converges toward "opt-in Rust-like discipline," which is philosophically close to the idea — just delivered as gradual constraints instead of a dialect.

Rust does not need actors because ownership plus `Send` and `Sync` plus move-by-default make data races a compile error at the type level, uniformly and for free. Swift's actors are insufficient for full isolation because an actor is a copyable reference type that only serializes access, and real isolation has to be rebuilt on top of a shared-mutable, C-compatible core. The root cause really is backward compatibility — and the fairer criticism is not that the complexity was pointless, but that the retrofit carries a worse cost-to-benefit than a foundation designed for ownership from day one.

### Sources

| Source | Link |
|---|---|
| `actor` — Apple Developer Documentation | [developer.apple.com](https://developer.apple.com/documentation/swift/actor) |
| `Sendable` — Apple Developer Documentation | [developer.apple.com](https://developer.apple.com/documentation/swift/sendable) |
| SE-0306: Actors | [swift-evolution](https://github.com/swiftlang/swift-evolution/blob/main/proposals/0306-actors.md) |
| SE-0302: `Sendable` and `@Sendable` closures | [swift-evolution](https://github.com/swiftlang/swift-evolution/blob/main/proposals/0302-concurrent-value-and-concurrent-closures.md) |
| SE-0414: Region-based isolation | [swift-evolution](https://github.com/swiftlang/swift-evolution/blob/main/proposals/0414-region-based-isolation.md) |
| SE-0430: `sending` parameters and results | [swift-evolution](https://github.com/swiftlang/swift-evolution/blob/main/proposals/0430-transferring-parameters-and-results.md) |
| SE-0390: Noncopyable structs and enums (`~Copyable`) | [swift-evolution](https://github.com/swiftlang/swift-evolution/blob/main/proposals/0390-noncopyable-structs-and-enums.md) |
| SE-0377: `borrowing` and `consuming` parameter ownership modifiers | [swift-evolution](https://github.com/swiftlang/swift-evolution/blob/main/proposals/0377-parameter-ownership-modifiers.md) |
| Swift 6 Migration Guide — data-race safety and strict concurrency | [swift.org](https://www.swift.org/migration/documentation/migrationguide/) |
| Automatic Reference Counting — The Swift Programming Language | [docs.swift.org](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/automaticreferencecounting/) |
| Mixing Swift and C++ — Swift.org | [swift.org](https://www.swift.org/documentation/cxx-interop/) |
| What Is Ownership? — The Rust Programming Language | [doc.rust-lang.org](https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html) |
| References and Borrowing — The Rust Programming Language | [doc.rust-lang.org](https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html) |
| Message Passing / channels — The Rust Programming Language | [doc.rust-lang.org](https://doc.rust-lang.org/book/ch16-02-message-passing.html) |
| `std::marker::Send` — Rust standard library | [doc.rust-lang.org](https://doc.rust-lang.org/std/marker/trait.Send.html) |
| `std::marker::Sync` — Rust standard library | [doc.rust-lang.org](https://doc.rust-lang.org/std/marker/trait.Sync.html) |
| `std::sync::Mutex` — Rust standard library | [doc.rust-lang.org](https://doc.rust-lang.org/std/sync/struct.Mutex.html) |
| Send and Sync — The Rustonomicon | [doc.rust-lang.org](https://doc.rust-lang.org/nomicon/send-and-sync.html) |
| The Rust Programming Language — official site | [rust-lang.org](https://www.rust-lang.org/) |
| Actix — actor framework for Rust | [actix.rs](https://actix.rs/) |
| Actor model — Wikipedia | [wikipedia.org](https://en.wikipedia.org/wiki/Actor_model) |
| Erlang — official site | [erlang.org](https://www.erlang.org/) |
