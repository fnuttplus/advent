from sys import stdin
from re import findall
from aoc import Grid

g = Grid().from_stdin()

def move(x,y,dx,dy):
    x0 = x
    y0 = y
    while g.fit(x+dx, y+dy) and g[x+dx, y+dy] == '.':
        y += dy
        x += dx
    g[x, y], g[x0, y0] = g[x0, y0], g[x, y]

from PIL import Image
image = Image.new('RGB', (g.x(), g.y()))

def save_image(i):
    global image
    image.putdata(g.image_data({'.': (9, 38, 53), '#': (92, 131, 116), 'O': (27, 66, 66), '+': (158, 200, 185)}))
    image2 = image.resize((8*g.x(), 8*g.y()), Image.Resampling.NEAREST)
    image2.save(f"frames/2023.14.{i}.png")
save_image(0)

def simp_cycle(n, start, new):
    return (n - start) % (new - start) + (start - 1)

memo={}
memos={}
def cycle(i):
    for x, y in g.xy_rd():
        if g[x, y] == 'O': move(x,y,0,-1)
    save_image(i +1)
    for x, y in g.xy_dr():
        if g[x, y] == 'O': move(x,y,-1,0)
#    save_image(i*4 +2)
    for x, y in g.xy_ru():
        if g[x, y] == 'O': move(x,y,0,1)
#    save_image(i*4 +3)
    for x, y in g.xy_dl():
        if g[x, y] == 'O': move(x,y,1,0)
#    save_image(i*4 +1)

    s = 0
    for x,y in g.xy():
        if g[x, y] == 'O':
            s += g.y() - y

    print(i, s)
    memos[i] = s

    if str(g) in memo:
        print('memo', memo[str(g)], memos[memo[str(g)]])
        print(memos[simp_cycle(1000000000, memo[str(g)], i)])
        exit()
    else:
        memo[str(g)] = i

for i in range(1000000000):
    cycle(i)

