from sys import stdin
#from aocd import lines, submit
from aoc import matrix

lines = stdin.read().splitlines()

numbers = list(map(int, lines[0].split(',')))

b = []
for l in range(2, len(lines), 6):
    bb = matrix()
    bb.fromLines(lines[l:l+5], ' ')
    b.append(bb)
#print(b)
for n in numbers:
    for bb in b:
        bb.bingo(n)
    for bb in b:
        if (None,None,None,None,None) in bb.rotation() or [None,None,None,None,None] in bb.data:
            print(bb.sum() * n)
            b.remove(bb)
