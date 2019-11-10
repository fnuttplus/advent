from sys import stdin
from copy import deepcopy
from time import sleep

m = []
y = 0
u = []
d = [(-1,0),(0,-1),(0,1),(1,0),]
for line in stdin.read().splitlines():
    x = 0
    for c in line:
        if c in "GE":
            u.append([y,x,'E' if c == 'G' else 'G',200])
        x += 1

    m.append(list(line))
    y += 1

for mm in m:
    print(''.join(mm))
print(u)

def path(e, m):
    y, x, z, _ = e
    i = 0
    s = [(x,y,i,0)]
    Done = False
    while not (Done or s == []):
        x,y,i,h = s.pop(0)
        for dy, dx in d:
            if m[y+dy][x+dx] == z:
                return (x,y) if h is 0 else h
            elif m[y+dy][x+dx] == '.':
                s.append((x+dx,y+dy,i+1,(x,y) if i == 1 else h))
                m[y+dy][x+dx] = str(i+1)
            #print(e, m[y+dy][x+dx])
        #for mm in m: print(''.join(mm))
    return 0

def adj(x, y, z):
    l = []
    for dy, dx in d:
        if m[y+dy][x+dx] == z:
            for e in u:
                if e[3] <= 0: continue
                if e[0] == y+dy and e[1] == x+dx and e[2] != z:
                    l.append((e[3], e[0], e[1], e))
#    print("a", sorted(l))
    return [e[3] for e in sorted(l)][0] if l != [] else None

i = 0
while all(z in [e[2] for e in u if e[3] > 0] for z in "GE"):
    i += 1
    for e in u:
        y, x, z, h = e
        if h <= 0: continue
        p = path(e, deepcopy(m))
        if p != 0:
#            print(p, m[p[1]][p[0]])
            m[y][x] = '.'
            x, y = p
            m[y][x] = 'G' if z == 'E' else 'E'
            e[0] = y
            e[1] = x
        n = adj(x,y,z)
        if n:
            n[3] -= (3 if n[2] == 'G' else 19)
            if n[3] <= 0:
                m[n[0]][n[1]] = '.'
                if n[2] == 'G':
                    print("DEAD")
                    print(i, u)
                    exit()
    u.sort()
    #print(i, u)
    #for mm in m: print(''.join(mm))

h = 0
for e in u:
    if e[3] > 0:
        h += e[3]
print(i-1, h, i*h-h)

"""
for each unit,
    find closest enemy.
        move towards them
    if anemy is cloes
        hp -= 3
"""