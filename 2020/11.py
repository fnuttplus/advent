from sys import stdin
from PIL import Image

g = [list(line) for line in stdin.read().splitlines()]

d = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1),]
def adj(x,y):
    global g
    n = 0
    for dy, dx in d:
        for i in range(1, 100):
            if 0 <=y+i*dy < len(g) and 0 <= x+i*dx < len(g[0]):
                if g[y+i*dy][x+i*dx] == '#':
                    n += 1
                    break
                if g[y+i*dy][x+i*dx] == 'L':
                    break
            else: break
    return n
i = 0
while True:
    if False: # animation
        if i % 2 == 0:
            image = Image.new('L', (len(g[0]), len(g)))
            cc = {"#": 150, "L": 100, ".": 0, }
            image.putdata([cc[ggg] for gg in g for ggg in gg])
            image = image.resize((1000,1000), Image.NEAREST)
            image.save("frames/advent_" + str(i//2) + ".png")
        i += 1

    acc = set()
    emp = set()
    for y in range(len(g)):
        for x in range(len(g[y])):
            if g[y][x] == 'L' and adj(x, y) == 0:
                acc.add((x,y))
            elif g[y][x] == '#' and adj(x, y) >= 5:
                emp.add((x,y))

    if acc == set() and emp == set(): break

    for x, y in acc: g[y][x] = '#'
    for x, y in emp: g[y][x] = 'L'
#for gg in g: print(''.join(gg))
print(sum([gg.count('#') for gg in g]))
