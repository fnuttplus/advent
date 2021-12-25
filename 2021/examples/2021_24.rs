
fn step(z:i64, w:i64, a:i64, b:i64, c:i64) -> i64{
    let x = if z%26+a == w {0} else {1};
    (25*x+1)*(z/b) + (w+c)*x
}

fn main() {
    let mut x = 999999999;
    let (mut za, mut zb, mut zc, mut zd, mut ze, mut zf, mut zg, mut zh, mut zi, mut zj, mut zk, mut zl, mut zm, mut zn);
    for a in (1..10).rev() {
        za = step(0, a, 11, 1, 8);
        for b in (1..10).rev() {
            zb = step(za, b, 12, 1, 8);
            for c in (1..10).rev() {
                zc = step(zb, c, 10, 1, 12);
                for d in (1..10).rev() {
                    zd = step(zc, d, -8, 26, 10);
                    for e in (1..10).rev() {
                        ze = step(zd, e, 15, 1, 2);
                        for f in (1..10).rev() {
                            zf = step(ze, f, 15, 1, 8);
                            for g in (1..10).rev() {
                                zg = step(zf, g, -11, 26, 4);
                                for h in (1..10).rev() {
                                    zh = step(zg, h, 10, 1, 9);
                                    for i in (1..10).rev() {
                                        zi = step(zh, i, -3, 26, 10);
                                        for j in (1..10).rev() {
                                            zj = step(zi, j, 15, 1, 3);
                                            for k in (1..10).rev() {
                                                zk = step(zj, k, -3, 26, 7);
                                                for l in (1..10).rev() {
                                                    zl = step(zk, l, -1, 26, 7);
                                                    for m in (1..10).rev() {
                                                        zm = step(zl, m, -10, 26, 2);
                                                        for n in (1..10).rev() {
                                                            zn = step(zm, n, -16, 26, 2);
                                                            if zn < x || zn == 0 {
                                                                x = zn;
                                                                println!("{}{}{}{}{}{}{}{}{}{}{}{}{}{} {}",a,b,c,d,e,f,g,h,i,j,k,l,m,n, x);
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
