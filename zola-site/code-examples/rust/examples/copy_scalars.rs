// In Rust, integers are Copy: assigning `x` to `y` duplicates the bits, so
// the original binding stays fully usable afterward. This is the behavior a
// Swift programmer expects from `let`, and it is the exception in Rust, not
// the rule.
fn main() {
    let x: i32 = 41;
    let y = x; // copies; x is NOT consumed
    println!("x = {x}, y = {y}");
}
