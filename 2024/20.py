from sys import stdin
from aocd import get_data, submit, puzzle
from re import findall
from itertools import product, combinations
from aoc import Grid, adj
from sympy.solvers import solve
from sympy import *
from oklab import viridis

s = 0
t = True
t = False

ls = puzzle.examples[0].input_data if t else get_data()
print(len(puzzle.examples), 'examples')
print(puzzle.examples)
print()

l = [list(x) for x in ls.strip().split('\n')]
g = Grid(l)

# Starting and ending points
x0, y0 = g.find('S')
x1, y1 = g.find('E')
g[x0,y0] = '.'
g[x1,y1] = '.'

print(x0,y0,x1,y1)
print(g)
v = viridis(5)
d = {".": v[1], "#": v[0], "O": v[2], "C": v[3]}
g.save_image_file(d, f"advent20.png")
bfs0 = g.bfs(x0,y0, x1,y1)
print(len(bfs0)-1)
bb = len(bfs0)-1

cc = {}
for i,(x,y) in enumerate(bfs0):
#    for dx,dy in [(1,0), (0,1), (-1,0), (0,-1)]:
#        if g[x+dx,y+dy] == '#' and (x+2*dx,y+2*dy) in bfs0[i:]:
    for j,(x2,y2) in enumerate(bfs0[i+1:]):
        if abs(x2-x)+abs(y2-y) <= 20:
            b = j+1 - (abs(x2-x)+abs(y2-y))
            if b > 0:
                #if t: print(x,y,x2,y2,i,j,b)
                if b in cc:
                    cc[b].append((x,y,x2,y2,i,j))
                else:
                    cc[b] = [(x,y,x2,y2,i,j)]

for c in cc:
    if c != 0 and c >= 9200:
        print(c, cc[c])
        #s += cc[c]

n= 0
for c in sorted(cc.keys()):
    gc = g.copy()
    x,y,x2,y2,i,j = cc[c][0]
    print(c, x,y,x2,y2,i,j)
    for x0,y0 in bfs0[:i]:
        gc[x0,y0] = 'O'
    for x0 in range(min(x,x2), max(x,x2)+1):
        gc[x0,y] = 'C'
    for y0 in range(min(y,y2),max(y,y2)+1):
        gc[x2,y0] = 'C'
    for x0,y0 in bfs0[j+i+2:]:
        gc[x0,y0] = 'O'
    gc.save_image_file(d, f"frames/advent{n}.png")
    n += 1


if t:
    print()
    print('answer:', s)
    for i, e in enumerate(puzzle.examples): print(i, e)
else:
    print(s)
