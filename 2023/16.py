from sys import stdin
from re import findall
from aoc import Grid

g = Grid().from_stdin()

def sol(l):

    light = set()
    while l:
        nl = set()
        for b in l:
            x,y,d = b
            light.add((x,y,d))
            nd = [d]
            if g[x,y] == '.':
                pass
            elif g[x,y] == '\\':
                nd = [(d[1], d[0])]
            elif g[x,y] == '/':
                nd = [(-d[1], -d[0])]
            elif g[x,y] == '|':
                if d == (0,1) or d == (0,-1):
                    pass
                else:
                    nd = ((d[1], d[0]), (-d[1], -d[0]))
            elif g[x,y] == '-':
                if d == (1,0) or d == (-1,0):
                    pass
                else:
                    nd = ((d[1], d[0]), (-d[1], -d[0]))
            for dd in nd:
                dx,dy = dd
                if g.fit(x + dx,y + dy) and not (x + dx,y + dy,dd) in light:
                    nl.add((x + dx,y + dy,dd))
        l = list(nl)

    #for x,y,d in light: g[x,y] = '#'
    return len(set([(x,y) for x,y,_ in light]))
print(sol([(0,0,(1,0))]))
print(sol([(3,0,(0,1))]))

m = 0
for x in range(g.x()):
    s = sol([(x,0,(0,1))])
    if s > m: m = s
    s = sol([(x,g.y()-1,(0,-1))])
    if s > m: m = s
for y in range(g.y()):
    s = sol([(0,y,(1,0))])
    if s > m: m = s
    s = sol([(g.x()-1,y,(-1,0))])
    if s > m: m = s
print(m)