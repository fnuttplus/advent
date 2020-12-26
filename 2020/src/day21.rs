use std::fs;
use std::fmt;
use std::collections::HashSet;
use std::collections::HashMap;

type Data = (HashSet<String>, Vec<Food>);
struct Food {
    ingredients: HashSet<String>,
    allergens: HashSet<String>
}
impl fmt::Debug for Food {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "[ingredients: {:?}\nallergens: {:?}]", self.ingredients, self.allergens)
    }
}

fn part2 (c: &mut HashMap<String, HashSet<String>>) -> String {
    let mut a: String = "".to_string();
    let mut b: HashSet<String> = HashSet::new();

    loop {
        let mut found = false;
        for v in c.values() {
            if v.len() == 1 {
                let aa = v.iter().next().unwrap().to_string();
                if !b.contains(&aa) {
                    found = true;
                    a = aa
                }
            }
        }
        if !found {
            let mut keys = c.keys().map(|x| x.to_string()).collect::<Vec<String>>();
            keys.sort();
            let mut v: Vec<String> = vec![];
            for k in keys {
                v.push(c[&k].iter().next().unwrap().to_string());
            }
            return v.join(",");
        }
        b.insert(a.to_string());
        
        for v in c.values_mut() {
            if v.len() > 1 {
                v.remove(&a);
            }
        }
    }
}

fn part(v: &Data) -> (usize, String) {
    let mut a:HashSet<String> = HashSet::new();
    let mut b:HashSet<String> = HashSet::new();
    let mut c:HashMap<String, HashSet<String>> = HashMap::new();
    for ee in v.0.iter() {
        a.drain();
        for ll in v.1.iter() {
            if ll.allergens.contains(ee) {
                if a.is_empty() {
                    a = ll.ingredients.clone();
                } else {
                    a = a.intersection(&ll.ingredients).cloned().collect();
                }
            }
        }
        c.insert(ee.to_string(), a.clone());
        for aa in a.iter() {
            b.insert(aa.clone());
        }
    }
    
    let mut n = 0;
    for ll in v.1.iter() {
        n += ll.ingredients.difference(&b).collect::<HashSet<_>>().len();
    }

    (n, part2(&mut c))
}

fn parse(v: &mut Data) {
    let s = fs::read_to_string("21.in").expect("file not found");
    for ss in s.split("\n") {
        let sss: Vec<String> = ss.split(" (contains ").map(|x| x.to_string()).collect();
        let food = Food {
            ingredients: sss[0].split(" ").map(|x| x.to_string()).collect(),
            allergens: sss[1][..sss[1].len()-1].split(", ").map(|x| x.to_string()).collect()
        };
        for a in food.allergens.iter() {
            v.0.insert(a.clone());
        }
        v.1.push(food);
    }
    //println!("{:?}", v);
}

pub fn run() {
    let mut v:Data = (HashSet::new(), vec![]);
    parse(&mut v);

    let p = part(&v);
    println!("PART 1: {}", p.0);
    println!("PART 2: {}", p.1);
}

#[test]
fn test21() {
    let mut v:Data = (HashSet::new(), vec![]);
    parse(&mut v);

    let p = part(&v);
    assert_eq!(p.0, 2282);
    assert_eq!(p.1, "vrzkz,zjsh,hphcb,mbdksj,vzzxl,ctmzsr,rkzqs,zmhnj");
}
