from sys import stdin
import re
from aocd import submit, get_data, lines
from PIL import Image

#ll = stdin.read().splitlines()
ll = get_data(day=12).splitlines()
g = [list(l) for l in ll]
gg = {}
ab = {b: a for (a,b) in enumerate('abcdefghijklmnopqrstuvwxyz')}
ab['S'] = 0
ab['E'] = 25
"""
print(ab)
for y in range(len(g)):
    for x in range(len(g[y])):
        gg[(x,y)] = set()
        if g[y][x] == 'S':
            s = (x,y)
        elif g[y][x] == 'E':
            e = (x,y)
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1),]:
            if 0 <= y+dy < len(g) and 0 <= x+dx < len(g[y]):
                if ab[g[y+dy][x+dx]] <= ab[g[y][x]]+1:
                    gg[(x,y)].add((x+dx, y+dy))
print(s,e)

v = {s}
n = 0
ne = {s}
while ne:
    t = set()
    for nn in ne:
        if nn == e:
            print(n)
            #submit(n)
            exit()
        for a in gg[nn]:
            if not a in v:
                t.add(a)
    ne = t
    n += 1

#print(gg)
"""
a = set()
for y in range(len(g)):
    for x in range(len(g[y])):
        gg[(x,y)] = set()
        if g[y][x] == 'a':
            a.add((x,y))
        elif g[y][x] == 'E':
            e = (x,y)
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1),]:
            if 0 <= y+dy < len(g) and 0 <= x+dx < len(g[y]):
                if ab[g[y+dy][x+dx]] >= ab[g[y][x]]-1:
                    gg[(x,y)].add((x+dx, y+dy))

v = {e}
n = 0
ne = {e}
while ne:
    t = set()
    for nn in ne:
        if nn in a:
            print(n)
            #submit(n)
            exit()
        for b in gg[nn]:
            if not b in v:
                t.add(b)
    ne = t
    n += 1
