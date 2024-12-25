from sys import stdin
from aocd import get_data, submit
from re import findall
from itertools import product, combinations
from aoc import Grid, adj
from oklab import viridis

s = 0

r = {}

t = True
t = False

ls = stdin.read() if t else get_data()
ls = [list(x) for x in ls.split('\n')]
g = Grid(ls)
gc = [[0 for x in range(g.x())] for y in range(g.y())]
ccn = {}
ml = 0
for x0,y0 in g.xy():
    c = g[x0,y0]
    if c == 0: continue
    q = [(x0, y0)]
    n = set()
    p = 0
    while q:
        (x,y) = q.pop()
        if (x,y) in n: continue
        n.add((x,y))
        for x1,y1 in adj(x,y):
            if g.fit(x1, y1) and g.data[y1][x1] == c:
                q.append((x1,y1))

    cn = {}
    for x,y in sorted(n):
        #north
        nx,ny = x,y-1
        if not g.fit(nx,ny) or g[nx,ny] != c:
            if not (((x-1, y) in cn and 'N' in cn[(x-1, y)]) or ((x+1, y) in cn and 'N' in cn[(x+1, y)])):
                p += 1
            if (x,y) in cn:
                cn[(x,y)].add('N')
            else:
                cn[(x,y)] = set(['N'])
        #south
        nx,ny = x,y+1
        if not g.fit(nx,ny) or g[nx,ny] != c:
            if not (((x-1, y) in cn and 'S' in cn[(x-1, y)]) or ((x+1, y) in cn and 'S' in cn[(x+1, y)])):
                p += 1
            if (x,y) in cn:
                cn[(x,y)].add('S')
            else:
                cn[(x,y)] = set(['S'])
        #east
        nx,ny = x+1,y
        if not g.fit(nx,ny) or g[nx,ny] != c:
            if not (((x, y-1) in cn and 'E' in cn[(x, y-1)]) or ((x, y+1) in cn and 'E' in cn[(x, y+1)])):
                p += 1
            if (x,y) in cn:
                cn[(x,y)].add('E')
            else:
                cn[(x,y)] = set(['E'])
        #west
        nx,ny = x-1,y
        if not g.fit(nx,ny) or g[nx,ny] != c:
            if not (((x, y-1) in cn and 'W' in cn[(x, y-1)]) or ((x, y+1) in cn and 'W' in cn[(x, y+1)])):
                p += 1
            if (x,y) in cn:
                cn[(x,y)].add('W')
            else:
                cn[(x,y)] = set(['W'])

    for pp in cn:
        if pp in ccn:
            print('this happens?')
        else:
            ccn[pp] = cn[pp]

    for x,y in n:
        g[x,y] = 0
        gc[y][x] = len(n)

    if len(n) > ml: ml = len(n)
    s += len(n) * p
    print(c, len(n), p)

print(ml)
from PIL import Image
b = 10
image = Image.new('RGB', (g.x() *b +1, g.y() *b +1))
v = viridis(255)
for x,y in g.xy():
    for yy in range(1,b+1):
        for xx in range(1,b+1):
            image.putpixel ((x*b+xx, b*y+yy), tuple(v[254 if gc[y][x] > 254 else gc[y][x]]))
    if (x,y) in ccn:
        #print(gc[y][x], gc[y][x])
        c = ccn[(x,y)]
        #if 'N' in c:
            #for xx in range(5): image.putpixel ((x * 5 + xx, 5*y), (255, 255, 255))
            #image.putpixel ((x * 5, 5*y+1), (255, 255, 255))
            #image.putpixel ((x * 5+4, 5*y+1), (255, 255, 255))
        if 'S' in c:
            for xx in range(b): image.putpixel ((x * b + xx +1, b*y+b), (0, 0, 0))
            #image.putpixel ((x * 5, 5*y+3), (0, 0, 0))
            #image.putpixel ((x * 5+4, 5*y+3), (0, 0, 0))
        if 'E' in c:
            for yy in range(b): image.putpixel ((x * b + b, b*y+yy +1), (0, 0, 0))
            #image.putpixel ((x * 5+3, 5*y), (0, 0, 0))
            #image.putpixel ((x * 5+3, 5*y+4), (0, 0, 0))
        #if 'W' in c:
            #for yy in range(5): image.putpixel ((x * 5, 5*y+yy), (0, 0, 0))
            #image.putpixel ((x * 5+1, 5*y), (0, 0, 0))
            #image.putpixel ((x * 5+1, 5*y+4), (0, 0, 0))
        if 'N' in c and 'W' in c:
            image.putpixel ((x * b, b*y), (0, 0, 0))
image.save("2024-12.png")
