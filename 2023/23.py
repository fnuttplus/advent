from sys import stdin
from re import findall
from aoc import Grid
from copy import deepcopy as copy
import heapq
import time


g = Grid().from_stdin()
#gc = [[g.copy() for _ in range(5)] for _ in range(5)]

slopes = '^>v<'
print(g)
m = 0
q = [((1, 0), 0, [(1, 0)])]
while q:
    (x,y), i, v = q.pop()
    #print(x,y)
    if x == g.x()-2 and y == g.y()-1:
        if i > m:
            m = i
            print(i)
            gc = g.copy()
            for x,y in v:
                gc[x,y] = 'O'
            gc.save_image({                '#': (9, 38, 53),
                '.': (27, 66, 66),
                '<': (27, 66, 66),
                '>': (27, 66, 66),
                'v': (27, 66, 66),
                '^': (27, 66, 66),
                '1': (92, 131, 116),
                'O': (92, 131, 116),
                '3': (158, 200, 185),
                '4': (158, 200, 185),}
)
        continue
    for x1,y1 in [(x+1, y),(x-1, y),(x, y+1),(x, y-1),]:
        if g[x1,y1] == '.' and (x1,y1) not in v:
            q.append(((x1,y1), i+1, v+[(x1,y1)]))
        if g[x1,y1] == '>' and (x1,y1) not in v and (x1+1,y1) not in v:
            q.append(((x1+1,y1), i+2, v+[(x1,y1),(x1+1,y1)]))
        if g[x1,y1] == '<' and (x1,y1) not in v and (x1-1,y1) not in v:
            q.append(((x1-1,y1), i+2, v+[(x1,y1),(x1-1,y1)]))
        if g[x1,y1] == 'v' and (x1,y1) not in v and (x1,y1+1) not in v:
            q.append(((x1,y1+1), i+2, v+[(x1,y1),(x1,y1+1)]))
        if g[x1,y1] == '^' and (x1,y1) not in v and (x1,y1-1) not in v:
            q.append(((x1+1,y1), i+2, v+[(x1,y1),(x1,y1-1)]))

print(m)