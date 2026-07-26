+++
title = "Swift's Safety Checks: Why a Crash Can Be Safe"
date = "2026-07-25"
description = "Swift sometimes preserves memory safety by stopping the program. Following a Character initializer into the standard library explains when to use assert, precondition, and fatalError."
template = "blog-post.html"
[taxonomies]
categories = ["Engineering Systems"]
tags = ["swift", "memory-safety", "assertions", "preconditions", "standard-library", "languages"]
[extra]
editorial_track = "engineering-systems"
+++

In 2020 I was writing queries in Kusto, a loosely typed database language, and
noticed something that felt wonderful at first. If I indexed past the end of a
dynamic array, the query did not crash. I got a null value and the query kept
going. Coming from Swift, where an out-of-range array subscript stops the
program, this seemed safer. Nothing broke.

The trouble was that something had broken. The query had violated an assumption,
then carried that violation farther away from its cause. Every operation
downstream now had to account for a value that should never have existed. When
the failure finally became visible, it no longer pointed at the bad index.

That experience kept pulling me back to a question that had always bothered me:
if Swift is a safe language, why is it so willing to crash?

## A Safe Stop Is Not the Same as Staying Alive

Swift uses "safety" in a narrower and more useful sense than "the process never
terminates." Its
[memory-safety model](https://github.com/swiftlang/swift-book/blob/main/TSPL.docc/LanguageGuide/MemorySafety.md)
prevents operations such as reading uninitialized memory, accessing memory after
it has been deallocated, indexing outside an array, and making conflicting
accesses to the same memory.

Calling a language "safe" does not mean every program written in it is correct.
It means ordinary language operations cannot silently step outside the
language's defined model and perform arbitrary memory access. Python is commonly
called memory-safe because its interpreter checks operations at runtime and
manages object lifetimes for the program. C++ is not memory-safe by default
because ordinary C++ permits unchecked pointer arithmetic, use after free, and
out-of-bounds access with undefined behavior. Both languages can fail, and both
can call native code that violates their usual boundaries. The distinction is
what their normal language semantics permit.

That last boundary makes the label less absolute than it first sounds. CPython
itself is implemented largely in C, and many of Python's most important
libraries wrap performance-critical C or C++ code. The Python expression calling
one of those libraries remains constrained by Python's semantics, but the native
implementation underneath can still contain a buffer overflow, use after free,
or incorrect reference count. A defect there can corrupt the interpreter rather
than becoming a clean Python exception.

So I need to ask what layer a safety claim describes. Python-the-language
protects ordinary Python operations, but a Python process is only as memory-safe
as its interpreter and every native extension loaded into it. Crossing that
extension boundary does not make Python's language rules false. It means those
rules cannot prove the safety of code they do not govern. The same qualification
applies when Swift calls C or C++, or when Rust crosses an `unsafe` or
foreign-function boundary. Safe code can narrow and audit those boundaries, but
it cannot make an unchecked dependency safe merely by wrapping it in a safer
interface.

Safety can also be enforced at different times. Python places most of that work
in its runtime. Rust moves far more of it into compile-time ownership,
borrowing, and lifetime checks, rejecting many invalid programs before they run.
Swift uses both approaches: its type and ownership rules prove some properties
during compilation, while runtime checks protect properties that depend on live
values. This is not a ranking where runtime safety is less real than
compile-time safety. It is a difference in when an invalid operation is rejected
and what cost or feedback comes with that rejection.

If a Swift array has ten elements, the compiler cannot always know whether the
index supplied at runtime will be 3 or 30. Swift checks the index before
performing the access. Rust performs the same kind of runtime bounds check when
an index cannot be proven valid. If the check fails, either language traps
rather than allowing the access.

The trap is the safety mechanism. The program stops before it can read unrelated
memory, corrupt state, or continue with a value that has no valid meaning. It
trades availability for integrity. As a user, I still experience a crash. As an
engineer investigating the failure, I get a boundary placed exactly where the
invariant was broken.

This distinction matters. A server that stays up is available. A program that
does not perform invalid memory operations is memory-safe. Good software needs
both, but pretending they are the same property only hides the trade-off.
Recoverable conditions should use recovery mechanisms. Broken invariants should
not quietly become data.

Memory safety is not the same as security against threats, either. Preventing
invalid memory access closes off important classes of exploits, but it does not
prove that authorization is correct, secrets are protected, dependencies are
trustworthy, or inputs cannot be abused. Memory safety is one foundation of a
secure system, not a complete threat model.

A crash by itself therefore does not tell me whether a language kept its safety
promise. A deliberate bounds-check trap can be the exact mechanism preserving
memory safety. Swift also cannot prevent every other reason a process might
terminate. It can still run out of memory, overflow the stack, recurse forever
until that stack is exhausted, encounter an operating-system failure, or call
unsafe code that violates Swift's guarantees. Those failures matter for
reliability, but their existence does not erase the narrower memory-safety
guarantee.

## Following `Character` Into the Standard Library

I first tried to understand this by following the initializer for `Character`. A
`Character` represents one extended grapheme cluster, but its initializer
accepts a `String`. The type system cannot express "a string containing exactly
one character" in that parameter, so the initializer has to inspect the value
after it arrives.

The earliest open-source Swift version I can verify, on the
[`swift-2.2-branch`](https://github.com/swiftlang/swift/blob/swift-2.2-branch/stdlib/public/core/Character.swift),
contains these checks:

```swift
_precondition(
  s._core.count != 0, "Can't form a Character from an empty String")
_precondition(
  s.startIndex.successor() == s.endIndex,
  "Can't form a Character from a String containing more than one extended grapheme cluster")
```

There is no honest default for the empty case. Returning a space would invent
data. Returning an optional would change the initializer's contract. Allowing an
invalid `Character` would push the broken invariant into every operation that
uses it. The precondition says something much sharper: given this API, an empty
string is invalid input, and execution cannot continue through this path.
`_precondition` is the standard library's internal counterpart to the public
`precondition`; both remain checked in ordinary `-O` release builds.

The
[current implementation](https://github.com/swiftlang/swift/blob/main/stdlib/public/core/Character.swift)
still protects the empty-string invariant with `_precondition`. The details have
changed as Swift's string model has evolved, but the boundary remains. This is a
useful example of runtime safety doing work that the type system cannot yet do.
A hypothetical `NonEmptyString` could move one part of the proof earlier, but
the program would still need to establish that invariant somewhere.

The source also preserves a small naming path. Swift 2.2 temporarily annotated
`precondition` and `preconditionFailure` for a future rename to `require` and
`requirementFailure`. That rename never shipped. An earlier version of my draft
claimed a longer path through `alwaysTrap`, `securityCheck`, and `required`, but
I cannot substantiate that sequence in the public repository. The language kept
the precondition names, and their meaning is now explicit in
[`Assert.swift`](https://github.com/swiftlang/swift/blob/main/stdlib/public/core/Assert.swift).

## Choosing How to Fail

Swift's failure functions look similar at the call site, but they encode
different promises:

- `assert` and `assertionFailure` are for internal checks during development. In
  normal `-O` release builds, their conditions are not evaluated.
- `precondition` and `preconditionFailure` are for requirements that must also
  stop shipping code. In `-O` builds, a failed precondition still traps.
- `fatalError` means the program cannot continue in any build configuration. It
  always traps.

The unusual case is `-Ounchecked`. That mode removes runtime safety checks for
speed. It can omit both assertions and preconditions, and the optimizer may
assume their conditions are true. Violating that assumption can produce
undefined behavior. Calling `-Ounchecked` "release mode" therefore misses the
most important distinction: ordinary `-O` keeps precondition checks;
`-Ounchecked` deliberately gives that safety up. `fatalError` remains
unconditional.

The choice is not really about which spelling produces a nicer crash. It is
about classifying the condition:

- If bad input is expected in normal operation, return an optional, throw an
  error, or use `Result`.
- If a caller has violated a documented requirement and continuing would make
  the program invalid, use `precondition`.
- If an internal assumption should be checked during development without
  charging shipping code for the check, use `assert`.
- If the current path cannot produce a valid program state in any configuration,
  use `fatalError` sparingly and deliberately.

This is why standard-library checks such as an array index being in range or a
collection being nonempty are not merely defensive programming. They mark the
last point where Swift can reject an invalid operation before it becomes unsafe.
The crash is loud because the alternative is worse: silently reading the wrong
memory or manufacturing a result that lets the original mistake travel.

---

_The Kusto query that kept running taught me that survival is not the only
measure of safety. Sometimes the safest program is the one that refuses to
continue after its assumptions become false. Swift's traps make that refusal
precise: recover what is recoverable, but stop at the boundary where continuing
would turn a local mistake into corrupted state. That same preference for
explicit constraints runs through
[Swift's actor model](/blog/swift-actor-model-vs-rust-ownership/) and through my
broader question of
[language choice in the LLM era](/blog/language-choice-in-the-llm-era/). A safe
language does not promise that software will never crash. It promises that
invalid memory operations do not get to masquerade as successful ones._
