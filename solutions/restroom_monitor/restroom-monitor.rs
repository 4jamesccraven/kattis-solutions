use std::error::Error;
use std::io;
use std::collections::VecDeque;


fn deque(queue: &mut VecDeque<i32>) {
    match queue.pop_front() {
        Some(_) => return,
        None => {
            println!("Yes");
            std::process::exit(0);
        }
    }
}

fn main() -> Result<(), Box<dyn Error>> {
    let mut need: Vec<i32> = Vec::new();
    let mut dont_need: Vec<i32> = Vec::new();

    let mut line: String = String::new();
    
    io::stdin().read_line(&mut line)?;

    let mut vals = line.split_whitespace();
    let stalls: i32 = vals.next().ok_or("25")?.parse()?;
    let count: i32 = vals.next().ok_or("26")?.parse()?;

    for _i in 0..count {
        line.clear();
        io::stdin().read_line(&mut line)?;
        vals = line.split_whitespace();
        let deadline: i32 = vals.next().ok_or("32")?.parse()?;
        let needed = vals.next().ok_or("33")? == "y";

        if needed {
            need.push(deadline);
        } else {
            dont_need.push(deadline);
        }
    }

    need.sort();
    dont_need.sort();    

    let mut need: VecDeque<i32> = VecDeque::from_iter(need);
    let mut dont_need: VecDeque<i32> = VecDeque::from_iter(dont_need);


    let lt_stalls: i32 = stalls - 1;
    let mut time: i32 = 0;
    loop {
        time += 1;

        if need.iter().any(|&s| s < time) || dont_need.iter().any(|&s| s < time) {
            println!("No");
            return Ok(());
        }

        if !need.is_empty() {
            deque(&mut need);
            for _i in 0..lt_stalls {
                deque(&mut dont_need);
            }
        } else if !dont_need.is_empty() {
            for _i in 0..stalls {
                deque(&mut dont_need);
            }
        } else {
            println!("Yes");
            return Ok(());
        }
    }
}
