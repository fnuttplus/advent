from sys import stdin
from aocd import get_data, submit
from re import findall
from itertools import product, combinations
from aoc import Grid, adj

s = 0

r = {}

t = True
t = False

ls = stdin.read() if t else get_data()
ls = list(map(int, ls.split(' ')))

print(ls)

for a in range(75):
    i = 0
    while i < len(ls):
        c = str(ls[i])
        # print(c)
        if ls[i] == 0:
            ls[i] = 1
        elif len(c) % 2 == 0:
            # print(c, c[:len(c)//2], c[len(c)//2:])
            ls[i] = int(c[:len(c)//2])
            ls.insert(i+1, int(c[len(c)//2:]))
            i += 1
        else:
            ls[i] = ls[i] * 2024
        i += 1
    print(a, len(ls))

if t:
    print(s)
else:
    submit(len(ls))
