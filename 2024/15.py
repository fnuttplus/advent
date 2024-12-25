from sys import stdin
from aocd import get_data, submit
from re import findall
from itertools import product, combinations
from aoc import Grid, adj
from sympy.solvers import solve
from sympy import *

s = 0

r = []

t = True
t = False

ls = stdin.read() if t else get_data()

l = [list(x) for x in ls.split('\n\n')[0].split('\n')]
g = Grid(l)

x,y = g.find('@')
moves = ls.split('\n\n')[1]

print(g, x,y)

def move_box(x,y,dx,dy):
    if g[x+dx, y+dy] == '.':
        g[x, y] = '.'
        x += dx
        y += dy
        g[x, y] = 'O'
        return True
    elif g[x+dx, y+dy] == 'O':
        if move_box(x+dx, y+dy, dx, dy):
            g[x, y] = '.'
            x += dx
            y += dy
            g[x, y] = 'O'
            return True
        return False
    elif g[x+dx, y+dy] == '#':
        return False

i = 0
for c in moves:
    if c == '<':
        dx,dy = -1,0
    elif c == '>':
        dx,dy = 1,0
    elif c == '^':
        dx,dy = 0,-1
    elif c == 'v':
        dx,dy = 0,1
    else: continue

    if g[x+dx, y+dy] == '.':
        g[x, y] = '.'
        x += dx
        y += dy
        g[x, y] = '@'
    elif g[x+dx, y+dy] == 'O':
        if move_box(x+dx, y+dy, dx, dy):
            g[x, y] = '.'
            x += dx
            y += dy
            g[x, y] = '@'
    elif g[x+dx, y+dy] == '#':
        pass
    if t: print(c)
    if t: print(g)
    #g.save_image(i)
    i += 1

for x,y in g.find_all('O'):
    s += 100*y+x
print(i)

if t:
    print(s)
else:
    #1517080
    print(s)
