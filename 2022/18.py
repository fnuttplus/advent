from sys import stdin
from aocd import submit, get_data, lines
from PIL import Image

ll = stdin.read().splitlines()
ll = get_data(day=18).splitlines()

s = 0
d = set()
for l in ll:
    x,y,z = map(int, l.split(','))
    d.add((x,y,z))

minx = min([x for x,y,z in d])
maxx = max([x for x,y,z in d]) + 1
miny = min([y for x,y,z in d])
maxy = max([y for x,y,z in d]) + 1
minz = min([z for x,y,z in d])
maxz = max([z for x,y,z in d]) + 1

c = 0
for a in d:
    n = 0
    for b in d:
        s = sum([abs(b[i]-a[i]) for i in range(3)])
        if s == 1: n += 1
    c += 6-n
print(c)

x,y,z = 0,0,0
ns = {(x,y,z)}
while ns:
    t = set()
    for x,y,z in ns:
        d.add((x,y,z))
        #print(x,y,z)
        for dx,dy,dz in [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1),]:
            if minx-1 <= x+dx <= maxx and miny-1 <= y+dy <= maxy and minz-1 <= z+dz <= maxz:
                if not (x+dx, y+dy, z+dz) in d:
                    t.add((x+dx, y+dy, z+dz))
                    #print("B", (x+dx, y+dy, z+dz))
    ns = t
#print(d)
a = set()
for x in range(minx,maxx):
    for y in range(miny,maxy):
        for z in range(minz,maxz):
            if not(x,y,z) in d:
                a.add((x,y,z))

print(len(a))

while a:
    x,y,z = a.pop()
    for dx,dy,dz in [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1),]:
        if (x+dx, y+dy, z+dz) in d:
           c -= 1
print(c)
#print(c)