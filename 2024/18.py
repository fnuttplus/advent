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
#t = False

ls = puzzle.examples[0].input_data if t else get_data()
print(len(puzzle.examples), 'examples')
print(puzzle.examples)

x0,y0 = 0,0
x1,y1 = (6,6) if t else (70,70)

g = Grid([['.' for _ in range(y1+1)] for _ in range(x1+1)])

b = 12 if t else 1024

v = viridis(5)
d = {".": v[0], "#": v[1], "O": v[3]}
for b, l in enumerate(ls.splitlines()):
    x,y = map(int, l.split(','))
    g[x,y] = '#'
    bfs = g.bfs(x0,y0, x1,y1)
    if len(bfs) == 0:
        #g.save_image_file(d, f"frames/advent{b}.png")
        print(f'{x},{y}')
    if b == (12 if t else 1024):
        print(len(bfs) -1)
        for x,y in bfs:
            g[x,y] = 'O'
        #g.save_image_file(d, f"frames/advent{b}.png")
        for x,y in bfs:
            g[x,y] = '.'

if t:
    print(s)
    print('A', puzzle.examples[0].answer_a)
    print('B', puzzle.examples[0].answer_b)
else:
    print(len(bfs)-1)
