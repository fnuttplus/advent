use std::fs;

type Data = (usize, usize);

fn part(v: &Data) -> usize {
    let n = 7;
    let mut a = 1;
    let mut i = 1;
    loop {
        i = (i * n) % 20201227;
        if i == v.0 { break }
        a += 1;
    }

    i = 1;
    for _ in 0..a {
        i = (i * v.1) % 20201227;
    }

    i
}

fn parse(v: &mut Data) {
    let s = fs::read_to_string("25.in").expect("file not found");
    let ss:Vec<usize> = s.split("\n").map(|x| x.parse().unwrap()).collect();
    v.0 = ss[0];
    v.1 = ss[1];
    //println!("{:?}", v);
}

pub fn run() {
    let mut v: Data = (0,0);
    parse(&mut v);

    println!("PART 1: {}", part(&v));
}

#[test]
fn test25() {
    let mut v: Data = (0,0);
    parse(&mut v);

    assert_eq!(part(&v), 17980581);
}
