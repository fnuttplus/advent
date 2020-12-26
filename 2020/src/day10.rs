use std::fs;

type Data = Vec<i64>;

fn part1(v: &Data) -> i64 {
    let mut ones = 0;
    let mut threes = 0;
    let mut n = 0;
    for vv in v {
        if vv - n == 1 {
            ones += 1
        } else if vv - n == 3 {
            threes += 1
        }
        n = *vv
    }
    ones * threes
}

fn part2(v: &Data) -> i64 {
    let mut streak = 0;
    let mut n = 0;
    let mut p = 1;
    let d = [2,4,7];
    for vv in v {
        if vv - n == 1 {
            streak += 1
        } else if vv - n == 3 {
            if streak > 1 {
                p *= d[streak-2]
            }
            streak = 0
        }
        n = *vv
    }
    p
}

fn parse(dd: &mut Data) {
    let s = fs::read_to_string("10.in").expect("file not found");
    for ss in s.split("\n") {
        dd.push(ss.parse().unwrap());
    }
    dd.sort();
    dd.push(dd.last().expect("list empty") + 3);
    //println!("{:?}", dd);
}

pub fn run() {
    let mut v: Data = vec![];
    parse(&mut v);

    println!("PART 1: {}", part1(&v));
    println!("PART 2: {}", part2(&v));
}

#[test]
fn test10() {
    let mut v: Data = vec![];
    parse(&mut v);

    assert_eq!(part1(&v), 2070);
    assert_eq!(part2(&v), 24179327893504);
}
