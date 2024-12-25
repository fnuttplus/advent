from sys import stdin
from aocd import get_data, submit
from re import findall
from itertools import product

s = 0

ls = stdin.read().split('\n')
for l in ls:
    a, b = l.split(': ')
    a = int(a)
    b = list(map(int, b.split(' ')))
    print(a, b)

    for op in product("*+|", repeat=len(b)-1):
        bb = b[0]
        for i in range(len(op)):
            if op[i] == "*":
                bb *= b[i+1]
            if op[i] == "+":
                bb += b[i+1]
            if op[i] == "|":
                bb = int(str(bb) + str(b[i+1]))
        if a == bb:
            s += a
            print(a, op)
            break

print(s)
