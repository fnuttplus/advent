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

ls = stdin.read() if t else get_data()

memo = {}

keypad = Grid([['7','8','9'],['4','5','6'],['1','2','3'],['','0','A']])
kx,ky,kc = 2,3,'A'
keypad2 = Grid([['','^','A'],['<','v','>']])
k2x,k2y,k2c = 2,0,'A'
k3x,k3y,k3c = 2,0,'A'

def move_key(x,y,c):
    global kx,ky,kc
    cx,cy = keypad.find(c)
    bfs = list(keypad.bfs2(x,y, cx,cy))
    kx,ky,kc = cx,cy,c
    l = len(bfs[0])
    for d in bfs:
        if len(d) == l:
            yield ''.join([{(1,0):'>', (0,1):'v', (-1,0):'<', (0,-1):'^'}[dd] for dd in d])

def move_key2(x,y,c):
    global k2x,k2y,k2c
    cx,cy = keypad2.find(c)
    bfs = list(keypad2.bfs2(x,y, cx,cy))
    k2x,k2y,k2c = cx,cy,c
    l = len(bfs[0])
    for d in bfs:
        if len(d) == l:
            yield ''.join([{(1,0):'>', (0,1):'v', (-1,0):'<', (0,-1):'^'}[dd] for dd in d])
def move_key3(x,y,c):
    global k3x,k3y,k3c
    cx,cy = keypad2.find(c)
    bfs = list(keypad2.bfs2(x,y, cx,cy))
    k3x,k3y,k3c = cx,cy,c
    l = len(bfs[0])
    for d in bfs:
        if len(d) == l:
            yield ''.join([{(1,0):'>', (0,1):'v', (-1,0):'<', (0,-1):'^'}[dd] for dd in d])


for code in ls.splitlines():
    n = int(code[:-1])
    print(code)

    kx,ky,kc = 2,3,'A'
    new_codes = ['']
    for c in code:
        ns = []
        mk = list(move_key(kx,ky,c))
        for nn in new_codes:
            ns += [nn + k + 'A' for k in mk]
        new_codes = ns

    print(new_codes)
    new_codes.sort(key=lambda x: len(x))
    k2x,k2y,k2c = 2,0,'A'
    newcodes2 = set()
    for nc in new_codes:
        new_codes2 = ['']
        for c in nc:
            ns = []
            mk = list(move_key2(k2x,k2y,c))
            for nn in new_codes2:
                ns += [nn + k + 'A' for k in mk]
            new_codes2 = ns
        newcodes2 |= set(new_codes2)
    newcodes2 = list(newcodes2)
    # sort by length
    newcodes2.sort(key=lambda x: len(x))
    # filter out the ones that are not shortest
    newcodes2 = [x for x in newcodes2 if len(x) == len(newcodes2[0])]
    print(newcodes2)

    #one more layer
    k3x,k3y,k3c = 2,0,'A'
    newcodes3 = set()
    for nc in newcodes2:
        new_codes3 = ['']
        for c in nc:
            ns = []
            mk = list(move_key3(k3x,k3y,c))
            for nn in new_codes3:
                ns += [nn + k + 'A' for k in mk]
            new_codes3 = ns
        newcodes3 |= set(new_codes3)
    newcodes3 = list(newcodes3)
    newcodes3.sort(key=lambda x: len(x))
    print(newcodes3)

    l = len(newcodes3[0])
    print(l, n)
    s += l * n

#<A^A>^^AvvvA
#v<<A>>^A<A>AvA<^AA>A<vAAA>^A
#v<<A>>^A<A>AvA<^AA>Av<AAA>^A

#<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
#v<A<AA>>^AvAA<^A>Av<<A>>^AvA^Av<A>^Av<<A>^A>AAvA^Av<A<A>>^AAAvA<^A>A

#<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A
#v<A<AA>>^AAvA<^A>AvA^Av<<A>>^AAvA^Av<A>^AA<A>Av<A<A>>^AAAvA<^A>A

if t:
    print()
    print('answer:', s)
    for i, e in enumerate(puzzle.examples): print(i, e)
else:
    submit(s)
