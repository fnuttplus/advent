from sys import stdin
from aocd import submit, get_data, lines
from PIL import Image
import cProfile

ll = stdin.read().splitlines()
ll = get_data(day=23).splitlines()

g = [list(l) for l in ll]
cords = []
for y,row in enumerate(g):
    for x,c in enumerate(row):
        if c == '#':
            cords.append((x,y))
#print(cords)
print(len(cords))

def draw(i,minx,maxx,miny,maxy):
    global dii,x,y
    #if dii > 400: return
    image = Image.new('1', (maxx-minx,maxy-miny))
    for x,y in cords:
        image.putpixel((x-minx,y-miny), 1)
    image = image.resize(((maxx-minx)*9,(maxy-miny)*9), Image.Resampling.NEAREST)
    image.save("frames/23_"+str(i)+".png")

d = [(0,-1), (0,1), (-1,0), (1,0)]
#pr = cProfile.Profile()
#pr.enable()

for i in range(1000):
    n = {}
    p = {}
    co = set(cords)
    c = 0
    for x,y in cords:
        if co.isdisjoint(set([(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1),])):
            c += 1
            continue
        for dx,dy in d:
            if dx == 0: ns = set([(x-1,y+dy), (x,y+dy), (x+1,y+dy)])
            if dy == 0: ns = set([(x+dx,y-1), (x+dx,y), (x+dx,y+1)])
            if co.isdisjoint(ns):
                try: n[((x+dx,y+dy))] += 1
                except: n[((x+dx,y+dy))] = 1
                p[(x,y)] = (x+dx,y+dy)
                break
    if c == len(cords):
        print('yo', i+1)
        break
    for j,(x,y) in enumerate(cords):
        if (x,y) in p and n[p[(x,y)]] == 1:
            cords[j] = p[(x,y)]
    d.append(d.pop(0))
    continue
#    print(n)
#    print(cords)
#    print(len(cords))
#   print(p)

    minx = min([x for (x,y) in cords])
    maxx = max([x for x,y in cords])+1
    miny = min([y for x,y in cords])
    maxy = max([y for x,y in cords])+1
    print(minx,maxx,miny,maxy)
#    minx,maxx,miny,maxy = 0,4,0,5
#    c = 0
#    for y in range(miny,maxy):
#        for x in range(minx,maxx):
 #           if not (x,y) in cords: c += 1
#            print('#' if (x,y) in cords else '.', end='')
#        print()
    print(c, i, ((maxx-minx)*(maxy-miny)-len(cords)))
    draw(i, -13,118,-13,121)

#pr.print_stats()
