// You can opt a small, all-Copy struct back into copy semantics with
// `#[derive(Copy, Clone)]`. Now `Point` behaves like `i32`: assignment
// duplicates it and the source stays usable, matching Swift's value-type feel.
#[derive(Copy, Clone)]
struct Point {
    x: i32,
    y: i32,
}

fn main() {
    let a = Point { x: 1, y: 2 };
    let b = a; // copies because Point is Copy
    println!("a = ({}, {}), b = ({}, {})", a.x, a.y, b.x, b.y);
}
