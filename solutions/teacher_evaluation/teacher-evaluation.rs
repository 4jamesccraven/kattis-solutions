fn main() {
    let mut input = String::new();

    std::io::stdin()
        .read_line(&mut input)
        .unwrap();

    let mut vals = input.split_whitespace();

    vals.next();

    let desired_avg: u32 = vals.next()
        .unwrap()
        .parse()
        .unwrap();

    input.clear();

    std::io::stdin()
        .read_line(& mut input)
        .unwrap();

    let mut vals: Vec<u32> = input
        .split_whitespace()
        .map(|s| s.parse::<u32>().unwrap())
        .collect();

    let mut additions: u32 = 0;

    let mut average: f64 = vals.iter().sum::<u32>() as f64 / vals.iter().count() as f64;

    if desired_avg == 100 {
        println!("impossible");
    }
    else {
        while average < desired_avg as f64 {
            vals.push(100);
            additions += 1;
            average = vals.iter().sum::<u32>() as f64 / vals.iter().count() as f64;
        }

    println!("{}", additions);
    }
}
