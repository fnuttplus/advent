use std::fs;

type Data = Vec<i64>;

fn isvalid(v: &Data, i: usize) -> bool{
    for j in (i-25)..v.len() {
        for k in (j+1)..i {
            if v[j] + v[k] == v[i] {
                return true
            }
        }
    }
    false
}

fn part1(v: &Data) -> i64 {
    for i in 25..v.len() {
        if !isvalid(v, i) {
            return v[i]
        }
    }
    0
}

fn part2(v: &Data, s: i64) -> i64 {
    for n in 2..v.len() {
        for i in 0..v.len()-n {
            if s == v.iter().skip(i).take(n).sum() {
                let mut min = 0i64;
                match v.iter().skip(i).take(n).min() {
                    Some(i) => min = *i,
                    None => ()
                }
                let mut max = 0i64;
                match v.iter().skip(i).take(n).max() {
                    Some(i) => max = *i,
                    None => ()
                }
                return min + max
            }
        }
    }
    0
}

fn parse(dd: &mut Data) {
    let s = fs::read_to_string("09.in").expect("");
    for ss in s.split("\n") {
        dd.push(ss.parse().unwrap());
    }
    //println!("{:?}", dd);
}

pub fn run() {
    let mut v: Data = vec![];
    parse(&mut v);

    let part1 = part1(&v);
    println!("PART 1: {}", part1);
    println!("PART 2: {}", part2(&v, part1));
}

#[test]
fn test09() {
    let mut v: Data = vec![];
    parse(&mut v);

    let part1 = part1(&v);
    assert_eq!(part1, 138879426);
    assert_eq!(part2(&v, part1), 23761694);
}
