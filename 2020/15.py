from sys import stdin

g = list(map(int, stdin.read().split(',')))

d = {}
for i, j in enumerate(g):
    d[j] = (i+1, -1)
a = j
print(d, j)
for i in range(len(g)+1, 30000001):
    if d[a][1] == -1:
        d[0] = (i, d[0][0])
        a = 0
    else:
        b = d[a][0] - d[a][1]
        if b in d:
            d[b] = (i, d[b][0])
        else:
            d[b] = (i, -1)
        a = b

print(i, a)
