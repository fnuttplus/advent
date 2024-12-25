from sys import stdin
from aocd import get_data, submit
from re import findall
from itertools import product, combinations
from aoc import Grid, adj

s = 0

r = {}

t = True
#t = False

ls = stdin.read() if t else get_data()
ls = [list(map(int, [-1 if ll == '.' else ll for ll in list(l)])) for l in ls.split('\n')]

g = Grid(ls)

ss = list(g.find_all(0))

if t: print(ss, len(ss))

def dfs(x0,y0):
    q = [(x0, y0)]
    while q:
        (x,y) = q.pop()
        if ls[y][x] == 9:
            yield (x,y)
        for x1,y1 in adj(x,y):
            if g.fit(x1,y1) and ls[y1][x1] == ls[y][x] +1:
                q.append((x1,y1))

for p in ss:
    if t: print(p, len(set(dfs(p[0],p[1]))))
    s += len(list(dfs(p[0],p[1])))

if t:
    print(s)
else:
    submit(s)
