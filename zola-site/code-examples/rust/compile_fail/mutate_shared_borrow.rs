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
