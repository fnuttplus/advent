from sys import stdin
from re import findall
from aoc import Grid

def h_reflect(g, i):
    j = 1
    rows = [x[1] for x in g.rows()]
    while i-j >= 0 and i < g.y():
        if rows[i-j] != rows[i]:
            return False
        i += 1
        j += 2
    return True

def v_reflect(g, i):
    j = 1
    rows = [x[1] for x in g.cols()]
    while i-j >= 0 and i < g.x():
        if rows[i-j] != rows[i]:
            return False
        i += 1
        j += 2
    return True

def l_reflect(g, skip = (-1, -1)):
    v,h = 0,0
    pr = []
    for i, row in g.rows():
        if row == pr:
            if h_reflect(g, i) and i != skip[0]:
                return (i, 0)
        pr = row
    pc = []
    for i, col in g.cols():
        if col == pc:
            if v_reflect(g, i) and i != skip[1]:
                return (0, i)
        pc = col
    return (h, v)

vs = 0
hs = 0
for grid in stdin.read().split('\n\n'):
    g = Grid([list(x) for x in grid.split('\n')])
    print()
    print(g)
    h0, v0 = l_reflect(g)
#    print(h0,v0)
    for x,y in g.xy():
        g[x, y] = '#' if g[x, y] == '.' else '.'
        h,v = l_reflect(g, (h0,v0))
        g[x, y] = '#' if g[x, y] == '.' else '.'
        if (h,v) != (0,0):
            if v0 != v:
                vs += v
                print('a', h0, v0, h,v, x, y)
            if h0 != h:
                hs += h
                print('b', h,v, x, y)
            break

print(hs*100+vs)