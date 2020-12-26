use std::collections::HashMap;
use std::fs::File;
use std::io::{BufRead, BufReader};
use regex::Regex;

fn isvalid(key: &str, value: &str) -> bool {
    match key {
        "byr" => {
            let y: i32 = value.parse().unwrap();
            return y >= 1920 && y <= 2002;
        },
        "iyr" => {
            let y: i32 = value.parse().unwrap();
            return y >= 2010 && y <= 2020;
        },
        "eyr" => {
            let y: i32 = value.parse().unwrap();
            return y >= 2020 && y <= 2030;
        },
        "hgt" => {
            if value.chars().nth_back(1).unwrap() == 'c' 
            && value.chars().nth_back(0).unwrap() == 'm' {
                let y: i32 = value[..(value.len()-2)].parse().unwrap();
                return y >= 150 && y <= 193
            } else if value.chars().nth_back(1).unwrap() == 'i' 
            && value.chars().nth_back(0).unwrap() == 'n' {
                let y: i32 = value[..(value.len()-2)].parse().unwrap();
                return y >= 59 && y <= 76
            } else {
                return false
            }
        },
        "hcl" => {
            let re = Regex::new(r"\#[0-9a-f]{6}").unwrap();
            return re.is_match(&value);
        },
        "ecl" => {
            return ["amb","blu","brn","gry","grn","hzl","oth"].contains(&value)
        },
        "pid" => {
            return value.len() == 9 && value.parse::<i32>().is_ok()
        },

        _ => (),
    }
    true
}

fn part1(v: &Vec<HashMap<String, String>>) -> i32 {
    let mut i = 0;
    for vv in v {
        i += 1;
        for &key in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"].iter() {
            if !vv.contains_key(key) {
                i -= 1;
                break;
            }
        }
    }
    i
}

fn part2(v: &Vec<HashMap<String, String>>) -> i32 {
    let mut i = 0;
    for vv in v {
        i += 1;
        for &key in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"].iter() {
            match vv.get(key) {
                Some(value) => {
                    if !isvalid(key, value) {
                        i -= 1;
                        break;
                    }
                }
                _ => {
                    i -= 1;
                    break;
                }
            }
        }
    }
    i
}

fn parse(dd: &mut Vec<HashMap<String, String>>) {
    let reader = BufReader::new(File::open("04.in").expect("Cannot open file"));
    let mut d = HashMap::new();
    for line in reader.lines() {
        let s = line.unwrap();
        if s == "" {
            dd.push(d);
            d = HashMap::new();
            continue;
        }
        let v: Vec<&str> = s.split(' ').collect();
        for vv in v {
            let a: Vec<&str> = vv.split(':').collect();
            d.insert(a[0].to_string(), a[1].to_string());
        }
    }
    dd.push(d);
    //println!("{:?}", dd);
}

pub fn run() {
    let mut v: Vec<HashMap<String, String>> = vec![];
    parse(&mut v);

    println!("PART 1: {}", part1(&v));
    println!("PART 2: {}", part2(&v));
}

#[test]
fn test04() {
    let mut v: Vec<HashMap<String, String>> = vec![];
    parse(&mut v);

    assert_eq!(part1(&v), 254);
    assert_eq!(part2(&v), 184);
}
