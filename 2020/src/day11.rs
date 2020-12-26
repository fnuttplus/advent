use std::collections::HashSet;
use std::fs;

type Data = Vec<Vec<char>>;

fn adj(g: &Data, x: isize, y: isize, m: isize) -> isize {
    let mut n = 0;
    for (dx, dy) in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)].iter() {
        for i in 1..m {
            if 0 <= y + i * dy
                && y + i * dy < g.len() as isize
                && 0 <= x + i * dx
                && x + i * dx < g[0].len() as isize
            {
                if g[(y + i * dy) as usize][(x + i * dx) as usize] == '#' {
                    n += 1;
                    break
                }
                if g[(y + i * dy) as usize][(x + i * dx) as usize] == 'L' {
                    break
                }
            } else {
                break
            }
        }
    }
    n
}

fn part1(g: &mut Data) -> usize {
    let mut acc: HashSet<(usize, usize)> = HashSet::new();
    let mut emp: HashSet<(usize, usize)> = HashSet::new();
    loop {
        acc.clear();
        emp.clear();

        for y in 0..g.len() {
            for x in 0..g[y].len() {
                if g[y][x] == 'L' && adj(&g, x as isize, y as isize, 2) == 0 {
                    acc.insert((x, y));
                } else if g[y][x] == '#' && adj(&g, x as isize, y as isize, 2) >= 4 {
                    emp.insert((x, y));
                }
            }
        }

        if acc.is_empty() && emp.is_empty() {
            break;
        }

        for (x, y) in acc.iter() {
            g[*y][*x] = '#';
        }
        for (x, y) in emp.iter() {
            g[*y][*x] = 'L';
        }
    }

    g.iter()
        .map(|x| x.iter().filter(|x| *x == &'#').count())
        .sum::<usize>()
}

fn part2(g: &mut Data) -> usize {
    let mut acc: HashSet<(usize, usize)> = HashSet::new();
    let mut emp: HashSet<(usize, usize)> = HashSet::new();
    loop {
        acc.clear();
        emp.clear();

        for y in 0..g.len() {
            for x in 0..g[y].len() {
                if g[y][x] == 'L' && adj(g, x as isize, y as isize, 100) == 0 {
                    acc.insert((x, y));
                } else if g[y][x] == '#' && adj(g, x as isize, y as isize, 100) >= 5 {
                    emp.insert((x, y));
                }
            }
        }

        if acc.is_empty() && emp.is_empty() {
            break;
        }

        for (x, y) in acc.iter() {
            g[*y][*x] = '#';
        }
        for (x, y) in emp.iter() {
            g[*y][*x] = 'L';
        }
    }

    g.iter()
        .map(|x| x.iter().filter(|x| *x == &'#').count())
        .sum::<usize>()
}

fn parse(dd: &mut Data) {
    let s = fs::read_to_string("11.in").expect("file not found");
    for ss in s.split("\n") {
        dd.push(ss.chars().collect());
    }
    //println!("{:?}", dd);
}

pub fn run() {
    let mut v: Data = vec![];
    parse(&mut v);

    println!("PART 1: {}", part1(&mut v.clone()));
    println!("PART 2: {}", part2(&mut v));
}

#[test]
fn test11() {
    let mut v: Data = vec![];
    parse(&mut v);

    assert_eq!(part1(&mut v.clone()), 2243);
    assert_eq!(part2(&mut v), 2027);
}
