from sys import stdin
from re import findall
from aoc import Grid

#g = Grid().from_stdin()

lines = stdin.read().split(',')

s = 0
boxes = {n: [] for n in range(256)}
lbls = {}
for line in lines:
    cv = 0
    lb = ''
    for c in line:
        if c in "-=": break
        lb += c
        cv = (17 * (cv + ord(c))) % 256
    if c == '-':
        if lb in lbls:
            boxes[lbls[lb][1]].remove(lb)
            del lbls[lb]
    if c == '=':
        n = int(line[-1])
        if not lb in lbls:
            boxes[cv].append(lb)
        lbls[lb] = (n, cv)
    s += cv
#print(boxes)
#print(lbls)

s = 0
for lb in lbls:
    s += (lbls[lb][1] +1) * lbls[lb][0] * (boxes[lbls[lb][1]].index(lb)+1)
print(s)