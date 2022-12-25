from sys import stdin
from aocd import submit, get_data, lines
from PIL import Image

ll = stdin.read().splitlines()
ll = get_data(day=16).splitlines()

valves = {}
for l in ll:
    s = l.split(' ')
    valves[s[1]] = (int(s[4][5:-1]), [x.replace(',','') for x in s[9:]])

"""
v = 'AA'
o = set()
mx = 0
memo = set()
def bfs(v, p, t, m, o, path):
    if (v, p, t, m) in memo: return
    memo.add((v, p, t, m))
    global mx
    if m >= 30:
        if m == 31:
            t -= p
        if t > mx:
            mx = t
            print(v,p,t,m,path)
        return
    for n in valves[v][1]:
        bfs(n, p, t+p, m+1,o,path+[n])
    if not(v in o or valves[v][0] == 0):
        t += p
        p += valves[v][0]
        for n in valves[v][1]:
            bfs(n, p, t+p, m+2, o|{v}, path+[0, n])
memo = set()
#memo = {}

def rec(v, t, s):
    for n in valves[v][1]:
        if t != n and ((not t in valves[n][2]) or valves[n][2][t][1] > s):
            valves[n][2][t] = (v, s)
            rec(n, t, s+1)

for v in valves:
    if valves[v][0] == 0: continue
    rec(v,v,1)

print(valves)
#exit()

def bfs(v, e, p, t, m, o, path):
    #if (v, e, p) in memo:
    #    if memo[(v, e, p)] <= m:
    #        return
    #memo[(v, e, p)] = m
    if (v, e, p, t, m) in memo: return
    memo.add((v, e, p, t, m))
    global mx
    if m >= 26:
        if t > mx:
            mx = t
            print(v,e,p,t,m,path)
        return
    for n1 in set([valves[v][2][x][0] for x in set(valves[v][2])-o]):
        for n2 in set([valves[e][2][y][0] for y in set(valves[e][2])-o]):
            if not(v in o or valves[v][0] == 0) and not(e == v or e in o or valves[e][0] == 0):
                bfs(v, e, p+valves[v][0]+valves[e][0], t+p, m+1, o|{v,e}, path+['E'+e+'V'+v])
            if not(v in o or valves[v][0] == 0):
                bfs(v, n2, p+valves[v][0], t+p, m+1, o|{v}, path+['V'+v+'e'+n2])
            if not(e == v or e in o or valves[e][0] == 0):
                bfs(n1, e, p+valves[e][0], t+p, m+1, o|{e}, path+['v'+n1+'E'+e])
            bfs(n1, n2, p, t+p, m+1,o,path+['v'+n1+'e'+n2])

v = 'AA'
o = set()
mx = 0
memo = set()
print(set(valves[v][2]))
bfs(v, v, 0, 0, 0,set(), [])
print(mx)
"""
g = {}

def rec(v0, v, s, vis):
    global g
    for n in valves[v][1]:
        if n in vis: continue
        if valves[n][0] > 0:
            if not n in g[v0][1] or g[v0][1][n] > s+1:
                g[v0][1][n] = s+1
        rec(v0, n, s+1, vis|{n})

for v in valves:
    if v != 'AA' and valves[v][0] == 0: continue
    g[v] = (valves[v][0], {})
    rec(v,v,1,{v})

print(valves)
print(g)
print(len(g))

mx = 0
memo = set()
"""
def dfs(v, p, t, m, vis, path):
    if (v, p, t, m) in memo: return
    memo.add((v, p, t, m))
    global mx
    if m >= 30:
        t -= (m-30)*p
        if t > mx:
            mx = t
            print(v,p,t,m,vis,path)
        return
    if set(g[v][1]) - vis == set():
        t += (30-m)*p
        if t > mx:
            mx = t
            print(v,p,t,m,vis,path)
        return
    for n in set(g[v][1]):
        if n in vis: continue
        dfs(n, p+g[n][0], t+p*g[v][1][n], m+g[v][1][n], vis|{n}, path+str(m)+n+','+str(p)+'|')
v = 'AA'
dfs(v, 0, 0, 0, set(), '')
"""
def dfs(v, v2, vm, p, t, m, vis, path):
    #if (v, v2, vm, p, t, m) in memo: return
    #memo.add((v, v2, vm, p, t, m))
    #print('A', v, v2, vm, p, t, m, vis, path)
    global mx
    if m >= 26:
        if vm == 0:
            p -= (g[v][0] + g[v2][0])
        else:
            p -= g[v][0]
        t -= (m-26)*p
        if t > mx:
            mx = t
            print(v,p,t,m,vis,path)
        #exit()
        return
    ns = set(g[v][1]) - vis
    #print(ns)
    if ns == set():
        if vm > 0:
            m += vm
            t += p*vm
            p += g[v2][0]
        t += (26-m)*p
        #print(t)
        if t > mx:
            mx = t
            print(v,p,t,m,vis,path)
        #exit()
        return
    if vm == 0:
        for n1 in ns:
            for n2 in (set(g[v2][1])-vis)-{n1}:
                if g[v][1][n1] < g[v2][1][n2]: continue
                if g[v][1][n1] == g[v2][1][n2]:
                    dfs(n1, n2, 0, p+g[n1][0]+g[n2][0], t+p*g[v][1][n1], m+g[v][1][n1], vis|{n1,n2}, f'{path},{str(m)},{n1},{n2},{str(p)}|')
                else:
                    dfs(n2, n1, g[v][1][n1] - g[v2][1][n2], p+g[n2][0], t+p*g[v2][1][n2], m+g[v2][1][n2], vis|{n1,n2}, f'{path},{str(m)},{n2},{str(p)}|')
    else:
        for n in ns:
            #print(n, vm, g[v][1][n], v, ns, g[v][1])
            if vm < g[v][1][n]:
                dfs(v2, n, g[v][1][n] - vm, p+g[v2][0], t+p*vm, m+vm, vis|{n,v2}, f'{path},{str(m)},{v2},{str(p)}|')
            elif vm > g[v][1][n]:
                dfs(n, v2, vm - g[v][1][n], p+g[n][0], t+p*g[v][1][n], m+g[v][1][n], vis|{n,v2}, f'{path},{str(m)},{n},{str(p)}|')
            else:
                dfs(v2, n, 0, p+g[n][0]+g[v2][0], t+p*g[v][1][n], m+g[v][1][n], vis|{n,v2}, f'{path},{str(m)},{n},{v2},{str(p)}|')

v = 'AA'
dfs(v, v, 0, 0, 0, 0, set(), '')
#UN 175 2323 30 {'JI', 'XM', 'HX', 'LC', 'BX', 'OH', 'CQ', 'IR', 'GR', 'GB', 'OK', 'UN', 'HF', 'GV'} ,0,OK,GR,0|,4,HF,JI,20|,7,CQ,XM,46|,10,OH,79|,13,GV,98|,14,BX,122|,16,HX,140|,18,IR,150|,21,GB,163|,23,UN,170|
