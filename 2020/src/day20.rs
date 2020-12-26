use std::fs;
use std::collections::HashMap;
use std::collections::HashSet;

type Tile = Vec<String>;
type Data = HashMap<usize, Vec<Tile>>;

fn perm(tile: &Tile) -> Vec<Tile>{
    let mut p: Vec<Tile> = vec![];
    let mut t = tile.clone();
    for _ in 0..4 {
        let mut ntile: Tile = vec![];
        for i in (0..tile.len()).rev() {
            ntile.push(t.iter().map(|x| x.chars().nth(i).unwrap()).collect::<String>());
        }
        t = ntile.clone();
        p.push(ntile.clone());
        ntile.reverse();
        p.push(ntile);
    }

    p
}

fn draw(tile: Tile, ids: &mut HashSet<usize>, image: &mut Vec<String>, tiles: &Data) {
    let mut h: String;
    let mut r: String = "".to_string();
    let mut i = 0;

    for j in 1..tile.len()-1 {
        image[i] += &tile[j][1..tile[j].len()-1];
        i += 1;
    }
    h = tile[tile.len()-1].clone();

    for j in 0..tile.len() {
        r += &tile[j].chars().last().unwrap().to_string();
    }

    for _ in 0..12 {
        'a: for (id, tile) in tiles {
            if ids.contains(id) { continue }
            for p in tile.iter() {
                if p[0] == h {
                    for j in 1..p.len()-1 {
                        image[i] += &p[j][1..p[j].len()-1];
                        i += 1;
                    }
                    h = p[p.len()-1].clone();
                    ids.insert(*id);
                    break 'a;
                }
            }
        }
    }

    for (id, tile) in tiles {
        if ids.contains(id) { continue }
        for p in tile.iter() {
            if r == p.iter().map(|x| x.chars().nth(0).unwrap()).collect::<String>() {
                ids.insert(*id);
                return draw(p.clone(), ids, image, tiles);
            }
        }
    }
}

fn paint(x: usize, y: usize, image: &mut Vec<String>, monster: [&str;3]) {
    let mut found = true;
    for z in 0..monster.len() {
        for w in 0..monster[z].len() {
            if monster[z].chars().nth(w) == Some('#')
            && image[y+z].chars().nth(x+w) != Some('#') {
                found = false
            }
        }
    }
    if found {
        for z in 0..monster.len() {
            let mut s:Vec<char> = image[y+z].chars().collect();
            for w in 0..monster[z].len() {
                if monster[z].chars().nth(w).unwrap() == '#' {
                    s[x+w] = 'O';
                }
            }
            image[y+z] = s.iter().collect::<String>();
        }
    }
}

fn part(v: &Data) -> (usize, usize) {
    let mut e: HashMap<usize, HashSet<usize>> = HashMap::new();
    for (k0, v0) in v {
        for (k1, v1) in v {
            if k0 == k1 { continue }
            for p0 in v0 {
                if v1.iter().map(|x| x.iter().nth(0).unwrap().to_string()).collect::<Vec<String>>().contains(&p0[0]) {
                    e.entry(*k0).or_insert(vec![*k1].into_iter().collect()).insert(k1.clone());
                }
            }
        }
    }

    let mut p = 1;
    for (ee, vv) in e {
        if vv.len() == 2 {
            p *= ee;
        }
    }

    let mut image: Vec<String> = vec![];
    for _ in 0..96 {
        image.push("".to_string());
    }
    draw(v[&2137][1].clone(), &mut [2137].iter().cloned().collect(), &mut image, &v);
    let monster = ["                  # ","#    ##    ##    ###"," #  #  #  #  #  #   "];
    for y in 0..image.len()-monster.len() {
        for x in 0..image[y].len()-monster[0].len() {
            paint(x, y, &mut image, monster);
        }
    }
    //image.iter().for_each(|x| println!("{:?}", x));
    let s = image.iter().map(|x| x.chars().filter(|&x| x == '#').count()).sum::<usize>();

    (p, s)
}

fn parse(v: &mut Data) {
    let s = fs::read_to_string("20.in").expect("file not found");
    for ss in s.split("\n\n") {
        let tile: Vec<&str> = ss.split("\n").collect();
        let id = tile[0].split(" ").collect::<Vec<&str>>()[1];
        let id:usize = id[..id.len()-1].parse().unwrap();
        v.insert(id, perm(&tile.iter().skip(1).map(|x| x.to_string()).collect()));
    }
    //println!("{:?}", v);
}

pub fn run() {
    let mut v: Data = HashMap::new();
    parse(&mut v);

    let p = part(&v);
    println!("PART 1: {}", p.0);
    println!("PART 2: {}", p.1);
}

#[test]
fn test20() {
    let mut v: Data = HashMap::new();
    parse(&mut v);

    let p = part(&v);
    assert_eq!(p.0, 23497974998093);
    assert_eq!(p.1, 2256);
}
