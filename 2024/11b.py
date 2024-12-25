from sys import stdin
from aocd import get_data, submit
from re import findall
from itertools import product, combinations
from aoc import Grid, adj

s = 0

r = {}

t = True
#t = False

ls = stdin.read() if t else get_data()
ls = list(map(int, ls.split(' ')))

print(ls)
memo = {}

def rec(l, d):
    #print(l, d)
    if d == 0:
        return 1
    if (l, d) in memo: return memo[(l, d)]
    if l == 0:
        r = rec(1, d-1)
    elif len(str(l)) % 2 == 0:
        c = str(l)
        r = rec(int(c[:len(c)//2]), d-1) + rec(int(c[len(c)//2:]), d-1)
    else:
        r = rec(l * 2024, d-1)
    memo[(l,d)] = r
    return r

for l in ls:
    s += rec(l, 75)

if t:
    print(s)
else:
    submit(len(ls))
