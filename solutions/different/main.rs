use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input)
        .expect("Failed to read input");

    for line in input.lines() {
        let nums: Vec<i128> = line.split_whitespace()
            .map(|x| x.parse::<i128>().unwrap())
            .collect();

        let diff = (nums[0] - nums[1]).abs();

        println!("{}", diff);
    }
}
