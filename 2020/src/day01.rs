use std::io::{BufRead, BufReader};
use std::fs::File;

fn part1 (v: &Vec<i32>) -> i32 {
    for i in 0..v.len() {
        for j in (i+1)..v.len() {
            if v[i] + v[j] == 2020 {
                return v[i]*v[j];
            }
        }
    }
    0
}

fn part2 (v: &Vec<i32>) -> i32 {
    for i in 0..v.len() {
        for j in (i+1)..v.len() {
            for k in (j+1)..v.len() {
                if v[i] + v[j] + v[k] == 2020 {
                    return v[i]*v[j]*v[k];
                }
            }
        }
    }
    0
}

fn parse(v: &mut Vec<i32>) {
    let reader = BufReader::new(File::open("01.in").expect("Cannot open file"));
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

    assert_eq!(part1(&v), 1014624);
    assert_eq!(part2(&v), 80072256);
}
