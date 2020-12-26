use std::fs;

type Data = Vec<(char, i32)>;

fn rotate_right(dx: &mut i32, dy: &mut i32, s: i32) {
    for _ in 0..s {
        let t = *dx;
        *dx = -*dy;
        *dy = t;
    }
}

fn part1(v: &Data) -> i32 {
    let mut x = 0;
    let mut y = 0;
    let mut dx = 1;
    let mut dy = 0;
    for vv in v {
        match vv.0 {
            'N' => y -= vv.1,
            'S' => y += vv.1,
            'E' => x += vv.1,
            'W' => x -= vv.1,
            'L' => rotate_right(&mut dx, &mut dy, 4-vv.1/90),
            'R' => rotate_right(&mut dx, &mut dy, vv.1/90),
            'F' => {
                x += vv.1 * dx;
                y += vv.1 * dy;
            },
            _ => ()
        }
    }
    x + y
}

fn part2(v: &Data) -> i32 {
    let mut x = 0;
    let mut y = 0;
    let mut dx = 10;
    let mut dy = -1;
    for vv in v {
        match vv.0 {
            'N' => dy -= vv.1,
            'S' => dy += vv.1,
            'E' => dx += vv.1,
            'W' => dx -= vv.1,
            'L' => rotate_right(&mut dx, &mut dy, 4-vv.1/90),
            'R' => rotate_right(&mut dx, &mut dy, vv.1/90),
            'F' => {
                x += vv.1 * dx;
                y += vv.1 * dy;
            },
            _ => ()
        }
    }
    x + y
}

fn parse(v: &mut Data) {
    let s = fs::read_to_string("12.in").expect("file not found");
    for ss in s.split("\n") {
        let mut c = ss.chars();
        v.push((c.next().unwrap(), c.as_str().parse().unwrap()));
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
fn test12() {
    let mut v: Data = vec![];
    parse(&mut v);

    assert_eq!(part1(&v), 2458);
    assert_eq!(part2(&v), 145117);
}
