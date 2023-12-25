from sys import stdin
from re import findall
from aoc import Grid
from copy import deepcopy as copy
from heapq import heappush
import time


g = Grid().from_stdin()
#gc = [[g.copy() for _ in range(5)] for _ in range(5)]

slopes = '^>v<'

for x,y in g.xy():
    if g[x,y] in slopes:
        g[x,y] = '.'

nodes = {(1,0): {}}
q = [((1, 1), 1, (1,0), (1,0), [(1, 1)])]
while q:
    (x,y), i, n, p, pp = q.pop()
    if (x == g.x()-2 and y == g.y()-1):
        nodes[n][(x,y)] = (i, pp)
        continue
    if (x,y) in nodes:
        nodes[(x,y)][n] = (i, list(reversed(pp[:-1])))
        nodes[n][(x,y)] = (i, pp[:-1])
        continue
    candidates = [(x1,y1) for x1,y1 in [(x+1, y),(x-1, y),(x, y+1),(x, y-1),] if g[x1,y1] == '.' and (x1,y1) != p]
    if len(candidates) > 1:
        nodes[n][(x,y)] = (i, pp[:-1])
        if (x,y) not in nodes:
            nodes[(x,y)] = {n: (i, list(reversed(pp[:-1])))}
        i = 0
        n = (x,y)
        pp = []
    for c in candidates:
        q.append((c, i+1, n, (x,y), pp+[c]))

for node in nodes:
    g[node[0], node[1]] = len(nodes[node])
    for nn in nodes[node]:
        print(node, nn, nodes[node][nn][0], len(nodes[node][nn][1]))

#part1 solution
path = [(1,0), (17, 5), (13, 35), (9, 63), (41, 61), (33, 75), (31, 111), (61, 103), (77, 99), (109, 101), (99, 135), (127, 123), (139, 140)]
a = path[0]
gc = g.copy()
for b in path[1:]:
    for x,y in nodes[a][b][1]:
        gc[x,y] = 'O'
    a = b
gc.save_image_file({
    '#': (9, 38, 53),
    '.': (27, 66, 66),
    '1': (92, 131, 116),
    'O': (92, 131, 116),
    '3': (158, 200, 185),
    '4': (158, 200, 185),
}, f'2023.23.0.png')

#exit()
node = (1,0)
q = [(node, [node])]
m = 0
i = 1
while q:
    node, path = q.pop()
    #print(node, path)
    if node == (139, 140):
#        print(path)
        s = 0
        a = path[0]
        for b in path[1:]:
            s += nodes[a][b][0]
            a = b
        #if s > 6700: print(s)
        #if s == 2186: print(path)
        if s > m:
            m = s
            #print(path)
            a = path[0]
            gc = g.copy()
            for b in path[1:]:
                for x,y in nodes[a][b][1]:
                    gc[x,y] = 'O'
                a = b
            gc.save_image_file({
                '#': (9, 38, 53),
                '.': (27, 66, 66),
                '1': (92, 131, 116),
                'O': (92, 131, 116),
                '3': (158, 200, 185),
                '4': (158, 200, 185),
            }, f'2023.23.{i}.png')
            i += 1
            print(s)
        continue
    for adj in nodes[node]:
        if adj not in path:
            q.append((adj, path + [adj]))

