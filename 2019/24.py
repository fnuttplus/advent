from sys import stdin
m = [list(r) for r in stdin.read().splitlines()]

bb = set()
d = [(-1,0),(1,0),(0,-1),(0,1),]
while True:
    die = []
    infest = []
    for y in range(len(m)):
        for x in range(len(m[0])):
            n = 0
            for dx, dy in d:
                if len(m) > y+dy >= 0 and len(m[0]) > x+dx >= 0:
                    if m[y+dy][x+dx] == "#":
                        n += 1
            if m[y][x] == "#":
                if n != 1: die.append((x,y))
            elif m[y][x] == ".":
                if n == 1 or n == 2: infest.append((x,y))
    for x,y in die:
        m[y][x] = "."

    for x,y in infest:
        m[y][x] = "#"

    b = (int(''.join(['1' if x == "#" else '0' for y in m for x in y])[::-1], 2))
    if b in bb: break
    bb.add(b)
print(b)