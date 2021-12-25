use std::time::{Instant};

mod day01;
mod day02;
mod day03;

fn run(day: &str, f: &dyn Fn()) {
    println!("DAY {}", day);
    let start = Instant::now();
    f();
    println!("{:?}", start.elapsed());
    println!();
}

fn main() {
    run("01", &day01::run);
    run("02", &day02::run);
    run("03", &day03::run);
}
