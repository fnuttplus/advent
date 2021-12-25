use std::io::{BufRead, BufReader};
use std::fs::File;

type Data = Vec<Vec<usize>>;

fn part1 (v: &Data) -> usize {
    let l = v.len();
    let mut gamma = 0;
    let mut epsilon = 0;
    for a in 0..v[0].len() {
        let mut c = 0;
        for b in 0..v.len() {
            c += v[b][a];
        }
        if c > l/2 {
            gamma |= 1 << (v[0].len() - a - 1);
        } else {
            epsilon |= 1 << (v[0].len() - a - 1);
        }
        //println!("{} {:b} {:b} {}", c, gamma, epsilon, gamma * epsilon);
    }
    gamma * epsilon
}

fn part2 (v: &Data) -> usize {
    v.len()
}

fn parse (dd: &mut Data) {
    let reader = BufReader::new(File::open("input/2021_03_input.txt").expect("Cannot open file"));
    for line in reader.lines() {
        let s = line.unwrap();
        let v: Vec<usize> = s.chars().map(|c| match c {
            '1' => 1,
            _ => 0,
        }).collect();
        dd.push(v);
    }
}

pub fn run() {
    let mut v: Data = vec![];
    parse(&mut v);

    println!("PART 1: {}", part1(&v));
    println!("PART 2: {}", part2(&v));
}

#[test]
fn test02() {
    let mut v: Data = vec![];
    parse(&mut v);

    assert_eq!(part1(&v), 3429254);
    assert_eq!(part2(&v), 5410338);
}
