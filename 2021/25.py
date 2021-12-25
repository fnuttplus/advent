from sys import stdin
from aoc import grid

lines = stdin.read().splitlines()
g = grid([list(line) for line in lines])

easters = []        
downers = []
for x,y,n in g.points():
    if n == '>':
        easters.append((x,y))
    if n == 'v':
        downers.append((x,y))

easters = []
downers = []
for x,y,n in g.points():
    if n == '>':
        easters.append((x,y))
    if n == 'v':
        downers.append((x,y))

for step in range(10000):
    nomove = False
    movers = []
    for i in range(len(easters)):
        x,y = easters[i]
        if g.get2(x,y+1) == '.':
            movers.append((x,y))
            easters[i] = (x,y+1)
    for x,y in movers:
        g.set2(x,y,'.')
        g.set2(x,y+1,'>')
    if movers == []:
        nomove = True
    movers = []
    for i in range(len(downers)):
        x,y = downers[i]
        if g.get2(x+1,y) == '.':
            movers.append((x,y))
            downers[i] = (x+1,y)
    for x,y in movers:
        g.set2(x,y,'.')
        g.set2(x+1,y,'v')
    if nomove and movers == []:
        break

    #print(step+1)
    #print(g)
print(step+1)
