// A String owns a heap buffer, so it is NOT Copy. Plain assignment MOVES it,
// which would leave the original unusable. To keep both bindings alive you ask
// for a copy explicitly with `.clone()` (Rust never deep-copies heap data
// behind your back).
fn main() {
    let original = String::from("swift");
    let duplicate = original.clone(); // explicit deep copy
    println!("original = {original}, duplicate = {duplicate}");
}
