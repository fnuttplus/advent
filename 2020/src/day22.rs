use std::fs;
use std::collections::HashSet;

type Data = (Vec<usize>, Vec<usize>);

fn rec(v: &mut (Vec<usize>, Vec<usize>), it: bool) -> (bool, Vec<usize>) {
    let mut s: HashSet<String> = HashSet::new();

    loop {
        let k:String = format!("{:?}", v);
        if s.contains(&k) {
            return (true, (vec![]))
        }
        s.insert(k);
        let a = v.0.remove(0);
        let b = v.1.remove(0);

        let p1w;
        if it && a <= v.0.len() && b <= v.1.len() {
            p1w = rec(&mut (v.0.iter().take(a).cloned().collect(), v.1.iter().take(b).cloned().collect()), true).0
        } else {
            p1w = a > b;
        }
        if p1w {
            v.0.push(a);
            v.0.push(b);
        } else {
            v.1.push(b);
            v.1.push(a);
        }

        if v.0.len() == 0 {
            return (false, v.1.clone())
        }
        if v.1.len() == 0 {
            return (true, v.0.clone())
        }
    }
}

fn part(v: &mut Data) -> (usize, usize) {
    let mut n1 = 0;
    let mut n2 = 0;
    let (_, p) = rec(&mut v.clone(), false);

    for (i,v) in p.iter().enumerate() {
        n1 += (p.len() - i) * v;
    }

    let (_, p) = rec(v, true);
    for (i,v) in p.iter().enumerate() {
        n2 += (p.len() - i) * v;
    }
    (n1, n2)
}

fn parse(v: &mut Data) {
    let s = fs::read_to_string("22.in").expect("file not found");
    let ss: Vec<&str> = s.split("\n\n").collect();
    v.0 = ss[0].split("\n").skip(1).map(|x| x.parse().unwrap()).collect();
    v.1 = ss[1].split("\n").skip(1).map(|x| x.parse().unwrap()).collect();
    //println!("{:?}", v);
}

pub fn run() {
    let mut v: Data = (vec![], vec![]);
    parse(&mut v);

    let p = part(&mut v);
    println!("PART 1: {}", p.0);
    println!("PART 2: {}", p.1);
}

#[test]
fn test22() {
    let mut v: Data = (vec![], vec![]);
    parse(&mut v);

    let p = part(&mut v);
    assert_eq!(p.0, 32856);
    assert_eq!(p.1, 33805);
}
