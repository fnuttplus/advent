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

program = [0,3,5,4,3,0] if t else [2,4,1,7,7,5,4,1,1,4,5,5,0,3,3,0]

#for a in range(100): print(a, ((((a % 8) ^ 7) ^ (a//(2**((a % 8) ^ 7)))) ^ 4) % 8)

aa = 0
i = -1
while True:
    output = []
    a = aa
    while True:
        if t:
            a = a//8 #0,3
            output.append(a % 8) #5,4
            if a == 0: break
        else:
            b = (a % 8) ^ 7
            output.append(((b ^ (a//(2**b))) ^ 4) % 8)
            a = a//8 #0,3
            if a == 0: break

    #if t: print(aa, output)
    if output == program:
        break
    if output[i:] == program[i:]:
        print(aa, output)
        i -= 1
        aa *= 8
    aa += 1

if t:
    print(aa, output)
else:
    print(aa)
