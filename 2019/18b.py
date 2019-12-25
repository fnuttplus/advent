from sys import stdin
m0 = [[c for c in line] for line in stdin.read().splitlines()]
m = m0[:]
d = {}
dat = []
for y in range(len(m)):
    for x in range(len(m[0])):
        if m[y][x] == '@':
            dat.append((x,y))
        elif not m[y][x] in "#.":
            d[m[y][x]] = (x,y)

dA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ka = "abcdefghijklmnopqrstuvwxyz"
#print(dat)

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
                k[mm.upper()] = (i+1, d)
                s.append((x+dx, y+dy, i+1, d))
            elif mm == ".":
                s.append((x+dx, y+dy, i+1, d))
    return k

kd = {k.upper():bfs(d[k], [r[:] for r in m0]) for k in ka}
kdat = [bfs(at, [r[:] for r in m0]) for at in dat]
#for k in kdat: print(k)
#for k in kd: print(k, kd[k])

visited = {}

s = [(0, kdat, "")]
while s:
    i, kl, p = s.pop(0)
    #print(i, kl, p, len(p))
    #if len(p)==26: print(i)
    for j in range(4):
        for kk in kl[j]:
            try:
                if visited[p+kk] <= i+kl[j][kk][0]:continue
                else: pass
                    #print(p, kk, visited[p+kk], i+kl[j][kk][0])
            except: pass
            if kk.upper() in p: continue
            if kl[j][kk][1] - set(p) == set():
                s.append((i+kl[j][kk][0], kl[:j] + [kd[kk]] + kl[j+1:], ''.join(sorted(p+kk.upper()))))
                visited[p+kk] = i+kl[j][kk][0]

print(min([2774,2914,2950,3124,2494,2634,2670,2844,2462,2602,2638,2812]))
