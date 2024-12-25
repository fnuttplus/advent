from sys import stdin
from aocd import get_data, submit
from re import findall
from itertools import product, combinations
from aoc import Grid, adj

s = 0

r = {}

t = True
t = False

ls = stdin.read() if t else get_data()
ls = [list(x) for x in ls.split('\n')]
g = Grid(ls)

for x0,y0 in g.xy():
    c = g[x0,y0]
    if c == 0: continue
    q = [(x0, y0)]
    n = set()
    p = 0
    while q:
        (x,y) = q.pop()
        if (x,y) in n: continue
        n.add((x,y))
        for x1,y1 in adj(x,y):
            if g.fit(x1, y1) and g.data[y1][x1] == c:
                q.append((x1,y1))

    if t: print(c, n)

    cn = {}
    for x,y in sorted(n):
        #north
        nx,ny = x,y-1
        if not g.fit(nx,ny) or g[nx,ny] != c:
            if not (((x-1, y) in cn and 'N' in cn[(x-1, y)]) or ((x+1, y) in cn and 'N' in cn[(x+1, y)])):
                p += 1
            if (x,y) in cn:
                cn[(x,y)].add('N')
            else:
                cn[(x,y)] = set(['N'])
        #south
        nx,ny = x,y+1
        if not g.fit(nx,ny) or g[nx,ny] != c:
            if not (((x-1, y) in cn and 'S' in cn[(x-1, y)]) or ((x+1, y) in cn and 'S' in cn[(x+1, y)])):
                p += 1
            if (x,y) in cn:
                cn[(x,y)].add('S')
            else:
                cn[(x,y)] = set(['S'])
        #east
        nx,ny = x+1,y
        if not g.fit(nx,ny) or g[nx,ny] != c:
            if not (((x, y-1) in cn and 'E' in cn[(x, y-1)]) or ((x, y+1) in cn and 'E' in cn[(x, y+1)])):
                p += 1
            if (x,y) in cn:
                cn[(x,y)].add('E')
            else:
                cn[(x,y)] = set(['E'])
        #west
        nx,ny = x-1,y
        if not g.fit(nx,ny) or g[nx,ny] != c:
            if not (((x, y-1) in cn and 'W' in cn[(x, y-1)]) or ((x, y+1) in cn and 'W' in cn[(x, y+1)])):
                p += 1
            if (x,y) in cn:
                cn[(x,y)].add('W')
            else:
                cn[(x,y)] = set(['W'])

    print(cn)

    for x,y in n:
        g[x,y] = 0

    s += len(n) * p
    if t: print(c, len(n), p)

if t:
    print(s)
else:
    submit(s)
