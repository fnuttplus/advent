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

#ls = puzzle.examples[0].input_data if t else get_data()
ls = stdin.read() if t else get_data()

memo = {}

keypad = Grid([['7','8','9'],['4','5','6'],['1','2','3'],['','0','A']])
keypad2 = Grid([['','^','A'],['<','v','>']])

def sequences(k,c,pad):
    bfs = list(pad.bfs2(pad.find(k), pad.find(c)))
    l = len(bfs[0])
    return [''.join([{(1,0):'>', (0,1):'v', (-1,0):'<', (0,-1):'^'}[dd] for dd in d]) for d in bfs if len(d) == l]

def sequence_length(code, depth):
    if (code, depth) in memo:
        return memo[(code, depth)]
    if depth == 0:
        return len(code)
    k = 'A'
    ll = 0
    for c in code:
        ll += min([sequence_length(m+'A', depth-1) for m in sequences(k,c,keypad2)])
        k = c
    memo[(code, depth)] = ll
    return ll

for code in ls.splitlines():
    n = int(code[:-1])
    print(code)

    k = 'A'
    new_codes = ['']
    for c in code:
        ns = []
        mk = sequences(k,c,keypad)
        k = c
        for nn in new_codes:
            ns += [nn + k + 'A' for k in mk]
        new_codes = ns
    print(new_codes)

    l = min([sequence_length(nc, 25) for nc in new_codes])
    print(l, n)
    s += l * n

if t:
    print()
    print('answer:', s)
    for i, e in enumerate(puzzle.examples): print(i, e)
else:
    submit(s)
