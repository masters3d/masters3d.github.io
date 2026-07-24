// Scalars such as Int are value types too: assignment copies them, so both
// bindings stay usable and independent. Rust agrees here (integers are Copy),
// which is why this one case feels the same in both languages.
var x = 41
var y = x          // copies
y += 1             // changes only y
print("x = \(x), y = \(y)")
