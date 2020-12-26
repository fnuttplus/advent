from sys import stdin

tiles = set()

def co(c, t):
    x, y, z = t
    if c == 'e':
        x += 1
        y += -1
        z += 0
    if c == 'w':
        x += -1
        y += 1
        z += 0
    if c == 'se':
        x += 0
        y += -1
        z += 1
    if c == 'sw':
        x += -1
        y += 0
        z += 1
    if c == 'ne':
        x += 1
        y += 0
        z += -1
    if c == 'nw':
        x += 0
        y += 1
        z += -1
    return x,y,z

for l in stdin.read().splitlines():
    cc = []
    i = 0
    while i < len(l):
        c = l[i]
        if c == 'e':
            cc.append('e')
        if c == 'w':
            cc.append('w')
        if c == 's':
            if l[i+1] == 'e':
                cc.append('se')
            if l[i+1] == 'w':
                cc.append('sw')
            i += 1
        if c == 'n':
            if l[i+1] == 'w':
                cc.append('nw')
            if l[i+1] == 'e':
                cc.append('ne')
            i += 1
        i += 1
    x,y,z = (0,0,0)
    for c in cc:
        x,y,z = co(c, (x,y,z))
    if (x,y,z) in tiles:
        tiles.remove((x,y,z))
    else:
        tiles.add((x,y,z))

print(len(tiles))
"""
def cube_to_oddr(cube):
    x,y,z = cube
    col = x + (z - (z&1)) // 2
    row = z
    return (col, row)

for t in tiles:
    print(list(cube_to_oddr(t)))
"""

def adji(t):
    n = 0
    for d in ['e', 'w', 'se', 'sw', 'ne', 'nw']:
        x,y,z = co(d, t)
        if not (x,y,z) in tiles:
            yield (x, y, z)

def adj(t):
    n = 0
    for d in ['e', 'w', 'se', 'sw', 'ne', 'nw']:
        x,y,z = co(d, t)
        if (x,y,z) in tiles:
            n += 1
    return n

for x in range(100):
    w = set()
    b = set()
    for t in tiles:
        n = adj(t)
        if n == 0 or n > 2:
            w.add(t)
        for a in adji(t):
            n = adj(a)
            if n == 2:
                b.add(a)

    for aa in w:
        tiles.remove(aa)

    for bb in b:
        tiles.add(bb)

print(len(tiles))
