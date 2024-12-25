from sys import stdin
from aocd import get_data, submit
from re import findall
from itertools import product, combinations

s = 0

r = {}

ls = stdin.read().split('\n')

for y in range(len(ls)):
    for x in range(len(ls[y])):
        c = ls[y][x]
        if c == '.':
            pass
        elif c in r:
            r[c].append((x,y))
        else:
            r[c] = [(x,y)]

my = len(ls)-1
mx = len(ls[0])-1

nn = set()

for rr in r:
    for a,b in combinations(r[rr], 2):
        i = set()

        dx = a[0] - b[0]
        dy = a[1] - b[1]

        m = 1
        while a[0]-m*dx >= 0 and a[1]-m*dy >= 0 and a[0]-m*dx <= mx and a[1]-m*dy <= my:
            i.add((a[0]-m*dx, a[1]-m*dy))
            m+=1
        m = 1
        while a[0]+m*dx >= 0 and a[1]+m*dy >= 0 and a[0]+m*dx <= mx and a[1]+m*dy <= my:
            i.add((a[0]+m*dx, a[1]+m*dy))
            m+=1
        m = 1
        while b[0]-m*dx >= 0 and b[1]-m*dy >= 0 and b[0]-m*dx <= mx and b[1]-m*dy <= my:
            i.add((b[0]-m*dx, b[1]-m*dy))
            m+=1
        m = 1
        while b[0]+m*dx >= 0 and b[1]+m*dy >= 0 and b[0]+m*dx <= mx and b[1]+m*dy <= my:
            i.add((b[0]+m*dx, b[1]+m*dy))
            m+=1
        print(a,b, dx, dy, i)

        nn |= i

        print(a,b)

submit(len(nn))

for y in range(len(ls)):
    for x in range(len(ls[y])):
        if (x,y) in nn:
            print('#', end='')
        else:
            print(ls[y][x], end='')
    print()