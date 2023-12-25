from sys import stdin
from aocd import get_data, submit
from re import findall

s1, s2 = 0, 0
d = {
    "red": 12,
    "green": 13,
    "blue": 14,
}
for line in stdin.read().splitlines():
    n = int(line.split(': ')[0][5:])
    games = line.split(': ')[1].split(';')
    for g in games:
        f = g.split(',')
        for c in f:
            a, b = c.strip().split(' ')
            a = int(a)
            if a > d[b]: break
        else: continue
        break
    else:
        s1 += n

    m = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for g in games:
        f = g.split(',')
        for c in f:
            a, b = c.strip().split(' ')
            a = int(a)
            if a > m[b]: m[b] = a
    s2 += m["red"] * m["green"] * m["blue"]

print(s1, s2)