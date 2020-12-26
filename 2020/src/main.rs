use std::time::{Instant};

mod day01;
mod day02;
mod day03;
mod day04;
mod day05;
mod day06;
mod day07;
mod day08;
mod day09;
mod day10;
mod day11;
mod day12;
mod day13;
mod day14;
mod day15;
mod day16;
mod day17;
mod day18;
mod day19;
mod day20;
mod day21;
mod day22;
mod day23;
mod day24;
mod day25;

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
    run("04", &day04::run);
    run("05", &day05::run);
    run("06", &day06::run);
    run("07", &day07::run);
    run("08", &day08::run);
    run("[9]", &day09::run);
    run("10", &day10::run);
    run("11", &day11::run);
    run("12", &day12::run);
    run("13", &day13::run);
    run("14", &day14::run);
    run("15", &day15::run);
    run("16", &day16::run);
    run("17", &day17::run);
    run("18", &day18::run);
    run("19", &day19::run);
    run("20", &day20::run);
    run("21", &day21::run);
    run("22", &day22::run);
    run("23", &day23::run);
    run("24", &day24::run);
    run("25", &day25::run);
}
