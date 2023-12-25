from aoc import Grid

g = Grid().from_stdin()
pipes = {
    '|': (( 0, -1), ( 0, 1)),
    '-': ((-1,  0), ( 1, 0)),
    '7': ((-1,  0), ( 0, 1)),
    'J': (( 0, -1), (-1, 0)),
    'L': (( 0, -1), ( 1, 0)),
    'F': (( 0,  1), ( 1, 0)),
}
def pipe(x, y, p):
    if p in pipes:
        for dx, dy in pipes[p]:
            if g.fit(x+dx, y+dy) and g[x+dx,y+dy] in pipes:
                return x+dx, y+dy, g[x+dx,y+dy]
    return False

sx, sy = g.find('S')
visited = [(sx,sy,'7')]
g[sx, sy] = '#'
for x, y, ps in [(sx-1, sy, '-FL'), (sx+1, sy, '-J7'), (sx, sy-1, '|F7'), (sx, sy+1, '|JL')]:
    if g[x, y] in ps: n = (x, y, g[x, y])

while n:
    visited.append(n)
    g[n[0], n[1]] = '#'
    n = pipe(*n)
print(len(visited) // 2)

g = Grid([['.' for _ in range(3*g.x())] for _ in range(3*g.y())])
for x,y,p in visited:
    g[3*x+1, 3*y+1] = '#'
    if p in '-7J': g[3*x+0, 3*y+1] = '#'
    if p in '-FL': g[3*x+2, 3*y+1] = '#'
    if p in '|JL': g[3*x+1, 3*y+0] = '#'
    if p in '|F7': g[3*x+1, 3*y+2] = '#'
g.flood_fill(0, 0, '.', 'O')

print(sum([1 for y in range(1, g.y(), 3) for x in range(1, g.x(), 3) if g[x, y] == '.']))
"""
for y in range(1, g.y(), 3):
    for x in range(1, g.x(), 3):
        if g[x, y] == '.': g[x, y] = '+'
from PIL import Image
image = Image.new('RGB', (g.x(), g.y()))
image.putdata(g.image_data({'O': (9, 38, 53), '#': (92, 131, 116), '.': (27, 66, 66), '+': (158, 200, 185)}))
image = image.resize((2*g.x(), 2*g.y()), Image.Resampling.NEAREST)
image.save("2023.10.png")
"""