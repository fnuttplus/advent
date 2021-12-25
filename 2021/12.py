from sys import stdin
#from aocd import lines, submit
lines = stdin.read().splitlines()

d = {}
for line in lines:
    a,b = line.split('-')
    if a in d: d[a].append(b)
    else: d[a] = [b]

    if b in d: d[b].append(a)
    else: d[b] = [a]
#print(d)

ss = set()
def bfs(s, v, dd):
    if s == 'end':
        ss.add(tuple(v))
        return
    for n in d[s]:
        if n.lower() == n:
            if n == dd:
                if v.count(n) > 1: continue
            elif n in v: continue
            bfs(n, v+[n], dd)
        else:
            bfs(n, v+[n], dd)

dd = []
for k in d:
    if k.lower() == k:
        if k != 'end' and k != 'start':
            dd.append(k)
i = 0
for ddd in dd:
    bfs('start', ['start'], ddd)
    
print(len(ss))
