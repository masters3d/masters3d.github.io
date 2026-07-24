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
