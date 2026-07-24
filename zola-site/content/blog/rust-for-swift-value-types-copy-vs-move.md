+++
title = "Rust for Swift Practitioners: Copy Is the Exception, Not the Rule"
date = "2026-07-25"
description = "The first and most disorienting difference for a Swift programmer learning Rust: Swift copies values by default, Rust moves them by default, and copying is the thing you opt into. A concrete walk through move, clone, Copy, and the borrow checker, with runnable proof at every step."
template = "blog-post.html"
[taxonomies]
categories = ["Engineering Systems"]
tags = ["rust", "swift", "rust-for-swift", "ownership", "move-semantics", "memory-safety", "languages"]
[extra]
editorial_track = "engineering-systems"
series = "rust-for-swift"
+++

The first Rust program I wrote that would not compile was four lines long and,
to my Swift eyes, obviously correct. I made a value, handed it to a function,
and used it again afterward. Swift does this ten thousand times a day without
comment. Rust refused, and the error talked about a "move" as if my value had
gone somewhere. It had. This is the difference that trips every Swift programmer
first, and it is worth slowing all the way down for, because once it clicks, a
surprising amount of Rust stops feeling like a series of arbitrary rules. (This
is the first full stop in the
[Rust for Swift Practitioners](/blog/rust-for-swift-practitioners-overview/)
field guide; start there for the map.)

## Swift copies, Rust moves

In Swift, a `struct` has value semantics. Assign it to a new binding and you get
an independent copy; change one and the other is untouched.

```swift
// In Swift a struct has value semantics: assigning it makes an independent
// copy. Mutating the copy leaves the original untouched. This is the default
// that a Swift programmer takes for granted, and it is exactly where Rust
// diverges (Rust would MOVE, not copy).
struct Point {
    var x: Int
    var y: Int
}

var a = Point(x: 1, y: 2)
var b = a          // copies the value
b.x = 99           // mutates only b
print("a = (\(a.x), \(a.y)), b = (\(b.x), \(b.y))")
```

That prints `a = (1, 2), b = (99, 2)`. The copy is silent and free-feeling, and
it is the reflex you carry into Rust. Now watch Rust take it away. A `String`
owns a heap buffer, so it is not one of the cheap types Rust will duplicate for
you. Plain assignment _moves_ it, and the original binding is gone. This program
is supposed to fail to compile, and it does:

```rust
// A String is moved by a plain assignment. The Swift instinct is that
// `original` is still valid (Swift would copy the value). Rust disagrees: once
// the value has moved into `duplicate`, the compiler forbids touching
// `original` again. This program is SUPPOSED to fail to compile.
fn main() {
    let original = String::from("swift");
    let duplicate = original; // moves; original is now invalid
    println!("original = {original}, duplicate = {duplicate}");
}
```

The compiler is not vague about it:

```text
error[E0382]: borrow of moved value: `original`
```

Nothing was copied. The `String` moved into `duplicate`, and `original` stopped
being a valid name for anything. Swift would have made a second `String`; Rust
made you notice that a heap-owning value has exactly one owner at a time.

## Keeping both means asking out loud

The Swift fix for "I want two of these" is nothing; you already have two. The
Rust fix is to say so explicitly with `.clone()`, which performs the deep copy
that Swift would have done implicitly. The cost is now visible in the source,
which is the whole point:

```rust
// A String owns a heap buffer, so it is NOT Copy. Plain assignment MOVES it,
// which would leave the original unusable. To keep both bindings alive you ask
// for a copy explicitly with `.clone()` (Rust never deep-copies heap data
// behind your back).
fn main() {
    let original = String::from("swift");
    let duplicate = original.clone(); // explicit deep copy
    println!("original = {original}, duplicate = {duplicate}");
}
```

This compiles and prints `original = swift, duplicate = swift`. The lesson a
Swift programmer should take is not "Rust makes you type more." It is that Swift
was making a decision on your behalf (deep-copy this value type) and Rust moved
that decision into the open. For a small `Point` you never think about it; for a
`String`, an array, or a megabyte of pixels, Rust wants the copy to be a thing
you chose.

The same split explains the other half of the Swift world: the `class`. A Swift
class has reference semantics, so two bindings share one instance and a mutation
through either is seen by both.

```swift
// A class is the exception to Swift's value-type default: it has reference
// semantics. Two bindings point at the SAME object, so a mutation through one
// is visible through the other. Rust has no built-in reference type like this;
// sharing there is always spelled out (Rc/Arc) and never implicit.
class Counter {
    var value: Int = 0
}

let first = Counter()
let second = first     // both refer to the same instance
second.value = 7
print("first.value = \(first.value), second.value = \(second.value)")
```

