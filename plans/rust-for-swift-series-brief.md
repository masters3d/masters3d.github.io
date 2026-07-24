# Series brief: Rust for Swift Practitioners

A shared reference for every post (and every sub-agent) in the **Rust for Swift
Practitioners** series. Keep this file in sync as the series grows.

## Thesis

A reader fluent in Swift, new to Rust, keeps reaching for a Swift mental model
and finding it missing, renamed, or inverted. Each post names the Swift model
first, shows exactly where Rust diverges, and gives the idiomatic Rust
alternative. The recurring emotional beat is "I know how to express this in
Swift; where did it go in Rust?"

## Framing rules

- **Swift-anchored.** Open from the Swift practitioner's expectation, then cross
  into Rust. Never explain Rust as if from scratch.
- **Concrete before abstract.** Lead with a runnable example, then name the
  rule it demonstrates.
- **Original throughout.** This series is modeled on the _idea_ of Doug Gregor's
  "Swift for C++ Practitioners" (topic scaffold only). Do not reproduce his
  prose or examples. Each post links to his series as attribution/inspiration.
- **Every code block is real.** All ```rust / ```swift blocks must be copied
  verbatim from a verified file under `zola-site/code-examples/`. Illustrative
  fragments use ```text. See `code-examples/README.md`.

## House style (from plans/agents.md)

- Quest Arc: personal-observation opening → 3-4 `##` sections (no `###`) →
  italicized closing reflection that cross-links.
- Parentheses, not em-dashes. Avoid the words "impact" and "stupid".
- Editorial track: **Engineering Systems** for every post
  (`categories = ["Engineering Systems"]`, `editorial_track = "engineering-systems"`).
- Series wiring: `extra.series = "rust-for-swift"` plus a `rust-for-swift` tag.
  The reading-order badge is derived from post date order at build time
  (see `templates/partials/editorial-track.html`); do not store an order number.
- Slugs: `rust-for-swift-<topic>.md`.

## Swift -> Rust glossary (living)

| Swift | Rust | One-line gotcha |
| --- | --- | --- |
| struct copies on assignment | move by default; `Copy`/`Clone` opt-in | scalars are `Copy`, most types move |
| `class` (ARC shared ref) | no default reference type; `&T`, `Rc`, `Arc` | sharing is always explicit |
| `Optional` / `nil` | `Option<T>` | no implicit unwrap, no optional chaining |
| `extension` on any type | `impl` + traits, orphan rule | you cannot add a foreign trait to a foreign type |
| protocol with associated type | trait with associated type / generics | `any P` is not the same as `dyn Trait` |
| `any P` / metatypes / reflection | `dyn Trait`, object safety, no runtime metatypes | erased types are limited by object safety |
| `throws` / `try` / `do-catch` | `Result<T, E>`, `?`, `panic!` | no exceptions |
| closures capture by reference (ARC) | `Fn`/`FnMut`/`FnOnce`, `move` | capture interacts with the borrow checker |
| lazy globals | `const` / `static`, `OnceLock`, `Mutex` | no mutable global without a lock or `unsafe` |
| `ExpressibleBy*Literal` | `From`/`Into`, literal inference | no literal protocols |
| operator functions | `std::ops` traits | coherence rules apply |
| result builders (SwiftUI) | `macro_rules!` / proc-macros | macros are the DSL mechanism |
| `consuming` / `~Copyable` (opt-in) | move is the default | the inversion at the heart of the series |
| `Unsafe*Pointer`, `MemoryLayout` | `unsafe`, `repr(C)`, slices | no flexible array member |
| built-in concurrency runtime (Task) | `async`/`await` is only syntax | Rust has no default async runtime (tokio/async-std) |
| `actor` isolation | `Send`/`Sync`, `Arc<Mutex<T>>` | data-race freedom is checked by the compiler, not a runtime |

## Post map and status

Two arcs. Arc 1 is the highest-value "model shift"; Arc 2 is the type-system
toolkit. Ship each post as its own PR against `master`.

| # | Slug | Topic | Arc | Status |
| --- | --- | --- | --- | --- |
| 0 | rust-for-swift-practitioners-overview | Series overview / thesis | - | shipped (this PR) |
| 1 | rust-for-swift-value-types-copy-vs-move | Value types: copy vs move | 1 | shipped (this PR) |
| 2 | rust-for-swift-references-and-optionals | References and optionals | 1 | planned |
| 3 | rust-for-swift-move-by-default | Move semantics (the inversion) | 1 | planned |
| 4 | rust-for-swift-closures | Closures and capture | 1 | planned |
| 5 | rust-for-swift-globals | Globals and shared mutable state | 1 | planned |
| 6 | rust-for-swift-send-sync | Send/Sync and fearless concurrency | 1 | planned |
| 7 | rust-for-swift-extensions-orphan-rule | Extensions, traits, orphan rule | 2 | planned |
| 8 | rust-for-swift-generics-and-traits | Generics and trait bounds | 2 | planned |
| 9 | rust-for-swift-type-erasure | Type erasure: `dyn` and object safety | 2 | planned |
| 10 | rust-for-swift-error-handling | Error handling: `Result` and `?` | 2 | planned |
| 11 | rust-for-swift-literals | Extensible literals | 2 | planned |
| 12 | rust-for-swift-operators | Operator overloading | 2 | planned |
| 13 | rust-for-swift-macros-as-dsls | Result builders vs macros | 2 | planned |
| 14 | rust-for-swift-unsafe-and-layout | Unsafe and memory layout | 2 | planned |
| 15 | rust-for-swift-no-async-runtime | No built-in async runtime | 2 | planned |

## Cross-links to reuse

- `/blog/swift-actor-model-vs-rust-ownership/` (concurrency anchor; the
  Send/Sync post points here rather than duplicating it)
- `/blog/sharing-one-core-across-languages/`
- `/blog/swift-journey-why-not-professional/`
- Doug Gregor's series (attribution): https://www.douggregor.net/posts/

## Per-post pipeline (sub-agents)

1. **Spec** - outline honoring the Quest Arc + a code-example spec (what each
   snippet demonstrates, its expected output, which are intentional failures).
2. **Example** - write the real files under `code-examples/`, add fixtures, get
   `verify.py` green before any prose.
3. **Draft** - write the post in house voice, pasting the verified snippets and
   cross-linking neighbors.
4. **Review** - check voice-guide compliance, technical accuracy, and that both
   the PR-validation and code-examples CI jobs pass.
