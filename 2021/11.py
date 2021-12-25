from sys import stdin
#from aocd import lines, submit
from aoc import grid

lines = stdin.read().splitlines()

g = grid([[int(x) for x in list(line)] for line in lines])
print(g)
def flashes(l, v):
    f = []
    for x,y in l:
        v.append((x,y))
        for x1,y1,n1 in g.neighbors2(x,y):
            if (x1,y1) in v+l+f: continue
            n1 += 1
            g.set(x1,y1,n1)
            if n1 > 9:
                f.append((x1,y1))
    if len(f) > 0:
        return flashes(f,v)
    return v
i = 0

from PIL import Image

for step in range(100000):
    f = []
    c = 0
    for x,y,n in g.points():
        n += 1
        g.set(x,y,n)
        if n > 9:
            f.append((x,y))
    
    if f:
        f = flashes(f,[])
        if len(f) == 100: break
        for x,y in f:
            i += 1
            g.set(x,y,0)

"""
    image = Image.new('RGB', (10, 10))
    image.putdata(g.imageData())
    image = image.resize((1000,1000),Image.NEAREST)
    image.save("frames/11_"+str(step)+".png")

image = Image.new('RGB', (10, 10))
image.putdata(g.imageData())
image = image.resize((1000,1000),Image.NEAREST)
image.save("frames/11_"+str(step)+".png")
image = Image.new('RGB', (1000, 1000))
image.save("frames/11_"+str(step+1)+".png")
"""
print(step + 1)
