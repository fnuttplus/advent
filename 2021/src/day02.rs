use std::io::{BufRead, BufReader};
use std::fs::File;

struct Data {
    a: String,
    b: usize,
}

fn part1 (v: &Vec<Data>) -> usize {
    let mut horizontal = 0;
    let mut depth = 0;
    for d in v {
        match d.a.as_str() {
            "up" => {
                depth -= d.b
            },
            "down" => {
                depth += d.b
            },
            "forward" => {
                horizontal += d.b
            },
            _ => {}
        }
    }
    horizontal * depth
}

fn part2 (v: &Vec<Data>) -> usize {
    let mut horizontal = 0;
    let mut depth = 0;
    let mut aim = 0;
    for d in v {
        match d.a.as_str() {
            "up" => {
                aim -= d.b;
            },
            "down" => {
                aim += d.b;
            },
            "forward" => {
                horizontal += d.b;
                depth += aim * d.b;
            },
            _ => {}
        }
    }
    horizontal * depth
}

fn parse (dd: &mut Vec<Data>) {
    let reader = BufReader::new(File::open("input/2021_02_input.txt").expect("Cannot open file"));
    for line in reader.lines() {
        let s = line.unwrap();
        let v: Vec<&str> = s.split(' ').collect();
        let d = Data {
            a: v[0].to_string(),
            b: v[1].parse().unwrap(),
        };
        dd.push(d);
    }
}

pub fn run() {
    let mut v: Vec<Data> = vec![];
    parse(&mut v);

    println!("PART 1: {}", part1(&v));
    println!("PART 2: {}", part2(&v));
}

#[test]
fn test02() {
    let mut v: Vec<Data> = vec![];
    parse(&mut v);

    assert_eq!(part1(&v), 1604850);
    assert_eq!(part2(&v), 1685186100);
}
