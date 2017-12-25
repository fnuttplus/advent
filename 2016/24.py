from sys import stdin
from itertools import permutations

maze = stdin.read().splitlines()

def sp(s,e,room):
    n = [s]
    d = 0
    i = 1
    while n:
        if e in n: return d
        d += 1
        nn = []
        for y,x in n:
            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                if 0 <= y+dy < len(room) and 0 <= x+dx < len(room[0]):
                    if room[y+dy][x+dx] is 0:
                        room[y+dy][x+dx] = 1
                        nn.append((y+dy,x+dx))
        n = nn

loc = {}
for y in range(len(maze)):
    for x in range(len(maze[0])):
        c = maze[y][x]
        if c in "12345670":
            loc[int(c)] = (y,x)
print(loc)
print()

dist = [[0 for _ in range(len(loc))] for _ in range(len(loc))]
for i in range(len(dist)):
    for j in range(i+1, len(dist)):
        d = sp(loc[i], loc[j], [[1 if c is '#' else 0 for c in row] for row in maze])
        dist[i][j] = d
        dist[j][i] = d

for i in range(len(dist)):
    for j in range(len(dist)):
        print("%4d"%(dist[i][j]), end='')
    print()
print()

md = 1000
for p in permutations(range(1, len(loc))):
    d = 0
    n0 = 0
    for n in p:
        d+=dist[n0][n]
        n0 = n
    d += dist[n][0]
    if d < md: md = d
print(md)
