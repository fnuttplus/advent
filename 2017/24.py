from sys import stdin

cs = [tuple(map(int, l.split('/'))) for l in stdin.read().splitlines()]
print(cs)

def find(i, cs):
    for ci in range(len(cs)):
        a, b = cs[ci]
        if   a is i: yield ci, b
        elif b is i: yield ci, a

def dfs(i, cs):
    l = [dfs(n, cs[:ci]+cs[ci+1:]) for ci, n in find(i, cs)]
    if not l: return i
    return i+i + max(l)

def dfs2(i, cs):
    ml = []
    mll = 0
    for ci, n in find(i, cs):
        d = dfs2(n, cs[:ci]+cs[ci+1:])
        ll = len(d)
        if ll > mll:
            mll = ll
            ml = d
        elif ll == mll:
            if sum(d) > sum(ml):
                ml = d
    if not ml: return [i]
    return [i]+[i] + ml


d2 = dfs2(0, cs)
print(sum(d2), len(d2)-1)
print(dfs(0, cs))
