use std::io::{BufRead, BufReader};
use std::fs::File;

fn part1 (v: &Vec<Vec<i32>>, dx: usize, dy: usize) -> i32 {
    let mut i = 0;
    let mut x = 0;
    let mut y = 0;
    while y+dy < v.len() {
        y += dy;
        x += dx;
        if x >= v[y].len() {
            x -= v[y].len();
        }
        i += v[y][x];
    }
    i
}

fn part2 (v: &Vec<Vec<i32>>) -> i32 {
    let mut p = 1;
    p *= part1(v, 1, 1);
    p *= part1(v, 3, 1);
    p *= part1(v, 5, 1);
    p *= part1(v, 7, 1);
    p *= part1(v, 1, 2);
    p
}

fn parse (dd: &mut Vec<Vec<i32>>) {
    let reader = BufReader::new(File::open("03.in").expect("Cannot open file"));
    for line in reader.lines() {
        let mut v: Vec<i32> = vec![];
        for c in line.unwrap().chars() {
            if c == '#' {
                v.push(1);
            } else {
                v.push(0);
            }
        }
        dd.push(v);
    }
    //println!("{:?}", dd);
}

pub fn run() {
    let mut v: Vec<Vec<i32>> = vec![];
    parse(&mut v);

    println!("PART 1: {}", part1(&v, 3, 1));
    println!("PART 2: {}", part2(&v));
}

#[test]
fn test03() {
    let mut v: Vec<Vec<i32>> = vec![];
    parse(&mut v);

    assert_eq!(part1(&v, 3, 1), 237);
    assert_eq!(part2(&v), 2106818610);
}
