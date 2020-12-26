use std::fs;
use std::collections::HashSet;

type Data = Vec<Vec<HashSet<char>>>;

fn part1(v: &Data) -> usize {
    let mut i = 0;
    let mut s: HashSet<char>;
    for vv in v {
        s = HashSet::new();
        for vvv in vv {
            s = s.union(&vvv).cloned().collect();
        }
        i += s.len()
    }
    i
}

fn part2(v: &Data) -> usize {
    let mut i = 0;
    let mut s: HashSet<char> = HashSet::new();
    for vv in v {
        s = s.union(vv.first().expect("")).cloned().collect();
        for vvv in vv {
            s = s.intersection(&vvv).cloned().collect();
        }
        i += s.len()
    }
    i
}

fn parse(dd: &mut Data) {
    let s = fs::read_to_string("06.in").expect("");
    for ss in s.split("\n\n") {
        let a = ss.split('\n').map(|x| x.chars().collect()).collect();
        dd.push(a);
    }
    //println!("{:?}", dd);
}

pub fn run() {
    let mut v: Data = vec![];
    parse(&mut v);

    println!("PART 1: {}", part1(&v));
    println!("PART 2: {}", part2(&v));
}

#[test]
fn test06() {
    let mut v: Data = vec![];
    parse(&mut v);

    assert_eq!(part1(&v), 6742);
    assert_eq!(part2(&v), 3447);
}
