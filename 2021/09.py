from sys import stdin
#from aocd import lines, submit
from aoc import grid

lines = stdin.read().splitlines()

g = grid([[int(x) for x in list(line)] for line in lines])

c = 0
b = []
for x,y,n in g.points():
    for x1,y1,n1 in g.neighbors(x,y):
        if n >= n1: break
    else:
        c += 1 + n
        b.append((x,y))

def flood(x,y,v):
    v.append((x,y))
    for x1,y1,n1 in g.neighbors(x,y):
        if not (x1,y1) in v:
            if 9 > n1 > g.get(x,y):
                flood(x1,y1,v)
    return v

cc = []
i = 0
ss = []
for x,y in b:
    s = flood(x,y,[])
    ss.append(s)
    #print(s)
    #print(len(s))
    cc.append(len(s))

m = 1
for c in sorted(cc,reverse=True)[:3]:
    m*=c
#print(len(b))
print(m)


from PIL import Image
image = Image.new('RGB', (len(g.data), len(g.data[0])))
image.putdata(g.imageData())

#image2 = Image.new('RGB', (10, 2))
#image2.putdata([(x*20, x*20, x*20) if y == 0 else (x*20, x*20, x*20+70) for y in range(2) for x in range(10)])
#image2.save("colors.png")

#print(len(g),len(g[0]))
for s in sorted(ss, key=len, reverse=True)[:3]:
    for x1,y1 in s:
        image.putpixel((y1,x1),(g.get(x1,y1)*20, g.get(x1,y1)*20, g.get(x1,y1)*20+70))
image = image.resize((1000,1000),Image.NEAREST)
image.save("09.png")
