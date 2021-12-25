use std::io::{BufRead, BufReader};
use std::fs::File;

fn part1 (v: &Vec<i32>) -> i32 {
    let mut a = v[0];
    let mut n = 0;
    for i in 1..v.len() {
        if v[i] > a {
            n += 1;
        }
        a = v[i];
    }
    n
}

fn part2 (v: &Vec<i32>) -> i32 {
    let mut a = v[0] + v[1];
    let mut b = v[1] + v[2];
    let mut n = 0;
    for i in 3..v.len() {
        a += v[i-1];
        b += v[i];
        if b > a {
            n += 1;
        }
        a -= v[i-3];
        b -= v[i-2];
    }
    n
}

fn parse(v: &mut Vec<i32>) {
    let reader = BufReader::new(File::open("input/2021_01_input.txt").expect("Cannot open file"));
    for line in reader.lines() {
        v.push(line.unwrap().parse().unwrap());
    }
}

pub fn run() {
    let mut v: Vec<i32> = vec![];
    parse(&mut v);

    println!("PART 1: {}", part1(&v));
    println!("PART 2: {}", part2(&v));
}

#[test]
fn test01() {
    let mut v: Vec<i32> = vec![];
    parse(&mut v);

    assert_eq!(part1(&v), 1548);
    assert_eq!(part2(&v), 1589);
}
