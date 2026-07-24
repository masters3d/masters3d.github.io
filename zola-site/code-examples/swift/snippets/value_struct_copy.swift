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
