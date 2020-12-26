use std::fs;

type Data = (i64, Vec<i64>);

fn modulus (a: i64, b: i64) -> i64 {
    return ((a % b) + b) % b
}

fn part1(v: &Data) -> i64 {
    let mut a = modulus(v.1[0] - v.0, v.1[0]);
    let mut b = v.1[0];
    for i in 1..v.1.len() {
        if v.1[i] == -1 { continue }
        if modulus(v.1[i] - v.0, v.1[i]) < a {
            a = modulus(v.1[i] - v.0, v.1[i]);
            b = v.1[i];
        }
    }
    return a * b
}

fn part2(v: &Data) -> i64 {
    let mut m = v.1[0];
    let mut x = m;
    for i in 1..v.1.len() {
        if v.1[i] == -1 { continue }
        while modulus(x, v.1[i]) != modulus(v.1[i] - i as i64, v.1[i]) {
            x += m
        }
        m *= v.1[i]
    }
    x
}

fn parse(v: &mut Data) {
    let s = fs::read_to_string("13.in").expect("file not found");
    let ss: Vec<&str> = s.split("\n").collect();
    v.0 = ss[0].parse().unwrap();
    v.1 = ss[1].split(',').map(|x| match x {
        "x" => -1,
        _ => x.parse().unwrap()
    }).collect();
    //println!("{:?}", v);
}

pub fn run() {
    let mut v: Data = (0, vec![]);
    parse(&mut v);

    println!("PART 1: {}", part1(&v));
    println!("PART 2: {}", part2(&v));
}

#[test]
fn test13() {
    let mut v: Data = (0, vec![]);
    parse(&mut v);

    assert_eq!(part1(&v), 259);
    assert_eq!(part2(&v), 210612924879242);
}