That prints `first.value = 7, second.value = 7`. Swift gives you two default
behaviors depending on whether you reached for `struct` or `class`. Rust gives
you neither for free: owning types move, and if you want the shared-reference
behavior of a Swift class you spell it out (a later post gets to `Rc` and
`Arc`).

## The exception that feels like home

Here is the relief. Not everything moves. Small, plain-old-data types are marked
`Copy`, and they behave exactly like your Swift instinct: assignment duplicates
the bits and the source stays usable. Integers are the headline case.

```rust
// In Rust, integers are Copy: assigning `x` to `y` duplicates the bits, so
// the original binding stays fully usable afterward. This is the behavior a
// Swift programmer expects from `let`, and it is the exception in Rust, not
// the rule.
fn main() {
    let x: i32 = 41;
    let y = x; // copies; x is NOT consumed
    println!("x = {x}, y = {y}");
}
```

This compiles and prints `x = 41, y = 41`, with both bindings alive. It is the
mirror image of the Swift scalar, which does the same:

```swift
// Scalars such as Int are value types too: assignment copies them, so both
// bindings stay usable and independent. Rust agrees here (integers are Copy),
// which is why this one case feels the same in both languages.
var x = 41
var y = x          // copies
y += 1             // changes only y
print("x = \(x), y = \(y)")
```

You can even opt your own small struct back into this world. Derive `Copy` (and
its companion `Clone`) and a `Point` starts behaving like an `i32`: assignment
duplicates it and the source survives.

```rust
// You can opt a small, all-Copy struct back into copy semantics with
// `#[derive(Copy, Clone)]`. Now `Point` behaves like `i32`: assignment
// duplicates it and the source stays usable, matching Swift's value-type feel.
#[derive(Copy, Clone)]
struct Point {
    x: i32,
    y: i32,
}

fn main() {
    let a = Point { x: 1, y: 2 };
    let b = a; // copies because Point is Copy
    println!("a = ({}, {}), b = ({}, {})", a.x, a.y, b.x, b.y);
}
```

So Swift's value-type feeling is not gone from Rust; it is available on request,
for the types where cheap copying is genuinely fine. What changed is the
default. Swift assumes copy and lets reference types be the exception; Rust
assumes move and lets `Copy` be the exception.

## Why the default is worth the trouble

It would be fair to ask what a Swift programmer gets in exchange for giving up
the free copy. The answer is that the same single-owner rule that annoyed me on
the first afternoon is what lets Rust reject data races at compile time, with no
runtime and no garbage collector. The borrow checker extends "one owner" into
"many readers or one writer, never both," and it enforces that as you go. This
is also supposed to fail, and it does:

```rust
// Rust's borrow checker allows many shared (&) borrows OR one exclusive (&mut)
// borrow, never both at once. Holding a shared reference while also trying to
// mutate the value is rejected at compile time. This program is SUPPOSED to
// fail to compile.
fn main() {
    let mut name = String::from("swift");
    let reader = &name; // shared borrow starts
    name.push_str("-rust"); // needs &mut while `reader` is alive
    println!("{reader}");
}
```

```text
error[E0502]: cannot borrow `name` as mutable because it is also borrowed as immutable
```

If that rule feels severe, here is the part that should reassure a Swift
programmer: Swift is walking toward it. Recent Swift added opt-in move-only
values, where a type declared `~Copyable` cannot be silently duplicated and a
`consuming` parameter takes ownership. Consume such a value twice and Swift
rejects it, using very nearly the same reasoning Rust applies to everything:

```swift
// Swift 5.9+ lets you OPT IN to Rust-style move-only values by suppressing
// Copyable with `~Copyable`. Once a noncopyable value is consumed, using it
// again is a compile error, just like Rust's default for every owning type.
// This is the exception in Swift and the rule in Rust. This program is
// SUPPOSED to fail to compile.
struct FileHandle: ~Copyable {
    let name: String
}

func close(_ handle: consuming FileHandle) {
    print("closing \(handle.name)")
}

func run() {
    let handle = FileHandle(name: "log.txt")
    close(handle) // consumes `handle`
    close(handle) // error: `handle` was already consumed
}

run()
```

```text
error: 'handle' consumed more than once
```

That is the whole idea in one comparison. What Swift offers as a specialized,
opt-in tool for the rare type that must not be copied, Rust makes the baseline
for every owning value, and builds its memory safety on top of it.

_The move-versus-copy default is the single unlock for a Swift programmer: once
you stop expecting a free copy and start reading assignment as "this value now
lives over there," the borrow-checker errors turn from obstacles into a running
commentary on ownership. The next posts follow the same thread outward, into
references and `Option`, and then into the concurrency story where this rule
finally pays off (I sketched the destination in
[why Rust needs no actors to be safe across threads](/blog/swift-actor-model-vs-rust-ownership/)).
Start from the value, and the rest of Rust starts to make sense._
