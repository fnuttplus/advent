use std::collections::HashSet;
use std::fs;

type Data = Vec<Vec<u8>>;
type Tile = (isize, isize, isize);

fn co(d: u8, t: Tile) -> Tile {
    let (mut x, mut y, mut z) = t;
    match d {
        0 => {
            x += 1;
            y -= 1;
        }
        1 => {
            x -= 1;
            y += 1;
        }
        2 => {
            y -= 1;
            z += 1;
        }
        3 => {
            x -= 1;
            z += 1;
        }
        4 => {
            x += 1;
            z -= 1;
        }
        5 => {
            y += 1;
            z -= 1;
        }
        _ => (),
    }
    (x, y, z)
}

fn adji(t: Tile, s: &HashSet<Tile>) -> Vec<Tile> {
    let mut tiles: Vec<Tile> = vec![];

    for d in 0..6 {
        let dt = co(d, t);
        if !s.contains(&dt) {
            tiles.push(dt)
        }
    }

    tiles
}

fn adj(t: Tile, s: &HashSet<Tile>) -> usize {
    let mut n = 0;

    for d in 0..6 {
        let dt = co(d, t);
        if s.contains(&dt) {
            n += 1
        }
    }
    n
}

fn part(v: &Data) -> (usize, usize) {
    let mut tiles: HashSet<Tile> = HashSet::new();
    for vv in v {
        let mut t = (0, 0, 0);
        for &c in vv {
            t = co(c, t);
        }
        if tiles.contains(&t) {
            tiles.remove(&t);
        } else {
            tiles.insert(t);
        }
    }
    let n1 = tiles.len();

    for _ in 0..100 {
        let mut w:HashSet<Tile> = HashSet::new();
        let mut b:HashSet<Tile> = HashSet::new();

        for &t in tiles.iter() {
            let n = adj(t, &tiles);
            if n == 0 || n > 2 {
                w.insert(t);
            }
            for a in adji(t, &tiles) {
                let n = adj(a, &tiles);
                if n == 2 {
                    b.insert(a);
                }
            }
        }

        for ww in w {
            tiles.remove(&ww);
        }

        for bb in b {
            tiles.insert(bb);
        }

        //println!("{:?}", tiles.len())
    }
    
    (n1, tiles.len())
}

fn parse(v: &mut Data) {
    let s = fs::read_to_string("24.in").expect("file not found");
    for ss in s.split("\n") {
        let mut vv: Vec<u8> = vec![];
        let mut cc = ss.chars();
        while let Some(c) = cc.next() {
            match c {
                'e' => vv.push(0),
                'w' => vv.push(1),
                's' => match cc.next().unwrap() {
                    'e' => vv.push(2),
                    'w' => vv.push(3),
                    _ => (),
                },
                'n' => match cc.next().unwrap() {
                    'e' => vv.push(4),
                    'w' => vv.push(5),
                    _ => (),
                },
                _ => (),
            }
        }
        v.push(vv);
    }
    //println!("{:?}", v);
}

pub fn run() {
    let mut v: Data = vec![];
    parse(&mut v);

    let p = part(&v);
    println!("PART 1: {}", p.0);
    println!("PART 2: {}", p.1);
}

#[test]
fn test24() {
    let mut v: Data = vec![];
    parse(&mut v);

    let p = part(&v);
    assert_eq!(p.0, 394);
    assert_eq!(p.1, 4036);
}
