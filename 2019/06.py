from sys import stdin

m = stdin.read().splitlines()

g = {}
for l in m:
    a, b = l.split(")")
    if a in g:
        g[a].append(b)
    else:
        g[a] = [b]


def dfs(p, i):
    if not p in g:
        return i
    return i + sum([dfs(pp, i+1) for pp in g[p]])

print(dfs("COM", 0))


g = {}
for l in m:
    a, b = l.split(")")
    if a in g:
        g[a].append(b)
    else:
        g[a] = [b]
    if b in g:
        g[b].append(a)
    else:
        g[b] = [a]

v = set()
def dfs2(p, i):
    v.add(p)
    if p == "SAN":
        return i-2
    return sum([dfs2(pp, i+1) if pp not in v else 0 for pp in g[p]])

print(dfs2("YOU", 0))
