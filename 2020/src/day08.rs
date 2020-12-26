use std::fs;
use std::fmt;
use std::collections::HashSet;

type Data = Vec<Ins>;

struct Ins {
    op: String,
    arg: isize
}

impl fmt::Debug for Ins {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{} {}", self.op, self.arg)
    }
}

fn part1(v: &Data) -> (bool, isize) {
    let mut s: HashSet<isize> = HashSet::new();
    let mut acc = 0;
    let mut ip: isize = 0;

    loop {
        if ip >= v.len() as isize {
            return (true, acc)
        }
        if s.contains(&ip) {
            return (false, acc)
        }
        s.insert(ip);
        match v[ip as usize].op.as_str() {
            "nop" => {
                ip += 1
            },
            "acc" => {
                acc += v[ip as usize].arg;
                ip += 1
            },
            "jmp" => {
                ip += v[ip as usize].arg
            },
            _ => ()
        }
    }
}

fn part2(v: &mut Data) -> isize {
    for i in 0..v.len() {
        if v[i].op == "nop" { v[i].op = "jmp".to_string() }
        else if v[i].op == "jmp" { v[i].op = "nop".to_string() }
        else { continue }
        let (a, b) = part1(v);
        if a {
            return b
        }
        if v[i].op == "nop" { v[i].op = "jmp".to_string() }
        else if v[i].op == "jmp" { v[i].op = "nop".to_string() }
    }
    0
}

fn parse(dd: &mut Data) {
    let s = fs::read_to_string("08.in").expect("");
    for ss in s.split("\n") {
        let a: Vec<&str> = ss.split(' ').collect();
        let ins = Ins {
            op: a[0].to_string(),
            arg: a[1].trim_start_matches('+').parse().unwrap()
        };
        dd.push(ins);
    }
    //println!("{:?}", dd);
}

pub fn run() {
    let mut v: Data = vec![];
    parse(&mut v);

    println!("PART 1: {}", part1(&v).1);
    println!("PART 2: {}", part2(&mut v));
}

#[test]
fn test08() {
    let mut v: Data = vec![];
    parse(&mut v);

    assert_eq!(part1(&v).1, 1818);
    assert_eq!(part2(&mut v), 631);
}
