use std::fs;

type Data = Vec<usize>;

fn part2(v: &mut Data) -> usize {
    let m = 1000000;
    let mut s = vec![0usize; m+1].into_boxed_slice();
    for i in 1..v.len() {
        s[v[i-1]] = v[i]
    }
    s[m] = v[0];
    //println!("{:?}", s[..31].to_vec());

    let mut d = v[0];
    for _ in 0..(10*m) {
        let a = s[d];
        let b = s[a];
        let c = s[b];
        s[d] = s[c];
        let mut i = d-1;
        if i == 0 { i = m }
        while [a,b,c].contains(&i) {
            i -= 1;
            if i == 0 { i = m }
        }
        s[c] = s[i];
        s[i] = a;
        d = s[d];
    }
    s[1] * s[s[1]]
}

fn part1(v: &mut Data) -> usize {
    let mut n: usize = 0;
    for _ in 0..100 {
        let f = v[0];
        let t = v[1..4].to_vec();
        let mut i = f - 1;

        while t.contains(&i) {
            i -= 1;
        }
        if i == 0 { i = 9 }
        while t.contains(&i) {
            i -= 1;
        }

        v.drain(..4);
        i = v.iter().position(|&x| x == i).unwrap();
        v.insert(i+1, t[0]);
        v.insert(i+2, t[1]);
        v.insert(i+3, t[2]);
        v.push(f);
    }

    let i = v.iter().position(|&x| x == 1).unwrap();
    

    for i in v[i+1..].to_vec() {
        n = n*10 + i;
    }
    for i in v[..i].to_vec() {
        n = n*10 + i;
    }
    n
}

fn parse(v: &mut Data) {
    let s = fs::read_to_string("23.in").expect("file not found");
    let mut ss: Vec<usize> = s.chars().map(|x| x.to_digit(10).unwrap() as usize).collect();
    v.append(&mut ss);
    //println!("{:?}", v);
}

pub fn run() {
    let mut v: Data = vec![];
    parse(&mut v);
    
    println!("PART 1: {}", part1(&mut v.clone()));

    v.append(&mut (10..1000001).collect());
    println!("PART 2: {}", part2(&mut v));
}

#[test]
fn test23() {
    let mut v: Data = vec![];
    parse(&mut v);

    assert_eq!(part1(&mut v.clone()), 65432978);

    v.append(&mut (10..1000001).collect());
    assert_eq!(part2(&mut v), 287230227046);
}
