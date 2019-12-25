from sys import stdin
from PIL import Image

m = [list(r) for r in stdin.read().splitlines()]
bugs = set()
for y in range(len(m)):
    for x in range(len(m[0])):
        if m[y][x] == "#":
            bugs.add((x,y,0))
#print(bugs)

def draw(i):
    n = 5**4
    image = Image.new('1', (n, n))
    image.putdata([1 if (x//(n//5),y//(n//5),-1) in bugs else 0 for y in range(n) for x in range(n)])
    n //= 5
    image1 = Image.new('1', (n, n))
    image1.putdata([1 if (x//25,y//25,0) in bugs else 0 for y in range(n) for x in range(n)])
    image.paste(image1, (250,250))
    n //= 5
    image1 = Image.new('1', (n, n))
    image1.putdata([1 if (x//5,y//5,1) in bugs else 0 for y in range(n) for x in range(n)])
    image.paste(image1, (300,300))
    n //= 5
    image1 = Image.new('1', (n, n))
    image1.putdata([1 if (x,y,2) in bugs else 0 for y in range(n) for x in range(n)])
    image.paste(image1, (310,310))
    image = image.resize((1250,1250), Image.NEAREST)
    image.save("frames/advent24_"+str(i)+".png")

d = [(-1,0),(1,0),(0,-1),(0,1),]
def dxdy(x,y,l):
    if x == 2 and y == 3:
        for dx in range(5): yield dx,4,l+1
    elif x == 2 and y == 1:
        for dx in range(5): yield dx,0,l+1
    elif x == 3 and y == 2:
        for dy in range(5): yield 4,dy,l+1
    elif x == 1 and y == 2:
        for dy in range(5): yield 0,dy,l+1

    for dx, dy in d:
        if x+dx == 2 and y+dy == 2: continue
        elif x+dx > 4: yield 3,2,l-1
        elif x+dx < 0: yield 1,2,l-1
        elif y+dy > 4: yield 2,3,l-1
        elif y+dy < 0: yield 2,1,l-1
        else: yield x+dx,y+dy,l

draw(0)
for j in range(1,201):
    infest = []
    die = []
    for x,y,l in bugs:
        i = 0
        for x0,y0,l0 in dxdy(x,y,l):
            if (x0,y0,l0) in bugs:
                i += 1
                continue
            n = 0
            for x1,y1,l1 in dxdy(x0,y0,l0):
                if (x1,y1,l1) in bugs:
                    n += 1
                if n > 2: break
            if n == 1 or n == 2:
                infest.append((x0,y0,l0))
        if i != 1:
            die.append((x,y,l))

    for b in die: bugs.remove(b)
    for b in infest: bugs.add(b)
    #print(bugs)
    draw(j)

print(len(bugs))
