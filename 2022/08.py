from sys import stdin
from aocd import submit, get_data, lines

d = {}
s = get_data(day=8).splitlines()
#s = stdin.read().splitlines()
g = [list(map(int, ss)) for ss in list(s)]

l = []
for x in range(1, len(g)-1):
    for y in range(1, len(g[x])-1):
        t = g[x][y]
        for i in range(x-1, -1, -1):
            if g[i][y] >= t:
                break
        else:
            l.append(t)
            continue
        for i in range(y-1, -1, -1):
            if g[x][i] >= t: break
        else:
            l.append(t)
            continue
        for i in range(x+1, len(g)):
            if g[i][y] >= t: break
        else:
            l.append(t)
            continue
        for i in range(y+1, len(g[x])):
            if g[x][i] >= t: break
        else:
            l.append(t)
            continue
print(len(l)+2*len(g) + 2*(len(g[0])-2))

m = 0
for x in range(1, len(g)-1):
    for y in range(1, len(g[x])-1):
        t = g[x][y]
        d1=d2=d3=d4=0
        for i in range(x-1, -1, -1):
            if g[i][y] >= t:
                d1 += 1
                break
            d1 += 1
        for i in range(y-1, -1, -1):
            if g[x][i] >= t:
                d2 += 1
                break
            d2 += 1
        for i in range(x+1, len(g)):
            if g[i][y] >= t:
                d3 += 1
                break
            d3 += 1
        for i in range(y+1, len(g[x])):
            if g[x][i] >= t:
                d4 += 1
                break
            d4 += 1
        d = d1*d2*d3*d4
        if d > m:
            m = d
print(m)
