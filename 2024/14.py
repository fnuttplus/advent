from sys import stdin
from aocd import get_data, submit
from re import findall
from itertools import product, combinations
from aoc import Grid, adj
from sympy.solvers import solve
from sympy import *
from oklab import viridis

s = 0

r = []

t = True
t = False

ls = stdin.read() if t else get_data(day=14)
w,h = (11,7) if t else (101,103)
g = Grid([[0 for _ in range(w)] for _ in range(h)])
print(g)

v = viridis(6)
d = {x: v[x] for x in range(6)}

for l in ls.split('\n'):
    print(l)
    p,v = l.split(' ')
    p = list(map(int, p[2:].split(',')))
    v = list(map(int, v[2:].split(',')))
    print(p,v)
    r.append([p,v])

for i in range(10000):
    g = Grid([[0 for _ in range(w)] for _ in range(h)])
    for ri in range(len(r)):
        rr = r[ri]
        x,y = rr[0]
        vx,vy = rr[1]
        g[x,y] += 1

        x = (x+vx)%w
        y = (y+vy)%h
        r[ri][0] = (x,y)
    if t: print(g)
    g.save_image_file(d, f"frames/advent{i}.png")

s = 1
c = sum(g[x, y] for x in range(w // 2) for y in range(h // 2))
print(c)
s *= c
c = sum(g[x, y] for x in range(w//2+1, w) for y in range(h // 2))
print(c)
s *= c
c = sum(g[x, y] for x in range(w//2+1, w) for y in range(h//2+1, h))
print(c)
s *= c
c = sum(g[x, y] for x in range(w//2) for y in range(h//2+1, h))
print(c)
s *= c

if t:
    print(s)
else:
    submit(s)
