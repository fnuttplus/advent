use std::fs;

type Data = Vec<Vec<usize>>;

fn term1(v: &Vec<usize>, i: &mut usize) -> usize {
    let a = 
        if peek(v, i, 12) { exp1(v, i) }
        else { v[*i] };
    *i += 1;
    a
}

fn exp1(v: &Vec<usize>, i: &mut usize) -> usize {
    let mut a = term1(v, i);
    loop {
        if peek(v, i, 10) { a += term1(v, i) }
        else if peek(v, i, 11) { a *= term1(v, i) }
        else { break }
    }
    a
}

fn part1(v: &Data) -> usize {
    let mut n = 0;
    for vv in v { n += exp1(vv, &mut 0) }
    n
}

fn peek(v: &Vec<usize>, i: &mut usize, c: usize) -> bool {
    if (*i) < v.len() && v[*i] == c {
        *i += 1;
        return true
    }
    false
}

fn term(v: &Vec<usize>, i: &mut usize) -> usize {
    let a = 
        if peek(v, i, 12) { exp(v, i) }
        else { v[*i] };
    *i += 1;
    a
}

fn summa(v: &Vec<usize>, i: &mut usize) -> usize {
    let mut a = term(v, i);
    while peek(v, i, 10) { a += term(v, i) }
    a
}

fn exp(v: &Vec<usize>, i: &mut usize) -> usize {
    let mut a = summa(v, i);
    while peek(v, i, 11) { a *= summa(v, i) }
    a
}

fn part2(v: &Data) -> usize {
    let mut n = 0;
    for vv in v { n += exp(vv, &mut 0) }
    n
}

fn token(c: char) -> usize {
    match c {
        '0' => 0,
        '1' => 1,
        '2' => 2,
        '3' => 3,
        '4' => 4,
        '5' => 5,
        '6' => 6,
        '7' => 7,
        '8' => 8,
        '9' => 9,
        '+' => 10,
        '*' => 11,
        '(' => 12,
        ')' => 13,
        _ => 14
    }
}

fn parse(v: &mut Data) {
    let s = fs::read_to_string("18.in").expect("file not found");
    for ss in s.split("\n") {
        v.push(ss.chars().filter(|x| *x != ' ').map(|x| token(x)).collect());
    }
    //println!("{:?}", v);
}

pub fn run() {
    let mut v: Data = vec![];
    parse(&mut v);

    println!("PART 1: {}", part1(&v));
    println!("PART 2: {}", part2(&v));
}

#[test]
fn test18() {
    let mut v: Data = vec![];
    parse(&mut v);

    assert_eq!(part1(&v), 30753705453324);
    assert_eq!(part2(&v), 244817530095503);
}
