from sys import stdin
from aocd import submit, get_data, lines
from PIL import Image
from queue import PriorityQueue

#ll = stdin.read().splitlines()
ll = get_data(day=24).splitlines()

g = [list(l) for l in ll]
bliz = []
for y,row in enumerate(g):
    for x,c in enumerate(row):
        if y == 0 and c == '.':
            ex,ey = x,y
        if y == len(g)-1 and c == '.':
            gx,gy = x,y
        if c in ['^','v','<','>']:
            bliz.append((x,y,c))
print(len(bliz))
print(ex,ey)
print(gx,gy)

bmemo = {}
def blizz(m):
    if m in bmemo: return bmemo[m]
    b = {}
    for x,y,c in bliz:
        x-=1
        y-=1
        if c == '^': y = ((y-m)%(gy-1))
        if c == 'v': y = ((y+m)%(gy-1))
        if c == '<': x = ((x-m)%(gx))
        if c == '>': x = ((x+m)%(gx))
        x+=1
        y+=1
        if (x,y) in b: b[(x,y)] += 1
        else: b[(x,y)] = 1
    bmemo[m] = b
    return b

"""
for n in range(18,32):
    b = blizz(n)
    for y in range(gy+1):
        for x in range(gx+2):
            if (x,y) in b:
                print(b[(x,y)], end='')
            else:
                print('.', end='')
        print()
    print()
"""
#print(bmemo)

pq = PriorityQueue()
#"""
pq.put((gx-ex+gy-ey, (ex,ey,499,[])))
vis = {(ex,ey,499)}
#pq.put((gx-ex+gy-ey, (ex,ey,0,[])))
#vis = {(ex,ey,0)}
mm = 3200
while not pq.empty():
    _,(x,y,m,p) = pq.get()
    if m+(gx-x)+(gy-y) > mm: continue
    b = blizz(m+1)
    vis.add((x,y,m))
    for dx,dy in [(0,-1), (0,1), (-1,0), (1,0)]:
        if (x+dx, y+dy) == (gx,gy):
            if m+1 < mm:
                mm = m+1
                print(mm, p)
            continue
        if not (1 <= x+dx <= gx and 1 <= y+dy < gy): continue
        if (x+dx, y+dy, m+1) in vis: continue
        if (x+dx, y+dy) in b: continue
        pq.put((gx-(x+dx)+gy-(y+dy), (x+dx,y+dy,m+1,p+[(x+dx,y+dy)])))
    if not (x,y) in b:
        pq.put((gx-(x)+gy-(y), (x,y,m+1,p+[(x,y)])))
#"""
#exit()
pq.put((gx+gy, (gx,gy,260,[])))
vis = {(gx,gy,260)}
mm = 3200
while not pq.empty():
    _,(x,y,m,p) = pq.get()
    if m+x+y > mm: continue
    b = blizz(m+1)
    vis.add((x,y,m))
    for dx,dy in [(0,-1), (0,1), (-1,0), (1,0)]:
        if (x+dx, y+dy) == (ex,ey):
            if m+1 < mm:
                mm = m+1
                print(mm,p)
            continue
        if not (1 <= x+dx <= gx and 1 <= y+dy < gy): continue
        if (x+dx, y+dy, m+1) in vis: continue
        if (x+dx, y+dy) in b: continue
        pq.put((x+dx+y+dy, (x+dx,y+dy,m+1,p+[(x+dx,y+dy)])))
    if not (x,y) in b:
        pq.put((x+y, (x,y,m+1,p+[(x,y)])))
