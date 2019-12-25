from sys import stdin
m = [[c for c in line] for line in stdin.read().splitlines()]
p={}

def portals(y, dy1, dy2):
    for x in range(len(m[y])):
        if not m[y][x] in "#. ":
            c = m[y][x] + m[y+dy1][x]
            m[y+dy2][x] = "@"
            if c in p:
                p[c].append((x,y+dy2))
            else:
                p[c] = [(x,y+dy2)]
def portals2(x, dx1, dx2):
    for y in range(len(m)):
        if not m[y][x] in "#. ":
            c = m[y][x] + m[y][x+dx1]
            m[y][x+dx2] = "@"
            if c in p:
                p[c].append((x+dx2,y))
            else:
                p[c] = [(x+dx2,y)]
portals(0, 1, 2)
portals(117, 1, -1)
portals2(0, 1, 2)
portals2(117, 1, -1)
portals(86, 1, 2)
portals(31, 1, -1)
portals2(86, 1, 2)
portals2(31, 1, -1)

ml = [[mm[:] for mm in m]]

def teleport(d, l):
    for pp in p:
        if len(p[pp]) == 1: continue
        if p[pp][0] == d:
            return p[pp][1] + (l-1,)
        elif p[pp][1] == d:
            if l+1 == len(ml): ml.append([mm[:] for mm in m])
            return p[pp][0] + (l+1,)
    return 0,0,-1

def bfs(d, g):
    x,y = d
    s = [(x,y,0,0)]
    ml[0][y][x] = "#"
    dd = ((0,-1),(0,1),(-1,0),(1,0))
    while s:
        x,y,l,i = s.pop(0)
        if (x,y) == g and l == 0: return i
        if ml[l][y][x] == "@":
            ml[l][y][x] = "#"
            x,y,l = teleport((x,y), l)
            if l >= 0:
                ml[l][y][x] = "#"
                s.append((x, y, l, i+1))
            continue
        for dx,dy in dd:
            mm = ml[l][y+dy][x+dx]
            if mm in '.@':
                if mm == ".": ml[l][y+dy][x+dx] = "#"
                s.append((x+dx, y+dy, l, i+1))
    return i

print(bfs(p['AA'][0],p['ZZ'][0]))
