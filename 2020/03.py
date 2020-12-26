from sys import stdin

g  = [list(line) for line in stdin.read().splitlines()]

p = 1
for dx,dy in [(1,1),(3,1),(5,1),(7,1),(1,2),]:
    x,y,i = 0,0,0
    while y+dy < len(g):
        y += dy
        x += dx
        if x >= len(g[y]):
            x -= len(g[y])
        if g[y][x] == '#':
            i += 1
    print(i)
    p *= i
print(237*65*59*61*38)
print(p)