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
