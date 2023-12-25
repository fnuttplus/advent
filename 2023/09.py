from sys import stdin
from aocd import get_data, submit
from re import findall

#d = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1),]

#grid = [list(x)+['.'] for x in stdin.read().splitlines()]

lines = stdin.read().splitlines()

s = 0
for line in lines:
    a = []
    a.append([int(x) for x in line.split(' ')])
    while a[-1].count(0) != len(a[-1]):
        a.append([a[-1][i] - a[-1][i-1] for i in range(1, len(a[-1]))])

#    print(a)
    for i in range(len(a) - 2, -1, -1):
#        a[i].append(a[i+1][-1] + a[i][-1])
        a[i].insert(0, a[i][0] - a[i+1][0])
#    print(a)
    s += a[0][0]

print(s)