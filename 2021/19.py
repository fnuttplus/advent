from sys import stdin
from itertools import combinations, product

lines = stdin.read().split('\n\n')

def beacons(sc):
    return [tuple(map(int, x.split(','))) for x in sc.split('\n')[1:]]

def move(bc, bc0):
    return tuple([bc[i] - bc0[i] for i in range(len(bc0))])

def neg(bc):
    yield (bc[0], bc[1], bc[2])
    yield (-bc[0], bc[1], bc[2])
    yield (bc[0], -bc[1], bc[2])
    yield (bc[0], bc[1], -bc[2])
    yield (-bc[0], -bc[1], bc[2])
    yield (bc[0], -bc[1], -bc[2])
    yield (-bc[0], bc[1], -bc[2])
    yield (-bc[0], -bc[1], -bc[2])

def rotate(bc):
    for n in neg([bc[0], bc[1], bc[2]]): yield n
    for n in neg([bc[0], bc[2], bc[1]]): yield n
    for n in neg([bc[1], bc[0], bc[2]]): yield n
    for n in neg([bc[1], bc[2], bc[0]]): yield n
    for n in neg([bc[2], bc[1], bc[0]]): yield n
    for n in neg([bc[2], bc[0], bc[1]]): yield n

def find(sc0, sc1):
    global scanners
    for ba, bb in product(sc0, sc1):
        for i in range(48):
            c = len(sc0[ba][0] & sc1[bb][i])
            if c >= 12:
                return move(ba, list(rotate(bb))[i]), [move(x, [-y for y in ba]) for x in sc1[bb][i]]

def scanner(b):
    sc = {}
    for bb in b:
        sc[bb] = []
        r = [list(rotate(bc)) for bc in [move(x, bb) for x in b]]
        for i in range(48):
            sc[bb].append(set([rr[i] for rr in r]))
    return sc

scanners = []
for i in range(len(lines)):
    b = beacons(lines[i])
    scanners.append(scanner(b))

visited = [0]
nodes = [0]
sp = {}
bs = set(scanners[0].keys())
while nodes:
    n0 = nodes.pop()
    for n in range(len(scanners)):
        if n in visited: continue
        f = find(scanners[n0], scanners[n])
        if not f: continue
        a,b = f
        scanners[n] = scanner(b)
        bs = bs | set(b)
        sp[n] = a
        nodes.append(n)
        visited.append(n)
        print(n, a)

"""
print("\n -- Scanners --")
for s in sorted(sp.keys()):
    print(f'vec3({sp[s][0]}., {sp[s][1]}., {sp[s][2]}.),')
print("\n -- Beacons --")
for b in bs:
    print(f'vec3({b[0]}., {b[1]}., {b[2]}.),')
"""
print(len(bs))

md = 0
for a,b in combinations(sp,2):
    d = sum([abs(sp[a][i] - sp[b][i]) for i in range(3)])
    if md < d: md = d
print(md)
