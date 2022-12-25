from sys import stdin
from aocd import get_data, submit

s = 0
for l in get_data(day=2).splitlines():
    a,b = l.split(' ')

    if b == 'X':
        if a == 'A':
            s += 3
        if a == 'B':
            s += 1
        if a == 'C':
            s += 2

    if b == 'Y':
        s += 3
        if a == 'A':
            s += 1
        if a == 'B':
            s += 2
        if a == 'C':
            s += 3

    if b == 'Z':
        s += 6
        if a == 'A':
            s += 2
        if a == 'B':
            s += 3
        if a == 'C':
            s += 1
print(s)
