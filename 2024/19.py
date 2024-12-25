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
print()

towels = ls.split('\n\n')[0].split(', ')
print(towels)

memo = {}
def parse(p):
    if p in memo:
        return memo[p]
    if len(p) == 0:
        memo[p] = 1
        return 1
    count = 0
    for token in towels:
        if p.startswith(token):
            #if t: print(p, '->', token)
            count += parse(p[len(token):])
    memo[p] = count
    return count

for p in ls.split('\n\n')[1].split('\n'):
    print(p, parse(p))
    s += parse(p)

if t:
    print()
    print('answer:', s)
    for i, e in enumerate(puzzle.examples): print(i, e)
else:
    submit(s)
