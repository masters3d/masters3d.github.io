# Runnable code examples

Every Swift and Rust snippet shown in the **Rust for Swift Practitioners** blog
series lives here as a real, compilable source file. CI compiles and runs each
one and asserts its behavior, so a post can never claim something the code does
not actually do. A second check confirms that the code fences printed in the
posts are byte-identical to these files, so prose and compiled code stay in
sync.

## Layout

```
code-examples/
  verify.py                     the checker (pure Python 3 standard library)
  rust/
    Cargo.toml                  no dependencies (std only, so CI needs no network)
    src/lib.rs                  empty support crate
    examples/<name>.rs          runnable snippet (cargo run --example <name>)
    expected/<name>.out         its exact expected stdout
    compile_fail/<name>.rs      code that MUST be rejected by rustc
    compile_fail/<name>.err     a substring the compiler error must contain
  swift/
    snippets/<name>.swift       runnable snippet (swift <file>)
    expected/<name>.out         its exact expected stdout
    compile_fail/<name>.swift   code that MUST be rejected by swiftc
    compile_fail/<name>.err     a substring the compiler error must contain
```

## Running the checks

```bash
cd zola-site/code-examples
python3 verify.py            # compile + run + sync (needs cargo, rustc, swift)
python3 verify.py --rust     # only Rust
python3 verify.py --swift    # only Swift
python3 verify.py --sync     # only the post <-> file byte-sync check
```

`--sync` needs no toolchain, so prose-only edits can be validated without Rust
or Swift installed. The GitHub Actions workflow `.github/workflows/code-examples.yml`
runs the full set on any change under `code-examples/**` or to a
`rust-for-swift-*` post.

## Adding a snippet to a post

1. Add the source file under the right directory (`examples/`, `snippets/`, or a
   `compile_fail/` folder) so it is a complete program.
2. Add its `expected/<name>.out` (runnable) or `compile_fail/<name>.err`
   (rejected) fixture. Generate the value by running the program / compiler
   locally, then commit exactly what it produced.
3. Run `python3 verify.py` until it is green.
4. In the post, paste the **exact** file contents into a fenced block tagged
   ```` ```rust ```` or ```` ```swift ````. The sync check enforces the match.
   Fragments that are only illustrative (a lone type signature, pseudo-code) use
   ```` ```text ```` so they are skipped.
