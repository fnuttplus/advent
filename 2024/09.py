from sys import stdin
from aocd import get_data, submit
from re import findall
from itertools import product, combinations

s = 0

r = {}

ls = stdin.read()
#ls = '2333133121414131402'

dd = []
i = 0
f = True
for c in ls:
    if f:
        dd += [i] * int(c)
        i += 1
    else:
        dd += [-1] * int(c)
    f = not f



b = len(dd) -1
for a in range(len(dd)):

    if dd[a] == -1:
        while dd[b] == -1:
            b -= 1
        if b <= a: break
        dd[a], dd[b] = dd[b], dd[a]
        #print(dd)

for i in range(a):
    #print(dd[i])
    s += i * dd[i]

submit(s)
