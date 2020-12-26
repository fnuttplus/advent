from sys import stdin
from PIL import Image

g = [list(line) for line in stdin.read().splitlines()]
m = 28
c = [[[['.' for _ in range(m)] for _ in range(m)] for _ in range(m)] for _ in range(m)]
print(c)

def adj(v,x,y,z):
    global g
    n = 0
    for dz in (-1, 0, 1):
        for dy in (-1, 0, 1):
            for dx in (-1, 0, 1):
                for dv in (-1, 0, 1):
                    if dz == dy == dx == dv == 0: continue
                    if 0 <= z + dz < m and 0 <= y + dy < m and 0 <= x + dx < m and 0 <= v + dv < m:
                        if c[z+dz][y+dy][x+dx][v+dv] == "#":
                            n += 1
    return n

for y in range(len(g)):
    for x in range(len(g[y])):
        print(y, x, g[y][x])
        if g[y][x] == "#":
            c[m//2][m//2][m//2+y][m//2+x] = "#"

for i in range(6):
    print("CYCLE", i)
    a = set()
    b = set()
    for z in range(m):
        for y in range(m):
            for x in range(m):
                for v in range(m):
                    if c[z][y][x][v] == "#":
                        if not (2 <= adj(v,x,y,z) <= 3):
                            a.add((v,x,y,z))
                    else:
                        if adj(v,x,y,z) == 3:
                            b.add((v,x,y,z))

    for (v,x,y,z) in a:
        c[z][y][x][v] = "."
    for (v,x,y,z) in b:
        c[z][y][x][v] = "#"

    n = 0
    for z in range(m):
        for w in range(m):
            #print(z, w)
            for cc in c[z][w]:
                n += cc.count('#')
                #print(''.join(cc))
    print(n)
