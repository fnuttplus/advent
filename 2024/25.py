from sys import stdin
from aocd import get_data, submit, puzzle
from aocd.models import Puzzle
from itertools import product, combinations
from aoc import Grid, adj
from oklab import viridis
from re import findall # 2024-03
from sympy.solvers import solve # 2024-13
from sympy import *
import networkx as nx # 2024-23
import matplotlib.pyplot as plt
from schemdraw.parsing import logicparse # 2024-24

s = 0
t = True
#t = False

ls = puzzle.examples[0].input_data if t else get_data()
#ls = stdin.read() if t else get_data()

memo = {}

locks = []
keys = []

for sce in ls.split('\n\n'):
    r = sce.split('\n')
    # rotate the grid
    rr = list(zip(*r))
    pin_heights = []
    if t: print(rr)

    if r[0] == '#####': #its a lock
        for i in range(5):
            pin_heights.append(rr[i].index('.') -1)
        locks.append(pin_heights)
    else:
        for i in range(5):
            pin_heights.append(5-(rr[i].index('#') -1))
        keys.append(pin_heights)
    if t: print(pin_heights)

for lock in locks:
    for key in keys:
        if not any([key[i] + lock[i] > 5 for i in range(5)]):
            if t: print(lock, key, 'fit')
            s += 1

if t:
    print()
    print('answer:', s)
    for i, e in enumerate(puzzle.examples): print(i, e)
else:
    submit(s)
