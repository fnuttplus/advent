from sys import stdin

d = [l.split() for l in stdin.read().splitlines()][2:]
g = [[0 for _ in range(30)]for _ in range(35)]
i = 0
m = 1000
for x in range(30):
    for y in range(35):
        a = int(d[i][1][:-1])
        b = int(d[i][2][:-1])
        i += 1
        g[y][x] = (a,b)
        if a < m: m = a

for row in g:
    for node in row:
        c = '.' if node[1] <= m else '#'
        if node [1] is 0: c = '_'
        print(c, end=' ')
    print()

c = 0
for i in range(len(d)):
    for j in range(len(d)):
        a = int(d[i][2][:-1])
        b = int(d[j][3][:-1])
        if a > 0 and i != j and a <= b:
            c += 1
print(c)