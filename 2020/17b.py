from sys import stdin

g = [list(line) for line in stdin.read().splitlines()]
active = set()

def adj_active(c):
    w,z,y,x = c
    n = 0
    for dw in (-1, 0, 1):
        for dz in (-1, 0, 1):
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    if dw == dz == dy == dx == 0: continue
                    if (w+dw, z+dz, y+dy, x+dx) in active:
                        n += 1
    return n

def adj_inactive(c):
    w,z,y,x = c
    for dw in (-1, 0, 1):
        for dz in (-1, 0, 1):
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    if dw == dz == dy == dx == 0: continue
                    if not (w+dw, z+dz, y+dy, x+dx) in active:
                        yield (w+dw, z+dz, y+dy, x+dx)

for y in range(len(g)):
    for x in range(len(g[y])):
        if g[y][x] == "#":
            active.add((0,0,y,x))

for i in range(6):
    print("CYCLE", i+1)
    a = set()
    b = set()

    for cube in active:
        if not (2 <= adj_active(cube) <= 3):
            a.add(cube)
        for adj in adj_inactive(cube):
            if adj_active(adj) == 3:
                b.add(adj)
    active -= a
    active |= b
    print(len(active))

