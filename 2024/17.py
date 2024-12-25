from sys import stdin
from aocd import get_data, submit
from re import findall
from itertools import product, combinations
from aoc import Grid, adj
from sympy.solvers import solve
from sympy import *

s = 0
t = True
t = False

ls = stdin.read() if t else get_data()

la = ls.split('\n\n')[0]

r = {}


for a in la.split('\n'):
    b = a.split(' ')

    r[b[1][:-1]] = int(b[2])

print(r)
program = list(map(int, ls.split('\n\n')[1].split(' ')[1].split(',')))
print(program)

ip = 0

output = []

while True:
    if ip >= len(program): break
    a,b = program[ip], program[ip+1]

    if t: print(a,b)

    c = b
    if b == 4: c = r['A']
    if b == 5: c = r['B']
    if b == 6: c = r['C']

    if a == 0:
        r['A'] = r['A'] // (2**c)
    elif a == 1:
        r['B'] = r['B'] ^ b
    elif a == 2:
        r['B'] = c % 8
    elif a == 3:
        if r['A'] != 0:
            ip = b -2
    elif a == 4:
        r['B'] = r['B'] ^ r['C']
    elif a == 5:
        output.append(c % 8)
    elif a == 6:
        r['B'] = r['A'] // (2**c)
    elif a == 7:
        r['C'] = r['A'] // (2**c)

    if t: print(r)

    ip += 2

print(output)

if t:
    print(output)
else:
    print(','.join(map(str, output)))
