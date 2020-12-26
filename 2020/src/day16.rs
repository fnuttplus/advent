use std::fs;
use std::fmt;
use std::collections::HashMap;

struct Data {
    notes: HashMap<String, Vec<usize>>,
    ticket: Vec<usize>,
    nearby: Vec<Vec<usize>>
}

impl fmt::Debug for Data {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "NOTES: {:?}\nTICKET: {:?}\nNEARBY: {:?}", self.notes, self.ticket, self.nearby)
    }
}

fn isvalid(i: usize, v: &Data) -> bool {
    for (_,v) in &v.notes {
        if (v[0] <= i && i <= v[1]) || (v[2] <= i && i <= v[3]) {
            return true
        }
    }
    false
}

fn part1(v: &Data) -> usize {
    let mut n = 0;
    for i in 0..v.nearby.len() {
        let ticket = &v.nearby[i];
        for j in ticket {
            if !isvalid(*j, v) {
                n += *j;
                break
            }
        }
    }
    n
}

fn part2(v: &Data) -> i64 {
    let mut g: [Vec<usize>; 20] = Default::default();
    for i in 0..v.nearby.len() {
        let ticket = &v.nearby[i];
        let mut valid = true;
        for j in ticket {
            if !isvalid(*j, v) {
                valid = false;
                break;
            }
        }
        if valid {
            for x in 0..20 {
                g[x].push(ticket[x])
            }
        }
    }

    let mut f: [Vec<String>; 20] = Default::default();
    for x in 0..20 {
        for (k,v) in &v.notes {
            let mut valid = true;
            for gg in g[x].iter() {
                if !((v[0] <= *gg && *gg <= v[1]) || (v[2] <= *gg && *gg <= v[3])) {
                    valid = false;
                    break;
                }
            }
            if valid {
                f[x].push(k.clone());
            }
        }
    }

    let mut h = f.iter().enumerate()
        .map(|(i,v)| (i, v)).collect::<Vec<(usize, &Vec<String>)>>();
    h.sort_by_key(|k| k.1.len());

    let mut ff: Vec<String> = vec![];
    let mut gg: Vec<usize> = vec![];
    for hh in h {
        let name  = hh.1.iter().filter(|&x| !ff.iter().any(|i| *i == *x)).next().unwrap().to_string();
        if name.starts_with("departure") {
            gg.push(hh.0)
        }
        ff.push(name);
    }

    let mut p = 1i64;
    for i in gg {
        p *= v.ticket[i] as i64
    }
    p
}

fn parse(v: &mut Data) {
    let s = fs::read_to_string("16.in").expect("file not found");
    let ss: Vec<&str> = s.split("\n\n").collect();
    for sss in ss[0].split("\n") {
        let ssss: Vec<&str> = sss.split(": ").collect();
        let sssss: Vec<usize> = ssss[1].split(|c| c == '-' || c == ' ')
            .filter(|x| *x != "or").map(|x| x.parse().unwrap()).collect();
        v.notes.insert(ssss[0].to_string(), sssss);
    }

    v.ticket = ss[1].split("\n").collect::<Vec<&str>>()[1].split(",")
        .map(|x| x.parse::<usize>().unwrap()).collect();

    for sss in ss[2].split("\n").skip(1) {
        let ssss: Vec<usize> = sss.split(",").map(|x| x.parse().unwrap()).collect();
        v.nearby.push(ssss);
    }
    //println!("{:?}", v);
}

pub fn run() {
    let mut v = Data {
        notes: HashMap::new(),
        ticket: vec![],
        nearby: vec![]
    };
    parse(&mut v);

    println!("PART 1: {}", part1(&v));
    println!("PART 2: {}", part2(&v));
}

#[test]
fn test16() {
    let mut v = Data {
        notes: HashMap::new(),
        ticket: vec![],
        nearby: vec![]
    };
    parse(&mut v);

    assert_eq!(part1(&v), 19070);
    assert_eq!(part2(&v), 161926544831);
}
