from sys import stdin
from aocd import submit, get_data, lines
from PIL import Image

ll = stdin.read().splitlines()
ll = get_data(day=15).splitlines()

m = 0
sensors = []

def dist(a,b,c,d):
    return abs(a-c) + abs(b-d)

for l in ll:
    s = l.split(' ')
    a,b,c,d = map(int, [s[2][2:-1], s[3][2:-1], s[8][2:-1], s[9][2:], ])
    sensors.append((a,b,dist(a,b,c,d)))

"""
minx = min([s[0] for s in sensors] + [s[2] for s in sensors])
maxx = max([s[0] for s in sensors] + [s[2] for s in sensors])


print(minx, maxx)
y = 10
y = 2000000
x = set()
for a,b,c,d in sensors:
    miny = b - dist(a,b,c,d)
    maxy = b + dist(a,b,c,d)
    if miny <= y <= b:
        minx = a-(y-miny)
        maxx = a+(y-miny)
        for t in range(minx, maxx+1):
            x.add(t)

    if b <= y <= maxy:
        minx = a-(maxy-y)
        maxx = a+(maxy-y)
        for t in range(minx, maxx+1):
            x.add(t)

    #print(a,b,c,d)
    #print(minx, maxx)

for a,b,c,d in sensors:
    if d == y and c in x: x.remove(c)
#print(x)
print(len(x))
#submit(len(x))
"""

n = 4000000
for y in range(n+1):
    x = 0
    while x <= n:
        for a,b,d in sensors:
            miny = b - d
            maxy = b + d
            if miny <= y <= b:
                minx = a-(y-miny)
                maxx = a+(y-miny)
                if minx <= x <= maxx:
                    x = maxx+1
                    break

            if b <= y <= maxy:
                minx = a-(maxy-y)
                maxx = a+(maxy-y)
                if minx <= x <= maxx:
                    x = maxx+1
                    break
        else:
            print('found', x,y)
            print(x * 4000000 + y)
            exit()
    if y%100000 == 0:
        print(y)
