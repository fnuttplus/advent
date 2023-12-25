from sys import stdin
from re import findall
from aoc import Grid

g = Grid([list(x) for x in stdin.read().splitlines()])

dy = [i for i, col in g.rows() if col.count('.') == len(col)]
dx = [i for i, col in g.cols() if col.count('.') == len(col)]
#print(dy, dx)

m = 1000000
galaxies = []
for x, y in g.xy():
    if g[x, y] == '#':
        x = x + (m-1)*len([xx for xx in dx if xx < x])
        y = y + (m-1)*len([yy for yy in dy if yy < y])
        galaxies.append((x, y))
#print(galaxies)

s = 0
for a in galaxies:
    for b in galaxies:
        if a == b: continue
        s += abs(a[0] - b[0]) + abs(a[1] - b[1])
print(s // 2)
