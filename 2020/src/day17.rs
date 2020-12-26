use std::fs;
use std::collections::HashSet;

type Data = HashSet<(i8, i8, i8, i8)>;

fn adj_active3d(v: &Data, c: (i8, i8, i8, i8)) -> i32 {
    let (x, y, z, _) = c;
    let mut n = 0;
    for dx in [-1, 0, 1].iter() {
        for dy in [-1, 0, 1].iter() {
            for dz in [-1, 0, 1].iter() {
                if *dx == 0 && *dy == 0 && *dz == 0 { continue }
                if v.contains(&(x+*dx, y+*dy, z+*dz, 0)) {
                    n += 1;
                }
            }
        }
    }
    n
}

fn adj_inactive3d(v: &Data, c: (i8, i8, i8, i8)) -> HashSet<(i8, i8, i8, i8)> {
    let (x, y, z, _) = c;
    let mut s: HashSet<(i8, i8, i8, i8)> = HashSet::new();
    for dx in [-1, 0, 1].iter() {
        for dy in [-1, 0, 1].iter() {
            for dz in [-1, 0, 1].iter() {
                if *dx == 0 && *dy == 0 && *dz == 0 { continue }
                if !v.contains(&(x+*dx, y+*dy, z+*dz, 0)) {
                    s.insert((x+*dx, y+*dy, z+*dz, 0));
                }
            }
        }
    }
    s
}

fn adj_active(v: &Data, c: (i8, i8, i8, i8)) -> i32 {
    let (x, y, z, w) = c;
    let mut n = 0;
    for dx in [-1, 0, 1].iter() {
        for dy in [-1, 0, 1].iter() {
            for dz in [-1, 0, 1].iter() {
                for dw in [-1, 0, 1].iter() {
                    if *dx == 0 && *dy == 0 && *dz == 0 && *dw == 0 { continue }
                    if v.contains(&(x+*dx, y+*dy, z+*dz, w+*dw)) {
                        n += 1;
                    }
                }
            }
        }
    }
    n
}

fn adj_inactive(v: &Data, c: (i8, i8, i8, i8)) -> HashSet<(i8, i8, i8, i8)> {
    let (x, y, z, w) = c;
    let mut s: HashSet<(i8, i8, i8, i8)> = HashSet::new();
    for dx in [-1, 0, 1].iter() {
        for dy in [-1, 0, 1].iter() {
            for dz in [-1, 0, 1].iter() {
                for dw in [-1, 0, 1].iter() {
                    if *dx == 0 && *dy == 0 && *dz == 0 && *dw == 0 { continue }
                    if !v.contains(&(x+*dx, y+*dy, z+*dz, w+*dw)) {
                        s.insert((x+*dx, y+*dy, z+*dz, w+*dw));
                    }
                }
            }
        }
    }
    s
}

fn part1(v: &mut Data) -> usize {
    for _ in 1..7 {
        let mut a: Vec<(i8, i8, i8, i8)> = vec![];
        let mut b: Vec<(i8, i8, i8, i8)> = vec![];

        for &c in v.iter() {
            let n = adj_active3d(v, c);
            if !( n == 2 || n == 3) {
                a.push(c);
            }
            for adj in adj_inactive3d(v, c) {
                if adj_active3d(v, adj) == 3 {
                    b.push(adj);
                }
            }
        }
        for aa in a {
            v.remove(&aa);
        }
        for bb in b {
            v.insert(bb);
        }
    }
    v.len()
}

fn part2(v: &mut Data) -> usize {
    for _ in 1..7 {
        let mut a: Vec<(i8, i8, i8, i8)> = vec![];
        let mut b: Vec<(i8, i8, i8, i8)> = vec![];

        for &c in v.iter() {
            let n = adj_active(v, c);
            if !( n == 2 || n == 3) {
                a.push(c);
            }
            for adj in adj_inactive(v, c) {
                if adj_active(v, adj) == 3 {
                    b.push(adj);
                }
            }
        }
        for aa in a {
            v.remove(&aa);
        }
        for bb in b {
            v.insert(bb);
        }
    }
    v.len()
} 

fn parse(v: &mut Data) {
    let s = fs::read_to_string("17.in").expect("file not found");
    let mut y = 0;
    for ss in s.split("\n") {
        let mut x = 0;
        for sss in ss.chars() {
            if sss == '#' {
                v.insert((x, y, 0, 0));
            }
            x += 1;
        }
        y += 1;
    }
    //println!("{:?}", v);
}

pub fn run() {
    let mut v: Data = HashSet::new();
    // performance improvement?
    //let mut test = [[[0u32;32];32];32]; 131072 bytes
    //4th dimension uses bit values
    //keep track of bounderies to not iterate over empty space
    parse(&mut v);

    println!("PART 1: {}", part1(&mut v.clone()));
    println!("PART 2: {}", part2(&mut v));
}

#[test]
fn test17() {
    let mut v: Data = HashSet::new();
    parse(&mut v);

    assert_eq!(part1(&mut v.clone()), 298);
    assert_eq!(part2(&mut v), 1792);
}
