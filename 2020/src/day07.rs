use std::fs;
use std::fmt;
use std::collections::HashMap;
use std::collections::HashSet;

type Data = HashMap<String, Vec<Bag>>;

struct Bag {
    n: usize,
    name: String
}

impl fmt::Debug for Bag {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{} {}", self.n, self.name)
    }
}

fn find(v: &Data, name: &String, s: &mut HashSet<String>) {
    for (bagname, bags) in v {
        for bag in bags {
            if bag.name == name.to_string() {
                if s.contains(bagname) { continue }
                s.insert(bagname.to_string());
                find(v, bagname, s);
            }
        }
    }
}

fn part1(v: &Data) -> usize {
    let mut s = HashSet::new();
    find(v, &"shiny gold".to_string(), &mut s);
    s.len()
}

fn count(v: &Data, name: &String) -> usize {
    let mut i = 1;
    for (bagname, bags) in v {
        if bagname == name {
            for bag in bags {
                i += bag.n * count(v, &bag.name);
            }
        }
    }
    i
}

fn part2(v: &Data) -> usize {
    count(v, &"shiny gold".to_string()) - 1
}

fn parse(dd: &mut Data) {
    let s = fs::read_to_string("07.in").expect("");
    for ss in s.split("\n") {
        let a: Vec<&str> = ss.split(' ').collect();
        if a.len() == 7 { continue }
        let mut b: Vec<Bag> = vec![];
        for x in (4..a.len()).step_by(4) {
            let bag = Bag {
                n: a[x].parse().unwrap(),
                name: format!("{} {}", a[x + 1], a[x + 2])
            };
            b.push(bag);
        }
        dd.insert(format!("{} {}", a[0], a[1]), b);
    }
    //println!("{:?}", dd);
}

pub fn run() {
    let mut v: Data = HashMap::new();
    parse(&mut v);

    println!("PART 1: {}", part1(&v));
    println!("PART 2: {}", part2(&v));
}

#[test]
fn test07() {
    let mut v: Data = HashMap::new();
    parse(&mut v);

    assert_eq!(part1(&v), 372);
    assert_eq!(part2(&v), 8015);
}
