use std::cmp::Ordering;
use std::io::{self, Read};

fn main() {
    let mut stdin = io::stdin();
    let _ = stdin.lock();

    let mut inp = String::new();
    stdin.read_to_string(&mut inp)
        .unwrap();

    let nums: Vec<isize> = inp.lines()
        .filter_map(|x| x.parse().ok())
        .collect();

    let to_print = match nums[0].cmp(&nums[1]) {
        Ordering::Less => "FAKE NEWS!",
        Ordering::Equal => "WORLD WAR 3!",
        Ordering::Greater => "MAGA!",
    };

    println!("{to_print}");
}
