from sys import stdin
from re import findall
from aoc import Grid
import heapq

#g = Grid().from_stdin()

lines = stdin.read().splitlines()

s = 0
x,y = 0,0
visited = [(0,0)]
for line in lines:
    _,_,c = line.split(' ')
    a = "RDLU"[int(c[-2])]
    b = int(c[2:-2], 16)
    print(a,b)
    d = {
        'R': (1,0),
        'L': (-1,0),
        'D': (0,1),
        'U': (0,-1)
    }[a]
    x += d[0] * b
    y += d[1] * b
    s += b
    visited.append((x,y))

#https://stackoverflow.com/a/24468019
def Area(corners):
    n = len(corners)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    return abs(area) // 2

print(Area(visited) +s//2 +1)
print(129849166997110)
exit()

s = 0
x,y = 0,0
visited = [(0,0)]
for line in lines:
    a,b,_ = line.split(' ')
    b = int(b)
    #print(a,b)
    d = {
        'R': (1,0),
        'L': (-1,0),
        'D': (0,1),
        'U': (0,-1)
    }[a]
    for i in range(b):
        x += d[0]
        y += d[1]
        visited.append((x,y))

print(len(visited))

minx = min([x[0] for x in visited])
maxx = max([x[0] for x in visited])
miny = min([x[1] for x in visited])
maxy = max([x[1] for x in visited])

print(minx, maxx, miny, maxy)
g = Grid([['#' if (x,y) in visited else '.' for x in range(minx, maxx+1)] for y in range(miny, maxy+1)])
g.save_image({'#': (92, 131, 116), '.': (9, 38, 53)})
g.flood_fill(156,1,'.','#')
print(g.count('#'))
