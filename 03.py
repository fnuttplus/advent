from sys import stdin

i = 0
for line in stdin:
    a0, b0, c0 = map(int, line.split())
    a1, b1, c1 = map(int, stdin.readline().split())
    a2, b2, c2 = map(int, stdin.readline().split())

    a = sorted([a0, a1, a2])
    if a[0] + a[1] > a[2]: i += 1

    b = sorted([b0, b1, b2])
    if b[0] + b[1] > b[2]: i += 1

    c = sorted([c0, c1, c2])
    if c[0] + c[1] > c[2]: i += 1

print(i)
