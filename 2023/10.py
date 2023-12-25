from sys import stdin
from re import findall

#d = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1),]

grid = [list(x) for x in stdin.read().splitlines()]

def neigh(x, y):
    for x1,y1 in [(x-1, y),(x, y+1),]:
        if 0 <= x1 < len(grid[0]) and 0 <= y1 < len(grid):
            yield x1, y1, grid[y1][x1]

pipes = {
    '|': ((0, -1), (0, 1)),
    '-': ((-1, 0), (1, 0)),
    '7': ((-1, 0), (0, 1)),
    'J': ((0, -1), (-1, 0)),
    'L': ((0, -1), (1, 0)),
    'F': ((0, 1), (1, 0)),
}

def pipe(x, y):
    if g in pipes:
        for dx, dy in pipes[g]:
            if 0 <= y+dy < len(grid) and 0 <= x+dx < len(grid[0]) and grid[y+dy][x+dx] in pipes:
                return x+dx, y+dy, grid[y+dy][x+dx]
    return False

sx, sy = -1, -1
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == 'S':
            sx = x
            sy = y
steps = 0
n = []
for x,y,g in neigh(sx, sy):
    if g in "|7LJF":
        n.append((x,y,g))
        grid[y][x] = 1
steps = 1

visited = []
visited.append((sx,sy,'7'))
visited.append(n[0])
visited.append(n[1])

while True:
    steps += 1
    a,b = n

    x,y,g = a
    n[0] = pipe(x,y)
    if not n[0]: break
    visited.append(n[0])
    grid[n[0][1]][n[0][0]] = steps
    x,y,g = b
    n[1] = pipe(x,y)
    if not n[1]: break
    visited.append(n[1])
    grid[n[1][1]][n[1][0]] = steps

print(len(visited))
print(steps * 2)

newgrid = [['.' for _ in range(3*len(grid[0]))] for _ in range(3*len(grid))]
for x,y,g in visited:
    newgrid[3 * y + 1][3 * x + 1] = '#'
    if g == '-':
        newgrid[3 * y + 1][3 * x + 0] = '#'
        newgrid[3 * y + 1][3 * x + 2] = '#'
    if g == '|':
        newgrid[3 * y + 0][3 * x + 1] = '#'
        newgrid[3 * y + 2][3 * x + 1] = '#'
    if g == 'F':
        newgrid[3 * y + 1][3 * x + 2] = '#'
        newgrid[3 * y + 2][3 * x + 1] = '#'
    if g == '7':
        newgrid[3 * y + 1][3 * x + 0] = '#'
        newgrid[3 * y + 2][3 * x + 1] = '#'
    if g == 'J':
        newgrid[3 * y + 0][3 * x + 1] = '#'
        newgrid[3 * y + 1][3 * x + 0] = '#'
    if g == 'L':
        newgrid[3 * y + 0][3 * x + 1] = '#'
        newgrid[3 * y + 1][3 * x + 2] = '#'

q = []
q.append((0,0))
while q:
    (x,y) = q.pop()
    newgrid[y][x] = "O"
    for x1,y1 in [(x+1, y),(x-1, y),(x, y+1),(x, y-1),]:
        if 0 <= y1 < len(newgrid) and 0 <= x1 < len(newgrid[0]) and newgrid[y1][x1] == '.':
            q.append((x1,y1))

s = 0
for y in range(0, len(newgrid), 3):
    for x in range(0, len(newgrid[y]), 3):
        if newgrid[y+1][x+1] == '.':
            newgrid[y+1][x+1] = '+'
            s += 1
print(s)

from PIL import Image
image = Image.new('RGB', (len(newgrid[0]), len(newgrid)))
image.putdata([{'O': (9, 38, 53), '#': (92, 131, 116), '.': (27, 66, 66), '+': (158, 200, 185)}[newgrid[y][x]] for y in range(len(newgrid)) for x in range(len(newgrid[0]))])
image = image.resize((2*len(newgrid[0]), 2*len(newgrid)), Image.Resampling.NEAREST)
image.save("2023.10.png")
