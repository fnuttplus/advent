use std::fs;
use std::collections::HashMap;

type Data = Vec<(i64, Vec<char>)>;

fn xor(mask: &Vec<char>, b: i64) -> i64 {
    let mut x = 0i64;
    for i in 0..mask.len() {
        x <<= 1;
        x += match mask[i] {
            'X' => (b >> mask.len() - i - 1) & 1,
            '1' => 1,
            _ => 0
        }
    }
    x
}

fn part1(v: &Data) -> i64 {
    let mut mask: &Vec<char> = &vec![];
    let mut mem: HashMap<i64, i64> = HashMap::new();
    for i in 0..v.len() {
        if v[i].0 == -1 {
            mask = &v[i].1
        } else {
            mem.insert(v[i].0, xor(&mask, v[i].1.iter().collect::<String>().parse().unwrap()));
        }
    }
    mem.values().sum()
}

fn ab (m: &Vec<char>, b: i64, c: usize) -> i64 {
    let mut x = 0i64;
    let mut i = c;
    for j in 0..m.len() {
        x <<= 1;
        if m[j] == 'X' {
            i -= 1;
            x += b >> i & 1;
        } else if m[j] == '1' {
            x += 1
        }
    }
    x
}

fn addr (mask: &Vec<char>, b: i64) -> Vec<i64>{
    let mut v: Vec<i64> = vec![];
    let mut x: Vec<char> = vec![];
    for i in 0..mask.len() {
        x.push(match mask[i] {
            '0' => match (b >> mask.len() - i - 1) & 1 {
                1 => '1',
                _ => '0'
            },
            _ => mask[i]
        })
    }
    let c = x.iter().filter(|x| *x == &'X').count();
    for i in 0..1<<c {
        v.push(ab(&mut x, i, c))
    }
    v
}

fn part2(v: &Data) -> i64 {
    let mut mask: &Vec<char> = &vec![];
    let mut mem: HashMap<i64, i64> = HashMap::new();
    for i in 0..v.len() {
        if v[i].0 == -1 {
            mask = &v[i].1
        } else {
            for j in addr(mask, v[i].0) {
                mem.insert(j, v[i].1.iter().collect::<String>().parse().unwrap());
            }
        }
    }
    mem.values().sum()
}

fn parse(v: &mut Data) {
    let s = fs::read_to_string("14.in").expect("file not found");
    for ss in s.split("\n") {
        let ss:Vec<&str> = ss.split(" = ").collect();
        let i;
        if ss[0] == "mask" {
            i = -1
        } else {
            let sss:Vec<&str> = ss[0].split("[").collect();
            i = sss[1][..sss[1].len()-1].parse().unwrap();
        }
        v.push((i, ss[1].chars().collect()));
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
fn test14() {
    let mut v: Data = vec![];
    parse(&mut v);

    assert_eq!(part1(&v), 7997531787333);
    assert_eq!(part2(&v), 3564822193820);
}
