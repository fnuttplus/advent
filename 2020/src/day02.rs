use std::io::{BufRead, BufReader};
use std::fs::File;

struct Data {
    a: usize,
    b: usize,
    c: char,
    d: String
}

fn part1 (v: &Vec<Data>) -> i32 {
    let mut i = 0;
    for d in v {
        let c = d.d.matches(d.c).count();
        if c >= d.a && c <= d.b {
            i += 1;
        }
    }
    i
}

fn part2 (v: &Vec<Data>) -> i32 {
    let mut i = 0;
    for d in v {
        let a = d.d.chars().nth(d.a-1).unwrap();
        let b = d.d.chars().nth(d.b-1).unwrap();
        if (a == d.c || b == d.c) && a != b {
            i += 1;
        }
    }
    i
}

fn parse (dd: &mut Vec<Data>) {
    let reader = BufReader::new(File::open("02.in").expect("Cannot open file"));
    for line in reader.lines() {
        let s = line.unwrap();
        let v: Vec<&str> = s.split(' ').collect();
        let a: Vec<&str> = v[0].split('-').collect();
        let d = Data {
            a: a[0].parse().unwrap(),
            b: a[1].parse().unwrap(),
            c: v[1].chars().nth(0).unwrap(),
            d: v[2].to_string()
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

    assert_eq!(part1(&v), 560);
    assert_eq!(part2(&v), 303);
}
