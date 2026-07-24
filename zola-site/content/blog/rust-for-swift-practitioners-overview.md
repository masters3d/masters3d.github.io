+++
title = "Rust for Swift Practitioners: A Field Guide to What Moved"
date = "2026-07-24"
description = "The start of a series for Swift programmers learning Rust: not a tour of syntax, but a map of the specific places where a Swift mental model reaches for something and finds it missing, renamed, or inverted, with the idiomatic Rust alternative each time."
template = "blog-post.html"
[taxonomies]
categories = ["Engineering Systems"]
tags = ["rust", "swift", "rust-for-swift", "ownership", "type-systems", "languages"]
[extra]
editorial_track = "engineering-systems"
series = "rust-for-swift"
+++

I learned Rust the way I suspect a lot of Swift programmers do: confidently, and
then not. The syntax looked familiar enough that I skimmed the early chapters
(structs, enums, generics, pattern matching, all present and roughly where I
expected them). Then I hit a wall that had nothing to do with syntax. I wrote a
function, passed a value into it, and tried to use that value again on the next
line, and the compiler told me no. Not a warning, not a runtime surprise, a flat
refusal to build. I had reached for the most basic Swift reflex I own (a value
is mine, I can keep using it) and Rust had quietly removed it.

That moment is the whole reason for this series. The interesting part of moving
from Swift to Rust is not the syntax you have to learn; it is the handful of
deeply held Swift assumptions you have to _unlearn_, because Rust made a
different choice at the foundation. This series is a field guide to those
choices, written from the Swift side of the fence. Each post starts from a thing
you already know how to say in Swift, shows the exact spot where Rust diverges,
and gives you the idiomatic Rust way to say it instead.

## Why a Swift practitioner, specifically

There is no shortage of "learn Rust" material, and this is not that. The premise
here is that you are already fluent in one modern, safe, statically typed
language with value types, generics, protocols, closures, and a strong opinion
about `nil`. That fluency is an asset and a trap. It is an asset because most of
Rust's surface will feel like a dialect you can half-read on day one. It is a
trap because the places that look identical are exactly where the differences
hide, and a familiar-looking construct that behaves differently is harder to
learn than a foreign one.

The shape of this series is borrowed, with gratitude, from Doug Gregor's
excellent [Swift for C++ Practitioners](https://www.douggregor.net/posts/),
which teaches Swift to people who already think in C++. I am flipping the
direction (Swift practitioners learning Rust) and writing everything from
scratch, but the underlying idea is his: the fastest way to learn a language is
to map it onto the one already in your head, especially where the map is wrong.

## The one that started it: copy is not the default

The first assumption to give up is the one I hit on that first afternoon. In
Swift, a `struct` has value semantics: assign it and you get an independent
copy, and the original stays yours.

```swift
// Scalars such as Int are value types too: assignment copies them, so both
// bindings stay usable and independent. Rust agrees here (integers are Copy),
// which is why this one case feels the same in both languages.
var x = 41
var y = x          // copies
y += 1             // changes only y
print("x = \(x), y = \(y)")
```

Rust does not do this by default. For most types, assigning a value _moves_ it,
and the source binding becomes unusable. The exceptions are small types like
integers, which are marked `Copy` and behave exactly like the Swift instinct
expects. That single inversion (copy is the exception, not the rule) ripples
outward into how functions take arguments, how closures capture, and how threads
share data. The
[first full post](/blog/rust-for-swift-value-types-copy-vs-move/) in this series
is entirely about it, because getting it into your bones makes half of the rest
of Rust stop feeling arbitrary.

## The map of what moved

The series walks the same ground a Swift programmer already knows, one familiar
concept at a time, and marks where Rust put things somewhere else. A few of the
stops, to set expectations:

- **References and optionals.** Swift's `class` gives you shared, mutable
  references for free, and `nil` is everywhere. Rust has no default reference
  type at all (sharing is always spelled out), and `Optional` becomes `Option`
  with none of the implicit unwrapping.
- **Move semantics, inverted.** Swift recently _added_ opt-in move-only values
  (`consuming`, `~Copyable`). In Rust, move is where you start and copying is
  what you opt into. Same feature, opposite default.
- **Type erasure.** Swift hands you `any Protocol`, metatypes, and reflection.
  Rust gives you `dyn Trait` with real limits (object safety) and no runtime
  metatypes, so the Swift habit of erasing types needs a different toolkit.
- **Concurrency without a runtime.** Swift ships a concurrency runtime, so
  `await` just works and `actor` isolates state for you. Rust's `async` is only
  syntax (you bring your own runtime), and data-race freedom is proven by the
  compiler through `Send` and `Sync` rather than by an actor. I have written
  before about
  [why Rust reaches thread safety without actors at all](/blog/swift-actor-model-vs-rust-ownership/);
  the series returns to that from the Swift practitioner's side.

Each post is short, anchored in a Swift expectation, and built around code you
can run. In fact every Swift and Rust snippet in this series is a real file that
gets compiled and executed on every change, and the output you see quoted is the
output the program actually produced. If a claim here is wrong, the build breaks
before you ever read it. That constraint is deliberate: the surest way to learn
what Rust rejects is to watch a compiler reject it, on purpose, and know that
the rejection is real. It is the same spirit as
[sharing one core across languages](/blog/sharing-one-core-across-languages/),
where the boundary only counts if it actually holds.

_I keep a soft spot for Swift (it is still
[my favorite language I never got paid to use](/blog/swift-journey-why-not-professional/)),
and this series is not an argument that Rust is better. It is an argument that
the two languages made different bets at the foundation, and that naming those
bets out loud is the fastest way across. The point of a field guide is not to
tell you the territory is wrong; it is to stop you walking off the same cliff I
did on the first afternoon._
