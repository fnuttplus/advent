use std::fs::File;
use std::io::{BufRead, BufReader};

type Data = Vec<isize>;

fn part1(v: &Data) -> isize {
    let mut i = 0;
    for vv in v {
        if *vv > i {
            i = *vv
        }
    }
    i
}

fn part2(v: &Data) -> isize {
    for vv in v {
        if !v.contains(&(vv - 1)) {
            return vv - 1;
        }
    }
    0
}

fn parse(dd: &mut Data) {
    let reader = BufReader::new(File::open("05.in").expect("Cannot open file"));
    for line in reader.lines() {
        let s: String = line.unwrap().chars()
            .map(|c| match c {
                'F' => '0',
                'B' => '1',
                'L' => '0',
                'R' => '1',
                _ => ' ',
            })
            .collect();
        let y = isize::from_str_radix(&s[0..7], 2).unwrap();
        let x = isize::from_str_radix(&s[7..], 2).unwrap();
        dd.push(y * 8 + x);
    }
}

pub fn run() {
    let mut v: Data = vec![];
    parse(&mut v);

    println!("PART 1: {}", part1(&v));
    println!("PART 2: {}", part2(&v));
}

#[test]
fn test05() {
    let mut v: Data = vec![];
    parse(&mut v);

    assert_eq!(part1(&v), 913);
    assert_eq!(part2(&v), 717);
}
