from sys import stdin
m0 = [[c for c in line] for line in stdin.read().splitlines()]
m = m0[:]
d = {}
for y in range(len(m)):
    for x in range(len(m[0])):
        if not m[y][x] in "#.":
            d[m[y][x]] = (x,y)

dA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ka = "abcdefghijklmnopqrstuvwxyz"

def bfs(d, m):
    x,y = d
    s = [(x,y,0,set())]
    m[y][x] = "#"
    dd = ((0,-1),(0,1),(-1,0),(1,0))
    k = {}
    while s:
        x,y,i,d = s.pop(0)
        for dx,dy in dd:
            mm = m[y+dy][x+dx]
            m[y+dy][x+dx] = "#"
            if mm in dA:
                s.append((x+dx, y+dy, i+1, d|{mm}))
            elif mm in ka:
                k[mm] = (i+1, d)
                s.append((x+dx, y+dy, i+1, d))
            elif mm == ".":
                s.append((x+dx, y+dy, i+1, d))
    return k

kd = {k:bfs(d[k], [r[:] for r in m0]) for k in '@'+ka}
#for k in kd: print(k, kd[k])
visited = {}
def bfs2(k):
    s = [(0, k, "")]
    while s:
        i, k, p = s.pop(0)
        print(i, p, len(p))
        if len(p)==26:yield i
        for kk in k:
            try:
                if visited[''.join(sorted(p))+kk] <= i+k[kk][0]:continue
            except: pass
            if kk.upper() in p: continue
            if k[kk][1] - set(p) == set():
                s.append((i+k[kk][0], kd[kk], p+kk.upper()))
                visited[''.join(sorted(p))+kk] = i+k[kk][0]

print(min(list(bfs2(kd['@']))))
#NOJIQDCTKWBUZVYERHFMASLGXP
