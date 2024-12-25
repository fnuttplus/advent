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

ls = stdin.read() if t else get_data(day=15)
print(ls)
l = [list(x) for x in ls.split('\n\n')[0].split('\n')]
g = Grid(l)

moves = ls.split('\n\n')[1]

ll = []
for y in range(len(l)):
    ll.append([])
    for x in range(len(l[0])):
        c = l[y][x]
        if c == '#': ll[y] += ['#','#']
        if c == 'O': ll[y] += ['[',']']
        if c == '.': ll[y] += ['.','.']
        if c == '@': ll[y] += ['@','.']

g = Grid(ll)
x,y = g.find('@')

print(g, x,y)

def try_move_box(x,y,dx,dy):
    if g[x+dx, y+dy] == '.':
        return True
    elif dy == 0 and (g[x+dx, y+dy] == '[' or g[x+dx, y+dy] == ']'):
        return try_move_box(x+dx, y+dy, dx, dy)
    elif g[x+dx, y+dy] == '[':
        if try_move_box(x+dx, y+dy, dx, dy) and try_move_box(x+dx+1, y+dy, dx, dy):
            return True
        return False
    elif g[x+dx, y+dy] == ']':
        if try_move_box(x+dx, y+dy, dx, dy) and try_move_box(x+dx-1, y+dy, dx, dy):
            return True
        return False
    elif g[x+dx, y+dy] == '#':
        return False


def move_box(x,y,dx,dy):
    if g[x+dx, y+dy] == '.':
        g.swap(x, y, x+dx, y+dy)
        return True
    elif dy == 0 and (g[x+dx, y+dy] == '[' or g[x+dx, y+dy] == ']'):
        if move_box(x+dx, y+dy, dx, dy):
            g.swap(x, y, x+dx, y+dy)
            return True
        return False

    elif g[x+dx, y+dy] == '[':
        if try_move_box(x+dx, y+dy, dx, dy) and try_move_box(x+dx+1, y+dy, dx, dy):
            move_box(x+dx, y+dy, dx, dy)
            move_box(x+dx+1, y+dy, dx, dy)
            g.swap(x, y, x+dx, y+dy)
            return True
        return False
    elif g[x+dx, y+dy] == ']':
        if try_move_box(x+dx, y+dy, dx, dy) and try_move_box(x+dx-1, y+dy, dx, dy):
            move_box(x+dx, y+dy, dx, dy)
            move_box(x+dx-1, y+dy, dx, dy)
            g.swap(x, y, x+dx, y+dy)
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

    can_move = False
    if g[x+dx, y+dy] == '.':
        can_move = True
    elif dy == 0 and (g[x+dx, y+dy] == '[' or g[x+dx, y+dy] == ']'):
        if move_box(x+dx, y+dy, dx, dy):
            can_move = True
    elif g[x+dx, y+dy] == '[':
        if try_move_box(x+dx, y+dy, dx, dy) and try_move_box(x+dx+1, y+dy, dx, dy):
            move_box(x+dx, y+dy, dx, dy)
            move_box(x+dx+1, y+dy, dx, dy)
            can_move = True
    elif g[x+dx, y+dy] == ']':
        if try_move_box(x+dx, y+dy, dx, dy) and try_move_box(x+dx-1, y+dy, dx, dy):
            move_box(x+dx, y+dy, dx, dy)
            move_box(x+dx-1, y+dy, dx, dy)
            can_move = True
    elif g[x+dx, y+dy] == '#':
        pass
    if can_move:
        g[x, y] = '.'
        x += dx
        y += dy
        g[x, y] = '@'

    if t: print(c)
    if t: print(g)
    #g.save_image(i)
    i += 1

for x,y in g.find_all('['):
    s += 100*y+x
print(i)

if t:
    print(s)
else:
    #1535509
    print(s)
