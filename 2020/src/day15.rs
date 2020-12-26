use std::fs;

struct Data {
    n: usize,
    i: usize,
    mem: Box<[(usize, usize)]>
}

fn part1(v: &mut Data, n: usize) -> usize {
    let mut c = v.n;
    for i in v.i..n+1 {
        let (a,b) = v.mem[c];
        c = if b == 0 { 0 } else { a-b };
        v.mem[c] = (i, v.mem[c].0);
    }
    v.i = n+1;
    v.n = c;
    v.n
}

fn parse(v: &mut Data) {
    let s = fs::read_to_string("15.in").expect("file not found");
    let mut i = 0;
    for ss in s.split(",") {
        v.n = ss.parse().unwrap();
        v.mem[v.n as usize] = (i+1, 0);
        i += 1;
    }
    v.i = i+1;
    //println!("{:?}", v.n);
}

pub fn run() {
    let mut v = Data {
        n: 0,
        i: 0,
        mem: vec![(0usize, 0usize);30000000].into_boxed_slice()
    };
    parse(&mut v);

    println!("PART 1: {}", part1(&mut v, 2020));
    println!("PART 2: {}", part1(&mut v, 30000000));
}

#[test]
fn test15() {
    let mut v = Data {
        n: 0,
        i: 0,
        mem: vec![(0usize, 0usize);30000000].into_boxed_slice()
    };
    parse(&mut v);

    assert_eq!(part1(&mut v, 2020), 1015);
    assert_eq!(part1(&mut v, 30000000), 201);
}
