// A String is moved by a plain assignment. The Swift instinct is that
// `original` is still valid (Swift would copy the value). Rust disagrees: once
// the value has moved into `duplicate`, the compiler forbids touching
// `original` again. This program is SUPPOSED to fail to compile.
fn main() {
    let original = String::from("swift");
    let duplicate = original; // moves; original is now invalid
    println!("original = {original}, duplicate = {duplicate}");
}
