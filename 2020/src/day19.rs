use std::fs;
use std::collections::HashMap;

struct Data {
    rules: HashMap<usize, Vec<Vec<usize>>>,
    messages: Vec<String>
}

fn gen(rules: &HashMap<usize, Vec<Vec<usize>>>, i: usize) -> Vec<String> {
    let mut matches: Vec<String> = vec![];
    let r = &rules[&i];
    if r[0][0] == 1 << 10 {
        return vec!["a".to_string()]
    }
    if r[0][0] == 1 << 11 {
        return vec!["b".to_string()]
    }
    for g0 in gen(rules, r[0][0]) {
        if r[0].len() > 1 {
            for g1 in gen(rules, r[0][1]) {
                matches.push([g0.clone(),g1].join(""));
            }
        }
        else {
            matches.push(g0)
        }
    }
    if r.len() > 1 {
        for g0 in gen(rules, r[1][0]) {
            if r[0].len() > 1 {
                for g1 in gen(rules, r[1][1]) {
                    matches.push([g0.clone(),g1].join(""));
                }
            }
            else {
                matches.push(g0)
            }
        }
    }
    matches
}

fn part(v: &Data) -> (usize, usize) {
    let mut n1 = 0;
    let mut n2 = 0;
    let l42 = gen(&v.rules, 42);
    let l31 = gen(&v.rules, 31);
    for i in 0..v.messages.len() {
        let mut starts = 0;
        let mut ends = 0;
        let mut message = v.messages[i].clone();
        loop {
            let mut found = false;
            for a in l42.iter() {
                if message.starts_with(a) {
                    starts += 1;
                    message = message[a.len()..].to_string();
                    found = true;
                    break
                }
            }
            if !found {
                break
            }
        }
        loop {
            let mut found = false;
            for a in l31.iter() {
                if message.ends_with(a) {
                    ends += 1;
                    message = message[..message.len() - a.len()].to_string();
                    found = true;
                    break
                }
            }
            if !found {
                break
            }
        }
        if message == "" && starts == 2 && ends == 1 {
            n1 += 1
        }
        if message == "" && starts > ends && ends >= 1 {
            n2 += 1
        }
    }
    (n1, n2)
}

fn parse(v: &mut Data) {
    let s = fs::read_to_string("19.in").expect("file not found");
    let ss:Vec<&str> = s.split("\n\n").collect();
    for rule in ss[0].split("\n") {
        let rule: Vec<&str> = rule.split(": ").collect();
        let b: Vec<Vec<usize>> = match rule[1] {
            "\"a\"" => vec![vec![1 << 10]],
            "\"b\"" => vec![vec![1 << 11]],
            _ => rule[1].split(" | ").map(|x| x.split(" ").map(|y| y.parse().unwrap()).collect()).collect()
        };
        v.rules.insert(rule[0].parse().unwrap(), b);
    }
    //println!("{:?}", v.rules);
    for sss in ss[1].split("\n") {
        v.messages.push(sss.to_string());
    }
    //println!("{:?}", v.messages);
}

pub fn run() {
    let mut v = Data {
        rules: HashMap::new(),
        messages: vec![]
    };
    parse(&mut v);

    let p = part(&v);
    println!("PART 1: {}", p.0);
    println!("PART 2: {}", p.1);
}

#[test]
fn test19() {
    let mut v = Data {
        rules: HashMap::new(),
        messages: vec![]
    };
    parse(&mut v);

    let p = part(&v);
    assert_eq!(p.0, 235);
    assert_eq!(p.1, 379);
}
