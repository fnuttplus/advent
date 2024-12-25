from sys import stdin
from aocd import get_data, submit
from re import findall
from itertools import product, combinations
from aoc import Grid, adj
from sympy.solvers import solve
from sympy import *

s = 0

r = {}

t = True
#t = False

ls = stdin.read() if t else get_data()

for p in ls.split('\n\n'):
    pp = p.split('\n')
    ax,ay = map(int, findall('\+\d+', pp[0]))
    bx,by = map(int, findall('\+\d+', pp[1]))
    tx,ty = map(int, [x[1:] for x in findall('=\d+', pp[2])])
    #tx += 10000000000000
    #ty += 10000000000000
    if t: print(tx, ty)

    var('a b')

    eq1 = Eq(a * ax + b*bx, tx)
    eq2 = Eq(a * ay + b*by, ty)


    output = solve([eq1,eq2],a,b,dict=True)
    print(len(output), output, output[0][a].is_Integer , output[0][b].is_Integer )
    if (output[0][a].is_Integer  and output[0][b].is_Integer ):
        s += 3*int(output[0][a]) + int(output[0][b])

    det = ax * by - bx * ay
    a = (by * tx - bx * ty) / det
    b = (ax * ty - ay * tx) / det
    print(a, b)

    continue
    c = 10**100
    for a in range(100):
        for b in range(100):
            if a*ax + b*bx == tx and a*ay + b*by == ty:
                if c > a*3+b*1: c = a*3+b*1

    s += c if c != 10**100 else 0
    if t: print(c)

if t:
    print(s)
else:
    submit(s)
